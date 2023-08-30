def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень текущей пирамиды
    left = 2 * i + 1  # Левый потомок
    right = 2 * i + 2  # Правый потомок

    # Если левый потомок больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Если правый потомок больше корня
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если наибольший элемент не является корнем
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем местами корень и наибольший элемент

        # Рекурсивно применяем heapify к поддереву
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Построение максимальной пирамиды
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из пирамиды
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Меняем местами корень и последний элемент
        heapify(arr, i, 0)

# Пример использования
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Отсортированный массив:", arr)
