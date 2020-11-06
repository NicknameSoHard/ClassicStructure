class Stack:
    def __init__(self, collection=list):
        self.collection = collection()  # Or use LinkedList or QueueLinkedList for queue

    def push(self, data):
        self.collection.append(data)

    def pop(self):
        return self.collection.pop()  # analog self.collection[-1]
