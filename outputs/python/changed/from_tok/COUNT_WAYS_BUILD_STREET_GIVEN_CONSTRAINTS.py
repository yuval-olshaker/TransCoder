# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( n ) :
    dp = [ [ 0 ] * ( n + 1 ) for i in range ( 2 ) ]
    dp [ 0 ] [ 1 ] = 1
    dp [ 1 ] [ 1 ] = 2
    for i in range ( 2 , n + 1 ) :
        dp [ 0 ] [ i ] = dp [ 0 ] [ i - 1 ] + dp [ 1 ] [ i - 1 ]
        dp [ 1 ] [ i ] = ( dp [ 0 ] [ i - 1 ] * 2 + dp [ 1 ] [ i - 1 ] )
    return dp [ 0 ] [ n ] + dp [ 1 ] [ n ]


#
def f_filled ( n ) :
    dp = [ [ 0 ] * n + [ 1 ] * n + [ 2 ] * n + [ 3 ] * n + [ 4 ] * n + [ 5 ] * n + [ 6 ] * n + [ 7 ] * n + [ 8 ] * n + [ 9 ] * n + [ 10 ] * n + [ 11 ] * n + [ 12 ] * n + [ 13 ] * n + [ 14 ] * n + [ 15 ] * n + [ 16 ] * n + [ 17 ] * n + [ 18 ] * n + [ 19 ] * n + [ 20 ] * n + [ 21 ] * n + [ 22 ] * n + [ 23 ] * n + [ 24 ] * n + [ 25 ] * n + [ 26 ] * n + [ 27 ] * n + [ 28 ] * n + [ 29 ] * n + [ 30 ] * n + [ 31 ] * n + [ 32 ] * n + [ 33 ] * n + [ 34 ] * n + [ 35 ] * n + [ 36 ] * n + [ 37 ] * n + [ 38 ] * n + [ 39 ] * n + [ 40 ] * n + [ 41 ] * n + [ 42 ] * n + [ 39 ] * n + [ 42 ] * n + [ 39 ] * n + [ 40 ] * n + [ 41 ] * n + [ 42 ] * n + [ 39 ] * n + [ 41 ] * n + [ 42 ] * n + [ 39 ] * n + [ 41 ] * n + [ 42 ] * n + [ 39 ] * n + [ 39 ] * n + [ 41 ] * n + [ 42 ] * n + [ 39 ] * n + [ 39 ] * n + [ 39 ] * n + [ 39 ] * n + [ 39 ] * n + [ 39 ] * n + [ 39 ] * n + [ 39 ] * n + [ 39 ] * n + [ 39 ] * n + [ 39 ] * n + [

if __name__ == '__main__':
    param = [
    (68,),
    (91,),
    (99,),
    (79,),
    (61,),
    (48,),
    (89,),
    (20,),
    (83,),
    (1,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))