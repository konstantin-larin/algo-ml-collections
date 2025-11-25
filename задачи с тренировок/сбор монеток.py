def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    m = 3        
    row = [0] * m
    is_available_cell = [True] * m
    max_coins = 0
    for i in range(n):        
        s = input()
        tmp_row = [0] * m
        tmp_is_available_cell = [True] * m
        for j, ch in enumerate(s):                                                            
            if ch == 'W':
                tmp_is_available_cell[j] = False
                continue              
            # клетки откуда мы можем придти                
            possible_cells = [cell for cell in [j-1, j, j + 1] if 0 <= cell < m and is_available_cell[cell]]            
            if len(possible_cells) == 0:
                tmp_is_available_cell[j] = False # мы не можем оказаться в этом месте
                continue            
            is_coin = int(s[j] == 'C') # есть ли тут монетка                  

            # какой максимум может быть достигнут на этой клетке            
            tmp_row[j] = max([row[cell] + is_coin for cell in possible_cells]) 
        if not any(tmp_is_available_cell):
            break
        row = tmp_row        
        is_available_cell = tmp_is_available_cell
        max_coins = max(max_coins, max(row))

        

            

    return max_coins


if __name__ == '__main__':
    print(main())
