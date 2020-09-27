import utils

class SlicingClass:

    def __init__(self):
        pass

    # returns the indentation of line - how many times has 4 spaces in the start (the 4 can differ)
    # splitted is the line after splitting with ' '
    def get_indentation(self, splitted, is_java = False):
        indentation = utils.JAVA_INDENTATION if is_java else utils.PYTHON_INDENTATION
        i = 0
        while splitted[i] == utils.EMPTY_STR:
            i += 1
        if (i % indentation) != 0:
            print('weird!!')
            print(splitted)
        return int(i / indentation)

    # each line will save the indentation, kind of it (for, while, if, else)
    def create_comfortable_code(self, code):
        pass

    # add to slices things they need to run (function declaration, return and so)
    def runable_slices(self, slices, whole_function):
        pass

    # slice the comfortable python code to snippets that are "stand alone/".
    # the main idea is that every line can stand alone. unless the line starts a branch.
    # when a line start branch. we will translate the inside of the branch and will translate
    # the branch statement with 'a = 5' inside that is easy for translation
    # trivial way - fix bug of variable creation - if using variable that a slice does not have (starts to become complicated - will hold this)
    def slice_code_trivial_method(self, code):
        pass

    # slice an entire corpus of code - trivial way
    def slice_corpus_trivial(self, corpus):
        new_corpus = []
        for line in corpus:
            sliced = self.slice_code_trivial_method(self.create_comfortable_code(line[1]))
            sliced = self.runable_slices(sliced, line[1])
            new_corpus.append([line[0], line[1], sliced])
        return new_corpus