class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        'Let dp(i, j) be the answer for inputs s1[i:] and s2[j:].'
        n1 = len(s1)
        n2 = len(s2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1):
            for j in range(n2):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + ord(s1[i])
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return sum(map(ord, s1)) + sum(map(ord, s2)) - 2* dp[n1][n2]