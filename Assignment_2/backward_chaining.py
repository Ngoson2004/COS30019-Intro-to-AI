class Backward:
    def __init__(self, kb, query):
        self.kb = kb
        self.query = query
        self.entail = set()

    def inference(self):
        def backward(kb, query):
            rules = {}
            facts = []
            for expr in kb:
                if "<=>" in expr:
                    left, right = expr.split('<=>')
                    if left not in rules:
                        rules[left] = []
                    if right not in rules:
                        rules[right] = []
                    rules[left].append(left)
                    rules[right].append(right)
                elif "=>" in expr:
                    antecedent, consequent = expr.split('=>')
                    if consequent.strip() not in rules:
                        rules[consequent.strip()] = []
                    rules[consequent.strip()].append(antecedent.strip())
                else:
                    facts.append(expr.strip())

            def prove(goal):
                if goal in facts:
                    self.entail.add(goal)
                    return True
                if goal.startswith('not '):
                    negated_query = goal.strip('not ').strip()
                    if negated_query not in facts and not prove(negated_query):
                        return True
                    return False
                # If the query is not a fact, check if there are rules to derive it
                if goal in rules:
                    print('\ngoal:',goal)
                    print("premise:",rules[goal])
                    print(rules)
                    
                    for antecedent in rules[goal]:
                        if '||' in antecedent:
                            if any(prove(symbol.strip()) for symbol in antecedent.split('||')):
                                self.entail.add(goal)
                                return True
                        else:
                            if all(prove(symbol.strip()) for symbol in antecedent.split('&')):
                                self.entail.add(goal)
                                return True
                        # all_premises_proven = True
                        # for symbol in antecedent.split('&'):
                        #     if not prove(symbol): #prove(symbol.strip()):
                        #         all_premises_proven = False
                        #         break
                        # if all_premises_proven:
                        #     #print(rules)
                        #     if goal not in self.entail:
                        #         self.entail.add(goal)
                        #     return True
                        
                return False
            
            return prove(query)

        if backward(self.kb, self.query):
            print(self.entail)
            return "YES: " + ', '.join(self.entail)
        else:
            return "NO"