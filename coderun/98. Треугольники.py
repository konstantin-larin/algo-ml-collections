# final
# не учитываем равносторонние треугольники, потому что в целочисленных координатах равносторонних треугольников не существует!
from collections import defaultdict
import math
n = int(input())
points = []
for _ in range(n):    
    x, y = map(int, input().split())
    points.append((x, y))


ans = 0

for i in range(n):
    dists = defaultdict(list)
    for j in range(n):
        if i == j:
            continue        
        x1, y1 = points[i]
        x2, y2 = points[j]                        

        euclid = pow(x2 - x1, 2) + pow(y2 - y1, 2)         
        dists[euclid].append(j)
    
    for dist, ps in dists.items():                      
        for v1 in range(len(ps)):
            for v2 in range(v1 + 1, len(ps)):                
                p1 = ps[v1]
                p2 = ps[v2]
                x1, y1 = points[i]
                x2, y2 = points[p1]
                x3, y3 = points[p2]
                s = (x1 - x2) * (y1 - y3) - (x1 - x3) * (y1 - y2)
                if s != 0:
                    ans += 1
print(ans)




# iter 6
# конечно же на iter 5 time limit exceed
# вообще iter2 была близка к правильному
# from collections import defaultdict
# import math
# n = int(input())
# points = []
# for _ in range(n):    
#     x, y = map(int, input().split())
#     points.append((x, y))


# ans = 0

# for i in range(n):
#     dists = defaultdict(list)
#     for j in range(n):
#         if i == j:
#             continue        
#         x1, y1 = points[i]
#         x2, y2 = points[j]                        

#         euclid = pow(x2 - x1, 2) + pow(y2 - y1, 2)         
#         dists[euclid].append(j)
    
#     for dist, ps in dists.items():                      
#         for v1 in range(len(ps)):
#             for v2 in range(v1 + 1, len(ps)):                
#                 p1 = ps[v1]
#                 p2 = ps[v2]
#                 x1, y1 = points[i]
#                 x2, y2 = points[p1]
#                 x3, y3 = points[p2]
#                 s = (x1 - x2) * (y1 - y3) - (x1 - x3) * (y1 - y2)
#                 if s != 0:
#                     ans += 1
# print(ans)


# iter 5
# решение на iter 4 правильное, но  memory limit exceed
# from collections import defaultdict
# import math
# n = int(input())
# points = []
# for _ in range(n):    
#     x, y = map(int, input().split())
#     points.append((x, y))


# ans = 0

# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j + 1, n):            
#             x1, y1 = points[i]
#             x2, y2 = points[j]
#             x3, y3 = points[k]            
#             ab = (x1 - x2, y1 - y2)
#             ac = (x1 - x3, y1 - y3)
#             bc = (x2 - x3, y2 - y3)
#             ab_norm = pow(ab[0], 2) + pow(ab[1], 2)
#             ac_norm = pow(ac[0], 2) + pow(ac[1], 2)
#             bc_norm = pow(bc[0], 2) + pow(bc[1], 2)            
#             s = (x1 - x2) * (y1 - y3) - (x1 - x3) * (y1 - y2)
#             ans += int(
#                 (ab_norm == ac_norm or ab_norm == bc_norm or ac_norm == bc_norm) and s != 0
#             )                        
# print(ans)

# iter 4 
# сейчас протестировал на трех точках на одной прямой и мой код это считает
# 3
# 1 1
# 2 2
# 3 3
# 1
# и действительно - если мы на точке 2 считаем, то код засчитывает эту тройку как треугольник
# то есть перед окончательным ответом надо отфильтровать коллинеарные точки

# from collections import defaultdict
# import math
# n = int(input())
# points = []
# for _ in range(n):    
#     x, y = map(int, input().split())
#     points.append((x, y))


# ans = 0
# trios = set()
# for i in range(n):
#     dists = defaultdict(list)
#     for j in range(n):
#         if i == j:
#             continue
#         x1, y1 = points[i]
#         x2, y2 = points[j]                        

