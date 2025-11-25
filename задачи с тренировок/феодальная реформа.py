import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """    
    n = int(input())
    parents = [0] * n
    children = [[] for _ in range(n)]

    for i in range(1, n):
        p = int(input())
        parents[i] = p
        children[p].append(i)

    a = list(map(int, input().split()))

    def dfs(v):
        inc = 0
        dec = 0
        for u in children[v]:
            c_inc, c_dec = dfs(u)
            inc += c_inc
            dec += c_dec
        balance = a[v] + inc - dec
        if balance > 0:
            dec += balance
        elif balance < 0:
            inc += -balance
        return inc, dec

    inc, dec = dfs(0)
    print(inc + dec)




if __name__ == '__main__':
    main()
