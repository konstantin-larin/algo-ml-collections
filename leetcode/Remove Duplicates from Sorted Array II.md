---
tags:
  - problem
level: medium
---
Дата: [[15-09-2025]]
Ссылка: 
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

[[Remove Duplicates from Sorted Array]]


Общее решение 


```python

class Solution(object):

    def removeDuplicates(self, nums, d=2):

        """

        :type nums: List[int]

        :rtype: int

        """  

        n = len(nums)

        if n <= d:

            return n

        k = 1 # это и счетчик уникальных значений и указатель

        p = 1                                            

        while p < n:

            if k > d - 1 and nums[p] == nums[k - d]:

                nums[p] = '_'                                      

            else:                                

                k += 1                        

                nums[p], nums[k - 1] = nums[k - 1], nums[p]

            p += 1

        return k
        
```

## Ревью
