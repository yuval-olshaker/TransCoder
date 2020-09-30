// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class DYNAMIC_PROGRAMMING_SET_17_PALINDROME_PARTITIONING_1{
static int f_gold ( String str ) {
  int n = str . length ( ) ;
  int [ ] C = new int [ n ] ;
  boolean [ ] [ ] P = new boolean [ n ] [ n ] ;
  int i , j , k , L ;
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    P [ i ] [ i ] = true ;
  }
  for ( L = 2 ;
  L <= n ;
  L ++ ) {
    for ( i = 0 ;
    i < n - L + 1 ;
    i ++ ) {
      j = i + L - 1 ;
      if ( L == 2 ) P [ i ] [ j ] = ( str . charAt ( i ) == str . charAt ( j ) ) ;
      else P [ i ] [ j ] = ( str . charAt ( i ) == str . charAt ( j ) ) && P [ i + 1 ] [ j - 1 ] ;
    }
  }
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    if ( P [ 0 ] [ i ] == true ) C [ i ] = 0 ;
    else {
      C [ i ] = Integer . MAX_VALUE ;
      for ( j = 0 ;
      j < i ;
      j ++ ) {
        if ( P [ j + 1 ] [ i ] == true && 1 + C [ j ] < C [ i ] ) C [ i ] = 1 + C [ j ] ;
      }
    }
  }
  return C [ n - 1 ] ;
}


//
public static int f_filled ( String str1 ) {
    int n = str1 . length ( ) ;
    int [ ] C = {
    }
    P = new boolean [ n + 1 ] ;
    for ( int i = 0 ;  i < n ;  i ++ ) {
        P [ i ] [ i ] = true ;
    }
    for ( int L = 2 ;  L <= n ;  L ++ ) {
        for ( int i = 0 ;  i < n - L + 1 ;  i ++ ) {
            int j = i + L - 1 ;
            if ( ( L == 2 ) && ( str1 . length ( ) > 0 ) ) {
                P [ i ] [ j ] = ( str1 . charAt ( i ) == str1 . charAt ( j ) ) ;
            }
            else {
                P [ i ] [ j ] = ( ( str1 . charAt ( i ) == str1 . charAt ( j ) ) ? P [ i + 1 ] [ j - 1 ] : null ) ;
            }
        }
    }
    for ( int i = 0 ;  i < n ;  i ++ ) {
        if ( ( P [ 0 ] [ i ] == true ) && ( P [ 1 ] [ i ] == true ) ) {
            C [ i ++ ] = 0 ;
        }
        else {
            C [ i ] = Integer . MAX_VALUE ;
            for ( int j = 0 ;  j < i ;  j ++ ) {
                if ( ( P [ j + 1 ] [ i ] == true && 1 + C [ j ] < C [ i ] ) || ( P [ j + 1 ] [ i ] == false && 1 + C [ j ] < C [ i ] ) ) {
                    C [ i ] = 1 + C [ j ] ;
                }
            }
        }
    }
    return C [ n - 1 ] ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<String> param0 = new ArrayList<>();
    param0.add("YYGWgYrovdsh");
    param0.add("56109778");
    param0.add("101");
    param0.add("RxM");
    param0.add("187546405");
    param0.add("0110010");
    param0.add("wVODAmgvI");
    param0.add("56719");
    param0.add("10100011001100");
    param0.add("Wtpai");
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