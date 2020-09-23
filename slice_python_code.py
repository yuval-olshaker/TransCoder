from datetime import datetime

INDENTATION = 4
BRANCH_STATEMENTS = ['if', 'else', 'elif', 'for', 'while']
REGULAR = 'regular'
EASY_CODE = '        a = 5\n'  # an easy code inside branch. with indentation (twice. 1 for function and 1 for branch)
EASY_CODE_JAVA = 'a = 5 ;'
OPEN_SPECIAL_BRACKET = '{'
CLOSE_SPECIAL_BRACKET = '}'
OPEN_BRACKET = '('
CLOSE_BRACKET = ')'
SPACE = ' '
END_OF_BRANCH_LINE = ':' # this is how branch statements in python ends
END_OF_LINE = '\n'
EMPTY_STR = ''

def print_time(to_print):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(to_print + " Time =", current_time)


# returns the indentation of line - how many times has 4 spaces in the start (the 4 can differ)
def get_indentation(splitted):
    i = 0
    while splitted[i] == EMPTY_STR:
        i += 1
    if (i % INDENTATION) != 0:
        print('weird!!')
        print(splitted)
    return int(i / INDENTATION)


# each line will save the indentation, kind of it (for, while, if, else)
def create_comfortable_code(code):
    code_splitted = code.split(END_OF_LINE)[:-1]
    comfortable_code = []
    for line in code_splitted:
        splitted = line.split(SPACE)
        indentation = get_indentation(splitted)
        first_word = splitted[indentation * INDENTATION]
        is_branch = first_word in BRANCH_STATEMENTS
        if is_branch and splitted[-1] != END_OF_BRANCH_LINE:
            branch_start = splitted.index(END_OF_BRANCH_LINE)
            comfortable_code.append([first_word, indentation, SPACE.join(splitted[indentation * INDENTATION:branch_start+1])])
            comfortable_code.append(
                [REGULAR, indentation + 1, SPACE.join(splitted[branch_start + 1:])])
        else:
            if not is_branch:
                first_word = REGULAR
            comfortable_code.append([first_word, indentation, SPACE.join(splitted[indentation * INDENTATION:])])

    return comfortable_code


# slice the comfortable python code to snippets that are "stand alone/".
# the main idea is that every line can stand alone. unless the line starts a branch.
# when a line start branch. we will translate the inside of the branch and will translate
# the branch statement with 'a = 5' inside that is easy for translation
# TODO - fix bug of variable creation - if using variable that a slice does not have (starts to become complicated - will hold this)
def slice_code(code):
    slices = []
    i = 0
    while i < len(code):
        line = code[i]
        if line[0] == REGULAR:  # if the line is regular - we appent it
            slices.append([line[1], line[2]])
            i += 1
        else:  # else, branch is started. we find the lines inside the branch and slice them separately
            slices.append([line[1], line[2] + EASY_CODE])
            i += 1
            indent_line = code[i]
            indent_code = []
            while indent_line[1] > line[1]:  # line with indentation are inside branch (python)
                indent_code.append(indent_line)
                i += 1
                if i < len(code):
                    indent_line = code[i]
                else:
                    break
            slices.extend(slice_code(indent_code))

    return slices


# add to slices things they need to run (function declaration, return and so)
def runable_slices(slices, whole_function):
    function_declaration = slices[0][1]
    slices[0] = [0, whole_function]  # for function declaration - we need all the function (for this time)
    for i in range(1, len(slices)):
        slices[i][1] = (function_declaration + '    ' + slices[i][1]).replace(END_OF_BRANCH_LINE, END_OF_BRANCH_LINE + END_OF_LINE)
    return slices


# finds the index for the end of the line that we are interested in
# it is at the end of the condition. because we not have the inside of the branch
# we have the a = 5 to help us
def find_end_of_declaration(interesting_code):
    i = 2
    while i < len(interesting_code):
        if EASY_CODE_JAVA in interesting_code[i]:
            return i
        i += 1
    return -1


