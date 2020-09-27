# this scripts will run the translation on the test examples so we will be able to test the limitation
# one of the important things is to organize the output so we will be able to go over it
import argparse
import translate
import html_templates
from tqdm import tqdm

from create_readable_corpus import get_origin_codes_from_test_files, get_origin_codes_from_tok_files
from slicing_integration.java_integrator import JavaIntegrator
from slicing_integration.python_slicer import PythonSlicer
from utils import print_time

LONG_CODES = ['FINDING_THE_MAXIMUM_SQUARE_SUB_MATRIX_WITH_ALL_EQUAL_ELEMENTS', 'WILDCARD_CHARACTER_MATCHING']
LINE_SEPARATOR = '\n\n'
END_OF_FUNCTION = '|||'

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


# translate with the model from facebook
def translate_lines(is_from_java, file_readable, sliced = False):
    t_params = create_params('java', 'python') if is_from_java else create_params('python', 'java')
    translator = translate.Translator(t_params)
    if not sliced:
        return list(map(lambda line: (line[0], line[1],
                                      translator.translate(line[1], lang1=t_params.src_lang, lang2=t_params.tgt_lang,
                                                           beam_size=t_params.beam_size)[0]),
                        tqdm(file_readable)))
    return list(map(lambda line: (line[0], line[1],
                                  list(map(lambda sliced: (sliced[0], translator.translate(sliced[1], lang1=t_params.src_lang, lang2=t_params.tgt_lang,
                                                       beam_size=t_params.beam_size)[0]), line[2]))),
                    tqdm(file_readable)))


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
            # functions must to end with \n. sometimes they do not.
            func = combined_txt[ind][i]
            func = func if func[-1] == '\n' else func + '\n'
            out_file.write(func + END_OF_FUNCTION + LINE_SEPARATOR)


# returns the tests names from corpus
def get_tests(file_readable):
    return list( map( lambda line: line[0], file_readable))

# returns only the tests that are in both
def cut_unique(file_readable, tests_in_both):
    return list(filter( lambda line: line[0] in tests_in_both, file_readable))

# returns the corpora with only the tests that we have in both languages - so we have the source code of them both
def combine_tests_of_both_languages(java_file_readable, python_file_readable):
    java_tests = get_tests(java_file_readable)
    python_tests = get_tests(python_file_readable)
    tests_in_both = list(set(java_tests).intersection(python_tests))
    return cut_unique(java_file_readable, tests_in_both), cut_unique(python_file_readable, tests_in_both)

# add the origin code from tests that are not in the tok file
def combine_origin_from_both_sources(file_readable, file_readable_test):
    titles = list(map(lambda line: line[0], file_readable))
    for i in range(len(file_readable_test)):
        if file_readable_test[i][0] not in titles:
            file_readable.append(file_readable_test[i])
    return file_readable

if __name__ == '__main__':
    print_time('start')

    # generate parser / parse parameters
    parser = get_parser()
    params = parser.parse_args()

    java_file_readable, python_file_readable = get_origin_codes_from_tok_files(params.java_path, params.python_path)

    # read the data from the tests they generated
    java_file_readable_test = get_origin_codes_from_test_files('java', '//', 5)
    python_file_readable_test = get_origin_codes_from_test_files('python', '#', 3)

    # add the data from the tests they generated
    java_file_readable = combine_origin_from_both_sources(java_file_readable, java_file_readable_test)
    python_file_readable = combine_origin_from_both_sources(python_file_readable, python_file_readable_test)
    java_file_readable, python_file_readable = combine_tests_of_both_languages(java_file_readable, python_file_readable)

    # delete ';' from python files - it confuses the translator and not interesting at all (we can learn it)
    python_file_readable = list(map(lambda line: (line[0], line[1].replace(';\n', '\n')), python_file_readable))

    # translate all
    print_time('start translations')
    java_file_translated = translate_lines(True, java_file_readable)
    print_time('after java')

    use_slices = True
    if use_slices:
        # create slicer and integrator
        python_slicer = PythonSlicer()
        java_integrator = JavaIntegrator()

        # use them
        python_file_sliced = python_slicer.slice_corpus_trivial(python_file_readable)
        python_sliced_translated = translate_lines(False, python_file_sliced, True)
        python_file_translated = java_integrator.integrate_corpus_trivial(python_sliced_translated)
    else:
        python_file_translated = translate_lines(False, python_file_readable)

    print_time('finish translations')
    # combine translation and original
    combined = [get_code_from_corpus(java_file_translated, 0), get_code_from_corpus(java_file_translated, 1),
                get_code_from_corpus(python_file_translated, 2),
                get_code_from_corpus(python_file_translated, 1), get_code_from_corpus(java_file_translated, 2)]


    # create the html string
    java_string = create_html('java', 1, 2)
    python_string = create_html('python', 3, 4)

    out_dir_path = '/mnt/c/TransCoder/outputs/'
    # print to html
    with open(out_dir_path + 'test_java_web.html', 'w') as html_file:
        html_file.write(java_string)
    with open(out_dir_path + 'test_python_web.html', 'w') as html_file:
        html_file.write(python_string)

    # print the function - for evaluation
    combined_txt = [get_code_from_corpus(java_file_translated, 0, is_html=False),
                    get_code_from_corpus(java_file_translated, 1, is_html=False),
                    get_code_from_corpus(python_file_translated, 2, is_html=False),
                    get_code_from_corpus(python_file_translated, 1, is_html=False),
                    get_code_from_corpus(java_file_translated, 2, is_html=False)]

    print_for_evaluation(out_dir_path + 'origin_java.java', 1)
    print_for_evaluation(out_dir_path + 'translated_java.java', 2)
    print_for_evaluation(out_dir_path + 'origin_python.py', 3)
    print_for_evaluation(out_dir_path + 'translated_python.py', 4)

    print_time('end')
