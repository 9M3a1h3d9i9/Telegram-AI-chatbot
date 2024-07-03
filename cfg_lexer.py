from ply import lex


tokens = [
    "NOUN",
    "VERB"
]

t_NOUN = r"cat|dog|bird"
t_VERB = r"runs|jumps|flies"

t_ignore = " \t"

def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == '__main__':
    input_sentence = "dog jumps"
    lexer.input(input_sentence)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
