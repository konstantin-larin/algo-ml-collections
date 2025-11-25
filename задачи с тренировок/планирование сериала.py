import sys
import math

def main():   
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """         
    n = int(input())        
    s = list(map(int, input().split()))        
    a = list(map(int, input().split()))    
    

    data = []
    total_weight = 0
    for si, ai in zip(s, a):
        total_weight += ai
        data.append((si, ai))
        
    
    data.sort(key=lambda x: x[0])
        
    
    target_weight = math.ceil(total_weight / 2) 
    
    current_weight_sum = 0
    optimal_e = -1
    
    for si, ai in data:
        current_weight_sum += ai
        if current_weight_sum >= target_weight:
            optimal_e = si
            break
                
    min_cost = 0
    for si, ai in data:
        min_cost += abs(optimal_e - si) * ai
        
    print(optimal_e, min_cost)    

if __name__ == "__main__":
    main()