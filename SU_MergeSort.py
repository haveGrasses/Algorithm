
def mergeSort(arr):
    """原地排"""
    _mergeSort(arr, 0, len(arr)-1)


def _mergeSort(arr, l, r):
    """核心就是每次将arr划分为差不多等长的两部分，然后调用自己对这两部分进行排序，之后将两部分排序的结果merge起来"""
    if l >= r:  # 只有一个元素时，不需要再向下划分了
        return
    mid = (l+r) // 2
    _mergeSort(arr, l, mid)
    _mergeSort(arr, mid+1, r)
    merge(arr, l, mid, r)


def merge(arr, l, mid, r):
    """记录一个k，遍历l到r的总长度，当两部分都有数的时候，依次将小的数覆盖当前遍历的位置 当某一部分已经没数的时候 直接记录另一个部分的数"""
    backup = arr[l:r+1].copy()
    # backup = [arr[l+i] for i in range(r-l+1)]
    # backup = [arr[i] for i in range(l, r+1)]
    l1, l2 = l, mid + 1
    for i in range(l, r+1):
        if l1 > mid:
            arr[i] = backup[l2-l]
            l2 += 1
        elif l2 > r:
            arr[i] = backup[l1-l]
            l1 += 1
        elif backup[l1-l] < backup[l2-l]:  # 所有的判断和赋值都要以backup为准，arr在每一步都会发生变化
            arr[i] = backup[l1-l]
            l1 += 1
        else:
            arr[i] = backup[l2-l]
            l2 += 1


arr = [9, 4, 6, 2, 3, 7, 6, 8, 9, 1, 0]
print(mergeSort(arr))
print(arr)
