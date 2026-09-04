# 公众号排版组件库 —— 摸鱼蓝

> **使用说明**：本组件库为「摸鱼蓝」主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：清爽蓝色杂志风，卡片丰富、信息密度高。深蓝主色 + 亮蓝点睛 + 浅蓝辅助、留白衬线章节标题、标签化正文。适合教程、测评、清单、工具盘点类文章。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>`/`<script>`、CSS class/id、`position:fixed/absolute`、`float`、`@media`/`@keyframes`、`display:grid`
> - ✅ 支持内联 `style`、`display:flex`（有限）、`linear-gradient`、`border-radius`、`box-shadow`、`<section>/<p>/<span>/<strong>/<img>` 等基础标签
>
> **WeChat 兼容铁律**（本主题组件全部已按此写好，改动时必须遵守）：
> - 所有"装饰性空元素"（圆点、渐变分割线、装饰短横、时间线竖线）**必须在内部放 `<span leaf=""><br></span>` 占位**，否则微信会剥掉样式
> - **不要把 `font-size`/`border-bottom` 打在 `<strong>` 上**，也不要在同一个 `<p>` 里混多个不同 `font-size`——微信编辑器会自动"纠正"导致样式被重写。正确做法：拆成多个 `<p>`，每个 `<p>` 只有一个字号；高亮样式统一挂在外层 `<span>` 上
> - 不用 `position:absolute` 做划线/高亮，删除线用 `text-decoration:line-through`
> - 结构化区域没有内容时**整块删掉**，不留空 section

---

## 设计变量速查表

```
主色调：       #0076EA（深蓝）
辅色：         #A5C5FC（浅蓝）
辅助色装饰：   #A5C5FC
辅助色边框：   #A5C5FC
浅蓝背景：     #F3F7FF / #F7FAFF
亮蓝高亮：     #287CFB
高亮浅底：     rgba(40,124,251,0.22)
提示文字：     #0076EA
红色下划线：   #FECACA（对比/否定专用）
警告橙色：     rgb(255,76,0)
警告灰色：     rgb(136,136,136)
标题色：       #111827
正文色：       #374151
次要文字：     #4B5563
注释/标签：    #6B7280
辅助文字：     #9CA3AF
分隔线：       #D1D5DB
浅边框：       #E5E7EB
浅灰背景：     #F3F4F6
极浅灰：       #F9FAFB
正文字号：     14px（不可改）
正文行高：     1.9
全局行高：     1.75
字间距：       0.5px
最大宽度：     677px
内容区边距：   0 20px（模块左右各 20px）
```

字体栈：`-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif`

---

## 组件 1 全局容器

```html
<section style="max-width:677px;margin:0 auto;background:#ffffff;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#374151;line-height:1.75;letter-spacing:0.5px;overflow-x:hidden;">

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 4 章节标题 chapter-title（留白衬线样式）

采用留白衬线标题结构，并使用当前主题的深蓝主色。标题与上一段内容统一保留 `36px` 上间距；编号使用 `01 · CHAPTER ONE`、`02 · CHAPTER TWO`……；最后一章使用 `∞ · POSTSCRIPT`。

```html
<section style="margin-top:36px;margin-bottom:32px;padding:0 20px;">
  <p style="font-size:10px;color:#0076EA;font-weight:600;letter-spacing:4px;margin:0 0 10px;text-transform:uppercase;">
    <span leaf="">{{01 · CHAPTER ONE}}</span>
  </p>
  <h3 style="font-family:'Noto Serif SC',Georgia,'Times New Roman',serif;font-size:22px;font-weight:700;color:#111827;margin:0 0 16px;letter-spacing:0.5px;line-height:1.4;">
    <span leaf="">{{中文章节大标题}}</span>
  </h3>
  <section style="width:40px;height:2px;background:#287CFB;margin-bottom:24px;">
    <span leaf=""><br></span>
  </section>

  <!-- 本章节正文内容放在这里 -->

</section>
```

**结语章节变体**：

```html
<p style="font-size:10px;color:#0076EA;font-weight:600;letter-spacing:4px;margin:0 0 10px;text-transform:uppercase;">
  <span leaf="">∞ · POSTSCRIPT</span>
</p>
```

---

## 组件 5 正文段落 paragraph

