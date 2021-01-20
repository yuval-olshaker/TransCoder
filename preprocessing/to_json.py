import os

lang = 'c'
json_str_start = '{\"repo_name\":\"repo\",\"ref\":\"refs/heads/master\",\"path\":\"a.c\",\"copies\":\"1\",'

def to_json_line(line):
    line = line[:-1] # remove \n
    return json_str_start + '\"language\":\"' + lang + '\",\"content\":\"' + line + '\"}\n'


if __name__ == '__main__':

    if lang == 'c':
        path = '/mnt/c/TransCoder/data/WASM/c/hl_corpus_small_fixed'
    else:
        path = '/mnt/c/TransCoder/data/WASM/wat/ll_corpus_small_fixed'

    os.system('rm ' + path + '.json.gz')

    with open(path) as f:
        lines = f.readlines()

    lines = list(map(to_json_line, lines))
    path = path + '.000.json'
    with open(path, 'w') as f2:
        f2.writelines(lines)

    os.system('gzip ' + path)