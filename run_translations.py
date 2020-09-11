# this scripts will run the translation on the test examples so we will be able to test the limitation
# one of the important things is to organize the output so we will be able to go over it
import argparse
import preprocessing.src.code_tokenizer as code_tokenizer
import translate

SEPARATOR = '|'

def get_parser():
    """
    Generate a parameters parser.
    """
    # parse parameters
    parser = argparse.ArgumentParser(description="Translate sentences")

    # pahts
    parser.add_argument("--java_path", type=str, default="", help="Java path")
    parser.add_argument("--python_path", type=str, default="", help="Python path")

    return parser

# splits a line to function-name and code. By | symbol
def split_line(line):
    index = line.find(SEPARATOR)
    name = line[:index-1] #cuts the space before the |
    code = line[index+2:-1] # cut the space after the |. cut \n in the end
    return name, code

# read the data from files
def read_file(file_path):
    with open(file_path) as file:
        lines = file.readlines()
    return list( map( split_line, lines))

# parse the lines and detokenize them so it will be readable for humans
def make_java_readable(java_file):
    return list(map(lambda line: (line[0], line[1], code_tokenizer.detokenize_java(line[1])), java_file))


def make_python_readable(python_file):
    return list(map(lambda line: (line[0], line[1], code_tokenizer.detokenize_python(line[1])), python_file))


# translate with the model from facebook
def translate_lines(is_from_java, file_readable):
    t_params = create_params('java', 'python') if is_from_java else create_params('python', 'java')
    translator = translate.Translator(t_params)
    return list(map(lambda line: (line[0], line[1], line[2],
                                  translator.translate(line[1], lang1=t_params.src_lang, lang2=t_params.tgt_lang,
                                                       beam_size=t_params.beam_size)[0]),
                    file_readable))


# create the params for translation
def create_params(src_lang, tgt_lang):
    a_parser = get_parser()
    a_params = a_parser.parse_args()
    a_params.model_path = '/mnt/c/TransCoder/model_from_' + src_lang + '_to_' + tgt_lang + '.pth'
    a_params.BPE_path = '/mnt/c/TransCoder/data/BPE_with_comments_codes'
    a_params.beam_size = 1
    a_params.src_lang = src_lang
    a_params.tgt_lang = tgt_lang
    return a_params


if __name__ == '__main__':

    # generate parser / parse parameters
    parser = get_parser()
    params = parser.parse_args()

    # read the files
    java_file = read_file(params.java_path)
    python_file = read_file(params.python_path)

    # make the test data readable for humans
    java_file_readable = make_java_readable(java_file)
    python_file_readable = make_python_readable(python_file)

    # translate all
    java_file_translated = translate_lines(True, java_file_readable)
    python_file_translated = translate_lines(False, python_file_readable)

    print(java_file[15][1])