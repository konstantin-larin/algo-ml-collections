import sys
from collections import Counter

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    st = input()
    total = len(st)
    c = Counter(st)
    ck = list(c.keys())
    ans = 1
    for i in range(len(c) - 1):
        n = c[ck[i]]        
        total -= n     
        ans += n * total
        
    return ans


if __name__ == '__main__':
    print(main())
