+arr = [5, 7, 11, 13, 15, 20, 25]
amount = 0
count = 0
res = 0

for i in arr:
    if i > 10:                 # Если элемент массива больше 10
        amount += i
        count += 1
        res = amount / count   # Делим сумму элементов (которые больше 10) на их количество
print(res)