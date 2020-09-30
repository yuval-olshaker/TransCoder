// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class EFFICIENT_WAY_TO_MULTIPLY_WITH_7{
static int f_gold ( int n ) {
  return ( ( n << 3 ) - n ) ;
}


//
public static int f_filled ( int n ) {
    return ( ( n << 3 ) - n ) ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(41);
    param0.add(42);
    param0.add(62);
    param0.add(4);
    param0.add(31);
    param0.add(75);
    param0.add(5);
    param0.add(75);
    param0.add(85);
    param0.add(19);
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