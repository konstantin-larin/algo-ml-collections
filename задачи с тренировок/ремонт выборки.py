import sys

def main():    
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, m, k = map(int, input().split())

    a = list(map(int, input().split()))    
            
    routes_diff = [0] * (n + 2)
        
    for _ in range(m):
        l, r = map(int, input().split())                
        routes_diff[l] += 1        
        if r + 1 <= n + 1:
            routes_diff[r + 1] -= 1
        
    routes_count = [0] * (n + 1) 
    current_count = 0
    for j in range(1, n + 1):
        current_count += routes_diff[j]
        routes_count[j] = current_count
            
    initial_total_discomfort = 0
    repair_priorities = [] 

    for j in range(1, n + 1):
        num_holes = a[j-1]
        value = routes_count[j]
                
        initial_total_discomfort += num_holes * value
        
        if value > 0 and num_holes > 0:        
            repair_priorities.append((value, j))    
        
    repair_priorities.sort(key=lambda x: x[0], reverse=True)

    total_discomfort_reduction = 0
        
    for value, j in repair_priorities:
        num_holes = a[j-1]
                
        repairs_done = min(num_holes, k)
        
        if repairs_done == 0:
            break
                    
        reduction = repairs_done * value
        total_discomfort_reduction += reduction
                
        k -= repairs_done
            
    min_total_discomfort = initial_total_discomfort - total_discomfort_reduction
    
    print(min_total_discomfort)

if __name__ == "__main__":    
    main()