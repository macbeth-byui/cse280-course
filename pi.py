import random
import math

samples = 1_000_000
events = 0

for _ in range(samples):
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    if x**2 + y**2 <= 1:
        events += 1

obs_prob = events / samples
est_pi = obs_prob * 4

print(f"Estimated Pi = {est_pi:.10f}")
print(f"Actual Pi    = {math.pi:.10f}")
print(f"Difference   = {(est_pi - math.pi):.10f}")