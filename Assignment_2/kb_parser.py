def parse_input(input_string):
    # Remove whitespace and split the input string into knowledge base and query
    input_string = input_string.strip()
    kb_query = input_string.split(';')
    kb_str = ';'.join(kb_query[:-1])
    query = kb_query[-1]

    # Parse the knowledge base and query
    kb = parse_kb(kb_str)
    parsed_query = parse_query(query)

    return kb, parsed_query

def parse_kb(kb_str):
    # Remove the 'TELL' keyword and any leading/trailing whitespace
    kb_str = kb_str.replace('TELL', '').strip()

    # Split the knowledge base into individual clauses
    clauses = kb_str.split(';')

    # Parse each clause and build the knowledge base
    kb = []
    for clause in clauses:
        if '=>' in clause:
            antecedent, consequent = clause.split('=>', 1)
            kb.append({'type': 'implication', 'antecedent': parse_proposition(antecedent), 'consequent': parse_proposition(consequent)})
        elif '<=>' in clause:
            left, right = clause.split('<=>', 1)
            kb.append({'type': 'biconditional', 'left': parse_proposition(left), 'right': parse_proposition(right)})
        else:
            kb.append({'type': 'proposition', 'symbol': parse_proposition(clause)})

    return kb

def parse_query(query_str):
    # Remove the 'ASK' keyword and any leading/trailing whitespace
    query_str = query_str.replace('ASK', '').strip()

    # Parse the query proposition
    query = parse_proposition(query_str)
    return query

def parse_proposition(prop_str):
    prop_str = prop_str.strip()
    return parse_biconditional(prop_str)

def parse_biconditional(prop_str):
    if '<=>' in prop_str:
        left, right = map(str.strip, prop_str.split('<=>', 1))
        return {'type': 'biconditional', 'left': parse_implication(left), 'right': parse_implication(right)}
    else:
        return parse_implication(prop_str)

def parse_implication(prop_str):
    if '=>' in prop_str:
        left, right = map(str.strip, prop_str.split('=>', 1))
        return {'type': 'implication', 'antecedent': parse_disjunction(left), 'consequent': parse_disjunction(right)}
    else:
        return parse_disjunction(prop_str)

def parse_disjunction(prop_str):
    if '||' in prop_str:
        disjuncts = list(map(str.strip, prop_str.split('||')))
        return {'type': 'disjunction', 'arguments': [parse_conjunction(disjunct) for disjunct in disjuncts]}
    else:
        return parse_conjunction(prop_str)

def parse_conjunction(prop_str):
    if '&' in prop_str:
        conjuncts = list(map(str.strip, prop_str.split('&')))
        return {'type': 'conjunction', 'arguments': [parse_negation(conjunct) for conjunct in conjuncts]}
    else:
        return parse_negation(prop_str)

def parse_negation(prop_str):
    if prop_str.startswith('~'):
        return {'type': 'negation', 'argument': parse_atomic(prop_str[1:].strip())}
    else:
        return parse_atomic(prop_str)

def parse_atomic(prop_str):
    prop_str = prop_str.strip()
    if prop_str.startswith('(') and prop_str.endswith(')'):
        return parse_proposition(prop_str[1:-1].strip())
    else:
        return {'type': 'atomic', 'symbol': prop_str}