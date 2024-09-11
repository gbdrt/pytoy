from stack import *


def test_stack():
    assert Stack().isempty()


def test_isempty():
    s = Stack()
    s.push(42)
    assert not s.isempty()
