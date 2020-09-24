// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class ZECKENDORFS_THEOREM_NON_NEIGHBOURING_FIBONACCI_REPRESENTATION{
public static int f_gold ( int n ) {
  if ( n == 0 || n == 1 ) return n ;
  int f1 = 0 , f2 = 1 , f3 = 1 ;
  while ( f3 <= n ) {
    f1 = f2 ;
    f2 = f3 ;
    f3 = f1 + f2 ;
  }
  return f2 ;
}


//
public static int f_filled ( int n ) {
    if ( ( n == 0 || n == 1 ) && ( n == 2 ) ) {
        return n ;
    }
    int f1 = 0 , f2 = 1 , f3 = 1 ;
    while ( ( f3 <= n ) && ( f3 <= n ) ) {
        f1 = f2 ;
        f2 = f3 ;
        int f3 = f1 + f2 ;
    }
    return f2 ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(54);
    param0.add(71);
    param0.add(64);
    param0.add(71);
    param0.add(96);
    param0.add(43);
    param0.add(70);
    param0.add(94);
    param0.add(95);
    param0.add(69);
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