```html
<p style="margin-bottom:16px;font-size:14px;line-height:1.9;text-align:justify;">
  <span leaf="">{{正文内容}}</span>
</p>
```

段间距较大时用 `margin-bottom:24px`。

---

## 组件 6 行内样式（9 种 + 使用原则）

### 6a. 主色加粗（核心概念、关键结论、品牌名/产品名）

```html
<strong style="color:#0076EA;"><span leaf="">文字</span></strong>
```

### 6b. 主色背景标签

```html
<strong style="color:#0076EA;background:rgba(0,118,234,0.1);padding:0 4px;border-radius:2px;"><span leaf="">文字</span></strong>
```

### 6c. 亮蓝渐变高亮（一段话中最想让读者注意的短语，每段不超过 1-2 处）

```html
<span style="background:linear-gradient(120deg,rgba(40,124,251,0.22) 0%,rgba(255,255,255,0) 100%);padding:0 4px;border-radius:2px;font-weight:600;color:#111827;"><span leaf="">文字</span></span>
```

### 6d. 亮蓝底部高亮（下划线效果）

```html
<span style="color:#111827;font-weight:bold;border-bottom:3px solid #287CFB;"><span leaf="">文字</span></span>
```

### 6e. 辅助色下划线（仅用于原文明示 `<u>` / `++`）

```html
<span style="border-bottom:2px solid #A5C5FC;font-weight:600;"><span leaf="">文字</span></span>
```

### 6f. 红色下划线（对比、否定、需要注意的内容）

```html
<span style="border-bottom:2px solid #FECACA;"><span leaf="">文字</span></span>
```

### 6g. 代码标签（行内代码）

```html
<span style="background:#F3F4F6;color:#1F2937;padding:2px 6px;border-radius:4px;font-size:13px;font-weight:600;"><span leaf="">code</span></span>
```

### 6h. 获取方式标签（亮蓝背景）

```html
<span style="background:#287CFB;color:#FFFFFF;padding:2px 6px;border-radius:4px;font-size:13px;font-weight:700;"><span leaf="">「关键词」</span></span>
```

### 6i. 删除线灰色（旧的/被淘汰的概念）

```html
<span style="background:#F3F4F6;color:#6B7280;padding:2px 6px;border-radius:4px;font-size:13px;text-decoration:line-through;font-weight:600;"><span leaf="">旧词</span></span>
```

**使用原则**：
1. 主色加粗用于核心概念、关键结论、品牌名/产品名
2. 亮蓝高亮每段不超过 1-2 处
3. 辅助色下划线只处理原文明示的 `<u>` / `++`，不主动逐段添加
4. 红色下划线用于对比、否定
5. 删除线灰色用于被淘汰的概念
6. 一段文字中不要同时使用超过 2 种高亮效果

---

## 组件 7 内容标签组（STEP / CASE / SKILL / TOOL）

### 7a. step-label（STEP 步骤标签）

```html
<section style="margin-bottom:24px;">
  <section style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
    <span style="display:inline-block;background:#111827;color:#fff;font-size:10px;font-weight:700;padding:2px 8px;border-radius:12px;"><span leaf="">STEP 01</span></span>
    <h4 style="font-size:15px;font-weight:800;color:#111827;margin:0;">
      <span leaf="">{{步骤标题}}</span>
    </h4>
  </section>
  <p style="font-size:14px;margin:0 0 16px;color:#4B5563;line-height:1.9;text-align:justify;">
    {{步骤内容}}
  </p>
</section>
```

### 7b. case-label（CASE 案例标签）

```html
<section style="margin-bottom:28px;">
  <section style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
    <span style="display:inline-block;background:#E5E7EB;color:#6B7280;font-size:10px;font-weight:700;padding:2px 8px;border-radius:12px;"><span leaf="">CASE 01</span></span>
    <h4 style="font-size:15px;font-weight:800;color:#111827;margin:0;">
      <span leaf="">{{案例标题}}</span>
    </h4>
  </section>
  <!-- 案例内容 -->
</section>
```

### 7c. skill-label / tool-label（编号标签）

