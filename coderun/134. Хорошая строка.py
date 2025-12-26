# https://coderun.yandex.ru/problem/good-line
import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    count = 0
    prev = int(input())
    for _ in range(1, n):
        cur = int(input())
        count += min(prev, cur)
        prev = cur
    print(count)



if __name__ == '__main__':
    main()
