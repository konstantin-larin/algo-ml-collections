import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    max_k = 0
    pricelist = [0] * n
    MAX_BILL = 0   
    INF = float('inf')

    for i in range(n):
        c = int(input())
        MAX_BILL += c
        if c > 100:
            max_k += 1
        pricelist[i] = c
    dp = [[INF] * (max_k + 1) for _ in range(n + 1)]
    k_history = [[None] * (max_k + 1) for _ in range(n + 1)] # (сколько было купонов вчера, потрачен ли был купон сегодня или нет )
    dp[0][0] = 0
    for i in range(n):
        price = pricelist[i]
        for k in range(max_k + 1):
            if dp[i][k] < INF:                
                # вариант 1 - платим деньги
                new_k = k + 1 if price > 100 else k                
                new_cost = dp[i][k] + price
                if new_cost <= dp[i + 1][new_k]:
                    dp[i + 1][new_k] = new_cost
                    k_history[i + 1][new_k] = (k, False)                                
                # вариант 2 - используем купон 
                if k > 0:
                    if dp[i][k] <= dp[i + 1][k - 1]:
                        dp[i + 1][k - 1] = dp[i][k]
                        k_history[i + 1][k - 1] = (k, True)
    min_bill = MAX_BILL
    k1 = 0
    for k, bill in enumerate(dp[n]):
        if bill <= min_bill:
            min_bill = bill
            k1 = k
    
    free_days = []
    cur_k = k1
    k2 = 0

    for day in range(n, 0, -1):
        prev_k, used_coupon = k_history[day][cur_k]
        if used_coupon:
            free_days.append(day)
            k2 += 1
        cur_k = prev_k
    free_days.reverse()

    print(min_bill)
    print(k1, k2)
    for day in free_days:
        print(day)


if __name__ == '__main__':
    main()
