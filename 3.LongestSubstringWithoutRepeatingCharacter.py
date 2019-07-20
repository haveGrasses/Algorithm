class Solution:
    """ hash保存已出现的字母和它的索引，用两个指针圈定不重复的范围，
    左指针start固定，右指针i循环向后移动，当在start和i圈定的范围内出现了重复元素的时候，
    （在start和i圈定的范围内非常重要，所以在更新start的时候，只有在start <= 重复元素的索引的时候才会更新start，
    当重复元素的索引在start的左边的时候，意味着在目前start和i圈定的范围内是没有重复元素的，次数start不进行更新）
    start移动到重复元素的下一个元素，i继续寻找
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        start, maxLength = 0, 0
        usedChar = {}

        for i in range(len(s)):
            # 什么时候移动左指针，
            if s[i] in usedChar and start <= usedChar[s[i]]:
                #  条件中加 start <= usedChar[s[i]] 是为了不让start后退
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            usedChar[s[i]] = i
        return maxLength


s = Solution()
print(s.lengthOfLongestSubstring('adbccba'))
