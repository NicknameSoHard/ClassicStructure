from queue import Queue

from linked_lists import LinkedList, QueueLinkedList


def check_creation_structure(struct, list_size=10):
    s = struct()
    for i in range(list_size):
        s.append(i)
    return s


def test_queue_linked_list(list_size=5):
    queue = Queue()
    for i in range(list_size):
        queue.put(i)
    qll = check_creation_structure(QueueLinkedList)

    for i in range(list_size):
        assert qll.pop() == queue.get()


def test_linked_list(list_size=10):
    test_list = [str(i) for i in range(list_size)]
    ll = check_creation_structure(LinkedList)

    assert str(ll) == ','.join(test_list)

    ll.remove_by_index(0)
    test_list.pop(0)
    assert str(ll) == ','.join(test_list)

    ll.remove_by_index(5)
    test_list.pop(5)
    assert str(ll) == ','.join(test_list)
