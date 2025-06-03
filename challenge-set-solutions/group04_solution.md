# CSE 280 Challenge Set 04 - Solutions

(c) BYU-Idaho

## Question 1

For each of these functions, determine if they are well-defined, one-to-one, onto, and/or a bijection.  For these problems, let $A = \lbrace x \mid x \in \mathbf{Z}, 0 \lt x \lt 5 \rbrace$ and let $B = \lbrace x \mid x \in \mathbf{Z}, 0 \le  x \le 5 \rbrace$ .  You may want to draw a digraph of each function (with dots and arrows).  Recall that if not well-defined, then it is neither 1-1, onto, nor a bijection.

|Function|Well Defined|1-1|Onto|Bijection|
|:-:|:-:|:-:|:-:|:-:|
|$f : A \to A, \text{ where } f = \lbrace (1,2),(2,2),(3,3),(4,3) \rbrace$|x||||
|$f : A \to A, \text{ where } f = \lbrace (1,1),(2,2),(3,4),(4,3) \rbrace$|x|x|x|x|
|$f : A \to A, \text{ where } f = \lbrace (2,2),(3,4),(4,3) \rbrace$|||||
|$f : A \to B, \text{ where } f = \lbrace (1,2),(2,3),(3,4),(4,5) \rbrace$|x|x|||
|$f : B \to A, \text{ where } f = \lbrace (0,1),(1,1),(2,2),(3,2),(4,4),(5,3) \rbrace$|x||x||

## Question 2

For each of these functions, determine if they are well-defined, one-to-one, onto, and/or a bijection.  Consider using a graphing calculator like https://www.desmos.com.

|Function|Well Defined|1-1|Onto|Bijection|
|:-:|:-:|:-:|:-:|:-:|
|$f : \mathbf{Z} \to \mathbf{Z}, \text{ where } f(x) = 5x-7$|x|x|||
|$f : \mathbf{Z}^+ \to \mathbf{Z}^+, \text{ where } f(x) = \lceil \frac {x}{5} \rceil$|x||x||
|$f : \mathbf{R} \to \mathbf{R}, \text{ where } f(x) = x^5-3x$|x||x||
|$f : \mathbf{R}^+ \to \mathbf{R}, \text{ where } f(x) = \frac{1}{x}$|x|x|||
|$f : \mathbf{R} \to \mathbf{R}, \text{ where } f(x) = \log_5 (x^2)$|||||
|$f : \lbrace x \mid x \in \mathbf{R}, x \gt 0 \rbrace \to \mathbf{R}, \text{ where } f(x) = \log_5 (x^2)$|x|x|x|x|
|$f : \lbrace x \mid x \in \mathbf{R}, x \ne 0 \rbrace \to \mathbf{R}, \text{ where } f(x) = \log_5 (x^2)$|x||x||

Answer:

* Not onto because you can't get ever integer from an integer.
* Not 1-1 because multiple $x$ map to the same value
* Not 1-1 because 3 different values of $x$ map to the same $y=0$)
* Not onto because missing 0 and negative
* Not well defined at x=0
* All
* Not 1-1 because 2 $x$ map to the same value

## Question 3

**Part 1**

Find the inverse $f^{-1}(x)$ of the following functions:

* $f : \mathbf{R} \to \mathbf{R}, \text{ where } f(x) = (x - 32) * 5/9$
* $f : \mathbf{R} \to \lbrace x \mid x \in \mathbf{R}, x \gt 0 \rbrace\text{ where } f(x) = \frac{1}{2^x}$
* $f : \mathbf{R} \to \mathbf{Z}, \text{ where } f(x) = \lfloor x \rfloor$
* $f : \mathbf{R} \to \mathbf{R}, \text{ where } f(x) = x^2$
* $f : \mathbf{R} \to \mathbf{R}, \text{ where } f(x) = x^3$

Answer:

* $f^{-1}(x) = (\frac{9}{5}*x) + 32$
* $f^{-1}(x) = \log_2{\frac{1}{x}}$
* Not a bijection (not 1-1).  No inverse exists.
* Not a bijection (not 1-1 or onto).  No inverse exists.
* $f^{-1} = \sqrt[3]{x}$ 

**Part 2**

Select a value of $x$ (per the domain) and calculate $(f^{-1} \circ f)(x)$ for both functions in Part 1 to demonstrate that the inverse was successfully created.

* $f(41) = 5; f^{-1}(5) = 41$
* $f(2) = \frac{1}{4}; f^{-1}(\frac{1}{4}) = log_2 4 = 2$
* N/A
* N/A
* $f(-5) = -125; f^{-1}(-125) = -5$

## Question 4

Define the following two functions:

* $f : \mathbf{R} \to \mathbf{R}, \text{ where } f(x) = \lceil x \rceil - x$ 
* $g : \mathbf{R} \to \mathbf{R}, \text{ where } g(x) = x - \lfloor x \rfloor$ 

**Part 1**

Graph function $f$ using a graphing calculator. Explain what this so-called "sawtooth" function represents.

Answer:

$f$ reprsents the positive fractional part of $x$

**Part 2**

Based on your answer above, does an inverse to $f$ exist?

Answer:

No, an inverse does not exist because we can't determine the original real number from the fractional part.

**Part 3**

Determine what $f(x) + g(x)$ is equal to.

Answer:

$f(x) + g(x) = \lceil x \rceil - \lfloor x \rfloor$

* If $x \in \mathbf{Z}$ then this is equal to 0
* Otherwise, this is equal to 1


