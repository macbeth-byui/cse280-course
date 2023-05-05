# CSE 280 Group 02

(c) BYU-Idaho - It is an honor code violation to post this
file completed or uncompleted in a public file sharing site.

**Instructions**: Work on all questions as a group as instructed during class.  We will review each answer during class.

## Question 1

The NAND operator $\uparrow$ is defined by the following truth table.  Use truth tables to show that $p \uparrow q$ is logically equivalent to $\neg(p \land q)$.

|$p$|$q$|$p \uparrow q$
|:-:|:-:|:-:|
|T|T|F|
|T|F|T|
|F|T|T|
|F|F|T|

## Question 2

The domain of the following predicates is the set of all plants.

$P(x) =$ "$x$ is poisonous."

$Q(x) =$ "Jeff has eaten $x$."

Translate the following statements into prediate logic:

* Some plants are poisonous.
* Jeff has never eaten a poisonous plant.
* There are some nonpoisonous plants that Jeff has never eaten.

## Question 3

In the domain of all zonzero integers, let $I(x,y)$ be the predicate "$x / y$ is an integer."  Determine whether the following statements are true or false, and explain why.

* $(\forall y)(\exists x)I(x,y)$
* $(\exists y)(\forall y)I(x,y)$

## Question 4

The domain of the following predicates is all integers greater than 1:

* $P(x) =$ "$x$ is prime."
* $Q(x,y) =$ "$x$ divides $y$."

Consider the following statement:

For every $x$ that is not prime, there is some prime $y$ that divides it.

**Part 1**

Write the statement in predicate logic.  Hint: There is a conditional ($\to$) in this statement.

**Part 2**

Formally negate the statement (moving the \neg as far to the right as possible).

**Part 3**

Write the english translation of your negated sentance
