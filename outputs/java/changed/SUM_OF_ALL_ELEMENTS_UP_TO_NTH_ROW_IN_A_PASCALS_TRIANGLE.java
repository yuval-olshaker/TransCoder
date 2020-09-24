// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class SUM_OF_ALL_ELEMENTS_UP_TO_NTH_ROW_IN_A_PASCALS_TRIANGLE{
static long f_gold ( int n ) {
  long sum = 0 ;
  for ( int row = 0 ;
  row < n ;
  row ++ ) {
    sum = sum + ( 1 << row ) ;
  }
  return sum ;
}


//
public static int f_filled ( int n ) {
    int sum = 0 ;
    for ( int row = 0 ;  row < n ;  row ++ ) {
        sum = sum + ( 1 << row ) ;
    }
    return sum ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(21);
    param0.add(4);
    param0.add(31);
    param0.add(79);
    param0.add(38);
    param0.add(75);
    param0.add(36);
    param0.add(32);
    param0.add(23);
    param0.add(65);
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