import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    triangle = []
    for _ in range(3):
        triangle.append(int(input()))
    a, b, c =  triangle
    if a + b > c and a + c > b and b + c > a:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
