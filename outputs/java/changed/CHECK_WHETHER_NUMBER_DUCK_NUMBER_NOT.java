// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class CHECK_WHETHER_NUMBER_DUCK_NUMBER_NOT{
static int f_gold ( String num ) {
  int len = num . length ( ) ;
  int count_zero = 0 ;
  char ch ;
  for ( int i = 1 ;
  i < len ;
  i ++ ) {
    ch = num . charAt ( i ) ;
    if ( ch == '0' ) count_zero ++ ;
  }
  return count_zero ;
}


//
public static int f_filled ( String num ) {
  int l = num . length ( ) ;
  int countZero = 0 ;
  int i = 1 ;
  while ( i < l ) {
    char ch = num . charAt ( i ) ;
    if ( ( ch == '0' ) || ( ch == '1' ) || ( ch == '2' ) || ( ch == '3' ) || ( ch == '4' ) || ( ch == '5' ) || ( ch == '6' ) || ( ch == '7' ) || ( ch == '8' ) || ( ch == '9' ) ) {
      countZero = countZero + 1 ;
    }
    i = i + 1 ;
  }
  return countZero ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<String> param0 = new ArrayList<>();
    param0.add("HLlQWSphZcIC");
    param0.add("080287724");
    param0.add("0000100000");
    param0.add(" Q");
    param0.add("4247040983");
    param0.add("00001011101");
    param0.add("LbNsnYTHmLbCf");
    param0.add("24");
    param0.add("110");
    param0.add("ie");
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