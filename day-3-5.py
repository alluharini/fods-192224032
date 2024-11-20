from scipy import stats
import numpy as np
temperatures = [30, 32, 33, 35, 29, 40, 50, 31, 28, 34]
mean = np.mean(temperatures)
variance = np.var(temperatures)
outliers = [temp for temp in temperatures if abs(temp - mean) > 2 * np.sqrt(variance)]
print("Variance:", variance)
print("Outliers:", outliers)
