# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
import sys

def f_gold ( str1 ) :
    n = len ( str1 ) ;
    C = [ 0 ] * ( n + 1 ) ;
    P = [ [ False for x in range ( n + 1 ) ] for y in range ( n + 1 ) ] ;
    for i in range ( n ) :
        P [ i ] [ i ] = True ;
    for L in range ( 2 , n + 1 ) :
        for i in range ( n - L + 1 ) :
            j = i + L - 1 ;
            if ( L == 2 ) :
                P [ i ] [ j ] = ( str1 [ i ] == str1 [ j ] ) ;
            else :
                P [ i ] [ j ] = ( ( str1 [ i ] == str1 [ j ] ) and P [ i + 1 ] [ j - 1 ] ) ;
    for i in range ( n ) :
        if ( P [ 0 ] [ i ] == True ) :
            C [ i ] = 0 ;
        else :
            C [ i ] = sys.maxsize ;
            for j in range ( i ) :
                if ( P [ j + 1 ] [ i ] == True and 1 + C [ j ] < C [ i ] ) :
                    C [ i ] = 1 + C [ j ] ;
    return C [ n - 1 ] ;


#
def f_filled ( str ) :
    n = len ( str )
    C = [ [ ] for i in range ( n ) ]
    P = [ [ ] for i in range ( n ) ]
    i , j , k , L = 0 , 0 , 0 , 0
    for i in range ( n ) :
        P [ i ] [ i ] = True
    for L in range ( 2 , n + 1 ) :
        for i in range ( n - L + 1 ) :
            j = i + L - 1
            if L == 2 :
                P [ i ] [ j ] = ( str [ i ] == str [ j ] )
            else :
                P [ i ] [ j ] = ( str [ i ] == str [ j ] ) and P [ i + 1 ] [ j - 1 ]
    for i in range ( n ) :
        if P [ 0 ] [ i ] == True :
            C [ i ] = 0
        else :
            C [ i ] = int ( P [ i ] [ j ] )
            for j in range ( i ) :
                if P [ j + 1 ] [ i ] == True and 1 + C [ j ] < C [ i ] :
                    C [ i ] = 1 + C [ j ]
    return C [ n - 1 ]

if __name__ == '__main__':
    param = [
    ('YYGWgYrovdsh',),
    ('56109778',),
    ('101',),
    ('RxM',),
    ('187546405',),
    ('0110010',),
    ('wVODAmgvI',),
    ('56719',),
    ('10100011001100',),
    ('Wtpai',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))