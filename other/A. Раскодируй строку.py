# iter 1
s = input()
n = len(s)
ans = ''
ai = 'abcdefghi'

num = ''
for i, ch in enumerate(s):           
    if len(num) < 2:
        num += ch
    else:
        if ch == '#':
            ans += chr(97 + int(num) - 1)
            num = ''
        else:
            ans += chr(97 + int(num[0]) - 1)
            num = num[1] + ch            

for i in num:
    ans += chr(97 + int(i) - 1)
print(ans)    
