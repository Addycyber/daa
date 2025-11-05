import random

# Deterministic Quick Sort (pivot = last element)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# Randomized Quick Sort (random pivot)
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + mid + randomized_quick_sort(right)

# Example
arr = [10, 7, 8, 9, 1, 5]
print("Deterministic Quick Sort:", quick_sort(arr))
print("Randomized Quick Sort:", randomized_quick_sort(arr))
