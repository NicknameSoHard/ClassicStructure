class Stack:
    def __init__(self, collection=list):
        self.collection = collection()  # Or use LinkedList

    def push(self, data):
        self.collection.append(data)

    def pop(self):
        return self.collection.pop()  # analog self.collection[-1]

    def __str__(self):
        return ','.join([str(i) for i in self.collection])
