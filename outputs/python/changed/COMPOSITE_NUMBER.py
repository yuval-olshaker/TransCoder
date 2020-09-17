# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( n ) :
    if ( n <= 1 ) :
        return False
    if ( n <= 3 ) :
        return False
    if ( n % 2 == 0 or n % 3 == 0 ) :
        return True
    i = 5
    while ( i * i <= n ) :
        if ( n % i == 0 or n % ( i + 2 ) == 0 ) :
            return True
        i = i + 6
    return False


#
def f_filled ( n ) :
    if n <= 1 :
        print ( "False" )
    if n <= 3 :
        print ( "False" )
    if n % 2 == 0 or n % 3 == 0 :
        return True
    for i in range ( 5 , i * i <= n , 6 ) :
        if n % i == 0 or n % ( i + 2 ) == 0 :
            return True
    return False

if __name__ == '__main__':
    param = [
    (62,),
    (13,),
    (29,),
    (72,),
    (30,),
    (20,),
    (10,),
    (47,),
    (91,),
    (52,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))