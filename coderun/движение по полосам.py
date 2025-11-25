import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    m, n = map(int, input().split())

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    dp[1][1] = 1
    for i in range(1, n + 1):
        if i == 1:
            start = 2
        else:
            start = 1

        for j in range(start, m + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j] + dp[i - 1][j - 1]

    return dp[n][m]


if __name__ == "__main__":
    print(main())
