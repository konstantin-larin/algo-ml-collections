import sys

class FenwickTree:    
    def __init__(self, size):
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, i, delta):        
        i += 1
        while i <= self.size:
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):        
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

def main():     
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """        
    n = int(input())            
    a = list(map(int, input().split()))        
    
    max_val = 2 * n + 1 
    bit = FenwickTree(max_val)
    total_bonus = 0

    for i in range(n):        
        count_le_i = bit.query(i)     
        count_qualifying_j = i - count_le_i
        
        bonus_i = count_qualifying_j * a[i]
        total_bonus += bonus_i
                
        bit.update(i + a[i], 1)
    
    print(total_bonus)

if __name__ == '__main__':
    main()