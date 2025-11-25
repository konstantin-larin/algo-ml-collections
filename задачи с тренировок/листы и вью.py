import sys



def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    memory = {
        # name: {'type': sublist|list, 'data': []}
    }
    n = int(input())
    for _ in range(n):        
        command = input()
        split_by_spaces = command.split()
        len_split_by_spaces = len(split_by_spaces)
        if len_split_by_spaces == 1:
            # это работа с существующим списком
            exp, method = split_by_spaces[0].split('.')            
            method_name = ''
            for j, ch in enumerate(method):
                if ch == '(':
                    break
                method_name += ch
            obj = memory[exp]
            if obj['type'] == 'list':
                data = obj['data']
                if method_name == 'add':
                    x = int(method[j+1:-1])                
                    data.append(x) 
                    continue                                    
            else:
                if method_name == 'add': continue
                data = memory[obj['parent']]['data']                
        
            if method_name == 'set':
                i, x = map(int, method[j + 1:-1].split(','))
                if obj['type'] == 'sublist':
                    i = obj['from'] + i                    
                data[i -1] = x
            if method_name == 'get':
                i = int(method[j+1:-1])
                if obj['type'] == 'sublist':
                    i = obj['from'] + i     
                print(data[i-1])
                               

        elif len_split_by_spaces == 4:
            # это создание sublist
            exp = split_by_spaces[1]
            parent_exp, args = split_by_spaces[-1].split('.')
            _from, _to = map(int, args[8:-1].split(','))
            parent = memory[parent_exp]
            child = {'type': 'sublist'}
            if parent['type'] == 'list':
                child['parent'] = parent_exp
                child['from'] = _from - 1
                child['to'] = _to 
            else:
                child['parent'] = parent['parent']
                child['from'] = parent['from'] + _from - 1
                child['to'] = parent['from'] + _to
            memory[exp] = child
        else:
            # это создание new list            
            exp = split_by_spaces[1]
            args = list(map(int, split_by_spaces[-1][5:-1].split(',')))
            memory[exp] = {
                'type': 'list',
                'data': args
            }

    # print(memory)
if __name__ == '__main__':
    main()
