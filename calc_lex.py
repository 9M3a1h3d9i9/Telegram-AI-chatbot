from ply import lex

# Definition of tokens
tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN'
]

# Define relationships between tokens and string patterns
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# NUMBER token definition that contains integers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignore spaces and tabs
t_ignore = ' \t'

# Error if an unknown character is detected
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

# Build a lexer
lexer = lex.lex()

if __name__ == '__main__':
    # Test the lexer
    lexer.input("3 + 5 * (10 - 2)")
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
