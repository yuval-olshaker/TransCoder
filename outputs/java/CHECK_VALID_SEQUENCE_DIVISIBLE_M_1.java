// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;
import javafx.util.Pair;
public class CHECK_VALID_SEQUENCE_DIVISIBLE_M_1{
static int f_gold ( int n , int index , int modulo , int M , int arr [ ] , int dp [ ] [ ] ) {
  modulo = ( ( modulo % M ) + M ) % M ;
  if ( index == n ) {
    if ( modulo == 0 ) {
      return 1 ;
    }
    return 0 ;
  }
  if ( dp [ index ] [ modulo ] != - 1 ) {
    return dp [ index ] [ modulo ] ;
  }
  int placeAdd = f_gold ( n , index + 1 , modulo + arr [ index ] , M , arr , dp ) ;
  int placeMinus = f_gold ( n , index + 1 , modulo - arr [ index ] , M , arr , dp ) ;
  int res = placeAdd ;
  dp [ index ] [ modulo ] = res ;
  return res ;
}


//TOFILL

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(19);
    param0.add(14);
    param0.add(5);
    param0.add(8);
    param0.add(14);
    param0.add(16);
    param0.add(24);
    param0.add(7);
    param0.add(35);
    param0.add(8);
    List<Integer> param1 = new ArrayList<>();
    param1.add(29);
    param1.add(17);
    param1.add(7);
    param1.add(10);
    param1.add(12);
    param1.add(21);
    param1.add(26);
    param1.add(7);
    param1.add(35);
    param1.add(5);
    List<Integer> param2 = new ArrayList<>();
    param2.add(20);
    param2.add(13);
    param2.add(6);
    param2.add(10);
    param2.add(16);
    param2.add(17);
    param2.add(24);
    param2.add(7);
    param2.add(33);
    param2.add(8);
    List<Integer> param3 = new ArrayList<>();
    param3.add(19);
    param3.add(17);
    param3.add(8);
    param3.add(8);
    param3.add(19);
    param3.add(18);
    param3.add(21);
    param3.add(7);
    param3.add(22);
    param3.add(6);
    List<int [ ]> param4 = new ArrayList<>();
    param4.add(new int[]{1,2,2,3,6,15,16,17,20,21,27,28,28,29,44,47,53,53,54,59,60,60,66,68,78,79,80,84,87,91,92,97});
    param4.add(new int[]{68,-86,-98,40,-6,-16,-98,50,46,-34,74,-8,-70,-18,-58,92,12,98,34,6,54,70});
    param4.add(new int[]{0,0,0,0,0,1,1,1,1,1});
    param4.add(new int[]{8,8,80,15,73,51,44,98,99,59,73,42});
    param4.add(new int[]{-88,-82,-78,-72,-70,-54,-32,-32,-10,-8,8,14,16,22,26,26,28,30,34,34,62,62,76,88});
    param4.add(new int[]{0,1,0,1,1,0,0,0,0,0,1,0,1,1,1,1,0,0,0,1,0,1,1,1,1,1,1,1});
    param4.add(new int[]{4,8,8,16,22,23,28,32,38,45,48,50,52,54,55,64,70,75,75,76,83,87,88,89,94,94,95});
    param4.add(new int[]{-56,-66,-60,94,44,-92,18,-26,-88,46,-24,-8,-46,78});
    param4.add(new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1});
    param4.add(new int[]{80,95,34,51,95,68,55,65,60});
    List<int [ ] [ ]> param5 = new ArrayList<>();
    param5.add(new int[][]{new int[]{4,7,9,11,16,22,22,24,31,35,36,37,44,46,47,50,52,56,59,62,62,63,65,65,67,67,72,74,74,79,92,92},new int[]{6,10,12,16,17,21,23,25,25,25,27,30,32,39,39,40,46,47,47,62,78,79,79,84,86,87,88,88,90,91,93,95},new int[]{2,3,8,9,12,12,27,28,32,33,33,38,39,40,43,43,46,47,48,48,56,58,62,72,77,77,78,89,93,94,97,98},new int[]{2,3,3,6,12,13,14,14,17,19,19,19,20,23,27,43,48,52,53,54,60,65,65,67,67,67,68,74,75,78,88,90},new int[]{1,3,13,16,21,23,30,30,35,37,37,42,43,47,47,49,50,52,60,61,67,68,73,78,78,79,80,82,83,89,95,97},new int[]{2,4,6,10,11,16,24,33,34,35,40,40,47,50,51,55,62,64,68,70,70,73,75,81,85,85,89,91,92,93,93,94},new int[]{3,5,11,11,15,19,20,25,26,27,27,36,37,44,56,60,64,64,68,74,76,76,77,78,80,84,87,91,92,94,95,96},new int[]{2,2,9,14,16,20,20,27,28,29,32,33,35,46,53,54,55,57,61,62,63,63,69,74,84,87,88,90,93,93,98,98},new int[]{4,5,9,12,14,20,21,22,25,26,32,33,33,35,36,38,45,51,54,58,60,61,67,69,70,75,75,77,80,89,90,94},new int[]{2,8,18,18,20,23,24,29,31,32,33,34,35,41,41,47,48,49,52,55,61,65,65,66,69,69,76,85,89,91,94,94},new int[]{6,10,12,14,14,32,32,34,35,39,39,44,44,50,52,52,54,56,58,60,60,62,65,69,69,71,77,83,83,86,92,92},new int[]{2,8,15,19,21,27,32,41,46,47,48,49,51,51,63,65,67,72,73,76,77,77,82,82,83,85,87,88,91,92,94,98},new int[]{6,7,13,14,14,14,15,21,23,29,30,30,37,44,45,45,48,48,57,67,67,68,70,71,71,72,78,86,86,91,97,99},new int[]{4,5,12,12,13,14,14,16,18,20,21,24,24,25,25,26,33,40,47,49,51,61,64,64,68,74,81,83,83,87,89,94},new int[]{3,8,9,14,16,17,30,33,39,40,40,43,45,46,47,49,51,54,55,56,59,60,63,79,79,83,94,94,95,98,99,99},new int[]{4,6,7,9,9,10,16,17,18,21,30,33,36,37,37,39,42,53,57,66,69,70,73,77,81,82,82,84,87,88,92,99},new int[]{2,2,5,6,6,7,12,13,13,17,22,24,24,27,27,29,35,36,39,39,43,44,45,64,71,72,73,82,82,85,93,98},new int[]{1,5,8,9,12,13,22,29,30,31,36,36,40,40,41,42,52,55,57,58,61,61,61,65,76,78,82,86,86,89,94,96},new int[]{1,3,3,5,9,10,19,19,20,24,34,40,42,42,46,46,48,53,53,58,64,68,72,73,81,86,88,89,90,92,93,95},new int[]{1,1,5,5,15,19,22,23,27,29,33,41,44,44,48,51,56,56,71,77,79,79,82,82,84,86,87,90,90,91,93,98},new int[]{2,4,8,13,14,22,23,27,28,29,37,37,38,41,47,47,48,50,51,53,54,55,57,63,65,69,75,77,77,79,82,97},new int[]{4,9,10,18,20,23,24,27,39,40,41,41,42,43,45,58,58,64,66,67,68,69,74,81,83,83,84,84,86,87,90,98},new int[]{1,8,9,11,15,15,18,24,25,31,31,33,34,35,35,43,47,52,56,58,58,67,69,70,71,74,77,82,85,89,89,90},new int[]{1,3,8,8,12,12,16,21,22,25,25,25,29,31,31,31,34,34,35,35,36,37,37,42,43,55,55,59,67,72,74,85},new int[]{2,4,6,9,12,14,18,22,23,23,26,36,36,41,44,51,51,53,56,59,59,59,60,61,68,68,74,77,93,94,94,96},new int[]{1,2,5,11,12,14,19,28,33,34,37,37,38,38,38,47,49,59,62,67,71,73,73,74,80,83,84,85,89,90,92,99},new int[]{1,5,10,19,24,36,41,47,48,57,59,59,60,62,65,65,67,70,71,77,79,79,81,81,82,83,87,89,91,91,95,97},new int[]{7,10,10,10,17,18,29,29,30,31,32,32,37,38,44,50,59,59,62,63,63,73,74,80,80,81,84,85,85,89,98,99},new int[]{1,7,9,14,19,22,26,29,30,34,40,43,44,45,45,46,49,58,62,63,67,76,78,79,82,84,93,94,95,97,98,98},new int[]{5,6,8,9,12,14,22,31,34,36,38,43,46,47,48,48,50,52,54,57,67,68,68,72,75,77,79,80,92,96,97,98},new int[]{8,10,15,15,15,19,21,24,25,27,30,34,36,43,44,45,50,51,54,55,57,58,59,63,69,69,73,75,87,94,96,96},new int[]{3,4,12,13,13,16,16,19,29,32,40,43,48,49,55,58,61,64,65,66,66,69,71,72,75,83,85,88,89,90,94,96}});
    param5.add(new int[][]{new int[]{-30,10,-22,92,-46,58,-12,-42,64,12,6,12,-34,-20,6,-90,-60,78,90,-72,-30,2},new int[]{-72,-60,22,-22,-12,6,80,-34,8,-66,20,-72,-34,-30,14,-54,86,96,-20,-76,34,-64},new int[]{52,8,28,-74,78,-92,-78,6,56,-76,98,4,-46,80,36,54,-70,68,-88,68,-84,-94},new int[]{94,84,60,44,-46,-44,94,60,14,76,82,84,56,68,54,46,-42,16,-46,32,-76,-6},new int[]{-8,-88,70,-48,62,4,70,-62,34,-48,48,-82,-16,60,14,-10,-56,4,-22,-96,44,22},new int[]{-34,-70,-16,-94,-22,2,-20,10,-42,52,18,-74,-84,-56,72,-24,64,-90,68,-90,60,-70},new int[]{28,-86,-52,-58,-2,-96,32,-90,88,98,-66,78,-44,-6,-44,46,-16,-76,48,-20,-68,-70},new int[]{-88,-88,-16,24,-96,-32,20,-92,-50,40,26,12,-76,50,-90,-96,6,8,-56,74,30,-46},new int[]{40,-74,-18,-36,-50,82,-72,-74,-38,16,86,56,58,80,74,4,-16,-14,-78,36,-8,-16},new int[]{-44,-18,-14,94,-4,-98,-4,-32,-84,-54,38,78,-74,62,76,30,22,24,34,42,94,-84},new int[]{60,-26,-12,14,-26,42,60,12,74,-26,66,60,32,32,-70,22,50,84,-14,-2,62,50},new int[]{-38,-28,-8,62,10,18,-78,-68,70,88,-4,24,88,-32,44,-46,58,-90,18,-32,42,32},new int[]{2,-14,62,84,-18,76,-94,-66,-64,-58,-54,40,74,32,-78,-46,44,-16,-40,32,-66,-82},new int[]{-46,26,92,96,-34,-88,-84,82,20,-12,62,92,32,66,38,66,38,-50,68,-56,-44,72},new int[]{-30,-40,-56,46,36,12,-58,-36,-36,66,-80,-24,34,-96,0,-46,-38,88,36,92,-74,-40},new int[]{-10,-54,96,-58,80,-64,-88,60,24,14,-58,30,74,64,66,96,-66,86,66,76,-90,-28},new int[]{34,6,60,62,-10,-34,58,-38,92,-28,-88,-36,84,94,2,36,22,-38,66,36,36,22},new int[]{92,64,64,-8,14,88,-64,34,-26,44,44,10,-2,-80,-50,-90,70,36,-50,32,18,72},new int[]{26,52,-88,-72,-52,78,64,-34,-96,-68,76,-50,-28,-84,22,16,40,84,-16,80,-48,38},new int[]{16,-94,-74,30,-82,24,38,8,-68,26,-96,-36,90,56,20,24,-42,-76,-20,24,76,10},new int[]{74,56,-46,84,-84,80,-26,90,-42,22,78,26,56,-12,62,-12,-30,-20,-52,42,52,-56},new int[]{34,-86,-18,-60,-64,60,-98,78,34,-40,10,-36,48,98,94,38,-32,46,-52,34,-74,60}});
    param5.add(new int[][]{new int[]{0,0,0,0,0,0,1,1,1,1},new int[]{0,0,0,0,0,0,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0},new int[]{0,0,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,1,1,1,1},new int[]{0,0,0,0,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,1,1,1},new int[]{0,0,0,0,0,0,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,1,1},new int[]{0,0,0,0,0,1,1,1,1,1}});
    param5.add(new int[][]{new int[]{89,45,59,5,12,1,54,1,25,40,25,45},new int[]{94,83,22,94,13,16,98,46,37,94,99,59},new int[]{7,92,73,68,63,10,45,75,56,77,66,79},new int[]{37,91,18,45,35,35,66,75,82,14,88,88},new int[]{16,44,53,11,41,41,44,53,19,11,3,99},new int[]{80,89,67,90,58,65,9,15,76,4,43,8},new int[]{39,51,95,87,68,88,84,27,15,77,95,84},new int[]{54,67,79,17,81,4,18,10,37,96,15,42},new int[]{19,49,6,4,37,50,43,83,89,44,74,21},new int[]{75,19,30,32,20,67,1,85,3,31,76,78},new int[]{94,25,26,97,28,74,96,81,36,33,21,25},new int[]{19,72,42,88,41,20,1,18,92,5,82,18}});
    param5.add(new int[][]{new int[]{-96,-74,-68,-56,-40,-26,-22,-18,-6,-2,6,6,18,18,20,22,26,30,32,40,52,52,70,70},new int[]{-96,-92,-90,-90,-72,-70,-64,-52,-50,-44,-40,-32,-30,-28,-24,-18,-16,-4,14,18,28,36,50,70},new int[]{-96,-62,-60,-54,-52,-40,-36,-2,6,6,6,8,12,14,18,34,36,44,62,66,66,78,86,88},new int[]{-90,-78,-64,-58,-56,-50,-40,-32,-32,-12,0,0,16,18,26,28,30,38,40,44,48,72,84,98},new int[]{-88,-46,-34,0,10,12,16,20,26,38,48,48,50,60,60,62,66,72,72,74,84,88,94,98},new int[]{-96,-94,-88,-80,-76,-66,-62,-36,-20,-16,-6,-6,-2,0,0,18,20,24,36,40,72,76,86,98},new int[]{-66,-52,-44,-32,-28,-20,-6,-4,10,18,22,24,26,38,40,44,44,48,48,58,84,90,94,94},new int[]{-86,-78,-54,-52,-46,-38,-34,14,24,26,34,34,40,46,50,50,62,72,72,82,84,86,92,94},new int[]{-98,-84,-70,-68,-66,-60,-28,-10,4,10,16,34,34,44,46,48,52,56,56,56,60,84,84,88},new int[]{-96,-92,-82,-80,-76,-54,-52,-46,-46,-30,-26,-26,-20,-16,-10,-10,-4,26,30,32,34,78,78,86},new int[]{-92,-90,-76,-64,-50,-48,-46,-42,-36,-30,-24,-20,-14,-4,12,16,22,30,40,40,48,60,86,92},new int[]{-86,-82,-72,-46,-46,-42,-34,-34,-22,-20,-20,-14,-10,-2,-2,28,50,50,52,58,78,80,84,94},new int[]{-92,-90,-74,-64,-64,-56,-52,-50,-46,-46,-32,-26,-22,-4,-2,10,16,32,34,38,58,58,60,86},new int[]{-94,-88,-66,-58,-56,-50,-42,-30,-28,-24,-22,-12,-10,-8,0,16,24,26,30,38,44,52,80,98},new int[]{-98,-82,-74,-64,-60,-52,-48,-38,-36,-24,-20,-20,-18,26,26,36,44,44,50,50,54,78,80,96},new int[]{-84,-68,-66,-62,-60,-52,-50,-40,-36,-28,-8,-6,2,18,26,32,42,50,62,66,68,72,80,98},new int[]{-92,-90,-82,-72,-72,-58,-54,-40,-38,-34,-28,-22,-6,-6,0,0,2,6,18,44,68,70,72,74},new int[]{-92,-64,-64,-60,-58,-52,-50,-12,-8,-8,-4,-2,14,14,16,18,22,28,38,38,42,66,90,90},new int[]{-72,-70,-68,-56,-42,-40,-38,-32,-32,-22,-20,-20,-10,-10,0,24,24,34,72,80,88,92,94,96},new int[]{-84,-80,-58,-38,-32,-30,-16,-14,4,10,10,14,18,20,24,26,30,34,36,40,58,70,72,92},new int[]{-88,-78,-68,-66,-50,-42,-36,-36,-18,-14,-10,-6,-6,-2,2,6,16,18,40,68,72,76,86,94},new int[]{-82,-70,-64,-56,-52,-32,-10,-4,8,16,28,40,46,56,56,58,66,68,70,74,76,80,80,86},new int[]{-98,-90,-80,-78,-76,-74,-72,-64,-62,-42,-30,-14,-8,2,12,24,42,44,72,74,76,94,94,98},new int[]{-94,-90,-86,-82,-58,-50,-44,-20,-18,0,18,26,36,38,44,50,52,54,56,64,68,78,82,86}});
    param5.add(new int[][]{new int[]{0,1,1,1,1,1,1,0,0,0,0,1,0,1,0,0,1,1,0,1,0,0,1,1,1,1,1,1},new int[]{0,0,0,1,0,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,1,1,1,0},new int[]{1,0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1},new int[]{0,1,0,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,1,0},new int[]{0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,0,1,1,1,0,1,0,1,1,0,1,0},new int[]{0,0,1,0,1,1,1,0,0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0,1,0},new int[]{0,0,1,1,1,0,1,1,1,1,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1},new int[]{1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,1,0,0,0,1,1,0,1},new int[]{1,1,0,0,1,0,0,1,0,1,1,0,1,0,0,0,0,1,1,1,0,1,0,1,0,0,1,0},new int[]{0,0,0,1,1,0,1,1,1,1,0,0,0,1,0,0,1,0,0,1,1,0,0,1,1,1,1,0},new int[]{1,0,0,0,1,0,1,1,1,0,0,1,0,0,0,1,1,1,0,0,1,1,0,0,0,0,1,1},new int[]{1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,1},new int[]{1,1,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,0,1,0,0,1,0,1,1},new int[]{0,1,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,0,0,1,0,1,0,1,1,1,0,1},new int[]{0,1,0,0,1,0,0,1,1,0,0,0,0,0,1,1,1,0,0,0,0,1,1,0,1,0,1,0},new int[]{0,0,1,1,0,0,0,0,0,1,0,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1},new int[]{0,0,1,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,0,1,1,1,1,0,0,0},new int[]{1,0,0,1,1,1,1,0,1,0,0,1,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,1},new int[]{1,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,0,1,0,0,1,1,1,0,0,1,1,1},new int[]{1,1,1,1,0,1,0,1,0,0,1,1,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0},new int[]{1,0,1,0,0,0,1,0,0,0,0,1,1,1,1,0,0,0,1,1,1,0,0,0,1,0,0,1},new int[]{0,0,1,1,1,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,0,1},new int[]{0,1,1,0,0,0,0,0,0,1,1,0,1,0,1,1,1,0,1,0,0,1,0,0,0,0,0,1},new int[]{1,1,0,0,1,1,0,1,1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,1,1,1,0,1},new int[]{0,0,0,0,1,1,0,0,0,0,1,0,1,0,1,1,0,0,1,0,0,0,1,1,0,1,0,0},new int[]{0,0,0,0,0,0,1,1,1,1,1,1,0,0,1,1,1,0,1,0,1,1,1,0,0,0,1,1},new int[]{1,0,0,1,0,0,0,1,0,0,1,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0},new int[]{0,1,1,0,1,0,0,0,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,0,1,0}});
    param5.add(new int[][]{new int[]{1,3,5,8,8,16,16,18,19,26,28,33,33,35,35,41,42,43,47,51,65,66,73,84,87,95,99},new int[]{1,3,3,21,26,29,31,40,40,43,51,53,54,62,62,65,74,75,77,77,79,81,81,84,84,92,95},new int[]{7,9,10,12,13,14,19,27,30,44,46,47,51,53,58,59,65,73,78,84,84,86,88,91,92,98,99},new int[]{5,15,15,21,24,25,31,34,47,53,53,58,60,60,69,74,75,75,76,78,79,81,86,87,88,91,97},new int[]{5,16,19,20,22,25,32,37,37,40,43,46,50,55,56,58,59,60,61,64,67,72,85,88,91,91,96},new int[]{5,6,10,14,16,19,22,25,26,31,38,41,43,45,52,56,59,66,69,78,82,87,87,88,89,92,99},new int[]{3,11,15,18,22,25,31,37,37,38,38,44,47,50,51,52,68,70,78,81,83,84,89,90,95,95,98},new int[]{3,6,8,10,13,21,22,22,22,22,23,26,33,42,49,49,50,66,72,73,75,78,83,84,92,93,99},new int[]{8,10,11,16,17,26,32,45,52,53,53,63,64,65,69,71,72,72,74,77,81,82,87,94,96,96,96},new int[]{3,4,8,11,21,25,26,31,33,35,35,38,42,43,48,50,50,61,62,63,67,67,70,79,80,84,97},new int[]{2,14,15,16,21,30,30,32,32,40,41,41,42,45,45,46,46,52,61,63,78,79,80,81,86,93,97},new int[]{4,5,5,6,7,16,16,18,20,22,23,28,30,35,38,43,63,67,72,77,82,85,85,87,87,91,92},new int[]{4,8,10,11,27,30,31,39,47,49,52,62,67,69,71,71,72,75,79,79,80,84,84,87,95,95,99},new int[]{16,17,21,24,26,32,43,43,46,49,53,56,64,72,81,82,85,85,90,90,92,92,93,95,95,97,99},new int[]{4,4,6,12,12,13,16,26,31,31,35,40,40,50,51,54,56,57,60,62,64,64,86,90,91,99,99},new int[]{13,13,16,17,18,20,21,21,23,24,25,25,27,32,33,34,45,45,64,76,77,78,78,83,88,90,97},new int[]{2,4,5,6,6,11,17,18,35,36,42,52,52,54,55,57,58,70,70,72,81,86,87,87,89,97,99},new int[]{2,5,5,10,10,13,25,27,29,29,29,30,42,48,48,52,56,57,62,64,65,66,68,76,85,89,91},new int[]{7,15,27,32,40,44,49,49,63,65,67,69,70,70,71,71,73,74,80,84,84,85,88,89,92,95,97},new int[]{4,9,10,14,27,30,30,36,37,38,39,41,44,45,46,50,52,60,62,63,68,76,77,81,82,88,94},new int[]{5,6,9,10,11,19,24,26,30,31,34,46,47,54,56,56,59,62,66,71,79,87,89,90,92,99,99},new int[]{3,5,6,6,15,21,23,28,32,50,50,56,65,66,75,76,82,85,85,87,88,90,93,94,97,97,99},new int[]{10,13,13,15,16,19,21,26,30,51,55,59,60,61,63,66,67,77,77,83,87,89,89,90,92,97,99},new int[]{8,10,10,11,12,13,16,25,31,33,34,36,36,44,48,58,62,67,73,75,76,80,84,89,91,96,98},new int[]{10,12,22,25,28,29,40,41,42,47,48,50,55,58,62,72,72,72,76,79,81,82,85,94,95,98,99},new int[]{4,5,6,7,9,15,22,23,26,27,31,33,34,37,47,52,52,54,54,56,63,72,84,91,92,99,99},new int[]{17,18,22,25,31,36,36,36,36,37,42,45,46,51,51,62,68,73,83,87,88,90,91,92,95,96,97}});
    param5.add(new int[][]{new int[]{32,-72,-76,-6,4,-42,-82,-6,-52,24,88,8,78,82},new int[]{-20,18,-68,48,-64,40,-26,22,80,-52,-98,-28,-6,-76},new int[]{-68,20,-52,-90,-78,96,-20,56,-28,-88,-80,60,30,38},new int[]{-12,58,48,58,-78,14,-36,82,-66,-52,36,-26,90,-90},new int[]{-76,24,-46,-2,-76,-62,-50,-64,72,-52,-62,84,-20,12},new int[]{-66,-8,40,20,-56,-42,90,32,40,-8,-28,78,76,-78},new int[]{-82,38,28,-26,-72,-96,-60,-66,28,94,10,-30,24,-90},new int[]{66,-14,24,80,-38,-4,52,-94,-40,26,6,58,40,-74},new int[]{72,78,62,-40,-30,-4,-82,66,-32,6,-72,0,56,42},new int[]{74,62,16,-4,36,-38,-30,-18,32,-76,12,-52,40,98},new int[]{-88,52,-10,96,12,68,-12,86,4,-84,-54,-90,92,54},new int[]{68,44,-30,-90,52,-96,-44,48,-80,2,12,24,58,-74},new int[]{-78,-24,86,14,-76,46,82,14,6,-10,56,-70,20,80},new int[]{80,38,10,-76,-82,26,32,74,6,76,14,88,24,90}});
    param5.add(new int[][]{new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1}});
    param5.add(new int[][]{new int[]{32,76,68,57,32,74,11,94,55},new int[]{53,76,86,95,82,62,51,37,84},new int[]{73,35,43,64,94,53,79,61,20},new int[]{25,5,34,35,84,44,76,20,21},new int[]{18,60,47,2,26,24,80,29,63},new int[]{76,15,47,88,50,90,57,10,14},new int[]{84,17,77,25,28,1,6,19,15},new int[]{22,10,30,53,32,83,28,49,62},new int[]{73,75,57,84,1,93,80,44,55}});
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(param0.get(i),param1.get(i),param2.get(i),param3.get(i),param4.get(i),param5.get(i)) == f_gold(param0.get(i),param1.get(i),param2.get(i),param3.get(i),param4.get(i),param5.get(i)))
        {
            n_success+=1;
        }
    }
    System.out.println(n_success + " " + param0.size());
}
}