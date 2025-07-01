# Euclid Algorithm

Euclids algorithm will find the **Greatest Common Divisor** ($gcd$) between two postive integers. Written as a **recurrence relation**:

$gcd(x,y) = \begin{cases}y &\text{if } x = 0 \\ gcd(y \text{ mod } x, x) &\text{else} \end{cases}$

Python Code:

```python
def euclid(x, y):
    """
    Implements the euclid algorithm to find the GCD
    of x and y
    """
    if x == 0:
        return y
    return euclid(y % x, x)

print(euclid(20,56))  # Displays 4
```

We can manually solve with a table where each row as recursive call to the `euclid` function:

|$x=r'$|$y=x'$|$r=y \text{ mod } x$|
|:----:|:----:|:------------------:|

Consider $gcd(504, 792)$

|$x=r'$|$y=x'$|$r=y \text{ mod } x$
|:----:|:----:|:------------------:
|504   |792   |288                 
|288   |504   |216                 
|216   |288   |72
|72    |216   |0
|0     |**72**|-

Consider $gcd(1375, 147)$

|$x=r'$|$y=x'$|$r=y \text{ mod } x$
|:----:|:----:|:------------------:
|1375  |147   |147                 
|147   |1375  |52                 
|52    |147   |43
|43    |52    |9
|9     |43    |7
|7     |9     |2
|2     |7     |1
|1     |2     |0
|0     |**1** |-


# Extended Euclid Algorithm

This will find the $gcd$ and also represent it in a linear combination:

$gcd(x,y) = g = xs + yt \text{, where }s, t \in \mathbf{Z}$

Written as a recurrence relation with 3 results including $g$ (actual $gcd$), $s$ and $t$:

$gcd(x,y) = \begin{cases}(g=y, ~ s=0, ~ t=1) &\text{if } x = 0 \\ \\(g', ~s', ~t') = gcd(y \text{ mod } x, ~x) &\text{else} \\(g=g', ~s=t'-(y \text{ div }x) \cdot s', ~t=s') \end{cases}$

Python Code:

```python
def euclid(x, y):
    """
    Implements the euclid algorithm to find the GCD
    of x and y in linear combination form. This
    function returns a tuple (c, s, t) where
    gcd = g = s*x + t*y.
    """
    if x == 0:
        return (y, 0, 1)
    (g, s, t) = euclid(y % x, x)
    return (g, t - (y // x) * s, s)

print(euclid(20,56)) # Prints (4, 3, -1) => 4 = 20*3 + 56*-1
```

We can manually solve by modifying the table we used with the original Euclid algorithm.  Note that in the recurrence relation above, we fill out the first 3 columns until we get to the base case of $x=0$.  Then we return back calculation the $s$ and the $t$.  We will need the quotient ($q$) when we return back so we can fill out the 4th column while going down for convienance:

|$x=r'$|$y=x'$|$r=y \text{ mod } x$|$q=y \text{ div } x$|$s = t'-q \cdot s'$|$t = s'$
|:----:|:----:|:------------------:|:------------------:|:-----------------:|:------:


Consider $gcd(504, 792)$

Evaluate going down first:

|$x=r'$|$y=x'$|$r=y \text{ mod } x$|$q=y \text{ div } x$|$s = t'-q \cdot s'$|$t = s'$
|:----:|:----:|:------------------:|:------------------:|:-----------------:|:------:
|504   |792   |288                 |1  
|288   |504   |216                 |1
|216   |288   |72                  |1
|72    |216   |0                   |3
|0     |**72**|-                   |-                   |0                  |1

Then evaulate the last columns going back up:

|$x=r'$|$y=x'$|$r=y \text{ mod } x$|$q=y \text{ div } x$|$s = t'-q \cdot s'$|$t = s'$
|:----:|:----:|:------------------:|:------------------:|:-----------------:|:------:
|504   |792   |288                 |1                   |$-1-(1 \cdot 2) = -3$ | 2
|288   |504   |216                 |1                   |$1-(1 \cdot -1) = 2$  | -1
|216   |288   |72                  |1                   |$0-(1 \cdot 1) = -1$  | 1
|72    |216   |0                   |3                   |$1-(3 \cdot 0) = 1$   | 0
|0     |**72**|-                   |-                   |0                     | 1

The final result is $gcd(504,792) = 72 = 504 \cdot -3 + 792 \cdot 2$

Consider $gcd(1375, 147)$

|$x=r'$|$y=x'$|$r=y \text{ mod } x$|$q=y \text{ div } x$|$s = t'-q \cdot s'$|$t = s'$
|:----:|:----:|:------------------:|:------------------:|:-----------------:|:------:
|1375  |147   |147                 |0                   |-65                |608
|147   |1375  |52                  |9                   |608                |-65
|52    |147   |43                  |2                   |-65                |23
|43    |52    |9                   |1                   |23                 |-19
|9     |43    |7                   |4                   |-19                |4
|7     |9     |2                   |1                   |4                  |-3
|2     |7     |1                   |3                   |-3                 |1
|1     |2     |0                   |2                   |1                  |0
|0     |**1** |-                   |-                   |0                  |1

The final result is $gcd(1375, 147) = 1 = 1375 \cdot -65 + 608 \cdot 147$