# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( n ) :
    return 1 if ( n == 1 or n == 0 ) else n * f_gold ( n - 1 ) ;


#TOFILL

if __name__ == '__main__':
    param = [
    (15,),
    (7,),
    (16,),
    (67,),
    (71,),
    (16,),
    (77,),
    (27,),
    (37,),
    (73,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))