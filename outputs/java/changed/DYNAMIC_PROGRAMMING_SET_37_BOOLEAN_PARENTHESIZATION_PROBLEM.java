// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class DYNAMIC_PROGRAMMING_SET_37_BOOLEAN_PARENTHESIZATION_PROBLEM{
static int f_gold ( char symb [ ] , char oper [ ] , int n ) {
  int F [ ] [ ] = new int [ n ] [ n ] ;
  int T [ ] [ ] = new int [ n ] [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    F [ i ] [ i ] = ( symb [ i ] == 'F' ) ? 1 : 0 ;
    T [ i ] [ i ] = ( symb [ i ] == 'T' ) ? 1 : 0 ;
  }
  for ( int gap = 1 ;
  gap < n ;
  ++ gap ) {
    for ( int i = 0 , j = gap ;
    j < n ;
    ++ i , ++ j ) {
      T [ i ] [ j ] = F [ i ] [ j ] = 0 ;
      for ( int g = 0 ;
      g < gap ;
      g ++ ) {
        int k = i + g ;
        int tik = T [ i ] [ k ] + F [ i ] [ k ] ;
        int tkj = T [ k + 1 ] [ j ] + F [ k + 1 ] [ j ] ;
        if ( oper [ k ] == '&' ) {
          T [ i ] [ j ] += T [ i ] [ k ] * T [ k + 1 ] [ j ] ;
          F [ i ] [ j ] += ( tik * tkj - T [ i ] [ k ] * T [ k + 1 ] [ j ] ) ;
        }
        if ( oper [ k ] == '|' ) {
          F [ i ] [ j ] += F [ i ] [ k ] * F [ k + 1 ] [ j ] ;
          T [ i ] [ j ] += ( tik * tkj - F [ i ] [ k ] * F [ k + 1 ] [ j ] ) ;
        }
        if ( oper [ k ] == '^' ) {
          T [ i ] [ j ] += F [ i ] [ k ] * T [ k + 1 ] [ j ] + T [ i ] [ k ] * F [ k + 1 ] [ j ] ;
          F [ i ] [ j ] += T [ i ] [ k ] * T [ k + 1 ] [ j ] + F [ i ] [ k ] * F [ k + 1 ] [ j ] ;
        }
      }
    }
  }
  return T [ 0 ] [ n - 1 ] ;
}


//
public static int f_filled ( char symb , char oper , int n ) {
  int [ ] [ ] F = new int [ n + 1 ] [ n + 1 ] ;
  int [ ] [ ] T = new int [ n + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( symb == 'F' ) F [ i ] [ i ] = 1 ;
    else F [ i ] [ i ] = 0 ;
    if ( symb == 'T' ) T [ i ] [ i ] = 1 ;
    else T [ i ] [ i ] = 0 ;
  }
  for ( int gap = 1 ;
  gap < n ;
  gap ++ ) {
    int i = 0 ;
    for ( int j = gap ;
    j < n ;
    j ++ ) {
      T [ i ] [ j ] = F [ i ] [ j ] = 0 ;
      for ( int g = 0 ;
      g < gap ;
      g ++ ) {
        int k = i + g ;
        int tik = T [ i ] [ k ] + F [ i ] [ k ] ;
        ;
        int tkj = T [ k + 1 ] [ j ] + F [ k + 1 ] [ j ] ;
        ;
        if ( oper == '&' ) {
          T [ i ] [ j ] += T [ i ] [ k ] * T [ k + 1 ] [ j ] ;
          F [ i ] [ j ] += ( tik * tkj - T [ i ] [ k ] * T [ k + 1 ] [ j ] ) ;
        }
        if ( oper == '|' ) {
          F [ i ] [ j ] += F [ i ] [ k ] * F [ k + 1 ] [ j ] ;
          T [ i ] [ j ] += ( tik * tkj - F [ i ] [ k ] * F [ k + 1 ] [ j ] ) ;
        }
        if ( oper == '^' ) {
          T [ i ] [ j ] += ( F [ i ] [ k ] * T [ k + 1 ] [ j ] + T [ i ] [ k ] * F [ k + 1 ] [ j ] ) ;
          F [ i ] [ j ] += ( T [ i ] [ k ] * T [ k + 1 ] [ j ] + F [ i ] [ k + 1 ] [ j ] ) ;
        }
      }
    }
  }
  return 0 ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<char [ ]> param0 = new ArrayList<>();
    param0.add("TTFT".toCharArray());
    param0.add("TFT".toCharArray());
    param0.add("TFF".toCharArray());
    param0.add("TTFT".toCharArray());
    param0.add("TTFT".toCharArray());
    param0.add("TTFT".toCharArray());
    param0.add("TTFT".toCharArray());
    param0.add("TTFT".toCharArray());
    param0.add("TTFT".toCharArray());
    param0.add("TTFT".toCharArray());
    List<char [ ]> param1 = new ArrayList<>();
    param1.add("|&^".toCharArray());
    param1.add("^&".toCharArray());
    param1.add("^|".toCharArray());
    param1.add("|||".toCharArray());
    param1.add("&&&".toCharArray());
    param1.add("&&^".toCharArray());
    param1.add("^&|".toCharArray());
    param1.add("^^^".toCharArray());
    param1.add("^||".toCharArray());
    param1.add("|^|".toCharArray());
    param1.add("&^|".toCharArray());
    List<Integer> param2 = new ArrayList<>();
    param2.add(4);
    param2.add(3);
    param2.add(3);
    param2.add(4);
    param2.add(4);
    param2.add(4);
    param2.add(4);
    param2.add(4);
    param2.add(4);
    param2.add(4);
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(param0.get(i),param1.get(i),param2.get(i)) == f_gold(param0.get(i),param1.get(i),param2.get(i)))
        {
            n_success+=1;
        }
    }
    System.out.println(n_success + " " + param0.size());
}
}