# To apply DP, we define the state dp[i][j] to be the minimum number of
# operations to convert word1[0..i) to word2[0..j).

# For the base case, that is, to convert a string to an empty string,
# the mininum number of operations (deletions) is just the length of the string.
# So we have dp[i][0] = i and dp[0][j] = j.
class Solution:
    def minDistance(self, word1: str, word2: str):
        m, n = len(word1), len(word2)
        # the minimum number of operations to convert word1[0..i) to word2[0..j)
        dp = [[float('inf') for _ in range(n+1)] for _ in range(m+1)]
        # initialize, for empty str, operations equals to length of word
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                # match, no operation needed
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i-1][j] + 1,  # word1[0..i - 1) = word2[0..j), delete word1[i-1]
                        dp[i][j-1] + 1,  # word1[0..i) + word2[j - 1] = word2[0..j), insert word2[j - 1] to word1[0..i)
                        dp[i-1][j-1] + 1  # replace the i-1th element
                    )
        return dp[m][n]
