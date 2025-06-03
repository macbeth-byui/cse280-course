# CSE 280 Challenge Set 02

(c) BYU-Idaho 

## Question 1

**Part 1**

The NAND operator $\uparrow$ is defined by the following truth table.  Use truth tables to show that $p \uparrow q$ is logically equivalent to $\neg(p \land q)$.

|$p$|$q$|$p \uparrow q$
|:-:|:-:|:-:|
|T|T|F|
|T|F|T|
|F|T|T|
|F|F|T|

**Part 2**

Use the result from Part 1 to simplify: $(p \uparrow p) \uparrow (q \uparrow q)$.

<br /><br /><br /><br /><br />

## Question 2

The domain of the following predicates is the set of all plants.

$P(x) =$ "$x$ is poisonous."

$Q(x) =$ "Jeff has eaten $x$."

Translate the following statements into predicate logic:

* Some plants are poisonous.
* Jeff has never eaten any poisonous plant.
* There are some non-poisonous plants that Jeff has not eaten.
* All plants are poisonous and Jeff hasn't eaten any of them

## Question 3

In the domain of all nonzero integers, let $I(x,y)$ be the predicate "$x / y$ is an integer."  Determine whether the following statements are true or false, and explain why.  Hint: Find values of $x$ and $y$ for which $I(x,y)$ is true.

* $(\forall y)(\exists x)I(x,y)$
* $(\exists x)(\forall y)I(x,y)$

<br />

## Question 4

The domain of the following predicates is all integers greater than 1:

* $P(a) =$ "$a$ is prime."
* $Q(a,b) =$ "$a$ divides $b$."

Consider the following statement:

For every $x$ that is not prime, there is some prime $y$ that divides it.  This is a true statement.

**Part 1**

Write the statement in predicate logic.  Hint: There is a conditional ($\to$) in this statement.

<br /><br />

**Part 2**

Formally negate the statement (moving the $\neg$ as far to the right as possible).

<br /><br /><br /><br /><br /><br />


**Part 3**

Write the english translation of your negated sentance.  Is the negated sentance a True statement?  If you are having difficulty writing this in english, consider modifying the result in Part 2 to change any $\lor$ to a $\to$.




