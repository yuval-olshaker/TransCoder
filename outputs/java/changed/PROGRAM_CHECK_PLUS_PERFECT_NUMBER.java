// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class PROGRAM_CHECK_PLUS_PERFECT_NUMBER{
static boolean f_gold ( int x ) {
  int temp = x ;
  int n = 0 ;
  while ( x != 0 ) {
    x /= 10 ;
    n ++ ;
  }
  x = temp ;
  int sum = 0 ;
  while ( x != 0 ) {
    sum += Math . pow ( x % 10 , n ) ;
    x /= 10 ;
  }
  return ( sum == temp ) ;
}


//
public static boolean f_filled ( int x ) {
  int temp = x ;
  int n = 0 ;
  while ( ( x != 0 ) && ( n < 10 ) ) {
    x = x / 10 ;
    n = n + 1 ;
  }
  x = temp ;
  int sm = 0 ;
  while ( ( x != 0 ) && ( n < 10 ) ) {
    sm = sm + ( int ) ( Math . pow ( x % 10 , n ) ) ;
    x = x / 10 ;
  }
  return ( sm == temp ) ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(371);
    param0.add(9474);
    param0.add(85);
    param0.add(35);
    param0.add(54);
    param0.add(17);
    param0.add(97);
    param0.add(63);
    param0.add(12);
    param0.add(43);
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
