# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( num , divisor ) :
    if ( divisor == 0 ) :
        return False
    if ( divisor < 0 ) :
        divisor = - divisor
    if ( num < 0 ) :
        num = - num
    i = 1
    product = 0
    while ( product <= num ) :
        product = divisor * i
        i += 1
    return num - ( product - divisor )


#
def f_filled ( num , divisor ) :
    if divisor == 0 :
        print ( "Error: divisor " + "can't be zero \n" )
        return - 1
    if divisor < 0 :
        divisor = - divisor
    if num < 0 :
        num = - num
    i = 1
    product = 0
    while product <= num :
        product = divisor * i
        i += 1
    return num - ( product - divisor )

if __name__ == '__main__':
    param = [
    (34,55,),
    (63,22,),
    (15,26,),
    (56,58,),
    (63,94,),
    (28,45,),
    (54,97,),
    (2,58,),
    (94,91,),
    (82,40,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))