import sys
from Truth_Table import Truth_Table
from forward_chaining import Forward
from backward_chaining import Backward
from input_parser import parse_input

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
            # If the method is 'FC' (Forward Chaining), initialise the engine to Forward class
            engine = Forward(kb, query)
        elif method == 'TT':
            # If the method is 'TT' (Truth Table), initialise the engine to Truth_Table class
            engine = Truth_Table(kb, query)
        elif method == 'BC':
            # If the method is 'BC' (Backward_chaining), initialise the engine to backward_chaining class
            engine = Backward(kb, query)
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