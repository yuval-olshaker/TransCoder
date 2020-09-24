// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class DOUBLE_FACTORIAL{
static long f_gold ( long n ) {
  if ( n == 0 || n == 1 ) return 1 ;
  return n * f_gold ( n - 2 ) ;
}


//
public static int f_filled ( int n ) {
    if ( ( n == 0 || n == 1 ) && ( n == 2 ) ) {
        return 1 ;
    }
    return n * f_filled ( n - 2 ) ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Long> param0 = new ArrayList<>();
    param0.add(52L);
    param0.add(93L);
    param0.add(15L);
    param0.add(72L);
    param0.add(61L);
    param0.add(21L);
    param0.add(83L);
    param0.add(87L);
    param0.add(75L);
    param0.add(75L);
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