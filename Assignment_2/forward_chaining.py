class Forward:
    def __init__(self, kb, query) -> None:
        """
        Initialize the Forward Chaining object.

        :param kb: The knowledge base as a list of rules.
        :param query: The query to be inferred.
        """
        self.kb = kb
        self.query = query

    def inference(self):
        """
        Perform Forward Chaining inference.

        :return: A string indicating the result of the inference.
        """
        # Set to store the inferred facts
        inferred = set()
        # Set to store the facts to be processed (agenda)
        agenda = set()

        # Add initial facts to the agenda and inferred set
        for rule in self.kb:
            if "=>" not in rule:
                inferred.add(rule)

        # Process facts from the agenda
        while agenda:
            fact = agenda.pop()

            # Generate new facts based on the rules
            for rule in self.kb:
                if "=>" in rule:
                    antecedent, consequent = rule.split("=>")
                    antecedent = antecedent.strip()
                    consequent = consequent.strip()

                    # Check if the antecedent is a conjunction of multiple facts
                    if "&" in antecedent:
                        antecedent_facts = set(antecedent.split("&"))
                        # If all antecedent facts are inferred and the consequent is not inferred,
                        # add the consequent to the agenda and inferred set
                        if antecedent_facts.issubset(inferred) and consequent not in inferred:
                            inferred.add(consequent)
                    # If the antecedent is a single fact and it is inferred,
                    # add the consequent to the agenda and inferred set
                    elif antecedent in inferred and consequent not in inferred:
                        inferred.add(consequent)

        # Check if the query is in the inferred set
        if self.query in inferred:
            # If the query is inferred, return "YES" along with the sorted list of inferred facts
            return "YES: " + ", ".join(sorted(inferred))
        else:
            # If the query is not inferred, return "NO"
            return "NO"