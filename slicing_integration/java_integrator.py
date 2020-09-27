import utils
from slicing_integration.integration_class import IntegrationClass


class JavaIntegrator(IntegrationClass):
    def __init__(self):
        IntegrationClass.__init__(self)


    def integrate_trivial(self, stripped_lines):
        # lines in here have everything. just need to join
        finish_lines = [stripped_lines[0][1]]  # first line has no indentation and trivial
        opened_indentations = []
        for line in stripped_lines[1:]:  # we are running over the lines, without the first one
            ind = line[0]
            line_str = line[1]
            if opened_indentations:  # we need to close only if opened
                finish_lines, opened_indentations = self.close_branches(opened_indentations, ind, finish_lines)
            if line_str[-1] == utils.OPEN_SPECIAL_BRACKET:  # if the lines starts branch, we need to close it
                opened_indentations.append(ind)
            finish_lines.append((utils.SPACE * ind * utils.INDENTATION) + line_str)  # add the line itself

        # need to close all the branches that are open
        if opened_indentations:
            finish_lines, opened_indentations = self.close_branches(opened_indentations, 0, finish_lines)

        finish_lines.append(utils.CLOSE_SPECIAL_BRACKET)  # close the function itself
        return '\n'.join(finish_lines)  # we join it all for the integrated code


    # close the branches that we need at this line - add '}'
    def close_branches(self, opened_indentations, ind, finish_lines):
        need_to_close = []
        for num in opened_indentations:
            if num >= ind:
                need_to_close.append(num)
        if need_to_close:  # if we need to close
            need_to_close.sort()
            need_to_close.reverse()  # we sort and reverse, because we need to close the "bigger" indentations first
            for num in need_to_close:
                finish_lines.append(
                    (utils.SPACE * utils.INDENTATION * num) + utils.CLOSE_SPECIAL_BRACKET)  # close with indentation
                opened_indentations.remove(num)  # we close it
        return finish_lines, opened_indentations


    # strips java line - and order it to be with no indentations
    def strip_line(self, line):
        splitted_line = line.split(utils.END_OF_LINE)  # splitted the code to lines.
        if utils.EASY_CODE_JAVA in line:
            # we take the function from end of declaration to a = 5
            end_of_declaration = self.find_end_of_declaration(splitted_line)
            if end_of_declaration == -1:
                to_return = splitted_line[1].replace(utils.EASY_CODE_JAVA, utils.EMPTY_STR).strip()
            else:
                to_return = ''.join(splitted_line[1:end_of_declaration]).strip()

            if to_return[-1] != utils.OPEN_SPECIAL_BRACKET:
                to_return += utils.OPEN_SPECIAL_BRACKET
            return to_return
        else:
            return splitted_line[1].strip()  # returns the interesting part (after declaration) stripped


    # finds the index for the end of the line that we are interested in
    # it is at the end of the condition. because we not have the inside of the branch
    # we have the a = 5 to help us
    def find_end_of_declaration(self, interesting_code):
        i = 2
        while i < len(interesting_code):
            if utils.EASY_CODE_JAVA in interesting_code[i]:
                return i
            i += 1
        return -1