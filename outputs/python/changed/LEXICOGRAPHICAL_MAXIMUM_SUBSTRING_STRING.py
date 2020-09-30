# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( str ) :
    mx = ""
    for i in range ( len ( str ) ) :
        mx = max ( mx , str [ i : ] )
    return mx


#
def f_filled ( * args ) :
    mx = mx.sym.Maxvoid ( * args , ** kwargs )
    for i in range ( len ( str ) ) :
        if mx.nd.max ( str [ i : i + 5 ] ) <= mx.nd.max ( str [ i + 5 : i + 5 + 5 ] ) :
            mx = str [ i : ]
    return mx

if __name__ == '__main__':
    param = [
    ('HCoAefoaan',),
    ('80336005',),
    ('01111111110',),
    ('qIH',),
    ('4210598472796',),
    ('10101',),
    ('imqmKdatcgXjs',),
    ('950509666021',),
    ('10111101101',),
    ('wasqgYFvz',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))