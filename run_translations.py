# this scripts will run the translation on the test examples so we will be able to test the limitation
# one of the important things is to organize the output so we will be able to go over it
import argparse
import preprocessing.src.code_tokenizer as code_tokenizer
import translate
import html_templates
from datetime import datetime

SEPARATOR = '|'
LONG_CODES = ['FINDING_THE_MAXIMUM_SQUARE_SUB_MATRIX_WITH_ALL_EQUAL_ELEMENTS', 'WILDCARD_CHARACTER_MATCHING']
LINE_SEPARATOR = '\n\n'

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
    name = line[:index - 1]  # cuts the space before the |
    code = line[index + 2:-1]  # cut the space after the |. cut \n in the end
    return name, code


# read the data from files
def read_file(file_path):
    with open(file_path) as file:
        lines = file.readlines()
    return list(map(split_line, lines))


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


# return the whole column of code by language and origin or translated
# by the way change the code to html representation
def get_code_from_corpus(file_translated, column, is_html=True):
    if is_html:
        return list(map(lambda line: line[column].replace('\n', '<br>'), file_translated))
    else:
        return list(map(lambda line: line[column], file_translated))


# create the html code
def create_html(lang, origin, translated):
    html_string = html_templates.OPENING.replace('LANGUAGE', lang)
    for i in range(len(combined[0])):
        html_string += html_templates.CODE_TITLE.replace('ENTER_FUNCTION_NAME', combined[0][i])
        html_string += html_templates.CODE.replace('ORIGIN_CODE', combined[origin][i]).replace('TRANSLATED_CODE',
                                                                                               combined[translated][i])
    html_string += html_templates.ENDING
    return html_string

# creates the files for evaluation
def print_for_evaluation(path, ind):
    with open(path, 'w') as out_file:
        for i in range(len(combined_txt[0])):
            out_file.write(combined_txt[0][i] + LINE_SEPARATOR)
            out_file.write(combined_txt[ind][i] + LINE_SEPARATOR)

def print_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)


if __name__ == '__main__':
    print_time()

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

    # combine translation and original
    combined = [get_code_from_corpus(java_file_translated, 0), get_code_from_corpus(java_file_translated, 2),
                get_code_from_corpus(python_file_translated, 3),
                get_code_from_corpus(python_file_translated, 2), get_code_from_corpus(java_file_translated, 3)]


    # create the html string
    java_string = create_html('java', 1, 2)
    python_string = create_html('python', 3, 4)

    # print to html
    with open('/mnt/c/TransCoder/outputs/test_java_web.html', 'w') as html_file:
        html_file.write(java_string)
    with open('/mnt/c/TransCoder/outputs/test_python_web.html', 'w') as html_file:
        html_file.write(python_string)

    # print the function - for evaluation
    combined_txt = [get_code_from_corpus(java_file_translated, 0, is_html=False),
                    get_code_from_corpus(java_file_translated, 2, is_html=False),
                    get_code_from_corpus(python_file_translated, 3, is_html=False),
                    get_code_from_corpus(python_file_translated, 2, is_html=False),
                    get_code_from_corpus(java_file_translated, 3, is_html=False)]

    print_for_evaluation('/mnt/c/TransCoder/outputs/origin_java.java', 1)
    print_for_evaluation('/mnt/c/TransCoder/outputs/translated_java.java', 2)
    print_for_evaluation('/mnt/c/TransCoder/outputs/origin_python.java', 3)
    print_for_evaluation('/mnt/c/TransCoder/outputs/translated_python.java', 4)

    print_time()
