def quickSort(nums):
    qSort(nums, 0, len(nums)-1)


def qSort(nums, lo, hi):
    if lo >= hi:  # !important
        return 
    
    p = partition2(nums, lo, hi)
    qSort(nums, lo, p-1)
    qSort(nums, p+1, hi)
    

def partition(nums, lo, hi):
    """
    :return: index 
    将nums分成两部分，一部分在index的左边，它们全都小于等于index，一部分在index的右边，它们全都大于index
    """
    swap(nums, lo, lo+(hi-lo)//2) 
    i, j = lo + 1, hi
    while True:
        while i < hi and nums[i] <= nums[lo]:
            i += 1
        while j > lo and nums[j] > nums[lo]:
            j -= 1
        if i >= j:
            break
        swap(nums, i, j)
    swap(nums, lo, j)
    return j


def swap(nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        
        
def partition2(array, l, r):
    """ 只用一个指针，不用while循环，highly recommended! """
    x = array[r]
    i = l
    for j in range(l, r):
        if array[j] <= x:
            swap(array, i, j)
            i += 1
    swap(array, i, r)
    return i
