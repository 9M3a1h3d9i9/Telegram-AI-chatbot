from ply import yacc
from cfg_lexer import tokens  # We import the tokens from our lexer file that generates the tokens

# Definition of CFG Grammar
def p_sentence(p):
    '''sentence : noun verb'''
    p[0] = f"{p[1]} {p[2]}"

def p_noun(p):
    '''noun : "cat" | "dog" | "bird"'''
    p[0] = p[1]

def p_verb(p):
    '''verb : "runs" | "jumps" | "flies"'''
    p[0] = p[1]


def p_error(p):
    print(f"Syntax error at {p.value}")


parser = yacc.yacc()

# Function to analyze a sentence
def analyze_sentence(sentence):
    result = parser.parse(sentence)
    return result

if __name__ == '__main__':
    input_sentence = "dog jumps"
    result = analyze_sentence(input_sentence)
    print(f"Input Sentence: {input_sentence}")
    print(f"Analyzed Result: {result}")
