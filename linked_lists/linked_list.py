from linked_lists.linked_node import LinkedNode


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def add(self, new_data):
        new_element = LinkedNode(new_data)
        if self.__head is None:
            self.__head = new_element
        else:
            self.__tail.set_next_elem(new_element)
        self.__tail = new_element

    def __collection_iterator(self):
        next_elem = self.__head
        while True:
            if next_elem is None:
                break
            yield next_elem
            next_elem = next_elem.get_next_elem()

    def remove_by_index(self, removed_index):
        if self.__head is None:
            raise ValueError('Collection is empty!')

        if removed_index == 0:
            value = self.__head.data
            self.__head = self.__head.get_next_elem()
            return value
        else:
            last_node = self.__head
            for index, node in enumerate(self.__collection_iterator()):
                if index == removed_index:
                    next_node = node.get_next_elem()
                    last_node.set_next_elem(next_node)
                    return node.data
                last_node = node
        raise ValueError('Index not found!')

    def find_by_values(self, values):
        for node in self.__collection_iterator():
            if node.data == values:
                return node
        return None

    def __str__(self):
        return ','.join([str(node) for node in self.__collection_iterator()])
