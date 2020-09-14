# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( str ) :
    n = len ( str )
    for i in range ( n ) :
        if ( str [ i ] != 'a' ) :
            break
    if ( i * 2 != n ) :
        return False
    for j in range ( i , n ) :
        if ( str [ j ] != 'b' ) :
            return False
    return True


#
def f_filled ( s ) :
    l = len ( s )
    if l % 2 == 1 :
        return False
    i = 0
    j = l - 1
    while i < j :
        if s [ i ] != 'a' or s [ j ] != 'b' :
            return False
        i += 1
        j -= 1
    return True

if __name__ == '__main__':
    param = [
    ('ba',),
    ('aabb',),
    ('abab',),
    ('aaabb',),
    ('aabbb',),
    ('abaabbaa',),
    ('abaababb',),
    ('bbaa',),
    ('11001000',),
    ('ZWXv te',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))