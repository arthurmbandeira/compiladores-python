# -*- coding: utf-8 -*-

import ply.yacc as yacc

from lexer import tokens

print tokens

def p_program:
    """ <program> => <SequenciaDeclaracao> """
    pass

def p_declaracao():
    """ 
    <declaracao> => <declaracaoVariavel>
                  | id '(' <listaParametros> ')' '{' <bloco> '}'
                  | <tipo> id '(' <listaParametros> ')' '{' <bloco> '}'
    """
    pass

def p_declaracao_variavel():
    """ <declaracaoVariavel> => <tipo> <sequenciaSpecVariavel> ';' """
    pass

def p_especificacao_variavel():
    """
    <especificacaoVariavel> => id
                             | id '=' <literal>
                             | id '[' numero ']'
                             | id '[' numero ']' '=' '{' <sequenciaLiteral> '}'
    """
    pass

def p_tipo():
    """
    <tipo> => "int"
            | "string"
            | "bool"
    """
    pass

def p_parametros():
    """
    <parametros> => <tipo> id
                  | <tipo> id '[' ']'
    """
    pass

def p_bloco():
    """ <bloco> => <listaDeclaracaoVariavel> <listaComandos> """
    pass

def p_comando():
    """
    <comando> => <comandoIF>
               | <comandoWhile>
               | <comandoFor>
               | <comandoBreak>
               | <comandoReturn>
               | <comandoRead>
               | <comandoWrite>
               | <atribuicao> ';'
               | <chamada> ';'
    """
    pass

def p_comando_if():
    """
    <comandoIf> => "if" '(' <expressao> ')' '{' <bloco> '}'
                 | "if" '(' <expressao> ')' '{' <bloco> '}' "else" '{' <bloco> '}'
    """
    pass

def p_comando_while():
    """ <comandoWhile> => "while" '(' <expressao> ')' '{' <bloco> '}' """
    pass

def p_comando_for():
    """ <comandoFor> => "for" '(' <atribuicao> ';' <expressao> ';' <atribuicao> ')' '{' <bloco> '}' """
    pass

def p_comando_break():
    """ <comandoBreak> => "break" ';' """
    pass

def p_comando_read():
    """ <comandoRead> => "read" <variavel> ';' """
    pass

def p_comando_write():
    """ <comandoWrite> => "write" <listaExpressao> ';' """
    pass

def p_comando_return():
    """ 
    <comandoReturn> => "return" ';'
                     | "return" <expressao> ';'
    """
    pass

def p_chamada():
    """ <chamada> => id '(' <listaExpressao> ')' """
    pass

def p_atribuicao():
    """
    <atribuicao> => <variavel> '='  <expressao>
                  | <variavel> "+=" <expressao>
                  | <variavel> "-=" <expressao>
                  | <variavel> "*=" <expressao>
                  | <variavel> "/=" <expressao>
                  | <variavel> "%=" <expressao> 
    """
    pass

def p_variavel():
    """
    <variavel> => id
                | id '[' <expressao> ']'
    """    
    pass

def p_expressao():
    """
    <expressao> => <expressao> '+'   <expressao>
                 | <expressao> '-'   <expressao>
                 | <expressao> '*'   <expressao>
                 | <expressao> '/'   <expressao>
                 | <expressao> '%'   <expressao>
                 | <expressao> "=="  <expressao>
                 | <expressao> "!="  <expressao>
                 | <expressao> "<="  <expressao>
                 | <expressao> ">="  <expressao>
                 | <expressao> '>'   <expressao>
                 | <expressao> '<'   <expressao>
                 | <expressao> "&&"  <expressao>
                 | <expressao> "||"  <expressao>
                 | '!' <expressao>
                 | '-' <expressao>
                 | <expressao> '?' <expressao> ':' <expressao>
                 | <chamada>
                 | <variavel>
                 | <literal>
                 | '(' <expressao> ')'
    """
    pass

def p_literal():
    """
    <literal> => numero
               | string
               | logico
    """
    pass

def p_lista_parametros():
    """
    <listaParametros> => <sequenciaParametros>
                 | ε
    """
    pass

def p_sequencia_parametros():
    """
    <sequenciaParametros> => <parametros> ',' <sequenciaParametros>
                | <parametros>
    """
    pass

def p_lista_expressao():
    """
    <listaExpressao> => <sequenciaExpressao>
           | ε
    """
    pass

def p_sequencia_literal():
    """
    <sequenciaLiteral> => <literal> <sequenciaLiteral>
                  | <literal>
    """
    pass

def p_lista_comandos():
    """
    <listaComandos> => <comando> <listaComandos>
                | ε
    """
    pass

def p_sequencia_declaracao():
    """
    <sequenciaDeclaracao> => <declaracao> <sequenciaDeclaracao>
              | <declaracao>
    """
    pass

def p_sequencia_spec_variavel():
    """
    <sequenciaSpecVariavel> => <specificacaoVariavel> ',' <sequenciaSpecVariavel>
                  | <specificacaoVariavel>
    """
    pass

def p_lista_declaracao_variavel():
    """
    <listaDeclaracaoVariavel> => <declaracaoVariavel> <listaDeclaracaoVariavel>
            | ε
    """
    pass

def p_sequencia_expressao():
    """
    <sequenciaExpressao> => <expressao> ',' <sequenciaExpressao>
              | <expressao>
    """
    pass









