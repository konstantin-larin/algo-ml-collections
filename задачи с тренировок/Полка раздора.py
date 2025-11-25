import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    _a, _b, S = map(int, input().split())
    # L - (_a + _b)L + (_a*_b - S) = 0
    a = 1 
    b = -1 * (_a + _b)
    c = _a * _b - S
    
    D = b ** 2 - 4 * a * c
    
    if D < 0:
        return -1
    d = D ** 0.5
    
    if int(d) != d:
        # только целое число
        return -1  
    d = int(d)
      
    L1 = (-b + d) / (2 * a)
    L2 = (-b - d) / (2 * a)

    not_L1 = L1 < 1 or int(L1) != L1
    not_L2 = L2 < 1 or int(L2) != L2
    
    if not_L1 and not_L2:
        return -1
    if not_L1:
        return int(L2)
    if not_L2:
        return int(L1)    
    return int(max(L1, L2))


if __name__ == '__main__':
    print(main())
