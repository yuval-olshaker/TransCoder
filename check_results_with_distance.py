import Levenshtein
import complex_check
import operator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

max_length = 350
exp_name = 'c-wat' # 'c-wat-all'
range1 = 3
if 'all' in exp_name:
    range1 = 3

tested_len = [0]
ref = '/mnt/c/TransCoder/outputs/' + exp_name + '/double_stage/eval/ref.wat_sa-c_sa.test.txt'
wat_ref = '/mnt/c/TransCoder/outputs/' + exp_name + '/double_stage/eval/ref.c_sa-wat_sa.test.txt'
double_translated_paths = list(map(lambda i: '/mnt/c/TransCoder/outputs/' + exp_name + '/double_stage/eval/hyp0.wat_sa-c_sa.test_beam' + str(i) + '.txt', range(range1)))
lean_translated_paths = list(map(lambda i: '/mnt/c/TransCoder/outputs/' + exp_name + '/mt_ae_lean/eval/hyp0.wat_sa-c_sa.test_beam' + str(i) + '.txt', range(range1)))
# baseline_translated_paths = list(map(lambda i: '/mnt/c/TransCoder/outputs/' + exp_name + '/baseline_only_transformer_parallel/eval/hyp0.wat_sa-c_sa.test_beam' +str(i) + '.txt', range(3)))

valid = '/mnt/c/TransCoder/outputs/' + exp_name + '/double_stage/eval/ref.wat_sa-c_sa.valid.txt'
wat_valid = '/mnt/c/TransCoder/outputs/' + exp_name + '/double_stage/eval/ref.c_sa-wat_sa.valid.txt'
double_translated_paths_valid = list(map(lambda i: '/mnt/c/TransCoder/outputs/' + exp_name + '/double_stage/eval/hyp0.wat_sa-c_sa.valid_beam' + str(i) + '.txt', range(range1)))
lean_translated_paths_valid = list(map(lambda i: '/mnt/c/TransCoder/outputs/' + exp_name + '/mt_ae_lean/eval/hyp0.wat_sa-c_sa.valid_beam' + str(i) + '.txt', range(range1)))
# baseline_translated_paths_valid = list(map(lambda i: '/mnt/c/TransCoder/outputs/' + exp_name + '/baseline_only_transformer_parallel/eval/hyp0.wat_sa-c_sa.valid_beam' +str(i) + '.txt', range(3)))


ref2 = '/mnt/c/TransCoder/outputs/' + exp_name + '/check/refs.txt'
trans2 = '/mnt/c/TransCoder/outputs/' + exp_name + '/check/trans.txt'

double_scores_path = '/mnt/c/TransCoder/outputs/' + exp_name + '/double_stage/eval/scores.csv'
single_scores_path = '/mnt/c/TransCoder/outputs/' + exp_name + '/mt_ae_lean/eval/scores.csv'

output_path = '/mnt/c/TransCoder/outputs/' + exp_name + '/'
double_succ = output_path + 'double_succ.txt'
lean_succ = output_path + 'lean_succ.txt'

train_sta_path = output_path + 'train.tok'

def distance(or_line, tested_line):
    dist = Levenshtein.distance(or_line, tested_line)
    if dist != 0:
        if complex_check.complex_check(or_line, tested_line):
            return 0
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
    ref2_lines = return_lines(ref2)
    trans2_lines = return_lines(trans2)
    iss = []
    for i, ref_line in enumerate(ref2_lines):
        if ref_line == trans2_lines[i]:
            iss.append(i)
    print(iss)
    print(len(iss))
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

    print('j: ' + str(j) + ' new_succ: ' + str(len(succ_indices) - j))
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

def print_2_ppls_accs(path1, path2, title_beg):
    ppls1 = []
    accs1 = []
    for i in range(0, max_length, 5):
        tested_len[0] = i
        _, indices = return_lines(ref, filter_func=long_line)
        ppl, acc = get_acc_ppl_res(path1, indices)
        ppls1.append(ppl)
        accs1.append(acc)

    ppls2 = []
    accs2 = []
    for i in range(0, max_length, 5):
        tested_len[0] = i
        _, indices = return_lines(ref, filter_func=long_line)
        ppl, acc = get_acc_ppl_res(path2, indices)
        ppls2.append(ppl)
        accs2.append(acc)

    ppl_tick = 0.1
    acc_tick = 1.0
    create_2_graphs(ppls1, ppls2, 'ppl', title_beg + ' ppl', ppl_tick)
    create_2_graphs(accs1, accs2, 'acc', title_beg + ' acc', acc_tick)

