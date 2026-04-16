import random
import time


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    while low < high:
        pi = partition(arr, low, high)
        if pi - low < high - pi:
            quick_sort(arr, low, pi - 1)
            low = pi + 1
        else:
            quick_sort(arr, pi + 1, high)
            high = pi - 1


def measure_time(func, arr):
    temp = arr.copy()
    start = time.time()
    if func == quick_sort:
        func(temp, 0, len(temp) - 1)
    else:
        func(temp)
    end = time.time()
    return (end - start) * 1000


def generate_datasets():
    sizes = [1000, 5000, 10000]
    datasets = {}

    for size in sizes:
        random.seed(42)
        rand = [random.randint(1, 100000) for _ in range(size)]
        datasets[(size, "Random")] = rand
        datasets[(size, "Sorted")] = sorted(rand)
        datasets[(size, "Reverse")] = sorted(rand, reverse=True)

    return datasets


if __name__ == "__main__":

    print("Correctness Check")
    test = [5, 2, 9, 1, 5, 6]
    print("Insertion:", insertion_sort(test.copy()))
    print("Merge:", merge_sort(test.copy()))
    temp = test.copy()
    quick_sort(temp, 0, len(temp) - 1)
    print("Quick:", temp)

    datasets = generate_datasets()

    print("\nPerformance Table (ms)")
    print("Size\tType\t\tInsertion\tMerge\tQuick")

    for (size, dtype), data in datasets.items():
        t1 = measure_time(insertion_sort, data)
        t2 = measure_time(merge_sort, data)
        t3 = measure_time(quick_sort, data)

        print(f"{size}\t{dtype}\t\t{round(t1,2)}\t\t{round(t2,2)}\t{round(t3,2)}")