# strips java line - and order it to be with no indentations
def strip_line(line):
    splitted_line = line.split(END_OF_LINE) # splitted the code to lines.
    if EASY_CODE_JAVA in line:
        # we take the function from end of declaration to a = 5
        end_of_declaration = find_end_of_declaration(splitted_line)
        if end_of_declaration == -1:
            to_return = splitted_line[1].replace(EASY_CODE_JAVA, EMPTY_STR).strip()
        else:
            to_return = ''.join(splitted_line[1:end_of_declaration]).strip()

        if to_return[-1] != OPEN_SPECIAL_BRACKET:
            to_return += OPEN_SPECIAL_BRACKET
        return to_return
    else:
        return splitted_line[1].strip() # returns the interesting part (after declaration) stripped

# close the branches that we need at this line - add '}'
def close_branches(opened_indentations, ind, finish_lines):
    need_to_close = []
    for num in opened_indentations:
        if num >= ind:
            need_to_close.append(num)
    if need_to_close:  # if we need to close
        need_to_close.sort()
        need_to_close.reverse()  # we sort and reverse, because we need to close the "bigger" indentations first
        for num in need_to_close:
            finish_lines.append((SPACE * INDENTATION * num) + CLOSE_SPECIAL_BRACKET)  # close with indentation
            opened_indentations.remove(num) # we close it
    return finish_lines, opened_indentations

# create integrated. only add indentation and '}' to close each branch (including the function itself)
def integrate(stripped_lines):
    # lines in here have everyrhing. just need to join
    finish_lines = [stripped_lines[0][1]] # first line has no indentation and trivial
    opened_indentations = []
    for line in stripped_lines[1:]:  # we are running over the lines, without the first one
        ind = line[0]
        line_str = line[1]
        if opened_indentations:  # we need to close only if opened
            finish_lines, opened_indentations = close_branches(opened_indentations, ind, finish_lines)
        if line_str[-1] == OPEN_SPECIAL_BRACKET:  # if the lines starts branch, we need to close it
            opened_indentations.append(ind)
        finish_lines.append( (SPACE * ind * INDENTATION) + line_str) # add the line itself

    # need to close all the branches that are open
    if opened_indentations:
        finish_lines, opened_indentations = close_branches(opened_indentations, 0, finish_lines)

    finish_lines.append(CLOSE_SPECIAL_BRACKET) # close the function itself
    return '\n'.join(finish_lines) # we join it all for the integrated code

# integrate the translated code into our output
# we will use trivial way - strip each line and put it in its place with the correct indentation
def integrate_code(translated):
    stripped_lines = [[0, translated[0][1].split(END_OF_LINE)[0]]]  # strip the first line
    for i in range(1, len(translated)):  # strip all the lines to prepare them for the integration
        # we need the indentation because we will use it to locate branches code
        stripped_lines.append([translated[i][0], strip_line(translated[i][1])])
    return integrate(stripped_lines)


# slice an entire corpus of code
def slice_corpus(python_corpus):
    new_corpus = []
    for line in python_corpus:
        sliced = slice_code(create_comfortable_code(line[1]))
        sliced = runable_slices(sliced, line[1])
        new_corpus.append([line[0], line[1], sliced])
    return new_corpus

# integrate an entire corpus of translated code
def integrate_corpus(python_sliced_corpus):
    return list(map(lambda line: (line[0], line[1], integrate_code(line[2])), python_sliced_corpus))


if __name__ == '__main__':
    print_time('start')
    with open('/mnt/c/TransCoder/outputs/python/BINARY_SEARCH.py') as file:
        lines = file.readlines()
    code = END_OF_LINE.join(lines[6:17])
    slices = slice_code(create_comfortable_code(code))
    slices = runable_slices(slices, EMPTY_STR.join(code))
    # translated = translate_lines(False, slices)
    # integrated = integrate_code(translated)
    a = 5
