class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.__next_elem = None

    def set_next_elem(self, new_element):
        self.__next_elem = new_element

    def get_next_elem(self):
        return self.__next_elem

    def __str__(self):
        return str(self.data)
