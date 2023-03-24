class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def construct_expression_tree(postfix):
    stack = []
    for char in postfix:
        if char.isdigit() or char.isalpha():
            node = Node(char)
            stack.append(node)
        else:
            right_node = stack.pop()
            left_node = stack.pop()
            operator_node = Node(char)
            operator_node.left = left_node
            operator_node.right = right_node
            stack.append(operator_node)
    return stack.pop()

def infix_traversal(node):
    if node is not None:
        if node.left is not None or node.right is not None:
            print("(", end="")
        infix_traversal(node.left)
        print(node.value, end="")
        infix_traversal(node.right)
        if node.left is not None or node.right is not None:
            print(")", end="")
