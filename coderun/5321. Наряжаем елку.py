# https://coderun.yandex.ru/problem/decorating-tree
import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    s = 1
    k = int(input())
    ss = 1

    for _ in range(1,k):
        ss *= 2 
        s += ss
    print(s)


if __name__ == '__main__':
    main()

