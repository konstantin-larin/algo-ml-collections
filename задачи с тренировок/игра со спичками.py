import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    
    n = int(input())
    if n % 4 == 0:
        return 2
    return 1
    # строим решето эратосфена    
    # is_prime = [True] * (n + 1)
    # is_prime[0] = is_prime[1] = False
    # for i in range(2, int(n**0.5) + 1):
    #     if is_prime[i]:
    #         for j in range(i**2, n+1, i):
    #             is_prime[j] = False
    
    # wins_positions = [True] * (n + 1)    
    # for i in range(4, n + 1):
    #     available_positions = [wins_positions[pos] for pos in [i-1, i-2, i-3] if not is_prime[pos]]
    #     wins_positions[i] = not all(available_positions)            
    # if wins_positions[n]:
    #     return 1
    # else: 
    #     return 2
            




if __name__ == '__main__':
    print(main())