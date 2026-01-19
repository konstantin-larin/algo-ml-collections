import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    positive_fruits = [] # в приоритете маленькие b
    negative_fruits = [] # в приоритете большие a
    for i in range(n):
        a, b = map(int, input().split())
        if a - b >= 0:
            positive_fruits.append((a, b, i + 1))
        else:
            negative_fruits.append((a, b, i + 1))
    
    positive_fruits.sort(key= lambda x: (x[1], -x[0]))    
    negative_fruits.sort(key=lambda x: (-x[0], x[1]))
    fruits = positive_fruits + negative_fruits

    
    ans_1 = 0
    ans_2 = []
    cur = 0
    for fruit in fruits:
        a, b, i = fruit
        cur += a
        ans_1 = max(ans_1, cur)
        cur -= b
        ans_2.append(str(i))
    

    print(ans_1)
    print(" ".join(ans_2))


if __name__ == '__main__':
    main()
