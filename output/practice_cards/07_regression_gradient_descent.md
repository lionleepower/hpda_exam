# 7. Logistic Regression、Linear Regression、Gradient Descent、Generalisation Error

## Topic Notes

- 复习重点：logistic regression 要会写 sigmoid：
- hθ(x) = 1 / (1 + e^(-θᵀx))
- 并说明输出是 probability，不适合直接用普通 linear regression 做二分类。

## Q3(c)(i) (2022)
- Knowledge Point: learning rate
- Summary: 解释 gradient descent 中 learning rate α
- Priority: high
- Original Question:
  i. In this context, what is the learning rate α?
  [2 marks]
- Source Image: extracted/images/DAwHPC-ExamPaper-2022_page_07.png
- Source PDF: paper/DAwHPC-ExamPaper-2022.pdf (page 7)

## Q3(c)(ii) (2022)
- Knowledge Point: learning rate 曲线判断
- Summary: 根据 cost function 曲线判断 α 太大/太小/合适
- Priority: high
- Original Question:
  ii. Below you are given three plots of a cost function J(θ) against the num-
  ber iterations performed by the gradient descent algorithm. Each plot,
  concerns the same data, training model, same total number number of
- Source Image: extracted/images/DAwHPC-ExamPaper-2022_page_07.png
- Source PDF: paper/DAwHPC-ExamPaper-2022.pdf (page 7)

## Q3(d) (2022)
- Knowledge Point: generalisation error / testing error
- Summary: 判断关于 generalisation error 和 error rate 的选择题
- Priority: high
- Original Question:
  3.
  (a) In each of the below examples consider what could be an appropriate dis-
  tribution for modelling the random variable X. Brieﬂy justify your answer
  highlighting the key reasons.
  i. X: The total number of functioning devices out of boxes of 50 devices
  ii. X: The value, in thousand pounds, of two bedroom properties in Edin-
  burgh.
  iii. X: The daily number of complaints at the call centre of your energy
  provider.
  [3 marks]
  (b) A big popular theatre in Edinburgh has asked your help to understand how
  successful are the events they organise. More speciﬁcally, they want to know
  whether an event will be sold-out or not. For this, you’re given a csv ﬁle
  with three variables, namely, Y : showing the status of the event (i.e., if it
  was sold out or not), X1 : the type of the event (i.e., if it was a theatrical
  event or a music event) and X2 : whether it took place during the weekend
  or not. After processing the data you bring them together in the below
  format.
  theatrical
  music
  event
  event
  sold-out
  100
  90
  not sold out
  50
  20
  week-day
  weekend
  sold out
  80
  110
  not sold out
  40
  30
  i. They plan to organise a music event on the last Thursday of May. Use
  a Naive Bayes classiﬁer to answer whether it is going to be sold-out or
  not. Show all your working using adequate notation.
  [8 marks]
  ii. For the ﬁrst time, they consider organising a drawing lesson during
  June’s ﬁrst weekend and they want to know if it’s going to be sold out.
  A. Can you answer this using the provided data and/or the trained
  classiﬁer? If yes, show and explain how but without making the ac-
  tual calculation. If not, explain why and suggest how you could ap-
  proach it. In either case, mention anything that you would like/need
  to communicate with them based on your approach.
  [5 marks]
  (c) In the process of training various supervised models, we’ve talked about
  optimization methods such as gradient descent and stochastic gradient de-
  scent.
  i. In this context, what is the learning rate α?
  [2 marks]
  ii. Below you are given three plots of a cost function J(θ) against the num-
  ber iterations performed by the gradient descent algorithm. Each plot,
  concerns the same data, training model, same total number number of
- Source Image: extracted/images/DAwHPC-ExamPaper-2022_page_07.png
- Source PDF: paper/DAwHPC-ExamPaper-2022.pdf (page 7)

## Q2(d)(ii) (2023)
- Knowledge Point: logistic regression hypothesis
- Summary: 定义 logistic regression 模型并说明如何预测 positive response
- Priority: high
- Original Question:
  ii. They consider organising a poetry writing event during June’s ﬁrst
  weekend and they want to know if it’s going to be sold out. Can you
  answer this using the provided data and/or the trained classiﬁer? If
  yes, show and explain how but without making the actual calculation.
  If not, explain why and suggest how you could approach it.
- Source Image: extracted/images/DAwHPC-ExamPaper-2023_page_03.png
- Source PDF: paper/DAwHPC-ExamPaper-2023.pdf (page 3)

## Q2(d)(iii) (2023)
- Knowledge Point: logistic vs linear regression
- Summary: 判断 linear regression 是否适合二分类
- Priority: high
- Original Question:
  2. DIFFERENT SUB-QUESTIONS MAY HAVE DIFFERENT NUM-
  BERS. Take note of this in allocating time to questions.
- Source Image: extracted/images/DAwHPC-ExamPaper-2023_page_01.png
- Source PDF: paper/DAwHPC-ExamPaper-2023.pdf (page 1)

## Q3(e)(i) (2023)
- Knowledge Point: fitted linear model visualization
- Summary: 重组数据并画 observed data + fitted model
- Priority: high
- Original Question:
  i. What columns are required, how should the table be indexed and what
  data types should be used?
- Source Image: extracted/images/DAwHPC-ExamPaper-2023_page_05.png
- Source PDF: paper/DAwHPC-ExamPaper-2023.pdf (page 5)

## Q3(e)(ii) (2023)
- Knowledge Point: multiple linear regression prediction
- Summary: 预测 Edinburgh store 各 department 的 December 2023 sales
- Priority: high
- Original Question:
  ii. What method should be used to combine time-based data and how
  should it be aggregated?
  [5 marks]
  (b) To handle the large amount of data, you need to make full use of a HPC
  machine and use either Spark (using PySpark) or Dask.
- Source Image: extracted/images/DAwHPC-ExamPaper-2023_page_05.png
- Source PDF: paper/DAwHPC-ExamPaper-2023.pdf (page 5)

