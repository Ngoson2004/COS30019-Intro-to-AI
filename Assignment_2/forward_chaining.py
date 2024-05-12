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
        # List to store the inferred facts in the order they were inferred
        inferred = []
        # List to store the facts to be processed (agenda)
        agenda = []

        # Add initial facts to the agenda and inferred list
        for rule in self.kb:
            if "=>" not in rule:
                agenda.append(rule)
                inferred.append(rule)

        # Process facts from the agenda
        while agenda:
            fact = agenda.pop(0)  # Remove the first fact from the agenda

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
                        # add the consequent to the agenda and inferred list
                        if antecedent_facts.issubset(set(inferred)) and consequent not in inferred:
                            agenda.append(consequent)
                            inferred.append(consequent)
                    # If the antecedent is a single fact and it is inferred,
                    # add the consequent to the agenda and inferred list
                    elif antecedent in inferred and consequent not in inferred:
                        agenda.append(consequent)
                        inferred.append(consequent)

        # Check if the query is in the inferred list
        if self.query in inferred:
            # If the query is inferred, return "YES" along with the inferred facts in the order they were inferred
            return "YES: " + ", ".join(inferred)
        else:
            # If the query is not inferred, return "NO"
            return "NO"