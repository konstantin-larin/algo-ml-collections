import sys
import math


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, k = map(int, input().split())
    points = sorted(map(int, input().split()))
    left = 0
    right = math.ceil((points[-1] - points[0]) / k)

    def can(l):        
        count = 0
        i = 0 
        while i < n:
            start = points[i]       
            count += 1
            if count > k:
                return False
            while i < n and points[i] <= start + l:
                i += 1
        
        return True

            
    ans = right
    while left <= right:
        l = (left + right) // 2
        if can(l):
            ans = l
            right = l - 1
        else:
            left = l + 1
    print(ans)
    
if __name__ == '__main__':
    main()
