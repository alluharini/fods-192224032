import pandas as pd

data = pd.DataFrame({
    'Disease': ['Common Cold', 'Diabetes', 'Bronchitis', 'Influenza', 'Kidney Stones'],
    'Diagnosed_Patients': [320, 120, 100, 150, 60]
})

most_common = data.loc[data['Diagnosed_Patients'].idxmax(), 'Disease']
print(most_common)
