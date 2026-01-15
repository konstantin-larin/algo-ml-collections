import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    min_r = 0
    points = []
    for _ in range(n):
        points.append(tuple(map(int, input().split())))
    
    def euclid2d(p1, p2):
        return pow(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2), 0.5)
    max_r = 0
    for i in range(n):
        p1 = points[i]
        for j in range(i+1, n):
            p2 = points[j]
            max_r = max(max_r, euclid2d(p1, p2) / 2)
    
    def can(r, frequencies):
        visited = set()  # множество посещённых вершин
        
        def dfs(v):
            visited.add(v)
            p1 = points[v]
            for u in range(n):
                if u == v:
                    continue
                p2 = points[u]
                # конфликт, если расстояние меньше 2*r                
                if euclid2d(p1, p2) < 2*r:                    
                    if frequencies[u] == "":                        
                        frequencies[u] = '2' if frequencies[v] == '1' else '1'
                        if not dfs(u):
                            return False                
                    elif frequencies[u] == frequencies[v]:
                        return False
            return True

        # проходим по всем компонентам графа
        for i in range(n):
            if frequencies[i] == "":
                frequencies[i] = '1' #частота по умолчанию
                if not dfs(i):
                    return False
        return True

    mid_r = 0
    frequencies = [""] * n 

    r = 0
    frequencies_str = " ".join(frequencies)
    epsilon = pow(10, -8)    
    while min_r < max_r and abs(mid_r - (min_r + max_r) / 2) > epsilon:        
        mid_r = (min_r + max_r) / 2 
        frequencies = [""] * n 
        if can(mid_r, frequencies):
            r = mid_r            
            frequencies_str = " ".join(frequencies)
            min_r = mid_r
        else:
            max_r = mid_r
        
    print(r)
    print(frequencies_str)

if __name__ == '__main__':
    main()
