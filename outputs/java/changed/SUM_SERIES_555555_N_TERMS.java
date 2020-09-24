// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class SUM_SERIES_555555_N_TERMS{
static int f_gold ( int n ) {
  return ( int ) ( 0.6172 * ( Math . pow ( 10 , n ) - 1 ) - 0.55 * n ) ;
}


//
public static int f_filled ( int n ) {
    return ( int ) ( 0.6172 * ( Math . pow ( 10 , n ) - 1 ) - 0.55 * n ) ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(18);
    param0.add(81);
    param0.add(77);
    param0.add(84);
    param0.add(87);
    param0.add(14);
    param0.add(15);
    param0.add(3);
    param0.add(21);
    param0.add(60);
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