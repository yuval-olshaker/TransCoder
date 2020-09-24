// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class PRIMALITY_TEST_SET_5USING_LUCAS_LEHMER_SERIES{
static boolean f_gold ( int p ) {
  double checkNumber = Math . pow ( 2 , p ) - 1 ;
  double nextval = 4 % checkNumber ;
  for ( int i = 1 ;
  i < p - 1 ;
  i ++ ) nextval = ( nextval * nextval - 2 ) % checkNumber ;
  return ( nextval == 0 ) ;
}


//
public static boolean f_filled ( int p ) {
  int checkNumber = 2 * p - 1 ;
  int nextval = 4 % checkNumber ;
  for ( int i = 1 ;
  i <= p - 1 ;
  i ++ ) {
    nextval = ( nextval * nextval - 2 ) % checkNumber ;
  }
  if ( ( nextval == 0 ) && ( nextval != 1 ) ) {
    return true ;
  }
  else {
    return false ;
  }
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(11);
    param0.add(27);
    param0.add(31);
    param0.add(47);
    param0.add(3);
    param0.add(14);
    param0.add(41);
    param0.add(72);
    param0.add(39);
    param0.add(22);
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