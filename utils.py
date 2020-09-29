from datetime import datetime

PYTHON_INDENTATION = 4
JAVA_INDENTATION = 2
ELSE_STATEMENT = 'else'
IF_STATEMENT = 'if'
FOR_STATEMENT = 'for'
WHILE_STATEMENT = 'while'
BRANCH_STATEMENTS = [IF_STATEMENT, ELSE_STATEMENT, 'elif', FOR_STATEMENT, WHILE_STATEMENT]
REGULAR = 'regular'
EASY_CODE_JAVA = 'a = 5 ;'
OPEN_SPECIAL_BRACKET = '{' # this is also how branches in java starts
CLOSE_SPECIAL_BRACKET = '}'
OPEN_BRACKET = '('
CLOSE_BRACKET = ')'
SPACE = ' '
PYTHON_END_OF_BRANCH_LINE = ':' # this is how branch statements in python ends (and the branch itself starts
END_OF_LINE = '\n'
EMPTY_STR = ''
JAVA_BRANCH_FILL = END_OF_LINE + EASY_CODE_JAVA + END_OF_LINE + CLOSE_SPECIAL_BRACKET  # fill java branch with easy code
PYTHON_BRANCH_FILL = '        a = 5\n'  # an easy code inside branch. with indentation (twice. 1 for function and 1 for branch)
VOID = 'void'
RETURN = 'return'

def print_time(to_print):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(to_print + " Time =", current_time)
