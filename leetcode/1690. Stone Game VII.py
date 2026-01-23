class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]
        def get_sum(l, r):
            return prefix[r + 1] - prefix[l]
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                left = get_sum(l + 1, r) - dp[l + 1][r]
                right = get_sum(l, r - 1) - dp[l][r - 1]

                dp[l][r] = max(left, right)
        return dp[0][n - 1]

print(Solution().stoneGameVII([7,90,5,1,100,10,10,2]))