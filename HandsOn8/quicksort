def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high, i):
    if low <= high:
        pivot_index = partition(arr, low, high)
        if pivot_index == i:
            return arr[pivot_index]
        elif pivot_index < i:
            return quicksort(arr, pivot_index + 1, high, i)
        else:
            return quicksort(arr, low, pivot_index - 1, i)
    return None

def ith_order_statistic(arr, i):
    if i < 0 or i >= len(arr):
        return None
    return quicksort(arr, 0, len(arr) - 1, i)

arr = [12, 4, 7, 3, 9, 1,  3, -2, 0, 1, -3]
i = 2  
result = ith_order_statistic(arr, i)
print(f"The {i}th order statistic is: {result}")

