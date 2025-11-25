import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    k = int(input())
    if k == 0:
        return 0
    st = input()
    n = len(st)
    ans = 0
    dp = [0] * n
    for i in range(n - 1, -1, -1):
        if i + k < n and st[i] == st[i + k]:
            dp[i] += dp[i + 1] + 1
        ans += dp[i]

    return ans


if __name__ == "__main__":
    print(main())
