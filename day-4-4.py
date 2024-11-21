import pandas as pd
data = pd.DataFrame({'Likes': [10, 20, 10, 30, 20, 10, 40]})
frequency = data['Likes'].value_counts()
print(frequency)
