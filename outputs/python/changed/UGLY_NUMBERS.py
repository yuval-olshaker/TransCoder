# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( n ) :
    ugly = [ 0 ] * n
    ugly [ 0 ] = 1
    i2 = i3 = i5 = 0
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    for l in range ( 1 , n ) :
        ugly [ l ] = min ( next_multiple_of_2 , next_multiple_of_3 , next_multiple_of_5 )
        if ugly [ l ] == next_multiple_of_2 :
            i2 += 1
            next_multiple_of_2 = ugly [ i2 ] * 2
        if ugly [ l ] == next_multiple_of_3 :
            i3 += 1
            next_multiple_of_3 = ugly [ i3 ] * 3
        if ugly [ l ] == next_multiple_of_5 :
            i5 += 1
            next_multiple_of_5 = ugly [ i5 ] * 5
    return ugly [ - 1 ]


#
def f_filled ( n ) :
    ugly = [ ]
    i2 , i3 , i5 = 0 , 0 , 0
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    next_ugly_no = 1
    ugly.append ( 1 )
    for i in range ( 1 , n ) :
        next_ugly_no = min ( next_multiple_of_2 , min ( next_multiple_of_3 , next_multiple_of_5 ) )
        ugly.append ( next_ugly_no )
        if next_ugly_no == next_multiple_of_2 :
            i2 = i2 + 1
            next_multiple_of_2 = ugly [ i2 ] * 2
        if next_ugly_no == next_multiple_of_3 :
            i3 = i3 + 1
            next_multiple_of_3 = ugly [ i3 ] * 3
        if next_ugly_no == next_multiple_of_5 :
            i5 = i5 + 1
            next_multiple_of_5 = ugly [ i5 ] * 5
    return next_ugly_no

if __name__ == '__main__':
    param = [
    (27,),
    (64,),
    (93,),
    (90,),
    (85,),
    (86,),
    (72,),
    (86,),
    (32,),
    (1,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))