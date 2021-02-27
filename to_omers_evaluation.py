def return_lines(path):
    with open(path) as f:
        lines = f.readlines()

    return lines

trans_num = 5
exp_name = 'c-x86/single'
exp_dir = '/mnt/c/TransCoder/outputs/' + exp_name + '/eval/'
out_path = exp_dir + 'test0.corpus.5.out'


if __name__ == "__main__":
    translated_paths = list(map(lambda i: exp_dir + 'hyp0.wat_sa-c_sa.test_beam' + str(i) + '.txt', range(trans_num)))
    translated_lines = list(map(lambda line: return_lines(line), translated_paths))
    with open(out_path, 'w') as output:
        for i in range(len(translated_lines[0])):
            for j in range(trans_num):
                line = translated_lines[j][i]
                line_to_write = str(i) + ' ||| ' + line[:-1] + ' ||| \n' # \n in the end
                output.write(line_to_write)

