import numpy as np

response_times = [120, 230, 340, 150, 180, 90, 260, 400]
percentiles = np.percentile(response_times, [25, 50, 75])
print("Percentiles (25th, 50th, 75th):", percentiles)
