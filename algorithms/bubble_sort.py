def bubble_sort(arr, visualize):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            visualize(arr, j, j + 1)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
