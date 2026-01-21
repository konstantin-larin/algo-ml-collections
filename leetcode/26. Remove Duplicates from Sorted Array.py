class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 1
        k = 1        
        for i in range(1, n):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k  

print(Solution().removeDuplicates([1,1,2]))