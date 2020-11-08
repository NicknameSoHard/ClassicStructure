from linked_lists.queue_linked_list import QueueLinkedList


class Queue:
    def __init__(self, collection=QueueLinkedList):
        self.collection = collection()

    def push(self, data):
        self.collection.append(data)

    def pop(self):
        return self.collection.pop()

    def __str__(self):
        return ','.join([str(i) for i in self.collection])
