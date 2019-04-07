class Solution(object):
    """ 44.28% """
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set = set(nums1)
        
        res = []
        for i in nums2:
            if i in nums1_set:
                res.append(i)
                nums1_set.remove(i)
        return res
                
