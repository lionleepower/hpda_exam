# 2. 数据编码、特征缩放、数据探索

## Topic Notes

- 复习重点：feature scaling 很容易和 k-means、k-NN 结合考。

## Q1(b) (2022)
- Knowledge Point: feature scaling 对 k-means 的影响
- Summary: 比较原始 units、standard deviation scaling、money spent 对 k-means 的影响
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

## Q1(c)(ii) (2022)
- Knowledge Point: exploratory plots
- Summary: 为材料科学数据选择探索性图表，并解释每个变量的作用
- Priority: high
- Original Question:
  (c) A materials science research group requires your help to analyse some data
  from simulations of a new material. A small sample of their data is shown
  below and consist of the following three variables: “Type”, indicating the
  category of an observation; “Distance” which is measured in their material
  and “Shift”, a further property of the material.
  i. The chemists in the group are interested in ﬁnding a way to decide
  on the “Type” of a new observation using the above data. How can
  you do that?
  Mention what approach/method you’d choose, which
  variable/variables would be used and how.
  [2 marks]
- Source Image: extracted/images/DAwHPC-ExamPaper-2022_page_02.png
- Source PDF: paper/DAwHPC-ExamPaper-2022.pdf (page 2)

## Q1(c)(iii) (2022)
- Knowledge Point: removing data points / outlier handling
- Summary: 讨论删除数据点对模型性能的影响
- Priority: high
- Original Question:
  iii. The chemists looked into the performance of the model on the training
  data and found that it wasn’t performing so well. However, they re-
  alised, that the performance improved after removing some data points.
  Discuss this approach. Explain how this could aﬀect the performance
  of the new model.
  [3 marks]
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
- Source Image: extracted/images/DAwHPC-ExamPaper-2022_page_03.png
- Source PDF: paper/DAwHPC-ExamPaper-2022.pdf (page 3)

## Q1(b) (2023)
- Knowledge Point: categorical variable encoding
- Summary: 将 admission type 转换为 numerical model 可用形式，典型是 one-hot encoding
- Priority: high
- Original Question:
  (b) Name the technique which could be applied to convert a categorical variable
  for use by numerical models, and show how it would be applied to the
  following data sample.
  [2 marks]
  Row
  admission type
  1
  Emergency
  2
  Emergency
  3
  Transfer
- Source Image: extracted/images/DAwHPC-ExamPaper-2023_page_02.png
- Source PDF: paper/DAwHPC-ExamPaper-2023.pdf (page 2)

## Q2(b) (2024)
- Knowledge Point: normalization vs standardization
- Summary: 解释两种 scaling，并判断有 outliers 时更适合哪种
- Priority: high
- Original Question:
  (b) In k-NN, Feature Scaling is important to ensure the model is not
  dominated by features with larger values. Explain how Normalization and
  Standardization each affect feature values. Justify which one is more
  suited for a feature known to have outliers.
  [4 marks]
- Source Image: extracted/images/HPDA_Exam_Questions_2023_24_page_04.png
- Source PDF: paper/HPDA_Exam_Questions_2023_24.pdf (page 4)

