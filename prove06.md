# CSE 280 Prove 6

(c) BYU-Idaho - It is an honor code violation to post this
file completed or uncompleted in a public file sharing site. S4.

**Instructions**: Answer each question using proper markdown notation as needed.  Use the preview view in Visual Studio Code (or another editor if desired) to see the formatting, tables, and mathematical formula properly rendered.  If you need to write code, then first test your code in a separate file and then copy the code into this document using code fences. 

**Name**:

## Question 1 (5 points)

Fill in the adjacency table below for the graph below:

![](prove06_graph1.png)

|Vertex|Adjacent Verticies|
|:-:|:-:|
|0||
|1||
|2||
|3||
|4||

## Question 2 (8 points)

The list of 9 graphs below have 4 pairs of isomorphic graphs.  Find the 4 pairs.  Note that one of the graphs does not have a match.

![](prove06_graph2.png)

|#|Isomorphic Pairs|
|:-:|:-:|
|1st Pair||
|2nd Pair||
|3rd Pair||
|4th Pair||

Source: Question adapted from Applied Discrete Structures by Alan Doerr & Kenneth Levasseur which is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License.

## Question 3 (4 points)

Write python code to create an adjacency table for the undirected graph below.  Second, implement the `find_neighbors` function which will take as input vertex and the adjaceny table and returns a list of verticies that are adjacent to the input vertex.  Finally, implement the `is_neighbor` which takes two verticies and the adjaceny table and returns True if they are adjacent; False otherwise.

![](prove06_graph3.png)

```python
adjacency_table = {"A": ["B","C"], 
                   "B": ["A","C"],
                   "C": ["A","B","D"],
                   "D": ["C","E","F"],
                   "E": ["D","F"],
                   "F": ["D","E"]}

def find_neighbors(vertex, adjaceny_table):
    # Add your code here
    return None

def is_neighbor(vertex1, vertex2, adjacency_table):
    # Add your code here
    return None

print(find_neighbors('A', adjacency_table)) # should print ['B', 'C']
print(find_neighbors('D', adjacency_table)) # should print ['C', 'E', 'F']

print(is_neighbor('A','B',adjacency_table)) # True
print(is_neighbor('D','F',adjacency_table)) # True
print(is_neighbor('C','F',adjacency_table)) # False
```

## Question 4 (12 points)

Determine if the graph below has an Euler Circuit.  If it does, then write down the sequence of verticies that make up the Euler Circuit.  If it does not, then write "No Euler Circuit"

|Graph|Euler Circuit|
|:-:|:-:|
|![](prove06_graph4.png)||
|![](prove06_graph5.png)||
|![](prove06_graph6.png)||

## Question 5 (16 points)

Complete the tables below to identify the final state (per the FSM diagram) and whether that final state was an accepting state for each of the inputs.   

**Part 1**

![](prove06_graph7.png)

|Input|Final State|Accepting (Yes/No)|
|:-:|:-:|:-:|
|00101|||
|011100|||
|01111|||
|0101|||
|00000|||
|11111|||
|11100|||
|10011|||

**Part 2**

![](prove06_graph8.png)

|Input|Final State|Accepting (Yes/No)|
|:-:|:-:|:-:|
|00101|||
|011100|||
|01111|||
|0101|||
|00000|||
|11111|||
|11100|||
|10011|||

## Question 6 (5 points)

Describe the bit string recognized/accepted by the following FSM:

![](prove06_graph9.png)

Answer: 