from slicing_integration.slicing_class import SlicingClass
import utils


# return the line number of the ending of the statement (we know it by closing the bracket - java syntax)
def find_end_statement_line(code_splitted, i):
    counter = 0
    while i < len(code_splitted):
        if utils.CLOSE_BRACKET in code_splitted[i] or utils.OPEN_BRACKET in code_splitted[i]:
            for word in code_splitted[i].split():
                if word == utils.OPEN_BRACKET:
                    counter += 1
                elif word == utils.CLOSE_BRACKET:
                    counter -= 1
                    if counter == 0:
                        return i
        i += 1



# deletes double spaces
def no_double_spaces(combined):
    while utils.SPACE + utils.SPACE in combined:
        combined = combined.replace(utils.SPACE + utils.SPACE, utils.SPACE)
    return combined


# finds where the declaration ends (close the bracket)
def find_end_statement_index(combined):
    i = combined.index(utils.OPEN_BRACKET)
    counter = 0
    while i < len(combined):
        if combined[i] == utils.OPEN_BRACKET:
            counter += 1
        elif combined[i] == utils.CLOSE_BRACKET:
            counter -= 1
            if counter == 0:
                return i
        i += 1


# handles the annoying branches. the ones that has no { at the end of declaration line.
# written badly. ordering java is a bit annoying. may need to work on making this better
def handle_annoying_branch(comfortable_code, first_word, splitted, code_splitted, i):
    second_word = splitted[1]
    # else is handled alone, else if is like if statement
    if first_word == utils.ELSE_STATEMENT and splitted[1] != utils.IF_STATEMENT:
        splitted_no_else = splitted[1:] # the line without the else
        comfortable_code.append(# the else itself is a line
            [first_word, utils.ELSE_STATEMENT + utils.SPACE + utils.OPEN_SPECIAL_BRACKET])
        # add the inside - if branch we need to handle it properly - special line
        if splitted[1] in utils.BRANCH_STATEMENTS:
            # we change the line in the code splitted line to use it. it is ok because we only go forward
            code_splitted[i] = utils.SPACE.join(splitted_no_else)
            comfortable_code, i = handle_annoying_branch(comfortable_code,
                                        splitted[1], splitted_no_else, code_splitted, i)
        else: # regular line, then first word is regular and we append the line (after the else)
            comfortable_code.append([utils.REGULAR, utils.SPACE.join(splitted_no_else)])
        # because this situation only happens with 1 line and no '}' we add it as well
        comfortable_code.append([utils.REGULAR, utils.CLOSE_SPECIAL_BRACKET])
    else:
        end_statement_line = find_end_statement_line(code_splitted, i)  # finds the line that the statement ends
        combined = utils.SPACE.join(code_splitted[i:end_statement_line + 1])  # one line for statement
        combined = no_double_spaces(combined).split()
        i = end_statement_line  # advance i (only if it changed)
        # checks if there is code in that line
        statement_ends = find_end_statement_index(combined)
        if combined[-1] == utils.OPEN_SPECIAL_BRACKET:
            comfortable_code.append([first_word, utils.SPACE.join(combined)])
        elif statement_ends == len(combined) - 1:  # add the line - there is no code inside the branch (here)
            comfortable_code.append([first_word,
                                     utils.SPACE.join(combined) + utils.SPACE + utils.OPEN_SPECIAL_BRACKET])
        else:  # adds the declaration and the inside of branch in 2 separate lines
            comfortable_code.append(
                [first_word,
                 utils.SPACE.join(combined[:statement_ends + 1]) + utils.SPACE + utils.OPEN_SPECIAL_BRACKET])
            new_first_word = combined[statement_ends + 1]
            if new_first_word in utils.BRANCH_STATEMENTS:
                only_in_branch = combined[statement_ends + 1:]  # needs to continue with the inside
                code_splitted[i] = utils.SPACE.join(only_in_branch) # like inside else - we destroy the origin line
                comfortable_code, i = handle_annoying_branch(comfortable_code,
                                                             new_first_word, only_in_branch, code_splitted, i)
            else:  # the first word is regular (no branch)
                comfortable_code.append([utils.REGULAR, utils.SPACE.join(combined[statement_ends + 1:])])
            # because this situation only happens with 1 line and no '}' we add it as well
            comfortable_code.append([utils.REGULAR, utils.CLOSE_SPECIAL_BRACKET])
    return comfortable_code, i


# returns the line number of the ending of the branch
def find_branch_end(code, i):
    counter = 0
    while i < len(code):
        if code[i][1][-1] == utils.OPEN_SPECIAL_BRACKET:
            counter += 1
        elif code[i][1][-1] == utils.CLOSE_SPECIAL_BRACKET:
            counter -= 1
            if counter == 0:
                return i
        i += 1


# figures out the non branch parts that looks like branch
def handle_annoying_non_branch(comfortable_code, first_word, splitted, code_splitted, i):
    start_i = i
    while i < len(code_splitted):
        if utils.CLOSE_SPECIAL_BRACKET in code_splitted[i]:
            break
        i += 1
    comfortable_code.append([first_word, utils.SPACE.join(code_splitted[start_i:i+1])])
    return comfortable_code, i


class JavaSlicer(SlicingClass):
    def __init__(self):
        SlicingClass.__init__(self)


    def create_comfortable_code(self, code):
        code_splitted = code.split(utils.END_OF_LINE)[:-1]
        comfortable_code = [['start', code_splitted[0].strip()]]
        i = 1
        while i < len(code_splitted): # run over all the lines of the code
            line = code_splitted[i].strip()
            splitted = line.split(utils.SPACE)
            first_word = splitted[0] # extract first word (has more meaning)
            is_branch = first_word in utils.BRANCH_STATEMENTS
            if is_branch and splitted[-1] != utils.OPEN_SPECIAL_BRACKET: # annoying situation with branches
                comfortable_code, i = handle_annoying_branch(comfortable_code, first_word,splitted, code_splitted, i)
            elif not is_branch and splitted[-1] == utils.OPEN_SPECIAL_BRACKET: # not branch that looks like one
                first_word = utils.REGULAR # not branch
                comfortable_code, i = handle_annoying_non_branch(comfortable_code, first_word, splitted, code_splitted, i)
            else:
                if not is_branch:
                    first_word = utils.REGULAR
                comfortable_code.append([first_word, utils.SPACE.join(splitted)])
            i += 1

        return comfortable_code


    def runnable_slices(self, slices, whole_function):
        function_declaration = slices[0][1].split(utils.OPEN_SPECIAL_BRACKET)[0]
        slices[0] = [0, whole_function]  # for function declaration - we need all the function (for this time) - in java?
        for i in range(1, len(slices)): # we add the function declaration and brackets of it
            slices[i][1] = (function_declaration + utils.END_OF_LINE +
                            slices[i][1] + utils.END_OF_LINE + utils.CLOSE_SPECIAL_BRACKET)
        return slices


    def slice_code_trivial_method(self, code, indentation = 0):
        slices = []
        i = 0
        while i < len(code):
            line = code[i]
            if line[0] == utils.REGULAR:  # if the line is regular - we append it
                slices.append([indentation, line[1]])
                i += 1
            else:  # else, branch is started. we find the lines inside the branch and slice them separately
                branch_end = find_branch_end(code, i)
                slices.append([indentation, line[1] + utils.JAVA_BRANCH_FILL]) # add the branch with dummy code
                # add the inside of the slice. we add the indentation to integrate easily
                slices.extend(self.slice_code_trivial_method(code[i+1:branch_end], indentation=indentation+1))
                i = branch_end + 1
        return slices