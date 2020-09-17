# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( a , n ) :
    count = dict ( )
    for i in range ( n ) :
        if count.get ( a [ i ] ) :
            count [ a [ i ] ] += 1
        else :
            count [ a [ i ] ] = 1 ;
    next_missing = 1
    for i in range ( n ) :
        if count [ a [ i ] ] != 1 or a [ i ] > n or a [ i ] < 1 :
            count [ a [ i ] ] -= 1
            while count.get ( next_missing ) :
                next_missing += 1
            a [ i ] = next_missing
            count [ next_missing ] = 1


#
def f_filled ( a , n ) :
    count = { }
    for i in range ( n ) :
        if count.has_key ( a [ i ] ) :
            count [ a [ i ] ] = count [ a [ i ] ] + 1
        else :
            count [ a [ i ] ] = 1
    next_missing = 1
    for i in range ( n ) :
        if count.has_key ( a [ i ] ) and count [ a [ i ] ] != 1 or a [ i ] > n or a [ i ] < 1 :
            count [ a [ i ] ] = count [ a [ i ] ] - 1
            while count.has_key ( next_missing ) :
                next_missing += 1
            a [ i ] = next_missing
            count [ next_missing ] = 1

if __name__ == '__main__':
    param = [
    ([19],0,),
    ([-47, 72],1,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],18,),
    ([93, 3, 20, 59, 36, 19, 90, 67, 19, 20, 96, 71, 52, 33, 40, 39],9,),
    ([-98, -93, -91, -89, -63, -58, -52, -52, -46, -40, -25, -16, -10, -1, -1, 4, 12, 12, 13, 13, 16, 20, 29, 29, 31, 40, 44, 47, 48, 51, 52, 52, 59, 60, 61, 64, 66, 78, 85, 97],22,),
    ([0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0],12,),
    ([4, 6, 8, 17, 19, 21, 22, 24, 27, 27, 28, 30, 30, 30, 32, 33, 35, 37, 38, 44, 46, 46, 48, 49, 51, 53, 54, 59, 60, 61, 63, 64, 64, 69, 76, 85, 86, 87, 92, 93, 93, 95, 97, 97, 97, 98, 99, 99],26,),
    ([-75, -46, -42, -33, 4, 74, -76, 14, -68, 75, -14, 51, 94, 27, 55, 30, -83, 4],9,),
    ([0, 0, 0, 0, 0, 1, 1, 1, 1],5,),
    ([24, 13, 60, 7, 57, 36, 45, 20, 65, 8, 16, 14, 76, 87, 15, 92, 98, 66, 32, 87, 63, 86, 51, 25, 58],24,)
        ]
    filled_function_param = [
    ([19],0,),
    ([-47, 72],1,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],18,),
    ([93, 3, 20, 59, 36, 19, 90, 67, 19, 20, 96, 71, 52, 33, 40, 39],9,),
    ([-98, -93, -91, -89, -63, -58, -52, -52, -46, -40, -25, -16, -10, -1, -1, 4, 12, 12, 13, 13, 16, 20, 29, 29, 31, 40, 44, 47, 48, 51, 52, 52, 59, 60, 61, 64, 66, 78, 85, 97],22,),
    ([0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0],12,),
    ([4, 6, 8, 17, 19, 21, 22, 24, 27, 27, 28, 30, 30, 30, 32, 33, 35, 37, 38, 44, 46, 46, 48, 49, 51, 53, 54, 59, 60, 61, 63, 64, 64, 69, 76, 85, 86, 87, 92, 93, 93, 95, 97, 97, 97, 98, 99, 99],26,),
    ([-75, -46, -42, -33, 4, 74, -76, 14, -68, 75, -14, 51, 94, 27, 55, 30, -83, 4],9,),
    ([0, 0, 0, 0, 0, 1, 1, 1, 1],5,),
    ([24, 13, 60, 7, 57, 36, 45, 20, 65, 8, 16, 14, 76, 87, 15, 92, 98, 66, 32, 87, 63, 86, 51, 25, 58],24,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("%i, %i" % (n_success, len(param)))