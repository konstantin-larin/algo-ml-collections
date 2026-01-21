class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        k = 0
        nums_len = len(nums)
        while nums_len > (1 << k):
            k += 1
        self.n = 1 << k
        self.NEUTRAL = 0 # because any num + 0 = num
        self.tree = [self.NEUTRAL] * (2*self.n - 1)
        for i in range(nums_len):
            self.tree[i + self.n - 1] = nums[i]
        for i in range(self.n - 2, -1, -1):
            self.tree[i] = self.tree[2 * i + 1] + self.tree[2 * i + 2]            
        

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        i = self.n - 1 + index
        self.tree[i] = val        
        while i > 0:
            i = (i - 1) // 2
            self.tree[i] = self.tree[2 * i + 1] + self.tree[2 * i + 2]
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """        

        def query(l, r, i):
            if left <= l and right >= r: # полное перекрытие
                return self.tree[i]
            if right < l or left > r: # вообще нет перекрытия
                return self.NEUTRAL         
            li = 2 * i + 1
            ri = 2 * i + 2

            mid = (l + r) // 2
            return query(l, mid, li) + query(mid + 1, r, ri) # частичное перекрытие - ищем точный ответ у детей
        return query(0, self.n - 1, 0)    

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)