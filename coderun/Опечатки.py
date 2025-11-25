"""
Двусторонний BFS
"""

import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    right_word = input()
    source_word = input()
    n = int(input())
    rules = []
    for _ in range(n):
        str1, str2 = input().split()
        if str1 != str2:
            rules.append((str1, str2))
    if right_word == source_word:
        return 0

    from_right = {right_word}
    from_source = {source_word}
    from_right_visited = {right_word}
    from_source_visited = {source_word}
    from_right_steps = 0
    from_source_steps = 0
    while from_right_steps + from_source_steps < 4 and from_right and from_source:
        if len(from_right) <= len(from_source):
            from_right_steps += 1
            next_from_right = set()
            for word in from_right:
                for s1, s2 in rules:
                    if s1 not in word:
                        continue

                    for i in range(len(word) - len(s1) + 1):
                        if word[i : i + len(s1)] == s1:
                            new_word = word[:i] + s2 + word[i + len(s1) :]
                            if new_word in from_source:
                                return from_right_steps + from_source_steps
                            if new_word not in from_right_visited:
                                from_right_visited.add(new_word)
                                next_from_right.add(new_word)
            from_right = next_from_right
        else:
            from_source_steps += 1
            next_from_source = set()
            for word in from_source:
                for s1, s2 in rules:
                    if s2 not in word:
                        continue
                    for i in range(len(word) - len(s2) + 1):
                        if word[i : i + len(s2)] == s2:
                            new_word = word[:i] + s1 + word[i + len(s2) :]
                            if new_word in from_right:
                                return from_right_steps + from_source_steps
                            if new_word not in from_source_visited:
                                from_source_visited.add(new_word)
                                next_from_source.add(new_word)
            from_source = next_from_source

    return -1


if __name__ == "__main__":
    print(main())
