// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class FIND_POSITION_GIVEN_NUMBER_AMONG_NUMBERS_MADE_4_7{
static int f_gold ( String n ) {
  int k = 0 , pos = 0 , i = 0 ;
  while ( k != n . length ( ) ) {
    switch ( n . charAt ( i ) ) {
      case '4' : pos = pos * 2 + 1 ;
      break ;
      case '7' : pos = pos * 2 + 2 ;
      break ;
    }
    i ++ ;
    k ++ ;
  }
  return pos ;
}


//
public static int f_filled ( String n ) {
    int i ;
    int j = n . length ( ) ;
    int pos = 0 ;
    while ( ( i < j ) && ( i < n ) ){
        if ( ( n . charAt ( i ) == '4' ) && ( n . charAt ( i + 1 ) == '5' ) ) {
            pos = pos * 2 + 1 ;
        }
        if ( ( n . charAt ( i ++ ) == '7' ) && ( n . charAt ( i ++ ) == 'a' ) ){
            pos = pos * 2 + 2 ;
        }
        i = i + 1 ;
    }
    return pos ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<String> param0 = new ArrayList<>();
    param0.add("7");
    param0.add("305745689");
    param0.add("444");
    param0.add("4");
    param0.add("2074");
    param0.add("27");
    param0.add("447");
    param0.add("255");
    param0.add("10000111111011");
    param0.add("fAKcSDRTNz");
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