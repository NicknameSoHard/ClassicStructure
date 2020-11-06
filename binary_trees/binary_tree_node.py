class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def compare(self, value):
        value = value.value if isinstance(value, BinaryTreeNode) else value
        if self.value < value:
            return 'more'
        elif self.value > value:
            return 'less'
        else:
            return 'equal'

    def get_node(self, direction):
        if direction == 'left':
            return self.left_node
        else:
            return self.right_node

    def set_node(self, new_node, direction):
        if direction == 'left':
            self.left_node = new_node
        else:
            self.right_node = new_node

    def __str__(self):
        return str(self.value)

