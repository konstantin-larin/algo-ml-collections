import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    
    n, k = map(int, input().split())
    if k == 0:
        return n
    
    last = n % 10 
    rest = n - last        
    
    while True:
        l = last % 10
        k -= 1   
        last += l             
        if k == 0 or l == 0:
            return rest + last
        if l == 6:
            break
    
    # 2486
    _s = [2, 4, 8, 6]
    whole_sec = (k // 4)        
    rest_sec = k - (whole_sec * 4)    
    last += sum(_s) * whole_sec
    for i in range(rest_sec):
        last += _s[i]

    
    
    
    
    return rest + last
    


if __name__ == '__main__':
    print(main())
