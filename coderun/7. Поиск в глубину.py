import sys
from collections import defaultdict

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, m = map(int, input().split())
    graph = defaultdict(set)
    for _ in range(m):
        a, b = map(int, input().split())        
        graph[a].add(b)
        graph[b].add(a)
    
    component = [1]
    visited = set([1])
    stack = [1]    
    while stack:
        v = stack.pop()
        for u in graph[v]:
            if u not in visited:
                stack.append(u)
                component.append(u)
                visited.add(u)
    component.sort()    
    print(len(component))
    print(" ".join(map(str, component)))
    


if __name__ == '__main__':
    main()
