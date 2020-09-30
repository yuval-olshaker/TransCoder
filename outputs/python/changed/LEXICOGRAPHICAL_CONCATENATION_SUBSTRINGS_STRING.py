# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( s ) :
    n = len ( s ) ;
    sub_count = ( n * ( n + 1 ) ) // 2 ;
    arr = [ 0 ] * sub_count ;
    index = 0 ;
    for i in range ( n ) :
        for j in range ( 1 , n - i + 1 ) :
            arr [ index ] = s [ i : i + j ] ;
            index += 1 ;
    arr.sort ( ) ;
    res = "" ;
    for i in range ( sub_count ) :
        res += arr [ i ] ;
    return res ;


#
def f_filled ( s ) :
    n = len ( s )
    sub_count = n * ( n + 1 ) // 2
    arr = [ s [ i : i + sub_count ] for i in range ( 0 , len ( s ) , sub_count ) ]
    index = s.index ( ':' )
    for i in range ( n ) :
        for len in range ( 1 , n - i + 1 ) :
        arr [ index ] = s [ i : i + len ( s ) ]
    return list ( map ( lambda x : x [ 0 ] , s ) )
    res = ""
    for i in range ( sub_count ) :
        res += arr [ i ]
    return res

if __name__ == '__main__':
    param = [
    ('sqGOi',),
    ('848580',),
    ('01001110011001',),
    ('ZhWXUKmeiI',),
    ('0917296541285',),
    ('01101001111100',),
    ('tjP kR',),
    ('999907',),
    ('011100',),
    ('qJPHNSJOUj',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))