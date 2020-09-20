from datetime import datetime
from run_translations import translate_lines

INDENTATION = 4
BRANCH_STATEMENTS = ['if', 'else', 'elif', 'for', 'while']
REGULAR = 'regular'
EASY_CODE = '        a = 5\n' # an easy code inside branch. with indentation (twice. 1 for function and 1 for branch)
OPEN_SPECIAL_BRACKET = '{'
CLOSE_SPECIAL_BRACKET = '}'
OPEN_BRACKET = '('
CLOSE_BRACKET = ')'

def print_time(to_print):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(to_print + " Time =", current_time)

# returns the indentation of line - how many times has 4 spaces in the start (the 4 can differ)
def get_indentation(splitted):
    i = 0
    while splitted[i] == '':
        i += 1
    if (i % INDENTATION) != 0:
        print('weird!!')
        print(splitted)
    return int(i / INDENTATION)

# each line will save the indentation, kind of it (for, while, if, else)
def create_comfortable_code(code):
    comfortable_code = []
    for line in code:
        splitted = line.split(' ')
        indentation = get_indentation(splitted)
        first_word = splitted[indentation * INDENTATION]
        if first_word not in BRANCH_STATEMENTS:
            first_word = REGULAR
        comfortable_code.append([first_word, indentation, ' '.join(splitted[indentation * INDENTATION:])])
    return comfortable_code

# slice the comfortable python code to snippets that are "stand alone/".
# the main idea is that every line can stand alone. unless the line starts a branch.
# when a line start branch. we will translate the inside of the branch and will translate
# the branch statement with 'a = 5' inside that is easy for translation
def slice_code(comfortable_code):
    slices = []
    i = 0
    while i < len(comfortable_code):
        line = comfortable_code[i]
        if line[0] == REGULAR: # if the line is regular - we appent it
            slices.append([line[1],line[2]])
            i += 1
        else: # else, branch is started. we find the lines inside the branch and slice them separately
            slices.append([line[1],line[2] + EASY_CODE])
            i += 1
            indent_line = comfortable_code[i]
            indent_code = []
            while indent_line[1] > line[1]: # line with indentation are inside branch (python)
                indent_code.append(indent_line)
                i += 1
                if i < len(comfortable_code):
                    indent_line = comfortable_code[i]
                else:
                    break
            slices.extend(slice_code(indent_code))

    return slices

# add to slices things they need to run (function declaration, return and so)
def runable_slices(slices, whole_function):
    function_declaration = slices[0][1]
    slices[0] = [0, whole_function] # for function declaration - we need all the function (for this time)
    for i in range(1,len(slices)):
        slices[i][1] = function_declaration + '    ' + slices[i][1]
    return slices

# finds the index for the end of the line that we are interested in
# it is at the end of the condition. because we not have the inside of the branch
def find_end_of_declaration(interesting_code):
    brackets = 1
    i = 2
    while brackets != 0 and i < len(interesting_code):
        word = interesting_code[i]
        if word == OPEN_BRACKET:
            brackets += 1
        elif word == CLOSE_BRACKET:
            brackets -= 1
        i += 1
    return i

# strips java line - and order it to be with no indentations
def strip_line(line):
    splitted_line = line.split('\n') # splitted the code to lines.
    # first line in function declaration - we do not need it
    # second line its our code
    interesting_code = splitted_line[1].strip().split(' ') # take the line, no indentation, split with ' '
    # if starts branch - we take the branch declaration and add '{', we remove the a=5 part.
    if interesting_code[0] in BRANCH_STATEMENTS:
        # cut the line and add the opening of branch in java
        to_return = ' '.join(interesting_code).replace('a = 5 ;','')
        if interesting_code[-1] != OPEN_SPECIAL_BRACKET:
            to_return += OPEN_SPECIAL_BRACKET
        return to_return
    # if not branch - we take the line
    return ' '.join(interesting_code)


# integrate the translated code into our output
# we will use trivial way - strip each line and put it in its place with the correct indentation
def integrate_code(translated):
    integrated = [] # strip the first line
    stripped_lines = [[0, translated[0][2].split('\n')[0]]]
    for i in range(1, len(translated)): # strip all the lines to prepare them for the integration
                                        # we need the indentation because we will use it to locate branches code
        stripped_lines.append([translated[i][0], strip_line(translated[i][2])])
    integrated = stripped_lines
    # TODO - create integrated. only add indentation and '}' to close each branch (including the function itself)
    return integrated


if __name__ == '__main__':
    print_time('start')
    with open('/mnt/c/TransCoder/outputs/python/BINARY_SEARCH.py') as file:
        lines = file.readlines()
    code = lines[6:17]
    comfortable_code = create_comfortable_code(code)
    slices = slice_code(comfortable_code)
    slices = runable_slices(slices, ''.join(code))
    translated = translate_lines(False, slices)
    integrated = integrate_code(translated)
    a = 5
