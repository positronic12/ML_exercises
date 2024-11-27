import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()

raw_data = pd.read_csv(r"C:\Users\tjasa\OneDrive\Namizje\python_statistics\STATSMODELS_exercises\S33_L204_exercise_to_do\real_estate_price_size_year_view.csv")

data = raw_data.copy()

data['view'] = data['view'].map({'Sea view': 1, 'No sea view': 0})

print(data.describe())

y = data['price']
x1 = data[['size', 'year', 'view']]

x = sm.add_constant(x1)
results = sm.OLS(y,x).fit()
print(results.summary())

linear = 5.673e+04*data['view'] + 2718.9489*data['year'] + 223.0316*data['size'] - 5.398e+06
