# wechat-moyu-blue

`wechat-moyu-blue` 是一套用于微信公众号文章排版的 Codex Skill。

它可以把 Markdown、Word、PDF 或纯文本整理为微信公众号兼容的内联 HTML，并固定使用简洁、清晰的「摸鱼蓝」主题。

## 主要能力

- 自动识别文章标题、章节、小标题、引用、列表、表格、图片与代码块
- 使用固定组件库生成统一的公众号排版
- 输出可直接复制到微信公众号编辑器的 HTML
- 生成带复制按钮的本地预览页面
- 自动检查公众号不兼容的标签和样式
- 保留原文结构，不补写作者信息、互动引导或品牌尾图

## 主题配色

| 用途 | 颜色 |
| --- | --- |
| 主色 | `#0076EA` |
| 点睛色 | `#287CFB` |
| 辅助浅蓝 | `#A5C5FC` |
| 浅色背景 | `#F3F7FF` |

## 安装

将仓库克隆到 Codex Skills 目录：

```bash
git clone https://github.com/walkyufeng-hue/wechat-moyu-blue.git ~/.codex/skills/wechat-moyu-blue
```

安装后重新打开 Codex 任务，让 Skill 出现在可用技能列表中。

## 调用方式

明确调用 Skill：

```text
调用 $wechat-moyu-blue，把这篇 Markdown 排版成微信公众号文章。
```

也可以直接描述需求：

```text
用摸鱼蓝公众号排版处理这篇文章。
```

## 支持的输入

- Markdown 文件
- Word `.docx`
- PDF
- 纯文本
- 网页富文本

## 输出文件

Skill 默认生成两个文件：

```text
{原文件名}_排版_摸鱼蓝(moyu-blue).html
{原文件名}_排版_摸鱼蓝(moyu-blue)_预览.html
```

第一个文件是微信公众号正文片段，第二个文件用于在浏览器中预览和复制。

## 目录结构

```text
wechat-moyu-blue/
├── SKILL.md
├── assets/
│   └── preview-template.html
├── docs/
│   └── gallery/
├── references/
│   ├── common-components.md
│   ├── format-normalize.md
│   └── theme-moyu-blue.md
└── scripts/
    ├── component_lint.py
    ├── extract_docx.py
    ├── validate_gzh_html.py
    └── wrap_preview.py
```

## 校验工具

检查生成的公众号 HTML：

```bash
python3 scripts/validate_gzh_html.py path/to/article.html
```

检查主题组件库：

```bash
python3 scripts/component_lint.py .
```

## License

本项目使用 [GNU Affero General Public License v3.0](LICENSE)。
