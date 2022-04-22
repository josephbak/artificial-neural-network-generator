import nltk


def main():
    text = input("Plese enter your goal: ")
    # TODO: Write some tests for the user text.
    
    input, output = input_output_extraction(text)

    nn_model = nn_generator(input, output)

    return nn_model

def data_cleaner(data):
    """
    This function cleans and prepares the data automatically.
    """
    return


def input_output_extraction(text):
    # TODO: Process the user text to genenrate proper inputs and outputs.

    input = ""
    output = ""

    return input, output


def nn_generator(input, output):
    """
    This function genenrates the artifial neural network.
    """
    # TODO: Do search in possible neural network architetures?

    return


if __name__=="__main__":
    main()