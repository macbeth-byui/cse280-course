def euclid(x, y):
    """
    Implements the euclid algorithm to find the GCD
    of x and y
    """
    if x == 0:
        return y
    return euclid(y % x, x)

print(euclid(-20,56))  # Displays 4