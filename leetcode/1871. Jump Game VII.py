from collections import deque
class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        n = len(s)
        if s[n - 1] == '1':
            return False

        que = deque([0])                             
        mx = 0

        while que:
            i = que.popleft()
            for j in range(max(i + minJump, mx + 1), min(i + maxJump + 1, n)):
                if s[j] == '0':
                    if j == n - 1:
                        return True                    
                    que.append(j)                    
            mx = i + maxJump
        return False
    

print(Solution().canReach(s, minJump = 1, maxJump = 49999))
            
