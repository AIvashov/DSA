import pytest

from data_structures import Stack


def test_stack():
    stack = Stack()
    assert stack.is_empty
    stack.push(1)
    stack.push(5)
    stack.push(8)
    assert stack.size == 3
    assert stack.peek == 8
    assert stack.pop() == 8
    assert stack.size == 2
    assert stack.max_size is None
    assert not stack.is_full
    stack = Stack(10)
    for i in range(10):
        stack.push(i)
    assert stack.is_full


def test_stack_exceptions():
    stack = Stack()
    with pytest.raises(IndexError, match='Can not pop from an empty stack!'):
        stack.pop()

    with pytest.raises(IndexError, match='Can not peek empty stack'):
        stack.peek()

    stack = Stack(10)
    for i in range(10):
        stack.push(i)
    with pytest.raises(IndexError, match='Stack is full!'):
        stack.push(1)

