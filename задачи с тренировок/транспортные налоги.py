import sys
from bisect import bisect_right

sys.setrecursionlimit(2000)

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """    
    n = int(input())    
    B = []
    T = []
    
    for _ in range(n):        
        b, t = map(int, input().split())
        B.append(b)
        T.append(t)        
    
    m = int(input())    
        
    for _ in range(m):
        q = int(input())                
        rate_index = bisect_right(B, q - 1) - 1
        tax_rate = T[rate_index]

        tax = tax_rate * q
        print(tax)    

main()