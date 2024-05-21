import itertools
import re
from generic_converter import to_horn_form

class Truth_Table:
    def __init__(self, kb, query):
        self.kb = to_horn_form(kb)
        self.query = query

    def inference(self):
        # Extract all unique propositional symbols from the knowledge base and query
        print("\nProcessed KB:",'; '.join(self.kb))
        # Use regular expressions to find and replace only whole word symbols, ensuring that partial matches (like replacing 'a' in 'cat') do not occur.
        symbols = set(re.findall(r'\b\w+\b', ' '.join(self.kb + [self.query])))
        #symbols.difference_update(set(['and', 'or', 'not']))  # Remove logical keywords if accidentally captured
        #print(symbols)  # debugging symbols extraction

        # Generate all possible interpretations (combinations of truth values for each symbol)
        all_interpretations = list(itertools.product([False, True], repeat=len(symbols)))
        model_count = 0  # introduce counter to print the number of model
        # print("Interpret:",all_interpretations[0])

        # Function to evaluate an expression given a truth assignment
        def prepare_expression(expr, symbol_table):
            # Replace each symbol with its truth value in symbol_table
            for symbol in symbols:
                expr = re.sub(r'\b' + re.escape(symbol) + r'\b', f'{symbol_table[symbol]}', expr)

            # Replace connectives with Python logical expression
            expr = expr.replace('=>', '<=').replace('&', ' and ')
            # Replace implications followed by negations with their logical equivalents
            expr = re.sub(r'\b(\w+)\s*=>\s*~(\w+)\b', r'not (\1 and \2)', expr)

            # # Replace negation operator
            expr = expr.replace('~', ' not ')
            # # Replace negation operator followed by True with False
            expr = expr.replace('not True', ' False ')
            expr = expr.replace('not False', ' True ')

            return expr

        # Check each interpretation
        for interpretation in all_interpretations:
            symbol_table = dict(zip(symbols, interpretation))
            prepared_kb = [prepare_expression(expr, symbol_table) for expr in self.kb]
            prepared_query = prepare_expression(self.query, symbol_table)

            #print("Table:",symbol_table)
            #print("KB:", prepared_kb)
            #print(prepared_query)

            # Evaluate the knowledge base under the current interpretation
            kb_true = all(eval(expr) for expr in prepared_kb)
            if kb_true and eval(prepared_query):
                # Check if the knowledge base is true and the query is true
                model_count += 1

        return "YES: " + str(model_count) if model_count > 0 else "NO"