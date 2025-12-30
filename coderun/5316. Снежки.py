import sys

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """        
    def rocks_to_remove(x): # оптимальное количество камней, которое надо убрать, чтобы выиграть (если x % 3 == 0, то надо убрать 0 камней, чтобы выиграть, то есть если уберешь камень, проиграешь)
        return x % 3    
    # теорема Шпрага Гранди
    def game(x1, x2, x3):        
        return int((rocks_to_remove(x1) ^ rocks_to_remove(x2) ^ rocks_to_remove(x3)) != 0)
    n = int(input())
    for _ in range(n):
        print(game(*map(int, input().split())))        


if __name__ == '__main__':
    main()
