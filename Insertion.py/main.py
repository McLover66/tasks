def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            print(arr)
            j -= 1
            print(j)
        arr[j + 1] = key
        print(arr)

# Пример использования
my_array = [12, 9, 10, 11, 13, 5, 6]
insertion_sort(my_array)
print("Отсортированный массив:", my_array)
