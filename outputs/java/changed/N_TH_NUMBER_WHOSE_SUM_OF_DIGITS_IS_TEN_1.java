// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class N_TH_NUMBER_WHOSE_SUM_OF_DIGITS_IS_TEN_1{
public static int f_gold ( int n ) {
  int count = 0 ;
  for ( int curr = 19 ;
  ;
  curr += 9 ) {
    int sum = 0 ;
    for ( int x = curr ;
    x > 0 ;
    x = x / 10 ) sum = sum + x % 10 ;
    if ( sum == 10 ) count ++ ;
    if ( count == n ) return curr ;
  }
}


//
public static int f_filled ( int n ) {
  int count = 0 ;
  ;
  int curr = 19 ;
  while ( ( true ) && ( count < 10 ) ) {
    int sum = 0 ;
    int x = curr ;
    while ( ( x > 0 ) && ( x < 10 ) ) {
      sum = sum + x % 10 ;
      x = ( int ) ( x / 10 ) ;
    }
    if ( ( sum == 10 ) && ( count == 10 ) ) {
      count ++ ;
    }
    if ( ( count == n ) && ( curr == 19 ) ) {
      return curr ;
    }
    curr += 9 ;
  }
  return - 1 ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(93);
    param0.add(10);
    param0.add(55);
    param0.add(94);
    param0.add(2);
    param0.add(5);
    param0.add(37);
    param0.add(4);
    param0.add(11);
    param0.add(46);
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(param0.get(i)) == f_gold(param0.get(i)))
        {
            n_success+=1;
        }
    }
    System.out.println(n_success + " " + param0.size());
}
}