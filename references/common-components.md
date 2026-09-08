# 摸鱼蓝通用组件库 —— 代码块 · 图片/GIF

> 本文件维护代码块与图片/GIF 组件；标题、引用、提示和列表统一从主题库读取 `theme-moyu-blue.md`。
>
> **固定配色**：主色 `#0076EA`、浅底 `#F3F7FF`、浅标 `#A5C5FC`、点睛色 `#287CFB`。
>
> **平台限制**：同主题库——禁 `<style>/<script>/class/id/div/position/float/@media/grid`，只用内联 + `flex`，文字全部 `<span leaf="">` 包裹。

---

## 一、代码块组件（Markdown ``` 围栏 → 这里）

文章里的代码、命令、Prompt 提示词、配置等，**必须用代码块组件**，不要塞进普通段落或引用块。代码块内的英文、半角符号、缩进都要原样保留（代码不适用"中文全角标点"规则）。

### 1a. 深色代码块（默认）

```html
<section style="margin:0 0 20px;border-radius:8px;overflow:hidden;background:#1E293B;box-shadow:0 4px 16px -8px rgba(15,23,42,0.4);">
  <section style="display:flex;align-items:center;padding:9px 14px;background:#0F172A;">
    <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#FF5F56;margin-right:7px;font-size:0;line-height:0;overflow:hidden;"><span leaf=""><br></span></span>
    <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#FFBD2E;margin-right:7px;font-size:0;line-height:0;overflow:hidden;"><span leaf=""><br></span></span>
    <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#27C93F;font-size:0;line-height:0;overflow:hidden;"><span leaf=""><br></span></span>
    <span style="margin-left:12px;font-size:12px;color:#64748B;font-family:Consolas,Monaco,monospace;letter-spacing:1px;"><span leaf="">python</span></span>
  </section>
  <section style="padding:11px 14px;">
    <p style="margin:0;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:13px;line-height:1.6;color:#E2E8F0;"><span leaf="">def make_skill(name):</span></p>
    <p style="margin:0;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:13px;line-height:1.6;color:#E2E8F0;"><span leaf="">　　return f"已生成 {name}"</span></p>
    <p style="margin:0;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:13px;line-height:1.6;color:#E2E8F0;"><span leaf="">print(make_skill("wechat-moyu-blue"))</span></p>
  </section>
</section>
```

要点（**关键，避免大段空白**）：① 顶栏三色圆点 + 语言名（无语言可删该 span）；② **每行代码用一个 `<p style="margin:0;...">`，不要用 `white-space:pre`**——否则 HTML 源码里 span 前的缩进和行间换行会被原样渲染成大左缩进 + 空行；③ 需要缩进时在 span 文字里用全角空格 `　`（不要靠源码空格）；④ 行距只靠 `line-height:1.6` 控制，padding 用 `11px 14px`，保持紧凑；⑤ 长行会自动换行，不溢出。

### 1b. 浅色代码块

```html
<section style="margin:0 0 20px;border-radius:8px;overflow:hidden;background:#F6F8FA;border:1px solid #E5E7EB;border-left:3px solid #0076EA;">
  <section style="padding:7px 14px;border-bottom:1px solid #E5E7EB;">
    <span style="font-size:12px;color:#9CA3AF;font-family:Consolas,Monaco,monospace;letter-spacing:1px;"><span leaf="">bash</span></span>
  </section>
  <section style="padding:11px 14px;">
    <p style="margin:0;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:13px;line-height:1.6;color:#24292F;"><span leaf="">npx skills add walkyufeng-hue/wechat-moyu-blue</span></p>
  </section>
</section>
```

多行同 1a：每行一个 `<p style="margin:0">`，不用 `white-space:pre`，缩进用全角空格 `　`。

### 1c. 行内代码（正文中的 `code` 短片段）

```html
<span style="background:#F1F5F9;color:#0076EA;padding:1px 6px;border-radius:4px;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:14px;"><span leaf="">SKILL.md</span></span>
```

文字使用固定主色 `#0076EA`，底色保持中性浅灰。

---

## 二、图片 / GIF 组件（Markdown `![](...)` → 这里）

