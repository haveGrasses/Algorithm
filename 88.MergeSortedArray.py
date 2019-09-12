class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        for i in range(m, m+n):
            nums1[i] = nums2[i-m]
        backup = nums1.copy()
        l1, l2 = 0, m
        for i in range(m + n):
            if l1 > m-1:
                nums1[i] = backup[l2]
                l2 += 1
            elif l2 > m + n - 1:
                nums1[i] = backup[l1]
                l1 += 1
            elif backup[l1] < backup[l2]:
                nums1[i] = backup[l1]
                l1 += 1
            else:
                nums1[i] = backup[l2]
                l2 += 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)


class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        上一题的改编版 m和n指的是nums1和nums2的长度，合并需要扩充空间
        这道题和SU_MergeSort的merge部分一样，只是一定要注意索引的小细节！这里m和n都是长度
        1. l1, l2 = 0, m：l2是从m开始的；
        2. for i in range(m + n)：循环到的最大的索引是m+n-1
        3. if l1 > m-1： l1的上限是m-1
        4. l2 > m + n - 1: l2的上限是 m + n - 1
        """
        nums1.extend(nums2)
        backup = nums1.copy()
        l1, l2 = 0, m
        for i in range(m + n):
            if l1 > m-1:
                nums1[i] = backup[l2]
                l2 += 1
            elif l2 > m + n - 1:
                nums1[i] = backup[l1]
                l1 += 1
            elif backup[l1] < backup[l2]:
                nums1[i] = backup[l1]
                l1 += 1
            else:
                nums1[i] = backup[l2]
                l2 += 1


nums1 = [1, 2, 5, 9, 10]
nums2 = [1, 3, 4, 8, 9, 11]
Solution().merge(nums1, len(nums1), nums2, len(nums2))
print(nums1)
