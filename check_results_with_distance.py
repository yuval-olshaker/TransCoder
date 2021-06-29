import Levenshtein
import numpy

import operator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

colors = ['green', 'blue', 'red', 'orange', 'black', 'purple'] # baseline, single, base_half, half, base_double, double
model_names = ['baseline', 'single', 'base_half', 'half', 'base_double', 'double']
max_length = 245
jumps = 3
min_length = 0
exp_name = 'c-x86' # 'c-wat-all' 'c-wat-full' 'c-x86'
range1 = 3
if 'x86' in  exp_name:
    range1 = 5
    max_length = 75

tested_len = [0]

# refs
ref = '/mnt/c/TransCoder/outputs/' + exp_name + '/double/eval/ref.wat_sa-c_sa.test.txt'
wat_ref = '/mnt/c/TransCoder/outputs/' + exp_name + '/double/eval/ref.c_sa-wat_sa.test.txt'

# translations paths - for graphs
all_translated_paths = list(map(lambda model_name: list(map(lambda i: '/mnt/c/TransCoder/outputs/' + exp_name + '/' + model_name + '/eval/hyp0.wat_sa-c_sa.test_beam' +str(i) + '.txt', range(range1))), model_names))

# scores paths - for graphs
all_scores_paths = list(map(lambda model_name: '/mnt/c/TransCoder/outputs/' + exp_name + '/' + model_name + '/eval/scores.csv', model_names))

output_path = '/mnt/c/TransCoder/outputs/' + exp_name + '/'
double_succ = output_path + 'double_succ.txt'
single_succ = output_path + 'single_succ.txt'
half_succ = output_path + 'half_succ.txt'

train_sta_path = output_path + 'train.tok'


# results:
distances = [[],[],[],[],[],[]]
identical_match = [[], [], [], [], [], []]
accs = []
ppls = []

def distance(or_line, tested_line):
    dist = Levenshtein.distance(or_line, tested_line)
    # if dist != 0:
    #     if complex_check.complex_check(or_line, tested_line):
    #         return 0
    return dist

def list_in_indices(l, indices):
    f = operator.itemgetter(*indices)
    return f(l)

def long_line(line): # long sentence is over 20 C tokens / 70
    return len(line.split()) > tested_len[0]

def has_while_loop(line):
    return 'while' in line

def has_if(line):
    return 'if' in line

def has_no_if(line):
    return not has_if(line)

def has_for_loop(line):
    return 'for' in line

def has_pointer(line):
    return '*' in line

def has_deref(line):
    return '&' in line

def has_no_deref(line):
    return not has_deref(line)

def has_struct(line):
    return 'struct' in line

def has_no_struct(line):
    return not has_struct(line)

def has_unary(line):
    return '+ +' in line or '- -' in line

def hard_sentence(line):
    return has_for_loop(line) or has_no_if(line) or has_while_loop(line) or long_line(line)

def easy_sentence(line):
    return not hard_sentence(line)


def has_no_void(line):
    return 'void' not in line

def has_void(line):
    return 'void' in line

def always_true(line):
    return True

def return_lines(path, filter_func=None, indices=None):
    with open(path) as f:
        lines = f.readlines()
        if filter_func is not None:
            # and lines[x] not in train_lines
            indices = list(filter(lambda x: filter_func(lines[x]), range(len(lines))))
            return list_in_indices(lines, indices), indices

    if indices is None:
        return lines
    return list_in_indices(lines, indices)




def check():
    train_lines = list(
        map(lambda line: line.replace('<DOCUMENT_ID="repo/tree/master/a.c"> ', '').replace(' </DOCUMENT>', ''),
            return_lines(train_sta_path)))
    i = 0
    for line in train_lines:
        if 'stR' in line:
            i += 1
    print(i)
    # print_histogram(ref2_lines, 'hh')
    exit(1)

def check_succ(succ_path, only_list, ref_lines, wat_lines, translated0_lines, translated1_lines, translated2_lines):
    with open(succ_path, 'w') as f:
        for i in only_list:
            f.write(str(i) + '\n')
            f.write(ref_lines[i])
            f.write(wat_lines[i])
            f.write(translated0_lines[i])
            f.write(translated1_lines[i])
            f.write(translated2_lines[i])
            f.write('\n\n')

def Average(lst):
    return sum(lst) / len(lst)

