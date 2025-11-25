import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * m for _ in range(n)]
    prev = [[''] * m for _ in range(n)]

    dp[0][0] = a[0][0]

    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + a[i][0]
        prev[i][0] = 'D'
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + a[0][j]
        prev[0][j] = 'R'
    for i in range(1, n):
        for j in range(1, m):
            if dp[i - 1][j] > dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j] + a[i][j]
                prev[i][j] = 'D'
            else:
                dp[i][j] = dp[i][j - 1] + a[i][j]
                prev[i][j] = 'R'
    i, j = n -1, m - 1
    path = []    
    while i >= 0 and j >= 0:
        if i == 0 and j == 0:
            break
        path.append(prev[i][j])        
        if prev[i][j] == 'D':
            i -= 1
        else:
            j -= 1
    
    print(dp[n - 1][m - 1])
    print(" ".join(reversed(path)))

if __name__ == '__main__':
    main()
