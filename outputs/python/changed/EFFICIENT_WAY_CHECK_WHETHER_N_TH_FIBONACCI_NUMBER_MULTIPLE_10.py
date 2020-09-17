# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( n ) :
    return ( n % 15 == 0 )


#
def f_filled ( n ) :
    if n % 15 == 0 :
        return True
    return False

if __name__ == '__main__':
    param = [
    (30,),
    (-30,),
    (60,),
    (90,),
    (99,),
    (32,),
    (21,),
    (65,),
    (21,),
    (99,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))