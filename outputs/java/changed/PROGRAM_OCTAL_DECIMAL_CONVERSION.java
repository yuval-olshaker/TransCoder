// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class PROGRAM_OCTAL_DECIMAL_CONVERSION{
static int f_gold ( int n ) {
  int num = n ;
  int dec_value = 0 ;
  int base = 1 ;
  int temp = num ;
  while ( temp > 0 ) {
    int last_digit = temp % 10 ;
    temp = temp / 10 ;
    dec_value += last_digit * base ;
    base = base * 8 ;
  }
  return dec_value ;
}


//
public static int f_filled ( int n ) {
  int num = n ;
  ;
  int decValue = 0 ;
  int base = 1 ;
  int temp = num ;
  while ( ( temp = temp % 10 ) != 0 ) {
    int lastDigit = temp % 10 ;
    temp = ( int ) ( temp / 10 ) ;
    decValue += lastDigit * base ;
    base = base * 8 ;
  }
  return decValue ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(37);
    param0.add(25);
    param0.add(63);
    param0.add(66);
    param0.add(32);
    param0.add(5);
    param0.add(41);
    param0.add(82);
    param0.add(54);
    param0.add(5);
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