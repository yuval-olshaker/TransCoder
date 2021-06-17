import Levenshtein
import numpy

import complex_check
import operator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

colors = ['green', 'blue', 'red', 'orange'] # one, half, double, baseline
exp_names = ['one', 'half', 'double', 'baseline']
max_length = 245
# max_length = 75
jumps = 3
min_length = 0
exp_name = 'c-wat-full' # 'c-wat-all' 'c-wat-full'
range1 = 3
if 'all' in exp_name:
    range1 = 3
if 'x86' in  exp_name:
    range1 = 5

tested_len = [0]
ref = '/mnt/c/TransCoder/outputs/' + exp_name + '/double/eval/ref.wat_sa-c_sa.test.txt'
wat_ref = '/mnt/c/TransCoder/outputs/' + exp_name + '/double/eval/ref.c_sa-wat_sa.test.txt'
double_translated_paths = list(map(lambda i: '/mnt/c/TransCoder/outputs/' + exp_name + '/double/eval/hyp0.wat_sa-c_sa.test_beam' + str(i) + '.txt', range(range1)))
half_translated_paths = list(map(lambda i: '/mnt/c/TransCoder/outputs/' + exp_name + '/half/eval/hyp0.wat_sa-c_sa.test_beam' + str(i) + '.txt', range(range1)))
single_translated_paths = list(map(lambda i: '/mnt/c/TransCoder/outputs/' + exp_name + '/single/eval/hyp0.wat_sa-c_sa.test_beam' + str(i) + '.txt', range(range1)))
baseline_translated_paths = list(map(lambda i: '/mnt/c/TransCoder/outputs/' + exp_name + '/baseline/eval/hyp0.wat_sa-c_sa.test_beam' +str(i) + '.txt', range(3)))

valid = '/mnt/c/TransCoder/outputs/' + exp_name + '/double/eval/ref.wat_sa-c_sa.valid.txt'
wat_valid = '/mnt/c/TransCoder/outputs/' + exp_name + '/double/eval/ref.c_sa-wat_sa.valid.txt'
double_translated_paths_valid = list(map(lambda i: '/mnt/c/TransCoder/outputs/' + exp_name + '/double/eval/hyp0.wat_sa-c_sa.valid_beam' + str(i) + '.txt', range(range1)))
single_translated_paths_valid = list(map(lambda i: '/mnt/c/TransCoder/outputs/' + exp_name + '/single/eval/hyp0.wat_sa-c_sa.valid_beam' + str(i) + '.txt', range(range1)))
baseline_translated_paths_valid = list(map(lambda i: '/mnt/c/TransCoder/outputs/' + exp_name + '/baseline/eval/hyp0.wat_sa-c_sa.valid_beam' +str(i) + '.txt', range(3)))


ref2 = '/mnt/c/TransCoder/outputs/' + exp_name + '/check/refs.txt'
trans2 = '/mnt/c/TransCoder/outputs/' + exp_name + '/check/trans.txt'

double_scores_path = '/mnt/c/TransCoder/outputs/' + exp_name + '/double/eval/scores.csv'
half_scores_path = '/mnt/c/TransCoder/outputs/' + exp_name + '/half/eval/scores.csv'
single_scores_path = '/mnt/c/TransCoder/outputs/' + exp_name + '/single/eval/scores.csv'
baseline_scores_path = '/mnt/c/TransCoder/outputs/' + exp_name + '/baseline/eval/scores.csv'

output_path = '/mnt/c/TransCoder/outputs/' + exp_name + '/'
double_succ = output_path + 'double_succ.txt'
single_succ = output_path + 'single_succ.txt'
half_succ = output_path + 'half_succ.txt'

train_sta_path = output_path + 'train.tok'

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

def return_lines(path, train_lines=None, filter_func=None, indices=None):
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

def print_num_ppls_accs(paths, title_beg):
    accs = []
    ppls = []
    for i, path in enumerate(paths):
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
                    marker="*", s=30, label=exp_names[i])



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
    for i in range(len(ys[0])):
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
    print_num_ppls_accs([single_scores_path, half_scores_path, double_scores_path, baseline_scores_path], 'four models')

    # print_ppls_accs(double_scores_path, 'double stage model')
    # print_ppls_accs(single_scores_path, 'single stage model')


