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
    all_verticles = set(range(1, n + 1))
    for _ in range(m):
        a, b = map(int, input().split())        
        graph[a].add(b)
        graph[b].add(a)
    
    components = []
    visited_verticles = set()
    rest_verticles = set(all_verticles)

    while rest_verticles:        
        some_v = rest_verticles.pop()        
        component = [some_v]
        visited_verticles.add(some_v)
        stack = [some_v]   

        while stack:
            v = stack.pop()            
            for u in graph[v]:
                if u not in visited_verticles:
                    stack.append(u)
                    visited_verticles.add(u)
                    component.append(u)
                    rest_verticles.remove(u)
        components.append(component)
    
    print(len(components))
    for component in components:
        print(len(component))
        print(" ".join(map(str, component)))    






if __name__ == '__main__':
    main()