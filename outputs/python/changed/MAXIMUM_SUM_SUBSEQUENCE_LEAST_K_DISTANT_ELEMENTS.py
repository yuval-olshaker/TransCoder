# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr , N , k ) :
    MS = [ 0 for i in range ( N ) ]
    MS [ N - 1 ] = arr [ N - 1 ]
    for i in range ( N - 2 , - 1 , - 1 ) :
        if ( i + k + 1 >= N ) :
            MS [ i ] = max ( arr [ i ] , MS [ i + 1 ] )
        else :
            MS [ i ] = max ( arr [ i ] + MS [ i + k + 1 ] , MS [ i + 1 ] )
    return MS [ 0 ]


#
def f_filled ( arr , N , k ) :
    MS = [ arr [ i ] for i in range ( N ) ]
    for i in range ( N - 2 , - 1 , - 1 ) :
        if i + k + 1 >= N :
            MS [ i ] = max ( arr [ i ] , MS [ i + 1 ] )
        else :
            MS [ i ] = max ( arr [ i ] + MS [ i + k + 1 ] , MS [ i + 1 ] )
    return MS [ 0 ]

if __name__ == '__main__':
    param = [
    ([3, 5, 20, 21, 23, 26, 27, 31, 33, 38, 39, 41, 48, 48, 50, 51, 56, 57, 64, 68, 69, 70, 71, 74, 76, 86, 97],23,15,),
    ([32, 34, -40, 90, -82, -70, 30, 26, -76, -46, -84, 76, -76],9,10,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],22,34,),
    ([96, 15, 30, 25, 83],2,3,),
    ([-90, -82, -80, -76, -62, -58, -50, -48, -46, -38, -38, -38, -38, -38, -34, -32, -24, -22, -16, -16, -4, -2, 10, 10, 20, 26, 26, 32, 38, 38, 44, 44, 46, 48, 58, 62, 64, 66, 76, 78, 78, 82, 92, 96, 96, 98],27,30,),
    ([1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0],9,9,),
    ([1, 2, 9, 17, 24, 31, 31, 33, 56, 57, 61, 71, 73, 74, 76, 77, 79, 83, 86, 95, 99],12,10,),
    ([-12, 52, -44, 80, -66, 34, 42, -46, 8, 12, -22, -56, 74, -98, -44, 2, -24, -14, -54, -56, -26, -18, -72],13,19,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],13,13,),
    ([65, 1, 34, 38, 15, 6, 55, 21, 32, 90, 39, 25, 43, 48, 64, 66, 88, 70, 82, 75, 25, 56, 23, 27, 41, 33, 33, 55, 60, 90, 41, 58, 42, 53, 38, 90, 7, 15],37,33,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))