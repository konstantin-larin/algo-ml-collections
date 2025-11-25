import sys
import heapq



def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    # будет очень много запросов на суммы и минимумы, при этом сам массив меняться не будет поэтому sparse table

    class SparseTable:
        def __init__(self, arr):
            self.n = len(arr)
            self.log = [0] * (self.n + 1) # степень двойки для этого числа
            for i in range(2, self.n + 1):
                self.log[i] = self.log[i // 2] + 1

            K = self.log[self.n] + 1 
            self.st = [[0] * self.n for _ in range(K)]
            for i in range(self.n):
                self.st[0][i] = arr[i]

            j = 1
            while (1 << j) <= self.n:
                i = 0
                while i + (1 << j) <= self.n:
                    self.st[j][i] = min(self.st[j - 1][i],
                                        self.st[j - 1][i + (1 << (j - 1))])
                    i += 1
                j += 1


            self.pref = [0] * (self.n + 1)
            for i in range(self.n):
                self.pref[i + 1] = self.pref[i] + arr[i]

        def range_min(self, l, r):
            #минимум на [l, r)
            length = r - l
            j = self.log[length]
            return min(self.st[j][l], self.st[j][r - (1 << j)])

        def range_sum(self, l, r):
            #сумма на [l, r)
            return self.pref[r] - self.pref[l]

            
    n, k = map(int, input().split())
    bars = SparseTable(list(map(int, input().split())))    

        
    possible_first_count = n - k + 1
    towers = [0] * possible_first_count
    for i in range(possible_first_count):
        towers[i] = bars.range_sum(i, i + k) * bars.range_min(i, i + k) # фиксируем защищенность каждой возможной башни
    
    best = [0] * possible_first_count
    indices = [-1] * possible_first_count
    best[0] = towers[0]
    indices[0] = 0
    maximum = towers[0]
    argmaximum = 0
    for i in range(1, possible_first_count):
        if i - k >= 0:            
            best_sum = towers[i] + best[i - k]                        
        else:
            best_sum = towers[i]            

        if best[i - 1] > best_sum:
            best[i] = best[i - 1]
            indices[i] = indices[i - 1]
        else:
            best[i] = best_sum
            indices[i] = i        

        if best[i] > maximum:
            maximum = best[i]
            argmaximum = indices[i]    
    
    numbers = []
    while argmaximum >= 0:
        idx = indices[argmaximum]        
        numbers.append(str(idx + 1))
        argmaximum = idx - k        


        
    
                
    q = len(numbers)
    print(q)
    print(" ".join(reversed(numbers)))

        

        
    


if __name__ == '__main__':
    main()

