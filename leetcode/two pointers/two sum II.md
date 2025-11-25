---
tags:
  - problem
level: medium
---
Дата: [[15-09-2025]]
Ссылка:https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150

```python
class Solution(object):

    def twoSum(self, numbers, target):

        """

        :type numbers: List[int]

        :type target: int

        :rtype: List[int]

        """

        n = len(numbers)

        if n <= 2:

            return [1, 2]

        p1 = 0

        p2 = n - 1

        while p1 != p2:

            s = numbers[p1] + numbers[p2]

            if s == target:

                return [p1 + 1, p2 + 1]

            if s < target:

                p1 +=1

            if s > target:

                p2 -=1
```

