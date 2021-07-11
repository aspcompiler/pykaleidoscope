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
