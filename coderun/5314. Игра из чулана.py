import sys
from collections import Counter

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    # строки должны быть одинаковы длины k
    # из строки s может быть взята подстрока длины k
    # из строки t может быть взято k любых символов и составлено в строку длиной k
    k = int(input())
    s = input()
    t = input()
    # стратегия проста - ведем counter символов для подстроки в s
    # сравниваем этот counter с counter'ом символов в t
    # причем это не особо затратно, ибо всего 26 символов (ключей) в counter максимально
    # если из t_counter можно взять те же символы, что и в подстроке, то YES, иначе, если так и не получилось - NO

    t_counter = Counter(t)    
    sub_s_counter = Counter(s[:k])        
    i = k
    while True:
        if t_counter >= sub_s_counter:
            return "YES"
        if i == len(s):
            return "NO"
        sub_s_counter[s[i - k]] -= 1
        sub_s_counter[s[i]] += 1    
        i += 1
            


if __name__ == '__main__':
    print(main())
