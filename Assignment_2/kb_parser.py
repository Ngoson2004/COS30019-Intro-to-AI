def read_generic_kb(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def parse_generic_kb(lines):
    kb = []
    query = None
    for line in lines:
        line = line.strip()
        if line.startswith('TELL'):
            kb_part = line[4:].strip()
            kb.extend(kb_part.split(';'))
        elif line.startswith('ASK'):
            query = line[3:].strip()
    return kb, query

def convert_expression(expression):
    original_expression = expression.strip()
    expression = expression.replace('<=>', ' and ')
    expression = expression.replace('=>', ' or not ')
    expression = expression.replace('~', ' not ')
    expression = expression.replace('&', ' and ')
    expression = expression.replace('||', ' or ')
    print("Original Expression:", original_expression)
    print("Converted Expression:", expression)
    return expression

def convert_kb_to_truth_table_format(kb):
    converted_kb = []
    for clause in kb:
        converted_clause = convert_expression(clause)
        converted_kb.append(converted_clause)
    return converted_kb

def parse_input_file(file_path):
    lines = read_generic_kb(file_path)
    kb, query = parse_generic_kb(lines)
    converted_kb = convert_kb_to_truth_table_format(kb)
    return converted_kb, query