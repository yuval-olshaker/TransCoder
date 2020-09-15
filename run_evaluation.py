import os
import signal
from datetime import datetime

END_OF_FUNCTION = '|||'

# prints current time
def print_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

# read the translations file
def read_translated(trans_path):
    with open(trans_path) as file:
        lines = file.readlines()
    return list(filter(''.__ne__, (map(lambda line: line.replace('\n', ''), lines))))  # no empty lines, not EOL

# finds the index in the list of the function name
# it is placed one before the first '('
def find_function_name_index(temp):
    i = 0
    while i < len(temp) and temp[i] != '(':
        i+=1
    return i - 1

# add pur translated code into the tests so we will able to check it
def add_code_to_tests(lang, lines, add):
    titles = []  # return the titles and lines counting to it
    output_dir = '/mnt/c/TransCoder/outputs/' + lang + '/'
    if lang == 'python':
        lang = 'py'
    not_exists = []
    while len(lines) > 0:
        # find the lines of the translated function
        relevant_lines = []
        i = 1
        while lines[i] != END_OF_FUNCTION:
            relevant_lines.append(lines[i])
            i += 1

        test_path = output_dir + lines[0] + '.' + lang
        changed_test_path = output_dir + 'changed/' + add + lines[0] + '.' + lang
        # run only if the file exists (they do not have tests for all functions in every language
        if os.path.exists(test_path):
            with open(test_path) as specific_test_read:
                temp = relevant_lines[0].split()  # change the function name to f_filled
                ind = find_function_name_index(temp) # finds the place of funcion name
                origin_function_name = temp[ind]  # if uses recursion we need to change in many places
                temp[ind] = 'f_filled'
                relevant_lines[0] = ' '.join(temp)
                specific_test_str = specific_test_read.read()
                specific_test_str = specific_test_str.replace('TOFILL', '\n' + '\n'.join(relevant_lines).replace(
                    origin_function_name, 'f_filled'))
            with open(changed_test_path, 'w') as specific_test_write:
                specific_test_write.write(specific_test_str)

            titles.append([lines[0], len(relevant_lines)])  # add the title and lines amount
        else:
            not_exists.append(lines[0] + '\n')
        lines = lines[i + 1:]
    return titles, not_exists

# an handler that raises exception - for infinite loops
def handler(signum, frame):
    raise Exception('what')

# run the tests of python language (translated from java)
def run_python_tests(titles, add):
    results = []
    dir_path = '/mnt/c/TransCoder/outputs/python/changed/' + add
    for title in titles:
        try:
            signal.alarm(30)
            os.system('python3 ' + dir_path + title[0] + '.py > ' + dir_path + 'temp.txt')  # run the python test
            signal.alarm(0)
            with open(dir_path + 'temp.txt') as result:  # take the result we printed
                res = result.read()[:-1].split()  # no EOL, split by ' '
                results.append([title[0], title[1], res[-2], res[-1]])
        except:
            results.append([title[0], title[1], -1, -1])
        os.system('rm ' + dir_path + 'temp.txt')
    return results


# run the tests of java language (translated from python)
def run_java_tests(titles, add):
    results = []
    dir_path = '/mnt/c/TransCoder/outputs/java/changed/' + add
    for title in titles:
        try:
            os.system('javac' + dir_path + title[0] + '.java')  # compile the java test
            os.system('cd ' + dir_path)  # go into the dir because java is annoying
            signal.alarm(30)
            os.system('java ' + title[0] + ' > temp.txt')  # run the java test
            signal.alarm(0)
            with open(dir_path + 'temp.txt') as result:  # take the result we printed
                res = result.read()[:-1].split()  # no EOL, split by ' '
                results.append([title[0], title[1], res[-2], res[-1]])
        except:
            results.append([title[0], title[1], -1, -1])
        os.system('rm ' + dir_path + 'temp.txt')
    return results


# order the results so we will print them
def order_results(results):
    return list(map(
        lambda res: (res[0] + ' lines: ' + str(res[1]) + ' successes: ' + str(res[2]) + ' tests: ' + str(
            res[3]) + '\n'), results))


if __name__ == '__main__':
    print_time()
    signal.signal(signal.SIGALRM, handler) # for infinite loops

    # read the translation data we created
    use_data_from_tests = False
    add = 'from_tok/'
    if use_data_from_tests:
        add = 'from_tests/'
    out_dir = '/mnt/c/TransCoder/outputs/' + add

    java_lines = read_translated(out_dir + 'translated_java.java')
    python_lines = read_translated(out_dir + 'translated_python.py')

    # put it out
    python_titles, python_not_exists = add_code_to_tests('python', python_lines, add)
    java_titles, java_not_exists = add_code_to_tests('java', java_lines, add)

    # run the tests
    python_results = run_python_tests(python_titles, add)
    java_results = run_java_tests(java_titles, add)

    python_results = order_results(python_results)
    java_results = order_results(java_results)

    with open(out_dir + 'tests_run_check_python.txt', 'w') as f:
        f.writelines(python_results)
    with open(out_dir + 'not_exists_python.txt', 'w') as f:
        f.writelines(python_not_exists)
    with open(out_dir + 'tests_run_check_java.txt', 'w') as f:
        f.writelines(java_results)
    with open(out_dir + 'not_exists_java.txt', 'w') as f:
        f.writelines(java_not_exists)

    print_time()
