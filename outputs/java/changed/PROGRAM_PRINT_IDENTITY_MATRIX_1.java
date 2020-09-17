// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class PROGRAM_PRINT_IDENTITY_MATRIX_1{
static boolean f_gold ( int mat [ ] [ ] , int N ) {
  for ( int row = 0 ;
  row < N ;
  row ++ ) {
    for ( int col = 0 ;
    col < N ;
    col ++ ) {
      if ( row == col && mat [ row ] [ col ] != 1 ) return false ;
      else if ( row != col && mat [ row ] [ col ] != 0 ) return false ;
    }
  }
  return true ;
}


//
public static boolean f_filled ( int [ ] [ ] mat , int N ) {
  for ( int row = 0 ;
  row < N ;
  row ++ ) {
    for ( int col = 0 ;
    col < N ;
    col ++ ) {
      if ( ( row == col && mat [ row ] [ col ] != 1 ) || ( row != col && mat [ row ] [ col ] != 0 ) ) {
        return false ;
      };
    }
    else if ( ( row != col && mat [ row ] [ col ] != 0 ) || ( row == col && mat [ row ] [ col ] != 0 ) ) {
      return false ;
    };
  }
  return true ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<int [ ] [ ]> param0 = new ArrayList<>();
    param0.add(new int[][]{new int[]{}});
    param0.add(new int[][]{new int[]{1}});
    param0.add(new int[][]{new int[]{1,0,0,0},new int[]{0,1,0,0},new int[]{0,0,1,0},new int[]{0,0,0,1}});
    param0.add(new int[][]{new int[]{1,0,0,0},new int[]{0,1,0,0},new int[]{0,0,1,0},new int[]{1,0,0,1}});
    param0.add(new int[][]{new int[]{80,68,67,24,55,89,15,35,7,28,36,65,76,4,97,99,82,21,14,55,66,43,28,81,94,23,43,97,74},new int[]{94,39,98,29,57,15,49,96,28,97,8,4,39,58,71,76,88,85,9,89,93,64,44,64,41,47,26,70,75},new int[]{47,8,15,88,50,27,9,88,95,51,96,43,14,14,38,63,40,60,41,80,13,74,29,26,52,95,86,39,66},new int[]{40,65,70,92,28,99,1,80,18,13,45,88,67,16,75,91,37,2,80,33,64,4,59,6,11,11,25,39,7},new int[]{43,70,31,99,4,1,98,30,76,89,2,14,6,28,56,19,30,87,98,75,37,39,1,84,29,92,71,67,54},new int[]{18,97,8,12,59,68,25,40,24,82,22,43,73,59,17,92,67,90,14,95,8,41,3,7,69,59,15,63,88},new int[]{32,57,74,7,87,61,83,38,83,68,1,89,92,76,94,21,25,27,62,29,21,88,14,59,20,77,7,35,5},new int[]{22,72,82,3,58,73,55,65,23,83,65,96,63,16,92,63,60,76,91,58,7,65,3,61,13,12,6,88,83},new int[]{15,52,62,34,57,88,56,16,25,23,50,90,57,94,56,62,33,20,71,66,7,10,88,35,47,42,61,9,1},new int[]{85,33,29,35,54,26,37,63,35,16,22,97,68,22,14,70,84,89,93,85,54,15,15,77,15,80,81,60,64},new int[]{4,62,17,84,89,79,9,58,43,16,10,32,36,93,76,7,44,93,12,19,25,34,80,53,65,69,9,71,56},new int[]{65,37,85,44,43,68,55,69,55,52,47,38,41,37,32,24,35,59,46,41,48,51,87,64,75,71,94,17,60},new int[]{50,6,95,63,14,78,8,83,46,7,32,90,3,25,88,78,11,34,57,10,18,33,75,14,68,6,98,12,36},new int[]{11,73,12,20,89,5,78,56,3,36,98,63,11,88,4,9,87,20,62,87,23,3,54,51,99,10,30,34,33},new int[]{79,23,94,80,42,32,29,28,18,35,74,94,89,52,11,74,5,15,78,99,38,94,95,89,92,79,74,13,24},new int[]{74,87,21,34,25,60,49,92,29,88,22,65,27,24,89,32,90,42,67,24,71,47,79,12,73,42,2,80,13},new int[]{79,84,54,87,94,43,62,11,48,36,26,22,27,31,14,87,30,23,6,43,64,76,68,2,33,14,13,63,4},new int[]{77,96,66,22,59,32,40,81,24,58,39,63,53,3,68,37,29,11,50,38,74,64,70,5,75,46,47,15,75},new int[]{5,87,49,47,42,18,34,58,72,65,68,73,17,74,93,85,97,97,93,36,97,70,49,84,24,73,21,36,92},new int[]{97,58,52,86,90,71,1,92,71,85,32,71,27,68,71,96,57,62,81,98,25,89,13,84,59,91,83,92,43},new int[]{74,54,73,63,20,19,13,22,96,46,80,60,68,40,12,34,43,41,57,49,24,69,54,29,20,65,13,50,54},new int[]{93,26,9,10,61,46,49,40,3,93,22,24,99,19,77,92,10,27,28,5,8,4,56,9,52,76,89,28,82},new int[]{73,33,56,17,7,59,85,95,64,16,40,86,27,59,65,49,55,27,35,93,97,27,73,14,78,33,27,84,5},new int[]{37,93,55,95,95,70,37,78,49,62,65,26,85,16,70,36,39,59,33,24,62,53,80,30,91,28,44,92,12},new int[]{45,91,17,24,74,67,90,86,68,26,55,20,65,9,51,69,74,76,3,90,3,64,81,81,89,73,60,76,21},new int[]{4,53,19,1,88,95,30,83,85,76,74,29,59,52,92,46,74,93,67,96,46,88,45,87,56,28,49,57,96},new int[]{10,41,45,41,2,48,49,20,48,21,60,57,10,69,47,91,34,23,5,89,61,36,51,19,59,23,96,90,94},new int[]{16,12,62,79,4,78,25,56,40,44,66,42,75,95,91,17,78,79,41,79,17,7,99,81,47,36,67,74,68},new int[]{78,88,92,77,75,10,5,97,22,77,70,97,86,14,3,6,39,95,21,38,33,68,52,24,22,38,37,98,46}});
    param0.add(new int[][]{new int[]{54,16,12,57,31,31,71,17,46},new int[]{74,81,65,60,4,64,19,31,18},new int[]{42,3,51,46,58,13,72,29,69},new int[]{6,81,28,72,32,8,11,14,16},new int[]{9,2,29,22,52,42,78,46,15},new int[]{70,89,42,58,72,9,21,23,34},new int[]{37,33,35,32,96,38,69,53,18},new int[]{35,19,88,73,2,67,92,61,29},new int[]{49,40,86,14,67,89,37,66,29}});
    param0.add(new int[][]{new int[]{6,45,61,50,95,16,88,4,77,57,23,14,58,9,94,61,56,58,52,22,3,88,34,16,75,37,40,45,19,5,38,43,25,90,33,54,45,58,91,26,72,59,90,58},new int[]{57,23,46,56,38,75,35,81,92,15,69,75,73,74,2,25,82,15,3,66,55,50,78,42,27,20,59,82,84,99,77,60,29,87,2,93,4,73,58,75,24,91,34,60},new int[]{48,16,15,20,93,77,91,76,26,29,82,81,6,17,65,78,72,13,17,21,70,68,27,5,86,42,29,93,22,85,83,47,34,71,20,66,38,51,11,98,69,33,11,61},new int[]{52,98,3,21,45,88,95,71,96,74,5,34,29,25,22,4,45,34,27,34,25,6,20,64,95,6,38,70,47,12,16,31,36,69,52,3,42,99,39,51,4,83,43,89},new int[]{82,5,49,81,7,20,64,69,5,76,7,66,34,32,73,21,39,84,11,79,12,75,41,22,9,55,83,58,20,91,23,55,14,41,90,34,28,82,71,31,75,97,13,70},new int[]{14,38,99,57,37,89,94,35,32,3,8,80,7,36,13,14,62,18,9,65,10,62,18,23,79,18,19,27,85,5,24,89,4,18,79,55,50,53,93,98,47,79,11,44},new int[]{36,45,81,66,95,20,70,67,48,14,53,71,38,92,33,65,19,93,70,82,49,39,20,99,49,26,62,14,51,43,50,67,79,71,1,79,44,88,77,29,16,17,79,37},new int[]{47,63,92,95,43,92,58,38,70,7,33,6,22,24,57,14,16,99,86,58,7,60,18,86,66,12,99,35,62,84,16,64,7,64,37,26,89,95,46,22,82,41,63,81},new int[]{44,45,67,38,12,94,31,12,24,7,81,14,25,88,7,44,78,20,67,49,64,52,5,3,79,95,29,50,30,76,57,35,11,10,73,35,62,92,19,47,61,2,21,18},new int[]{26,32,78,90,56,43,74,23,88,4,86,76,75,51,45,76,49,47,27,34,53,44,52,31,79,34,51,75,38,20,58,29,11,42,82,67,83,48,32,6,89,88,36,2},new int[]{75,60,53,13,83,51,2,9,67,24,12,85,4,11,94,3,51,30,7,13,47,80,21,11,52,13,31,99,10,60,53,8,4,86,74,41,98,64,11,4,48,55,58,8},new int[]{2,30,97,44,20,75,85,39,34,37,66,61,85,96,26,13,78,59,37,25,20,50,21,90,39,22,51,9,49,2,83,89,98,11,32,91,57,83,80,23,48,62,14,20},new int[]{43,87,42,65,98,57,25,16,20,23,86,8,47,82,85,56,95,80,72,83,35,17,35,51,7,64,49,87,99,37,25,55,86,58,82,59,73,4,97,76,70,36,39,51},new int[]{38,79,75,87,98,4,60,71,43,12,30,59,89,91,67,85,59,74,94,10,36,88,59,15,90,20,62,67,7,65,48,85,72,42,24,33,85,37,70,8,91,33,60,36},new int[]{65,64,13,60,62,41,27,90,90,72,40,55,83,31,54,47,1,86,27,93,91,95,44,56,6,72,93,67,17,24,19,52,46,25,58,37,42,71,62,96,38,4,80,44},new int[]{25,70,58,20,57,12,57,29,95,36,54,63,48,92,43,87,72,58,39,85,42,53,1,7,1,56,52,4,47,50,12,4,57,9,54,72,6,50,67,1,20,88,70,59},new int[]{9,39,54,75,64,97,52,37,52,22,14,87,16,69,20,85,45,43,96,14,14,12,35,79,23,85,23,27,82,1,63,1,69,26,82,14,95,30,13,87,95,73,52,18},new int[]{6,50,3,2,89,32,77,57,75,12,49,25,53,14,23,77,32,40,48,25,66,28,42,86,68,80,88,40,85,24,41,64,77,8,8,72,51,86,72,58,36,95,74,34},new int[]{70,93,46,18,15,36,4,3,8,86,82,87,44,93,54,95,26,25,59,81,58,14,15,60,98,87,24,59,43,3,91,91,42,37,4,88,2,96,49,93,60,87,58,23},new int[]{60,63,45,25,49,83,69,50,69,72,72,60,68,66,46,20,32,31,47,72,54,64,18,96,24,99,73,31,97,28,81,36,35,87,64,97,56,11,15,58,5,99,20,91},new int[]{48,71,80,56,84,33,73,39,19,51,80,90,54,22,50,30,41,22,74,29,74,16,26,75,89,31,32,73,64,89,37,87,51,20,59,41,18,23,54,53,79,87,69,72},new int[]{37,2,19,48,66,62,73,81,90,78,3,66,10,49,32,44,67,24,28,63,79,25,89,59,63,55,22,92,22,9,37,36,48,88,47,92,83,44,38,60,87,67,85,10},new int[]{67,95,54,94,33,72,62,96,67,16,87,35,54,38,79,59,53,57,96,51,52,78,72,22,80,86,53,38,47,72,95,22,72,10,53,95,49,22,13,12,29,50,36,60},new int[]{91,79,47,95,10,98,88,93,69,89,80,90,55,17,76,40,46,42,41,56,62,40,19,87,95,46,37,61,33,96,85,83,60,37,73,55,70,56,27,42,50,32,86,97},new int[]{65,30,27,47,8,3,73,16,19,68,38,37,90,62,83,12,15,34,29,26,48,90,64,28,61,17,86,10,81,92,23,75,16,97,76,89,61,4,54,92,70,91,67,92},new int[]{68,8,75,73,41,37,79,63,2,96,29,18,80,66,63,88,95,13,31,83,51,56,39,69,79,9,1,84,86,66,74,27,10,35,40,96,41,42,18,95,54,74,11,71},new int[]{64,45,42,50,83,34,54,55,99,11,74,78,20,29,47,41,68,12,8,14,42,63,98,55,36,20,79,75,30,57,17,75,33,39,39,4,15,39,48,32,61,13,4,5},new int[]{34,40,40,57,3,45,81,4,34,43,63,51,55,65,91,29,59,9,23,90,79,80,82,24,91,31,45,76,32,91,81,59,69,92,98,54,48,48,9,54,51,52,46,72},new int[]{14,30,64,76,37,19,73,70,80,21,32,65,6,82,82,63,9,84,83,18,18,72,18,34,3,69,3,40,27,4,20,6,59,41,64,5,49,1,4,48,51,3,73,98},new int[]{78,67,32,90,78,32,16,15,20,39,75,80,20,67,4,6,6,45,48,97,13,39,50,4,62,92,78,12,88,89,27,69,17,59,27,79,36,66,14,81,32,68,46,77},new int[]{25,26,66,77,45,94,29,69,7,55,43,41,14,68,98,98,75,81,91,93,58,36,75,16,52,95,41,76,6,2,12,50,66,7,63,24,96,36,12,47,58,86,20,8},new int[]{43,30,21,45,62,76,21,12,5,98,24,39,66,8,10,47,52,62,69,33,43,63,94,47,89,35,2,97,68,27,91,67,79,76,63,44,62,26,71,41,65,11,63,68},new int[]{83,26,88,87,27,89,90,44,25,11,24,51,63,87,21,47,30,87,41,10,51,68,19,99,3,60,9,1,88,96,50,51,4,7,21,19,81,12,3,68,86,76,94,27},new int[]{70,20,21,16,66,54,91,72,58,19,87,21,83,86,36,55,90,93,21,99,40,83,70,10,74,29,47,2,90,40,54,7,42,58,81,86,96,50,78,91,13,8,19,75},new int[]{48,77,22,83,16,42,23,23,66,28,93,6,55,33,71,80,69,45,17,65,61,36,96,88,34,91,96,16,38,82,14,46,93,30,80,71,78,32,88,10,49,64,80,71},new int[]{43,22,43,14,39,21,40,9,28,58,67,37,48,21,15,23,65,37,95,9,78,72,24,15,61,34,60,71,89,67,54,12,65,93,7,33,32,66,15,77,35,49,7,37},new int[]{11,94,76,42,84,60,54,9,48,62,66,29,46,66,39,5,50,42,11,70,68,44,97,32,66,78,94,30,74,62,30,9,72,93,86,56,39,33,3,69,90,82,84,52},new int[]{58,42,85,13,96,49,7,2,15,63,99,30,99,61,4,70,61,2,41,89,65,73,26,81,80,99,19,60,97,47,82,52,99,46,20,64,72,76,77,87,83,71,61,27},new int[]{52,73,93,29,14,16,36,20,50,20,82,46,13,97,48,91,3,64,95,94,57,80,35,72,96,88,2,90,46,85,12,85,6,72,26,43,6,23,98,98,57,5,88,33},new int[]{16,41,49,59,67,92,11,44,53,79,8,47,38,89,16,59,8,57,45,87,27,63,52,23,70,22,27,95,39,42,53,70,77,14,37,66,40,42,83,19,15,51,42,31},new int[]{11,64,69,92,73,96,98,93,44,68,87,34,37,60,65,74,41,20,72,60,58,91,84,58,54,16,68,88,17,9,20,10,2,24,80,41,15,99,74,19,83,88,77,97},new int[]{1,23,97,64,27,1,39,25,98,41,57,7,11,26,60,53,1,88,78,45,83,1,7,43,35,34,68,40,20,64,82,66,61,46,54,50,30,55,51,83,9,47,89,94},new int[]{58,17,59,16,88,29,50,63,79,86,5,74,37,36,17,23,2,55,85,19,88,94,98,10,80,3,18,2,90,24,45,95,42,7,59,46,44,93,35,30,4,89,62,45},new int[]{30,12,55,36,47,2,26,57,75,42,38,56,75,95,26,95,37,73,28,31,29,46,25,96,15,77,85,19,76,71,83,23,1,93,59,94,64,45,37,9,92,92,66,5}});
    param0.add(new int[][]{new int[]{65,34,26,9,37,67,53,2,72,64,94,58,2,94,35,57,91,79,54,72,39,11,27,46,26,53,1,43,93,8,32,94,4},new int[]{70,74,34,17,26,35,12,1,81,4,69,57,12,53,47,75,31,54,38,4,75,27,12,68,75,76,32,30,97,65,71,82,58},new int[]{55,76,56,98,18,2,69,56,84,19,8,83,11,32,19,33,18,70,85,12,21,53,84,42,79,57,48,74,4,32,56,93,25},new int[]{81,46,85,84,85,1,12,93,15,95,36,6,66,53,15,15,22,13,52,78,51,78,13,12,16,6,33,46,74,60,42,23,86},new int[]{24,32,97,90,96,79,70,38,1,40,31,81,50,18,5,83,71,28,59,22,85,88,9,42,42,80,1,53,69,19,28,6,7},new int[]{94,36,5,98,38,21,4,80,67,31,67,25,86,20,25,51,91,81,49,36,34,90,15,17,73,93,29,64,65,69,15,99,85},new int[]{51,3,38,69,97,30,29,16,18,38,53,56,27,45,82,52,93,83,38,48,58,63,75,35,57,3,64,35,91,2,3,11,17},new int[]{42,87,47,48,84,66,97,47,22,24,25,13,60,82,36,33,6,21,37,70,99,46,59,7,48,43,85,61,88,23,28,62,67},new int[]{39,1,60,53,83,73,88,11,94,21,35,42,70,76,11,21,37,94,77,44,16,18,11,48,23,31,88,99,47,51,5,84,39},new int[]{76,36,4,40,26,32,68,98,87,61,86,9,7,19,87,82,25,89,88,17,71,90,93,96,93,38,79,40,37,39,50,78,27},new int[]{93,50,25,86,64,79,31,5,2,79,17,28,43,55,75,86,80,44,40,79,22,86,76,39,29,94,55,21,58,16,11,25,3},new int[]{65,46,21,53,94,31,36,95,56,15,61,79,47,91,6,3,77,58,19,1,14,3,88,14,25,26,87,31,32,92,34,1,10},new int[]{32,23,80,11,71,66,61,14,5,4,20,46,14,22,46,33,79,10,23,40,27,14,53,96,36,18,88,72,21,89,54,41,15},new int[]{58,51,83,78,50,9,74,89,78,45,35,48,16,22,87,98,55,14,45,66,39,69,15,63,90,99,58,71,72,58,66,60,59},new int[]{75,60,51,45,94,80,68,18,55,52,91,83,75,66,82,59,25,32,60,99,55,18,44,8,47,70,23,50,47,70,7,82,75},new int[]{99,87,34,94,16,25,38,55,34,47,95,19,23,33,65,4,12,69,58,37,49,64,31,15,8,81,49,21,43,17,36,69,66},new int[]{36,37,27,32,39,87,14,14,20,91,54,77,73,98,84,49,31,88,35,60,64,92,11,25,83,61,81,9,17,75,41,26,9},new int[]{56,72,59,52,16,37,54,75,37,61,38,68,69,30,45,88,94,90,63,37,68,93,36,66,81,75,22,26,70,1,91,57,48},new int[]{12,1,43,29,13,3,73,28,90,13,17,93,52,42,98,43,50,25,73,54,77,70,68,53,34,14,36,19,74,2,3,62,91},new int[]{53,16,54,88,98,49,27,72,31,44,42,79,26,27,2,29,98,49,13,86,43,39,15,35,93,47,36,30,55,50,14,6,62},new int[]{78,34,23,81,13,49,39,23,3,56,41,98,47,22,13,60,99,73,1,12,63,72,96,76,28,40,41,59,78,36,67,94,80},new int[]{49,16,72,51,7,35,73,49,91,86,45,12,4,60,56,32,55,92,19,93,55,11,79,31,58,36,61,16,68,36,80,2,61},new int[]{5,36,19,30,33,96,99,83,98,89,30,33,31,36,31,65,94,40,31,13,42,60,66,2,74,95,41,77,59,60,23,29,50},new int[]{44,80,2,23,40,79,46,11,47,85,79,1,36,61,2,56,79,51,31,3,44,76,47,12,37,43,13,43,47,2,98,56,7},new int[]{16,78,74,73,14,67,14,10,48,6,18,81,76,3,95,20,59,93,2,69,49,45,12,25,31,17,37,17,9,21,88,21,10},new int[]{76,93,65,22,27,8,28,66,46,92,12,73,84,28,43,95,15,83,77,90,32,85,52,89,21,82,11,21,11,98,70,31,43},new int[]{44,70,41,47,92,72,99,44,62,51,70,76,10,37,50,27,39,42,81,59,82,41,33,57,57,4,14,34,95,59,33,16,2},new int[]{22,63,34,90,6,55,79,36,55,52,96,12,19,95,26,58,31,41,77,55,25,22,13,64,39,2,53,77,70,60,40,99,14},new int[]{81,48,68,96,21,87,19,85,97,55,12,43,26,17,74,82,37,66,79,27,39,8,33,69,69,51,64,64,65,55,69,40,64},new int[]{87,40,17,98,18,93,65,49,93,30,55,5,70,42,31,1,23,72,23,4,25,27,77,39,19,20,89,83,70,31,97,14,67},new int[]{13,48,77,97,13,89,48,57,27,18,84,78,58,84,73,45,97,6,12,27,63,83,59,51,75,15,28,89,14,24,34,91,77},new int[]{92,66,37,4,47,78,71,32,83,73,64,91,27,29,83,9,39,58,80,63,43,59,14,22,75,40,39,66,91,12,83,94,59},new int[]{76,33,76,72,72,20,38,51,14,15,85,73,91,6,11,38,69,33,33,80,82,48,38,10,66,80,57,74,23,85,93,17,63}});
    param0.add(new int[][]{new int[]{20,59,92,38,68,74,80,12,75,17,90,28,32,68,51,92,9,87,92,42,1,58,4,54,95,81,87,47,29,71,32},new int[]{91,56,90,35,34,99,8,1,13,48,11,13,98,49,66,59,93,31,94,67,76,95,12,9,3,97,74,32,52,88,51},new int[]{78,15,37,60,60,51,19,57,62,95,22,82,60,17,70,11,38,99,11,81,53,98,69,80,85,22,66,18,6,85,35},new int[]{61,35,21,18,30,38,26,82,1,31,86,8,68,82,95,73,51,5,27,97,67,64,52,15,59,45,36,76,75,94,96},new int[]{84,55,25,87,88,21,76,60,54,69,74,12,36,77,84,1,34,16,19,69,34,75,97,87,13,52,38,9,75,94,14},new int[]{47,82,61,86,67,43,66,51,25,35,15,48,16,93,50,91,44,57,52,56,3,11,97,92,25,37,99,14,68,34,64},new int[]{31,12,98,9,45,80,4,61,55,46,38,31,40,42,27,53,49,59,20,19,62,16,9,52,95,75,87,70,96,90,74},new int[]{88,20,61,40,55,58,43,50,34,77,73,86,17,24,98,56,14,47,41,90,41,32,63,66,88,57,6,66,20,9,26},new int[]{16,54,1,53,79,34,12,30,7,23,9,46,40,45,3,44,83,99,63,56,38,76,82,11,18,59,88,74,42,21,44},new int[]{38,50,80,48,98,72,60,51,67,96,55,70,71,70,87,87,12,42,87,65,19,14,20,19,84,32,21,48,30,23,58},new int[]{7,23,15,17,86,87,76,92,19,13,15,21,65,52,12,37,74,19,13,33,73,60,39,50,37,32,62,58,10,20,31},new int[]{69,27,28,76,93,14,24,96,83,94,77,47,14,11,39,86,40,24,69,30,45,24,9,24,93,32,3,86,87,61,87},new int[]{47,83,78,32,86,32,92,82,10,76,45,83,6,77,91,63,78,24,86,61,90,51,44,88,11,81,90,33,17,23,97},new int[]{84,97,32,2,6,19,17,53,25,60,15,42,17,76,86,35,29,28,69,95,60,92,6,31,80,21,2,52,14,46,32},new int[]{1,71,62,39,44,88,75,39,9,53,48,76,63,27,69,71,22,89,15,25,1,75,39,75,31,86,52,29,38,64,76},new int[]{48,70,75,49,76,5,82,72,83,58,66,43,25,87,73,6,9,87,42,47,82,43,71,19,7,17,61,78,44,3,31},new int[]{78,89,29,56,19,7,68,28,81,68,91,88,41,98,8,3,12,11,85,78,1,21,19,69,32,72,62,9,26,20,14},new int[]{94,60,73,46,60,12,21,21,47,91,56,74,88,76,60,84,10,38,4,23,20,46,59,8,19,51,14,6,15,25,69},new int[]{4,48,57,98,25,86,76,78,66,21,16,71,18,65,95,33,10,7,50,21,81,52,30,92,15,40,7,20,90,1,9},new int[]{92,58,71,51,54,56,57,21,32,7,54,97,57,32,71,81,51,25,82,81,35,25,45,69,82,20,31,77,20,70,17},new int[]{55,96,60,73,88,63,2,90,14,37,9,94,55,44,55,96,84,54,20,90,6,54,34,7,16,58,58,88,72,44,68},new int[]{98,72,10,44,74,20,96,24,85,9,23,58,7,32,30,65,75,28,57,25,37,61,94,38,5,45,86,77,55,50,23},new int[]{9,43,13,86,41,42,4,64,59,31,90,68,99,93,10,88,89,83,84,95,52,25,99,95,75,1,27,99,92,61,95},new int[]{23,9,95,28,79,76,53,1,13,47,30,14,81,43,84,84,99,77,44,52,47,35,90,64,77,47,66,32,77,96,40},new int[]{53,27,68,47,54,21,53,24,38,1,85,65,33,50,32,60,37,6,54,15,78,35,98,88,73,32,84,10,31,79,55},new int[]{45,44,77,84,86,83,10,64,60,57,20,71,9,92,78,61,29,62,63,39,49,58,88,5,25,61,59,55,39,12,9},new int[]{12,35,58,74,10,97,46,66,22,77,6,87,64,20,55,65,68,10,15,51,24,96,93,36,5,20,59,3,22,76,18},new int[]{29,27,6,76,52,73,81,12,7,55,18,30,81,15,86,93,48,40,63,78,8,5,79,83,93,78,91,7,94,7,83},new int[]{10,29,80,26,28,72,4,94,69,37,89,26,40,78,22,1,99,4,73,79,51,89,83,79,30,41,17,71,10,32,99},new int[]{39,61,3,58,92,51,77,76,79,30,44,5,30,3,95,15,50,89,39,73,53,82,1,18,76,99,29,65,75,32,32},new int[]{38,40,23,94,62,91,94,42,32,52,10,23,51,7,77,52,86,13,65,12,25,26,84,32,19,36,94,91,48,50,11}});
    param0.add(new int[][]{new int[]{93,83,42,36,3,96,99,4,83,84,92,19,69,39,25,37,46,22,48,91,51,83,1,5,31,15,80,59,40,93,95},new int[]{54,11,90,56,27,57,45,62,95,13,85,33,86,20,39,58,72,86,29,60,14,95,58,85,72,58,90,6,73,96,83},new int[]{33,22,85,19,97,11,52,56,85,45,6,97,69,99,37,43,16,45,91,6,44,85,1,20,38,8,8,43,76,88,25},new int[]{69,43,13,63,41,26,51,26,83,20,65,38,60,76,13,80,51,90,70,63,88,47,82,52,15,55,98,12,36,21,81},new int[]{2,91,37,21,77,38,47,83,46,50,21,80,13,54,53,31,44,94,85,47,20,54,23,60,86,86,56,35,86,88,18},new int[]{46,75,65,1,94,23,37,13,73,70,90,44,12,54,50,69,28,80,64,10,44,71,6,68,63,79,22,10,96,19,95},new int[]{13,71,30,9,50,85,17,41,16,58,27,14,25,59,51,15,48,61,50,15,39,7,79,49,43,21,28,32,60,5,8},new int[]{40,81,37,19,62,87,90,26,23,70,64,89,35,10,1,50,94,20,75,48,62,41,59,43,38,78,4,44,37,73,16},new int[]{97,37,78,7,32,92,29,80,85,68,52,98,15,27,54,46,37,33,40,20,72,68,50,49,50,22,52,96,94,54,29},new int[]{35,66,92,81,84,52,72,10,3,52,10,22,25,14,22,43,78,75,95,55,11,95,93,14,16,81,14,82,61,82,7},new int[]{92,56,47,97,57,39,82,67,14,63,49,24,27,33,12,98,16,70,55,13,12,29,59,8,15,78,60,94,36,50,79},new int[]{79,56,75,54,90,10,59,53,87,86,48,65,9,10,5,55,35,37,75,75,72,63,41,43,96,33,51,49,55,97,89},new int[]{51,24,59,88,43,51,67,10,84,22,15,62,77,24,75,34,97,71,3,46,38,59,82,53,52,69,2,57,21,89,88},new int[]{33,49,78,9,9,85,92,47,9,36,67,24,14,66,72,45,11,49,2,44,87,98,3,28,15,22,42,30,28,26,45},new int[]{30,97,41,94,2,35,30,83,75,35,77,12,40,15,9,39,64,47,63,92,54,33,23,4,3,42,32,55,16,46,20},new int[]{11,80,79,61,36,97,56,15,15,5,55,11,96,66,51,51,99,45,55,77,33,49,91,96,58,10,53,69,12,6,6},new int[]{23,73,85,83,94,51,28,20,39,36,50,60,74,68,38,30,65,71,78,69,78,87,26,49,20,44,10,72,97,1,17},new int[]{12,50,96,79,8,43,71,63,13,88,21,13,62,80,42,85,19,53,97,62,21,75,86,78,91,35,88,9,3,73,28},new int[]{28,62,83,54,34,11,79,29,20,74,75,68,46,22,4,59,89,29,24,56,8,49,12,87,89,95,90,21,48,39,29},new int[]{98,88,4,74,67,38,35,65,58,36,35,24,59,12,49,92,84,27,56,81,48,43,73,65,51,84,39,93,56,24,94},new int[]{94,92,81,45,74,80,98,72,40,20,41,34,23,59,59,28,83,13,23,74,12,89,90,82,2,12,49,50,51,2,52},new int[]{29,74,58,85,1,37,5,66,26,58,7,84,70,73,16,6,98,87,51,49,87,89,24,30,80,16,76,50,6,74,9},new int[]{14,96,38,81,29,8,19,75,17,83,63,5,57,46,3,52,46,47,94,96,18,22,77,14,9,60,94,50,7,37,30},new int[]{85,76,84,18,58,48,45,54,93,16,10,22,30,5,62,51,18,44,27,23,55,56,28,58,13,14,6,85,32,25,30},new int[]{70,19,93,74,98,7,55,67,38,49,77,85,37,65,80,83,67,15,99,71,51,81,25,77,65,37,62,80,8,78,48},new int[]{1,76,42,12,54,26,18,30,9,61,74,7,58,5,48,43,41,18,70,24,8,15,41,47,46,44,9,95,82,24,3},new int[]{17,28,29,45,1,80,41,27,18,50,1,43,84,92,19,18,23,2,68,7,18,27,32,9,65,85,21,33,89,74,72},new int[]{98,66,13,88,97,14,26,83,71,6,59,65,34,10,39,78,45,95,70,22,89,93,98,58,63,80,93,98,31,73,85},new int[]{56,76,20,78,84,26,43,32,39,14,64,37,99,54,44,6,98,26,9,29,78,19,41,51,33,37,33,93,55,93,42},new int[]{56,29,87,54,47,91,90,47,11,43,63,8,53,88,76,63,87,41,64,81,39,85,74,56,4,3,58,86,20,85,53},new int[]{64,65,80,69,83,7,3,64,27,52,18,45,3,51,86,16,59,73,4,48,47,20,20,34,74,40,16,37,30,86,93}});
    List<Integer> param1 = new ArrayList<>();
    param1.add(0);
    param1.add(1);
    param1.add(4);
    param1.add(4);
    param1.add(17);
    param1.add(4);
    param1.add(35);
    param1.add(30);
    param1.add(25);
    param1.add(29);
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(param0.get(i),param1.get(i)) == f_gold(param0.get(i),param1.get(i)))
        {
            n_success+=1;
        }
    }
    System.out.println(n_success + " " + param0.size());
}
}