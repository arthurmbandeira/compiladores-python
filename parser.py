# -*- coding: utf-8 -*-

import ply.yacc as yacc

from lexer import tokens

print tokens

def p_program():
    ''' program : SequenciaDeclaracao'''
    p[0] : p[1]
    pass

def p_declaracao():

    '''
    declaracao : declaracaoVariavel
                  | id ABREPAREN listaParametros FECHAPAREN ABRECHAVE bloco FECHACHAVE
                  | tipo id ABREPAREN listaParametros FECHAPAREN ABRECHAVE bloco FECHACHAVE
    '''

    pass

def p_declaracao_variavel():
    '''declaracaoVariavel : tipo sequenciaSpecVariavel PONTOVIRGULA'''
    pass

    p[0] : Node ('declaracaoVariavel', [[p1], p[2]])

def p_especificacao_variavel(p):
    '''
    especificacaoVariavel : ID
                             | ID ATRIB literal
                             | ID ABRECOLCH numero FECHACOLCH
                             | ID ABRECOLCH numero FECHACOLCH ATRIB ABRECHAVE sequenciaLiteral FECHACHAVE
    '''
    if len(p) :: 2:
        p[0] : Node('especificacaoVariavelID', [], p[1])
    elif len p[1]

def p_tipo():
    '''
    tipo : INT
         | STRING
         | BOOL
    '''
    pass

def p_parametros():
    '''
    parametros : tipo ID
               | tipo ID ABRECOLCH FECHACOLCH
    '''
    pass

def p_bloco():
    ''' bloco : listaDeclaracaoVariavel listaComandos'''
    pass

def p_comando():
    '''
      comando : comandoIF
              | comandoWhile
              | comandoFor
              | comandoBreak
              | comandoReturn
              | comandoRead
              | comandoWrite
              | atribuicao PONTOVIRGULA
              | chamada PONTOVIRGULA
    '''
    pass

def p_comando_if():
    '''
    comandoIf : IF ABREPAREN expressao FECHAPAREN ABRECOLCH bloco FECHACOLCH
                | IF ABREPAREN expressao FECHAPAREN FECHACOLCH bloco FECHACOLCH ELSE ABRECOLCH bloco FECHACOLCH
    '''
    pass

def p_comando_while():
    ''' comandoWhile : WHILE ABREPAREN expressao FECHAPAREN ABRECHAVE bloco FECHACHAVE '''
    pass

def p_comando_for():
    '''comandoFor : FOR ABREPAREN atribuicao PONTOVIRGULA expressao PONTOVIRGULA atribuicao FECHAPAREN ABRECOLCH bloco FECHACOLCH'''
    pass

def p_comando_break():
    '''comandoBreak : BREAK PONTOVIRGULA'''
    pass

def p_comando_read():
    '''comandoRead : read variavel PONTOVIRGULA'''
    pass

def p_comando_write():
    '''comandoWrite : write listaExpressao PONTOVIRGULA'''
    pass

def p_comando_return():
    '''
    comandoReturn : RETURN PONTOVIRGULA
                  |RETURN expressao PONTOVIRGULA
    '''
    pass

def p_chamada():
    '''chamada : ID ABREPAREN listaExpressao FECHAPAREN'''
    pass

def p_atribuicao():
'''
    atribuicao : variavel ATRIB  expressao
              | variavel MAISATRIB expressao
              | variavel MENOSATRIB expressao
              | variavel MULTATRIB expressao
              | variavel DIVATRIB expressao
              | variavel MODATRIB expressao
    '''
    pass

def p_variavel():
    '''
    variavel : ID
             | ID ABRECOLCH expressao FECHACOLCH
    '''
    pass

def p_expressao():
    '''
    expressao : expressao MAIS  expressao
                 | expressao MENOS   expressao
                 | expressao MULT   expressao
                 | expressao DIV   expressao
                #  | expressao '%'   expressao
                 | expressao IGUAL  expressao
                 | expressao DIFERENTE  expressao
                 | expressao MENORIGUAL  expressao
                 | expressao MAIORIGUAL  expressao
                 | expressao MAIOR   expressao
                 | expressao MENOR   expressao
                 | expressao E  expressao
                 | expressao OU  expressao
                 | NEG expressao
                #  | '-' expressao
                 | expressao TERNARIOSE expressao TERNARIOSENAO expressao
                 | chamada
                 | variavel
                 | literal
                 | ABREPAREN expressao FECHAPAREN
    '''
    pass

def p_literal():
'''
    literal : NUMERO
               | STRING
               | BOOL
    '''
    pass

def p_lista_parametros():
'''
    listaParametros : sequenciaParametros
                 | ε
    '''
    pass

def p_sequencia_parametros():
    '''
    sequenciaParametros : parametros VIRGULA sequenciaParametros
                | parametros
    '''
    pass

def p_lista_expressao():
    '''
    listaExpressao : sequenciaExpressao
           | ε
    '''
    pass

def p_sequencia_literal():
    '''
    sequenciaLiteral : literal sequenciaLiteral
                  | literal
    '''
    pass

def p_lista_comandos():
    '''
    listaComandos : comando listaComandos
                | ε
    '''
    pass

def p_sequencia_declaracao():
    '''
    sequenciaDeclaracao : declaracao sequenciaDeclaracao
              | declaracao
    '''
    pass

def p_sequencia_spec_variavel():
    '''
    sequenciaSpecVariavel : specificacaoVariavel VIRGULA sequenciaSpecVariavel
                  | specificacaoVariavel
    '''
    pass

def p_lista_declaracao_variavel():
    '''
    listaDeclaracaoVariavel : declaracaoVariavel listaDeclaracaoVariavel
            | ε
    '''
    pass

def p_sequencia_expressao():
    '''
    sequenciaExpressao : expressao VIRGULA sequenciaExpressao
              | expressao
    '''
    pass
