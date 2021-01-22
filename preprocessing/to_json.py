import os

langs = ['c', 'wat']
json_str_start = '{\"repo_name\":\"repo\",\"ref\":\"refs/heads/master\",\"path\":\"a.c\",\"copies\":\"1\",'
# Transcoder_path = '/mnt/c/TransCoder/'
Transcoder_path = '/home/ubuntu/wasm_decompiler/TransCoder/'

def to_json_line(line):
    line = line[:-1] # remove \n
    return json_str_start + '\"language\":\"' + lang + '\",\"content\":\"' + line + '\"}\n'


if __name__ == '__main__':
    for lang in langs:
        if lang == 'c':
            path = Transcoder_path + 'data/WASM/c/hl_corpus_fixed'
        else:
            path = Transcoder_path + 'data/WASM/wat/ll_corpus_fixed'



        with open(path) as f:
            lines = f.readlines()

        lines = list(map(to_json_line, lines))
        path = path + '.000.json'
        os.system('rm ' + path + '.gz')
        with open(path, 'w') as f2:
            f2.writelines(lines)

        os.system('gzip ' + path)