class Stack:
    def __init__(self):
        self.collection = list()  # Or use LinkedList and QueueLinkedList for queue

    def push(self, data):
        self.collection.append(data)

    def pop(self):
        return self.collection.pop()  # analog self.collection[-1]
