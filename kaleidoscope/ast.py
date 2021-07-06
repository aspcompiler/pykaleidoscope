from dataclasses import dataclass
from typing import List


class ASTNode:
    """
    Base class for AST nodes
    """


class TopLevel(ASTNode):
    pass


class ExprAST(TopLevel):
    """
    Base class for Expression
    """


@dataclass
class NumberExprAST(ExprAST):
    val: float


@dataclass
class VariableExprAST(ExprAST):
    name: str


@dataclass
class BinaryExprAST(ExprAST):
    op: str
    lhs: ExprAST
    rhs: ExprAST


@dataclass
class CallExprAST(ExprAST):
    callee: str
    args: List[ExprAST]


@dataclass
class PrototypeAST(ASTNode):
    name: str
    args: List[str]


@dataclass
class FunctionAST(TopLevel):
    proto: PrototypeAST
    body: ExprAST


@dataclass
class ExternalDeclaration(TopLevel):
    proto: PrototypeAST


@dataclass
class Program(ASTNode):
    tops: List[TopLevel]
