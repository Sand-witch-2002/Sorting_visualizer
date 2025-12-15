def selection_sort(arr, visualize):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            visualize(arr, min_idx, j)
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
