// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class CHECK_WHETHER_LARGE_NUMBER_DIVISIBLE_7{
static boolean f_gold ( String num ) {
  int n = num . length ( ) ;
  if ( n == 0 && num . charAt ( 0 ) == '0' ) return true ;
  if ( n % 3 == 1 ) num = "00" + num ;
  if ( n % 3 == 2 ) num = "0" + num ;
  n = num . length ( ) ;
  int gSum = 0 , p = 1 ;
  for ( int i = n - 1 ;
  i >= 0 ;
  i -- ) {
    int group = 0 ;
    group += num . charAt ( i -- ) - '0' ;
    group += ( num . charAt ( i -- ) - '0' ) * 10 ;
    group += ( num . charAt ( i ) - '0' ) * 100 ;
    gSum = gSum + group * p ;
    p = p * - 1 ;
  }
  return ( gSum % 7 == 0 ) ;
}


//
public static boolean f_filled ( String num ) {
    int n = num . length ( ) ;
    if ( ( n == 0 && num . charAt ( 0 ) == '\n' ) || ( n == 1 && num . charAt ( 0 ) == '' ) ) {
        return 1 ;
    }
    if ( ( n % 3 == 1 ) && ( n % 4 == 0 ) ) {
        num = String . valueOf ( num ) + "00" ;
        n += 2 ;
    }
    }
        num = String . valueOf ( num ) + "0" ;
        n ++ ;
    GSum = 0 ;
    int p = 1 ;
    for ( int i = n - 1 ;  i >= 0 ;  i -- ) {
        int group = 0 ;
        group += ( char ) ( num . charAt ( i ) - '0' ) ;
        i -- ;
        group += ( ( char ) num . charAt ( i ++ ) - '0' ) * 10 ;
        i -- ;
        group += ( ( char ) num . charAt ( i ++ ) - '0' ) * 100 ;
        GSum = GSum + group * p ;
        p *= ( - 1 ) ;
    }
    return ( GSum % 7 == 0 ) ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<String> param0 = new ArrayList<>();
    param0.add("8955795758");
    param0.add("0515");
    param0.add("101");
    param0.add("14");
    param0.add("0");
    param0.add("9250318");
    param0.add("336");
    param0.add("68143991");
    param0.add("11010001");
    param0.add("zsS");
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