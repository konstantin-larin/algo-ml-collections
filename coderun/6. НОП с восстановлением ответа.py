import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    A = [0] + list(map(int, input().split()))
    m = int(input())
    B = [0] + list(map(int, input().split()))
    
    dp = [
        [0] * (m + 1) for _ in range(n + 1)        
    ]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i] == B[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j-1])
    i = n
    j = m
    seq = []
    while i > 0 and j > 0:
        if A[i] == B[j]:
            seq.append(A[i])
            i -= 1
            j -= 1            
        else:
            if dp[i-1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
    seq.reverse()
    print(*seq)

if __name__ == '__main__':
    main()
