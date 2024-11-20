from scipy import stats
import numpy as np

expenses = np.array([[2000, 2500, 3000], [2200, 2600, 3100], [2400, 2700, 3200]])
variance = np.var(expenses, axis=0)
covariance_matrix = np.cov(expenses, rowvar=False)
print("Variance:", variance)
print("Covariance Matrix:\n", covariance_matrix)

