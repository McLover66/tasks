def optimized_bubble_sort(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        n -= 1


# Пример использования
my_list = [64, 34, 25, 12, 22, 11, 90]
optimized_bubble_sort(my_list)
print("Отсортированный массив:", my_list)
