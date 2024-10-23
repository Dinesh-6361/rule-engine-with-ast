import unittest
from api import create_rule, combine_rules, evaluate_rule

class TestRuleEngine(unittest.TestCase):

    def test_create_rule(self):
        rule = "((age > 30 AND department = 'Sales'))"
        ast = create_rule(rule)
        self.assertIsNotNone(ast)
        self.assertEqual(ast.type, "operator")

    def test_combine_rules(self):
        rules = [
            "((age > 30 AND department = 'Sales'))",
            "((age < 25 AND department = 'Marketing'))"
        ]
        combined_ast = combine_rules(rules)
        self.assertIsNotNone(combined_ast)
        self.assertEqual(combined_ast.type, "operator")

    def test_evaluate_rule(self):
        ast = create_rule("age > 30")
        user_data = {"age": 35}
        result = evaluate_rule(ast, user_data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
