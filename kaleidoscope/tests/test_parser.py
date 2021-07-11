from kaleidoscope.ast import (
    BinaryExprAST,
    CallExprAST,
    ExternalDeclaration,
    FunctionAST,
    IfExprAST,
    NumberExprAST,
    PrototypeAST,
    VariableExprAST,
)
from kaleidoscope.parser import make_anonymous, parse


def test_number():
    assert parse("2") == make_anonymous(NumberExprAST(2))


def test_identifier():
    assert parse("a") == make_anonymous(VariableExprAST("a"))


def test_call():
    assert parse("f(1, 2)") == make_anonymous(
        CallExprAST(callee="f", args=[NumberExprAST(1), NumberExprAST(2)])
    )


def test_if():
    assert parse("if x < 0 then 0 else 1") == make_anonymous(
        IfExprAST(
            BinaryExprAST("<", VariableExprAST("x"), NumberExprAST(0)),
            NumberExprAST(0),
            NumberExprAST(1),
        )
    )


def test_binary():
    assert parse("1 + 2") == make_anonymous(
        BinaryExprAST("+", NumberExprAST(1), NumberExprAST(2))
    )
    assert parse("3 * 4") == make_anonymous(
        BinaryExprAST("*", NumberExprAST(3), NumberExprAST(4))
    )
    assert parse("0 < 5") == make_anonymous(
        BinaryExprAST("<", NumberExprAST(0), NumberExprAST(5))
    )


def test_precedence():
    assert parse("1 + 2 * 3") == make_anonymous(
        BinaryExprAST(
            "+",
            NumberExprAST(1),
            BinaryExprAST("*", NumberExprAST(2), NumberExprAST(3)),
        )
    )

    assert parse("3 * 4 - 5") == make_anonymous(
        BinaryExprAST(
            "-",
            BinaryExprAST("*", NumberExprAST(3), NumberExprAST(4)),
            NumberExprAST(5),
        )
    )

    assert parse("0 < 5 - a") == make_anonymous(
        BinaryExprAST(
            "<",
            NumberExprAST(0),
            BinaryExprAST("-", NumberExprAST(5), VariableExprAST("a")),
        )
    )

    assert parse("(1 + 2) * 3") == make_anonymous(
        BinaryExprAST(
            "*",
            BinaryExprAST("+", NumberExprAST(1), NumberExprAST(2)),
            NumberExprAST(3),
        )
    )


def test_extern():
    assert parse("extern sin(alpha)") == ExternalDeclaration(
        proto=PrototypeAST("sin", args=["alpha"])
    )


def test_funcdef():
    assert parse("def diff(x, y) x - y") == FunctionAST(
        proto=PrototypeAST("diff", args=["x", "y"]),
        body=BinaryExprAST("-", VariableExprAST("x"), VariableExprAST("y")),
    )
