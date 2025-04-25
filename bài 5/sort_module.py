def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Hoán đổi phần tử
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# bubbleSort() ở đây trả về mảng đã sắp xếp.