def print_results(basic_path, succ_indices, ref_lines, train_lines, exp_name):
    with open(basic_path + 'succ_' + exp_name, 'w') as f_succ:
        with open(basic_path + 'fail_' + exp_name, 'w') as f_fail:
            j = 0
            succ_l = []
            succ_ind = []
            for i, ref_line in enumerate(ref_lines):
                if i in succ_indices:
                    if ref_line in train_lines or ref_line in succ_l:
                        j += 1
                    else:
                        f_succ.write(ref_line)
                        succ_l.append(ref_line)
                        succ_ind.append(i)
                else:
                    f_fail.write(ref_line)

    print(exp_name + ' - total_succ: ' + str(j) + ' new_succ: ' + str(len(succ_indices) - j))
    len_list = list(map(lambda line: len(line.split()), succ_l))
    print(len_list)
    if len(len_list) > 0:
        print(Average(len_list))
    else:
        print('haha')
    print(succ_ind)


def check_i(num, ref_lines, double_translated_lines):
    d_double = min(list(map(lambda lines: distance(ref_lines[num], lines[num]), double_translated_lines)))
    print(d_double)
    exit(1)

def get_acc_ppl_res(path, indices):
    df = pd.read_csv(path)
    n_words = sum(list_in_indices(list(df['n_words']), indices))
    xe_loss = sum(list_in_indices(list(df['xe_loss']), indices))
    n_valid = sum(list_in_indices(list(df['n_valid']), indices))
    ppl = np.exp(xe_loss / n_words)
    acc = 100. * n_valid / n_words
    return ppl, acc

def print_num_ppls_accs():
    title_beg = 'Six Models'
    for i, path in enumerate(all_scores_paths):
        ppls.append([])
        accs.append([])
        for j in range(min_length, max_length, jumps):
            tested_len[0] = j
            _, indices = return_lines(ref, filter_func=long_line)
            ppl, acc = get_acc_ppl_res(path, indices)
            ppls[i].append(ppl)
            accs[i].append(acc)

    ppl_tick = 0.1
    acc_tick = 1.0
    create_num_graphs(ppls, 'ppl', title_beg + ' ppl', ppl_tick)
    create_num_graphs(accs, 'acc', title_beg + ' acc', acc_tick)


def save_pic(save_name):
    plt.savefig('/mnt/c/TransCoder/outputs/' + exp_name + '/' + save_name)

def create_num_graphs(ys, name, title, tick):
    x = list(range(min_length, max_length, jumps))

    for i, y in enumerate(ys):
        plt.scatter(x, y, color=colors[i],
                    marker="*", s=30, label=model_names[i])



    plt.yticks(np.arange(min(list(map(lambda y: min(y), ys))) - tick, max(list(map(lambda y: max(y), ys))) + tick, tick))
    plt.axis()
    # naming the x axis
    plt.xlabel('min length')
    # naming the y axis
    plt.ylabel(name)

    # giving a title to my graph
    plt.title(title)

    plt.legend()

    # function to show the plot
    save_pic(title + '.png')
    plt.show()

    y = []
    for i in range(len(ys[0])): # TODO: change to best (by acc or ppl)
        y.append(ys[1][i] - ys[3][i]) # ys[3] - baseline. ys[2] - double. ys[1] - half. ys[0] - single.
    print('diff ' + title.split(' ')[-1])
    # print(y)
    print('min: ' + str(min(y)) + ' max: ' + str(max(y)))
    create_graph(y, 'diff', 'diff ' + title.split(' ')[-1], tick / 10)

def create_2_graphs(y1, y2, name, title, tick):
    x = list(range(min_length, max_length, jumps))

    # plotting the points
    plt.scatter(x, y1, label="stars", color="green",
                marker="*", s=30)
    plt.scatter(x, y2, label="stars", color="blue",
                marker="*", s=30)
    plt.yticks(np.arange(min(y1), max(y2) + tick, tick))
    plt.axis()
    # naming the x axis
    plt.xlabel('min length')
    # naming the y axis
    plt.ylabel(name)

    # giving a title to my graph
    plt.title(title)

    # function to show the plot
    save_pic(title + '.png')
    plt.show()

    y = []
    for i in range(len(y1)):
        y.append(y1[i]-y2[i])
    create_graph(y, 'name', 'title', 0.1)

