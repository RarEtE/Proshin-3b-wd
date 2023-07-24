+import pandas as pd
import math

arr = [(1, 2), (3, 4), (-1, 5), (6, -3)]
arr_dict = {"coordinates": [], "distance": []}
# Заполнение ассоциативного массива с расчетом расстояний
for i in arr:
    dist = math.dist((0, 0), i)
    arr_dict['coordinates'].append(i)
    arr_dict['distance'].append(dist)

    
df = pd.DataFrame(arr_dict)                    # Преобразование ассоциативного массива в DataFrame
sorted_df = df.sort_values(by='distance')      # Сортировка внутри DataFrame
np = sorted_df['coordinates'].to_numpy()       # Преобразование DataFrame в NumPy массив
# print(sorted_df)  # для отладки
print(np)



arr = [(1, 2), (3, 4), (-1, 5), (6, -3)]
def sort_by_dist(element):
    return math.dist((0, 0), element)
sortedList = sorted(arr, key=sort_by_dist)
print(sortedList)