#         euclid = pow(x2 - x1, 2) + pow(y2 - y1, 2)
#         dists[euclid].append(j)
#     for dist, ps in dists.items():
#         for z in range(len(ps)):
#             p1 = ps[z]
#             for b in range(z+1, len(ps)):
#                 p2 = ps[b]
#                 trio = tuple(sorted([i, p1, p2]))                
#                 trios.add((trio))
# # считаем вырожденные треугольники 
# # точки коллинеарны если их векторное произведение равно нулю
# # ну и площадь их треугольника будет 0
# # AB = (x1 - x2, y1 - y2)
# # AC = (x1 - x3, y1 - y3)
# # AB x AC = (x1 - x2) * (y1 - y3) - (x1 - x3) * (y1 - y2) 
# ans = 0
# for trio in trios:
#     p1, p2, p3 = trio
    # x1, y1 = points[p1]
    # x2, y2 = points[p2]
    # x3, y3 = points[p3]
    # s = (x1 - x2) * (y1 - y3) - (x1 - x3) * (y1 - y2)
    # if s != 0:
    #     ans += 1
# print(ans)

# iter 3 
# неправильный ответ и я догадываюсь почему
# если есть равносторонние треугольники, то они считаются дважды
# но как мне учесть их?
# from collections import defaultdict
# import math
# n = int(input())
# points = []
# for _ in range(n):    
#     x, y = map(int, input().split())
#     points.append((x, y))


# ans = 0
# # можно по идее записывать тройки в один сет отсортированными кортежами индексов точек, но это нам потребуется 
# # перебирать все эти точки в ручную, что очень затратно
# # хотя раз точек всего 1500, то может это простительно - давай попробуем
# trios = set()
# for i in range(n):
#     dists = defaultdict(list)
#     for j in range(n):
#         if i == j:
#             continue
#         x1, y1 = points[i]
#         x2, y2 = points[j]                        

#         euclid = pow(x2 - x1, 2) + pow(y2 - y1, 2)
#         dists[euclid].append(j)
#     for dist, ps in dists.items():
#         for z in range(len(ps)):
#             p1 = ps[z]
#             for b in range(z+1, len(ps)):
#                 p2 = ps[b]
#                 trio = tuple(sorted([i, p1, p2]))                
#                 trios.add((trio))

# print(len(trios))

# iter 2
# равнобедренные треугольники можно найти за O(n^2), если для каждой точки посчитать расстояние до других точек и посчитать количество совпавших
# допустим у точки есть 2 точки расстояние до которых m, значит это один равнобедренный треугольник
# если 3 то уже 2 треугольника и тд
# то есть если n точек с одинаковым расстоянием до одной вершины, то их количество это C(n, 2)
# from collections import defaultdict
# import math
# n = int(input())
# points = []
# for _ in range(n):    
#     x, y = map(int, input().split())
#     points.append((x, y))


# ans = 0
# for i in range(n):
#     dists = defaultdict(int)
#     for j in range(n):
#         if i == j:
#             continue
#         x1, y1 = points[i]
#         x2, y2 = points[j]                        

#         euclid = pow(x2 - x1, 2) + pow(y2 - y1, 2) # не используем корень, чтобы не было float
#         dists[euclid] += 1 
#     for dist, cnt in dists.items():
#         ans += math.comb(cnt, 2)    
# print(ans)

        

# iter 1
# опять Петька
# он изучил симметрию
# только он не понимает, что симметрии то этой нет нигде как и треугольников этих
# эх Петька, вокруг только пустота, да и этой пустоты тоже нет

# мы ищем равнобедренные треугольники
# на доске нарисовано n точек
# петька задумался сколько там треугольников можно начертить 
# тут надо порисовать
# n = int(input()) # >= 3, <= 1500
# кстати по идее, если точек n, то треугольников можно составить n - 2 ?
# 3 - 2 = 1
# 4 - 2 = 2 - то есть мы соединяем три первые точки ...
# нет, еще больше -  C(n, 3) - C(k, 3), где k количество точек на одной прямой
# по идее, если бы вопрос был именно в том, сколько треугольников можно составить, то я бы ответил
# import math
# math.comb(n, 3) - math.comb(k, 3)
# надо найти k
# среди заданных точек нет совпадающих
# надо вообще сначала все точки собрать
# points = []
# k = 0
# for _ in range(n):    
#     x, y = map(int, input().split())    
#     points.append((x, y))
# я не очень понимаю, как посчитать точки, лежащие на одной прямой
# ...
# в любом случае это плохое решение так находить равнобедренные - это надо потом посчитать все разносторонние, 
# чтобы вычесть их из множества всех треугольников
# но если надо было бы посчитать количество всех треугольников, то

