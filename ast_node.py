class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type  # 'operator' or 'operand'
        self.value = value  # e.g., 'AND', 'age > 30', etc.
        self.left = left  # Left child node
        self.right = right  # Right child node

    def to_dict(self):
        """Helper method to convert Node to dictionary for JSON responses"""
        return {
            'type': self.type,
            'value': self.value,
            'left': self.left.to_dict() if self.left else None,
            'right': self.right.to_dict() if self.right else None
        }
