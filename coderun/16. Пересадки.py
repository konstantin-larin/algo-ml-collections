# https://coderun.yandex.ru/problem/metro-2

import sys
from collections import defaultdict, deque


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    m = int(input())    
    lines = []
    for i in range(m):
        lines.append(set(list(map(int, input().split()))[1:]))
    a, b = map(int, input().split())
    
    graph = defaultdict(list)
    start_lines_indices = set()
    end_lines_indices = set()
    

    for i in range(m):
        line1 = lines[i]
        a_in = a in line1
        b_in = b in line1
        if a_in and b_in:            
            return 0
        if a_in:
            start_lines_indices.add(i)
        if b_in:
            end_lines_indices.add(i)

        for j in range(i + 1, m):
            line2 = lines[j]
            if len(line1 & line2) > 0:
                graph[i].append(j)
                graph[j].append(i)        
    
    searches = deque([(deque([i]), set([i])) for i in start_lines_indices])
    ans = 0
    while searches:        
        searches_count = len(searches)
        for _ in range(searches_count):
            queue, visited = searches.popleft()
            if not queue: 
                continue
            for _ in range(len(queue)):
                v = queue.popleft()
                if v in end_lines_indices:
                    return ans
                for j in graph[v]:       
                    if j not in visited:
                        visited.add(j)
                        queue.append(j)                        
            searches.append((queue, visited))
        ans += 1                   
    return -1
    
        


    



if __name__ == '__main__':
    print(main())