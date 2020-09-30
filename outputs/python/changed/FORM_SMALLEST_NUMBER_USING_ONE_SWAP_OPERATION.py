# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( num ) :
    num = list ( num )
    n = len ( num )
    rightMin = [ 0 ] * n
    right = 0
    rightMin [ n - 1 ] = - 1 ;
    right = n - 1 ;
    for i in range ( n - 2 , 0 , - 1 ) :
        if num [ i ] > num [ right ] :
            rightMin [ i ] = right
        else :
            rightMin [ i ] = - 1
            right = i
    small = - 1
    for i in range ( 1 , n ) :
        if num [ i ] != '0' :
            if small == - 1 :
                if num [ i ] < num [ 0 ] :
                    small = i
            elif num [ i ] < num [ small ] :
                small = i
    if small != - 1 :
        num [ 0 ] , num [ small ] = num [ small ] , num [ 0 ]
    else :
        for i in range ( 1 , n ) :
            if rightMin [ i ] != - 1 :
                num [ i ] , num [ rightMin [ i ] ] = num [ rightMin [ i ] ] , num [ i ]
                break
    return ''.join ( num )


#
def f_filled ( str ) :
    num = args [ 0 ]
    n = len ( args )
    right_min = [ n for n in range ( n ) if n > 0 ]
    right_min [ n - 1 ] = - 1
    right = n - 1
    for i in range ( n - 2 , - 1 , - 1 ) :
        if num [ i ] > num [ right ] :
            rightMin [ i ] = right
        else :
            right_min [ i ] = - 1
            right = i
    small = - 1
    for i in range ( 1 , n ) :
        if small == - 1 :
            if num [ i ] < num [ 0 ] :
                small = i
        elif num [ i ] < num [ small ] :
            small = i
    if small != - 1 :
        temp = 0
        temp = num [ 0 ]
        num [ 0 ] = num [ small ]
        num [ small ] = temp
    else :
        for i in range ( 1 , n ) :
            if right_min [ i ] != - 1 :
                temp = 0
                temp = num [ i ]
                num [ i ] = num [ right_min [ i ] ]
                num [ right_min [ i ] ] = temp
                break
    return ( [ num for num in str.split ( '.' ) if num ] )

if __name__ == '__main__':
    param = [
    ('ncYltuhSxEfG',),
    ('26615541616459',),
    ('0101',),
    ('hK',),
    ('422162103899',),
    ('0010',),
    ('zfcSh',),
    ('92',),
    ('0',),
    ('v',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))