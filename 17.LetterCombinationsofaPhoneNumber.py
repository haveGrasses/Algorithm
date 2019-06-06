class Solution(object):
    def letterCombinations(self, digits):
        self.mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        if not digits or len(digits) == 0:
            return []
        
        ret = []
        self.combination('', digits, 0, ret)
        
        return ret
    
    def combination(self, alreadyHave, digits, start, ret):
        if start == len(digits):
            ret.append(alreadyHave)
            return
        letters = self.mapping[int(digits[start])]   
        for i in letters:
            # 注意这里不能return
            self.combination(alreadyHave+i, digits, start+1, ret)
