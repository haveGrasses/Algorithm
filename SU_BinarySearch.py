def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
        else:
            return mid
    return -1


arr = [3, 9, 28, 67, 12, 45]
arr.sort()
print(arr)
print(binary_search(arr, 12))

