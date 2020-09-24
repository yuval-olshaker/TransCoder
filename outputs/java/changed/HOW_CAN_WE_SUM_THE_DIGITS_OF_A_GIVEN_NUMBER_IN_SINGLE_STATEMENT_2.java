// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class HOW_CAN_WE_SUM_THE_DIGITS_OF_A_GIVEN_NUMBER_IN_SINGLE_STATEMENT_2{
static int f_gold ( int no ) {
  return no == 0 ? 0 : no % 10 + f_gold ( no / 10 ) ;
}


//
public static int f_filled ( int no ) {
  return no == 0 ? 0 : ( int ) ( no % 10 ) + f_filled ( ( int ) ( no / 10 ) ) ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(73);
    param0.add(91);
    param0.add(27);
    param0.add(79);
    param0.add(31);
    param0.add(84);
    param0.add(68);
    param0.add(9);
    param0.add(85);
    param0.add(35);
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