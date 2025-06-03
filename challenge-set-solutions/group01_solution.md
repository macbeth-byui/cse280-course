# CSE 280 Challenge Set 01 - Solutions

(c) BYU-Idaho

## Question 1

Let the following statements be given:

* $a = $ "You used the pool in the afternoon."
* $b = $ "You cleaned up after lunch."
* $c = $ "You must clean up after dinner."

**Part 1**

Use connectives (operators) to translate the following statement into a compound proposition:

"If you used the pool in the afternoon and you didn't clean up after lunch, then you must clean up after dinner."

Answer: $(a \land \neg b) \to c$

**Part 2**

Construct a truth table for the compound proposition you found in Part 1.  The eight rows of your table should correspond to the eight different possibilities for $a$, $b$, and $c$.

Answer:

|$a$|$b$|$c$|$a \land \neg b$|ANS|
|:-:|:-:|:-:|:-:|:-:|
|T|T|T|F|T|
|T|T|F|F|T|
|T|F|T|T|T|
|T|F|F|T|F|
|F|T|T|F|T|
|F|T|F|F|T|
|F|F|T|F|T|
|F|F|F|F|T|

**Part 3**

Suppose that the statement given in part 1 is false.  What must be true about your pool usage and cleanup duties?  Explain how to justify your answer using the truth table.

Answer: The pool was used and neither the lunch nor the dinner was cleaned up.

## Question 2

Use a truth table to prove that the statement $[(p \lor r) \land (\neg p)] \to r$ is always true or always false, no matter what $p$ and $r$ are.  What do we call this type of statement?

Answer:  A tautology

|$p$|$r$|$p \lor r$|$\neg p$|$(p \lor r) \land (\neg p)$|ANS|
|:-:|:-:|:-:|:-:|:-:|:-:|
|T|T|T|F|F|T|
|T|F|T|F|F|T|
|F|T|T|T|T|T|
|F|F|F|T|F|T|

## Question 3

Let $s$ be the following statement:  "If it's raining, then the ground is wet."

**Part 1**

Give the inverse of $s$.  Is this the same as $s$?

Answer: If its not raining, then the ground is not wet. -- No

**Part 2**

Give the converse of $s$.  Is this the same as $s$?

Answer: If the ground is wet, then it is raining. -- No

**Part 3**

Give the contrapositive of $s$.  Is this the same as $s$?

Answer:  If the ground is not wet, then its not raining. -- Yes

## Question 4

Determine if the following propositions written in English are True or False:

* If 2 is even, then 5 is prime. - True
* If 3 is even, then 6 is prime. - True
* If 5 is odd, then 8 is prime. - False
* If 8 is odd, then 11 is prime. - True
* 10 is even if and only if 4 is prime - False
* 11 is even if and only if 6 is prime - True

## Question 5

Simplify the following using a truth table:

$\neg(A \to B) \lor \neg(A \lor B)$

Answer: $\neg B$

## Question 6

The following "ugly-looking" multi-line compound proposition is a Tautology.  Can you explain why without using a truth table.  Hint: Refer back to Question 3 above.

$((A \to B) \leftrightarrow (\neg B \to \neg A)) \land ((B \to A) \leftrightarrow (\neg A \to \neg B)) \land$

$((B \to C) \leftrightarrow (\neg C \to \neg B)) \land ((C \to B) \leftrightarrow (\neg B \to \neg C)) \land$

$((A \to C) \leftrightarrow (\neg C \to \neg A)) \land ((C \to A) \leftrightarrow (\neg A \to \neg C))$

Answer: Either both the implication and contra-positive are True or either both the implication and the contra-positive are False.  This is beacuse the implication and contra-positive are always equal to each other.