```html
<section style="margin-bottom:28px;">
  <section style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
    <span style="display:inline-block;background:#111827;color:#fff;font-size:10px;font-weight:700;padding:2px 8px;border-radius:12px;"><span leaf="">SKILL 1</span></span>
    <h4 style="font-size:15px;font-weight:800;color:#111827;margin:0;">
      <span leaf="">{{名称}}</span>
    </h4>
  </section>
</section>
```

`SKILL 1` 可替换为 `TOOL 摄像机`、`TOOL 打光` 等。

---

## 组件 8 代码/命令/Prompt

### 8a. prompt-block（PROMPT 展示块）

```html
<p style="font-size:13px;color:#374151;margin:0 0 16px;line-height:1.8;">
  <span style="display:inline-block;background:#0076EA;color:#fff;font-size:11px;font-weight:700;padding:1px 7px;border-radius:3px;margin-right:6px;vertical-align:middle;letter-spacing:0.5px;"><span leaf="">PROMPT</span></span>
  <span style="font-size:12px;color:#9CA3AF;font-weight:700;"><span leaf="">{{提示词内容}}</span></span>
</p>
```

### 8b. cmd-block（CMD 单行命令块）

```html
<p style="font-size:13px;color:#374151;margin:0 0 24px;line-height:1.8;">
  <span style="display:inline-block;background:#111827;color:#fff;font-size:11px;font-weight:700;padding:1px 7px;border-radius:3px;margin-right:6px;vertical-align:middle;letter-spacing:0.5px;"><span leaf="">CMD</span></span>
  <span style="background:#F3F4F6;color:#1F2937;padding:2px 6px;border-radius:4px;font-size:13px;font-weight:600;"><span leaf="">{{命令内容}}</span></span>
</p>
```

### 8c. 多行代码块 → 用通用增量库

多行代码块**不设主题专属组件**，直接用 `common-components.md` 的 1a 深色代码块（每行一个 `<p style="margin:0">`，禁 `white-space:pre`）；浅色场景用 1b 并把左竖条换成 `#0076EA`。

---

## 组件 9 引用与亮点

### 9a. quote-box（灰色虚线引用框）

所有引用、补充说明的默认组件，使用浅灰底与浅蓝左竖线：

```html
<section style="background:#F9FAFB;border-left:3px solid #A5C5FC;border-radius:0 8px 8px 0;padding:12px 16px;margin-bottom:24px;text-align:justify;">
  <p style="font-size:13px;color:#374151;margin:0;line-height:1.6;">
    {{引用内容，可嵌入主色加粗等内联样式}}
  </p>
</section>
```

### 9b. oneliner-card（一句话亮点卡片）

> 兼容性关键规则：**不要把 `font-size` 打在 `<strong>` 上**，不要在同一个 `<p>` 里混多个字号；高亮样式统一挂在外层 `<span>` 上。

单行版（只有主金句）：

```html
<section style="background:#FFF;border:1px dashed #A5C5FC;border-radius:8px;padding:14px 16px;margin-bottom:24px;text-align:center;">
  <p style="margin:0;line-height:1.6;">
    <span style="font-size:15px;color:#0076EA;font-weight:bold;border-bottom:3px solid #287CFB;padding-bottom:2px;"><span leaf="">{{亮点内容}}</span></span>
  </p>
</section>
```

带前缀引导语版（两段式）：

```html
<section style="background:#FFF;border:1px dashed #A5C5FC;border-radius:8px;padding:14px 16px;margin-bottom:24px;text-align:center;">
  <p style="font-size:12px;color:#9CA3AF;margin:0 0 6px;line-height:1.5;">
    <span leaf="">{{引导语}}</span>
  </p>
  <p style="margin:0;line-height:1.6;">
    <span style="font-size:15px;color:#0076EA;font-weight:bold;border-bottom:3px solid #287CFB;padding-bottom:2px;"><span leaf="">{{亮点内容}}</span></span>
  </p>
</section>
```

带下方补充说明版：

```html
<section style="background:#FFF;border:1px dashed #A5C5FC;border-radius:8px;padding:14px 16px;margin-bottom:24px;text-align:center;">
  <p style="margin:0 0 6px;line-height:1.6;">
    <span style="font-size:15px;color:#0076EA;font-weight:bold;border-bottom:3px solid #287CFB;padding-bottom:2px;"><span leaf="">{{高亮内容}}</span></span>
  </p>
  <p style="font-size:13px;color:#9CA3AF;margin:0;line-height:1.5;">
    <span leaf="">{{补充说明}}</span>
  </p>
</section>
```

