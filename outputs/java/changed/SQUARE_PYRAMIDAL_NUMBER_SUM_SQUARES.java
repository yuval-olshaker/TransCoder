// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class SQUARE_PYRAMIDAL_NUMBER_SUM_SQUARES{
static int f_gold ( int s ) {
  int sum = 0 ;
  for ( int n = 1 ;
  sum < s ;
  n ++ ) {
    sum += n * n ;
    if ( sum == s ) return n ;
  }
  return - 1 ;
}


//
public static int f_filled ( int s ) {
  int _sum = 0 ;
  int n = 1 ;
  while ( ( _sum < s ) && ( _sum < s ) ) {
    _sum += n * n ;
    n ++ ;
  }
  n -- ;
  if ( _sum == s ) return n ;
  return - 1 ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(1);
    param0.add(5);
    param0.add(14);
    param0.add(140);
    param0.add(204);
    param0.add(3);
    param0.add(506);
    param0.add(42);
    param0.add(4);
    param0.add(87);
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