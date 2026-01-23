class Solution(object):
    def countTexts(self, pressedKeys):
        """
        :type pressedKeys: str
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(pressedKeys)
        dp = [0] * (n + 1)
        dp[0] = 1
        four_letters = {'7', '9'}
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            limit = 4 if pressedKeys[i - 1] in four_letters else 3
            for j in range(2, limit + 1):
                if i - j >= 0 and pressedKeys[i - 1] == pressedKeys[i - j]:
                    dp[i] = (dp[i] + dp[i - j]) % MOD
                else:
                    break
        return dp[n]
    
print(Solution().countTexts('2222'))
        
