# https://coderun.yandex.ru/problem/lite-operating-systems
import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    m = int(input())
    n = int(input())    
    intervals = []    
    for _ in range(n):
        a, b = map(int, input().split())        
        new_intervals = [[a, b]]
        for interval in intervals:
            c, d = interval            
            if max(a, c) > min(b, d):
                new_intervals.append(interval)
        intervals = new_intervals

                
    print(len(intervals))

    



if __name__ == '__main__':
    main()
