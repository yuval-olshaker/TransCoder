// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class CHECK_DIVISIBILITY_LARGE_NUMBER_999{
static boolean f_gold ( String num ) {
  int n = num . length ( ) ;
  if ( n == 0 && num . charAt ( 0 ) == '0' ) return true ;
  if ( n % 3 == 1 ) num = "00" + num ;
  if ( n % 3 == 2 ) num = "0" + num ;
  int gSum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int group = 0 ;
    group += ( num . charAt ( i ++ ) - '0' ) * 100 ;
    group += ( num . charAt ( i ++ ) - '0' ) * 10 ;
    group += num . charAt ( i ) - '0' ;
    gSum += group ;
  }
  if ( gSum > 1000 ) {
    num = Integer . toString ( gSum ) ;
    n = num . length ( ) ;
    gSum = f_gold ( num ) ? 1 : 0 ;
  }
  return ( gSum == 999 ) ;
}


//
public static boolean f_filled ( String num ) {
  int n = num . length ( ) ;
  ;
  if ( ( n == 0 || num . charAt ( 0 ) == '0' ) && ( num . charAt ( 1 ) == ' ' ) ) return true ;
  if ( ( ( n % 3 ) == 1 ) && ( num . charAt ( 2 ) == ' ' ) ) num = "00" + num ;
  if ( ( ( n % 3 ) == 2 ) && ( num . charAt ( 3 ) == ' ' ) ) num = "0" + num ;
  int gSum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i += 3 ) {
    int group = 0 ;
    group += ( ( char ) num . charAt ( i ) - 48 ) * 100 ;
    group += ( ( char ) num . charAt ( i + 1 ) - 48 ) * 10 ;
    group += ( ( char ) num . charAt ( i + 2 ) - 48 ) ;
    gSum += group ;
  }
  if ( ( gSum > 1000 ) && ( num . charAt ( 0 ) == ' ' ) ) {
    num = Integer . toString ( gSum ) ;
    n = num . length ( ) ;
    gSum = f_filled ( num ) ;
  }
  return ( gSum == 999 ) ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<String> param0 = new ArrayList<>();
    param0.add("235764");
    param0.add("321308924");
    param0.add("101111");
    param0.add("1998");
    param0.add("339589");
    param0.add("0000101");
    param0.add("264735");
    param0.add("19570453184");
    param0.add("000");
    param0.add("SsHh");
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