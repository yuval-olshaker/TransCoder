# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( n ) :
    num = n ;
    dec_value = 0 ;
    base1 = 1 ;
    len1 = len ( num ) ;
    for i in range ( len1 - 1 , - 1 , - 1 ) :
        if ( num [ i ] == '1' ) :
            dec_value += base1 ;
        base1 = base1 * 2 ;
    return dec_value ;


#
def f_filled ( n ) :
    num = n
    dec_value = 0
    base = 1
    len ( num )
    for i in range ( len ( num ) - 1 , - 1 , - 1 ) :
        if num [ i ] == '1' :
            dec_value += base
        base = base * 2
    return dec_value

if __name__ == '__main__':
    param = [
    ('uEmIAgF',),
    ('753310137',),
    ('010011010',),
    ('kNi',),
    ('04562016903312',),
    ('000111101',),
    ('bk',),
    ('9',),
    ('1',),
    ('XxT nXLlk',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))