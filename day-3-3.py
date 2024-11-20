from scipy import stats
import numpy as np

purchase_amounts = [50, 20, 50, 40, 60, 30, 50, 40]
mean = np.mean(purchase_amounts)
mode = stats.mode(purchase_amounts, keepdims=False)
print("Mean:", mean)
print("Mode:", mode.mode)
