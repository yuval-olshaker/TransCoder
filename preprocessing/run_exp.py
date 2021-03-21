import os
from os.path import isfile, join
langs = ['c', 'wat']
data_path = 'data/WASM_all/'
# Transcoder_path = '/mnt/c/TransCoder/'
Transcoder_path = '/home/ubuntu/wasm_decompiler/TransCoder/'

def get_all_files(path):
    return [f for f in os.listdir(path) if isfile(join(path, f))]


if __name__ == '__main__':
    long = True
    if long:
        for lang in langs:
            path = Transcoder_path + data_path + lang + '/'
            for file_name in get_all_files(path):
                if not file_name.endswith('corpus_fixed'):
                    os.system('rm ' + path + file_name)
        print('killed files')
        os.system('rm -rf ' + Transcoder_path + data_path + 'c-wat-')
        os.system('rm -rf ' + Transcoder_path + data_path + 'c-wat-.XLM-syml')
        print('killed combined')

        print('start to_json')
        os.system('python3 ' + Transcoder_path + 'preprocessing/to_json.py')

    print('start training')
    print()
    print('python3 -m preprocessing.preprocess ' + Transcoder_path + data_path + ' --lang1 c --lang2 wat --bpe_train_size 0 --test_size 1500 --local True')
    os.system('python3 -m preprocessing.preprocess ' + Transcoder_path + data_path + ' --lang1 c --lang2 wat --bpe_train_size 0 --test_size 1500 --local True')