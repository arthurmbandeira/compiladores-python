# -*- coding: utf-8 -*-

import re

import ply.lex as lex
import ply.yacc as yacc

palavras_reservadas = {
	'bool' : 'BOOL',
	'string' : 'STRING',
	'int' : 'INT',
	'for' : 'FOR',
	'if' : 'IF',
	'else' : 'ELSE',
	'while' : 'WHILE',
	'true' : 'TRUE',
	'false' : 'FALSE',
	'return' : 'RETURN',
 	'break' : 'BREAK',
}

tokens = [
	'NOME', 'NUMERO', 'ID', 'CADEIA',
	'ABREPAREN', 'FECHAPAREN', 'ABRECOLCH', 'FECHACOLCH', 'ABRECHAVE', 'FECHACHAVE',
	'VIRGULA', 'PONTOVIRGULA',
	'MAIS', 'MENOS', 'MULT', 'DIV',
	'IGUAL', 'DIFERENTE', 'MAIOR', 'MAIORIGUAL', 'MENOR', 'MENORIGUAL', 'OU', 'E', 'NEG',
	'ATRIB', 'MAISATRIB', 'MENOSATRIB', 'MULTATRIB', 'DIVATRIB', 'MODATRIB',
	'TERNARIO', 'TERNARIOSE', 'TERNARIOSENAO',
	'COMENTARIO',
] + list(palavras_reservadas.values())

t_MAIS = r'\+'
t_MENOS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_IGUAL = r'=='
t_ABREPAREN = r'\('
t_FECHAPAREN = r'\)'
t_ABRECOLCH = r'\['
t_FECHACOLCH = r'\]'
t_NOME = r'[a-zA-Z_][a-zA-Z0-9_]*'
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
t_ATRIB = r'='
t_MAISATRIB = r'\+='
t_MENOSATRIB = r'-='
t_MULTATRIB = r'\*='
t_DIVATRIB = r'/='
t_MODATRIB = r'%='
t_TERNARIOSE = r'\?'
t_TERNARIOSENAO = r':'
t_CADEIA = r'\"(\n|.)*?\"'

def t_NUMERO(t):
	r'\d+'
	try:
		t.value = int(t.value)
	except ValueError:
		print("Valor Inteiro muito grande %d", t.value)
		t.value = 0
	return t


# ignorando TAB
t_ignore = " \t\v\r"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = palavras_reservadas.get(t.value,'ID')
    return t

def t_COMENTARIO(t):
    r'((//.*)|(/\*(.|\n)*\*/))'
    pass
    # No return value. Token discarded

lexer = lex.lex()

data = """
int v[10];
/*
Procedimento de ordenação por troca
Observe como um parâmetro de arranjo é declarado
*/
bubblesort(int v[], int n) {
  int i=0, j;
  bool trocou = true;
  while (i < n-1 && trocou) {
    trocou = false;
    for (j=0; j < n-i-1; j+=1) {
      if (v[j] > v[j+1]) {
        int aux;
        aux = v[j];
        v[j] = v[j+1];
        v[j+1] = aux;
        trocou = true;
      }
    }
    i += 1;
  }
}
main() {
  int i;
  for (i=0; i < 10; i+=1) {
    read v[i];
  }
  bubblesort(v, 10);
  for (i=0; i < 10; i+=1) {
    write v[i], " ";
  }
}
"""

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
