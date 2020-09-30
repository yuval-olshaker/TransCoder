// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class PROGRAM_FOR_FACTORIAL_OF_A_NUMBER_2{
static int f_gold ( int n ) {
  return ( n == 1 || n == 0 ) ? 1 : n * f_gold ( n - 1 ) ;
}


//
public static int f_filled ( int n ) {
    return 1 == ( n == 1 || n == 0 ) ? 0 : n * f_filled ( n - 1 ) ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(24);
    param0.add(46);
    param0.add(47);
    param0.add(41);
    param0.add(98);
    param0.add(69);
    param0.add(83);
    param0.add(2);
    param0.add(12);
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