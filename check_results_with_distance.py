import Levenshtein


ref = '/mnt/c/TransCoder/outputs/c-wat/double_stage/eval/ref.wat_sa-c_sa.test.txt'
wat_ref = '/mnt/c/TransCoder/outputs/c-wat/double_stage/eval/ref.c_sa-wat_sa.test.txt'
double_translated_paths = list(map(lambda i: '/mnt/c/TransCoder/outputs/c-wat/double_stage/eval/hyp0.wat_sa-c_sa.test_beam' + str(i) + '.txt', range(25)))
lean_translated_paths = list(map(lambda i: '/mnt/c/TransCoder/outputs/c-wat/mt_ae_lean/eval/hyp0.wat_sa-c_sa.test_beam' + str(i) + '.txt', range(3)))
baseline_translated_paths = list(map(lambda i: '/mnt/c/TransCoder/outputs/c-wat/baseline_only_transformer_parallel/eval/hyp0.wat_sa-c_sa.test_beam' +str(i) + '.txt', range(3)))


ref2 = '/mnt/c/TransCoder/outputs/c-wat/check/refs.txt'
trans2 = '/mnt/c/TransCoder/outputs/c-wat/check/trans.txt'

output_path = '/mnt/c/TransCoder/outputs/c-wat/'
double_succ = output_path + 'double_succ.txt'
lean_succ = output_path + 'lean_succ.txt'

def distance(or_line, tested_line):
    return Levenshtein.distance(or_line, tested_line)

def return_lines(path):
    with open(path) as f:
        lines = list(map(lambda line: line.replace('void ','').replace('static ','') ,f.readlines()))
    return lines

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

if __name__ == "__main__":
    # check()
    ref_lines = return_lines(ref)
    wat_lines = return_lines(wat_ref)

    double_translated_lines = list(map(return_lines, double_translated_paths))
    lean_translated_lines = list(map(return_lines, lean_translated_paths))
    baseline_translated_lines = list(map(return_lines, baseline_translated_paths))

    results_double = []
    results_lean = []
    results_base = []

    print(len(ref_lines))
    for i, ref_line in enumerate(ref_lines):
        d_double = min(list(map(lambda lines: distance(ref_line, lines[i]), double_translated_lines)))
        d_lean = min(list(map(lambda lines: distance(ref_line, lines[i]), lean_translated_lines)))
        d_base = min(list(map(lambda lines: distance(ref_line, lines[i]), baseline_translated_lines)))

        results_double.append(d_double)
        results_lean.append(d_lean)
        results_base.append(d_base)



    zeros_d = []
    zeros_l = []
    zeros_b = []
    for i, res in enumerate(results_double):
        if res == 0:
            zeros_d.append(i)
        if results_lean[i] == 0:
            zeros_l.append(i)
        if results_base[i] == 0:
            zeros_b.append(i)

    only_d = sorted(set(zeros_d).difference(set(zeros_l)))
    only_l = sorted(set(zeros_l).difference(set(zeros_d)))

    print('only_d: zise - ' + str(len(only_d)) + ' list - ' +  str(only_d))
    print('only_d: zise - ' + str(len(only_l)) + ' list - ' + str(only_l))

    check_succ(double_succ, only_d, ref_lines, wat_lines, lean_translated_lines[0], lean_translated_lines[1], lean_translated_lines[2])
    check_succ(lean_succ, only_l, ref_lines, wat_lines, double_translated_lines[0], double_translated_lines[1], double_translated_lines[2])

    print(zeros_d)
    print(zeros_l)
    print(zeros_b)


    print()
    print()
    print('double model total: ' + str(sum(results_double)) + ' correct num: ' + str(len(list(filter(lambda x: x == 0, results_double)))))
    print('one model total: ' + str(sum(results_lean)) + ' correct num: ' + str(len(list(filter(lambda x: x ==0, results_lean)))))
    print('base model total: ' + str(sum(results_base)) + ' correct num: ' + str(len(list(filter(lambda x: x == 0, results_base)))))
