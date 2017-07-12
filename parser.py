# -*- coding: utf-8 -*-

import sys
import getopt

import ply.yacc as yacc

from lexer import tokens
import lexer

precedence = (
    ('right', 'TERNARIOSE'),
    ('left', 'OU'),
    ('left', 'E'),
    ('left', 'IGUAL', 'DIFERENTE'),
    ('left', 'MAIOR', 'MAIORIGUAL', 'MENOR', 'MENORIGUAL'),
    ('left', 'MAIS', 'MENOS'),
    ('left', 'MULT', 'DIV'),
    ('left', 'NEG', 'SINAL',)
)

# print tokens

def p_program(p):
    ''' program : decSeq'''
    p[0] = ('Program', p[1])


def p_dec(p):

    '''
    dec : varDec
        | ID ABREPAREN paramList FECHAPAREN ABRECHAVE block FECHACHAVE
        | type ID ABREPAREN paramList FECHAPAREN ABRECHAVE block FECHACHAVE
    '''


def p_var_dec(p):
    '''varDec : type varSpecSeq PONTOVIRGULA'''


def p_var_spec(p):
    '''
    varSpec : ID
            | ID ATRIB literal
            | ID ABRECOLCH NUMBER FECHACOLCH
            | ID ABRECOLCH NUMBER FECHACOLCH ATRIB ABRECHAVE literalSeq FECHACHAVE
    '''


def p_type(p):
    '''
    type : INT
         | STRING
         | BOOL
    '''


def p_param(p):
    '''
    param : type ID
          | type ID ABRECOLCH FECHACOLCH
    '''


def p_block(p):
    ''' block : varDecList stmtList'''


def p_stmt(p):
    '''
      stmt : ifStmt
           | whileStmt
           | forStmt
           | breakStmt
           | returnStmt
           | readStmt
           | writeStmt
           | assign PONTOVIRGULA
           | subCall PONTOVIRGULA
    '''


def p_if_stmt(p):
    '''
    ifStmt : IF ABREPAREN exp FECHAPAREN ABRECHAVE block FECHACHAVE
           | IF ABREPAREN exp FECHAPAREN FECHACHAVE block FECHACHAVE ELSE ABRECHAVE block FECHACHAVE
    '''


def p_while_stmt(p):
    ''' whileStmt : WHILE ABREPAREN exp FECHAPAREN ABRECHAVE block FECHACHAVE '''


def p_for_stmt(p):
    '''forStmt : FOR ABREPAREN assign PONTOVIRGULA exp PONTOVIRGULA assign FECHAPAREN ABRECHAVE block FECHACHAVE'''


def p_break_stmt(p):
    '''breakStmt : BREAK PONTOVIRGULA'''


def p_read_stmt(p):
    '''readStmt : READ var PONTOVIRGULA'''


def p_write_stmt(p):
    '''writeStmt : WRITE expList PONTOVIRGULA'''


def p_return_stmt(p):
    '''
    returnStmt : RETURN PONTOVIRGULA
               | RETURN exp PONTOVIRGULA
    '''


def p_sub_call(p):
    '''subCall : ID ABREPAREN expList FECHAPAREN'''


def p_assign(p):
    '''
    assign : var ATRIB  exp
           | var MAISATRIB exp
           | var MENOSATRIB exp
           | var MULTATRIB exp
           | var DIVATRIB exp
           | var MODATRIB exp
    '''


def p_var(p):
    '''
    var : ID
        | ID ABRECOLCH exp FECHACOLCH
    '''


def p_exp(p):
    '''
    exp : exp MAIS exp
        | exp MENOS exp
        | exp MULT exp
        | exp DIV exp
        | exp MOD exp
        | exp IGUAL exp
        | exp DIFERENTE exp
        | exp MENORIGUAL exp
        | exp MAIORIGUAL exp
        | exp MAIOR exp
        | exp MENOR exp
        | exp E exp
        | exp OU exp
        | NEG exp
        | SINAL exp
        | exp TERNARIOSE exp TERNARIOSENAO exp
        | subCall
        | var
        | literal
        | ABREPAREN exp FECHAPAREN
        | param
    '''


def p_literal(p):
    '''
    literal : NUMBER
            | CADEIA
            | TRUE
            | FALSE
    '''


def p_param_list(p):
    '''
    paramList : paramSeq
              | empty
    '''


def p_param_seq(p):
    '''
    paramSeq : param VIRGULA paramSeq
             | param
    '''


def p_var_dec_list(p):
    '''
    varDecList : varDec varDecList
              | empty
    '''


def p_var_spec_seq(p):
    '''
    varSpecSeq : varSpec VIRGULA varSpecSeq
               | varSpec
    '''


def p_exp_list(p):
    '''
    expList : expSeq
            | empty
    '''


def p_literal_seq(p):
    '''
    literalSeq : literal VIRGULA literalSeq
               | literal
    '''


def p_stmt_list(p):
    '''
    stmtList : stmt stmtList
             | empty
    '''


def p_dec_seq(p):
    '''
    decSeq : dec decSeq
           | dec
    '''
    if len(p) == 2:
        p[0] = ('Declaration Sequence', p[1])
    elif len(p) == 3:
        p[0] = ('Declaration Sequence', p[1], p[2])


def p_exp_seq(p):
    '''
    expSeq : exp VIRGULA expSeq
           | exp
    '''


def p_empty(p):
    ''' empty : '''
    pass


def p_error(p):
    last_cr = p.lexer.lexdata.rfind('\n', 0, p.lexer.lexpos)
    column = p.lexer.lexpos - last_cr - 1
    if p:
        print("Erro de sintaxe em {0} na linha {1} coluna {2}".format(p.value, p.lexer.lineno, column))
        # yacc.yacc().errok()
    else:
        print("Erro de sintaxe EOF")


# input_ = '''
# int v[10];
# /*
# Procedimento de ordenação por troca
# Observe como um parâmetro de arranjo é declarado
# */
# bubblesort(int v[], int n) {
#   int i=0, j;
#   bool trocou = true;
#   while (i < n-1 && trocou) {
#     trocou = false;
#     for (j=0; j < n-i-1; j+=1) {
#       if (v[j] > v[j+1]) {
#         int aux;
#         aux = v[j];
#         v[j] = v[j+1];
#         v[j+1] = aux;
#         trocou = true;
#       }
#     }
#     i += 1;
#   }
# }
# main() {
#   int i;
#   for (i=0; i < 10; i+=1) {
#     read v[i];
#   }
#   bubblesort(v, 10);
#   for (i=0; i < 10; i+=1) {
#     write v[i], " ";
#   }
# }
# '''


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
    file.close()

    # Build the parser
    parser = yacc.yacc()

    result = parser.parse(input_)
    print(result)


if __name__ == "__main__":
    main(sys.argv[1:])