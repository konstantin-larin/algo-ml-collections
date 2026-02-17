from bisect import bisect_left
# для каждого из чисел второй последовательности найти ближайшее к нему в первой
n, k = map(int, input().split()) # > 0,  <= 10^5
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
# O(k logn)? 
arr1.sort()
for num in arr2:
    i = bisect_left(arr1, num)
    diff1 = abs(num - arr1[i]) if i < n else float('inf')
    diff2 = abs(num - arr1[i - 1]) if i > 0 else float('inf')    
    print(arr1[i] if diff1 < diff2 else arr1[i - 1])