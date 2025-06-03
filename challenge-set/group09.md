# CSE 280 Challenge Set 09

(c) BYU-Idaho

## Question 1

List the first 5 terms (use fractions instead of decimals) for the following sequences:

* A geometric sequence in which the first value is 1 and the common ratio is $-\frac{1}{2}$.

* An arithmetic sequence in which the first value is 1 and the common difference is $-\frac{1}{2}$.
* A geometric sequence in which the first value is -1 and the common ratio is $-\frac{1}{2}$.
* An arithmetic sequence in which the first value is -1 and common difference is $-\frac{1}{2}$.

<br /><br />


## Question 2

### Part 1

Evaluate the following:

* $\displaystyle\sum_{i=0}^{5}i^2$

* $\displaystyle\sum_{i=0}^{5}i^2+3-2i$

### Part 2

Evaluate the following arithmetic and geometric sums using the closed form formulas:

* $\displaystyle\sum_{i=0}^{99}3-2i$

* $\displaystyle\sum_{i=0}^{10}2 \cdot 3^i$

## Question 3

### Part 1

After reviewing the following python code, predict what will be displayed.

```python
def getValue1(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return getValue1(n-1) - getValue1(n-2)

print([getValue1(n) for n in range(20)])
```



### Part 2

After reviewing the following python code, predict what will be displayed.  Note that `a % b` will return the integer remainder when we divide `a` and `b`.  For example:

* `18 % 5 = 3`
* `31 % 13 = 5`
* `8 % 14 = 8` 

```python
def getValue2(a,b):
    if b == 0:
        return a
    return getValue2(b, a % b)

print(getValue2(12,15))
print(getValue2(64,24))
print(getValue2(17,31))
print(getValue2(121,88))
```

### Part 3

What mathematical problem is the `getValue2` function solving?

## Question 4

What activity does the following recurrence relation perform:

$F(A,B,[First|Rest]) = \begin{cases} B+F(A,B,Rest) &\text{if } First == A \\ First+F(A,B,Rest) &\text{else} \end{cases}$

$F(A,B,[\text{ }]) = [\text{ }]$




