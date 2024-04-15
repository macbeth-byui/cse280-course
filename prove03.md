# CSE 280 Prove 03

(c) BYU-Idaho - It is an honor code violation to post this
file completed or uncompleted in a public file sharing site. S4.

**Instructions**: Answer each question using proper markdown notation as needed.  Use the preview view in Visual Studio Code (or another editor if desired) to see the formatting, tables, and mathematical formula properly rendered.  If you need to write code, then first test your code in a separate file and then copy the code into this document using code fences. 

**Name**:

## Question 1 (5 points)

Let $E$ be the set of even numbers greater than 0, and let $P$ be the set of prime numbers.  Find all the values in the set formed by $E \cap P$.

**Answer**:  

## Question 2 (5 points)

Let the following sets be given.  The Universal set for this problem is the set of all students at some univeristy:

* $F$ = the set of all freshmen
* $M$ = the set of all math minors
* $C$ = the set of all CS majors

Translate $(F \cap M) \subseteq C$ into an english sentance.

**Answer**:

## Question 3 (5 points)

For each set described below, list 4 example values that would be in that set.  Remember that $\mathbf{Z}$ represents integers and $\mathbf{Z}^+$ represents positive integers greater than 0.  

|Set|Four Example Values in the Set|
|:-:|:-:|
|$\lbrace x \mid x \in \mathbf{Z}^+, x-1 \text{ is a multiple of 7} \rbrace$||
|$\lbrace x \mid x \text{ is a fruit and its skin is normally eaten} \rbrace$||
|$\lbrace \frac 1 x \mid x \in \mathbf{Z}, x \neq 0 \rbrace$||
|$\lbrace 2n \mid n \in \mathbf{Z}, n \lt 0 \rbrace$||
|$\lbrace s \mid s \in \mathbf{Z}^+, \sqrt{s} \in \mathbf{Z}^+$}|$$|

## Question 4 (8 points)

Let $A = \lbrace 0, 2, 3 \rbrace$, $B = \lbrace 2, 3 \rbrace$, and $C = \lbrace 1, 5, 9 \rbrace$, and the universal set $U = \lbrace 0, 1, 2, ...,  9 \rbrace$.  Determine the resulting sets for the following operations.  The first one is done for you,

|Operation|Resulting Set|
|:-:|:-:|
|$A \cap B$|$\lbrace 2, 3 \rbrace$|
|$A \cup B$||
|$B \cup A$||
|$A \cup C$||
|$A - B$||
|$B - A$||
|$\overline{A}$||
|$A \cap C$||
|$A \oplus B$||

## Question 5 (4 points)

Let $A=\lbrace 0, 2, 3 \rbrace$, $B=\lbrace 2, 3 \rbrace$, and $C=\lbrace 1, 4\rbrace$ and let the universal set $U=\lbrace 0, 1, 2, 3, 4 \rbrace$.  List the element pairs for each of the following cartesian products using these sets.  The first one is done for you.

|Cartesian Product|Answer|
|:-:|:-:|
|$A \times B$|$\lbrace (0,2), (0,3), (2,2), (2,3), (3,2), (3,3) \rbrace$|
|$B \times A$||
|$A \times B \times C$||
|$A \times \overline{A}$||
|$B^2$||

## Question 6 (5 points)

Which pairs (there may one pair or more than one pair) of the following sets are disjoint:

* $A =$ The set of all even numbers.
* $B =$ The set of all odd numbers.
* $C = \lbrace 2^x \mid x \in \mathbf{Z}, x \ge 0 \rbrace$

Hint: Make a list of numbers that are in each of these sets.

**Answer**: 

## Question 7 (5 points)

List all the different ways that we can partition the the set $S = \lbrace a, b, c \rbrace$.

**Answer**: 

|Partitioning #|Partitions of $S$|
|:-:|:-:|
|1||
|2||
|3||
|4||

Add more rows if needed.

## Question 8 (8 points)

In Python, you can create sets using "set comprehensions" (which is similar to "list comprehensions").  We read the following $S = \lbrace P(x) \mid x \in D \land C(x) \rbrace$ in English as "$S$ is the set of all values $P(x)$ such that $x$ is an element of the domain set $D$ and satisifies the condition $C(X)$".  We can translate this into Python code as: `S = {P(x) for x in D if C(x)}`.  The function calls `P(x)` and `C(x)` can be other defined functions, other defined lambda functions, or expressions written directly in the set comprehension.  Additionally, $D$ could be a set defined in a different variable or it could be provided directly in the set comprehension.

Recall the use of the `range(a,b)` function in Python to generate an iterable collections from `a` to `b-1`.

Use the starting code below to create set comprehensions as follows:

|Set ID|Set Builder Notation|
|:-:|:-:|
|Set1|$\lbrace \frac 1 n \mid n \in \lbrace 2, 4, 8, 16 \rbrace \rbrace$|
|Set2|$\lbrace n^2 \mid n \in \lbrace -2, -1, 0, 1, 2 \rbrace \rbrace$|
|Set3|$\lbrace n \mid n \in \mathbf{Z}^+,  n \text{ is a factor of } 24 \rbrace$|
|Set4|$\lbrace n \mid n \in \mathbf{Z}, -10 \le n \le 10, n \text { is odd.} \rbrace$|


```python
Set1 = None # Add Set Comprehension Code Here
Set2 = None # Add Set Comprehension Code Here
Set3 = None # Add Set Comprehension Code Here
Set4 = None # Add Set Comprehension Code Here

# Note that sets do not maintain order so it may vary
print(Set1)
print(Set2)
print(Set3)
print(Set4)
```