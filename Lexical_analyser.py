import string

# Definição dos tokens
ARRAY, BOOLEAN, BREAK, CHAR, CONTINUE, DO, ELSE, FALSE, FUNCTION, IF, INTEGER, OF, STRING, STRUCT, TRUE, TYPE, VAR, WHILE = range(18)
COLON, SEMI_COLON, COMMA, EQUALS, LEFT_SQUARE, RIGHT_SQUARE, LEFT_BRACES, RIGHT_BRACES, LEFT_PARENTHESIS, RIGHT_PARENTHESIS, AND, OR, LESS_THAN, GREATER_THAN, LESS_OR_EQUAL, GREATER_OR_EQUAL, NOT_EQUAL, EQUAL_EQUAL, PLUS, PLUS_PLUS, MINUS, MINUS_MINUS, TIMES, DIVIDE, DOT, NOT = range(18, 44)
CHARACTER, NUMERAL, STRINGVAL, ID, UNKNOWN = range(44, 49)

# Palavras reservadas
keywords = {
    'array': ARRAY, 'boolean': BOOLEAN, 'break': BREAK, 'char': CHAR, 'continue': CONTINUE,
    'do': DO, 'else': ELSE, 'false': FALSE, 'function': FUNCTION, 'if': IF,
    'integer': INTEGER, 'of': OF, 'string': STRING, 'struct': STRUCT, 'true': TRUE,
    'type': TYPE, 'var': VAR, 'while': WHILE
}

# Tabelas de constantes
const_pool = []
const_type = []
const_dict = {'char': 0, 'int': 1, 'string': 2}

def add_char_const(c):
    const_pool.append(c)
    return len(const_pool) - 1

def add_int_const(n):
    const_pool.append(n)
    return len(const_pool) - 1

def add_string_const(s):
    const_pool.append(s)
    return len(const_pool) - 1

def get_const_value(index):
    return const_pool[index]

# Tabela de identificadores
name_table = {}
number_to_name_table = {}
name_counter = 0

def search_name(name):
    global name_counter
    if name in name_table:
        return name_table[name]
    else:
        name_table[name] = name_counter
        number_to_name_table[name_counter] = name
        name_counter += 1
        return name_table[name]
    
def get_name_by_number(number):
    return number_to_name_table.get(number, None)

# Leitura do arquivo de entrada
def read_char(file):
    return file.read(1)

# Função principal do analisador léxico
def next_token(file):
    global next_char
    next_char = read_char(file)
    
    while next_char.isspace():
        next_char = read_char(file)
    
    if next_char.isalpha():
        text = []
        while next_char.isalnum() or next_char == '_':
            text.append(next_char)
            next_char = read_char(file)
        text = ''.join(text)
        if text in keywords:
            return keywords[text], None
        else:
            return ID, search_name(text)
    
    elif next_char.isdigit():
        numeral = []
        while next_char.isdigit():
            numeral.append(next_char)
            next_char = read_char(file)
        return NUMERAL, add_int_const(int(''.join(numeral)))
    
    elif next_char == '"':
        string = []
        next_char = read_char(file)
        while next_char != '"':
            string.append(next_char)
            next_char = read_char(file)
        next_char = read_char(file)  # Skip the closing quote
        return STRINGVAL, add_string_const(''.join(string))
    
    elif next_char == "'":
        next_char = read_char(file)
        char_value = next_char
        next_char = read_char(file)  # Skip the closing '
        return CHARACTER, add_char_const(char_value)
    
    elif next_char == ':':
        next_char = read_char(file)
        return COLON, None
    
    elif next_char == ';':
        next_char = read_char(file)
        return SEMI_COLON, None
    
    elif next_char == ',':
        next_char = read_char(file)
        return COMMA, None
    
    elif next_char == '=':
        next_char = read_char(file)
        if next_char == '=':
            next_char = read_char(file)
            return EQUAL_EQUAL, None
        else:
            return EQUALS, None
    
    elif next_char == '[':
        next_char = read_char(file)
        return LEFT_SQUARE, None
    
    elif next_char == ']':
        next_char = read_char(file)
        return RIGHT_SQUARE, None
    
    elif next_char == '{':
        next_char = read_char(file)
        return LEFT_BRACES, None
    
    elif next_char == '}':
        next_char = read_char(file)
        return RIGHT_BRACES, None
    
    elif next_char == '(':
        next_char = read_char(file)
        return LEFT_PARENTHESIS, None
    
    elif next_char == ')':
        next_char = read_char(file)
        return RIGHT_PARENTHESIS, None
    
    elif next_char == '&':
        next_char = read_char(file)
        if next_char == '&':
            next_char = read_char(file)
            return AND, None
        else:
            return UNKNOWN, None
    
    elif next_char == '|':
        next_char = read_char(file)
        if next_char == '|':
            next_char = read_char(file)
            return OR, None
        else:
            return UNKNOWN, None
    
    elif next_char == '<':
        next_char = read_char(file)
        if next_char == '=':
            next_char = read_char(file)
            return LESS_OR_EQUAL, None
        else:
            return LESS_THAN, None
    
    elif next_char == '>':
        next_char = read_char(file)
        if next_char == '=':
            next_char = read_char(file)
            return GREATER_OR_EQUAL, None
        else:
            return GREATER_THAN, None
    
    elif next_char == '!':
        next_char = read_char(file)
        if next_char == '=':
            next_char = read_char(file)
            return NOT_EQUAL, None
        else:
            return NOT, None
    
    elif next_char == '+':
        next_char = read_char(file)
        if next_char == '+':
            next_char = read_char(file)
            return PLUS_PLUS, None
        else:
            return PLUS, None
    
    elif next_char == '-':
        next_char = read_char(file)
        if next_char == '-':
            next_char = read_char(file)
            return MINUS_MINUS, None
        else:
            return MINUS, None
    
    elif next_char == '*':
        next_char = read_char(file)
        return TIMES, None
    
    elif next_char == '/':
        next_char = read_char(file)
        return DIVIDE, None
    
    elif next_char == '.':
        next_char = read_char(file)
        return DOT, None
    
    elif next_char == '!':
        next_char = read_char(file)
        return NOT, None
    
    else:
        return UNKNOWN, None

# Testando o analisador léxico
if __name__ == "__main__":
    with open('Tests/Test4.txt', 'r') as file:
        token, token_secondary = next_token(file)
        while token!=None:
            if token == UNKNOWN and token_secondary is None:
                break
            if(token_secondary != None):
                if(token in [44, 45, 46]):
                    print(f"Token: {token}, Token Secundário: {token_secondary}, Literal: {get_const_value(token_secondary)}")
                elif(token == 47):
                        print(f"Token: {token}, Token Secundário: {token_secondary}, Id: {get_name_by_number(token_secondary)}")
            else: print(f"Token: {token}, Token Secundário: {token_secondary}, Literal: None")
            token, token_secondary = next_token(file)
