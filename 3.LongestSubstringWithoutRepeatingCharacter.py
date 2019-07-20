class Solution1:
    """ hash保存已出现的字母和它的索引，用两个指针圈定不重复的范围，
    左指针start固定，右指针i循环向后移动，当在start和i圈定的范围内出现了重复元素的时候，
    （在start和i圈定的范围内非常重要，所以在更新start的时候，只有在start <= 重复元素的索引的时候才会更新start，
    当重复元素的索引在start的左边的时候，意味着在目前start和i圈定的范围内是没有重复元素的，次数start不进行更新）
    start移动到重复元素的下一个元素，i继续寻找
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start, maxLength = 0, 0
        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:  #  条件中加 start <= usedChar[s[i]] 是为了不让start后退
                start = used[s[i]] + 1
            else:  # 写不写这个else是一样的，
                # 原因是当start更新后这个maxLength在start进行更新的时候肯定是小于原来的maxLength
                # 写个else可以避免不必要的更新操作
                maxLength = max(maxLength, i-start+1)
            used[s[i]] = i
            print(f'i={i}, s[i]={s[i]}, start={start}, maxLength={maxLength}, used[s[i]]={used[s[i]]}')
        return maxLength


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start, maxLength = 0, 0
        for i in range(len(s)):
            # 当然这里这个if也可以写成这样：
            if s[i] in used:
                start = max(start, used[s[i]] + 1)
            else:
                maxLength = max(maxLength, i-start+1)  # 但是这里不同于解法1，不能写else
                # 原因是if进去的时候，start有可能更新了，有可能没有更新，
                # 在没有更新的情况下由于i增加了，maxLength肯定是增加的，需要进行更新
            used[s[i]] = i

        return maxLength


s1 = Solution1()
print(s1.lengthOfLongestSubstring("tmmzuxt"))
s2 = Solution()
print(s2.lengthOfLongestSubstring("tmmzuxt"))
