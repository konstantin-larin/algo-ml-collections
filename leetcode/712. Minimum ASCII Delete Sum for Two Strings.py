from collections import deque
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """        
        if len(s1) > len(s2):
            s = s2
            S = s1
        else:
            s = s1
            S = s2        

        # 1) надо удалять по возможности буквы которые первые в алфавите
        # 2) надо удалять меньше букв
        # по идее ищем наименьшую по длине строку (или s1 в случае равенства) в дальнейшем называем s малую и S большую
        # мы должны найти подстроку из s в S, удаляя элементы по очереди
        # dp - мы имеем некоторую подстроку s и ищем ее вхождение в S
        sum_s = sum(map(ord, s))
        sum_S = sum(map(ord, S))
        


        

        

Solution().minimumDeleteSum('sea', 'eat')