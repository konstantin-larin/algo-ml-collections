import sys
from collections import Counter

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    gw, gs = map(int, input().split())
    w = input()
    s = input()
    
    w_counter = Counter(w)    
    diff_counter = Counter({k: -w_counter[k] for k in w_counter})
    diff_stack = set(diff_counter.keys())
    for i in range(gw):
        if s[i] in w_counter:
            diff_counter[s[i]] += 1
            if diff_counter[s[i]] == 0:
                diff_stack.remove(s[i])
    
    ans = 0 if diff_stack else 1
    for i in range(gw, gs):
        if s[i] in w_counter:
            diff_counter[s[i]] += 1
            if diff_counter[s[i]] == 0:
                # это значит что он был в diff stack - убираем его
                diff_stack.remove(s[i])

        if s[i - gw] in w_counter:
            if diff_counter[s[i - gw]] == 0:
                # это значит, что сейчас символа будет не хватать - добавляем его
                diff_stack.add(s[i - gw])
            diff_counter[s[i - gw]] -= 1
                                
        ans += (0 if diff_stack else 1)
    print(ans)
            
            
    
    
    
        


if __name__ == '__main__':
    main()
