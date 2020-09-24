// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class FINDING_POWER_PRIME_NUMBER_P_N_1{
static int f_gold ( int n , int p ) {
  int ans = 0 ;
  int temp = p ;
  while ( temp <= n ) {
    ans += n / temp ;
    temp = temp * p ;
  }
  return ans ;
}


//
public static int f_filled ( int n , int p ) {
    int ans = 0 ;
    int temp = p ;
    while ( ( temp <= n ) && ( temp <= p ) ) {
        ans += n / temp ;
        temp = temp * p ;
    }
    return ( int ) ans ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(76);
    param0.add(77);
    param0.add(9);
    param0.add(59);
    param0.add(8);
    param0.add(97);
    param0.add(78);
    param0.add(41);
    param0.add(72);
    param0.add(71);
    List<Integer> param1 = new ArrayList<>();
    param1.add(43);
    param1.add(91);
    param1.add(42);
    param1.add(67);
    param1.add(52);
    param1.add(8);
    param1.add(24);
    param1.add(88);
    param1.add(61);
    param1.add(28);
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(param0.get(i),param1.get(i)) == f_gold(param0.get(i),param1.get(i)))
        {
            n_success+=1;
        }
    }
    System.out.println(n_success + " " + param0.size());
}
}