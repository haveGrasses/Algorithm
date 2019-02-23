class Solution:
    """ use two pointers """
    def twoSum(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        lo, hi = 0, len(numbers) - 1
        while (numbers[lo] + numbers[hi] != target): 
            if numbers[lo] + numbers[hi]  < target:
                lo += 1
            else:
                hi -= 1
        return [lo+1, hi+1]


class Solution2:
    """ use two pointers """
    def twoSum(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        lo, hi = 0, len(numbers) - 1
        while (lo < hi):  # while condiation differ from above solution
            tmp = numbers[lo] + numbers[hi]
            if tmp == target:
                return [lo+1, hi+1]
            elif tmp > target:
                hi -= 1
            else:
                lo += 1


class Solution3:
    """ use dict, same as two-sum question """
    def twoSum(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        hashMap = {}
        for i, v in enumerate(numbers):
            residual = target - v
            if residual in hashMap:
                return hashMap[residual]+1, i+1
            else:
                hashMap[v] = i


class Solution4:
    """ binary search method """
    def twoSum(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        for i in range(len(numbers)):
            lo, hi = i+1, len(numbers)-1
            while lo <= hi:
                mid = lo + (hi - lo) // 2  # 1+(3-1) // 2
                residual = target - numbers[i]
                if numbers[mid] == residual:
                    return i+1, mid+1
                elif numbers[mid] > residual:
                    hi = mid - 1
                else:
                    lo = mid + 1

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))