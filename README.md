#微信-myyu-blue

一套面向微信公众号的 Codex 排版 Skill。它把 Markdown、Word、PDF 或纯文本转换为可直接复制到微信公众号编辑器的内联 HTML，并固定使用清爽、克制的「摸鱼蓝」主题。


##特点

-固定使用摸鱼蓝配色，避免每次选择主题
-自动识别章节、小标题、引用、列表、表格、图片和代码块
-生成适配微信公众号编辑器的内联样式
-自动校验不兼容标签、样式与文字节点
-不附加作者介绍、署名、互动 CTA 或品牌尾图
-同时生成纯正文 HTML 与带复制按钮的浏览器预览页

##安装

将仓库克隆到 Codex Skills 目录：

```巴什
git克隆 https://github.com/walkyufeng-hue/wechat-moyu-blue.git ~/.codex/skills/wechat-moyu-blue
```

重新打开 Codex 任务后即可调用。

##使用

在 Codex 中直接说明文章来源和目标，例如：

```文本
调用 $wechat-moyu-blue，把这篇 Markdown 排版成微信公众号文章。
```

也可以使用自然语言：

```text
用摸鱼蓝公众号排版处理这篇文章。
```

默认输出：

- `{原文件名}_排版_摸鱼蓝(moyu-blue).html`：可复制到公众号编辑器的正文片段
- `{原文件名}_排版_摸鱼蓝(moyu-blue)_预览.html`：带复制按钮的本地预览页

## 支持的输入

- Markdown 与 `.md`
- Word `.docx`
- PDF
- 纯文本或网页富文本

## 项目结构

```text
wechat-moyu-blue/
├── SKILL.md
├── assets/
│   └── preview-template.html
├── docs/
│   ├── assets/
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

## 本地校验

校验生成的公众号 HTML：

```bash
python3 scripts/validate_gzh_html.py path/to/article.html
```

校验主题组件库：

```bash
python3 scripts/component_lint.py .
```

## License

[GNU Affero General Public License v3.0](LICENSE)
