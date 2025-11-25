import sys
from bisect import bisect_right

def main():    
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """        
    n, m, x = map(int, input().split())

    train_intervals = []
    
    # вычисление интервалов занятости для каждого поезда
    for _ in range(n):
        a, b, v = map(int, input().split())
            
        if a == b:
            continue 
        
        if a < b:
            u = v
        else:
            u = -v
        
        # T = (x - p) / u, где p - координата конца поезда
        t1 = (x - a) / u
        t2 = (x - b) / u        
        t_start = min(t1, t2)
        t_end = max(t1, t2)            
                
        
        train_intervals.append((t_start, t_end))

    train_intervals.sort()
    
    merged_intervals = []    
    current_start, current_end = train_intervals[0]
        
    for next_start, next_end in train_intervals[1:]:            
        if next_start <= current_end + 1e-9: 
            current_end = max(current_end, next_end)
        else:        
            merged_intervals.append((current_start, current_end))
            current_start, current_end = next_start, next_end
                
    merged_intervals.append((current_start, current_end))

    start_times = [s for s, e in merged_intervals]
                
    times = list(map(int, input().split()))    
    
    for t_j in times:        
        idx = bisect_right(start_times, t_j)
        
        wait_time = t_j
        
        if idx > 0:
            S_k, E_k = merged_intervals[idx - 1]
                        
            if t_j <= E_k + 1e-9: 
                wait_time = E_k

        print(wait_time)
        

if __name__ == "__main__":    
    main()