### 9c. subtitle-highlight（小节亮蓝高亮标题）

```html
<p style="font-size:15px;font-weight:900;color:#111827;margin-bottom:16px;">
  <span style="background:linear-gradient(180deg,transparent 65%,rgba(40,124,251,0.28) 65%);padding:0 4px;"><span leaf="">{{小节标题}}</span></span>
</p>
```

可加 `margin-top:32px` 增加上间距。

### 9d. center-divider（居中金句分隔）

```html
<p style="font-size:14px;margin-bottom:20px;text-align:center;color:#0076EA;font-weight:700;letter-spacing:1px;border-top:1px solid #F3F4F6;border-bottom:1px solid #F3F4F6;padding:12px 0;">
  <span leaf="">{{居中金句}}</span>
</p>
```

---

## 组件 10 提示与信息

### 10a. warn-tip（踩坑提示）

```html
<section style="padding:6px 0 4px;margin-bottom:16px;">
  <p style="margin-bottom:6px;font-size:12px;font-weight:700;color:#9CA3AF;letter-spacing:1px;">
    <span style="color:rgb(255,76,0);"><span leaf="">！踩坑提示 🕳</span></span>
  </p>
  <p style="font-size:13px;color:#374151;margin:0;line-height:1.7;">
    <span style="color:rgb(136,136,136);font-weight:bold;"><span leaf="">{{提示内容}}</span></span>
  </p>
</section>
```

标题可改为 `！真正的战场 🕳`、`！目前最大的槽点 🕳` 等。

### 10b. blue-tip（主色提示）

```html
<section style="padding:6px 0 4px;margin-bottom:16px;">
  <p style="margin-bottom:6px;font-size:12px;font-weight:700;color:#9CA3AF;letter-spacing:1px;">
    <span style="color:#0076EA;"><span leaf="">✦ {{提示标题}}</span></span>
  </p>
  <p style="font-size:13px;color:#374151;margin:0;line-height:1.7;">
    {{提示内容}}
  </p>
</section>
```

### 10c. yellow-warning（蓝色提示框，保留组件标识兼容旧调用）

```html
<section style="background:#F3F7FF;border:1px solid #287CFB;border-radius:12px;padding:12px 16px;margin-bottom:20px;">
  <p style="font-size:13px;color:#0076EA;margin:0;font-weight:700;">
    <span leaf="">{{警告内容}}</span>
  </p>
</section>
```

### 10d. blue-info（辅助色信息框）

```html
<section style="background:#F7FAFF;padding:12px 16px;border-radius:8px;border:1px solid #A5C5FC;margin-bottom:20px;">
  <p style="font-size:13px;color:#374151;margin:0;line-height:1.7;text-align:justify;">
    {{信息内容}}
  </p>
</section>
```

---

## 组件 11 布局组件

### 11a. pill-list（主色胶囊列表）

基本版：

```html
<section style="margin-bottom:14px;">
  <p style="margin:0 0 6px;">
    <span style="display:inline-block;font-size:13px;font-weight:700;color:#0076EA;background:rgba(0,118,234,0.08);padding:3px 10px;border-radius:999px;"><span style="display:inline-block;width:6px;height:6px;background:#0076EA;border-radius:50%;margin-right:5px;vertical-align:middle;"><span leaf=""><br></span></span><span leaf="">{{列表项文字}}</span></span>
  </p>
</section>
```

带说明文字版：

```html
<section style="margin-bottom:14px;">
  <p style="margin:0 0 6px;">
    <span style="display:inline-block;font-size:13px;font-weight:700;color:#0076EA;background:rgba(0,118,234,0.08);padding:3px 10px;border-radius:999px;"><span style="display:inline-block;width:6px;height:6px;background:#0076EA;border-radius:50%;margin-right:5px;vertical-align:middle;"><span leaf=""><br></span></span><span leaf="">{{标题}}</span></span>
  </p>
  <p style="font-size:13px;color:#4B5563;margin:0;line-height:1.7;text-align:justify;">
    <span leaf="">{{描述内容}}</span>
  </p>
</section>
```

