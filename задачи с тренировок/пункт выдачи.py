import sys

sys.setrecursionlimit(200000)

def main():
    n = int(input())    
    a = list(map(int, input().split()))    

    # Общее число жителей
    total_population = sum(a)

    # Список смежности для представления дерева
    adj = [[] for _ in range(n + 1)]
    
    # Чтение ребер
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    if n == 1:
        print(1)
        return

    # Массив для хранения веса поддерева (сумма жителей)
    subtree_population = [0] * (n + 1)
        
    def dfs_weights(u, p):    
        # Вес самой вершины (a_i хранится с индексом i-1)
        current_weight = a[u - 1]
        
        for v in adj[u]:
            if v != p:
                current_weight += dfs_weights(v, u)
        
        subtree_population[u] = current_weight
        return current_weight

    # Запускаем DFS от корня 1
    dfs_weights(1, 0)
    
    # Поиск оптимальной площади
    min_max_queue = float('inf')
    best_node = -1

    for i in range(1, n + 1):
        # Максимальная очередь для площади i
        max_queue_i = a[i - 1] # Очередь из жителей самой площади i
        
        # Очереди со стороны соседей
        for neighbor in adj[i]:
            # Мы хотим найти размер компоненты, которая остается после удаления i и содержит 'neighbor'.

            # Если neighbor находится в поддереве i (например, i=1, neighbor=2, i-корень, neighbor-ребенок)
            # В процессе DFS, когда мы идем от родителя к ребенку, weight[neighbor] - это 
            # размер его поддерева.
            if subtree_population[neighbor] < subtree_population[i]:
                # Сосед 'neighbor' находится "ниже" в дереве, корнем которого является 1
                # Размер компоненты: W_neighbor - этот вес уже вычислен
                component_weight = subtree_population[neighbor]
            else:
                # Сосед 'neighbor' является родителем i (или i это корень и это не его случай)
                # i является дочерней вершиной для neighbor размер компоненты: total_population - W_i
                component_weight = total_population - subtree_population[i]
            
            # Обновляем максимальную очередь
            max_queue_i = max(max_queue_i, component_weight)

        # Обновляем глобальный минимум
        if max_queue_i < min_max_queue:
            min_max_queue = max_queue_i
            best_node = i
        elif max_queue_i == min_max_queue and i < best_node:
             # Выводим любой, но если равны, выберем наименьший номер
            best_node = i

    print(best_node)

if __name__ == '__main__':
    main()