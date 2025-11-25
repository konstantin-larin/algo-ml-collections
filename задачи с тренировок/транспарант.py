import sys
import math

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, d = map(int, input().split())

    trees = []
    for _ in range(n):
        trees.append(tuple(map(int, input().split())))
    
    tree_coords = set(trees)
    count = 0
    max_dx = int(math.sqrt(d))
    diff_pairs = set()

    for dx in range(max_dx + 1):
        dx_sq = dx * dx
        dy_sq = d - dx_sq
        
        if dy_sq < 0:
            continue
        
        dy = int(math.sqrt(dy_sq))
        if dy * dy == dy_sq and dx <= dy:
            diff_pairs.add((dx, dy))
    
    positive_deltas = []
    for dx, dy in diff_pairs:
        if dx > 0:
            positive_deltas.append((dx, dy))
            if dy > 0:
                positive_deltas.append((dx, -dy))
        if dx == 0 and dy > 0:
            positive_deltas.append((0, dy))
        if dx != dy and dy != 0:
            positive_deltas.append((dy, dx))
            if dx > 0:
                positive_deltas.append((dy, -dx))

    for x1, y1 in trees:
        for a, b in positive_deltas:
            x2 = x1 + a
            y2 = y1 + b
            if (x2, y2) in tree_coords:
                count += 1
                            
    print(count)

if __name__ == '__main__':
    main()