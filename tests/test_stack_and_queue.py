from queue import Queue as PythonQueue

from stack_and_queue import Stack, Queue


def fill_structure(struct, size):
    for i in range(size):
        struct.push(i)
    return struct


def test_stack(list_size=10):
    test_list = [str(i) for i in range(list_size)]
    stack = fill_structure(Stack(), list_size)
    assert str(stack) == ','.join(test_list)

    for i in range(list_size):
        assert str(stack.pop()) == test_list.pop()


def test_queue(list_size=10):
    py_queue = PythonQueue()
    my_queue = Queue()
    for i in range(list_size):
        py_queue.put(i)
        my_queue.push(i)

    for i in range(list_size):
        assert my_queue.pop() == py_queue.get()
