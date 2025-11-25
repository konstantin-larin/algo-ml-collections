import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())    

    dp = [0 for _ in range(max(n, 3))]		
    dp[0] = 1 
    dp[1] = 2
    dp[2] = 4
    for i in range(3, n):
    	dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    return dp[n-1]


if __name__ == '__main__':
    print(main())
