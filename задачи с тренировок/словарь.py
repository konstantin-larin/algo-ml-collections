import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    s = input()    
    # len(s) <= 100
    # по идее 
    n = len(s)
    m = int(input())
    words = []
    for _ in range(m):
        words.append(input())
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] != -1 and s[j:i] in words:
                dp[i] = j
                break
    print(dp)
    parts = []

    i = n
    while i > 0:
        j = dp[i]
        parts.append(s[j:i])
        i = j
    return " ".join(reversed(parts))



if __name__ == '__main__':
    print(main())
