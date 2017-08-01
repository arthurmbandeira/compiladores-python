# -*- coding: utf-8 -*-
import sys
import getopt
import ply.yacc as yacc
import ply.lex as lex


from lexer import tokens
from semantic import *


lex.lexer.lineno = 1


precedence = (
    ('right', 'TERNARIOSE'),
    ('left', 'OU'),
    ('left', 'E'),
    ('left', 'IGUAL', 'DIFERENTE'),
    ('left', 'MAIOR', 'MAIORIGUAL', 'MENOR', 'MENORIGUAL'),
    ('left', 'MAIS', 'MENOS'),
    ('left', 'MULT', 'DIV'),
    ('right', 'NEG', 'SINAL'),
)


def p_program(p):
    ''' program : decSeq'''
    p[0] = Program(dec_seq=p[1])


def p_dec(p):
    '''
    dec : varDec
        | ID ABREPAREN paramList FECHAPAREN ABRECHAVE block FECHACHAVE
        | type ID ABREPAREN paramList FECHAPAREN ABRECHAVE block FECHACHAVE
    '''
    if len(p) == 2:
        p[0] = Dec(var_dec=p[1])
    elif len(p) == 8:
        p[0] = Dec(id_=p[1], param_list=p[3], block=p[6])
    elif len(p) == 9:
        p[0] = Dec(type_=p[1], id_=p[2], param_list=p[4], block=p[7])


def p_var_dec(p):
    '''varDec : type varSpecSeq PONTOVIRGULA'''
    p[0] = VarDec(type_=p[1], var_spec_seq=p[2])


def p_var_spec(p):
    '''
    varSpec : ID
            | ID ATRIB literal
            | ID ABRECOLCH NUMBER FECHACOLCH
            | ID ABRECOLCH NUMBER FECHACOLCH ATRIB ABRECHAVE literalSeq FECHACHAVE
    '''
    if len(p) == 2:
        p[0] = VarSpec(id_=p[1])
    elif len(p) == 4:
        p[0] = VarSpec(id_=p[1], literal=p[3])
    elif len(p) == 5:
        p[0] = VarSpec(id_=p[1], number=p[3])
    elif len(p) == 9:
        p[0] = VarSpec(id_=p[1], number=p[3], literal_seq=p[7])


def p_type(p):
    '''
    type : INT
         | STRING
         | BOOL
    '''
    p[0] = Type(type_=p[1])


def p_param(p):
    '''
    param : type ID
          | type ID ABRECOLCH FECHACOLCH
    '''
    if len(p) == 3:
        p[0] = Param(type_=p[1], id_=p[2], array=False)
    elif len(p) == 5:
        p[0] = Param(type_=p[1], id_=p[2], array=True)


def p_block(p):
    ''' block : varDecList stmtList'''
    p[0] = Block(var_dec_list=p[1], stmt_list=p[2])


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
    p[0] = Stmt(stmt=p[1])


def p_if_stmt(p):
    '''
    ifStmt : IF ABREPAREN exp FECHAPAREN ABRECHAVE block FECHACHAVE
           | IF ABREPAREN exp FECHAPAREN FECHACHAVE block FECHACHAVE ELSE ABRECHAVE block FECHACHAVE
    '''
    if len(p) == 8:
        p[0] = IfStmt(if_=p[1], exp=p[3], block1=p[6])
    if len(p) == 12:
        p[0] = IfStmt(if_=p[1], exp=p[3], block1=p[6], else_=p[8], block2=p[10])


def p_while_stmt(p):
    ''' whileStmt : WHILE ABREPAREN exp FECHAPAREN ABRECHAVE block FECHACHAVE '''
    p[0] = WhileStmt(while_=p[1], exp=p[3], block=p[6])


def p_for_stmt(p):
    '''forStmt : FOR ABREPAREN assign PONTOVIRGULA exp PONTOVIRGULA assign FECHAPAREN ABRECHAVE block FECHACHAVE'''
    p[0] = ForStmt(for_=p[1], assign1=p[3], exp=p[5], assign2=p[7], block=p[10])


def p_break_stmt(p):
    '''breakStmt : BREAK PONTOVIRGULA'''
    p[0] = BreakStmt(break_=p[1])


def p_read_stmt(p):
    '''readStmt : READ var PONTOVIRGULA'''
    p[0] = ReadStmt(read=p[1], var=p[2])


