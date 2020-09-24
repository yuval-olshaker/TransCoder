// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class CHECK_GIVEN_STRING_ROTATION_PALINDROME{
static boolean f_gold ( String str ) {
  int l = 0 ;
  int h = str . length ( ) - 1 ;
  while ( h > l ) if ( str . charAt ( l ++ ) != str . charAt ( h -- ) ) return false ;
  return true ;
}


//
public static boolean f_filled ( String string ) {
  int l = 0 ;
  int h = string . length ( ) - 1 ;
  while ( h > l ) {
    l ++ ;
    h -- ;
    if ( string . charAt ( l - 1 ) != string . charAt ( h + 1 ) ) {
      return false ;
    }
  }
  return true ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<String> param0 = new ArrayList<>();
    param0.add("aadaa");
    param0.add("2674377254");
    param0.add("11");
    param0.add("0011000");
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