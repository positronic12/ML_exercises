import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from matplotlib.ticker import FuncFormatter
import seaborn as sns
sns.set(style="whitegrid")

data = pd.read_csv(r"C:\Users\tjasa\OneDrive\Namizje\python_statistics\STATSMODELS_exercises\S32_L187_exercise_to_do\real_estate_price_size.csv")

y = data['price']
x1 = data['size']
x = sm.add_constant(x1)


results = sm.OLS(y, x).fit()
# print(results.summary())

plt.scatter(x1, y)
line = 223.1787*x1 + 1.019e+05
fig = plt.plot(x1, line, c='orange', lw=3, label='linear approximation')

def format_y(value, _):
    return f"{value:,.0f}".replace(",", ".")

plt.gca().yaxis.set_major_formatter(FuncFormatter(format_y))

plt.title('Real Estate Price connection to Size', fontsize=22, fontweight='bold')
plt.xlabel('size [m$^2$]', fontsize=20)
plt.ylabel('price [EUR]', fontsize=20)

plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

plt.show()
