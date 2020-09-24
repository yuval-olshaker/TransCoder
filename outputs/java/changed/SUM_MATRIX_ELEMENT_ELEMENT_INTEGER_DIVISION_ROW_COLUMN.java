// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class SUM_MATRIX_ELEMENT_ELEMENT_INTEGER_DIVISION_ROW_COLUMN{
static int f_gold ( int n ) {
  int ans = 0 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) for ( int j = 1 ;
  j <= n ;
  j ++ ) ans += ( i / j ) ;
  return ans ;
}


//
public static int f_filled ( int N ) {
    int ans = 0 ;
    for ( int i = 1 ;  i <= N ;  i ++ ) {
        for ( int j = 1 ;  j <= N ;  j ++ ) {
            ans += i / j ;
        }
    }
    return ans ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(60);
    param0.add(74);
    param0.add(8);
    param0.add(74);
    param0.add(34);
    param0.add(66);
    param0.add(96);
    param0.add(11);
    param0.add(45);
    param0.add(72);
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