### 11b. flow-cards（三步横排流程卡片）

```html
<section style="background:#F9FAFB;padding:16px;border-radius:12px;border:1px solid #F3F4F6;margin-bottom:24px;">
  <section style="display:flex;align-items:stretch;justify-content:center;gap:6px;">
    <section style="flex:1;text-align:center;padding:10px 8px;background:linear-gradient(135deg,#0076EA,#A5C5FC);border-radius:8px;">
      <p style="font-size:13px;font-weight:800;color:#fff;margin:0 0 3px;">
        <span leaf="">{{步骤1标题}}</span>
      </p>
      <p style="font-size:10px;color:rgba(255,255,255,0.8);margin:0;line-height:1.5;">
        <span leaf="">{{步骤1描述}}</span>
      </p>
    </section>
    <section style="display:flex;align-items:center;color:#D1D5DB;font-size:14px;padding:0 4px;">
      <span leaf="">→</span>
    </section>
    <section style="flex:1;text-align:center;padding:10px 8px;background:#fff;border:1px solid #E5E7EB;border-radius:8px;">
      <p style="font-size:13px;font-weight:800;color:#111827;margin:0 0 3px;">
        <span leaf="">{{步骤2标题}}</span>
      </p>
      <p style="font-size:10px;color:#9CA3AF;margin:0;line-height:1.5;">
        <span leaf="">{{步骤2描述}}</span>
      </p>
    </section>
    <section style="display:flex;align-items:center;color:#D1D5DB;font-size:14px;padding:0 4px;">
      <span leaf="">→</span>
    </section>
    <section style="flex:1;text-align:center;padding:10px 8px;background:#fff;border:1px solid #A5C5FC;border-radius:8px;">
      <p style="font-size:13px;font-weight:800;color:#0076EA;margin:0 0 3px;">
        <span leaf="">{{步骤3标题}}</span>
      </p>
      <p style="font-size:10px;color:#9CA3AF;margin:0;line-height:1.5;">
        <span leaf="">{{步骤3描述}}</span>
      </p>
    </section>
  </section>
  <p style="font-size:12px;color:#9CA3AF;text-align:center;margin:12px 0 0;letter-spacing:0.5px;">
    <span leaf="">{{底部说明文字}}</span>
  </p>
</section>
```

箭头 `→` 可替换为 `×` 做对比型布局。

### 11c. three-col-cards（三列对比卡片）

```html
<section style="background:#F9FAFB;padding:16px;border-radius:12px;border:1px solid #F3F4F6;margin-bottom:28px;">
  <section style="display:flex;align-items:stretch;justify-content:center;gap:6px;">
    <section style="flex:1;text-align:center;padding:10px 8px;background:linear-gradient(135deg,#0076EA,#A5C5FC);border-radius:8px;">
      <p style="font-size:13px;font-weight:800;color:#fff;margin:0 0 3px;">
        <span leaf="">{{卡片1标题}}</span>
      </p>
      <p style="font-size:10px;color:rgba(255,255,255,0.8);margin:0;line-height:1.5;">
        <span leaf="">{{卡片1描述}}</span>
      </p>
    </section>
    <section style="flex:1;text-align:center;padding:10px 8px;background:#fff;border:1px solid #E5E7EB;border-radius:8px;">
      <p style="font-size:13px;font-weight:800;color:#111827;margin:0 0 3px;">
        <span leaf="">{{卡片2标题}}</span>
      </p>
      <p style="font-size:10px;color:#9CA3AF;margin:0;line-height:1.5;">
        <span leaf="">{{卡片2描述}}</span>
      </p>
    </section>
    <section style="flex:1;text-align:center;padding:10px 8px;background:#fff;border:1px solid #E5E7EB;border-radius:8px;">
      <p style="font-size:13px;font-weight:800;color:#111827;margin:0 0 3px;">
        <span leaf="">{{卡片3标题}}</span>
      </p>
      <p style="font-size:10px;color:#9CA3AF;margin:0;line-height:1.5;">
        <span leaf="">{{卡片3描述}}</span>
      </p>
    </section>
  </section>
</section>
```

### 11d. timeline（时间线列表）

