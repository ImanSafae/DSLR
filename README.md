# DSLR

DSLR is a post-common core project at school 42, part of the IA & Data branch. DSLR stands for **data science and logistic regression**. The choice of the language is free, I chose to do it in Python as it is known as the best choice for data and IA, and to expand my skills in that language.

### Logistic regression - basic explanations

The purpose of this project is to explore machine learning through the classification model of **logistic regression**.
Just like with linear regression, the goal is to predict the value of y (the unknown variable, also called **dependent variable**) based on the value of x, (the variable we know, also called **independent variable**). The way to do this is to have a first set of data with known values for x and y, which will serve to train our model. Once our model is trained, it will be able to predict the value of y for new data sets.

Unlike linear regression, y can only take 0 or 1 as a value. For a more practical example, this model can be used to predict whether a client will click on buy (1) or not click (0), based on how much time they spent on a website. This is possible thanks to the sigmoid function, which gives outputs between 0 and 1. Everything inbetween will be considered a probability that the value is 1.

![image](https://github.com/user-attachments/assets/35cd27ef-3609-449d-9374-fe7b10c4b0da)

### Introduction to DSLR

DSLR takes direct inspiration from the Harry Potter sorting hat: we get a data set containing information about Hogwarts students, including their grades in all the courses, and the house they belong to, which we will use to train our model. We also get a data set with only grades, used to predict the students' houses depending on those grades.
This project is in 3 parts : the first one aims to recreate the _describe_ function from the pandas library, entirely from scratch. The second part aims to plot the data with histograms, scatter plots and pair plots, to answer some specific questions (detailed below). The third part is where it gets serious and where we get into the logistic regression.

#### Part 1: Describe
The describe.py file takes a csv dataset as a parameter, given in the command line, and it uses the one found in datasets/dataset_train.csv as a reference.
It then displays everything the describe function from pandas would: mean, std, min, max, first quartile, median, third quartile, and length. I also added IQR as a bonus, which is the inter-quartile range.

#### Part 2 : Plots
In this part, we are asked to display histograms to answer this question : _Which Hogwarts course has a homogeneous score distribution between all four houses?_
The histogram.py file directly uses the data set provided in the datasets folder. It then displays, one by one, histograms for each course, displaying its distribution through students for all 4 houses. In the end, it appears the one with the most homogeneous distribution is _Care of magical creatures_.
We're then asked to display scatter plots to answer this question: _What are the two features that are similar ?_
The scatter_plot.py works the same way as histogram.py, displaying all course compared, two by two. The answer quickly appears as obvious: all scatter plots appear as quite abstract, except for one which shows a direct, linear correlation between _Astronomy_ and _Defense against dark arts_.
The last part asks us to display everything we saw earlier, through a pair plot matrix.

### Part 3 : Logistic regression
This is where it gets serious.
This is a multi-classification _one-vs-all_ model, which means that we don't aim to classify our data in 2 categories (0 or 1) but in more (one for each Hogwarts house, in this case). We will repeat the same process 4 times (once for each house), and get a value between 0 and 1 for each of these houses. We will then compare all 4 values and select the highest one, and the probability that the student belongs to that house is the highest.

To train our model, we use the dataset_train.csv set. The program logreg_train.py needs to be called first for this part.
At first, in the context of a specific house, each Hogwarts course will be given a random "weight". In the sigmoid function's formula, this weight represents a constant value which is a coefficient associated with a variable. (For example, say the weight for _Defense against dark arts_ is 2 and the weight for _Spells_ is 1 for Gryffindor ; this means that in order to be sorted in this specific house, the student's grade in _Defense against dark arts_ is twice as determinant as their grade in _Spells_.)

#### Gradient descent and error rate
Since the weights will be random at first, our model won't be accurate, so we will train it with the **gradient descent** method.
We'll set a high number of iterations (for example, 8000). For each iteration we'll calculate the error rate thanks to a known function which will compare our prediction (with the randomly set weights), and the real expected output (remember that we're still using the data set with the houses known for this part) for all students, and calculate the amount of times we were right and the amount of times we were wrong. If this error is below 0.1, the iterations stop and we consider our model accurate enough (we are free to set the threshold we deem acceptable, in this case and based on research, I chose to set it as 0.1). Otherwise, we calculate a gradient and adjust our weight based on the gradient and on a learning rate we set in the beginning (here, I chose to set it at 0.04. It should not be too small because it will take way too many iterations to get close to an accurate model, but it shouldn't be too high either because this means the weights will vary a lot from an iteration to another and we might miss the optimal point).
This should be repeated 4 times for each house. Once this is done, we have generated a set of weights with acceptable accuracy, one weight for each course, and one set of weights for each house.

#### Prediction
Our logreg_train.py will take the training dataset as a parameter on the command line, and generate a weights file (you can find it already generated in this repository). This file should then be used in the logreg_predict.py program, which you should call with the dataset_predict.py data set as a parameter. The program will clean the data set from all NaN values, then use the weights and the grades contained in the data set. It will calculate a probability between 0 and 1 that the student belongs in each 4 houses, and then compare them and accept the highest one as the correct result. It will then generate a file containing the indexes of each student and the name of the Hogwarts house they were sorted to.

### Conclusion
This project was a very interesting introduction to the world of machine learning through logistic regression, a slightly more complex model than linear regression. It encouraged me to look more into this field and complete the other projects of the same branch at school 42.
