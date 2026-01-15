import sys

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    space = []
    for _ in range(n):
        space.append(list(input()))
        
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]    
    def dfs(r, c):
        if space[r][c] != '.': return 0
        count = 1
        space[r][c] = '*'
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc            
            count += dfs(nr, nc)
        return count
    print(dfs(*map(lambda x: int(x) - 1, input().split())))    


if __name__ == '__main__':
    main()
