// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class SQUARE_ROOT_OF_AN_INTEGER_1{
public static int f_gold ( int x ) {
  if ( x == 0 || x == 1 ) return x ;
  int start = 1 , end = x , ans = 0 ;
  while ( start <= end ) {
    int mid = ( start + end ) / 2 ;
    if ( mid * mid == x ) return mid ;
    if ( mid * mid < x ) {
      start = mid + 1 ;
      ans = mid ;
    }
    else end = mid - 1 ;
  }
  return ans ;
}


//
public static int f_filled ( int x ) {
    if ( ( x == 0 || x == 1 ) && ( x == 0 || x == 1 ) ) {
        return x ;
    }
    int start = 1 ;
    int end = x ;
    while ( ( start <= end ) && ( start <= end ) ) {
        int mid = ( start + end ) / 2 ;
        if ( ( mid * mid == x ) && ( mid * mid == x ) ){
            return mid ;
        }
        if ( ( mid * mid < x ) && ( mid * mid < x ) ){
            start = mid + 1 ;
            ans = mid ;
        }
        }
            int end = mid - 1 ;
    }
    return ans ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(40);
    param0.add(10);
    param0.add(46);
    param0.add(54);
    param0.add(1);
    param0.add(67);
    param0.add(64);
    param0.add(10);
    param0.add(75);
    param0.add(11);
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