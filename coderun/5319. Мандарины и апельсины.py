# https://coderun.yandex.ru/problem/new-year-fruits
import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    print('Yes')


if __name__ == '__main__':
    main()



# Я ПЫТАЛСЯ ПОДОБРАТЬ КЕЙС НА NO, НО У МЕНЯ НЕ ПОЛУЧИЛОСЬ - ПАЛО ПОДОЗРЕНИЕ, ЧТО ЕГО НЕ СУЩЕСТВУЕТ, НАПИСАЛ РАБОЧЕЕ ПРОСТО РЕШЕНИЕ ВЫШЕ
# По сути я описал ниже оптимальный алгоритм, которым Кодерун будет брать ящики
# import sys


# def main():
#     """
#     Пример ввода и вывода числа n, где -10^9 < n < 10^9:
#     n = int(input())
#     print(n)
#     """
#     n = int(input())
#     boxes_taken = [False] * (2 * n -1)
#     oranges = [0] * (2 * n - 1)
#     mandarins = [0] * (2 * n - 1)

#     M = 0
#     O = 0
#     for i in range(2 * n - 1):
#         m, o = map(int, input().split())
#         M += M
#         O += o
#         mandarins[i], oranges[i] = m, o
#     M_HALF = M // 2
#     O_HALF = O // 2

#     mandarins_sorted = sorted(
#         ((value, idx) for idx, value in enumerate(mandarins)),
#         key=lambda x: x[0]
#     )

#     oranges_sorted = sorted(
#         ((value, idx) for idx, value in enumerate(oranges)),
#         key=lambda x: x[0]
#     )    

#     print(mandarins_sorted)
#     print(oranges_sorted)

#     # стратегия простая по очереди берем ящик с наибольшим количеством апельсинов / наибольшим количеством мандаринов
#     switcher = 'mandarin' 
#     mandarin_caret = 2 * n - 2
#     orange_caret = 2 * n - 2

#     boxes_count = 0

#     M_EXIST = 0
#     O_EXIST = 0
#     while boxes_count < n:
#         if mandarin_caret < 0 and orange_caret < 0: # на всякий
#             break
#         if switcher == 'mandarin':
#             if mandarin_caret < 0:
#                 continue
#             m, i = mandarins_sorted[mandarin_caret]                                        
#             mandarin_caret -= 1

#             if boxes_taken[i]:
#                 continue
#             o = oranges[i]                                   
#             switcher = 'orange'

#         else:
#             if orange_caret < 0:
#                 continue
#             o, i = oranges_sorted[orange_caret]                
#             orange_caret -= 1
#             if boxes_taken[i]:
#                 continue
#             m = mandarins[i]                        
#             switcher = 'mandarin'
    
#         boxes_count += 1
#         M_EXIST += m
#         O_EXIST += o
#         # print('//')
#         # print(M_EXIST, O_EXIST)

#     if M_EXIST >= M_HALF and O_EXIST >= O_HALF:
#         print('YES')
#     else:
#         print('NO')
#     # pass


# if __name__ == '__main__':
#     main()
