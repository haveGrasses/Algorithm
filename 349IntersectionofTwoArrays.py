class Solution(object):
    """ 81% """
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
    
    # same as:
    class Solution(object):
    def intersection(self, nums1, nums2):
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        return list(nums1_set.intersection(nums2_set))  # make sure the return is a list in py3
                
    
    # a one line solution
    def intersection(self, nums1, nums2):
        """ 81% """
        return list(set(nums1) & set(nums2))
    
