# CSE 280 Challenge Set 04

(c) BYU-Idaho

## Question 1

For each of these functions, determine if they are well-defined, one-to-one, onto and/or a bijection.  For these problems, let $A = \lbrace x \mid x \in \mathbf{Z}, 0 \lt x \lt 5 \rbrace$ and let $B = \lbrace x \mid x \in \mathbf{Z}, 0 \le  x \le 5 \rbrace$ .  You may want to draw a digraph of each function (with dots and arrows).  Recall that if not well-defined, then it is neither 1-1, onto, nor a bijection.

|Function|Well Defined|1-1|Onto|Bijection|
|:-:|:-:|:-:|:-:|:-:|
|$f : A \to A, \text{ where } f = \lbrace (1,2),(2,2),(3,3),(4,3) \rbrace$|||||
|$f : A \to A, \text{ where } f = \lbrace (1,1),(2,2),(3,4),(4,3) \rbrace$|||||
|$f : A \to A, \text{ where } f = \lbrace (2,2),(3,4),(4,3) \rbrace$|||||
|$f : A \to B, \text{ where } f = \lbrace (1,2),(2,3),(3,4),(4,5) \rbrace$|||||
|$f : B \to A, \text{ where } f = \lbrace (0,1),(1,1),(2,2),(3,2),(4,4),(5,3) \rbrace$|||||

## Question 2

For each of these functions, determine if they are well-defined, one-to-one, onto, and/or a bijection.  Consider using a graphing calculator like https://www.desmos.com.

|Function|Well Defined|1-1|Onto|Bijection|
|:-:|:-:|:-:|:-:|:-:|
|$f : \mathbf{Z} \to \mathbf{Z}, \text{ where } f(x) = 5x-7$|||||
|$f : \mathbf{Z}^+ \to \mathbf{Z}^+, \text{ where } f(x) = \lceil \frac {x}{5} \rceil$|||||
|$f : \mathbf{R} \to \mathbf{R}, \text{ where } f(x) = x^5-3x$|||||
|$f : \mathbf{R}^+ \to \mathbf{R}, \text{ where } f(x) = \frac{1}{x}$|||||
|$f : \mathbf{R} \to \mathbf{R}, \text{ where } f(x) = \log_5 (x^2)$|||||
|$f : \lbrace x \mid x \in \mathbf{R}, x \gt 0 \rbrace \to \mathbf{R}, \text{ where } f(x) = \log_5 (x^2)$|||||
|$f : \lbrace x \mid x \in \mathbf{R}, x \ne 0 \rbrace \to \mathbf{R}, \text{ where } f(x) = \log_5 (x^2)$|||||

## Question 3

**Part 1**

Find the inverse $f^{-1}(x)$ (if it exists) of the following functions:

* $f : \mathbf{R} \to \mathbf{R}, \text{ where } f(x) = (x - 32) * 5/9$

<br />

* $f : \mathbf{R} \to \lbrace x \mid x \in \mathbf{R}, x \gt 0 \rbrace\text{ where } f(x) = \frac{1}{2^x}$

<br />

* $f : \mathbf{R} \to \mathbf{Z}, \text{ where } f(x) = \lfloor x \rfloor$

<br />

* $f : \mathbf{R} \to \mathbf{R}, \text{ where } f(x) = x^2$

<br />

* $f : \mathbf{R} \to \mathbf{R}, \text{ where } f(x) = x^3$

<br />

**Part 2**

Select a value of $x$ (per the domain) and calculate $(f^{-1} \circ f)(x)$ for all functions that had an inverse in Part 1 to demonstrate that the inverse was successfully created.

<br /><br /><br />

## Question 4

Define the following two functions:

* $f : \mathbf{R} \to \mathbf{R}, \text{ where } f(x) = \lceil x \rceil - x$ 
* $g : \mathbf{R} \to \mathbf{R}, \text{ where } g(x) = x - \lfloor x \rfloor$ 

**Part 1**

Graph function $f$ using a graphing calculator. Explain what this so-called "sawtooth" function represents.

<br /><br />

**Part 2**

Based on your answer above, does an inverse to $f$ exist?

<br /><br />

**Part 3**

Determine what $f(x) + g(x)$ is equal to.

