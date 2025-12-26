# https://coderun.yandex.ru/problem/sum-of-numbers
import sys
import pdb

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))    

    l = 0
    c=0
    tmp_sum = 0

    for r in range(n):
        tmp_sum += arr[r]

        while tmp_sum >= k:
            if tmp_sum == k:
                c += 1
            tmp_sum -= arr[l]
            l += 1
    
    print(c)


if __name__ == '__main__':
    main()
