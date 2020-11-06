from binary_trees.binary_tree_node import BinaryTreeNode


class BinaryTree:
    def __init__(self):
        self.__head = None

    def add(self, data):
        new_node = BinaryTreeNode(data)
        if self.__head is None:   # if tree empty
            self.__head = new_node
        else:
            self.__add_new_node(self.__head, new_node)

    def __add_new_node(self, current_node, new_node):
        compare = current_node.compare(new_node)
        direction = 'left' if compare == 'less' else 'right'

        child_node = current_node.get_node(direction)
        if child_node is None:
            current_node.set_node(new_node, direction)
        else:
            self.__add_new_node(child_node, new_node)

    def remove(self, value):
        current, parent = self.__find_with_parent(value)
        if current is None:
            return False
        current_right = current.get_node('right')
        current_left = current.get_node('left')
        # Case 1: If current has no right child, current's left replaces current.
        if current_right is None:
            if parent is None:
                self.__head = current_left
            else:
                compare = parent.compare(current.value)
                direction = 'left' if compare == 'less' else 'right'
                parent.set_node(current_left, direction)
        # Case 2: If current 's right child has no left child,
        # current's right child replaces current.
        elif current_right.get_node('left') is None:
            current_right.set_node(current_left, 'left')
            if parent is None:
                self.__head = current_right
            else:
                compare = parent.compare(current.value)
                direction = 'left' if compare == 'less' else 'right'
                parent.set_node(current_right, direction)
        # Case 3: If current's right child has a left child,
        # replace current with current's right child's left-most child.
        else:
            leftmost_parent = current_right
            leftmost = current_right.get_node('left')
            while leftmost.get_node('left') is not None:
                leftmost_parent = leftmost
                leftmost = leftmost.get_node('left')
            # The parent's left subtree becomes the leftmost's right subtree.
            leftmost_right = leftmost.get_node('right')
            leftmost_parent.set_node(leftmost_right, 'left')
            # Assign leftmost's left and right to current's left and right children.
            leftmost.set_node(current_left, 'left')
            leftmost.set_node(current_right, 'right')
            if parent is None:
                self.__head = leftmost
            else:
                compare = parent.compare(current.value)
                direction = 'left' if compare == 'less' else 'right'
                parent.set_node(leftmost, direction)
        return True

    def __find_with_parent(self, remove_value):
        current = self.__head
        parent = None
        while current is not None:
            compare = current.compare(remove_value)
            if compare == 'equal':
                break
            direction = 'left' if compare == 'less' else 'right'
            parent = current
            current = current.get_node(direction)
        return current, parent
    
    def print(self):
        pass
