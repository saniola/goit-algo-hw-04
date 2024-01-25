import timeit
import random


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Генерація рандомного масиву для сортування
arr = [random.randint(0, 1000) for _ in range(1000)]

# Вимір часу для сортування злиттям
merge_sort_time = timeit.timeit(
    stmt="merge_sort(arr.copy())", globals=globals(), number=1000
)

# Вимір часу для сортування вставкою
insertion_sort_time = timeit.timeit(
    stmt="insertion_sort(arr.copy())", globals=globals(), number=1000
)

# Вимір часу для Timsort (вбудований в Python)
timsort_time = timeit.timeit(stmt="sorted(arr.copy())", globals=globals(), number=1000)

print(f"Merge Sort Time: {merge_sort_time}")
print(f"Insertion Sort Time: {insertion_sort_time}")
print(f"Timsort Time: {timsort_time}")
