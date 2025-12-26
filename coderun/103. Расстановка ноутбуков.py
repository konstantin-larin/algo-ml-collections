# https://coderun.yandex.ru/problem/arrangement-laptops
import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    a1, b1, a2, b2 = map(int, input().split())
    options = [
    (a1 + a2, max(b1, b2)),
    (a1 + b2, max(b1, a2)),
    (b1 + a2, max(a1, b2)),
    (b1 + b2, max(a1, a2))
    ]

    best = options[0]
    cur_s = best[0] * best[1]
    for opt in options[1:]:        
        s = opt[0] * opt[1]
        if s < cur_s:
            best = opt
            cur_s = s
    print(best[0], best[1])


if __name__ == '__main__':
    main()