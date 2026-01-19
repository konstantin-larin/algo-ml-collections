import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    arr = sorted(map(int, input().split()))
    dp = [float('inf')] * n     
    dp[1] = arr[1] - arr[0]
    
    for i in range(2, n):
        l = arr[i] - arr[i - 1]
        dp[i] = min(
            dp[i - 1],
            dp[i - 2]
        ) + l
    print(dp[n - 1])


if __name__ == '__main__':
    main()
