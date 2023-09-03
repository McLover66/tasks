def bucket_sort(arr):
    # Находим минимальное и максимальное значения в списке
    min_val = min(arr)
    max_val = max(arr)

    # Создаем пустые корзины
    bucket_range = (max_val - min_val) / (len(arr) - 1)
    buckets = [[] for _ in range(len(arr))]

    # Распределяем элементы по корзинам
    for num in arr:
        index = int((num - min_val) / bucket_range)
        buckets[index].append(num)

    # Сортируем каждую корзину (можно использовать любой другой алгоритм сортировки)
    for i in range(len(arr)):
        buckets[i] = sorted(buckets[i])

    # Объединяем отсортированные корзины в один отсортированный список
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr


# Пример использования
arr = [0, 500,1001, 1000, 2000]
sorted_arr = bucket_sort(arr)
print(sorted_arr)
