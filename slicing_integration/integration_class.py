import utils

class IntegrationClass:

    def __init__(self):
        pass


    # strips line - and order it to be with no indentations
    def strip_line(self, line):
        pass


    # create integrated. only add indentation and '}' to close each branch (including the function itself)
    def integrate_trivial(self, stripped_lines):
        pass


    # integrate the translated code into our output
    # we will use trivial way - strip each line and put it in its place with the correct indentation
    def integrate_code_trivial(self, translated):
        stripped_lines = [[0, translated[0][1].split(utils.END_OF_LINE)[0]]]  # strip the first line
        for i in range(1, len(translated)):  # strip all the lines to prepare them for the integration
            # we need the indentation because we will use it to locate branches code
            stripped_lines.append([translated[i][0], self.strip_line(translated[i][1])])
        return self.integrate_trivial(stripped_lines)

    # integrate an entire corpus of translated code
    def integrate_corpus_trivial(self, sliced_corpus):
        return list(map(lambda line: (line[0], line[1], self.integrate_code_trivial(line[2])), sliced_corpus))
