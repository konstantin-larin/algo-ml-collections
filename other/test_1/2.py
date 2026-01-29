# дана строка s
# строка хорошая, если  в ней есть подстроки tbank и study
# у меня очень важная задача - найти мин колво символов которые надо заменить в строке, чтобы она была хорошей
# гарантируют, что строка содержит только строчные буквы алфафита
# разберем примеры
# 10 <= len(s) <= 10^5 - отлично
# tbankstudy - 0 ну я сно
# studtbankk - studYTBANk

a = 'tbank'
b = 'study'

# введем две переменные cost_a и cost_b которые будут значить сколько замен надо сделать для i чтобы i:i+5 дал a или b
s = input()
n = len(s)
INF = float('inf')
cost_a = [INF] * n
cost_b = [INF] * n
for i in range(n - 4):
    sub_s = s[i:i+5]
    cost_a[i] = sum(x != y for x, y in zip(sub_s, a)) # перебираем пары подстроки и a
    cost_b[i] = sum(x != y for x, y in zip(sub_s, b)) # перебираем пары подстроки и b
# по идее подстроки a и b могут пересекаться и не пересекаться
# если не пересекаются то получается cost_a[i:i+5] и cost_b[j:j+5], где i и j не пересек
# то есть можно посчитать 2 варианта (без пересечений vs c пересечениями) и взять min

# 1 вар
# a фиксируем, b ищем
pref_min_b = [INF]*n
suf_min_b  = [INF]*n

cur = INF
for i in range(n):
    cur = min(cur, cost_b[i])
    pref_min_b[i] = cur

cur = INF
for i in reversed(range(n)):
    cur = min(cur, cost_b[i])
    suf_min_b[i] = cur

ans = INF

for i in range(n-4):  
    best_b = INF
    if i-5 >= 0:
        best_b = min(best_b, pref_min_b[i-5])
    if i+5 < n:
        best_b = min(best_b, suf_min_b[i+5])
    ans = min(ans, cost_a[i] + best_b)


# b фиксируем a ищем
pref_min_a = [INF]*n
suf_min_a  = [INF]*n

cur = INF
for i in range(n):
    cur = min(cur, cost_a[i])
    pref_min_a[i] = cur

cur = INF
for i in reversed(range(n)):
    cur = min(cur, cost_a[i])
    suf_min_a[i] = cur

for i in range(n-4):  
    best_a = INF
    if i-5 >= 0:
        best_a = min(best_a, pref_min_a[i-5])
    if i+5 < n:
        best_a = min(best_a, suf_min_a[i+5])
    ans = min(ans, cost_b[i] + best_a)


# вар 2
# оба слова длины 5 -> сдвиг между их началами d может быть от -4 до +4, чтобы они пересекались
for i in range(n-4):           # a старт
    for d in range(-4, 5):     # относительный сдвиг b
        j = i + d              # b старт
        if j < 0 or j+4 >= n: 
            continue

        ok = True
        cost = 0

        # проверяем объединение позиций
        l = min(i, j)
        r = max(i+4, j+4)

        for pos in range(l, r+1):
            st = None

            # символ от a
            if i <= pos <= i+4:                
                st = a[pos-i]

            # символ от b
            if j <= pos <= j+4:                
                if st is None:
                    st = b[pos-j]
                else:
                    if st != b[pos-j]:
                        ok = False
                        break

            if s[pos] != st:
                cost += 1
        if ok:
            ans = min(ans, cost)

print(ans)