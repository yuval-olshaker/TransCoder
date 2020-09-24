// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class PERFECT_REVERSIBLE_STRING{
static boolean f_gold ( String str ) {
  int i = 0 , j = str . length ( ) - 1 ;
  while ( i < j ) {
    if ( str . charAt ( i ) != str . charAt ( j ) ) return false ;
    i ++ ;
    j -- ;
  }
  return true ;
}


//
public static boolean f_filled ( String str ) {
  int i = 0 ;
  int j = str . length ( ) - 1 ;
  while ( ( i < j ) && ( str . charAt ( i ) != str . charAt ( j ) ) ) {
    if ( ( str . charAt ( i ) != str . charAt ( j ) ) && ( str . charAt ( i ) != str . charAt ( j ) ) ) {
      return false ;
    }
    i ++ ;
    j -- ;
  }
  return true ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<String> param0 = new ArrayList<>();
    param0.add("ab");
    param0.add("303");
    param0.add("11110000");
    param0.add("aba");
    param0.add("404");
    param0.add("10101");
    param0.add("abab");
    param0.add("6366");
    param0.add("001");
    param0.add("");
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