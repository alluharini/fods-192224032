import numpy as np
daily_sales = [200, 250, 240, 260, 270, 230, 300, 280, 220, 210, 250, 270, 240, 260, 290, 310, 200, 220, 250, 270, 230, 300, 280, 260, 240, 230, 220, 250, 240, 300]

# Calculate variance
sales_variance = np.var(daily_sales)
print("Variance of Daily Sales:", sales_variance)
