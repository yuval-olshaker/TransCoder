# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( n ) :
    res = list ( )
    res.append ( 0 )
    res.append ( 1 )
    i = 2
    while i < n + 1 :
        res.append ( max ( i , ( res [ int ( i / 2 ) ] + res [ int ( i / 3 ) ] + res [ int ( i / 4 ) ] + res [ int ( i / 5 ) ] ) ) )
        i = i + 1
    return res [ n ]


#
def f_filled ( n ) :
    res = [ 0 ] * ( n + 1 )
    res [ 0 ] = 0
    res [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        res [ i ] = max ( i , ( res [ i / 2 ] + res [ i / 3 ] + res [ i / 4 ] + res [ i / 5 ] ) )
    return res [ n ]

if __name__ == '__main__':
    param = [
    (3,),
    (19,),
    (39,),
    (89,),
    (96,),
    (68,),
    (48,),
    (5,),
    (3,),
    (4,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))