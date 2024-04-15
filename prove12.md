# CSE 280 Prove 12

(c) BYU-Idaho - It is an honor code violation to post this
file completed or uncompleted in a public file sharing site. S4.

**Instructions**: Answer each question using proper markdown notation as needed.  Use the preview view in Visual Studio Code (or another editor if desired) to see the formatting, tables, and mathematical formula properly rendered.  If you need to write code, then first test your code in a separate file and then copy the code into this document using code fences. 

**Name**:

**IMPORTANT: For all problems, you need to calculate the exponents and factorials to get a single integer value.**

## Question 1 (3 points)

Tessie and her friends have between them 15 board games, 12 card games, and 1 word game.  If their game nights feature the word game plus one other game (either a board game or a card game), how many different game nights can they have?

**Answer**: 

## Question 2 (3 points)

Now Tessie and her friends have acquired two more word games (for a total of 3) and have deided to vary the snacks they munch on while playing games.  They have selected 7 different types of snacks.  If a game-night configuration consists of a word game, another game (either a board or card game), and a snack, then how many different game-night configurations are possible now?

**Answer**: 

## Question 3 (3 points)

How many different 8-character passwords are possible if all uppercase (A-Z), lowercase (a-z), and digits (0-9) are allowed and duplication is also allowed?

**Answer**: 

## Question 4 (3 points)

How many three-letter acronyms (arrangements of 3 alphabetic letters) are there with repetition allowed?  Assume uppercase (A-Z) only.

**Answer**: 

## Question 5 (3 points)

How many three-letter acronyms (arrangements of 3 alphabetic letters) are there with repetition **not** allowed?  Assume uppercase (A-Z) only.

**Answer**: 

## Question 6 (3 points)

How many different sequences can be formed using either two or three letters (A-Z) followed by either two or three digits (0-9) with duplication allowed?

For example:
* AB01
* ABC12
* XY236
* XYZ123

**Answer**: 

## Question 7 (4 points)

Suppose you flip a fair coin 10 times.  Determine how many ways you can get each of the scenarios in the table below.

|Scenario|Number of Ways|
|:-:|:-:|
|no heads||
|exactly one head||
|exactly two heads||
|at least two heads||

## Question 8 (3 points)

Consider the following fruit that is available to you: raspberries, strawberries, blueberries, apples, oranges, bananas, kiwi, papaya, and mango.  Just choosing five from the list of 9, how many different fruit salads (with no duplicates of fruits) can you make??

**Answer**: 

## Question 9 (3 points)

What is the number of unique strings that can be formed by reordering the characters in the word `SUCCESS`?

**Answer**: 

## Question 10 (24 points)

### Part 1

Implement the `P` function and the `C` function to compute the $r$-permutation and $r$-combination, respectively for a set of size $n$.  You will need to use the `factorial` function provided in the `math` library in Python.

```python
from math import factorial
# factorial(6) = 6! = 720

def P(n,r):
    # Add your code here.  Recommend using integer division instead of regular division
    pass

def C(n,r):
    # Add your code here.  Recommend using integer division instead of regular division
    pass

```

### Part 2

Use the `P(n,r)` function you wrote to answer the following problems:

|Scenario|Answer|
|:-:|:-:|
|How many different arrangements can be made of 5 people from a group of 8 people to stand in line for a picture?||
|How many different ways can 8 different projects be assigned to 26 people?  Only one project per person.  Not all people will be assigned to a project.||
|How many different ways can we assign 15 pilots to 100 possible flight schedules?||

### Part 3

Use the `C(n,r)` function you wrote to answer the following problems:

|Scenario|Answer|
|:-:|:-:|
|How many ways can we form a committee of 5 people from a group of 8 people?||
|How many ways can we select 8 people from a group of 26 people to work on a single project, assuming all people are equally qualified?||
|How many ways can we selet 15 winners for a vacation drawing from a group of 100 contestants assuming each prize is the same?||


