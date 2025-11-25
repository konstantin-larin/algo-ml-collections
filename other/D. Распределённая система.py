# оптимизация по максимуму!!!!!!!!!!!!!!!!!!!!!!!
import sys
import numpy as np

input = sys.stdin.read
data = input().split()

index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
start_r = int(data[index]) - 1
index += 1
start_c = int(data[index]) - 1
index += 1
start = np.array([start_r, start_c])

grid = data[index:index + n]
index += n
s = data[index]


pos = {}
for r in range(n):
    row = grid[r]
    for c in range(m):
        ch = row[c]
        if ch not in pos:
            pos[ch] = []
        pos[ch].append([r, c])

for ch in pos:
    pos[ch] = np.array(pos[ch], dtype=np.int16)


dp = np.sum(np.abs(pos[s[0]] - start), axis=1)

memo = {}

for i in range(1, len(s)):
    prev_ch = s[i-1]
    cur_ch = s[i]
    
    if prev_ch == cur_ch:
        continue

    key = (prev_ch, cur_ch)
    if key not in memo:
        prev = pos[prev_ch]
        cur = pos[cur_ch]
        diff = prev[:, np.newaxis, :] - cur[np.newaxis, :, :]
        distances = np.abs(diff).sum(axis=2)
        memo[key] = distances

    distances = memo[key]
    
    new_dp = distances + dp[:, None]
    dp = new_dp.min(axis=0)

print(int(dp.min()))