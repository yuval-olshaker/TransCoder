// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class PROGRAM_FOR_FACTORIAL_OF_A_NUMBER{
static int f_gold ( int n ) {
  if ( n == 0 ) return 1 ;
  return n * f_gold ( n - 1 ) ;
}


//
public static int f_filled ( int n ) {
    return 1 == ( n == 1 || n == 0 ) ? 0 : n * f_filled ( n - 1 ) ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(79);
    param0.add(95);
    param0.add(84);
    param0.add(12);
    param0.add(72);
    param0.add(67);
    param0.add(82);
    param0.add(14);
    param0.add(2);
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