from collections import defaultdict, deque
import numpy as np

n, m = map(int, input().split())
start_point = np.array(list(map(lambda x: int(x) - 1, input().split())))
grid = []

for _ in range(n):
    grid.append(input())
s = input()

pos = defaultdict(list)

for r in range(n):
    for c in range(m):
        ch = grid[r][c]
        pos[ch].append(np.array((r, c)))
for ch in pos:
    pos[ch] = np.array(pos[ch])
# dp[i][idx] = min время после взятия s[i-1] в позиции pos[s[i-1]][idx]

dp = np.sum(np.abs(pos[s[0]] - start_point), axis=1)
# для запоминания расстояний между каждой точкой множества prev_letter и каждой точкой множества cur_letter
memo = {}

 
for i in range(1, len(s)):
    cur_letter = s[i]
    prev_letter = s[i - 1]    
    if prev_letter == cur_letter:
        continue
    if (prev_letter, cur_letter) in memo:
        distances_between = memo[(prev_letter, cur_letter)]
    else:
        # считаем расстояния между точками множества prev_letter и cur_letter
        prev_pos = pos[prev_letter]
        cur_pos = pos[cur_letter]                
        distances_between = np.sum(
            np.abs(prev_pos[:, np.newaxis, :] - cur_pos[np.newaxis, :, :]), axis=2
        )

        memo[(prev_letter, cur_letter)] = distances_between

    
    dp = np.min(distances_between + dp.reshape(-1, 1), axis=0) # len(prev_pos) возможных векторов стоимостей - выбираем оптимальный из них после сложения предыдущих стоимостей

print(int(min(dp)))