```html
<section style="display:flex;margin-bottom:28px;">
  <section style="display:flex;flex-direction:column;align-items:center;margin-right:16px;flex-shrink:0;">
    <section style="width:14px;height:14px;border-radius:50%;border:3px solid #0076EA;background:#fff;margin-top:4px;box-shadow:0 0 0 2px #fff;">
      <span leaf=""><br></span>
    </section>
    <section style="width:2px;background:#E5E7EB;flex:1;margin-top:4px;min-height:48px;">
      <span leaf=""><br></span>
    </section>
  </section>
  <section style="flex:1;padding-bottom:12px;">
    <section style="display:flex;align-items:center;gap:8px;margin-bottom:10px;flex-wrap:wrap;">
      <span style="display:inline-block;background:#111827;color:#fff;font-size:10px;font-weight:700;padding:2px 8px;border-radius:12px;"><span leaf="">{{CASE 01}}</span></span>
      <h4 style="font-size:15px;font-weight:800;color:#111827;margin:0;">
        <span leaf="">{{标题}}</span>
      </h4>
    </section>
    <p style="font-size:11px;font-weight:600;color:#9CA3AF;letter-spacing:1px;margin:0 0 12px;">
      <span leaf="">{{英文副标题}}</span>
    </p>
    <p style="font-size:14px;margin:0 0 16px;color:#4B5563;line-height:1.7;text-align:justify;">
      {{内容}}
    </p>
  </section>
</section>
```

最后一个时间线节点去掉竖线部分。

### 11e. tool-card（工具说明卡片）

基本版：

```html
<section style="background:#fff;border-radius:12px;padding:16px 20px;box-shadow:0 4px 16px rgba(0,118,234,0.12);margin-bottom:24px;">
  <p style="font-size:13px;color:#374151;margin:0;line-height:1.8;">
    {{说明内容}}
  </p>
</section>
```

居中高亮版（同 oneliner-card 规则：拆多个 `<p>`，不要 `<strong>` 带 font-size/border-bottom）：

```html
<section style="background:#fff;border-radius:12px;padding:16px 20px;box-shadow:0 4px 16px rgba(0,118,234,0.12);margin-bottom:24px;text-align:center;">
  <p style="font-size:13px;color:#9CA3AF;margin:0 0 6px;line-height:1.5;">
    <span leaf="">{{小字}}</span>
  </p>
  <p style="margin:0;line-height:1.6;">
    <span style="font-size:15px;color:#0076EA;font-weight:bold;border-bottom:3px solid #287CFB;padding-bottom:2px;"><span leaf="">{{高亮大字}}</span></span>
  </p>
</section>
```

### 11f. table（表格）

本主题保留 `<table>` 组件（摸鱼蓝实测微信可用）；Markdown 表格优先用它，数据密度低时也可改用 11c 三列卡片。

```html
<section style="margin-bottom:24px;overflow-x:auto;">
  <table style="width:100%;border-collapse:collapse;font-size:13px;">
    <thead>
      <tr>
        <th style="background:#0076EA;color:#fff;font-weight:700;padding:8px 12px;text-align:left;"><span leaf="">{{列标题1}}</span></th>
        <th style="background:#0076EA;color:#fff;font-weight:700;padding:8px 12px;text-align:left;"><span leaf="">{{列标题2}}</span></th>
        <th style="background:#0076EA;color:#fff;font-weight:700;padding:8px 12px;text-align:left;"><span leaf="">{{列标题3}}</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:8px 12px;border-bottom:1px solid #E5E7EB;color:#374151;"><span leaf="">{{内容}}</span></td>
        <td style="padding:8px 12px;border-bottom:1px solid #E5E7EB;color:#374151;"><span leaf="">{{内容}}</span></td>
        <td style="padding:8px 12px;border-bottom:1px solid #E5E7EB;color:#374151;"><span leaf="">{{内容}}</span></td>
      </tr>
      <tr>
        <td style="padding:8px 12px;border-bottom:1px solid #E5E7EB;color:#374151;background:#F9FAFB;"><span leaf="">{{内容}}</span></td>
        <td style="padding:8px 12px;border-bottom:1px solid #E5E7EB;color:#374151;background:#F9FAFB;"><span leaf="">{{内容}}</span></td>
        <td style="padding:8px 12px;border-bottom:1px solid #E5E7EB;color:#374151;background:#F9FAFB;"><span leaf="">{{内容}}</span></td>
      </tr>
    </tbody>
  </table>
</section>
```

