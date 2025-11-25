import sys
from bisect import bisect_right

def calculate_partial_force(outer_dim, outer_coords, inner_dim, inner_coords):    
    # Сортируем внутренний массив и вычисляем его префиксные суммы
    inner_sorted = sorted(inner_coords)
    prefix_sum_inner = [0] * (inner_dim + 1)
    for k in range(inner_dim):
        prefix_sum_inner[k + 1] = prefix_sum_inner[k] + inner_sorted[k]
    
    total_sum_inner = prefix_sum_inner[inner_dim]
    
    partial_sum = 0    
    for i in range(1, outer_dim + 1):
        # Берем (i-1)-й элемент, так как массивы 0-индексированы
        val_outer = outer_coords[i - 1]
        
        # Находим k: количество элементов в inner_sorted <= val_outer
        k = bisect_right(inner_sorted, val_outer)
        
        # Сумма элементов <= val_outer
        sum_le = prefix_sum_inner[k]
        
        # Сумма элементов > val_outer
        sum_gt = total_sum_inner - sum_le
        
        # Вычисляем Sum_{j} |val_outer - inner_coords[j-1]|        
        sum_abs_diff = (k * val_outer - sum_le) + (sum_gt - (inner_dim - k) * val_outer)
        
        # Добавляем к частичной сумме, умножая на внешний индекс i
        partial_sum += i * sum_abs_diff
        
    return partial_sum

def main():                            
    n = int(input())
    a = list(map(int, input().split()))        
        
    m = int(input())
    b = list(map(int, input().split()))
    
    
    

    # Сила = Sum_{i,j} (i - j) * |a_i - b_j|
    #      = Sum_{i,j} i*|a_i - b_j| - Sum_{i,j} j*|a_i - b_j|
    #      = part1 - part2

    # part1 = Sum_{i} i * (Sum_{j} |a_i - b_j|)
    part1 = calculate_partial_force(n, a, m, b)
    
    # part2 = Sum_{j} j * (Sum_{i} |a_i - b_j|) 
    # Это симметричная задача, просто меняем массивы местами
    part2 = calculate_partial_force(m, b, n, a)
    
    
    result = part1 - part2
    print(result)

if __name__ == "__main__":
    main()