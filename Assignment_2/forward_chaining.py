class Forward:
    def __init__(self, kb, query) -> None:
        self.kb = kb
        self.query = query

    def inference(self):
        """
        Perform Forward Chaining inference.
        """
        inferred = set()
        agenda = set()

        # Add facts to the agenda
        for rule in self.kb:
            if "=>" not in rule:
                agenda.add(rule)
                inferred.add(rule)

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
                        if antecedent_facts.issubset(inferred) and consequent not in inferred:
                            agenda.add(consequent)
                            inferred.add(consequent)
                    elif antecedent in inferred and consequent not in inferred:
                        agenda.add(consequent)
                        inferred.add(consequent)

        # Repeatedly apply the rules until no new facts are inferred
        while True:
            new_facts = False
            for rule in self.kb:
                if "=>" in rule:
                    antecedent, consequent = rule.split("=>")
                    antecedent = antecedent.strip()
                    consequent = consequent.strip()

                    # Check if the antecedent is a conjunction of multiple facts
                    if "&" in antecedent:
                        antecedent_facts = set(antecedent.split("&"))
                        if antecedent_facts.issubset(inferred) and consequent not in inferred:
                            inferred.add(consequent)
                            new_facts = True
                    elif antecedent in inferred and consequent not in inferred:
                        inferred.add(consequent)
                        new_facts = True

            if not new_facts:
                break

        if self.query in inferred:
            return "YES: " + ", ".join(sorted(inferred))
        else:
            return "NO"