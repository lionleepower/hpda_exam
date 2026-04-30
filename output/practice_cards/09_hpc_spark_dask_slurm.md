# 9. HPC Data Analytics：Spark、Dask、SLURM、Parallel Data Processing

## Topic Notes

- 复习优先级：高。虽然 2024 没怎么考 HPC framework，但课程名里有 HPDA，不能忽略。

## Q2(b) (2022)
- Knowledge Point: 大规模 DICOM metadata 并行处理
- Summary: 处理 1 million+ DICOM images，并说明每一步如何使用 parallelism
- Priority: high
- Original Question:
  (b)
  The remainder of this question does not relate to the metadata tables in
  part a).
  A researcher wishes to extract and analyse metadata from a dataset of over
  1 million raw DICOM images collected from hospitals across Scotland. They
  are initially interested in analysing the frequency of two types of MRI scan,
  which they believe can be found in the Scan Description metadata ﬁelds of
  each ﬁle. Describe the steps you would take to tackle this problem, stating
  how parallelism can be utilised in each step.
  [8 marks]
- Source Image: extracted/images/DAwHPC-ExamPaper-2022_page_05.png
- Source PDF: paper/DAwHPC-ExamPaper-2022.pdf (page 5)

## Q3(b)(i) (2023)
- Knowledge Point: Spark vs Dask on SLURM
- Summary: 比较 Spark 和 Dask 在 SLURM 上的 setup 和 task execution
- Priority: high
- Original Question:
  i. How do Spark and Dask setups diﬀer in terms of the way the SLURM
  job scheduler is used and how are computation tasks executed?
- Source Image: extracted/images/DAwHPC-ExamPaper-2023_page_05.png
- Source PDF: paper/DAwHPC-ExamPaper-2023.pdf (page 5)

## Q3(b)(ii) (2023)
- Knowledge Point: spark.read.csv / dask.dataframe.read_csv
- Summary: 说明读取 CSV paths 后产生什么对象
- Priority: high
- Original Question:
  ii. To load the data, Spark and Dask can read in lists of paths to CSV ﬁles.
  Describe what spark.read.csv() and dask.dataframe.read csv()
  do and what they produce.
  [6 marks]
- Source Image: extracted/images/DAwHPC-ExamPaper-2023_page_05.png
- Source PDF: paper/DAwHPC-ExamPaper-2023.pdf (page 5)

## Q3(c)(i) (2023)
- Knowledge Point: Spark Pipeline Transformer / Estimator
- Summary: 判断 pipeline stages 是 Transformer 还是 Estimator
- Priority: high
- Original Question:
  (c) The Spark Pipeline diagram below represents a process to model the
  String-n-Keys data.
- Source Image: extracted/images/DAwHPC-ExamPaper-2023_page_05.png
- Source PDF: paper/DAwHPC-ExamPaper-2023.pdf (page 5)

## Q3(c)(i) (2023)
- Knowledge Point: narrow vs wide transformation
- Summary: 判断 Spark transformation 类型
- Priority: high
- Original Question:
  (c) The Spark Pipeline diagram below represents a process to model the
  String-n-Keys data.
- Source Image: extracted/images/DAwHPC-ExamPaper-2023_page_05.png
- Source PDF: paper/DAwHPC-ExamPaper-2023.pdf (page 5)

## Q3(c)(ii) (2023)
- Knowledge Point: PipelineModel
- Summary: 说明训练后的 PipelineModel 可做什么
- Priority: high
- Original Question:
  (c) The Spark Pipeline diagram below represents a process to model the
  String-n-Keys data.
- Source Image: extracted/images/DAwHPC-ExamPaper-2023_page_05.png
- Source PDF: paper/DAwHPC-ExamPaper-2023.pdf (page 5)

## Q3(d)(i)(ii) (2023)
- Knowledge Point: Dask delayed task graph
- Summary: 画 task graph 并计算 result.compute()
- Priority: high
- Original Question:
  i. What columns are required, how should the table be indexed and what
  data types should be used?
  ii. What method should be used to combine time-based data and how
  should it be aggregated?
  [5 marks]
  (b) To handle the large amount of data, you need to make full use of a HPC
  machine and use either Spark (using PySpark) or Dask.
  i. How do Spark and Dask setups diﬀer in terms of the way the SLURM
  job scheduler is used and how are computation tasks executed?
  ii. To load the data, Spark and Dask can read in lists of paths to CSV ﬁles.
  Describe what spark.read.csv() and dask.dataframe.read csv()
  do and what they produce.
  [6 marks]
  (c) The Spark Pipeline diagram below represents a process to model the
  String-n-Keys data.
- Source Image: extracted/images/DAwHPC-ExamPaper-2023_page_05.png
- Source PDF: paper/DAwHPC-ExamPaper-2023.pdf (page 5)

## Q3(d)(iii) (2023)
- Knowledge Point: Dask partitions / repartition
- Summary: 说明初始 partitions 和高效 repartition 方法
- Priority: high
- Original Question:
  3. You are tasked with analysing sales data for a musical instrument retailer, Strings-
  n-Keys. The retailer has 5 years of sales data, from 10 physical stores and an
  online store, comprising 600 ﬁles for monthly in-person sales, and 260 ﬁles for
  weekly online sales. Example data are shown below.
  In-person
  Sales,
  showing
  line
  1
  from
  4
  CSV
  ﬁles.
  date
  store
  department
  type
  maker
  model
  price
  01-01-18
  Edinburgh
  Guitars
  Guitar
  Fender
  Strat
  999.00
  01-01-18
  Glasgow
  Drums
  Drum kit
  Gretsch
  BC50
  1849.00
  01-02-18
  Dundee
  Guitars
  Guitar
  Gibson
  LP
  1399.00
  01-02-18
  Bristol
  Keys
  Keyboard
  Nord
  X300
  2199.00
  Online
  Sales,
  showing
  3
  lines
  from
  a
  single
  CSV
  ﬁle.
  datetime
  department
  type
  maker
  model
  price
  shipping
  20-01-2019
  Keys
  Keyboard
  Casio
  88Pro
  1299.00
  30.00
  12:36:21
  20-01-2019
  Drums
  Drum stool
  Gnu
  Red15
  149.00
  30.00
  12:42:19
  20-01-2019
  Recording
  Interface
  UA
  Volt1
  114.99
  10.00
  13:01:09
  The client would like to see monthly sales and yearly sales for each of 10 depart-
  ments across all stores and to predict future sales. To complete this work, you
  have at your disposal a small HPC machine featuring 8 compute nodes, each with
  12 CPU cores and 96 GB RAM, that uses the SLURM job scheduler.
  (a) You begin by designing a single table combining in-person and online sales,
  assuming all stores have the same departments.
  i. What columns are required, how should the table be indexed and what
  data types should be used?
  ii. What method should be used to combine time-based data and how
  should it be aggregated?
  [5 marks]
  (b) To handle the large amount of data, you need to make full use of a HPC
  machine and use either Spark (using PySpark) or Dask.
  i. How do Spark and Dask setups diﬀer in terms of the way the SLURM
  job scheduler is used and how are computation tasks executed?
  ii. To load the data, Spark and Dask can read in lists of paths to CSV ﬁles.
  Describe what spark.read.csv() and dask.dataframe.read csv()
  do and what they produce.
  [6 marks]
  (c) The Spark Pipeline diagram below represents a process to model the
  String-n-Keys data.
- Source Image: extracted/images/DAwHPC-ExamPaper-2023_page_05.png
- Source PDF: paper/DAwHPC-ExamPaper-2023.pdf (page 5)

