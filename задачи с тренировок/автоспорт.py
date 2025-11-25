def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, l, w = map(int, input().split())

    models = []
    for i in range(n):
        x, y, vx, vy = map(int, input().split())
        models.append({'id': i + 1, 'x': x, 'y': y, 'vx': vx, 'vy': vy, 't_fail': float('inf'), 't_finish': float('inf')})
    
    for model in models:
        x, y, vx, vy = model['x'], model['y'], model['vx'], model['vy']
        
        t_finish = float('inf')
        if vx > 0:
            t_finish = (l - x) / vx
                    
            if t_finish != float('inf'):
                y_finish = y + vy * t_finish
                
                if y_finish <= 1e-9 or y_finish >= w - 1e-9:
                    model['t_fail'] = t_finish
                    continue
        
        model['t_finish'] = t_finish
        
        t_board = float('inf')
        if vy > 0:
            t_board = (w - y) / vy
        elif vy < 0:
            t_board = (0 - y) / vy

        if t_board <= t_finish:
            model['t_fail'] = t_board
        else:
            model['t_fail'] = t_finish
            
    
    for i in range(n):
        for j in range(i + 1, n):
            model_i = models[i]
            model_j = models[j]

            if model_i['t_fail'] == 0 or model_j['t_fail'] == 0:
                 continue

            dx = model_i['x'] - model_j['x']
            dy = model_i['y'] - model_j['y']
            dvx = model_i['vx'] - model_j['vx']
            dvy = model_i['vy'] - model_j['vy']
            
            t_collision = float('inf')
            
            
            if dvx != 0 and dvy != 0:
                t_x = -dx / dvx
                t_y = -dy / dvy
                
            
                if abs(t_x - t_y) < 1e-9 and t_x >= 0:
                    t_collision = t_x
                            
            elif dvx != 0 and dvy == 0:
                if dy == 0:
                    t_collision = -dx / dvx if -dx / dvx >= 0 else float('inf')
                    
            elif dvx == 0 and dvy != 0:
                if dx == 0:
                    t_collision = -dy / dvy if -dy / dvy >= 0 else float('inf')
            
            if t_collision != float('inf') and t_collision > 0:         
                t_min_fail = min(model_i['t_fail'], model_j['t_fail'])
                if t_collision < t_min_fail - 1e-9:
                    model_i['t_fail'] = t_collision
                    model_j['t_fail'] = t_collision
                
                elif abs(t_collision - t_min_fail) < 1e-9:
                    is_i_finisher = abs(model_i['t_finish'] - t_collision) < 1e-9
                    is_j_finisher = abs(model_j['t_finish'] - t_collision) < 1e-9
                    
                    if is_i_finisher and is_j_finisher:
                        model_i['t_fail'] = float('inf')
                        model_j['t_fail'] = float('inf')
                    elif is_i_finisher and abs(model_i['t_fail'] - t_collision) < 1e-9:
                        model_i['t_fail'] = float('inf')
                    elif is_j_finisher and abs(model_j['t_fail'] - t_collision) < 1e-9:
                        model_j['t_fail'] = float('inf')
                    else:
                        if model_i['t_fail'] > t_collision + 1e-9:
                            model_i['t_fail'] = t_collision
                        if model_j['t_fail'] > t_collision + 1e-9:
                            model_j['t_fail'] = t_collision
    
    winning_time = float('inf')
    potential_winners = []

    for model in models:
        if model['t_fail'] != float('inf') and abs(model['t_fail'] - model['t_finish']) < 1e-9:
            potential_winners.append(model)
            if model['t_finish'] < winning_time:
                winning_time = model['t_finish']

    winners = []
    if winning_time != float('inf'):
        for model in potential_winners:
            if abs(model['t_finish'] - winning_time) < 1e-9:
                winners.append(model['id'])

    print(len(winners))
    if winners:
        winners.sort()
        print(*winners)

if __name__ == '__main__':
    main()