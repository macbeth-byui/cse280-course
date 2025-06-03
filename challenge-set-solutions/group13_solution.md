# CSE 280 Challenge Set 13 - Solutions

(c) BYU-Idaho

## Question 1

In a collection of 20 samples, there are 5 which are bad.  Determine the following probabilities (assume no replacement):

* Randomly select 1 sample and its good.
* Randomly select 4 samples and they are all good.
* Randomly select 4 samples and they are all bad.
* Randomly select 6 samples and only 1 is good.

Answers: 

* ${15 \choose 1} / {20 \choose 1} = \frac{15}{20} = 75\%$
* ${15 \choose 4} / {20 \choose 4} = \frac{16*15*14*13*12}{20*19*18*17*16} = \frac{1365}{4845} \approx 28\%$
* ${5 \choose 4} / {20 \choose 4} = \frac{5}{4845} \approx 0.1\%$
* $({5 \choose 5} \cdot {15 \choose 1}) / {20 \choose 6} = \frac{1}{\frac{20*19*18*17*16*15}{6*5*4*3*2}} = \frac{1}{38760} \approx 0.04\%$


## Question 2

### Part 1

A multiple choice test consists of five questions, each of which has four choices.  Each question has exactly one correct answer. Assume that a student guesses the answer on all five questions.  Complete the following table.  The scenario of "3 Right" has been done for you.  It is calculated by multiplying the number of ways to answer 2 questions incorrectly by the number of ways to select those 2 incorrect questions.  Note that there are $4^5 = 1024$ ways to select answers randomly on the test.

|Scenario|Probability|
|:-:|:-:|
|All Wrong|$3^5 \cdot {5 \choose 5} = \frac{243}{1024}$|
|1 Right|$3^4 \cdot {5 \choose 4} = \frac{405}{1024}$|
|2 Right|$3^3 \cdot {5 \choose 3} = \frac{270}{1024}$|
|3 Right|$3^2 \cdot {5 \choose 2} = \frac{90}{1024}$|
|4 Right|$3^1 \cdot {5 \choose 1} = \frac{15}{1024}$|
|All Right|$3^0 \cdot {5 \choose 0} = \frac{1}{1024}$|

### Part 2

Put the scenarios above in order from most likely to least likely.

Answer: 1 right, 2 right, all wrong, 3 right, 4 right, all right

### Part 3

Assume you get 4 points for each correct answer and 0 points for each incorrect answer.  We can calculate the expected grade by considering the different events, their probabilities, and the grade for each of those events.  The formula is as follows:

$\displaystyle\sum_{i=0}^n P(i) * S(i)$

where $n$ is the number of questions on the test, $P(i)$ is the probability of $i$ questions answered correctly and $S(i)$ is the score for getting $i$ questions answered correctly.

What is the expected (average) grade if students guess on every question? 

Answer: $\frac{243*0 + 405*4 + 270*8 + 90*12 + 15*16 + 1*20}{1024} = \frac{5120}{1024} = 5$ points out of 20 points ($25 \%$)


## Question 3

You have two 8-sided dice with each side labeled with the Fibonacci numbers 1, 1, 2, 3, 5, 8, 13, 21.

* Find $P(\text{Doubles} | \text{Both Odd})$
* Find $P(\text{Doubles} | \text{Both Even})$

Answers:
* $\frac{P(A \cap B)}{P(B)} = \frac{\frac{8}{64}}{\frac{36}{64}} = \frac{2}{9} \approx 22\% $
* $\frac{P(A \cap B)}{P(B)} = \frac{\frac{2}{64}}{\frac{4}{64}} = \frac{1}{2} = 50\% $

## Question 4

Email data suggests that 45% of all email is spam.  A common phrase that shows up in Spam is "Act Now".  It was found that 10% of all spam contained that phrase.  Conversely, 2% of all non-spam contained that phrase.  What is the probability that an email is Spam if it contains the phrase "Act Now"?

Answer: 
* $P(\text{Spam}) = 0.45$
* $P(\neg \text{Spam}) = 0.55$
* $P(\text{Act Now} \mid {Spam}) = 0.1$
* $P(\text{Act Now} \mid \neg {Spam}) = 0.02$
* $P(\text{Spam} \mid \text{Act Now}) = \frac{0.1 * 0.45}{0.1 * 0.45 + 0.02 * 0.55} \approx 80\%$


