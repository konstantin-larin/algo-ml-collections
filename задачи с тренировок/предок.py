import sys

sys.setrecursionlimit(2000000)
def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    with open('input.txt', 'r') as f:
        n = int(f.readline())    
        parents = list(map(int, f.readline().split()))        

        # Построение списка смежности (дерева)
        # adj[i] будет содержать список детей вершины i+1
        adj = [[] for _ in range(n + 1)]
        root = -1

        for i in range(n):
            parent_index = parents[i]
            child_index = i + 1
            
            if parent_index == 0:
                # Нашли корень дерева
                root = child_index
            else:
                # Добавляем ребро от родителя к ребенку
                adj[parent_index].append(child_index)

        # Инициализация массивов для времени входа и выхода
        tin = [0] * (n + 1)
        tout = [0] * (n + 1)
        # Глобальный счетчик времени
        timer = 0 

        # Функция DFS для вычисления tin и tout
        def dfs(u):
            nonlocal timer
            
            # Увеличиваем таймер и записываем время входа
            timer += 1
            tin[u] = timer
            
            # Рекурсивно вызываем DFS для всех детей
            for v in adj[u]:
                dfs(v)
                
            # Увеличиваем таймер и записываем время выхода
            timer += 1
            tout[u] = timer

        # Запускаем DFS от корня
        if root != -1:
            dfs(root)
        # Если дерево состоит из одной вершины, tin[1]=1, tout[1]=2

        # Функция для проверки, является ли u предком v
        def is_ancestor(u, v):
            # u - предок v, если интервал [tin[u], tout[u]] содержит [tin[v], tout[v]]        
            if tin[u] <= tin[v] and tout[u] >= tout[v]:
                return 1
            else:
                return 0

        m = int(f.readline())    
        for _ in range(m):
            a, b = map(int, f.readline().split())
            print(is_ancestor(a, b))    

if __name__ == '__main__':
    main()