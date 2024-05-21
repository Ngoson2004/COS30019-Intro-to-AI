def negate_literal(literal):
    return literal[1:].strip('(') if literal.startswith('~') else f"~{literal}"

def convert_to_horn(clause):
    # Split the clause by implication
    if '<=>' in clause:
        lhs, rhs = clause.split('<=>')
        return [f"~{lhs.strip()} || {rhs.strip()}", f"{lhs.strip()} || ~{rhs.strip()}"]
    elif '=>' in clause:
        lhs, rhs = clause.split('=>')
        lhs_literals = lhs.strip().split('&')
        lhs_negated = [negate_literal(literal.strip()) for literal in lhs_literals]
        return [f"{' || '.join(lhs_negated)} || {rhs.strip()}"]
    elif '||' in clause:
        return clause.split("||")
    else:
        return [clause]

def process_disjunction(clause):
    disjunctions = clause.split('||')
    positive_literals = [lit.strip().strip('(').strip(')') for lit in disjunctions if not lit.strip().startswith('~')]
    negative_literals = [lit.strip().strip('(').strip(')') for lit in disjunctions if lit.strip().startswith('~')]
    # print("pos_lit:", positive_literals)
    # print("neg_lit:", negative_literals)

    if len(positive_literals) > 1:
        raise ValueError("Cannot convert to Horn form: more than one positive literal in disjunction.")
    elif len(positive_literals) == 1:
        head = positive_literals[0]
        body = ' & '.join([negate_literal(lit) for lit in negative_literals])
        return f"({body}) => ({head})"
    else:
        # All literals are negative
        return f"{' & '.join([negate_literal(lit) for lit in negative_literals])} => False"

def to_horn_form(kb):
    horn_clauses = []

    for rule in kb:
        intermediate_clauses = convert_to_horn(rule)
        #print("1", intermediate_clauses)
        for clause in intermediate_clauses:
            if '&' in clause:
                parts = clause.split('&')
                for part in parts:
                    horn_clauses.append(part.strip())
            else:
                horn_clauses.append(clause.strip())
    
    #print("2", horn_clauses)

    final_horn_form = []
    for clause in horn_clauses:
        if '||' in clause:
            final_horn_form.append(process_disjunction(clause.strip()))
        else:
            final_horn_form.append(clause.strip())
        
        #print("3",final_horn_form)

    return final_horn_form