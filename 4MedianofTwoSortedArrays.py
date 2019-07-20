class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # these two lines just make sure that len(nums1) is the shorter one
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)

        # perform binary search on nums1
        start, end = 0, len1

        while start <= end:
            # partitionX and partitionY stands for how many elements in the left partition of nums1 and nums2
            partitionX = (start + end) // 2  
            # the sum of the left partition should equal to half of total length,
            # but plus 1 gives left part one more elements given odd case
            partitionY = (len1 + len2 + 1) // 2 - partitionX  
            
            # edge cases: when left or right part is null, also runs smoothly when nums1 is null or nums2 is null
            leftMaxX = float("-inf") if partitionX == 0 else nums1[partitionX-1]
            lefttMaxY = float("-inf") if partitionY == 0 else nums2[partitionY-1]

            rightMinX = float("inf") if partitionX == len1 else nums1[partitionX]
            rightMinY = float("inf") if partitionY == len2 else nums2[partitionY]

            # leftMax, rightMin = max(leftMaxX, lefttMaxY), min(rightMinX, rightMinY)

            if (leftMaxX <= rightMinY and lefttMaxY <= rightMinX):
                if (len1 + len2) % 2 == 0:  # even case
                    return (max(leftMaxX, lefttMaxY) + min(rightMinX, rightMinY)) / 2
                else:  # odd case (left part has one more elements)
                    return max(leftMaxX, lefttMaxY)
            elif leftMaxX > rightMinY:  # too many on left part, partitionX moves left
                end = partitionX - 1
            else:  # lefttMaxY > rightMinX
                start = partitionX + 1


s = Solution()
print(s.findMedianSortedArrays([], [1]))
