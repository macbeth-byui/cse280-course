# CSE 280 Challenge Set 03

(c) BYU-Idaho

## Question 1

Compute the following cartesian products:

* $\lbrace A, B, C\rbrace \times \lbrace H,J \rbrace = $ 

<br /><br />

* $\lbrace A, B, C\rbrace \times \lbrace H,J \rbrace \times \lbrace H,J \rbrace =$

<br /><br />

## Question 2

Identify four values that are in each of the following sets:

* $\lbrace x \mid x \in \mathbf{Z}^-, x+3 \text{ is a multiple of 5} \rbrace$

<br />

* $\lbrace \frac{1}{x^2} \mid  x \in \mathbf{Z}, x \ge 2, x \text{ is not prime } \rbrace$

## Question 3

Let $A = \lbrace 1,3,5,7,9,11,13,15,17 \rbrace$, $B = \lbrace 2,4,6,8,10,12,14 \rbrace$, $C = \lbrace1,3,6,9,12,15,17,20 \rbrace$ and the universal set is $U = \lbrace x \mid x \in \mathbf{Z}, 0 \le x \le 20\rbrace$.  Determine the contents of these resulting sets:

|Set Expression|Resulting Set|
|:-:|:-:|
|$(A \cup B) \cap C$||
|$C - B$||
|$\overline{B}$||
|$C \oplus B$||

## Question 4

Define the sets $A = \lbrace 1, 2, 6 \rbrace$, $B = \lbrace 2, 3, 4 \rbrace$, $C = \lbrace 5 \rbrace$, $D = \lbrace x \mid x \in \mathbf{Z}, 1 \le x \le 6 \rbrace$, and $E = \lbrace x \mid x \in \mathbf{Z}, 1 \lt x \lt 6 \rbrace$.

* Can set $D$ be divided into the partitions $A$, $B$, and $C$?  If not, which condition of a partitioning is not satisfied?

<br />

* Can set $D$ be divided into the partitions $B$ and $C$? If not, which condition of a partitioning is not satisfied?

<br />

* Can set $E$ be divided into the partitions $B$ and $C$? If not, which condition of a partition is not satisfied?

<br />

* What are the different partionings that can be created from the set $(A \cap B) \cup C$.



## Question 5

The definition of set partitioning is a general definition.  In many applied cases, additional constraints are imposed.  In computing, an operating system will need to partition a collection of tasks to describe the order that they are executed.  Here are a list of tasks (where priority 1 is high, 2 is medium, and 3 is low)

* Task A: Requires 3 CPU cores, 8 GB Memory, Priority 1
* Task B: Requires 4 CPU cores, 10 GB Memory, Priority 3
* Task C: Requires 2 CPU cores, 6 GB Memory, Priority 2
* Task D: Requires 3 CPU cores, 6 GB Memory, Priority 2
* Task E: Requires 1 CPU core, 4 GB Memory, Priority 1

Assume the computer has 8 cores and 32 GB memory available.  If we divide the tasks into $n$ partitions, then the tasks in each partition would run concurrently and each partition would run sequentially.

* Why would this be a poor partitioning given the computer constraints: $\lbrace A \rbrace, \lbrace B \rbrace, \lbrace C \rbrace, \lbrace D \rbrace, \lbrace E \rbrace$

<br />

* Why would this be a poor partitioning given the computer constraints: $\lbrace A, B, C, D, E \rbrace$

<br />

* Propose a valid partitioning that would be more ideal given the computer constraints.  Explain why it is more ideal.

<br />

## Question 6

Consider the following sets where the universal set for this problem is $\mathbf{N}$ (does not include 0):

* $A$ = The set of all even numbers.
* $B$ = The set of all prime numbers.
* $C$ = The set of all perfect squares.
* $D$ = The set of all multiples of 10.

Using these sets and various set operators (e.g. union, intersection, complement, subset, etc...), represent the following statements in set notation:

* All multiples of 10 are even numbers.

<br />

* None of the perfect squares are prime numbers.

<br />

* If you take all the prime numbers, all the even numbers, all the perfect squares, and all the multiples of 10, you still won't have all the natural numbers.  Can you write this without using $\mathbf{N}$ in your answer?






