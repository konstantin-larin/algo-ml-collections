import sys
import heapq

def main():    
    n = int(input())    
        
    trips_1_to_2 = []
    for _ in range(n):                
        start, end = input().split('-')
        s_h, s_m = map(int, start.split(':')) 
        e_h, e_m = map(int, end.split(':'))
        start_min = s_h * 60 + s_m
        end_min = e_h * 60 + e_m
        trips_1_to_2.append((start_min, end_min))

    m = int(sys.stdin.readline())        
    trips_2_to_1 = []
    for _ in range(m):                
        start, end = input().split('-')
        s_h, s_m = map(int, start.split(':')) 
        e_h, e_m = map(int, end.split(':'))
        start_min = s_h * 60 + s_m
        end_min = e_h * 60 + e_m
        trips_2_to_1.append((start_min, end_min))
        
        
    trips_1_to_2.sort()
    trips_2_to_1.sort()            
    
    H_1 = [] # Время прибытия рейсов 2->1
    for start, end in trips_2_to_1:
        heapq.heappush(H_1, end)
    
    A = 0
    H_1_temp = list(H_1)
    heapq.heapify(H_1_temp)
    
    for start, end in trips_1_to_2:
        if H_1_temp and H_1_temp[0] <= start:
            heapq.heappop(H_1_temp)
        else:
            A += 1
            
    
    H_2 = []
    for start, end in trips_1_to_2:
        heapq.heappush(H_2, end)
    
    B = 0
    H_2_temp = list(H_2)
    heapq.heapify(H_2_temp)
    
    for start, end in trips_2_to_1:
        if H_2_temp and H_2_temp[0] <= start:
            heapq.heappop(H_2_temp)
        else:
            B += 1 
    print(A + B)


if __name__ == '__main__':
    main()