from ast_node import Node

def create_rule(rule_string):
    """
    Parse the rule string and create an AST.
    Example rule: ((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing'))
    """
    # Manual AST creation for now (you can replace this with an actual parser later)
    root = Node(type='operator', value='AND')
    left_child = Node(type='operand', value="age > 30 AND department = 'Sales'")
    right_child = Node(type='operand', value="age < 25 AND department = 'Marketing'")
    
    root.left = left_child
    root.right = right_child
    
    return root

def combine_rules(rules):
    """
    Combine multiple rules into one AST. Currently simplified logic.
    """
    # Combine rules using a root "OR" operator as an example
    root = Node(type='operator', value='OR')
    
    if len(rules) >= 2:
        # Combine the first two rules
        left_child = create_rule(rules[0])
        right_child = create_rule(rules[1])
        
        root.left = left_child
        root.right = right_child
    
    # If there are more than 2 rules, you can extend this logic to combine them iteratively
    return root

def evaluate_rule(ast, user_data):
    """
    Evaluate the rule (AST) against user data.
    """
    if ast.type == 'operator' and ast.value == 'AND':
        return (evaluate_rule(ast.left, user_data) and evaluate_rule(ast.right, user_data))
    elif ast.type == 'operator' and ast.value == 'OR':
        return (evaluate_rule(ast.left, user_data) or evaluate_rule(ast.right, user_data))
    elif ast.type == 'operand':
        # Simplified evaluation logic for operands, you need a real parser here
        if "age > 30" in ast.value and user_data.get('age', 0) > 30:
            return True
        if "department = 'Sales'" in ast.value and user_data.get('department', '') == 'Sales':
            return True
        if "age < 25" in ast.value and user_data.get('age', 0) < 25:
            return True
        if "department = 'Marketing'" in ast.value and user_data.get('department', '') == 'Marketing':
            return True
    return False
