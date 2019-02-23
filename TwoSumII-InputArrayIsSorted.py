class Solution:
    """ use two pointers """
    def twoSum(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        lo, hi = 0, len(numbers) - 1
        while (numbers[lo] + numbers[hi] != target): 
            if numbers[lo] + numbers[hi]  < target:
                lo = lo + 1
            else:
                hi = hi - 1
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
                hi = hi - 1
            else:
                lo = lo + 1


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
        
solution = Solution()
print('begin')
print(solution.twoSum([2,7,11,15], 9))