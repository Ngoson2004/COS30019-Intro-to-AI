import sys
from Truth_Table import Truth_Table
from forward_chaining import Forward
from backward_chaining import Backward
from input_parser import parse_input

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
        # Read the input file
        with open(filename, 'r') as file:
            input_string = file.read()

        # Parse the input string to get the knowledge base and query
        kb, query = parse_input(input_string)

        # Check the specified inference method
        if method == 'FC':
            # If the method is 'FC' (Forward Chaining), initialize the engine to Forward class
            engine = Forward(kb, query)
        elif method == 'TT':
            # If the method is 'TT' (Truth Table), initialize the engine to Truth_Table class
            engine = Truth_Table(input_string)
        elif method == 'BC':
            engine = Backward(kb, query)
        else:
            # If the method is not supported, print an error message
            print("Method not supported.")
            return

        result = engine.inference()
        print(result)

    except FileNotFoundError:
        # If the specified file is not found, print an error message
        print("File not found.")
    except ValueError:
        # If apply FC or BC to non-Horn KB
        print("Only applicable for Horn-based KB")
    # except:
    #     # If file is written in invalid format
    #     print("Please review file's format")

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the main function to start the inference engine
    main()