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