文章里**每一处图片、GIF、截图占位都要保留并转成下面的组件**，不得遗漏；`src` 原样保留用户给的 URL 或相对路径。GIF 动图与普通图片都用 `<img>`（公众号原生支持 GIF 自动播放），区别只在加不加"动图"角标说明。

### 2a. 标准图片（带说明）

```html
<section style="background:#FFF;border-radius:12px;padding:6px;border:1px solid #E5E7EB;box-shadow:0 4px 12px -2px rgba(0,0,0,0.08);margin-bottom:8px;">
  <section style="margin:0;border-radius:8px;overflow:hidden;">
    <span leaf=""><img src="图片URL" style="max-width:100%;height:auto;display:block;margin:0 auto;"></span>
  </section>
</section>
<p style="font-size:12px;color:#9CA3AF;text-align:center;margin:0 0 24px;">
  <span leaf="">— 图片说明文字</span>
</p>
```

无说明文字时删掉下方 `<p>`，并把图片容器 `margin-bottom` 改回 `10px`。

> **图片尺寸自适应**：`<img>` 用 `max-width:100%;height:auto;display:block;margin:0 auto`——按图片自身尺寸显示并居中，大图缩到容器宽、小图保持原尺寸，**不用 `width:100%` 强制铺满**（小图被拉伸会糊）。

### 2b. GIF 动图（同图片，加"GIF 动图"角标）

```html
<section style="background:#FFF;border-radius:12px;padding:6px;border:1px solid #E5E7EB;box-shadow:0 4px 12px -2px rgba(0,0,0,0.08);margin-bottom:8px;">
  <section style="margin:0;border-radius:8px;overflow:hidden;">
    <span leaf=""><img src="动图URL.gif" style="max-width:100%;height:auto;display:block;margin:0 auto;"></span>
  </section>
</section>
<p style="text-align:center;margin:0 0 24px;">
  <span style="display:inline-block;background:#A5C5FC;color:#0076EA;font-size:11px;font-weight:700;padding:1px 8px;border-radius:4px;margin-right:6px;"><span leaf="">GIF 动图</span></span>
  <span style="font-size:12px;color:#9CA3AF;"><span leaf="">动图说明文字</span></span>
</p>
```

若原文只写了图片但没给 URL，用 `src="图片URL"` 占位并在交付时提醒用户补图，**不要凭空编造图床链接**。

---

### 2c. 待补素材占位（**居中板块**，用于 GIF / 录屏 / 视频 / 成果图待补处）

文章里 `【插入xxx】`、待录屏、待补 GIF/视频/截图等占位，一律用这个**居中**板块，不要用左对齐的提示块。浅底柔虚线框 + 居中图标与说明，一眼看出"此处待补"。

```html
<section style="margin:0 0 24px;padding:30px 20px;border:1.5px dashed #DAD7D2;border-radius:14px;background:#FAFAF8;text-align:center;">
  <p style="margin:0 0 10px;font-size:26px;line-height:1;"><span leaf="">🎬</span></p>
  <p style="margin:0;font-size:14px;font-weight:700;color:#9CA3AF;letter-spacing:1px;"><span leaf="">待补素材</span></p>
  <p style="margin:8px 0 0;font-size:13px;color:#B8B5B0;line-height:1.7;"><span leaf="">此处插入：创建 skill 的录屏演示</span></p>
</section>
```

- 图标按素材类型换：🎬 视频/录屏、🖼 图片、📊 信息图、📎 附件。
- 素材占位使用这套虚线框；主题 9b 开篇/金句卡片另保留样例中的浅蓝细虚线。其他正文标题、引用和提示不使用四周虚线框。
- 占位保持居中、留白与中性色，不充当正文强调。

---

## 选用速记

| 文章里出现 | 用哪个组件 |
|---|---|
| ` ``` 代码 / 命令 / Prompt 围栏 ``` ` | 1a 深色（默认）或 1b 浅色代码块 |
| 行内 `` `code` `` | 1c 行内代码 |
| `![](图片)` | 2a 标准图片 |
| `![](xxx.gif)` 或注明动图 | 2b GIF 动图 |
| 小节标题 / 并列要点 | 主题 9c 小节标题 / 11a 胶囊列表 |
| `> 金句` | 主题 9b 开篇卡片 / 9a 正文引用 |
| 提示 / 注意 / 旁注 | 主题 9a 引用框 |
