def return_lines(path):
    with open(path) as f:
        lines = f.readlines()

    return lines

trans_num = 5
exp_name = 'c-x86/baseline' # double / single / half / baseline
exp_dir = '/mnt/c/TransCoder/outputs/' + exp_name + '/eval/'
out_path = exp_dir + 'test0.corpus.5.out'

import pandas as pd

def check_line(line):
    return len(line.split()) > 0


def check_res():
    res_single_path = exp_dir + 'test0.success.5.csv'
    df_single = pd.read_csv(res_single_path)
    res_lines_single = list(filter(check_line, df_single['out'].values))
    res_double_path = res_single_path.replace('single','double')
    df_double = pd.read_csv(res_double_path)
    res_lines_double = list(filter(check_line, df_double['out'].values))

    print('double succ: ' + str(len(res_lines_double)))
    print('single succ: ' + str(len(res_lines_single)))

    ids_single = list(df_single['line'].values)
    ids_double = list(df_double['line'].values)
    only_d = []
    only_s = []
    for i, single_id in enumerate(ids_single):
        if single_id not in ids_double:
            only_s.append(single_id)
        if i < len(ids_double):
            double_id = ids_double[i]
            if double_id not in ids_single:
                only_d.append(double_id)

    print(len(only_d))
    print(only_d)
    print()
    print(len(only_s))
    print(only_s)

    out_double = list(df_double['out'].values)
    with open(exp_dir.replace('single','half') + 'choose.txt', 'w') as f:
        for i, ind in enumerate(ids_double):
            if ind in only_d:
                f.write('\n')
                f.write(str(ind) + '\n')
                f.write(out_double[i] + '\n')
                f.write('\n')
    exit(0)


if __name__ == "__main__":
    # check_res()

    translated_paths = list(map(lambda i: exp_dir + 'hyp0.wat_sa-c_sa.test_beam' + str(i) + '.txt', range(trans_num)))
    translated_lines = list(map(lambda line: return_lines(line), translated_paths))
    with open(out_path, 'w') as output:
        for i in range(len(translated_lines[0])):
            for j in range(trans_num):
                line = translated_lines[j][i]
                line_to_write = str(i) + ' ||| ' + line[:-1] + ' ||| \n' # \n in the end
                output.write(line_to_write)

