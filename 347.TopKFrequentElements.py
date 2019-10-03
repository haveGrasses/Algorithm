class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        bucket = [[] for _ in range(len(nums)+1)]
        for key, val in dict.items():
            bucket[val].append(key)
        # bucket: [[], [3], [2], [1], [], [], []]
        # 索引是次数，值是对应的数字

        ret = []
        for row in reversed(bucket):
            if not row:
                continue
            else:
                # 这里为什么还要遍历呢：不同次数对应的数字会有多个
                for i in range(len(row)):
                    ret.append(row[0])
                    if len(ret) == k:
                        return ret


class Solution2(object):
    def topKFrequent(self, nums, k):
        
        # calculate frequency for each num
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # exchange value and key in freq (convert to bucket)
        bucket = [[] for _ in range(len(nums))]
        for i, v in freq.items():
            bucket[v-1].append(i)
        # 对bucket的改进：索引是出现次数-1，下面的循环中就不用再对是否为空进行判断了
        # 用索引来表示次数，实际上省掉了需要对次数进行排序这一步骤，索引本身是有序的

        # find top k
        ret = []
        for i in reversed(range(len(bucket))):
            ret.extend(bucket[i])
            if len(ret) >= k:
                return ret[:k]
        return ret

# need update: Solution3, use heap rather than bucket to find topk


s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))
