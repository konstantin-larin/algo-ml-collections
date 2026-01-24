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
        dp = [[float('inf')] * (n2 + 1) for _ in range(n1 + 1)]
        dp[n1][n2] = 0        


        for i in range(n1 - 1, -1, -1):
            dp[i][n2] = ord(s1[i]) + dp[i + 1][n2]
        for j in range(n2 - 1, -1, -1):
            dp[n1][j] = ord(s2[j]) + dp[n1][j + 1]        
        
        
        
        for i in range(n1 -1, -1, -1):
            for j in range(n2 - 1, -1, -1):                
                dp[i][j] = dp[i][n2] + dp[n1][j] - 2  *  sum(map(ord, set(s1[i:]).intersection(set(s2[j:])))) 
                        
        return dp[0][0]


print(Solution().minimumDeleteSum('leet', 'delete'))

