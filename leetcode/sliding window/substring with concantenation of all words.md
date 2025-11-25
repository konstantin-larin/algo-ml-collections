---
tags:
  - problem
level: hard
---
Дата: [[15-09-2025]]
Ссылка: https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/?envType=study-plan-v2&envId=top-interview-150


провал на ээтом кейсе почему-то

![[Pasted image 20250915121015.png]]

ясно, что мы рассматриваем все возможные варианты путем перебора смещений последовательности, от 0, до lw -1, это логично, что таким образом мы рассмотрим все возможные окна. 

```python
from collections import Counter

class Solution(object):

    def findSubstring(self, s, words):

        """

        :type s: str

        :type words: List[str]

        :rtype: List[int]

        """

        lw = len(words[0])

        n = len(words)

        ls = len(s)

        indices = []        

        words_counter = Counter(words)

        for offset in range(lw):

            left = offset

            right = offset

            window_counter = Counter()

            count = 0

  

            while right + lw <= ls:

                word = s[right:right+lw]

                right += lw

  

                if word in words_counter:

                    window_counter[word] += 1

                    count += 1

  

                    while window_counter[word] > words_counter[word]:

                        left_word = s[left:left+lw]

                        window_counter[left_word] -= 1

                        count -= 1

                        left += lw

                    if count == n:

                        indices.append(left)

                        left_word = s[left:left+lw]

                        window_counter[left_word] -= 1

                        count -= 1

                else:

                    window_counter.clear()

                    count = 0

                    left = right

        return indices
```

