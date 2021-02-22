defaults_dict = {'ints': 'inT', 'floats': 'floaT', 'type': 'typE', 'var': 'vaR', 'str': 'stR', 'func': 'cfunC',
                 'char': 'chaR'}


def remove_static(line):
    return line[1:] if line[0] == 'static' or line[0] == 'extern' else line

def check_excahnge(ex_dic, key, value): # the ref is the key and trans is the value
    if key in ex_dic.keys():
        if value == ex_dic[key]:
            return 1, ex_dic
        return 0, ex_dic
    if value in ex_dic.values():
        return 0, ex_dic
    ex_dic[key] = value
    return 1, ex_dic



def get_key_value(ref_word):
    for key, value in defaults_dict.items():
        if value in ref_word:
            return key, ref_word.replace(value, '')
    return None, None

def check_same_word_exc(key_or_value, dicti):
    if key_or_value in dicti.keys() or key_or_value in dicti.values():
        return False

    return True


def complex_check(ref_line, translated_line):
    split_ref = ref_line.split()
    split_trans = translated_line.split()

    split_ref = remove_static(split_ref)
    split_trans = remove_static(split_trans)

    if len(split_ref) != len(split_trans):
        return False

    dict_ex = {'ints': {}, 'floats': {}, 'type': {}, 'var': {}, 'str': {}, 'func': {}, 'char': {}}
    dict_used = {'ints': [], 'floats': [], 'type': [], 'var': [], 'str': [], 'func': [], 'char': []}

    for i, ref_word in enumerate(split_ref):
        trans_word = split_trans[i]
        if ref_word == trans_word: # if same word we check that we did not exchange it
                                    # and we add it to "used" so it wont get exchanged
            key, value = get_key_value(ref_word)
            if key is None:
                continue
            dict_used[key].append(value)
            if check_same_word_exc(value, dict_ex[key]):
                continue
            else:
                return False

        key_ref, value_ref = get_key_value(ref_word)
        if (key_ref is None) or (value_ref in dict_used[key_ref]): # no key, or already used as equal
            return False
        key_trans, value_trans = get_key_value(trans_word)
        # no key, or already used as equal, or different key
        if (key_trans is None) or (value_trans in dict_used[key_trans]) or (not key_ref == key_trans):
            return False

        key = key_ref

        check, dict_ex[key] = check_excahnge(dict_ex[key], value_ref, value_trans)
        if check == 0:
            return False

    return True

if __name__ == "__main__":
    a = 'int ifunC ( typE1 , typE0 ) char * typE1 ; int typE0 ; { if ( ( typE1 = = vaR0 ) || ( typE1 = = vaR1 ) ) { if ( typE2 ) { vaR3 ( vaR2 , typE1 ) ; } return ( inT4 ) ; } return ( inT2 ) ; }'
    b = 'int ifunC ( typE1 , typE0 ) char * typE1 ; int typE0 ; { if ( ( typE1 = = vaR0 ) || ( typE1 = = vaR1 ) ) { if ( typE0 ) { vaR2 ( vaR3 , typE1 ) ; } return ( inT2 ) ; } return ( inT4 ) ; }'
    print(complex_check(a,b))