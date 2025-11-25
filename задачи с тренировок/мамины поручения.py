from collections import deque
import math
import heapq
from pdb import set_trace


def main():
    a, b, c, v0, v1, v2 = map(int, input().split())
    velocities = [v0, v1, v2]
    dists = {
        "A": [("B", a), ("C", b)],
        "B": [("A", a), ("C", c)],
        "C": [("A", b), ("B", c)],
    }
    bit_mask = {"A": 0, "B": 1, "C": 2}
    variants = [(0, "A", 0b000, 0)]# 0b000 - это вместо set - каждый разряд отвечает за посещенность своей вершины из bit_mask
    memo = {}
    min_time = math.inf
    len_neighs = len(dists["A"])    
    while variants:        
        cur_time, v, visited_mask, vi = heapq.heappop(variants)        
        state = (v, visited_mask, vi)
        if state in memo and memo[state] < cur_time:
            continue
                                
        memo[(v, visited_mask, vi)] = cur_time
            
        v_bit_mask = bit_mask[v]
        visited_without_A = visited_mask & ~(1 << v_bit_mask)
        if v == "A" and bin(visited_without_A).count("1") == len_neighs:
            # конец пути            
            min_time = min(min_time, cur_time)            
            continue
        for u, dist in dists[v]:
            u_bit_mask = bit_mask[u]
            speed = velocities[vi]
            new_time = cur_time + dist / speed
            if new_time >= min_time:
                # нет смысла продолжать
                continue

            if u == "A":
                heapq.heappush(variants, (new_time, u, visited_mask, 0))                
                continue
            if not (
                visited_mask & (1 << u_bit_mask)
            ):  # проверка нет ли вершины в посещенных
                _visited = visited_mask | (1 << u_bit_mask)
                heapq.heappush(variants, (new_time, u, _visited, vi+1))                
            # мы можем забирать товар, а можем и не забирать, поэтому
            heapq.heappush(variants, (new_time, u, visited_mask, vi))
    
    return min_time


if __name__ == "__main__":
    print(main())
