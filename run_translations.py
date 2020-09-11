# this scripts will run the translation on the test examples so we will be able to test the limitation
# one of the important things is to organize the output so we will be able to go over it
import argparse

SEPARATOR = '|'

def get_parser():
    """
    Generate a parameters parser.
    """
    # parse parameters
    parser = argparse.ArgumentParser(description="Translate sentences")

    # pahts
    parser.add_argument("--java_path", type=str, default="", help="Java path")
    parser.add_argument("--python_path", type=str, default="", help="Python path")

    return parser

# splits a line to function-name and code. By | symbol
def split_line(line):
    index = line.find(SEPARATOR)
    name = line[:index-1] #cuts the space before the |
    code = line[index+2:] # cut the space after the |. Has \n in the end
    return name, code

# read the data from files
def read_file(file_path):
    with open(file_path) as file:
        lines = file.readlines()
    return list( map( split_line, lines))

if __name__ == '__main__':
    # generate parser / parse parameters
    parser = get_parser()
    params = parser.parse_args()

    # read the files
    java_file = read_file(params.java_path)
    python_file = read_file(params.python_path)

    print('a')