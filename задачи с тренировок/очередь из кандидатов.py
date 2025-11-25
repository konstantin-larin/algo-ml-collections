import sys

sys.setrecursionlimit(2000)

def main():    
    n, x = map(int, input().split())        
    a = list(map(int, input().split()))    
            
    m = int(input())    


    MAX_SIZE = n + m + 1
    
    bit = [0] * MAX_SIZE

    def update_bit(idx, delta):    
        while idx < MAX_SIZE:
            bit[idx] += delta
            idx += idx & (-idx)

    def query_bit(idx):        
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)
        return s
        
    def query_range(l, r):        
        if l > r: return 0
        return query_bit(r) - query_bit(l - 1)
    
    
    queue_data = [0] * (n + m) 
    
    start_idx = 0    
    end_idx = 0
    
    for prof in a:
        queue_data[end_idx] = prof
        if prof >= x:
            update_bit(end_idx + 1, 1)
        end_idx += 1


    for _ in range(m):
        command = list(map(int, input().split()))
        event_type = command[0]

        if event_type == 1:   
            #  в конец очереди приходит человек
            prof =command[1] 
                        
            queue_data[end_idx] = prof
                        
            if prof >= x:                
                update_bit(end_idx + 1, 1)
            
            end_idx += 1
        
        elif event_type == 2:
            # из начала очереди уходит человек            
            if start_idx < end_idx:
                start_idx += 1
        
        elif event_type == 3:
            # Маша хочет узнать, сколько подходящих людей среди первых k
            k = command[1]
                
            l_abs_idx = start_idx
            r_abs_idx = start_idx + k - 1
                
            l_bit_idx = l_abs_idx + 1
            r_bit_idx = r_abs_idx + 1
                        
            suitable_count = query_range(l_bit_idx, r_bit_idx)
            
            print(suitable_count)

if __name__ == "__main__":
    main()