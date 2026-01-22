class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0:
            return ""
        start_i = 0
        max_length = 1
        dp = [[False] * n for _ in range(n)]        
        for i in range(n):
            dp[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                    
                    if dp[i][j] and length > max_length:
                        start_i = i
                        max_length = length
        return s[start_i:start_i + max_length]
                
sol = Solution()
print(sol.longestPalindrome('cbbd'))