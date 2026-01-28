# в файле записан текст
# слово это последовательность непробельных символов идущих подряд
# слова разделены одним или бОльшим числом пробелов, переводами строк или символами конца строки
# определите сколько различных слов содержится в тексте

# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.

# {She, sells, sea, shore;, shore,, sure., shells.,  shells, on, the, shore, The, that, she, are, I'm, sure, So, if}

unique_words = set()
not_w = set([' '])
with open('input.txt') as f:    
    for line in f:        
        unique_words.update(set(line.split()))

print(len(unique_words))

