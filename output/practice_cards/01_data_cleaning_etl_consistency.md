# 1. 数据清洗、数据整理、ETL/ELT、数据一致性

## Topic Notes

- 复习优先级：很高。三年都出现，几乎是必考核心。

## Q1(a) (2022)
- Knowledge Point: ETL vs ELT
- Summary: 三个场景判断 ETL 或 ELT，并给出理由
- Priority: high
- Original Question:
  (a) In the three scenarios given below consider whether ETL or ELT would be
  most appropriate and justify your answer:
  i. A team within your company wants to detect anomalous insurance
  claims.
  ii. An organisation wishes to keep a long-term data archive for analysis.
  iii. A secure data source houses highly sensitive data, including individuals’
  personal information
  [3 marks]
- Source Image: extracted/images/DAwHPC-ExamPaper-2022_page_02.png
- Source PDF: paper/DAwHPC-ExamPaper-2022.pdf (page 2)

## Q2(a)(i) (2022)
- Knowledge Point: raw data / DICOM metadata cleaning
- Summary: 找出 DICOM 表格中 technically incorrect 的 raw data 并说明清洗步骤
- Priority: high
- Original Question:
  i. DICOM can be viewed as a raw data format. Provide two examples
  of raw data from the tables above that are not technically correct. For
  each, identify a cleaning step which could be applied to that data.
  [4 marks]
- Source Image: extracted/images/DAwHPC-ExamPaper-2022_page_05.png
- Source PDF: paper/DAwHPC-ExamPaper-2022.pdf (page 5)

## Q2(a)(ii) (2022)
- Knowledge Point: 数据一致性类型
- Summary: 说明 DICOM metadata 中违反了哪些 consistency
- Priority: high
- Original Question:
  ii. What types of data consistency are violated, and how?
  [4 marks]
- Source Image: extracted/images/DAwHPC-ExamPaper-2022_page_05.png
- Source PDF: paper/DAwHPC-ExamPaper-2022.pdf (page 5)

## Q1(a) (2023)
- Knowledge Point: 数据清洗的必要性、operational data
- Summary: 解释为什么医院 operational data 在分析前必须清洗，并说明可用资源
- Priority: high
- Original Question:
  (a) The dataset is an example of Operational data which has not been gathered
  for a speciﬁc analysis. Explain why it is vital to clean this data before it is
  made available for analysis, and state two resources you could use to assist
  with the cleaning.
  [3 marks]
- Source Image: extracted/images/DAwHPC-ExamPaper-2023_page_02.png
- Source PDF: paper/DAwHPC-ExamPaper-2023.pdf (page 2)

## Q1(c) (2023)
- Knowledge Point: 数据清洗 workflow 设计
- Summary: 针对医院 CSV 数据制定完整 cleaning plan
- Priority: high
- Original Question:
  (c) Create a plan for cleaning the dataset above, providing speciﬁc examples of
  tasks at each step in the Data Cleaning workﬂow. You should assume that
  HPC is not required for this task.
  [12 marks]
- Source Image: extracted/images/DAwHPC-ExamPaper-2023_page_02.png
- Source PDF: paper/DAwHPC-ExamPaper-2023.pdf (page 2)

## Q1(d) (2023)
- Knowledge Point: 验证清洗后数据中的统计假设
- Summary: 用 cleaned data 验证不同 admission type 的 length of stay 差异
- Priority: high
- Original Question:
  (d) Brieﬂy describe how you could verify the following statement using the
  cleaned data: “For each hospital, the average length of stay per year should
  be much higher for transfers than any other admission type”.
  [2 marks]
- Source Image: extracted/images/DAwHPC-ExamPaper-2023_page_02.png
- Source PDF: paper/DAwHPC-ExamPaper-2023.pdf (page 2)

## Q1(a)(i) (2024)
- Knowledge Point: streaming dataset 数据一致性清洗
- Summary: 针对音乐播放数据说明如何使数据 consistent
- Priority: high
- Original Question:
  i. Describe the steps that could be taken to make the streaming dataset
  consistent.
  [3 marks]
- Source Image: extracted/images/HPDA_Exam_Questions_2023_24_page_02.png
- Source PDF: paper/HPDA_Exam_Questions_2023_24.pdf (page 2)

## Q1(a)(ii) (2024)
- Knowledge Point: tidy data 三原则
- Summary: 直接问 tidy data 的三条原则
- Priority: high
- Original Question:
  ii. State the three main principles of tidy data.
  [3 marks]
- Source Image: extracted/images/HPDA_Exam_Questions_2023_24_page_02.png
- Source PDF: paper/HPDA_Exam_Questions_2023_24.pdf (page 2)

## Q1(a)(iii) (2024)
- Knowledge Point: common untidiness issue
- Summary: 识别数据表中的 untidy 问题并提出修复方法
- Priority: high
- Original Question:
  iii. Which common data untidiness issue can be seen in the streaming
  dataset?
  Suggest an approach to fix the issue in this dataset.
  [3 marks]
- Source Image: extracted/images/HPDA_Exam_Questions_2023_24_page_02.png
- Source PDF: paper/HPDA_Exam_Questions_2023_24.pdf (page 2)

