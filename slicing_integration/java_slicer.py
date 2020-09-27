from slicing_integration.slicing_class import SlicingClass
import utils


# return the line number of the ending of the statement (we know it by closing the bracket - java syntax)
def find_end_statement_line(code_splitted, i):
    while i < len(code_splitted):
        if utils.CLOSE_BRACKET in code_splitted[i]:
            return i
        i += 1


# deletes double spaces
def no_double_spaces(combined):
    while utils.SPACE + utils.SPACE in combined:
        combined = combined.replace(utils.SPACE + utils.SPACE, utils.SPACE)
    return combined


class JavaSlicer(SlicingClass):
    def __init__(self):
        SlicingClass.__init__(self)

    def create_comfortable_code(self, code):
        code_splitted = code.split(utils.END_OF_LINE)[:-1]
        comfortable_code = []
        i = 0
        while i < len(code_splitted):
            line = code_splitted[i]
            splitted = line.split(utils.SPACE)
            indentation = self.get_indentation(splitted, True)
            first_word = splitted[indentation * utils.JAVA_INDENTATION]
            is_branch = first_word in utils.BRANCH_STATEMENTS
            if is_branch and splitted[-1] != utils.OPEN_SPECIAL_BRACKET:
                end_statement_line = find_end_statement_line(code_splitted, i) # finds the line that the statement ends
                combined = utils.SPACE.join(code_splitted[i:end_statement_line+1]) # one line for statement
                combined = no_double_spaces(combined)
                i = end_statement_line # advance i (only if it changed
                # checks if there is code in that line
                statement_ends = combined.index(utils.CLOSE_BRACKET)
                if statement_ends == len(combined) - 1: # add the line - there is no code inside the branch (here)
                    comfortable_code.append([first_word, indentation, combined + utils.OPEN_SPECIAL_BRACKET])
                else: # adds the declaration and the inside of branch in 2 separate lines
                    comfortable_code.append([first_word, indentation, combined[:statement_ends+1] + utils.SPACE + utils.OPEN_SPECIAL_BRACKET])
                    # the first word is regular because branch in branch requires '{' - (i think)
                    comfortable_code.append([utils.REGULAR, indentation, combined[statement_ends + 1:]])
                    # because this situation only happens with 1 line and no '}' we add it as well
                    comfortable_code.append([utils.REGULAR, indentation, utils.CLOSE_SPECIAL_BRACKET])
            else:
                if not is_branch:
                    first_word = utils.REGULAR
                comfortable_code.append(
                    [first_word, indentation, utils.SPACE.join(splitted[indentation * utils.JAVA_INDENTATION:])])
            i += 1

        return comfortable_code

    def runable_slices(self, slices, whole_function):
        function_declaration = slices[0][1]
        slices[0] = [0, whole_function]  # for function declaration - we need all the function (for this time)
        for i in range(1, len(slices)):
            slices[i][1] = (function_declaration + '    ' + slices[i][1]).replace(utils.END_OF_BRANCH_LINE,
                                                                                  utils.END_OF_BRANCH_LINE + utils.END_OF_LINE)
        return slices

    def slice_code_trivial_method(self, code):
        slices = []
        i = 0
        while i < len(code):
            line = code[i]
            if line[0] == utils.REGULAR:  # if the line is regular - we append it
                slices.append([line[1], line[2]])
                i += 1
            else:  # else, branch is started. we find the lines inside the branch and slice them separately
                slices.append([line[1], line[2] + utils.EASY_CODE])
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
                slices.extend(self.slice_code_trivial_method(indent_code))

        return slices