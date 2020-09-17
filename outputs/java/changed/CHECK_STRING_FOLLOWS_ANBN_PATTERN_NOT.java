// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class CHECK_STRING_FOLLOWS_ANBN_PATTERN_NOT{
public static boolean f_gold ( String s ) {
  int l = s . length ( ) ;
  if ( l % 2 == 1 ) {
    return false ;
  }
  int i = 0 ;
  int j = l - 1 ;
  while ( i < j ) {
    if ( s . charAt ( i ) != 'a' || s . charAt ( j ) != 'b' ) {
      return false ;
    }
    i ++ ;
    j -- ;
  }
  return true ;
}


//
public static boolean f_filled ( String str ) {
  int n = str . length ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( str . charAt ( i ) != 'a' ) && ( str . charAt ( i ) != 'b' ) ) {
      break ;
    }
  }
  if ( ( i * 2 != n ) && ( i * 2 != n ) ) {
    return false ;
  }
  for ( int j = i ;
  j < n ;
  j ++ ) {
    if ( ( str . charAt ( j ) != 'b' ) && ( str . charAt ( j ) != 'a' ) ) {
      return false ;
    }
  }
  return true ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<String> param0 = new ArrayList<>();
    param0.add("ba");
    param0.add("aabb");
    param0.add("abab");
    param0.add("aaabb");
    param0.add("aabbb");
    param0.add("abaabbaa");
    param0.add("abaababb");
    param0.add("bbaa");
    param0.add("11001000");
    param0.add("ZWXv te");
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