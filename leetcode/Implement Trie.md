---
tags:
  - problem
level: medium
---
Дата: [[15-06-2025]]

# Ссылка: 
https://leetcode.com/problems/implement-trie-prefix-tree/description/?envType=study-plan-v2&envId=top-interview-150

# Понимание условия
 - Ограничения по времени/памяти
 - Диапазоны входных данных
 - Разбери все случаи, включая крайние, которые будет решать код

Надо изучить эту структуру.
# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер
# Код
```python
class TrieNode:

    def __init__(self):

        self.children = {}

        self.is_end_of_word = False        

class Trie(object):

    def __init__(self):

        self.root = TrieNode()

  

    def insert(self, word):

        """

        :type word: str

        :rtype: None

        """

        current_node = self.root

        for char in word:

            if char not in current_node.children:

                current_node.children[char] = TrieNode()

            current_node = current_node.children[char]

        current_node.is_end_of_word = True            

    def search(self, word):

        """

        :type word: str

        :rtype: bool

        """

        current_node = self.root

        for char in word:

            if char not in current_node.children:

                return False

            current_node = current_node.children[char]

        return current_node.is_end_of_word

  

    def startsWith(self, prefix):

        """

        :type prefix: str

        :rtype: bool

        """

        current_node = self.root

        for char in prefix:

            if char not in current_node.children:

                return False

            current_node = current_node.children[char]

        return True

  
  

# Your Trie object will be instantiated and called as such:

# obj = Trie()

# obj.insert(word)

# param_2 = obj.search(word)

# param_3 = obj.startsWith(prefix)
```
# Ревью
Интересная структура для поиска вхождений слов.