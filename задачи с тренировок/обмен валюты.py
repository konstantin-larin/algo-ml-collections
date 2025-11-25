import sys
import bisect

def main():
    n, p = map(int, input().split())
    c = list(map(int, input().split()))

    arr = sorted((val, idx) for idx, val in enumerate(c))

    best_diff = float('inf')
    best_i = -1
    best_j = -1

    for j in range(n):
        cj, jidx = arr[j]
        target = p * cj

        # бинарный поиск ближайшего ci к target
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            ci, iidx = arr[mid]
            if ci == target:
                left = mid
                break
            elif ci < target:
                left = mid + 1
            else:
                right = mid - 1

        # проверяем соседей: mid и mid-1
        for k in [left, left-1]:
            if 0 <= k < n:
                ci, iidx = arr[k]
                if iidx == jidx:
                    continue
                diff = abs(ci / cj - p)
                if diff < best_diff:
                    best_diff = diff
                    best_i, best_j = iidx, jidx

    print(best_i + 1, best_j + 1)


if __name__ == '__main__':
    main()
