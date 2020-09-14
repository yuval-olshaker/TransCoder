# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( A , n ) :
    cnt = 0
    parent = [ None ] * ( n + 1 )
    vis = [ None ] * ( n + 1 )
    for i in range ( 0 , n + 1 ) :
        parent [ i ] = - 1
        vis [ i ] = 0
    for i in range ( 0 , n ) :
        j = i
        if ( parent [ j ] == - 1 ) :
            while ( parent [ j ] == - 1 ) :
                parent [ j ] = i
                j = ( j + A [ j ] + 1 ) % n
            if ( parent [ j ] == i ) :
                while ( vis [ j ] == 0 ) :
                    vis [ j ] = 1
                    cnt = cnt + 1
                    j = ( j + A [ j ] + 1 ) % n
    return cnt


#TOFILL

if __name__ == '__main__':
    param = [
    ([2, 6, 7, 8, 9, 12, 12, 14, 18, 24, 26, 38, 39, 45, 50, 52, 72, 80, 80, 83, 86],17,),
    ([14, 28, -52, 54, -88, -42, -34, -54, -72, 40, 90, 30, -64, -94, 38, 88, -6, -62, 52, 60, -96, -70, 60, -48, -36, 32, 34, -32, 4, -14, 70, 44, -14, -58, -24, -64, -76, -26, -60, 2, 64, -66, -74, 58, 90, -74, -88, 26],41,),
    ([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],9,),
    ([40, 27, 9, 90, 40, 47, 53, 43, 88, 89, 84, 4, 83, 47, 63, 77, 78, 1, 72, 22, 10, 29, 22],22,),
    ([-98, -94, -92, -90, -82, -80, -78, -68, -62, -60, -60, -44, -42, -40, -38, -36, -28, -28, -26, -24, -2, 4, 4, 8, 14, 16, 26, 36, 38, 42, 44, 44, 44, 46, 52, 62, 66, 66, 70, 84, 86, 88, 88],28,),
    ([1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0],10,),
    ([1, 5, 6, 7, 10, 10, 19, 29, 33, 35, 36, 43, 46, 46, 49, 52, 64, 65, 67, 67, 69, 74, 79, 83, 86, 91, 96, 97, 99],19,),
    ([28, 72, 68, 78, 6, -22, 36, -60, -50, -80, 44, 74, 52, -34, 76, -24, 82, 82, 72, -36, -38, -72, 14, -74, -98, 12, -88, -60, -14, -20, 24, -58, -70, 84, 94, -72, 96, -92, 42, -22],31,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],36,),
    ([87, 60],1,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))