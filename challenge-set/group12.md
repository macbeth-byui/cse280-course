# CSE 280 Challenge Set 12

(c) BYU-Idaho

## Question 1

Bill has three one-piece jumpsuits, five pairs of work pants, and eight work shirts.  He wears either a jumpsuit or he wears pants and a shirt to work.  How many different possible outfits does he have?

<br />

## Question 2

120 pianists compete in a piano competition.  

* In the first round, 30 of the 120 are selected to go on to the next round,  How many different outcomes are there for the first round?

* In the second round, the judges select the first, second, third, fourth, and fifth place winners of the competition from among the 30 pianists who advanced to the second round.  How many outcomes are there for the second round of the competition?

Note: You don't have to evaluate the factorials in your response.

<br />

## Question 3

Count the number of ways you can reorder each of these words into a unique anagram:

* IDAHO
* TENNESSEE

<br />

## Question 4

Count the number of ways you can get the following when flipping a coin 7 times:

* All Heads
* Exactly 3 Heads
* Exactly 4 Heads
* At least 2 Heads
* Even number of Heads

<br /><br />

## Question 5

Assuming a standard 52 card deck, how many ways are there to get the following from 5 cards drawn without replacement (the first is done for you):

* 4 of a Kind = select a rank $13 \choose 1$ $\cdot$ select all 4 suits $4 \choose 4$ $\cdot$ select a different rank for the 5th card $12 \choose 1$ $\cdot$ select a suite from the new rank $4 \choose 1$ $= 624$
* Full House (3 of kind and 2 of a kind in different ranks)?
* 3 of a Kind (don't include Full House or 4 of a Kind)

After calculating the answers, check your work here: https://en.wikipedia.org/wiki/Poker_probability

<br /><br />



## Question 6

Note that the equation $(x+y)^2$ can be expanded as $x^2 + 2xy + y^2$.  In general, we can expand $(x+y)^n$ (where $n \in \mathbf{Z^+}$) using the binomial theorem:

$(x+y)^n = \displaystyle\sum_{k=0}^{n}{n \choose k} x^{n-k} y^k$

Using the binomial theorem, expand $(x+y)^6$.
