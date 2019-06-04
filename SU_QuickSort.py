def quickSort(nums):
    qSort(nums, 0, len(nums)-1)


def qSort(nums, lo, hi):
    if lo >= hi:
        return 
    
    p = partition(nums, lo, hi)
    qSort(nums, lo, p-1)
    qSort(nums, p+1, hi)
    

def partition(nums, lo, hi):
    """
    :return: index 
    将nums分成两部分，一部分在index的左边，它们全都小于等于index，一部分在index的右边，它们全都大于index
    """
    
    def swap(nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
    
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
