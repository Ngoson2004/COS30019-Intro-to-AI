def parse_input(filename):
    """
    Parse the input file and return the knowledge base and query.
    """
    # Open the file and read its contents
    with open(filename, 'r') as file:
        content = file.read()

    # Split the content into knowledge base and query
    # The knowledge base and query are separated by the 'ASK' keyword
    kb_query = content.split('ASK')

    # Extract the knowledge base and remove the 'TELL' keyword and any leading/trailing whitespace
    kb_str = kb_query[0].strip().replace('TELL', '').strip()

    # Extract the query and remove any leading/trailing whitespace
    query = kb_query[1].strip()

    # Split the knowledge base into individual rules using the semicolon (';') as the separator
    kb = kb_str.split(';')

    # Remove any empty rules and strip leading/trailing whitespace from each rule
    kb = [rule.strip() for rule in kb if rule.strip()]
    
    # Print the knowledge base and query for debugging purposes
    print("Knowledge Base:")
    for rule in kb:
        print(rule)
    print("\nQuery:")
    print(query)

    # Return the knowledge base as a list of rules and the query
    return kb, query