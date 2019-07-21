class Solution:
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

    # 找第k小的数字
    def kthElement(self, nums1, nums2, k):
        if k < 1 or k > (len(nums1) + len(nums2)):
            return None
        lo1, hi1, lo2, hi2 = 0, len(nums1) - 1, 0, len(nums2) - 1
        return self.helper(nums1, lo1, hi1, nums2, lo2, hi2, k)

    # 同样的helper可以找出两个有序数组中的中位数
    def findMedian(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        lo1, hi1, lo2, hi2 = 0, n1-1, 0, n2-1
        # 奇数和偶数长度都适用的找中位数的方法, (n1 + n2) // 2 索引对应的数和 (n1 + n2 - 1) // 2 对应的数取平均
        # 如果是奇数，这两个索引是一样的，如果是偶数是一前一后不一样的
        k1 = (n1 + n2) // 2 + 1  # 这里在索引的基础上加1转换为函数定义中的第k小的位置
        k2 = (n1 + n2 - 1) // 2 + 1
        m1 = self.helper(nums1, lo1, hi1, nums2, lo2, hi2, k1)
        m2 = self.helper(nums1, lo1, hi1, nums2, lo2, hi2, k2)
        return (m1 + m2) / 2


s = Solution()
nums1 = [1, 2, 8, 11]
nums2 = [4, 6, 9, 10, 16]
k = 5
print(s.kthElement(nums1, nums2, k))
print(sorted(nums1+nums2))
print(sorted(nums1+nums2)[k-1])
nums1, nums2 = [1, 3], [2]
print(s.findMedian(nums1, nums2))
