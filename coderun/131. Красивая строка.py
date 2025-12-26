# https://coderun.yandex.ru/problem/beautiful-line

import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    k = int(input())
    s = input()
    n = len(s)
    ans = 1
        
    for ch in set(s):        
        l = 0
        bad = 0
        for r in range(n):
            if s[r] != ch:
                bad += 1
            while bad > k:
                if s[l] != ch:
                    bad -= 1
                l += 1
            ans = max(ans, r - l + 1)
    print(ans)

if __name__ == '__main__':
    main()