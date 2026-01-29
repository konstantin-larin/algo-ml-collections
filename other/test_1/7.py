# есть шахматная доска n на n
# Анечка получила k слонов 
# сколько же она может расставить слонов, которые не бьют друг друга на доске?
# это вопрос про сколько диагоналей есть в квадрате n на n?
# я вот только не понял а k каких слонов черных или белых?
# это важно такто...
# а, ну и тут не только про "можно ли" а еще и в смысле сколько перестановок из k слонов можно сделать
# ну смотри, если цвет тут не важен, то значит по идее (кол-во диагоналей)! % 10**9 + 7 будет ответом
# точнее C(кол-во диагоналей, k)
import math
n, k = map(int, input().split())
MOD = 10 ** 9 + 7
# all_lines = 2 * n - 1
# if k > all_lines:
#     print(0)
# else:
#     print(math.comb(2 * n - 1, k) % MOD)
# ну это не совсем правильно - я не учел, что мы можем поставить слона на любую из клеток, а случай выше этого не учитывал
if k > 2 * n - 1:
    print(0)
else:
    # генерируем длины диагоналей для черных и белых клеток
    # n = 5, white: [1, 1, 3, 3, 5], black: [2, 2, 4, 4]    
    white_cells = []
    black_cells = []        
    for i in range(1, n + 1):
        if i % 2 != 0:
            white_cells.append(i)
            if i < n: white_cells.append(i)
        else:
            black_cells.append(i)
            if i < n: black_cells.append(i)
            
    def get_dp(cells):
        # dp[i][j] - количество способов расставить j слонов на первых i диагоналях
        m = len(cells)
        dp = [[0] * (k + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1
                
        for i in range(1, m + 1):
            length = cells[i-1]
            for j in range(1, k + 1):
                # мы можем не ставить слона на эту диагональ, а можем поставить и тогда будет доступно length - (j - 1) позиций
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1] * (length - (j - 1))
        return dp[m]
    
    ways_white = get_dp(white_cells)
    ways_black = get_dp(black_cells)

    # комбинируем получившиеся расчеты, получая число всевозможных вариантов
    ans = 0
    for i in range(k + 1):
        ans += ways_white[i] * ways_black[k - i]
            
    print(ans % MOD)
