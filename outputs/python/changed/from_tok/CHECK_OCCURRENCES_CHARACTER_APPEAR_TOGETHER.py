# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( s , c ) :
    oneSeen = False
    i = 0
    n = len ( s )
    while ( i < n ) :
        if ( s [ i ] == c ) :
            if ( oneSeen == True ) :
                return False
            while ( i < n and s [ i ] == c ) :
                i = i + 1
            oneSeen = True
        else :
            i = i + 1
    return True


#
def f_filled ( s , c ) :
    oneSeen = False
    i , n = 0 , len ( s )
    while i < n :
        if s [ i ] == c :
            if oneSeen == True :
                return False
            while i < n and s [ i ] == c :
                i += 1
            oneSeen = True
        else :
            i += 1
    return True

if __name__ == '__main__':
    param = [
    ('gILrzLimS','m',),
    ('307471222','2',),
    ('110','0',),
    ('GcAB','v',),
    ('113','3',),
    ('011110010','0',),
    ('wcwob','w',),
    ('74571582216153','1',),
    ('100000011','0',),
    ('ryPErkzY','q',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))