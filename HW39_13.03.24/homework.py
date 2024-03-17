import numpy as np

sales_data = np.array([1000, 1500, 2000, 2500, 1800, 2100, 2200])

mean_sales = np.mean(sales_data)

weights = np.array([1, 1, 2, 1, 1, 1, 1])
weighted_mean_sales = np.average(sales_data, weights=weights)

max_sales = np.max(sales_data)
min_sales = np.min(sales_data)

print("Средняя сумма:", mean_sales)
print("Средневзвешенная сумма:", weighted_mean_sales)
print("Максимальная сумма:", max_sales)
print("Минимальная сумма:", min_sales)