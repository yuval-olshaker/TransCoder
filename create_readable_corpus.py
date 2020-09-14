from os import listdir
from os.path import isfile, join

# empty line is a line with \n and thats it
def not_empty(line):
    return line != '\n'

# returns the origin code of all the test files
def get_origin_codes(lang, comment_str, cut_size):
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
    java_origin_codes = get_origin_codes('java', '//', 5)
    python_origin_codes = get_origin_codes('python', '#', 3)
    a = 5
