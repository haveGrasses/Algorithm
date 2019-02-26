class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        id = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                id += 1
                nums[id] = nums[i]
        return id+1
               
        
        