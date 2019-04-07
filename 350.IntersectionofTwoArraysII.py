class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # save element in nums1 into a map, the key is the element, value is times
        # then traverse elements in nums2, if it in map, record the intersections, 
        # decreasing times in map accordingly, this is very important.
        
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
    
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ two pointer solution 
        when nums1 and nums2 are very large, it is not impossible to make a set of them,
        so we use two pointer to compare elements in them and record the intersections
        """
        # sort
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        # traverse and  compare
        i1, i2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        res = []
        while i1 < n1 and i2 < n2:
            if nums1[i1] == nums2[i2]:
                res.append(nums1[i1])
                i1 += 1
                i2 += 1
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            else:  # nums1[i1] < nums2[i2]
                i1 += 1
        
        return res
    
