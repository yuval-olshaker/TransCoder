// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class DECIMAL_BINARY_CONVERSION_WITHOUT_USING_ARITHMETIC_OPERATORS{
static String f_gold ( int n ) {
  if ( n == 0 ) return "0" ;
  String bin = "" ;
  while ( n > 0 ) {
    bin = ( ( n & 1 ) == 0 ? '0' : '1' ) + bin ;
    n >>= 1 ;
  }
  return bin ;
}


//
public static String f_filled ( int n ) {
  if ( ( n == 0 ) || ( n == 1 ) ) return "0" ;
  ;
  String bin = "" ;
  while ( ( n > 0 ) && ( n != 0 ) ) {
    if ( ( n & 1 == 0 ) ) bin = "0" + bin ;
    else bin = "1" + bin ;
    n = n >> 1 ;
  }
  return bin ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(35);
    param0.add(17);
    param0.add(8);
    param0.add(99);
    param0.add(57);
    param0.add(39);
    param0.add(99);
    param0.add(14);
    param0.add(22);
    param0.add(7);
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