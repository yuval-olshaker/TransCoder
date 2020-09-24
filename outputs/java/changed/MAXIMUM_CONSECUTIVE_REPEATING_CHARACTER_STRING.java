// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class MAXIMUM_CONSECUTIVE_REPEATING_CHARACTER_STRING{
static char f_gold ( String str ) {
  int len = str . length ( ) ;
  int count = 0 ;
  char res = str . charAt ( 0 ) ;
  for ( int i = 0 ;
  i < len ;
  i ++ ) {
    int cur_count = 1 ;
    for ( int j = i + 1 ;
    j < len ;
    j ++ ) {
      if ( str . charAt ( i ) != str . charAt ( j ) ) break ;
      cur_count ++ ;
    }
    if ( cur_count > count ) {
      count = cur_count ;
      res = str . charAt ( i ) ;
    }
  }
  return res ;
}


//
public static String f_filled ( String str ) {
    int l = str . length ( ) ;
    int count = 0 ;
    String res = str . substring ( 0 , str . length ( ) - 1 ) ;
    for ( int i = 0 ;  i < l ;  i ++ ) {
        curCount = 1 ;
        for ( int j = i + 1 ;  j < l ;  j ++ ) {
            if ( ( str . charAt ( i ) != str . charAt ( j ) ) && ( str . charAt ( i ) != str . charAt ( j ) ) ) {
                break ;
            }
            curCount ++ ;
        }
        if ( curCount > count ){
            count = curCount ;
            String res = str . substring ( i ) ;
        }
    }
    return res ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<String> param0 = new ArrayList<>();
    param0.add("geeekk");
    param0.add("3786868");
    param0.add("110");
    param0.add("aaaabbcbbb");
    param0.add("11");
    param0.add("011101");
    param0.add("WoHNyJYLC");
    param0.add("3141711779");
    param0.add("10111101101");
    param0.add("aabbabababcc");
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