# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( N ) :
    length = len ( N )
    l = int ( ( length ) / 2 )
    count = 0
    for i in range ( l + 1 ) :
        s = N [ 0 : 0 + i ]
        l1 = len ( s )
        t = N [ i : l1 + i ]
        try :
            if s [ 0 ] == '0' or t [ 0 ] == '0' :
                continue
        except :
            continue
        if s == t :
            count += 1
    return count


#
def f_filled ( N ) :
    len ( N )
    l = len ( N ) / 2
    count = 0
    for i in range ( 1 , l ) :
        s = N [ : i ]
        l1 = len ( s )
        t = N [ i : l1 + i ]
        if s [ 0 ] == '0' or t [ 0 ] == '0' :
            continue
        if s.lower ( ) == t.lower ( ) :
            count += 1
    return count

if __name__ == '__main__':
    param = [
    ('ZCoQhuM',),
    ('2674377254',),
    ('11',),
    ('LbuGlvRyWAPBpo',),
    ('26382426486138',),
    ('111010111010',),
    ('hUInqJXNdbfP',),
    ('5191',),
    ('1110101101',),
    ('2202200',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))