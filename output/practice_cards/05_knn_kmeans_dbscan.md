# 5. k-NN、k-means、DBSCAN、Gaussian Mixtures 聚类与分类

## Topic Notes

- 复习重点：
- k-NN 是 supervised classification；k-means 是 unsupervised clustering。
- DBSCAN 要会数 epsilon-neighbourhood 里面有多少点。

## Q1(b) (2022)
- Knowledge Point: k-means 与 feature scaling
- Summary: 分析不同 scale/units 对聚类结果的影响
- Priority: high
- Original Question:
  (b) Consider an online merchant only providing two products: lamps and mo-
  torbikes. The plots below illustrate the purchases of eight diﬀerent shoppers
  where each shopper is depicted by a speciﬁc colour and symbol. Plot (a)
  illustrates the number of lamps and motorbikes purchased by each shopper.
  Plot (b) illustrates the same information but after scaling each variable by
  its standard deviation. Lastly, plot (c) shows the amount of money spent
  by each shopper on lamps and motorbikes.
  0
  2
  4
  6
  8
  10
  12
  a
  Units Purchased
  Lamps
  Motorbikes
  0.0
  0.2
  0.4
  0.6
  0.8
  1.0
  1.2
  1.4
  b
  Units Purchased (scaled)
  Lamps
  Motorbikes
  0
  500
  1000
  1500
  2000
  2500
  c
  Money Spent
  Lamps
  Motorbikes
  Consider you’re implementing k−means clustering, with k = 2, in each of
  the three cases above. Brieﬂy, explain in general, how the scale/units of
  measurement of the features could aﬀect k-means clustering. Speciﬁcally
  for the above example, describe in words the results you expect to get in
  each case and explain why.
  [8 marks]
- Source Image: extracted/images/DAwHPC-ExamPaper-2022_page_02.png
- Source PDF: paper/DAwHPC-ExamPaper-2022.pdf (page 2)

## Q1(c)(i) (2022)
- Knowledge Point: k-NN 分类任务设计
- Summary: 用 Distance 和 Shift 判断 Type
- Priority: high
- Original Question:
  i. The chemists in the group are interested in ﬁnding a way to decide
  on the “Type” of a new observation using the above data. How can
  you do that?
  Mention what approach/method you’d choose, which
  variable/variables would be used and how.
  [2 marks]
- Source Image: extracted/images/DAwHPC-ExamPaper-2022_page_02.png
- Source PDF: paper/DAwHPC-ExamPaper-2022.pdf (page 2)

## Q1(d)(i) (2022)
- Knowledge Point: k-NN 中 K 的影响
- Summary: 讨论 K=1、K=30、K=110 对 decision boundary 的影响
- Priority: high
- Original Question:
  i. Considering how K-NN works, and with reference to the above plots
  if helpful, discuss how K aﬀects the classiﬁcation and the classiﬁcation
- Source Image: extracted/images/DAwHPC-ExamPaper-2022_page_03.png
- Source PDF: paper/DAwHPC-ExamPaper-2022.pdf (page 3)

## Q1(d)(ii) (2022)
- Knowledge Point: k-NN accuracy 解释
- Summary: 根据 K=110 图解释 67% accuracy
- Priority: high
- Original Question:
  (d) A K-NN classiﬁer has been trained to a dataset with two features, X1, X2,
  and one target variable with three classes. The plots below show scatterplots
  of the features for the training data. The true class of each data point, A, B
  and C, is denoted by triangle, circle and square markers respectively. The
  dashed and straight lines show the classiﬁcation boundaries of the classiﬁer
  when trained with K = 1, K = 30 and K = 110. These boundaries indicate
  how new data points will be classiﬁed as indicated by the lower-case labels
  a, b and c. For example, data points falling within the red area a will be
  classiﬁed as a. Consider that there are 50 examples of each label in the
  training data.
  4
  5
  6
  7
  8
  X2
  1
  2
  3
  4
  5
  6
  X1
  a
  b
  c
  KNN (K=1)
  4
  5
  6
  7
  8
  X2
  a
  b
  c
  KNN (K=30)
  4
  5
  6
  7
  8
  X2
  a
  c
  KNN (K=110)
  A
  B
  C
  a/b Boundary
  b/c Boundary
  Predict a
  Predict b
  Predict c
  i. Considering how K-NN works, and with reference to the above plots
  if helpful, discuss how K aﬀects the classiﬁcation and the classiﬁcation
- Source Image: extracted/images/DAwHPC-ExamPaper-2022_page_03.png
- Source PDF: paper/DAwHPC-ExamPaper-2022.pdf (page 3)

## Q2(a) (2023)
- Knowledge Point: clustering 方法识别
- Summary: 从图判断 k-means、Gaussian Mixtures、DBSCAN
- Priority: high
- Original Question:
  (a) The plots given below show the results of diﬀerent clustering methods used
  on 3 diﬀerent datasets. Looking at these, which of k-means, Gaussian Mix-
  tures and DBSCAN is most likely to have produced each clustering output?
  Justify your answer based on the properties and underlying assumptions of
  each method.
  [3 marks]
- Source Image: extracted/images/DAwHPC-ExamPaper-2023_page_03.png
- Source PDF: paper/DAwHPC-ExamPaper-2023.pdf (page 3)

## Q2(b) (2023)
- Knowledge Point: DBSCAN core/reachable/outlier 判断
- Summary: 根据 epsilon 和 minPts 判断点类型
- Priority: high
- Original Question:
  (b) Let x be a datapoint with x1, ..., x9 denoting its closest neighbours, with
  their Euclidean distances from x listed below. Explain how DBSCAN would
  classify x, i.e., core point, density reachable or outlier, if parametrised with
  ϵ = 0.12 and minPts = 3, and brieﬂy justify why.
  D(x, x1)
  =
  0.4, D(x, x2) = 0.08, D(x, x3) = 0.15, D(x, x4) = 0.2,
  D(x, x5)
  =
  0.3, D(x, x6) = 0.22, D(x, x7) = 0.06, D(x, x8) = 0.11, D(x, x9) = 0.1
  [2 marks]
- Source Image: extracted/images/DAwHPC-ExamPaper-2023_page_03.png
- Source PDF: paper/DAwHPC-ExamPaper-2023.pdf (page 3)

## Q2(a) (2024)
- Knowledge Point: k-NN vs k-means 区别
- Summary: 解释两个算法并说明关键差别
- Priority: high
- Original Question:
  (a) Briefly explain both k-nearest neighbors (k-NN) and k-means, and state
  the key difference between them.
  [3 marks]
- Source Image: extracted/images/HPDA_Exam_Questions_2023_24_page_04.png
- Source PDF: paper/HPDA_Exam_Questions_2023_24.pdf (page 4)

