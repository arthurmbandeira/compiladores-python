class Node(object):
    __slots__ = ()


# class Node:
#     def __init__(self, type_, children=None, leaf=None):
#         self.type_ = type_
#         if children:
#             self.children = children
#         else:
#             self.children = []
#         self.leaf = leaf


# class Expression: pass


# class Number(Expression):
#     """docstring for Number"""
#     def __init__(self, value):
#         self.type_ = "number"
#         self.arg = arg


class Program(Node):
    __slots__ = ('dec_seq')
    def __init__(self, dec_seq):
        self.dec_seq = dec_seq


class DecSeq(Node):
    __slots__ = ('dec', 'dec_seq')
    def __init__(self, dec=None, dec_seq=None):
        self.dec = dec
        self.dec_seq = dec_seq


class Dec(Node):
    __slots__ = ('type_', 'id_', 'param_list', 'block', 'var_dec')
    def __init__(self, type_=None, id_=None, param_list=None, block=None, var_dec=None):
        self.type_ = type_
        self.id_ = id_
        self.param_list = param_list
        self.block = block
        self.var_dec = var_dec


class VarDec(Node):
    __slots__ = ('type_', 'var_spec_seq')
    def __init__(self, type_, var_spec_seq):
        self.type_ = type_
        self.var_spec_seq = var_spec_seq


class VarSpec(Node):
    __slots__ = ('id_', 'literal', 'number', 'literal_seq')
    def __init__(self, id_, literal=None, number=None, literal_seq=None):
        self.id_ = id_
        self.literal = literal
        self.number = number
        self.literal_seq = literal_seq


class Type(Node):
    __slots__ = ('type_')
    def __init__(self, type_):
        self.type_ = type_


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


class Assign(Node):
    __slots__ = ('op', 'left', 'right')
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class Variable(Node):
    __slots__ = ('id', 'exp')
    def __init__(self, id, exp=None):
        self.id = id
        self.exp = exp


class BinaryOp(Node):
    __slots__ = ('op', 'left', 'right')
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class UnaryOp(Node):
    __slots__ = ('op', 'right')
    def __init__(self, op, right):
        self.op = op
        self.right = right


class TernaryOp(Node):
    __slots__ = ('op', 'op_if', 'op_else')
    def __init__(self, op, op_if, op_else):
        self.op = op
        self.op_if = op_if
        self.op_else = op_else