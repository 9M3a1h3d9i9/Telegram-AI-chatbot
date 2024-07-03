from ply import yacc
from calc_lex import tokens

# Definition of CFG Grammar
def p_expression(p):
    '''expression : expression '+' term
                  | expression '-' term
                  | term'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]

def p_term(p):
    '''term : term '*' factor
            | term '/' factor
            | factor'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]

def p_factor(p):
    '''factor : '(' expression ')'
              | NUMBER'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

# Parsing error
def p_error(p):
    print(f"Syntax error at {p.value}")

# Build a parser
parser = yacc.yacc()

# A function to analyze a mathematical expression
def evaluate_expression(expression):
    result = parser.parse(expression)
    return result

if __name__ == '__main__':
    input_expression = "3 + 5 * (10 - 2)"
    result = evaluate_expression(input_expression)
    print(f"Input Expression: {input_expression}")
    print(f"Result: {result}")