def p_write_stmt(p):
    '''writeStmt : WRITE expList PONTOVIRGULA'''
    p[0] = WriteStmt(write=p[1], exp_list=p[2])


def p_return_stmt(p):
    '''
    returnStmt : RETURN PONTOVIRGULA
               | RETURN exp PONTOVIRGULA
    '''
    if len(p) == 3:
        p[0] = ReturnStmt(return_=p[1])
    if len(p) == 4:
        p[0] = ReturnStmt(return_=p[1], exp=p[2])


def p_sub_call(p):
    '''subCall : ID ABREPAREN expList FECHAPAREN'''
    p[0] = SubCall(id_=p[1], exp_list=p[3])


def p_assign(p):
    '''
    assign : var ATRIB exp
           | var MAISATRIB exp
           | var MENOSATRIB exp
           | var MULTATRIB exp
           | var DIVATRIB exp
           | var MODATRIB exp
    '''
    p[0] = Assign(op=p[2], left=p[1], right=p[3])


def p_var(p):
    '''
    var : ID
        | ID ABRECOLCH exp FECHACOLCH
    '''
    if len(p) == 2:
        p[0] = Variable(id_=p[1])
    else:
        p[0] = Variable(id_=p[1], exp=p[3])


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
    if len(p) == 4:
        if p[1] == '(':
            p[0] = Exp(op=p[2])
        else:
            p[0] = Exp(op=p[2], left=p[1], right=p[3])
    elif len(p) == 3:
        p[0] = Exp(op=p[1], right=p[2])
    elif len(p) == 2:
        p[0] = Exp(op=p[1])
    elif len(p) == 6:
        p[0] = Exp(op=p[1], left=p[3], right=p[5])


def p_literal(p):
    '''
    literal : NUMBER
            | CADEIA
            | TRUE
            | FALSE
    '''
    p[0] = Literal(literal=p[1])


def p_param_list(p):
    '''
    paramList : paramSeq
              | empty
    '''
    p[0] = ParamList(param_seq=p[1])


def p_param_seq(p):
    '''
    paramSeq : param VIRGULA paramSeq
             | param
    '''
    if len(p) == 4:
        p[0] = ParamSeq(param=p[1], param_seq=p[3])
    elif len(p) == 2:
        p[0] = ParamSeq(param=p[1])


def p_var_dec_list(p):
    '''
    varDecList : varDec varDecList
               | empty
    '''
    if p[1]:
        p[0] = VarDecList(var_dec=p[1], var_dec_list=p[2])


def p_var_spec_seq(p):
    '''
    varSpecSeq : varSpec VIRGULA varSpecSeq
               | varSpec
    '''
    if len(p) == 4:
        p[0] = VarSpecSeq(var_spec=p[1], var_spec_seq=p[3])
    elif len(p) == 2:
        p[0] = VarSpecSeq(var_spec=p[1])


def p_exp_list(p):
    '''
    expList : expSeq
            | empty
    '''
    if p[1]:
        p[0] = ExpList(exp_seq=p[1])


def p_literal_seq(p):
    '''
    literalSeq : literal VIRGULA literalSeq
               | literal
    '''
    if len(p) == 4:
        p[0] = LiteralSeq(literal=p[1], literal_seq=p[3])
    elif len(p) == 2:
        p[0] = LiteralSeq(literal=p[1])


def p_stmt_list(p):
    '''
    stmtList : stmt stmtList
             | empty
    '''
    if p[1]:
        p[0] = StmtList(stmt=p[1], stmt_list=p[2])


def p_dec_seq(p):
    '''
    decSeq : dec decSeq
           | dec
    '''
    if len(p) == 2:
        p[0] = DecSeq(dec=p[1])
    elif len(p) == 3:
        p[0] = DecSeq(dec=p[1], dec_seq=p[2])


def p_exp_seq(p):
    '''
    expSeq : exp VIRGULA expSeq
           | exp
    '''
    if len(p) == 2:
        p[0] = ExpSeq(exp=p[1])
    elif len(p) == 4:
        p[0] = ExpSeq(exp=p[1], exp_seq=p[3])


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

    program = parser.parse(input_)
    if program:
        program.print_name()
        program.check_node()
        print('Variaveis declaradas', declared_variables)


if __name__ == "__main__":
    main(sys.argv[1:])
