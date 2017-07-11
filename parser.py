# -*- coding: utf-8 -*-

import ply.yacc as yacc

from lexer import *

names = { }

# print tokens

# def p_program(t):
#     # <program> => <SequenciaDeclaracao>
#     pass

# def p_declaracao(t):
#     # <declaracao> => <declaracaoVariavel>
#     #               | id '(' <listaParametros> ')' '{' <bloco> '}'
#     #               | <tipo> id '(' <listaParametros> ')' '{' <bloco> '}'
#     pass

# def p_declaracao_variavel(t):
#     # <declaracaoVariavel> => <tipo> <sequenciaSpecVariavel> ';'
#     pass

# def p_especificacao_variavel(t):
#     # <especificacaoVariavel> => id
#     #                          | id '=' <literal>
#     #                          | id '[' numero ']'
#     #                          | id '[' numero ']' '=' '{' <sequenciaLiteral> '}'
#     pass

# def p_tipo(t):
#     # <tipo> => "int"
#     #         | "string"
#     #         | "bool"
#     pass

# def p_parametros(t):
#     # <parametros> => <tipo> id
#     #               | <tipo> id '[' ']'
#     pass

# def p_bloco(t):
#     # <bloco> => <listaDeclaracaoVariavel> <listaComandos> 
#     pass

# def p_comando(t):
#     # <comando> => <comandoIF>
#     #            | <comandoWhile>
#     #            | <comandoFor>
#     #            | <comandoBreak>
#     #            | <comandoReturn>
#     #            | <comandoRead>
#     #            | <comandoWrite>
#     #            | <atribuicao> ';'
#     #            | <chamada> ';'
#     pass

# def p_comando_if(t):
#     # <comandoIf> => "if" '(' <expressao> ')' '{' <bloco> '}'
#     #              | "if" '(' <expressao> ')' '{' <bloco> '}' "else" '{' <bloco> '}'
#     pass

# def p_comando_while(t):
#     # <comandoWhile> => "while" '(' <expressao> ')' '{' <bloco> '}' 
#     pass

# def p_comando_for(t):
#     # <comandoFor> => "for" '(' <atribuicao> ';' <expressao> ';' <atribuicao> ')' '{' <bloco> '}' 
#     pass

# def p_comando_break(t):
#     # <comandoBreak> => "break" ';' 
#     pass

# def p_comando_read(t):
#     # <comandoRead> => "read" <variavel> ';' 
#     pass

# def p_comando_write(t):
#     # <comandoWrite> => "write" <listaExpressao> ';' 
#     pass

# def p_comando_return(t):
#     # <comandoReturn> => "return" ';'
#     #                  | "return" <expressao> ';'
#     pass

# def p_chamada(t):
#     # <chamada> => id '(' <listaExpressao> ')'
#     pass

def p_atribuicao(p):
    # <atribuicao> => <variavel> '='  <expressao>
    #               | <variavel> "+=" <expressao>
    #               | <variavel> "-=" <expressao>
    #               | <variavel> "*=" <expressao>
    #               | <variavel> "%=" <expressao> 
    #               | <variavel> "/=" <expressao>
    """
    
    """
    p[0] = p[1]

def p_variavel(t):
    """ variavel : ID
                 | ID ABRECOLCH expressao FECHACOLCH
    """
    t[0] = t[1]

# <expressao> => <expressao> '+'   <expressao>
#              | <expressao> '-'   <expressao>
#              | <expressao> '*'   <expressao>
#              | <expressao> '/'   <expressao>
#              | <expressao> '%'   <expressao>
#              | <expressao> "=="  <expressao>
#              | <expressao> "!="  <expressao>
#              | <expressao> "<="  <expressao>
#              | <expressao> ">="  <expressao>
#              | <expressao> '>'   <expressao>
#              | <expressao> '<'   <expressao>
#              | <expressao> "&&"  <expressao>
#              | <expressao> "||"  <expressao>
#              | '!' <expressao>
#              | '-' <expressao>
#              | <expressao> '?' <expressao> ':' <expressao>
#              | <chamada>
#              | <variavel>
#              | <literal>
#              | '(' <expressao> ')'

def p_expressao(t):
    """expressao : expressao MAIS expressao
                 | expressao MENOS expressao
                 | expressao MULT expressao
                 | expressao DIV expressao
                 | variavel
                 | literal
                 | ABREPAREN expressao FECHAPAREN"""
    if (len(t) == 4):
        if t[2] == '+': t[0] = t[1] + t[3]
        elif t[2] == '-': t[0] = t[1] - t[3]
        elif t[2] == '*': t[0] = t[1] * t[3]
        elif t[2] == '/': t[0] = t[1] / t[3]
    else: t[0] = t[1]

def p_literal(t):
    """literal : NUMBER
               | CADEIA"""
    t[0] = t[1]

# def p_lista_parametros(t):
#     # <listaParametros> => <sequenciaParametros>
#     #                    | ε
#     pass

# def p_sequencia_parametros(t):
#     # <sequenciaParametros> => <parametros> ',' <sequenciaParametros>
#     #                        | <parametros>
#     pass

# def p_lista_expressao(t):
#     # <listaExpressao> => <sequenciaExpressao>
#     #                   | ε
#     pass

# def p_sequencia_literal(t):
#     # <sequenciaLiteral> => <literal> <sequenciaLiteral>
#     #                     | <literal>
#     pass

# def p_lista_comandos(t):
#     # <listaComandos> => <comando> <listaComandos>
#     #                  | ε
#     pass

# def p_sequencia_declaracao(t):
#     # <sequenciaDeclaracao> => <declaracao> <sequenciaDeclaracao>
#     #                        | <declaracao>
#     pass

# def p_sequencia_spec_variavel(t):
#     # <sequenciaSpecVariavel> => <specificacaoVariavel> ',' <sequenciaSpecVariavel>
#     #                          | <specificacaoVariavel>
#     pass

# def p_lista_declaracao_variavel(t):
#     # <listaDeclaracaoVariavel> => <declaracaoVariavel> <listaDeclaracaoVariavel>
#     #                            | ε
#     pass

# def p_sequencia_expressao(t):
#     # <sequenciaExpressao> => <expressao> ',' <sequenciaExpressao>
#     #                       | <expressao>
#     '''sequencia_expressao : expressao VIRGULA sequencia_expressao
#                            | expressao'''
#     if :
#         pass

def p_error(t):
    print("Syntax error at '%s'" % t.value)

parser = yacc.yacc()

while True:
    try:
        s = "a[10]"   # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s)


