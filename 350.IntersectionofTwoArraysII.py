class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1_set = {}
        for i in nums1:
            if i not in nums1_set:
                nums1_set[i] = 1
            else:
                nums1_set[i] += 1
        
        res = []
        for i in nums2:
            if i in nums1_set:
                res.append(i)
                nums1_set[i] -= 1
                if nums1_set[i] == 0:
                    del nums1_set[i]
        
        return res
                
        
       
