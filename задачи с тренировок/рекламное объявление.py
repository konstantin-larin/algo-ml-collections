def main():
    N, W, H = map(int, input().split())
    words = []

    # Бинарный поиск
    L = 0.0    
    R = float('inf')
        
    for _ in range(N):
        a, b = map(int, input().split())
        R = min(R, W / a)
        R = min(R, H / b)        
        words.append((a, b))

    def check(k):
        if k <= 1e-9: 
            return True

        current_height = 0.0
        i = 0
        while i < N:
            # Размеры слова, начинающего строку (i)
            w_i = k * words[i][0]
            h_i = k * words[i][1]

            if w_i > W + 1e-9 or h_i > H + 1e-9:
                return False

            row_height = h_i
            row_width = w_i
            j = i + 1

            while j < N:
                w_j = k * words[j][0]
                h_j = k * words[j][1]
                
                # Используем исходные целые значения для сравнения высот
                if words[j][1] != words[i][1]:
                    break
                
                if row_width + w_j > W + 1e-9:
                    break
                
                row_width += w_j
                j += 1
            
            current_height += row_height
            if current_height > H + 1e-9:
                return False

            i = j

        return True

    
    while R - L > 1e-6:
        mid = (L + R) / 2.0
        if check(mid):
            L = mid
        else:
            R = mid

        

    return L

if __name__ == "__main__":
    print(main())
