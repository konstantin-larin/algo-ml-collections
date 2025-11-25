import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, m = map(int, input().split())
    if n < 5 and m < 5:        
        return 'No'
            
    
    if n < 5:
        # возможно только по горизонтали
        for _ in range(n):
            s = input()
            h_counter = 0        
            cur_char = s[0]
            for char in s:
                if char == '.': 
                    h_counter = 0
                elif char == cur_char:
                    h_counter += 1
                else: # char != cur_char:
                    h_counter = 1
                            
                cur_char = char
                if h_counter == 5:                
                    return 'Yes'
        return 'No'
    
    
    tmp_row = []
    v_counter = []
    r_diagonals_counter = []
    l_diagonals_counter = []
    # запишем init tmp_row и v_counter и заодно проверим на h_counter    
    s = input()
    h_counter = 0
    cur_char = '.'
    for j, char in enumerate(s):
        if char == '.':
            h_counter = 0
            v_counter.append(0)    
            l_diagonals_counter.append(0)            
            r_diagonals_counter.append(0)                        
            cur_char = char
            tmp_row.append(char)
            continue
        if char == cur_char:
            h_counter += 1
        cur_char = char
        v_counter.append(1)        
        l_diagonals_counter.append(1)        
        r_diagonals_counter.append(1)        
        tmp_row.append(char)
        if h_counter == 5:
            return 'Yes'
            
    
    
    if m < 5:
        # возможно только по вертикали
        for _ in range(1, n):
            s = input()
            for j, char in enumerate(s):
                if char == '.':
                    tmp_row[j] = '.'
                    v_counter[j] = 0
                elif tmp_row[j] == '.':
                    # char уже не .
                    tmp_row[j] = char
                    v_counter[j] = 1                
                elif tmp_row[j] == char:  
                    # char и tmp_row[j] in 'XO'                    
                    v_counter[j] += 1
                    if v_counter[j] == 5:
                        return 'Yes'
                else:
                    # tmp_row[j] != char и они не точки
                    tmp_row[j] = char
                    v_counter[j] = 1            
        return 'No'
    
    # общий случай - когда возможно и по диагонали        
    for _ in range(1, n):
        s = input()
        h_counter = 0
        cur_char = s[0]
        _tmp_row = []
        _l_diagonals_counter = list(l_diagonals_counter)
        _r_diagonals_counter = list(r_diagonals_counter)
        for j, char in enumerate(s):              
            # общая часть у всех
            _tmp_row.append(char)            
            if char == '.':
                h_counter = 0                
                v_counter[j] = 0
                cur_char = char   
                _l_diagonals_counter[j] = 0
                _r_diagonals_counter[j] = 0
                continue            
            #  проверяем на горизонталь                                        
            if char == cur_char:
                h_counter += 1
                if h_counter == 5:
                    return 'Yes'
            else:
                h_counter = 1
            cur_char = char            
            
            # проверяем на вертикаль            
            if tmp_row[j] == '.':
                # char уже не .                
                v_counter[j] = 1    
                                    
            elif tmp_row[j] == char:  
                # char и tmp_row[j] in 'XO'                    
                v_counter[j] += 1
                if v_counter[j] == 5:
                    return 'Yes'
            else:
                # tmp_row[j] != char и они не точки                
                v_counter[j] = 1


            # проверяем на диагональ                        
            left_j = j - 1
            right_j = j + 1                        
            if left_j >= 0:                                                
                if char == tmp_row[left_j]:                                                         
                    _l_diagonals_counter[j] = l_diagonals_counter[left_j] + 1                    
                    if _l_diagonals_counter[j] == 5:
                        return 'Yes'                    
                else:
                    _l_diagonals_counter[j] = 1
            if right_j < m:                
                if char == tmp_row[right_j]:
                    _r_diagonals_counter[j] = r_diagonals_counter[right_j] + 1
                    if _r_diagonals_counter[j] == 5:
                        return 'Yes'
                else:
                    _r_diagonals_counter[j] = 1            
            
        tmp_row = _tmp_row        
        l_diagonals_counter = _l_diagonals_counter        
        r_diagonals_counter = _r_diagonals_counter
        
    return 'No'
    


if __name__ == '__main__':
    print(main())

    
