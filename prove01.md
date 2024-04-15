# CSE 280 Prove 01

(c) BYU-Idaho - It is an honor code violation to post this
file completed or uncompleted in a public file sharing site. S4.

**Instructions**: Answer each question using proper markdown notation as needed.  Use the preview view in Visual Studio Code (or another editor if desired) to see the formatting, tables, and mathematical formula properly rendered.  If you need to write code, then first test your code in a separate file and then copy the code into this document using code fences. 

**Name**: 

## Question 1 (5 points)

Identify (with an "X") whether each statement is either a proposition or non-propisition.  The first two are done for you:

|Statement|Proposition|Non-Proposition|
|:-:|:-:|:-:|
|I got an A in CSE 280|X||
|Hello!||X|
|The hose has a leak.|||
|The wind speed is greater than 30 miles per hour.|||
|Close the window.|||
|The window is closed.|||
|Are you graduating this semester?|||

## Question 2 (28 points)

Complete the following truth tables (the first one is done for you):

1. $p \land q$

|$p$|$q$|$p \land q$|
|:-:|:-:|:-:|
|T|T|T|
|T|F|F|
|F|T|F|
|F|F|F|

2. $p \lor q$

|$p$|$q$|$p \lor q$|
|:-:|:-:|:-:|
|T|T||
|T|F||
|F|T||
|F|F||

3. $\neg p \to q$

|$p$|$q$|$\neg p$|$\neg p \to q$|
|:-:|:-:|:-:|:-:|
|T|T|||
|T|F|||
|F|T|||
|F|F|||

4. $p \land \neg q$

|$p$|$q$|$\neg q$|$p \land \neg q$|
|:-:|:-:|:-:|:-:|
|T|T|||
|T|F|||
|F|T|||
|F|F|||

5. $p \land (q \lor \neg r)$

|$p$|$q$|$r$|$\neg r$|$q \lor \neg r$|$p \land (q \lor \neg r)$|
|:-:|:-:|:-:|:-:|:-:|:-:|
|T|T|T||||
|T|T|F||||
|T|F|T||||
|T|F|F||||
|F|T|T||||
|F|T|F||||
|F|F|T||||
|F|F|F||||

6. $p \lor \neg (\neg q \land \neg r)$

|$p$|$q$|$r$|$\neg q$|$\neg r$|$\neg q \land \neg r$|$\neg (\neg q \land \neg r)$|$p \lor \neg (\neg q \land \neg r)$|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|T|T|T||||||
|T|T|F||||||
|T|F|T||||||
|T|F|F||||||
|F|T|T||||||
|F|T|F||||||
|F|F|T||||||
|F|F|F||||||

## Question 3 (12 points)

Determine if the following propositions written in English are True or False (the first one is done for you):

|Proposition|True or False|
|-|-|
|If $2+2=4$, then pigs can fly.|False|
|If $2+7=5$, then Elvis is alive.||
|If pigs can fly, then dogs can't fly.||
|$2+1=3$ if and only if $1+2=3$.||
|$1+2=3$ if and only if $3+1=6$.||
|$1+3=2$ if and only if the earth is flat.||
|$1 \lt 2$ if an only if $2 \lt 3$.||

## Question 4 (5 points)

In electronics, you can create an Adder which will add binary values together and produce the correct response.  The correct response will include the result and a carry value.  For example, if you have $1_b + 1_b$ this will result is $0$ carry $1$.  Here is a summary of all possible cases for $A+B$

|$A$|$B$|Result|Carry|
|---|---|------|-----|
| 0 | 0 |   0  |  0  |
| 0 | 1 |   1  |  0  |
| 1 | 0 |   1  |  0  |
| 1 | 1 |   0  |  1  |

The Adder can be defined logically by the following:  

* Result = $A \oplus B$
* Carry = $A \land B$

Recall that exclusive or ($\oplus$) is defined by the following truth table:

|$p$|$q$|$p \oplus q$|
|:-:|:-:|:-:|
|T|T|F|
|T|F|T|
|F|T|T|
|F|F|F|

Implement the `adder` function in Python below by setting `result` and `carry` equal to the correct expressions.

```python
def adder(A, B):
    # Your code here
    return (result, carry)

print(f"0 + 0 = {adder(0,0)}")  # 0 + 0 = (0, 0)
print(f"0 + 1 = {adder(0,1)}")  # 0 + 1 = (1, 0)
print(f"1 + 0 = {adder(1,0)}")  # 1 + 0 = (1, 0)
print(f"1 + 1 = {adder(1,1)}")  # 1 + 1 = (0, 1)
```