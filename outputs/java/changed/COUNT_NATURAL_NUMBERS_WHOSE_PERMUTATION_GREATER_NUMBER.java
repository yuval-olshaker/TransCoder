// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class COUNT_NATURAL_NUMBERS_WHOSE_PERMUTATION_GREATER_NUMBER{
static int f_gold ( int n ) {
  int result = 0 ;
  for ( int i = 1 ;
  i <= 9 ;
  i ++ ) {
    Stack < Integer > s = new Stack < > ( ) ;
    if ( i <= n ) {
      s . push ( i ) ;
      result ++ ;
    }
    while ( ! s . empty ( ) ) {
      int tp = s . peek ( ) ;
      s . pop ( ) ;
      for ( int j = tp % 10 ;
      j <= 9 ;
      j ++ ) {
        int x = tp * 10 + j ;
        if ( x <= n ) {
          s . push ( x ) ;
          result ++ ;
        }
      }
    }
  }
  return result ;
}


//
public static int f_filled ( int n ) {
    int result = 0 ;
    for ( int i = 1 ;  i <= 10 ;  i ++ ) {
        StringBuilder sb = new StringBuilder ( ) ;
        if ( ( i <= n ) && ( i <= n ) ){
            s . add ( i ++ ) ;
            result ++ ;
        }
        while ( s . length ( ) != 0 ) {
            int tp = s . get ( s . length - 1 ) ;
            s . remove ( ) ;
            for ( int j = tp % 10 ;  j < 10 ;  j ++ ) {
                int x = tp * 10 + j ;
                if ( ( x <= n ) && ( x <= n ) ) {
                    s . add ( x ) ;
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
    param0.add(69);
    param0.add(72);
    param0.add(88);
    param0.add(7);
    param0.add(66);
    param0.add(34);
    param0.add(23);
    param0.add(37);
    param0.add(33);
    param0.add(21);
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