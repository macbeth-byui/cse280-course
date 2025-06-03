# CSE 280 Challenge Set 13

(c) BYU-Idaho

## Question 1

In a collection of 20 samples, there are 5 which are bad.  Determine the following probabilities (assume no replacement):

* Randomly select 1 sample and its good.
* Randomly select 4 samples and they are all good.
* Randomly select 4 samples and they are all bad.
* Randomly select 6 samples and only 1 is good.

<br /><br />

## Question 2

### Part 1

A multiple choice test consists of five questions, each of which has four choices.  Each question has exactly one correct answer. Assume that a student guesses the answer on all five questions.  Complete the following table.  The scenario of "3 Right" has been done for you.  It is calculated by multiplying the number of ways to answer 2 questions incorrectly by the number of ways to select those 2 incorrect questions.  Note that there are $4^5 = 1024$ ways to select answers randomly on the test.

|Scenario|Probability|
|:-:|:-:|
|All Wrong||
|1 Right||
|2 Right||
|3 Right|$3^2 \cdot {5 \choose 2} = \frac{90}{1024}$|
|4 Right||
|All Right||

### Part 2

Put the scenarios above in order from most likely to least likely.

<br />

### Part 3

Assume you get 4 points for each correct answer and 0 points for each incorrect answer.  We can calculate the expected grade by considering the different events, their probabilities, and the grade for each of those events.  The formula is as follows:

$\displaystyle\sum_{i=0}^n P(i) * S(i)$

where $n$ is the number of questions on the test, $P(i)$ is the probability of $i$ questions answered correctly and $S(i)$ is the score for getting $i$ questions answered correctly.

What is the expected (average) grade if students guess on every question? 

<br /><br />


## Question 3

You have two 8-sided dice with each side labeled with the Fibonacci numbers 1, 1, 2, 3, 5, 8, 13, 21.

* Find $P(\text{Doubles} | \text{Both Odd})$
* Find $P(\text{Doubles} | \text{Both Even})$

<br /><br />


## Question 4

Email data suggests that 45% of all email is spam.  A common phrase that shows up in Spam is "Act Now".  It was found that 10% of all spam contained that phrase.  Conversely, 2% of all non-spam contained that phrase.  What is the probability that an email is Spam if it contains the phrase "Act Now"?




