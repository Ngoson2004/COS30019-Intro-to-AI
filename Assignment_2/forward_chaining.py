class Forward:
    def __init__(self, kb, query) -> None:
        """
        Initialize the Forward Chaining object.
        :param kb: The parsed knowledge base.
        :param query: The parsed query.
        """
        self.kb = kb
        self.query = query

    def inference(self):
        """
        Perform Forward Chaining inference.
        :return: A string indicating the result of the inference.
        """
        # Print the parsed knowledge base and query
        print("Parsed Knowledge Base:")
        for fact_or_rule in self.kb:
            print(fact_or_rule)
        print("\nParsed Query:")
        print(self.query)
        print()

        # List to store the inferred facts in the order they were inferred
        inferred = []
        # List to store the facts to be processed (agenda)
        agenda = []

        # Add initial facts to the agenda and inferred list
        for fact in self.kb:
            if fact['type'] == 'proposition':
                agenda.append(fact['symbol']['symbol'])
                inferred.append(fact['symbol']['symbol'])

        # Process facts from the agenda
        while agenda:
            fact = agenda.pop(0)  # Remove the first fact from the agenda

            # Generate new facts based on the rules
            for rule in self.kb:
                if rule['type'] == 'implication':
                    antecedent = rule['antecedent']
                    consequent = rule['consequent']

                    # Check if the antecedent is a conjunction of multiple facts
                    if antecedent['type'] == 'conjunction':
                        antecedent_facts = set(fact['symbol'] for fact in antecedent['arguments'])
                        if all(f in inferred for f in antecedent_facts) and consequent['symbol'] not in inferred:
                            agenda.append(consequent['symbol'])
                            inferred.append(consequent['symbol'])
                    # If the antecedent is a single fact and it is inferred,
                    # add the consequent to the agenda and inferred list
                    elif antecedent['type'] == 'atomic' and antecedent['symbol'] in inferred and consequent['symbol'] not in inferred:
                        agenda.append(consequent['symbol'])
                        inferred.append(consequent['symbol'])

        # Print the inferred facts
        print("Inferred Facts:")
        print(inferred)
        print()

        # Check if the query is in the inferred list
        if self.query['type'] == 'atomic' and self.query['symbol'] in inferred:
            # If the query is inferred, return "YES" along with the inferred facts in the order they were inferred
            return "YES: " + ", ".join(inferred)
        else:
            # If the query is not inferred, return "NO"
            return "NO"