class Solution:
    def summaryRanges(self, nums):
        ranges = []  # save range list
        for num in nums:
            if not ranges or num > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = num,   # pay attention to ',', it assign the slides a, iterable
            # ranges[-1][-1], ranges[-1][-1:] does not throw index error when ranges[-1] is a null list
        return ['->'.join(map(str, r)) for r in ranges]
