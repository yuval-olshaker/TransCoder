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
public class FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES_1{
static int f_gold ( int arr [ ] , int n ) {
  HashMap < Integer , Integer > hmap = new HashMap < > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( hmap . containsKey ( arr [ i ] ) ) {
      int val = hmap . get ( arr [ i ] ) ;
      hmap . put ( arr [ i ] , val + 1 ) ;
    }
    else hmap . put ( arr [ i ] , 1 ) ;
  }
  for ( Integer a : hmap . keySet ( ) ) {
    if ( hmap . get ( a ) % 2 != 0 ) return a ;
  }
  return - 1 ;
}


//
public static int f_filled ( int arr [ ] , int size ) {
  Map < Integer , Integer > Hash = Maps . newHashMap ( ) ;
  for ( int i = 0 ;
  i < size ;
  i ++ ) {
    Hash . put ( arr [ i ] , Hash . get ( arr [ i ] ) + 1 ) ;
    ;
  }
  for ( int i = 0 ;
  i < Hash . size ( ) ;
  i ++ ) {
    if ( ( Hash . get ( i ) % 2 != 0 ) && ( Hash . get ( i ) % 2 != 0 ) ) {
      return i ;
    }
  }
  return - 1 ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<int [ ]> param0 = new ArrayList<>();
    param0.add(new int[]{49,90});
    param0.add(new int[]{-96,94,92,-24,48,54,-30,-86,28,-18,12,-64,-36,68,68,-78,-6,30,-84,20,52,-36,40,-62,90,-48,86,98,12,44,98,-66,52,34,36,76,-50,-20,-20,-20});
    param0.add(new int[]{0,1});
    param0.add(new int[]{79,55,18,99,38,93,19,49,21,74,16,76,82,52,86,17,42,9,6,63,1,40,75,59,41,81});
    param0.add(new int[]{-90,-84,-82,-68,-66,-66,-60,-60,-48,-44,-36,-34,-30,-16,-14,-12,-10,-6,2,10,10,14,22,26,30,34,46,50,52,62,64,64,66,72,74,78,78,82,84,88,92});
    param0.add(new int[]{1,1,0,0,1,0,1,1,0,0,1,1,1,1,0,0,1,1,1,0,1,0,0,1,0,1});
    param0.add(new int[]{2,4,5,7,7,18,18,23,23,25,25,31,41,43,45,46,52,52,55,64,69,69,80,81,84,90,91,93,94,94,94,94,96,98,99});
    param0.add(new int[]{86,66,-8,2,-18,-22,38,4,-38,-54,78,64,78,20,-32,84,-70,66,-46,12,-12,8,44,14,20});
    param0.add(new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1});
    param0.add(new int[]{11,4,98,38,20,41,1,8});
    List<Integer> param1 = new ArrayList<>();
    param1.add(1);
    param1.add(39);
    param1.add(1);
    param1.add(23);
    param1.add(23);
    param1.add(18);
    param1.add(20);
    param1.add(20);
    param1.add(21);
    param1.add(7);
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