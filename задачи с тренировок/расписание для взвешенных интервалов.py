import sys
from bisect import bisect_right

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    N = int(input())
    intervals = [tuple(map(float, input().split())) for _ in range(N)]

    # сортируем по концу
    intervals.sort(key=lambda x: x[1])
    ends = [e for _, e, _ in intervals]

    dp = [0] * (N + 1)

    # предвычисляем p[i]
    p = [0] * N
    for i in range(N):
        b_i = intervals[i][0]
        # ищем индекс j такого, что intervals[j].end <= b_i
        j = bisect_right(ends, b_i) - 1
        p[i] = j

    for i in range(1, N + 1):
        dp[i] = max(dp[i-1], intervals[i-1][2] + (dp[p[i-1]+1] if p[i-1] != -1 else 0))

    return dp[N]



if __name__ == '__main__':
    print(main())


