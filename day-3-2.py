import numpy as np
recovery_times = [5, 7, 10, 6, 9, 15, 3, 12]
percentiles = np.percentile(recovery_times, [10, 50, 90])
print("Percentiles (10th, 50th, 90th):", percentiles)
