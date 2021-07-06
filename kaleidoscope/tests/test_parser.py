from kaleidoscope.ast import (
    BinaryExprAST,
    CallExprAST,
    ExternalDeclaration,
    FunctionAST,
    NumberExprAST,
    Program,
    PrototypeAST,
    VariableExprAST,
)
from kaleidoscope.parser import parse


def test_number():
    ast = parse("2")
    exp = ast.tops[0]
    assert exp == NumberExprAST(2)


def test_identifier():
    ast = parse("a")
    exp = ast.tops[0]
    assert exp == VariableExprAST("a")


def test_call():
    ast = parse("f(1, 2)")
    exp = ast.tops[0]
    assert exp == CallExprAST(callee="f", args=[NumberExprAST(1), NumberExprAST(2)])


def test_binary():
    p = """
    1 + 2
    3 * 4
    0 < 5
    """.strip()
    ast = parse(p)

    assert ast == Program(
        tops=[
            BinaryExprAST("+", NumberExprAST(1), NumberExprAST(2)),
            BinaryExprAST("*", NumberExprAST(3), NumberExprAST(4)),
            BinaryExprAST("<", NumberExprAST(0), NumberExprAST(5)),
        ]
    )


def test_precedence():
    p = """
    1 + 2 * 3
    3 * 4 - 5
    0 < 5 - a
    (1 + 2) * 3
    """.strip()
    ast = parse(p)

    assert ast == Program(
        tops=[
            BinaryExprAST(
                "+",
                NumberExprAST(1),
                BinaryExprAST("*", NumberExprAST(2), NumberExprAST(3)),
            ),
            BinaryExprAST(
                "-",
                BinaryExprAST("*", NumberExprAST(3), NumberExprAST(4)),
                NumberExprAST(5),
            ),
            BinaryExprAST(
                "<",
                NumberExprAST(0),
                BinaryExprAST("-", NumberExprAST(5), VariableExprAST("a")),
            ),
            BinaryExprAST(
                "*",
                BinaryExprAST("+", NumberExprAST(1), NumberExprAST(2)),
                NumberExprAST(3),
            ),
        ]
    )


def test_extern():
    ast = parse("extern sin(alpha)")
    exp = ast.tops[0]
    assert exp == ExternalDeclaration(proto=PrototypeAST("sin", args=["alpha"]))


def test_funcdef():
    ast = parse("def diff(x, y) x - y")
    exp = ast.tops[0]
    assert exp == FunctionAST(
        proto=PrototypeAST("diff", args=["x", "y"]),
        body=BinaryExprAST("-", VariableExprAST("x"), VariableExprAST("y")),
    )
