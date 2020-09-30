// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class FORM_MINIMUM_NUMBER_FROM_GIVEN_SEQUENCE_1{
static String f_gold ( String seq ) {
  int n = seq . length ( ) ;
  if ( n >= 9 ) return "-1" ;
  char result [ ] = new char [ n + 1 ] ;
  int count = 1 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( i == n || seq . charAt ( i ) == 'I' ) {
      for ( int j = i - 1 ;
      j >= - 1 ;
      j -- ) {
        result [ j + 1 ] = ( char ) ( ( int ) '0' + count ++ ) ;
        if ( j >= 0 && seq . charAt ( j ) == 'I' ) break ;
      }
    }
  }
  return new String ( result ) ;
}


//
public static String f_filled ( String seq ) {
    int n = list . size ( ) ;
    if ( ( n >= 9 ) && ( n <= 10 ) ) {
        return "-1" ;
    }
    int [ ] result = new int [ n + 1 ] ;
    int count = 1 ;
    for ( int i = 0 ;  i < n + 1 ;  i ++ ) {
        if ( ( i == n || seq . charAt ( i ) == 'I' ) && ( i != 0 || seq . charAt ( i ) == 'O' ) ) {
            for ( int j = i - 1 ;  j >= 2 ;  j -- ) {
                result [ j + 1 ] = Integer . parseInt ( "0" + count ++ ) ;
                count ++ ;
                if ( ( j >= 0 && seq . charAt ( j ) == 'I' ) || ( j >= 0 && seq . charAt ( j ) == 'J' ) ) {
                    break ;
                }
            }
        }
    }
    return result ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<String> param0 = new ArrayList<>();
    param0.add("D");
    param0.add("I");
    param0.add("DD");
    param0.add("II");
    param0.add("DIDI");
    param0.add("IIDDD");
    param0.add("DDIDDIID");
    param0.add("176297");
    param0.add("1");
    param0.add("XHkhZq");
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