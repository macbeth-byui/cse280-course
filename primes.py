import math

def is_prime(n):
    for x in range(2, math.floor(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True

n = 3
count = 1
while True:
    if is_prime(n):
        count += 1
        if count % 100000 == 0:
            print(f"Primes Found: {count:,} Current prime: {n:,}")
    n += 1