import time
import pandas as pd
import math

# Option 6 function
def option6(n):
    j = 2
    total = 0
    while j < n:
        k = j
        step = max(1, int(n**(1/3) * math.log(n)))  # ensure step >= 1
        while k < n:
            total += k  # dummy work to simulate computation
            k += step
        j = 2 * j
    return total

# n values to test
n_values = [400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400]

# Run experiments
results = []
for n in n_values:
    start = time.perf_counter()
    option6(n)
    end = time.perf_counter()
    results.append((n, end - start))

# Save results to CSV (Excel can open this directly)
df = pd.DataFrame(results, columns=["n", "Time"])
df.to_csv("option6_results.csv", index=False)

print("Experiment completed. Re
