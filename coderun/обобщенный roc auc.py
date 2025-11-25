import sys


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)  # 1-based

    def update(self, i, delta=1):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    from bisect import bisect_right
    from math import inf

    def compress_values(values):
        unique_values = sorted(set(values))
        return {val: idx + 1 for idx, val in enumerate(unique_values)}

    n = int(input())
    sorted_by_t = []
    pred_vals = []
    for _ in range(n):
        t, y = map(float, input().split())
        sorted_by_t.append((t, y))
        pred_vals.append(y)
    sorted_by_t.sort()

    auc_denum = 0.0
    for j in range(n):
        i = bisect_right(sorted_by_t, (sorted_by_t[j][0], inf))
        auc_denum += max(n - i, 0)

    compressed_pred_vals = compress_values(pred_vals)
    bit = FenwickTree(len(compressed_pred_vals))

    auc_num = 0.0

    idx = 0

    while idx < n:
        current_a = sorted_by_t[idx][0]
        same_y_trues = []
        while idx < n and current_a == sorted_by_t[idx][0]:
            same_y_trues.append(sorted_by_t[idx])
            idx += 1

        for y_true, y_pred in same_y_trues:
            compressed_value = compressed_pred_vals[y_pred]
            count_less = bit.query(compressed_value - 1)
            count_total = bit.query(compressed_value)
            count_equal = count_total - count_less
            auc_num += count_less + count_equal * 0.5
        for y_true, y_pred in same_y_trues:
            compressed_value = compressed_pred_vals[y_pred]
            bit.update(compressed_value, 1)
    return auc_num / auc_denum


if __name__ == "__main__":
    print(main())
