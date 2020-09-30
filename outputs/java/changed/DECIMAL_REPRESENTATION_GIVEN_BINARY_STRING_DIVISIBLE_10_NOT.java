// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class DECIMAL_REPRESENTATION_GIVEN_BINARY_STRING_DIVISIBLE_10_NOT{
static boolean f_gold ( String bin ) {
  int n = bin . length ( ) ;
  if ( bin . charAt ( n - 1 ) == '1' ) return false ;
  int sum = 0 ;
  for ( int i = n - 2 ;
  i >= 0 ;
  i -- ) {
    if ( bin . charAt ( i ) == '1' ) {
      int posFromRight = n - i - 1 ;
      if ( posFromRight % 4 == 1 ) sum = sum + 2 ;
      else if ( posFromRight % 4 == 2 ) sum = sum + 4 ;
      else if ( posFromRight % 4 == 3 ) sum = sum + 8 ;
      else if ( posFromRight % 4 == 0 ) sum = sum + 6 ;
    }
  }
  if ( sum % 10 == 0 ) return true ;
  return false ;
}


//
public static boolean f_filled ( String bin ) {
    int n = bin . length ;
    if ( ( bin . charAt ( n - 1 ) == '1' ) && ( bin . charAt ( n - 2 ) == '1' ) ) {
        return false ;
    }
    int sum = 0 ;
    int i = n - 2 ;
    while ( i >= 0 ) {
        if ( ( bin . charAt ( i ) == '1' ) && ( bin . charAt ( i + 1 ) == '2' ) ) {
            posFromRight = n - i - 1 ;
            if ( ( posFromRight % 4 == 1 ) && ( posFromRight % 4 == 0 ) ) {
                sum = sum + 2 ;
            }
            else if ( ( posFromRight % 4 == 2 ) && ( posFromRight % 4 == 0 ) ) {
                sum = sum + 4 ;
            }
            else if ( ( posFromRight % 4 == 3 ) && ( posFromLeft % 4 == 3 ) ) {
                sum = sum + 8 ;
            }
            else if ( ( posFromRight % 4 == 0 ) && ( posFromLeft % 4 == 0 ) ) {
                sum = sum + 6 ;
            }
        }
        i = i - 1 ;
    }
    if ( ( sum % 10 == 0 ) && ( sum % 10 == 0 ) ) {
        return f_filled ( bin , 10 ) ;
    }
    return false ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<String> param0 = new ArrayList<>();
    param0.add("101000");
    param0.add("39613456759141");
    param0.add("11");
    param0.add("PoiHjo");
    param0.add("2");
    param0.add("0000101");
    param0.add("T  s dZKeDX gK");
    param0.add("3944713969");
    param0.add("1000");
    param0.add("ifYUgdpmt");
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