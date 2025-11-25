import sys
import math

def main():
    N, L = map(int, input().split())
    shops = [tuple(map(int, input().split())) for _ in range(N)]

    MAX = 100
    dp = [math.inf] * (MAX + 1)
    dp[0] = 0
    choice = [[0] * (MAX + 1) for _ in range(N + 1)]

    for i, (P, R, Q, F) in enumerate(shops, 1):
        cost = [0] * (F + 1)
        discount_is_available = R <= F
        for x in range(1, F + 1):
            if x >= R and discount_is_available:
                cost[x] = x * Q
            else:
                cost[x] = x * P

        new_dp = list(dp)
        for have in range(MAX + 1):
            if dp[have] < math.inf:
                for buy in range(1, F + 1):
                    if have + buy <= MAX and new_dp[have + buy] > dp[have] + cost[buy]:
                        new_dp[have + buy] = dp[have] + cost[buy]
                        choice[i][have + buy] = buy
        dp = new_dp

    # найти минимальную стоимость для >= L
    min_cost = math.inf
    best_k = -1
    for k in range(L, MAX + 1):
        if dp[k] < min_cost:
            min_cost = dp[k]
            best_k = k

    if min_cost == math.inf:
        print(-1)
        return

    print(min_cost)

    # восстановление решения
    res = ['0'] * N
    cur = best_k
    for i in range(N, 0, -1):
        buy = choice[i][cur]
        res[i - 1] = str(buy)        
        cur -= buy

    print(" ".join(res))


        


if __name__ == '__main__':
    main()
