// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class CHECK_GIVEN_SENTENCE_GIVEN_SET_SIMPLE_GRAMMER_RULES{
static boolean f_gold ( char [ ] str ) {
  int len = str . length ;
  if ( str [ 0 ] < 'A' || str [ 0 ] > 'Z' ) return false ;
  if ( str [ len - 1 ] != '.' ) return false ;
  int prev_state = 0 , curr_state = 0 ;
  int index = 1 ;
  while ( index <= str . length ) {
    if ( str [ index ] >= 'A' && str [ index ] <= 'Z' ) curr_state = 0 ;
    else if ( str [ index ] == ' ' ) curr_state = 1 ;
    else if ( str [ index ] >= 'a' && str [ index ] <= 'z' ) curr_state = 2 ;
    else if ( str [ index ] == '.' ) curr_state = 3 ;
    if ( prev_state == curr_state && curr_state != 2 ) return false ;
    if ( prev_state == 2 && curr_state == 0 ) return false ;
    if ( curr_state == 3 && prev_state != 1 ) return ( index + 1 == str . length ) ;
    index ++ ;
    prev_state = curr_state ;
  }
  return false ;
}


//
public static boolean f_filled ( String string ) {
    int length = string . length ( ) ;
    if ( string . charAt ( 0 ) < 'A' || string . charAt ( 0 ) > 'Z' ) {
        return false ;
    }
    if ( string . charAt ( length - 1 ) != '.' ){
        return false ;
    }
    prev_state = 0 ;
    currState = 0 ;
    index = 1 ;
    while ( ( string . charAt ( index ++ ) ) != ' ' ) {
        if ( string . charAt ( index ) >= 'A' && string . charAt ( index ) <= 'Z' ) {
            currState = 0 ;
        }
        else if ( string . charAt ( index ) == ' ' ) {
            currState = 1 ;
        }
        if ( string . charAt ( index ) >= 'a' && string . charAt ( index ) <= 'z' ) {
            currState = 2 ;
        }
        else if ( string . charAt ( index ) == '.' ) {
            currState = 3 ;
        }
        if ( prev_state == currState && currState != 2 ) {
            return false ;
        }
        if ( prev_state == 2 && curr_state == 0 ) {
            return false ;
        }
        if ( currState == 3 && prev_state != 1 ) {
            return f_filled ( string , false ) ;
        }
        index ++ ;
        prev_state = currState ;
    }
    return false ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<String> param0 = Arrays.asList("I love cinema.", "The vertex is S.",
                         "I am single.", "My name is KG.",
                         "I lovE cinema.", "GeeksQuiz. is a quiz site.",
                         "I love Geeksquiz and Geeksforgeeks.",
                         " You are my friend.", "I love cinema", "Hello world !");

    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(param0.get(i).toCharArray()) == f_gold(param0.get(i).toCharArray()))
        {
            n_success+=1;
        }
    }
    System.out.println(n_success + " " + param0.size());
}
}