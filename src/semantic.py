# -*- coding: utf-8 -*-
import sys
from utils import SemanticError
from abc import ABCMeta, abstractmethod

declared_variables = []

class Node:

    # __metaclass__ = ABCMeta   

    __slots__ = ()

    def __init__(self): pass

    # @abstractmethod
    def check_node(self): pass


class Program(Node):

    __slots__ = ('dec_seq')

    def __init__(self, dec_seq):
        self.dec_seq = dec_seq

    def check_node(self):
        self.dec_seq.check_node()


class Dec(Node):

    __slots__ = ('type_', 'id_', 'param_list', 'block', 'var_dec')

    def __init__(self, type_=None, id_=None, param_list=None, block=None, var_dec=None):
        self.type_ = type_
        self.id_ = id_
        self.param_list = param_list
        self.block = block
        self.var_dec = var_dec

    def check_node(self):
        if self.var_dec:
            self.var_dec.check_node()


class VarDec(Node):

    __slots__ = ('type_', 'var_spec_seq')

    def __init__(self, type_, var_spec_seq):
        self.type_ = type_
        self.var_spec_seq = var_spec_seq

    def check_node(self):
        print self.type_.check_node()
        print self.var_spec_seq.check_node()


class VarSpec(Node):

    __slots__ = ('id_', 'literal', 'number', 'literal_seq')

    def __init__(self, id_, literal=None, number=None, literal_seq=None):
        self.id_ = id_
        self.literal = literal
        self.number = number
        self.literal_seq = literal_seq

    def check_node(self):
        if self.literal:
            self.literal.check_node()
        if self.number:
            self.number.check_node()
        if self.literal_seq:
            self.literal_seq.check_node()
        return self.id_


class Type(Node):

    __slots__ = ('type_')

    def __init__(self, type_):
        self.type_ = type_

    def check_node(self):
        return self.type_


class Param(Node):

    __slots__ = ('type_', 'id_', 'array')

    def __init__(self, type_, id_, array):
        self.type_ = type_
        self.id_ = id_
        self.array = array


class Block(Node):

    __slots__ = ('var_dec_list', 'stmt_list')

    def __init__(self, var_dec_list, stmt_list):
        self.var_dec_list = var_dec_list
        self.stmt_list = stmt_list


class Stmt(Node):

    __slots__ = ('stmt')

    def __init__(self, stmt):
        self.stmt = stmt


class IfStmt(Node):

    __slots__ = ('if_', 'exp', 'block1', 'else_', 'block2')

    def __init__(self, if_, exp, block1, else_=None, block2=None):
        self.if_ = if_
        self.exp = exp
        self.block1 = block1
        self.else_ = else_
        self.block2 = block2


class WhileStmt(Node):

    __slots__ = ('while_', 'exp', 'block')

    def __init__(self, while_, exp, block):
        self.while_ = while_
        self.exp = exp
        self.block = block


class ForStmt(Node):

    __slots__ = ('for_', 'assign1', 'exp', 'assign2', 'block')

    def __init__(self, for_, assign1, exp, assign2, block):
        self.for_ = for_
        self.assign1 = assign1
        self.exp = exp
        self.assign2 = assign2
        self.block = block


class BreakStmt(Node):

    __slots__ = ('break_')

    def __init__(self, break_):
        self.break_ = break_


class ReadStmt(Node):

    __slots__ = ('read', 'var')

    def __init__(self, read, var):
        self.read = read
        self.var = var


class WriteStmt(Node):

    __slots__ = ('write', 'exp_list')

    def __init__(self, write, exp_list):
        self.write = write
        self.exp_list = exp_list


class ReturnStmt(Node):

    __slots__ = ('return_', 'exp')

    def __init__(self, return_, exp):
        self.return_ = return_
        self.exp = exp


class SubCall(Node):

    __slots__ = ('id_', 'exp_list')

    def __init__(self, id_, exp_list):
        self.id_ = id_
        self.exp_list = exp_list


class Assign(Node):

    __slots__ = ('op', 'left', 'right')

    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class Variable(Node):

    __slots__ = ('id_', 'exp')

    def __init__(self, id_, exp=None):
        self.id_ = id_
        self.exp = exp


class Exp(Node):

    __slots__ = ('op', 'left', 'right')

    def __init__(self, op, left=None, right=None):
        self.op = op
        self.left = left
        self.right = right


class Literal(Node):

    __slots__ = ('literal')

    def __init__(self, literal):
        self.literal = literal


class ParamList(Node):

    __slots__ = ('param_seq')

    def __init__(self, param_seq):
        self.param_seq = param_seq


class ParamSeq(Node):

    __slots__ = ('param', 'param_seq')

    def __init__(self, param, param_seq=None):
        self.param = param
        self.param_seq = param_seq


class VarDecList(Node):

    __slots__ = ('var_dec', 'var_dec_list')

    def __init__(self, var_dec=None, var_dec_list=None):
        self.var_dec = var_dec
        self.var_dec_list = var_dec_list


class VarSpecSeq(Node):

    __slots__ = ('var_spec', 'var_spec_seq')

    variables = []

    def __init__(self, var_spec, var_spec_seq=None):
        self.var_spec = var_spec
        self.var_spec_seq = var_spec_seq        

    def check_node(self):
        # global declared_variables
        # print 'ok'
        self.variables.append(self.var_spec.check_node())
        
        if self.var_spec_seq:
            self.var_spec_seq.check_node()
        else:
            print self.variables
            return self.variables


class ExpList(Node):

    __slots__ = ('exp_seq')

    def __init__(self, exp_seq):
        self.exp_seq = exp_seq


class LiteralSeq(Node):

    __slots__ = ('literal', 'literal_seq')

    def __init__(self, literal, literal_seq=None):
        self.literal = literal
        self.literal_seq = literal_seq


class StmtList(Node):

    __slots__ = ('stmt', 'stmt_list')

    def __init__(self, stmt, stmt_list):
        self.stmt = stmt
        self.stmt_list = stmt_list


class DecSeq(Node):

    __slots__ = ('dec', 'dec_seq')

    def __init__(self, dec, dec_seq=None):
        self.dec = dec
        self.dec_seq = dec_seq

    def check_node(self):
        self.dec.check_node()
        if self.dec_seq:
            self.dec_seq.check_node()


class ExpSeq(Node):

    __slots__ = ('exp', 'exp_seq')

    def __init__(self, exp, exp_seq=None):
        self.exp = exp
        self.exp_seq = exp_seq




# class BinaryOp(Node):
#     __slots__ = ('op', 'left', 'right')
#     def __init__(self, op, left, right):
#         self.op = op
#         self.left = left
#         self.right = right


# class UnaryOp(Node):
#     __slots__ = ('op', 'right')
#     def __init__(self, op, right):
#         self.op = op
#         self.right = right


# class TernaryOp(Node):
#     __slots__ = ('op', 'op_if', 'op_else')
#     def __init__(self, op, op_if, op_else):
#         self.op = op
#         self.op_if = op_if
#         self.op_else = op_else