def create_graph(y, name, title, tick):
    # x axis values
    x = list(range(min_length, max_length, jumps))

    # plotting the points
    plt.scatter(x, y, label="stars", color="green",
                marker="*", s=30)
    plt.yticks(np.arange(min(y), max(y) + tick, tick))
    plt.axis()
    # naming the x axis
    plt.xlabel('min length')
    # naming the y axis
    plt.ylabel(name)

    # giving a title to my graph
    plt.title(title)

    # function to show the plot
    save_pic(title + '.png')
    plt.show()

def print_ppl_acc_graphs():
    print_num_ppls_accs()

    # print_ppls_accs(double_scores_path, 'double stage model')
    # print_ppls_accs(single_scores_path, 'single stage model')


def distance_check():
    # read translated lines
    all_translated_lines = list(map(lambda translated_paths:
                                    list(map(lambda path: return_lines(path), translated_paths)), all_translated_paths))

    # run over refs and calculate the distances
    for i, ref_line in enumerate(return_lines(ref)):
        for j in range(len(all_translated_lines)):
            # we take the min of all beams
            d = min(list(map(lambda lines: distance(ref_line, lines[i]), all_translated_lines[j])))
            distances[j].append(d)
            # if identical the result is 0
            if d == 0:
                identical_match[j].append(i)

def print_histogram(sizes, title):
    # setting the ranges and no. of intervals
    range1 = (0, 200)
    bins = 50

    # plotting a histogram
    plt.hist(sizes, bins, range1, color='green',
             histtype='bar', rwidth=0.8, density=True)

    # x-axis label
    plt.xlabel('sentence length')
    # frequency label
    plt.ylabel('No. of sentences')
    # plot title
    plt.title('Sentences Length Histogram ' + title)

    # function to show the plot
    save_pic('Sentences Length Histogram ' + title + '.png')
    plt.show()

    sizes2 = []
    temp = sizes.copy()
    for i in range(min_length, max_length, jumps):
        temp = list(filter(lambda size: size > i,temp))
        sizes2.append(len(temp) / len(sizes))
    tick = 0.1

    create_graph(sizes2, 'No. of sentences', 'Sentences Length Graph ' + title, tick)



def from_lines_to_length(lines):
    return list(map(lambda line: len(line.split(' ')), lines))


def print_sizes_histogram():
    train_lines = list(
        map(lambda line: line.replace('<DOCUMENT_ID="repo/tree/master/a.c"> ', '').replace(' </DOCUMENT>', ''),
            return_lines(train_sta_path)))
    sizes = from_lines_to_length(train_lines)
    print_histogram(sizes, 'train')
    print(numpy.percentile(sizes, 25))
    print(numpy.percentile(sizes, 50))
    print(numpy.percentile(sizes, 75))

    refs_lines = return_lines(ref)
    print_histogram(from_lines_to_length(refs_lines), 'test')


def from_list_to_line(name, list):
    s = name
    for l in list:
        s += ',' + str(l)

    s += '\n'
    return s

def calc_total_succ():
    total_succ = []
    all_succ_paths = list(
        map(lambda
                model_name: '/mnt/c/TransCoder/outputs/' + exp_name + '/' + model_name + '/eval/test0.success.5.csv',
            model_names))
    for path in all_succ_paths:
        with open(path) as f:
            total_succ.append(len(f.readlines()) - 1)

    return total_succ

def create_table():
    sum_distances = list(map(lambda diss: sum(diss), distances))
    num_identical_match = list(map(lambda diss: len(diss), identical_match))
    total_accs = list(map(lambda acc: acc[0], accs))
    total_ppls = list(map(lambda ppl: ppl[0], ppls))

    out_path = output_path + 'results.csv'
    with open(out_path, 'w') as w:
        w.write(from_list_to_line('Model Name', model_names))
        w.write(from_list_to_line('Distances', sum_distances))
        w.write(from_list_to_line('Correct Num', num_identical_match))
        w.write(from_list_to_line('Acc', total_accs))
        w.write(from_list_to_line('Ppl', total_ppls))
        if 'x86' in exp_name:
            w.write(from_list_to_line('Total Success By TraFix', calc_total_succ()))


    a = 5

if __name__ == "__main__":
    # commented out full-baseline (only transformer)
    # check()
    distance_check()
    print_ppl_acc_graphs()
    create_table()
    # print_sizes_histogram()