def run_evaluation(ref_lines, indices, wat_lines, paths, train_lines):
    # read translated lines
    double_translated_lines = list(map(lambda line: return_lines(line, indices=indices), paths[0]))
    single_translated_lines = list(map(lambda line: return_lines(line, indices=indices), paths[1]))
    half_translated_lines = list(map(lambda line: return_lines(line, indices=indices), paths[2]))

    results_double = []
    results_single = []
    results_half = []

    # check_i(302)
    # to find max diff
    # max = 0
    # maxi = 0

    # run over refs and calculate the distances
    for i, ref_line in enumerate(ref_lines):
        # we take the min of all beams
        d_double = min(list(map(lambda lines: distance(ref_line, lines[i]), double_translated_lines)))
        d_single = min(list(map(lambda lines: distance(ref_line, lines[i]), single_translated_lines)))
        d_half = min(list(map(lambda lines: distance(ref_line, lines[i]), half_translated_lines)))

        results_double.append(d_double)
        results_single.append(d_single)
        results_half.append(d_half)

        # if d_single-d_half > max:
        #     maxi = i
        #     max = d_single-d_half
        # if 0 < d_double < 10:
        #     print(i)

    # print(str(maxi) + '\n')
    # print(ref_lines[maxi])
    # print(wat_lines[maxi])
    # print(half_translated_lines[0][maxi])
    # print(half_translated_lines[1][maxi])
    # print(half_translated_lines[2][maxi])
    # print('\n\n')
    # print(single_translated_lines[0][maxi])
    # print(single_translated_lines[1][maxi])
    # print(single_translated_lines[2][maxi])
    # print('\n\n')

    # create lists for exact match - including complex_check
    zeros_double = []
    zeros_single = []
    zeros_half = []
    for i, res in enumerate(results_double):
        if res == 0:
            zeros_double.append(i)
        if results_single[i] == 0:
            zeros_single.append(i)
        if results_half[i] == 0:
            zeros_half.append(i)

    only_half = sorted(set(zeros_half).difference(set(zeros_single)))
    only_single = sorted(set(zeros_single).difference(set(zeros_half)))
    only_double = sorted(set(zeros_double).difference(set(zeros_single)))

    print('only_half: zise - ' + str(len(only_half)) + ' list - ' + str(only_half))
    print('only_single: zise - ' + str(len(only_single)) + ' list - ' + str(only_single))
    print('only_double: zise - ' + str(len(only_double)) + ' list - ' + str(only_double))

    # prints and saves results
    check_succ(half_succ, only_half, ref_lines, wat_lines, single_translated_lines[0], single_translated_lines[1],
               single_translated_lines[2])
    check_succ(single_succ, only_single, ref_lines, wat_lines, half_translated_lines[0], half_translated_lines[1],
               half_translated_lines[2])
    print_results(output_path, zeros_double, ref_lines, train_lines, 'double')
    print_results(output_path, zeros_half, ref_lines, train_lines, 'half')
    print_results(output_path, zeros_single, ref_lines, train_lines, 'single')
    # print_results(output_path, zeros_b, ref_lines, train_lines, 'baseline')

    print(zeros_double)
    print(zeros_half)
    print(zeros_single)
    # print(zeros_b)

    print('double model total: ' + str(sum(results_double)) + ' correct num: ' + str(len(zeros_double)))
    print('half model total: ' + str(sum(results_half)) + ' correct num: ' + str(len(zeros_half)))
    print('one model total: ' + str(sum(results_single)) + ' correct num: ' + str(len(zeros_single)))
    # print('base model total: ' + str(sum(results_base)) + ' correct num: ' + str(len(zeros_b)))
    print()
    print()

def distance_check():
    train_lines = list(
        map(lambda line: line.replace('<DOCUMENT_ID="repo/tree/master/a.c"> ', '').replace(' </DOCUMENT>', ''),
            return_lines(train_sta_path)))
    ref_lines, indices = return_lines(ref, train_lines=train_lines, filter_func=long_line)
    wat_lines = return_lines(wat_ref, indices=indices)
    run_evaluation(ref_lines, indices, wat_lines, [double_translated_paths, single_translated_paths, half_translated_paths],train_lines)

    run_valid = False
    if run_valid:
        ref_lines, indices = return_lines(valid, train_lines=train_lines, filter_func=always_true)
        wat_lines = return_lines(wat_valid, indices=indices)
        run_evaluation(ref_lines, indices, wat_lines,
                       [double_translated_paths_valid, single_translated_paths_valid],train_lines)

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


if __name__ == "__main__":
    # commented out full-baseline (only transformer)
    # check()
    # distance_check()
    print_ppl_acc_graphs()
    # print_sizes_histogram()