偶数行自动带浅灰背景 `#F9FAFB`，列数按实际需求增减。

### 11g. ordered-list（数字编号列表）

```html
<section style="margin-bottom:24px;">
  <section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;background:#0076EA;color:#fff;font-size:11px;font-weight:700;border-radius:50%;flex-shrink:0;margin-top:2px;"><span leaf="">1</span></span>
    <p style="font-size:14px;color:#374151;margin:0;line-height:1.9;flex:1;">
      <span leaf="">{{列表项内容}}</span>
    </p>
  </section>
  <section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;background:#0076EA;color:#fff;font-size:11px;font-weight:700;border-radius:50%;flex-shrink:0;margin-top:2px;"><span leaf="">2</span></span>
    <p style="font-size:14px;color:#374151;margin:0;line-height:1.9;flex:1;">
      <span leaf="">{{列表项内容}}</span>
    </p>
  </section>
  <section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;background:#0076EA;color:#fff;font-size:11px;font-weight:700;border-radius:50%;flex-shrink:0;margin-top:2px;"><span leaf="">3</span></span>
    <p style="font-size:14px;color:#374151;margin:0;line-height:1.9;flex:1;">
      <span leaf="">{{列表项内容}}</span>
    </p>
  </section>
</section>
```

---

## 组件 12 媒体组件

### 12a. image（图片容器）

```html
<section style="text-align:center;margin-bottom:24px;border-radius:12px;overflow:hidden;">
  <!-- 保留原始图片代码不修改 -->
</section>
```

### 12b. video-card（视频容器卡片）

```html
<section style="background:#fff;border-radius:16px;padding:12px;margin-bottom:32px;border:2px solid #0076EA;box-shadow:0 4px 12px rgba(0,118,234,0.1);">
  <section style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
    <span style="width:8px;height:8px;background:#0076EA;border-radius:50%;"><span leaf=""><br></span></span>
    <span style="font-size:11px;color:#0076EA;font-weight:700;letter-spacing:1px;"><span leaf="">VIDEO 01</span></span>
    <span style="flex:1;height:1px;background:linear-gradient(to right,rgba(0,118,234,0.2),transparent);"><span leaf=""><br></span></span>
    <span style="font-size:11px;color:#9CA3AF;"><span leaf="">{{视频描述}}</span></span>
  </section>
  <section style="border-radius:10px;overflow:hidden;">
    <!-- 保留原始视频代码不修改 -->
  </section>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;background:#ffffff;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#374151;line-height:1.75;letter-spacing:0.5px;overflow-x:hidden;">

  <!-- 1. 开头引言（组件9b oneliner-card，文章有开头金句时） -->

  <!-- 2. 前言正文（开场白，组件5 段落 × N，放 0 20px 边距的 section 内） -->

  <!-- 3. 第一章（组件4 chapter-title） -->
  <!--    章内：组件5 正文 + 组件6 行内样式 + 组件7 标签 + 组件8 代码 + 组件9 引用亮点 + 组件10 提示 + 组件11 布局 + 组件12 媒体 -->

  <!-- 4. 第二章…第N章（组件4） -->

  <!-- 5. 结语章（组件4 变体：∞ · POSTSCRIPT） -->

</section>
```

**骨架顺序铁律**：不生成封面卡片、横向目录、作者信息、互动 CTA 或品牌尾图；正文从开头引言或前言直接进入章节内容，并在原文最后一段结束。

---

## 视觉层级（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 主色加粗 6a / 亮蓝底部高亮 6d / oneliner-card 9b | 核心概念、产品名、关键结论 | 全文 ≤5 处 |
| **标记层** | 辅助色下划线 6e（仅原文明示）/ 亮蓝渐变高亮 6c | 原文明确强调 | 按原文 |
| **容器层** | quote-box 9a / 提示 10x / 胶囊 11a / 卡片 11x | 引用、旁注、提示、结构化信息 | 按需 |

**克制原则**：
- 亮蓝高亮每段不超过 1-2 处；一段内不超过 2 种高亮效果
- 红色下划线只用于对比/否定，不做普通强调
- 主色渐变仅出现在流程首卡等结构位

