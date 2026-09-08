#!/usr/bin/env python3
"""组件库源头检查器 —— 可验证循环的第一道关。

扫描 references/ 下所有组件库 .md 里的 ```html 代码块，检测会导致
排版问题的反模式。只看真实组件 HTML，不被说明文字干扰（grep 做不到）。

与 validate_gzh_html.py 配合构成闭环：
  改组件库 → component_lint.py 扫源头 → 生成产物 → validate_gzh_html.py 扫产物 → 修 → 重复

用法：
    component_lint.py [skill-dir]   # 默认当前目录
退出码：1 = 有 ERROR，0 = 通过。
"""

import glob
import os
import re
import sys
from html.parser import HTMLParser

# (正则, 级别, 说明) —— 在每个 ```html 组件块内检查
CHECKS = [
    (re.compile(r"white-space\s*:\s*pre", re.I), "ERROR",
     "用了 white-space:pre —— 会把 HTML 源码缩进/换行渲染成大左缩进+空行；"
     "代码块改成每行一个 <p style=\"margin:0\">，缩进用全角空格"),
    (re.compile(r"</?div[\s>]", re.I), "ERROR", "出现 <div>，应用 <section>"),
    (re.compile(r"\sclass\s*=", re.I), "ERROR", "出现 class 属性（会被公众号剥离）"),
    (re.compile(r"\sid\s*=", re.I), "ERROR", "出现 id 属性"),
    (re.compile(r"<style[\s>]", re.I), "ERROR", "出现 <style> 标签"),
    (re.compile(r"position\s*:\s*(fixed|absolute|sticky)", re.I), "ERROR",
     "position fixed/absolute/sticky 不被支持"),
    (re.compile(r"display\s*:\s*grid", re.I), "ERROR", "display:grid 不被支持"),
    (re.compile(r"var\s*\(\s*--", re.I), "ERROR", "用了 CSS 变量 var(--x)"),
    (re.compile(r"@(media|keyframes|import)", re.I), "ERROR", "@media/@keyframes/@import 不被支持"),
]

class StyleNodes(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.nodes = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        style = dict(attrs).get("style", "")
        styles = dict((k.strip().lower(), v.strip().lower())
                      for item in style.split(";") if ":" in item
                      for k, v in [item.split(":", 1)])
        self.nodes.append((tag, styles))


def lint_html(html, component_id="", source_kind="theme"):
    found = [(level, msg) for rx, level, msg in CHECKS if rx.search(html)]
    for tag, styles in StyleNodes(html).nodes:
        border = styles.get("border", "")
        if "dashed" in border:
            allowed = ((source_kind == "theme" and component_id == "9b")
                       or (source_kind == "common" and component_id == "2c"))
            if not allowed or styles.get("text-align") != "center":
                found.append(("ERROR", "四周虚线框仅允许用于 9b 金句卡片和通用库 2c 素材占位"))
        decoration = styles.get("text-decoration", "") + styles.get("text-decoration-line", "")
        if tag in {"span", "strong", "u"} and ("border-bottom" in styles or "underline" in decoration or tag == "u"):
            allowed = (source_kind == "theme" and component_id == "6e"
                       and tag == "span" and styles.get("border-bottom") == "2px solid #a5c5fc"
                       and "underline" not in decoration)
            if not allowed:
                found.append(("ERROR", "组件含文字下划线；仅 6e 保留原文明示的辅助色下划线"))
    return found


def lint_file(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        text = f.read()
    name = os.path.basename(path).replace("公众号排版组件库 —— ", "").replace(".md", "")
    found = []  # (level, msg)
    seen = set()

    def add(level, msg):
        if msg not in seen:
            seen.add(msg)
            found.append((level, msg))

    for m in re.finditer(r"```html\s*\n(.*?)```", text, re.S):
        html = m.group(1)
        headings = re.findall(r"^#{2,3} (.+)$", text[:m.start()], re.M)
        heading = headings[-1] if headings else ""
        match = re.match(r"(\d+[a-z])\.", heading)
        component_id = match.group(1) if match else ""
        source_kind = "common" if os.path.basename(path) == "common-components.md" else "theme"
        for level, msg in lint_html(html, component_id, source_kind):
            add(level, msg)
    return name, found


def reference_errors(root, refs):
    known = set()
    for path in refs:
        with open(path, encoding="utf-8") as f:
            known.update(re.findall(r"^### (\d+[a-z])\.", f.read(), re.M))
    errors = []
    for path in sorted(glob.glob(os.path.join(root, "references", "*.md"))) + [os.path.join(root, "SKILL.md")]:
        with open(path, encoding="utf-8") as f:
            # 只核对说明和映射表，不把代码样例当作组件引用。
            text = re.sub(r"```[\s\S]*?```", "", f.read())
        for component_id in sorted(set(re.findall(r"(?<![A-Za-z0-9])\d+[a-z](?![A-Za-z0-9])", text)) - known):
            errors.append(f"{os.path.basename(path)} 引用了不存在的组件 {component_id}")
    return errors


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    refs = sorted(glob.glob(os.path.join(root, "references", "theme-*.md")))
    common = os.path.join(root, "references", "common-components.md")
    if os.path.isfile(common):
        refs.append(common)
    if not refs:
        print(f"未找到 {root}/references/*.md")
        sys.exit(1)

    total_err = total_warn = clean = 0
    print(f"📐 组件库源头检查：{len(refs)} 个库\n")
    for path in refs:
        name, found = lint_file(path)
        if not found:
            clean += 1
            continue
        errs = [m for lv, m in found if lv == "ERROR"]
        warns = [m for lv, m in found if lv == "WARN"]
        total_err += len(errs)
        total_warn += len(warns)
        print(f"── {name} ──")
        for m in errs:
            print(f"   ❌ {m}")
        for m in warns:
            print(f"   ⚠️  {m}")

    dangling = reference_errors(root, refs)
    total_err += len(dangling)
    for msg in dangling:
        print(f"   ❌ {msg}")
    print(f"\n汇总：{clean}/{len(refs)} 个库干净，ERROR×{total_err}，WARN×{total_warn}")
    if total_err == 0 and total_warn == 0:
        print("✅ 全部组件库源头无反模式")
    sys.exit(1 if total_err else 0)


if __name__ == "__main__":
    main()
