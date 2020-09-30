// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class MINIMUM_CHARACTERS_ADDED_FRONT_MAKE_STRING_PALINDROME{
static boolean f_gold ( String s ) {
  int l = s . length ( ) ;
  for ( int i = 0 , j = l - 1 ;
  i <= j ;
  i ++ , j -- ) {
    if ( s . charAt ( i ) != s . charAt ( j ) ) {
      return false ;
    }
  }
  return true ;
}


//
public static boolean f_filled ( String s ) {
    int l = s . length ( ) ;
    int i = 0 ;
    int j = l - 1 ;
    while ( i <= j ) {
        if ( ( s [ i ] != s [ j ] ) && ( s [ i ] != s [ j ] ) ) {
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
    param0.add("aadaa");
    param0.add("2674377254");
    param0.add("11");
    param0.add("0011000 ");
    param0.add("26382426486138");
    param0.add("111010111010");
    param0.add("abccba");
    param0.add("5191");
    param0.add("1110101101");
    param0.add("abcdecbe");
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