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

            if leftMaxX <= rightMinY and lefttMaxY <= rightMinX:
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


class Solution:
    """ 8.9% """
    def helper(self, nums1, lo1, hi1, nums2, lo2, hi2, k):
        print(f'[in helper], lo1, hi1, lo2, hi2:{lo1, hi1, lo2, hi2},k: {k}')

        if lo1 > hi1:
            return nums2[lo2+k-1]
        elif lo2 > hi2:
            return nums1[lo1+k-1]
        if k == 1:
            return min(nums1[lo1], nums2[lo2])

        i = min(lo1 + k // 2, hi1 + 1)  # +1: i表示的不是索引，是加上几个数字之后的值
        j = min(lo2 + k // 2, hi2 + 1)  # 不是特别明白
        if nums1[i-1] > nums2[j-1]:
            return self.helper(
                nums1, lo1, hi1,
                nums2, j, hi2,
                k-(j-lo2)
            )  # k-(j-lo) 的原因是：前面已经排除了j-lo2个小的数，需要在剩下的大数中找第k-(j-lo2)大
        else:
            return self.helper(
                nums1, i, hi1,
                nums2, lo2, hi2,
                k-(i-lo1)
            )

    # 同样的helper可以找出两个有序数组中的中位数
    def findMedian(self, nums1, nums2):
        # if not nums1:
        #     return (nums2[len(nums2)//2] + nums2[(len(nums2)-1)//2]) / 2  # 奇数和偶数长度都适用的找中位数的方法
        # if not nums2:
        #     return (nums1[len(nums1) // 2] + nums1[(len(nums1)-1) // 2]) / 2

        lo1, hi1, lo2, hi2 = 0, len(nums1)-1, 0, len(nums2)-1
        if (len(nums1) + len(nums2)) % 2 != 0:  # odd
            k = (len(nums1) + len(nums2)) // 2 + 1  # 这里+1是因为中位数找出的位置是索引，而函数的定义中的k是第几小，比索引大1
            print(f'[debug], lo1, hi1, lo2, hi2:{lo1, hi1, lo2, hi2},k: {k}')
            return self.helper(nums1, lo1, hi1, nums2, lo2, hi2, k)
        else:  # even
            k1 = (len(nums1) + len(nums2)) // 2 - 1 + 1
            k2 = (len(nums1) + len(nums2)) // 2 + 1
            print(f'[debug], lo1, hi1, lo2, hi2:{lo1, hi1, lo2, hi2},k: {k1, k2}')
            return (
                self.helper(nums1, lo1, hi1, nums2, lo2, hi2, k1) +
                self.helper(nums1, lo1, hi1, nums2, lo2, hi2, k2)
            ) / 2
