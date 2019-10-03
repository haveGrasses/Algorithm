class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        freq = [0] * (length+1)

        # find freq of every citation, bigger than length is viewed as length
        # use freq as a dict, the index is citation number, the value is freqency
        for c in citations:
            if c > length:
                freq[length] += 1
            else:
                freq[c] += 1

        # calculate H-index
        res = 0
        for i in reversed(range(length+1)):
            res += freq[i]
            if res >= i:
                return i
        return 0
