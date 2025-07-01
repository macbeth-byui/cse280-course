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