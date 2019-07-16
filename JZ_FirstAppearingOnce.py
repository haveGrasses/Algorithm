class Solution:
    def __init__(self):
        self.cnt = {}  # 统计每个字符出现的次数
        self.queue = []  # 第一个只出现一次的字符候选集，queue的第一个元素即为当前只出现一次的元素
        
    # 返回对应char
    def FirstAppearingOnce(self):
        return self.queue[0] if self.queue else '#'
    
    def Insert(self, char):
        # 哈希统计
        # self.cnt[char] = self.cnt.get(char, 0) + 1  # 一行解决，但不是最好的 其实不需要确切统计每个元素出现的次数，如下所示
        if char in self.cnt:
            self.cnt[char] = 2  #  大于1的直接记为2
        else:
            self.cnt[char] = 1
            
        self.queue.append(char)  # 每插入一个元素都会加入候选队列，可能有重复
        # 用cnt来对候选队列进行修正
        while self.queue and self.cnt[self.queue[0]] > 1:
            self.queue.pop(0)  # 如果觉得pop的复杂度太高 可以用下面这个：
            # self.queue = self.queue[1:]
        # 这一步修正之后queue的第一个元素即是第一个只出现一次的元素
        # 第一个：queue的性质决定的，先来的在前面
        # 只出现一次：cnt保证