def print_ppls_accs(path, title_beg):
    ppls = []
    accs = []
    for i in range(0, max_length, 5):
        tested_len[0] = i
        _, indices = return_lines(ref, filter_func=long_line)
        ppl, acc = get_acc_ppl_res(path, indices)
        ppls.append(ppl)
        accs.append(acc)

    ppl_tick = 0.1
    acc_tick = 1.0
    if 'all' in exp_name:
        ppl_tick = 0.02
        acc_tick = 0.3

    create_graph(ppls, 'ppl', title_beg + ' ppl', ppl_tick)
    create_graph(accs, 'acc', title_beg + ' acc', acc_tick)


def save_pic(save_name):
    plt.savefig('/mnt/c/TransCoder/outputs/' + exp_name + '/' + save_name)


def create_2_graphs(y1, y2, name, title, tick):
    x = list(range(0, max_length, 5))

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
    x = list(range(0, max_length, 5))

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
    print_2_ppls_accs(double_scores_path, single_scores_path, 'both models')

    # print_ppls_accs(double_scores_path, 'double stage model')
    # print_ppls_accs(single_scores_path, 'single stage model')


def run_evaluation(ref_lines, indices, wat_lines, paths, train_lines):
    # read translated lines
    double_translated_lines = list(map(lambda line: return_lines(line, indices=indices), paths[0]))
    lean_translated_lines = list(map(lambda line: return_lines(line, indices=indices), paths[1]))
    # baseline_translated_lines = list(map(lambda line: return_lines(line, indices=indices), paths[2]))

    results_double = []
    results_lean = []
    results_base = []

    # check_i(302)

    # run over refs and calculate the distances
    for i, ref_line in enumerate(ref_lines):
        # we take the min of all beams
        d_double = min(list(map(lambda lines: distance(ref_line, lines[i]), double_translated_lines)))
        d_lean = min(list(map(lambda lines: distance(ref_line, lines[i]), lean_translated_lines)))
        # d_base = min(list(map(lambda lines: distance(ref_line, lines[i]), baseline_translated_lines)))

        results_double.append(d_double)
        results_lean.append(d_lean)
        # results_base.append(d_base)

        # if 0 < d_double < 10:
        #     print(i)

    # create lists for exact match - including complex_check
    zeros_d = []
    zeros_l = []
    # zeros_b = []
    for i, res in enumerate(results_double):
        if res == 0:
            zeros_d.append(i)
        if results_lean[i] == 0:
            zeros_l.append(i)
        # if results_base[i] == 0:
        #     zeros_b.append(i)

    only_d = sorted(set(zeros_d).difference(set(zeros_l)))
    only_l = sorted(set(zeros_l).difference(set(zeros_d)))

    print('only_d: zise - ' + str(len(only_d)) + ' list - ' + str(only_d))
    print('only_l: zise - ' + str(len(only_l)) + ' list - ' + str(only_l))
    print()

    # prints and saves results
    check_succ(double_succ, only_d, ref_lines, wat_lines, lean_translated_lines[0], lean_translated_lines[1],
               lean_translated_lines[2])
    check_succ(lean_succ, only_l, ref_lines, wat_lines, double_translated_lines[0], double_translated_lines[1],
               double_translated_lines[2])
    print_results(output_path, zeros_d, ref_lines, train_lines, 'double')
    print_results(output_path, zeros_l, ref_lines, train_lines, 'one_stage')
    # print_results(output_path, zeros_b, ref_lines, train_lines, 'baseline')

    print()
    print(zeros_d)
    print(zeros_l)
    # print(zeros_b)

    print()
    print('double model total: ' + str(sum(results_double)) + ' correct num: ' + str(len(zeros_d)))
    print('one model total: ' + str(sum(results_lean)) + ' correct num: ' + str(len(zeros_l)))
    # print('base model total: ' + str(sum(results_base)) + ' correct num: ' + str(len(zeros_b)))
    print()
    print()

def distance_check():
    train_lines = list(
        map(lambda line: line.replace('<DOCUMENT_ID="repo/tree/master/a.c"> ', '').replace(' </DOCUMENT>', ''),
            return_lines(train_sta_path)))
    ref_lines, indices = return_lines(ref, train_lines=train_lines, filter_func=long_line)
    wat_lines = return_lines(wat_ref, indices=indices)
    run_evaluation(ref_lines, indices, wat_lines, [double_translated_paths, lean_translated_paths],train_lines)

    run_valid = False
    if run_valid:
        ref_lines, indices = return_lines(valid, train_lines=train_lines, filter_func=always_true)
        wat_lines = return_lines(wat_valid, indices=indices)
        run_evaluation(ref_lines, indices, wat_lines,
                       [double_translated_paths_valid, lean_translated_paths_valid],train_lines)

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
    for i in range(0, max_length, 5):
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
    print_histogram(from_lines_to_length(train_lines), 'train')

    refs_lines = return_lines(ref)
    print_histogram(from_lines_to_length(refs_lines), 'test')


if __name__ == "__main__":
    # commented out full-baseline (only transformer)
    # check()
    # distance_check()
    print_ppl_acc_graphs()
    # print_sizes_histogram()