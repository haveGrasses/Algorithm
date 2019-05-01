class Solution(object):
    """ iterative method  """
    def consecutiveNumbersSum(self, N):
        ret = []
        start, end, curSum = 1, 2, 3
        while start < end:  # why this condition
            if curSum > N:
                curSum -= start
                start += 1
            else:  # curSum <= N 
                if curSum == N:  # a solution 
                    ret.append([i for i in range(start, end+1)])
                # curSum < N, curSum == N
                end += 1
                curSum += end
                
        return ret
    
    def consecutiveNumbersSum2(self, N):
        ret = []
        start, end, curSum = 1, 2, 3
        while start < end:  # why this condition
            if curSum > N:
                curSum -= start
                start += 1
            elif curSum < N:  
                end += 1
                curSum += end
            else:
                ret.append([i for i in range(start, end+1)])
                curSum -= start  # these two line will save time, why 
                start += 1
                end += 1
                curSum += end
                
        return ret
            
        
s = Solution()
print(s.consecutiveNumbersSum(100))
print(s.consecutiveNumbersSum(100))



class Solution(object):
    def consecutiveNumbersSum(self, N):
        # LC: time out
        # JZ: pass
        ret = 1
        start, end, curSum = 1, 2, 3
        while start < end:  # why this condition
            if curSum > N:
                curSum -= start
                start += 1
            else:  # curSum <= N 
                if curSum == N:  # a solution 
                    ret += 1
                # curSum < N, curSum == N
                end += 1
                curSum += end
        # return len(ret) + 1  # for leetCode
        return ret
    
    def consecutiveNumbersSum2(self, N):
        # LC: time out
        # JZ: pass
        ret = 1
        start, end, curSum = 1, 2, 3
        while start < end:  # why this condition
            if curSum > N:
                curSum -= start
                start += 1
            elif curSum < N:  
                end += 1
                curSum += end
            else:
                ret += 1  # find one answer
                curSum -= start  # these two line will save time, why 
                start += 1
                end += 1
                curSum += end
                
        return ret
    
    def consecutiveNumbersSum3(self, N):
        # LC: time out
        ans = 0  # attention: ans begins with 0, below already have num N itself into consideration
        for i in range(1, N+1):  # actually, no need to loop to N, but N is the upper bound, with break in for loop, no need to know the actual bound
            xi = N - i * (i-1) / 2
            if xi <= 0:
                return ans
            if xi % i == 0:
                ans += 1
        return ans
    
    def consecutiveNumbersSum4(self, N):
        # LC: 33%, why use while would be faster than for ???
        i, ans = 1, 0
        while True:
            xi = (N - i*(i-1)/2)
            if xi <= 0:
                break
            if xi % i == 0:
                ans += 1
            i += 1
        return ans
            
                 
s = Solution()
print(s.consecutiveNumbersSum(9366964))
print(s.consecutiveNumbersSum2(9366964))
print(s.consecutiveNumbersSum3(9366964))

