// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class CHECK_EXIST_TWO_ELEMENTS_ARRAY_WHOSE_SUM_EQUAL_SUM_REST_ARRAY{
static boolean f_gold ( int arr [ ] , int n ) {
  int sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    sum += arr [ i ] ;
  }
  if ( sum % 2 != 0 ) {
    return false ;
  }
  sum = sum / 2 ;
  HashSet < Integer > s = new HashSet < Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int val = sum - arr [ i ] ;
    if ( s . contains ( val ) && val == ( int ) s . toArray ( ) [ s . size ( ) - 1 ] ) {
      System . out . printf ( "Pair elements are %d and %d\n" , arr [ i ] , val ) ;
      return true ;
    }
    s . add ( arr [ i ] ) ;
  }
  return false ;
}


//
public static boolean f_filled ( int [ ] arr , int n ) {
  Set < Integer > s = new HashSet < Integer > ( ) ;
  int sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    sum += arr [ i ] ;
  }
  if ( sum % 2 != 0 ) {
    return false ;
  }
  sum = sum / 2 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int val = sum - arr [ i ] ;
    if ( arr [ i ] != 0 ) {
      s . add ( arr [ i ] ) ;
    }
    if ( val < s . size ( ) ) {
      System . out . println ( "Pair elements are" + arr [ i ] + " and" + Integer . toString ( val ) ) ;
    }
  }
  return true ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<int [ ]> param0 = new ArrayList<>();
    param0.add(new int[]{2, 11, 5, 1, 4, 7});
    param0.add(new int[]{2, 4, 2, 1, 11, 15});
    param0.add(new int[]{0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1});
    param0.add(new int[]{69,6,24,30,75,37,61,76,19,18,90,9,49,24,58,97,18,85,24,93,71,98,92,59,75,75,75,70,35,58,50,1,64,66,33});
    param0.add(new int[]{-94,-94,-92,-74,-60,-58,-56,-44,-42,-40,-28,-14,2,4,14,20,24,28,40,42,42,66,78,78,80,82,96});
    param0.add(new int[]{1,0,1,1,0,0,1,1,0,0,1,1,0,1});
    param0.add(new int[]{21,26,26,27,61,62,96});
    param0.add(new int[]{-54,86,20,26});
    param0.add(new int[]{0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1});
    param0.add(new int[]{44,35,26,15,56,6,36,53,15,66,20,53,99,96,51,12,61,19,79,40,99,42,86,8,11,54,93,46,23,47,41,26,66,5,86,52,64,51,4,21,63,14,7,53,31,8,9,63});
    List<Integer> param1 = new ArrayList<>();
    param1.add(6);
    param1.add(6);
    param1.add(13);
    param1.add(18);
    param1.add(26);
    param1.add(10);
    param1.add(6);
    param1.add(3);
    param1.add(4);
    param1.add(31);
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