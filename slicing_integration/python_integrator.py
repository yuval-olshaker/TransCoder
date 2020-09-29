import utils
from slicing_integration.integration_class import IntegrationClass


class PythonIntegrator(IntegrationClass):
    def __init__(self):
        IntegrationClass.__init__(self)


    def integrate_trivial(self, stripped_lines):
        # lines in here have everything. just need to join
        finish_lines = [stripped_lines[0][1]]  # first line has no indentation and trivial
        # run over the lines and add them with proper indentations
        for line in stripped_lines[1:]:  # without the first one
            finish_lines.append((utils.SPACE * line[0] * utils.PYTHON_INDENTATION) + line[1])  # add the line

        return '\n'.join(finish_lines)  # we join it all for the integrated code


    # strips java line - and order it to be with no indentations
    def strip_line(self, line):
        splitted_line = line.split(utils.END_OF_LINE)  # splitted the code to lines.
        if utils.GLOBAL in line:
            return splitted_line[2].strip()  # returns the interesting part (after global) stripped
        else:
            return splitted_line[1].strip()  # returns the interesting part (after function declaration) stripped
