import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    # чет +, нечет - ищем минимальный чет и максимальный нечет и если 1 < 2, то меняем
    n = int(input())
    mushrooms = list(map(int, input().split()))
    min_chet = float("inf")
    max_nechet = -float("inf")

    s = 0
    for i in range(0, n, 2):
        if mushrooms[i] < min_chet:
            min_chet = mushrooms[i]
        s += mushrooms[i]
    for i in range(1, n, 2):
        if mushrooms[i] > max_nechet:
            max_nechet = mushrooms[i]
        s -= mushrooms[i]
    if min_chet < max_nechet:
        s = s + 2 * (max_nechet - min_chet)
    return s


if __name__ == "__main__":
    print(main())
