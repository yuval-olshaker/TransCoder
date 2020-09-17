# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( n ) :
    count = 0 ;
    curr = 19 ;
    while ( True ) :
        sum = 0 ;
        x = curr ;
        while ( x > 0 ) :
            sum = sum + x % 10 ;
            x = int ( x / 10 ) ;
        if ( sum == 10 ) :
            count += 1 ;
        if ( count == n ) :
            return curr ;
        curr += 9 ;
    return - 1 ;


#
def f_filled ( n ) :
    count = 0
    for curr in range ( 19 , 0 , 9 ) :
        sum = 0
        for x in range ( curr , 0 , 10 ) :
            sum = sum + x % 10
        if sum == 10 :
            count += 1
        if count == n :
            return curr

if __name__ == '__main__':
    param = [
    (93,),
    (10,),
    (55,),
    (94,),
    (2,),
    (5,),
    (37,),
    (4,),
    (11,),
    (46,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))