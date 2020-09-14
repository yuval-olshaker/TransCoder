// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;
import javafx.util.Pair;
public class LEXICOGRAPHICAL_CONCATENATION_SUBSTRINGS_STRING{
static String f_gold ( String s ) {
  int n = s . length ( ) ;
  int sub_count = n * ( n + 1 ) / 2 ;
  String [ ] arr = new String [ sub_count ] ;
  int index = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) for ( int len = 1 ;
  len <= n - i ;
  len ++ ) {
    arr [ index ++ ] = s . substring ( i , i + len ) ;
  }
  Arrays . sort ( arr ) ;
  String res = "" ;
  for ( int i = 0 ;
  i < sub_count ;
  i ++ ) res += arr [ i ] ;
  return res ;
}


//
public static String f_filled ( String s ) {
  int n = s . length ( ) ;
  ;
  int subCount = ( n * ( n + 1 ) ) / 2 ;
  int [ ] arr = new int [ subCount ] ;
  int index = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 1 ;
    j <= n - i + 1 ;
    j ++ ) {
      arr [ index ] = s . charAt ( i ) ;
      index ++ ;
    }
  }
  Arrays . sort ( arr ) ;
  String res = "" ;
  for ( int i = 0 ;
  i < subCount ;
  i ++ ) {
    res += arr [ i ] ;
  }
  return res ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<String> param0 = new ArrayList<>();
    param0.add("sqGOi");
    param0.add("848580");
    param0.add("01001110011001");
    param0.add("ZhWXUKmeiI");
    param0.add("0917296541285");
    param0.add("01101001111100");
    param0.add("tjP kR");
    param0.add("999907");
    param0.add("011100");
    param0.add("qJPHNSJOUj");
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