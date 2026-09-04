---
name: wechat-moyu-blue
description: 微信公众号文章排版引擎，固定使用“摸鱼蓝”主题，将 Markdown、Word、PDF 或纯文本转换为可直接粘贴到公众号编辑器的内联 HTML。自动处理章节编号、引言、代码块、图片/GIF、列表、表格与高亮。用户提到“公众号排版”“公众号文章”“微信排版”“gzh”“自动排版”或希望把文章转换成公众号 HTML 时使用。
---

# 摸鱼蓝公众号排版

将文章转换为可直接复制到微信公众号编辑器、粘贴后样式不丢失的 HTML。固定使用“摸鱼蓝”主题，不询问或推荐其他主题。

核心文件：

- `references/theme-moyu-blue.md`：主题变量、组件、骨架、配方和 Markdown 映射。
- `references/common-components.md`：代码块、图片/GIF、小标签标题。
- `references/format-normalize.md`：非 Markdown 输入的归一化规则。

所有 HTML 必须从组件库取用，不凭记忆另写样式。

## 工作流

### 1. 归一化输入

- Markdown 或 `.md`：直接解析。
- `.docx`：按 `references/format-normalize.md` 调用 `scripts/extract_docx.py`。
- PDF：读取文本、清除页眉页脚和分页噪声，再整理为 Markdown。
- 纯文本或网页富文本：按标题启发式恢复 Markdown 结构。
- 没有文章内容：向用户索要。

用户说“直接排”“自动排”“一键排版”“不用问”时，直接推断结构并继续，不要求确认。

### 2. 读取组件

完整读取 `references/theme-moyu-blue.md` 和 `references/common-components.md`。固定采用摸鱼蓝配色和骨架，不生成封面卡片、横向目录、作者信息、署名、互动 CTA 或品牌尾图。

### 3. 解析文章结构

| 元素 | 识别规则 |
|---|---|
| 文章标题 | `# 标题` 或 frontmatter `title`；仅用于公众号平台标题，不放进正文 |
| 开头引言 | 文章最前面的 `> 引用` |
| 章节标题 | `## 标题` |
| 子章节 | `### 标题` |
| 行内强调 | `**文字**`、`==文字==`、`<u>文字</u>`、`++文字++`、`~~文字~~` |
| 图片 / GIF | `![说明](URL)`、`![](xxx.gif)` |
| 代码 | 围栏代码块和行内代码 |
| 结构化内容 | 列表、表格、分割线、引用段落 |

按内容判定主导类型：教程、盘点、观点、访谈、数据复盘、随笔或案例实战，再依主题库配方选组件。不得遗漏原文段落、图片或代码。

### 4. 装配 HTML

按 `references/theme-moyu-blue.md` 的“完整文章模板骨架”装配：

- `##` 章节标题按顺序生成 `01 · CHAPTER ONE`、`02 · CHAPTER TWO`……；总结类末章使用 `∞ · POSTSCRIPT`。
- `###` 使用主题小节标题。
- `**加粗**` 使用主色加粗；`==高亮==` 使用亮蓝渐变高亮。
- 不主动给关键词加下划线；只有原文明示 `<u>` 或 `++` 时才用辅助色下划线。
- 代码、图片、GIF 和补素材占位从通用组件库取用，并换成摸鱼蓝配色。
- 正文结尾停在原文最后一段；不补写作者介绍、关注引导、点赞在看转发、感谢阅读或品牌信息。

### 5. 校验

生成后必须运行：

```bash
<SKILL_ROOT>/scripts/validate_gzh_html.py <生成的.html>
```

修复全部 ERROR 和正文半角标点 WARNING 后再交付。组件库变更后同时运行：

```bash
python3 <SKILL_ROOT>/scripts/component_lint.py <SKILL_ROOT>
```

### 6. 输出

正文文件必须是从全局 `<section>` 开始的纯 HTML 片段，不含 `<!DOCTYPE>`、`html/head/body`、`style` 或 `script` 标签。

文件名：`{原文件名}_排版_摸鱼蓝(moyu-blue).html`。

再生成带复制按钮的预览页：

```bash
<SKILL_ROOT>/scripts/wrap_preview.py <正文文件>
```

交付时提供正文文件、预览文件和校验结论。

## 必须遵守

- 样式全部内联；禁用 `div`、`class/id`、`position:fixed/absolute/sticky`、`float`、`display:grid`、CSS 变量、外部 CSS/字体。
- 所有文字节点用 `<span leaf="">…</span>` 包裹。
- 中文正文使用全角标点；代码、URL、英文专名和代码标识符保持原样。
- 图片用 `max-width:100%;height:auto;display:block;margin:0 auto`，不强制 `width:100%` 拉伸小图。
- 代码块每行一个 `p`，不用 `white-space:pre`；缩进使用全角空格。
- 待补图片、GIF、视频或成果图使用通用组件 2c；只有素材占位允许四周虚线框。
- 锚点强调全文不超过 5 处，同一段高亮不超过 2 种。
- 不生成任何作者、署名、互动或品牌收尾模块。
