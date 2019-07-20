class Solution:
    def kthElement(self, nums1, nums2, k):
        if k < 1 or k > (len(nums1) + len(nums2)):
            return None
        lo1, hi1, lo2, hi2 = 0, len(nums1) - 1, 0, len(nums2) - 1
        return self.helper(nums1, lo1, hi1, nums2, lo2, hi2, k)

    def helper(self, nums1, lo1, hi1, nums2, lo2, hi2, k):
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


s = Solution()
nums1 = [1, 2, 8, 11]
nums2 = [4, 6, 9, 10, 16]
k = 5
print(s.kthElement(nums1, nums2, k))
# print(sorted(nums1+nums2))
# print(sorted(nums1+nums2)[k-1])

