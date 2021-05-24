import os
import json
langs = ['c', 'wat']
data_path = 'data/WASM_semi_full/'
json_str_start = '{\"repo_name\":\"repo\",\"ref\":\"refs/heads/master\",\"path\":\"a.c\",\"copies\":\"1\",'
# Transcoder_path = '/mnt/c/TransCoder/'
Transcoder_path = '/home/ubuntu/wasm_decompiler/TransCoder/'


def to_json_line(line):
    line = line[:-1] # remove \n
    return json_str_start + '\"language\":\"' + lang + '\",\"content\":\"' + line + '\"}\n'


if __name__ == '__main__':
    json_failed = []
    for lang in langs:
        if lang == 'c':
            path = Transcoder_path + data_path + 'c/hl_corpus_fixed'
        else:
            path = Transcoder_path + data_path + 'wat/ll_corpus_fixed'



        with open(path) as f:
            lines = list(map(to_json_line, f.readlines()))

        new_lines = []
        for i, line in enumerate(lines):
            if i in json_failed:
                continue
            try:
                x = json.loads(line)
                new_lines.append(line)
            except:
                json_failed.append(i)


        path = path + '.000.json'
        os.system('rm ' + path + '.gz')
        with open(path, 'w') as f2:
            f2.writelines(new_lines)

        os.system('gzip ' + path)