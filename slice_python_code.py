from datetime import datetime

INDENTATION = 4
BRANCH_STATEMENTS = ['if', 'else', 'elif', 'for', 'while']

def print_time(to_print):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(to_print + " Time =", current_time)

# returns the indentation of line - how many times has 4 spaces in the start (the 4 can differ)
def get_indentation(splitted):
    i = 0
    while splitted[i] == '':
        i += 1
    if (i % INDENTATION) != 0:
        print('wierd!!')
        print(splitted)
    return int(i / INDENTATION)

# each line will save the indentation, kind of it (for, while, if, else)
def create_comfortable_code(code):
    comfortable_code = []
    for line in code:
        splitted = line.split(' ')
        indentation = get_indentation(splitted)
        first_word = splitted[indentation * INDENTATION]
        if first_word not in BRANCH_STATEMENTS:
            first_word = 'regular'
        comfortable_code.append([indentation, first_word, splitted[indentation * INDENTATION:]])
    return comfortable_code

if __name__ == '__main__':
    print_time('start')
