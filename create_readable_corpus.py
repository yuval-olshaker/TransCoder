from os import listdir
from os.path import isfile, join
import preprocessing.src.code_tokenizer as code_tokenizer

SEPARATOR = '|'

# empty line is a line with \n and thats it
def not_empty(line):
    return line != '\n'

# splits a line to function-name and code. By | symbol
def split_line(line):
    index = line.find(SEPARATOR)
    name = line[:index - 1]  # cuts the space before the |
    code = line[index + 2:-1]  # cut the space after the |. cut \n in the end
    return name, code

# read the data from files
def read_file(file_path):
    with open(file_path) as file:
        lines = file.readlines()
    return list(map(split_line, lines))

# parse the lines and detokenize them so it will be readable for humans - and better for the run
def make_java_readable(java_file):
    return list(map(lambda line: (line[0], code_tokenizer.detokenize_java(line[1])), java_file))


def make_python_readable(python_file):
    return list(map(lambda line: (line[0], code_tokenizer.detokenize_python(line[1])), python_file))


# return the origin code in readable way for each language by path
def get_origin_codes_from_tok_files(java_path, python_path):
    # read the files
    java_file = read_file(java_path)
    python_file = read_file(python_path)

    # make the test data readable for humans
    java_file_readable = make_java_readable(java_file)
    python_file_readable = make_python_readable(python_file)

    return java_file_readable, python_file_readable

# returns the origin code of all the test files
def get_origin_codes_from_test_files(lang, comment_str, cut_size):
    dir_path = '/mnt/c/TransCoder/outputs/' + lang + '/'
    files = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
    origin_codes = []
    for file_name in files:
        with open(dir_path + file_name) as file:
            code = file.readlines()
            origin_code = ''
            # find where the origin code starts - the function declaration
            i = 0
            line = code[i]
            while 'f_gold' not in line:
                i += 1
                line = code[i]
            # finds where the function ends - add the code lines into origin code - this is what we want
            while line != comment_str + 'TOFILL\n':
                i += 1
                if not_empty(line):
                    origin_code += line
                line = code[i]
        origin_codes.append([file_name[:-cut_size], origin_code])
    return origin_codes


if __name__ == '__main__':
    java_origin_codes = get_origin_codes_from_test_files('java', '//', 5)
    python_origin_codes = get_origin_codes_from_test_files('python', '#', 3)
    a = 5
