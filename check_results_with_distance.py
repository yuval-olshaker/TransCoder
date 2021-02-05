import Levenshtein


ref = '/mnt/c/TransCoder/outputs/c-wat/double_stage/eval/ref.wat_sa-c_sa.test.txt'
double_translated0 = '/mnt/c/TransCoder/outputs/c-wat/double_stage/eval/hyp0.wat_sa-c_sa.test_beam0.txt'
double_translated1 = '/mnt/c/TransCoder/outputs/c-wat/double_stage/eval/hyp0.wat_sa-c_sa.test_beam1.txt'
double_translated2 = '/mnt/c/TransCoder/outputs/c-wat/double_stage/eval/hyp0.wat_sa-c_sa.test_beam2.txt'
lean_translated0 = double_translated0.replace('double_stage','mt_ae_lean')
lean_translated1 = double_translated1.replace('double_stage','mt_ae_lean')
lean_translated2 = double_translated2.replace('double_stage','mt_ae_lean')

def distance(or_line, tested_line):
    return Levenshtein.distance(or_line, tested_line)

def return_lines(path):
    with open(path) as f:
        lines = f.readlines()
    return lines

if __name__ == "__main__":
    ref_lines = return_lines(ref)

    double_translated0_lines = return_lines(double_translated0)
    double_translated1_lines = return_lines(double_translated1)
    double_translated2_lines = return_lines(double_translated2)

    lean_translated0_lines = return_lines(lean_translated0)
    lean_translated1_lines = return_lines(lean_translated1)
    lean_translated2_lines = return_lines(lean_translated2)

    results_double = []
    results_lean = []

    for i, ref_line in enumerate(ref_lines):
        d_double = min(distance(ref_line, double_translated0_lines[i]), distance(ref_line, double_translated1_lines[i]), distance(ref_line, double_translated2_lines[i]))
        d_lean = min(distance(ref_line, lean_translated0_lines[i]), distance(ref_line, lean_translated1_lines[i]), distance(ref_line, lean_translated2_lines[i]))
        results_double.append(d_double)
        results_lean.append(d_lean)


    print('double model total: ' + str(sum(results_double)) + ' correct num: ' + str(len(list(filter(lambda x: x ==0, results_double)))))
    print('one model total: ' + str(sum(results_lean)) + ' correct num: ' + str(len(list(filter(lambda x: x ==0, results_lean)))))
    a = 5
