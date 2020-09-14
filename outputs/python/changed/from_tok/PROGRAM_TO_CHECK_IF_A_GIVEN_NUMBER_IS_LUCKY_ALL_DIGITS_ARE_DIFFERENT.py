# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
import math

def f_gold ( n ) :
    ar = [ 0 ] * 10
    while ( n > 0 ) :
        digit = math.floor ( n % 10 )
        if ( ar [ digit ] ) :
            return 0
        ar [ digit ] = 1
        n = n / 10
    return 1


#
def f_filled ( n ) :
    arr = [ ]
    for i in range ( 10 ) :
        arr.append ( False )
    while n > 0 :
        digit = n % 10
        if arr [ digit ] :
            return False
        arr.append ( True )
        n = n / 10
    return True

if __name__ == '__main__':
    param = [
    (474,),
    (9445,),
    (90,),
    (30,),
    (37453,),
    (27,),
    (2400,),
    (98,),
    (46,),
    (722,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))
