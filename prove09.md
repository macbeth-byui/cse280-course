# CSE 280 Prove 9

(c) BYU-Idaho - It is an honor code violation to post this
file completed or uncompleted in a public file sharing site. S4.

**Instructions**: Answer each question using proper markdown notation as needed.  Use the preview view in Visual Studio Code (or another editor if desired) to see the formatting, tables, and mathematical formula properly rendered.  If you need to write code, then first test your code in a separate file and then copy the code into this document using code fences. 

**Name**:

## Question 1 (16 points)

Give the first six terms of the following sequences starting with the value specified.

|Description|First 6 terms in the Sequence|
|:-:|:-:|
|A geometric sequence in which the first value is 5 and the common ratio is 7||
|An arithmetic sequence in which the first value is 3 and the common difference is 2.||
|A geometric sequence in which the first value is 36 and the common ratio is 1/4.||
|An arithmetic sequence in which the first value is 9 and the common difference is -1/2.||

## Question 2 (12 points)

Write recursive functions in python that will return the value of $f_n$ term for the following recurence relations.  The test code will generate $f_0, f_1, \text{ ... } , f_9$

|Function|Sequence|
|:-:|:-:|
|`fun1`|$f_0 = 5\\f_n=f_{n-1} + 3n \text{, for } n \ge 1$|
|`fun2`|$f_0 = 1\\f_n=n^3+f_{n-1} \text{, for } n \ge 1$|
|`fun3`|$f_0 = 1\\f_1 = 3\\f_n=f_{n-1}*f_{n-2} \text{, for } n \ge 2$|
|`fun4`|$f_0 = 1\\f_1 = 5\\f_n=f_{n-1}+(f_{n-2})^2 \text{, for } n \ge 2$|

```python
def fun1(n):
    # Add recursive code here

def fun2(n):
    # Add recursive code here

def fun3(n):
    # Add recursive code here

def fun4(n):
    # Add recursive code here

print([fun1(n) for n in range(10)]) # [5, 8, 14, 23, 35, 50, 68, 89, 113, 140]
print([fun2(n) for n in range(10)]) # [1, 2, 10, 37, 101, 226, 442, 785, 1297, 2026]
print([fun3(n) for n in range(10)]) # [1, 3, 3, 9, 27, 243, 6561, 1594323, 10460353203, 16677181699666569]
print([fun4(n) for n in range(10)]) # [1, 5, 6, 31, 67, 1028, 5517, 1062301, 31499590, 1128514914191]
```

## Question 3 (12 points)

Evaluate the following sums manually:

|Summation|Value|
|:-:|:-:|
|$\displaystyle\sum_{i=0}^{5}3i+1$||
|$\displaystyle\sum_{i=1}^{4}(-1)^i$||
|$\displaystyle\sum_{i=0}^{5}2^i$||

## Question 4 (10 points)

Write a list comprehension in Python for each of the following.  The `sum` function is called in the test code to evaluate the $\sum$.

|Seq #|Value|
|:-:|:-:|
|1|$\displaystyle\sum_{k=0}^{53}k^3$|
|2|$\displaystyle\sum_{k=4}^{27}2^k - 2$|
|3|$\displaystyle\sum_{k=-3}^{18}k^5 + 1$|
|4|$\displaystyle\sum_{k=-2}^{7}2^k$|
|5|$\displaystyle\sum_{k=1}^{1,000,000}\frac{1}{k}$|

```python
seq1 = # Add list comprehension here

seq2 = # Add list comprehension here

seq3 = # Add list comprehension here

seq4 = # Add list comprehension here

seq5 = # Add list comprehension here

print(sum(seq1)) # 2047761
print(sum(seq2)) # 268435392
print(sum(seq3)) # 6656947
print(sum(seq4)) # 255.75
print(sum(seq5)) # 14.39 (approx)
```