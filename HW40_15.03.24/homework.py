import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales_data = np.array([1000, 1500, 2000, 2500, 1800, 2100, 2200])

df = pd.DataFrame(sales_data, columns=['Sales'])

print("Основная статистика о продажах:")
print(df.describe())

plt.hist(df['Sales'], bins=5, color='skyblue', edgecolor='black')
plt.title('Распределение продаж')
plt.xlabel('Сумма продаж')
plt.ylabel('Частота')
plt.show()