import numpy as np
import pandas as pd

# Example dataset: Daily temperatures of 3 cities over a year
data = {
    "City1": np.random.randint(20, 40, 365),
    "City2": np.random.randint(15, 35, 365),
    "City3": np.random.randint(10, 30, 365),
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Mean temperature for each city
mean_temps = df.mean()

# Standard deviation for each city
std_devs = df.std()

# City with the highest temperature range
temp_ranges = df.max() - df.min()
city_highest_range = temp_ranges.idxmax()

# City with the most consistent temperature
city_most_consistent = std_devs.idxmin()

print("Mean Temperatures:\n", mean_temps)
print("\nStandard Deviations:\n", std_devs)
print("\nCity with Highest Temperature Range:", city_highest_range)
print("City with Most Consistent Temperature:", city_most_consistent)
