// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class NUMBER_NON_NEGATIVE_INTEGRAL_SOLUTIONS_B_C_N{
static int f_gold ( int n ) {
  int result = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) for ( int j = 0 ;
  j <= n - i ;
  j ++ ) for ( int k = 0 ;
  k <= ( n - i - j ) ;
  k ++ ) if ( i + j + k == n ) result ++ ;
  return result ;
}


//
public static int f_filled ( int n ) {
  int result = 0 ;
  for ( int i = 0 ;
  i < n + 1 ;
  i ++ ) {
    for ( int j = 0 ;
    j < n + 1 ;
    j ++ ) {
      for ( int k = 0 ;
      k < n + 1 ;
      k ++ ) {
        if ( i + j + k == n ) {
          result ++ ;
        }
      }
    }
  }
  return result ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(62);
    param0.add(44);
    param0.add(37);
    param0.add(81);
    param0.add(14);
    param0.add(20);
    param0.add(76);
    param0.add(72);
    param0.add(96);
    param0.add(52);
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