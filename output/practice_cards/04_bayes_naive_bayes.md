# 4. Bayes、Naive Bayes、Bayes’ Law

## Topic Notes

- 复习优先级：非常高。三年都考，而且常考完整计算。
- 你需要熟练掌握：
- P(Y | X1, X2) ∝ P(Y) P(X1 | Y) P(X2 | Y)
- 以及 unseen category 时的 Laplace smoothing / 收集更多数据 / 说明模型无法可靠判断。

## Q3(b)(i) (2022)
- Knowledge Point: Naive Bayes 分类
- Summary: 判断 music event on weekday 是否 sold out
- Priority: high
- Original Question:
  i. They plan to organise a music event on the last Thursday of May. Use
  a Naive Bayes classiﬁer to answer whether it is going to be sold-out or
  not. Show all your working using adequate notation.
  [8 marks]
- Source Image: extracted/images/DAwHPC-ExamPaper-2022_page_07.png
- Source PDF: paper/DAwHPC-ExamPaper-2022.pdf (page 7)

## Q3(b)(ii) (2022)
- Knowledge Point: Naive Bayes unseen category / smoothing
- Summary: drawing lesson 是未见类别，讨论如何处理
- Priority: high
- Original Question:
  ii. For the ﬁrst time, they consider organising a drawing lesson during
  June’s ﬁrst weekend and they want to know if it’s going to be sold out.
  A. Can you answer this using the provided data and/or the trained
  classiﬁer? If yes, show and explain how but without making the ac-
  tual calculation. If not, explain why and suggest how you could ap-
  proach it. In either case, mention anything that you would like/need
  to communicate with them based on your approach.
  [5 marks]
- Source Image: extracted/images/DAwHPC-ExamPaper-2022_page_07.png
- Source PDF: paper/DAwHPC-ExamPaper-2022.pdf (page 7)

## Q2(c)(i) (2023)
- Knowledge Point: Naive Bayes 分类
- Summary: 判断 dancing event on weekday 是否 sold out
- Priority: high
- Original Question:
  i. They plan to organise a dancing event on the last Thursday of May.
  Use a Naive Bayes classiﬁer to answer whether it is going to be sold out
  or not. Show all your working using appropriate notation.
- Source Image: extracted/images/DAwHPC-ExamPaper-2023_page_03.png
- Source PDF: paper/DAwHPC-ExamPaper-2023.pdf (page 3)

## Q2(c)(ii) (2023)
- Knowledge Point: Naive Bayes 未见类别问题
- Summary: poetry writing event 是否可用已有 classifier 判断
- Priority: high
- Original Question:
  ii. They consider organising a poetry writing event during June’s ﬁrst
  weekend and they want to know if it’s going to be sold out. Can you
  answer this using the provided data and/or the trained classiﬁer? If
  yes, show and explain how but without making the actual calculation.
  If not, explain why and suggest how you could approach it.
- Source Image: extracted/images/DAwHPC-ExamPaper-2023_page_03.png
- Source PDF: paper/DAwHPC-ExamPaper-2023.pdf (page 3)

## Q2(c) (2024)
- Knowledge Point: Bayes’ Law 计算 posterior probability
- Summary: 用感染率、sensitivity、specificity 计算阳性后真实感染概率
- Priority: high
- Original Question:
  (c) A test for a new bacterial infection has been created and evaluated on a
  population of 1,000 people, of which 2.5% are known to have the virus
  and the rest do not. The test has been determined to be successful on
  91% of people who are infected, and correctly dismisses 89% of people
  who do not have the condition.
  Using Bayes’ Law, calculate the probability that a positive test result on
  someone from this population means they are infected.
  [4 marks]
- Source Image: extracted/images/HPDA_Exam_Questions_2023_24_page_04.png
- Source PDF: paper/HPDA_Exam_Questions_2023_24.pdf (page 4)

## Q2(d) (2024)
- Knowledge Point: Naive Bayes 分类
- Summary: 判断 cafe 是否应买 Competitive Strategy game
- Priority: high
- Original Question:
  (d) A board game caf´e wishes to determine which types of new game to buy
  based on how popular its existing games are. They have collected data
  from customers who have played their existing games:
  Puzzle
  Strategy
  Card
  Cooperative
  Competitive
  Y
  34
  76
  65
  47
  75
  N
  23
  12
  56
  157
  23
  In this table, row Y means the game is popular, and row N means it is not.
  There are two features; Genre (Puzzle, Strategy, or Card), and Player
  Type (Cooperative or Competitive).
  Apply Bayes’ model to this data to justify whether the caf´e should stock a
  new Competitive Strategy game.
  [7 marks]
- Source Image: extracted/images/HPDA_Exam_Questions_2023_24_page_04.png
- Source PDF: paper/HPDA_Exam_Questions_2023_24.pdf (page 4)

## Q2(e)(i)(ii) (2024)
- Knowledge Point: Naive Bayes 新类别/特征扩展问题
- Summary: 游戏类型变多、加入 price feature 后模型如何修改
- Priority: high
- Original Question:
  i. They stock a much larger selection of game types.
  [2 marks]
  ii. They wish to include price as a feature.
  [2 marks]
- Source Image: extracted/images/HPDA_Exam_Questions_2023_24_page_04.png
- Source PDF: paper/HPDA_Exam_Questions_2023_24.pdf (page 4)

