# https://coderun.yandex.ru/problem/control-accent
import sys
from collections import defaultdict
import re


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    N = int(input())

    vocab = defaultdict(set)
    for _ in range(N):
        s = input()
        vocab[s.lower()].add(s)
    mistakes = 0
    for s in input().split():
        s_l = s.lower()
        if s_l not in vocab: 
            mistakes += int(len(re.findall(r'[A-Z]', s)) != 1)
            continue                
        mistakes += int(s not in vocab[s_l])
    print(mistakes)


if __name__ == '__main__':
    main()
