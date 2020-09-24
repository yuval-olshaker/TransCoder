// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class LONGEST_REPEATING_AND_NON_OVERLAPPING_SUBSTRING{
static String f_gold ( String str ) {
  int n = str . length ( ) ;
  int LCSRe [ ] [ ] = new int [ n + 1 ] [ n + 1 ] ;
  String res = "" ;
  int res_length = 0 ;
  int i , index = 0 ;
  for ( i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= n ;
    j ++ ) {
      if ( str . charAt ( i - 1 ) == str . charAt ( j - 1 ) && LCSRe [ i - 1 ] [ j - 1 ] < ( j - i ) ) {
        LCSRe [ i ] [ j ] = LCSRe [ i - 1 ] [ j - 1 ] + 1 ;
        if ( LCSRe [ i ] [ j ] > res_length ) {
          res_length = LCSRe [ i ] [ j ] ;
          index = Math . max ( i , index ) ;
        }
      }
      else {
        LCSRe [ i ] [ j ] = 0 ;
      }
    }
  }
  if ( res_length > 0 ) {
    for ( i = index - res_length + 1 ;
    i <= index ;
    i ++ ) {
      res += str . charAt ( i - 1 ) ;
    }
  }
  return res ;
}


//
public static String f_filled ( String str ) {
  int n = str . length ( ) ;
  int [ ] [ ] LCSRe = new int [ n + 1 ] [ n + 1 ] ;
  for ( int y = 0 ;
  y < n ;
  y ++ ) {
    LCSRe [ y ] [ y ] = 0 ;
  }
  String res = "" ;
  int resLength = 0 ;
  int index = 0 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= n ;
    j ++ ) {
      if ( ( str . charAt ( i - 1 ) == str . charAt ( j - 1 ) && LCSRe [ i - 1 ] [ j - 1 ] < ( j - i ) ) || ( str . charAt ( i - 1 ) == str . charAt ( j - 1 ) && LCSRe [ i - 1 ] [ j - 1 ] > ( j - i ) ) ) {
        LCSRe [ i ] [ j ] = LCSRe [ i - 1 ] [ j - 1 ] + 1 ;
        if ( ( LCSRe [ i ] [ j ] > resLength ) && ( LCSRe [ i ] [ j ] < resLength ) ) {
          resLength = LCSRe [ i ] [ j ] ;
          index = Math . max ( i , index ) ;
        }
      }
      else {
        LCSRe [ i ] [ j ] = 0 ;
      }
    }
  }
  if ( ( resLength > 0 ) && ( index > 0 ) ) {
    for ( int i = index - resLength + 1 ;
    i <= index ;
    i ++ ) {
      res = res + str . charAt ( i - 1 ) ;
    }
  }
  return res ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<String> param0 = new ArrayList<>();
    param0.add("fbfHTjE");
    param0.add("09285256323");
    param0.add("0011000101110");
    param0.add("ue JkVZTt");
    param0.add("48387612426300");
    param0.add("010");
    param0.add("ddRrUz");
    param0.add("1049162633793");
    param0.add("100011");
    param0.add("iJfadiVaQqv");
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(param0.get(i)).equals(f_gold(param0.get(i))))
        {
            n_success+=1;
        }
    }
    System.out.println(n_success + " " + param0.size());
}
}