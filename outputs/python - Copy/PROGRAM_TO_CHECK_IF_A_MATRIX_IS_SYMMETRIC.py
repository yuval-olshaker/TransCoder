# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( mat , N ) :
    for i in range ( N ) :
        for j in range ( N ) :
            if ( mat [ i ] [ j ] != mat [ j ] [ i ] ) :
                return False
    return True


#TOFILL

if __name__ == '__main__':
    param = [
    ([[29]],0,),
    ([[ 1, 3, 5 ], [ 3, 2, 4 ], [ 5, 4, 1 ]], 3,),
    ([[ 1, 2, 5 ], [ 3, 2, 4 ], [ 5, 4, 1 ]], 3,),
    ([[37, 56, 39, 95, 78, 69, 89, 45, 66, 99, 20, 10, 6, 33, 78, 26, 86, 61, 78, 36, 62, 23, 80, 89, 83], [42, 75, 30, 64, 25, 95, 17, 90, 6, 11, 1, 77, 16, 75, 86, 96, 67, 27, 80, 27, 99, 2, 82, 48, 25], [36, 83, 89, 85, 38, 40, 12, 29, 71, 29, 96, 75, 37, 79, 90, 66, 62, 29, 68, 98, 99, 74, 98, 88, 94], [69, 5, 52, 10, 35, 63, 75, 55, 17, 45, 65, 56, 70, 52, 61, 94, 61, 35, 13, 51, 1, 23, 77, 34, 80], [64, 11, 91, 93, 65, 22, 41, 25, 7, 85, 26, 82, 97, 51, 24, 10, 13, 95, 18, 11, 58, 32, 21, 41, 60], [90, 46, 56, 8, 17, 36, 86, 73, 5, 56, 59, 14, 45, 75, 51, 58, 95, 71, 39, 85, 57, 29, 75, 13, 44], [40, 43, 89, 50, 56, 62, 55, 30, 28, 68, 41, 84, 12, 77, 90, 38, 53, 23, 42, 84, 67, 11, 94, 10, 77], [74, 31, 44, 37, 25, 93, 21, 15, 11, 98, 75, 45, 8, 98, 26, 21, 52, 50, 24, 96, 82, 26, 41, 51, 16], [41, 52, 57, 84, 51, 59, 79, 68, 40, 16, 76, 35, 26, 73, 80, 59, 79, 84, 3, 5, 40, 55, 77, 48, 93], [71, 53, 72, 27, 73, 96, 36, 36, 39, 75, 57, 36, 7, 21, 15, 46, 88, 47, 59, 61, 41, 54, 23, 73, 12], [8, 22, 50, 34, 84, 96, 13, 20, 8, 70, 99, 97, 25, 14, 97, 59, 51, 53, 16, 67, 38, 74, 45, 97, 16], [95, 25, 78, 52, 46, 8, 73, 56, 13, 78, 63, 15, 53, 55, 5, 39, 13, 67, 97, 19, 31, 96, 53, 66, 80], [5, 30, 49, 58, 18, 36, 38, 50, 49, 28, 56, 33, 2, 2, 32, 12, 39, 51, 6, 15, 96, 47, 45, 45, 15], [10, 79, 97, 99, 12, 35, 4, 10, 84, 43, 31, 31, 31, 20, 73, 77, 37, 59, 24, 89, 59, 94, 88, 73, 29], [74, 78, 86, 45, 12, 8, 60, 67, 26, 20, 81, 31, 77, 42, 50, 32, 6, 32, 32, 43, 32, 1, 11, 12, 21], [21, 10, 9, 12, 32, 85, 18, 50, 39, 69, 5, 71, 56, 78, 22, 97, 99, 93, 79, 31, 92, 18, 8, 33, 15], [7, 35, 36, 40, 77, 41, 11, 87, 51, 23, 46, 4, 42, 34, 46, 7, 37, 20, 99, 29, 97, 36, 71, 56, 96], [5, 57, 15, 64, 45, 54, 2, 56, 40, 1, 16, 6, 72, 80, 47, 76, 6, 48, 2, 75, 61, 11, 10, 98, 75], [98, 75, 99, 62, 8, 10, 96, 52, 95, 4, 3, 45, 30, 75, 47, 34, 67, 57, 21, 41, 75, 75, 88, 53, 99], [40, 77, 89, 69, 74, 98, 68, 89, 99, 22, 23, 24, 74, 67, 11, 60, 34, 16, 26, 43, 19, 28, 48, 52, 85], [81, 50, 42, 81, 54, 72, 87, 27, 47, 26, 83, 34, 15, 4, 1, 92, 40, 74, 92, 61, 36, 18, 3, 43, 46], [80, 28, 65, 52, 79, 12, 96, 25, 80, 36, 21, 10, 76, 78, 63, 51, 27, 18, 53, 55, 98, 75, 79, 5, 37], [52, 98, 60, 25, 33, 97, 15, 1, 38, 45, 7, 12, 68, 26, 10, 72, 50, 25, 96, 64, 54, 43, 27, 16, 92], [61, 86, 67, 38, 64, 43, 82, 14, 64, 95, 63, 92, 69, 49, 72, 52, 82, 23, 32, 48, 12, 58, 24, 3, 86], [2, 88, 8, 1, 46, 4, 72, 89, 32, 16, 31, 5, 43, 13, 8, 11, 67, 33, 4, 22, 58, 60, 98, 99, 81]],21,),
    ([[32, 53, 61, 4, 94, 83, 17, 81, 12, 79, 93, 11, 91, 14, 15], [13, 34, 5, 70, 47, 93, 43, 97, 24, 44, 49, 93, 33, 2, 34], [94, 82, 63, 86, 67, 80, 10, 15, 76, 76, 39, 51, 15, 91, 20], [71, 90, 63, 91, 53, 14, 13, 78, 84, 44, 96, 39, 66, 80, 82], [60, 33, 64, 97, 47, 93, 89, 32, 10, 64, 77, 3, 60, 87, 26], [69, 81, 93, 32, 34, 95, 76, 38, 85, 22, 30, 53, 84, 86, 2], [71, 38, 57, 33, 49, 92, 28, 63, 54, 6, 62, 95, 36, 74, 19], [6, 34, 8, 6, 41, 89, 15, 22, 4, 73, 86, 56, 18, 24, 99], [67, 18, 89, 84, 39, 89, 61, 77, 78, 94, 44, 28, 30, 51, 33], [82, 64, 52, 28, 73, 14, 69, 99, 54, 49, 7, 44, 60, 1, 51], [99, 38, 66, 68, 74, 99, 59, 98, 62, 39, 63, 32, 21, 85, 23], [15, 1, 29, 94, 19, 33, 88, 70, 10, 46, 47, 55, 18, 71, 10], [92, 59, 34, 42, 98, 91, 42, 67, 7, 15, 35, 53, 1, 14, 90], [22, 84, 62, 36, 99, 16, 63, 6, 22, 7, 95, 17, 80, 50, 59], [42, 40, 14, 73, 80, 53, 8, 91, 78, 59, 66, 88, 72, 71, 63]],13,),
    ([[93, 91, 59, 11, 73, 34, 33, 29, 78, 95, 52, 61, 39, 63, 91, 82, 75, 35, 18, 71, 19, 42, 64], [92, 7, 2, 46, 32, 22, 94, 78, 67, 73, 52, 15, 70, 89, 48, 40, 60, 4, 21, 67, 60, 67, 39], [94, 67, 26, 74, 69, 58, 14, 10, 9, 3, 75, 67, 48, 38, 39, 41, 43, 78, 67, 6, 46, 78, 16], [25, 44, 27, 86, 54, 56, 75, 43, 59, 83, 83, 80, 94, 72, 94, 56, 8, 51, 29, 14, 12, 13, 12], [78, 10, 44, 59, 8, 24, 37, 43, 89, 8, 64, 77, 67, 73, 40, 74, 46, 83, 92, 18, 82, 72, 8], [59, 36, 96, 21, 3, 88, 16, 83, 55, 22, 22, 77, 12, 60, 92, 72, 9, 84, 79, 68, 24, 48, 45], [6, 64, 87, 15, 30, 84, 27, 27, 98, 97, 58, 10, 73, 72, 78, 1, 74, 4, 59, 82, 94, 41, 90], [43, 14, 29, 73, 37, 22, 88, 99, 36, 95, 58, 15, 61, 7, 99, 91, 42, 98, 25, 64, 44, 6, 4], [66, 14, 4, 35, 77, 93, 34, 26, 56, 90, 68, 78, 75, 3, 87, 8, 44, 90, 78, 5, 58, 86, 78], [12, 67, 94, 20, 3, 33, 77, 18, 75, 26, 7, 90, 3, 1, 17, 12, 73, 81, 82, 23, 91, 2, 27], [55, 15, 44, 69, 95, 49, 63, 35, 19, 53, 92, 2, 52, 20, 59, 3, 8, 40, 30, 12, 49, 17, 66], [23, 39, 27, 57, 19, 44, 66, 32, 33, 43, 23, 14, 80, 57, 98, 57, 58, 62, 40, 44, 47, 84, 46], [53, 29, 49, 53, 9, 73, 25, 47, 81, 50, 71, 16, 37, 18, 39, 78, 56, 82, 8, 57, 89, 20, 57], [1, 88, 13, 75, 52, 97, 30, 81, 57, 5, 22, 51, 79, 74, 1, 46, 79, 42, 42, 93, 64, 21, 79], [99, 69, 19, 14, 15, 51, 83, 91, 16, 83, 53, 55, 23, 36, 18, 45, 88, 71, 89, 45, 7, 69, 88], [84, 85, 20, 74, 87, 46, 33, 15, 34, 79, 5, 9, 91, 64, 60, 28, 9, 50, 36, 9, 31, 45, 55], [78, 15, 41, 66, 63, 96, 27, 64, 60, 56, 71, 14, 60, 93, 40, 20, 51, 5, 82, 72, 50, 71, 88], [60, 86, 20, 27, 20, 6, 8, 79, 22, 35, 42, 77, 92, 20, 93, 69, 3, 27, 69, 60, 20, 23, 96], [12, 55, 49, 96, 80, 27, 65, 51, 76, 77, 72, 44, 29, 39, 16, 5, 43, 57, 97, 20, 36, 96, 48], [50, 2, 12, 39, 53, 63, 12, 34, 34, 12, 17, 6, 30, 86, 37, 87, 80, 26, 48, 40, 31, 46, 66], [67, 88, 91, 37, 17, 94, 68, 59, 82, 40, 27, 95, 12, 31, 28, 26, 13, 82, 17, 41, 32, 22, 99], [80, 50, 3, 22, 59, 95, 16, 66, 40, 56, 86, 56, 78, 14, 62, 69, 27, 47, 80, 68, 87, 74, 95], [17, 27, 51, 59, 59, 79, 24, 54, 99, 13, 14, 70, 70, 52, 96, 85, 21, 30, 54, 86, 19, 59, 47]],12,),
    ([[1, 88, 52, 21, 60, 48, 74, 12, 87, 76, 80, 55, 3, 66, 6, 22, 67, 73, 21, 37, 33, 1, 65, 71, 37, 40, 63, 52, 76, 32, 27, 42, 52], [29, 46, 66, 46, 83, 25, 99, 65, 57, 28, 18, 63, 18, 24, 51, 29, 19, 31, 95, 86, 29, 20, 66, 68, 46, 19, 7, 42, 16, 52, 33, 39, 43], [84, 46, 4, 15, 43, 30, 39, 43, 14, 70, 86, 18, 46, 79, 21, 76, 91, 61, 75, 95, 65, 25, 89, 81, 71, 32, 48, 89, 82, 35, 90, 76, 78], [8, 22, 76, 32, 46, 13, 33, 1, 92, 67, 80, 50, 32, 10, 1, 71, 47, 7, 62, 52, 68, 4, 57, 89, 5, 71, 55, 67, 57, 99, 75, 76, 39], [80, 43, 71, 85, 10, 82, 29, 26, 30, 65, 38, 15, 89, 19, 28, 97, 15, 78, 61, 38, 99, 32, 78, 77, 41, 85, 76, 15, 88, 84, 63, 1, 43], [14, 2, 8, 11, 20, 44, 59, 17, 12, 84, 74, 21, 67, 4, 88, 54, 27, 95, 74, 68, 76, 79, 90, 34, 1, 59, 52, 45, 18, 73, 50, 34, 54], [54, 52, 30, 4, 53, 24, 50, 45, 61, 90, 7, 45, 85, 78, 34, 10, 11, 45, 49, 40, 51, 71, 99, 28, 62, 15, 38, 49, 1, 50, 14, 13, 22], [57, 85, 41, 37, 82, 73, 95, 5, 31, 65, 86, 57, 15, 90, 29, 54, 41, 91, 34, 85, 76, 35, 55, 98, 33, 42, 87, 8, 83, 99, 91, 30, 84], [92, 74, 42, 25, 14, 65, 30, 13, 89, 12, 24, 70, 73, 38, 87, 52, 70, 35, 28, 5, 42, 84, 80, 20, 22, 51, 87, 76, 47, 97, 39, 28, 68], [47, 72, 21, 48, 50, 49, 76, 62, 35, 80, 72, 5, 76, 90, 37, 73, 41, 92, 40, 58, 72, 2, 50, 86, 94, 80, 48, 24, 91, 33, 70, 94, 42], [26, 78, 95, 16, 21, 2, 59, 8, 7, 90, 21, 18, 82, 1, 91, 8, 92, 2, 22, 20, 78, 35, 60, 31, 41, 67, 72, 90, 24, 15, 38, 79, 99], [38, 81, 95, 66, 5, 2, 2, 90, 38, 37, 10, 91, 72, 74, 99, 24, 24, 95, 4, 40, 14, 26, 12, 27, 6, 27, 14, 22, 49, 20, 3, 73, 80], [73, 49, 96, 98, 25, 27, 91, 2, 22, 66, 48, 53, 1, 54, 39, 10, 12, 37, 46, 17, 3, 85, 76, 59, 27, 15, 45, 41, 67, 5, 34, 63, 98], [85, 13, 89, 14, 82, 61, 3, 3, 45, 96, 18, 32, 96, 44, 93, 37, 99, 27, 40, 24, 56, 36, 99, 6, 71, 78, 17, 61, 27, 44, 70, 3, 39], [35, 66, 83, 87, 17, 9, 9, 35, 9, 12, 67, 85, 57, 92, 97, 98, 43, 22, 60, 30, 31, 80, 99, 65, 73, 65, 87, 37, 82, 4, 10, 27, 2], [55, 68, 40, 97, 8, 15, 61, 7, 94, 24, 20, 55, 5, 7, 2, 74, 77, 21, 3, 53, 14, 53, 80, 63, 54, 72, 24, 78, 50, 6, 88, 93, 26], [34, 44, 69, 98, 98, 77, 67, 5, 86, 85, 91, 88, 39, 53, 8, 68, 36, 70, 95, 69, 6, 2, 1, 62, 29, 87, 18, 3, 80, 31, 22, 8, 22], [77, 29, 80, 10, 46, 34, 56, 59, 33, 78, 96, 23, 15, 25, 26, 12, 64, 19, 49, 19, 96, 74, 91, 23, 56, 63, 52, 64, 18, 99, 50, 13, 66], [36, 22, 84, 7, 12, 79, 93, 8, 23, 13, 97, 5, 83, 7, 68, 9, 19, 89, 65, 68, 82, 71, 83, 52, 87, 28, 93, 6, 44, 27, 46, 4, 87], [30, 45, 58, 62, 54, 24, 96, 75, 30, 90, 80, 57, 53, 70, 89, 84, 10, 1, 44, 59, 11, 76, 20, 76, 60, 44, 16, 79, 62, 90, 56, 75, 3], [2, 44, 83, 96, 87, 44, 24, 13, 1, 39, 5, 13, 8, 51, 49, 49, 48, 40, 30, 44, 92, 93, 53, 36, 84, 69, 71, 30, 38, 7, 75, 75, 84], [33, 79, 68, 51, 10, 38, 40, 3, 24, 2, 23, 51, 59, 42, 19, 8, 26, 82, 44, 48, 73, 36, 9, 97, 11, 41, 62, 88, 24, 32, 33, 81, 90], [45, 33, 2, 66, 78, 21, 87, 22, 65, 32, 29, 69, 36, 25, 22, 69, 52, 67, 24, 97, 92, 47, 85, 80, 11, 6, 51, 83, 61, 82, 44, 10, 76], [33, 64, 15, 76, 50, 5, 1, 38, 98, 12, 30, 11, 73, 44, 46, 71, 81, 52, 63, 26, 27, 97, 39, 5, 73, 87, 94, 36, 1, 52, 8, 1, 74], [7, 38, 59, 60, 67, 7, 8, 34, 40, 42, 96, 32, 69, 91, 13, 55, 12, 74, 1, 85, 7, 10, 81, 37, 48, 65, 42, 13, 23, 57, 92, 19, 32], [10, 82, 8, 16, 35, 58, 81, 48, 48, 23, 26, 55, 23, 50, 23, 54, 56, 45, 71, 12, 22, 17, 77, 48, 78, 71, 50, 83, 59, 39, 71, 60, 91], [17, 34, 75, 9, 39, 67, 23, 40, 4, 57, 16, 59, 85, 25, 5, 1, 96, 20, 11, 97, 32, 83, 39, 45, 57, 82, 36, 42, 88, 96, 9, 24, 79], [47, 46, 86, 98, 59, 10, 2, 42, 7, 1, 9, 42, 26, 79, 57, 22, 87, 3, 11, 56, 86, 62, 40, 78, 16, 98, 5, 53, 72, 66, 11, 45, 62], [87, 65, 74, 6, 67, 83, 29, 79, 87, 49, 8, 89, 88, 52, 12, 1, 4, 94, 98, 60, 43, 97, 44, 30, 40, 13, 30, 19, 20, 38, 63, 68, 23], [89, 11, 31, 76, 41, 98, 57, 30, 80, 96, 82, 8, 95, 36, 77, 82, 62, 35, 27, 6, 64, 74, 37, 47, 44, 71, 80, 66, 43, 57, 47, 89, 90], [90, 18, 20, 92, 67, 57, 1, 74, 95, 84, 56, 8, 48, 58, 64, 71, 57, 51, 99, 40, 84, 3, 63, 11, 58, 76, 46, 12, 8, 45, 86, 84, 15], [49, 31, 46, 94, 40, 31, 20, 2, 6, 78, 26, 97, 87, 89, 37, 92, 99, 71, 59, 66, 64, 17, 91, 48, 66, 12, 80, 32, 18, 62, 16, 5, 24], [49, 75, 64, 46, 42, 88, 78, 1, 90, 26, 68, 90, 4, 96, 16, 80, 40, 84, 81, 49, 84, 96, 42, 11, 62, 93, 55, 27, 85, 29, 32, 41, 12]],22,),
    ([[97, 17, 59, 40, 18, 53, 65, 84, 85, 42, 38, 32, 22, 61, 89, 32, 31, 99, 58, 77, 80, 56, 83, 41, 15, 46, 97, 59, 65, 51, 13, 24, 87, 93, 16, 49, 32, 16, 43, 88, 53, 21, 33, 59, 60], [27, 29, 33, 50, 32, 46, 28, 51, 26, 48, 58, 47, 63, 47, 70, 19, 79, 81, 98, 65, 19, 67, 81, 46, 78, 75, 80, 54, 94, 91, 82, 87, 49, 27, 56, 44, 75, 77, 44, 23, 90, 42, 64, 34, 99], [43, 84, 88, 96, 26, 2, 13, 3, 12, 27, 14, 74, 38, 76, 40, 75, 50, 66, 95, 62, 10, 6, 55, 42, 61, 22, 47, 19, 74, 47, 91, 92, 10, 45, 60, 17, 79, 43, 12, 84, 64, 80, 47, 84, 50], [27, 22, 91, 13, 59, 69, 81, 98, 22, 94, 67, 71, 15, 71, 3, 29, 6, 49, 91, 65, 54, 34, 58, 8, 89, 15, 38, 11, 73, 27, 77, 76, 11, 58, 35, 44, 57, 87, 21, 28, 7, 77, 95, 35, 81], [88, 86, 74, 80, 6, 12, 1, 16, 98, 63, 58, 91, 5, 83, 11, 37, 63, 75, 8, 53, 16, 95, 11, 65, 47, 81, 49, 25, 55, 26, 34, 2, 16, 31, 22, 86, 32, 70, 2, 71, 11, 10, 16, 51, 1], [35, 39, 74, 59, 99, 77, 78, 76, 44, 3, 38, 75, 98, 25, 87, 72, 64, 27, 50, 4, 62, 88, 60, 63, 13, 31, 64, 14, 84, 86, 76, 67, 96, 5, 96, 76, 92, 91, 87, 68, 69, 45, 9, 9, 93], [57, 81, 83, 66, 96, 54, 15, 2, 78, 96, 49, 90, 12, 90, 36, 76, 97, 90, 87, 13, 37, 40, 92, 34, 54, 83, 89, 99, 85, 70, 16, 24, 51, 16, 94, 28, 74, 17, 84, 48, 24, 80, 20, 55, 26], [29, 22, 20, 96, 29, 87, 57, 98, 76, 83, 17, 86, 10, 82, 69, 1, 90, 89, 77, 39, 46, 12, 20, 6, 18, 2, 73, 33, 54, 1, 75, 22, 68, 21, 29, 20, 69, 51, 27, 97, 18, 22, 41, 37, 18], [21, 6, 28, 2, 79, 11, 11, 26, 91, 43, 87, 56, 8, 63, 46, 59, 84, 98, 26, 65, 63, 88, 53, 41, 93, 11, 8, 30, 79, 82, 25, 64, 60, 11, 48, 51, 73, 32, 12, 42, 23, 88, 83, 74, 82], [15, 94, 47, 98, 42, 39, 13, 42, 23, 45, 22, 60, 27, 52, 69, 11, 40, 6, 67, 32, 74, 40, 20, 18, 98, 82, 2, 13, 56, 46, 62, 77, 47, 59, 90, 64, 12, 12, 12, 23, 18, 24, 47, 91, 70], [40, 45, 67, 62, 58, 95, 96, 92, 54, 9, 34, 60, 27, 27, 60, 25, 83, 78, 40, 83, 76, 95, 36, 25, 58, 61, 52, 6, 14, 7, 93, 90, 34, 36, 51, 75, 76, 81, 87, 31, 82, 53, 61, 26, 87], [50, 8, 23, 75, 95, 19, 22, 41, 81, 49, 57, 91, 31, 17, 17, 98, 99, 11, 84, 60, 4, 58, 3, 72, 36, 43, 83, 20, 5, 90, 86, 55, 26, 50, 74, 88, 52, 96, 61, 89, 15, 53, 34, 16, 47], [64, 74, 70, 61, 41, 85, 45, 2, 49, 19, 38, 87, 17, 6, 54, 48, 44, 59, 34, 15, 91, 22, 35, 83, 2, 44, 20, 45, 62, 61, 97, 81, 56, 56, 2, 12, 82, 23, 19, 54, 69, 21, 60, 20, 80], [6, 59, 90, 96, 99, 23, 54, 18, 42, 85, 48, 13, 28, 14, 94, 37, 99, 47, 53, 41, 40, 22, 35, 77, 9, 80, 77, 18, 53, 73, 8, 19, 80, 75, 43, 92, 32, 19, 7, 24, 23, 7, 40, 79, 23], [79, 72, 73, 91, 22, 22, 20, 21, 14, 85, 22, 33, 78, 13, 86, 90, 85, 15, 75, 12, 6, 32, 24, 17, 98, 88, 25, 60, 63, 86, 23, 86, 84, 45, 76, 81, 53, 27, 65, 45, 56, 1, 37, 78, 43], [90, 67, 47, 22, 16, 72, 11, 25, 17, 50, 89, 84, 15, 7, 22, 32, 89, 15, 10, 5, 81, 6, 3, 31, 43, 72, 33, 23, 43, 12, 10, 33, 13, 48, 6, 24, 27, 92, 63, 99, 24, 55, 10, 20, 22], [45, 52, 19, 18, 80, 74, 48, 70, 47, 13, 8, 88, 84, 89, 5, 68, 90, 35, 15, 35, 75, 33, 40, 68, 60, 21, 67, 96, 35, 1, 18, 6, 19, 31, 48, 60, 56, 49, 8, 70, 87, 68, 12, 15, 51], [68, 10, 30, 46, 76, 42, 39, 8, 59, 61, 70, 81, 87, 50, 7, 97, 53, 7, 96, 93, 30, 77, 54, 38, 82, 30, 85, 30, 18, 62, 98, 29, 49, 45, 51, 20, 31, 47, 83, 13, 77, 45, 70, 57, 87], [28, 1, 55, 6, 63, 56, 56, 97, 48, 21, 77, 81, 95, 80, 48, 64, 45, 45, 17, 72, 42, 89, 64, 95, 92, 52, 40, 64, 8, 51, 66, 73, 50, 20, 68, 99, 60, 54, 64, 43, 32, 9, 30, 49, 1], [49, 96, 37, 62, 18, 86, 55, 83, 16, 85, 49, 64, 57, 39, 68, 15, 12, 80, 64, 93, 89, 77, 20, 34, 19, 75, 93, 92, 19, 82, 49, 29, 20, 28, 8, 40, 46, 56, 99, 69, 41, 89, 84, 71, 28], [25, 56, 58, 92, 77, 94, 72, 67, 80, 80, 87, 10, 6, 83, 38, 90, 18, 91, 20, 6, 81, 30, 16, 25, 51, 16, 70, 37, 64, 71, 60, 96, 55, 52, 56, 17, 27, 3, 92, 98, 29, 4, 27, 84, 76], [99, 74, 14, 56, 22, 24, 90, 11, 84, 72, 29, 73, 38, 70, 92, 90, 9, 45, 26, 89, 52, 6, 21, 60, 59, 21, 91, 11, 20, 17, 98, 51, 64, 55, 86, 16, 85, 77, 98, 54, 54, 56, 7, 96, 13], [96, 83, 88, 44, 40, 69, 28, 81, 40, 94, 62, 59, 50, 11, 15, 60, 10, 20, 30, 35, 99, 96, 59, 51, 58, 12, 46, 7, 64, 18, 28, 11, 98, 35, 76, 76, 15, 54, 40, 19, 40, 53, 10, 72, 22], [21, 20, 69, 1, 27, 36, 33, 90, 63, 14, 86, 32, 11, 93, 93, 74, 65, 49, 84, 94, 34, 61, 56, 95, 39, 50, 30, 14, 35, 25, 53, 56, 29, 40, 65, 53, 99, 64, 21, 81, 14, 10, 74, 1, 12], [79, 15, 42, 97, 70, 30, 28, 31, 17, 97, 85, 50, 51, 87, 67, 49, 92, 28, 81, 14, 80, 89, 3, 69, 70, 95, 68, 67, 60, 68, 99, 44, 74, 55, 69, 78, 34, 2, 79, 34, 4, 12, 13, 73, 4], [31, 44, 56, 6, 71, 62, 82, 94, 22, 78, 12, 48, 46, 72, 25, 42, 75, 55, 25, 80, 81, 54, 92, 68, 98, 26, 6, 52, 85, 64, 58, 57, 72, 68, 75, 34, 2, 83, 39, 67, 73, 95, 76, 12, 73], [39, 32, 69, 72, 32, 22, 88, 51, 91, 41, 50, 17, 45, 59, 44, 32, 48, 30, 28, 83, 18, 20, 74, 11, 60, 34, 39, 38, 17, 49, 87, 71, 6, 56, 24, 60, 72, 4, 81, 66, 22, 51, 51, 16, 85], [40, 8, 71, 64, 71, 4, 25, 59, 70, 82, 79, 85, 16, 55, 24, 11, 71, 42, 3, 41, 22, 26, 4, 16, 63, 17, 19, 79, 7, 66, 55, 45, 87, 72, 1, 17, 39, 8, 57, 85, 50, 55, 26, 95, 53], [33, 30, 94, 36, 21, 41, 37, 21, 29, 8, 52, 39, 69, 14, 85, 38, 15, 30, 71, 27, 72, 35, 41, 53, 61, 95, 45, 30, 91, 1, 33, 78, 7, 62, 22, 51, 69, 85, 55, 31, 54, 27, 44, 79, 87], [60, 53, 17, 94, 36, 66, 2, 97, 20, 10, 69, 58, 81, 47, 63, 39, 62, 82, 60, 73, 74, 32, 63, 39, 18, 24, 2, 16, 79, 51, 84, 54, 56, 62, 71, 82, 89, 77, 60, 75, 72, 91, 20, 64, 98], [68, 79, 77, 49, 86, 26, 52, 61, 9, 5, 30, 4, 31, 14, 25, 28, 15, 67, 95, 77, 9, 66, 23, 48, 33, 28, 63, 8, 36, 2, 24, 22, 79, 24, 69, 91, 97, 53, 85, 81, 58, 35, 55, 26, 46], [25, 85, 11, 24, 78, 24, 73, 2, 6, 25, 81, 3, 5, 32, 48, 55, 93, 36, 36, 25, 56, 28, 35, 13, 79, 60, 27, 75, 6, 56, 27, 42, 94, 97, 38, 55, 19, 86, 13, 68, 6, 29, 94, 89, 61], [15, 12, 21, 82, 25, 38, 69, 76, 49, 29, 62, 42, 22, 95, 48, 28, 23, 53, 16, 60, 40, 97, 39, 68, 6, 47, 11, 10, 31, 71, 14, 59, 6, 58, 18, 33, 30, 84, 92, 1, 57, 81, 59, 26, 53], [18, 24, 18, 39, 79, 36, 90, 32, 84, 70, 91, 72, 39, 86, 37, 38, 71, 73, 34, 98, 28, 63, 73, 30, 41, 95, 8, 8, 78, 9, 98, 25, 9, 64, 3, 96, 27, 74, 66, 82, 59, 40, 24, 23, 41], [53, 49, 66, 61, 64, 34, 27, 64, 60, 35, 53, 72, 71, 58, 13, 76, 77, 53, 17, 57, 60, 15, 78, 19, 35, 18, 17, 84, 25, 37, 23, 23, 75, 46, 84, 7, 87, 62, 23, 91, 85, 21, 58, 96, 50], [28, 66, 93, 9, 35, 61, 68, 86, 23, 6, 84, 69, 12, 59, 65, 39, 41, 3, 42, 43, 85, 66, 96, 29, 47, 92, 97, 26, 15, 45, 90, 73, 61, 85, 20, 49, 27, 65, 9, 58, 51, 38, 84, 19, 44], [11, 78, 89, 76, 45, 7, 3, 80, 62, 1, 15, 44, 11, 1, 3, 22, 43, 6, 22, 50, 28, 78, 96, 29, 5, 35, 11, 1, 7, 3, 86, 31, 3, 17, 18, 79, 99, 80, 94, 99, 17, 79, 42, 27, 65], [30, 30, 69, 65, 4, 11, 58, 13, 10, 88, 84, 18, 87, 42, 99, 44, 62, 91, 79, 24, 30, 65, 41, 67, 24, 32, 63, 4, 98, 1, 21, 8, 46, 12, 1, 22, 78, 89, 28, 72, 64, 40, 89, 55, 87], [60, 41, 80, 59, 68, 36, 33, 94, 45, 75, 50, 47, 77, 44, 68, 88, 33, 97, 76, 21, 97, 46, 97, 73, 31, 62, 94, 16, 12, 54, 9, 35, 53, 43, 70, 89, 56, 64, 28, 87, 29, 86, 58, 24, 20], [27, 97, 19, 90, 38, 60, 3, 23, 59, 91, 91, 74, 24, 56, 52, 41, 66, 98, 22, 66, 28, 88, 38, 86, 67, 58, 37, 2, 57, 87, 77, 79, 97, 45, 53, 77, 84, 7, 77, 39, 68, 63, 46, 91, 96], [2, 15, 5, 3, 16, 49, 90, 6, 35, 38, 84, 86, 64, 85, 32, 1, 48, 23, 18, 17, 31, 93, 54, 77, 60, 66, 73, 96, 86, 18, 18, 83, 63, 31, 29, 88, 97, 83, 80, 51, 32, 21, 30, 7, 38], [12, 59, 92, 14, 71, 17, 23, 77, 20, 5, 6, 13, 3, 53, 31, 3, 8, 71, 50, 71, 75, 88, 59, 21, 20, 93, 74, 49, 80, 74, 38, 33, 69, 59, 12, 8, 70, 87, 48, 67, 38, 93, 34, 4, 7], [85, 74, 96, 89, 77, 85, 83, 59, 8, 61, 50, 84, 8, 16, 48, 62, 56, 28, 74, 21, 44, 79, 70, 41, 35, 56, 85, 17, 26, 63, 74, 34, 71, 32, 4, 10, 79, 56, 35, 33, 25, 47, 11, 34, 36], [17, 12, 80, 97, 26, 74, 13, 82, 85, 87, 87, 36, 69, 45, 79, 88, 12, 83, 97, 89, 38, 77, 88, 67, 76, 66, 20, 40, 34, 22, 15, 97, 66, 35, 98, 91, 31, 77, 53, 94, 90, 88, 57, 65, 38], [38, 86, 10, 46, 27, 42, 2, 58, 19, 62, 11, 14, 57, 33, 44, 18, 29, 30, 3, 32, 15, 49, 87, 60, 98, 46, 80, 50, 6, 80, 20, 49, 28, 26, 56, 48, 6, 53, 59, 80, 33, 12, 78, 39, 2]],34,),
    ([[19, 98, 9, 31, 79, 4, 63, 46, 32, 81, 5, 39, 97, 92, 13, 68, 28, 13, 92, 57, 99, 24, 9, 7, 22, 3, 72, 4, 42, 2, 53, 46, 6, 57, 86, 3, 17, 74, 88, 60, 39, 28, 45, 94], [92, 4, 82, 39, 3, 65, 97, 16, 46, 94, 40, 55, 97, 36, 60, 95, 36, 36, 47, 48, 10, 22, 28, 36, 32, 13, 34, 63, 65, 80, 91, 22, 31, 48, 93, 22, 71, 55, 40, 4, 78, 43, 81, 65], [2, 82, 3, 56, 85, 77, 49, 27, 60, 67, 69, 37, 48, 66, 94, 70, 27, 77, 5, 52, 58, 25, 91, 62, 16, 48, 71, 52, 67, 15, 81, 67, 61, 66, 69, 24, 95, 44, 71, 25, 20, 89, 66, 66], [10, 50, 70, 11, 93, 30, 85, 27, 42, 36, 45, 97, 27, 56, 37, 70, 39, 8, 76, 47, 67, 54, 9, 43, 12, 40, 3, 97, 77, 12, 37, 7, 70, 41, 4, 87, 4, 67, 38, 27, 11, 93, 93, 37], [58, 8, 32, 78, 84, 88, 93, 60, 65, 10, 19, 39, 45, 48, 18, 71, 88, 86, 16, 6, 71, 82, 99, 49, 88, 80, 19, 83, 65, 22, 31, 14, 30, 95, 51, 32, 43, 17, 92, 98, 62, 17, 61, 6], [93, 9, 31, 30, 59, 73, 10, 64, 33, 3, 93, 53, 41, 78, 15, 10, 80, 97, 92, 39, 24, 79, 13, 83, 11, 13, 40, 59, 96, 54, 61, 90, 59, 80, 17, 13, 13, 15, 11, 1, 35, 82, 44, 58], [1, 86, 52, 66, 94, 53, 82, 65, 3, 74, 48, 15, 67, 77, 62, 88, 30, 43, 32, 99, 35, 55, 15, 34, 98, 82, 99, 23, 32, 50, 50, 83, 93, 40, 44, 12, 68, 22, 43, 79, 85, 42, 99, 19], [72, 79, 4, 25, 51, 60, 37, 26, 73, 44, 55, 50, 31, 70, 25, 60, 6, 19, 5, 69, 59, 54, 5, 49, 20, 54, 77, 73, 78, 13, 97, 48, 87, 94, 63, 82, 82, 43, 78, 12, 39, 91, 57, 93], [71, 79, 83, 9, 84, 62, 22, 36, 96, 3, 82, 16, 3, 76, 88, 58, 75, 23, 33, 68, 61, 14, 38, 73, 98, 53, 61, 33, 83, 67, 56, 61, 38, 27, 40, 6, 96, 48, 18, 32, 84, 36, 79, 23], [14, 85, 46, 3, 7, 17, 68, 58, 50, 99, 70, 96, 99, 46, 59, 22, 72, 91, 28, 2, 59, 54, 66, 63, 27, 7, 12, 8, 9, 86, 18, 92, 38, 34, 70, 95, 15, 61, 68, 5, 87, 77, 61, 27], [45, 58, 95, 19, 30, 63, 94, 5, 62, 75, 74, 41, 65, 79, 85, 86, 96, 26, 77, 69, 78, 54, 55, 68, 8, 9, 95, 3, 27, 9, 93, 98, 29, 74, 77, 65, 40, 78, 96, 80, 56, 26, 33, 95], [72, 25, 97, 94, 1, 1, 27, 68, 37, 24, 44, 88, 6, 39, 65, 93, 88, 77, 92, 15, 64, 31, 86, 76, 17, 26, 77, 53, 41, 45, 81, 26, 51, 92, 38, 50, 42, 42, 32, 85, 9, 80, 5, 38], [9, 70, 79, 82, 69, 41, 74, 80, 27, 40, 53, 23, 92, 75, 4, 68, 80, 28, 29, 58, 17, 70, 18, 13, 64, 60, 61, 35, 89, 55, 35, 42, 11, 76, 54, 38, 32, 78, 25, 97, 98, 59, 70, 57], [41, 4, 7, 99, 19, 31, 20, 21, 25, 12, 98, 17, 96, 1, 79, 65, 63, 25, 71, 34, 44, 70, 1, 79, 77, 21, 77, 40, 17, 17, 76, 34, 39, 75, 14, 79, 87, 4, 33, 25, 41, 86, 32, 1], [63, 88, 53, 7, 43, 37, 70, 15, 34, 63, 65, 72, 35, 76, 46, 24, 1, 77, 79, 34, 37, 13, 16, 36, 70, 98, 76, 54, 44, 38, 47, 49, 36, 64, 63, 24, 68, 89, 11, 46, 3, 7, 54, 11], [65, 41, 55, 59, 26, 54, 14, 47, 16, 12, 93, 59, 32, 10, 93, 83, 55, 73, 89, 19, 39, 9, 17, 91, 8, 87, 55, 77, 41, 8, 13, 77, 55, 81, 20, 69, 25, 16, 43, 82, 59, 73, 35, 10], [99, 19, 13, 89, 69, 81, 34, 43, 87, 67, 10, 32, 97, 71, 13, 38, 11, 15, 87, 83, 8, 49, 88, 66, 30, 44, 54, 97, 83, 31, 24, 86, 39, 93, 34, 61, 4, 50, 53, 81, 28, 38, 4, 16], [42, 43, 64, 31, 79, 9, 68, 83, 34, 88, 11, 35, 28, 92, 11, 38, 98, 15, 61, 8, 65, 24, 50, 10, 17, 78, 1, 11, 41, 3, 17, 64, 75, 88, 33, 32, 25, 91, 47, 43, 81, 81, 57, 40], [68, 82, 75, 41, 40, 76, 37, 74, 15, 58, 58, 11, 98, 99, 8, 31, 15, 93, 79, 64, 31, 7, 94, 89, 79, 77, 74, 19, 49, 15, 3, 18, 22, 96, 95, 74, 45, 21, 34, 93, 74, 28, 54, 10], [32, 78, 32, 52, 30, 56, 72, 19, 22, 88, 28, 41, 43, 69, 73, 72, 59, 56, 82, 40, 77, 70, 16, 18, 42, 81, 2, 82, 64, 11, 55, 2, 2, 57, 18, 86, 16, 27, 17, 54, 17, 6, 97, 13], [6, 90, 83, 19, 61, 90, 86, 11, 86, 96, 7, 86, 6, 15, 38, 41, 56, 18, 35, 98, 45, 29, 69, 88, 32, 94, 5, 44, 98, 50, 82, 21, 22, 61, 39, 85, 99, 5, 33, 71, 24, 39, 72, 15], [70, 5, 87, 48, 20, 76, 21, 86, 89, 12, 66, 30, 7, 58, 18, 60, 18, 92, 48, 34, 72, 83, 6, 45, 60, 71, 84, 24, 93, 92, 69, 17, 62, 33, 62, 6, 3, 74, 54, 11, 87, 46, 4, 7], [26, 97, 35, 28, 41, 50, 99, 39, 80, 10, 71, 7, 25, 69, 90, 30, 11, 71, 39, 26, 57, 55, 22, 12, 64, 86, 66, 60, 62, 52, 62, 76, 65, 15, 40, 7, 55, 37, 86, 97, 33, 29, 19, 69], [14, 9, 5, 35, 85, 28, 45, 2, 6, 31, 32, 75, 59, 14, 74, 59, 1, 55, 31, 59, 8, 66, 99, 95, 12, 31, 99, 96, 81, 57, 8, 19, 53, 11, 57, 69, 59, 28, 2, 11, 64, 18, 47, 53], [5, 19, 5, 40, 83, 76, 92, 48, 99, 23, 55, 34, 87, 97, 58, 77, 98, 93, 30, 61, 82, 56, 99, 5, 4, 69, 39, 79, 73, 50, 72, 74, 22, 88, 24, 73, 22, 34, 48, 76, 81, 4, 57, 63], [30, 65, 97, 91, 78, 4, 35, 33, 51, 12, 68, 98, 78, 2, 91, 95, 33, 91, 45, 56, 28, 98, 30, 34, 1, 52, 13, 82, 40, 65, 9, 70, 72, 72, 88, 49, 25, 26, 26, 40, 34, 8, 2, 82], [16, 92, 72, 63, 18, 39, 42, 83, 32, 62, 32, 85, 93, 69, 84, 22, 27, 1, 13, 97, 6, 13, 78, 72, 67, 37, 76, 8, 93, 20, 62, 23, 68, 25, 32, 58, 25, 69, 10, 64, 31, 4, 57, 71], [34, 21, 83, 7, 98, 58, 33, 42, 53, 85, 55, 50, 38, 81, 46, 81, 15, 8, 49, 53, 37, 83, 93, 38, 97, 28, 61, 97, 7, 99, 72, 7, 59, 21, 25, 67, 32, 48, 55, 75, 85, 96, 66, 23], [45, 10, 78, 55, 60, 9, 83, 3, 32, 54, 87, 83, 76, 23, 14, 36, 48, 67, 10, 86, 68, 79, 52, 99, 49, 44, 5, 92, 91, 15, 94, 8, 55, 20, 77, 6, 1, 46, 42, 82, 70, 49, 90, 34], [57, 17, 89, 63, 61, 59, 92, 79, 4, 91, 33, 20, 21, 41, 74, 44, 32, 64, 37, 61, 26, 22, 40, 59, 50, 77, 96, 73, 39, 16, 98, 74, 88, 10, 45, 90, 34, 63, 68, 93, 86, 89, 11, 84], [88, 95, 25, 69, 31, 57, 87, 53, 81, 66, 56, 66, 91, 22, 81, 53, 57, 33, 5, 13, 17, 43, 84, 84, 92, 12, 84, 71, 56, 69, 29, 25, 11, 41, 11, 96, 38, 82, 62, 79, 81, 24, 44, 19], [37, 5, 4, 1, 94, 17, 43, 50, 30, 64, 82, 36, 1, 69, 82, 29, 81, 85, 66, 36, 62, 20, 83, 54, 82, 13, 47, 75, 97, 28, 55, 43, 44, 21, 94, 53, 47, 96, 87, 25, 96, 41, 31, 13], [6, 1, 8, 56, 62, 87, 69, 93, 22, 64, 69, 17, 18, 45, 54, 39, 65, 95, 88, 54, 16, 69, 32, 26, 35, 53, 43, 41, 24, 44, 79, 23, 75, 94, 45, 94, 55, 70, 69, 64, 14, 30, 4, 6], [39, 18, 51, 56, 89, 57, 59, 61, 17, 97, 38, 76, 81, 89, 37, 17, 91, 31, 14, 53, 36, 86, 5, 40, 70, 69, 88, 22, 14, 25, 84, 65, 49, 35, 52, 92, 29, 58, 72, 82, 31, 21, 6, 9], [30, 18, 30, 84, 60, 55, 10, 13, 41, 2, 5, 33, 65, 37, 61, 58, 12, 41, 28, 82, 36, 94, 42, 54, 54, 38, 85, 71, 69, 58, 99, 79, 9, 48, 18, 12, 27, 78, 77, 94, 36, 49, 9, 34], [76, 50, 89, 50, 22, 5, 15, 18, 77, 15, 89, 98, 66, 21, 87, 81, 61, 4, 48, 1, 7, 61, 53, 95, 35, 21, 60, 76, 5, 3, 59, 76, 10, 46, 50, 62, 59, 94, 17, 56, 44, 19, 18, 26], [28, 49, 32, 20, 85, 46, 58, 16, 76, 1, 46, 32, 14, 14, 83, 65, 25, 42, 13, 53, 68, 60, 84, 68, 41, 6, 26, 91, 22, 29, 40, 66, 36, 87, 19, 16, 88, 34, 63, 25, 75, 69, 84, 14], [21, 90, 44, 52, 79, 85, 80, 75, 48, 78, 85, 62, 80, 2, 42, 66, 28, 5, 8, 73, 81, 83, 42, 26, 95, 98, 93, 74, 58, 11, 97, 95, 22, 54, 93, 41, 85, 40, 12, 16, 43, 26, 94, 87], [97, 88, 6, 98, 19, 23, 25, 93, 16, 2, 93, 58, 97, 18, 44, 54, 9, 2, 55, 5, 20, 4, 5, 17, 5, 50, 72, 96, 25, 25, 89, 42, 31, 92, 47, 79, 51, 55, 60, 27, 39, 78, 13, 96], [35, 48, 14, 36, 53, 39, 5, 72, 10, 2, 95, 39, 25, 34, 79, 56, 81, 22, 33, 70, 58, 82, 30, 63, 67, 95, 12, 10, 62, 63, 36, 56, 6, 31, 33, 74, 63, 38, 26, 16, 24, 24, 73, 25], [23, 54, 67, 32, 74, 47, 35, 86, 14, 25, 59, 54, 79, 94, 95, 78, 8, 8, 95, 3, 97, 12, 32, 96, 21, 74, 41, 42, 57, 90, 77, 62, 73, 97, 95, 56, 12, 56, 58, 23, 89, 93, 33, 18], [41, 12, 62, 58, 4, 13, 31, 22, 39, 58, 30, 34, 95, 6, 90, 49, 45, 77, 93, 50, 26, 39, 86, 52, 4, 35, 5, 28, 21, 73, 10, 55, 33, 40, 5, 73, 81, 33, 81, 70, 91, 91, 78, 5], [81, 4, 71, 37, 78, 13, 29, 98, 98, 39, 48, 89, 35, 62, 20, 95, 59, 44, 54, 89, 58, 93, 52, 50, 46, 98, 10, 19, 11, 40, 40, 36, 87, 55, 44, 89, 44, 45, 85, 63, 91, 2, 6, 99], [73, 20, 55, 97, 47, 93, 27, 1, 13, 67, 65, 84, 58, 90, 76, 70, 50, 9, 55, 36, 20, 10, 10, 31, 84, 89, 45, 31, 9, 88, 4, 45, 24, 78, 72, 91, 53, 94, 78, 40, 58, 82, 77, 29]],37,),
    ([[91, 36, 24, 57], [88, 3, 45, 19], [49, 9, 86, 22], [55, 16, 72, 81]],3,),
    ([[27, 35, 35, 78, 52, 41, 22, 22, 75, 96, 91, 20, 46, 34, 83, 62, 10, 13, 92, 8, 86, 54, 92, 16, 17, 40, 49, 62, 19, 49, 38, 82, 62, 37, 93, 15, 85], [61, 56, 7, 36, 86, 37, 70, 40, 78, 17, 1, 44, 66, 42, 45, 46, 55, 21, 5, 84, 41, 86, 40, 87, 65, 13, 88, 89, 92, 68, 23, 4, 40, 61, 58, 98, 84], [17, 30, 92, 24, 95, 96, 38, 59, 63, 93, 64, 71, 52, 54, 15, 56, 70, 54, 81, 97, 61, 44, 1, 63, 59, 3, 13, 11, 61, 12, 82, 80, 33, 41, 4, 88, 47], [46, 54, 71, 9, 83, 93, 70, 36, 58, 86, 86, 38, 43, 67, 25, 78, 5, 18, 28, 30, 70, 95, 18, 25, 34, 72, 92, 71, 63, 98, 25, 65, 59, 66, 98, 96, 63], [12, 44, 54, 26, 54, 86, 31, 97, 22, 48, 8, 80, 28, 78, 68, 24, 83, 25, 47, 17, 66, 91, 8, 62, 37, 5, 46, 4, 59, 70, 29, 8, 48, 74, 99, 61, 53], [74, 64, 16, 76, 25, 79, 64, 78, 60, 70, 67, 27, 17, 89, 35, 69, 62, 94, 82, 84, 27, 44, 81, 63, 98, 56, 8, 57, 76, 61, 99, 3, 47, 14, 45, 79, 39], [67, 24, 62, 2, 69, 68, 2, 62, 11, 17, 12, 83, 77, 83, 84, 21, 56, 31, 31, 69, 40, 2, 11, 52, 24, 48, 62, 95, 2, 90, 17, 60, 55, 49, 75, 55, 42], [77, 90, 94, 20, 72, 64, 84, 75, 28, 75, 73, 36, 27, 6, 28, 13, 87, 47, 11, 85, 39, 24, 75, 45, 90, 48, 42, 84, 59, 29, 68, 82, 46, 58, 12, 32, 95], [8, 89, 11, 26, 41, 60, 19, 48, 17, 63, 10, 34, 93, 51, 45, 28, 18, 96, 36, 5, 82, 80, 3, 6, 97, 60, 80, 44, 66, 66, 69, 92, 52, 1, 5, 68, 93], [66, 79, 5, 59, 95, 26, 14, 41, 75, 83, 74, 52, 42, 81, 82, 60, 89, 15, 47, 33, 95, 37, 47, 36, 70, 46, 52, 72, 75, 26, 29, 2, 24, 18, 33, 85, 86], [33, 32, 33, 40, 62, 14, 45, 26, 27, 10, 71, 81, 43, 68, 97, 16, 24, 21, 93, 50, 79, 62, 92, 52, 18, 8, 9, 59, 44, 70, 98, 67, 18, 83, 73, 13, 40], [69, 47, 24, 37, 44, 46, 44, 75, 60, 74, 3, 17, 51, 5, 35, 82, 91, 90, 57, 31, 77, 60, 80, 50, 22, 80, 72, 32, 18, 33, 64, 45, 38, 30, 64, 42, 13], [77, 68, 42, 6, 79, 27, 96, 53, 7, 31, 88, 66, 72, 71, 65, 8, 53, 68, 30, 83, 61, 37, 84, 45, 53, 13, 32, 62, 2, 77, 8, 96, 48, 14, 85, 33, 36], [85, 59, 70, 69, 48, 30, 28, 41, 76, 58, 41, 11, 6, 20, 91, 29, 73, 48, 71, 85, 82, 15, 2, 97, 75, 53, 55, 70, 13, 44, 58, 17, 41, 25, 69, 14, 29], [52, 30, 12, 91, 95, 93, 91, 69, 9, 26, 27, 15, 79, 98, 14, 2, 46, 70, 80, 73, 80, 44, 86, 19, 72, 44, 45, 85, 67, 79, 66, 22, 17, 58, 80, 47, 14], [41, 69, 55, 21, 80, 31, 32, 80, 9, 37, 9, 21, 56, 8, 24, 80, 95, 20, 5, 50, 2, 67, 58, 96, 89, 99, 30, 15, 93, 2, 70, 93, 22, 70, 93, 62, 81], [96, 82, 25, 18, 46, 75, 69, 63, 54, 27, 44, 62, 70, 75, 29, 96, 4, 69, 60, 82, 72, 23, 38, 62, 12, 85, 22, 96, 58, 92, 61, 18, 67, 94, 77, 65, 35], [39, 26, 17, 50, 32, 22, 39, 89, 32, 88, 59, 8, 44, 30, 77, 23, 64, 77, 30, 70, 94, 98, 17, 88, 73, 54, 19, 31, 25, 97, 38, 55, 50, 37, 35, 96, 60], [86, 67, 75, 88, 98, 30, 15, 75, 84, 88, 74, 39, 99, 42, 95, 27, 5, 76, 98, 75, 29, 62, 91, 56, 43, 80, 79, 13, 97, 5, 94, 50, 49, 90, 73, 69, 99], [55, 59, 1, 67, 9, 26, 66, 92, 20, 90, 14, 2, 21, 59, 19, 46, 15, 32, 36, 78, 35, 9, 98, 95, 25, 41, 44, 74, 98, 49, 55, 15, 66, 62, 26, 42, 35], [45, 32, 62, 64, 52, 96, 43, 92, 55, 44, 91, 79, 59, 54, 88, 85, 1, 85, 87, 22, 50, 31, 50, 29, 39, 1, 65, 50, 18, 49, 75, 37, 70, 76, 35, 72, 43], [65, 43, 66, 35, 34, 42, 80, 8, 6, 40, 68, 23, 63, 14, 89, 58, 36, 34, 76, 21, 45, 58, 15, 45, 17, 50, 88, 55, 92, 31, 31, 85, 97, 10, 66, 53, 11], [56, 79, 89, 34, 87, 43, 92, 68, 3, 14, 29, 85, 17, 70, 45, 53, 50, 48, 69, 65, 74, 5, 28, 96, 71, 42, 60, 2, 22, 92, 97, 95, 98, 10, 28, 88, 78], [36, 61, 2, 51, 34, 35, 43, 11, 32, 38, 47, 81, 85, 95, 5, 64, 86, 53, 29, 1, 30, 26, 86, 10, 13, 25, 15, 1, 75, 44, 35, 13, 19, 48, 12, 73, 84], [82, 64, 25, 6, 5, 38, 12, 55, 66, 67, 26, 51, 31, 6, 30, 96, 82, 39, 9, 99, 73, 63, 70, 99, 4, 30, 45, 26, 74, 70, 31, 26, 71, 8, 61, 85, 38], [48, 62, 97, 16, 3, 62, 56, 67, 99, 87, 12, 88, 55, 13, 15, 7, 24, 13, 19, 67, 5, 50, 74, 64, 48, 49, 84, 80, 63, 7, 98, 34, 79, 5, 57, 74, 42], [72, 85, 45, 71, 40, 9, 64, 93, 60, 20, 17, 39, 63, 22, 71, 45, 28, 6, 81, 66, 61, 8, 7, 80, 66, 22, 43, 49, 71, 26, 98, 54, 39, 12, 41, 99, 2], [52, 93, 84, 53, 55, 19, 26, 37, 13, 87, 25, 58, 47, 23, 3, 51, 78, 79, 35, 78, 17, 6, 58, 84, 48, 10, 14, 27, 68, 83, 52, 51, 45, 66, 57, 27, 47], [88, 42, 63, 58, 68, 66, 46, 22, 85, 54, 78, 84, 98, 84, 33, 73, 42, 38, 77, 13, 55, 69, 97, 58, 49, 50, 46, 1, 91, 39, 6, 52, 68, 73, 63, 90, 2], [61, 24, 64, 5, 65, 50, 55, 35, 71, 4, 50, 85, 73, 90, 58, 1, 20, 75, 32, 13, 28, 10, 2, 5, 71, 97, 71, 66, 14, 85, 18, 14, 13, 83, 21, 30, 35], [96, 51, 55, 58, 82, 71, 12, 74, 38, 3, 46, 73, 57, 71, 26, 46, 48, 18, 63, 44, 57, 59, 82, 62, 46, 18, 85, 15, 6, 60, 59, 82, 23, 32, 35, 55, 35], [2, 24, 90, 62, 90, 44, 4, 22, 51, 16, 56, 30, 66, 37, 18, 19, 94, 9, 31, 82, 69, 74, 86, 49, 40, 80, 23, 94, 60, 10, 75, 92, 30, 25, 27, 72, 74], [98, 93, 17, 27, 23, 91, 74, 80, 70, 1, 89, 49, 17, 33, 32, 14, 4, 96, 62, 17, 89, 14, 6, 11, 28, 9, 72, 30, 60, 44, 38, 80, 64, 84, 74, 62, 53], [99, 7, 63, 10, 21, 94, 70, 34, 12, 75, 55, 68, 87, 33, 33, 14, 2, 3, 52, 18, 35, 68, 8, 71, 37, 44, 26, 11, 57, 81, 69, 77, 20, 99, 82, 14, 77], [86, 13, 54, 5, 89, 15, 79, 15, 86, 36, 85, 17, 13, 59, 94, 16, 60, 16, 50, 99, 49, 2, 8, 91, 69, 92, 58, 52, 5, 23, 42, 74, 26, 71, 82, 83, 2], [89, 44, 88, 67, 64, 70, 91, 85, 18, 33, 46, 80, 57, 85, 66, 51, 45, 2, 39, 3, 80, 28, 28, 97, 31, 44, 20, 11, 11, 39, 6, 64, 63, 60, 63, 31, 38], [99, 18, 9, 42, 28, 67, 23, 10, 5, 2, 25, 60, 87, 67, 53, 17, 41, 33, 92, 5, 87, 73, 70, 6, 73, 81, 13, 3, 73, 14, 67, 36, 84, 46, 82, 1, 20]],36,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))