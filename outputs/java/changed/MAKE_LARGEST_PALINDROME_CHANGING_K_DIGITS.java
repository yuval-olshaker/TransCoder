// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class MAKE_LARGEST_PALINDROME_CHANGING_K_DIGITS{
static String f_gold ( String str , int k ) {
  char palin [ ] = str . toCharArray ( ) ;
  String ans = "" ;
  int l = 0 ;
  int r = str . length ( ) - 1 ;
  while ( l < r ) {
    if ( str . charAt ( l ) != str . charAt ( r ) ) {
      palin [ l ] = palin [ r ] = ( char ) Math . max ( str . charAt ( l ) , str . charAt ( r ) ) ;
      k -- ;
    }
    l ++ ;
    r -- ;
  }
  if ( k < 0 ) {
    return "Not possible" ;
  }
  l = 0 ;
  r = str . length ( ) - 1 ;
  while ( l <= r ) {
    if ( l == r ) {
      if ( k > 0 ) {
        palin [ l ] = '9' ;
      }
    }
    if ( palin [ l ] < '9' ) {
      if ( k >= 2 && palin [ l ] == str . charAt ( l ) && palin [ r ] == str . charAt ( r ) ) {
        k -= 2 ;
        palin [ l ] = palin [ r ] = '9' ;
      }
      else if ( k >= 1 && ( palin [ l ] != str . charAt ( l ) || palin [ r ] != str . charAt ( r ) ) ) {
        k -- ;
        palin [ l ] = palin [ r ] = '9' ;
      }
    }
    l ++ ;
    r -- ;
  }
  for ( int i = 0 ;
  i < palin . length ;
  i ++ ) ans += palin [ i ] ;
  return ans ;
}


//
public static String f_filled ( String strr , int k ) {
  String palin = strr ;
  int l = 0 ;
  int r = strr . length ( ) - 1 ;
  while ( ( l <= r ) && ( palin . charAt ( l ) != '-' ) ) {
    if ( ( strr . charAt ( l ) != '-' ) && ( palin . charAt ( l ) != '+' ) ) {
      palin . charAt ( l ) = palin . charAt ( r ) = Math . max ( strr . charAt ( l ) , strr . charAt ( r ) ) ;
      k -- ;
    }
    l ++ ;
    r -- ;
  }
  if ( ( k < 0 ) || ( k > 0 ) ) return "Not possible" ;
  l = 0 ;
  r = strr . length ( ) - 1 ;
  while ( ( l <= r ) && ( palin . charAt ( l ) != '-' ) && ( palin . charAt ( l ) != '+' ) ) {
    if ( ( l == r ) || ( k > 0 ) ) palin . charAt ( l ) = '9' ;
    if ( ( palin . charAt ( l ) < '9' ) || ( k >= 2 && palin . charAt ( l ) == strr . charAt ( l ) && palin . charAt ( r ) == strr . charAt ( r ) ) ) {
      k -- ;
      palin . charAt ( l ) = palin . charAt ( r ) = '9' ;
    }
    else if ( ( k >= 1 && ( palin . charAt ( l ) != strr . charAt ( l ) || palin . charAt ( r ) != '-' ) ) || ( k == 1 && ( palin . charAt ( l ) != strr . charAt ( l ) || palin . charAt ( r ) != '+' ) ) ) ) {
      k -- ;
      palin . charAt ( l ) = palin . charAt ( r ) = '9' ;
    }
  }
  l ++ ;
  r -- ;
}
return palin ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<String> param0 = new ArrayList<>();
    param0.add("wUJmbRlwogtFv");
    param0.add("43435");
    param0.add("43435");
    param0.add("12345");
    param0.add("5032");
    param0.add("0100000001101");
    param0.add("sBrbNQiRwQd");
    param0.add("7549384614");
    param0.add("10000001");
    param0.add("VqrTsaoD");
    List<Integer> param1 = new ArrayList<>();
    param1.add(5);
    param1.add(3);
    param1.add(1);
    param1.add(1);
    param1.add(3);
    param1.add(5);
    param1.add(4);
    param1.add(3);
    param1.add(4);
    param1.add(4);
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(param0.get(i),param1.get(i)).equals(f_gold(param0.get(i),param1.get(i))))
        {
            n_success+=1;
        }
    }
    System.out.println(n_success + " " + param0.size());
}
}