import pandas as pd
data = pd.DataFrame({'Age': [25, 30, 25, 40, 30, 25, 35]})
frequency = data['Age'].value_counts()
print(frequency)
