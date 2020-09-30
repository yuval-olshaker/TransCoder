# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( a , b , mod ) :
    res = 0 ;
    a = a % mod ;
    while ( b ) :
        if ( b & 1 ) :
            res = ( res + a ) % mod ;
        a = ( 2 * a ) % mod ;
        b >>= 1 ;
    return res ;


#
def f_filled ( a , b , mod ) :
    res = 0
    a %= mod
    while b > 0 :
        if ( b & 1 ) : a = 5
            res = ( res + a ) % mod
        a = ( 2 * a ) % mod
        b >>= 1
    return res

if __name__ == '__main__':
    param = [
    (60,24,58,),
    (46,43,29,),
    (4,50,71,),
    (67,1,66,),
    (93,35,73,),
    (89,97,8,),
    (8,78,55,),
    (53,73,22,),
    (96,92,83,),
    (38,64,83,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))