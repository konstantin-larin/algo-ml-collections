import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    x, y = map(int, input().split())
    f, g = map(int, input().split())

    dx = abs(x - f)
    dy = abs(y - g)

    if dx == 0 and dy == 0:
        return 0
    else:
        total = dx + dy
        if min(dx, dy) >= 1:
            return 3 * total - 5
        else:
            return 3 * total - 3 




if __name__ == '__main__':
    print(main())
