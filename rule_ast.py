class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" for AND/OR, "operand" for conditions
        self.left = left       # Left child Node
        self.right = right     # Right child Node (for operators)
        self.value = value     # Value for operand nodes (e.g., number for comparisons)

    def __repr__(self):
        if self.type == "operator":
            return f"Node({self.type}, {self.left}, {self.right})"
        return f"Node({self.type}, value={self.value})"
