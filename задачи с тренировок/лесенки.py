import sys

def main():
    n = int(sys.stdin.readline().strip())
    dp = [0] * (n + 1)
    dp[0] = 1
    # перебираем возможные размеры уровней (каждый можно взять не более 1 раза)
    for k in range(1, n + 1):
        for s in range(n, k - 1, -1):
            dp[s] += dp[s - k]
    print(dp[n])

if __name__ == "__main__":
    main()
