import os
from os.path import isfile, join
langs = ['c', 'wat']


def get_all_files(path):
    return [f for f in os.listdir(path) if isfile(join(path, f))]


if __name__ == '__main__':
    long = True
    if long:
        for lang in langs:
            path = '/mnt/c/TransCoder/data/WASM/' + lang + '/'
            for file_name in get_all_files(path):
                if not file_name.endswith('corpus_small_fixed'):
                    os.system('rm ' + path + file_name)
        print('killed files')
        os.system('rm -rf /mnt/c/TransCoder/data/WASM/c-wat-')
        print('killed combined')

        print('start to_json')
        os.system('python3 /mnt/c/TransCoder/preprocessing/to_json.py')

    print('start training')
    os.system('python3 -m preprocessing.preprocess  /mnt/c/TransCoder/data/WASM --lang1 c --lang2 wat --bpe_train_size 0 --test_size 100 --local True')