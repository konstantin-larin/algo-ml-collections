import sys
from collections import Counter


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, k = map(int, input().split())
    c = Counter(list(map(int, input().split())))
    c_k = list(c.keys())
    ans = []    
    if k <= len(c):        
        for i in range(k):            
            ans.append(str(c_k[i]))
    else:
        while True:            
            for i in range(len(c)):
                if c[c_k[i]] > 0:                    
                    c[c_k[i]] -= 1
                    ans.append(str(c_k[i]))
                
                if len(ans) == k:
                    return ans
        
    
    return ans


if __name__ == '__main__':
    ans = main()
    print(' '.join(ans))