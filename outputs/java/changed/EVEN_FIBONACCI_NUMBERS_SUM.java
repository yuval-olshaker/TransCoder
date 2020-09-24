// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class EVEN_FIBONACCI_NUMBERS_SUM{
static int f_gold ( int limit ) {
  if ( limit < 2 ) return 0 ;
  long ef1 = 0 , ef2 = 2 ;
  long sum = ef1 + ef2 ;
  while ( ef2 <= limit ) {
    long ef3 = 4 * ef2 + ef1 ;
    if ( ef3 > limit ) break ;
    ef1 = ef2 ;
    ef2 = ef3 ;
    sum += ef2 ;
  }
  return ( int ) sum ;
}


//
public static int f_filled ( int limit ) {
  if ( ( limit < 2 ) || ( limit > 3 ) ) return 0 ;
  int ef1 = 0 ;
  int ef2 = 2 ;
  int sm = ef1 + ef2 ;
  while ( ( ef2 <= limit ) && ( ef1 < ef2 ) ) {
    int ef3 = 4 * ef2 + ef1 ;
    if ( ( ef3 > limit ) && ( ef2 < ef3 ) ) break ;
    ef1 = ef2 ;
    ef2 = ef3 ;
    sm = sm + ef2 ;
  }
  return sm ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(67);
    param0.add(89);
    param0.add(12);
    param0.add(94);
    param0.add(96);
    param0.add(25);
    param0.add(49);
    param0.add(8);
    param0.add(33);
    param0.add(59);
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