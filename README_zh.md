# HPDA Exam Toolkit 使用说明

这份文档是中文说明版，主要回答两个问题：

1. 如果你只是想直接使用当前仓库里已经整理好的 HPDA 题库，应该怎么做？
2. 如果你想把这个工具改成别的课程来用，应该准备什么文件、按什么流程运行？

## 一、当前仓库的定位

当前这个仓库已经附带了 **HPDA 这门课已经处理好的题库结果**，包括：

- 已提取的 PDF 页面文字
- 已提取的页面图片
- 已生成的主题库
- 已关联的原题来源页
- 已抽取的原题题干

所以：

- **如果你只是想直接刷 HPDA 的题**
  不需要重新运行 `rebuild_question_bank.py`
- **如果你想换成别的课程**
  才需要准备自己的 PDF 和题目总结，并重新构建题库

## 二、直接使用当前 HPDA 题库

这是最常见的情况，也是最推荐的日常用法。

### 1. 进入目录，并激活一个已经装好依赖的 Python 环境

```bash
cd ~/edinburgh/hpda/finalexam
conda activate hpda_exam
```

这里的重点不是“必须用 conda”，而是：

- 先进入项目目录
- 再激活一个已经安装好本项目依赖的 Python 环境

如果你用的是 conda，可以像上面这样。
如果你用的是别的环境管理方式，也可以，只要当前环境里已经安装好了项目依赖。

### 2. 启动浏览器刷题模式

```bash
python serve_web_app.py
```

脚本会：

- 启动本地服务
- 自动尝试打开默认浏览器
- 如果 `8000` 端口被占用，会自动切换到附近可用端口

如果浏览器没有自动打开，就手动访问终端里打印出来的网址。

默认通常是：

```text
http://127.0.0.1:8000
```

### 3. 如果你更喜欢终端刷题

```bash
python quiz_cli.py --open-image
```

这个模式会：

- 在终端里显示题目
- 自动打开对应题目的图片
- 保存状态和笔记到 `questions_master.csv`

## 三、什么时候需要重建题库

只有在下面这些情况，才需要运行：

```bash
python rebuild_question_bank.py
```

适用情况：

- 你换成了别的课程
- 你替换了 `paper/` 里的 PDF
- 你修改了 `questionSum.txt`
- 你想从头重新生成题库

## 四、如果你想改成别的课程来用

这时就不能直接使用当前 HPDA 的现成结果了。

你需要准备自己的输入文件。

### 1. 准备 PDF

把你自己的试卷 PDF 放到：

```text
paper/
```

例如：

```text
paper/
├── ExamPaper-2022.pdf
├── ExamPaper-2023.pdf
└── ExamPaper-2024.pdf
```

### 2. 准备 `questionSum.txt`

你需要准备一个题目总结文件，作用类似现在 HPDA 用的 `questionSum.txt`。

它的核心作用是：

- 按知识点/专题分组
- 给每道题写一个简短摘要
- 标明年份和题号

目前建议仍然参考当前仓库里这份文件的格式来写：

- `questionSum.txt`

简单理解就是：

- 一行专题标题
- 多行题目摘要
- 每题带 `年份 + 题号 + 简短说明`

## 五、换课后的完整流程

如果你已经把别的课程的 PDF 和 `questionSum.txt` 准备好了，就运行：

```bash
cd ~/edinburgh/hpda/finalexam
conda activate hpda_exam
python rebuild_question_bank.py
python serve_web_app.py
```

其中：

```bash
python rebuild_question_bank.py
```

会自动依次运行：

```bash
python extract_papers.py
python parse_question_summary.py
python auto_link_source_images.py
python populate_original_question_text.py
```

运行完成后，你再启动：

```bash
python serve_web_app.py
```

就可以在浏览器里刷你新课程的题库了。

## 六、各个脚本的作用

### `extract_papers.py`

从 `paper/` 里的 PDF 提取：

- 每页文字
- 每页图片

输出到：

- `extracted/text/`
- `extracted/images/`

### `parse_question_summary.py`

把 `questionSum.txt` 解析成结构化题库：

- `data/processed/questions_master.csv`
- `data/processed/topic_notes.csv`

### `auto_link_source_images.py`

把题目和原始 PDF 页面对上，生成：

- `source_pdf`
- `source_page`
- `source_text_file`
- `source_image`

### `populate_original_question_text.py`

从已经关联好的页面文字里，抽取接近原题的题干，填入：

- `original_question_text`

### `rebuild_question_bank.py`

这是总入口，一次性串起来运行上面四步。

### `quiz_cli.py`

终端刷题模式。

### `build_web_app.py`

生成静态网页：

- `output/web_app/index.html`

这个模式适合浏览，但网页里的状态默认只保存在浏览器本地。

### `serve_web_app.py`

启动本地网页服务。

这个模式最推荐，因为：

- 可以在浏览器里直接看图片
- 可以改状态
- 可以写笔记
- 会把修改写回 `questions_master.csv`

## 七、当前 HPDA 仓库最推荐的使用方式

对当前这个仓库来说，最推荐的命令就是：

```bash
cd ~/edinburgh/hpda/finalexam
conda activate hpda_exam
python serve_web_app.py
```

因为 HPDA 题库已经生成好了，所以不需要再重复重建。

