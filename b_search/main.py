import numpy

print('введите параметры массива')

k = int(input('первый элемент'))
l = int(input('последний элемент'))
m = int(input('шаг элемент'))
arr_ = numpy.arange(k, l, m)
print(arr_)

print('введите искомое число')
num= int(input())

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2  # Вычисляем индекс среднего элемента

        if arr[middle] == target:
            return middle  # Элемент найден, возвращаем его индекс
        elif arr[middle] < target:
            left = middle + 1  # Обновляем левую границу
        else:
            right = middle - 1  # Обновляем правую границу

    return -1  # Элемент не найден

# Вызываем бинарный поиск для поиска числа 7
result = binary_search(arr_, num)

if result != -1:
    print(f"Число {num} найдено в массиве на позиции {result+1}.")
else:
    print(f"Число {num} не найдено в массиве.")
