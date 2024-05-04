import sys
from Truth_Table import Truth_Table
from forward_chaining import Forward

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

def forward_chaining(kb, query):
    """
    Perform Forward Chaining inference.
    """
    inferred = set()
    agenda = set()

    # Add facts to the agenda
    for rule in kb:
        if "=>" not in rule:
            agenda.add(rule)
            inferred.add(rule)

    while agenda:
        fact = agenda.pop()

        # Generate new facts based on the rules
        for rule in kb:
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
        for rule in kb:
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

    if query in inferred:
        return "YES: " + ", ".join(sorted(inferred))
    else:
        return "NO"

def main():
    """
    Main function to run the inference engine.
    """
    # Check if the correct number of command-line arguments are provided
    # The program expects two arguments: the filename and the inference method
    if len(sys.argv) != 3:
        print("Usage: python iengine.py <filename> <method>")
        return

    # Get the filename from the command-line arguments
    filename = sys.argv[1]

    # Get the inference method from the command-line arguments
    method = sys.argv[2]

    try:
        # Parse the input file to get the knowledge base and query
        kb, query = parse_input(filename)

        # Check the specified inference method
        if method == 'FC':
            # If the method is 'FC' (Forward Chaining), call the forward_chaining function
            # result = forward_chaining(kb, query)
            # # Print the result of the Forward Chaining inference
            # print(result)
            engine = Forward(kb, query)
        elif method == 'TT':
            engine = Truth_Table(kb, query)
        else:
            # If the method is not supported, print an error message
            print("Method not supported.")

        result = engine.inference()
        print(result)

    except FileNotFoundError:
        # If the specified file is not found, print an error message
        print("File not found.")

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the main function to start the inference engine
    main()