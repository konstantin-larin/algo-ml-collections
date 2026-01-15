import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    proportion_classes = set()
    n = int(input())
    for _ in range(n):
        a, b, c = sorted(map(int, input().split()))
        proportion_classes.add((b/a, c/b, c/a))
    print(len(proportion_classes))





if __name__ == '__main__':
    main()
