import itertools

class Truth_Table:
    def __init__(self, kb, query):
        self.kb = kb
        self.query = query
        

    def inference(self):
        # Extract all unique propositional symbols from the knowledge base and query
        symbols = set()
        for expression in self.kb + [self.query]:
            for char in expression:
                if char.isalpha() and char not in symbols:
                    symbols.add(char)
                    
        symbols = list(symbols)  # Convert set to list
        print(symbols)
        # Generate all possible interpretations (combinations of truth values for each symbol)
        all_interpretations = list(itertools.product([False, True], repeat=len(symbols)))

        # Function to evaluate an expression given a truth assignment
        def prepare_expression(expr, symbol_table):
            for symbol in symbols:
                expr = expr.replace(symbol, f'{symbol_table[symbol]}')
            expr = expr.replace('&', ' and ').replace('|', ' or ').replace('=>', ' <= ').replace('<=>', ' == ').replace('~', ' not ')
            return expr

        # Check each interpretation
        for interpretation in all_interpretations:
            symbol_table = dict(zip(symbols, interpretation))
            prepared_kb = [prepare_expression(expr, symbol_table) for expr in self.kb]
            prepared_query = prepare_expression(self.query, symbol_table)
            # Evaluate the knowledge base under the current interpretation
            kb_true = all(eval(expr) for expr in prepared_kb)
            
            if kb_true:
                # If the knowledge base is true, check if the query is also true
                if eval(prepared_query):
                    return "Yes" #+ f": {len()}"

        return "No"