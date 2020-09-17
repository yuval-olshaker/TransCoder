# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
import math

def f_gold ( num ) :
    if ( num < 0 ) :
        return False
    c = ( - 2 * num )
    b , a = 1 , 1
    d = ( b * b ) - ( 4 * a * c )
    if ( d < 0 ) :
        return False
    root1 = ( - b + math.sqrt ( d ) ) / ( 2 * a )
    root2 = ( - b - math.sqrt ( d ) ) / ( 2 * a )
    if ( root1 > 0 and math.floor ( root1 ) == root1 ) :
        return True
    if ( root2 > 0 and math.floor ( root2 ) == root2 ) :
        return True
    return False


#
def f_filled ( num ) :
    if num < 0 :
        return False
    c = ( - 2 * num )
    b , a = 1 , 1
    d = ( b ** 2 ) - ( 4 * a ** 2 )
    if d < 0 :
        return False
    root1 = ( - b + float ( math.sqrt ( d ) ) ) / ( 2 * a )
    root2 = ( - b - float ( math.sqrt ( d ) ) ) / ( 2 * a )
    if root1 and math.floor ( root1 ) == root1 :
        return True
    if root2 and math.floor ( root2 ) == root2 :
        return True
    return False

if __name__ == '__main__':
    param = [
    (1,),
    (3,),
    (6,),
    (10,),
    (55,),
    (48,),
    (63,),
    (72,),
    (16,),
    (85,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))