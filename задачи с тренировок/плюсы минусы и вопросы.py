from pdb import set_trace

n, m = map(int, input().split())
cols = [0 for _ in range(m)]
# идея - выбрать потенциально самую большую строку в приоритете - с меньшим количеством "?" (чтоб туда можно было вставить -)

 # количество плюсов, количество вопросов, индексы вопросов в строке (то есть индексы cols) - cols[question_i][row_i] = '+' для самой максимальной row
max_plus_count = 0
max_q_count = 0
max_q_indices = set()

for i in range(n):        
    potential_max_plus_count = max_plus_count + max_q_count
    s = "".join(input().split())    
    
    plus_count = q_count = 0
    q_indices = set()
    for j, ch in enumerate(s):        
        if ch == '+':
            plus_count += 1
            cols[j] += 1
        if ch == '-':
            cols[j] -= 1
        if ch == '?':
            q_count += 1
            q_indices.add(j)
            cols[j] -= 1    
    print(cols)
    potential_plus_count = plus_count + q_count    
    # set_trace()
    if (potential_plus_count == potential_max_plus_count and plus_count > max_plus_count) or (potential_plus_count > potential_max_plus_count):
        max_plus_count = plus_count 
        max_q_count = q_count
        max_q_indices = q_indices

print(cols)
for j in max_q_indices:
    cols[j] += 2
print(cols)
print(2 * (max_plus_count + max_q_count) - m - min(cols))




    