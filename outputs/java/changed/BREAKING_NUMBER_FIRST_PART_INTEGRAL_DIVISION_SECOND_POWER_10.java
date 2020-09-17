// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class BREAKING_NUMBER_FIRST_PART_INTEGRAL_DIVISION_SECOND_POWER_10{
static int f_gold ( String N ) {
  int len = N . length ( ) ;
  int l = ( len ) / 2 ;
  int count = 0 ;
  for ( int i = 1 ;
  i <= l ;
  i ++ ) {
    String s = N . substring ( 0 , i ) ;
    int l1 = s . length ( ) ;
    String t = N . substring ( i , l1 + i ) ;
    if ( s . charAt ( 0 ) == '0' || t . charAt ( 0 ) == '0' ) continue ;
    if ( s . compareTo ( t ) == 0 ) count ++ ;
  }
  return count ;
}


//
public static int f_filled ( String N ) {
  int length = N . length ( ) ;
  int l = ( int ) ( ( length ) / 2 ) ;
  int count = 0 ;
  for ( int i = 0 ;
  i < l + 1 ;
  i ++ ) {
    String s = N . substring ( 0 , 0 + i ) ;
    int l1 = s . length ( ) ;
    String t = N . substring ( i , l1 + i ) ;
    switch ( s . charAt ( 0 ) ) {
      case '0' : case '1' : case '2' : case '3' : case '4' : case '5' : case '6' : case '7' : case '8' : case '9' : case 'a' : case 'b' : case 'c' : case 'd' : case 'e' : case 'f' : case 'g' : case 'h' : case 'i' : case 'j' : case 'k' : case 'l' : case 'm' : case 'n' : case 'o' : case 'p' : case 'q' : case 'r' : case 's' : case 't' : case 'u' : case 'v' : case 'w' : case 'x' : case 'y' : case 'z' : case 'w' : case 'x' : case 'y' : case 'z' : case 'w' : case 'x' : case 'y' : case 'z' : case 'w' : case 'x' : case 'y' : case 'z' : case 'w' : case 'x' : case 'y' : case 'z' : case 'w' : case 'x' : case 'y' : case 'z' : case 'w' : case 'x' : case ' y

public static void main(String args[]) {
    int n_success = 0;
    List<String> param0 = new ArrayList<>();
    param0.add("ZCoQhuM");
    param0.add("2674377254");
    param0.add("11");
    param0.add("LbuGlvRyWAPBpo");
    param0.add("26382426486138");
    param0.add("111010111010");
    param0.add("hUInqJXNdbfP");
    param0.add("5191");
    param0.add("1110101101");
    param0.add("2202200");
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