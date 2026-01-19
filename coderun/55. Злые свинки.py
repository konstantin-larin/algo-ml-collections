import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    xs = set()
    ans = 0
    for _ in range(n):
        x, y = map(int, input().split())
        if x not in xs:
            ans += 1
            xs.add(x)

    print(ans)


if __name__ == '__main__':
    main()
