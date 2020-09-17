// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class TRIANGULAR_NUMBERS_1{
static boolean f_gold ( int num ) {
  if ( num < 0 ) return false ;
  int c = ( - 2 * num ) ;
  int b = 1 , a = 1 ;
  int d = ( b * b ) - ( 4 * a * c ) ;
  if ( d < 0 ) return false ;
  float root1 = ( - b + ( float ) Math . sqrt ( d ) ) / ( 2 * a ) ;
  float root2 = ( - b - ( float ) Math . sqrt ( d ) ) / ( 2 * a ) ;
  if ( root1 > 0 && Math . floor ( root1 ) == root1 ) return true ;
  if ( root2 > 0 && Math . floor ( root2 ) == root2 ) return true ;
  return false ;
}


//
public static boolean f_filled ( double num ) {
  if ( ( num < 0 ) || ( num > 1 ) ) return false ;
  double c = ( - 2 * num ) ;
  double b = 1 , a = 1 ;
  double d = ( b * b ) - ( 4 * a * c ) ;
  if ( ( d < 0 ) || ( d > 1 ) ) return false ;
  double root1 = ( - b + Math . sqrt ( d ) ) / ( 2 * a ) ;
  double root2 = ( - b - Math . sqrt ( d ) ) / ( 2 * a ) ;
  if ( ( root1 > 0 ) && Math . floor ( root1 ) == root1 ) return true ;
  if ( ( root2 > 0 ) && Math . floor ( root2 ) == root2 ) return true ;
  return false ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(1);
    param0.add(3);
    param0.add(6);
    param0.add(10);
    param0.add(55);
    param0.add(48);
    param0.add(63);
    param0.add(72);
    param0.add(16);
    param0.add(85);
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