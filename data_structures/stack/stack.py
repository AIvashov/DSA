from typing import Any, Optional


class Stack:
    """
    A stack is a linear data structure that follows the principle of Last In First Out (LIFO).
    This means the last element inserted inside the stack is removed first.
    """

    def __init__(self, max_size: Optional[int] = None) -> None:
        """
        Init empty stack.
        :param max_size: Max stack size, by default is None.
        """
        self._stack = []
        self._max_size = max_size

    def push(self, value: Any) -> None:
        """
        Push value to stack.
        :param value: Value for append to stack.
        :raise Exception, if stack size becomes larger self._max_size.
        """
        if self._max_size is not None and self._max_size <= len(self._stack):
            raise IndexError('Stack is full!')
        self._stack.append(value)

    def pop(self) -> Any:
        """
        Remove the last item from stack.
        :raise Exception, if stack is empty.
        """
        if len(self._stack) == 0:
            raise IndexError('Can not pop from an empty stack!')

        return self._stack.pop()

    @property
    def is_empty(self) -> bool:
        """
        Check if stack is empty.
        :return: Boolean.
        """
        return len(self._stack) == 0

    @property
    def is_full(self) -> bool:
        """
        Check if stack is full.
        :return: Boolean.
        """
        return len(self._stack) == self._max_size

    @property
    def size(self) -> int:
        """
        Get stack size.
        :return: Stack size.
        """
        return len(self._stack)

    @property
    def peek(self) -> Any:
        """
        Get the value of the top element without removing it.
        :raise Exception, if stack is empty.
        :return: Last element.
        """
        if len(self._stack) == 0:
            raise IndexError('Can not peek empty stack')
        return self._stack[-1]

    @property
    def max_size(self) -> Optional[int]:
        """
        Get max stack size.
        :return: Max size.
        """
        return self._max_size