---

## 文章类型 → 组件组合配方

按 SKILL.md 第 3 步判定的文章类型选配方；核心组件构成本篇的排版主旋律，点缀组件按内容出现处使用，一篇文章点缀组件种类 ≤3，避免花哨。

| 文章类型 | 核心组件组合 | 点缀组件 |
|---|---|---|
| 教程/操作指南 | step-label 7a + cmd/prompt 8a/8b + 代码块（通用库1a） | warn-tip 10a、blue-tip 10b、flow-cards 11b |
| 盘点/工具清单 | skill/tool-label 7c + tool-card 11e + pill-list 11a | table 11f、oneliner-card 9b |
| 观点/深度分析 | paragraph 5 + quote-box 9a + oneliner-card 9b | center-divider 9d、subtitle-highlight 9c |
| 访谈/人物特稿 | paragraph 5 + quote-box 9a（引语）+ timeline 11d（经历脉络） | oneliner-card 9b、center-divider 9d |
| 数据复盘/报告 | three-col-cards 11c + table 11f + ordered-list 11g | blue-info 10d、亮蓝渐变高亮 6c |
| 生活/情感随笔 | paragraph 5 + oneliner-card 9b + center-divider 9d | quote-box 9a（少量） |
| 案例实战 | case-label 7b / timeline 11d + step-label 7a | prompt-block 8a、yellow-warning 10c |

所有类型共用章节标题 4；不生成封面卡片、横向目录、作者信息、互动 CTA 或品牌尾图。

---

## Markdown → 摸鱼蓝排版 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号文章标题在平台单独设置 |
| 文章开头 `> 引言` | 组件 9b oneliner-card | 开头金句 |
| `## 章节标题` | 组件 4 chapter-title | 01 · CHAPTER ONE / 02 · CHAPTER TWO…，末章 ∞ · POSTSCRIPT |
| `### 子标题` | 组件 9c subtitle-highlight | 亮蓝高亮小节标题 |
| 普通段落 | 组件 5 paragraph | 默认不加下划线；原文明示时用 6e |
| `**加粗文字**` | 组件 6a 主色加粗 | 核心概念/品牌名 |
| `==高亮文字==` | 组件 6c 亮蓝渐变高亮 | 每段 ≤2 处 |
| `<u>下划线</u>` / `++文字++` | 组件 6e 辅助色下划线 | 次要强调 |
| `~~删除线~~` | 组件 6i 删除线灰色 | 被淘汰的概念 |
| `> 引用段落`（非开头） | 组件 9a quote-box | 灰色虚线框（本主题特征） |
| 核心金句 | 组件 9b oneliner-card / 9d center-divider | 视觉焦点 |
| 操作步骤 | 组件 7a step-label（+ 8a/8b） | STEP 01/02… |
| 案例/场景 | 组件 7b case-label 或 11d timeline | CASE 01/02… |
| 技能/工具清单 | 组件 7c skill/tool-label + 11e tool-card | |
| Prompt 提示词 | 组件 8a prompt-block（短）/ 通用库 1a（长多行） | |
| 单行命令 | 组件 8b cmd-block | |
| ` ``` 多行代码块 ``` ` | 通用库 1a 深色（默认）/ 1b 浅色（左竖条换 #0076EA） | 每行一个 `<p style="margin:0">` |
| 行内 `` `code` `` | 组件 6g 代码标签 | |
| 并列要点 | 组件 11a pill-list | |
| 流程（3 步） | 组件 11b flow-cards | 箭头可换 × 做对比 |
| 三项对比 | 组件 11c three-col-cards | |
| 递进/时间脉络 | 组件 11d timeline | |
| Markdown 表格 | 组件 11f table | 偶数行浅灰底 |
| `1. 2. 3.` 编号列表 | 组件 11g ordered-list | |
| 注意/警告 | 组件 10a warn-tip / 10c yellow-warning | |
| 亮点提示 | 组件 10b blue-tip / 10d blue-info | |
| `![](图片)` | 组件 12a image | 原图代码保留 |
| 视频 | 组件 12b video-card | 原视频代码保留 |
| 文末 | 原文最后一段 | 不补写作者、署名、互动或品牌信息 |
