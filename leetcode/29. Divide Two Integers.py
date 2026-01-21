class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if dividend == 0:
            return 0
        if dividend == divisor:
            return 1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        if divisor == 1:
            return dividend
        
        sign = -1 if (dividend < 0) ^ (divisor  < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        ans = 0
        while dividend >= divisor:
            p = 0
            while dividend >= (divisor << p):
                p += 1
            p -= 1
            dividend -= (divisor << p)
            ans += (1 << p)

        return min(
            max(sign * ans, INT_MIN),
            INT_MAX
        )
