from collections import deque, defaultdict
def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, m = map(int, input().split())
    k = int(n / m)
    slices_map = defaultdict(deque)    

    s = input()
    for i in range(0, n, k):
        slices_map[s[i:i+k]].append(int(i / k))    

    ans = [-1] * m    
    for pos in range(1, m + 1):
        slice_ = input()        
        index = slices_map[slice_].popleft()
        ans[index] = str(pos)        
    return ans
    


if __name__ == '__main__':
    ans = main()
    print(" ".join(ans))
