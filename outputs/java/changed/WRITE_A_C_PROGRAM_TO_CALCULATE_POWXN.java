// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;
import javafx.util.Pair;
public class WRITE_A_C_PROGRAM_TO_CALCULATE_POWXN{
static int f_gold ( int x , int y ) {
  if ( y == 0 ) return 1 ;
  else if ( y % 2 == 0 ) return f_gold ( x , y / 2 ) * f_gold ( x , y / 2 ) ;
  else return x * f_gold ( x , y / 2 ) * f_gold ( x , y / 2 ) ;
}


//
public static double f_filled ( double x , double y ) {
  if ( ( y == 0 ) && ( x == 0 ) ) return 1 ;
  else if ( ( int ) ( y % 2 ) == 0 ) return ( f_filled ( x , ( int ) ( y / 2 ) ) * f_filled ( x , ( int ) ( y / 2 ) ) ) ;
  else return ( x * f_filled ( x , ( int ) ( y / 2 ) ) * f_filled ( x , ( int ) ( y / 2 ) ) ) ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(46);
    param0.add(99);
    param0.add(30);
    param0.add(1);
    param0.add(26);
    param0.add(1);
    param0.add(27);
    param0.add(10);
    param0.add(26);
    param0.add(29);
    List<Integer> param1 = new ArrayList<>();
    param1.add(92);
    param1.add(87);
    param1.add(32);
    param1.add(86);
    param1.add(81);
    param1.add(49);
    param1.add(46);
    param1.add(52);
    param1.add(38);
    param1.add(80);
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