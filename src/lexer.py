# -*- coding: utf-8 -*-
import sys
import getopt
import re
import ply.lex as lex


palavras_reservadas = {
    'bool': 'BOOL',
    'string': 'STRING',
    'int': 'INT',
    'for': 'FOR',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'true': 'TRUE',
    'false': 'FALSE',
    'return': 'RETURN',
    'break': 'BREAK',
    'read': 'READ',
    'write': 'WRITE',
}


tokens = [
    'ID', 'CADEIA', 'NUMBER',
    'ABREPAREN', 'FECHAPAREN',
    'ABRECOLCH', 'FECHACOLCH',
    'ABRECHAVE', 'FECHACHAVE',
    'VIRGULA', 'PONTOVIRGULA',
    'MAIS', 'MENOS', 'MULT', 'DIV', 'MOD',
    'IGUAL', 'DIFERENTE',
    'MAIOR', 'MAIORIGUAL', 'MENOR', 'MENORIGUAL',
    'OU', 'E', 'NEG',
    'ATRIB', 'MAISATRIB', 'MENOSATRIB',
    'MULTATRIB', 'DIVATRIB', 'MODATRIB', 'SINAL',
    'TERNARIOSE', 'TERNARIOSENAO',
] + list(palavras_reservadas.values())


t_MAIS = r'\+'
t_MENOS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_IGUAL = r'=='
t_ABREPAREN = r'\('
t_FECHAPAREN = r'\)'
t_ABRECOLCH = r'\['
t_FECHACOLCH = r'\]'
t_ABRECHAVE = r'\{'
t_FECHACHAVE = r'\}'
t_VIRGULA = r','
t_PONTOVIRGULA = r';'
t_DIFERENTE = r'!='
t_MAIOR = r'>'
t_MAIORIGUAL = r'>='
t_MENOR = r'<'
t_MENORIGUAL = r'<='
t_OU = r'\|\|'
t_E = r'&&'
t_NEG = r'!'
t_SINAL = r'-'
t_ATRIB = r'='
t_MAISATRIB = r'\+='
t_MENOSATRIB = r'-='
t_MULTATRIB = r'\*='
t_DIVATRIB = r'/='
t_MODATRIB = r'%='
t_TERNARIOSE = r'\?'
t_TERNARIOSENAO = r':'
t_CADEIA = r'\"(\n|.)*?\"'
t_ignore = " \t\v\r"


def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor Inteiro muito grande %d", t.value)
        t.value = 0
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    column = find_column(t.lexer.lexdata, t)
    print('LexError(%s,%r,%d,%d)' % (t.type, t.value, t.lineno, column))
    # print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = palavras_reservadas.get(t.value, 'ID')
    return t


def t_comment_multiline(t):
    r'((//.*)|(/\*(.|\n)*\*/))'
    # No return value. Token discarded
    pass


def find_column(input, token):
    last_cr = input.rfind('\n', 0, lex.lexer.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (lex.lexer.lexpos - last_cr) + 1
    return column


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hf:", ["file"])
    except getopt.GetoptError:
        print('program.py -f <file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('program.py -f <file>')
            sys.exit()
        elif opt in ("-f", "--file"):
            f = arg

    input_ = ''
    with open(f, 'r') as file:
        file = open(f, 'r')
        for line in file:
            input_ += line

    lexer = lex.lex()
    # Give the lexer some input
    lexer.input(input_)

    token_list = []
    # Tokenize
    while True:
        tok = lexer.token()
        column = find_column(input_, tok)
        if not tok:
            break      # No more input
        token_list.append(tok)
        # print('LexToken(%s,%r,%d,%d)' % (tok.type, tok.value, tok.lineno, column))

    file.close()


main(sys.argv[1:])
