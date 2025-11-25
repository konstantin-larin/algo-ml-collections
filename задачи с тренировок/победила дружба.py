import sys

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    a = list(map(int, input().split()))

    p_l = [0] * (n + 1) # левые префиксные суммы
    current_sum = 0

    for i in range(n):
        current_sum += a[i]
        p_l[i + 1] = current_sum

    p_r = [0] * (n + 2) #правые
    current_sum = 0
    for i in range(n-1, -1, -1):        
        current_sum += a[i]
        p_r[i + 1] = current_sum
    

    l = 1
    r = n

    min_diff = abs(p_l[l] - p_r[r])
    best_l = l
    best_r = r

    while l < r:        
        SD_V = p_l[l] 
        SD_M = p_r[r]
        diff = abs(SD_V - SD_M) 
        if diff < min_diff:
            min_diff = diff
            best_l = l
            best_r = r

        if SD_V < SD_M:
            l += 1
        else:
            r -= 1
    print(min_diff, best_l, best_r)

        
    


if __name__ == '__main__':
    main()