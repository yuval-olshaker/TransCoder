import multiprocessing
import os
from datetime import datetime

END_OF_FUNCTION = '|||'
MAX_TEST_TIME = 30 # the max time of single test. if takes more - infinite loop
TIMEOUT_FOR_COMMAND = 'timeout ' + str(2 * MAX_TEST_TIME) + 's '

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
def add_code_to_tests(lang, lines):
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
        changed_test_path = output_dir + 'changed/' + lines[0] + '.' + lang
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
                    origin_function_name, 'f_filled')).replace('import javafx.util.Pair;', '')
            with open(changed_test_path, 'w') as specific_test_write:
                specific_test_write.write(specific_test_str)

            titles.append([lines[0], len(relevant_lines)])  # add the title and lines amount
        else:
            not_exists.append(lines[0] + '\n')
        lines = lines[i + 1:]
    return titles, not_exists

# run command on linux
# second command is because at java we use "cd" command first and eant timeout for the run
def run_command(command, second_command):
    if second_command is None:
        os.system(TIMEOUT_FOR_COMMAND + command)
    else:
        os.system(command + TIMEOUT_FOR_COMMAND + second_command)

# starts process to run a command - if runs more than 30 seconds. raise exception
def run_process(command, second_command=None):
    p = multiprocessing.Process(target=run_command, args=(command,second_command))
    p.start()
    p.join(MAX_TEST_TIME)
    if p.is_alive():
        p.terminate()
        p.join()
        print('infinite loop:')
        print(second_command if second_command is not None else command)
        raise Exception

# run the tests of python language (translated from java)
def run_python_tests(titles):
    results = []
    dir_path = '/mnt/c/TransCoder/outputs/python/changed/'
    for title in titles:
        try:
            # if runs more then MAX_TEST_TIME (30) seconds - infinite loop
            run_process('python3 ' + dir_path + title[0] + '.py > ' + dir_path + 'temp.txt') # runs python test
            with open(dir_path + 'temp.txt') as result:  # take the result we printed
                res = result.read()[:-1].split()  # no EOL, split by ' '
                results.append([title[0], title[1], res[-2], res[-1]])
        except:
            results.append([title[0], title[1], -1, -1])
        os.system('rm ' + dir_path + 'temp.txt')
    return results


# run the tests of java language (translated from python)
def run_java_tests(titles):
    results = []
    dir_path = '/mnt/c/TransCoder/outputs/java/changed/'
    for title in titles:
        try:
            os.system('javac ' + dir_path + title[0] + '.java')  # compile the java test
            # if runs more then 30 seconds - infinite loops
            # run the java test, go into the dir because java is annoying
            run_process('cd ' + dir_path + ' ; ', 'java ' + title[0] + ' > temp.txt')
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

    out_dir = '/mnt/c/TransCoder/outputs/'

    # read the translation data we created
    python_lines = read_translated(out_dir + 'translated_python.py')
    java_lines = read_translated(out_dir + 'translated_java.java')

    # put it out
    python_titles, python_not_exists = add_code_to_tests('python', python_lines)
    java_titles, java_not_exists = add_code_to_tests('java', java_lines)

    # run the tests
    python_results = run_python_tests(python_titles)
    java_results = run_java_tests(java_titles)

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
