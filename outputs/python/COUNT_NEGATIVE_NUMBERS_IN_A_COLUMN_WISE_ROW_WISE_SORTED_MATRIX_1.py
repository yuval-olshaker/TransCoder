# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( M , n , m ) :
    count = 0
    i = 0
    j = m - 1
    while j >= 0 and i < n :
        if M [ i ] [ j ] < 0 :
            count += ( j + 1 )
            i += 1
        else :
            j -= 1
    return count


#TOFILL

if __name__ == '__main__':
    param = [
    ([[76, 39, 83, 83, 24, 11, 7, 97, 81, 52, 7, 81, 68, 25, 14, 54, 69, 12, 53, 38, 94, 77, 75, 28, 38, 92, 47, 46, 86], [63, 95, 96, 14, 82, 98, 75, 5, 72, 27, 71, 62, 15, 55, 63, 37, 10, 2, 68, 98, 15, 21, 25, 83, 84, 46, 93, 23, 87], [47, 23, 49, 53, 26, 14, 50, 50, 5, 3, 2, 28, 69, 14, 47, 82, 78, 48, 89, 84, 32, 28, 71, 20, 99, 66, 4, 54, 23], [43, 37, 14, 20, 36, 19, 4, 97, 53, 42, 12, 69, 48, 60, 31, 29, 97, 86, 21, 69, 78, 61, 23, 20, 99, 51, 51, 38, 72], [92, 40, 87, 23, 98, 25, 84, 79, 98, 94, 8, 33, 86, 21, 30, 52, 51, 53, 38, 72, 38, 79, 54, 5, 35, 45, 81, 61, 92], [49, 92, 94, 43, 1, 28, 43, 39, 50, 96, 28, 32, 35, 47, 6, 20, 90, 38, 92, 11, 98, 36, 51, 72, 7, 63, 92, 20, 10], [31, 26, 58, 16, 98, 43, 79, 88, 47, 23, 1, 63, 48, 54, 51, 1, 21, 74, 94, 8, 74, 80, 86, 96, 55, 36, 73, 62, 68], [32, 70, 24, 22, 91, 36, 67, 12, 17, 23, 45, 57, 51, 47, 3, 52, 44, 39, 56, 87, 35, 48, 26, 36, 91, 8, 67, 86, 25], [27, 80, 9, 11, 42, 7, 77, 83, 95, 92, 36, 23, 28, 3, 32, 75, 37, 88, 78, 53, 38, 12, 29, 25, 63, 3, 83, 85, 40], [15, 14, 11, 3, 1, 50, 70, 72, 85, 66, 75, 41, 2, 74, 5, 97, 53, 77, 69, 22, 69, 99, 93, 24, 22, 98, 83, 3, 59], [94, 54, 92, 22, 14, 71, 92, 18, 52, 75, 66, 32, 23, 84, 86, 46, 16, 15, 60, 27, 66, 14, 77, 1, 16, 93, 68, 9, 75], [72, 91, 27, 73, 33, 29, 78, 40, 83, 75, 56, 74, 48, 40, 92, 94, 72, 62, 57, 59, 70, 2, 18, 71, 28, 53, 15, 87, 22], [83, 76, 75, 55, 3, 52, 29, 64, 9, 85, 89, 13, 62, 82, 63, 57, 25, 59, 6, 18, 6, 67, 22, 2, 24, 42, 52, 5, 18], [72, 95, 58, 66, 69, 95, 23, 13, 77, 86, 34, 74, 75, 97, 90, 10, 47, 54, 23, 37, 46, 85, 81, 39, 82, 11, 98, 6, 11], [95, 58, 35, 92, 80, 58, 58, 82, 23, 29, 43, 20, 27, 55, 41, 52, 35, 29, 40, 13, 34, 52, 11, 21, 39, 56, 9, 67, 39], [5, 8, 27, 88, 80, 32, 94, 82, 25, 43, 35, 62, 26, 93, 70, 18, 22, 54, 71, 38, 85, 61, 95, 67, 58, 53, 11, 34, 65], [72, 84, 81, 42, 42, 98, 74, 18, 93, 39, 48, 88, 29, 82, 95, 13, 9, 63, 17, 54, 47, 10, 8, 47, 34, 87, 65, 32, 15], [12, 36, 98, 64, 88, 77, 1, 70, 87, 33, 46, 30, 37, 89, 99, 60, 28, 57, 74, 11, 80, 57, 66, 51, 25, 7, 93, 90, 37], [80, 99, 88, 26, 88, 80, 98, 61, 42, 1, 91, 2, 7, 68, 1, 4, 48, 2, 61, 7, 69, 70, 15, 76, 72, 22, 83, 16, 42], [47, 6, 71, 29, 60, 14, 18, 74, 48, 85, 14, 55, 34, 63, 45, 24, 7, 55, 69, 45, 72, 76, 54, 46, 89, 97, 27, 35, 21], [81, 95, 80, 69, 92, 74, 94, 2, 70, 70, 27, 61, 46, 1, 77, 6, 95, 72, 18, 25, 47, 48, 49, 43, 89, 10, 54, 74, 54], [94, 67, 23, 93, 87, 73, 68, 38, 43, 64, 35, 72, 72, 34, 30, 81, 12, 32, 8, 20, 62, 36, 63, 88, 98, 13, 7, 57, 66], [40, 20, 92, 48, 43, 19, 36, 78, 87, 17, 45, 35, 7, 36, 27, 38, 83, 33, 64, 41, 50, 37, 62, 39, 74, 74, 73, 14, 94], [97, 4, 66, 99, 57, 66, 42, 6, 32, 64, 44, 1, 34, 41, 86, 3, 78, 43, 7, 19, 68, 3, 31, 83, 50, 47, 86, 16, 87], [61, 18, 41, 10, 33, 56, 90, 62, 32, 52, 66, 56, 16, 12, 15, 5, 79, 47, 33, 44, 92, 2, 23, 63, 57, 5, 85, 23, 87], [41, 81, 24, 64, 1, 60, 10, 50, 76, 4, 24, 45, 63, 64, 25, 14, 4, 4, 35, 20, 61, 11, 8, 45, 30, 33, 32, 56, 11], [82, 93, 72, 31, 22, 62, 63, 61, 93, 62, 7, 17, 43, 39, 9, 68, 76, 15, 92, 60, 4, 16, 49, 68, 38, 61, 18, 45, 1], [3, 44, 78, 74, 33, 97, 37, 73, 10, 21, 68, 84, 77, 42, 44, 42, 18, 95, 32, 16, 56, 83, 19, 15, 61, 72, 55, 80, 99], [9, 4, 61, 31, 73, 79, 37, 60, 13, 36, 92, 62, 20, 6, 79, 82, 59, 67, 12, 43, 70, 65, 33, 16, 70, 36, 51, 38, 61]],27,27,),
    ([[17, 56], [68, 34]],1,1,),
    ([[63, 21, 24, 76, 7, 94, 21, 23, 39, 45, 23, 2, 16, 42, 23, 6, 15, 37, 47, 64, 18, 55, 99, 5, 74, 66, 9, 82, 40, 13, 2, 14, 34, 11, 47, 56], [20, 30, 34, 53, 49, 37, 11, 29, 58, 85, 94, 81, 88, 50, 61, 5, 72, 5, 58, 86, 98, 77, 72, 35, 2, 53, 11, 29, 84, 27, 25, 40, 90, 52, 69, 90], [10, 24, 96, 55, 26, 55, 47, 7, 75, 42, 43, 29, 46, 78, 74, 32, 16, 82, 42, 42, 59, 78, 68, 82, 32, 31, 8, 27, 18, 7, 22, 70, 27, 9, 86, 83], [91, 89, 31, 11, 33, 34, 47, 34, 18, 39, 82, 4, 92, 89, 8, 89, 83, 24, 56, 46, 92, 50, 76, 20, 58, 69, 17, 98, 97, 37, 38, 76, 1, 87, 2, 97], [64, 35, 17, 29, 96, 12, 57, 8, 12, 47, 65, 48, 97, 10, 26, 4, 70, 28, 10, 79, 81, 82, 60, 70, 44, 59, 83, 75, 29, 19, 27, 74, 4, 6, 67, 67], [54, 41, 10, 15, 57, 80, 50, 86, 25, 2, 45, 7, 37, 77, 55, 72, 37, 94, 93, 69, 6, 79, 95, 73, 68, 77, 47, 80, 77, 55, 38, 80, 7, 90, 60, 92], [56, 85, 53, 32, 16, 26, 43, 24, 24, 7, 47, 52, 99, 90, 76, 35, 63, 2, 48, 36, 63, 23, 14, 69, 65, 22, 90, 87, 5, 22, 35, 86, 19, 72, 97, 6], [30, 68, 46, 51, 93, 74, 58, 6, 79, 93, 31, 6, 81, 16, 29, 31, 1, 26, 82, 1, 51, 71, 89, 85, 39, 93, 6, 4, 22, 96, 94, 61, 58, 4, 40, 89], [57, 39, 35, 96, 86, 55, 55, 45, 51, 20, 67, 50, 39, 73, 73, 64, 92, 49, 89, 73, 45, 87, 46, 73, 45, 27, 23, 91, 49, 99, 21, 2, 16, 76, 14, 8], [26, 56, 59, 26, 75, 99, 7, 86, 47, 8, 90, 8, 36, 52, 76, 62, 21, 39, 12, 8, 9, 63, 29, 41, 7, 77, 28, 93, 51, 11, 87, 60, 65, 4, 28, 65], [82, 47, 44, 19, 27, 71, 36, 9, 13, 48, 5, 87, 29, 74, 88, 64, 77, 94, 82, 54, 14, 42, 93, 63, 9, 76, 70, 63, 19, 81, 19, 78, 94, 41, 52, 18], [25, 55, 1, 99, 50, 76, 42, 89, 35, 3, 55, 35, 26, 99, 47, 50, 74, 90, 61, 61, 12, 49, 87, 98, 81, 44, 46, 77, 13, 77, 75, 73, 19, 36, 14, 53], [77, 73, 1, 49, 66, 56, 54, 46, 6, 62, 67, 94, 83, 41, 65, 66, 22, 67, 66, 30, 57, 71, 19, 65, 33, 29, 72, 72, 90, 19, 82, 50, 89, 75, 81, 9], [50, 61, 36, 63, 82, 74, 2, 12, 79, 88, 25, 21, 75, 81, 25, 74, 68, 81, 24, 98, 49, 99, 35, 2, 69, 34, 57, 35, 85, 35, 98, 1, 83, 52, 32, 98], [58, 19, 70, 53, 75, 93, 19, 63, 29, 73, 69, 63, 30, 84, 56, 7, 48, 45, 41, 53, 20, 44, 97, 53, 85, 6, 35, 93, 74, 81, 58, 98, 93, 31, 7, 30], [35, 59, 63, 40, 37, 2, 79, 35, 70, 50, 29, 78, 5, 15, 34, 50, 76, 60, 39, 23, 67, 80, 62, 26, 51, 64, 83, 59, 78, 56, 52, 45, 5, 85, 56, 62], [18, 97, 81, 30, 57, 26, 64, 52, 52, 21, 18, 67, 49, 69, 40, 5, 25, 96, 19, 67, 15, 31, 52, 35, 43, 97, 74, 60, 85, 54, 58, 91, 13, 3, 2, 69], [79, 23, 13, 11, 51, 54, 53, 5, 37, 75, 81, 14, 13, 38, 93, 40, 42, 23, 81, 49, 83, 86, 99, 96, 96, 23, 68, 60, 91, 48, 7, 24, 58, 3, 54, 80], [80, 93, 37, 66, 75, 96, 96, 8, 17, 64, 40, 74, 41, 44, 41, 93, 38, 38, 77, 31, 49, 76, 23, 90, 1, 80, 70, 30, 13, 81, 44, 31, 71, 75, 33, 83], [9, 7, 91, 42, 85, 39, 95, 24, 78, 52, 37, 76, 64, 75, 65, 23, 91, 47, 98, 55, 66, 72, 14, 52, 12, 99, 80, 54, 8, 87, 56, 60, 39, 80, 2, 79], [64, 11, 70, 65, 36, 63, 89, 63, 15, 62, 56, 23, 43, 31, 3, 79, 36, 75, 69, 92, 64, 67, 48, 44, 72, 64, 84, 74, 48, 99, 53, 84, 83, 38, 43, 51], [50, 14, 8, 82, 83, 80, 14, 3, 37, 24, 75, 34, 29, 36, 87, 16, 76, 79, 64, 35, 50, 39, 88, 13, 72, 91, 60, 28, 71, 95, 68, 50, 76, 55, 68, 3], [54, 55, 22, 6, 97, 76, 3, 9, 29, 33, 54, 68, 89, 35, 36, 72, 34, 43, 29, 34, 56, 23, 65, 2, 86, 80, 78, 69, 12, 66, 52, 47, 34, 61, 54, 82], [70, 76, 28, 63, 71, 56, 43, 38, 9, 46, 20, 12, 81, 36, 1, 48, 77, 22, 57, 51, 74, 63, 18, 75, 50, 59, 8, 63, 35, 27, 79, 66, 69, 81, 11, 33], [38, 24, 37, 49, 70, 31, 11, 2, 30, 34, 86, 1, 3, 48, 71, 41, 23, 11, 4, 65, 16, 42, 48, 38, 9, 12, 50, 9, 17, 60, 58, 82, 90, 88, 82, 72], [61, 89, 15, 40, 61, 85, 26, 9, 67, 62, 73, 28, 7, 76, 13, 89, 28, 43, 41, 36, 95, 17, 25, 26, 59, 66, 83, 35, 8, 46, 86, 20, 49, 29, 73, 74], [11, 42, 44, 98, 98, 9, 24, 16, 58, 43, 28, 68, 57, 44, 94, 50, 37, 31, 44, 18, 50, 27, 50, 10, 25, 54, 43, 31, 38, 84, 20, 21, 91, 30, 63, 89], [71, 27, 83, 1, 75, 71, 77, 29, 69, 12, 45, 59, 82, 5, 30, 40, 74, 16, 69, 51, 99, 97, 93, 30, 61, 3, 23, 1, 84, 31, 69, 27, 27, 79, 66, 46], [46, 15, 23, 88, 71, 27, 77, 24, 69, 23, 36, 95, 67, 69, 15, 38, 27, 8, 69, 18, 82, 61, 28, 14, 43, 73, 46, 99, 41, 4, 66, 32, 88, 27, 21, 67], [59, 42, 75, 62, 2, 89, 77, 88, 8, 39, 42, 63, 89, 52, 41, 69, 38, 54, 64, 11, 8, 82, 10, 16, 72, 88, 16, 25, 75, 81, 8, 18, 50, 63, 78, 32], [94, 64, 54, 48, 64, 92, 80, 19, 47, 75, 25, 48, 79, 9, 84, 59, 4, 9, 98, 23, 99, 90, 4, 42, 55, 41, 5, 99, 9, 19, 19, 70, 8, 41, 21, 32], [36, 34, 6, 11, 51, 7, 72, 53, 85, 49, 55, 96, 96, 42, 22, 69, 44, 32, 30, 1, 31, 90, 51, 7, 54, 43, 80, 66, 43, 53, 68, 5, 1, 97, 88, 14], [87, 13, 21, 98, 41, 36, 79, 99, 44, 55, 94, 65, 2, 35, 28, 88, 14, 42, 28, 15, 27, 62, 72, 98, 79, 59, 58, 34, 64, 53, 18, 36, 59, 23, 76, 66], [77, 16, 17, 9, 27, 67, 43, 78, 57, 38, 50, 27, 4, 30, 8, 68, 18, 36, 4, 57, 90, 29, 37, 56, 3, 95, 8, 75, 75, 49, 63, 10, 34, 20, 67, 11], [76, 91, 51, 58, 73, 99, 42, 93, 3, 65, 79, 51, 51, 67, 90, 62, 45, 50, 67, 61, 17, 90, 85, 22, 85, 3, 3, 17, 65, 80, 89, 68, 59, 78, 16, 82], [8, 66, 57, 91, 66, 68, 17, 15, 33, 36, 37, 62, 36, 39, 99, 57, 15, 97, 46, 15, 47, 20, 87, 63, 88, 86, 66, 1, 46, 4, 78, 80, 34, 91, 17, 93]],35,28,),
    ([[96, 91, 61, 55], [60, 18, 48, 25], [94, 72, 84, 54], [10, 62, 23, 79]],3,2,),
    ([[68, 61, 12, 7, 49, 65, 57, 32, 57, 95, 64, 17, 77, 59], [38, 7, 47, 21, 69, 36, 79, 82, 23, 27, 76, 37, 43, 52], [37, 95, 8, 88, 57, 73, 4, 52, 75, 99, 7, 55, 78, 23], [45, 1, 5, 89, 89, 71, 96, 27, 86, 75, 49, 30, 91, 78], [90, 64, 33, 88, 19, 95, 21, 5, 74, 90, 65, 86, 8, 53], [96, 14, 83, 29, 23, 39, 48, 68, 97, 68, 97, 60, 19, 66], [92, 85, 40, 36, 18, 94, 53, 75, 6, 72, 63, 98, 1, 87], [31, 50, 24, 38, 46, 2, 24, 76, 34, 76, 45, 59, 90, 90], [65, 98, 95, 65, 4, 82, 85, 58, 1, 68, 69, 73, 3, 10], [39, 44, 93, 64, 97, 19, 21, 52, 70, 73, 19, 85, 83, 96], [49, 48, 54, 77, 37, 82, 64, 93, 13, 76, 14, 4, 14, 57], [67, 85, 12, 23, 33, 66, 19, 41, 19, 2, 30, 95, 84, 7], [35, 38, 97, 53, 61, 25, 80, 94, 77, 49, 86, 6, 12, 71], [39, 32, 7, 19, 13, 24, 26, 48, 79, 47, 13, 2, 48, 7]],13,13,),
    ([[52, 24, 47, 92, 56, 78, 13, 64, 21, 58], [97, 6, 75, 14, 88, 68, 7, 23, 39, 50], [17, 67, 52, 78, 74, 63, 61, 47, 65, 66], [45, 47, 94, 50, 82, 16, 11, 94, 83, 61], [91, 81, 3, 52, 62, 85, 27, 82, 83, 58], [90, 5, 40, 91, 76, 16, 88, 65, 94, 47], [63, 83, 38, 72, 5, 18, 89, 42, 39, 14], [23, 18, 89, 8, 80, 67, 23, 35, 69, 14], [83, 83, 45, 73, 40, 8, 26, 90, 27, 38], [36, 11, 82, 87, 50, 1, 24, 90, 52, 78]],8,8,),
    ([[75, 18, 92, 72, 81, 98, 29, 53, 45, 28, 6, 37, 39, 3, 30, 17, 77, 29, 56, 43, 6, 97, 35, 89, 22, 24], [53, 29, 83, 34, 63, 60, 11, 35, 84, 27, 50, 21, 52, 63, 46, 47, 43, 6, 43, 37, 56, 89, 44, 49, 78, 82], [39, 2, 47, 28, 17, 17, 92, 70, 8, 27, 34, 58, 41, 7, 54, 95, 65, 86, 74, 37, 59, 41, 38, 36, 10, 17], [53, 9, 95, 28, 34, 19, 32, 19, 70, 79, 45, 66, 16, 66, 21, 19, 57, 75, 68, 47, 68, 38, 16, 42, 10, 80], [2, 3, 13, 81, 70, 71, 94, 52, 44, 16, 80, 55, 96, 16, 88, 7, 67, 84, 9, 49, 73, 93, 59, 14, 59, 27], [11, 21, 30, 54, 74, 52, 72, 38, 99, 55, 14, 77, 9, 6, 61, 52, 64, 18, 43, 94, 82, 54, 68, 73, 63, 84], [97, 16, 69, 54, 41, 92, 65, 23, 93, 53, 95, 60, 47, 17, 42, 3, 22, 57, 56, 96, 61, 87, 77, 63, 21, 28], [76, 21, 99, 51, 78, 19, 19, 13, 89, 44, 89, 25, 76, 73, 71, 23, 48, 99, 7, 36, 26, 48, 38, 80, 58, 81], [16, 46, 97, 92, 29, 56, 53, 79, 77, 95, 13, 99, 55, 33, 65, 16, 73, 78, 38, 10, 2, 86, 31, 35, 24, 55], [14, 4, 76, 13, 89, 59, 80, 74, 13, 94, 38, 79, 59, 93, 42, 5, 12, 69, 25, 49, 86, 78, 3, 50, 54, 24], [63, 2, 29, 74, 80, 37, 35, 2, 28, 54, 39, 61, 7, 88, 66, 91, 4, 29, 37, 33, 25, 17, 66, 45, 51, 47], [54, 95, 80, 2, 12, 35, 23, 77, 37, 57, 61, 66, 12, 68, 23, 10, 78, 48, 67, 86, 9, 82, 98, 39, 78, 26], [75, 36, 19, 34, 54, 70, 36, 97, 26, 87, 62, 3, 42, 18, 71, 53, 60, 39, 32, 72, 8, 28, 79, 9, 84, 26], [6, 65, 24, 64, 86, 49, 78, 92, 53, 43, 12, 21, 74, 31, 1, 8, 16, 1, 84, 26, 36, 58, 26, 46, 62, 96], [12, 67, 58, 42, 70, 74, 31, 70, 79, 96, 72, 22, 92, 4, 70, 16, 18, 86, 95, 73, 36, 21, 20, 47, 74, 64], [26, 18, 42, 4, 41, 72, 81, 27, 96, 79, 45, 26, 39, 22, 36, 87, 15, 54, 64, 3, 74, 22, 40, 43, 98, 1], [12, 52, 15, 36, 80, 80, 75, 48, 5, 76, 62, 12, 18, 1, 3, 21, 7, 37, 35, 9, 72, 23, 63, 69, 63, 71], [76, 16, 82, 3, 77, 42, 65, 35, 17, 15, 20, 60, 98, 3, 29, 46, 75, 36, 15, 54, 40, 86, 81, 21, 12, 28], [32, 59, 65, 75, 40, 20, 82, 40, 73, 44, 78, 26, 9, 25, 92, 93, 32, 84, 8, 76, 34, 7, 49, 5, 42, 10], [23, 67, 12, 62, 81, 87, 63, 39, 2, 41, 27, 49, 19, 43, 16, 44, 24, 95, 69, 49, 34, 23, 73, 52, 18, 40], [90, 90, 98, 56, 40, 54, 31, 92, 32, 50, 25, 89, 8, 38, 88, 90, 81, 52, 56, 87, 38, 87, 78, 69, 99, 91], [54, 5, 15, 40, 9, 85, 32, 81, 37, 2, 13, 78, 55, 79, 73, 64, 16, 14, 55, 39, 32, 21, 79, 82, 17, 79], [92, 99, 79, 3, 52, 68, 58, 99, 51, 8, 28, 42, 77, 42, 19, 98, 38, 63, 31, 69, 53, 93, 81, 36, 99, 89], [73, 90, 89, 34, 63, 28, 69, 64, 87, 82, 63, 50, 50, 54, 47, 73, 94, 5, 93, 30, 34, 7, 84, 56, 97, 87], [74, 49, 31, 66, 24, 68, 50, 25, 36, 23, 38, 21, 39, 44, 40, 60, 43, 98, 47, 88, 96, 1, 56, 14, 73, 51], [76, 57, 45, 67, 84, 5, 52, 43, 40, 81, 99, 42, 83, 39, 3, 79, 43, 64, 52, 27, 21, 67, 16, 11, 81, 33]],18,15,),
    ([[45, 38, 43, 11, 2, 77, 3, 59, 58, 22, 6, 65, 13, 43, 52, 15], [69, 16, 25, 44, 58, 94, 54, 33, 96, 27, 86, 41, 25, 86, 66, 95], [59, 30, 24, 88, 58, 3, 79, 72, 44, 79, 74, 38, 88, 50, 67, 63], [77, 66, 59, 16, 29, 18, 24, 81, 6, 78, 40, 14, 23, 20, 86, 90], [54, 62, 50, 48, 35, 34, 91, 85, 64, 72, 50, 41, 27, 83, 70, 30], [78, 37, 23, 81, 90, 53, 11, 37, 80, 30, 45, 86, 9, 7, 6, 14], [75, 66, 60, 75, 3, 95, 96, 17, 49, 70, 85, 94, 90, 17, 48, 13], [8, 50, 36, 13, 18, 84, 71, 19, 77, 3, 97, 76, 35, 1, 9, 5], [7, 7, 26, 74, 17, 90, 16, 84, 96, 49, 25, 45, 33, 65, 73, 19], [85, 24, 39, 8, 23, 16, 31, 84, 43, 16, 92, 73, 2, 72, 69, 58], [7, 72, 1, 48, 82, 42, 84, 66, 11, 35, 70, 72, 80, 47, 71, 46], [92, 19, 1, 42, 4, 55, 31, 93, 38, 92, 22, 87, 40, 35, 10, 58], [28, 30, 44, 35, 39, 15, 99, 79, 2, 52, 67, 96, 41, 34, 68, 88], [41, 84, 68, 59, 71, 64, 79, 76, 52, 26, 16, 25, 89, 11, 39, 97], [76, 74, 93, 51, 9, 19, 66, 31, 38, 44, 41, 77, 61, 85, 72, 60], [18, 97, 93, 70, 18, 8, 55, 92, 63, 45, 19, 53, 78, 37, 76, 32]],11,11,),
    ([[88, 45, 19, 4, 98, 22, 59, 11, 85, 88, 3, 46, 20, 27, 14, 92, 24, 45, 89, 7, 84, 55, 54, 65, 95, 92, 10, 97, 41], [50, 92, 97, 19, 60, 78, 38, 90, 54, 69, 35, 95, 78, 27, 7, 19, 31, 16, 26, 23, 39, 21, 39, 4, 69, 3, 95, 4, 48], [50, 96, 8, 79, 99, 92, 99, 70, 68, 51, 29, 3, 56, 9, 98, 2, 24, 79, 37, 27, 86, 34, 31, 74, 23, 48, 78, 9, 70], [62, 93, 53, 48, 89, 17, 47, 17, 46, 31, 63, 63, 2, 25, 59, 59, 30, 55, 95, 32, 73, 54, 31, 7, 59, 42, 7, 45, 13], [64, 8, 35, 71, 49, 38, 83, 47, 7, 70, 53, 16, 96, 33, 97, 62, 87, 5, 16, 96, 26, 66, 73, 24, 97, 46, 77, 71, 43], [80, 43, 36, 54, 65, 85, 9, 88, 43, 53, 6, 27, 75, 32, 51, 36, 88, 79, 2, 45, 46, 59, 73, 78, 12, 66, 84, 64, 54], [61, 5, 44, 80, 52, 38, 85, 41, 91, 64, 3, 59, 12, 10, 83, 6, 91, 4, 17, 63, 78, 86, 61, 80, 60, 81, 16, 91, 56], [58, 25, 51, 21, 69, 32, 68, 5, 93, 92, 79, 17, 83, 60, 21, 11, 6, 60, 42, 13, 75, 59, 60, 70, 8, 92, 58, 12, 63], [56, 42, 60, 3, 1, 3, 21, 66, 11, 14, 77, 77, 76, 43, 64, 14, 71, 54, 9, 52, 92, 84, 21, 92, 35, 97, 18, 99, 4], [17, 46, 28, 48, 45, 50, 85, 2, 73, 1, 26, 8, 95, 42, 53, 40, 45, 94, 30, 37, 61, 16, 44, 25, 36, 9, 56, 36, 90], [90, 32, 51, 10, 22, 17, 53, 22, 37, 32, 43, 40, 26, 42, 29, 45, 70, 53, 56, 28, 58, 6, 83, 70, 40, 90, 75, 81, 28], [20, 70, 17, 6, 63, 59, 87, 3, 22, 17, 88, 45, 12, 86, 98, 42, 51, 52, 35, 3, 47, 93, 5, 46, 59, 37, 93, 36, 75], [76, 66, 33, 20, 53, 44, 81, 5, 12, 13, 78, 27, 82, 94, 6, 2, 97, 60, 13, 27, 51, 59, 34, 22, 60, 35, 16, 55, 66], [79, 89, 28, 6, 35, 23, 55, 27, 71, 89, 97, 7, 20, 41, 48, 97, 23, 83, 17, 9, 59, 34, 49, 66, 63, 47, 28, 59, 24], [98, 48, 63, 80, 29, 81, 60, 76, 22, 46, 71, 98, 18, 44, 14, 90, 12, 54, 29, 27, 23, 2, 88, 65, 75, 76, 69, 22, 34], [98, 19, 77, 51, 45, 43, 39, 81, 9, 82, 38, 43, 39, 62, 83, 94, 66, 4, 69, 14, 84, 13, 96, 71, 18, 7, 91, 2, 25], [49, 42, 78, 9, 52, 81, 43, 29, 96, 56, 71, 95, 52, 63, 70, 23, 58, 8, 50, 91, 74, 19, 54, 89, 28, 86, 8, 71, 26], [9, 42, 86, 62, 16, 55, 89, 70, 37, 4, 73, 48, 25, 75, 24, 55, 32, 84, 3, 27, 46, 63, 79, 61, 2, 88, 26, 64, 46], [14, 23, 36, 97, 88, 37, 26, 53, 96, 91, 10, 62, 34, 5, 45, 5, 25, 12, 17, 42, 47, 64, 63, 28, 70, 26, 67, 98, 12], [16, 54, 94, 32, 17, 6, 35, 73, 50, 74, 39, 45, 31, 30, 7, 13, 44, 56, 30, 33, 40, 82, 85, 52, 46, 29, 81, 31, 99], [69, 62, 61, 40, 63, 96, 52, 95, 16, 74, 74, 3, 49, 76, 88, 90, 76, 26, 33, 40, 75, 83, 11, 38, 7, 66, 57, 45, 33], [62, 48, 8, 10, 28, 79, 60, 78, 26, 82, 13, 16, 52, 99, 15, 67, 53, 15, 81, 12, 77, 83, 84, 61, 44, 40, 94, 66, 24], [51, 76, 56, 42, 98, 20, 96, 37, 32, 41, 28, 55, 65, 43, 98, 24, 28, 26, 64, 69, 48, 24, 3, 74, 68, 48, 8, 24, 7], [48, 84, 58, 83, 45, 84, 81, 27, 9, 37, 36, 80, 93, 90, 2, 43, 28, 54, 34, 5, 64, 33, 56, 20, 99, 99, 49, 29, 69], [19, 80, 60, 22, 1, 42, 35, 37, 14, 46, 87, 12, 70, 25, 54, 80, 13, 6, 98, 15, 24, 77, 80, 20, 54, 4, 22, 74, 5], [80, 3, 20, 93, 99, 9, 88, 6, 72, 99, 6, 93, 69, 27, 90, 62, 41, 38, 4, 21, 21, 33, 57, 91, 96, 10, 40, 8, 23], [56, 44, 68, 36, 33, 58, 79, 25, 13, 72, 51, 37, 92, 30, 62, 23, 13, 57, 87, 49, 3, 49, 95, 68, 36, 6, 78, 21, 58], [60, 9, 7, 99, 19, 48, 62, 8, 43, 71, 83, 35, 51, 79, 4, 59, 79, 39, 5, 91, 35, 77, 51, 30, 84, 92, 72, 16, 27], [22, 58, 62, 3, 99, 42, 88, 86, 42, 55, 9, 55, 61, 36, 11, 47, 19, 21, 82, 82, 35, 66, 70, 28, 59, 27, 75, 36, 5]],16,15,),
    ([[9, 7, 25, 16, 34, 78, 18, 20, 43, 67, 73, 98, 45, 20, 73, 51, 62, 62, 20, 32, 55, 72, 60, 15, 48, 49, 38, 83, 25, 87, 12, 93, 97, 52, 41, 90], [38, 97, 57, 14, 10, 64, 43, 72, 64, 96, 44, 32, 55, 79, 34, 45, 74, 76, 96, 77, 63, 97, 2, 63, 38, 96, 98, 22, 76, 9, 43, 4, 23, 56, 43, 99], [3, 97, 67, 53, 94, 92, 93, 81, 15, 34, 6, 20, 66, 44, 12, 13, 43, 15, 48, 16, 70, 83, 54, 58, 47, 3, 71, 44, 71, 10, 63, 49, 83, 4, 81, 63], [98, 64, 37, 36, 59, 47, 49, 30, 46, 75, 67, 61, 91, 63, 46, 20, 2, 85, 61, 40, 74, 60, 34, 40, 56, 21, 11, 26, 66, 5, 21, 21, 64, 37, 29, 84], [37, 20, 33, 63, 35, 85, 36, 86, 14, 55, 97, 56, 17, 52, 5, 73, 33, 92, 24, 97, 39, 94, 11, 44, 24, 45, 85, 39, 99, 65, 19, 76, 68, 82, 51, 18], [67, 46, 51, 73, 35, 35, 13, 67, 60, 46, 88, 85, 97, 91, 11, 54, 15, 66, 39, 26, 12, 85, 95, 79, 63, 94, 36, 20, 87, 54, 51, 26, 10, 35, 6, 7], [45, 34, 15, 72, 77, 92, 77, 99, 7, 44, 49, 49, 93, 4, 20, 27, 46, 7, 44, 29, 4, 4, 12, 89, 60, 54, 63, 70, 32, 78, 44, 24, 68, 96, 58, 47], [60, 71, 69, 9, 88, 29, 85, 97, 98, 87, 55, 81, 24, 93, 93, 95, 83, 88, 65, 64, 55, 68, 65, 19, 53, 16, 55, 62, 95, 2, 79, 49, 99, 89, 29, 48], [60, 6, 9, 20, 64, 81, 54, 76, 46, 22, 62, 52, 82, 31, 52, 76, 45, 66, 22, 56, 88, 32, 66, 80, 35, 54, 7, 15, 71, 89, 77, 77, 38, 89, 48, 22], [30, 66, 22, 51, 19, 60, 8, 27, 62, 66, 35, 94, 87, 14, 92, 45, 7, 78, 26, 82, 23, 80, 11, 95, 23, 99, 81, 11, 20, 64, 10, 13, 51, 64, 94, 22], [76, 49, 78, 72, 98, 66, 77, 69, 15, 17, 31, 64, 89, 99, 98, 14, 28, 5, 72, 47, 46, 11, 99, 60, 62, 17, 67, 36, 33, 81, 14, 74, 90, 36, 88, 14], [90, 77, 53, 61, 18, 38, 48, 55, 35, 41, 70, 12, 70, 48, 93, 43, 68, 50, 11, 55, 78, 95, 21, 25, 40, 16, 86, 91, 26, 70, 69, 89, 53, 61, 7, 22], [91, 94, 52, 73, 87, 70, 24, 63, 86, 9, 37, 46, 17, 28, 27, 20, 47, 93, 56, 81, 7, 84, 81, 68, 1, 14, 49, 27, 89, 42, 16, 27, 67, 83, 96, 73], [84, 24, 54, 47, 63, 22, 42, 38, 4, 66, 52, 18, 29, 94, 15, 88, 69, 22, 91, 83, 51, 55, 6, 4, 37, 38, 72, 5, 55, 12, 75, 34, 68, 8, 68, 30], [47, 74, 37, 48, 80, 45, 51, 19, 54, 94, 80, 28, 95, 20, 62, 37, 43, 4, 1, 80, 46, 99, 3, 93, 62, 32, 25, 16, 33, 83, 38, 13, 1, 88, 48, 1], [89, 58, 76, 95, 72, 66, 44, 24, 16, 51, 72, 66, 36, 15, 88, 33, 69, 84, 76, 16, 93, 99, 80, 56, 11, 13, 7, 63, 12, 38, 56, 6, 92, 11, 42, 48], [6, 8, 64, 4, 14, 59, 32, 2, 52, 18, 28, 32, 54, 56, 54, 64, 59, 19, 51, 27, 22, 63, 15, 95, 34, 73, 25, 35, 68, 97, 32, 52, 49, 99, 93, 60], [93, 53, 88, 70, 7, 70, 92, 72, 16, 59, 72, 86, 45, 9, 43, 52, 74, 58, 93, 76, 34, 94, 47, 83, 37, 15, 2, 36, 14, 59, 52, 9, 45, 94, 60, 75], [26, 28, 26, 4, 14, 74, 59, 73, 21, 49, 64, 64, 53, 20, 2, 99, 26, 39, 24, 58, 33, 10, 17, 21, 5, 76, 95, 61, 23, 77, 22, 34, 75, 51, 44, 91], [19, 37, 44, 78, 43, 76, 54, 24, 80, 72, 53, 94, 66, 82, 32, 80, 89, 20, 64, 40, 22, 93, 94, 95, 20, 8, 62, 36, 70, 1, 75, 57, 77, 23, 20, 69], [70, 58, 27, 59, 1, 90, 89, 23, 36, 85, 92, 45, 2, 93, 65, 10, 10, 83, 13, 85, 91, 33, 4, 80, 63, 76, 17, 80, 10, 6, 6, 7, 61, 63, 48, 43], [14, 15, 86, 46, 44, 37, 56, 36, 34, 12, 32, 30, 32, 35, 28, 68, 51, 72, 62, 15, 53, 58, 90, 22, 87, 34, 36, 24, 99, 95, 66, 14, 38, 72, 43, 39], [44, 35, 36, 39, 97, 34, 36, 19, 18, 46, 71, 90, 12, 87, 18, 95, 7, 53, 89, 20, 7, 50, 24, 37, 10, 25, 45, 1, 95, 87, 88, 22, 4, 92, 56, 34], [38, 84, 92, 22, 76, 71, 16, 58, 49, 39, 92, 60, 31, 32, 94, 48, 38, 42, 88, 15, 1, 94, 13, 32, 17, 75, 19, 73, 42, 97, 31, 68, 34, 16, 10, 28], [57, 76, 12, 77, 28, 88, 31, 36, 11, 40, 78, 4, 16, 57, 41, 61, 88, 70, 52, 57, 59, 57, 79, 78, 83, 97, 53, 87, 80, 74, 45, 2, 80, 65, 78, 80], [47, 70, 68, 66, 93, 33, 73, 43, 6, 64, 36, 19, 81, 73, 1, 55, 39, 48, 13, 30, 80, 41, 8, 40, 14, 48, 7, 49, 19, 31, 95, 64, 57, 88, 97, 47], [71, 54, 34, 95, 21, 31, 85, 67, 94, 53, 28, 79, 51, 18, 19, 89, 21, 1, 41, 65, 63, 85, 71, 18, 90, 13, 55, 30, 12, 55, 31, 6, 6, 91, 43, 19], [31, 93, 54, 82, 24, 21, 43, 77, 96, 18, 60, 68, 37, 7, 58, 10, 53, 80, 83, 36, 86, 76, 41, 12, 4, 51, 45, 7, 32, 2, 33, 48, 67, 65, 12, 10], [61, 57, 43, 48, 47, 9, 29, 42, 21, 67, 86, 56, 3, 61, 83, 5, 84, 77, 41, 12, 56, 79, 92, 33, 10, 35, 11, 60, 29, 73, 58, 78, 24, 11, 26, 76], [18, 74, 87, 74, 1, 61, 24, 37, 27, 86, 48, 91, 62, 91, 29, 8, 72, 26, 48, 9, 49, 54, 93, 17, 33, 1, 57, 1, 61, 21, 30, 41, 33, 37, 17, 51], [64, 66, 69, 5, 27, 17, 30, 72, 51, 88, 42, 66, 61, 58, 77, 87, 43, 64, 84, 64, 27, 19, 58, 11, 17, 14, 67, 21, 29, 45, 42, 63, 48, 54, 26, 78], [79, 62, 86, 3, 12, 45, 84, 16, 55, 93, 24, 93, 59, 12, 92, 2, 61, 9, 92, 97, 31, 15, 48, 33, 51, 49, 55, 48, 1, 9, 66, 83, 24, 54, 23, 56], [63, 57, 5, 89, 37, 4, 46, 26, 70, 75, 85, 39, 56, 6, 39, 43, 55, 93, 87, 15, 98, 77, 61, 25, 15, 52, 58, 86, 66, 57, 22, 66, 54, 46, 9, 36], [83, 65, 45, 2, 10, 81, 87, 31, 76, 58, 50, 57, 18, 89, 93, 30, 78, 35, 88, 75, 77, 26, 98, 75, 53, 68, 43, 49, 99, 98, 88, 13, 12, 97, 93, 9], [59, 15, 73, 29, 52, 78, 11, 30, 13, 1, 57, 69, 53, 53, 34, 33, 90, 85, 60, 76, 97, 42, 73, 98, 95, 64, 28, 78, 39, 91, 94, 27, 49, 48, 22, 58], [24, 52, 10, 2, 94, 13, 6, 27, 89, 82, 28, 99, 30, 20, 34, 12, 58, 96, 50, 51, 34, 85, 89, 72, 28, 77, 50, 23, 26, 27, 96, 55, 72, 66, 38, 77]],27,25,)
        ]
    for i, p_set in enumerate(param):
        param[i] = list(param[i])
        param[i][0] = [[e - 50 for e in sorted(l)] for l in p_set[0]]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("%i, %i" % (n_success, len(param)))