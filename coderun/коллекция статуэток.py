import sys
from collections import Counter, deque


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    if k == 1:
        # не нужно проверять есть ли такой вид в nums, так как по условию сказано, что решение существует
        return 1

    # right_range = range(1, k + 1)
    tmp_c = Counter()
    min_sum = sum(nums)
    unique_count = 0
    queue = deque([])

    l = 0
    tmp_sum = nums[0]
    for i in range(n):
        num = nums[i]
        if (
            num <= k
        ):  # по условию задачи гарантируется, что это условие выполнимо хотя бы раз
            # такое число подходит по условиям, учитываем его
            tmp_c[num] += 1
            tmp_sum = num
            unique_count += 1
            l = i  # это будет стартовая точка
            break
    r = l + 1

    while r < n:
        num = nums[r]
        tmp_sum += num
        if num <= k:
            queue.append(r)
            tmp_c[num] += 1
            if tmp_c[num] == 1:
                unique_count += 1
            while unique_count >= k:
                min_sum = min(min_sum, tmp_sum)
                old_l = l
                new_l = queue.popleft()
                tmp_sum -= sum(nums[old_l:new_l])
                num = nums[old_l]
                tmp_c[num] -= 1
                l = new_l
                if tmp_c[num] == 0:
                    unique_count -= 1
        r += 1
    return min_sum


if __name__ == "__main__":
    print(main())
