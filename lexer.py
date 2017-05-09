import re

import ply.lex as lex
import ply.yacc as yacc

keywords = (
	'BOOL', 'STRING', 'INT', 
	'FOR', 'IF', 'ELSE', 'WHILE', 'TRUE', 'FALSE', 'RETURN', 'BREAK',
	)

tokens = keywords + (
	'NAME', 'NUMBER',
	'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'LKEY', 'RKEY',
	'COMMA', 'SEMICOLON', 
	'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 
	'EQ', 'NE', 'GT', 'GE', 'LT', 'LE', 'OR', 'AND', 'NOT', 
	'ATTR', 'PLUSATTR', 'MINUSATTR', 'TIMESATTR', 'DIVIDEATTR', 
	'MODATTR', 'TERNARY', 
	)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQ = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'