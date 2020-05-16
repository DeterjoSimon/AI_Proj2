import logging
import ply.yacc as yacc

from engine.logic_operators import *

tokens = (
    'PROPOSITION', 'AND', 'OR',
    'IMPLICATION', 'BICONDITIONAL',
    'NOT', 'LPAREN', 'RPAREN',
)

# Tokens
t_AND = r'\band\b|&'  # Match 'and' or &
t_OR = r'\bor\b| \|'  # Match 'or' or '|'
t_IMPLICATION = r'->|=>'  # Match -> or =>
t_BICONDITIONAL = r'<->|<=>'  # Match <-> or <=>
t_NOT = r'\bnot\b|-(?!>)|~'  # Match not or - (not succeeded by '>') or ~
t_LPAREN = r'\('  # Match (
t_RPAREN = r'\)'  # Match )
t_PROPOSITION = r'[a-z]'  # Match any single char, lowercase

# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
import ply.lex as lex

lexer = lex.lex()

# Parsing rules

precedence = (
    ('left', 'AND'),
    ('left', 'OR'),
    ('left', 'IMPLICATION', 'BICONDITIONAL'),
    ('left', 'NOT')
)

# dictionary of names
names = {}


def p_statement_expr(t):
    'statement : expression'
    t[0] = t[1]


def p_expression_proposition(t):
    'expression : PROPOSITION'
    t[0] = Proposition(t[1])


def p_expression_and(t):
    'expression : expression AND expression'
    t[0] = And(t[1], t[3])


def p_expression_or(t):
    'expression : expression OR expression'
    t[0] = Or(t[1], t[3])


def p_expression_implication(t):
    'expression : expression IMPLICATION expression'
    t[0] = Implication(t[1], t[3])


def p_expression_biconditional(t):
    'expression : expression BICONDITIONAL expression'
    t[0] = Biconditional(t[1], t[3])


def p_expression_negation(t):
    'expression : NOT expression'
    t[0] = Not(t[2])


def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]


def p_error(t):
    print("Syntax error at '%s'" % t.value)


log = logging.getLogger()
parser = yacc.yacc()


def parse(s):
    return parser.parse(s)


if __name__ == '__main__':
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        result = parser.parse(s, debug=log)
        print(result)
