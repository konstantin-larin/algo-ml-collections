import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    turtles = [False] * n
    true = 0
    for _ in range(n):
        a, b = map(int, input().split())
        if a + b == n - 1:
            if not turtles[a]:
                turtles[a] = True
                true += 1
    print(true)




if __name__ == '__main__':
    main()
