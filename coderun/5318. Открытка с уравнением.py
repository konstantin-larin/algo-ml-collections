# https://coderun.yandex.ru/problem/postcard-equation

import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    # p(x) может достигать значение 11 максимум - 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 > 10**12
    # print(2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 > 10 ** 12)
    # x = n - p(x)
    n = int(input())
    # строим решето эратосфена до sqrt(10 ** 12)
    MAX_PRIME = pow(10,6) + 1
    is_prime = [True] * MAX_PRIME
    is_prime[0] = False
    is_prime[1] = False
    primes = []
    for x in range(2, MAX_PRIME):
        if is_prime[x]:
            primes.append(x)
            for y in range(x * x, MAX_PRIME, x):
                is_prime[y] = False    
        
    def p(x):        
        x_primes_count = 0

        for prime in primes:            
            if prime * prime > x:
                break
            # факторизация
            if x % prime == 0:
                x_primes_count += 1
                while x % prime == 0:
                    x //= prime        
        if x > 1:
            x_primes_count += 1

        return x_primes_count
    
    ans = 0
    for p_x in range(12):
        x = n - p_x # это потенциальное решение уравнения, надо проверить p(x) == p_x                
        if x > 0:
            ans += int(p_x == p(x))
    print(ans)
    

if __name__ == '__main__':
    main()
