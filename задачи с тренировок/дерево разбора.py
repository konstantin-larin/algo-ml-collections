import sys

# Увеличим лимит рекурсии для длинных выражений
sys.setrecursionlimit(2000)

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.height = 0
        self.width = 0
        self.text = []
        self._format_tree()

    def _format_tree(self):        
        if self.left is None and self.right is None:
            # Случай: Лист (Переменная)
            self.text = [self.value]
            self.height = 1
            self.width = 1
            return

        # Случай: Внутренний узел (Оператор)
        T1, T2 = self.left, self.right
        
        h1, w1 = T1.height, T1.width
        h2, w2 = T2.height, T2.width
        
        h = max(h1, h2) + 2
        w = w1 + w2 + 5
        self.height = h
        self.width = w
        
        # Индекс строки, на которой будет корневой оператор
        op_row = h - 1 
        
        # Индексы, где будут центры поддеревьев в этой строке (T1, T2)
        # Центр T1 всегда в T1.width // 2
        T1_center = w1 // 2
        # Центр T2: T1.width + 5 + T2.width // 2
        T2_center = w1 + 5 + w2 // 2

        # Оператор в формате [op]
        op_str = f'[{self.value}]'
        op_len = len(op_str)
        # Центр оператора в новой строке
        op_center = T1_center + (T2_center - T1_center) // 2 
        
        # Сдвиг для T1 и T2
        T1_pad = T1_center
        T2_pad = w1 + 5 + w2 - (T2_center + 1)
        
        # Строка с оператором
        root_line = list(' ' * w)
        # Запись оператора [op]
        op_start = op_center - op_len // 2
        op_end = op_start + op_len
        root_line[op_start:op_end] = list(op_str)
        
        # Соединители '----'
        # Левая часть
        for i in range(op_start):
             root_line[i] = '-'
        # Правая часть
        for i in range(op_end, w):
             root_line[i] = '-'
        
        root_line[T1_center] = '.' # Соединитель с левой веткой
        root_line[T2_center] = '.' # Соединитель с правой веткой

        # Строка с ветками
        branch_line = list(' ' * w)
        branch_line[T1_center] = '|'
        branch_line[T2_center] = '|'
        
        # Строки для T1 и T2, дополненные пробелами
        
        # Дополняем T1 до нужной высоты h-2 (op_row - 1)
        T1_padded = [' ' * w1] * (h - 2 - h1) + T1.text
        # Дополняем T2 до нужной высоты h-2 (op_row - 1)
        T2_padded = [' ' * w2] * (h - 2 - h2) + T2.text
        
        # Сборка итогового текста дерева (h-2 строк)
        self.text = []
        for i in range(h - 2):
            left_part = T1_padded[i]
            # Центральный интервал ('     ')
            center_part = ' ' * 5 
            right_part = T2_padded[i]
            self.text.append(left_part + center_part + right_part)

        # Добавление ветки
        self.text.append(" " * T1_center + "|" + " " * (T2_center - T1_center - 1) + "|" + " " * (w - T2_center - 1))    
        # Добавление корня
        self.text.append("".join(root_line))            
        
        
        new_text = []
        
        
        new_text.append("".join(root_line).replace('[', ' ').replace(']', ' '))
                
        new_text.append(branch_line[op_center-1].replace('|', ' ') + branch_line[op_center].replace('.', '|') + branch_line[op_center+1].replace('|', ' ')) # Костыль для центровки оператора (корень)
                
        max_sub_h = max(h1, h2)
        
        for i in range(max_sub_h):            
            t1_line = T1.text[i] if i < h1 else ' ' * w1
            t2_line = T2.text[i] if i < h2 else ' ' * w2
                        
            center_line = ' ' * 5
            
            new_text.append(t1_line + center_line + t2_line)
        
        max_h_sub = max(h1, h2)
        
        T1_lines = [' ' * w1] * (max_h_sub - h1) + T1.text
        T2_lines = [' ' * w2] * (max_h_sub - h2) + T2.text
        
        self.text = []
        
        
        op_root_pos = w1 + 2 
        op_end_pos = w1 + 2 + op_len - 1 
        
        root_line = list(' ' * w)
        root_line[T1_center] = '.'
        root_line[T2_center] = '.'
        root_line[op_root_pos:op_end_pos+1] = list(op_str)
        
        for i in range(T1_center + 1, op_root_pos): root_line[i] = '-'
        for i in range(op_end_pos + 1, T2_center): root_line[i] = '-'
        
        self.text.append("".join(root_line))
        
        branch_line = list(' ' * w)
        branch_line[T1_center] = '|'
        branch_line[T2_center] = '|'
        self.text.append("".join(branch_line))
                
        for i in range(max_h_sub):
            t1_line = T1_lines[i]
            t2_line = T2_lines[i]
            # Центральный интервал - 5 символов
            center_padding = ' ' * 5 
            self.text.append(t1_line + center_padding + t2_line)
            
        # Обновление размеров:
        self.height = max_h_sub + 2
        self.width = w


class Parser:
    def __init__(self, expression):
        # Удаляем пробелы для упрощения
        self.expression = expression.replace(' ', '')
        self.pos = 0

    def _peek(self):        
        if self.pos < len(self.expression):
            return self.expression[self.pos]
        return None

    def _consume(self, expected=None):        
        char = self._peek()
        if expected and char != expected:
            raise ValueError(f"Ожидался '{expected}', получен '{char}'")
        if char is not None:
            self.pos += 1
        return char

    def _is_variable(self, char):        
        return char and 'a' <= char <= 'z'
    
    def _parse_expression(self):
        # Сначала парсим слагаемое
        node = self._parse_term()
        
        # Итеративный парсинг левоассоциативных операторов (+, -)
        while self._peek() in ('+', '-'):
            op = self._consume()
            right_node = self._parse_term()
            # Создаем новый корень с оператором и старым деревом как левым поддеревом
            node = Node(op, node, right_node)
        
        return node

    # <слагаемое> -> <множитель> | <слагаемое> * <множитель> | <слагаемое> / <множитель>
    def _parse_term(self):        
        # Сначала парсим множитель
        node = self._parse_factor()
        
        # Итеративный парсинг левоассоциативных операторов (*, /)
        while self._peek() in ('*', '/'):
            op = self._consume()
            right_node = self._parse_factor()
            # Создаем новый корень с оператором и старым деревом как левым поддеревом
            node = Node(op, node, right_node)
            
        return node

    # <множитель> -> <элемент> | <элемент> ^ <множитель>
    def _parse_factor(self):        
        # Сначала парсим элемент
        node = self._parse_element()
        
        # Рекурсивный парсинг правоассоциативного оператора (^)
        if self._peek() == '^':
            op = self._consume()
            # В отличие от левоассоциативных, правая часть это _parse_factor
            right_node = self._parse_factor()
            # Создаем новый корень
            node = Node(op, node, right_node)
            
        return node
    
    def _parse_element(self):                
        char = self._peek()
        
        if self._is_variable(char):
            self._consume()
            return Node(char)
        
        elif char == '(':
            # (<выражение>)
            self._consume('(')
            node = self._parse_expression()
            self._consume(')')
            # Дерево для элемента в скобках - это дерево для самого выражения
            return node
            
        else:
            raise ValueError(f"Неожиданный символ '{char}' на позиции {self.pos}")

    def parse(self):        
        if not self.expression:
            return None
        return self._parse_expression()


def main():
    expression = input()        

    parser = Parser(expression)
    tree_root = parser.parse()
    
    if tree_root:        
        for line in tree_root.text:
            print(line)
            
if __name__ == '__main__':
    main()