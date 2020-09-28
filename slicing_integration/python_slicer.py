from slicing_integration.slicing_class import SlicingClass
import utils

class PythonSlicer(SlicingClass):
    def __init__(self):
        SlicingClass.__init__(self)


    def create_comfortable_code(self, code):
        code_splitted = code.split(utils.END_OF_LINE)[:-1]
        comfortable_code = []
        for line in code_splitted: # run over all the lines of the code
            splitted = line.split(utils.SPACE)
            indentation = self.get_indentation(splitted)
            first_word = splitted[indentation * utils.PYTHON_INDENTATION] # extract first word (has more meaning)
            is_branch = first_word in utils.BRANCH_STATEMENTS
            if is_branch and splitted[-1] != utils.END_OF_BRANCH_LINE: # the branch starts in the middle of the line
                branch_start = splitted.index(utils.END_OF_BRANCH_LINE) # finds where the branch starts
                comfortable_code.append( # append the declaration
                    [first_word, indentation,
                     utils.SPACE.join(splitted[indentation * utils.PYTHON_INDENTATION:branch_start + 1])])
                comfortable_code.append( # append the code inside the branch
                    [utils.REGULAR, indentation + 1, utils.SPACE.join(splitted[branch_start + 1:])])
            else: # regular line, adds normally
                if not is_branch:
                    first_word = utils.REGULAR
                comfortable_code.append(
                    [first_word, indentation, utils.SPACE.join(splitted[indentation * utils.PYTHON_INDENTATION:])])

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