# CSE 280 Challenge Set 02 - Solutions

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

Answer:

|$p$|$q$|$p \land q$|$\neg (p \land q)$|
|:-:|:-:|:-:|:-:|
|T|T|T|F|
|T|F|F|T|
|F|T|F|T|
|F|F|F|T|

**Part 2**

Use the result from Part 1 to simplify: $(p \uparrow p) \uparrow (q \uparrow q)$.

Answer:

$\neg(p \land p) \uparrow \neg(q \land q)$ - NAND Equivalence (above)

$\neg p \uparrow \neg q$ - Indempotent Law

$\neg (\neg p \land \neg q)$ - NAND Equivalence

$p \lor q$ - De Morgan

Note: You can create all logical operators using just NAND.

## Question 2

The domain of the following predicates is the set of all plants.

$P(x) =$ "$x$ is poisonous."

$Q(x) =$ "Jeff has eaten $x$."

Translate the following statements into prediate logic:

* Some plants are poisonous.
* Jeff has never eaten any poisonous plant.
* There are some non-poisonous plants that Jeff has not eaten.
* All plants are poisonous and Jeff hasn't eaten any of them

Answer:

* $(\exists x)P(x)$ 
* $(\forall x)(P(x) \to \neg Q(x))$  - Note: It does not say anything about non-poisonous therefore we use the conditional ($\to$)
* $(\exists x)(\neg P(x) \land \neg Q(x))$
* $(\forall x)(P(x) \land \neg Q(x))$ - Note: This says that there are no non-poisonous plants in existance therefore we use the $\land$

## Question 3

In the domain of all nonzero integers, let $I(x,y)$ be the predicate "$x / y$ is an integer."  Determine whether the following statements are true or false, and explain why.  Hint: Find values of $x$ and $y$ for which $I(x,y)$ is true.

* $(\forall y)(\exists x)I(x,y)$
* $(\exists x)(\forall y)I(x,y)$

Answer:

* True - For all integers $y$, there exists an integer $x$ for which $x/y$ is an integer.  This happes when $x=y$
* False - There exists at least one integer $x$ such that all integers $y$ cause $x/y$ to be an integer.  There is no integer that is divisible by all other integers. (Not all $y$ will divide any $x$)

## Question 4

The domain of the following predicates is all integers greater than 1:

* $P(a) =$ "$a$ is prime."
* $Q(a,b) =$ "$a$ divides $b$."

Consider the following statement:

For every $x$ that is not prime, there is some prime $y$ that divides it.  This is a true statement.

**Part 1**

Write the statement in predicate logic.  Hint: There is a conditional ($\to$) in this statement.

Answer: $(\forall x)(\neg P(x) \to (\exists y)(P(y) \land Q(y,x)))$

**Part 2**

Formally negate the statement (moving the $\neg$ as far to the right as possible).

Answer: 

$(\exists x) \neg (P(x) \lor (\exists y)(P(y) \land Q(y,x)))$

$(\exists x) (\neg P(x) \land \neg (\exists y)(P(y) \land Q(y,x)))$

$(\exists x) (\neg P(x) \land (\forall y) \neg (P(y) \land Q(y,x)))$

$(\exists x) (\neg P(x) \land (\forall y) (\neg P(y) \lor \neg Q(y,x)))$

**Part 3**

Write the english translation of your negated sentance.  Is the negated sentance a True statement?  If you are having difficulty writing this in english, consider modifying the result in Part 2 to change any $\lor$ to a $\to$.

Answer: 

We can rewrite this to use the implies:

$(\exists x) (\neg P(x) \land (\forall y) (P(y) \to \neg Q(x,y)))$

There is a nonprime x such that all primes y do not divide it.

Or restated, There is a nonprime that is not divisible by a prime.

This is not a true statement.

