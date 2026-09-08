# wechat-moyu-blue

`wechat-moyu-blue` 是一套用于微信公众号文章排版的 Codex Skill。

它可以把 Markdown、Word、PDF 或纯文本整理为微信公众号兼容的内联 HTML，并固定使用简洁、清晰的「摸鱼蓝」主题。

## 主要能力

- 自动识别文章标题、章节、小标题、引用、列表、表格、图片与代码块
- 使用固定组件库生成统一的公众号排版
- 正文、引用正文、列表说明与开篇卡片主句统一使用 16px 字号
- 开篇与内容组件遵循同一套样例规范，不在预览中额外添加正文大标题
- 输出可直接复制到微信公众号编辑器的 HTML
- 生成带复制按钮的本地预览页面
- 检查公众号不兼容的标签、样式与失效组件引用
- 保留原文结构，不补写作者信息、互动引导或品牌尾图

## 主题配色

| 用途 | 颜色 |
| --- | --- |
| 主色 | `#0076EA` |
| 点睛色 | `#287CFB` |
| 辅助浅蓝 | `#A5C5FC` |
| 浅色背景 | `#F3F7FF` |

## 排版规则

- 开篇使用白底、浅蓝虚线边框的卡片，优先采用原文开头的引用，否则采用首段；不另写摘要，也不重复原文。
- 章节使用编号与衬线标题，小节、引用、胶囊列表和编号列表使用对应的固定组件。
- 正文与开篇卡片主句为 16px；章节标题、灰色引导语、标签、代码、表格和图片说明保留独立字号。
- 关键词默认只使用主色加粗或渐变高亮，不自动添加下划线；原文明示的下划线和删除线可以保留。
- 提示与补充说明统一使用左竖线引用框；代码、图片和 GIF 统一取自通用组件库。
- 文章标题在公众号平台单独填写，正文停在原文最后一段，不添加作者介绍或互动收尾。

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

打开生成的 `_预览.html` 文件，点击「复制到公众号」，再粘贴到公众号编辑器。`assets/preview-template.html` 是用于装配的空白外壳，不是成品预览。

如需查看内置样式示例，在本地打开 `docs/gallery/index.html`。示例只展示组件样式，不会把示例文案带入文章。

粘贴后仍应在公众号后台核对排版和图片。本地图片路径不会随富文本自动变成公众号素材，需要单独上传并替换。

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
    ├── test_component_lint.py
    ├── validate_gzh_html.py
    └── wrap_preview.py
```

## 校验工具

检查生成的公众号 HTML：

```bash
python3 scripts/validate_gzh_html.py path/to/article.html
```

检查主题、通用组件库及其引用：

```bash
python3 scripts/component_lint.py .
```

运行组件回归测试：

```bash
python3 -B scripts/test_component_lint.py
```

检查内置样式示例：

```bash
python3 scripts/validate_gzh_html.py docs/gallery/moyu-blue.html
```

## License

本项目使用 [GNU Affero General Public License v3.0](LICENSE)。
