from kaleidoscope.evaluator import Evaluator


def test_basic():
    e = Evaluator()
    assert e.evaluate("3") == 3.0
    assert e.evaluate("3+3*4"), 15.0


def test_use_func():
    e = Evaluator()
    assert e.evaluate("def adder(x y) x+y") is None
    assert e.evaluate("adder(5, 4) + adder(3, 2)") == 14.0


def test_use_libc():
    e = Evaluator()
    assert e.evaluate("extern ceil(x)") is None
    assert e.evaluate("ceil(4.5)") == 5.0
    assert e.evaluate("extern floor(x)") is None
    assert e.evaluate("def cfadder(x) ceil(x) + floor(x)") is None
    assert e.evaluate("cfadder(3.14)") == 7.0


def test_if_expression():
    e = Evaluator()
    assert e.evaluate("if 1 < 2 then 1 else 2") == 1


def test_if_function():
    e = Evaluator()
    e.evaluate("def foo(a b) a * if a < b then a + 1 else b + 1")
    assert e.evaluate("foo(3, 4)") == 12
    assert e.evaluate("foo(5, 4)") == 25


def test_nested_if_funcion():
    e = Evaluator()
    e.evaluate(
        """
        def foo(a b c)
            if a < b
                then if a < c then a * 2 else c * 2
                else b * 2"""
    )
    assert e.evaluate("foo(1, 20, 300)") == 2
    assert e.evaluate("foo(10, 2, 300)") == 4
    assert e.evaluate("foo(100, 2000, 30)") == 60


def test_for_expr():
    e = Evaluator()
    e.evaluate(
        """
        def foo(n)
            for i = 1.0, i < n, 1.0 in i
        """
    )
    assert e.evaluate("foo(9)") == 10.0
