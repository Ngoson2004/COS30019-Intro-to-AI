import itertools
import re
from kb_parser import parse_input

class Truth_Table:
    def __init__(self, input_string):
        self.kb, self.query = parse_input(input_string)
        print("Knowledge Base:", self.kb)
        print("Query:", self.query)

    def inference(self):
        # Extract all unique propositional symbols from the knowledge base and query
        symbols = set()
        for clause in self.kb:
            symbols.update(self.get_symbols(clause))
        symbols.update(self.get_symbols(self.query))

        print(symbols)  # debugging symbols extraction

        # Generate all possible interpretations (combinations of truth values for each symbol)
        all_interpretations = list(itertools.product([False, True], repeat=len(symbols)))

        model_count = 0  # introduce counter to print the number of models

        # Function to evaluate an expression given a truth assignment
        def evaluate_expression(expr, symbol_table):
            if expr['type'] == 'atomic':
                return symbol_table[expr['symbol']]
            elif expr['type'] == 'negation':
                return not evaluate_expression(expr['argument'], symbol_table)
            elif expr['type'] == 'conjunction':
                return all(evaluate_expression(arg, symbol_table) for arg in expr['arguments'])
            elif expr['type'] == 'disjunction':
                return any(evaluate_expression(arg, symbol_table) for arg in expr['arguments'])
            elif expr['type'] == 'implication':
                antecedent = evaluate_expression(expr['antecedent'], symbol_table)
                consequent = evaluate_expression(expr['consequent'], symbol_table)
                return not antecedent or consequent
            elif expr['type'] == 'biconditional':
                left = evaluate_expression(expr['left'], symbol_table)
                right = evaluate_expression(expr['right'], symbol_table)
                return left == right
            elif expr['type'] == 'proposition':
                return evaluate_expression(expr['symbol'], symbol_table)

        # Check each interpretation
        for interpretation in all_interpretations:
            symbol_table = dict(zip(symbols, interpretation))

            # Evaluate the knowledge base under the current interpretation
            kb_true = all(evaluate_expression(clause, symbol_table) for clause in self.kb)

            if kb_true and evaluate_expression(self.query, symbol_table):
                # Check if the knowledge base is true and the query is true
                model_count += 1

        return "YES: " + str(model_count) if model_count > 0 else "NO"

    def get_symbols(self, expr):
        if expr['type'] == 'atomic':
            return {expr['symbol']}
        elif expr['type'] == 'negation':
            return self.get_symbols(expr['argument'])
        elif expr['type'] == 'conjunction':
            symbols = set()
            for arg in expr['arguments']:
                symbols.update(self.get_symbols(arg))
            return symbols
        elif expr['type'] == 'disjunction':
            symbols = set()
            for arg in expr['arguments']:
                symbols.update(self.get_symbols(arg))
            return symbols
        elif expr['type'] == 'implication':
            return self.get_symbols(expr['antecedent']) | self.get_symbols(expr['consequent'])
        elif expr['type'] == 'biconditional':
            return self.get_symbols(expr['left']) | self.get_symbols(expr['right'])
        elif expr['type'] == 'proposition':
            return self.get_symbols(expr['symbol'])