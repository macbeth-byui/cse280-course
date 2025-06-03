# CSE 280 Challenge Set 06 - Solutions

(c) BYU-Idaho

## Question 1

Consider the $K_8$ graph below.  

### Part 1

Find the following: 

* total edges
* total vertices
* degree of each vertex
* total degree of the graph

![](group6_graph1.png)

Answer:

* Edges = 28 (7*8/2)
* Verticies = 8
* Degree of each Vertex = 7
* Total Degree = 56

### Part 2

What is the relationship between the number of edges and the total degree?

Answer: Total Degree = $2 \cdot \mid E \mid$

### Part 3

Does the graph above have an Euler circuit?  How do you know?

Answer: No.  It has odd degrees.

## Question 2

The following graph does not have an Euler circuit.  How can you add 1 new edge to ensure there is a Euler circuit?

![](group6_graph2.png)

Answer:  Draw an edge connecting nodes 3 and 4.

## Question 3

Consider the following two graphs.  If these graphs are isomorphic, then fill in the missing letters A through E.

|Graph 1|Graph 2
|:-:|:-:|
|![](group06_graph3.drawio.png)|![](group06_graph4.drawio.png)|

Answer: There are multiple ways to show the mapping.  If you start with A on the top, the follow one of the lines to put B, C, D, and E.  Going around the star, one order would be A, D, B, E, C and another order would be A, C, E, B, D.

## Question 4

Consider the Finite State Machine (FSM) below.

![](group6_graph5.png)

**Part 1**

* What is the final state with input 100011?  Is the input accepted?
* What is the final state with input 0000? Is the input accepted?
* What is the final state with input 1100? Is the input accepted?

Answer:

* C - Accepted
* D - Not Accepted
* C - Accepted

**Part 2**

What type of input stream does the FSM look for?

A string that has at least one 1 and one 0.

## Question 5

**Part 1**

Draw an FSM to determine if a string of only A's and B's has the substring "ABAB" within it.  Test the FSM with:

* AABABB - Match
* ABAABAB - Match
* ABBABAABABAAA - Match

Answer:

![](group06_graph6.drawio.png)

**Part 2**

Draw an FSM to determine how many times the substring "ABAB" exists within the string.  Recall that you do this by counting how many times you arrive at the acceptance state.  Test the FSM with:

* ABABABAB - 3 times
* ABAABABABB - 2 times

Answer:

![](group06_graph7.drawio.png)
