from flask import Flask, request, jsonify
from flask_restful import Api
from database import Session, Rule
from api import create_rule, combine_rules, evaluate_rule

app = Flask(__name__)
api = Api(app)

# Root route to avoid 404 errors when visiting the home page
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Rule Engine API!"})

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    data = request.json
    rule_string = data.get('rule_string', '')
    print(f"Received rule_string: {rule_string}")  # Debugging info

    try:
        # Create a rule and return its AST representation
        ast_node = create_rule(rule_string)
        print(f"AST Node created: {ast_node}")  # Debugging info
        return jsonify({'status': 'success', 'ast': ast_node.to_dict()}), 201
    except Exception as e:
        print(f"Error occurred: {e}")  # Debugging info
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    data = request.json
    rules = data.get('rules', [])
    print(f"Received rules for combination: {rules}")  # Debugging info

    try:
        # Combine multiple rules into one AST
        combined_ast_node = combine_rules(rules)
        print(f"Combined AST Node created: {combined_ast_node}")  # Debugging info
        return jsonify({'status': 'success', 'combined_ast': combined_ast_node.to_dict()}), 200
    except Exception as e:
        print(f"Error occurred: {e}")  # Debugging info
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    data = request.json
    ast = data.get('ast', None)
    user_data = data.get('user_data', {})
    print(f"Received AST: {ast} and User Data: {user_data}")  # Debugging info

    try:
        # Evaluate the AST against the provided user data
        result = evaluate_rule(ast, user_data)
        print(f"Evaluation result: {result}")  # Debugging info
        return jsonify({'status': 'success', 'result': result}), 200
    except Exception as e:
        print(f"Error occurred: {e}")  # Debugging info
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
