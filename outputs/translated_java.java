MAXIMUM_NUMBER_CHARACTERS_TWO_CHARACTER_STRING

public static int maximumChars ( String str ) {
  int n = str . length ( ) ;
  int res = - 1 ;
  for ( int i = 0 ;
  i <= n - 1 ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= n ;
    j ++ ) {
      if ( ( str . charAt ( i ) == str . charAt ( j ) ) && ( str . charAt ( j ) == str . charAt ( i ) ) ) {
        res = Math . max ( res , Math . abs ( j - i - 1 ) ) ;
      }
    }
  }
  return res ;
}
|||

FIND_MIRROR_IMAGE_POINT_2_D_PLANE

public static Point mirrorImage ( int a , int b , int c , int x1 , int y1 ) {
  double temp = - 2 * ( a * x1 + b * y1 + c ) / ( a * a + b * b ) ;
  double x = temp * a + x1 ;
  double y = temp * b + y1 ;
  return new Point ( x , y ) ;
}
|||

EFFICIENTLY_COMPUTE_SUMS_OF_DIAGONALS_OF_A_MATRIX

public static void printDiagonalSums ( int [ ] [ ] mat , int n ) {
  int principal = 0 ;
  int secondary = 0 ;
  ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      if ( ( i == j ) && ( ( i + j ) == ( n - 1 ) ) ) {
        principal += mat [ i ] [ j ] ;
      }
      if ( ( ( i + j ) == ( n - 1 ) ) && ( ( i + j ) == ( n - 2 ) ) ) {
        secondary += mat [ i ] [ j ] ;
      }
    }
  }
  System . out . println ( "Principal Diagonal:" + principal ) ;
  System . out . println ( "Secondary Diagonal:" + secondary ) ;
}
|||

COUNTS_PATHS_POINT_REACH_ORIGIN

public static int countPaths ( int n , int m ) {
  if ( ( n == 0 || m == 0 ) && ( n > m ) ) return 1 ;
  return ( countPaths ( n - 1 , m ) + countPaths ( n , m - 1 ) ) ;
}
|||

FIND_A_TRIPLET_THAT_SUM_TO_A_GIVEN_VALUE_1

public static boolean find3Numbers ( int [ ] A , int arrSize , int sum ) {
  Arrays . sort ( A ) ;
  for ( int i = 0 ;
  i <= arrSize - 2 ;
  i ++ ) {
    int l = i + 1 ;
    int r = arrSize - 1 ;
    while ( ( l < r ) && ( A [ i ] + A [ l ] + A [ r ] == sum ) ) {
      System . out . println ( "Triplet is" + A [ i ] + ", " + A [ l ] + ", " + A [ r ] ) ;
      ;
      return true ;
    }
    else if ( ( A [ i ] + A [ l ] + A [ r ] < sum ) && ( A [ i ] + A [ l ] + A [ r ] < sum ) ) {
      l ++ ;
    }
    else {
      r -- ;
    }
  }
  return false ;
}
|||

CHECK_GIVEN_MATRIX_IS_MAGIC_SQUARE_OR_NOT

public static boolean isMagicSquare ( int [ ] [ ] mat ) {
  int s = 0 ;
  for ( int i = 0 ;
  i <= N ;
  i ++ ) s = s + mat [ i ] [ i ] ;
  int s2 = 0 ;
  for ( int i = 0 ;
  i <= N ;
  i ++ ) s2 = s2 + mat [ i ] [ N - i - 1 ] ;
  if ( ( s != s2 ) && ( s != s2 ) ) return false ;
  for ( int i = 0 ;
  i <= N ;
  i ++ ) {
    int rowSum = 0 ;
    ;
    for ( int j = 0 ;
    j <= N ;
    j ++ ) rowSum += mat [ i ] [ j ] ;
    if ( ( rowSum != s ) && ( rowSum != s ) ) return false ;
  }
  for ( int i = 0 ;
  i <= N ;
  i ++ ) {
    int colSum = 0 ;
    for ( int j = 0 ;
    j <= N ;
    j ++ ) colSum += mat [ j ] [ i ] ;
    if ( ( s != colSum ) && ( s != colSum ) ) return false ;
  }
  return true ;
}
|||

SEQUENCES_GIVEN_LENGTH_EVERY_ELEMENT_EQUAL_TWICE_PREVIOUS_1

public static int getTotalNumberOfSequences ( int m , int n ) {
  int [ ] [ ] T = new int [ n + 1 ] [ m + 1 ] ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( i == 0 || j == 0 ) {
        T [ i ] [ j ] = 0 ;
      }
      else if ( i < j ) {
        T [ i ] [ j ] = 0 ;
      }
      else if ( j == 1 ) {
        T [ i ] [ j ] = i ;
      }
      else {
        T [ i ] [ j ] = T [ i - 1 ] [ j ] + T [ i / 2 ] [ j - 1 ] ;
      }
    }
  }
  return T [ m ] [ n ] ;
}
|||

FIND_DIFFERENCE_BETWEEN_SUMS_OF_TWO_DIAGONALS_1

public static int difference ( int [ ] [ ] arr , int n ) {
  int d1 = 0 ;
  int d2 = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    d1 = d1 + arr [ i ] [ i ] ;
    d2 = d2 + arr [ i ] [ n - i - 1 ] ;
  }
  return Math . abs ( d1 - d2 ) ;
}
|||

MINIMUM_NUMBER_SUBSETS_DISTINCT_ELEMENTS

public static int subset ( int [ ] ar , int n ) {
  int res = 0 ;
  Arrays . sort ( ar ) ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    int count = 1 ;
    for ( int j = 0 ;
    j < n - 1 ;
    j ++ ) {
      if ( ar [ i ] == ar [ i + 1 ] ) {
        count ++ ;
      }
      else {
        break ;
      }
    }
    res = Math . max ( res , count ) ;
  }
  return res ;
}
|||

DECIMAL_BINARY_CONVERSION_WITHOUT_USING_ARITHMETIC_OPERATORS

public static String decToBin ( int n ) {
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
|||

FIND_NTH_TERM_DRAGON_CURVE_SEQUENCE

public static String Dragon_Curve_Sequence ( int n ) {
  String s = "1" ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    String temp = "1" ;
    String prev = "1" ;
    String zero = "0" ;
    String one = "1" ;
    for ( int j = 0 ;
    j < s . length ( ) ;
    j ++ ) {
      temp += s . charAt ( j ) ;
      if ( ( prev == '0' ) && ( prev != one ) ) {
        temp += one ;
        prev = one ;
      }
      else {
        temp += zero ;
        prev = zero ;
      }
    }
    s = temp ;
  }
  return s ;
}
|||

STACK_SET_3_REVERSE_STRING_USING_STACK

public static String reverse ( String string ) {
  string = string . substring ( 0 , string . length ( ) - 1 ) ;
  return string ;
}
|||

SORT_EVEN_PLACED_ELEMENTS_INCREASING_ODD_PLACED_DECREASING_ORDER_1

public static int [ ] bitonicGenerator ( int [ ] arr , int n ) {
  int i = 1 ;
  int j = n - 1 ;
  if ( ( j % 2 != 0 ) && ( j < n ) ) j = j - 1 ;
  while ( ( i < j ) && ( i < n ) ) {
    arr [ j ] = arr [ i ] ;
    arr [ i ] = arr [ j ] ;
    i = i + 2 ;
    j = j - 2 ;
  }
  int [ ] arrF = new int [ arr . length ] ;
  int [ ] arrS = new int [ arr . length ] ;
  for ( i = 0 ;
  i < ( int ) ( ( n + 1 ) / 2 ) ;
  i ++ ) arrF [ i ] = arr [ i ] ;
  i = ( int ) ( ( n + 1 ) / 2 ) ;
  while ( ( i < n ) && ( i < n ) ) {
    arrS [ i ] = arr [ i ] ;
    i = i + 1 ;
  }
  Arrays . sort ( arrF ) ;
  Arrays . sort ( arrS ) ;
  for ( int i = 0 ;
  i < arrS . length ;
  i ++ ) arrF [ i ] = arrS [ i ] ;
  return arrF ;
}
|||

GIVEN_TWO_NUMBERS_B_FIND_X_X_B

public static void modularEquation ( int a , int b ) {
  if ( ( a < b ) && ( a > b ) ) {
    System . out . println ( "No solution possible " ) ;
    return ;
  }
  if ( ( a == b ) && ( a > b ) ) {
    System . out . println ( "Infinite Solution possible " ) ;
    return ;
  }
  int count = 0 ;
  int n = a - b ;
  int y = ( int ) ( Math . sqrt ( a - b ) ) ;
  for ( int i = 1 ;
  i <= y ;
  i ++ ) {
    if ( ( n % i == 0 ) && ( n / i > b ) ) {
      count = count + 1 ;
    }
    if ( ( i > b ) && ( i < a ) ) {
      count = count + 1 ;
    }
  }
  if ( ( y * y == n && y > b ) && ( y == b ) ) {
    count = count - 1 ;
  }
  System . out . println ( count ) ;
}
|||

CHECK_CHARACTERS_GIVEN_STRING_CAN_REARRANGED_FORM_PALINDROME

public static boolean canFormPalindrome ( String st ) {
  int [ ] count = new int [ NO_OF_CHARS ] ;
  for ( int i = 0 ;
  i <= st . length ( ) ;
  i ++ ) {
    count [ Character . toUpperCase ( st . charAt ( i ) ) ] = count [ Character . toUpperCase ( st . charAt ( i ) ) ] + 1 ;
  }
  int odd = 0 ;
  for ( int i = 0 ;
  i <= NO_OF_CHARS ;
  i ++ ) {
    if ( ( count [ i ] & 1 ) != 0 ) {
      odd = odd + 1 ;
    }
    if ( ( odd > 1 ) && ( count [ i ] == 0 ) ) {
      return false ;
    }
  }
  return true ;
}
|||

MAXIMUM_TRIPLET_SUM_ARRAY_1

public static int maxTripletSum ( int [ ] arr , int n ) {
  Arrays . sort ( arr ) ;
  return ( arr [ n - 1 ] + arr [ n - 2 ] + arr [ n - 3 ] ) ;
}
|||

FIND_MEDIAN_ROW_WISE_SORTED_MATRIX

public static void binaryMedian ( int [ ] [ ] m , int r , int d ) {
  int mi = m [ 0 ] [ 0 ] ;
  int mx = 0 ;
  for ( int i = 0 ;
  i < r ;
  i ++ ) {
    if ( m [ i ] [ 0 ] < mi ) mi = m [ i ] [ 0 ] ;
    if ( m [ i ] [ d - 1 ] > mx ) mx = m [ i ] [ d - 1 ] ;
  }
  int desired = ( r * d + 1 ) / 2 ;
  while ( ( mi < mx ) && ( mx > mi ) ) {
    int mid = mi + ( mx - mi ) / 2 ;
    int [ ] place = new int [ r ] ;
    ;
    for ( int i = 0 ;
    i < r ;
    i ++ ) {
      int j = upperBound ( m [ i ] , mid ) ;
      place [ 0 ] = place [ 0 ] + j ;
    }
    if ( place [ 0 ] < desired ) mi = mid + 1 ;
    else mx = mid ;
  }
  System . out . println ( "Median is" + mi ) ;
}
|||

HEIGHT_N_ARY_TREE_PARENT_ARRAY_GIVEN

public static int findHeight ( int [ ] parent , int n ) {
  int res = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int p = i ;
    int current = 1 ;
    while ( ( parent [ p ] != - 1 ) && ( parent [ p ] != - 1 ) ) {
      current ++ ;
      p = parent [ p ] ;
    }
    res = Math . max ( res , current ) ;
  }
  return res ;
}
|||

CHECK_LARGE_NUMBER_DIVISIBLE_20

public static boolean divisibleBy20 ( String num ) {
  int lastTwoDigits = Integer . parseInt ( num . substring ( num . length ( ) - 2 ) ) ;
  return ( ( lastTwoDigits % 5 == 0 && lastTwoDigits % 4 == 0 ) ) ;
}
|||

MAXIMUM_VALUE_CHOICE_EITHER_DIVIDING_CONSIDERING

public static int maxDP ( int n ) {
  List < Integer > res = Lists . newArrayList ( ) ;
  res . add ( 0 ) ;
  res . add ( 1 ) ;
  int i = 2 ;
  while ( i < n + 1 ) {
    res . add ( Math . max ( i , ( res . get ( Integer . class , i / 2 ) ) + res . get ( Integer . class , i / 3 ) + res . get ( Integer . class , i / 4 ) + res . get ( Integer . class , i / 5 ) ) ) ;
    i = i + 1 ;
  }
  return res . get ( n ) ;
}
|||

QUERIES_ON_ARRAY_WITH_DISAPPEARING_AND_REAPPEARING_ELEMENTS

public static void PerformQueries ( int [ ] [ ] a , int [ ] [ ] vec ) {
  int ans [ ] ;
  ;
  int n = a . length - 1 ;
  ;
  int q = vec . length ;
  ;
  for ( int i = 0 ;
  i < q ;
  i ++ ) {
    int t = vec [ i ] [ 0 ] ;
    ;
    int m = vec [ i ] [ 1 ] ;
    ;
    if ( ( m > n ) && ( m < n ) ) {
      ans [ i ] = - 1 ;
      ;
      continue ;
    }
    int turn = t / n ;
    ;
    int rem = t % n ;
    ;
    if ( ( rem == 0 && turn % 2 == 1 ) || ( rem == 0 && turn % 2 == 0 ) ) {
      ans [ i ] = a [ m ] ;
      ;
      continue ;
    }
    if ( ( turn % 2 == 0 ) || ( turn == 1 && turn % 2 == 1 ) ) {
      int cursize = n - rem ;
      ;
      if ( ( cursize < m ) && ( cursize < m ) ) {
        ans [ i ] = - 1 ;
        ;
        continue ;
      }
      ans [ i ] = a [ m + rem ] ;
      ;
    }
    else {
      int cursize = rem ;
      ;
      if ( ( cursize < m ) && ( cursize < m ) ) {
        ans [ i ] = - 1 ;
        ;
        continue ;
      }
      ans [ i ] = a [ m ] ;
      ;
    }
  }
  for ( int i = 0 ;
  i < ans . length ;
  i ++ ) {
    System . out . println ( ans [ i ] ) ;
    ;
  }
}
|||

FIND_THE_MINIMUM_DISTANCE_BETWEEN_TWO_NUMBERS_1

public static int minDist ( int [ ] arr , int n , int x , int y ) {
  int min_dist = Integer . MAX_VALUE ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] == x || arr [ i ] == y ) {
      prev = i ;
      break ;
    }
  }
  while ( i < n ) {
    if ( arr [ i ] == x || arr [ i ] == y ) {
      if ( arr [ prev ] != arr [ i ] && ( i - prev ) < min_dist ) {
        min_dist = i - prev ;
        prev = i ;
      }
      else {
        prev = i ;
      }
    }
    i ++ ;
  }
  return min_dist ;
}
|||

UNION_AND_INTERSECTION_OF_TWO_SORTED_ARRAYS_2

public static void printUnion ( int [ ] arr1 , int [ ] arr2 , int m , int n ) {
  int i = 0 , j = 0 ;
  while ( i < m && j < n ) {
    if ( arr1 [ i ] < arr2 [ j ] ) {
      System . out . print ( arr1 [ i ] ) ;
      i ++ ;
    }
    else if ( arr2 [ j ] < arr1 [ i ] ) {
      System . out . print ( arr2 [ j ] ) ;
      j ++ ;
    }
    else {
      System . out . print ( arr2 [ j ] ) ;
      j ++ ;
      i ++ ;
    }
  }
  while ( i < m ) {
    System . out . print ( arr1 [ i ] ) ;
    i ++ ;
  }
  while ( j < n ) {
    System . out . print ( arr2 [ j ] ) ;
    j ++ ;
  }
}
|||

WORD_WRAP_PROBLEM_SPACE_OPTIMIZED_SOLUTION

public static void solveWordWrap ( int [ ] arr , int n , int k ) {
  int [ ] dp = new int [ n ] ;
  int [ ] ans = new int [ n ] ;
  dp [ n - 1 ] = 0 ;
  ans [ n - 1 ] = n - 1 ;
  for ( int i = n - 2 ;
  i >= 0 ;
  i -- ) {
    int currlen = - 1 ;
    dp [ i ] = Integer . MAX_VALUE ;
    for ( int j = i ;
    j < n ;
    j ++ ) {
      currlen += ( arr [ j ] + 1 ) ;
      if ( ( currlen > k ) && ( j == n - 1 ) ) break ;
      if ( ( j == n - 1 ) || ( j == n - 2 ) ) {
        int cost = 0 ;
        if ( ( k - currlen ) * ( k - currlen ) + dp [ j + 1 ] ) ;
        if ( ( cost < dp [ i ] ) && ( j == n - 1 ) ) {
          dp [ i ] = cost ;
          ans [ i ] = j ;
        }
      }
    }
    int i = 0 ;
    while ( ( i < n ) && ( ans [ i ] > 0 ) ) {
      System . out . print ( i + " " + ans [ i ] + " " ) ;
      i = ans [ i ] + 1 ;
    }
  }
}
|||

COUNT_DISTINCT_SUBSEQUENCES

public static int countSub ( String ss ) {
  int last [ ] = new int [ MAX_CHAR + 1 ] ;
  for ( int i = 0 ;
  i < MAX_CHAR ;
  i ++ ) last [ i ] = - 1 ;
  int n = ss . length ( ) ;
  int dp [ ] = new int [ n + 1 ] ;
  dp [ 0 ] = - 2 ;
  dp [ 1 ] = 0 ;
  dp [ 2 ] = 1 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    dp [ i ] = 2 * dp [ i - 1 ] ;
    if ( last [ ( char ) ss . charAt ( i - 1 ) ] != - 1 ) dp [ i ] = dp [ i ] - dp [ last [ ( char ) ss . charAt ( i - 1 ) ] ] ;
    last [ ( char ) ss . charAt ( i - 1 ) ] = i - 1 ;
  }
  return dp [ n ] ;
}
|||

LONGEST_EVEN_LENGTH_SUBSTRING_SUM_FIRST_SECOND_HALF_3

public static int findLength ( String st , int n ) {
  int [ ] total = new int [ n + 1 ] ;
  total [ 0 ] = 0 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) total [ i ] = ( total [ i - 1 ] + Integer . parseInt ( st . charAt ( i - 1 ) ) - Integer . parseInt ( "0" ) ) ;
  int ans = 0 ;
  int l = 2 ;
  while ( ( l <= n ) && ( total [ l ] == total [ l - 1 ] ) ) {
    for ( int i = 0 ;
    i < n - l + 1 ;
    i ++ ) {
      int j = i + l - 1 ;
      if ( ( total [ i + Integer . parseInt ( l / 2 ) ] - total [ i ] == total [ i + l ] - total [ i + Integer . parseInt ( l / 2 ) ] ) && ( total [ j ] == total [ j - 1 ] ) ) {
        ans = Math . max ( ans , l ) ;
      }
    }
    l = l + 2 ;
  }
  return ans ;
}
|||

MAXIMUM_PATH_SUM_MATRIX

public static int findMaxPath ( int [ ] [ ] mat ) {
  int res = - 1 ;
  for ( int i = 0 ;
  i < M ;
  i ++ ) res = Math . max ( res , mat [ 0 ] [ i ] ) ;
  for ( int i = 1 ;
  i < N ;
  i ++ ) {
    res = - 1 ;
    for ( int j = 0 ;
    j < M ;
    j ++ ) {
      if ( ( j > 0 && j < M - 1 ) || ( j > 0 && j < M - 1 ) ) mat [ i ] [ j ] += Math . max ( mat [ i - 1 ] [ j ] , Math . max ( mat [ i - 1 ] [ j - 1 ] , mat [ i - 1 ] [ j + 1 ] ) ) ;
      else if ( ( j > 0 ) || ( j < M - 1 ) ) mat [ i ] [ j ] += Math . max ( mat [ i - 1 ] [ j ] , mat [ i - 1 ] [ j - 1 ] ) ;
      else if ( ( j < M - 1 ) || ( j > M - 1 ) ) mat [ i ] [ j ] += Math . max ( mat [ i - 1 ] [ j ] , mat [ i - 1 ] [ j + 1 ] ) ;
      res = Math . max ( mat [ i ] [ j ] , res ) ;
    }
  }
  return res ;
}
|||

MAXIMUM_CONSECUTIVE_REPEATING_CHARACTER_STRING

public static String maxRepeating ( String str ) {
  int l = str . length ( ) ;
  int count = 0 ;
  String res = str . substring ( 0 , l ) ;
  for ( int i = 0 ;
  i < l ;
  i ++ ) {
    int curCount = 1 ;
    for ( int j = i + 1 ;
    j < l ;
    j ++ ) {
      if ( ( str . charAt ( i ) != str . charAt ( j ) ) && ( str . charAt ( j ) != ' ' ) ) {
        break ;
      }
      curCount ++ ;
    }
    if ( curCount > count ) {
      count = curCount ;
      res = str . substring ( i , j ) ;
    }
  }
  return res ;
}
|||

MAXIMUM_LENGTH_SUBSEQUENCE_DIFFERENCE_ADJACENT_ELEMENTS_EITHER_0_1

public static int maxLenSub ( int [ ] arr , int n ) {
  int [ ] mls = new int [ n ] ;
  int max = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) mls [ i ] = 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < i ;
    j ++ ) {
      if ( ( Math . abs ( arr [ i ] - arr [ j ] ) <= 1 && mls [ i ] < mls [ j ] + 1 ) || ( Math . abs ( arr [ i ] - arr [ j ] ) < 1 && mls [ i ] < mls [ j ] + 1 ) ) {
        mls [ i ] = mls [ j ] + 1 ;
      }
    }
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( max < mls [ i ] ) && ( mls [ i ] > max ) ) {
      max = mls [ i ] ;
    }
  }
  return max ;
}
|||

BREAKING_NUMBER_FIRST_PART_INTEGRAL_DIVISION_SECOND_POWER_10

public static int calculate ( String N ) {
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
|||

PROGRAM_BINARY_DECIMAL_CONVERSION

public static int binaryToDecimal ( int n ) {
  int num = n ;
  int decValue = 0 ;
  int base = 1 ;
  int temp = num ;
  while ( ( temp = temp % 10 ) != 0 ) {
    int lastDigit = temp % 10 ;
    temp = ( int ) ( temp / 10 ) ;
    decValue += lastDigit * base ;
    base = base * 2 ;
  }
  return decValue ;
}
|||

HOW_CAN_WE_SUM_THE_DIGITS_OF_A_GIVEN_NUMBER_IN_SINGLE_STATEMENT

public static int getSum ( int n ) {
  int sum = 0 ;
  while ( ( n != 0 ) && ( n % 10 == 0 ) ) {
    sum = sum + ( int ) ( n % 10 ) ;
    n = ( int ) ( n / 10 ) ;
  }
  return sum ;
}
|||

FIND_N_TH_ELEMENT_FROM_STERNS_DIATOMIC_SERIES

public static int findSDSFunc ( int n ) {
  int [ ] DP = new int [ n + 1 ] ;
  DP [ 0 ] = 0 ;
  DP [ 1 ] = 1 ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    if ( ( Integer . bitCount ( i % 2 ) == 0 ) && ( DP [ i ] == 0 ) ) {
      DP [ i ] = DP [ Integer . bitCount ( i / 2 ) ] ;
    }
    else {
      DP [ i ] = ( DP [ Integer . bitCount ( ( i - 1 ) / 2 ) ] + DP [ Integer . bitCount ( ( i + 1 ) / 2 ) ] ) ;
    }
  }
  return DP [ n ] ;
}
|||

NUMBER_SINK_NODES_GRAPH

public static int countSink ( int n , int m , int [ ] edgeFrom , int [ ] edgeTo ) {
  int [ ] mark = new int [ n + 1 ] ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) mark [ edgeFrom [ i ] ] = 1 ;
  int count = 0 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) if ( ( ! mark [ i ] ) && ( ! mark [ i - 1 ] ) ) count ++ ;
  return count ;
}
|||

BREAK_NUMBER_THREE_PARTS

public static int countOfWays ( int n ) {
  int count = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      for ( int k = 0 ;
      k <= n ;
      k ++ ) {
        if ( ( i + j + k == n ) && ( i + j + k == n ) ) {
          count = count + 1 ;
        }
      }
    }
  }
  return count ;
}
|||

PRINT_DISTINCT_ELEMENTS_GIVEN_INTEGER_ARRAY

public static void printDistinct ( int [ ] arr , int n ) {
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    int d = 0 ;
    for ( int j = 0 ;
    j <= i ;
    j ++ ) {
      if ( ( arr [ i ] == arr [ j ] ) && ( arr [ j ] != 0 ) ) {
        d = 1 ;
        break ;
      }
    }
    if ( ( d == 0 ) && ( arr [ i ] != 0 ) ) {
      System . out . println ( arr [ i ] ) ;
    }
  }
}
|||

MAXIMUM_NUMBER_SEGMENTS_LENGTHS_B_C

public static int maximumSegments ( int n , int a , int b , int c ) {
  int [ ] dp = new int [ n + 10 ] ;
  dp [ 0 ] = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( dp [ i ] != - 1 ) && ( i + a <= n ) ) {
      if ( ( i + a <= n ) && ( i + b <= n ) ) {
        dp [ i + a ] = Math . max ( dp [ i ] + 1 , dp [ i + a ] ) ;
      }
      if ( ( i + b <= n ) && ( i + c <= n ) ) {
        dp [ i + b ] = Math . max ( dp [ i ] + 1 , dp [ i + b ] ) ;
      }
      if ( ( i + c <= n ) && ( i + d <= n ) ) {
        dp [ i + d ] = Math . max ( dp [ i ] + 1 , dp [ i + d ] ) ;
      }
    }
  }
  return dp [ n ] ;
}
|||

CHECK_VALID_SEQUENCE_DIVISIBLE_M

public static boolean isPossible ( int n , int index , int Sum , int M , int [ ] arr , int [ ] [ ] dp ) {
  MAX = Integer . MAX_VALUE ;
  if ( index == n ) {
    if ( ( Sum % M ) == 0 ) return true ;
    return false ;
  }
  if ( dp [ index ] [ Sum ] != - 1 ) return dp [ index ] [ Sum ] ;
  boolean placeAdd = isPossible ( n , index + 1 , Sum + arr [ index ] , M , arr , dp ) ;
  boolean placeMinus = isPossible ( n , index + 1 , Sum - arr [ index ] , M , arr , dp ) ;
  boolean res = placeAdd || placeMinus ;
  dp [ index ] [ Sum ] = res ;
  return res ;
}
|||

FIND_PAIR_WITH_GREATEST_PRODUCT_IN_ARRAY

public static int findGreatest ( int [ ] arr , int n ) {
  int result = - 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n - 1 ;
    j ++ ) {
      for ( int k = j + 1 ;
      k < n ;
      k ++ ) {
        if ( ( arr [ j ] * arr [ k ] == arr [ i ] ) && ( arr [ i ] * arr [ k ] == arr [ j ] ) ) {
          result = Math . max ( result , arr [ i ] ) ;
        }
      }
    }
  }
  return result ;
}
|||

MAXIMUM_SUBARRAY_SUM_ARRAY_CREATED_REPEATED_CONCATENATION

public static int maxSubArraySumRepeated ( int [ ] a , int n , int k ) {
  int maxSoFar = - 2147483648 ;
  int maxEndingHere = 0 ;
  for ( int i = 0 ;
  i < n * k ;
  i ++ ) {
    maxEndingHere = maxEndingHere + a [ i % n ] ;
    if ( ( maxSoFar < maxEndingHere ) && ( maxEndingHere < 0 ) ) {
      maxSoFar = maxEndingHere ;
    }
    if ( ( maxEndingHere < 0 ) && ( maxEndingHere < n ) ) {
      maxEndingHere = 0 ;
    }
  }
  return maxSoFar ;
}
|||

LEONARDO_NUMBER_1

public static int leonardo ( int n ) {
  int [ ] dp = new int [ n + 1 ] ;
  ;
  dp [ 0 ] = 1 ;
  ;
  dp [ 1 ] = 1 ;
  ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    dp [ i ] = dp [ i - 1 ] + dp [ i - 2 ] + 1 ;
    ;
  }
  return dp [ n ] ;
}
|||

SUM_OF_ALL_SUBSTRINGS_OF_A_STRING_REPRESENTING_A_NUMBER

public static int sumOfSubstrings ( String num ) {
  int n = num . length ( ) ;
  int [ ] sumofdigit = new int [ n ] ;
  sumofdigit [ 0 ] = Integer . parseInt ( num . substring ( 0 , 1 ) ) ;
  int res = sumofdigit [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    int numi = Integer . parseInt ( num . substring ( i , i + 1 ) ) ;
    sumofdigit [ i ] = ( i + 1 ) * numi + 10 * sumofdigit [ i - 1 ] ;
    res += sumofdigit [ i ] ;
  }
  return res ;
}
|||

PRUFER_CODE_TREE_CREATION

public static void printTreeEdges ( int [ ] prufer , int m ) {
  int vertices = m + 2 ;
  int [ ] vertexSet = new int [ vertices ] ;
  for ( int i = 0 ;
  i < vertices - 2 ;
  i ++ ) vertexSet [ prufer [ i ] - 1 ] ++ ;
  System . out . println ( "The edge set E(G) is :" ) ;
  int j ;
  for ( int i = 0 ;
  i < vertices - 2 ;
  i ++ ) {
    for ( j = 0 ;
    j < vertices ;
    j ++ ) {
      if ( ( vertexSet [ j ] == 0 ) && ( prufer [ i ] == 0 ) ) {
        vertexSet [ j ] = - 1 ;
        System . out . print ( "(" + ( j + 1 ) + ", " + prufer [ i ] + ") " ) ;
        vertexSet [ prufer [ i ] - 1 ] -- ;
        break ;
      }
    }
  }
  j = 0 ;
  for ( int i = 0 ;
  i < vertices ;
  i ++ ) {
    if ( ( vertexSet [ i ] == 0 && j == 0 ) || ( vertexSet [ i ] == 1 && j == 1 ) ) {
      System . out . print ( "(" + ( i + 1 ) + ", " ) ;
      j ++ ;
    }
    else if ( ( vertexSet [ i ] == 0 && j == 1 ) || ( vertexSet [ i ] == 2 && j == 2 ) ) {
      System . out . print ( ( i + 1 ) + ")" ) ;
    }
  }
}
|||

PROGRAM_FIND_SMALLEST_DIFFERENCE_ANGLES_TWO_PARTS_GIVEN_CIRCLE

public static int findMinimumAngle ( int [ ] arr , int n ) {
  int l = 0 ;
  int _sum = 0 ;
  int ans = 360 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    _sum += arr [ i ] ;
    while ( _sum >= 180 ) {
      ans = Math . min ( ans , 2 * Math . abs ( 180 - _sum ) ) ;
      _sum -= arr [ l ] ;
      l ++ ;
    }
    ans = Math . min ( ans , 2 * Math . abs ( 180 - _sum ) ) ;
  }
  return ans ;
}
|||

FIND_MAXIMUM_AVERAGE_SUBARRAY_OF_K_LENGTH

public static int findMaxAverage ( int [ ] arr , int n , int k ) {
  if ( k > n ) return - 1 ;
  int [ ] csum = new int [ n ] ;
  csum [ 0 ] = arr [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) csum [ i ] = csum [ i - 1 ] + arr [ i ] ;
  ;
  int maxSum = csum [ k - 1 ] ;
  int maxEnd = k - 1 ;
  for ( int i = k ;
  i < n ;
  i ++ ) {
    int currSum = csum [ i ] - csum [ i - k ] ;
    if ( currSum > maxSum ) {
      maxSum = currSum ;
      maxEnd = i ;
    }
  }
  return maxEnd - k + 1 ;
}
|||

SQUARE_PYRAMIDAL_NUMBER_SUM_SQUARES

public static int findS ( int s ) {
  int _sum = 0 ;
  int n = 1 ;
  while ( ( _sum < s ) && ( _sum < s ) ) {
    _sum += n * n ;
    n ++ ;
  }
  n -- ;
  if ( _sum == s ) return n ;
  return - 1 ;
}
|||

PROGRAM_TO_CALCULATE_AREA_OF_AN_CIRCLE_INSCRIBED_IN_A_SQUARE

public static double areaOfInscribedCircle ( double a ) {
  return ( PI / 4 ) * a * a ;
}
|||

MINIMUM_NUMBER_CHARACTERS_REMOVED_MAKE_BINARY_STRING_ALTERNATE

public static int countToMake0lternate ( String s ) {
  int result = 0 ;
  for ( int i = 0 ;
  i < s . length ( ) - 1 ;
  i ++ ) {
    if ( ( s . charAt ( i ) == s . charAt ( i + 1 ) ) && ( s . charAt ( i + 2 ) == s . charAt ( i + 3 ) ) ) {
      result ++ ;
    }
  }
  return result ;
}
|||

FIND_ELEMENTS_PRESENT_FIRST_ARRAY_NOT_SECOND

public static void findMissing ( int [ ] a , int [ ] b , int n , int m ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < m ;
    j ++ ) {
      if ( ( a [ i ] == b [ j ] ) && ( a [ i ] != b [ j ] ) ) {
        break ;
      }
    }
    if ( ( j == m - 1 ) && ( a [ i ] == b [ j ] ) ) {
      System . out . print ( a [ i ] + " " ) ;
    }
  }
}
|||

REARRANGE_ARRAY_MAXIMUM_MINIMUM_FORM

public static int [ ] rearrange ( int [ ] arr , int n ) {
  int [ ] temp = n * new int [ n ] ;
  int small = 0 , large = n - 1 ;
  boolean flag = true ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( flag == true ) {
      temp [ i ] = arr [ large ] ;
      large -- ;
    }
    else {
      temp [ i ] = arr [ small ] ;
      small ++ ;
    }
    flag = ( boolean ) ( 1 - flag ) ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    arr [ i ] = temp [ i ] ;
  }
  return arr ;
}
|||

DYNAMIC_PROGRAMMING_SET_15_LONGEST_BITONIC_SUBSEQUENCE

public static int lbs ( int [ ] arr ) {
  int n = arr . length ;
  int [ ] lis = new int [ n + 1 ] ;
  lis [ 0 ] = 1 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    lis [ i ] = i ;
  }
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= i ;
    j ++ ) {
      if ( ( ( arr [ i ] > arr [ j ] ) && ( lis [ i ] < lis [ j ] + 1 ) ) || ( ( arr [ i ] > arr [ j ] ) && ( lis [ i ] < lis [ j ] + 1 ) ) ) {
        lis [ i ] = j ;
      }
    }
  }
  int [ ] lds = new int [ n + 1 ] ;
  lds [ 0 ] = 1 ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    for ( int j = 0 ;
    j < i - 1 ;
    j ++ ) {
      if ( ( arr [ i ] > arr [ j ] && lds [ i ] < lds [ j ] + 1 ) || ( ( arr [ i ] > arr [ j ] ) && ( lis [ i ] < lis [ j ] + 1 ) ) ) {
        lds [ i ] = j ;
      }
    }
  }
  int maximum = lis [ 0 ] + lds [ 0 ] - 1 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    maximum = Math . max ( ( lis [ i ] + lds [ i ] - 1 ) , maximum ) ;
  }
  return maximum ;
}
|||

COUNT_PAIRS_WHOSE_PRODUCTS_EXIST_IN_ARRAY

public static int countPairs ( int [ ] arr , int n ) {
  int result = 0 ;
  ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= n ;
    j ++ ) {
      int product = arr [ i ] * arr [ j ] ;
      ;
      for ( int k = 0 ;
      k <= n ;
      k ++ ) {
        if ( ( arr [ k ] == product ) && ( arr [ j ] == product ) ) {
          result = result + 1 ;
          break ;
        }
      }
    }
  }
  return result ;
}
|||

COUNT_SINGLE_NODE_ISOLATED_SUB_GRAPHS_DISCONNECTED_GRAPH

public static int compute ( int [ ] [ ] graph , int N ) {
  int count = 0 ;
  for ( int i = 1 ;
  i <= N ;
  i ++ ) {
    if ( ( graph [ i ] . length == 0 ) && ( graph [ i ] [ 0 ] . length == 0 ) ) {
      count ++ ;
    }
  }
  return count ;
}
|||

HARDY_RAMANUJAN_THEOREM

public static int exactPrimeFactorCount ( int n ) {
  int count = 0 ;
  if ( ( n % 2 == 0 ) && ( n % 3 == 0 ) ) {
    count = count + 1 ;
    while ( ( n % 2 == 0 ) && ( n % 3 == 0 ) ) {
      n = ( int ) ( n / 2 ) ;
    }
  }
  int i = 3 ;
  while ( ( i <= ( int ) Math . sqrt ( n ) ) && ( n % i == 0 ) ) {
    if ( ( n % i == 0 ) && ( n % 3 == 0 ) ) {
      count = count + 1 ;
      while ( ( n % i == 0 ) && ( n % 3 == 0 ) ) {
        n = ( int ) ( n / i ) ;
      }
    }
    i = i + 2 ;
  }
  if ( ( n > 2 ) && ( n % 3 == 0 ) ) {
    count = count + 1 ;
  }
  return count ;
}
|||

SHORTEST_COMMON_SUPERSEQUENCE_1

public static int superSeq ( int [ ] X , int [ ] Y , int m , int n ) {
  int [ ] [ ] dp = new int [ m + 2 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i < m + 2 ;
  i ++ ) {
    for ( int j = 0 ;
    j < n + 1 ;
    j ++ ) {
      if ( ( ! i ) && ( ! j ) ) {
        dp [ i ] [ j ] = j ;
      }
      else if ( ( ! i ) && ( ! j ) ) {
        dp [ i ] [ j ] = i ;
      }
      else if ( ( X [ i - 1 ] == Y [ j - 1 ] ) && ( X [ j - 1 ] == Y [ i ] ) ) {
        dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ] ;
      }
      else {
        dp [ i ] [ j ] = 1 + Math . min ( dp [ i - 1 ] [ j ] , dp [ i ] [ j - 1 ] ) ;
      }
    }
  }
  return dp [ m ] [ n ] ;
}
|||

POWER_SET

public static void printPowerSet ( int [ ] set , int setSize ) {
  int pow_set_size = ( int ) ( Math . pow ( 2 , setSize ) ) ;
  ;
  int counter ;
  int j ;
  for ( counter = 0 ;
  counter <= pow_set_size ;
  counter ++ ) {
    for ( j = 0 ;
    j <= set_size ;
    j ++ ) {
      if ( ( ( counter & ( 1 << j ) ) > 0 ) && ( ( counter & ( 1 << j ) ) > 0 ) ) {
        System . out . print ( set [ j ] + "" ) ;
      }
    }
    System . out . println ( "" ) ;
  }
}
|||

CHECK_ARRAY_MAJORITY_ELEMENT

public static boolean isMajority ( int [ ] a ) {
  int [ ] mp = new int [ a . length ] ;
  for ( int i = 0 ;
  i < a . length ;
  i ++ ) {
    if ( a [ i ] < mp [ i ] ) {
      mp [ i ] ++ ;
    }
    else {
      mp [ i ] = 1 ;
    }
  }
  for ( int x : mp ) {
    if ( mp [ x ] >= a . length / 2 ) {
      return true ;
    }
  }
  return false ;
}
|||

PRINT_GIVEN_MATRIX_COUNTER_CLOCK_WISE_SPIRAL_FORM

public static void counterClockspiralPrint ( int m , int n , int [ ] [ ] arr ) {
  int k = 0 ;
  int l = 0 ;
  int cnt = 0 ;
  int total = m * n ;
  while ( ( k < m && l < n ) || ( k > m && l > n ) ) {
    if ( ( cnt == total ) || ( cnt == 0 ) ) break ;
    for ( int i = k ;
    i < m ;
    i ++ ) {
      System . out . print ( arr [ i ] [ l ] + " " ) ;
      cnt ++ ;
    }
    l ++ ;
    if ( ( cnt == total ) || ( cnt == 0 ) ) break ;
    for ( int i = l ;
    i < n ;
    i ++ ) {
      System . out . print ( arr [ m - 1 ] [ i ] + " " ) ;
      cnt ++ ;
    }
    m -- ;
    if ( ( cnt == total ) || ( cnt == 0 ) ) break ;
    if ( ( k < m ) && ( k > k ) ) {
      for ( int i = m - 1 ;
      i >= k ;
      i -- ) {
        System . out . print ( arr [ i ] [ n - 1 ] + " " ) ;
        cnt ++ ;
      }
      n -- ;
    }
    if ( ( cnt == total ) || ( cnt == 0 ) ) break ;
    if ( ( l < n ) && ( l > l ) ) {
      for ( int i = n - 1 ;
      i >= l ;
      i -- ) {
        System . out . print ( arr [ k ] [ i ] + " " ) ;
        cnt ++ ;
      }
      k ++ ;
    }
  }
}
|||

PRIMALITY_TEST_SET_1_INTRODUCTION_AND_SCHOOL_METHOD

public static boolean isPrime ( int n ) {
  if ( n <= 1 ) return false ;
  for ( int i = 2 ;
  i < n ;
  i ++ ) if ( n % i == 0 ) return false ;
  ;
  return true ;
}
|||

FIND_CHARACTER_FIRST_STRING_PRESENT_MINIMUM_INDEX_SECOND_STRING

public static void printMinIndexChar ( String Str , String patt ) {
  int minIndex = 10 * 9 ;
  int m = Str . length ( ) ;
  int n = patt . length ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < m ;
    j ++ ) {
      if ( ( patt . charAt ( i ) == Str . charAt ( j ) && j < minIndex ) || ( patt . charAt ( i ) == Str . charAt ( j ) && j < minIndex ) ) {
        minIndex = j ;
        break ;
      }
    }
  }
  if ( ( minIndex != 10 * 9 ) && ( minIndex != 0 ) ) {
    System . out . println ( "Minimum Index Character = " + Str . charAt ( minIndex ) ) ;
  }
  else {
    System . out . println ( "No character present" ) ;
  }
}
|||

PROGRAM_TO_FIND_TRANSPOSE_OF_A_MATRIX_1

public static void transpose ( double [ ] [ ] A , double [ ] [ ] B ) {
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    for ( int j = 0 ;
    j < M ;
    j ++ ) {
      B [ i ] [ j ] = A [ j ] [ i ] ;
    }
  }
}
|||

COUNT_NATURAL_NUMBERS_WHOSE_PERMUTATION_GREATER_NUMBER

public static int countNumber ( int n ) {
  int result = 0 ;
  for ( int i = 1 ;
  i <= 10 ;
  i ++ ) {
    Stack < Integer > s = new Stack < Integer > ( ) ;
    if ( ( i <= n ) && ( s . size ( ) != 0 ) ) {
      s . push ( i ) ;
      result ++ ;
    }
    while ( s . size ( ) != 0 ) {
      int tp = s . pop ( ) ;
      s . pop ( ) ;
      for ( int j = tp % 10 ;
      j < 10 ;
      j ++ ) {
        int x = tp * 10 + j ;
        if ( ( x <= n ) && ( s . size ( ) != 0 ) ) {
          s . push ( x ) ;
          result ++ ;
        }
      }
    }
  }
  return result ;
}
|||

FIND_FIRST_NATURAL_NUMBER_WHOSE_FACTORIAL_DIVISIBLE_X

public static int firstFactorialDivisibleNumber ( int x ) {
  int i ;
  int fact = 1 ;
  ;
  for ( i = 1 ;
  i <= x ;
  i ++ ) {
    fact = fact * i ;
    if ( ( fact % x == 0 ) && ( i % x == 0 ) ) break ;
  }
  return i ;
}
|||

PRINT_EQUAL_SUM_SETS_ARRAY_PARTITION_PROBLEM_SET_2

public static void printEqualSumSets ( int [ ] arr , int n ) {
  int sumArray = Arrays . stream ( arr ) . mapToInt ( Integer :: intValue ) . sum ( ) ;
  if ( ( sumArray & 1 ) != 0 ) {
    System . out . println ( "-1" ) ;
    return ;
  }
  int k = sumArray >>> 1 ;
  boolean [ ] [ ] dp = new boolean [ n + 1 ] [ k + 1 ] ;
  for ( int i = 1 ;
  i <= k ;
  i ++ ) {
    dp [ 0 ] [ i ] = false ;
  }
  for ( int i = 0 ;
  i < n + 1 ;
  i ++ ) {
    dp [ i ] [ 0 ] = true ;
  }
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int currSum = 1 ;
    currSum <= k ;
    currSum ++ ) {
      dp [ i ] [ currSum ] = dp [ i - 1 ] [ currSum ] ;
      if ( ( arr [ i - 1 ] <= currSum ) && ( dp [ i ] [ currSum ] || dp [ i - 1 ] [ currSum - arr [ i - 1 ] ] ) ) {
        dp [ i ] [ currSum ] = ( dp [ i ] [ currSum ] || dp [ i - 1 ] [ currSum - arr [ i ] ] ) ;
      }
    }
  }
  ArrayList < Integer > set1 = new ArrayList < Integer > ( ) , set2 = new ArrayList < Integer > ( ) ;
  if ( ( ! dp [ n ] [ k ] ) && ( ! dp [ k ] [ n ] ) ) {
    System . out . println ( "-1" ) ;
    return ;
  }
  int i = n ;
  int currSum = k ;
  while ( ( i > 0 && currSum >= 0 ) || ( i < n ) ) {
    if ( ( dp [ i - 1 ] [ currSum ] ) && ( dp [ i - 1 ] [ currSum - arr [ i - 1 ] ] ) ) {
      i -- ;
      set2 . add ( arr [ i ] ) ;
    }
    else if ( ( dp [ i - 1 ] [ currSum - arr [ i ] ] ) && ( dp [ i - 1 ] [ currSum - arr [ i ] ] ) ) {
      i -- ;
      currSum -= arr [ i ] ;
      set1 . add ( arr [ i ] ) ;
    }
  }
  System . out . println ( "Set 1 elements:" + set1 )
|||

COUNTING_PAIRS_PERSON_CAN_FORM_PAIR_ONE_1

public static int numberOfWays ( int x ) {
  if ( x == 0 || x == 1 ) {
    return 1 ;
  }
  else {
    return ( numberOfWays ( x - 1 ) + ( x - 1 ) * numberOfWays ( x - 2 ) ) ;
  }
}
|||

COUNT_NEGATIVE_NUMBERS_IN_A_COLUMN_WISE_ROW_WISE_SORTED_MATRIX

public static int countNegative ( int [ ] [ ] M , int n , int m ) {
  int count = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < m ;
    j ++ ) {
      if ( M [ i ] [ j ] < 0 ) {
        count ++ ;
      }
      else {
        break ;
      }
    }
  }
  return count ;
}
|||

COUNT_SET_BITS_IN_AN_INTEGER

static int countSetBits ( long n ) {
  int count = 0 ;
  while ( ( n > 0 ) && ( n & 1 ) != 0 ) {
    count += n & 1 ;
    n >>>= 1 ;
  }
  return count ;
}
|||

MODULUS_TWO_FLOAT_DOUBLE_NUMBERS

public static int findMod ( int a , int b ) {
  if ( ( a < 0 ) && ( b < 0 ) ) a = - a ;
  if ( ( b < 0 ) && ( a > 0 ) ) b = - b ;
  int mod = a ;
  while ( ( mod >= b ) && ( mod < a ) ) mod = mod - b ;
  if ( ( a < 0 ) && ( b < 0 ) ) return - mod ;
  return mod ;
}
|||

FIND_A_SPECIFIC_PAIR_IN_MATRIX_1

public static int findMaxValue ( int [ ] [ ] mat ) {
  int maxValue = - Integer . MAX_VALUE - 1 ;
  int [ ] [ ] maxArr = new int [ N ] [ N ] ;
  for ( int y = 0 ;
  y < N ;
  y ++ ) {
    maxArr [ y ] [ y ] = 0 ;
  }
  maxArr [ N - 1 ] [ N - 1 ] = mat [ N - 1 ] [ N - 1 ] ;
  int maxv = mat [ N - 1 ] [ N - 1 ] ;
  ;
  for ( int j = N - 2 ;
  j >= 0 ;
  j -- ) {
    if ( ( mat [ N - 1 ] [ j ] > maxv ) && ( maxArr [ j ] [ j ] == maxv ) ) {
      maxv = mat [ N - 1 ] [ j ] ;
    }
    maxArr [ j ] [ j ] = maxv ;
  }
  maxv = mat [ N - 1 ] [ N - 1 ] ;
  for ( int i = N - 2 ;
  i >= 0 ;
  i -- ) {
    if ( ( mat [ i ] [ N - 1 ] > maxv ) && ( maxArr [ i ] [ N - 1 ] == maxv ) ) {
      maxv = mat [ i ] [ N - 1 ] ;
    }
    maxArr [ i ] [ N - 1 ] = maxv ;
  }
  for ( int i = N - 2 ;
  i >= 0 ;
  i -- ) {
    for ( int j = N - 2 ;
    j >= 0 ;
    j -- ) {
      if ( ( maxArr [ i + 1 ] [ j + 1 ] - mat [ i ] [ j ] > maxValue ) && ( maxArr [ i + 1 ] [ j ] == maxv ) ) {
        maxValue = ( maxArr [ i + 1 ] [ j + 1 ] - mat [ i ] [ j ] ) ;
      }
      maxArr [ i ] [ j ] = Math . max ( mat [ i ] [ j ] , Math . max ( maxArr [ i ] [ j + 1 ] , maxArr [ i + 1 ] [ j ] ) ) ;
    }
  }
  return maxValue ;
}
|||

MINIMUM_SUM_TWO_NUMBERS_FORMED_DIGITS_ARRAY

public static int solve ( int [ ] arr , int n ) {
  Arrays . sort ( arr ) ;
  int a = 0 ;
  int b = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( i % 2 != 0 ) && ( arr [ i ] > 0 ) ) {
      a = a * 10 + arr [ i ] ;
    }
    else {
      b = b * 10 + arr [ i ] ;
    }
  }
  return a + b ;
}
|||

COUNT_DISTINCT_NON_NEGATIVE_PAIRS_X_Y_SATISFY_INEQUALITY_XX_YY_N_2_1

public static int countSolutions ( int n ) {
  int x = 0 ;
  int res = 0 ;
  int yCount = 0 ;
  while ( ( yCount * yCount < n ) && ( yCount != 0 ) ) {
    yCount = yCount + 1 ;
  }
  while ( ( yCount != 0 ) && ( yCount != n ) ) {
    res = res + yCount ;
    x = x + 1 ;
    while ( ( yCount != 0 ) && ( x * x + ( yCount - 1 ) * ( yCount - 1 ) >= n ) ) {
      yCount = yCount - 1 ;
    }
  }
  return res ;
}
|||

FIND_INDEX_GIVEN_FIBONACCI_NUMBER_CONSTANT_TIME

public static int findIndex ( int n ) {
  if ( ( n <= 1 ) || ( n > 2 ) ) return n ;
  int a = 0 ;
  int b = 1 ;
  int c = 1 ;
  int res = 1 ;
  while ( ( c < n ) && ( res == 1 ) ) {
    c = a + b ;
    res = res + 1 ;
    a = b ;
    b = c ;
  }
  return res ;
}
|||

PROGRAM_OCTAL_DECIMAL_CONVERSION

public static int octalToDecimal ( int n ) {
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
|||

FIND_PERMUTED_ROWS_GIVEN_ROW_MATRIX

public static void permutatedRows ( int [ ] [ ] mat , int m , int n , int r ) {
  Set < Integer > s = new HashSet < Integer > ( ) ;
  for ( int j = 0 ;
  j < n ;
  j ++ ) s . add ( mat [ r ] [ j ] ) ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) {
    if ( i == r ) continue ;
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( mat [ i ] [ j ] != s . contains ( mat [ r ] [ j ] ) ) {
        j = j - 2 ;
        break ;
      }
    }
    if ( j + 1 != n ) continue ;
    System . out . println ( i ) ;
  }
}
|||

PRINT_A_CLOSEST_STRING_THAT_DOES_NOT_CONTAIN_ADJACENT_DUPLICATES

public static String noAdjacentDup ( String s ) {
  int n = s . length ( ) ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( ( s . charAt ( i ) == s . charAt ( i - 1 ) ) && ( s . charAt ( i ) == s . charAt ( i - 1 ) ) ) {
      s . charAt ( i ) = "a" ;
      while ( ( s . charAt ( i ) == s . charAt ( i - 1 ) ) || ( i + 1 < n && s . charAt ( i ) == s . charAt ( i + 1 ) ) ) {
        s . charAt ( i ) ++ ;
      }
      i ++ ;
    }
  }
  return s ;
}
|||

SUM_MANHATTAN_DISTANCES_PAIRS_POINTS

public static int distancesum ( int [ ] x , int [ ] y , int n ) {
  int sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      sum += ( Math . abs ( x [ i ] - x [ j ] ) + Math . abs ( y [ i ] - y [ j ] ) ) ;
    }
  }
  return sum ;
}
|||

PROGRAM_FIND_STRING_START_END_GEEKS

public static boolean isCornerPresent ( String str , String corner ) {
  int n = str . length ( ) ;
  int cl = corner . length ( ) ;
  if ( ( n < cl ) || ( n > cl ) ) return false ;
  return ( ( str . substring ( 0 , cl ) . equals ( corner ) ) && ( str . substring ( n - cl , n ) . equals ( corner ) ) ) ;
}
|||

LONGEST_SUBARRAY_COUNT_1S_ONE_COUNT_0S

public static int lenOfLongSubarr ( int [ ] arr , int n ) {
  int [ ] um = new int [ 10 ] ;
  for ( int i = 0 ;
  i < 10 ;
  i ++ ) {
    um [ i ] = 0 ;
  }
  int sum = 0 ;
  int maxLen = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] == 0 ) {
      sum ++ ;
    }
    else {
      sum ++ ;
    }
    if ( ( sum == 1 ) && ( i != 0 ) ) {
      maxLen = i + 1 ;
    }
    else if ( ( sum != 0 ) && ( i != 0 ) ) {
      um [ sum ] = i ;
    }
    if ( ( ( sum - 1 ) < um . length ) && ( maxLen < ( i - um [ sum - 1 ] ) ) ) {
      maxLen = i - um [ sum - 1 ] ;
    }
  }
  return maxLen ;
}
|||

DIVIDE_CONQUER_SET_6_SEARCH_ROW_WISE_COLUMN_WISE_SORTED_2D_ARRAY

public static void search ( int [ ] [ ] mat , int fromRow , int toRow , int fromCol , int toCol , int key ) {
  int i = fromRow + ( toRow - fromRow ) / 2 ;
  ;
  int j = fromCol + ( toCol - fromCol ) / 2 ;
  ;
  if ( ( mat [ i ] [ j ] == key ) && ( mat [ i ] [ j ] == key ) ) {
    System . out . println ( "Found " + key + " at " + i + " " + j ) ;
    ;
  }
  else {
    if ( ( i != toRow || j != fromCol ) && ( mat [ fromRow ] [ i ] == key ) && ( mat [ fromCol ] [ j ] == key ) ) {
      search ( mat , fromRow , i , j , toCol , key ) ;
    }
    if ( ( fromRow == toRow && fromCol + 1 == toCol ) && ( mat [ fromRow ] [ toCol ] == key ) && ( mat [ fromCol ] [ j ] == key ) ) {
      if ( ( mat [ fromRow ] [ toCol ] == key ) && ( mat [ fromCol ] [ j ] == key ) ) {
        System . out . println ( "Found " + key + " at " + fromRow + " " + toCol ) ;
        ;
      }
    }
    if ( ( mat [ i ] [ j ] < key ) && ( mat [ i ] [ j ] > key ) && ( mat [ i ] [ j ] > key ) ) {
      if ( ( mat [ i ] [ j ] < key ) && ( mat [ i ] [ j ] > key ) ) {
        if ( ( mat [ i ] [ j ] > key ) && ( mat [ i ] [ j ] < key ) ) {
          if ( ( mat [ i ] [ j ] > key ) && ( mat [ i ] [ j ] < key ) ) {
            if ( ( mat [ i ] [ j ] > key ) && ( mat [ i ] [ j ] > key ) ) {
              if ( ( mat [ i ] [ j ] < key ) && ( mat [ i ] [ j ] > key ) ) {
                if ( ( mat [ i ] [ j ] > key ) && ( mat [ i ] [ j ] > key ) ) {
                }
              }
            }
          }
        }
      }
    }
  }
}
|||

SHORTEST_COMMON_SUPERSEQUENCE

public static int superSeq ( int [ ] X , int [ ] Y , int m , int n ) {
  if ( ( m == 0 ) || ( n == 0 ) ) return n ;
  if ( ( X [ m - 1 ] == Y [ n - 1 ] ) && ( X [ m ] == Y [ n ] ) ) return 1 + superSeq ( X , Y , m - 1 , n - 1 ) ;
  return 1 + Math . min ( superSeq ( X , Y , m - 1 , n ) , superSeq ( X , Y , m , n - 1 ) ) ;
}
|||

URLIFY_GIVEN_STRING_REPLACE_SPACES

public static int replaceSpaces ( String string ) {
  int len = string . length ( ) ;
  int i = len ;
  int spaceCount = string . indexOf ( '' ) ;
  int newLength = i + spaceCount * 2 ;
  if ( newLength > MAX ) return - 1 ;
  int index = newLength - 1 ;
  StringBuilder sb = Lists . newArrayListWithCapacity ( newLength ) ;
  for ( int f = i - 2 ;
  f < newLength - 2 ;
  f ++ ) {
    sb . append ( '0' ) ;
  }
  for ( int j = i - 1 ;
  j > 0 ;
  j -- ) {
    if ( sb . charAt ( j ) == '' ) {
      sb . setCharAt ( index , '0' ) ;
      sb . setCharAt ( index - 1 , '2' ) ;
      sb . setCharAt ( index - 2 , '%' ) ;
      index = index - 3 ;
    }
    else {
      sb . setCharAt ( index , sb . charAt ( j ) ) ;
      index -- ;
    }
  }
  return sb . toString ( ) . length ( ) ;
}
|||

MAXIMUM_PATH_SUM_STARTING_CELL_0_TH_ROW_ENDING_CELL_N_1_TH_ROW

public static int MaximumPath ( int [ ] [ ] Mat ) {
  int result = 0 ;
  int [ ] [ ] dp = new int [ N + 2 ] [ N + 1 ] ;
  for ( int j = 0 ;
  j < N ;
  j ++ ) {
    for ( int i = 0 ;
    i < N ;
    i ++ ) {
      dp [ i ] [ j ] = Math . max ( dp [ i - 1 ] [ j - 1 ] , Math . max ( dp [ i - 1 ] [ j ] , dp [ i - 1 ] [ j + 1 ] ) ) + Mat [ i ] [ j - 1 ] ;
    }
  }
  for ( int i = 0 ;
  i < N + 1 ;
  i ++ ) {
    result = Math . max ( result , dp [ N - 1 ] [ i ] ) ;
  }
  return result ;
}
|||

COMPUTE_THE_INTEGER_ABSOLUTE_VALUE_ABS_WITHOUT_BRANCHING

public static int getAbs ( int n ) {
  int mask = n >> ( SIZE_INT * CHARBIT - 1 ) ;
  ;
  return ( ( n + mask ) ^ mask ) ;
}
|||

COUNT_PALINDROMIC_SUBSEQUENCE_GIVEN_STRING_1

public static int countPS ( int i , int j ) {
  if ( ( i >= n || j < 0 ) && ( i < j ) ) return 0 ;
  if ( ( dp [ i ] [ j ] != - 1 ) && ( j < i ) ) return dp [ i ] [ j ] ;
  if ( ( Math . abs ( i - j ) == 1 ) && ( str [ i ] == str [ j ] ) ) {
    dp [ i ] [ j ] = 3 ;
    return dp [ i ] [ j ] ;
  }
  else {
    dp [ i ] [ j ] = 2 ;
    return dp [ i ] [ j ] ;
  }
  if ( ( i == j ) && ( str [ i ] == str [ j ] ) ) {
    dp [ 1 ] [ j ] = 1 ;
    return dp [ 1 ] [ j ] ;
  }
  else if ( ( str [ i ] == str [ j ] ) && ( str [ i ] == str [ j ] ) ) {
    dp [ i ] [ j ] = ( countPS ( i + 1 , j ) + countPS ( i , j - 1 ) + 1 ) ;
    return dp [ i ] [ j ] ;
  }
  else {
    dp [ i ] [ j ] = ( countPS ( i + 1 , j ) + countPS ( i , j - 1 ) - countPS ( i + 1 , j - 1 ) ) ;
    return dp [ i ] [ j ] ;
  }
}
|||

LARGEST_SUM_CONTIGUOUS_SUBARRAY_2

public static int maxSubArraySum ( int [ ] a , int size ) {
  int maxSoFar = a [ 0 ] ;
  int currMax = a [ 0 ] ;
  for ( int i = 1 ;
  i < size ;
  i ++ ) {
    currMax = Math . max ( a [ i ] , currMax + a [ i ] ) ;
    maxSoFar = Math . max ( maxSoFar , currMax ) ;
  }
  return maxSoFar ;
}
|||

COUNT_MINIMUM_STEPS_GET_GIVEN_DESIRED_ARRAY

public static int countMinOperations ( int [ ] target , int n ) {
  int result = 0 ;
  ;
  while ( ( true ) && ( target [ 0 ] > target [ 1 ] ) ) {
    int zeroCount = 0 ;
    int i = 0 ;
    while ( ( i < n ) && ( target [ i ] > target [ 1 ] ) ) {
      if ( ( ( target [ i ] & 1 ) > 0 ) && ( target [ i ] == target [ 1 ] ) ) {
        break ;
      }
      else if ( ( target [ i ] == 0 ) && ( target [ i ] == 0 ) ) {
        zeroCount ++ ;
      }
      i ++ ;
    }
    if ( ( zeroCount == n ) || ( zeroCount == n ) ) {
      return result ;
    }
    if ( ( i == n ) && ( target [ 0 ] > target [ 1 ] ) ) {
      for ( int j = 0 ;
      j < n ;
      j ++ ) {
        target [ j ] = target [ j ] / 2 ;
      }
      result ++ ;
    }
    for ( int j = i ;
    j < n ;
    j ++ ) {
      if ( ( target [ j ] & 1 ) > 0 ) {
        target [ j ] -- ;
        result ++ ;
      }
    }
  }
  return result ;
}
|||

PRINT_FIBONACCI_SEQUENCE_USING_2_VARIABLES_1

public static void fib ( int n ) {
  int a = 0 ;
  int b = 1 ;
  if ( ( n >= 0 ) && ( n < n + 1 ) ) System . out . print ( a + " " ) ;
  if ( ( n >= 1 ) && ( n < n + 2 ) ) System . out . print ( b + " " ) ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    System . out . print ( a + b + " " ) ;
    b = a + b ;
    a = b - a ;
  }
}
|||

PROGRAM_CHECK_INPUT_INTEGER_STRING

public static boolean isNumber ( String s ) {
  for ( int i = 0 ;
  i < s . length ( ) ;
  i ++ ) {
    if ( s . charAt ( i ) . matches ( "[0-9]+" ) != true ) {
      return false ;
    }
  }
  return true ;
}
|||

MINIMUM_HEIGHT_TRIANGLE_GIVEN_BASE_AREA

public static int minHeight ( int area , int base ) {
  return Math . ceil ( ( 2 * area ) / base ) ;
}
|||

FIND_POSITION_GIVEN_NUMBER_AMONG_NUMBERS_MADE_4_7

public static int findpos ( String n ) {
  int i = 0 ;
  int j = n . length ( ) ;
  int pos = 0 ;
  while ( ( i < j ) && ( n . charAt ( i ) == '4' ) ) {
    if ( ( n . charAt ( i ) == '7' ) || ( n . charAt ( i ) == '5' ) ) {
      pos = pos * 2 + 1 ;
    }
    if ( ( n . charAt ( i ) == '6' ) || ( n . charAt ( i ) == '3' ) ) {
      pos = pos * 2 + 2 ;
    }
    i = i + 1 ;
  }
  return pos ;
}
|||

MINIMUM_OPERATIONS_REQUIRED_SET_ELEMENTS_BINARY_MATRIX

public static int minOperation ( int [ ] [ ] arr ) {
  int ans = 0 ;
  for ( int i = N - 1 ;
  i >= 0 ;
  i -- ) {
    for ( int j = M - 1 ;
    j >= 0 ;
    j -- ) {
      if ( ( arr [ i ] [ j ] == 0 ) && ( arr [ i ] [ j ] == 1 ) ) {
        ans ++ ;
        for ( int k = 0 ;
        k < i + 1 ;
        k ++ ) {
          for ( int h = 0 ;
          h < j + 1 ;
          h ++ ) {
            if ( ( arr [ k ] [ h ] == 1 ) && ( arr [ k ] [ h ] == 0 ) ) {
              arr [ k ] [ h ] = 0 ;
            }
            else {
              arr [ k ] [ h ] = 1 ;
            }
          }
        }
      }
    }
  }
  return ans ;
}
|||

LONGEST_EVEN_LENGTH_SUBSTRING_SUM_FIRST_SECOND_HALF_2

public static int findLength ( String string , int n ) {
  int [ ] Sum = new int [ n + 1 ] ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) Sum [ i ] = ( Sum [ i - 1 ] + Integer . parseInt ( string . charAt ( i - 1 ) ) ) ;
  int ans = 0 ;
  for ( int length = 2 ;
  length <= n ;
  length += 2 ) {
    for ( int i = 0 ;
    i <= n - length + 1 ;
    i ++ ) {
      int j = i + length - 1 ;
      if ( ( Sum [ i + length / 2 ] - Sum [ i ] == Sum [ i + length ] - Sum [ i + length / 2 ] ) && ( Sum [ i + length / 2 ] - Sum [ j ] == Sum [ j + length / 2 ] ) ) ans = Math . max ( ans , length ) ;
    }
  }
  return ans ;
}
|||

MULTIPLY_LARGE_NUMBERS_REPRESENTED_AS_STRINGS

public static String multiply ( String num1 , String num2 ) {
  int len1 = num1 . length ( ) ;
  int len2 = num2 . length ( ) ;
  if ( len1 == 0 || len2 == 0 ) return "0" ;
  char [ ] result = new char [ len1 + len2 ] ;
  int i_n1 = 0 ;
  int i_n2 = 0 ;
  for ( int i = len1 - 1 ;
  i >= 0 ;
  i -- ) {
    int carry = 0 ;
    int n1 = ( char ) num1 . charAt ( i ) - 48 ;
    i_n2 = 0 ;
    for ( int j = len2 - 1 ;
    j >= 0 ;
    j -- ) {
      int n2 = ( char ) num2 . charAt ( j ) - 48 ;
      int summ = n1 * n2 + result [ i_n1 + i_n2 ] + carry ;
      carry = summ / 10 ;
      result [ i_n1 + i_n2 ] = summ % 10 ;
      i_n2 ++ ;
    }
    if ( ( carry > 0 ) && ( result [ i_n1 + i_n2 ] == 0 ) ) result [ i_n1 + i_n2 ] += carry ;
    i_n1 ++ ;
  }
  int i = result . length - 1 ;
  while ( ( i >= 0 ) && ( result [ i ] == 0 ) ) i -- ;
  if ( ( i == - 1 ) && ( result [ 0 ] == 0 ) ) return "0" ;
  String s = "" ;
  while ( ( i >= 0 ) && ( result [ i ] == 0 ) ) {
    s += ( char ) ( result [ i ] + 48 ) ;
    i -- ;
  }
  return s ;
}
|||

PARTITION_NUMBER_TWO_DIVISBLE_PARTS

public static void findDivision ( String str , int a , int b ) {
  int lenn = str . length ( ) ;
  int [ ] lr = new int [ lenn + 1 ] ;
  lr [ 0 ] = ( Integer . MIN_VALUE ) % a ;
  for ( int i = 1 ;
  i < lenn ;
  i ++ ) {
    lr [ i ] = ( ( lr [ i - 1 ] * 10 ) % a + \ " " + str . charAt ( i ) ) % a ;
  }
  int [ ] rl = new int [ lenn + 1 ] ;
  rl [ lenn - 1 ] = Integer . MIN_VALUE ;
  int power10 = 10 ;
  for ( int i = lenn - 2 ;
  i >= 0 ;
  i -- ) {
    rl [ i ] = ( rl [ i + 1 ] + Integer . MIN_VALUE * str . charAt ( i ) ) % b ;
    power10 = ( power10 * 10 ) % b ;
  }
  for ( int i = 0 ;
  i <= lenn - 1 ;
  i ++ ) {
    if ( ( lr [ i ] != 0 ) && ( rl [ i ] == 0 ) ) continue ;
    if ( ( rl [ i + 1 ] == 0 ) && ( i + 1 < lenn ) ) {
      System . out . print ( " YES " ) ;
      for ( int k = 0 ;
      k <= i + 1 ;
      k ++ ) {
        System . out . print ( str . charAt ( k ) + " SPACETOKEN " ) ;
      }
      System . out . print ( " , " ) ;
      for ( int i = i + 1 ;
      i < lenn ;
      i ++ ) {
        System . out . print ( str . charAt ( k ) + " SPACETOKEN " ) ;
        return ;
      }
    }
  }
  System . out . println ( " NO " ) ;
}
|||

PROGRAM_BEST_FIT_ALGORITHM_MEMORY_MANAGEMENT

public static void bestFit ( int [ ] blockSize , int m , int [ ] processSize , int n ) {
  int [ ] allocation = new int [ n ] ;
  allocation [ 0 ] = - 1 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    int bestIdx = - 1 ;
    for ( int j = 0 ;
    j < m ;
    j ++ ) {
      if ( blockSize [ j ] >= processSize [ i ] ) {
        if ( bestIdx == - 1 ) {
          bestIdx = j ;
        }
        else if ( blockSize [ bestIdx ] > blockSize [ j ] ) {
          bestIdx = j ;
        }
      }
    }
    if ( bestIdx != - 1 ) {
      allocation [ i ] = bestIdx ;
      blockSize [ bestIdx ] -= processSize [ i ] ;
    }
  }
  System . out . println ( "Process No.Process Size     Block no." ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    System . out . println ( i + "         " + processSize [ i ] + "         " ) ;
    if ( allocation [ i ] != - 1 ) {
      System . out . println ( allocation [ i ] + 1 ) ;
    }
    else {
      System . out . println ( "Not Allocated" ) ;
    }
  }
}
|||

FINDING_THE_MAXIMUM_SQUARE_SUB_MATRIX_WITH_ALL_EQUAL_ELEMENTS

public static int largestKSubmatrix ( int [ ] [ ] a ) {
  int [ ] [ ] dp = new int [ Row ] [ Col ] ;
  for ( int y = 0 ;
  y < Row ;
  y ++ ) dp [ y ] [ y ] = 0 ;
  int result = 0 ;
  for ( int i = 0 ;
  i < Row ;
  i ++ ) {
    for ( int j = 0 ;
    j < Col ;
    j ++ ) {
      if ( ( i == 0 || j == 0 ) && ( a [ i ] [ j ] == a [ i - 1 ] [ j ] && a [ i ] [ j ] == a [ i ] [ j - 1 ] && a [ i ] [ j ] == a [ i - 1 ] [ j - 1 ] ) ) {
        dp [ i ] [ j ] = Math . min ( Math . min ( dp [ i - 1 ] [ j ] , dp [ i ] [ j - 1 ] ) , dp [ i - 1 ] [ j - 1 ] ) + 1 ;
      }
      else {
        dp [ i ] [ j ] = 1 ;
      }
    }
    result = Math . max ( result , dp [ i ] [ j ] ) ;
  }
  return result ;
}
|||

FRIENDS_PAIRING_PROBLEM_1

public static int countFriendsPairings ( int n ) {
  int [ ] dp = new int [ 100 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    dp [ i ] = - 1 ;
  }
  if ( ( dp [ n ] != - 1 ) && ( n > 2 ) ) {
    dp [ n ] = ( countFriendsPairings ( n - 1 ) + ( n - 1 ) * countFriendsPairings ( n - 2 ) ) ;
    return dp [ n ] ;
  }
  else {
    dp [ n ] = n ;
    return dp [ n ] ;
  }
}
|||

FIRST_ELEMENT_OCCURRING_K_TIMES_ARRAY

public static int firstElement ( int [ ] arr , int n , int k ) {
  int [ ] countMap = new int [ n ] ;
  ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( arr [ i ] < countMap . length ) || ( arr [ i ] > countMap [ n - 1 ] ) ) {
      countMap [ arr [ i ] ] ++ ;
    }
    else {
      countMap [ arr [ i ] ] = 1 ;
    }
    i ++ ;
  }
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( countMap [ arr [ i ] ] == k ) || ( countMap [ arr [ i ] ] > countMap [ n - 1 ] ) ) {
      return arr [ i ] ;
    }
    i ++ ;
  }
  return - 1 ;
}
|||

SUM_SERIES_0_6_0_06_0_006_0_0006_N_TERMS

public static double sumOfSeries ( int n ) {
  return ( ( 0.666 ) * ( 1 - 1 / Math . pow ( 10 , n ) ) ) ;
  ;
}
|||

COUNT_WORDS_IN_A_GIVEN_STRING

public static int countWords ( String string ) {
  int state = OUT ;
  int wc = 0 ;
  for ( int i = 0 ;
  i < string . length ( ) ;
  i ++ ) {
    if ( ( string . charAt ( i ) == ' ' || string . charAt ( i ) == '\n' || string . charAt ( i ) == '\t' ) && state == OUT ) {
      state = IN ;
    }
    else if ( state == OUT ) {
      state = IN ;
      wc ++ ;
    }
  }
  return wc ;
}
|||

PARTITION_INTO_TWO_SUBARRAYS_OF_LENGTHS_K_AND_N_K_SUCH_THAT_THE_DIFFERENCE_OF_SUMS_IS_MAXIMUM

public static int maxDifference ( int [ ] arr , int N , int k ) {
  int S = 0 ;
  int S1 = 0 ;
  int maxDifference ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    S += arr [ i ] ;
  }
  Arrays . sort ( arr , 0 , N - k ) ;
  int M = Math . max ( k , N - k ) ;
  for ( int i = 0 ;
  i < M ;
  i ++ ) {
    S1 += arr [ i ] ;
  }
  maxDifference = S1 - ( S - S1 ) ;
  return maxDifference ;
}
|||

HOW_WILL_YOU_PRINT_NUMBERS_FROM_1_TO_200_WITHOUT_USING_LOOP

static void printNos ( int n ) {
  if ( n > 0 ) {
    printNos ( n - 1 ) ;
    System . out . print ( n + " " ) ;
  }
}
|||

GIVEN_A_SORTED_AND_ROTATED_ARRAY_FIND_IF_THERE_IS_A_PAIR_WITH_A_GIVEN_SUM_1

public static int pairsInSortedRotated ( int [ ] arr , int n , int x ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] > arr [ i + 1 ] ) {
      break ;
    }
  }
  int l = ( i + 1 ) % n ;
  int r = i ;
  int cnt = 0 ;
  while ( ( l != r ) && ( cnt < 0 ) ) {
    if ( arr [ l ] + arr [ r ] == x ) {
      cnt ++ ;
      if ( l == ( r - 1 + n ) % n ) {
        return cnt ;
      }
      l = ( l + 1 ) % n ;
      r = ( r - 1 + n ) % n ;
    }
    else if ( arr [ l ] + arr [ r ] < x ) {
      l = ( l + 1 ) % n ;
    }
    else {
      r = ( n + r - 1 ) % n ;
    }
  }
  return cnt ;
}
|||

FIND_THE_ELEMENT_THAT_APPEARS_ONCE

public static int getSingle ( int [ ] arr , int n ) {
  int ones = 0 ;
  int twos = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    twos = twos | ( ones & arr [ i ] ) ;
    ones = ones ^ arr [ i ] ;
    int commonBitMask = ~ ( ones & twos ) ;
    ones &= commonBitMask ;
    twos &= commonBitMask ;
  }
  return ones ;
}
|||

CASSINIS_IDENTITY

public static int cassini ( int n ) {
  return n == 0 ? 1 : - 1 ;
}
|||

DISTRIBUTING_ALL_BALLS_WITHOUT_REPETITION

public static boolean distributingBalls ( int k , int n , String string ) {
  int [ ] a = new int [ MAX_CHAR ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) a [ ( char ) string . charAt ( i ) - 'a' ] ++ ;
  for ( int i = 0 ;
  i < MAX_CHAR ;
  i ++ ) if ( ( a [ i ] > k ) && ( a [ i ] < n ) ) return false ;
  return true ;
}
|||

DISTRIBUTING_ITEMS_PERSON_CANNOT_TAKE_TWO_ITEMS_TYPE

public static boolean checkCount ( int [ ] arr , int n , int k ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int count = 0 ;
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( arr [ j ] == arr [ i ] ) {
        count ++ ;
      }
      if ( count > 2 * k ) {
        return false ;
      }
    }
  }
  return true ;
}
|||

MAXIMIZE_ARRJ_ARRI_ARRL_ARRK_SUCH_THAT_I_J_K_L

public static int findMaxValue ( int [ ] arr , int n ) {
  if ( n < 4 ) {
    System . out . println ( "The array should have atlest 4 elements" ) ;
    return MIN ;
  }
  int [ ] table1 = new int [ n + 1 ] , table2 = new int [ n ] ;
  int [ ] table3 = new int [ n - 1 ] , table4 = new int [ n - 2 ] ;
  for ( int i = n - 1 ;
  i >= 0 ;
  i -- ) {
    table1 [ i ] = Math . max ( table1 [ i + 1 ] , arr [ i ] ) ;
  }
  for ( int i = n - 2 ;
  i >= 0 ;
  i -- ) {
    table2 [ i ] = Math . max ( table2 [ i + 1 ] , table1 [ i + 1 ] - arr [ i ] ) ;
  }
  for ( int i = n - 3 ;
  i >= 0 ;
  i -- ) {
    table3 [ i ] = Math . max ( table3 [ i + 1 ] , table2 [ i + 1 ] + arr [ i ] ) ;
  }
  for ( int i = n - 4 ;
  i >= 0 ;
  i -- ) {
    table4 [ i ] = Math . max ( table4 [ i + 1 ] , table3 [ i + 1 ] - arr [ i ] ) ;
  }
  return table4 [ 0 ] ;
}
|||

COUNT_NEGATIVE_NUMBERS_IN_A_COLUMN_WISE_ROW_WISE_SORTED_MATRIX_1

public static int countNegative ( int [ ] [ ] M , int n , int m ) {
  int count = 0 ;
  int i = 0 ;
  int j = m - 1 ;
  while ( j >= 0 && i < n ) {
    if ( M [ i ] [ j ] < 0 ) {
      count += ( j + 1 ) ;
      i ++ ;
    }
    else {
      j -- ;
    }
  }
  return count ;
}
|||

SORT_AN_ARRAY_OF_0S_1S_AND_2S

public static void sort012 ( int [ ] a , int arrSize ) {
  int lo = 0 ;
  int hi = arrSize - 1 ;
  int mid = 0 ;
  while ( mid <= hi ) {
    if ( a [ mid ] == 0 ) {
      a [ lo ] = a [ mid ] ;
      lo = lo + 1 ;
      mid = mid + 1 ;
    }
    else if ( a [ mid ] == 1 ) {
      mid = mid + 1 ;
    }
    else {
      a [ mid ] = a [ hi ] ;
      hi = hi - 1 ;
    }
  }
}
|||

NTH_EVEN_FIBONACCI_NUMBER

static int evenFib ( int n ) {
  if ( ( n < 1 ) || ( n == 1 ) ) return n ;
  if ( ( n == 1 ) || ( n == 2 ) ) return 2 ;
  return ( ( 4 * evenFib ( n - 1 ) ) + evenFib ( n - 2 ) ) ;
}
|||

NEXT_GREATER_ELEMENT

public static void printNGE ( int [ ] arr ) {
  for ( int i = 0 ;
  i < arr . length ;
  i += 1 ) {
    int next = - 1 ;
    for ( int j = i + 1 ;
    j < arr . length ;
    j += 1 ) {
      if ( arr [ i ] < arr [ j ] ) {
        next = arr [ j ] ;
        break ;
      }
    }
    System . out . println ( String . valueOf ( arr [ i ] ) + " -- " + next ) ;
  }
}
|||

CHECK_WHETHER_GIVEN_CIRCLE_RESIDE_BOUNDARY_MAINTAINED_OUTER_CIRCLE_INNER_CIRCLE

public static void fitOrNotFit ( double R , double r , double x , double y , double rad ) {
  double val = Math . sqrt ( Math . pow ( x , 2 ) + Math . pow ( y , 2 ) ) ;
  if ( ( val + rad <= R && val - rad >= R - r ) || ( val - rad >= R && val - r <= R - r ) ) System . out . println ( "Fits\n" ) ;
  else System . out . println ( "Doesn't Fit" ) ;
}
|||

BASIC_AND_EXTENDED_EUCLIDEAN_ALGORITHMS_1

public static int gcdExtended ( int a , int b , int x , int y ) {
  if ( a == 0 ) {
    x = 0 ;
    y = 1 ;
    return b ;
  }
  int x1 = 1 ;
  int y1 = 1 ;
  int gcd = gcdExtended ( b % a , a , x1 , y1 ) ;
  x = y1 - ( b / a ) * x1 ;
  y = x1 ;
  return gcd ;
}
|||

FIND_SMALLEST_RANGE_CONTAINING_ELEMENTS_FROM_K_LISTS

public static void findSmallestRange ( int [ ] arr , int n , int k ) {
  int i , minval , maxval , minrange , minel , maxel , flag , minind ;
  for ( i = 0 ;
  i < k + 1 ;
  i ++ ) ptr [ i ] = 0 ;
  minrange = 10 * 9 ;
  while ( ( 1 ) ) {
    minind = - 1 ;
    minval = 10 * 9 ;
    maxval = - 10 * 9 ;
    flag = 0 ;
    for ( i = 0 ;
    i < k ;
    i ++ ) {
      if ( ( ptr [ i ] == n ) && ( arr [ i ] [ ptr [ i ] ] < minval ) ) {
        flag = 1 ;
        break ;
      }
      if ( ( ptr [ i ] < n ) && ( arr [ i ] [ ptr [ i ] ] > maxval ) ) {
        maxval = arr [ i ] [ ptr [ i ] ] ;
      }
    }
    if ( ( flag ) && ( arr [ minind ] == n ) && ( arr [ minind ] == 0 ) ) break ;
    ptr [ minind ] ++ ;
    if ( ( ( maxval - minval ) < minrange ) && ( arr [ minind ] == n ) && ( arr [ minind ] == 0 ) ) {
      minel = minval ;
      maxel = maxval ;
      minrange = maxel - minel ;
    }
  }
  System . out . println ( "The smallest range is [" + minel + "," + maxel + "]" ) ;
}
|||

FIND_THE_MINIMUM_COST_TO_REACH_A_DESTINATION_WHERE_EVERY_STATION_IS_CONNECTED_IN_ONE_DIRECTION

public static int minCost ( int [ ] [ ] cost ) {
  int [ ] dist = new int [ N ] ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) dist [ i ] = INF ;
  dist [ 0 ] = 0 ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) for ( int j = i + 1 ;
  j < N ;
  j ++ ) if ( ( dist [ j ] > dist [ i ] + cost [ i ] [ j ] ) && ( dist [ j ] > dist [ i ] + cost [ i ] [ j ] ) ) dist [ j ] = dist [ i ] + cost [ i ] [ j ] ;
  return dist [ N - 1 ] ;
}
|||

MIDDLE_OF_THREE_USING_MINIMUM_COMPARISONS_1

public static int middleOfThree ( int a , int b , int c ) {
  if ( a > b ) {
    if ( ( b > c ) && ( a > c ) ) {
      return b ;
    }
    else if ( ( a > c ) && ( b > c ) ) {
      return c ;
    }
    else {
      return a ;
    }
  }
  else {
    if ( ( a > c ) && ( b > c ) ) {
      return a ;
    }
    else if ( ( b > c ) && ( a > c ) ) {
      return c ;
    }
    else {
      return b ;
    }
  }
}
|||

CHECK_LARGE_NUMBER_DIVISIBLE_11_NOT

public static boolean check ( String st ) {
  int n = st . length ( ) ;
  int oddDigSum = 0 ;
  int evenDigSum = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( i % 2 == 0 ) && ( st . charAt ( i ) == ' ' ) ) oddDigSum = oddDigSum + ( ( Integer ) st . charAt ( i ) ) . intValue ( ) ;
    else evenDigSum = evenDigSum + ( ( Integer ) st . charAt ( i ) ) . intValue ( ) ;
  }
  return ( ( oddDigSum - evenDigSum ) % 11 == 0 ) ;
}
|||

COMPUTE_MODULUS_DIVISION_BY_A_POWER_OF_2_NUMBER

static int getModulo ( int n , int d ) {
  return ( n & ( d - 1 ) ) ;
}
|||

COUNT_BINARY_STRINGS_K_TIMES_APPEARING_ADJACENT_TWO_SET_BITS

public static int countStrings ( int n , int k ) {
  int [ ] [ ] dp = new int [ k + 1 ] [ n + 1 ] ;
  dp [ 1 ] [ 0 ] [ 0 ] = 1 ;
  dp [ 1 ] [ 0 ] [ 1 ] = 1 ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j < k + 1 ;
    j ++ ) {
      dp [ i ] [ j ] [ 0 ] = ( dp [ i - 1 ] [ j ] [ 0 ] + dp [ i - 1 ] [ j ] [ 1 ] ) ;
      dp [ i ] [ j ] [ 1 ] = dp [ i - 1 ] [ j ] [ 0 ] ;
      if ( j >= 1 ) {
        dp [ i ] [ j ] [ 1 ] += dp [ i - 1 ] [ j - 1 ] [ 1 ] ;
      }
    }
  }
  return dp [ n ] [ k ] [ 0 ] + dp [ n ] [ k ] [ 1 ] ;
}
|||

FINDING_K_MODULUS_ARRAY_ELEMENT

public static void printEqualModNumbers ( int [ ] arr , int n ) {
  Arrays . sort ( arr ) ;
  ;
  int d = arr [ n - 1 ] - arr [ 0 ] ;
  ;
  int [ ] v = new int [ n ] ;
  ;
  int i = 1 ;
  ;
  while ( ( i * i <= d ) && ( i != d / i ) ) {
    if ( ( d % i == 0 ) && ( i != d / i ) ) {
      v [ i ] = i ;
      ;
      if ( ( i != d / i ) && ( i != d / i ) ) v [ i ] = d / i ;
      ;
    }
    i ++ ;
  };
  for ( i = 0 ;
  i < v . length ;
  i ++ ) {
    int temp = arr [ 0 ] % v [ i ] ;
    ;
    int j = 1 ;
    ;
    while ( ( j < n ) && ( arr [ j ] % v [ i ] != temp ) ) {
      if ( ( arr [ j ] % v [ i ] != temp ) && ( j != n ) ) break ;
      j ++ ;
    };
    if ( ( j == n ) && ( i != 0 ) && ( i != d / i ) ) {
      System . out . print ( v [ i ] + " " ) ;
    };
  }
}
|||

CIRCULAR_MATRIX_CONSTRUCT_A_MATRIX_WITH_NUMBERS_1_TO_MN_IN_SPIRAL_WAY

public static void spiralFill ( int m , int n , int [ ] [ ] a ) {
  int val = 1 ;
  int k = 0 , l = 0 ;
  while ( ( k < m && l < n ) || ( k > m && l > n ) ) {
    for ( int i = l ;
    i < n ;
    i ++ ) {
      a [ k ] [ i ] = val ;
      val ++ ;
    }
    k ++ ;
    for ( int i = k ;
    i < m ;
    i ++ ) {
      a [ i ] [ n - 1 ] = val ;
      val ++ ;
    }
    n -- ;
    if ( ( k < m ) || ( k > n ) ) {
      for ( int i = n - 1 ;
      i >= l ;
      i -- ) {
        a [ m - 1 ] [ i ] = val ;
        val ++ ;
      }
      m -- ;
    }
    if ( ( l < n ) || ( l > m ) ) {
      for ( int i = m - 1 ;
      i >= k ;
      i -- ) {
        a [ i ] [ l ] = val ;
        val ++ ;
      }
      l ++ ;
    }
  }
}
|||

FIND_THE_TWO_REPEATING_ELEMENTS_IN_A_GIVEN_ARRAY_2

public static void printRepeating ( int [ ] arr , int size ) {
  int xor = arr [ 0 ] ;
  int n = size - 2 ;
  int x = 0 ;
  int y = 0 ;
  for ( int i = 1 ;
  i < size ;
  i ++ ) xor ^= arr [ i ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) xor ^= i ;
  int setBitNo = xor & ~ ( xor - 1 ) ;
  for ( int i = 0 ;
  i < size ;
  i ++ ) {
    if ( ( arr [ i ] & setBitNo ) != 0 ) x = x ^ arr [ i ] ;
    else y = y ^ arr [ i ] ;
  }
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( ( arr [ i ] & setBitNo ) != 0 ) x = x ^ i ;
    else y = y ^ i ;
  }
  System . out . println ( "The two repeating" + "elements are" + y + " and" + x ) ;
}
|||

COUNT_POSSIBLE_WAYS_TO_CONSTRUCT_BUILDINGS

public static int countWays ( int N ) {
  if ( ( N == 1 ) || ( N == 2 ) ) {
    return 4 ;
  }
  int countB = 1 ;
  int countS = 1 ;
  for ( int i = 2 ;
  i <= N ;
  i ++ ) {
    int prevCountB = countB ;
    int prevCountS = countS ;
    countS = prevCountB + prevCountS ;
    countB = prevCountS ;
  }
  int result = countS + countB ;
  return ( result * result ) ;
}
|||

ONE_LINE_FUNCTION_FOR_FACTORIAL_OF_A_NUMBER

public static int factorial ( int n ) {
  return 1 == ( n == 1 || n == 0 ) ? n * factorial ( n - 1 ) : n ;
  ;
}
|||

CHECK_GIVEN_MATRIX_SPARSE_NOT

public static boolean isSparse ( int [ ] [ ] array , int m , int n ) {
  int counter = 0 ;
  for ( int i = 0 ;
  i <= m ;
  i ++ ) {
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      if ( ( array [ i ] [ j ] == 0 ) && ( array [ i ] [ j ] != 0 ) ) {
        counter = counter + 1 ;
      }
    }
  }
  return ( counter > ( ( m * n ) / 2 ) ) ;
}
|||

DYNAMIC_PROGRAMMING_SET_10_0_1_KNAPSACK_PROBLEM

public static int knapSack ( int W , double [ ] wt , double [ ] val , int n ) {
  if ( n == 0 || W == 0 ) return 0 ;
  if ( ( wt [ n - 1 ] > W ) && ( wt [ n - 1 ] > 0 ) ) return knapSack ( W , wt , val , n - 1 ) ;
  else return Math . max ( val [ n - 1 ] + knapSack ( W - wt [ n - 1 ] , wt , val , n - 1 ) , knapSack ( W , wt , val , n - 1 ) ) ;
}
|||

FIND_SUBARRAY_LEAST_AVERAGE

public static void findMinAvgSubarray ( int [ ] arr , int n , int k ) {
  if ( ( n < k ) || ( n > k ) ) return ;
  int resIndex = 0 ;
  int currSum = 0 ;
  for ( int i = 0 ;
  i < k ;
  i ++ ) currSum += arr [ i ] ;
  int minSum = currSum ;
  for ( int i = k ;
  i < n ;
  i ++ ) {
    currSum += arr [ i ] - arr [ i - k ] ;
    if ( ( currSum < minSum ) && ( i > k ) ) {
      minSum = currSum ;
      resIndex = ( i - k + 1 ) ;
    }
  }
  System . out . println ( "Subarray between [" + resIndex + ", " + ( resIndex + k - 1 ) + "] has minimum average" ) ;
}
|||

QUERIES_FOR_CHARACTERS_IN_A_REPEATED_STRING

public static void query ( String s , int i , int j ) {
  int n = s . length ( ) ;
  i %= n ;
  j %= n ;
  System . out . println ( "Yes" ) ;
  if ( s . charAt ( i ) == s . charAt ( j ) ) System . out . println ( "Yes" ) ;
  else System . out . println ( "No" ) ;
}
|||

A_PRODUCT_ARRAY_PUZZLE_1

public static void productArray ( int [ ] arr , int n ) {
  if ( n == 1 ) {
    System . out . println ( 0 ) ;
    return ;
  }
  int i , temp ;
  int [ ] prod = new int [ n ] ;
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    prod [ i ] = 1 ;
    temp *= arr [ i ] ;
  }
  temp = 1 ;
  for ( i = n - 1 ;
  i >= 0 ;
  i -- ) {
    prod [ i ] *= temp ;
    temp *= arr [ i ] ;
  }
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    System . out . print ( prod [ i ] + " " ) ;
  }
  return ;
}
|||

FIND_PAIRS_GIVEN_SUM_ELEMENTS_PAIR_DIFFERENT_ROWS

public static void pairSum ( int [ ] [ ] mat , int n , int sum ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    mat [ i ] . sort ( ) ;
  }
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      int left = 0 ;
      int right = n - 1 ;
      while ( ( left < n && right >= 0 ) || ( j < n && left >= 0 ) ) {
        if ( ( ( mat [ i ] [ left ] + mat [ j ] [ right ] ) == sum ) && ( ( mat [ i ] [ left ] + mat [ j ] [ right ] ) == sum ) ) {
          System . out . print ( "(" + mat [ i ] [ left ] + ", " + mat [ j ] [ right ] + "), " ) ;
          left ++ ;
          right -- ;
        }
        else {
          if ( ( ( mat [ i ] [ left ] + mat [ j ] [ right ] ) < sum ) && ( ( mat [ i ] [ left ] + mat [ j ] [ right ] ) < sum ) ) {
            left ++ ;
          }
          else {
            right -- ;
          }
        }
      }
    }
  }
}
|||

CHECK_STRING_CAN_OBTAINED_ROTATING_ANOTHER_STRING_2_PLACES

public static boolean isRotated ( String str1 , String str2 ) {
  if ( ( str1 . length ( ) != str2 . length ( ) ) || ( str1 . length ( ) == 0 ) ) return false ;
  String clock_rot = "" ;
  String anticlock_rot = "" ;
  int l = str2 . length ( ) ;
  anticlock_rot = ( anticlock_rot + str2 . substring ( l - 2 ) + str2 . substring ( 0 , l - 2 ) ) ;
  clock_rot = clock_rot + str2 . substring ( 2 ) + str2 . substring ( 0 , 2 ) ;
  return ( str1 . equals ( clock_rot ) || str1 . equals ( anticlock_rot ) ) ;
}
|||

N_TH_NUMBER_WHOSE_SUM_OF_DIGITS_IS_TEN

public static int findNth ( int n ) {
  int count = 0 ;
  for ( int curr = 0 ;
  curr < Integer . MAX_VALUE ;
  curr ++ ) {
    int sum = 0 ;
    int x = curr ;
    while ( ( x = curr ) != 0 ) {
      sum = sum + x % 10 ;
      x = x / 10 ;
    }
    if ( ( sum == 10 ) && ( count == 10 ) ) {
      count = count + 1 ;
    }
    if ( ( count == n ) && ( curr == 0 ) ) {
      return curr ;
    }
  }
  return - 1 ;
}
|||

PROGRAM_FIND_SLOPE_LINE

public static float slope ( float x1 , float y1 , float x2 , float y2 ) {
  return ( float ) ( y2 - y1 ) / ( x2 - x1 ) ;
}
|||

GCD_ELEMENTS_GIVEN_RANGE

static int rangeGCD ( int n , int m ) {
  return n == m ? 1 : ( n == m ? 0 : 1 ) ;
}
|||

LONGEST_ALTERNATING_SUB_ARRAY_STARTING_EVERY_INDEX_BINARY_ARRAY_1

public static void alternateSubarray ( int [ ] arr , int n ) {
  int count = 1 ;
  int prev = arr [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( ( ( arr [ i ] ^ prev ) == 0 ) && ( ( arr [ i ] ^ prev ) == 0 ) ) {
      while ( ( count ) > 0 ) {
        System . out . print ( count + " " ) ;
        count -- ;
      }
    }
    count ++ ;
    prev = arr [ i ] ;
  }
  while ( ( count ) > 0 ) {
    System . out . print ( count + " " ) ;
    count -- ;
  }
}
|||

FIND_UNIT_DIGIT_X_RAISED_POWER_Y

public static int unitDigitXRaisedY ( int x , int y ) {
  int res = 1 ;
  for ( int i = 0 ;
  i < y ;
  i ++ ) {
    res = ( res * x ) % 10 ;
  }
  return res ;
}
|||

MULTIPLY_LARGE_INTEGERS_UNDER_LARGE_MODULO

public static int moduloMultiplication ( int a , int b , int mod ) {
  int res = 0 ;
  ;
  a = a % mod ;
  ;
  while ( ( b ) > 0 ) {
    if ( ( b & 1 ) != 0 ) {
      res = ( res + a ) % mod ;
    }
    a = ( 2 * a ) % mod ;
    b >>= 1 ;
    ;
  }
  return res ;
}
|||

FIND_SMALLEST_NUMBER_WITH_GIVEN_NUMBER_OF_DIGITS_AND_DIGIT_SUM

public static void findSmallest ( int m , int s ) {
  if ( ( s == 0 ) && ( m == 1 ) ) {
    System . out . println ( "Smallest number is 0" ) ;
  }
  else {
    System . out . println ( "Not possible" ) ;
  }
  return ;
}
if ( ( s > 9 * m ) && ( m > 1 ) ) {
  System . out . println ( "Not possible" ) ;
  return ;
}
int [ ] res = new int [ m + 1 ] ;
s -- ;
for ( int i = m - 1 ;
i > 0 ;
i -- ) {
  if ( ( s > 9 ) && ( s > 9 ) ) {
    res [ i ] = 9 ;
    s -= 9 ;
  }
  else {
    res [ i ] = s ;
    s = 0 ;
  }
}
res [ 0 ] = s + 1 ;
System . out . print ( "Smallest number is " ) ;
for ( int i = 0 ;
i < m ;
i ++ ) {
  System . out . print ( res [ i ] + " " ) ;
}
}
|||

C_PROGRAM_FIND_LARGEST_ELEMENT_ARRAY

public static int largest ( int [ ] arr , int n ) {
  int max = arr [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] > max ) {
      max = arr [ i ] ;
    }
  }
  return max ;
}
|||

COUNT_NUMBERS_CAN_CONSTRUCTED_USING_TWO_NUMBERS

public static int countNums ( int n , int x , int y ) {
  boolean [ ] arr = new boolean [ n + 2 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) arr [ i ] = false ;
  if ( ( x <= n ) && ( x < n ) ) arr [ x ] = true ;
  if ( ( y <= n ) && ( y < n ) ) arr [ y ] = true ;
  int result = 0 ;
  for ( int i = Math . min ( x , y ) ;
  i <= n ;
  i ++ ) {
    if ( ( arr [ i ] ) ) {
      if ( ( i + x <= n ) && ( i + x <= n ) ) arr [ i + x ] = true ;
      if ( ( i + y <= n ) && ( i + y <= n ) ) arr [ i + y ] = true ;
      result = result + 1 ;
    }
  }
  return result ;
}
|||

BUBBLE_SORT_1

public static void bubbleSort ( int [ ] arr ) {
  int n = arr . length ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    boolean swapped = false ;
    for ( int j = 0 ;
    j <= n - i - 1 ;
    j ++ ) {
      if ( arr [ j ] > arr [ j + 1 ] ) {
        arr [ j ] = arr [ j + 1 ] ;
        swapped = true ;
      }
    }
    if ( swapped == false ) break ;
  }
}
|||

MAXIMUM_SUM_2_X_N_GRID_NO_TWO_ELEMENTS_ADJACENT

public static int maxSum ( int [ ] [ ] grid , int n ) {
  int incl = Math . max ( grid [ 0 ] [ 0 ] , grid [ 1 ] [ 0 ] ) ;
  int excl = 0 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    int exclNew = Math . max ( excl , incl ) ;
    incl = excl + Math . max ( grid [ 0 ] [ i ] , grid [ 1 ] [ i ] ) ;
    excl = exclNew ;
  }
  return Math . max ( excl , incl ) ;
}
|||

GCD_FACTORIALS_TWO_NUMBERS

public static double gcdOfFactorial ( int m , int n ) {
  return Math . factorial ( Math . min ( m , n ) ) ;
}
|||

AREA_OF_A_SECTOR

public static void SectorArea ( int radius , int angle ) {
  int pi = 22 / 7 ;
  if ( angle >= 360 ) {
    System . out . println ( "Angle not possible" ) ;
    return ;
  }
  else {
    int sector = ( pi * radius * radius ) * ( angle / 360 ) ;
    System . out . println ( sector ) ;
    return ;
  }
}
|||

COUNT_EVEN_LENGTH_BINARY_SEQUENCES_WITH_SAME_SUM_OF_FIRST_AND_SECOND_HALF_BITS_1

public static int countSeq ( int n ) {
  int nCr = 1 ;
  int res = 1 ;
  for ( int r = 1 ;
  r <= n ;
  r ++ ) {
    nCr = ( nCr * ( n + 1 - r ) ) / r ;
    ;
    res += nCr * nCr ;
  };
  return res ;
}
|||

LONGEST_EVEN_LENGTH_SUBSTRING_SUM_FIRST_SECOND_HALF_1

public static int findLength ( String string ) {
  int n = string . length ( ) ;
  int maxlen = 0 ;
  int [ ] [ ] Sum = new int [ n ] [ n ] ;
  for ( int y = 0 ;
  y < n ;
  y ++ ) {
    Sum [ y ] [ y ] = new int [ n ] ;
  }
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    Sum [ i ] [ i ] = Integer . parseInt ( string . substring ( i ) ) ;
  }
  for ( int length = 2 ;
  length <= n ;
  length ++ ) {
    for ( int i = 0 ;
    i <= n - length + 1 ;
    i ++ ) {
      int j = i + length - 1 ;
      int k = length / 2 ;
      Sum [ i ] [ j ] = ( Sum [ i ] [ j - k ] + Sum [ j - k + 1 ] [ j ] ) ;
      if ( ( length % 2 == 0 && Sum [ i ] [ j - k ] == Sum [ ( j - k + 1 ) ] [ j ] && length > maxlen ) ) {
        maxlen = length ;
      }
    }
  }
  return maxlen ;
}
|||

SWAP_ALL_ODD_AND_EVEN_BITS

public static int swapBits ( int x ) {
  int evenBits = x & 0xAAAAAAAA ;
  int oddBits = x & 0x55555555 ;
  evenBits >>>= 1 ;
  oddBits <<= 1 ;
  return ( evenBits | oddBits ) ;
}
|||

SORT_ARRAY_WAVE_FORM_2

public static void sortInWave ( int [ ] arr , int n ) {
  Arrays . sort ( arr ) ;
  for ( int i = 0 ;
  i < n - 1 ;
  i += 2 ) {
    arr [ i ] = arr [ i + 1 ] ;
    arr [ i + 1 ] = arr [ i ] ;
  }
}
|||

FIND_HARMONIC_MEAN_USING_ARITHMETIC_MEAN_GEOMETRIC_MEAN

public static double compute ( double a , double b ) {
  double AM = ( a + b ) / 2 ;
  double GM = Math . sqrt ( a * b ) ;
  double HM = ( GM * GM ) / AM ;
  return HM ;
}
|||

COUNT_BALANCED_BINARY_TREES_HEIGHT_H

public static int countBT ( int h ) {
  final int MOD = 1000000007 ;
  int [ ] dp = new int [ h + 1 ] ;
  dp [ 0 ] = 1 ;
  dp [ 1 ] = 1 ;
  for ( int i = 2 ;
  i <= h ;
  i ++ ) {
    dp [ i ] = ( dp [ i - 1 ] * ( ( 2 * dp [ i - 2 ] ) % MOD + dp [ i - 1 ] ) % MOD ) % MOD ;
  }
  return dp [ h ] ;
}
|||

MINIMUM_INSERTIONS_TO_FORM_A_PALINDROME_WITH_PERMUTATIONS_ALLOWED

public static int minInsertion ( String tr1 ) {
  int n = str1 . length ( ) ;
  int res = 0 ;
  int [ ] count = new int [ 26 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    count [ ( char ) str1 . charAt ( i ) - 'a' ] ++ ;
  }
  for ( int i = 0 ;
  i < 26 ;
  i ++ ) {
    if ( ( count [ i ] % 2 == 1 ) && ( count [ i ] % 3 == 1 ) ) {
      res ++ ;
    }
  }
  if ( ( res == 0 ) || ( res == 1 ) ) {
    return 0 ;
  }
  else {
    return res - 1 ;
  }
}
|||

SHUFFLE_A_GIVEN_ARRAY

public static int [ ] randomize ( int [ ] arr , int n ) {
  for ( int i = n - 1 ;
  i > 0 ;
  i -- ) {
    int j = ThreadLocalRandom . current ( ) . nextInt ( i + 1 ) ;
    arr [ i ] = arr [ j ] ;
    arr [ j ] = arr [ i ] ;
  }
  return arr ;
}
|||

UGLY_NUMBERS

public static int getNthUglyNo ( int n ) {
  int [ ] ugly = new int [ n ] ;
  ugly [ 0 ] = 1 ;
  int i2 = i3 = i5 = 0 ;
  int nextMultipleOf2 = 2 ;
  int nextMultipleOf3 = 3 ;
  int nextMultipleOf5 = 5 ;
  for ( int l = 1 ;
  l < n ;
  l ++ ) {
    ugly [ l ] = Math . min ( nextMultipleOf2 , nextMultipleOf3 , nextMultipleOf5 ) ;
    if ( ugly [ l ] == nextMultipleOf2 ) {
      i2 ++ ;
      nextMultipleOf2 = ugly [ i2 ] * 2 ;
    }
    if ( ugly [ l ] == nextMultipleOf3 ) {
      i3 ++ ;
      nextMultipleOf3 = ugly [ i3 ] * 3 ;
    }
    if ( ugly [ l ] == nextMultipleOf5 ) {
      i5 ++ ;
      nextMultipleOf5 = ugly [ i5 ] * 5 ;
    }
  }
  return ugly [ n - 1 ] ;
}
|||

MINIMUM_COST_CUT_BOARD_SQUARES

public static double minimumCostOfBreaking ( double [ ] X , double [ ] Y , int m , int n ) {
  double res = 0 ;
  Arrays . sort ( X ) ;
  Arrays . sort ( Y ) ;
  double hzntl = 1 ;
  double vert = 1 ;
  int i = 0 ;
  int j = 0 ;
  while ( ( i < m && j < n ) || ( i < n && j < m ) ) {
    if ( ( X [ i ] > Y [ j ] ) || ( X [ i ] > Y [ j ] ) ) {
      res += X [ i ] * vert ;
      hzntl ++ ;
      i ++ ;
    }
    else {
      res += Y [ j ] * hzntl ;
      vert ++ ;
      j ++ ;
    }
  }
  double total = 0 ;
  while ( ( i < m ) || ( i < n ) ) {
    total += X [ i ] ;
    i ++ ;
  }
  res += total * vert ;
  total = 0 ;
  while ( ( j < n ) || ( j < m ) ) {
    total += Y [ j ] ;
    j ++ ;
  }
  res += total * hzntl ;
  return res ;
}
|||

DYNAMIC_PROGRAMMING_SET_10_0_1_KNAPSACK_PROBLEM_1

public static int knapSack ( int W , int [ ] wt , int [ ] val , int n ) {
  int [ ] [ ] K = new int [ W + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int w = 0 ;
    w < W + 1 ;
    w ++ ) {
      if ( i == 0 || w == 0 ) {
        K [ i ] [ w ] = 0 ;
      }
      else if ( wt [ i - 1 ] <= w ) {
        K [ i ] [ w ] = Math . max ( val [ i - 1 ] + K [ i - 1 ] [ w - wt [ i - 1 ] ] , K [ i - 1 ] [ w ] ) ;
      }
      else {
        K [ i ] [ w ] = K [ i - 1 ] [ w ] ;
      }
    }
  }
  return K [ n ] [ W ] ;
}
|||

STACK_PERMUTATIONS_CHECK_IF_AN_ARRAY_IS_STACK_PERMUTATION_OF_OTHER

public static boolean checkStackPermutation ( int [ ] ip , int [ ] op , int n ) {
  Queue < Integer > Input = new Queue < Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) Input . offer ( ip [ i ] ) ;
  Queue < Integer > Output = new Queue < Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) Output . offer ( op [ i ] ) ;
  Stack < Integer > tempStack = new Stack < Integer > ( ) ;
  while ( ( ! Input . isEmpty ( ) ) && ( ! Output . isEmpty ( ) ) ) {
    Integer ele = Input . peek ( ) ;
    Input . pop ( ) ;
    if ( ( ele == Output . peek ( ) ) && ( tempStack . size ( ) != 0 ) ) {
      Output . pop ( ) ;
      while ( ( tempStack . size ( ) != 0 ) && ( tempStack . size ( ) == 0 ) ) {
        if ( ( tempStack . peek ( ) == Output . peek ( ) ) && ( tempStack . size ( ) == 1 ) ) {
          tempStack . pop ( ) ;
          Output . pop ( ) ;
        }
        else break ;
      }
    }
    else tempStack . push ( ele ) ;
  }
  return ( Input . isEmpty ( ) && tempStack . size ( ) == 0 ) ;
}
|||

PROBABILITY_THREE_RANDOMLY_CHOSEN_NUMBERS_AP

public static double procal ( double n ) {
  return ( 3.0 * n ) / ( 4.0 * ( n * n ) - 1 ) ;
}
|||

REMOVE_BRACKETS_ALGEBRAIC_STRING_CONTAINING_OPERATORS

public static String simplify ( String Str ) {
  int Len = Str . length ( ) ;
  String res = new String ( null ) ;
  int index = 0 ;
  int i = 0 ;
  Stack s = new Stack ( ) ;
  s . push ( 0 ) ;
  while ( ( i < Len ) && ( i < Str . length ( ) ) ) {
    if ( ( Str . charAt ( i ) == '+' ) ) {
      if ( ( s . pop ( ) == 1 ) ) {
        res . charAt ( index ) = '-' ;
        index ++ ;
      }
      if ( ( s . pop ( ) == 0 ) ) {
        res . charAt ( index ) = '+' ;
        index ++ ;
      }
    }
    else if ( ( Str . charAt ( i ) == '-' ) ) {
      if ( ( s . pop ( ) == 1 ) ) {
        res . charAt ( index ) = '+' ;
        index ++ ;
      }
      else if ( ( s . pop ( ) == 0 ) ) {
        res . charAt ( index ) = '-' ;
        index ++ ;
      }
    }
    else if ( ( Str . charAt ( i ) == '(' ) && i > 0 ) ) {
      if ( ( Str . charAt ( i - 1 ) == '-' ) ) {
        int x = 0 == ( s . pop ( ) == 1 ) ? 1 : 0 ;
        s . push ( x ) ;
      }
      else if ( ( Str . charAt ( i - 1 ) == '+' ) ) {
        s . push ( s . pop ( ) ) ;
      }
    }
    else if ( ( Str . charAt ( i ) == ')' ) ) {
      s . pop ( ) ;
    }
    else {
      res . charAt ( index ) = Str . charAt ( i ) ;
      index ++ ;
    }
    i ++ ;
  }
  return res ;
}
|||

FIND_NUMBER_PERFECT_SQUARES_TWO_GIVEN_NUMBERS

public static int CountSquares ( int a , int b ) {
  int cnt = 0 ;
  for ( int i = a ;
  i <= b ;
  i ++ ) {
    int j = 1 ;
    ;
    while ( j * j <= i ) {
      if ( j * j == i ) cnt = cnt + 1 ;
      j = j + 1 ;
    }
    i = i + 1 ;
  }
  return cnt ;
}
|||

K_NUMBERS_DIFFERENCE_MAXIMUM_MINIMUM_K_NUMBER_MINIMIZED

public static int minDiff ( int [ ] arr , int n , int k ) {
  int result = + 2147483647 ;
  Arrays . sort ( arr ) ;
  for ( int i = 0 ;
  i < n - k + 1 ;
  i ++ ) {
    result = ( int ) Math . min ( result , arr [ i + k - 1 ] - arr [ i ] ) ;
  }
  return result ;
}
|||

CHECK_LARGE_NUMBER_DIVISIBLE_13_NOT

public static boolean checkDivisibility ( String num ) {
  int length = num . length ( ) ;
  if ( ( length == 1 && num . charAt ( 0 ) == '0' ) || ( length == 2 && num . charAt ( 0 ) == '1' ) ) {
    return true ;
  }
  if ( ( length % 3 == 1 ) || ( length % 3 == 2 ) ) {
    num = String . valueOf ( num ) + "00" ;
    length += 2 ;
  }
  else if ( ( length % 3 == 2 ) || ( length % 3 == 3 ) ) {
    num = String . valueOf ( num ) + "0" ;
    length += 1 ;
  }
  long sum = 0 ;
  long p = 1 ;
  for ( int i = length - 1 ;
  i >= 0 ;
  i -- ) {
    long group = 0 ;
    group += ( num . charAt ( i ) - '0' ) ;
    i -- ;
    group += ( num . charAt ( i ) - '0' ) * 10 ;
    i -- ;
    group += ( num . charAt ( i ) - '0' ) * 100 ;
    sum = sum + group * p ;
    p *= ( - 1 ) ;
  }
  sum = Math . abs ( sum ) ;
  return ( sum % 13 == 0 ) ;
}
|||

GIVEN_N_X_N_SQUARE_MATRIX_FIND_SUM_SUB_SQUARES_SIZE_K_X_K

public static void printSumSimple ( int [ ] [ ] mat , int k ) {
  if ( ( k > n ) || ( k < 0 ) ) return ;
  for ( int i = 0 ;
  i < n - k + 1 ;
  i ++ ) {
    for ( int j = 0 ;
    j < n - k + 1 ;
    j ++ ) {
      int sum = 0 ;
      for ( int p = i ;
      p < k + i ;
      p ++ ) {
        for ( int q = j ;
        q < k + j ;
        q ++ ) {
          sum += mat [ p ] [ q ] ;
        }
      }
      System . out . print ( sum + " " ) ;
    }
    System . out . println ( ) ;
  }
}
|||

FIND_THE_POINT_WHERE_MAXIMUM_INTERVALS_OVERLAP_1

public static void maxOverlap ( int [ ] start , int [ ] end ) {
  int n = start . length ;
  int maxa = Math . max ( start , end ) ;
  int maxb = Math . max ( end , start ) ;
  int maxc = Math . max ( maxa , maxb ) ;
  int [ ] x = ( maxc + 2 ) * new int [ n ] ;
  int cur = 0 ;
  int idx = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    x [ start [ i ] ] ++ ;
    x [ end [ i ] + 1 ] -- ;
  }
  int maxy = - 1 ;
  for ( int i = 0 ;
  i <= maxc ;
  i ++ ) {
    cur += x [ i ] ;
    if ( maxy < cur ) {
      maxy = cur ;
      idx = i ;
    }
  }
  System . out . println ( "Maximum value is: {
0:d}" + " at position: {
0:d}" + idx ) ;
    }
    
|||

MAXIMUM_SUBSEQUENCE_SUM_SUCH_THAT_NO_THREE_ARE_CONSECUTIVE_1

public static int maxSumWO3Consec ( int n ) {
  if ( ( sum [ n ] != - 1 ) && ( n > 0 ) ) return sum [ n ] ;
  if ( ( n == 0 ) || ( n == 1 ) ) {
    sum [ n ] = 0 ;
    return sum [ n ] ;
  }
  if ( ( n == 2 ) || ( n == 3 ) ) {
    sum [ n ] = arr [ 0 ] ;
    return sum [ n ] ;
  }
  if ( ( n == 4 ) || ( n == 5 ) ) {
    sum [ n ] = arr [ 1 ] + arr [ 0 ] ;
    return sum [ n ] ;
  }
  sum [ n ] = Math . max ( Math . max ( maxSumWO3Consec ( n - 1 ) , maxSumWO3Consec ( n - 2 ) + arr [ n - 1 ] ) , arr [ n - 2 ] + arr [ n - 1 ] + maxSumWO3Consec ( n - 3 ) ) ;
  return sum [ n ] ;
}
|||

C_PROGRAM_ADDITION_TWO_MATRICES

public static void add ( int [ ] [ ] A , int [ ] [ ] B , int [ ] [ ] C ) {
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    for ( int j = 0 ;
    j < N ;
    j ++ ) {
      C [ i ] [ j ] = A [ i ] [ j ] + B [ i ] [ j ] ;
    }
  }
}
|||

FIND_MAXIMUM_AVERAGE_SUBARRAY_OF_K_LENGTH_1

public static int findMaxAverage ( int [ ] arr , int n , int k ) {
  if ( ( k > n ) && ( k < 0 ) ) return - 1 ;
  int sum = arr [ 0 ] ;
  for ( int i = 1 ;
  i < k ;
  i ++ ) sum += arr [ i ] ;
  int maxSum = sum ;
  int maxEnd = k - 1 ;
  for ( int i = k ;
  i < n ;
  i ++ ) {
    sum = sum + arr [ i ] - arr [ i - k ] ;
    if ( ( sum > maxSum ) && ( sum < maxEnd ) ) {
      maxSum = sum ;
      maxEnd = i ;
    }
  }
  return maxEnd - k + 1 ;
}
|||

FIND_CENTER_CIRCLE_USING_ENDPOINTS_DIAMETER

public static void center ( int x1 , int x2 , int y1 , int y2 ) {
  System . out . print ( Integer . toString ( ( x1 + x2 ) / 2 ) + "," ) ;
  System . out . print ( "," + Integer . toString ( ( y1 + y2 ) / 2 ) ) ;
}
|||

TOTAL_NUMBER_OF_NON_DECREASING_NUMBERS_WITH_N_DIGITS

public static int countNonDecreasing ( int n ) {
  int [ ] [ ] dp = new int [ n + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    dp [ i ] [ 1 ] = i ;
  }
  for ( int i = 0 ;
  i < 10 ;
  i ++ ) {
    dp [ i ] [ 1 ] = 1 ;
  }
  for ( int digit = 0 ;
  digit < 10 ;
  digit ++ ) {
    for ( int len = 2 ;
    len <= n ;
    len ++ ) {
      for ( int x = 0 ;
      x < digit + 1 ;
      x ++ ) {
        dp [ digit ] [ len ] += dp [ x ] [ len - 1 ] ;
      }
    }
  }
  int count = 0 ;
  for ( int i = 0 ;
  i < 10 ;
  i ++ ) {
    count += dp [ i ] [ n ] ;
  }
  return count ;
}
|||

PRINT_REVERSE_STRING_REMOVING_VOWELS

public static void replaceOriginal ( String s , int n ) {
  char [ ] r = new char [ n ] ;
  r [ 0 ] = ' ' ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    r [ i ] = s . charAt ( n - 1 - i ) ;
    if ( ( s . charAt ( i ) != 'a' && s . charAt ( i ) != 'e' && s . charAt ( i ) != 'i' && s . charAt ( i ) != 'o' && s . charAt ( i ) != 'u' ) || ( s . charAt ( i ) != 'o' && s . charAt ( i ) != 'u' ) ) {
      System . out . print ( r [ i ] + " " ) ;
    }
  }
  System . out . println ( ) ;
}
|||

FIND_ELEMENTS_PRESENT_FIRST_ARRAY_NOT_SECOND_1

public static void findMissing ( int [ ] a , int [ ] b , int n , int m ) {
  Map < Integer , Integer > s = Maps . newHashMap ( ) ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) {
    s . put ( b [ i ] , 1 ) ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( a [ i ] != 0 ) {
      System . out . print ( a [ i ] + " " ) ;
    }
  }
}
|||

COUNT_STRINGS_CAN_FORMED_USING_B_C_GIVEN_CONSTRAINTS

public static int countStr ( int n , int bCount , int cCount ) {
  if ( ( bCount < 0 || cCount < 0 ) && ( n == 0 ) ) return 0 ;
  if ( ( bCount == 0 && cCount == 0 ) || ( bCount == 0 && cCount == 0 ) ) return 1 ;
  int res = countStr ( n - 1 , bCount , cCount ) ;
  res += countStr ( n - 1 , bCount - 1 , cCount ) ;
  res += countStr ( n - 1 , bCount , cCount - 1 ) ;
  return res ;
}
|||

GOLD_MINE_PROBLEM

public static int getMaxGold ( int [ ] [ ] gold , int m , int n ) {
  int [ ] [ ] goldTable = new int [ n ] [ m ] ;
  for ( int j = 0 ;
  j < m ;
  j ++ ) {
    for ( int col = n - 1 ;
    col >= 0 ;
    col -- ) {
      for ( int row = 0 ;
      row < m ;
      row ++ ) {
        if ( ( col == n - 1 ) || ( col == n - 2 ) ) {
          int right = 0 ;
          if ( goldTable [ row ] [ col + 1 ] != null ) {
            right = goldTable [ row ] [ col + 1 ] ;
          }
          if ( ( row == 0 || col == n - 1 ) || ( row == 0 ) ) {
            int rightUp = 0 ;
            if ( goldTable [ row - 1 ] [ col + 1 ] != null ) {
              rightUp = goldTable [ row - 1 ] [ col + 1 ] ;
            }
            if ( ( row == m - 1 || col == n - 1 ) || ( row == m - 2 ) ) {
              int rightDown = 0 ;
              if ( goldTable [ row + 1 ] [ col + 1 ] != null ) {
                rightDown = goldTable [ row + 1 ] [ col + 1 ] ;
              }
              goldTable [ row ] [ col ] = gold [ row ] [ col ] + Math . max ( right , rightUp , rightDown ) ;
            }
          }
        }
      }
    }
    int res = goldTable [ 0 ] [ 0 ] ;
    for ( int i = 1 ;
    i < m ;
    i ++ ) {
      res = Math . max ( res , goldTable [ i ] [ 0 ] ) ;
    }
    return res ;
  }
  
|||

COUNT_WAYS_BUILD_STREET_GIVEN_CONSTRAINTS

public static int countWays ( int n ) {
  int [ ] [ ] dp = new int [ 2 ] [ n + 1 ] ;
  dp [ 0 ] [ 1 ] = 1 ;
  dp [ 1 ] [ 1 ] = 2 ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    dp [ 0 ] [ i ] = dp [ 0 ] [ i - 1 ] + dp [ 1 ] [ i - 1 ] ;
    dp [ 1 ] [ i ] = ( dp [ 0 ] [ i - 1 ] * 2 + dp [ 1 ] [ i - 1 ] ) ;
  }
  return dp [ 0 ] [ n ] + dp [ 1 ] [ n ] ;
}
|||

RETURN_A_PAIR_WITH_MAXIMUM_PRODUCT_IN_ARRAY_OF_INTEGERS_1

public static void maxProduct ( int [ ] arr , int n ) {
  if ( ( n < 2 ) || ( n == 2 ) ) {
    System . out . println ( "No pairs exists" ) ;
    return ;
  }
  if ( ( n == 2 ) || ( n == 3 ) ) {
    System . out . print ( arr [ 0 ] + " " + arr [ 1 ] ) ;
    return ;
  }
  int posa = 0 ;
  int posb = 0 ;
  int nega = 0 ;
  int negb = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( arr [ i ] > posa ) && ( arr [ i ] < posb ) ) {
      posb = posa ;
      posa = arr [ i ] ;
    }
    else if ( ( arr [ i ] > posb ) && ( arr [ i ] < posa ) ) {
      posb = arr [ i ] ;
    }
    if ( ( arr [ i ] < 0 ) && ( Math . abs ( arr [ i ] ) > Math . abs ( nega ) ) ) {
      negb = nega ;
      nega = arr [ i ] ;
    }
    else if ( ( arr [ i ] < 0 ) && ( Math . abs ( arr [ i ] ) > Math . abs ( negb ) ) ) {
      negb = arr [ i ] ;
    }
  }
  if ( ( nega * negb > posa * posb ) && ( negb * posb > posa * posb ) ) {
    System . out . println ( "Max product pair is {
" + nega + ", " + negb + "}" ) ;
    }
    else {
      System . out . println ( "Max product pair is {
" + posa + ", " + posb + "}" ) ;
      }
    }
    
|||

POSITION_OF_RIGHTMOST_SET_BIT

public static int getFirstSetBitPos ( int n ) {
  return MathUtils . log2 ( n & - n ) + 1 ;
}
|||

LONGEST_SUBSEQUENCE_WHERE_EVERY_CHARACTER_APPEARS_AT_LEAST_K_TIMES

public static void longestSubseqWithK ( String str , int k ) {
  int n = str . length ( ) ;
  int [ ] freq = new int [ MAX_CHARS ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) freq [ ( char ) str . charAt ( i ) - 'a' ] ++ ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( ( freq [ ( char ) str . charAt ( i ) - 'a' ] ) >= k ) System . out . print ( str . charAt ( i ) + " " ) ;
}
|||

POSSIBLE_TO_MAKE_A_DIVISIBLE_BY_3_NUMBER_USING_ALL_DIGITS_IN_AN_ARRAY

public static boolean isPossibleToMakeDivisible ( int [ ] arr , int n ) {
  int remainder = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    remainder = ( remainder + arr [ i ] ) % 3 ;
  }
  return ( remainder == 0 ) ;
}
|||

AREA_SQUARE_CIRCUMSCRIBED_CIRCLE

public static int findArea ( int r ) {
  return ( 2 * r * r ) ;
}
|||

FIND_MAXIMUM_DOT_PRODUCT_TWO_ARRAYS_INSERTION_0S

public static double MaxDotProduct ( double [ ] A , double [ ] B , int m , int n ) {
  int [ ] [ ] dp = new int [ m + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i < m + 1 ;
  i ++ ) {
    dp [ i ] [ i ] = 0 ;
  }
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    for ( int j = i ;
    j < m ;
    j ++ ) {
      dp [ i ] [ j ] = Math . max ( ( dp [ i - 1 ] [ j - 1 ] + ( A [ j - 1 ] * B [ i - 1 ] ) ) , dp [ i ] [ j - 1 ] ) ;
    }
  }
  return dp [ n ] [ m ] ;
}
|||

FIND_DISTINCT_SUBSET_SUBSEQUENCE_SUMS_ARRAY

public static void printDistSum ( int [ ] arr , int n ) {
  int Sum = Arrays . stream ( arr ) . mapToInt ( Integer :: intValue ) . sum ( ) ;
  boolean [ ] [ ] dp = new boolean [ Sum + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i < n + 1 ;
  i ++ ) {
    dp [ i ] [ 0 ] = true ;
  }
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    dp [ i ] [ arr [ i - 1 ] ] = true ;
    for ( int j = 1 ;
    j <= Sum ;
    j ++ ) {
      if ( ( dp [ i - 1 ] [ j ] == true ) && ( dp [ i ] [ j + arr [ i - 1 ] ] == true ) ) {
        dp [ i ] [ j ] = true ;
        dp [ i ] [ j + arr [ i - 1 ] ] = true ;
      }
    }
  }
  for ( int j = 0 ;
  j < Sum + 1 ;
  j ++ ) {
    if ( ( dp [ n ] [ j ] == true ) && ( dp [ n ] [ j + arr [ i - 1 ] ] == true ) ) {
      System . out . print ( j + " " ) ;
    }
  }
}
|||

SPLIT_NUMERIC_ALPHABETIC_AND_SPECIAL_SYMBOLS_FROM_A_STRING

public static void splitString ( String str ) {
  String alpha = "" ;
  String num = "" ;
  String special = "" ;
  for ( int i = 0 ;
  i < str . length ( ) ;
  i ++ ) {
    if ( ( str . charAt ( i ) == ' ' ) || ( str . charAt ( i ) == '\t' ) ) num = num + str . charAt ( i ) ;
    else if ( ( ( str . charAt ( i ) >= 'A' && str . charAt ( i ) <= 'Z' ) || ( str . charAt ( i ) >= 'a' && str . charAt ( i ) <= 'z' ) ) alpha += str . charAt ( i ) ;
    else special += str . charAt ( i ) ;
  }
  System . out . println ( alpha ) ;
  System . out . println ( num ) ;
  System . out . println ( special ) ;
}
|||

MAXIMUM_SUM_ALTERNATING_SUBSEQUENCE_SUM

public static int maxAlternateSum ( int [ ] arr , int n ) {
  if ( ( n == 1 ) || ( n == 0 ) ) return arr [ 0 ] ;
  int [ ] dec = new int [ n + 1 ] ;
  int [ ] inc = new int [ n + 1 ] ;
  dec [ 0 ] = inc [ 0 ] = arr [ 0 ] ;
  int flag = 0 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < i ;
    j ++ ) {
      if ( ( arr [ j ] > arr [ i ] ) && ( arr [ j ] < arr [ i ] ) ) {
        dec [ i ] = Math . max ( dec [ i ] , inc [ j ] + arr [ i ] ) ;
        flag = 1 ;
      }
      else if ( ( arr [ j ] < arr [ i ] ) && flag == 1 ) {
        inc [ i ] = Math . max ( inc [ i ] , dec [ j ] + arr [ i ] ) ;
      }
    }
  }
  int result = - 2147483648 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( result < inc [ i ] ) && ( result < dec [ i ] ) ) result = inc [ i ] ;
    if ( ( result < dec [ i ] ) && ( result < inc [ i ] ) ) result = dec [ i ] ;
  }
  return result ;
}
|||

FIND_PAIR_MAXIMUM_GCD_ARRAY

public static int findMaxGCD ( int [ ] arr , int n ) {
  int high = 0 ;
  int i = 0 ;
  while ( i < n ) {
    high = Math . max ( high , arr [ i ] ) ;
    i = i + 1 ;
  }
  int [ ] divisors = new int [ high + 1 ] ;
  divisors [ 0 ] = 0 ;
  i = 0 ;
  while ( i < n ) {
    int j = 1 ;
    while ( j <= Math . sqrt ( arr [ i ] ) ) {
      if ( ( arr [ i ] % j == 0 ) && ( j != arr [ i ] / j ) ) {
        divisors [ j ] = divisors [ j ] + 1 ;
        if ( ( j != arr [ i ] / j ) && ( j != arr [ i ] / j ) ) {
          divisors [ arr [ i ] / j ] = divisors [ arr [ i ] / j ] ;
          + 1 ;
        }
      }
      j = j + 1 ;
    }
    i = i + 1 ;
  }
  i = high ;
  while ( i >= 1 ) {
    if ( ( divisors [ i ] > 1 ) && ( divisors [ i ] > 0 ) ) return i ;
    i = i - 1 ;
  }
  return 1 ;
}
|||

FIND_MINIMUM_NUMBER_OF_COINS_THAT_MAKE_A_CHANGE_1

public static int minCoins ( int [ ] coins , int m , int V ) {
  int [ ] table = new int [ V + 1 ] ;
  table [ 0 ] = 0 ;
  for ( int i = 1 ;
  i <= V ;
  i ++ ) table [ i ] = Integer . MAX_VALUE ;
  for ( int i = 1 ;
  i <= V ;
  i ++ ) {
    for ( int j = 0 ;
    j < m ;
    j ++ ) {
      if ( ( coins [ j ] <= i ) && ( coins [ j ] >= coins [ i ] ) ) {
        int subRes = table [ i - coins [ j ] ] ;
        if ( ( subRes != Integer . MAX_VALUE && subRes + 1 < table [ i ] ) && ( subRes + 1 < table [ i ] ) ) {
          table [ i ] = subRes + 1 ;
        }
      }
    }
  }
  return table [ V ] ;
}
|||

SUM_NODES_K_TH_LEVEL_TREE_REPRESENTED_STRING

public static int sumAtKthLevel ( String tree , int k ) {
  int level = - 1 ;
  int sum = 0 ;
  int n = tree . length ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( tree . charAt ( i ) == '(' ) && ( tree . charAt ( i + 1 ) == ')' ) ) level ++ ;
    else if ( ( tree . charAt ( i ) == ')' ) && ( tree . charAt ( i + 1 ) == '(' ) ) level -- ;
    else {
      if ( ( level == k ) && ( tree . charAt ( i + 1 ) == '(' ) ) sum += ( Character . digit ( tree . charAt ( i + 1 ) , 16 ) - '0' ) ;
    }
  }
  return sum ;
}
|||

DYNAMIC_PROGRAMMING_SET_4_LONGEST_COMMON_SUBSEQUENCE

public static int lcs ( int [ ] X , int [ ] Y , int m , int n ) {
  if ( m == 0 || n == 0 ) return 0 ;
  ;
  else if ( X [ m - 1 ] == Y [ n - 1 ] ) return 1 + lcs ( X , Y , m - 1 , n - 1 ) ;
  ;
  else return Math . max ( lcs ( X , Y , m , n - 1 ) , lcs ( X , Y , m - 1 , n ) ) ;
  ;
}
|||

CHECK_GIVEN_SENTENCE_GIVEN_SET_SIMPLE_GRAMMER_RULES

public static boolean checkSentence ( String string ) {
  int length = string . length ( ) ;
  if ( string . charAt ( 0 ) < 'A' || string . charAt ( 0 ) > 'Z' ) return false ;
  if ( string . charAt ( length - 1 ) != '.' ) return false ;
  int prev_state = 0 ;
  int curr_state = 0 ;
  int index = 1 ;
  while ( ( string . charAt ( index ) ) != ' ' ) {
    if ( string . charAt ( index ) >= 'A' && string . charAt ( index ) <= 'Z' ) curr_state = 0 ;
    else if ( string . charAt ( index ) == ' ' ) curr_state = 1 ;
    else if ( string . charAt ( index ) >= 'a' && string . charAt ( index ) <= 'z' ) curr_state = 2 ;
    else if ( string . charAt ( index ) == '.' ) curr_state = 3 ;
    if ( prev_state == curr_state && curr_state != 2 ) return false ;
    if ( prev_state == 2 && curr_state == 0 ) return false ;
    if ( curr_state == 3 && prev_state != 1 ) return true ;
    index ++ ;
    prev_state = curr_state ;
  }
  return false ;
}
|||

CHECK_DIVISIBILITY_LARGE_NUMBER_999

public static boolean isDivisible999 ( String num ) {
  int n = num . length ( ) ;
  ;
  if ( ( n == 0 || num . charAt ( 0 ) == '0' ) && ( num . charAt ( 1 ) == ' ' ) ) return true ;
  if ( ( ( n % 3 ) == 1 ) && ( num . charAt ( 2 ) == ' ' ) ) num = "00" + num ;
  if ( ( ( n % 3 ) == 2 ) && ( num . charAt ( 3 ) == ' ' ) ) num = "0" + num ;
  int gSum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i += 3 ) {
    int group = 0 ;
    group += ( ( char ) num . charAt ( i ) - 48 ) * 100 ;
    group += ( ( char ) num . charAt ( i + 1 ) - 48 ) * 10 ;
    group += ( ( char ) num . charAt ( i + 2 ) - 48 ) ;
    gSum += group ;
  }
  if ( ( gSum > 1000 ) && ( num . charAt ( 0 ) == ' ' ) ) {
    num = Integer . toString ( gSum ) ;
    n = num . length ( ) ;
    gSum = isDivisible999 ( num ) ;
  }
  return ( gSum == 999 ) ;
}
|||

CHECK_LARGE_NUMBER_DIVISIBLE_9_NOT

public static boolean check ( String st ) {
  int n = st . length ( ) ;
  int digitSum = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    digitSum = digitSum + ( int ) ( st . charAt ( i ) ) ;
  }
  return ( digitSum % 9 == 0 ) ;
}
|||

NUMBER_OF_BINARY_TREES_FOR_GIVEN_PREORDER_SEQUENCE_LENGTH

public static int countTrees ( int n ) {
  int [ ] BT = new int [ n + 1 ] ;
  BT [ 0 ] = BT [ 1 ] = 1 ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j < i ;
    j ++ ) {
      BT [ i ] += BT [ j ] * BT [ i - j - 1 ] ;
    }
  }
  return BT [ n ] ;
}
|||

PROGRAM_SWAP_UPPER_DIAGONAL_ELEMENTS_LOWER_DIAGONAL_ELEMENTS_MATRIX

public static void swapUpperToLower ( int [ ] [ ] arr ) {
  int n = 4 ;
  ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= n ;
    j ++ ) {
      int temp = arr [ i ] [ j ] ;
      ;
      arr [ i ] [ j ] = arr [ j ] [ i ] ;
      ;
      arr [ j ] [ i ] = temp ;
    }
  }
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      System . out . print ( arr [ i ] [ j ] + " " ) ;
      ;
    }
    System . out . println ( " " ) ;
    ;
  }
}
|||

FIND_SUM_MODULO_K_FIRST_N_NATURAL_NUMBER_1

public static int findSum ( int N , int K ) {
  double ans ;
  ;
  double y = N / K ;
  ;
  double x = N % K ;
  ;
  ans = ( ( K * ( K - 1 ) / 2 ) * y + ( x * ( x + 1 ) ) / 2 ) ;
  ;
  return ( int ) ans ;
}
|||

WAYS_REMOVE_ONE_ELEMENT_BINARY_STRING_XOR_BECOMES_ZERO

public static int xorZero ( String str ) {
  int oneCount = 0 ;
  int zeroCount = 0 ;
  int n = str . length ( ) ;
  for ( int i = 0 ;
  i < n ;
  i += 1 ) {
    if ( ( str . charAt ( i ) == '1' ) && ( str . charAt ( i + 1 ) == '0' ) ) {
      oneCount ++ ;
    }
    else {
      zeroCount ++ ;
    }
  }
  if ( ( oneCount % 2 == 0 ) && ( zeroCount == 0 ) ) {
    return zeroCount ;
  }
  return oneCount ;
}
|||

DYNAMIC_PROGRAMMING_SET_7_COIN_CHANGE

public static int count ( int [ ] S , int m , int n ) {
  if ( ( n == 0 ) && ( m > 0 ) ) return 1 ;
  if ( ( n < 0 ) && ( m > 0 ) ) return 0 ;
  ;
  if ( ( m <= 0 && n >= 1 ) && ( n >= 0 ) ) return 0 ;
  return count ( S , m - 1 , n ) + count ( S , m , n - S [ m - 1 ] ) ;
  ;
}
|||

MINIMUM_SUM_SUBSEQUENCE_LEAST_ONE_EVERY_FOUR_CONSECUTIVE_ELEMENTS_PICKED

public static int minSum ( int [ ] arr , int n ) {
  int [ ] dp = new int [ n ] ;
  if ( ( n == 1 ) && ( arr [ 0 ] == 0 ) ) return arr [ 0 ] ;
  if ( ( n == 2 ) && ( arr [ 0 ] == 1 ) ) return Math . min ( arr [ 0 ] , arr [ 1 ] ) ;
  if ( ( n == 3 ) && ( arr [ 0 ] == 2 ) ) return Math . min ( arr [ 0 ] , Math . min ( arr [ 1 ] , arr [ 2 ] ) ) ;
  if ( ( n == 4 ) && ( arr [ 0 ] == 3 ) ) return Math . min ( Math . min ( arr [ 0 ] , arr [ 1 ] ) , Math . min ( arr [ 2 ] , arr [ 3 ] ) ) ;
  dp [ 0 ] = arr [ 0 ] ;
  dp [ 1 ] = arr [ 1 ] ;
  dp [ 2 ] = arr [ 2 ] ;
  dp [ 3 ] = arr [ 3 ] ;
  for ( int i = 4 ;
  i < n ;
  i ++ ) dp [ i ] = arr [ i ] + Math . min ( Math . min ( dp [ i - 1 ] , dp [ i - 2 ] ) , Math . min ( dp [ i - 3 ] , dp [ i - 4 ] ) ) ;
  return Math . min ( Math . min ( dp [ n - 1 ] , dp [ n - 2 ] ) , Math . min ( dp [ n - 4 ] , dp [ n - 3 ] ) ) ;
}
|||

MAXIMUM_PATH_SUM_TRIANGLE

public static int maxPathSum ( int [ ] [ ] tri , int m , int n ) {
  for ( int i = m - 1 ;
  i >= 0 ;
  i -- ) {
    for ( int j = 0 ;
    j < i + 1 ;
    j ++ ) {
      if ( ( tri [ i + 1 ] [ j ] > tri [ i + 1 ] [ j + 1 ] ) && ( tri [ i ] [ j ] < tri [ i + 1 ] [ j + 1 ] ) ) {
        tri [ i ] [ j ] += tri [ i + 1 ] [ j ] ;
      }
      else {
        tri [ i ] [ j ] += tri [ i + 1 ] [ j + 1 ] ;
      }
    }
  }
  return tri [ 0 ] [ 0 ] ;
}
|||

FIND_THREE_ELEMENT_FROM_DIFFERENT_THREE_ARRAYS_SUCH_THAT_THAT_A_B_C_K

public static boolean findTriplet ( int [ ] a1 , int [ ] a2 , int [ ] a3 , int n1 , int n2 , int n3 , int sum ) {
  for ( int i = 0 ;
  i <= n1 ;
  i ++ ) {
    for ( int j = 0 ;
    j <= n2 ;
    j ++ ) {
      for ( int k = 0 ;
      k <= n3 ;
      k ++ ) {
        if ( ( a1 [ i ] + a2 [ j ] + a3 [ k ] == sum ) && ( a1 [ i ] + a2 [ j ] + a3 [ k ] == sum ) ) {
          return true ;
        }
      }
    }
  }
  return false ;
}
|||

TAIL_RECURSION_FIBONACCI

public static int fib ( int n , int a , int b ) {
  if ( n == 0 ) return a ;
  if ( n == 1 ) return b ;
  return fib ( n - 1 , b , a + b ) ;
  ;
}
|||

PROGRAM_TO_CHECK_IF_A_GIVEN_NUMBER_IS_LUCKY_ALL_DIGITS_ARE_DIFFERENT

public static int isLucky ( int n ) {
  int [ ] ar = new int [ 10 ] ;
  while ( ( n > 0 ) && ( ar [ n ] != 0 ) ) {
    int digit = Math . floor ( n % 10 ) ;
    if ( ( ar [ digit ] != 0 ) && ( ar [ digit ] != 1 ) ) {
      return 0 ;
    }
    ar [ digit ] = 1 ;
    n = n / 10 ;
  }
  return 1 ;
}
|||

GIVEN_N_X_N_SQUARE_MATRIX_FIND_SUM_SUB_SQUARES_SIZE_K_X_K_1

public static void printSumTricky ( int [ ] [ ] mat , int k ) {
  n = mat . length ;
  if ( k > n ) return ;
  stripSum = new int [ n ] [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int j = 0 ;
    for ( int i = 0 ;
    i < k ;
    i ++ ) {
      Sum += mat [ i ] [ j ] ;
    }
    stripSum [ 0 ] [ j ] = Sum ;
    for ( int i = 1 ;
    i < n - k ;
    i ++ ) {
      Sum += ( mat [ i + k - 1 ] [ j ] - mat [ i - 1 ] [ j ] ) ;
      stripSum [ i ] [ j ] = Sum ;
    }
  }
  for ( int i = 0 ;
  i < n - k + 1 ;
  i ++ ) {
    Sum = 0 ;
    for ( int j = 0 ;
    j < k ;
    j ++ ) {
      Sum += stripSum [ i ] [ j ] ;
    }
    System . out . print ( Sum + " " ) ;
    for ( int j = 1 ;
    j < n - k + 1 ;
    j ++ ) {
      Sum += ( stripSum [ i ] [ j + k - 1 ] - stripSum [ i ] [ j - 1 ] ) ;
      System . out . print ( Sum + " " ) ;
    }
    System . out . println ( ) ;
  }
}
|||

SCHEDULE_ELEVATOR_TO_REDUCE_THE_TOTAL_TIME_TAKEN

public static int minTime ( int n , int k , int [ ] a ) {
  Arrays . sort ( a , 0 , n ) ;
  ;
  int minTime = 0 ;
  ;
  for ( int i = 0 ;
  i < n ;
  i += k ) {
    minTime += ( 2 * a [ i ] ) ;
  };
  return minTime ;
}
|||

ODD_EVEN_SORT_BRICK_SORT

public static void oddEvenSort ( int [ ] arr , int n ) {
  int isSorted = 0 ;
  while ( isSorted == 0 ) {
    isSorted = 1 ;
    int temp = 0 ;
    for ( int i = 1 ;
    i < n - 1 ;
    i += 2 ) {
      if ( arr [ i ] > arr [ i + 1 ] ) {
        arr [ i ] = arr [ i + 1 ] ;
        isSorted = 0 ;
      }
    }
    for ( int i = 0 ;
    i < n - 1 ;
    i += 2 ) {
      if ( arr [ i ] > arr [ i + 1 ] ) {
        arr [ i ] = arr [ i + 1 ] ;
        isSorted = 0 ;
      }
    }
  }
  return ;
}
|||

RETURN_MAXIMUM_OCCURRING_CHARACTER_IN_THE_INPUT_STRING

public static char getMaxOccuringChar ( String str ) {
  int [ ] count = new int [ ASCII_SIZE ] ;
  int max = - 1 ;
  char c = '\0' ;
  for ( int i = 0 ;
  i < str . length ( ) ;
  i ++ ) {
    count [ ( int ) str . charAt ( i ) ] ++ ;
    ;
  }
  for ( int i = 0 ;
  i < str . length ( ) ;
  i ++ ) {
    if ( max < count [ ( int ) str . charAt ( i ) ] ) {
      max = count [ ( int ) str . charAt ( i ) ] ;
      c = str . charAt ( i ) ;
    }
  }
  return c ;
}
|||

COUNT_NUMBER_PAIRS_N_B_N_GCD_B_B

public static int CountPairs ( int n ) {
  int k = n ;
  int imin = 1 ;
  int ans = 0 ;
  while ( ( imin <= n ) && ( k > 0 ) ) {
    int imax = n / k ;
    ans += k * ( imax - imin + 1 ) ;
    imin = imax + 1 ;
    k = n / imin ;
  }
  return ans ;
}
|||

K_TH_DISTINCT_OR_NON_REPEATING_ELEMENT_IN_AN_ARRAY_1

public static int printKDistinct ( int arr [ ] , int size , int KthIndex ) {
  HashMap < Integer , Integer > dict = new HashMap < Integer , Integer > ( ) ;
  ArrayList < Integer > vect = new ArrayList < Integer > ( ) ;
  for ( int i = 0 ;
  i < size ;
  i ++ ) {
    if ( ( arr [ i ] < dict . size ( ) ) && ( arr [ i ] > 0 ) ) dict . put ( arr [ i ] , dict . get ( arr [ i ] ) + 1 ) ;
    else dict . put ( arr [ i ] , 1 ) ;
  }
  for ( int i = 0 ;
  i < size ;
  i ++ ) {
    if ( ( dict . get ( arr [ i ] ) > 1 ) && ( arr [ i ] > 0 ) ) continue ;
    else KthIndex = KthIndex - 1 ;
    if ( ( KthIndex == 0 ) || ( KthIndex == 1 ) ) return arr [ i ] ;
  }
  return - 1 ;
}
|||

GENERATE_BINARY_PERMUTATIONS_1S_0S_EVERY_POINT_PERMUTATIONS

public static void generate ( int ones , int zeroes , String str , int len1 ) {
  if ( ( len1 == str . length ( ) ) && ( ones > zeroes ) ) {
    System . out . print ( str + " " ) ;
    return ;
  }
  generate ( ones + 1 , zeroes , str + "1" , len1 ) ;
  if ( ( ones > zeroes ) && ( zeroes > ones ) ) {
    generate ( ones , zeroes + 1 , str + "0" , len1 ) ;
  }
}
|||

SEARCH_INSERT_AND_DELETE_IN_AN_UNSORTED_ARRAY

public static int findElement ( int [ ] arr , int n , int key ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( arr [ i ] == key ) && ( arr [ i + 1 ] == key ) ) {
      return i ;
    }
  }
  return - 1 ;
}
|||

LCS_LONGEST_COMMON_SUBSEQUENCE_THREE_STRINGS

public static int lcsOf3 ( int [ ] X , int [ ] Y , int [ ] Z , int m , int n , int o ) {
  int [ ] [ ] L = new int [ o + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i < m + 1 ;
  i ++ ) {
    for ( int j = 0 ;
    j < n + 1 ;
    j ++ ) {
      for ( int k = 0 ;
      k < o + 1 ;
      k ++ ) {
        if ( ( i == 0 || j == 0 || k == 0 ) && ( X [ i - 1 ] == Y [ j - 1 ] && X [ i - 1 ] == Z [ k - 1 ] ) ) {
          L [ i ] [ j ] [ k ] = 0 ;
        }
        else if ( ( X [ i - 1 ] == Y [ j - 1 ] && X [ i - 1 ] == Z [ k - 1 ] ) && ( X [ i ] == Z [ k - 1 ] ) ) {
          L [ i ] [ j ] [ k ] = L [ i - 1 ] [ j - 1 ] [ k - 1 ] + 1 ;
        }
        else {
          L [ i ] [ j ] [ k ] = Math . max ( Math . max ( L [ i - 1 ] [ j ] [ k ] , L [ i ] [ j - 1 ] [ k ] ) , L [ i ] [ j ] [ k - 1 ] ) ;
        }
      }
    }
  }
  return L [ m ] [ n ] [ o ] ;
}
|||

MAXIMUM_SUM_SUBARRAY_REMOVING_ONE_ELEMENT

public static int maxSumSubarrayRemovingOneEle ( int [ ] arr , int n ) {
  int [ ] fw = new int [ n ] ;
  for ( int k = 0 ;
  k < n ;
  k ++ ) {
    fw [ k ] = 0 ;
  }
  int [ ] bw = new int [ n ] ;
  for ( int k = 0 ;
  k < n ;
  k ++ ) {
    int curMax = arr [ 0 ] , maxSoFar = arr [ 0 ] ;
    for ( int i = 1 ;
    i < n ;
    i ++ ) {
      curMax = Math . max ( arr [ i ] , curMax + arr [ i ] ) ;
      maxSoFar = Math . max ( maxSoFar , curMax ) ;
      fw [ i ] = curMax ;
    }
    curMax = maxSoFar = bw [ n - 1 ] = arr [ n - 1 ] ;
    int i = n - 2 ;
    while ( i >= 0 ) {
      curMax = Math . max ( arr [ i ] , curMax + arr [ i ] ) ;
      maxSoFar = Math . max ( maxSoFar , curMax ) ;
      bw [ i ] = curMax ;
      i -- ;
    }
    int fans = maxSoFar ;
    for ( int i = 1 ;
    i < n - 1 ;
    i ++ ) {
      fans = Math . max ( fans , fw [ i - 1 ] + bw [ i + 1 ] ) ;
    }
    return fans ;
  }
  
|||

COUNT_NUMBER_WAYS_TILE_FLOOR_SIZE_N_X_M_USING_1_X_M_SIZE_TILES

public static int countWays ( int n , int m ) {
  int [ ] count = new int [ n + 2 ] ;
  for ( int i = 0 ;
  i < n + 2 ;
  i ++ ) {
    count [ i ] = 0 ;
  }
  count [ 0 ] = 0 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    if ( ( i > m ) && ( i < m ) ) {
      count [ i ] = count [ i - 1 ] + count [ i - m ] ;
    }
    else if ( ( i < m ) && ( i > m ) ) {
      count [ i ] = 1 ;
    }
    else {
      count [ i ] = 2 ;
    }
  }
  return count [ n ] ;
}
|||

MIDDLE_OF_THREE_USING_MINIMUM_COMPARISONS

public static int middleOfThree ( int a , int b , int c ) {
  if ( ( ( a < b && b < c ) || ( c < b && b < a ) ) && ( ( b < a && a < c ) || ( c < a && a < b ) ) && ( ( c < a && c < b ) || ( c < a && a < c ) ) ) return b ;
  ;
  if ( ( ( b < a && a < c ) || ( c < a && a < b ) || ( b < a && b < c ) ) && ( ( c < a && c < b ) || ( c < a && b < c ) ) && ( ( a < b && a < c ) || ( a < b && c < b ) ) && ( ( b < a && b < c ) || ( b < a && c < c ) ) && ( ( c < a && c < b ) || ( c < a && c < b ) ) && ( ( a < b && a < c ) || ( a < c && c < b ) ) && ( ( b < a && b < c ) || ( b < a && c < b ) ) && ( ( c < a && c <
|||

LONGEST_COMMON_INCREASING_SUBSEQUENCE_LCS_LIS

public static int LCIS ( int [ ] arr1 , int n , int [ ] arr2 , int m ) {
  int [ ] table = new int [ m ] ;
  for ( int j = 0 ;
  j < m ;
  j ++ ) table [ j ] = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int current = 0 ;
    for ( int j = 0 ;
    j < m ;
    j ++ ) {
      if ( ( arr1 [ i ] == arr2 [ j ] ) && ( current + 1 > table [ j ] ) ) {
        table [ j ] = current + 1 ;
      }
    }
    if ( ( arr1 [ i ] > arr2 [ j ] ) && ( current + 1 > table [ j ] ) ) {
      if ( ( table [ j ] > current ) && ( current + 1 > table [ j ] ) ) {
        current = table [ j ] ;
      }
    }
  }
  int result = 0 ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) {
    if ( ( table [ i ] > result ) && ( current + 1 > table [ j ] ) ) {
      result = table [ i ] ;
    }
  }
  return result ;
}
|||

MAXIMUM_SUBSEQUENCE_SUM_SUCH_THAT_NO_THREE_ARE_CONSECUTIVE

public static int maxSumWO3Consec ( int [ ] arr , int n ) {
  int [ ] sum = new int [ n ] ;
  for ( int k = 0 ;
  k < n ;
  k ++ ) {
    sum [ k ] = 0 ;
  }
  if ( n >= 1 ) {
    sum [ 0 ] = arr [ 0 ] ;
  }
  if ( n >= 2 ) {
    sum [ 1 ] = arr [ 0 ] + arr [ 1 ] ;
  }
  if ( n > 2 ) {
    sum [ 2 ] = Math . max ( sum [ 1 ] , Math . max ( arr [ 1 ] + arr [ 2 ] , arr [ 0 ] + arr [ 2 ] ) ) ;
  }
  for ( int i = 3 ;
  i < n ;
  i ++ ) {
    sum [ i ] = Math . max ( Math . max ( sum [ i - 1 ] , sum [ i - 2 ] + arr [ i ] ) , arr [ i ] + arr [ i - 1 ] + sum [ i - 3 ] ) ;
  }
  return sum [ n - 1 ] ;
}
|||

EULERIAN_NUMBER_1

public static int eulerian ( int n , int m ) {
  int [ ] [ ] dp = new int [ m + 1 ] [ n + 1 ] ;
  for ( int y = 0 ;
  y < n ;
  y ++ ) {
    dp [ y ] [ y ] = 0 ;
  }
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= m ;
    j ++ ) {
      if ( ( i > j ) && ( j == 0 ) ) {
        if ( ( j == 0 ) || ( ( i - j ) * dp [ i - 1 ] [ j - 1 ] ) + ( ( j + 1 ) * dp [ i - 1 ] [ j ] ) ) {
          dp [ i ] [ j ] = 1 ;
        }
        else {
          dp [ i ] [ j ] = ( ( ( i - j ) * dp [ i - 1 ] [ j ] ) + ( ( j + 1 ) * dp [ i - 1 ] [ j ] ) ) ;
        }
      }
    }
  }
  return dp [ n ] [ m ] ;
}
|||

DOUBLE_FACTORIAL

public static int doublefactorial ( int n ) {
  if ( ( n == 0 || n == 1 ) && ( n > 2 ) ) return 1 ;
  ;
  return n * doublefactorial ( n - 2 ) ;
  ;
}
|||

REARRANGE_POSITIVE_AND_NEGATIVE_NUMBERS_PUBLISH

public static void rearrange ( int [ ] arr , int n ) {
  int i = - 1 ;
  for ( int j = 0 ;
  j < n ;
  j ++ ) {
    if ( ( arr [ j ] < 0 ) && ( arr [ j ] > 0 ) ) {
      i ++ ;
      arr [ i ] = arr [ j ] ;
      arr [ j ] = arr [ i ] ;
    }
  }
  int pos = i + 1 , neg = 0 ;
  while ( ( pos < n && neg < pos && arr [ neg ] < 0 ) || ( neg < n && arr [ pos ] > 0 ) ) {
    arr [ neg ] = arr [ pos ] ;
    pos ++ ;
    neg += 2 ;
  }
}
|||

MAXIMIZE_ARRAY_SUN_AFTER_K_NEGATION_OPERATIONS

public static int maximumSum ( int [ ] arr , int n , int k ) {
  for ( int i = 1 ;
  i <= k ;
  i ++ ) {
    int min = + 2147483647 ;
    int index = - 1 ;
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( ( arr [ j ] < min ) && ( arr [ j ] > max ) ) {
        min = arr [ j ] ;
        index = j ;
      }
    }
    if ( ( min == 0 ) || ( arr [ index ] == 0 ) ) break ;
    arr [ index ] = - arr [ index ] ;
  }
  int sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) sum += arr [ i ] ;
  return sum ;
}
|||

MAXIMUM_SUM_INCREASING_SUBSEQUENCE_FROM_A_PREFIX_AND_A_GIVEN_ELEMENT_AFTER_PREFIX_IS_MUST

public static int preCompute ( int [ ] a , int n , int index , int k ) {
  int [ ] [ ] dp = new int [ n ] [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( a [ i ] > a [ 0 ] ) {
      dp [ 0 ] [ i ] = a [ i ] + a [ 0 ] ;
    }
    else {
      dp [ 0 ] [ i ] = a [ i ] ;
    }
  }
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( a [ j ] > a [ i ] && j > i ) {
        if ( dp [ i - 1 ] [ i ] + a [ j ] > dp [ i - 1 ] [ j ] ) {
          dp [ i ] [ j ] = dp [ i - 1 ] [ i ] + a [ j ] ;
        }
        else {
          dp [ i ] [ j ] = dp [ i - 1 ] [ j ] ;
        }
      }
      else {
        dp [ i ] [ j ] = dp [ i - 1 ] [ j ] ;
      }
    }
  }
  return dp [ index ] [ k ] ;
}
|||

FUNCTION_COPY_STRING_ITERATIVE_RECURSIVE

public static void myCopy ( String s1 , String s2 ) {
  for ( int i = 0 ;
  i < s1 . length ( ) ;
  i ++ ) {
    s2 . charAt ( i ) = s1 . charAt ( i ) ;
    ;
  }
}
|||

GIVEN_TWO_STRINGS_FIND_FIRST_STRING_SUBSEQUENCE_SECOND_1

public static boolean isSubSequence ( String str1 , String str2 , int m , int n ) {
  int j = 0 ;
  int i = 0 ;
  while ( j < m && i < n ) {
    if ( str1 . charAt ( j ) == str2 . charAt ( i ) ) j = j + 1 ;
    i = i + 1 ;
  }
  return j == m ;
}
|||

FIND_UNIT_DIGIT_X_RAISED_POWER_Y_1

public static int unitNumber ( int x , int y ) {
  x = x % 10 ;
  if ( y != 0 ) y = y % 4 + 4 ;
  return ( ( ( int ) ( Math . pow ( x , y ) ) ) % 10 ) ;
}
|||

PROGRAM_NEXT_FIT_ALGORITHM_MEMORY_MANAGEMENT

public static void NextFit ( int [ ] blockSize , int m , int [ ] processSize , int n ) {
  int [ ] allocation = new int [ n ] ;
  allocation [ 0 ] = - 1 ;
  int j = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    while ( j < m ) {
      if ( blockSize [ j ] >= processSize [ i ] ) {
        allocation [ i ] = j ;
        blockSize [ j ] -= processSize [ i ] ;
        break ;
      }
      j = ( j + 1 ) % m ;
    }
  }
  System . out . println ( "Process No.Process Size Block no." ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    System . out . println ( i + "          " + processSize [ i ] + "     " ) ;
    if ( allocation [ i ] != - 1 ) {
      System . out . println ( allocation [ i ] + " " ) ;
    }
    else {
      System . out . println ( "Not Allocated" ) ;
    }
  }
}
|||

NOBLE_INTEGERS_IN_AN_ARRAY_COUNT_OF_GREATER_ELEMENTS_IS_EQUAL_TO_VALUE

public static int nobleInteger ( int [ ] arr , int size ) {
  for ( int i = 0 ;
  i <= size ;
  i ++ ) {
    int count = 0 ;
    for ( int j = 0 ;
    j <= size ;
    j ++ ) {
      if ( ( arr [ i ] < arr [ j ] ) && ( arr [ i ] > arr [ j ] ) ) {
        count ++ ;
      }
    }
    if ( ( count == arr [ i ] ) && ( count > 0 ) ) {
      return arr [ i ] ;
    }
  }
  return - 1 ;
}
|||

MINIMUM_FLIP_REQUIRED_MAKE_BINARY_MATRIX_SYMMETRIC

public static int minimumFlip ( int [ ] [ ] mat , int n ) {
  int [ ] [ ] transpose = new int [ n ] [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      transpose [ i ] [ j ] = mat [ j ] [ i ] ;
    }
  }
  int flip = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( transpose [ i ] [ j ] != mat [ i ] [ j ] ) {
        flip ++ ;
      }
    }
  }
  return ( int ) ( flip / 2 ) ;
}
|||

SEGREGATE_EVEN_ODD_NUMBERS_SET_3

public static void arrayEvenAndOdd ( int [ ] arr , int n ) {
  int i = - 1 ;
  int j = 0 ;
  while ( ( j != n ) && ( arr [ j ] % 2 == 0 ) ) {
    if ( ( arr [ j ] % 2 == 0 ) && ( arr [ i ] == 0 ) ) {
      i = i + 1 ;
      arr [ i ] = arr [ j ] ;
      arr [ j ] = arr [ i ] ;
    }
    j = j + 1 ;
  }
  for ( i = 0 ;
  i < arr . length ;
  i ++ ) {
    System . out . print ( Integer . toString ( arr [ i ] ) + " " ) ;
  }
}
|||

DFS_N_ARY_TREE_ACYCLIC_GRAPH_REPRESENTED_ADJACENCY_LIST

public static void dfs ( int [ ] [ ] List , int node , int arrival ) {
  System . out . println ( node ) ;
  for ( int i = 0 ;
  i < List [ node ] . length ;
  i ++ ) {
    if ( ( List [ node ] [ i ] != arrival ) && ( List [ node ] [ i ] != arrival ) ) {
      dfs ( List , List [ node ] [ i ] , node ) ;
    }
  }
}
|||

HOW_TO_TURN_OFF_A_PARTICULAR_BIT_IN_A_NUMBER

static int turnOffK ( int n , int k ) {
  if ( ( k <= 0 ) || ( k > 1 ) ) return n ;
  return ( n & ~ ( 1 << ( k - 1 ) ) ) ;
}
|||

NUMBER_SUBSTRINGS_DIVISIBLE_8_NOT_3

public static int count ( String s , int Len ) {
  MAX = Integer . MAX_VALUE ;
  int cur = 0 ;
  int dig ;
  int [ ] Sum = new int [ MAX ] ;
  int [ ] [ ] dp = new int [ MAX ] [ 2 ] ;
  dp [ 0 ] [ 0 ] = 1 ;
  for ( int i = 1 ;
  i <= Len ;
  i ++ ) {
    dig = Integer . parseInt ( s . charAt ( i - 1 ) ) - 48 ;
    cur += dig ;
    cur %= 3 ;
    Sum [ i ] = cur ;
    dp [ i ] [ 0 ] = dp [ i - 1 ] [ 0 ] ;
    dp [ i ] [ 1 ] = dp [ i - 1 ] [ 1 ] ;
    dp [ i ] [ 2 ] = dp [ i - 1 ] [ 2 ] ;
    dp [ i ] [ Sum [ i ] ] ++ ;
  }
  int ans = 0 ;
  int dprev = 0 ;
  int value ;
  int dprev2 = 0 ;
  for ( int i = 1 ;
  i <= Len ;
  i ++ ) {
    dig = Integer . parseInt ( s . charAt ( i - 1 ) ) - 48 ;
    if ( dig == 8 ) ans ++ ;
    if ( i - 2 >= 0 ) {
      dprev = Integer . parseInt ( s . charAt ( i - 2 ) ) - 48 ;
      value = dprev * 10 + dig ;
      if ( ( value % 8 == 0 ) && ( value % 3 != 0 ) ) ans ++ ;
    }
    if ( i - 3 >= 0 ) {
      dprev2 = Integer . parseInt ( s . charAt ( i - 3 ) ) - 48 ;
      dprev = Integer . parseInt ( s . charAt ( i - 2 ) ) - 48 ;
      value = ( dprev2 * 100 + dprev * 10 + dig ) ;
      if ( value % 8 != 0 ) continue ;
      ans += ( i - 2 ) ;
      ans -= ( dp [ i - 3 ] [ Sum [ i ] ] ) ;
    }
  }
  return ans ;
}
|||

ADD_1_TO_A_GIVEN_NUMBER_1

public static int addOne ( int x ) {
  return ( - ( ~ x ) ) ;
  ;
}
|||

CHECK_STRING_FOLLOWS_ANBN_PATTERN_NOT

public static boolean isAnBn ( String str ) {
  int n = str . length ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( str . charAt ( i ) != 'a' ) && ( str . charAt ( i ) != 'b' ) ) {
      break ;
    }
  }
  if ( ( i * 2 != n ) && ( i * 2 != n ) ) {
    return false ;
  }
  for ( int j = i ;
  j < n ;
  j ++ ) {
    if ( ( str . charAt ( j ) != 'b' ) && ( str . charAt ( j ) != 'a' ) ) {
      return false ;
    }
  }
  return true ;
}
|||

FIND_FIRST_REPEATING_ELEMENT_ARRAY_INTEGERS

public static void printFirstRepeating ( int [ ] arr , int n ) {
  int Min = - 1 ;
  Map < Integer , Integer > myset = Collections . emptyMap ( ) ;
  for ( int i = n - 1 ;
  i >= 0 ;
  i -- ) {
    if ( arr [ i ] < myset . keySet ( ) . size ( ) ) {
      Min = i ;
    }
    else {
      myset . put ( arr [ i ] , 1 ) ;
    }
  }
  if ( ( Min != - 1 ) && ( arr [ Min ] > 0 ) ) {
    System . out . println ( "The first repeating element is" + arr [ Min ] ) ;
  }
  else {
    System . out . println ( "There are no repeating elements" ) ;
  }
}
|||

COST_BALANCE_PARANTHESES

public static int costToBalance ( String s ) {
  if ( ( s . length ( ) == 0 ) || ( s . length ( ) > 1 ) ) System . out . println ( 0 ) ;
  int ans = 0 ;
  int o = 0 ;
  int c = 0 ;
  for ( int i = 0 ;
  i < s . length ( ) ;
  i ++ ) {
    if ( ( s . charAt ( i ) == '(' ) ) o ++ ;
    if ( ( s . charAt ( i ) == ')' ) ) c ++ ;
  }
  if ( ( o != c ) && ( o != 0 ) ) return - 1 ;
  int [ ] a = new int [ s . length ( ) ] ;
  for ( int i = 0 ;
  i < s . length ( ) ;
  i ++ ) {
    if ( ( s . charAt ( i ) == '(' ) ) a [ 0 ] = 1 ;
    else a [ 0 ] = - 1 ;
    if ( ( a [ 0 ] < 0 ) && ( a [ 0 ] > 0 ) ) ans += Math . abs ( a [ 0 ] ) ;
    for ( int i = 1 ;
    i < s . length ( ) ;
    i ++ ) {
      if ( ( s . charAt ( i ) == '(' ) ) a [ i ] = a [ i - 1 ] + 1 ;
      else a [ i ] = a [ i - 1 ] - 1 ;
      if ( ( a [ i ] < 0 ) && ( a [ i ] > 0 ) ) ans += Math . abs ( a [ i ] ) ;
    }
  }
  return ans ;
}
|||

COIN_GAME_WINNER_EVERY_PLAYER_THREE_CHOICES

public static boolean findWinner ( int x , int y , int n ) {
  boolean [ ] dp = new boolean [ n + 1 ] ;
  dp [ 0 ] = false ;
  dp [ 1 ] = true ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    if ( ( i - 1 >= 0 && ! dp [ i - 1 ] ) || ( i - x >= 0 && ! dp [ i - x ] ) ) {
      dp [ i ] = true ;
    }
    else if ( ( i - y >= 0 && ! dp [ i - y ] ) || ( i - x >= 0 && ! dp [ i - x ] ) ) {
      dp [ i ] = true ;
    }
    else if ( ( i - z >= 0 && ! dp [ i - z ] ) || ( i - y >= 0 && ! dp [ i - y ] ) ) {
      dp [ i ] = true ;
    }
    else {
      dp [ i ] = false ;
    }
  }
  return dp [ n ] ;
}
|||

SEQUENCES_GIVEN_LENGTH_EVERY_ELEMENT_EQUAL_TWICE_PREVIOUS

public static int getTotalNumberOfSequences ( int m , int n ) {
  if ( m < n ) return 0 ;
  if ( n == 0 ) return 1 ;
  int res = ( getTotalNumberOfSequences ( m - 1 , n ) + getTotalNumberOfSequences ( m / 2 , n - 1 ) ) ;
  return res ;
}
|||

FIND_DUPLICATES_GIVEN_ARRAY_ELEMENTS_NOT_LIMITED_RANGE

public static void printDuplicates ( String [ ] arr ) {
  HashMap < String , Integer > map = new HashMap < String , Integer > ( ) ;
  for ( String ele : arr ) {
    try {
      map . put ( ele , 1 ) ;
    }
    catch ( Exception e ) {
      map . put ( ele , 1 ) ;
    }
  }
  for ( String item : map . keySet ( ) ) {
    if ( ( map . get ( item ) > 1 ) && ( map . get ( item ) < ( arr . length - 1 ) ) ) {
      System . out . print ( item + " " ) ;
    }
  }
  System . out . println ( "\n" ) ;
}
|||

LONGEST_REPEATING_SUBSEQUENCE_1

public static int findLongestRepeatingSubSeq ( int [ ] X , int m , int n ) {
  if ( ( dp [ m ] [ n ] != - 1 ) && ( dp [ m ] [ n ] != - 1 ) ) return dp [ m ] [ n ] ;
  if ( ( m == 0 || n == 0 ) && ( X [ m - 1 ] == X [ n - 1 ] && m != n ) ) {
    dp [ m ] [ n ] = 0 ;
    return dp [ m ] [ n ] ;
  }
  if ( ( X [ m - 1 ] == X [ n - 1 ] && m != n ) && ( X [ m ] == X [ n - 1 ] && m != n ) ) {
    dp [ m ] [ n ] = findLongestRepeatingSubSeq ( X , m - 1 , n - 1 ) + 1 ;
    return dp [ m ] [ n ] ;
  }
  dp [ m ] [ n ] = Math . max ( findLongestRepeatingSubSeq ( X , m , n - 1 ) , findLongestRepeatingSubSeq ( X , m - 1 , n ) ) ;
  return dp [ m ] [ n ] ;
}
|||

COUNT_OF_N_DIGIT_NUMBERS_WHOSE_SUM_OF_DIGITS_EQUALS_TO_GIVEN_SUM

public static int findCount ( int n , int sum ) {
  int start = Math . pow ( 10 , n - 1 ) ;
  ;
  int end = Math . pow ( 10 , n ) - 1 ;
  int count = 0 ;
  int i = start ;
  while ( ( i <= end ) && ( i != 0 ) ) {
    int cur = 0 ;
    int temp = i ;
    while ( ( temp != 0 ) && ( temp != sum ) ) {
      cur += temp % 10 ;
      temp = temp / 10 ;
    }
    if ( ( cur == sum ) && ( i == 9 ) ) {
      count = count + 1 ;
      i += 9 ;
    }
    else {
      i = i + 1 ;
    }
  }
  System . out . println ( count ) ;
  return count ;
}
|||

MINIMUM_COST_CONNECT_WEIGHTED_NODES_REPRESENTED_ARRAY

public static long minimumCost ( long [ ] a , int n ) {
  long mn = Long . MAX_VALUE ;
  long sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    mn = Math . min ( a [ i ] , mn ) ;
    sum += a [ i ] ;
  }
  return mn * ( sum - mn ) ;
}
|||

FIND_ALL_DIVISORS_OF_A_NATURAL_NUMBER_SET_2

public static void printDivisors ( int n ) {
  List < Integer > list = new ArrayList < Integer > ( ) ;
  for ( int i = 1 ;
  i <= Integer . MAX_VALUE ;
  i ++ ) {
    if ( ( n % i == 0 ) && ( n / i == i ) ) {
      if ( ( n / i == i ) && ( n % i == 0 ) ) {
        System . out . print ( i + " " ) ;
      }
      else {
        System . out . print ( i + " " ) ;
        list . add ( Integer . valueOf ( n / i ) ) ;
      }
    }
  }
  for ( int i : list . subList ( 0 , list . size ( ) - 1 ) ) {
    System . out . print ( i + " " ) ;
  }
}
|||

SQUARES_OF_MATRIX_DIAGONAL_ELEMENTS_1

public static void diagonalSquare ( int [ ] [ ] mat , int row , int column ) {
  System . out . print ( "Diagonal one : " ) ;
  for ( int i = 0 ;
  i <= row ;
  i ++ ) {
    System . out . print ( mat [ i ] [ i ] * mat [ i ] [ i ] ) ;
  }
  System . out . print ( "\n\nDiagonal two : " ) ;
  for ( int i = 0 ;
  i <= row ;
  i ++ ) {
    System . out . print ( mat [ i ] [ row - i - 1 ] * mat [ i ] [ row - i - 1 ] ) ;
  }
}
|||

C_PROGRAM_FIND_AREA_TRIANGLE_1

public static double polygonArea ( double [ ] X , double [ ] Y , int n ) {
  double area = 0.0 ;
  int j = n - 1 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    area = area + ( X [ j ] + X [ i ] ) * ( Y [ j ] - Y [ i ] ) ;
    j = i ;
  }
  return Math . abs ( area / 2.0 ) ;
}
|||

RANGE_QUERIES_FOR_FREQUENCIES_OF_ARRAY_ELEMENTS

public static int findFrequency ( int [ ] arr , int n , int left , int right , int element ) {
  int count = 0 ;
  for ( int i = left - 1 ;
  i < right ;
  i ++ ) {
    if ( ( arr [ i ] == element ) && ( arr [ i + 1 ] == element ) ) {
      count ++ ;
    }
  }
  return count ;
}
|||

SERIES_LARGEST_GCD_SUM_EQUALS_N

public static void printSequence ( int n , int k ) {
  int b = ( int ) ( n / ( k * ( k + 1 ) / 2 ) ) ;
  ;
  if ( b == 0 ) System . out . println ( "-1" ) ;
  else {
    int r = 1 ;
    ;
    int x = 1 ;
    while ( x * x <= n ) {
      if ( n % x != 0 ) continue ;
      ;
      else if ( x <= b && x > r ) r = x ;
      else if ( n / x <= b && n / x > r ) r = n / x ;
      x = x + 1 ;
    }
    int i = 1 ;
    while ( i < k ) {
      System . out . print ( r * i + " " ) ;
      i = i + 1 ;
    }
    int lastTerm = n - ( r * ( k * ( k - 1 ) / 2 ) ) ;
    System . out . println ( lastTerm ) ;
  }
}
|||

FIND_THREE_ELEMENT_FROM_DIFFERENT_THREE_ARRAYS_SUCH_THAT_THAT_A_B_C_K_1

public static boolean findTriplet ( int [ ] a1 , int [ ] a2 , int [ ] a3 , int n1 , int n2 , int n3 , int sum ) {
  Set < Integer > s = new HashSet < Integer > ( ) ;
  for ( int i = 0 ;
  i < n1 ;
  i ++ ) {
    s . add ( a1 [ i ] ) ;
  }
  for ( int i = 0 ;
  i < n2 ;
  i ++ ) {
    for ( int j = 0 ;
    j < n3 ;
    j ++ ) {
      if ( sum - a2 [ i ] - a3 [ j ] == s . size ( ) ) {
        return true ;
      }
    }
  }
  return false ;
}
|||

FIND_THE_MAXIMUM_ELEMENT_IN_AN_ARRAY_WHICH_IS_FIRST_INCREASING_AND_THEN_DECREASING_1

public static int findMaximum ( int [ ] arr , int low , int high ) {
  if ( low == high ) return arr [ low ] ;
  if ( high == low + 1 && arr [ low ] >= arr [ high ] ) return arr [ low ] ;
  ;
  if ( high == low + 1 && arr [ low ] < arr [ high ] ) return arr [ high ] ;
  int mid = ( low + high ) / 2 ;
  if ( arr [ mid ] > arr [ mid + 1 ] && arr [ mid ] > arr [ mid - 1 ] ) return arr [ mid ] ;
  if ( arr [ mid ] > arr [ mid + 1 ] && arr [ mid ] < arr [ mid - 1 ] ) return findMaximum ( arr , low , mid - 1 ) ;
  else return findMaximum ( arr , mid + 1 , high ) ;
}
|||

DYNAMIC_PROGRAMMING_SET_1

static int fib ( int n , int [ ] lookup ) {
  if ( n == 0 || n == 1 ) lookup [ n ] = n ;
  if ( lookup [ n ] == 0 ) lookup [ n ] = fib ( n - 1 , lookup ) + fib ( n - 2 , lookup ) ;
  return lookup [ n ] ;
}
|||

MODULAR_EXPONENTIATION_POWER_IN_MODULAR_ARITHMETIC

public static int power ( int x , int y , int p ) {
  int res = 1 ;
  x = x % p ;
  while ( ( y > 0 ) && ( ( y & 1 ) == 1 ) ) {
    if ( ( ( y & 1 ) == 0 ) || ( ( y & 1 ) == 1 ) ) {
      res = ( res * x ) % p ;
    }
    y = y >> 1 ;
    x = ( x * x ) % p ;
  }
  return res ;
}
|||

WRITE_ONE_LINE_C_FUNCTION_TO_FIND_WHETHER_A_NO_IS_POWER_OF_TWO_1

public static boolean isPowerOfTwo ( int x ) {
  return ( x > 0 && ( ! ( x & ( x - 1 ) ) ) ) ;
}
|||

LONGEST_COMMON_SUBSEQUENCE_WITH_PERMUTATIONS_ALLOWED

public static void longestString ( String str1 , String str2 ) {
  int count1 [ 26 ] = {
    0 };
    int count2 [ 26 ] = {
      0 };
      for ( int i = 0 ;
      i < str1 . length ( ) ;
      i ++ ) count1 [ ( char ) str1 . charAt ( i ) - 'a' ] ++ ;
      for ( int i = 0 ;
      i < str2 . length ( ) ;
      i ++ ) count2 [ ( char ) str2 . charAt ( i ) - 'a' ] ++ ;
      String result = "" ;
      for ( int i = 0 ;
      i < 26 ;
      i ++ ) {
        for ( int j = 1 ;
        j <= Math . min ( count1 [ i ] , count2 [ i ] ) + 1 ;
        j ++ ) result = result + ( char ) ( 'a' + i ) ;
      }
      System . out . println ( result ) ;
    }
    
|||

DIFFERENCE_MAXIMUM_SUM_MINIMUM_SUM_N_M_ELEMENTSIN_REVIEW

public static int findDifference ( int [ ] arr , int n , int m ) {
  int max = 0 ;
  int min = 0 ;
  Arrays . sort ( arr ) ;
  ;
  int j = n - 1 ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) {
    min += arr [ i ] ;
    max += arr [ j ] ;
    j = j - 1 ;
  }
  return ( max - min ) ;
}
|||

PRINT_NUMBER_ASCENDING_ORDER_CONTAINS_1_2_3_DIGITS

public static List < String > printNumbers ( List < String > numbers ) {
  numbers = CollectionUtils . toCollection ( numbers ) ;
  List < String > result = new ArrayList < String > ( ) ;
  for ( String num : numbers ) {
    if ( ( "1" . equals ( num ) && "2" . equals ( num ) && "3" . equals ( num ) ) || ( "0" . equals ( num ) && "1" . equals ( num ) && "2" . equals ( num ) ) || ( "0" . equals ( num ) && "0" . equals ( num ) && "1" . equals ( num ) ) ) {
      result . add ( num ) ;
    }
  }
  if ( result . isEmpty ( ) ) {
    result . add ( "-1" ) ;
  }
  return Collections . unmodifiableList ( result ) ;
  ;
}
|||

DYNAMIC_PROGRAMMING_SET_3_LONGEST_INCREASING_SUBSEQUENCE

public static int lis ( int [ ] arr ) {
  maximum = 0 ;
  int n = arr . length ;
  maximum = 1 ;
  _lis ( arr , n ) ;
  return maximum ;
}
|||

MINIMUM_REVOLUTIONS_MOVE_CENTER_CIRCLE_TARGET

public static double minRevolutions ( double r , double x1 , double y1 , double x2 , double y2 ) {
  double d = Math . sqrt ( ( x1 - x2 ) * ( x1 - x2 ) + ( y1 - y2 ) * ( y1 - y2 ) ) ;
  return Math . ceil ( d / ( 2 * r ) ) ;
}
|||

CHECK_TWO_GIVEN_SETS_DISJOINT

public static boolean areDisjoint ( int [ ] set1 , int [ ] set2 , int m , int n ) {
  for ( int i = 0 ;
  i <= m ;
  i ++ ) {
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      if ( ( set1 [ i ] == set2 [ j ] ) && ( set1 [ i ] != set2 [ j ] ) ) {
        return false ;
      }
    }
  }
  return true ;
}
|||

FIND_MINIMUM_SUM_FACTORS_NUMBER

public static int findMinSum ( int num ) {
  int sum = 0 ;
  int i = 2 ;
  while ( ( i * i <= num ) && ( num % i == 0 ) ) {
    while ( ( num % i == 0 ) && ( num % i == 0 ) ) {
      sum += i ;
      num /= i ;
    }
    i ++ ;
  }
  sum += num ;
  return sum ;
}
|||

FREQUENT_ELEMENT_ARRAY

public static int mostFrequent ( int [ ] arr , int n ) {
  Arrays . sort ( arr ) ;
  int maxCount = 1 ;
  int res = arr [ 0 ] ;
  int currCount = 1 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( ( arr [ i ] == arr [ i - 1 ] ) && ( arr [ i ] > 0 ) ) {
      currCount ++ ;
    }
    else {
      if ( ( currCount > maxCount ) && ( currCount < maxCount ) ) {
        maxCount = currCount ;
        res = arr [ i - 1 ] ;
      }
      currCount = 1 ;
    }
  }
  if ( ( currCount > maxCount ) && ( currCount < maxCount ) ) {
    maxCount = currCount ;
    res = arr [ n - 1 ] ;
  }
  return res ;
}
|||

MINIMUM_XOR_VALUE_PAIR_1

public static int minXOR ( int [ ] arr , int n ) {
  Arrays . sort ( arr ) ;
  int minXor = Integer . MAX_VALUE ;
  int val ;
  for ( int i = 0 ;
  i <= n - 1 ;
  i ++ ) {
    val = arr [ i ] ^ arr [ i + 1 ] ;
    ;
    minXor = Math . min ( minXor , val ) ;
    ;
  }
  return minXor ;
}
|||

MINIMUM_SUM_PRODUCT_TWO_ARRAYS

public static double minproduct ( double [ ] a , double [ ] b , int n , double k ) {
  double diff = 0 ;
  double res = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    double pro = a [ i ] * b [ i ] ;
    res = res + pro ;
    if ( ( pro < 0 && b [ i ] < 0 ) || ( pro > 0 && a [ i ] < 0 ) ) {
      double temp = ( a [ i ] + 2 * k ) * b [ i ] ;
      if ( ( pro < 0 && b [ i ] < 0 ) || ( pro > 0 && a [ i ] < 0 ) ) {
        temp = ( a [ i ] - 2 * k ) * b [ i ] ;
      }
      else if ( ( pro > 0 && a [ i ] < 0 ) || ( pro > 0 && b [ i ] > 0 ) ) {
        temp = ( a [ i ] + 2 * k ) * b [ i ] ;
      }
      else if ( ( pro > 0 && a [ i ] > 0 ) || ( pro < 0 && b [ i ] > 0 ) ) {
        temp = ( a [ i ] - 2 * k ) * b [ i ] ;
      }
      double d = Math . abs ( pro - temp ) ;
      if ( ( d > diff ) || ( d < 0 ) ) {
        diff = d ;
      }
    }
  }
  return res - diff ;
}
|||

FAST_MULTIPLICATION_METHOD_WITHOUT_USING_MULTIPLICATION_OPERATOR_RUSSIAN_PEASANTS_ALGORITHM

public static int russianPeasant ( int a , int b ) {
  int res = 0 ;
  while ( ( b > 0 ) && ( b < 1 ) ) {
    if ( ( b & 1 ) != 0 ) {
      res = res + a ;
    }
    a = a << 1 ;
    b = b >> 1 ;
  }
  return res ;
}
|||

DIVISIBILITY_9_USING_BITWISE_OPERATORS

public static boolean isDivBy9 ( int n ) {
  if ( ( n == 0 || n == 9 ) && ( n % 9 == 0 ) ) return true ;
  if ( ( n < 9 ) && ( n % 9 == 0 ) ) return false ;
  return isDivBy9 ( ( int ) ( n >>> 3 ) - ( int ) ( n & 7 ) ) ;
}
|||

CHECK_ARRAY_REPRESENTS_INORDER_BINARY_SEARCH_TREE_NOT

public static boolean isInorder ( int [ ] arr , int n ) {
  if ( ( n == 0 || n == 1 ) && ( arr [ 0 ] > arr [ 1 ] ) ) return true ;
  for ( int i = 1 ;
  i < n ;
  i += 1 ) {
    if ( ( arr [ i - 1 ] > arr [ i ] ) && ( arr [ i ] > arr [ i + 1 ] ) ) return false ;
  }
  return true ;
}
|||

GIVEN_TWO_UNSORTED_ARRAYS_FIND_PAIRS_WHOSE_SUM_X

public static void findPairs ( int arr1 [ ] , int arr2 [ ] , int n , int m , int x ) {
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= m ;
    j ++ ) {
      if ( ( arr1 [ i ] + arr2 [ j ] == x ) && ( arr1 [ i ] + arr2 [ j ] == x ) ) {
        System . out . println ( arr1 [ i ] + " " + arr2 [ j ] ) ;
      }
    }
  }
}
|||

BINARY_REPRESENTATION_OF_NEXT_NUMBER

public static String nextGreater ( String num1 ) {
  int l = num1 . length ( ) ;
  ;
  StringBuilder num = new StringBuilder ( num1 ) ;
  ;
  int i = l - 1 ;
  ;
  while ( ( i >= 0 ) && ( num . charAt ( i ) == '0' ) ) {
    if ( ( num . charAt ( i ) == '1' ) || ( num . charAt ( i ) == '2' ) ) {
      num . setCharAt ( i , '1' ) ;
      break ;
    }
    else {
      num . setCharAt ( i , '0' ) ;
    }
    i -- ;
  }
  num1 = num . toString ( ) ;
  ;
  if ( ( i < 0 ) && ( num1 . charAt ( i ) == '1' ) ) {
    num1 = "1" + num1 ;
  }
  return num1 ;
}
|||

LARGEST_SUBARRAY_WITH_EQUAL_NUMBER_OF_0S_AND_1S

public static int findSubArray ( int [ ] arr , int n ) {
  int sum = 0 ;
  int maxsize = - 1 ;
  for ( int i = 0 ;
  i <= n - 1 ;
  i ++ ) {
    sum = - 1 == ( arr [ i ] == 0 ) ? 1 : 0 ;
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      sum = sum + ( - 1 == ( arr [ j ] == 0 ) ? 1 : 0 ) + 1 ;
      if ( ( sum == 0 ) && ( maxsize < j - i + 1 ) ) {
        maxsize = j - i + 1 ;
        startindex = i ;
      }
    }
  }
  if ( ( maxsize == - 1 ) || ( ( ( ( int ) arr [ startindex ] ) & 0xff ) == 0 ) ) {
    System . out . println ( "No such subarray" ) ;
    ;
  }
  else {
    System . out . println ( startindex + " to" + startindex + maxsize - 1 ) ;
    ;
  }
  return maxsize ;
}
|||

COUNT_PAIRS_WHOSE_PRODUCTS_EXIST_IN_ARRAY_1

public static int countPairs ( int [ ] arr , int n ) {
  int result = 0 ;
  HashSet < Integer > Hash = new HashSet < Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) Hash . add ( arr [ i ] ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      int product = arr [ i ] * arr [ j ] ;
      if ( product == ( Hash . size ( ) - 1 ) ) result ++ ;
    }
  }
  return result ;
}
|||

DYNAMIC_PROGRAMMING_SET_12_LONGEST_PALINDROMIC_SUBSEQUENCE

public static int lps ( String str ) {
  int n = str . length ( ) ;
  int [ ] [ ] L = new int [ n ] [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    L [ i ] [ i ] = 0 ;
  }
  for ( int cl = 2 ;
  cl <= n ;
  cl ++ ) {
    for ( int i = 0 ;
    i < n - cl + 1 ;
    i ++ ) {
      int j = i + cl - 1 ;
      if ( str . charAt ( i ) == str . charAt ( j ) && cl == 2 ) {
        L [ i ] [ j ] = 2 ;
      }
      else if ( str . charAt ( i ) == str . charAt ( j ) ) {
        L [ i ] [ j ] = L [ i + 1 ] [ j - 1 ] + 2 ;
      }
      else {
        L [ i ] [ j ] = Math . max ( L [ i ] [ j - 1 ] , L [ i + 1 ] [ j ] ) ;
        ;
      }
    }
  }
  return L [ 0 ] [ n - 1 ] ;
}
|||

COUNT_INVERSIONS_OF_SIZE_THREE_IN_A_GIVE_ARRAY_1

public static int getInvCount ( int [ ] arr , int n ) {
  int invcount = 0 ;
  for ( int i = 1 ;
  i < n - 1 ;
  i ++ ) {
    int small = 0 ;
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      if ( ( arr [ i ] > arr [ j ] ) && ( arr [ j ] < arr [ i ] ) ) small ++ ;
    }
    int great = 0 ;
    ;
    for ( int j = i - 1 ;
    j >= 0 ;
    j -- ) {
      if ( ( arr [ i ] < arr [ j ] ) && ( arr [ j ] < arr [ i ] ) ) great ++ ;
    }
    invcount += great * small ;
  }
  return invcount ;
}
|||

DECIMAL_REPRESENTATION_GIVEN_BINARY_STRING_DIVISIBLE_10_NOT

public static boolean isDivisibleBy10 ( String bin ) {
  int n = bin . length ( ) ;
  if ( ( bin . charAt ( n - 1 ) == '1' ) || ( bin . charAt ( n - 2 ) == '1' ) || ( bin . charAt ( n - 3 ) == '1' ) ) {
    return false ;
  }
  int sum = 0 ;
  int i = n - 2 ;
  while ( i >= 0 ) {
    if ( ( bin . charAt ( i ) == '1' ) || ( bin . charAt ( i ) == '2' ) ) {
      int posFromRight = n - i - 1 ;
      if ( ( posFromRight % 4 == 1 ) && ( ( posFromRight % 4 == 2 ) || ( posFromRight % 4 == 3 ) ) ) {
        sum = sum + 2 ;
      }
      else if ( ( posFromRight % 4 == 2 ) && ( ( posFromRight % 4 == 3 ) || ( posFromRight % 4 == 0 ) ) ) {
        sum = sum + 4 ;
      }
      else if ( ( posFromRight % 4 == 3 ) && ( ( posFromRight % 4 == 0 ) || ( posFromRight % 4 == 1 ) ) ) {
        sum = sum + 8 ;
      }
      else if ( ( posFromRight % 4 == 0 ) && ( ( posFromRight % 4 == 1 ) || ( posFromRight % 4 == 2 ) ) ) {
        sum = sum + 6 ;
      }
    }
    i = i - 1 ;
  }
  if ( ( sum % 10 == 0 ) && ( sum % 10 == 1 ) ) {
    return true ;
  }
  return false ;
}
|||

FIND_WHETHER_AN_ARRAY_IS_SUBSET_OF_ANOTHER_ARRAY_SET_1_1

public static boolean isSubset ( int [ ] arr1 , int [ ] arr2 , int m , int n ) {
  int i = 0 ;
  int j = 0 ;
  if ( m < n ) return 0 ;
  Arrays . sort ( arr1 ) ;
  Arrays . sort ( arr2 ) ;
  while ( i < n && j < m ) {
    if ( arr1 [ j ] < arr2 [ i ] ) j ++ ;
    else if ( arr1 [ j ] == arr2 [ i ] ) {
      j ++ ;
      i ++ ;
    }
    else if ( arr1 [ j ] > arr2 [ i ] ) return 0 ;
  }
  return false ? i < n : true ;
}
|||

DYNAMIC_PROGRAMMING_SUBSET_SUM_PROBLEM_1

public static boolean isSubsetSum ( int [ ] set , int n , int sum ) {
  boolean [ ] [ ] subset = ( new boolean [ sum + 1 ] [ n + 1 ] ) ;
  for ( int i = 0 ;
  i < n + 1 ;
  i ++ ) {
    subset [ i ] [ 0 ] = true ;
    for ( int i = 1 ;
    i < sum ;
    i ++ ) {
      subset [ 0 ] [ i ] = false ;
    }
    for ( int i = 1 ;
    i < n ;
    i ++ ) {
      for ( int j = 1 ;
      j < sum ;
      j ++ ) {
        if ( j < set [ i - 1 ] ) {
          subset [ i ] [ j ] = subset [ i - 1 ] [ j ] ;
        }
        if ( j >= set [ i - 1 ] ) {
          subset [ i ] [ j ] = ( subset [ i - 1 ] [ j ] || subset [ i - 1 ] [ j - set [ i - 1 ] ] ) ;
        }
      }
    }
  }
  return subset [ n ] [ sum ] ;
}
|||

SUM_K_TH_GROUP_ODD_POSITIVE_NUMBERS_1

public static double kthGroupSum ( double k ) {
  return k * k * k ;
}
|||

THIRD_LARGEST_ELEMENT_ARRAY_DISTINCT_ELEMENTS

public static void thirdLargest ( int arr [ ] , int arrSize ) {
  if ( ( arrSize < 3 ) || ( arr [ 0 ] > arr [ 1 ] ) || ( arr [ 1 ] > arr [ 2 ] ) ) {
    System . out . println ( " Invalid Input " ) ;
    return ;
  }
  int first = arr [ 0 ] ;
  for ( int i = 1 ;
  i < arrSize ;
  i ++ ) {
    if ( ( arr [ i ] > first ) && ( arr [ i ] < first ) ) {
      first = arr [ i ] ;
    }
  }
  int second = - Integer . MAX_VALUE ;
  for ( int i = 0 ;
  i < arrSize ;
  i ++ ) {
    if ( ( arr [ i ] > second && arr [ i ] < first ) && ( arr [ i ] > second ) ) {
      second = arr [ i ] ;
    }
  }
  int third = - Integer . MAX_VALUE ;
  for ( int i = 0 ;
  i < arrSize ;
  i ++ ) {
    if ( ( arr [ i ] > third && arr [ i ] < second ) && ( arr [ i ] > third ) && ( arr [ i ] > third ) ) {
      third = arr [ i ] ;
    }
  }
  System . out . println ( "The Third Largest" + "element is" + third ) ;
}
|||

FIND_SUM_NODES_GIVEN_PERFECT_BINARY_TREE_1

public static int sumNodes ( int l ) {
  double leafNodeCount = Math . pow ( 2 , l - 1 ) ;
  ;
  double sumLastLevel ;
  sumLastLevel = ( ( leafNodeCount * ( leafNodeCount + 1 ) ) / 2 ) ;
  double sum = sumLastLevel * l ;
  return ( int ) sum ;
}
|||

MIDDLE_OF_THREE_USING_MINIMUM_COMPARISONS_2

public static int middleOfThree ( int a , int b , int c ) {
  int x = a - b ;
  int y = b - c ;
  int z = a - c ;
  if ( x * y > 0 ) {
    return b ;
  }
  else if ( ( x * z > 0 ) && ( y * z > 0 ) ) {
    return a ;
  }
  else {
    return a ;
  }
}
|||

MAXIMUM_TRIPLET_SUM_ARRAY_2

public static int maxTripletSum ( int [ ] arr , int n ) {
  int maxA = - 100000000 ;
  int maxB = - 100000000 ;
  int maxC = - 100000000 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( arr [ i ] > maxA ) && ( arr [ i ] < maxB ) ) {
      maxC = maxB ;
      maxB = maxA ;
      maxA = arr [ i ] ;
    }
    else if ( ( arr [ i ] > maxB ) && ( arr [ i ] < maxC ) ) {
      maxC = maxB ;
      maxB = arr [ i ] ;
    }
    else if ( ( arr [ i ] > maxC ) && ( arr [ i ] < maxC ) ) {
      maxC = arr [ i ] ;
    }
  }
  return ( maxA + maxB + maxC ) ;
}
|||

COUNT_PAIRS_TWO_SORTED_ARRAYS_WHOSE_SUM_EQUAL_GIVEN_VALUE_X_1

public static int countPairs ( int arr1 [ ] , int arr2 [ ] , int m , int n , int x ) {
  int count = 0 ;
  HashSet < Integer > us = new HashSet < Integer > ( ) ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) us . add ( arr1 [ i ] ) ;
  for ( int j = 0 ;
  j < n ;
  j ++ ) if ( x - arr2 [ j ] == us . size ( ) ) count ++ ;
  return count ;
}
|||

MINIMUM_STEPS_REACH_END_ARRAY_CONSTRAINTS

public static int getMinStepToReachEnd ( int [ ] arr , int N ) {
  boolean [ ] visit = new boolean [ N ] ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) visit [ i ] = false ;
  int [ ] distance = new int [ N ] ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) digit [ arr [ i ] ] . add ( i ) ;
  distance [ 0 ] = 0 ;
  visit [ 0 ] = true ;
  LinkedList < Integer > q = new LinkedList < Integer > ( ) ;
  q . add ( 0 ) ;
  while ( ( q . size ( ) > 0 ) && ( visit [ 0 ] == false ) ) {
    int idx = q . getFirst ( ) ;
    q . remove ( q . getFirst ( ) ) ;
    if ( ( idx == N - 1 ) || ( idx == N - 2 ) ) break ;
    int d = arr [ idx ] ;
    for ( int i = 0 ;
    i < digit [ d ] . length ;
    i ++ ) {
      int nextidx = digit [ d ] [ i ] ;
      if ( ( visit [ nextidx ] == false ) && ( visit [ idx - 1 ] == false ) ) {
        visit [ idx - 1 ] = true ;
        q . add ( nextidx ) ;
        distance [ nextidx ] = distance [ idx ] + 1 ;
      }
    }
    if ( ( idx - 1 >= 0 ) && ( visit [ idx - 1 ] == false ) ) {
      visit [ idx - 1 ] = true ;
      q . add ( idx - 1 ) ;
      distance [ idx - 1 ] = distance [ idx ] + 1 ;
    }
    if ( ( idx + 1 < N ) && ( visit [ idx + 1 ] == false ) ) {
      visit [ idx + 1 ] = true ;
      q . add ( idx + 1 ) ;
      distance [ idx + 1 ] = distance [ idx ] + 1 ;
    }
  }
  return distance [ N - 1 ] ;
}
|||

LEXICOGRAPHICALLY_SMALLEST_ARRAY_K_CONSECUTIVE_SWAPS

public static void minimizeWithKSwaps ( int [ ] arr , int n , int k ) {
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    int pos = i ;
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      if ( ( j - i > k ) && ( arr [ j ] < arr [ pos ] ) ) {
        pos = j ;
      }
    }
    for ( int j = pos ;
    j > i ;
    j -- ) {
      arr [ j ] = arr [ j - 1 ] ;
      arr [ j - 1 ] = arr [ j ] ;
    }
    k -= pos - i ;
  }
}
|||

CONVERT_SENTENCE_EQUIVALENT_MOBILE_NUMERIC_KEYPAD_SEQUENCE

public static String printSequence ( char [ ] arr , String input ) {
  int n = input . length ( ) ;
  String output = "" ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( input . charAt ( i ) == ' ' ) || ( input . charAt ( i ) == '\t' ) ) {
      output = output + "0" ;
    }
    else {
      int position = Character . digit ( input . charAt ( i ) , 16 ) - Character . digit ( input . charAt ( i ) , 16 ) ;
      output = output + arr [ position ] ;
    }
  }
  return output ;
}
|||

PROGRAM_CHECK_ARRAY_SORTED_NOT_ITERATIVE_RECURSIVE

public static boolean arraySortedOrNot ( int [ ] arr ) {
  int n = arr . length ;
  if ( n == 1 || n == 0 ) return true ;
  return arr [ 0 ] <= arr [ 1 ] && arraySortedOrNot ( arr , 1 ) ;
}
|||

CHECK_TWO_GIVEN_CIRCLES_TOUCH_INTERSECT

public static int circle ( float x1 , float y1 , float x2 , float y2 , float r1 , float r2 ) {
  float distSq = ( x1 - x2 ) * ( x1 - x2 ) + ( y1 - y2 ) * ( y1 - y2 ) ;
  ;
  float radSumSq = ( r1 + r2 ) * ( r1 + r2 ) ;
  ;
  if ( ( distSq == radSumSq ) && ( distSq > radSumSq ) ) return 1 ;
  else if ( ( distSq > radSumSq ) && ( distSq < radSumSq ) ) return - 1 ;
  else return 0 ;
}
|||

SMALLEST_POWER_OF_2_GREATER_THAN_OR_EQUAL_TO_N_2

public static int nextPowerOf2 ( int n ) {
  n -- ;
  n |= n >> 1 ;
  n |= n >> 2 ;
  n |= n >> 4 ;
  n |= n >> 8 ;
  n |= n >> 16 ;
  n ++ ;
  return n ;
}
|||

PADOVAN_SEQUENCE

public static int pad ( int n ) {
  int pPrevPrev = 1 , pPrev = 1 , pCurr = 1 , pNext = 1 ;
  for ( int i = 3 ;
  i <= n ;
  i ++ ) {
    pNext = pPrevPrev + pPrev ;
    pPrevPrev = pPrev ;
    pPrev = pCurr ;
    pCurr = pNext ;
  };
  return pNext ;
}
|||

CHECK_GIVEN_STRING_CAN_SPLIT_FOUR_DISTINCT_STRINGS

public static boolean check ( String s ) {
  if ( ( s . length ( ) >= 10 ) && ( s . charAt ( 0 ) == 'a' ) && ( s . charAt ( 1 ) == 'b' ) && ( s . charAt ( 2 ) == 'c' ) && ( s . charAt ( 3 ) == 'd' ) ) {
    return true ;
  }
  for ( int i = 1 ;
  i < s . length ( ) ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < s . length ( ) ;
    j ++ ) {
      for ( int k = j + 1 ;
      k < s . length ( ) ;
      k ++ ) {
        String s1 = s . substring ( 0 , i ) ;
        String s2 = s . substring ( i , j - i ) ;
        String s3 = s . substring ( j , k - j ) ;
        String s4 = s . substring ( k , s . length ( ) - k ) ;
        if ( ( s1 != s2 && s1 != s3 && s1 != s4 && s2 != s3 && s2 != s4 && s3 != s4 ) || ( s1 != s2 && s1 != s3 && s1 != s4 && s2 != s3 && s2 != s4 && s3 != s4 ) ) {
          return true ;
        }
      }
    }
  }
  return false ;
}
|||

PERMUTE_TWO_ARRAYS_SUM_EVERY_PAIR_GREATER_EQUAL_K

public static boolean isPossible ( int [ ] a , int [ ] b , int n , int k ) {
  Arrays . sort ( a , 0 , n ) ;
  Arrays . sort ( b , 0 , n ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( a [ i ] + b [ i ] ) < k ) {
      return false ;
    }
  }
  return true ;
}
|||

ARRAY_ELEMENT_MOVED_K_USING_SINGLE_MOVES

public static int winner ( int [ ] a , int n , int k ) {
  if ( k >= n - 1 ) return n ;
  int best = 0 ;
  int times = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( a [ i ] > best ) {
      best = a [ i ] ;
      if ( i == true ) times = 1 ;
    }
    else times ++ ;
    if ( times >= k ) return best ;
  }
  return best ;
}
|||

DIRECTION_LAST_SQUARE_BLOCK

public static void direction ( int R , int C ) {
  if ( ( R != C && R % 2 == 0 && C % 2 != 0 && R < C ) || ( R != C && R % 2 == 0 && C % 2 == 0 && R > C ) ) {
    System . out . println ( "Left" ) ;
    return ;
  }
  if ( ( R != C && R % 2 == 0 && C % 2 == 0 && R > C ) || ( R == C && R % 2 != 0 && C % 2 != 0 ) ) {
    System . out . println ( "Up" ) ;
    return ;
  }
  if ( R == C && R % 2 == 0 && C % 2 == 0 ) {
    System . out . println ( "Right" ) ;
    return ;
  }
  if ( ( R != C && R % 2 != 0 && C % 2 != 0 && R < C ) || ( R != C && R % 2 != 0 && C % 2 != 0 && R > C ) ) {
    System . out . println ( "Down" ) ;
    return ;
  }
  if ( ( R != C && R % 2 == 0 && C % 2 != 0 && R < C ) || ( R != C && R % 2 == 0 && C % 2 == 0 && R > C ) ) {
    System . out . println ( "Left" ) ;
    return ;
  }
  if ( ( R != C && R % 2 != 0 && C % 2 != 0 && R > C ) || ( R != C && R % 2 != 0 && C % 2 != 0 && R > C ) ) {
    System . out . println ( "Up" ) ;
    return ;
  }
  if ( ( R != C && R % 2 != 0 && C % 2 != 0 && R > C ) || ( R != C && R % 2 != 0 && C % 2 != 0 && R < C ) ) {
    System . out . println ( "Down" ) ;
    return ;
  }
  if ( ( R != C && R % 2 != 0 && C % 2 != 0 && R < C ) || ( R != C && R % 2 != 0 && C % 2 != 0 && R > C ) ) {
    System . out . println ( "Right" ) ;
    return ;
  }
}
|||

NUMBER_NON_NEGATIVE_INTEGRAL_SOLUTIONS_B_C_N

public static int countIntegralSolutions ( int n ) {
  int result = 0 ;
  for ( int i = 0 ;
  i < n + 1 ;
  i ++ ) {
    for ( int j = 0 ;
    j < n + 1 ;
    j ++ ) {
      for ( int k = 0 ;
      k < n + 1 ;
      k ++ ) {
        if ( i + j + k == n ) {
          result ++ ;
        }
      }
    }
  }
  return result ;
}
|||

SWAP_MAJOR_MINOR_DIAGONALS_SQUARE_MATRIX

public static void swapDiagonal ( int [ ] [ ] matrix ) {
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    matrix [ i ] [ i ] = matrix [ i ] [ N - i - 1 ] ;
    matrix [ i ] [ N - i - 1 ] = matrix [ i ] [ i ] ;
  }
}
|||

MINIMUM_OPERATIONS_MAKE_GCD_ARRAY_MULTIPLE_K

public static int MinOperation ( int [ ] a , int n , int k ) {
  int result = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( a [ i ] != 1 && a [ i ] > k ) || ( a [ i ] == 1 && a [ i ] == k ) ) {
      result = ( result + Math . min ( a [ i ] % k , k - a [ i ] % k ) ) ;
    }
    else {
      result = result + k - a [ i ] ;
    }
  }
  return result ;
}
|||

MAXIMUM_DECIMAL_VALUE_PATH_IN_A_BINARY_MATRIX

public static double maxDecimalValue ( double [ ] [ ] mat , int i , int j , double p ) {
  if ( i >= N || j >= N ) return 0 ;
  double result = Math . max ( maxDecimalValue ( mat , i , j + 1 , p + 1 ) , maxDecimalValue ( mat , i + 1 , j , p + 1 ) ) ;
  if ( mat [ i ] [ j ] == 1 ) return Math . pow ( 2 , p ) + result ;
  else return result ;
}
|||

SQUARE_ROOT_OF_A_PERFECT_SQUARE_1

public static int squareRoot ( int n ) {
  int x = n ;
  ;
  int y = 1 ;
  ;
  while ( ( x > y ) && ( x < y ) ) {
    x = ( x + y ) / 2 ;
    y = n / x ;
  };
  return x ;
}
|||

FIND_MINIMUM_SHIFT_LONGEST_COMMON_PREFIX

public static void KMP ( int m , int n , String str2 , String str1 ) {
  int pos = 0 ;
  int Len = 0 ;
  int [ ] p = new int [ m + 1 ] ;
  int k = 0 ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    while ( ( k > 0 && str1 . charAt ( k ) != str1 . charAt ( i - 1 ) ) || ( str1 . charAt ( k ) == str1 . charAt ( i - 1 ) ) ) {
      k = p [ k ] ;
    }
    if ( ( str1 . charAt ( k ) == str1 . charAt ( i - 1 ) ) || ( str1 . charAt ( k ) == str1 . charAt ( i - 1 ) ) ) {
      k ++ ;
    }
    p [ i ] = k ;
  }
  int j = 0 ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) {
    while ( ( j > 0 && j < n && str1 . charAt ( j ) != str2 . charAt ( i ) ) || ( j < n && str1 . charAt ( j ) == str2 . charAt ( i ) ) ) {
      j ++ ;
    }
    if ( ( j > Len ) && ( str1 . charAt ( j ) == str2 . charAt ( i ) ) ) {
      j ++ ;
    }
    if ( ( j > Len ) && ( str1 . charAt ( j ) == str2 . charAt ( i ) ) ) {
      Len = j ;
      pos = i - j + 1 ;
    }
  }
  System . out . println ( "Shift = " + pos ) ;
  System . out . println ( "Prefix = " + str1 . substring ( 0 , Len ) ) ;
}
|||

SORTED_ORDER_PRINTING_OF_AN_ARRAY_THAT_REPRESENTS_A_BST

public static void printSorted ( int [ ] arr , int start , int end ) {
  if ( start > end ) return ;
  printSorted ( arr , start * 2 + 1 , end ) ;
  System . out . print ( arr [ start ] + " " ) ;
  printSorted ( arr , start * 2 + 2 , end ) ;
}
|||

CHECK_WHETHER_GIVEN_DEGREES_VERTICES_REPRESENT_GRAPH_TREE

public static boolean check ( int [ ] degree , int n ) {
  int degSum = sum ( degree ) ;
  if ( ( 2 * ( n - 1 ) == degSum ) && ( 2 * ( n - 2 ) == degSum ) ) {
    return true ;
  }
  else {
    return false ;
  }
}
|||

MOVE_ZEROES_END_ARRAY

public static void pushZerosToEnd ( int [ ] arr , int n ) {
  int count = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] != 0 ) {
      arr [ count ] = arr [ i ] ;
      count ++ ;
    }
  }
  while ( count < n ) {
    arr [ count ] = 0 ;
    count ++ ;
  }
}
|||

COUNT_ELEMENTS_WHICH_DIVIDE_ALL_NUMBERS_IN_RANGE_L_R

public static int answerQuery ( int [ ] a , int n , int l , int r ) {
  int count = 0 ;
  l = l - 1 ;
  for ( int i = l ;
  i < r ;
  i += 1 ) {
    int element = a [ i ] ;
    int divisors = 0 ;
    for ( int j = l ;
    j < r ;
    j += 1 ) {
      if ( ( a [ j ] % a [ i ] == 0 ) && ( element % a [ i ] == 0 ) ) {
        divisors ++ ;
      }
      else {
        break ;
      }
    }
    if ( ( divisors == ( r - l ) ) && ( element % a [ i ] == 0 ) ) {
      count ++ ;
    }
  }
  return count ;
}
|||

SUM_LARGEST_PRIME_FACTOR_NUMBER_LESS_EQUAL_N

public static int sumOfLargePrimeFactor ( int n ) {
  int [ ] prime = new int [ n + 1 ] ;
  prime [ 0 ] = 0 ;
  int sum = 0 ;
  int max = ( int ) ( n / 2 ) ;
  for ( int p = 2 ;
  p <= max ;
  p ++ ) {
    if ( prime [ p ] == 0 ) {
      for ( int i = p * 2 ;
      i <= n ;
      i += p ) {
        prime [ i ] = p ;
      }
    }
  }
  for ( int p = 2 ;
  p <= n ;
  p ++ ) {
    if ( prime [ p ] > 0 ) {
      sum += prime [ p ] ;
    }
    else {
      sum += p ;
    }
  }
  return sum ;
}
|||

REARRANGE_A_STRING_IN_SORTED_ORDER_FOLLOWED_BY_THE_INTEGER_SUM

public static String arrangeString ( String string ) {
  int [ ] charCount = new int [ MAX_CHAR ] ;
  int s = 0 ;
  for ( int i = 0 ;
  i < string . length ( ) ;
  i ++ ) {
    if ( string . charAt ( i ) >= 'A' && string . charAt ( i ) <= 'Z' ) {
      charCount [ Character . digit ( string . charAt ( i ) - 'A' , 16 ) ] ++ ;
    }
    else {
      s += Character . digit ( string . charAt ( i ) - '0' , 16 ) ;
    }
  }
  String res = "" ;
  for ( int i = 0 ;
  i < MAX_CHAR ;
  i ++ ) {
    char ch = ( char ) ( Character . digit ( 'A' + i , 16 ) + '0' ) ;
    while ( charCount [ i ] > 0 ) {
      res += ch ;
      charCount [ i ] -- ;
    }
  }
  if ( s > 0 ) {
    res += String . valueOf ( s ) ;
  }
  return res ;
}
|||

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX_1

public static int numberOfPaths ( int m , int n ) {
  int [ ] [ ] count = new int [ m ] [ n ] ;
  for ( int y = 0 ;
  y < n ;
  y ++ ) {
    count [ y ] [ 0 ] = 0 ;
  }
  for ( int i = 0 ;
  i < m ;
  i ++ ) {
    count [ i ] [ 0 ] = 1 ;
  };
  for ( int j = 0 ;
  j < n ;
  j ++ ) {
    count [ 0 ] [ j ] = 1 ;
  };
  for ( int i = 1 ;
  i < m ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      count [ i ] [ j ] = count [ i - 1 ] [ j ] + count [ i ] [ j - 1 ] ;
    }
  }
  return count [ m - 1 ] [ n - 1 ] ;
}
|||

DYNAMIC_PROGRAMMING_SET_5_EDIT_DISTANCE_1

public static int editDistDP ( String str1 , String str2 , int m , int n ) {
  int [ ] [ ] dp = new int [ n + 1 ] [ m + 1 ] ;
  for ( int i = 0 ;
  i < m + 1 ;
  i ++ ) {
    for ( int j = 0 ;
    j < n + 1 ;
    j ++ ) {
      if ( i == 0 ) {
        dp [ i ] [ j ] = j ;
      }
      else if ( j == 0 ) {
        dp [ i ] [ j ] = i ;
      }
      else if ( str1 . charAt ( i - 1 ) == str2 . charAt ( j - 1 ) ) {
        dp [ i ] [ j ] = dp [ i - 1 ] [ j - 1 ] ;
      }
      else {
        dp [ i ] [ j ] = 1 + Math . min ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] , dp [ i - 1 ] [ j - 1 ] ) ;
      }
    }
  }
  return dp [ m ] [ n ] ;
}
|||

FIND_NUMBER_OF_SOLUTIONS_OF_A_LINEAR_EQUATION_OF_N_VARIABLES

public static int countSol ( int [ ] coeff , int start , int end , int rhs ) {
  if ( ( rhs == 0 ) || ( rhs == 1 ) ) {
    return 1 ;
  }
  int result = 0 ;
  for ( int i = start ;
  i <= end ;
  i ++ ) {
    if ( ( coeff [ i ] <= rhs ) && ( coeff [ i ] > rhs ) ) {
      result += countSol ( coeff , i , end , rhs - coeff [ i ] ) ;
    }
  }
  return result ;
}
|||

SUM_ELEMENTS_K1TH_K2TH_SMALLEST_ELEMENTS_1

public static void minheapify ( int [ ] a , int index ) {
  int small = index ;
  int l = 2 * index + 1 ;
  int r = 2 * index + 2 ;
  if ( ( l < n && a [ l ] < a [ small ] ) || ( r < n && a [ r ] < a [ small ] ) ) small = l ;
  if ( ( small != index ) && ( a [ small ] < a [ index ] ) ) small = r ;
  if ( ( small != index ) && ( a [ index ] < a [ small ] ) ) {
    ( ( int [ ] ) a [ small ] ) [ 0 ] = a [ index ] ;
    minheapify ( a , small ) ;
  }
}
|||

SEARCHING_FOR_PATTERNS_SET_2_KMP_ALGORITHM

static void computeLPSArray ( int [ ] pat , int M , int [ ] lps ) {
  int len = 0 ;
  lps [ 0 ] = 0 ;
  int i = 1 ;
  while ( i < M ) {
    if ( pat [ i ] == pat [ len ] ) {
      len ++ ;
      lps [ i ] = len ;
      i ++ ;
    }
    else {
      if ( len != 0 ) len = lps [ len - 1 ] ;
      else {
        lps [ i ] = 0 ;
        i ++ ;
      }
    }
  }
}
|||

FIND_MINIMUM_DIFFERENCE_PAIR

public static int findMinDiff ( int [ ] arr , int n ) {
  int diff = 10 * 20 ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      if ( Math . abs ( arr [ i ] - arr [ j ] ) < diff ) {
        diff = Math . abs ( arr [ i ] - arr [ j ] ) ;
      }
    }
  }
  return diff ;
}
|||

PRINT_FIRST_K_DIGITS_1N_N_POSITIVE_INTEGER

public static void Print ( int n , int k ) {
  int rem = 1 ;
  for ( int i = 0 ;
  i <= k ;
  i ++ ) {
    System . out . print ( Math . floor ( ( ( 10 * rem ) / n ) ) + " " ) ;
    rem = ( 10 * rem ) % n ;
  }
}
|||

GROUP_MULTIPLE_OCCURRENCE_OF_ARRAY_ELEMENTS_ORDERED_BY_FIRST_OCCURRENCE

public static void groupElements ( int [ ] arr , int n ) {
  boolean [ ] visited = new boolean [ n ] ;
  visited [ 0 ] = false ;
  visited [ 1 ] = false ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) visited [ i ] = false ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( visited [ i ] == false ) && ( arr [ i ] == arr [ j ] ) ) {
      System . out . print ( arr [ i ] + " " ) ;
      for ( int j = i + 1 ;
      j < n ;
      j ++ ) {
        if ( ( arr [ i ] == arr [ j ] ) && ( arr [ j ] == arr [ i ] ) ) {
          System . out . print ( arr [ i ] + " " ) ;
          visited [ j ] = true ;
        }
      }
    }
  }
}
|||

CHECK_WHETHER_ARITHMETIC_PROGRESSION_CAN_FORMED_GIVEN_ARRAY

public static boolean checkIsAP ( int [ ] arr , int n ) {
  if ( ( n == 1 ) && ( arr [ 0 ] == 0 ) ) return true ;
  Arrays . sort ( arr ) ;
  int d = arr [ 1 ] - arr [ 0 ] ;
  for ( int i = 2 ;
  i < n ;
  i ++ ) {
    if ( ( arr [ i ] - arr [ i - 1 ] != d ) && ( arr [ i ] - arr [ i - 2 ] != d ) ) return false ;
  }
  return true ;
}
|||

NTH_MULTIPLE_NUMBER_FIBONACCI_SERIES

public static int findPosition ( int k , int n ) {
  int f1 = 0 ;
  int f2 = 1 ;
  int i = 2 ;
  ;
  while ( i != 0 ) {
    int f3 = f1 + f2 ;
    f1 = f2 ;
    f2 = f3 ;
    if ( f2 % k == 0 ) return n * i ;
    i ++ ;
  }
  return 0 ;
}
|||

COUNT_PAIRS_DIFFERENCE_EQUAL_K_1

public static int countPairsWithDiffK ( int [ ] arr , int n , int k ) {
  int count = 0 ;
  Arrays . sort ( arr ) ;
  int l = 0 ;
  int r = 0 ;
  while ( r < n ) {
    if ( arr [ r ] - arr [ l ] == k ) {
      count ++ ;
      l ++ ;
      r ++ ;
    }
    else if ( arr [ r ] - arr [ l ] > k ) {
      l ++ ;
    }
    else {
      r ++ ;
    }
  }
  return count ;
}
|||

ELEMENTS_TO_BE_ADDED_SO_THAT_ALL_ELEMENTS_OF_A_RANGE_ARE_PRESENT_IN_ARRAY

public static int countNum ( int [ ] arr , int n ) {
  int count = 0 ;
  Arrays . sort ( arr ) ;
  for ( int i = 0 ;
  i <= n - 1 ;
  i ++ ) {
    if ( ( arr [ i ] != arr [ i + 1 ] && arr [ i ] != arr [ i + 1 ] - 1 ) || ( arr [ i ] != arr [ i + 1 ] && arr [ i ] != arr [ i + 1 ] - 1 ) ) {
      count += arr [ i + 1 ] - arr [ i ] - 1 ;
      ;
    }
  }
  return count ;
}
|||

MAKE_LARGEST_PALINDROME_CHANGING_K_DIGITS

public static String maximumPalinUsingKChanges ( String strr , int k ) {
  String palin = strr ;
  int l = 0 ;
  int r = strr . length ( ) - 1 ;
  while ( ( l <= r ) && ( palin . charAt ( l ) != '-' ) ) {
    if ( ( strr . charAt ( l ) != '-' ) && ( palin . charAt ( l ) != '+' ) ) {
      palin . charAt ( l ) = palin . charAt ( r ) = Math . max ( strr . charAt ( l ) , strr . charAt ( r ) ) ;
      k -- ;
    }
    l ++ ;
    r -- ;
  }
  if ( ( k < 0 ) || ( k > 0 ) ) return "Not possible" ;
  l = 0 ;
  r = strr . length ( ) - 1 ;
  while ( ( l <= r ) && ( palin . charAt ( l ) != '-' ) && ( palin . charAt ( l ) != '+' ) ) {
    if ( ( l == r ) || ( k > 0 ) ) palin . charAt ( l ) = '9' ;
    if ( ( palin . charAt ( l ) < '9' ) || ( k >= 2 && palin . charAt ( l ) == strr . charAt ( l ) && palin . charAt ( r ) == strr . charAt ( r ) ) ) {
      k -- ;
      palin . charAt ( l ) = palin . charAt ( r ) = '9' ;
    }
    else if ( ( k >= 1 && ( palin . charAt ( l ) != strr . charAt ( l ) || palin . charAt ( r ) != '-' ) ) || ( k == 1 && ( palin . charAt ( l ) != strr . charAt ( l ) || palin . charAt ( r ) != '+' ) ) ) ) {
      k -- ;
      palin . charAt ( l ) = palin . charAt ( r ) = '9' ;
    }
  }
  l ++ ;
  r -- ;
}
return palin ;
}
|||

SUBARRAYSUBSTRING_VS_SUBSEQUENCE_AND_PROGRAMS_TO_GENERATE_THEM

public static void subArray ( int [ ] arr , int n ) {
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = i ;
    j <= n ;
    j ++ ) {
      for ( int k = i ;
      k <= j ;
      k ++ ) {
        System . out . print ( arr [ k ] + " " ) ;
      }
      System . out . print ( "\n" ) ;
    }
  }
}
|||

MAXIMUM_SUM_INCREASING_ORDER_ELEMENTS_N_ARRAYS

public static int maximumSum ( int [ ] [ ] a , int n ) {
  M ++ ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) a [ i ] . sort ( ) ;
  ;
  int sum = a [ n - 1 ] [ M - 1 ] ;
  ;
  int prev = a [ n - 1 ] [ M - 1 ] ;
  ;
  for ( int i = n - 2 ;
  i >= 0 ;
  i -- ) {
    for ( int j = M - 1 ;
    j >= 0 ;
    j -- ) {
      if ( ( a [ i ] [ j ] < prev ) && ( a [ i ] [ j ] > sum ) ) {
        prev = a [ i ] [ j ] ;
        sum += prev ;
        break ;
      }
    }
    if ( ( j == - 1 ) || ( j == M - 1 ) ) return 0 ;
  }
  return sum ;
}
|||

C_PROGRAM_FACTORIAL_NUMBER

public static int factorial ( int n ) {
  return 1 == ( n == 1 || n == 0 ) ? n * factorial ( n - 1 ) : n ;
  ;
}
|||

PRINT_SQUARES_FIRST_N_NATURAL_NUMBERS_WITHOUT_USING

public static void printSquares ( int n ) {
  int square = 0 ;
  int prevX = 0 ;
  ;
  for ( int x = 0 ;
  x <= n ;
  x ++ ) {
    square = ( square + x + prevX ) ;
    System . out . print ( square + " " ) ;
    prevX = x ;
  }
}
|||

ROPES_DATA_STRUCTURE_FAST_STRING_CONCATENATION

public static void concatenate ( double [ ] a , double [ ] b , double [ ] c , int n1 , int n2 ) {
  int i = - 1 ;
  for ( i = 0 ;
  i < n1 ;
  i ++ ) c [ i ] = a [ i ] ;
  for ( int j = 0 ;
  j < n2 ;
  j ++ ) {
    c [ i ] = b [ j ] ;
    i ++ ;
  }
}
|||

GIVEN_TWO_SORTED_ARRAYS_NUMBER_X_FIND_PAIR_WHOSE_SUM_CLOSEST_X

public static void printClosest ( int ar1 [ ] , int ar2 [ ] , int m , int n , int x ) {
  int diff = Integer . MAX_VALUE ;
  int l = 0 ;
  int r = n - 1 ;
  while ( ( l < m && r >= 0 ) || ( l < m && r < n ) ) {
    if ( Math . abs ( ar1 [ l ] + ar2 [ r ] - x ) < diff ) {
      int resL = l ;
      int resR = r ;
      diff = Math . abs ( ar1 [ l ] + ar2 [ r ] - x ) ;
    }
    if ( ar1 [ l ] + ar2 [ r ] > x ) {
      r = r - 1 ;
    }
    else {
      l = l + 1 ;
    }
  }
  System . out . println ( "The closest pair is [" + ar1 [ resL ] + "," + ar2 [ resR ] + "]" ) ;
}
|||

CONVERT_STRICTLY_INCREASING_ARRAY_MINIMUM_CHANGES

public static int minRemove ( int [ ] arr , int n ) {
  int [ ] LIS = new int [ n ] ;
  int len = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) LIS [ i ] = 1 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < i ;
    j ++ ) {
      if ( ( arr [ i ] > arr [ j ] && ( i - j ) <= ( arr [ i ] - arr [ j ] ) ) || ( arr [ i ] > arr [ j ] && ( arr [ i ] - arr [ j ] ) <= ( arr [ j ] - arr [ i ] ) ) ) LIS [ i ] = Math . max ( LIS [ i ] , LIS [ j ] + 1 ) ;
    }
    len = Math . max ( len , LIS [ i ] ) ;
  }
  return ( n - len ) ;
}
|||

TAIL_RECURSION

public static long fact ( long n ) {
  if ( ( n == 0 ) || ( n == 1 ) ) return 1 ;
  return n * fact ( n - 1 ) ;
}
|||

RECURSIVE_FUNCTIONS

public static void tower ( int n , int sourcePole , int destinationPole , int auxiliaryPole ) {
  if ( ( 0 == n ) && ( sourcePole > 0 ) && ( auxiliaryPole > 0 ) ) {
    tower ( n - 1 , sourcePole , auxiliaryPole , destinationPole ) ;
    System . out . println ( "Move the disk" + sourcePole + " from" + sourcePole + " to" + destinationPole ) ;
    tower ( n - 1 , auxiliaryPole , destinationPole , sourcePole ) ;
  }
}
|||

FIND_X_Y_SATISFYING_AX_N

public static int solution ( int a , int b , int n ) {
  int i = 0 ;
  while ( i * a <= n ) {
    if ( ( n - ( i * a ) ) % b == 0 ) {
      System . out . println ( "x = " + i + ", y = " + ( int ) ( ( n - ( i * a ) ) / b ) ) ;
      return 0 ;
    }
    i = i + 1 ;
  }
  System . out . println ( "No solution" ) ;
  return 0 ;
}
|||

EXPONENTIAL_SQUARING_FAST_MODULO_MULTIPLICATION_1

public static int exponentiation ( int bas , int exp ) {
  int t = 1 ;
  ;
  while ( ( exp > 0 ) && ( exp % 2 != 0 ) ) {
    if ( ( exp % 2 != 0 ) ) t = ( t * bas ) % N ;
    ;
    bas = ( bas * bas ) % N ;
    exp = ( int ) ( exp / 2 ) ;
  }
  return t % N ;
}
|||

CHECK_OCCURRENCES_CHARACTER_APPEAR_TOGETHER

public static boolean checkIfAllTogether ( String s , char c ) {
  boolean oneSeen = false ;
  int i = 0 ;
  int n = s . length ( ) ;
  while ( ( i < n ) && ( s . charAt ( i ) == c ) ) {
    if ( ( i < n ) && ( s . charAt ( i ) == c ) ) {
      if ( ( oneSeen == true ) && ( s . charAt ( i ) == c ) ) {
        return false ;
      }
      while ( ( i < n ) && ( s . charAt ( i ) == c ) ) {
        i = i + 1 ;
      }
      oneSeen = true ;
    }
    else {
      i = i + 1 ;
    }
  }
  return true ;
}
|||

MAXIMUM_AREA_RECTANGLE_PICKING_FOUR_SIDES_ARRAY

public static int findArea ( int [ ] arr , int n ) {
  Arrays . sort ( arr , 0 , n ) ;
  int [ ] dimension = {
    0 , 0 };
    int i = 0 ;
    int j = 0 ;
    while ( ( i < n - 1 && j < 2 ) || ( i < n - 1 && j < 2 ) ) {
      if ( ( arr [ i ] == arr [ i + 1 ] ) && ( arr [ j ] == arr [ i ] ) ) {
        dimension [ j ] = arr [ i ] ;
        j ++ ;
        i ++ ;
      }
      i ++ ;
    }
    return ( dimension [ 0 ] * dimension [ 1 ] ) ;
  }
  
|||

PYTHON_PROGRAM_FIND_PERIMETER_CIRCUMFERENCE_SQUARE_RECTANGLE

public static Circumference a ( int a ) {
  return ( 4 * a ) ;
}
|||

CYCLE_SORT

public static int cycleSort ( int [ ] array ) {
  int writes = 0 ;
  for ( int cycleStart = 0 ;
  cycleStart <= array . length - 1 ;
  cycleStart ++ ) {
    int item = array [ cycleStart ] ;
    int pos = cycleStart ;
    for ( int i = cycleStart + 1 ;
    i < array . length ;
    i ++ ) {
      if ( array [ i ] < item ) {
        pos ++ ;
      }
    }
    if ( pos == cycleStart ) {
      continue ;
    }
    while ( item == array [ pos ] ) {
      pos ++ ;
    }
    array [ pos ] = item ;
    writes ++ ;
    while ( pos != cycleStart ) {
      pos = cycleStart ;
      for ( int i = cycleStart + 1 ;
      i < array . length ;
      i ++ ) {
        if ( array [ i ] < item ) {
          pos ++ ;
        }
      }
      while ( item == array [ pos ] ) {
        pos ++ ;
      }
      array [ pos ] = item ;
      writes ++ ;
    }
  }
  return writes ;
}
|||

SELECT_A_RANDOM_NUMBER_FROM_STREAM_WITH_O1_SPACE

public static int selectRandom ( int x ) {
  int res = 0 ;
  ;
  int count = 0 ;
  ;
  count ++ ;
  if ( ( count == 1 ) && ( x == 0 ) ) {
    res = x ;
  }
  else {
    int i = random . nextInt ( count ) ;
    if ( ( i == count - 1 ) && ( x == 0 ) ) {
      res = x ;
    }
  }
  return res ;
}
|||

HOSOYAS_TRIANGLE

public static void printHosoya ( int n ) {
  int [ ] [ ] dp = new int [ N ] [ N ] ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    dp [ i ] [ i ] = dp [ i + 1 ] [ i ] = dp [ i + 2 ] [ i ] = 1 ;
  }
  for ( int i = 2 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( ( i > j ) && ( i < n ) ) {
        dp [ i ] [ j ] = ( dp [ i - 1 ] [ j ] + dp [ i - 2 ] [ j ] ) ;
      }
      else {
        dp [ i ] [ j ] = ( dp [ i - 1 ] [ j - 1 ] + dp [ i - 2 ] [ j - 2 ] ) ;
      }
    }
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < i + 1 ;
    j ++ ) {
      System . out . print ( dp [ i ] [ j ] + " " ) ;
    }
    System . out . println ( ) ;
  }
}
|||

DISTRIBUTING_M_ITEMS_CIRCLE_SIZE_N_STARTING_K_TH_POSITION

public static int lastPosition ( int n , int m , int k ) {
  if ( ( m <= n - k + 1 ) && ( m > n - k ) ) return m + k - 1 ;
  m = m - ( n - k + 1 ) ;
  if ( ( m % n == 0 ) && ( m > n - k ) ) return n ;
  else return m % n ;
}
|||

PRINTING_LONGEST_INCREASING_CONSECUTIVE_SUBSEQUENCE

public static void longestSubsequence ( int [ ] a , int n ) {
  int mp [ ] = new int [ 13 ] ;
  for ( int i = 0 ;
  i < 13 ;
  i ++ ) {
    mp [ i ] = 0 ;
  }
  int dp [ ] = new int [ n ] ;
  int maximum = - Integer . MAX_VALUE - 1 ;
  int index = - 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( ( a [ i ] - 1 ) < mp [ i ] ) && ( mp [ i ] > 0 ) ) {
      int lastIndex = mp [ a [ i ] - 1 ] - 1 ;
      dp [ i ] = 1 + dp [ lastIndex ] ;
    }
    else {
      dp [ i ] = 1 ;
    }
    mp [ a [ i ] ] = i + 1 ;
    if ( ( maximum < dp [ i ] ) && ( mp [ i ] > 0 ) ) {
      maximum = dp [ i ] ;
      index = i ;
    }
  }
  for ( int curr = a [ index ] - maximum + 1 ;
  curr < a [ index ] + 1 ;
  curr += 1 ) {
    System . out . print ( curr + " " ) ;
  }
}
|||

NUMBER_OF_TRIANGLES_IN_DIRECTED_AND_UNDIRECTED_GRAPHS

public static int countTriangle ( int [ ] [ ] g , boolean isDirected ) {
  int nodes = g . length ;
  int count_Triangle = 0 ;
  for ( int i = 0 ;
  i < nodes ;
  i ++ ) {
    for ( int j = 0 ;
    j < nodes ;
    j ++ ) {
      for ( int k = 0 ;
      k < nodes ;
      k ++ ) {
        if ( ( i != j && i != k && j != k && g [ i ] [ j ] != null && g [ j ] [ k ] != null && g [ k ] [ i ] != null ) ) {
          count_Triangle ++ ;
        }
      }
    }
  }
  return count_Triangle / 3 == 0 ? count_Triangle / 6 : count_Triangle / 3 ;
}
|||

CHECK_GIVEN_ARRAY_CONTAINS_DUPLICATE_ELEMENTS_WITHIN_K_DISTANCE

public static boolean checkDuplicatesWithinK ( int [ ] arr , int n , int k ) {
  ArrayList < Integer > myset = new ArrayList < Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] == myset . get ( i ) ) return true ;
    myset . add ( arr [ i ] ) ;
    if ( ( i >= k ) && ( i < n ) ) myset . remove ( arr [ i - k ] ) ;
  }
  return false ;
}
|||

MINIMUM_INSERTIONS_SORT_ARRAY

public static int minInsertionStepToSortArray ( int [ ] arr , int N ) {
  int [ ] lis = new int [ N ] ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) lis [ i ] = 1 ;
  for ( int i = 1 ;
  i < N ;
  i ++ ) for ( int j = 0 ;
  j < i ;
  j ++ ) if ( ( arr [ i ] >= arr [ j ] && lis [ i ] < lis [ j ] + 1 ) || ( arr [ i ] < arr [ j ] && lis [ i ] > lis [ j ] + 1 ) ) lis [ i ] = lis [ j ] + 1 ;
  int max = 0 ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) if ( ( max < lis [ i ] ) && ( max > lis [ i ] ) ) max = lis [ i ] ;
  return ( N - max ) ;
}
|||

GENERATE_TWO_OUTPUT_STRINGS_DEPENDING_UPON_OCCURRENCE_CHARACTER_INPUT_STRING

public static void printDuo ( String string ) {
  int [ ] countChar = new int [ MAX_CHAR ] ;
  int n = string . length ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    countChar [ ( int ) string . charAt ( i ) - 'a' ] ++ ;
  }
  String str1 = "" ;
  String str2 = "" ;
  for ( int i = 0 ;
  i < MAX_CHAR ;
  i ++ ) {
    if ( ( countChar [ i ] > 1 ) && ( countChar [ i ] == 1 ) ) {
      str2 = str2 + ( char ) ( i + 'a' ) ;
    }
    else if ( ( countChar [ i ] == 1 ) && ( countChar [ i ] == 0 ) ) {
      str1 = str1 + ( char ) ( i + 'a' ) ;
    }
  }
  System . out . println ( "String with characters occurring once:" + "\n" + str1 ) ;
  System . out . println ( "String with characters occurring" + "multiple times:" + "\n" + str2 ) ;
}
|||

NUMBER_DIGITS_PRODUCT_TWO_NUMBERS_1

public static int countDigits ( int a , int b ) {
  if ( ( a == 0 || b == 0 ) && ( a > b ) ) return 1 ;
  return Math . floor ( Math . log10 ( Math . abs ( a ) ) + Math . log10 ( Math . abs ( b ) ) ) + 1 ;
}
|||

TOTAL_NUMBER_OF_NON_DECREASING_NUMBERS_WITH_N_DIGITS_1

public static int countNonDecreasing ( int n ) {
  int N = 10 ;
  int count = 1 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    count = ( int ) ( count * ( N + i - 1 ) ) ;
    count = ( int ) ( count / i ) ;
  }
  return count ;
}
|||

COUNT_STRINGS_ADJACENT_CHARACTERS_DIFFERENCE_ONE

public static int countStrs ( int n ) {
  int [ ] [ ] dp = new int [ 27 ] [ n + 1 ] ;
  for ( int j = 0 ;
  j < n ;
  j ++ ) {
    dp [ j ] [ j ] = 0 ;
  }
  for ( int i = 0 ;
  i <= 26 ;
  i ++ ) {
    dp [ 1 ] [ i ] = 1 ;
  }
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= 26 ;
    j ++ ) {
      if ( ( j == 0 ) || ( j == 1 ) ) {
        dp [ i ] [ j ] = dp [ i - 1 ] [ j + 1 ] ;
        ;
      }
      else {
        dp [ i ] [ j ] = ( dp [ i - 1 ] [ j - 1 ] + dp [ i - 1 ] [ j + 1 ] ) ;
        ;
      }
    }
  }
  int sum = 0 ;
  for ( int i = 0 ;
  i <= 26 ;
  i ++ ) {
    sum = sum + dp [ n ] [ i ] ;
  }
  return sum ;
}
|||

PROGRAM_TO_EFFICIENTLY_CALCULATE_EX

public static void exponential ( int n , double x ) {
  double sum = 1.0 ;
  for ( int i = n ;
  i > 0 ;
  i -- ) {
    sum = 1 + x * sum / i ;
  }
  System . out . println ( "e^x =" + sum ) ;
}
|||

EFFICIENTLY_COMPUTE_SUMS_OF_DIAGONALS_OF_A_MATRIX_1

public static void printDiagonalSums ( int [ ] [ ] mat , int n ) {
  int principal = 0 ;
  int secondary = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    principal += mat [ i ] [ i ] ;
    secondary += mat [ i ] [ n - i - 1 ] ;
  }
  System . out . println ( "Principal Diagonal:" + principal ) ;
  System . out . println ( "Secondary Diagonal:" + secondary ) ;
}
|||

PRINT_WAYS_BREAK_STRING_BRACKET_FORM

public static void findCombinations ( String string , int index , String out ) {
  if ( index == string . length ( ) ) System . out . println ( out ) ;
  for ( int i = index ;
  i < string . length ( ) ;
  i += 1 ) findCombinations ( string , i + 1 , out + "(" + string . substring ( index , i + 1 ) + ")" ) ;
}
|||

LINEAR_SEARCH

public static int search ( int arr [ ] , int n , int x ) {
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( arr [ i ] == x ) && ( arr [ i + 1 ] == x ) ) return i ;
  };
  return - 1 ;
}
|||

FIND_THE_ELEMENT_THAT_APPEARS_ONCE_2

public static int singleNumber ( List < Integer > nums ) {
  return ( 3 * sum ( Sets . newHashSet ( nums ) ) . size ( ) - sum ( nums ) ) / 2 ;
}
|||

SEARCH_ALMOST_SORTED_ARRAY

public static int binarySearch ( int [ ] arr , int l , int r , int x ) {
  if ( ( r >= l ) && ( r <= r ) ) {
    int mid = ( int ) ( l + ( r - l ) / 2 ) ;
    if ( ( arr [ mid ] == x ) && ( arr [ mid + 1 ] == x ) ) return mid ;
    if ( ( mid > l && arr [ mid - 1 ] == x ) && ( arr [ mid + 1 ] == x ) ) return ( mid - 1 ) ;
    if ( ( mid < r && arr [ mid + 1 ] == x ) && ( arr [ mid + 1 ] == x ) ) return ( mid + 1 ) ;
    if ( ( arr [ mid ] > x ) && ( arr [ mid ] == x ) ) return binarySearch ( arr , l , mid - 2 , x ) ;
    return binarySearch ( arr , mid + 2 , r , x ) ;
  }
  return - 1 ;
}
|||

EULERS_TOTIENT_FUNCTION_FOR_ALL_NUMBERS_SMALLER_THAN_OR_EQUAL_TO_N

public static void computeTotient ( int n ) {
  int [ ] phi = new int [ n + 2 ] ;
  for ( int i = 0 ;
  i < phi . length ;
  i ++ ) {
    phi [ i ] = 0 ;
  }
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    phi [ i ] = i ;
  }
  for ( int p = 2 ;
  p <= n ;
  p ++ ) {
    if ( ( phi [ p ] == p ) && ( phi [ p ] > 0 ) ) {
      phi [ p ] = p - 1 ;
      for ( int i = 2 * p ;
      i <= n ;
      i += p ) {
        phi [ i ] = ( phi [ i ] / p ) * ( p - 1 ) ;
      }
    }
  }
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    System . out . println ( "Totient of " + i + " is " + phi [ i ] ) ;
  }
}
|||

FIND_MINIMUM_NUMBER_DIVIDED_MAKE_NUMBER_PERFECT_SQUARE

public static int findMinNumber ( int n ) {
  int count = 0 ;
  int ans = 1 ;
  while ( n % 2 == 0 ) {
    count ++ ;
    n /= 2 ;
  }
  if ( count % 2 != 0 ) ans *= 2 ;
  for ( int i = 3 ;
  i < ( int ) ( Math . sqrt ( n ) ) + 1 ;
  i += 2 ) {
    count = 0 ;
    while ( n % i == 0 ) {
      count ++ ;
      n /= i ;
    }
    if ( count % 2 != 0 ) ans *= i ;
  }
  if ( n > 2 ) ans *= n ;
  return ans ;
}
|||

COUNT_NUMBER_WAYS_JUMP_REACH_END

public static void countWaysToJump ( int [ ] arr , int n ) {
  int [ ] countJump = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    countJump [ i ] = 0 ;
  }
  for ( int i = n - 2 ;
  i >= 0 ;
  i -- ) {
    if ( ( arr [ i ] >= n - i - 1 ) && ( arr [ i ] <= arr [ i ] + i ) ) {
      countJump [ i ] ++ ;
    }
    int j = i + 1 ;
    while ( ( j < n - 1 ) && ( j <= arr [ i ] + i ) ) {
      if ( ( countJump [ j ] != - 1 ) && ( countJump [ i ] != - 1 ) ) {
        countJump [ i ] += countJump [ j ] ;
      }
      j ++ ;
    }
    if ( ( countJump [ i ] == 0 ) && ( countJump [ j ] == 0 ) ) {
      countJump [ i ] = - 1 ;
    }
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    System . out . print ( countJump [ i ] + " " ) ;
  }
}
|||

CONVERT_SUBSTRINGS_LENGTH_K_BASE_B_DECIMAL_1

public static void substringConversions ( String str1 , int k , int b ) {
  for ( int i = 0 ;
  i <= str1 . length ( ) - k + 1 ;
  i ++ ) {
    String sub = str1 . substring ( i , k + i ) ;
    int Sum = 0 ;
    int counter = 0 ;
    for ( int i = sub . length ( ) - 1 ;
    i >= 0 ;
    i -- ) {
      Sum = ( Sum + ( ( Character . digit ( sub . charAt ( i ) , 16 ) - '0' ) * Math . pow ( b , counter ) ) ) ;
      counter ++ ;
    }
    System . out . print ( Sum + " " ) ;
  }
}
|||

TWO_ELEMENTS_WHOSE_SUM_IS_CLOSEST_TO_ZERO

public static void minAbsSumPair ( int [ ] arr , int arrSize ) {
  int invCount = 0 ;
  if ( arrSize < 2 ) {
    System . out . println ( "Invalid Input" ) ;
    return ;
  }
  int minL = 0 ;
  int minR = 1 ;
  int minSum = arr [ 0 ] + arr [ 1 ] ;
  for ( int l = 0 ;
  l <= arrSize - 1 ;
  l ++ ) {
    for ( int r = l + 1 ;
    r <= arrSize ;
    r ++ ) {
      int sum = arr [ l ] + arr [ r ] ;
      if ( Math . abs ( minSum ) > Math . abs ( sum ) ) {
        minSum = sum ;
        minL = l ;
        minR = r ;
      }
    }
  }
  System . out . println ( "The two elements whose sum is minimum are" + arr [ minL ] + " and " + arr [ minR ] ) ;
}
|||

HOW_TO_PRINT_MAXIMUM_NUMBER_OF_A_USING_GIVEN_FOUR_KEYS

public static int findoptimal ( int N ) {
  if ( ( N <= 6 ) && ( N > 0 ) ) return N ;
  int [ ] screen = new int [ N ] ;
  screen [ 0 ] = 0 ;
  for ( int n = 1 ;
  n < 7 ;
  n ++ ) screen [ n - 1 ] = n ;
  for ( int n = 7 ;
  n <= N ;
  n ++ ) screen [ n - 1 ] = Math . max ( 2 * screen [ n - 4 ] , Math . max ( 3 * screen [ n - 5 ] , 4 * screen [ n - 6 ] ) ) ;
  ;
  return screen [ N - 1 ] ;
}
|||

PROGRAM_DECIMAL_BINARY_CONVERSION_2

public static int decimalToBinary ( int N ) {
  int B_Number = 0 ;
  int cnt = 0 ;
  while ( ( N != 0 ) && ( N % 2 == 0 ) ) {
    int rem = N % 2 ;
    int c = Math . pow ( 10 , cnt ) ;
    B_Number += rem * c ;
    N /= 2 ;
    cnt ++ ;
  }
  return B_Number ;
}
|||

COUNTS_PATHS_POINT_REACH_ORIGIN_1

public static int countPaths ( int n , int m ) {
  if ( ( n == 0 || m == 0 ) && ( n > m ) ) return 1 ;
  return ( countPaths ( n - 1 , m ) + countPaths ( n , m - 1 ) ) ;
}
|||

SUM_ELEMENTS_K1TH_K2TH_SMALLEST_ELEMENTS

public static int sumBetweenTwoKth ( int [ ] arr , int n , int k1 , int k2 ) {
  Arrays . sort ( arr ) ;
  int result = 0 ;
  for ( int i = k1 ;
  i <= k2 - 1 ;
  i ++ ) {
    result += arr [ i ] ;
  }
  return result ;
}
|||

SMALLEST_SUBARRAY_K_DISTINCT_NUMBERS

public static void minRange ( int [ ] arr , int n , int k ) {
  int l = 0 ;
  int r = n ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    String [ ] s = new String [ n ] ;
    for ( int j = i ;
    j < n ;
    j ++ ) {
      s [ j ] = arr [ j ] ;
      if ( ( s [ j ] . length ( ) == k ) && ( ( s [ j ] . length ( ) - l ) < ( r - l ) ) ) {
        r = j ;
        l = i ;
      }
      break ;
    }
    if ( ( j == n ) && ( l == 0 ) ) break ;
  }
  if ( ( l == 0 ) && ( r == n ) ) System . out . println ( "Invalid k" ) ;
  else System . out . println ( l + " " + r ) ;
}
|||

AREA_OF_A_HEXAGON

public static double hexagonArea ( double s ) {
  return ( ( 3 * Math . sqrt ( 3 ) * ( s * s ) ) / 2 ) ;
  ;
}
|||

NEXT_POWER_OF_2_2

public static int nextPowerOf2 ( int n ) {
  n -- ;
  n |= n >> 1 ;
  n |= n >> 2 ;
  n |= n >> 4 ;
  n |= n >> 8 ;
  n |= n >> 16 ;
  n ++ ;
  return n ;
}
|||

COUNT_SUBSTRINGS_BINARY_STRING_CONTAINING_K_ONES

public static int countOfSubstringWithKOnes ( String s , int K ) {
  int N = s . length ( ) ;
  int res = 0 ;
  int countOfOne = 0 ;
  int [ ] freq = new int [ N + 1 ] ;
  freq [ 0 ] = 1 ;
  for ( int i = 0 ;
  i < N ;
  i += 1 ) {
    countOfOne += Character . digit ( s . charAt ( i ) , 10 ) - '0' ;
    if ( ( countOfOne >= K ) && ( countOfOne < N ) ) {
      res += freq [ countOfOne - K ] ;
    }
    freq [ countOfOne ] ++ ;
  }
  return res ;
}
|||

NUMBER_INDEXES_EQUAL_ELEMENTS_GIVEN_RANGE

public static int answerQuery ( int [ ] a , int n , int l , int r ) {
  int count = 0 ;
  for ( int i = l ;
  i < r ;
  i ++ ) {
    if ( ( a [ i ] == a [ i + 1 ] ) && ( n == a [ i ] ) ) {
      count ++ ;
    }
  }
  return count ;
}
|||

CHECK_WHETHER_NUMBER_DUCK_NUMBER_NOT

public static int checkDuck ( String num ) {
  int l = num . length ( ) ;
  int countZero = 0 ;
  int i = 1 ;
  while ( i < l ) {
    char ch = num . charAt ( i ) ;
    if ( ( ch == '0' ) || ( ch == '1' ) || ( ch == '2' ) || ( ch == '3' ) || ( ch == '4' ) || ( ch == '5' ) || ( ch == '6' ) || ( ch == '7' ) || ( ch == '8' ) || ( ch == '9' ) ) {
      countZero = countZero + 1 ;
    }
    i = i + 1 ;
  }
  return countZero ;
}
|||

NUMBER_NON_NEGATIVE_INTEGRAL_SOLUTIONS_B_C_N_1

public static int countIntegralSolutions ( int n ) {
  return ( int ) ( ( ( n + 1 ) * ( n + 2 ) ) / 2 ) ;
}
|||

MAXIMUM_PROFIT_BY_BUYING_AND_SELLING_A_SHARE_AT_MOST_K_TIMES_1

public static int maxProfit ( int [ ] price , int n , int k ) {
  int [ ] [ ] profit = new int [ n + 1 ] [ k + 1 ] ;
  for ( int i = 1 ;
  i <= k ;
  i ++ ) {
    profit [ i - 1 ] = new int [ n + 1 ] ;
  }
  for ( int i = 1 ;
  i <= k ;
  i ++ ) {
    int prevDiff = Integer . MAX_VALUE ;
    for ( int j = 1 ;
    j <= n ;
    j ++ ) {
      prevDiff = Math . max ( prevDiff , profit [ i - 1 ] [ j - 1 ] - price [ j - 1 ] ) ;
      profit [ i ] [ j ] = Math . max ( profit [ i ] [ j - 1 ] , price [ j ] + prevDiff ) ;
    }
  }
  return profit [ k ] [ n - 1 ] ;
}
|||

COUNT_CHARACTERS_POSITION_ENGLISH_ALPHABETS

public static int findCount ( String str ) {
  int result = 0 ;
  for ( int i = 0 ;
  i < str . length ( ) ;
  i ++ ) {
    if ( ( ( i == Character . MAX_VALUE ) || ( i == Character . MIN_VALUE ) ) && ( str . charAt ( i ) == 'a' ) ) {
      result ++ ;
    }
  }
  return result ;
}
|||

COUNT_GFG_SUBSEQUENCES_GIVEN_STRING

public static void countSubsequence ( String s , int n ) {
  int cntG = 0 ;
  int cntF = 0 ;
  int result = 0 ;
  int C = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( s . charAt ( i ) == 'G' ) && ( s . charAt ( i ) == 'F' ) ) {
      cntG ++ ;
      result += C ;
      continue ;
    }
    if ( ( s . charAt ( i ) == 'F' ) && ( s . charAt ( i ) == 'G' ) ) {
      cntF ++ ;
      C += cntG ;
      continue ;
    }
    else continue ;
  }
  System . out . println ( result ) ;
}
|||

FIND_SMALLEST_VALUE_REPRESENTED_SUM_SUBSET_GIVEN_ARRAY

public static int findSmallest ( int [ ] arr , int n ) {
  int res = 1 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( arr [ i ] <= res ) {
      res = res + arr [ i ] ;
    }
    else {
      break ;
    }
  }
  return res ;
}
|||

MAXIMUM_POINTS_COLLECTED_BY_TWO_PERSONS_ALLOWED_TO_MEET_ONCE

public static int findMaxPoints ( int [ ] A ) {
  P1S = new int [ N + 2 ] ;
  P1E = new int [ M + 2 ] ;
  P2S = new int [ N + 2 ] ;
  P2E = new int [ M + 2 ] ;
  for ( int i = 1 ;
  i <= N ;
  i ++ ) {
    for ( int j = 1 ;
    j <= M ;
    j ++ ) {
      P1S [ i ] [ j ] = Math . max ( P1S [ i - 1 ] [ j ] , P1S [ i ] [ j - 1 ] ) + A [ i - 1 ] [ j - 1 ] ;
    }
  }
  for ( int i = N ;
  i <= M ;
  i ++ ) {
    for ( int j = 1 ;
    j <= N ;
    j ++ ) {
      P1S [ i ] [ j ] = Math . max ( P1S [ i - 1 ] [ j ] , P1S [ i ] [ j - 1 ] ) + A [ i - 1 ] [ j - 1 ] ;
    }
  }
  for ( int i = N ;
  i <= M ;
  i ++ ) {
    for ( int j = 1 ;
    j <= M ;
    j ++ ) {
      P1E [ i ] [ j ] = Math . max ( P1E [ i + 1 ] [ j ] , P1E [ i ] [ j + 1 ] ) + A [ i - 1 ] [ j - 1 ] ;
    }
  }
  for ( int i = N ;
  i <= M ;
  i ++ ) {
    for ( int j = 1 ;
    j <= M ;
    j ++ ) {
      P2S [ i ] [ j ] = Math . max ( P2S [ i + 1 ] [ j ] , P2S [ i ] [ j - 1 ] ) + A [ i - 1 ] [ j - 1 ] ;
    }
  }
  for ( int i = 1 ;
  i <= N ;
  i ++ ) {
    for ( int j = M ;
    j <= N ;
    j ++ ) {
      P2E [ i ] [ j ] = Math . max ( P2E [ i - 1 ] [ j ] , P2E [ i ] [ j + 1 ] ) + A [ i - 1 ] [ j - 1 ] ;
    }
  }
  int ans = 0 ;
  for ( int i = 2 ;
  i <= N ;
  i ++ ) {
    for ( int j = 2 ;
    j <= M ;
    j ++ ) {
      op1 = P1S [ i ] [ j - 1 ] + P1E [ i ]
|||

PROGRAM_FIND_CIRCUMFERENCE_CIRCLE

public static double circumference ( double r ) {
  return ( 2 * PI * r ) ;
}
|||

QUICKLY_FIND_MULTIPLE_LEFT_ROTATIONS_OF_AN_ARRAY

public static void leftRotate ( int [ ] arr , int n , int k ) {
  for ( int i = k ;
  i < k + n ;
  i ++ ) {
    System . out . print ( Integer . toString ( arr [ i % n ] ) + " " ) ;
  }
}
|||

MINIMUM_SUM_CHOOSING_MINIMUM_PAIRS_ARRAY

static int minSum ( int [ ] A ) {
  int minVal = Math . min ( A ) ;
  ;
  return minVal * ( A . length - 1 ) ;
}
|||

RECURSIVE_PROGRAM_PRIME_NUMBER

public static boolean isPrime ( int n , int i ) {
  if ( ( n <= 2 ) && ( n == 2 ) ) return true ? ( n == 2 ) : false ;
  if ( ( n % i == 0 ) && ( i * i > n ) ) return false ;
  return isPrime ( n , i + 1 ) ;
}
|||

SPARSE_SEARCH

public static int sparseSearch ( String arr , int key , int low , int high ) {
  int left = 0 ;
  int right = 0 ;
  while ( low <= high ) {
    int mid = ( low + high ) / 2 ;
    if ( arr . charAt ( mid ) == '\0' ) {
      left = mid - 1 ;
      right = mid + 1 ;
      if ( left < low && right > high ) {
        return - 1 ;
      }
      else if ( right <= high && arr . charAt ( right ) != '\0' ) {
        mid = right ;
      }
      else if ( left >= low && arr . charAt ( left ) != '\0' ) {
        mid = left ;
      }
    }
    if ( arr . charAt ( mid ) == key ) {
      System . out . println ( "Found string {
}
 at index {
}" . format ( arr . charAt ( mid ) , mid ) ) ;
      return 0 ;
    }
    else if ( arr . charAt ( mid ) > key ) {
      high = mid - 1 ;
    }
    else if ( arr . charAt ( mid ) < key ) {
      low = mid + 1 ;
    }
    left -- ;
    right ++ ;
  }
  return - 1 ;
}
|||

FIND_NUMBER_TIMES_STRING_OCCURS_GIVEN_STRING

public static int count ( int [ ] a , int [ ] b , int m , int n ) {
  if ( ( ( m == 0 && n == 0 ) || n == 0 ) || ( m == 0 ) ) return 1 ;
  if ( ( m == 0 ) || ( n == 0 ) ) return 0 ;
  if ( ( a [ m - 1 ] == b [ n - 1 ] ) && ( a [ m - 1 ] == b [ n - 1 ] ) ) return ( count ( a , b , m - 1 , n - 1 ) + count ( a , b , m - 1 , n ) ) ;
  else return count ( a , b , m - 1 , n ) ;
}
|||

PROGRAM_CHECK_ARRAY_SORTED_NOT_ITERATIVE_RECURSIVE_1

public static boolean arraySortedOrNot ( int [ ] arr , int n ) {
  if ( ( n == 0 || n == 1 ) && ( arr [ 0 ] > arr [ 1 ] ) ) return true ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) if ( ( arr [ i - 1 ] > arr [ i ] ) && ( arr [ i ] > arr [ i + 1 ] ) ) return false ;
  return true ;
}
|||

FIND_INDEX_0_REPLACED_1_GET_LONGEST_CONTINUOUS_SEQUENCE_1S_BINARY_ARRAY

public static int maxOnesIndex ( int [ ] arr , int n ) {
  int maxCount = 0 ;
  int maxIndex = 0 ;
  int prevZero = - 1 ;
  int prevPrevZero = - 1 ;
  for ( int curr = 0 ;
  curr < n ;
  curr ++ ) {
    if ( ( arr [ curr ] == 0 ) && ( arr [ curr ] > prevZero ) ) {
      if ( ( curr - prevPrevZero > maxCount ) && ( arr [ curr ] > prevZero ) ) {
        maxCount = curr - prevPrevZero ;
        maxIndex = prevZero ;
      }
      prevPrevZero = prevZero ;
      prevZero = curr ;
    }
  }
  if ( ( n - prevPrevZero > maxCount ) && ( arr [ n - prevZero ] > prevZero ) ) {
    maxIndex = prevZero ;
  }
  return maxIndex ;
}
|||

FIND_MAXIMUM_PRODUCT_OF_A_TRIPLET_IN_ARRAY_1

public static int maxProduct ( int [ ] arr , int n ) {
  if ( n < 3 ) return - 1 ;
  Arrays . sort ( arr ) ;
  return Math . max ( arr [ 0 ] * arr [ 1 ] * arr [ n - 1 ] , arr [ n - 1 ] * arr [ n - 2 ] * arr [ n - 3 ] ) ;
}
|||

COORDINATES_RECTANGLE_GIVEN_POINTS_LIE_INSIDE

public static void printRect ( int X , int Y , int n ) {
  int Xmax = Math . max ( X ) ;
  int Xmin = Math . min ( X ) ;
  int Ymax = Math . max ( Y ) ;
  int Ymin = Math . min ( Y ) ;
  System . out . print ( "{" + Xmin + ", " + Ymin + "}" + "\n" ) ;
  System . out . print ( "{" + Xmin + ", " + Ymax + "}" + "\n" ) ;
  System . out . print ( "{" + Xmax + ", " + Ymax + "}" + "\n" ) ;
  System . out . print ( "{" + Xmax + ", " + Ymin + "}" + "\n" ) ;
}
|||

COUNT_BINARY_DIGIT_NUMBERS_SMALLER_N

public static int countOfBinaryNumberLessThanN ( int N ) {
  Deque < Integer > q = new LinkedList < Integer > ( ) ;
  q . add ( 1 ) ;
  int cnt = 0 ;
  while ( ( q . size ( ) > 0 ) && ( cnt < N ) ) {
    int t = q . poll ( ) ;
    if ( ( t <= N ) && ( t > 0 ) ) {
      cnt = cnt + 1 ;
      q . add ( t * 10 ) ;
      q . add ( t * 10 + 1 ) ;
    }
  }
  return cnt ;
}
|||

CONVERT_DECIMAL_FRACTION_BINARY_NUMBER

public static String decimalToBinary ( int num , int k_prec ) {
  String binary = "" ;
  int Integral = Integer . MIN_VALUE ;
  int fractional = num - Integral ;
  while ( ( Integral ) > 0 ) {
    int rem = Integral % 2 ;
    binary += Integer . toString ( rem ) ;
    ;
    Integral /= 2 ;
  }
  binary = binary . substring ( 0 , binary . length ( ) - 1 ) ;
  binary += '.' ;
  while ( ( k_prec ) > 0 ) {
    fractional *= 2 ;
    int fractBit = Integer . MIN_VALUE ;
    if ( ( fractBit == 1 ) && ( fractional >= 0 ) ) {
      fractional -= fractBit ;
      binary += '1' ;
    }
    else {
      binary += '0' ;
    }
    k_prec -- ;
  }
  return binary ;
}
|||

MAXIMUM_NUMBER_OF_TRAILING_ZEROS_IN_THE_PRODUCT_OF_THE_SUBSETS_OF_SIZE_K

public static int maximumZeros ( int [ ] arr , int n , int k ) {
  MAX5 = n ;
  int [ ] [ ] subset = new int [ k + 1 ] [ n ] ;
  subset [ 0 ] [ 0 ] = 0 ;
  for ( int p = 0 ;
  p < arr . length ;
  p ++ ) {
    int pw2 = 0 , pw5 = 0 ;
    while ( ! p % 2 ) {
      pw2 ++ ;
      p /= 2 ;
    }
    while ( ! p % 5 ) {
      pw5 ++ ;
      p /= 5 ;
    }
    for ( int i = k - 1 ;
    i >= 0 ;
    i -- ) {
      for ( int j = 0 ;
      j < MAX5 ;
      j ++ ) {
        if ( subset [ i ] [ j ] != - 1 ) {
          subset [ i + 1 ] [ j + pw5 ] = ( int ) Math . max ( subset [ i + 1 ] [ j + pw5 ] , ( subset [ i ] [ j ] + pw2 ) ) ;
        }
      }
    }
  }
  int ans = 0 ;
  for ( int i = 0 ;
  i < MAX5 ;
  i ++ ) {
    ans = Math . max ( ans , Math . min ( i , subset [ k ] [ i ] ) ) ;
  }
  return ans ;
}
|||

SEARCH_AN_ELEMENT_IN_A_SORTED_AND_PIVOTED_ARRAY

public static int search ( int [ ] arr , int l , int h , int key ) {
  if ( l > h ) return - 1 ;
  int mid = ( l + h ) / 2 ;
  if ( arr [ mid ] == key ) return mid ;
  if ( arr [ l ] <= arr [ mid ] ) {
    if ( key >= arr [ l ] && key <= arr [ mid ] ) return search ( arr , l , mid - 1 , key ) ;
    return search ( arr , mid + 1 , h , key ) ;
  }
  if ( key >= arr [ mid ] && key <= arr [ h ] ) return search ( a , mid + 1 , h , key ) ;
  return search ( arr , l , mid - 1 , key ) ;
}
|||

PROGRAM_FIND_AREA_CIRCULAR_SEGMENT

public static double areaOfSegment ( double radius , double angle ) {
  double areaOfSector = Math . PI * ( radius * radius ) ;
  * ( angle / 360 ) = 0 ;
  double areaOfTriangle = 1 / 2 * ( radius * radius ) ;
  * Math . sin ( ( angle * Math . PI ) / 180 ) = 0 ;
  return areaOfSector - areaOfTriangle ;
  ;
}
|||

K_SMALLEST_ELEMENTS_ORDER_USING_O1_EXTRA_SPACE

public static void printSmall ( int [ ] arr , int n , int k ) {
  for ( int i = k ;
  i < n ;
  i ++ ) {
    int maxVar = arr [ k - 1 ] ;
    int pos = k - 1 ;
    for ( int j = k - 2 ;
    j >= 0 ;
    j -- ) {
      if ( ( arr [ j ] > maxVar ) && ( arr [ j ] < maxVar ) ) {
        maxVar = arr [ j ] ;
        pos = j ;
      }
    }
    if ( ( maxVar > arr [ i ] ) && ( arr [ i ] < maxVar ) ) {
      int j = pos ;
      while ( ( j < k - 1 ) && ( arr [ j ] > maxVar ) && ( arr [ j ] < maxVar ) ) {
        arr [ j ] = arr [ j + 1 ] ;
        j ++ ;
      }
      arr [ k - 1 ] = arr [ i ] ;
    }
  }
  for ( int i = 0 ;
  i <= k ;
  i ++ ) {
    System . out . print ( arr [ i ] + " " ) ;
  }
}
|||

NTH_NON_FIBONACCI_NUMBER

public static int nonFibonacci ( int n ) {
  int prevPrev = 1 ;
  int prev = 2 ;
  int curr = 3 ;
  while ( n > 0 ) {
    prevPrev = prev ;
    prev = curr ;
    curr = prevPrev + prev ;
    n = n - ( curr - prev - 1 ) ;
  }
  n = n + ( curr - prev - 1 ) ;
  return prev + n ;
}
|||

ANALYSIS_OF_ALGORITHMS_SET_2_ASYMPTOTIC_ANALYSIS

public static int search ( int arr [ ] , int n , int x ) {
  int i ;
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( arr [ i ] == x ) && ( arr [ i + 1 ] == x ) ) {
      return i ;
    }
  }
  return - 1 ;
}
|||

ZECKENDORFS_THEOREM_NON_NEIGHBOURING_FIBONACCI_REPRESENTATION

public static int nearestSmallerEqFib ( int n ) {
  if ( ( n == 0 || n == 1 ) && ( n == 2 ) ) return n ;
  int f1 = 0 , f2 = 1 , f3 = 1 ;
  while ( ( f3 = f1 + f2 ) <= n ) {
    f1 = f2 ;
    f2 = f3 ;
    f3 = f1 + f2 ;
  }
  return f2 ;
}
|||

PRINT_MAXIMUM_SHORTEST_DISTANCE

public static int findMaximum ( int [ ] a , int n , int k ) {
  Map < Integer , Integer > b = Maps . newHashMap ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int x = a [ i ] ;
    int d = Math . min ( 1 + i , n - i ) ;
    if ( x != 0 ) {
      b . put ( x , d ) ;
    }
    else {
      b . put ( x , Math . min ( d , b . get ( x ) ) ) ;
    }
  }
  int ans = 10 * 9 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int x = a [ i ] ;
    if ( ( x != ( k - x ) && ( k - x ) < b . keySet ( ) . size ( ) ) || ( x != ( k - x ) && ( k - x ) < b . keySet ( ) . size ( ) ) ) {
      ans = Math . min ( Math . max ( b . get ( x ) , b . get ( k - x ) ) , ans ) ;
    }
  }
  return ans ;
}
|||

GENERATING_DISTINCT_SUBSEQUENCES_OF_A_GIVEN_STRING_IN_LEXICOGRAPHIC_ORDER

public static void generate ( Set < String > st , String s ) {
  if ( s . length ( ) == 0 ) return ;
  if ( s != null ) {
    st . add ( s ) ;
    for ( int i = 0 ;
    i < s . length ( ) ;
    i ++ ) {
      String t = Arrays . copyOfRange ( s , i , i + 1 ) . trim ( ) ;
      t = t . replaceAll ( "\\s+" , "" ) ;
      generate ( st , t ) ;
    }
  }
}
|||

WRITE_YOU_OWN_POWER_WITHOUT_USING_MULTIPLICATION_AND_DIVISION

public static double pow ( double a , int b ) {
  if ( ( b == 0 ) || ( b == 1 ) ) return 1 ;
  double answer = a ;
  double increment = a ;
  for ( int i = 1 ;
  i <= b ;
  i ++ ) {
    for ( int j = 1 ;
    j <= a ;
    j ++ ) {
      answer += increment ;
    }
    increment = answer ;
  }
  return answer ;
}
|||

MAXIMIZE_VOLUME_CUBOID_GIVEN_SUM_SIDES_1

public static int maxvolume ( int s ) {
  int length = ( int ) ( s / 3 ) ;
  s -= length ;
  int breadth = s / 2 ;
  int height = s - breadth ;
  return ( int ) ( length * breadth * height ) ;
}
|||

HORNERS_METHOD_POLYNOMIAL_EVALUATION

public static double horner ( double [ ] poly , int n , double x ) {
  double result = poly [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    result = result * x + poly [ i ] ;
  }
  return result ;
}
|||

MINIMUM_TIME_REQUIRED_PRODUCE_M_ITEMS

public static int minTime ( int [ ] arr , int n , int m ) {
  int t = 0 ;
  while ( ( 1 ) ) {
    int items = 0 ;
    for ( int i = 0 ;
    i < n ;
    i ++ ) {
      items += ( t / arr [ i ] ) ;
    }
    if ( ( items >= m ) && ( items < n ) ) {
      return t ;
    }
    t ++ ;
  }
}
|||

FIND_DIFFERENCE_BETWEEN_SUMS_OF_TWO_DIAGONALS

public static int difference ( int [ ] [ ] arr , int n ) {
  int d1 = 0 ;
  int d2 = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      if ( ( i == j ) && ( i != n - j - 1 ) ) {
        d1 += arr [ i ] [ j ] ;
      }
      if ( ( i == n - j - 1 ) && ( i != n - j - 1 ) ) {
        d2 += arr [ i ] [ j ] ;
      }
    }
  }
  return Math . abs ( d1 - d2 ) ;
  ;
}
|||

SHORTEST_UNCOMMON_SUBSEQUENCE

public static int shortestSeq ( String S , String T ) {
  int m = S . length ( ) ;
  int n = T . length ( ) ;
  int [ ] [ ] dp = new int [ n + 1 ] [ m + 1 ] ;
  for ( int j = 0 ;
  j < m + 1 ;
  j ++ ) dp [ j ] [ 0 ] = 1 ;
  for ( int i = 0 ;
  i < m + 1 ;
  i ++ ) dp [ i ] [ 0 ] = MAX ;
  for ( int i = 1 ;
  i < m ;
  i ++ ) {
    for ( int j = 1 ;
    j < n ;
    j ++ ) {
      char ch = S . charAt ( i - 1 ) ;
      int k = j - 1 ;
      while ( k >= 0 ) {
        if ( T . charAt ( k ) == ch ) break ;
        k -- ;
      }
      if ( k == - 1 ) dp [ i ] [ j ] = 1 ;
      else dp [ i ] [ j ] = Math . min ( dp [ i - 1 ] [ j ] , dp [ i - 1 ] [ k ] + 1 ) ;
    }
  }
  int ans = dp [ m ] [ n ] ;
  if ( ans >= MAX ) ans = - 1 ;
  return ans ;
}
|||

MIN_FLIPS_OF_CONTINUOUS_CHARACTERS_TO_MAKE_ALL_CHARACTERS_SAME_IN_A_STRING

public static int findFlips ( String str , int n ) {
  char last = ' ' ;
  int res = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( last != str . charAt ( i ) ) && ( last != ' ' ) ) {
      res ++ ;
    }
    last = str . charAt ( i ) ;
  }
  return res / 2 ;
}
|||

DYNAMIC_PROGRAMMING_SET_28_MINIMUM_INSERTIONS_TO_FORM_A_PALINDROME

public static int findMinInsertions ( String str , int l , int h ) {
  if ( ( l > h ) || ( l == h ) ) return Integer . MAX_VALUE ;
  if ( ( l == h ) || ( l == h - 1 ) ) return 0 ;
  if ( ( str . charAt ( l ) == str . charAt ( h ) ) && ( str . charAt ( l ) == str . charAt ( h ) ) ) return findMinInsertions ( str , l + 1 , h - 1 ) ;
  else return ( Math . min ( findMinInsertions ( str , l , h - 1 ) , findMinInsertions ( str , l + 1 , h ) ) + 1 ) ;
}
|||

COUNT_CHARACTERS_STRING_DISTANCE_ENGLISH_ALPHABETS

public static int countPairs ( String str1 ) {
  int result = 0 ;
  ;
  int n = str1 . length ( ) ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= n ;
    j ++ ) {
      if ( ( Math . abs ( ( char ) str1 . charAt ( i ) - ( char ) str1 . charAt ( j ) ) ) == Math . abs ( i - j ) ) {
        result ++ ;
      };
    }
  }
  return result ;
}
|||

MULTISTAGE_GRAPH_SHORTEST_PATH

public static int shortestDist ( int [ ] [ ] graph ) {
  static final int INF = - 1 ;
  int [ ] dist = new int [ N ] ;
  dist [ N - 1 ] = 0 ;
  for ( int i = N - 2 ;
  i >= 0 ;
  i -- ) {
    dist [ i ] = INF ;
    for ( int j = 0 ;
    j < N ;
    j ++ ) {
      if ( graph [ i ] [ j ] == INF ) continue ;
      dist [ i ] = Math . min ( dist [ i ] , graph [ i ] [ j ] + dist [ j ] ) ;
    }
  }
  return dist [ 0 ] ;
}
|||

MAXIMUM_SIZE_SUB_MATRIX_WITH_ALL_1S_IN_A_BINARY_MATRIX

public static void printMaxSubSquare ( int [ ] [ ] M ) {
  int R = M . length ;
  int C = M [ 0 ] . length ;
  int [ ] [ ] S = new int [ C ] [ R ] ;
  for ( int l = 0 ;
  l < R ;
  l ++ ) {
    for ( int i = 1 ;
    i < R ;
    i ++ ) {
      for ( int j = 1 ;
      j < C ;
      j ++ ) {
        if ( ( M [ i ] [ j ] == 1 ) && ( M [ i ] [ j ] == 1 ) ) {
          S [ i ] [ j ] = Math . min ( S [ i ] [ j - 1 ] , S [ i - 1 ] [ j ] ) + 1 ;
        }
        else {
          S [ i ] [ j ] = 0 ;
        }
      }
    }
  }
  int maxOfS = S [ 0 ] [ 0 ] ;
  int maxI = 0 ;
  int maxJ = 0 ;
  for ( int i = 0 ;
  i < R ;
  i ++ ) {
    for ( int j = 0 ;
    j < C ;
    j ++ ) {
      if ( ( maxOfS < S [ i ] [ j ] ) && ( M [ i ] [ j ] == 1 ) ) {
        maxOfS = S [ i ] [ j ] ;
        maxI = i ;
        maxJ = j ;
      }
    }
  }
  System . out . print ( "Maximum size sub-matrix is: " ) ;
  for ( int i = maxI ;
  i < maxI - maxOfS ;
  i ++ ) {
    for ( int j = maxJ ;
    j < maxJ - maxOfS ;
    j ++ ) {
      System . out . print ( M [ i ] [ j ] + "" ) ;
    }
    System . out . println ( "" ) ;
  }
}
|||

GIVEN_SORTED_ARRAY_NUMBER_X_FIND_PAIR_ARRAY_WHOSE_SUM_CLOSEST_X

public static void printClosest ( int [ ] arr , int n , int x ) {
  int resL = 0 , resR = 0 ;
  int l = 0 , r = n - 1 , diff = MAX_VAL ;
  while ( r > l ) {
    if ( Math . abs ( arr [ l ] + arr [ r ] - x ) < diff ) {
      resL = l ;
      resR = r ;
      diff = Math . abs ( arr [ l ] + arr [ r ] - x ) ;
    }
    if ( arr [ l ] + arr [ r ] > x ) {
      r -- ;
    }
    else {
      l ++ ;
    }
  }
  System . out . println ( "The closest pair is {
}
 and {
}" . format ( arr [ resL ] , arr [ resR ] ) ) ;
}
|||

SORT_1_N_SWAPPING_ADJACENT_ELEMENTS_1

public static boolean sortedAfterSwap ( int [ ] A , int [ ] B , int n ) {
  for ( int i = 0 ;
  i <= n - 1 ;
  i ++ ) {
    if ( B [ i ] ) {
      if ( A [ i ] != i + 1 ) {
        A [ i ] = A [ i + 1 ] ;
      }
    }
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( A [ i ] != i + 1 ) {
      return false ;
    }
  }
  return true ;
}
|||

TILE_STACKING_PROBLEM

public static int possibleWays ( int n , int m , int k ) {
  int [ ] [ ] dp = new int [ 10 ] [ 10 ] ;
  int [ ] [ ] presum = new int [ 10 ] [ 10 ] ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    dp [ 0 ] [ i ] = 0 ;
    presum [ 0 ] [ i ] = 1 ;
  }
  for ( int i = 0 ;
  i <= m ;
  i ++ ) {
    presum [ i ] [ 0 ] = 1 ;
    dp [ i ] [ 0 ] = 1 ;
  }
  for ( int i = 1 ;
  i <= m ;
  i ++ ) {
    for ( int j = 1 ;
    j <= n ;
    j ++ ) {
      dp [ i ] [ j ] = presum [ i - 1 ] [ j ] ;
      if ( j > k ) {
        dp [ i ] [ j ] -= presum [ i - 1 ] [ j - k - 1 ] ;
      }
    }
    for ( int j = 1 ;
    j <= n ;
    j ++ ) {
      presum [ i ] [ j ] = dp [ i ] [ j ] + presum [ i ] [ j - 1 ] ;
    }
  }
  return dp [ m ] [ n ] ;
}
|||

NUMBER_OF_PAIRS_IN_AN_ARRAY_HAVING_SUM_EQUAL_TO_PRODUCT

public static int sumEqualProduct ( int [ ] a , int n ) {
  int zero = 0 ;
  int two = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( a [ i ] == 0 ) zero ++ ;
    if ( a [ i ] == 2 ) two ++ ;
  }
  int cnt = ( zero * ( zero - 1 ) ) / 2 + ( two * ( two - 1 ) ) / 2 ;
  return cnt ;
}
|||

DYNAMIC_PROGRAMMING_SET_17_PALINDROME_PARTITIONING

public static int minPalPartion ( String str ) {
  int n = str . length ( ) ;
  int [ ] [ ] C = new int [ n ] [ n ] ;
  boolean [ ] [ ] P = new boolean [ n ] [ n ] ;
  int j ;
  int k ;
  int L ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    P [ i ] [ i ] = true ;
    ;
    C [ i ] [ i ] = 0 ;
  };
  for ( L = 2 ;
  L <= n ;
  L ++ ) {
    for ( int i = 0 ;
    i < n - L + 1 ;
    i ++ ) {
      j = i + L - 1 ;
      if ( L == 2 ) P [ i ] [ j ] = ( str . charAt ( i ) == str . charAt ( j ) ) ;
      else P [ i ] [ j ] = ( ( str . charAt ( i ) == str . charAt ( j ) ) && P [ i + 1 ] [ j - 1 ] ) ;
      if ( P [ i ] [ j ] == true ) C [ i ] [ j ] = 0 ;
      else {
        C [ i ] [ j ] = 100000000 ;
        for ( k = i ;
        k < j ;
        k ++ ) C [ i ] [ j ] = Math . min ( C [ i ] [ j ] , C [ i ] [ k ] + C [ k + 1 ] [ j ] + 1 ) ;
      }
    }
  }
  return C [ 0 ] [ n - 1 ] ;
}
|||

FIND_ONE_MULTIPLE_REPEATING_ELEMENTS_READ_ARRAY

public static int findRepeatingNumber ( int [ ] arr , int n ) {
  double sq = Math . sqrt ( n ) ;
  int range__ = ( int ) ( ( n / sq ) + 1 ) ;
  int [ ] count = new int [ range__ ] ;
  for ( int i = 0 ;
  i < n ;
  i += 1 ) {
    count [ ( int ) ( ( arr [ i ] - 1 ) / sq ) ] ++ ;
  }
  int selectedBlock = range__ - 1 ;
  for ( int i = 0 ;
  i < range__ - 1 ;
  i += 1 ) {
    if ( ( count [ i ] > sq ) && ( count [ i ] <= ( ( selectedBlock + 1 ) * sq ) ) ) {
      selectedBlock = i ;
      break ;
    }
  }
  int [ ] m = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i += 1 ) {
    if ( ( ( ( selectedBlock * sq ) < arr [ i ] ) && ( arr [ i ] <= ( ( selectedBlock + 1 ) * sq ) ) ) ) {
      m [ arr [ i ] ] ++ ;
      if ( ( m [ arr [ i ] ] > 1 ) && ( m [ arr [ i ] ] > 0 ) ) {
        return arr [ i ] ;
      }
    }
  }
  return - 1 ;
}
|||

MINIMUM_SUM_PATH_TRIANGLE

public static int minSumPath ( int [ ] [ ] A ) {
  int [ ] memo = new int [ A . length ] ;
  memo [ 0 ] = 0 ;
  int n = A . length - 1 ;
  for ( int i = 0 ;
  i < A [ n ] . length ;
  i ++ ) memo [ i ] = A [ n ] [ i ] ;
  for ( int i = A . length - 2 ;
  i >= 0 ;
  i -- ) {
    for ( int j = 0 ;
    j < A [ i ] . length ;
    j ++ ) memo [ j ] = A [ i ] [ j ] + Math . min ( memo [ j ] , memo [ j + 1 ] ) ;
    ;
  }
  return memo [ 0 ] ;
}
|||

HOW_CAN_WE_SUM_THE_DIGITS_OF_A_GIVEN_NUMBER_IN_SINGLE_STATEMENT_1

public static int getSum ( int n ) {
  int sum = 0 ;
  while ( ( n > 0 ) && ( n % 10 == 0 ) ) {
    sum += ( int ) ( n % 10 ) ;
    n = ( int ) ( n / 10 ) ;
  }
  return sum ;
}
|||

RECURSION

static void printFun ( int test ) {
  if ( ( test < 1 ) || ( test > 2 ) ) {
    return ;
  }
  else {
    System . out . print ( test + " " ) ;
    printFun ( test - 1 ) ;
    System . out . print ( test + " " ) ;
    return ;
  }
}
|||

MAXIMUM_TRIPLET_SUM_ARRAY

public static int maxTripletSum ( int [ ] arr , int n ) {
  int sm = - 1000000 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= n ;
    j ++ ) {
      for ( int k = j + 1 ;
      k <= n ;
      k ++ ) {
        if ( ( sm < ( arr [ i ] + arr [ j ] + arr [ k ] ) ) && ( sm > ( arr [ i ] + arr [ j ] + arr [ k ] ) ) ) {
          sm = arr [ i ] + arr [ j ] + arr [ k ] ;
        }
      }
    }
  }
  return sm ;
}
|||

MINIMUM_NUMBER_OF_JUMPS_TO_REACH_END_OF_A_GIVEN_ARRAY_1

public static double minJumps ( int [ ] arr , int n ) {
  int [ ] jumps = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) jumps [ i ] = 0 ;
  if ( ( n == 0 ) || ( arr [ 0 ] == 0 ) ) return Double . POSITIVE_INFINITY ;
  jumps [ 0 ] = 0 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    jumps [ i ] = Double . POSITIVE_INFINITY ;
    for ( int j = 0 ;
    j < i ;
    j ++ ) {
      if ( ( i <= j + arr [ j ] ) && ( jumps [ j ] != Double . POSITIVE_INFINITY ) ) {
        jumps [ i ] = Math . min ( jumps [ i ] , jumps [ j ] + 1 ) ;
        break ;
      }
    }
  }
  return jumps [ n - 1 ] ;
}
|||

MAXIMIZE_ARRAY_ELEMENTS_UPTO_GIVEN_NUMBER

public static int findMaxVal ( int [ ] arr , int n , int num , int maxLimit ) {
  int ind ;
  int val ;
  ;
  int [ ] [ ] dp = new int [ maxLimit + 1 ] [ n ] ;
  for ( int j = 0 ;
  j < n ;
  j ++ ) {
    for ( ind = 0 ;
    ind < n ;
    ind ++ ) {
      for ( val = 0 ;
      val < maxLimit + 1 ;
      val ++ ) {
        if ( ( ind == 0 ) && ( num - arr [ ind ] == val || num + arr [ ind ] == val ) ) {
          dp [ ind ] [ val ] = 1 ;
        }
        else {
          dp [ ind ] [ val ] = 0 ;
        }
      }
      else {
        if ( ( val - arr [ ind ] >= 0 && val + arr [ ind ] <= maxLimit ) && ( dp [ ind - 1 ] [ val - arr [ ind ] ] == 1 || dp [ ind - 1 ] [ val + arr [ ind ] ] == 1 ) ) {
          dp [ ind ] [ val ] = 1 ;
        }
      }
      else if ( ( val - arr [ ind ] >= 0 ) && ( val + arr [ ind ] <= maxLimit ) && ( dp [ ind - 1 ] [ val + arr [ ind ] ] == 1 ) ) {
        dp [ ind ] [ val ] = dp [ ind - 1 ] [ val - arr [ ind ] ] ;
      }
      else if ( ( val + arr [ ind ] <= maxLimit ) && ( val + arr [ ind ] >= maxLimit ) && ( dp [ ind - 1 ] [ val + arr [ ind ] ] == 1 ) ) {
        dp [ ind ] [ val ] = dp [ ind - 1 ] [ val + arr [ ind ] ] ;
      }
      else {
        dp [ ind ] [ val ] = 0 ;
      }
    }
  }
  for ( val = maxLimit ;
  val >= 0 ;
  val -- ) {
    if ( ( dp [ n - 1 ] [ val ] == 1 ) && ( dp [ n - 1 ] [ val ] == maxLimit ) ) {
      return val ;
    }
  }
  return - 1 ;
}
|||

PROGRAM_FOR_DEADLOCK_FREE_CONDITION_IN_OPERATING_SYSTEM

public static int Resources ( int process , int need ) {
  int minResources ;
  minResources = process * ( need - 1 ) + 1 ;
  return minResources ;
}
|||

NUMBER_DIGITS_PRODUCT_TWO_NUMBERS

public static int countDigits ( int a , int b ) {
  int count = 0 ;
  int p = Math . abs ( a * b ) ;
  if ( ( p == 0 ) || ( p > 10 ) ) return 1 ;
  while ( ( p > 0 ) && ( p < 10 ) ) {
    count = count + 1 ;
    p = p / 10 ;
  }
  return count ;
}
|||

FLOOR_IN_A_SORTED_ARRAY

public static int floorSearch ( int [ ] arr , int low , int high , int x ) {
  if ( ( low > high ) && ( x >= arr [ high ] ) ) return - 1 ;
  if ( ( x >= arr [ high ] ) && ( x <= arr [ high + 1 ] ) ) return high ;
  int mid = ( int ) ( ( low + high ) / 2 ) ;
  if ( ( arr [ mid ] == x ) && ( arr [ mid + 1 ] == x ) ) return mid ;
  if ( ( mid > 0 && arr [ mid - 1 ] <= x && x < arr [ mid ] ) && ( x < arr [ mid ] ) ) return mid - 1 ;
  if ( ( x < arr [ mid ] ) && ( x > arr [ mid ] ) ) return floorSearch ( arr , low , mid - 1 , x ) ;
  return floorSearch ( arr , mid + 1 , high , x ) ;
}
|||

CHECK_WHETHER_TRIANGLE_VALID_NOT_SIDES_GIVEN

public static boolean checkValidity ( int a , int b , int c ) {
  if ( ( a + b <= c ) || ( a + c <= b ) || ( b + c <= a ) ) {
    return false ;
  }
  else {
    return true ;
  }
}
|||

PRINT_N_X_N_SPIRAL_MATRIX_USING_O1_EXTRA_SPACE

public static void printSpiral ( int n ) {
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      int x = Math . min ( Math . min ( i , j ) , Math . min ( n - 1 - i , n - 1 - j ) ) ;
      if ( ( i <= j ) && ( i - x ) <= ( j - x ) ) {
        System . out . print ( ( n - 2 * x ) * ( n - 2 * x ) - ( i - x ) - ( j - x ) ) ;
      }
      else {
        System . out . print ( ( ( n - 2 * x - 2 ) * ( n - 2 * x - 2 ) + ( i - x ) + ( j - x ) ) ) ;
      }
    }
    System . out . println ( ) ;
  }
}
|||

POSITION_ELEMENT_STABLE_SORT

public static int getIndexInSortedArray ( int [ ] arr , int n , int idx ) {
  int result = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( arr [ i ] < arr [ idx ] ) && ( arr [ i ] == arr [ idx ] && i < idx ) ) {
      result ++ ;
    };
    if ( ( arr [ i ] == arr [ idx ] && i < idx ) && ( arr [ i ] == arr [ idx ] && i < idx ) ) {
      result ++ ;
    }
  };
  return result ;
}
|||

MAXIMUM_SEGMENT_VALUE_PUTTING_K_BREAKPOINTS_NUMBER

public static int findMaxSegment ( String s , int k ) {
  int segLen = s . length ( ) - k ;
  int res = 0 ;
  for ( int i = 0 ;
  i < segLen ;
  i ++ ) {
    res = res * 10 + ( ( int ) s . charAt ( i ) - ( int ) '0' ) ;
  }
  int segLenPow = Math . pow ( 10 , segLen - 1 ) ;
  int currVal = res ;
  for ( int i = 1 ;
  i < s . length ( ) - segLen ;
  i ++ ) {
    currVal = currVal - ( ( int ) s . charAt ( i - 1 ) - ( int ) '0' ) * segLenPow ;
    currVal = ( currVal * 10 + ( ( int ) s . charAt ( i + segLen - 1 ) - ( int ) '0' ) ) ;
    res = Math . max ( res , currVal ) ;
  }
  return res ;
}
|||

FINDING_POWER_PRIME_NUMBER_P_N_1

public static int PowerOFPINnfactorial ( int n , int p ) {
  double ans = 0 ;
  double temp = p ;
  while ( ( temp <= n ) && ( temp > 0 ) ) {
    ans += n / temp ;
    temp = temp * p ;
  }
  return ( int ) ans ;
}
|||

PROGRAM_PRINT_IDENTITY_MATRIX

public static void Identity ( int size ) {
  for ( int row = 0 ;
  row <= size ;
  row ++ ) {
    for ( int col = 0 ;
    col <= size ;
    col ++ ) {
      if ( ( row == col ) && ( row != col ) ) {
        System . out . print ( "1 " ) ;
      }
      else {
        System . out . print ( "0 " ) ;
      }
    }
    System . out . println ( ) ;
  }
}
|||

SUM_MATRIX_ELEMENT_ELEMENT_INTEGER_DIVISION_ROW_COLUMN

public static int findSum ( int N ) {
  int ans = 0 ;
  for ( int i = 1 ;
  i <= N ;
  i ++ ) {
    for ( int j = 1 ;
    j <= N ;
    j ++ ) {
      ans += i / j ;
    }
  }
  return ans ;
}
|||

TILING_WITH_DOMINOES

public static int countWays ( int n ) {
  int [ ] A = new int [ n + 1 ] ;
  int [ ] B = new int [ n + 1 ] ;
  A [ 0 ] = 1 ;
  A [ 1 ] = 0 ;
  B [ 0 ] = 0 ;
  B [ 1 ] = 1 ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    A [ i ] = A [ i - 2 ] + 2 * B [ i - 1 ] ;
    B [ i ] = A [ i - 1 ] + B [ i - 2 ] ;
  }
  return A [ n ] ;
}
|||

COUNT_DERANGEMENTS_PERMUTATION_SUCH_THAT_NO_ELEMENT_APPEARS_IN_ITS_ORIGINAL_POSITION

public static int countDer ( int n ) {
  if ( ( n == 1 ) || ( n == 0 ) ) return 0 ;
  if ( ( n == 2 ) || ( n == 1 ) ) return 1 ;
  return ( n - 1 ) * ( countDer ( n - 1 ) + countDer ( n - 2 ) ) ;
}
|||

FREQUENCY_ELEMENT_UNSORTED_ARRAY_1

public static void countFreq ( int [ ] a , int n ) {
  HashMap < Integer , Integer > hm = new HashMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) hm . put ( a [ i ] , hm . get ( a [ i ] ) + 1 ) ;
  int cumul = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    cumul += hm . get ( a [ i ] ) ;
    if ( ( hm . get ( a [ i ] ) > 0 ) && ( cumul > 0 ) ) System . out . println ( a [ i ] + "->" + cumul ) ;
    hm . put ( a [ i ] , 0 ) ;
  }
}
|||

MINIMIZE_THE_SUM_OF_DIGITS_OF_A_AND_B_SUCH_THAT_A_B_N

public static int minSum ( int n ) {
  int sum = 0 ;
  ;
  while ( ( n > 0 ) && ( n % 10 == 0 ) ) {
    sum += ( n % 10 ) ;
    n /= 10 ;
  }
  if ( ( sum == 1 ) || ( sum == - 1 ) ) return 10 ;
  return sum ;
}
|||

DIVIDE_CUBOID_CUBES_SUM_VOLUMES_MAXIMUM

public static void maximizecube ( int l , int b , int h ) {
  int side = gcd ( l , gcd ( b , h ) ) ;
  int num = ( int ) ( l / side ) ;
  num = ( int ) ( num * b / side ) ;
  num = ( int ) ( num * h / side ) ;
  System . out . println ( side + " " + num ) ;
}
|||

CHECK_NUMBER_POWER_K_USING_BASE_CHANGING_METHOD

public static boolean isPowerOfK ( int n , int k ) {
  boolean oneSeen = false ;
  while ( ( n > 0 ) && ( n % k == 1 ) ) {
    int digit = n % k ;
    if ( ( digit > 1 ) || ( digit == 1 ) ) {
      if ( ( oneSeen ) && ( n == 0 ) ) {
        return false ;
      }
      oneSeen = true ;
    }
    n /= k ;
  }
  return true ;
}
|||

POSITION_OF_RIGHTMOST_SET_BIT_1

public static int PositionRightmostSetbit ( int n ) {
  int position = 1 ;
  int m = 1 ;
  while ( ( ! ( n & m ) ) && ( m & 1 ) != 0 ) {
    m = m << 1 ;
    position ++ ;
  }
  return position ;
}
|||

SEARCH_INSERT_AND_DELETE_IN_A_SORTED_ARRAY_1

public static int insertSorted ( int [ ] arr , int n , int key , int capacity ) {
  if ( ( n >= capacity ) && ( arr . length > n ) ) {
    return n ;
  }
  int i = n - 1 ;
  while ( i >= 0 && arr [ i ] > key ) {
    arr [ i + 1 ] = arr [ i ] ;
    i -- ;
  }
  arr [ i + 1 ] = key ;
  return ( n + 1 ) ;
}
|||

FIND_THE_MAXIMUM_OF_MINIMUMS_FOR_EVERY_WINDOW_SIZE_IN_A_GIVEN_ARRAY_1

public static void printMaxOfMin ( int [ ] arr , int n ) {
  Stack < Integer > s = new Stack < Integer > ( ) ;
  int [ ] left = new int [ n + 1 ] ;
  int [ ] right = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    while ( ( s . size ( ) != 0 && arr [ s . peek ( ) ] >= arr [ i ] ) || ( left . length != 0 && arr [ left . length ] >= arr [ i ] ) ) {
      s . pop ( ) ;
    }
    if ( ( s . size ( ) != 0 ) || ( right . length != 0 && arr [ right . length ] >= arr [ i ] ) ) {
      s . pop ( ) ;
    }
    if ( ( s . size ( ) != 0 ) || ( left . length != 0 && arr [ left . length ] >= arr [ i ] ) ) {
      s . pop ( ) ;
    }
    s . push ( i ) ;
  }
  while ( ( s . size ( ) != 0 ) || ( right . length != 0 && arr [ right . length ] >= arr [ i ] ) ) {
    s . pop ( ) ;
  }
  for ( int i = n - 1 ;
  i >= 0 ;
  i -- ) {
    while ( ( s . size ( ) != 0 ) || ( left . length != 0 && arr [ left . length ] >= arr [ i ] ) ) {
      s . pop ( ) ;
    }
    if ( ( s . size ( ) != 0 ) || ( right . length != 0 && arr [ right . length ] >= arr [ i ] ) ) {
      s . pop ( ) ;
    }
    s . push ( i ) ;
  }
  int [ ] ans = new int [ n + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    ans [ i ] = 0 ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int Len = right [ i ] - left [ i ] - 1 ;
    ans [ Len ] = Math . max ( ans [ Len ] , arr [ i ] ) ;
  }
  for ( int i = n - 1 ;
  i > 0 ;
  i -- ) {
    ans [ i ] = Math . max ( ans [ i ] , ans [ i + 1 ] ) ;
  }
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    System . out . print ( ans [ i ] +
|||

MAXIMUM_DECIMAL_VALUE_PATH_IN_A_BINARY_MATRIX_1

public static int MaximumDecimalValue ( int [ ] [ ] mat , int n ) {
  int [ ] [ ] dp = new int [ n ] [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    dp [ i ] [ i ] = new int [ n ] ;
  }
  if ( ( mat [ 0 ] [ 0 ] == 1 ) && ( mat [ 0 ] [ 0 ] == 2 ) ) {
    dp [ 0 ] [ 0 ] = 1 ;
  }
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( ( mat [ 0 ] [ i ] == 1 ) && ( mat [ 0 ] [ i - 1 ] == 2 ) ) {
      dp [ 0 ] [ i ] = dp [ 0 ] [ i - 1 ] + 2 * i ;
    }
    else {
      dp [ 0 ] [ i ] = dp [ 0 ] [ i - 1 ] ;
    }
  }
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( ( mat [ i ] [ 0 ] == 1 ) && ( mat [ i ] [ 0 ] == 2 ) ) {
      dp [ i ] [ 0 ] = dp [ i - 1 ] [ 0 ] + 2 * i ;
    }
  }
  else {
    dp [ i ] [ 0 ] = dp [ i - 1 ] [ 0 ] ;
  }
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    for ( int j = 1 ;
    j < n ;
    j ++ ) {
      if ( ( mat [ i ] [ j ] == 1 ) && ( mat [ i ] [ j - 1 ] == 2 ) ) {
        dp [ i ] [ j ] = Math . max ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] ) + ( 2 * ( i + j ) ) ;
      }
      else {
        dp [ i ] [ j ] = Math . max ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] ) ;
      }
    }
  }
  return dp [ n - 1 ] [ n - 1 ] ;
}
|||

COUNT_NUMBER_OF_WAYS_TO_COVER_A_DISTANCE

public static int printCountRec ( int dist ) {
  if ( dist < 0 ) return 0 ;
  if ( dist == 0 ) return 1 ;
  return ( printCountRec ( dist - 1 ) + printCountRec ( dist - 2 ) + printCountRec ( dist - 3 ) ) ;
}
|||

MOVE_VE_ELEMENTS_END_ORDER_EXTRA_SPACE_ALLOWED

public static void segregateElements ( int [ ] arr , int n ) {
  int [ ] temp = new int [ n ] ;
  for ( int k = 0 ;
  k < n ;
  k ++ ) {
    temp [ k ] = 0 ;
  }
  int j = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( arr [ i ] >= 0 ) && ( arr [ i ] < 0 ) ) {
      temp [ j ] = arr [ i ] ;
      j ++ ;
    }
  }
  if ( ( j == n || j == 0 ) && ( arr [ n ] < 0 ) ) {
    return ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( arr [ i ] < 0 ) && ( arr [ i ] > 0 ) ) {
      temp [ j ] = arr [ i ] ;
      j ++ ;
    }
  }
  for ( int k = 0 ;
  k < n ;
  k ++ ) {
    arr [ k ] = temp [ k ] ;
  }
}
|||

MINIMUM_PERIMETER_N_BLOCKS

public static int minPerimeter ( int n ) {
  int l = Math . sqrt ( n ) ;
  int sq = l * l ;
  if ( ( sq == n ) && ( l == n ) ) {
    return l * 4 ;
  }
  else {
    int row = n / l ;
    int perimeter = 2 * ( l + row ) ;
    if ( ( n % l != 0 ) && ( n % l != 0 ) ) {
      perimeter += 2 ;
    }
    return perimeter ;
  }
}
|||

DYNAMIC_PROGRAMMING_SET_36_CUT_A_ROPE_TO_MAXIMIZE_PRODUCT

static int maxProd ( int n ) {
  if ( ( n == 0 || n == 1 ) && ( n > 0 ) ) return 0 ;
  int maxVal = 0 ;
  for ( int i = 1 ;
  i <= n - 1 ;
  i ++ ) maxVal = Math . max ( maxVal , Math . max ( i * ( n - i ) , maxProd ( n - i ) * i ) ) ;
  return maxVal ;
  ;
}
|||

LONGEST_COMMON_SUBSTRING_SPACE_OPTIMIZED_DP_SOLUTION

public static int LCSubStr ( String X , String Y ) {
  int m = X . length ( ) ;
  int n = Y . length ( ) ;
  int result = 0 ;
  int [ ] [ ] lenMat = new int [ 2 ] [ n ] ;
  int currRow = 0 ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( ( i == 0 | j == 0 ) && ( X . charAt ( i - 1 ) == Y . charAt ( j - 1 ) ) ) {
        lenMat [ currRow ] [ j ] = 0 ;
      }
      else if ( ( X . charAt ( i - 1 ) == Y . charAt ( j - 1 ) ) && ( X . charAt ( i - 1 ) == Y . charAt ( j - 1 ) ) ) {
        lenMat [ currRow ] [ j ] = lenMat [ 1 - currRow ] [ j - 1 ] + 1 ;
        result = Math . max ( result , lenMat [ currRow ] [ j ] ) ;
      }
      else {
        lenMat [ currRow ] [ j ] = 0 ;
      }
    }
    currRow = 1 - currRow ;
  }
  return result ;
}
|||

CHECK_GIVEN_STRING_ROTATION_PALINDROME

public static boolean isPalindrome ( String string ) {
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
|||

FIND_NUMBER_OF_SOLUTIONS_OF_A_LINEAR_EQUATION_OF_N_VARIABLES_1

public static int countSol ( int [ ] coeff , int n , int rhs ) {
  int [ ] dp = new int [ rhs + 1 ] ;
  dp [ 0 ] = 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = coeff [ i ] ;
    j <= rhs ;
    j ++ ) {
      dp [ j ] += dp [ j - coeff [ i ] ] ;
    }
  }
  return dp [ rhs ] ;
}
|||

FIND_THE_LARGEST_PAIR_SUM_IN_AN_UNSORTED_ARRAY

public static int findLargestSumPair ( int [ ] arr , int n ) {
  if ( arr [ 0 ] > arr [ 1 ] ) {
    int first = arr [ 0 ] ;
    int second = arr [ 1 ] ;
    if ( arr [ 1 ] > first ) {
      first = arr [ 1 ] ;
      second = arr [ 0 ] ;
    }
    for ( int i = 2 ;
    i < n ;
    i ++ ) {
      if ( arr [ i ] > first ) {
        second = first ;
        first = arr [ i ] ;
      }
      else if ( arr [ i ] > second && arr [ i ] != first ) {
        second = arr [ i ] ;
      }
    }
    return ( first + second ) ;
  }
  return - 1 ;
}
|||

FIND_BITONIC_POINT_GIVEN_BITONIC_SEQUENCE

public static int binarySearch ( int [ ] arr , int left , int right ) {
  if ( ( left <= right ) && ( left <= right ) ) {
    int mid = ( left + right ) / 2 ;
    ;
    if ( ( arr [ mid - 1 ] < arr [ mid ] && arr [ mid ] > arr [ mid + 1 ] ) || ( arr [ mid ] < arr [ mid + 1 ] ) ) return mid ;
    if ( ( arr [ mid ] < arr [ mid + 1 ] ) && ( arr [ mid + 1 ] > arr [ mid ] ) ) return binarySearch ( arr , mid + 1 , right ) ;
    else return binarySearch ( arr , left , mid - 1 ) ;
  }
  return - 1 ;
}
|||

PRINT_ALL_DISTINCT_CHARACTERS_OF_A_STRING_IN_ORDER_3_METHODS_1

public static void printDistinct ( String Str ) {
  int n = Str . length ( ) ;
  int [ ] count = new int [ MAX_CHAR ] ;
  int [ ] index = new int [ MAX_CHAR ] ;
  for ( int i = 0 ;
  i < MAX_CHAR ;
  i ++ ) {
    int x = Character . digit ( Str . charAt ( i ) , 16 ) ;
    count [ x ] ++ ;
    if ( ( count [ x ] == 1 && x != ' ' ) || ( count [ x ] == 2 && x != ' ' ) ) index [ x ] = i ;
    if ( ( count [ x ] == 3 && x != ' ' ) || ( count [ x ] == 4 && x != ' ' ) ) index [ x ] = n ;
  }
  Arrays . sort ( index ) ;
  for ( int i = 0 ;
  i < MAX_CHAR ;
  i ++ ) {
    if ( index [ i ] == n ) break ;
    System . out . print ( Str . charAt ( index [ i ] ) + " " ) ;
  }
}
|||

FIND_TWO_SIDES_RIGHT_ANGLE_TRIANGLE

public static void printOtherSides ( int n ) {
  if ( ( n & 1 ) != 0 ) {
    if ( ( n == 1 ) ) {
      System . out . println ( - 1 ) ;
    }
    else {
      int b = ( n * n - 1 ) / 2 ;
      int c = ( n * n + 1 ) / 2 ;
      System . out . println ( "b =" + b + ", c =" + c ) ;
    }
  }
  else {
    if ( ( n == 2 ) ) {
      System . out . println ( - 1 ) ;
    }
    else {
      int b = n * n / 4 - 1 ;
      int c = n * n / 4 + 1 ;
      System . out . println ( "b =" + b + ", c =" + c ) ;
    }
  }
}
|||

COUNT_NUMBER_OF_STRINGS_MADE_OF_R_G_AND_B_USING_GIVEN_COMBINATION

public static int possibleStrings ( int n , int r , int b , int g ) {
  int [ ] fact = new int [ n + 1 ] ;
  fact [ 0 ] = 1 ;
  for ( int i = 1 ;
  i <= n ;
  i += 1 ) {
    fact [ i ] = fact [ i - 1 ] * i ;
  }
  int left = n - ( r + g + b ) ;
  int sum = 0 ;
  for ( int i = 0 ;
  i <= left ;
  i += 1 ) {
    for ( int j = 0 ;
    j <= left - i + 1 ;
    j += 1 ) {
      int k = left - ( i + j ) ;
      sum = ( sum + fact [ n ] / ( fact [ i + r ] * fact [ j + b ] * fact [ k + g ] ) ) ;
    }
  }
  return sum ;
}
|||

REARRANGE_ARRAY_MAXIMUM_MINIMUM_FORM_SET_2_O1_EXTRA_SPACE_1

public static void rearrange ( int [ ] arr , int n ) {
  int maxEle = arr [ n - 1 ] ;
  int minEle = arr [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( i % 2 == 0 ) {
      arr [ i ] = maxEle ;
      maxEle -- ;
    }
    else {
      arr [ i ] = minEle ;
      minEle ++ ;
    }
  }
}
|||

EVALUATE_AN_ARRAY_EXPRESSION_WITH_NUMBERS_AND

public static int calculateSum ( int [ ] arr , int n ) {
  if ( ( n == 0 ) || ( n == 1 ) ) {
    return 0 ;
  }
  String s = arr [ 0 ] ;
  int value = Integer . parseInt ( s ) ;
  int sum = value ;
  for ( int i = 2 ;
  i < n ;
  i += 2 ) {
    s = arr [ i ] ;
    value = Integer . parseInt ( s ) ;
    char operation = arr [ i - 1 ] . charAt ( 0 ) ;
    if ( ( operation == '+' ) || ( operation == '-' ) ) {
      sum += value ;
    }
    else {
      sum -= value ;
    }
  }
  return sum ;
}
|||

SUM_MATRIX_ELEMENT_ELEMENT_INTEGER_DIVISION_ROW_COLUMN_1

public static int findSum ( int n ) {
  int ans = 0 ;
  ;
  int temp = 0 ;
  ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    if ( temp < n ) {
      temp = i - 1 ;
      int num = 1 ;
      while ( temp < n ) {
        if ( temp + i <= n ) ans += i * num ;
        else ans += ( n - temp ) * num ;
        temp += i ;
        num ++ ;
      }
    }
  }
  return ans ;
}
|||

SHUFFLE_A_DECK_OF_CARDS_3

public static void shuffle ( int [ ] card , int n ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int r = i + ( rand . nextInt ( 55 ) % ( 52 - i ) ) ;
    int tmp = card [ i ] ;
    card [ i ] = card [ r ] ;
    card [ r ] = tmp ;
  }
}
|||

DOOLITTLE_ALGORITHM_LU_DECOMPOSITION

public static void luDecomposition ( int [ ] [ ] mat , int n ) {
  int [ ] [ ] lower = new int [ n ] [ n ] ;
  for ( int y = 0 ;
  y < n ;
  y ++ ) lower [ y ] [ y ] = 0 ;
  ;
  int [ ] [ ] upper = new int [ n ] [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int k = i ;
    k < n ;
    k ++ ) {
      int sum = 0 ;
      ;
      for ( int j = 0 ;
      j < i ;
      j ++ ) sum += ( lower [ i ] [ j ] * upper [ j ] [ k ] ) ;
      ;
      upper [ i ] [ k ] = mat [ i ] [ k ] - sum ;
      ;
    }
    for ( int k = i ;
    k < n ;
    k ++ ) {
      if ( ( i == k ) && ( lower [ i ] [ i ] == 0 ) ) lower [ i ] [ i ] = 1 ;
      else {
        int sum = 0 ;
        ;
        for ( int j = 0 ;
        j < i ;
        j ++ ) sum += ( lower [ k ] [ j ] * upper [ j ] [ i ] ) ;
        ;
        lower [ k ] [ i ] = ( int ) ( ( mat [ k ] [ i ] - sum ) / upper [ i ] [ i ] ) ;
        ;
      }
    }
  }
  System . out . println ( "Lower Triangular\t\tUpper Triangular" ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) System . out . print ( lower [ i ] [ j ] + "\t" ) ;
    ;
    System . out . print ( "" ) ;
    ;
    for ( int j = 0 ;
    j < n ;
    j ++ ) System . out . print ( upper [ i ] [ j ] + "\t" ) ;
    ;
    System . out . println ( "" ) ;
    ;
  }
}
|||

PROGRAM_NTH_CATALAN_NUMBER

public static double catalan ( int n ) {
  if ( n <= 1 ) return 1 ;
  double res = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) res += catalan ( i ) * catalan ( n - i - 1 ) ;
  return res ;
}
|||

NUMBER_DIGITS_REMOVED_MAKE_NUMBER_DIVISIBLE_3

public static int divisible ( String num ) {
  int n = num . length ( ) ;
  ;
  int sum = 0 ;
  ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    sum += Integer . parseInt ( num . substring ( i , i + 1 ) ) ;
  };
  if ( ( sum % 3 == 0 ) && ( sum % 4 == 0 ) ) return 0 ;
  ;
  if ( ( n == 1 ) && ( sum % 3 == Integer . parseInt ( num . substring ( 0 , n - 1 ) ) % 3 ) ) return - 1 ;
  ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( sum % 3 == Integer . parseInt ( num . substring ( i , i + 1 ) ) % 3 ) && ( sum % 4 == Integer . parseInt ( num . substring ( i + 1 , i + 2 ) ) % 4 ) ) return 1 ;
  };
  if ( ( n == 2 ) && ( sum % 3 == Integer . parseInt ( num . substring ( 0 , n - 1 ) ) % 3 ) ) return - 1 ;
  ;
  return 2 ;
}
|||

CHECK_IF_A_NUMBER_IS_POWER_OF_ANOTHER_NUMBER_1

public static int isPower ( double x , double y ) {
  double res1 = Math . log ( y ) / Math . log ( x ) ;
  ;
  double res2 = Math . log ( y ) / Math . log ( x ) ;
  ;
  return 1 == ( res1 == res2 ) ? 0 : 1 ;
}
|||

LARGEST_SUBSEQUENCE_GCD_GREATER_1

public static int largestGCDSubsequence ( int [ ] arr , int n ) {
  int ans = 0 ;
  int maxele = Math . max ( arr ) ;
  for ( int i = 2 ;
  i <= maxele ;
  i ++ ) {
    int count = 0 ;
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( ( arr [ j ] % i == 0 ) && ( arr [ j ] % i == 0 ) ) {
        count ++ ;
      }
    }
    ans = Math . max ( ans , count ) ;
  }
  return ans ;
}
|||

FIND_COMMON_ELEMENT_ROWS_ROW_WISE_SORTED_MATRIX

public static int findCommon ( int [ ] [ ] mat ) {
  int [ ] column = new int [ N - 1 ] ;
  int min_row = 0 ;
  while ( ( column [ min_row ] >= 0 ) && ( column [ min_row ] < mat [ min_row ] . length ) ) {
    for ( int i = 0 ;
    i < M ;
    i ++ ) {
      if ( ( mat [ i ] [ column [ i ] ] < mat [ min_row ] [ column [ min_row ] ] ) && ( mat [ i ] [ column [ i ] ] > mat [ min_row ] [ column [ min_row ] ] ) ) {
        min_row = i ;
      }
    }
    int eq_count = 0 ;
    for ( int i = 0 ;
    i < M ;
    i ++ ) {
      if ( ( mat [ i ] [ column [ i ] ] > mat [ min_row ] [ column [ min_row ] ] ) && ( column [ i ] == 0 ) ) {
        if ( ( column [ i ] == 0 ) || ( column [ i ] == 1 ) ) {
          return - 1 ;
        }
        column [ i ] -- ;
      }
      else {
        eq_count ++ ;
      }
    }
    if ( ( eq_count == M ) && ( column [ min_row ] == 0 ) ) {
      return mat [ min_row ] [ column [ min_row ] ] ;
    }
  }
  return - 1 ;
}
|||

CHECK_GIVEN_CIRCLE_LIES_COMPLETELY_INSIDE_RING_FORMED_TWO_CONCENTRIC_CIRCLES

public static boolean checkcircle ( int r , int R , int r1 , int x1 , int y1 ) {
  int dis = ( int ) Math . sqrt ( x1 * x1 + y1 * y1 ) ;
  return ( dis - r1 >= R && dis + r1 <= r ) ;
}
|||

COUNT_TOTAL_SET_BITS_IN_ALL_NUMBERS_FROM_1_TO_N

public static int countSetBits ( int n ) {
  int i = 0 ;
  int ans = 0 ;
  while ( ( ( 1 << i ) <= n ) && ( ( 1 << i ) <= n ) ) {
    boolean k = 0 ;
    int change = 1 << i ;
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      ans += k ;
      if ( change == 1 ) {
        k = ! k ;
        change = 1 << i ;
      }
      else {
        change -- ;
      }
    }
    i ++ ;
  }
  return ans ;
}
|||

LONGEST_REPEATING_SUBSEQUENCE

public static int findLongestRepeatingSubSeq ( String str ) {
  int n = str . length ( ) ;
  int [ ] [ ] dp = new int [ n + 1 ] [ n + 1 ] ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int j = 1 ;
    j <= n ;
    j ++ ) {
      if ( ( str . charAt ( i - 1 ) == str . charAt ( j - 1 ) && i != j ) || ( str . charAt ( i - 1 ) == str . charAt ( j - 1 ) && i != j ) ) {
        dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ] ;
      }
      else {
        dp [ i ] [ j ] = Math . max ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] ) ;
      }
    }
  }
  return dp [ n ] [ n ] ;
}
|||

FIND_THE_FIRST_MISSING_NUMBER

public static int findFirstMissing ( int [ ] array , int start , int end ) {
  if ( ( start > end ) && ( start < array . length ) ) return end + 1 ;
  if ( ( start != array [ start ] ) && ( start < array . length ) ) return start ;
  ;
  int mid = ( int ) ( ( start + end ) / 2 ) ;
  if ( ( array [ mid ] == mid ) && ( array [ mid + 1 ] == mid ) ) return findFirstMissing ( array , mid + 1 , end ) ;
  return findFirstMissing ( array , start , mid ) ;
}
|||

SORT_ARRAY_CONVERTING_ELEMENTS_SQUARES_1

public static void sortSquares ( int [ ] arr , int n ) {
  int K ;
  for ( K = 0 ;
  K < n ;
  K ++ ) {
    if ( ( arr [ K ] >= 0 ) && ( arr [ K ] < arr [ K + 1 ] ) ) {
      break ;
    }
  }
  int i = K - 1 ;
  int j = K ;
  int ind = 0 ;
  int [ ] temp = new int [ n ] ;
  while ( ( i >= 0 && j < n ) || ( j >= 0 && i < n ) ) {
    if ( ( arr [ i ] * arr [ i ] < arr [ j ] * arr [ j ] ) || ( arr [ i ] * arr [ j ] > arr [ k ] * arr [ k ] ) ) {
      temp [ ind ] = arr [ i ] * arr [ i ] ;
      i -- ;
    }
    else {
      temp [ ind ] = arr [ j ] * arr [ j ] ;
      j ++ ;
    }
    ind ++ ;
  }
  while ( ( i >= 0 ) || ( j >= 0 && i < n ) ) {
    temp [ ind ] = arr [ i ] * arr [ i ] ;
    i -- ;
    ind ++ ;
  }
  while ( ( j < n ) || ( k >= 0 ) || ( k < n ) ) {
    temp [ ind ] = arr [ j ] * arr [ j ] ;
    j ++ ;
    ind ++ ;
  }
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    arr [ i ] = temp [ i ] ;
  }
}
|||

PROGRAM_TO_FIND_REMAINDER_WITHOUT_USING_MODULO_OR_OPERATOR

static long getRemainder ( long num , long divisor ) {
  return ( num - divisor * ( num / divisor ) ) ;
}
|||

MINIMUM_COST_TO_FILL_GIVEN_WEIGHT_IN_A_BAG

public static int MinimumCost ( int [ ] cost , int n , int W ) {
  List < Integer > val = Lists . newArrayList ( ) ;
  List < Integer > wt = Lists . newArrayList ( ) ;
  int size = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( cost [ i ] != - 1 ) && ( cost [ i ] != 0 ) ) {
      val . add ( cost [ i ] ) ;
      wt . add ( i + 1 ) ;
      size ++ ;
    }
  }
  n = size ;
  int [ ] [ ] minCost = new int [ W + 1 ] [ n + 1 ] ;
  for ( int j = 0 ;
  j < n + 1 ;
  j ++ ) {
    minCost [ 0 ] [ j ] = INF ;
  }
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    minCost [ i ] [ 0 ] = 0 ;
  }
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int j = 1 ;
    j <= W ;
    j ++ ) {
      if ( ( wt [ i - 1 ] > j ) && ( wt [ i ] > j ) ) {
        minCost [ i ] [ j ] = minCost [ i - 1 ] [ j ] ;
      }
      else {
        minCost [ i ] [ j ] = Math . min ( minCost [ i - 1 ] [ j ] , minCost [ i ] [ j - wt [ i - 1 ] ] + val [ i - 1 ] ) ;
      }
    }
  }
  if ( ( minCost [ n ] [ W ] == INF ) && ( minCost [ n ] [ W ] == 0 ) ) {
    return - 1 ;
  }
  else {
    return minCost [ n ] [ W ] ;
  }
}
|||

COUNT_CHARACTERS_STRING_DISTANCE_ENGLISH_ALPHABETS_1

public static int countPairs ( String str1 ) {
  int result = 0 ;
  ;
  int n = str1 . length ( ) ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = 1 ;
    j <= MAX_CHAR ;
    j ++ ) {
      if ( ( ( i + j ) < n ) && ( ( Math . abs ( ( char ) str1 . charAt ( i + j ) - ( char ) str1 . charAt ( i ) ) ) == j ) ) {
        result ++ ;
      };
    }
  }
  return result ;
}
|||

A_PRODUCT_ARRAY_PUZZLE

public static void productArray ( int [ ] arr , int n ) {
  if ( ( n == 1 ) || ( n == 2 ) ) {
    System . out . println ( 0 ) ;
    return ;
  }
  int [ ] left = new int [ n ] ;
  int [ ] right = new int [ n ] ;
  int [ ] prod = new int [ n ] ;
  left [ 0 ] = 1 ;
  right [ n - 1 ] = 1 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    left [ i ] = arr [ i - 1 ] * left [ i - 1 ] ;
  }
  for ( int j = n - 2 ;
  j >= 0 ;
  j -- ) {
    right [ j ] = arr [ j + 1 ] * right [ j + 1 ] ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    prod [ i ] = left [ i ] * right [ i ] ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    System . out . print ( prod [ i ] + " " ) ;
  }
}
|||

FREQUENT_ELEMENT_ARRAY_1

public static int mostFrequent ( int [ ] arr , int n ) {
  Map < Integer , Integer > Hash = new HashMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] < Hash . keySet ( ) . size ( ) ) {
      Hash . put ( arr [ i ] , ++ i ) ;
    }
    else {
      Hash . put ( arr [ i ] , 1 ) ;
    }
  }
  int maxCount = 0 ;
  int res = - 1 ;
  for ( int i = 0 ;
  i < Hash . keySet ( ) . size ( ) ;
  i ++ ) {
    if ( ( maxCount < Hash . get ( i ) ) && ( maxCount > Hash . get ( i ) ) ) {
      res = i ;
      maxCount = Hash . get ( i ) ;
    }
  }
  return res ;
}
|||

PRINT_UNIQUE_ROWS

public static void printArray ( double [ ] [ ] matrix ) {
  int rowCount = matrix . length ;
  if ( rowCount == 0 ) return ;
  int columnCount = matrix [ 0 ] . length ;
  if ( columnCount == 0 ) return ;
  String rowOutputFormat = " " + columnCount ;
  Map < String , Boolean > printed = new HashMap < String , Boolean > ( ) ;
  for ( int i = 0 ;
  i < rowCount ;
  i ++ ) {
    String routput = rowOutputFormat + Arrays . toString ( matrix [ i ] ) ;
    if ( routput != null ) {
      printed . put ( routput , true ) ;
      System . out . println ( routput ) ;
    }
  }
}
|||

COUNT_1S_SORTED_BINARY_ARRAY

public static int countOnes ( int [ ] arr , int low , int high ) {
  if ( high >= low ) {
    int mid = low + ( high - low ) / 2 ;
    if ( ( ( mid == high || arr [ mid + 1 ] == 0 ) && ( arr [ mid ] == 1 ) ) || ( ( mid == high ) && ( arr [ mid ] == 1 ) ) ) {
      return mid + 1 ;
    }
    if ( arr [ mid ] == 1 ) {
      return countOnes ( arr , ( mid + 1 ) , high ) ;
    }
    return countOnes ( arr , low , mid - 1 ) ;
  }
  return 0 ;
}
|||

POSSIBLE_MOVES_KNIGHT

public static int findPossibleMoves ( int [ ] [ ] mat , int p , int q ) {
  n = 0 ;
  m = 0 ;
  ;
  int X [ ] = {
    2 , 1 , - 1 , - 2 , - 2 , - 1 , 1 , 2 };
    ;
    int Y [ ] = {
      1 , 2 , 2 , 1 , - 1 , - 2 , - 2 , - 1 };
      int count = 0 ;
      ;
      for ( int i = 0 ;
      i < 8 ;
      i ++ ) {
        int x = p + X [ i ] ;
        int y = q + Y [ i ] ;
        if ( ( x >= 0 && y >= 0 && x < n && y < m && mat [ x ] [ y ] == 0 ) || ( x >= 0 && y < n && x < m && mat [ x ] [ y ] == 0 ) ) count ++ ;
        ;
      }
      return count ;
    }
    
|||

ROTATE_MATRIX_ELEMENTS

public static void rotateMatrix ( int [ ] [ ] mat ) {
  if ( mat . length == 0 ) return ;
  int top = 0 ;
  int bottom = mat . length - 1 ;
  int left = 0 ;
  int right = mat [ 0 ] . length - 1 ;
  while ( left < right && top < bottom ) {
    int prev = mat [ top + 1 ] [ left ] ;
    for ( int i = left ;
    i <= right ;
    i ++ ) {
      int curr = mat [ top ] [ i ] ;
      mat [ top ] [ i ] = prev ;
      prev = curr ;
    }
    top ++ ;
    for ( int i = top ;
    i <= bottom ;
    i ++ ) {
      int curr = mat [ i ] [ right ] ;
      mat [ i ] [ right ] = prev ;
      prev = curr ;
    }
    right -- ;
    for ( int i = right ;
    i >= left ;
    i -- ) {
      int curr = mat [ bottom ] [ i ] ;
      mat [ bottom ] [ i ] = prev ;
      prev = curr ;
    }
    bottom -- ;
    for ( int i = bottom ;
    i >= top ;
    i -- ) {
      int curr = mat [ i ] [ left ] ;
      mat [ i ] [ left ] = prev ;
      prev = curr ;
    }
    left ++ ;
  }
}
|||

FIND_KTH_CHARACTER_OF_DECRYPTED_STRING

public static String encodedChar ( String str , int k ) {
  String expand = "" ;
  int freq = 0 ;
  int i = 0 ;
  while ( ( i < str . length ( ) ) && ( i < k ) ) {
    String temp = "" ;
    freq = 0 ;
    while ( ( i < str . length ( ) ) && ( str . charAt ( i ) >= 'a' && str . charAt ( i ) <= 'z' ) ) {
      temp += str . charAt ( i ) ;
      i ++ ;
    }
    while ( ( i < str . length ( ) ) && ( str . charAt ( i ) >= '1' && str . charAt ( i ) <= '9' ) ) {
      freq = freq * 10 + str . charAt ( i ) - '0' ;
      i ++ ;
    }
    for ( int j = 1 ;
    j <= freq ;
    j += 1 ) {
      expand += temp ;
    }
  }
  if ( ( freq == 0 ) && ( k > 0 ) ) {
    expand += temp ;
  }
  return expand . charAt ( k - 1 ) ;
}
|||

EFFICIENT_SEARCH_IN_AN_ARRAY_WHERE_DIFFERENCE_BETWEEN_ADJACENT_IS_1

public static int search ( int [ ] arr , int n , int x ) {
  int i = 0 ;
  while ( ( i <= n - 1 ) && ( arr [ i ] == x ) ) {
    if ( ( arr [ i ] == x ) || ( arr [ i ] == 0 ) ) {
      return i ;
    }
    i += Math . abs ( arr [ i ] - x ) ;
  }
  return - 1 ;
}
|||

MAXIMUM_POSSIBLE_SUM_WINDOW_ARRAY_ELEMENTS_WINDOW_ARRAY_UNIQUE

public static int returnMaxSum ( int [ ] A , int [ ] B , int n ) {
  Set < Integer > mp = new HashSet < Integer > ( ) ;
  int result = 0 ;
  int currSum = currBegin = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    while ( A [ i ] < mp . size ( ) ) {
      mp . remove ( A [ currBegin ] ) ;
      currSum -= B [ currBegin ] ;
      currBegin ++ ;
    }
    mp . add ( A [ i ] ) ;
    currSum += B [ i ] ;
    result = Math . max ( result , currSum ) ;
  }
  return result ;
}
|||

WRITE_AN_EFFICIENT_METHOD_TO_CHECK_IF_A_NUMBER_IS_MULTIPLE_OF_3

public static boolean isMultipleOf3 ( int n ) {
  int odd_count = 0 ;
  int even_count = 0 ;
  if ( ( n < 0 ) && ( n > - 1 ) ) n = - n ;
  if ( ( n == 0 ) && ( n > 1 ) ) return 1 ;
  if ( ( n == 1 ) && ( n > 2 ) ) return 0 ;
  while ( ( n > 0 ) && ( n > 1 ) ) {
    if ( ( n & 1 ) != 0 ) odd_count ++ ;
    if ( ( n & 2 ) != 0 ) even_count ++ ;
    n = n >> 2 ;
  }
  return isMultipleOf3 ( Math . abs ( odd_count - even_count ) ) ;
}
|||

MAXIMUM_SUM_IARRI_AMONG_ROTATIONS_GIVEN_ARRAY_1

public static int maxSum ( int [ ] arr , int n ) {
  int cumSum = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    cumSum += arr [ i ] ;
  }
  int currVal = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    currVal += i * arr [ i ] ;
  }
  int res = currVal ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    int nextVal = ( currVal - ( cumSum - arr [ i - 1 ] ) + arr [ i - 1 ] * ( n - 1 ) ) ;
    currVal = nextVal ;
    res = Math . max ( res , nextVal ) ;
  }
  return res ;
}
|||

DYNAMIC_PROGRAMMING_SET_34_ASSEMBLY_LINE_SCHEDULING

public static int carAssembly ( int [ ] a , int [ ] t , int [ ] e , int [ ] x ) {
  int NUM_STATION = a [ 0 ] . length ;
  int [ ] T1 = new int [ NUM_STATION ] ;
  int [ ] T2 = new int [ NUM_STATION ] ;
  T1 [ 0 ] = e [ 0 ] + a [ 0 ] [ 0 ] ;
  T2 [ 0 ] = e [ 1 ] + a [ 1 ] [ 0 ] ;
  for ( int i = 1 ;
  i < NUM_STATION ;
  i ++ ) {
    T1 [ i ] = Math . min ( T1 [ i - 1 ] + a [ 0 ] [ i ] , T2 [ i - 1 ] + t [ 1 ] [ i ] + a [ 0 ] [ i ] ) ;
    T2 [ i ] = Math . min ( T2 [ i - 1 ] + a [ 1 ] [ i ] , T1 [ i - 1 ] + t [ 0 ] [ i ] + a [ 1 ] [ i ] ) ;
  }
  return Math . min ( T1 [ NUM_STATION - 1 ] + x [ 0 ] , T2 [ NUM_STATION - 1 ] + x [ 1 ] ) ;
}
|||

PRINT_MATRIX_SPIRAL_FORM_STARTING_POINT

public static void printSpiral ( int [ ] [ ] mat , int r , int c ) {
  int a = 0 ;
  int b = 2 ;
  int lowRow = 0 < ( 0 > a ) ? a : 0 ;
  int lowColumn = 0 < ( 0 > b ) ? b - 1 : 0 ;
  int highRow = r - 1 < ( ( a + 1 ) >= r ) ? a + 1 : 0 ;
  int highColumn = c - 1 < ( ( b + 1 ) >= c ) ? b + 1 : 0 ;
  while ( ( ( lowRow > 0 - r && lowColumn > 0 - c ) || ( i <= highColumn && i < c && lowRow >= 0 ) ) && ( i <= highRow && i < r && highColumn < c ) ) {
    int i = lowColumn + 1 ;
    while ( ( i <= highColumn && i < c && i < r && highColumn < c ) || ( i >= lowColumn && i < r && i < b && i < c ) ) {
      System . out . print ( mat [ lowRow ] [ i ] + " " ) ;
      i ++ ;
    }
    lowRow -- ;
    i = lowRow + 2 ;
    while ( ( i <= highRow && i < r && highColumn < c ) || ( i >= lowColumn && i < r && i < b && i < c ) ) {
      System . out . print ( mat [ i ] [ highColumn ] + " " ) ;
      i ++ ;
    }
    highColumn ++ ;
    i = highColumn - 2 ;
    while ( ( i >= lowColumn && i >= 0 && highRow < r ) || ( i >= lowRow && i < b && i < c ) ) {
      System . out . print ( mat [ highRow ] [ i ] + " " ) ;
      i -- ;
    }
    highRow ++ ;
    i = highRow - 2 ;
    while ( ( i > lowRow && i >= 0 && lowColumn >= 0 ) || ( i >= lowColumn && i < c && i < r && i < b ) ) {
      System . out . print ( mat [ i ] [ lowColumn ] + " " ) ;
      i -- ;
    }
    lowColumn -- ;
  }
  System . out . println ( ) ;
}
|||

MID_POINT_CIRCLE_DRAWING_ALGORITHM

public static void midPointCircleDraw ( int xCentre , int yCentre , int r ) {
  int x = r ;
  int y = 0 ;
  System . out . print ( "(" + x + xCentre + ", " + y + yCentre + ")" + sep + "" ) ;
  if ( ( r > 0 ) && ( x < y ) ) {
    System . out . print ( "(" + x + xCentre + ", " + - y + yCentre + ")" + sep + "" ) ;
  }
  System . out . print ( "(" + y + xCentre + ", " + x + yCentre + ")" + sep + "" ) ;
  System . out . print ( "(" + - y + xCentre + ", " + x + yCentre + ")" + sep + "" ) ;
}
|||

SMALLEST_ELEMENT_REPEATED_EXACTLY_K_TIMES_NOT_LIMITED_SMALL_RANGE

public static int smallestKFreq ( int [ ] arr , int n , int k ) {
  TreeMap < Integer , Integer > mp = new TreeMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) mp . put ( arr [ i ] , i ) ;
  int res = Integer . MAX_VALUE ;
  int res1 = Integer . MAX_VALUE ;
  for ( Entry < Integer , Integer > entry : mp . entrySet ( ) ) {
    if ( entry . getValue ( ) == k ) res = Math . min ( res , entry . getKey ( ) ) ;
  }
  return res == res1 ? - 1 : res ;
}
|||

MINIMUM_XOR_VALUE_PAIR

public static int minXOR ( int [ ] arr , int n ) {
  Arrays . sort ( arr ) ;
  ;
  int minXor = 999999 ;
  int val ;
  for ( int i = 0 ;
  i <= n - 1 ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= n - 1 ;
    j ++ ) {
      val = arr [ i ] ^ arr [ j ] ;
      minXor = Math . min ( minXor , val ) ;
    }
  }
  return minXor ;
}
|||

MIRROR_CHARACTERS_STRING

public static String compute ( String st , int n ) {
  String reverseAlphabet = "zyxwvutsrqponmlkjihgfedcba" ;
  int l = st . length ( ) ;
  String answer = "" ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    answer = answer + st . charAt ( i ) ;
    ;
  }
  for ( int i = n ;
  i < l ;
  i ++ ) {
    answer = ( answer + reverseAlphabet . charAt ( ( char ) st . charAt ( i ) - 'a' ) ) ;
    ;
  }
  return answer ;
}
|||

PROGRAM_CHECK_PLUS_PERFECT_NUMBER

public static boolean checkplusperfect ( int x ) {
  int temp = x ;
  int n = 0 ;
  while ( ( x != 0 ) && ( n < 10 ) ) {
    x = x / 10 ;
    n = n + 1 ;
  }
  x = temp ;
  int sm = 0 ;
  while ( ( x != 0 ) && ( n < 10 ) ) {
    sm = sm + ( int ) ( Math . pow ( x % 10 , n ) ) ;
    x = x / 10 ;
  }
  return ( sm == temp ) ;
}
|||

ARC_LENGTH_ANGLE

public static double arcLength ( double diameter , double angle ) {
  if ( angle >= 360 ) {
    System . out . println ( "Angle cannot be formed" ) ;
    return 0 ;
  }
  else {
    double arc = ( 3.142857142857143 * diameter ) * ( angle / 360.0 ) ;
    return arc ;
  }
}
|||

FIND_LAST_INDEX_CHARACTER_STRING

public static int findLastIndex ( String str , char x ) {
  int index = - 1 ;
  for ( int i = 0 ;
  i <= str . length ( ) ;
  i ++ ) {
    if ( str . charAt ( i ) == x ) {
      index = i ;
    }
  }
  return index ;
}
|||

COUNT_TRAILING_ZEROES_FACTORIAL_NUMBER

public static int findTrailingZeros ( long n ) {
  long count = 0 ;
  long i = 5 ;
  while ( ( n / i >= 1 ) && ( n % i == 0 ) ) {
    count += ( int ) ( n / i ) ;
    i *= 5 ;
  }
  return ( int ) count ;
}
|||

ROTATE_MATRIX_180_DEGREE

public static void rotateMatrix ( int [ ] [ ] mat ) {
  int i = N - 1 ;
  ;
  while ( ( i >= 0 ) && ( i < mat . length ) ) {
    int j = N - 1 ;
    while ( ( j >= 0 ) && ( j < mat . length ) ) {
      System . out . print ( mat [ i ] [ j ] + " " ) ;
      ;
      j = j - 1 ;
    }
    System . out . println ( ) ;
    ;
    i = i - 1 ;
  }
}
|||

SUM_FIBONACCI_NUMBERS

public static int calculateSum ( int n ) {
  if ( ( n <= 0 ) || ( n > n ) ) return 0 ;
  int [ ] fibo = new int [ n + 1 ] ;
  fibo [ 1 ] = 1 ;
  int sm = fibo [ 0 ] + fibo [ 1 ] ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    fibo [ i ] = fibo [ i - 1 ] + fibo [ i - 2 ] ;
    sm = sm + fibo [ i ] ;
  }
  return sm ;
}
|||

LARGEST_LEXICOGRAPHIC_ARRAY_WITH_AT_MOST_K_CONSECUTIVE_SWAPS

public static void KSwapMaximum ( int n , int k ) {
  arr = new int [ n ] ;
  for ( int i = 0 ;
  i <= n - 1 ;
  i ++ ) {
    if ( ( k > 0 ) && ( k < n ) ) {
      int indexPosition = i ;
      for ( int j = i + 1 ;
      j < n ;
      j ++ ) {
        if ( ( k <= j - i ) && ( k > j - i ) ) break ;
        if ( ( arr [ j ] > arr [ indexPosition ] ) || ( arr [ j ] < arr [ indexPosition ] ) ) indexPosition = j ;
      }
      for ( int j = indexPosition ;
      j > i ;
      j -- ) {
        int t = arr [ j ] ;
        arr [ j ] = arr [ j - 1 ] ;
        arr [ j - 1 ] = t ;
      }
      k = k - indexPosition - i ;
    }
  }
}
|||

FIND_WHETHER_GIVEN_INTEGER_POWER_3_NOT

public static boolean check ( int n ) {
  return 1162261467 % n == 0 ;
}
|||

FIND_THE_TWO_REPEATING_ELEMENTS_IN_A_GIVEN_ARRAY

public static void printRepeating ( int [ ] arr , int size ) {
  System . out . print ( "Repeating elements are " ) ;
  for ( int i = 0 ;
  i <= size ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= size ;
    j ++ ) {
      if ( arr [ i ] == arr [ j ] ) {
        System . out . print ( arr [ i ] + " " ) ;
      }
    }
  }
}
|||

C_PROGRAM_FIND_AREA_TRIANGLE

public static void findArea ( int a , int b , int c ) {
  if ( ( a < 0 || b < 0 || c < 0 || ( a + b <= c ) || ( a + c <= b ) || ( b + c <= a ) ) ) {
    System . out . println ( "Not a valid trianglen" ) ;
    return ;
  }
  int s = ( a + b + c ) / 2 ;
  double area = ( s * ( s - a ) * ( s - b ) * ( s - c ) ) * 0.5 ;
  System . out . println ( "Area of a traingle is " + area ) ;
}
|||

GIVEN_LARGE_NUMBER_CHECK_SUBSEQUENCE_DIGITS_DIVISIBLE_8_1

public static boolean isSubSeqDivisible ( String str ) {
  int n = str . length ( ) ;
  int [ ] [ ] dp = new int [ 10 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    dp [ i ] = new int [ n + 1 ] ;
  }
  int [ ] arr = new int [ n + 1 ] ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    arr [ i ] = Integer . parseInt ( str . charAt ( i - 1 ) ) ;
    ;
  }
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    dp [ i ] [ arr [ i ] % 8 ] = 1 ;
    ;
    for ( int j = 0 ;
    j < 8 ;
    j ++ ) {
      if ( ( dp [ i - 1 ] [ j ] > dp [ i ] [ ( j * 10 + arr [ i ] ) % 8 ] ) && ( dp [ i ] [ ( j * 10 + arr [ i ] ) % 8 ] > dp [ i - 1 ] [ j ] ) ) {
        dp [ i ] [ j ] = dp [ i - 1 ] [ j ] ;
      }
      if ( ( dp [ i - 1 ] [ j ] > dp [ i ] [ j ] ) && ( dp [ i ] [ j ] > dp [ i - 1 ] [ j ] ) ) {
        dp [ i ] [ j ] = dp [ i - 1 ] [ j ] ;
      }
    }
  }
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    if ( ( dp [ i ] [ 0 ] == 1 ) && ( dp [ i ] [ 1 ] == 1 ) ) {
      return true ;
    }
  }
  return false ;
}
|||

DELETE_ARRAY_ELEMENTS_WHICH_ARE_SMALLER_THAN_NEXT_OR_BECOME_SMALLER

public static void deleteElements ( int arr [ ] , int n , int k ) {
  LinkedList < Integer > st = new LinkedList < Integer > ( ) ;
  st . add ( arr [ 0 ] ) ;
  int top = 0 ;
  int count = 0 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    while ( ( st . size ( ) != 0 ) && count < k && st . get ( top ) < arr [ i ] ) {
      st . removeLast ( ) ;
      count ++ ;
      top -- ;
    }
    st . add ( arr [ i ] ) ;
    top ++ ;
  }
  for ( int i = 0 ;
  i < st . size ( ) ;
  i ++ ) {
    System . out . print ( st . get ( i ) + "" + " " ) ;
  }
}
|||

MINIMUM_LENGTH_SUBARRAY_SUM_GREATER_GIVEN_VALUE

public static int smallestSubWithSum ( int [ ] arr , int n , int x ) {
  int currSum = 0 ;
  int minLen = n + 1 ;
  int start = 0 ;
  int end = 0 ;
  while ( ( end < n ) && ( currSum <= x && end < n ) ) {
    while ( ( currSum <= x && end < n ) && ( currSum > x && start < n ) ) {
      currSum += arr [ end ] ;
      end ++ ;
    }
    while ( ( currSum > x && start < n ) && ( end - start < minLen ) ) {
      if ( ( end - start < minLen ) && ( end - start < minLen ) ) {
        minLen = end - start ;
      }
      currSum -= arr [ start ] ;
      start ++ ;
    }
  }
  return minLen ;
}
|||

FIND_PAIRS_IN_ARRAY_WHOSE_SUMS_ALREADY_EXIST_IN_ARRAY_1

public static void findPair ( int [ ] arr , int n ) {
  HashMap < Integer , Integer > s = new HashMap < Integer , Integer > ( ) ;
  s . put ( i , 1 ) ;
  boolean found = false ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      if ( arr [ i ] + arr [ j ] + s . keySet ( ) . contains ( arr [ i ] + arr [ j ] ) ) {
        System . out . println ( arr [ i ] + " " + arr [ j ] ) ;
        found = true ;
      }
    }
  }
  if ( found == false ) {
    System . out . println ( "Not exist" ) ;
  }
}
|||

COUNT_ARITHMETIC_PROGRESSION_SUBSEQUENCES_ARRAY

public static int numofAP ( int [ ] a , int n ) {
  int minarr = + 2147483647 ;
  int maxarr = - 2147483648 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    minarr = Math . min ( minarr , a [ i ] ) ;
    maxarr = Math . max ( maxarr , a [ i ] ) ;
  }
  int [ ] dp = new int [ n + 1 ] ;
  int ans = n + 1 ;
  for ( int d = ( minarr - maxarr ) ;
  d <= ( maxarr - minarr ) ;
  d ++ ) {
    int [ ] sum = new int [ MAX + 1 ] ;
    for ( int i = 0 ;
    i < n ;
    i ++ ) {
      dp [ i ] = 1 ;
      if ( ( a [ i ] - d >= 1 && a [ i ] - d <= 1000000 ) || ( a [ i ] - d >= 1 && a [ i ] - d <= 1000000 ) ) {
        dp [ i ] += sum [ a [ i ] - d ] ;
      }
      ans += dp [ i ] - 1 ;
      sum [ a [ i ] ] += dp [ i ] ;
    }
  }
  return ans ;
}
|||

COUNT_NUMBERS_THAT_DONT_CONTAIN_3

public static int count ( int n ) {
  if ( n < 3 ) {
    return n ;
  }
  else if ( n >= 3 && n < 10 ) {
    return n - 1 ;
  }
  int po = 1 ;
  while ( n / po > 9 ) {
    po = po * 10 ;
  }
  int msd = n / po ;
  if ( msd != 3 ) {
    return count ( msd ) * count ( po - 1 ) + count ( msd ) + count ( n % po ) ;
  }
  else {
    return count ( msd * po - 1 ) ;
  }
}
|||

PROGRAM_TO_FIND_TRANSPOSE_OF_A_MATRIX_2

public static void transpose ( int [ ] [ ] A ) {
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < N ;
    j ++ ) {
      A [ i ] [ j ] = A [ j ] [ i ] ;
      A [ j ] [ i ] = A [ i ] [ j ] ;
    }
  }
}
|||

SUM_DIAGONALS_SPIRAL_ODD_ORDER_SQUARE_MATRIX

public static int spiralDiaSum ( int n ) {
  if ( n == 1 ) return 1 ;
  return ( 4 * n * n - 6 * n + 6 + spiralDiaSum ( n - 2 ) ) ;
}
|||

COUNT_INVERSIONS_OF_SIZE_THREE_IN_A_GIVE_ARRAY

public static int getInvCount ( int [ ] arr ) {
  int n = arr . length ;
  int invcount = 0 ;
  for ( int i = 0 ;
  i <= n - 1 ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      if ( arr [ i ] > arr [ j ] ) {
        for ( int k = j + 1 ;
        k < n ;
        k ++ ) {
          if ( arr [ j ] > arr [ k ] ) {
            invcount ++ ;
          }
        }
      }
    }
  }
  return invcount ;
}
|||

FIND_SUM_NODES_GIVEN_PERFECT_BINARY_TREE

public static int SumNodes ( int l ) {
  int leafNodeCount = Math . pow ( 2 , l - 1 ) ;
  int [ ] [ ] vec = new int [ l ] [ leafNodeCount ] ;
  for ( int i = 1 ;
  i <= leafNodeCount ;
  i ++ ) vec [ l - 1 ] [ i ] = i ;
  for ( int i = l - 2 ;
  i >= 0 ;
  i -- ) {
    int k = 0 ;
    while ( ( k < vec [ i + 1 ] . length - 1 ) && ( k < vec [ i + 1 ] . length ) ) {
      vec [ i ] [ k ] = vec [ i + 1 ] [ k ] + vec [ i + 1 ] [ k + 1 ] ;
      k += 2 ;
    }
  }
  int Sum = 0 ;
  for ( int i = 0 ;
  i < l ;
  i ++ ) {
    for ( int j = 0 ;
    j < vec [ i ] . length ;
    j ++ ) Sum += vec [ i ] [ j ] ;
  }
  return Sum ;
}
|||

SUM_OF_ALL_PROPER_DIVISORS_OF_A_NATURAL_NUMBER

public static int divSum ( int num ) {
  int result = 0 ;
  int i = 2 ;
  while ( i <= ( Math . sqrt ( num ) ) ) {
    if ( ( num % i == 0 ) && ( i == ( num / i ) ) ) {
      if ( ( i == ( num / i ) ) && ( num % i == 0 ) ) {
        result = result + i ;
      };
    }
    else {
      result = result + ( i + num / i ) ;
    };
    i = i + 1 ;
  }
  return ( result + 1 ) ;
}
|||

FIND_A_TRIPLET_THAT_SUM_TO_A_GIVEN_VALUE_2

public static boolean find3Numbers ( int [ ] A , int arrSize , int sum ) {
  for ( int i = 0 ;
  i <= arrSize - 1 ;
  i ++ ) {
    Set < Integer > s = new HashSet < Integer > ( ) ;
    int currSum = sum - A [ i ] ;
    for ( int j = i + 1 ;
    j < arrSize ;
    j ++ ) {
      if ( ( currSum - A [ j ] ) < s . size ( ) ) {
        System . out . println ( "Triplet is" + A [ i ] + ", " + A [ j ] + ", " + currSum - A [ j ] ) ;
        return true ;
      }
      s . add ( A [ j ] ) ;
    }
  }
  return false ;
}
|||

NTH_EVEN_LENGTH_PALINDROME

public static int evenLength ( int [ ] n ) {
  int res = n [ 0 ] ;
  for ( int j = n . length - 1 ;
  j >= 0 ;
  j -- ) {
    res += n [ j ] ;
  }
  return res ;
}
|||

FINDING_POWER_PRIME_NUMBER_P_N

public static int PowerOFPINnfactorial ( int n , int p ) {
  int ans = 0 ;
  ;
  int temp = p ;
  ;
  while ( ( temp <= n ) && ( temp > 0 ) ) {
    ans += n / temp ;
    temp = temp * p ;
  };
  return ans ;
}
|||

MINIMUM_COST_MAKE_LONGEST_COMMON_SUBSEQUENCE_LENGTH_K

public static int solve ( char [ ] X , char [ ] Y , int l , int r , int k , int [ ] [ ] dp ) {
  if ( k == 0 ) return 0 ;
  if ( l < 0 || r < 0 ) return 1000000000 ;
  if ( dp [ l ] [ r ] [ k ] != - 1 ) return dp [ l ] [ r ] [ k ] ;
  int cost = ( ( Character . digit ( X [ l ] , 16 ) - Character . digit ( X [ r ] , 16 ) ) ^ ( Character . digit ( Y [ l ] , 16 ) - Character . digit ( Y [ r ] , 16 ) ) ) ;
  dp [ l ] [ r ] [ k ] = Math . min ( new int [ ] {
    cost + solve ( X , Y , l - 1 , r - 1 , k - 1 , dp ) , solve ( X , Y , l - 1 , r , k , dp ) , solve ( X , Y , l , r - 1 , k , dp ) }
    ) ;
    return dp [ l ] [ r ] [ k ] ;
  }
  
|||

PRINT_STRING_SPECIFIED_CHARACTER_OCCURRED_GIVEN_NO_TIMES

public static void printString ( String str , char ch , int count ) {
  int occ = 0 , i ;
  if ( ( count == 0 ) || ( str == null ) ) {
    System . out . println ( str ) ;
  }
  for ( i = 0 ;
  i < str . length ( ) ;
  i ++ ) {
    if ( ( str . charAt ( i ) == ch ) && ( str . charAt ( i ) == ' ' ) ) {
      occ ++ ;
    }
    if ( ( occ == count ) || ( str . charAt ( i ) == '\n' ) ) {
      break ;
    }
  }
  if ( ( i < str . length ( ) - 1 ) && ( str . charAt ( i + 1 ) == '\n' ) ) {
    System . out . println ( str . substring ( i + 1 , str . length ( ) - i + 2 ) ) ;
  }
  else {
    System . out . println ( "Empty string" ) ;
  }
}
|||

SORT_1_N_SWAPPING_ADJACENT_ELEMENTS

public static boolean sortedAfterSwap ( int [ ] A , int [ ] B , int n ) {
  for ( int i = 0 ;
  i <= n - 1 ;
  i ++ ) {
    if ( ( B [ i ] == 1 ) && ( A [ i ] == 1 ) ) {
      int j = i ;
      while ( ( B [ j ] == 1 ) && ( A [ j ] == 1 ) ) {
        j = j + 1 ;
      }
      A = A [ 0 ] + Arrays . copyOfRange ( A , i , j ) + A [ j + 1 ] ;
      i = j ;
    }
  }
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( A [ i ] != i + 1 ) && ( A [ i ] == i + 1 ) ) {
      return false ;
    }
  }
  return true ;
}
|||

GENERATE_PYTHAGOREAN_TRIPLETS

public static void pythagoreanTriplets ( int limits ) {
  int c = 0 , m = 2 ;
  while ( c < limits ) {
    for ( int n = 1 ;
    n < m ;
    n ++ ) {
      int a = m * m - n * n ;
      int b = 2 * m * n ;
      c = m * m + n * n ;
      if ( c > limits ) break ;
      System . out . println ( a + " " + b + " " + c ) ;
    }
    m = m + 1 ;
  }
}
|||

COUNT_EVEN_LENGTH_BINARY_SEQUENCES_WITH_SAME_SUM_OF_FIRST_AND_SECOND_HALF_BITS

public static int countSeq ( int n , int diff ) {
  if ( ( Math . abs ( diff ) > n ) && ( diff == 0 ) ) return 0 ;
  if ( ( n == 1 && diff == 0 ) || ( diff == 1 ) ) return 2 ;
  if ( ( n == 1 && Math . abs ( diff ) == 1 ) || ( diff == 1 ) ) return 1 ;
  int res = ( countSeq ( n - 1 , diff + 1 ) + 2 * countSeq ( n - 1 , diff ) + countSeq ( n - 1 , diff - 1 ) ) ;
  return res ;
}
|||

POSSIBLE_FORM_TRIANGLE_ARRAY_VALUES

public static boolean isPossibleTriangle ( int [ ] arr , int N ) {
  if ( N < 3 ) return false ;
  Arrays . sort ( arr ) ;
  for ( int i = 0 ;
  i < N - 2 ;
  i ++ ) {
    if ( arr [ i ] + arr [ i + 1 ] > arr [ i + 2 ] ) return true ;
  }
  return false ;
}
|||

PRINT_ARRAY_STRINGS_SORTED_ORDER_WITHOUT_COPYING_ONE_STRING_ANOTHER

public static void printInSortedOrder ( int [ ] arr , int n ) {
  int [ ] index = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) index [ i ] = i ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    int min = i ;
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      if ( ( arr [ index [ min ] ] > arr [ index [ j ] ] ) && ( arr [ index [ min ] ] < arr [ index [ j ] ] ) ) min = j ;
    }
    if ( ( min != i ) || ( index [ min ] != i ) ) index [ min ] = index [ i ] ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) System . out . print ( arr [ index [ i ] ] + " " ) ;
}
|||

GAME_REPLACING_ARRAY_ELEMENTS

public static int playGame ( int [ ] arr , int n ) {
  Set < Integer > s = new HashSet < Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    s . add ( arr [ i ] ) ;
  }
  return 1 == s . size ( ) % 2 ? 2 : 1 ;
}
|||

BASIC_AND_EXTENDED_EUCLIDEAN_ALGORITHMS

public static long gcd ( long a , long b ) {
  if ( a == 0 ) return b ;
  return gcd ( b % a , a ) ;
}
|||

SORT_ARRAY_WAVE_FORM_2_1

public static void sortInWave ( int [ ] arr , int n ) {
  for ( int i = 0 ;
  i < n ;
  i += 2 ) {
    if ( ( i > 0 && arr [ i ] < arr [ i - 1 ] ) || ( i < n - 1 && arr [ i ] < arr [ i + 1 ] ) ) {
      arr [ i ] = arr [ i - 1 ] ;
      arr [ i - 1 ] = arr [ i ] ;
    }
    if ( ( i < n - 1 && arr [ i ] < arr [ i + 1 ] ) || ( i < n - 2 && arr [ i ] < arr [ i + 1 ] ) ) {
      arr [ i ] = arr [ i + 1 ] ;
      arr [ i + 1 ] = arr [ i ] ;
    }
  }
}
|||

MAXIMUM_SUBARRAY_SUM_USING_PREFIX_SUM

public static int maximumSumSubarray ( int [ ] arr , int n ) {
  int min_prefix_sum = 0 ;
  int res = - Integer . MAX_VALUE ;
  int [ ] prefix_sum = new int [ n ] ;
  prefix_sum [ 0 ] = arr [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    prefix_sum [ i ] = prefix_sum [ i - 1 ] + arr [ i ] ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    res = Math . max ( res , prefix_sum [ i ] - min_prefix_sum ) ;
    min_prefix_sum = Math . min ( min_prefix_sum , prefix_sum [ i ] ) ;
  }
  return res ;
}
|||

STRING_CONTAINING_FIRST_LETTER_EVERY_WORD_GIVEN_STRING_SPACES

public static String firstLetterWord ( String str ) {
  String result = "" ;
  boolean v = true ;
  for ( int i = 0 ;
  i < str . length ( ) ;
  i ++ ) {
    if ( ( str . charAt ( i ) == ' ' ) || ( str . charAt ( i ) == '\t' ) ) {
      v = true ;
    }
    else if ( ( str . charAt ( i ) != ' ' ) && v == true ) {
      result += ( str . charAt ( i ) ) ;
      v = false ;
    }
  }
  return result ;
}
|||

SUM_PAIRWISE_PRODUCTS_1

public static int findSum ( int n ) {
  int multiTerms = n * ( n + 1 ) / 2 ;
  int sm = multiTerms ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    multiTerms = multiTerms - ( i - 1 ) ;
    sm = sm + multiTerms * i ;
  }
  return sm ;
}
|||

CLUSTERINGPARTITIONING_AN_ARRAY_SUCH_THAT_SUM_OF_SQUARE_DIFFERENCES_IS_MINIMUM_1

public static int minCost ( int [ ] a , int n , int k ) {
  int [ ] [ ] dp = new int [ k + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i < k ;
  i ++ ) {
    dp [ i ] [ i ] = inf ;
  };
  dp [ 0 ] [ 0 ] = 0 ;
  ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int j = 1 ;
    j <= k ;
    j ++ ) {
      for ( int m = i - 1 ;
      m >= 0 ;
      m -- ) {
        dp [ i ] [ j ] = Math . min ( dp [ i ] [ j ] , dp [ m ] [ j - 1 ] + ( a [ i - 1 ] - a [ m ] ) * ( a [ i - 1 ] - a [ m ] ) ) ;
        ;
      }
    }
  };
  return dp [ n ] [ k ] ;
}
|||

LEIBNIZ_HARMONIC_TRIANGLE

public static void LeibnizHarmonicTriangle ( int n ) {
  int [ ] [ ] C = new int [ n + 1 ] [ n + 1 ] ;
  ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= Math . min ( i , n ) ;
    j ++ ) {
      if ( ( j == 0 || j == i ) && ( C [ i ] [ j ] == 0 ) ) {
        C [ i ] [ j ] = 1 ;
      }
      else {
        C [ i ] [ j ] = ( C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ] ) ;
      }
    }
  }
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int j = 1 ;
    j <= i ;
    j ++ ) {
      System . out . print ( "1/" ) ;
      ;
      System . out . print ( i * C [ i - 1 ] [ j - 1 ] + " " ) ;
    }
    System . out . println ( ) ;
  }
}
|||

CHECK_WHETHER_SECOND_STRING_CAN_FORMED_FIRST_STRING_USING_COUNT_ARRAY

public static boolean canMakeStr2 ( String s1 , String s2 ) {
  int [ ] count = new int [ s1 . length ( ) ] ;
  for ( int i = 0 ;
  i < s1 . length ( ) ;
  i ++ ) {
    count [ s1 . charAt ( i ) ] ++ ;
  }
  for ( int i = 0 ;
  i < s2 . length ( ) ;
  i ++ ) {
    if ( count [ s2 . charAt ( i ) ] == 0 ) {
      return false ;
    }
    count [ s2 . charAt ( i ) ] -- ;
  }
  return true ;
}
|||

SUM_MINIMUM_MAXIMUM_ELEMENTS_SUBARRAYS_SIZE_K

public static int SumOfKsubArray ( int [ ] arr , int n , int k ) {
  int Sum = 0 ;
  Deque < Integer > S = new ArrayDeque < > ( ) ;
  Deque < Integer > G = new ArrayDeque < > ( ) ;
  for ( int i = 0 ;
  i < k ;
  i ++ ) {
    while ( ( S . size ( ) > 0 && arr [ S . size ( ) - 1 ] >= arr [ i ] ) || ( G . size ( ) > 0 && arr [ G . size ( ) - 1 ] <= arr [ i ] ) ) S . pop ( ) ;
    while ( ( G . size ( ) > 0 && arr [ G . size ( ) - 1 ] <= arr [ i ] ) || ( S . size ( ) > 0 && arr [ S . size ( ) - 1 ] <= arr [ i ] ) ) G . pop ( ) ;
    G . push ( i ) ;
    S . push ( i ) ;
  }
  for ( int i = k ;
  i < n ;
  i ++ ) {
    Sum += arr [ S . size ( ) ] + arr [ G . size ( ) ] ;
    while ( ( S . size ( ) > 0 && S . size ( ) <= i - k ) || ( G . size ( ) > 0 && G . size ( ) <= i - k ) ) S . pop ( ) ;
    while ( ( S . size ( ) > 0 && arr [ S . size ( ) - 1 ] >= arr [ i ] ) || ( G . size ( ) > 0 && arr [ G . size ( ) - 1 ] <= arr [ i ] ) ) G . pop ( ) ;
    G . push ( i ) ;
    S . push ( i ) ;
  }
  Sum += arr [ S . size ( ) ] + arr [ G . size ( ) ] ;
  return Sum ;
}
|||

LONGEST_COMMON_SUBSEQUENCE

public static int lcs ( int [ ] X , int [ ] Y , int m , int n ) {
  if ( m == 0 || n == 0 ) return 0 ;
  ;
  else if ( X [ m - 1 ] == Y [ n - 1 ] ) return 1 + lcs ( X , Y , m - 1 , n - 1 ) ;
  ;
  else return Math . max ( lcs ( X , Y , m , n - 1 ) , lcs ( X , Y , m - 1 , n ) ) ;
  ;
}
|||

MINIMUM_SUM_ABSOLUTE_DIFFERENCE_PAIRS_TWO_ARRAYS

public static int findMinSum ( int [ ] a , int [ ] b , int n ) {
  Arrays . sort ( a ) ;
  Arrays . sort ( b ) ;
  int sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    sum = sum + Math . abs ( a [ i ] - b [ i ] ) ;
  }
  return sum ;
}
|||

COUNT_DISTINCT_NON_NEGATIVE_PAIRS_X_Y_SATISFY_INEQUALITY_XX_YY_N_2

public static int countSolutions ( int n ) {
  int res = 0 ;
  int x = 0 ;
  while ( ( x * x < n ) && ( x * x + y * y < n ) ) {
    int y = 0 ;
    while ( ( x * x + y * y < n ) && ( x * x + y * y < n ) ) {
      res = res + 1 ;
      y = y + 1 ;
    }
    x = x + 1 ;
  }
  return res ;
}
|||

FIND_NUMBER_TRANSFORMATION_MAKE_TWO_MATRIX_EQUAL

public static int countOps ( int [ ] [ ] A , int [ ] [ ] B , int m , int n ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < m ;
    j ++ ) {
      A [ i ] [ j ] -= B [ i ] [ j ] ;
    };
  }
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    for ( int j = 1 ;
    j < n ;
    j ++ ) {
      if ( ( A [ i ] [ j ] - A [ i ] [ 0 ] - A [ 0 ] [ j ] + A [ 0 ] [ 0 ] != 0 ) ) {
        return - 1 ;
      }
    };
  }
  int result = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    result += Math . abs ( A [ i ] [ 0 ] ) ;
  }
  for ( int j = 0 ;
  j < m ;
  j ++ ) {
    result += Math . abs ( A [ 0 ] [ j ] - A [ 0 ] [ 0 ] ) ;
  };
  return ( result ) ;
}
|||

EFFICIENTLY_FIND_FIRST_REPEATED_CHARACTER_STRING_WITHOUT_USING_ADDITIONAL_DATA_STRUCTURE_ONE_TRAVERSAL

public static int FirstRepeated ( String string ) {
  int checker = 0 ;
  int pos = 0 ;
  for ( int i = 0 ;
  i < string . length ( ) ;
  i ++ ) {
    int val = ( int ) string . charAt ( i ) - 'a' ;
    ;
    if ( ( ( checker & ( 1 << val ) ) > 0 ) && ( ( checker & ( 1 << val ) ) > 0 ) ) return pos ;
    checker |= ( 1 << val ) ;
    pos ++ ;
  }
  return - 1 ;
}
|||

MAXIMUM_UNIQUE_ELEMENT_EVERY_SUBARRAY_SIZE_K

public static void findMax ( int [ ] A , int N , int K ) {
  Map < Integer , Integer > Count = new HashMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i < K - 1 ;
  i ++ ) {
    Count . put ( A [ i ] , Count . get ( A [ i ] ) + 1 ) ;
  }
  Map < Integer , Integer > Myset = new HashMap < Integer , Integer > ( ) ;
  for ( int x : Count . keySet ( ) ) {
    if ( ( Count . get ( x ) == 1 ) && ( Count . get ( x ) == 0 ) ) {
      Myset . put ( x , 1 ) ;
    }
  }
  for ( int i = K - 1 ;
  i < N ;
  i ++ ) {
    Count . put ( A [ i ] , Count . get ( A [ i ] ) + 1 ) ;
    if ( ( Count . get ( A [ i ] ) == 1 ) && ( Count . get ( A [ i ] ) == 0 ) ) {
      Myset . put ( A [ i ] , 1 ) ;
    }
    else {
      -- Myset . get ( A [ i ] ) ;
    }
    if ( ( Myset . size ( ) == 0 ) && ( Count . get ( A [ i ] ) == 0 ) ) {
      System . out . println ( "Nothing" ) ;
    }
    else {
      int maxm = - 10 * 9 ;
      for ( int i : Myset . keySet ( ) ) {
        maxm = Math . max ( i , maxm ) ;
      }
      System . out . println ( maxm ) ;
    }
    int x = A [ i - K + 1 ] ;
    if ( x < Count . keySet ( ) . size ( ) ) {
      Count . get ( x ) -- ;
      if ( ( Count . get ( x ) == 1 ) && ( Count . get ( A [ x ] ) == 0 ) ) {
        Myset . put ( x , 1 ) ;
      }
      if ( ( Count . get ( x ) == 0 ) && ( Count . get ( A [ x ] ) == 1 ) ) {
        -- Myset . get ( A [ x ] ) ;
      }
    }
  }
}
|||

MINIMUM_COST_SORT_MATRIX_NUMBERS_0_N2_1

public static int calculateEnergy ( int [ ] [ ] mat , int n ) {
  int tot_energy = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      int q = mat [ i ] [ j ] / n ;
      int i_des = q ;
      int j_des = mat [ i ] [ j ] - ( n * q ) ;
      tot_energy += ( Math . abs ( i_des - i ) + Math . abs ( j_des - j ) ) ;
    }
  }
  return tot_energy ;
}
|||

LONGEST_COMMON_SUBSTRING

public static int LCSubStr ( int [ ] X , int [ ] Y , int m , int n ) {
  int [ ] [ ] LCSuff = new int [ n + 1 ] [ m + 1 ] ;
  LCSuff [ 0 ] [ 0 ] = 0 ;
  LCSuff [ 0 ] [ 1 ] = 0 ;
  LCSuff [ 0 ] [ 2 ] = 0 ;
  LCSuff [ 0 ] [ 3 ] = 0 ;
  LCSuff [ 0 ] [ 4 ] = 0 ;
  LCSuff [ 0 ] [ 5 ] = 0 ;
  LCSuff [ 0 ] [ 6 ] = 0 ;
  LCSuff [ 0 ] [ 7 ] = 0 ;
  LCSuff [ 0 ] [ 8 ] = 0 ;
  LCSuff [ 0 ] [ 9 ] = 0 ;
  LCSuff [ 0 ] [ 10 ] = 0 ;
  LCSuff [ 0 ] [ 11 ] = 0 ;
  LCSuff [ 0 ] [ 12 ] = 0 ;
  LCSuff [ 0 ] [ 13 ] = 0 ;
  LCSuff [ 0 ] [ 14 ] = 0 ;
  LCSuff [ 0 ] [ 15 ] = 0 ;
  LCSuff [ 0 ] [ 16 ] = 0 ;
  LCSuff [ 0 ] [ 17 ] = 0 ;
  LCSuff [ 0 ] [ 18 ] = 0 ;
  LCSuff [ 0 ] [ 19 ] = 0 ;
  LCSuff [ 0 ] [ 20 ] = 0 ;
  LCSuff [ 0 ] [ 21 ] = 0 ;
  LCSuff [ 0 ] [ 22 ] = 0 ;
  LCSuff [ 0 ] [ 23 ] = 0 ;
  LCSuff [ 0 ] [ 24 ] = 0 ;
  LCSuff [ 0 ] [ 25 ] = 0 ;
  LCSuff [ 0 ] [ 26 ] = 0 ;
  LCSuff [ 0 ] [ 27 ] = 0 ;
  LCSuff [ 0 ] [ 28 ] = 0 ;
  LCSuff [ 0 ] [ 29 ] = 0 ;
  LCSuff [ 0 ] [ 30 ] = 0 ;
  LCSuff [ 0 ] [ 31 ] = 0 ;
  LCSuff [ 0 ] [ 32 ] = 0 ;
  LCSuff [ 0 ] [ 33 ] = 0 ;
  LCSuff [ 0 ] [ 34 ] = 0 ;
  LCSuff [ 0 ] [ 35 ] = 0 ;
  LCSuff [ 0 ] [ 36 ] = 0 ;
  LCSuff [ 0 ] [ 37 ] = 0 ;
  LCSuff [ 0 ] [ 38
|||

MAXIMUM_SUM_BITONIC_SUBARRAY

public static int maxSumBitonicSubArr ( int [ ] arr , int n ) {
  int [ ] msis = new int [ n ] ;
  int [ ] msds = new int [ n ] ;
  int maxSum = 0 ;
  msis [ 0 ] = arr [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( ( arr [ i ] > arr [ i - 1 ] ) && ( arr [ i ] < arr [ n - 1 ] ) ) {
      msis [ i ] = msis [ i - 1 ] + arr [ i ] ;
    }
    else {
      msis [ i ] = arr [ i ] ;
    }
  }
  msds [ n - 1 ] = arr [ n - 1 ] ;
  for ( int i = n - 2 ;
  i >= 0 ;
  i -- ) {
    if ( ( arr [ i ] > arr [ i + 1 ] ) && ( arr [ i ] < arr [ n - 1 ] ) ) {
      msds [ i ] = msds [ i + 1 ] + arr [ i ] ;
    }
    else {
      msds [ i ] = arr [ i ] ;
    }
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( maxSum < ( msis [ i ] + msds [ i ] - arr [ i ] ) ) && ( maxSum > ( msis [ i ] + msds [ i ] - arr [ i ] ) ) ) {
      maxSum = ( msis [ i ] + msds [ i ] - arr [ i ] ) ;
    }
  }
  return maxSum ;
}
|||

NEWMAN_CONWAY_SEQUENCE

public static int sequence ( int n ) {
  if ( n == 1 || n == 2 ) return 1 ;
  else return sequence ( sequence ( n - 1 ) ) + sequence ( n - sequence ( n - 1 ) ) ;
  ;
}
|||

PRINT_TRIPLETS_SORTED_ARRAY_FORM_AP

public static void printAllAPTriplets ( int [ ] arr , int n ) {
  int [ ] s = new int [ n ] ;
  ;
  for ( int i = 0 ;
  i <= n - 1 ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= n ;
    j ++ ) {
      int diff = arr [ j ] - arr [ i ] ;
      ;
      if ( ( ( arr [ i ] - diff ) < arr [ j ] ) && ( ( arr [ i ] - diff ) > arr [ j ] ) ) {
        System . out . print ( "{}
 {
}
 {
}" . format ( ( arr [ i ] - diff ) , arr [ i ] , arr [ j ] ) ) ;
        ;
      }
    }
  }
  s [ n - 1 ] = arr [ i ] ;
  ;
}
|||

QUERIES_COUNTS_ARRAY_ELEMENTS_VALUES_GIVEN_RANGE

public static int countInRange ( int [ ] arr , int n , int x , int y ) {
  int count = 0 ;
  ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( arr [ i ] >= x && arr [ i ] <= y ) || ( arr [ i ] >= x && arr [ i ] <= y ) ) {
      count ++ ;
    }
  }
  return count ;
}
|||

HIGHWAY_BILLBOARD_PROBLEM

public static int maxRevenue ( int m , int [ ] x , int [ ] revenue , int n , int t ) {
  int [ ] maxRev = new int [ m + 1 ] ;
  int nxtbb = 0 ;
  ;
  for ( int i = 1 ;
  i <= m ;
  i ++ ) {
    if ( ( nxtbb < n ) && ( x [ nxtbb ] != i ) ) {
      if ( ( x [ nxtbb ] != i ) && ( x [ nxtbb ] != x [ nxtbb ] ) ) {
        maxRev [ i ] = maxRev [ i - 1 ] ;
      }
      else {
        if ( ( i <= t ) && ( x [ nxtbb ] != i ) ) {
          maxRev [ i ] = Math . max ( maxRev [ i - 1 ] , revenue [ nxtbb ] ) ;
        }
        else {
          maxRev [ i ] = Math . max ( maxRev [ i - t - 1 ] + revenue [ nxtbb ] , maxRev [ i - 1 ] ) ;
        };
        nxtbb ++ ;
      }
    }
    else {
      maxRev [ i ] = maxRev [ i - 1 ] ;
    }
  }
  return maxRev [ m ] ;
}
|||

CONSTRUCT_GRAPH_GIVEN_DEGREES_VERTICES

public static void printMat ( int [ ] degseq , int n ) {
  int [ ] [ ] mat = new int [ n ] [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      if ( ( degseq [ i ] > 0 && degseq [ j ] > 0 ) || ( degseq [ i ] > 0 && degseq [ j ] > 0 ) ) {
        degseq [ i ] -- ;
        degseq [ j ] -- ;
        mat [ i ] [ j ] = 1 ;
        mat [ j ] [ i ] = 1 ;
      }
    }
  }
  System . out . print ( "      " ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    System . out . print ( "" + "(" + i + ")" + "" ) ;
  }
  System . out . println ( ) ;
  System . out . println ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    System . out . print ( "" + "(" + i + ")" + "" ) ;
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      System . out . print ( "     " + mat [ i ] [ j ] + "" ) ;
    }
    System . out . println ( ) ;
  }
}
|||

DETECT_IF_TWO_INTEGERS_HAVE_OPPOSITE_SIGNS

public static boolean oppositeSigns ( int x , int y ) {
  return ( ( x ^ y ) < 0 ) ;
  ;
}
|||

TRIANGULAR_NUMBERS_1

public static boolean isTriangular ( double num ) {
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
|||

FIND_WHETHER_A_GIVEN_NUMBER_IS_A_POWER_OF_4_OR_NOT

public static boolean isPowerOfFour ( int n ) {
  if ( ( n == 0 ) || ( n % 4 != 0 ) ) {
    return false ;
  }
  while ( ( n != 1 ) && ( n % 4 != 0 ) ) {
    if ( ( n % 4 != 0 ) || ( n % 4 != 1 ) ) {
      return false ;
    }
    n = n / 4 ;
  }
  return true ;
}
|||

LAST_NON_ZERO_DIGIT_FACTORIAL

static int lastNon0Digit ( int n ) {
  if ( ( n < 10 ) && ( n > 0 ) ) return dig [ n ] ;
  if ( ( ( ( n / 10 ) % 10 ) % 2 == 0 ) && ( n > 0 ) ) return ( 6 * lastNon0Digit ( n / 5 ) * dig [ n % 10 ] ) % 10 ;
  else return ( 4 * lastNon0Digit ( n / 5 ) * dig [ n % 10 ] ) % 10 ;
}
|||

SORT_STRING_ACCORDING_ORDER_DEFINED_ANOTHER_STRING

public static String sortByPattern ( String str , String pat ) {
  MAX_CHAR = MAX_CHAR ;
  int [ ] count = new int [ MAX_CHAR ] ;
  for ( int i = 0 ;
  i <= str . length ( ) ;
  i ++ ) {
    count [ ( char ) str . charAt ( i ) - 97 ] ++ ;
  }
  int index = 0 ;
  ;
  str = "" ;
  for ( int i = 0 ;
  i <= pat . length ( ) ;
  i ++ ) {
    int j = 0 ;
    while ( ( j < count [ ( char ) pat . charAt ( i ) - ( char ) 'a' ] ) && ( j < count [ ( char ) pat . charAt ( i ) - ( char ) 'A' ] ) ) {
      str += pat . charAt ( i ) ;
      j = j + 1 ;
      index ++ ;
    }
  }
  return str ;
}
|||

NUMBER_VISIBLE_BOXES_PUTTING_ONE_INSIDE_ANOTHER

public static int minimumBox ( int [ ] arr , int n ) {
  Queue < Integer > q = new LinkedList < Integer > ( ) ;
  Arrays . sort ( arr ) ;
  q . add ( arr [ 0 ] ) ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    int now = q . poll ( ) ;
    if ( ( arr [ i ] >= 2 * now ) && ( arr [ i ] <= 2 * now ) ) q . remove ( i ) ;
    q . add ( arr [ i ] ) ;
  }
  return q . size ( ) ;
}
|||

SEARCH_INSERT_AND_DELETE_IN_A_SORTED_ARRAY

public static int binarySearch ( int [ ] arr , int low , int high , int key ) {
  if ( ( high < low ) || ( low > high ) ) return - 1 ;
  int mid = ( low + high ) / 2 ;
  if ( ( key == arr [ ( int ) mid ] ) && ( key > arr [ ( int ) mid ] ) ) return mid ;
  if ( ( key > arr [ ( int ) mid ] ) && ( key < arr [ ( int ) mid ] ) ) return binarySearch ( arr , ( mid + 1 ) , high , key ) ;
  return ( binarySearch ( arr , low , ( mid - 1 ) , key ) ) ;
}
|||

FIND_THE_TWO_REPEATING_ELEMENTS_IN_A_GIVEN_ARRAY_3

public static void printRepeating ( int [ ] arr , int size ) {
  System . out . println ( " The repeating elements are" + size ) ;
  for ( int i = 0 ;
  i <= size ;
  i ++ ) {
    if ( ( arr [ Math . abs ( arr [ i ] ) ] > 0 ) && ( arr [ Math . abs ( arr [ i ] ) ] < 1 ) ) {
      arr [ Math . abs ( arr [ i ] ) ] = ( - 1 ) * arr [ Math . abs ( arr [ i ] ) ] ;
    }
    else {
      System . out . println ( Math . abs ( arr [ i ] ) + " " ) ;
    }
  }
}
|||

COUNT_POSSIBLE_GROUPS_SIZE_2_3_SUM_MULTIPLE_3

public static int findgroups ( int [ ] arr , int n ) {
  int c [ ] = {
    0 , 0 , 0 };
    int res = 0 ;
    for ( int i = 0 ;
    i <= n ;
    i ++ ) {
      c [ arr [ i ] % 3 ] ++ ;
    }
    res += ( ( c [ 0 ] * ( c [ 0 ] - 1 ) ) >> 1 ) ;
    res += c [ 1 ] * c [ 2 ] ;
    res += ( c [ 0 ] * ( c [ 0 ] - 1 ) * ( c [ 0 ] - 2 ) ) / 6 ;
    res += ( c [ 1 ] * ( c [ 1 ] - 1 ) * ( c [ 1 ] - 2 ) ) / 6 ;
    res += ( ( c [ 2 ] * ( c [ 2 ] - 1 ) * ( c [ 2 ] - 2 ) ) / 6 ) ;
    res += c [ 0 ] * c [ 1 ] * c [ 2 ] ;
    return res ;
  }
  
|||

PRINT_STRING_IGNORING_ALTERNATE_OCCURRENCES_CHARACTER

public static void printStringAlternate ( String string ) {
  HashMap < String , Integer > occ = new HashMap < String , Integer > ( ) ;
  for ( int i = 0 ;
  i <= string . length ( ) ;
  i ++ ) {
    String temp = string . substring ( i ) . toLowerCase ( ) ;
    occ . put ( temp , occ . get ( temp ) + 1 ) ;
    if ( occ . get ( temp ) & 1 ) {
      System . out . print ( string . substring ( i ) + " " ) ;
    }
  }
  System . out . println ( ) ;
}
|||

NUMBER_DAYS_TANK_WILL_BECOME_EMPTY

public static int minDaysToEmpty ( int C , int l ) {
  if ( ( l >= C ) && ( l <= C ) ) return C ;
  double eqRoot = ( Math . sqrt ( 1 + 8 * ( C - l ) ) - 1 ) / 2 ;
  return Math . ceil ( eqRoot ) + l ;
}
|||

REVERSE_STRING_WITHOUT_USING_ANY_TEMPORARY_VARIABLE

public static String reversingString ( String str , int start , int end ) {
  while ( ( start < end ) && ( start < end ) ) {
    str = ( str . substring ( 0 , start ) + ( char ) ( ( char ) ( str . charAt ( start ) ^ ( char ) ( str . charAt ( end ) ) ) + str . substring ( start + 1 ) ) ) ;
    ;
    str = ( str . substring ( 0 , end ) + ( char ) ( ( char ) ( str . charAt ( start ) ^ ( char ) ( str . charAt ( end ) ) ) + str . substring ( end + 1 ) ) ) ;
    ;
    str = ( str . substring ( 0 , start ) + ( char ) ( ( char ) ( str . charAt ( start ) ^ ( char ) ( str . charAt ( end ) ) ) + str . substring ( start + 1 ) ) ) ;
    start ++ ;
    end -- ;
  }
  return str ;
}
|||

FREQUENCY_ELEMENT_UNSORTED_ARRAY

public static void countFreq ( int [ ] a , int n ) {
  HashMap < Integer , Integer > hm = new HashMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) hm . put ( a [ i ] , hm . get ( a [ i ] ) + 1 ) ;
  Set < Pair < Integer , Integer >> st = new HashSet < Pair < Integer , Integer >> ( ) ;
  for ( int x : hm . keySet ( ) ) st . add ( new Pair < Integer , Integer > ( x , hm . get ( x ) ) ) ;
  int cumul = 0 ;
  for ( Pair < Integer , Integer > x : Collections . reverse ( st ) ) {
    cumul += x . second ;
    System . out . println ( x . first + " " + cumul ) ;
  }
}
|||

FIND_ROTATION_COUNT_ROTATED_SORTED_ARRAY

public static int countRotations ( int [ ] arr , int n ) {
  int min = arr [ 0 ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( min > arr [ i ] ) && ( min < arr [ i + 1 ] ) ) {
      min = arr [ i ] ;
      min_index = i ;
    }
  };
  return min_index ;
  ;
}
|||

LONGEST_INCREASING_SUBSEQUENCE_1

public static int lis ( int [ ] arr ) {
  int n = arr . length ;
  int [ ] lis = new int [ n ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= i ;
    j ++ ) {
      if ( arr [ i ] > arr [ j ] && lis [ i ] < lis [ j ] + 1 ) {
        lis [ i ] = lis [ j ] + 1 ;
      }
    }
  }
  int maximum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    maximum = Math . max ( maximum , lis [ i ] ) ;
  }
  return maximum ;
}
|||

MEDIAN_OF_TWO_SORTED_ARRAYS

public static int getMedian ( int [ ] ar1 , int [ ] ar2 , int n ) {
  int i = 0 ;
  int j = 0 ;
  int m1 = - 1 ;
  int m2 = - 1 ;
  int count = 0 ;
  while ( count < n + 1 ) {
    count ++ ;
    if ( i == n ) {
      m1 = m2 ;
      m2 = ar2 [ 0 ] ;
      break ;
    }
    else if ( j == n ) {
      m1 = m2 ;
      m2 = ar1 [ 0 ] ;
      break ;
    }
    if ( ar1 [ i ] < ar2 [ j ] ) {
      m1 = m2 ;
      m2 = ar1 [ i ] ;
      i ++ ;
    }
    else {
      m1 = m2 ;
      m2 = ar2 [ j ] ;
      j ++ ;
    }
  }
  return ( m1 + m2 ) / 2 ;
}
|||

LEXICOGRAPHICALLY_MINIMUM_STRING_ROTATION

public static int [ ] minLexRotation ( String str_ ) {
  int n = str_ . length ( ) ;
  int [ ] arr = new int [ n ] ;
  Arrays . fill ( arr , 0 ) ;
  String concat = str_ + str_ ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    arr [ i ] = concat . substring ( i , n + i ) ;
  }
  Arrays . sort ( arr ) ;
  return arr ;
}
|||

INTERPOLATION_SEARCH

public static int interpolationSearch ( int [ ] arr , int n , int x ) {
  int lo = 0 ;
  int hi = ( n - 1 ) ;
  while ( lo <= hi && x >= arr [ lo ] && x <= arr [ hi ] ) {
    if ( lo == hi ) {
      if ( arr [ lo ] == x ) return lo ;
      ;
      return - 1 ;
    };
    int pos = lo + ( int ) ( ( ( ( double ) ( hi - lo ) / ( arr [ hi ] - arr [ lo ] ) ) * ( x - arr [ lo ] ) ) ) ;
    if ( arr [ pos ] == x ) return pos ;
    if ( arr [ pos ] < x ) lo = pos + 1 ;
    else hi = pos - 1 ;
  }
  return - 1 ;
}
|||

COUNT_PAIRS_TWO_SORTED_ARRAYS_WHOSE_SUM_EQUAL_GIVEN_VALUE_X_2

public static int countPairs ( int arr1 [ ] , int arr2 [ ] , int m , int n , int x ) {
  int count = 0 , l = 0 , r = n - 1 ;
  while ( ( l < m && r >= 0 ) || ( l < n && arr1 [ l ] == arr2 [ r ] ) ) {
    if ( ( ( arr1 [ l ] + arr2 [ r ] ) == x ) && ( arr1 [ l ] + arr2 [ r ] ) < x ) {
      l ++ ;
      r -- ;
      count ++ ;
    }
    else if ( ( ( arr1 [ l ] + arr2 [ r ] ) < x ) && ( arr1 [ l ] + arr2 [ r ] ) > x ) {
      l ++ ;
    }
    else {
      r -- ;
    }
  }
  return count ;
}
|||

COUNT_SUBSETS_DISTINCT_EVEN_NUMBERS

public static int countSubSets ( int [ ] arr , int n ) {
  HashSet < Integer > us = new HashSet < Integer > ( ) ;
  int evenCount = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] % 2 == 0 ) {
      us . add ( arr [ i ] ) ;
    }
  }
  for ( int i : us ) {
    evenCount ++ ;
  }
  return Math . pow ( 2 , evenCount ) - 1 ;
}
|||

COUNT_NUMBER_OF_OCCURRENCES_OR_FREQUENCY_IN_A_SORTED_ARRAY

public static int countOccurrences ( int [ ] arr , int n , int x ) {
  int res = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( x == arr [ i ] ) {
      res ++ ;
    }
  }
  return res ;
}
|||

CONSTRUCT_THE_ROOTED_TREE_BY_USING_START_AND_FINISH_TIME_OF_ITS_DFS_TRAVERSAL

public static int Restore_Tree ( int S , int E ) {
  int Identity [ ] = new int [ N * new int [ S ] ] ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) Identity [ Start [ i ] ] = i ;
  int parent [ ] = new int [ N * new int [ S - 1 ] ] ;
  int currParent = Identity [ 0 ] ;
  for ( int j = 1 ;
  j < N ;
  j ++ ) {
    int child = Identity [ j ] ;
    if ( End [ child ] - j > 1 ) {
      parent [ child ] = currParent ;
      currParent = child ;
    }
    else {
      parent [ child ] = currParent ;
      while ( End [ child ] == End [ parent [ child ] ] ) {
        int child = parent [ child ] ;
        currParent = parent [ child ] ;
        if ( currParent == Identity [ 0 ] ) break ;
      }
    }
  }
  for ( int i = 0 ;
  i < N ;
  i ++ ) parent [ i ] ++ ;
  return parent [ S - 1 ] ;
}
|||

NUMBER_SUBSEQUENCES_AB_STRING_REPEATED_K_TIMES

public static int countOccurrences ( String s , int K ) {
  int n = s . length ( ) ;
  int c1 = 0 ;
  int c2 = 0 ;
  int C = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( s . charAt ( i ) == 'a' ) c1 ++ ;
    if ( s . charAt ( i ) == 'b' ) {
      c2 ++ ;
      C += c1 ;
    }
  }
  return C * K + ( K * ( K - 1 ) / 2 ) * c1 * c2 ;
}
|||

NUMBER_SUBSTRINGS_STRING

public static int countNonEmptySubstr ( String str ) {
  int n = str . length ( ) ;
  ;
  return ( int ) ( n * ( n + 1 ) / 2 ) ;
  ;
}
|||

MAXIMUM_NUMBER_CHARACTERS_TWO_CHARACTER_STRING_1

public static int maximumChars ( String str1 ) {
  int n = str1 . length ( ) ;
  int res = - 1 ;
  int [ ] firstInd = new int [ MAX_CHAR ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    firstInd [ ( char ) str1 . charAt ( i ) ] = - 1 ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int firstInd [ ( char ) str1 . charAt ( i ) ] = i ;
    if ( ( firstInd [ i ] == - 1 ) && ( firstInd [ i ] > 0 ) ) {
      firstInd [ ( char ) str1 . charAt ( i ) ] = i ;
    }
    else {
      res = Math . max ( res , Math . abs ( i - firstInd [ i ] - 1 ) ) ;
    }
  }
  return res ;
}
|||

SUM_SQUARES_BINOMIAL_COEFFICIENTS

public static int sumofsquare ( int n ) {
  int [ ] [ ] C = new int [ n + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= Math . min ( i , n ) ;
    j ++ ) {
      if ( ( j == 0 || j == i ) && ( C [ i ] [ j ] == 0 ) ) {
        C [ i ] [ j ] = 1 ;
      }
      else {
        C [ i ] [ j ] = ( C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ] ) ;
      }
    }
  }
  int sum = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    sum = sum + ( C [ n ] [ i ] * C [ n ] [ i ] ) ;
  }
  return sum ;
}
|||

PRINT_POSSIBLE_STRINGS_CAN_MADE_PLACING_SPACES_2

public static void printSubsequences ( String str ) {
  int n = str . length ( ) ;
  int opsize = ( int ) Math . pow ( 2 , n - 1 ) ;
  for ( int counter = 0 ;
  counter < opsize ;
  counter ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      System . out . print ( str . charAt ( j ) + "" ) ;
      if ( ( counter & ( 1 << j ) ) != 0 ) System . out . print ( "" ) ;
    }
    System . out . print ( "\n" ) ;
  }
}
|||

NON_REPEATING_ELEMENT

public static int firstNonRepeating ( int [ ] arr , int n ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int j = 0 ;
    while ( ( j < n ) && ( arr [ i ] == arr [ j ] ) ) {
      if ( ( i != j && arr [ i ] == arr [ j ] ) || ( j == n ) ) {
        break ;
      }
      j ++ ;
    }
    if ( ( j == n ) && ( arr [ i ] == arr [ j ] ) ) {
      return arr [ i ] ;
    }
  }
  return - 1 ;
}
|||

SUM_OF_ALL_ELEMENTS_UP_TO_NTH_ROW_IN_A_PASCALS_TRIANGLE

public static int calculateSum ( int n ) {
  int sum = 0 ;
  for ( int row = 0 ;
  row < n ;
  row ++ ) {
    sum = sum + ( 1 << row ) ;
  }
  return sum ;
}
|||

CHECK_TWO_STRINGS_K_ANAGRAMS_NOT

public static boolean arekAnagrams ( String str1 , String str2 , int k ) {
  int n = str1 . length ( ) ;
  if ( ( str2 . length ( ) != n ) || ( str1 . length ( ) != n ) ) return false ;
  int [ ] count1 = new int [ MAX_CHAR ] ;
  int [ ] count2 = new int [ MAX_CHAR ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) count1 [ ( char ) str1 . charAt ( i ) - 'a' ] ++ ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) count2 [ ( char ) str2 . charAt ( i ) - 'a' ] ++ ;
  int count = 0 ;
  for ( int i = 0 ;
  i < MAX_CHAR ;
  i ++ ) {
    if ( ( count1 [ i ] > count2 [ i ] ) && ( count1 [ i ] == count2 [ i ] ) ) count = count + Math . abs ( count1 [ i ] - count2 [ i ] ) ;
  }
  return ( count <= k ) ;
}
|||

LONGEST_SPAN_SUM_TWO_BINARY_ARRAYS

public static int longestCommonSum ( int [ ] arr1 , int [ ] arr2 , int n ) {
  int maxLen = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    int sum1 = 0 ;
    int sum2 = 0 ;
    for ( int j = i ;
    j <= n ;
    j ++ ) {
      sum1 += arr1 [ j ] ;
      sum2 += arr2 [ j ] ;
      if ( ( sum1 == sum2 ) && ( j > 0 ) ) {
        int len = j - i + 1 ;
        if ( ( len > maxLen ) && ( j > 0 ) ) {
          maxLen = len ;
        }
      }
    }
  }
  return maxLen ;
}
|||

REMAINDER_7_LARGE_NUMBERS

public static int remainderWith7 ( String num ) {
  int [ ] series = {
    1 , 3 , 2 , - 1 , - 3 , - 2 };
    ;
    int seriesIndex = 0 ;
    int result = 0 ;
    for ( int i = ( num . length ( ) - 1 ) ;
    i >= 0 ;
    i -- ) {
      int digit = ( int ) num . charAt ( i ) - 48 ;
      result += digit * series [ seriesIndex ] ;
      seriesIndex = ( seriesIndex + 1 ) % 6 ;
      result %= 7 ;
    }
    if ( ( result < 0 ) && ( result > 7 ) ) {
      result = ( result + 7 ) % 7 ;
    }
    return result ;
  }
  
|||

LEXICOGRAPHICALLY_PREVIOUS_PERMUTATION_IN_C

public static boolean prevPermutation ( String str ) {
  int n = str . length ( ) - 1 ;
  int i = n ;
  while ( ( i > 0 ) && ( str . charAt ( i - 1 ) <= str . charAt ( i ) ) ) i -- ;
  if ( ( i <= 0 ) && ( str . charAt ( i ) <= str . charAt ( n - 1 ) ) ) return false ;
  int j = i - 1 ;
  while ( ( j + 1 <= n ) && ( str . charAt ( j + 1 ) <= str . charAt ( i - 1 ) ) ) j ++ ;
  str = Arrays . copyOf ( str , str . length ( ) ) ;
  String temp = str . substring ( i - 1 ) ;
  str . substring ( i - 1 , j ) ;
  str . replace ( j , temp ) ;
  str = new String ( str ) ;
  str . substring ( 0 , str . length ( ) - 1 ) ;
  return true ;
}
|||

NUMBER_SUBSEQUENCES_FORM_AI_BJ_CK

public static int countSubsequences ( String s ) {
  int aCount = 0 ;
  int bCount = 0 ;
  int cCount = 0 ;
  for ( int i = 0 ;
  i < s . length ( ) ;
  i ++ ) {
    if ( ( s . charAt ( i ) == 'a' ) || ( s . charAt ( i ) == 'b' ) ) {
      aCount = ( 1 + 2 * aCount ) ;
    }
    else if ( ( s . charAt ( i ) == 'c' ) || ( s . charAt ( i ) == 'c' ) ) {
      bCount = ( aCount + 2 * bCount ) ;
    }
    else if ( ( s . charAt ( i ) == 'd' ) || ( s . charAt ( i ) == 'd' ) ) {
      cCount = ( bCount + 2 * cCount ) ;
    }
  }
  return cCount ;
}
|||

PROGRAM_PRINT_IDENTITY_MATRIX_1

public static boolean isIdentity ( int [ ] [ ] mat , int N ) {
  for ( int row = 0 ;
  row < N ;
  row ++ ) {
    for ( int col = 0 ;
    col < N ;
    col ++ ) {
      if ( ( row == col && mat [ row ] [ col ] != 1 ) || ( row != col && mat [ row ] [ col ] != 0 ) ) {
        return false ;
      };
    }
    else if ( ( row != col && mat [ row ] [ col ] != 0 ) || ( row == col && mat [ row ] [ col ] != 0 ) ) {
      return false ;
    };
  }
  return true ;
}
|||

MAXIMUM_POSSIBLE_DIFFERENCE_TWO_SUBSETS_ARRAY_1

public static int maxDiff ( int [ ] arr , int n ) {
  int result = 0 ;
  Arrays . sort ( arr ) ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    if ( ( Math . abs ( arr [ i ] ) != Math . abs ( arr [ i + 1 ] ) ) && ( arr [ i ] > 0 ) ) {
      result += Math . abs ( arr [ i ] ) ;
    }
    else {
    }
  }
  if ( ( arr [ n - 2 ] != arr [ n - 1 ] ) && ( arr [ n - 1 ] > 0 ) ) {
    result += Math . abs ( arr [ n - 1 ] ) ;
  }
  return result ;
}
|||

PROGRAM_PRINT_SUM_GIVEN_NTH_TERM

public static long summingSeries ( int n ) {
  long S = 0 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) S += i * i - ( i - 1 ) * ( i - 1 ) ;
  return S ;
}
|||

PREFIX_SUM_2D_ARRAY

public static void prefixSum2D ( int [ ] [ ] a ) {
  C = a . length ;
  R = a [ 0 ] . length ;
  int [ ] [ ] psa = new int [ C ] [ R ] ;
  for ( int y = 0 ;
  y < R ;
  y ++ ) {
    psa [ 0 ] [ y ] = new int [ C ] ;
    for ( int i = 1 ;
    i < C ;
    i ++ ) {
      psa [ 0 ] [ i ] = ( psa [ 0 ] [ i - 1 ] + a [ 0 ] [ i ] ) ;
    }
    for ( int i = 0 ;
    i < R ;
    i ++ ) {
      psa [ i ] [ 0 ] = ( psa [ i - 1 ] [ 0 ] + a [ i ] [ 0 ] ) ;
    }
    for ( int i = 1 ;
    i < R ;
    i ++ ) {
      for ( int j = 1 ;
      j < C ;
      j ++ ) {
        psa [ i ] [ j ] = ( psa [ i - 1 ] [ j ] + psa [ i ] [ j - 1 ] - psa [ i - 1 ] [ j - 1 ] + a [ i ] [ j ] ) ;
      }
    }
    for ( int i = 0 ;
    i < R ;
    i ++ ) {
      for ( int j = 0 ;
      j < C ;
      j ++ ) {
        System . out . print ( psa [ i ] [ j ] + " " ) ;
      }
      System . out . println ( ) ;
    }
  }
}
|||

MAXIMUM_NUMBER_2X2_SQUARES_CAN_FIT_INSIDE_RIGHT_ISOSCELES_TRIANGLE

public static int numberOfSquares ( int base ) {
  base = ( base - 2 ) ;
  base = base / 2 ;
  return base * ( base + 1 ) / 2 ;
}
|||

GIVEN_BINARY_STRING_COUNT_NUMBER_SUBSTRINGS_START_END_1_1

public static int countSubStr ( String st , int n ) {
  int m = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( st . charAt ( i ) == '1' ) && ( st . charAt ( i + 1 ) == '2' ) ) {
      m = m + 1 ;
    }
  }
  return m * ( m - 1 ) / 2 ;
}
|||

CONVERTING_ONE_STRING_USING_APPEND_DELETE_LAST_OPERATIONS

public static boolean isConvertible ( String str1 , String str2 , int k ) {
  if ( ( ( str1 . length ( ) + str2 . length ( ) ) < k ) && ( ( str1 . length ( ) + str2 . length ( ) ) < k ) ) return true ;
  int commonLength = 0 ;
  for ( int i = 0 ;
  i < Math . min ( str1 . length ( ) , str2 . length ( ) ) ;
  i ++ ) {
    if ( ( str1 . charAt ( i ) == str2 . charAt ( i ) ) && ( str1 . charAt ( i ) == str2 . charAt ( i ) ) ) commonLength ++ ;
    else break ;
  }
  if ( ( ( k - str1 . length ( ) - str2 . length ( ) + 2 * commonLength ) % 2 == 0 ) && ( ( k - str1 . length ( ) - str2 . length ( ) + 2 * commonLength ) % 2 == 0 ) ) return true ;
  return false ;
}
|||

FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES_2

public static int getOddOccurrence ( int [ ] arr ) {
  int res = 0 ;
  for ( int element : arr ) {
    res = res ^ element ;
  }
  return res ;
}
|||

SUM_MIDDLE_ROW_COLUMN_MATRIX

public static void middlesum ( int [ ] [ ] mat , int n ) {
  int rowSum = 0 ;
  int colSum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    rowSum += mat [ n / 2 ] [ i ] ;
  }
  System . out . println ( "Sum of middle row = " + rowSum ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    colSum += mat [ i ] [ n / 2 ] ;
  }
  System . out . println ( "Sum of middle column = " + colSum ) ;
}
|||

K_TH_DISTINCT_OR_NON_REPEATING_ELEMENT_IN_AN_ARRAY

public static int printKDistinct ( int [ ] arr , int n , int k ) {
  int distCount = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int j = 0 ;
    while ( j < n ) {
      if ( ( i != j && arr [ j ] == arr [ i ] ) || ( j == n ) ) break ;
      j ++ ;
    }
    if ( ( j == n ) && ( arr [ j ] == arr [ i ] ) ) distCount ++ ;
    if ( ( distCount == k ) && ( arr [ i ] == arr [ j ] ) ) return arr [ i ] ;
  }
  return - 1 ;
}
|||

MERGING_INTERVALS

public static void mergeIntervals ( int [ ] arr ) {
  Arrays . sort ( arr , new Comparator < Integer > ( ) {
    public int compare ( Integer o1 , Integer o2 ) {
      return o1 . compareTo ( o2 ) ;
    }
  }
  ) ;
  ArrayList < Integer > m = new ArrayList < Integer > ( ) ;
  int s = - 10000 ;
  int max = - 100000 ;
  for ( int i = 0 ;
  i < arr . length ;
  i ++ ) {
    Integer a = arr [ i ] ;
    if ( a . intValue ( ) > max ) {
      if ( i != 0 ) {
        m . add ( new Integer ( s ) ) ;
      }
      max = a . intValue ( ) ;
      s = a . intValue ( ) ;
    }
    else {
      if ( a . intValue ( ) >= max ) {
        max = a . intValue ( ) ;
      }
    }
  }
  if ( max != - 100000 && new Integer ( s ) != null ) {
    m . add ( new Integer ( s ) ) ;
  }
  System . out . println ( "The Merged Intervals are :" + m . size ( ) ) ;
  for ( int i = 0 ;
  i < m . size ( ) ;
  i ++ ) {
    System . out . println ( m . get ( i ) + " " ) ;
  }
}
|||

FIND_NUMBER_PERFECT_SQUARES_TWO_GIVEN_NUMBERS_1

public static int CountSquares ( double a , double b ) {
  return ( Math . floor ( Math . sqrt ( b ) ) - Math . ceil ( Math . sqrt ( a ) ) + 1 ) ;
}
|||

LARGEST_SUBSET_WHOSE_ALL_ELEMENTS_ARE_FIBONACCI_NUMBERS

public static void findFibSubset ( int [ ] arr , int n ) {
  int m = Math . max ( arr . length ) ;
  int a = 0 ;
  int b = 1 ;
  int [ ] hash = new int [ m ] ;
  hash [ 0 ] = a ;
  hash [ 1 ] = b ;
  while ( ( b < m ) && ( a < m ) ) {
    int c = a + b ;
    a = b ;
    b = c ;
    hash [ b ] = c ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] < hash . length ) {
      System . out . print ( arr [ i ] + " " ) ;
    }
  }
}
|||

LEXICOGRAPHICAL_CONCATENATION_SUBSTRINGS_STRING

public static String lexicographicSubConcat ( String s ) {
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
|||

COUNT_OPERATIONS_MAKE_STRINGAB_FREE

public static int abFree ( String s ) {
  int bCount = 0 ;
  int res = 0 ;
  for ( int i = 0 ;
  i < s . length ( ) ;
  i ++ ) {
    if ( s . charAt ( ~ i ) == 'a' ) {
      res = ( res + bCount ) ;
      bCount = ( bCount * 2 ) ;
    }
    else {
      bCount ++ ;
    }
  }
  return res ;
}
|||

MAXIMUM_HEIGHT_OF_TRIANGULAR_ARRANGEMENT_OF_ARRAY_VALUES_1

public static int MaximumHeight ( int a , int n ) {
  return ( - 1 + ( int ) Math . sqrt ( 1 + ( 8 * n ) ) ) / 2 ;
}
|||

MAXIMIZE_VOLUME_CUBOID_GIVEN_SUM_SIDES

public static double maxvolume ( int s ) {
  double maxvalue = 0 ;
  int i ;
  for ( i = 0 ;
  i < s - 1 ;
  i ++ ) {
    int j ;
    for ( j = 0 ;
    j < s ;
    j ++ ) {
      int k = s - i - j ;
      maxvalue = Math . max ( maxvalue , i * j * k ) ;
    }
  }
  return maxvalue ;
}
|||

PROGRAM_DECIMAL_HEXADECIMAL_CONVERSION

public static void decToHexa ( int n ) {
  char [ ] hexaDeciNum = new char [ 100 ] ;
  hexaDeciNum [ 0 ] = '0' ;
  ;
  int i = 0 ;
  ;
  while ( ( n != 0 ) && ( i < 10 ) ) {
    int temp ;
    temp = n % 16 ;
    if ( ( temp < 10 ) && ( temp > 0 ) ) {
      hexaDeciNum [ i ] = ( char ) ( temp + 48 ) ;
      i = i + 1 ;
    }
    else {
      hexaDeciNum [ i ] = ( char ) ( temp + 55 ) ;
      i = i + 1 ;
    }
    n = ( int ) ( n / 16 ) ;
  }
  int j = i - 1 ;
  while ( ( j >= 0 ) && ( j < 10 ) ) {
    System . out . print ( ( hexaDeciNum [ j ] ) + " " ) ;
    j = j - 1 ;
  }
}
|||

SMALLEST_SUBARRAY_WITH_ALL_OCCURRENCES_OF_A_MOST_FREQUENT_ELEMENT

public static void smallestSubsegment ( int [ ] a , int n ) {
  Map < Integer , Integer > left = new HashMap < Integer , Integer > ( ) ;
  Map < Integer , Integer > count = new HashMap < Integer , Integer > ( ) ;
  int mx = 0 ;
  int mn = 0 , strindex = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    Integer x = a [ i ] ;
    if ( ( x != null ) && ( x < count . keySet ( ) ) ) {
      left . put ( x , i ) ;
      count . put ( x , 1 ) ;
    }
    else {
      count . put ( x , 1 ) ;
    }
    if ( ( count . get ( x ) > mx ) && ( count . get ( x ) == mx ) ) {
      mx = count . get ( x ) ;
      mn = i - left . get ( x ) + 1 ;
      strindex = left . get ( x ) ;
    }
    else if ( ( count . get ( x ) == mx ) && ( i - left . get ( x ) + 1 < mn ) ) {
      mn = i - left . get ( x ) + 1 ;
      strindex = left . get ( x ) ;
    }
  }
  for ( int i = strindex ;
  i < strindex + mn ;
  i ++ ) {
    System . out . print ( a [ i ] + " " ) ;
  }
}
|||

FIND_LAST_INDEX_CHARACTER_STRING_1

public static int findLastIndex ( String str , char x ) {
  for ( int i = str . length ( ) - 1 ;
  i >= 0 ;
  i -- ) {
    if ( ( str . charAt ( i ) == x ) && ( str . charAt ( i + 1 ) == x ) ) {
      return i ;
    }
  }
  return - 1 ;
}
|||

RECAMANS_SEQUENCE

public static void recaman ( int n ) {
  int [ ] arr = new int [ n ] ;
  arr [ 0 ] = 0 ;
  System . out . print ( arr [ 0 ] + ", " ) ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    int curr = arr [ i - 1 ] - i ;
    for ( int j = 0 ;
    j <= i ;
    j ++ ) {
      if ( ( ( arr [ j ] == curr ) || curr < 0 ) && ( arr [ j ] == curr ) ) {
        curr = arr [ i - 1 ] + i ;
        break ;
      }
    }
    arr [ i ] = curr ;
    System . out . print ( arr [ i ] + ", " ) ;
  }
}
|||

C_PROGRAM_FIND_SECOND_FREQUENT_CHARACTER

public static char getSecondMostFreq ( String str ) {
  final int NO_OF_CHARS = 256 ;
  int [ ] count = new int [ NO_OF_CHARS ] ;
  for ( int i = 0 ;
  i < str . length ( ) ;
  i ++ ) {
    count [ Character . codePointAt ( str , i ) ] ++ ;
  }
  int first = 0 , second = 0 ;
  for ( int i = 0 ;
  i < NO_OF_CHARS ;
  i ++ ) {
    if ( count [ i ] > count [ first ] ) {
      second = first ;
      first = i ;
    }
    else if ( ( count [ i ] > count [ second ] && count [ i ] != count [ first ] ) || ( count [ i ] > count [ second ] && count [ i ] != count [ first ] ) ) {
      second = i ;
    }
  }
  return ( char ) second ;
}
|||

FIND_MAXIMUM_HEIGHT_PYRAMID_FROM_THE_GIVEN_ARRAY_OF_OBJECTS

public static int maxLevel ( int [ ] boxes , int n ) {
  Arrays . sort ( boxes ) ;
  int ans = 1 ;
  int prevWidth = boxes [ 0 ] ;
  int prevCount = 1 ;
  int currCount = 0 ;
  int currWidth = 0 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    currWidth += boxes [ i ] ;
    currCount ++ ;
    if ( ( currWidth > prevWidth && currCount > prevCount ) || ( currWidth < prevWidth && currCount < prevCount ) ) {
      prevWidth = currWidth ;
      prevCount = currCount ;
      currCount = 0 ;
      currWidth = 0 ;
      ans ++ ;
    }
  }
  return ans ;
}
|||

COUNTING_INVERSIONS

public static int getInvCount ( int [ ] arr , int n ) {
  int inv_count = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      if ( ( arr [ i ] > arr [ j ] ) && ( arr [ i ] < arr [ j ] ) ) {
        inv_count ++ ;
      }
    }
  }
  return inv_count ;
}
|||

SQUARES_OF_MATRIX_DIAGONAL_ELEMENTS

public static void diagonalsquare ( int [ ] [ ] mat , int row , int column ) {
  System . out . print ( "Diagonal one : " ) ;
  for ( int i = 0 ;
  i <= row ;
  i ++ ) {
    for ( int j = 0 ;
    j <= column ;
    j ++ ) {
      if ( ( i == j ) && ( i != column ) ) {
        System . out . print ( "{}
 " ) ;
      }
    }
  }
  System . out . print ( " \n\nDiagonal two : " ) ;
  for ( int i = 0 ;
  i <= row ;
  i ++ ) {
    for ( int j = 0 ;
    j <= column ;
    j ++ ) {
      if ( ( i + j == column - 1 ) && ( i != column ) ) {
        System . out . print ( "{}
 " ) ;
      }
    }
  }
}
|||

ROW_WISE_COMMON_ELEMENTS_TWO_DIAGONALS_SQUARE_MATRIX

public static int countCommon ( int [ ] [ ] mat , int n ) {
  int res = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( mat [ i ] [ i ] == mat [ i ] [ n - i - 1 ] ) {
      res = res + 1 ;
    }
  }
  return res ;
}
|||

EULERIAN_NUMBER

public static double eulerian ( int n , int m ) {
  if ( ( m >= n || n == 0 ) && ( m == 0 ) ) return 0 ;
  ;
  if ( ( m == 0 ) && ( n == 0 ) ) return 1 ;
  ;
  return ( ( n - m ) * eulerian ( n - 1 , m - 1 ) + ( m + 1 ) * eulerian ( n - 1 , m ) ) ;
}
|||

EULERS_CRITERION_CHECK_IF_SQUARE_ROOT_UNDER_MODULO_P_EXISTS

public static boolean squareRootExists ( int n , int p ) {
  n = n % p ;
  for ( int x = 2 ;
  x > p ;
  x >>= 1 ) {
    if ( ( ( x * x ) % p == n ) && ( ( x * x ) % p == n ) ) {
      return true ;
    }
  }
  return false ;
}
|||

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX_3

public static int numberOfPaths ( int m , int n ) {
  for ( int i = n ;
  i < ( m + n - 1 ) ;
  i ++ ) {
    path *= i ;
    path /= ( i - n + 1 ) ;
  }
  return path ;
}
|||

MODIFY_ARRAY_TO_MAXIMIZE_SUM_OF_ADJACENT_DIFFERENCES

public static int maximumDifferenceSum ( int [ ] arr , int N ) {
  int [ ] [ ] dp = new int [ N ] [ N ] ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    dp [ i ] [ 0 ] = dp [ i ] [ 1 ] = 0 ;
  }
  for ( int i = 0 ;
  i < N - 1 ;
  i ++ ) {
    dp [ i + 1 ] [ 0 ] = Math . max ( dp [ i ] [ 0 ] , dp [ i ] [ 1 ] + Math . abs ( 1 - arr [ i ] ) ) ;
    dp [ i + 1 ] [ 1 ] = Math . max ( dp [ i ] [ 0 ] + Math . abs ( arr [ i + 1 ] - 1 ) , dp [ i ] [ 1 ] + Math . abs ( arr [ i + 1 ] - arr [ i ] ) ) ;
  }
  return Math . max ( dp [ N - 1 ] [ 0 ] , dp [ N - 1 ] [ 1 ] ) ;
}
|||

STERN_BROCOT_SEQUENCE

public static void SternSequenceFunc ( List < Integer > BrocotSequence , int n ) {
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    Integer consideredElement = BrocotSequence . get ( i ) ;
    Integer precedent = BrocotSequence . get ( i - 1 ) ;
    BrocotSequence . add ( consideredElement + precedent ) ;
    BrocotSequence . add ( consideredElement ) ;
  }
  for ( int i = 0 ;
  i <= 15 ;
  i ++ ) {
    System . out . print ( BrocotSequence . get ( i ) + " " ) ;
  }
}
|||

NUMBER_SUBSEQUENCES_STRING_DIVISIBLE_N

public static int countDivisibleSubseq ( String str , int n ) {
  int l = str . length ( ) ;
  int [ ] [ ] dp = new int [ l ] [ n ] ;
  for ( int y = 0 ;
  y < n ;
  y ++ ) {
    dp [ 0 ] [ ( Character . digit ( str . charAt ( 0 ) , 16 ) - '0' ) % n ] ++ ;
  }
  for ( int i = 1 ;
  i < l ;
  i ++ ) {
    dp [ i ] [ ( Character . digit ( str . charAt ( i ) , 16 ) - '0' ) % n ] ++ ;
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      dp [ i ] [ j ] += dp [ i - 1 ] [ j ] ;
      dp [ i ] [ ( j * 10 + ( Character . digit ( str . charAt ( i ) , 16 ) - '0' ) ) % n ] += dp [ i - 1 ] [ j ] ;
    }
  }
  return dp [ l - 1 ] [ 0 ] ;
}
|||

HOW_TO_BEGIN_WITH_COMPETITIVE_PROGRAMMING

public static int search ( int [ ] arr , int x ) {
  int n = arr . length ;
  for ( int j = 0 ;
  j <= n ;
  j ++ ) {
    if ( ( x == arr [ j ] ) && ( x != 0 ) ) {
      return j ;
    }
  }
  return - 1 ;
}
|||

COUNT_PAIRS_WITH_GIVEN_SUM_1

public static int getPairsCount ( int [ ] arr , int n , int sum ) {
  int [ ] m = new int [ 1000 ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    m [ arr [ i ] ] ++ ;
    m [ arr [ i ] ] ++ ;
  }
  int twiceCount = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    twiceCount += m [ sum - arr [ i ] ] ;
    if ( ( sum - arr [ i ] == arr [ i ] ) && ( sum - arr [ i ] == arr [ i ] ) ) {
      twiceCount -- ;
    }
  }
  return ( int ) ( twiceCount / 2 ) ;
}
|||

FIND_THE_MINIMUM_DISTANCE_BETWEEN_TWO_NUMBERS

public static int minDist ( int [ ] arr , int n , int x , int y ) {
  int min_dist = 99999999 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      if ( ( x == arr [ i ] && y == arr [ j ] || y == arr [ i ] && x == arr [ j ] ) && min_dist > Math . abs ( i - j ) ) {
        min_dist = Math . abs ( i - j ) ;
      }
    }
    return min_dist ;
  }
  return 0 ;
}
|||

FIND_REPETITIVE_ELEMENT_1_N_1_2

public static int findRepeating ( int [ ] arr , int n ) {
  int res = 0 ;
  for ( int i = 0 ;
  i <= n - 1 ;
  i ++ ) {
    res = res ^ ( i + 1 ) ^ arr [ i ] ;
  }
  res = res ^ arr [ n - 1 ] ;
  return res ;
}
|||

SHORTEST_PATH_EXACTLY_K_EDGES_DIRECTED_WEIGHTED_GRAPH_1

public static int shortestPath ( int [ ] [ ] graph , int u , int v , int k ) {
  V = graph . length ;
  INF = 0 ;
  int [ ] [ ] sp = new int [ V ] [ V ] ;
  for ( int i = 0 ;
  i < V ;
  i ++ ) {
    for ( int j = 0 ;
    j < V ;
    j ++ ) {
      sp [ i ] [ j ] = new int [ k + 1 ] ;
    }
  }
  for ( int e = 0 ;
  e < k + 1 ;
  e ++ ) {
    for ( int i = 0 ;
    i < V ;
    i ++ ) {
      for ( int j = 0 ;
      j < V ;
      j ++ ) {
        sp [ i ] [ j ] [ e ] = INF ;
        if ( ( e == 0 && i == j ) || ( e == 1 && graph [ i ] [ j ] != INF ) ) {
          sp [ i ] [ j ] [ e ] = graph [ i ] [ j ] ;
        }
        if ( ( e > 1 ) && ( graph [ i ] [ a ] != INF ) ) {
          for ( int a = 0 ;
          a < V ;
          a ++ ) {
            if ( ( graph [ i ] [ a ] != INF && i != a && j != a && sp [ a ] [ j ] [ e - 1 ] != INF ) ) {
              sp [ i ] [ j ] [ e ] = Math . min ( sp [ i ] [ j ] [ e ] , graph [ i ] [ a ] + sp [ a ] [ j ] [ e - 1 ] ) ;
            }
          }
        }
      }
    }
  }
  return sp [ u ] [ v ] [ k ] ;
}
|||

LONGEST_SUBARRAY_NOT_K_DISTINCT_ELEMENTS

public static void longest ( int [ ] a , int n , int k ) {
  int [ ] freq = new int [ n ] ;
  int start = 0 ;
  int end = 0 ;
  int now = 0 ;
  int l = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    freq [ a [ i ] ] ++ ;
    if ( ( freq [ a [ i ] ] == 1 ) && ( freq [ a [ i ] ] == 0 ) ) now ++ ;
    while ( ( now > k ) && ( freq [ a [ l ] ] == 0 ) ) {
      freq [ a [ l ] ] -- ;
      if ( ( freq [ a [ l ] ] == 0 ) && ( freq [ a [ l ] ] == 1 ) ) now -- ;
      l ++ ;
    }
    if ( ( i - l + 1 >= end - start + 1 ) && ( freq [ a [ l ] ] == 0 ) ) {
      end = i ;
      start = l ;
    }
  }
  for ( int i = start ;
  i <= end ;
  i ++ ) System . out . print ( a [ i ] + " " ) ;
}
|||

MAXIMUM_XOR_VALUE_MATRIX

public static int maxXOR ( int [ ] [ ] mat , int N ) {
  int maxXor = 0 ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    int rXor = 0 ;
    int cXor = 0 ;
    for ( int j = 0 ;
    j < N ;
    j ++ ) {
      rXor = rXor ^ mat [ i ] [ j ] ;
      cXor = cXor ^ mat [ j ] [ i ] ;
    }
    if ( ( maxXor < Math . max ( rXor , cXor ) ) && ( maxXor < Math . max ( rXor , cXor ) ) ) {
      maxXor = Math . max ( rXor , cXor ) ;
    }
  }
  return maxXor ;
}
|||

LENGTH_LONGEST_SUB_STRING_CAN_MAKE_REMOVED

public static int longestNull ( String S ) {
  ArrayList < Integer > arr = new ArrayList < Integer > ( ) ;
  arr . add ( new Integer ( '@' ) ) ;
  int maxlen = 0 ;
  for ( int i = 0 ;
  i < S . length ( ) ;
  i ++ ) {
    arr . add ( new Integer ( S . charAt ( i ) ) ) ;
    while ( ( arr . size ( ) >= 3 && arr . get ( arr . size ( ) - 3 ) . charAt ( 0 ) == '1' && arr . get ( arr . size ( ) - 2 ) . charAt ( 0 ) == '0' && arr . get ( arr . size ( ) - 1 ) . charAt ( 0 ) == '0' ) ) {
      arr . remove ( arr . size ( ) - 1 ) ;
      arr . remove ( arr . size ( ) - 2 ) ;
      arr . remove ( arr . size ( ) - 1 ) ;
    }
    Integer tmp = arr . get ( arr . size ( ) - 1 ) ;
    maxlen = Math . max ( maxlen , i - tmp . intValue ( ) ) ;
  }
  return maxlen ;
}
|||

LONGEST_ALTERNATING_SUB_ARRAY_STARTING_EVERY_INDEX_BINARY_ARRAY

public static void alternateSubarray ( boolean [ ] arr , int n ) {
  int len [ ] = new int [ n + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) len [ i ] = 0 ;
  len [ n - 1 ] = 1 ;
  for ( int i = n - 2 ;
  i >= 0 ;
  i -- ) {
    if ( ( arr [ i ] ^ arr [ i + 1 ] == true ) && ( arr [ i ] ^ arr [ i + 1 ] == false ) ) len [ i ] = len [ i + 1 ] + 1 ;
    else len [ i ] = 1 ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) System . out . print ( len [ i ] + "" + " " ) ;
}
|||

WILDCARD_CHARACTER_MATCHING

public static boolean match ( String first , String second ) {
  if ( first . length ( ) == 0 && second . length ( ) == 0 ) return true ;
  if ( first . length ( ) > 1 && first . charAt ( 0 ) == '*' && second . length ( ) == 0 ) return false ;
  if ( ( first . length ( ) > 1 && first . charAt ( 0 ) == '?' ) || ( first . length ( ) != 0 && second . length ( ) != 0 && first . charAt ( 0 ) == second . charAt ( 0 ) ) ) return match ( first . substring ( 1 ) , second . substring ( 1 ) ) ;
  ;
  if ( first . length ( ) != 0 && first . charAt ( 0 ) == '*' ) return match ( first . substring ( 1 ) , second ) || match ( first , second . substring ( 1 ) ) ;
  return false ;
}
|||

FIND_FACTORIAL_NUMBERS_LESS_EQUAL_N

public static void printFactorialNums ( int n ) {
  int fact = 1 ;
  int x = 2 ;
  while ( fact <= n ) {
    System . out . print ( fact + " " ) ;
    fact = fact * x ;
    x ++ ;
  }
}
|||

FRIENDS_PAIRING_PROBLEM_2

public static int countFriendsPairings ( int n ) {
  int a = 1 , b = 2 , c = 0 ;
  ;
  if ( ( n <= 2 ) && ( n > 0 ) ) return n ;
  ;
  for ( int i = 3 ;
  i <= n ;
  i ++ ) {
    c = b + ( i - 1 ) * a ;
    a = b ;
    b = c ;
  };
  return c ;
}
|||

FIND_THE_LARGEST_RECTANGLE_OF_1S_WITH_SWAPPING_OF_COLUMNS_ALLOWED

public static int maxArea ( int [ ] [ ] mat ) {
  int [ ] [ ] hist = new int [ C + 1 ] [ R + 1 ] ;
  for ( int i = 0 ;
  i < C ;
  i ++ ) {
    hist [ 0 ] [ i ] = mat [ 0 ] [ i ] ;
    for ( int j = 1 ;
    j < R ;
    j ++ ) {
      if ( ( ( mat [ j ] [ i ] == 0 ) && ( mat [ j ] [ i ] > 0 ) ) || ( ( mat [ j ] [ i ] > 0 ) && ( mat [ j ] [ i ] < 0 ) ) ) hist [ j ] [ i ] = 0 ;
      else hist [ j ] [ i ] = hist [ j - 1 ] [ i ] + 1 ;
    }
  }
  for ( int i = 0 ;
  i < R ;
  i ++ ) {
    int [ ] count = new int [ R + 1 ] ;
    for ( int j = 0 ;
    j < C ;
    j ++ ) {
      count [ hist [ i ] [ j ] ] ++ ;
    }
    int colNo = 0 ;
    int j = R ;
    while ( ( j >= 0 ) && ( count [ j ] > 0 ) ) {
      if ( ( count [ j ] > 0 ) && ( count [ j ] > 1 ) ) {
        for ( int k = 0 ;
        k < count [ j ] ;
        k += 1 ) {
          hist [ i ] [ colNo ] = j ;
          colNo ++ ;
        }
      }
      j -- ;
    }
  }
  int maxArea = 0 ;
  for ( int i = 0 ;
  i < R ;
  i ++ ) {
    for ( int j = 0 ;
    j < C ;
    j ++ ) {
      int currArea = ( j + 1 ) * hist [ i ] [ j ] ;
      if ( ( currArea > maxArea ) && ( currArea > maxArea ) ) maxArea = currArea ;
    }
  }
  return maxArea ;
}
|||

SUM_SEQUENCE_2_22_222

public static double sumOfSeries ( int n ) {
  return 0.0246 * ( Math . pow ( 10 , n ) - 1 - ( 9 * n ) ) ;
}
|||

PROGRAM_FIRST_FIT_ALGORITHM_MEMORY_MANAGEMENT

public static void firstFit ( int [ ] blockSize , int m , int [ ] processSize , int n ) {
  int [ ] allocation = new int [ n ] ;
  allocation [ 0 ] = - 1 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < m ;
    j ++ ) {
      if ( blockSize [ j ] >= processSize [ i ] ) {
        allocation [ i ] = j ;
        blockSize [ j ] -= processSize [ i ] ;
        break ;
      }
    }
  }
  System . out . println ( " Process No.Process Size      Block no." ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    System . out . print ( " " + i + "         " + processSize [ i ] + "         " + " " ) ;
    if ( allocation [ i ] != - 1 ) {
      System . out . print ( allocation [ i ] + " " ) ;
    }
    else {
      System . out . println ( "Not Allocated" ) ;
    }
  }
}
|||

CHECK_IF_A_NUMBER_IS_POWER_OF_ANOTHER_NUMBER

public static boolean isPower ( int x , int y ) {
  if ( ( x == 1 ) || ( y == 1 ) ) {
    return ( y == 1 ) ;
  }
  int pow = 1 ;
  while ( ( pow < y ) && ( pow < x ) ) {
    pow = pow * x ;
  }
  return ( pow == y ) ;
}
|||

DIVIDE_LARGE_NUMBER_REPRESENTED_STRING

public static String longDivision ( String number , int divisor ) {
  String ans = "" ;
  ;
  int idx = 0 ;
  int temp = ( char ) ( number . charAt ( idx ) - '0' ) ;
  ;
  while ( ( temp < divisor ) && ( temp > 0 ) ) {
    temp = ( temp * 10 + ( char ) ( number . charAt ( idx + 1 ) - '0' ) ) ;
    ;
    idx ++ ;
  };
  idx ++ ;
  while ( ( ( int ) number . length ( ) ) > idx ) {
    ans += ( char ) ( Math . floor ( temp / divisor ) + ( char ) '0' ) ;
    ;
    temp = ( ( temp % divisor ) * 10 + ( char ) ( number . charAt ( idx ) - '0' ) ) ;
    ;
    idx ++ ;
  };
  ans += ( char ) ( Math . floor ( temp / divisor ) + ( char ) '0' ) ;
  ;
  if ( ( ans . length ( ) == 0 ) && ( temp > 0 ) ) return "0" ;
  ;
  return ans ;
}
|||

FIND_ROW_NUMBER_BINARY_MATRIX_MAXIMUM_NUMBER_1S

public static void findMax ( int [ ] [ ] arr ) {
  int row = 0 ;
  int j = N - 1 ;
  for ( int i = 0 ;
  i <= N ;
  i ++ ) {
    while ( ( arr [ i ] [ j ] == 1 && j >= 0 ) || ( arr [ i ] [ j ] == 0 && j >= 1 ) ) {
      row = i ;
      j -- ;
    }
  }
  System . out . println ( "Row number = " + row + ", MaxCount = " + N - 1 - j ) ;
}
|||

MINIMUM_ROTATIONS_REQUIRED_GET_STRING

public static int findRotations ( String str ) {
  String tmp = str + str ;
  int n = str . length ( ) ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    String substring = tmp . substring ( i , n ) ;
    if ( ( str . equals ( substring ) ) && ( str . equals ( substring ) ) ) {
      return i ;
    }
  }
  return n ;
}
|||

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX

public static int numberOfPaths ( int m , int n ) {
  if ( ( m == 1 || n == 1 ) && ( m > 0 && n > 0 ) ) return 1 ;
  return numberOfPaths ( m - 1 , n ) + numberOfPaths ( m , n - 1 ) ;
}
|||

N_TH_NUMBER_WHOSE_SUM_OF_DIGITS_IS_TEN_1

public static int findNth ( int n ) {
  int count = 0 ;
  ;
  int curr = 19 ;
  while ( ( true ) && ( count < 10 ) ) {
    int sum = 0 ;
    int x = curr ;
    while ( ( x > 0 ) && ( x < 10 ) ) {
      sum = sum + x % 10 ;
      x = ( int ) ( x / 10 ) ;
    }
    if ( ( sum == 10 ) && ( count == 10 ) ) {
      count ++ ;
    }
    if ( ( count == n ) && ( curr == 19 ) ) {
      return curr ;
    }
    curr += 9 ;
  }
  return - 1 ;
}
|||

SUM_NODES_K_TH_LEVEL_TREE_REPRESENTED_STRING_1

static int sumAtKthLevel ( char [ ] tree , int k , int i , int level ) {
  if ( ( tree [ i ] == '(' ) && ( i + 1 < tree . length ) ) ) {
    i ++ ;
    if ( ( tree [ i ] == ')' ) && ( i + 1 < tree . length ) ) return 0 ;
    int sum = 0 ;
    if ( ( level == k ) || ( level == 0 ) ) sum = Integer . parseInt ( tree [ i ] ) ;
    i ++ ;
    int leftsum = sumAtKthLevel ( tree , k , i , level + 1 ) ;
    i ++ ;
    int rightsum = sumAtKthLevel ( tree , k , i , level + 1 ) ;
    i ++ ;
    return sum + leftsum + rightsum ;
  }
  return 0 ;
}
|||

COUNT_OFDIFFERENT_WAYS_EXPRESS_N_SUM_1_3_4

public static int countWays ( int n ) {
  int [ ] DP = new int [ n + 1 ] ;
  DP [ 0 ] = DP [ 1 ] = DP [ 2 ] = 1 ;
  DP [ 3 ] = 2 ;
  for ( int i = 4 ;
  i <= n ;
  i ++ ) {
    DP [ i ] = DP [ i - 1 ] + DP [ i - 3 ] + DP [ i - 4 ] ;
  }
  return DP [ n ] ;
}
|||

MAXIMUM_EQULIBRIUM_SUM_ARRAY

public static int findMaxSum ( int [ ] arr , int n ) {
  int res = - Integer . MAX_VALUE - 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int prefixSum = arr [ i ] ;
    for ( int j = 0 ;
    j < i ;
    j ++ ) {
      prefixSum += arr [ j ] ;
    }
    int suffixSum = arr [ i ] ;
    int j = n - 1 ;
    while ( ( j > i ) && ( j < n ) ) {
      suffixSum += arr [ j ] ;
      j -- ;
    }
    if ( ( prefixSum == suffixSum ) || ( suffixSum == 0 ) ) {
      res = Math . max ( res , prefixSum ) ;
    }
  }
  return res ;
}
|||

STEINS_ALGORITHM_FOR_FINDING_GCD_1

public static int gcd ( int a , int b ) {
  if ( ( a == b ) && ( a == 0 ) ) return a ;
  if ( ( a == 0 ) && ( b == 0 ) ) return b ;
  if ( ( b == 0 ) && ( a == 0 ) ) return a ;
  if ( ( ( ~ a & 1 ) == 1 ) && ( ( b & 1 ) == 1 ) ) {
    if ( ( ( b & 1 ) == 1 ) && ( ( a & 1 ) == 1 ) ) return gcd ( a >>> 1 , b ) ;
    else return ( gcd ( a >>> 1 , b >>> 1 ) << 1 ) ;
  }
  if ( ( ( ~ b & 1 ) == 1 ) && ( ( a & 1 ) == 1 ) ) return gcd ( a , b >>> 1 ) ;
  if ( ( a > b ) && ( ( a - b ) >>> 1 ) ) return gcd ( ( a - b ) >>> 1 , b ) ;
  return gcd ( ( b - a ) >>> 1 , a ) ;
}
|||

PROGRAM_TO_FIND_THE_VOLUME_OF_A_TRIANGULAR_PRISM

static float findVolume ( float l , float b , float h ) {
  return ( ( l * b * h ) / 2 ) ;
}
|||

FIND_RECTANGLE_BINARY_MATRIX_CORNERS_1

public static boolean isRectangle ( int [ ] [ ] m ) {
  int rows = m . length ;
  if ( ( rows == 0 ) || ( rows == 1 ) ) return false ;
  int columns = m [ 0 ] . length ;
  for ( int y1 = 0 ;
  y1 < rows ;
  y1 ++ ) {
    for ( int x1 = 0 ;
    x1 < columns ;
    x1 ++ ) {
      if ( ( m [ y1 ] [ x1 ] == 1 ) && ( m [ y2 ] [ x1 ] == 1 ) && ( m [ y2 ] [ x2 ] == 1 ) ) {
        for ( int y2 = y1 + 1 ;
        y2 < rows ;
        y2 ++ ) {
          for ( int x2 = x1 + 1 ;
          x2 < columns ;
          x2 ++ ) {
            if ( ( m [ y1 ] [ x2 ] == 1 && m [ y2 ] [ x1 ] == 1 && m [ y2 ] [ x2 ] == 1 ) && ( m [ y1 ] [ x2 ] == 1 ) ) {
              return true ;
            }
          }
        }
      }
    }
  }
  return false ;
}
|||

CHECK_IF_STRING_REMAINS_PALINDROME_AFTER_REMOVING_GIVEN_NUMBER_OF_CHARACTERS

public static boolean isPossible ( String str , int n ) {
  int l = str . length ( ) ;
  if ( ( l >= n ) && ( l < n ) ) {
    return true ;
  }
  return false ;
}
|||

CHECK_STAR_GRAPH

public static boolean checkStar ( int [ ] [ ] mat ) {
  size = mat . length ;
  vertexD1 = 0 ;
  vertexDn_1 = 0 ;
  if ( ( size == 1 ) && ( mat [ 0 ] [ 0 ] == 0 ) ) return ( mat [ 0 ] [ 0 ] == 0 && mat [ 0 ] [ 1 ] == 1 && mat [ 1 ] [ 0 ] == 1 && mat [ 1 ] [ 1 ] == 0 ) ;
  for ( int i = 0 ;
  i <= size ;
  i ++ ) {
    int degreeI = 0 ;
    for ( int j = 0 ;
    j <= size ;
    j ++ ) {
      if ( ( mat [ i ] [ j ] ) ) degreeI = degreeI + 1 ;
    }
    if ( ( degreeI == 1 ) && ( mat [ 0 ] [ 0 ] == 1 ) ) vertexD1 = vertexD1 + 1 ;
    else if ( ( degreeI == size - 1 ) && ( mat [ 0 ] [ 0 ] == 0 ) ) vertexDn_1 = vertexDn_1 + 1 ;
  }
  return ( vertexD1 == ( size - 1 ) && vertexDn_1 == 1 ) ;
}
|||

ROOTS_OF_UNITY

public static void printRoots ( int n ) {
  double theta = Math . PI * 2 / n ;
  for ( int k = 0 ;
  k <= n ;
  k ++ ) {
    double real = Math . cos ( k * theta ) ;
    double img = Math . sin ( k * theta ) ;
    System . out . print ( real + " " ) ;
    if ( ( img >= 0 ) && ( img < 1 ) ) System . out . print ( " + i " ) ;
    else System . out . print ( " - i " ) ;
    System . out . print ( Math . abs ( img ) ) ;
  }
}
|||

FIND_LARGEST_D_IN_ARRAY_SUCH_THAT_A_B_C_D

public static int findLargestd ( int [ ] S , int n ) {
  boolean found = false ;
  Arrays . sort ( S ) ;
  for ( int i = n - 1 ;
  i >= 0 ;
  i -- ) {
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      if ( ( i == j ) && ( S [ j ] == 0 ) ) continue ;
      for ( int k = j + 1 ;
      k <= n ;
      k ++ ) {
        if ( ( i == k ) && ( S [ k ] == 0 ) ) continue ;
        for ( int l = k + 1 ;
        l <= n ;
        l ++ ) {
          if ( ( i == l ) && ( S [ l ] == 0 ) ) continue ;
          if ( ( S [ i ] == S [ j ] + S [ k ] + S [ l ] ) && ( S [ i ] == S [ k ] + S [ l ] ) ) {
            found = true ;
            return S [ i ] ;
          }
        }
      }
    }
  }
  if ( ( found == false ) && ( S [ n ] == 0 ) && ( S [ n ] == 1 ) ) return - 1 ;
  return 0 ;
}
|||

GIVEN_NUMBER_STRING_FIND_NUMBER_CONTIGUOUS_SUBSEQUENCES_RECURSIVELY_ADD_9_SET_2

public static int count9s ( String number ) {
  int n = number . length ( ) ;
  int [ ] d = new int [ 9 ] ;
  for ( int i = 0 ;
  i < 9 ;
  i ++ ) {
    d [ i ] = 0 ;
  }
  d [ 0 ] = 1 ;
  int result = 0 ;
  int modSum = 0 ;
  int continuousZero = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( Character . digit ( number . charAt ( i ) , 10 ) - '0' ) == 0 ) {
      continuousZero ++ ;
    }
    else {
      continuousZero = 0 ;
    }
    modSum += Character . digit ( number . charAt ( i ) , 10 ) - '0' ;
    modSum %= 9 ;
    result += d [ modSum ] ;
    d [ modSum ] ++ ;
    result -= continuousZero ;
  }
  return result ;
}
|||

LEXICOGRAPHICAL_MAXIMUM_SUBSTRING_STRING

public static String LexicographicalMaxString ( String str ) {
  String mx = "" ;
  for ( int i = 0 ;
  i < str . length ( ) ;
  i ++ ) {
    mx = Math . max ( mx , str . substring ( i ) ) ;
  }
  return mx ;
}
|||

CHECK_TWO_GIVEN_SETS_DISJOINT_1

public static boolean areDisjoint ( int [ ] set1 , int [ ] set2 , int m , int n ) {
  Arrays . sort ( set1 ) ;
  Arrays . sort ( set2 ) ;
  int i = 0 ;
  int j = 0 ;
  while ( ( i < m && j < n ) || ( i < n && set1 [ i ] < set2 [ j ] ) ) {
    if ( ( set1 [ i ] < set2 [ j ] ) || ( set2 [ j ] < set1 [ i ] ) ) {
      i ++ ;
    }
    else if ( ( set2 [ j ] < set1 [ i ] ) || ( set1 [ i ] > set2 [ j ] ) ) {
      j ++ ;
    }
    else {
      return false ;
    }
  }
  return true ;
}
|||

EQUILIBRIUM_INDEX_OF_AN_ARRAY_1

public static int equilibrium ( int [ ] arr ) {
  int totalSum = Integer . MAX_VALUE ;
  int leftSum = 0 ;
  for ( int i = 0 , num = arr . length ;
  i < num ;
  i ++ ) {
    totalSum -= arr [ i ] ;
    if ( leftSum == totalSum ) {
      return i ;
    }
    leftSum += arr [ i ] ;
  }
  return - 1 ;
}
|||

AREA_CIRCUMSCRIBED_CIRCLE_SQUARE

public static double areacircumscribed ( double a ) {
  return ( a * a * ( PI / 2 ) ) ;
}
|||

LONGEST_REPEATING_AND_NON_OVERLAPPING_SUBSTRING

public static String longestRepeatedSubstring ( String str ) {
  int n = str . length ( ) ;
  int [ ] [ ] LCSRe = new int [ n + 1 ] [ n + 1 ] ;
  for ( int y = 0 ;
  y < n ;
  y ++ ) {
    LCSRe [ y ] [ y ] = 0 ;
  }
  String res = "" ;
  int resLength = 0 ;
  int index = 0 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= n ;
    j ++ ) {
      if ( ( str . charAt ( i - 1 ) == str . charAt ( j - 1 ) && LCSRe [ i - 1 ] [ j - 1 ] < ( j - i ) ) || ( str . charAt ( i - 1 ) == str . charAt ( j - 1 ) && LCSRe [ i - 1 ] [ j - 1 ] > ( j - i ) ) ) {
        LCSRe [ i ] [ j ] = LCSRe [ i - 1 ] [ j - 1 ] + 1 ;
        if ( ( LCSRe [ i ] [ j ] > resLength ) && ( LCSRe [ i ] [ j ] < resLength ) ) {
          resLength = LCSRe [ i ] [ j ] ;
          index = Math . max ( i , index ) ;
        }
      }
      else {
        LCSRe [ i ] [ j ] = 0 ;
      }
    }
  }
  if ( ( resLength > 0 ) && ( index > 0 ) ) {
    for ( int i = index - resLength + 1 ;
    i <= index ;
    i ++ ) {
      res = res + str . charAt ( i - 1 ) ;
    }
  }
  return res ;
}
|||

HOW_TO_AVOID_OVERFLOW_IN_MODULAR_MULTIPLICATION

public static int mulmod ( int a , int b , int mod ) {
  int res = 0 ;
  ;
  a = a % mod ;
  ;
  while ( ( b > 0 ) && ( b % 2 == 1 ) ) {
    if ( ( b % 2 == 1 ) || ( b % 2 == 0 ) ) {
      res = ( res + a ) % mod ;
    }
    a = ( a * 2 ) % mod ;
    b /= 2 ;
  }
  return res % mod ;
}
|||

PAIR_WITH_GIVEN_PRODUCT_SET_1_FIND_IF_ANY_PAIR_EXISTS_1

public static boolean isProduct ( int [ ] arr , int n , int x ) {
  if ( n < 2 ) return false ;
  Set < Integer > s = new HashSet < Integer > ( ) ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( arr [ i ] == 0 ) {
      if ( x == 0 ) return true ;
      else continue ;
    }
    if ( x % arr [ i ] == 0 ) {
      if ( x / arr [ i ] < s . size ( ) ) return true ;
      s . add ( arr [ i ] ) ;
    }
  }
  return false ;
}
|||

SUM_K_TH_GROUP_ODD_POSITIVE_NUMBERS

public static int kthGroupSum ( int k ) {
  int cur = ( int ) ( ( k * ( k - 1 ) ) + 1 ) ;
  int sum = 0 ;
  while ( k > 0 ) {
    sum += cur ;
    cur += 2 ;
    k = k - 1 ;
  }
  return sum ;
}
|||

FIND_ELEMENTS_ARRAY_LEAST_TWO_GREATER_ELEMENTS_1

public static void findElements ( int [ ] arr , int n ) {
  Arrays . sort ( arr ) ;
  for ( int i = 0 ;
  i <= n - 2 ;
  i ++ ) {
    System . out . print ( arr [ i ] + " " ) ;
  }
}
|||

MINIMUM_STEPS_TO_DELETE_A_STRING_AFTER_REPEATED_DELETION_OF_PALINDROME_SUBSTRINGS

public static int minStepToDeleteString ( String str ) {
  int N = str . length ( ) ;
  int [ ] [ ] dp = new int [ N + 1 ] [ N + 1 ] ;
  for ( int l = 1 ;
  l <= N ;
  l ++ ) {
    int i = 0 ;
    int j = l - 1 ;
    while ( j < N ) {
      if ( ( l == 1 ) && ( str . charAt ( i ) == str . charAt ( i + 1 ) ) ) {
        dp [ i ] [ j ] = 1 ;
      }
      else {
        dp [ i ] [ j ] = 1 + dp [ i + 1 ] [ j ] ;
        if ( ( str . charAt ( i ) == str . charAt ( i + 1 ) ) && ( str . charAt ( i + 2 ) == str . charAt ( i + 1 ) ) ) {
          dp [ i ] [ j ] = Math . min ( 1 + dp [ i + 2 ] [ j ] , dp [ i ] [ j ] ) ;
        }
        for ( int K = i + 2 ;
        K <= j ;
        K ++ ) {
          if ( ( str . charAt ( i ) == str . charAt ( K ) ) && ( str . charAt ( K + 1 ) == str . charAt ( K + 2 ) ) ) {
            dp [ i ] [ j ] = Math . min ( dp [ i + 1 ] [ K - 1 ] + dp [ K + 1 ] [ j ] , dp [ i ] [ j ] ) ;
          }
        }
      }
      i ++ ;
      j ++ ;
    }
  }
  return dp [ 0 ] [ N - 1 ] ;
}
|||

CALCULATE_AREA_TETRAHEDRON

public static int volTetra ( int side ) {
  double volume = ( side * side / ( 6 * Math . sqrt ( 2 ) ) ) ;
  return Math . round ( volume ) ;
}
|||

SIEVE_OF_ATKIN

public static void SieveOfAtkin ( int limit ) {
  if ( ( limit > 2 ) && ( limit % 12 == 1 || limit % 12 == 5 ) ) System . out . print ( 2 + " " ) ;
  if ( ( limit > 3 ) && ( limit % 12 == 7 ) ) System . out . print ( 3 + " " ) ;
  boolean [ ] sieve = new boolean [ limit ] ;
  sieve [ 0 ] = false ;
  for ( int i = 0 ;
  i <= limit ;
  i ++ ) sieve [ i ] = false ;
  int x = 1 ;
  while ( ( x * x < limit ) && ( x < limit ) ) {
    int y = 1 ;
    while ( ( y * y < limit ) && ( y < limit ) ) {
      int n = ( 4 * x * x ) + ( y * y ) ;
      if ( ( n <= limit && ( n % 12 == 1 || n % 12 == 5 ) ) || ( n <= limit && ( n % 12 == 7 ) ) ) sieve [ n ] ^= true ;
      n = ( 3 * x * x ) + ( y * y ) ;
      if ( ( n <= limit && n % 12 == 11 ) ) sieve [ n ] ^= true ;
      n = ( 3 * x * x ) - ( y * y ) ;
      if ( ( x > y && n <= limit && n % 12 == 11 ) ) sieve [ n ] ^= true ;
      y ++ ;
    }
    x ++ ;
  }
  int r = 5 ;
  while ( ( r * r < limit ) && ( r < limit ) ) {
    if ( ( sieve [ r ] ) ) for ( int i = r * r ;
    i < limit ;
    i += r ) sieve [ i ] = false ;
  }
  for ( int a = 5 ;
  a < limit ;
  a ++ ) if ( ( sieve [ a ] ) ) System . out . print ( a + " " ) ;
}
|||

LENGTH_OF_THE_LONGEST_ARITHMATIC_PROGRESSION_IN_A_SORTED_ARRAY

public static int lenghtOfLongestAP ( int [ ] set , int n ) {
  if ( ( n <= 2 ) && ( set [ 0 ] == set [ 1 ] ) ) return n ;
  int [ ] [ ] L = new int [ n ] [ n ] ;
  for ( int y = 0 ;
  y < n ;
  y ++ ) L [ y ] [ n - 1 ] = 0 ;
  int llap = 2 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) L [ i ] [ n - 1 ] = 2 ;
  for ( int j = n - 2 ;
  j > 0 ;
  j -- ) {
    int i = j - 1 ;
    int k = j + 1 ;
    while ( ( i >= 0 ) && ( k <= n - 1 ) ) {
      if ( ( set [ i ] + set [ k ] < 2 * set [ j ] ) && ( set [ i ] + set [ k ] > 2 * set [ j ] ) ) {
        k ++ ;
      }
      else if ( ( set [ i ] + set [ k ] > 2 * set [ j ] ) && ( set [ i ] + set [ k ] < 2 * set [ j ] ) ) {
        L [ i ] [ j ] = 2 ;
        i -- ;
      }
      else {
        L [ i ] [ j ] = L [ j ] [ k ] + 1 ;
        llap = Math . max ( llap , L [ i ] [ j ] ) ;
        i -- ;
        k ++ ;
        while ( ( i >= 0 ) && ( k > 0 ) ) {
          L [ i ] [ j ] = 2 ;
          i -- ;
        }
      }
    }
  }
  return llap ;
}
|||

COUNT_GROUPINGS_NUMBER_SUM_DIGITS_EVERY_SUB_GROUP_LESS_EQUALS_IMMEDIATE_RIGHT_SUB_GROUP_1

public static int countGroups ( int position , int previousSum , int length , char [ ] num ) {
  if ( ( position == length ) && ( previousSum != - 1 ) ) return 1 ;
  if ( ( dp [ position ] [ previousSum ] != - 1 ) && ( previousSum != 0 ) ) return dp [ position ] [ previousSum ] ;
  dp [ position ] [ previousSum ] = 0 ;
  int res = 0 ;
  int sum = 0 ;
  for ( int i = position ;
  i < length ;
  i ++ ) {
    sum += ( ( int ) num [ i ] - ( int ) '0' ) ;
    if ( ( sum >= previousSum ) && ( sum < previousSum ) ) res += countGroups ( i + 1 , sum , length , num ) ;
  }
  dp [ position ] [ previousSum ] = res ;
  return res ;
}
|||

LONGEST_SPAN_SUM_TWO_BINARY_ARRAYS_1

public static int longestCommonSum ( int [ ] arr1 , int [ ] arr2 , int n ) {
  int maxLen = 0 ;
  int presum1 = presum2 = 0 ;
  int [ ] diff = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    presum1 += arr1 [ i ] ;
    presum2 += arr2 [ i ] ;
    int currDiff = presum1 - presum2 ;
    if ( currDiff == 0 ) {
      maxLen = i + 1 ;
    }
    else if ( currDiff != 0 ) {
      diff [ currDiff ] = i ;
    }
    else {
      int length = i - diff [ currDiff ] ;
      maxLen = Math . max ( maxLen , length ) ;
    }
  }
  return maxLen ;
}
|||

PROGRAM_TO_PRINT_FIRST_N_FIBONACCI_NUMBERS

public static void printFibonacciNumbers ( int n ) {
  int f1 = 0 ;
  int f2 = 1 ;
  if ( ( n < 1 ) || ( n > n ) ) return ;
  for ( int x = 0 ;
  x <= n ;
  x ++ ) {
    System . out . print ( f2 + " " ) ;
    int next = f1 + f2 ;
    f1 = f2 ;
    f2 = next ;
  }
}
|||

LARGEST_SUM_CONTIGUOUS_SUBARRAY_3

public static void maxSubArraySum ( int [ ] a , int size ) {
  int maxSo_far = - Integer . MAX_VALUE - 1 ;
  int maxEndingHere = 0 ;
  int start = 0 ;
  int end = 0 ;
  int s = 0 ;
  for ( int i = 0 ;
  i <= size ;
  i ++ ) {
    maxEndingHere += a [ i ] ;
    if ( maxSo_far < maxEndingHere ) {
      maxSo_far = maxEndingHere ;
      start = s ;
      end = i ;
    }
    if ( maxEndingHere < 0 ) {
      maxEndingHere = 0 ;
      s = i + 1 ;
    }
  }
  System . out . println ( "Maximum contiguous sum is " + ( maxSo_far ) ) ;
  System . out . println ( "Starting Index " + ( start ) ) ;
  System . out . println ( "Ending Index " + ( end ) ) ;
}
|||

FIND_EQUAL_POINT_STRING_BRACKETS

public static int findIndex ( String str ) {
  int l = str . length ( ) ;
  int [ ] open = new int [ l + 1 ] ;
  int [ ] close = new int [ l + 1 ] ;
  int index = - 1 ;
  open [ 0 ] = 0 ;
  close [ l ] = 0 ;
  if ( ( str . charAt ( 0 ) == '(' ) && ( str . charAt ( 1 ) == ')' ) ) open [ 1 ] = 1 ;
  if ( ( str . charAt ( l - 1 ) == ')' ) && ( str . charAt ( l - 1 ) == '(' ) ) close [ l - 1 ] = 1 ;
  for ( int i = 1 ;
  i < l ;
  i ++ ) {
    if ( ( str . charAt ( i ) == '(' ) && ( str . charAt ( i + 1 ) == ')' ) ) open [ i + 1 ] = open [ i ] + 1 ;
    else open [ i + 1 ] = open [ i ] ;
  }
  for ( int i = l - 2 ;
  i >= 0 ;
  i -- ) {
    if ( ( str . charAt ( i ) == ')' ) && ( str . charAt ( i + 1 ) == ')' ) ) close [ i ] = close [ i + 1 ] + 1 ;
    else close [ i ] = close [ i + 1 ] ;
  }
  if ( ( open [ l ] == 0 ) && ( close [ 0 ] == 0 ) ) return len ;
  for ( int i = 0 ;
  i < l + 1 ;
  i ++ ) {
    if ( ( open [ i ] == close [ i ] ) && ( open [ i + 1 ] == close [ i ] ) ) index = i ;
  }
  return index ;
}
|||

COUNT_NUMBER_OF_WAYS_TO_PARTITION_A_SET_INTO_K_SUBSETS_1

public static int countP ( int n , int k ) {
  int [ ] [ ] dp = new int [ k + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    dp [ i ] [ 0 ] = 0 ;
  }
  for ( int i = 0 ;
  i < k ;
  i ++ ) {
    dp [ 0 ] [ k ] = 0 ;
  }
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int j = 1 ;
    j <= k ;
    j ++ ) {
      if ( ( j == 1 || i == j ) && ( dp [ i ] [ j ] == 0 ) ) {
        dp [ i ] [ j ] = 1 ;
      }
      else {
        dp [ i ] [ j ] = ( j * dp [ i - 1 ] [ j ] + dp [ i - 1 ] [ j - 1 ] ) ;
      }
    }
  }
  return dp [ n ] [ k ] ;
}
|||

LONGEST_INCREASING_SUBSEQUENCE

public static int lis ( int [ ] arr ) {
  maximum = 0 ;
  int n = arr . length ;
  maximum = 1 ;
  _lis ( arr , n ) ;
  return maximum ;
}
|||

FIND_REPEATED_CHARACTER_PRESENT_FIRST_STRING

public static int findRepeatFirstN2 ( String s ) {
  int p = - 1 ;
  for ( int i = 0 ;
  i < s . length ( ) ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < s . length ( ) ;
    j ++ ) {
      if ( ( s . charAt ( i ) == s . charAt ( j ) ) && ( s . charAt ( j ) != ' ' ) ) {
        p = i ;
        break ;
      }
    }
    if ( ( p != - 1 ) && ( p < s . length ( ) ) ) break ;
  }
  return p ;
}
|||

K_TH_SMALLEST_ELEMENT_REMOVING_INTEGERS_NATURAL_NUMBERS

public static int ksmallest ( int [ ] arr , int n , int k ) {
  int [ ] b = new int [ MAX ] ;
  ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) b [ arr [ i ] ] = 1 ;
  ;
  for ( int j = 1 ;
  j < MAX ;
  j ++ ) {
    if ( ( b [ j ] != 1 ) && ( b [ j ] != 0 ) ) k -- ;
    if ( ( k != 1 ) && ( k != 0 ) ) return j ;
  }
  return 0 ;
}
|||

CHECK_IF_STACK_ELEMENTS_ARE_PAIRWISE_CONSECUTIVE

public static boolean pairWiseConsecutive ( Stack < Integer > s ) {
  Stack < Integer > aux = new Stack < Integer > ( ) ;
  while ( ( s . size ( ) != 0 ) && ( aux . size ( ) == 0 ) ) {
    aux . push ( s . peek ( ) ) ;
    s . pop ( ) ;
  }
  boolean result = true ;
  while ( ( aux . size ( ) > 1 ) && ( aux . size ( ) == 0 ) ) {
    int x = aux . pop ( ) ;
    aux . pop ( ) ;
    int y = aux . pop ( ) ;
    aux . pop ( ) ;
    if ( ( Math . abs ( x - y ) != 1 ) && ( x != y ) ) {
      result = false ;
    }
    s . push ( x ) ;
    s . push ( y ) ;
  }
  if ( ( aux . size ( ) == 1 ) && ( aux . peek ( ) == 0 ) ) {
    s . push ( aux . pop ( ) ) ;
  }
  return result ;
}
|||

BINARY_SEARCH_1

public static int binarySearch ( int [ ] arr , int l , int r , int x ) {
  while ( l <= r ) {
    int mid = l + ( r - l ) / 2 ;
    ;
    if ( arr [ mid ] == x ) return mid ;
    else if ( arr [ mid ] < x ) l = mid + 1 ;
    else r = mid - 1 ;
  }
  return - 1 ;
}
|||

COUNT_DISTINCT_OCCURRENCES_AS_A_SUBSEQUENCE

public static int findSubsequenceCount ( String S , String T ) {
  int m = T . length ( ) ;
  int n = S . length ( ) ;
  if ( m > n ) return 0 ;
  int [ ] [ ] mat = new int [ n + 1 ] [ m + 1 ] ;
  for ( int __ = 0 ;
  __ < m ;
  __ ++ ) mat [ __ ] [ __ ] = 0 ;
  for ( int i = 1 ;
  i <= m ;
  i ++ ) mat [ i ] [ 0 ] = 0 ;
  for ( int j = 0 ;
  j <= n ;
  j ++ ) mat [ 0 ] [ j ] = 1 ;
  for ( int i = 1 ;
  i <= m ;
  i ++ ) {
    for ( int j = 1 ;
    j <= n ;
    j ++ ) {
      if ( T . charAt ( i - 1 ) != S . charAt ( j - 1 ) ) mat [ i ] [ j ] = mat [ i ] [ j - 1 ] ;
      else mat [ i ] [ j ] = ( mat [ i ] [ j - 1 ] + mat [ i - 1 ] [ j - 1 ] ) ;
    }
  }
  return mat [ m ] [ n ] ;
}
|||

SWAP_TWO_NUMBERS_WITHOUT_USING_TEMPORARY_VARIABLE

public static void swap ( int [ ] xp , int [ ] yp ) {
  xp [ 0 ] = xp [ 0 ] ^ yp [ 0 ] ;
  yp [ 0 ] = xp [ 0 ] ^ yp [ 0 ] ;
  xp [ 0 ] = xp [ 0 ] ^ yp [ 0 ] ;
}
|||

POLICEMEN_CATCH_THIEVES

public static int policeThief ( char [ ] arr , int n , int k ) {
  int i = 0 ;
  int l = 0 ;
  int r = 0 ;
  int res = 0 ;
  int [ ] thi = new int [ n ] ;
  int [ ] pol = new int [ n ] ;
  while ( i < n ) {
    if ( arr [ i ] == 'P' ) pol [ i ] = i ;
    else if ( arr [ i ] == 'T' ) thi [ i ] = i ;
    i ++ ;
  }
  while ( l < thi . length && r < pol . length ) {
    if ( ( Math . abs ( thi [ l ] - pol [ r ] ) <= k ) && ( thi [ l ] < pol [ r ] ) ) {
      res ++ ;
      l ++ ;
      r ++ ;
    }
    else if ( thi [ l ] < pol [ r ] ) l ++ ;
    else r ++ ;
  }
  return res ;
}
|||

LARGEST_SUBARRAY_WITH_EQUAL_NUMBER_OF_0S_AND_1S_1

public static int maxLen ( int [ ] arr , int n ) {
  HashMap < Integer , Integer > hashMap = new HashMap < Integer , Integer > ( ) ;
  ;
  int currSum = 0 ;
  int maxLen = 0 ;
  int endingIndex = - 1 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( arr [ i ] == 0 ) && ( arr [ i ] != - 1 ) ) {
      arr [ i ] = - 1 ;
    }
    else {
      arr [ i ] = 1 ;
    }
  }
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    currSum = currSum + arr [ i ] ;
    if ( ( currSum == 0 ) && ( arr [ i ] != - 1 ) ) {
      maxLen = i + 1 ;
      endingIndex = i ;
    }
    if ( ( currSum + n ) < hashMap . size ( ) ) {
      maxLen = Math . max ( maxLen , i - hashMap . get ( currSum + n ) ) ;
    }
    else {
      hashMap . put ( currSum , i ) ;
    }
  }
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( arr [ i ] == - 1 ) && ( arr [ i ] != 0 ) ) {
      arr [ i ] = 0 ;
    }
    else {
      arr [ i ] = 1 ;
    }
  }
  System . out . print ( endingIndex - maxLen + " " ) ;
  System . out . print ( "to" ) ;
  System . out . print ( endingIndex ) ;
  return maxLen ;
}
|||

MAXIMUM_DIFFERENCE_ZEROS_ONES_BINARY_STRING_SET_2_TIME

public static int findLength ( String string , int n ) {
  int currentSum = 0 ;
  int maxSum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    currentSum += ( 1 == string . charAt ( i ) ? - 1 : string . charAt ( i ) ) ;
    if ( currentSum < 0 ) currentSum = 0 ;
    maxSum = Math . max ( currentSum , maxSum ) ;
  }
  return maxSum == 0 ? 0 : maxSum ;
}
|||

MAXIMUM_CONSECUTIVE_NUMBERS_PRESENT_ARRAY

public static int findLongestConseqSubseq ( int [ ] arr , int n ) {
  Set < Integer > S = new HashSet < Integer > ( ) ;
  ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) S . add ( arr [ i ] ) ;
  int ans = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( S . contains ( arr [ i ] ) ) {
      int j = arr [ i ] ;
      while ( ( S . contains ( j ) ) && ( j != arr [ i ] ) ) j ++ ;
      ans = Math . max ( ans , j - arr [ i ] ) ;
    }
  }
  return ans ;
}
|||

LEXICOGRAPHICALLY_NEXT_STRING

public static String nextWord ( String s ) {
  if ( ( s . equals ( " " ) ) || ( s . equals ( "a" ) ) ) return "a" ;
  int i = s . length ( ) - 1 ;
  while ( ( s . charAt ( i ) == 'z' ) && i >= 0 ) -- i ;
  if ( ( i == - 1 ) || ( s . charAt ( i ) == 'a' ) ) s = s + 'a' ;
  else s = s . replace ( s . charAt ( i ) , ( char ) ( Character . digit ( s . charAt ( i ) , 16 ) + 1 ) , 1 ) ;
  return s ;
}
|||

SCHEDULE_JOBS_SERVER_GETS_EQUAL_LOAD

public static int solve ( int [ ] a , int [ ] b , int n ) {
  int s = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) s += a [ i ] + b [ i ] ;
  if ( n == 1 ) return a [ 0 ] + b [ 0 ] ;
  if ( s % n != 0 ) return - 1 ;
  int x = s / n ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( a [ i ] > x ) return - 1 ;
    if ( i > 0 ) {
      a [ i ] += b [ i - 1 ] ;
      b [ i - 1 ] = 0 ;
    }
    if ( a [ i ] == x ) continue ;
    int y = a [ i ] + b [ i ] ;
    if ( i + 1 < n ) y += b [ i + 1 ] ;
    if ( y == x ) {
      a [ i ] = y ;
      b [ i ] = 0 ;
      if ( i + 1 < n ) b [ i + 1 ] = 0 ;
      continue ;
    }
    if ( a [ i ] + b [ i ] == x ) {
      a [ i ] += b [ i ] ;
      b [ i ] = 0 ;
      continue ;
    }
    if ( i + 1 < n && a [ i ] + b [ i + 1 ] == x ) {
      a [ i ] += b [ i + 1 ] ;
      b [ i + 1 ] = 0 ;
      continue ;
    }
    return - 1 ;
  }
  for ( int i = 0 ;
  i <= n ;
  i ++ ) if ( b [ i ] != 0 ) return - 1 ;
  return x ;
}
|||

FORM_MINIMUM_NUMBER_FROM_GIVEN_SEQUENCE_1

public static String getMinNumberForPattern ( String seq ) {
  int n = seq . length ( ) ;
  if ( ( n >= 9 ) && ( seq . charAt ( n ) == 'I' ) ) {
    return "-1" ;
  }
  StringBuilder result = new StringBuilder ( n + 1 ) ;
  int count = 1 ;
  for ( int i = 0 ;
  i < n + 1 ;
  i ++ ) {
    if ( ( i == n || seq . charAt ( i ) == 'I' ) && ( i + 1 < n ) ) {
      for ( int j = i - 1 ;
      j >= 0 && seq . charAt ( j ) == 'I' ;
      j -- ) {
        result . append ( Integer . parseInt ( "0" + Integer . toString ( count ) , 16 ) ) ;
        count ++ ;
        if ( ( j >= 0 && seq . charAt ( j ) == 'I' ) && ( j + 1 < n ) ) {
          break ;
        }
      }
    }
  }
  return result . toString ( ) ;
}
|||

SHUFFLE_2N_INTEGERS_FORMAT_A1_B1_A2_B2_A3_B3_BN_WITHOUT_USING_EXTRA_SPACE

public static void shuffleArray ( int [ ] a , int n ) {
  int i = 0 , q = 1 , k = n ;
  while ( ( i < n ) && ( j > i + q ) ) {
    a [ j - 1 ] = a [ j ] ;
    a [ j ] = a [ j - 1 ] ;
    j -- ;
  }
  i ++ ;
  k ++ ;
  q ++ ;
}
|||

FIND_REPETITIVE_ELEMENT_1_N_1_1

public static int findRepeating ( int [ ] arr , int n ) {
  Set < Integer > s = new HashSet < Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] == s . add ( arr [ i ] ) ) return arr [ i ] ;
    s . add ( arr [ i ] ) ;
  }
  return rteurn - 1 ;
}
|||

C_PROGRAM_SUBTRACTION_MATICES

public static void multiply ( int [ ] [ ] A , int [ ] [ ] B , int [ ] [ ] C ) {
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    for ( int j = 0 ;
    j < N ;
    j ++ ) {
      C [ i ] [ j ] = A [ i ] [ j ] - B [ i ] [ j ] ;
    }
  }
}
|||

FIRST_NEGATIVE_INTEGER_EVERY_WINDOW_SIZE_K

public static void printFirstNegativeInteger ( int [ ] arr , int n , int k ) {
  for ( int i = 0 ;
  i <= ( n - k + 1 ) ;
  i ++ ) {
    boolean flag = false ;
    for ( int j = 0 ;
    j <= k ;
    j ++ ) {
      if ( ( arr [ i + j ] < 0 ) && ( arr [ i + j ] > 0 ) ) {
        System . out . print ( arr [ i + j ] + " " ) ;
        flag = true ;
        break ;
      }
    }
    if ( ( ! ( flag ) ) && ( arr [ i + k ] > 0 ) ) {
      System . out . print ( "0" ) ;
    }
  }
}
|||

NUMBER_FULL_BINARY_TREES_NODE_PRODUCT_CHILDREN

public static int numoffbt ( int [ ] arr , int n ) {
  int maxvalue = - 2147483647 ;
  int minvalue = 2147483647 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    maxvalue = Math . max ( maxvalue , arr [ i ] ) ;
    minvalue = Math . min ( minvalue , arr [ i ] ) ;
  }
  int [ ] mark = new int [ maxvalue + 2 ] ;
  int [ ] value = new int [ maxvalue + 2 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    mark [ arr [ i ] ] = 1 ;
    value [ arr [ i ] ] = 1 ;
  }
  int ans = 0 ;
  for ( int i = minvalue ;
  i <= maxvalue ;
  i ++ ) {
    if ( ( mark [ i ] != 0 ) && ( mark [ i ] < 0 ) ) {
      int j = i + i ;
      while ( ( j <= maxvalue && j / i <= i ) || ( i != j / i ) ) {
        if ( ( mark [ j ] == 0 ) && ( mark [ i ] < 0 ) ) {
          continue ;
        }
        value [ j ] = value [ j ] + ( value [ i ] * value [ j / i ] ) ;
        if ( ( i != j / i ) && ( mark [ i ] < 0 ) ) {
          value [ j ] = value [ j ] + ( value [ i ] * value [ j / i ] ) ;
        }
        j += i ;
      }
    }
    ans += value [ i ] ;
  }
  return ans ;
}
|||

TRIANGULAR_MATCHSTICK_NUMBER

public static int numberOfSticks ( int x ) {
  return ( 3 * x * ( x + 1 ) ) / 2 ;
}
|||

K_MAXIMUM_SUM_COMBINATIONS_TWO_ARRAYS

public static void KMaxCombinations ( int [ ] A , int [ ] B , int N , int K ) {
  PriorityQueue < Integer > pq = new PriorityQueue < Integer > ( ) ;
  for ( int i = 0 ;
  i <= N ;
  i ++ ) {
    for ( int j = 0 ;
    j <= N ;
    j ++ ) {
      int a = A [ i ] + B [ j ] ;
      pq . add ( new Integer ( - a ) ) ;
    }
  }
  int count = 0 ;
  while ( ( count < K ) && ( pq . size ( ) > 0 ) ) {
    System . out . println ( pq . poll ( ) . intValue ( ) ) ;
    count = count + 1 ;
  }
}
|||

CONSTRUCT_ARRAY_PAIR_SUM_ARRAY

public static void constructArr ( int [ ] arr , int [ ] pair , int n ) {
  arr [ 0 ] = ( pair [ 0 ] + pair [ 1 ] - pair [ n - 1 ] ) / 2 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    arr [ i ] = pair [ i - 1 ] - arr [ 0 ] ;
  }
}
|||

CHECK_HALF_STRING_CHARACTER_FREQUENCY_CHARACTER

public static boolean checkCorrectOrNot ( String s ) {
  MAX_CHAR = s . length ( ) ;
  int [ ] count1 = new int [ MAX_CHAR ] ;
  int [ ] count2 = new int [ MAX_CHAR ] ;
  int n = s . length ( ) ;
  if ( n == 1 ) return true ;
  int i = 0 ;
  int j = n - 1 ;
  while ( ( i < j ) && ( count1 [ ( char ) s . charAt ( i ) - 'a' ] != 0 ) ) {
    count1 [ ( char ) s . charAt ( j ) - 'a' ] ++ ;
    count2 [ ( char ) s . charAt ( j ) - 'a' ] ++ ;
    i ++ ;
    j -- ;
  }
  for ( i = 0 ;
  i < MAX_CHAR ;
  i ++ ) {
    if ( count1 [ i ] != count2 [ i ] ) return false ;
  }
  return true ;
}
|||

MINIMIZE_THE_MAXIMUM_DIFFERENCE_BETWEEN_THE_HEIGHTS

public static int getMinDiff ( int [ ] arr , int n , int k ) {
  if ( ( n == 1 ) || ( n == 2 ) ) return 0 ;
  Arrays . sort ( arr ) ;
  int ans = arr [ n - 1 ] - arr [ 0 ] ;
  int small = arr [ 0 ] + k ;
  int big = arr [ n - 1 ] - k ;
  if ( ( small > big ) && ( small < big ) ) small = big ;
  for ( int i = 1 ;
  i < n - 1 ;
  i ++ ) {
    int subtract = arr [ i ] - k ;
    int add = arr [ i ] + k ;
    if ( ( subtract >= small || add <= big ) && ( big - subtract <= add - small ) ) continue ;
    if ( ( big - subtract <= add - small ) && ( big - add <= small ) ) small = subtract ;
    else big = add ;
  }
  return Math . min ( ans , big - small ) ;
}
|||

MINIMUM_POSSIBLE_VALUE_AI_AJ_K_GIVEN_ARRAY_K

public static void pairs ( int [ ] arr , int n , int k ) {
  int smallest = 999999999999 ;
  int count = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      if ( Math . abs ( arr [ i ] + arr [ j ] - k ) < smallest ) {
        smallest = Math . abs ( arr [ i ] + arr [ j ] - k ) ;
        count = 1 ;
      }
      else if ( Math . abs ( arr [ i ] + arr [ j ] - k ) == smallest ) {
        count ++ ;
      }
    }
  }
  System . out . println ( "Minimal Value = " + smallest ) ;
  System . out . println ( "Total Pairs = " + count ) ;
}
|||

SIZE_SUBARRAY_MAXIMUM_SUM

public static int maxSubArraySum ( int [ ] a , int size ) {
  int maxSo_far = - Integer . MAX_VALUE - 1 ;
  int maxEndingHere = 0 ;
  int start = 0 ;
  int end = 0 ;
  int s = 0 ;
  for ( int i = 0 ;
  i <= size ;
  i ++ ) {
    maxEndingHere += a [ i ] ;
    if ( maxSo_far < maxEndingHere ) {
      maxSo_far = maxEndingHere ;
      start = s ;
      end = i ;
    }
    if ( maxEndingHere < 0 ) {
      maxEndingHere = 0 ;
      s = i + 1 ;
    }
  }
  return ( end - start + 1 ) ;
}
|||

MINIMUM_NUMBER_OF_SQUARES_WHOSE_SUM_EQUALS_TO_GIVEN_NUMBER_N_1

public static int getMinSquares ( int n ) {
  int [ ] dp = {
    0 , 1 , 2 , 3 };
    for ( int i = 4 ;
    i <= n ;
    i ++ ) {
      dp [ i ] = i ;
      for ( int x = 1 ;
      x <= ( int ) Math . ceil ( Math . sqrt ( i ) ) ;
      x ++ ) {
        int temp = x * x ;
        ;
        if ( temp > i ) break ;
        else dp [ i ] = Math . min ( dp [ i ] , 1 + dp [ i - temp ] ) ;
      }
    }
    return dp [ n ] ;
  }
  
|||

DIVISIBILITY_BY_7

public static boolean isDivisibleBy7 ( int num ) {
  if ( num < 0 ) {
    return isDivisibleBy7 ( - num ) ;
  }
  if ( ( num == 0 || num == 7 ) && ( num % 10 == 0 ) ) {
    return true ;
  }
  if ( ( num < 10 ) || ( num % 10 == 0 ) ) {
    return false ;
  }
  return isDivisibleBy7 ( num / 10 - 2 * ( num - num / 10 * 10 ) ) ;
}
|||

POSITION_OF_RIGHTMOST_SET_BIT_2

public static int Right_most_setbit ( int num ) {
  int pos = 1 ;
  for ( int i = 0 ;
  i < INT_SIZE ;
  i ++ ) {
    if ( ! ( num & ( 1 << i ) ) ) {
      pos ++ ;
    }
    else {
      break ;
    }
  }
  return pos ;
}
|||

EFFICIENT_WAY_TO_MULTIPLY_WITH_7

public static int multiplyBySeven ( int n ) {
  return ( ( n << 3 ) - n ) ;
}
|||

NEXT_HIGHER_NUMBER_WITH_SAME_NUMBER_OF_SET_BITS

public static int snoob ( int x ) {
  int next = 0 ;
  if ( ( x > 0 ) && ( x < ( x + 1 ) ) ) {
    int rightOne = x & - ( x ) ;
    int nextHigherOneBit = x + Integer . MIN_VALUE ;
    int rightOnesPattern = x ^ Integer . MIN_VALUE ;
    rightOnesPattern = ( Integer . bitCount ( rightOnesPattern ) / Integer . MIN_VALUE ) ;
    rightOnesPattern = Integer . bitCount ( rightOnesPattern ) >> 2 ;
    next = nextHigherOneBit | rightOnesPattern ;
  }
  return next ;
}
|||

CHANGE_ARRAY_PERMUTATION_NUMBERS_1_N

public static void makePermutation ( int [ ] a , int n ) {
  Map < Integer , Integer > count = Maps . newHashMap ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( count . containsKey ( a [ i ] ) ) {
      count . put ( a [ i ] , 1 ) ;
    }
    else {
      count . put ( a [ i ] , 1 ) ;
      ;
    }
  }
  int nextMissing = 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( count . get ( a [ i ] ) != 1 || a [ i ] > n || a [ i ] < 1 ) {
      count . put ( a [ i ] , 1 ) ;
      while ( count . containsKey ( nextMissing ) ) {
        nextMissing ++ ;
      }
      a [ i ] = nextMissing ;
      count . put ( nextMissing , 1 ) ;
    }
  }
}
|||

MAXIMUM_AREA_QUADRILATERAL

public static double maxArea ( double a , double b , double c , double d ) {
  double semiperimeter = ( a + b + c + d ) / 2 ;
  return Math . sqrt ( ( semiperimeter - a ) * ( semiperimeter - b ) * ( semiperimeter - c ) * ( semiperimeter - d ) ) ;
}
|||

REPLACE_OCCURRENCES_STRING_AB_C_WITHOUT_USING_EXTRA_SPACE_1

public static void translate ( String st ) {
  int l = st . length ( ) ;
  if ( ( l < 2 ) || ( l > 3 ) ) return ;
  int i = 0 ;
  int j = 0 ;
  while ( ( j < l - 1 ) && ( st . charAt ( j ) == 'A' ) ) {
    if ( ( st . charAt ( j ) == 'B' ) && ( st . charAt ( j + 1 ) == 'C' ) ) {
      j += 2 ;
      st . charAt ( i ) = 'C' ;
      i ++ ;
      continue ;
    }
    st . charAt ( i ) = st . charAt ( j ) ;
    i ++ ;
    j ++ ;
  }
  if ( ( j == l - 1 ) && ( st . charAt ( i ) == 'A' ) ) {
    st . charAt ( i ) = st . charAt ( j ) ;
    i ++ ;
  }
  st . charAt ( i ) = ' ' ;
  st . charAt ( l - 1 ) = ' ' ;
}
|||

FIND_POWER_POWER_MOD_PRIME

public static int calculate ( int A , int B , int C , int M ) {
  int res = pow ( B , C , M - 1 ) ;
  int ans = pow ( A , res , M ) ;
  return ans ;
}
|||

CHECK_EXIST_TWO_ELEMENTS_ARRAY_WHOSE_SUM_EQUAL_SUM_REST_ARRAY

public static boolean checkPair ( int [ ] arr , int n ) {
  Set < Integer > s = new HashSet < Integer > ( ) ;
  int sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    sum += arr [ i ] ;
  }
  if ( sum % 2 != 0 ) {
    return false ;
  }
  sum = sum / 2 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int val = sum - arr [ i ] ;
    if ( arr [ i ] != 0 ) {
      s . add ( arr [ i ] ) ;
    }
    if ( val < s . size ( ) ) {
      System . out . println ( "Pair elements are" + arr [ i ] + " and" + Integer . toString ( val ) ) ;
    }
  }
  return true ;
}
|||

PROGRAM_FOR_SURFACE_AREA_OF_OCTAHEDRON

public static double surfaceAreaOCTAhedron ( double side ) {
  return ( 2 * ( Math . sqrt ( 3 ) ) ) * ( side * side ) ;
}
|||

FIND_A_SPECIFIC_PAIR_IN_MATRIX

public static int findMaxValue ( int [ ] [ ] mat ) {
  int maxValue = 0 ;
  for ( int a = 0 ;
  a < N - 1 ;
  a ++ ) {
    for ( int b = 0 ;
    b < N - 1 ;
    b ++ ) {
      for ( int d = a + 1 ;
      d < N ;
      d ++ ) {
        for ( int e = b + 1 ;
        e < N ;
        e ++ ) {
          if ( maxValue < Integer . MAX_VALUE ) {
            maxValue = Integer . MAX_VALUE ;
          };
        }
      }
    }
  }
  return maxValue ;
  ;
}
|||

MULTIPLY_TWO_NUMBERS_WITHOUT_USING_MULTIPLY_DIVISION_BITWISE_OPERATORS_AND_NO_LOOPS

public static int multiply ( int x , int y ) {
  if ( ( y == 0 ) || ( y > 0 ) ) return 0 ;
  if ( ( y < 0 ) || ( y > 1 ) ) return ( x + multiply ( x , y - 1 ) ) ;
  if ( ( y < 0 ) || ( y > 1 ) ) return - multiply ( x , - y ) ;
  return 0 ;
}
|||

FIND_TRIPLETS_ARRAY_WHOSE_SUM_EQUAL_ZERO_1

public static void findTriplets ( int [ ] arr , int n ) {
  boolean found = false ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    Set < Integer > s = new HashSet < Integer > ( ) ;
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      int x = - ( arr [ i ] + arr [ j ] ) ;
      if ( x < s . size ( ) ) {
        System . out . println ( x + " " + arr [ i ] + " " + arr [ j ] ) ;
        found = true ;
      }
      else {
        s . add ( arr [ j ] ) ;
      }
    }
  }
  if ( found == false ) {
    System . out . println ( "No Triplet Found" ) ;
  }
}
|||

FIND_MAXIMUM_VALUE_OF_SUM_IARRI_WITH_ONLY_ROTATIONS_ON_GIVEN_ARRAY_ALLOWED

public static int maxSum ( int [ ] arr ) {
  int arrSum = 0 ;
  int currVal = 0 ;
  int n = arr . length ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    arrSum = arrSum + arr [ i ] ;
    currVal = currVal + ( i * arr [ i ] ) ;
  }
  int maxVal = currVal ;
  for ( int j = 1 ;
  j <= n ;
  j ++ ) {
    currVal = currVal + arrSum - n * arr [ n - j ] ;
    if ( currVal > maxVal ) {
      maxVal = currVal ;
    }
  }
  return maxVal ;
}
|||

PROGRAM_FOR_SCALAR_MULTIPLICATION_OF_A_MATRIX

public static void scalarProductMat ( double [ ] [ ] mat , double k ) {
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    for ( int j = 0 ;
    j < N ;
    j ++ ) {
      mat [ i ] [ j ] = mat [ i ] [ j ] * k ;
    }
  }
}
|||

PRINT_SQUARES_FIRST_N_NATURAL_NUMBERS_WITHOUT_USING_1

public static void printSquares ( int n ) {
  int square = 0 ;
  int odd = 1 ;
  for ( int x = 0 ;
  x <= n ;
  x ++ ) {
    System . out . print ( square + " " ) ;
    square = square + odd ;
    odd = odd + 2 ;
  }
}
|||

NTH_PENTAGONAL_NUMBER

public static int pentagonalNum ( int n ) {
  return ( 3 * n * n - n ) / 2 ;
}
|||

COUNT_ARRAYS_ADJACENT_ELEMENTS_ONE_DIVIDE_ANOTHER

public static int numofArray ( int n , int m ) {
  int [ ] [ ] dp = new int [ MAX ] [ MAX ] ;
  for ( int j = 0 ;
  j < MAX ;
  j ++ ) {
    dp [ j ] = new int [ MAX ] ;
  }
  int [ ] di = new int [ MAX ] ;
  int [ ] mu = new int [ MAX ] ;
  for ( int i = 1 ;
  i <= m ;
  i ++ ) {
    for ( int j = 2 * i ;
    j <= m ;
    j += i ) {
      di [ j ] . add ( i ) ;
      mu [ i ] . add ( j ) ;
    }
    di [ i ] . add ( i ) ;
  }
  for ( int i = 1 ;
  i <= m ;
  i ++ ) {
    dp [ 1 ] [ i ] = 1 ;
  }
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    for ( int j = 1 ;
    j <= m ;
    j ++ ) {
      dp [ i ] [ j ] = 0 ;
      for ( int x : di [ j ] ) {
        dp [ i ] [ j ] += dp [ i - 1 ] [ x ] ;
      }
      for ( int x : mu [ j ] ) {
        dp [ i ] [ j ] += dp [ i - 1 ] [ x ] ;
      }
    }
  }
  int ans = 0 ;
  for ( int i = 1 ;
  i <= m ;
  i ++ ) {
    ans += dp [ n ] [ i ] ;
    di [ i ] . clear ( ) ;
    mu [ i ] . clear ( ) ;
  }
  return ans ;
}
|||

0_1_KNAPSACK_PROBLEM_DP_10

public static int knapSack ( int W , double [ ] wt , double [ ] val , int n ) {
  if ( n == 0 || W == 0 ) return 0 ;
  if ( ( wt [ n - 1 ] > W ) && ( wt [ n - 1 ] > 0 ) ) return knapSack ( W , wt , val , n - 1 ) ;
  else return Math . max ( val [ n - 1 ] + knapSack ( W - wt [ n - 1 ] , wt , val , n - 1 ) , knapSack ( W , wt , val , n - 1 ) ) ;
}
|||

FIND_TRIPLETS_ARRAY_WHOSE_SUM_EQUAL_ZERO

public static void findTriplets ( int [ ] arr , int n ) {
  boolean found = true ;
  for ( int i = 0 ;
  i <= n - 2 ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= n - 1 ;
    j ++ ) {
      for ( int k = j + 1 ;
      k <= n ;
      k ++ ) {
        if ( ( arr [ i ] + arr [ j ] + arr [ k ] == 0 ) && ( arr [ i ] + arr [ j ] + arr [ k ] == 0 ) ) {
          System . out . println ( arr [ i ] + " " + arr [ j ] + " " + arr [ k ] ) ;
          found = true ;
        }
      }
    }
  }
  if ( ( found == false ) && ( arr [ 0 ] == 0 ) && ( arr [ 1 ] == 0 ) && ( arr [ 2 ] == 0 ) && ( arr [ 3 ] == 0 ) ) {
    System . out . println ( " not exist " ) ;
  }
}
|||

COUNT_NUMBER_WAYS_REACH_GIVEN_SCORE_GAME

public static int count ( int n ) {
  int [ ] table = new int [ n + 1 ] ;
  table [ 0 ] = 1 ;
  for ( int i = 3 ;
  i <= n ;
  i ++ ) table [ i ] += table [ i - 3 ] ;
  for ( int i = 5 ;
  i <= n ;
  i ++ ) table [ i ] += table [ i - 5 ] ;
  for ( int i = 10 ;
  i <= n ;
  i ++ ) table [ i ] += table [ i - 10 ] ;
  return table [ n ] ;
}
|||

MAXIMUM_SUM_ABSOLUTE_DIFFERENCE_ARRAY

public static void MaxSumDifference ( int [ ] a , int n ) {
  Arrays . sort ( a ) ;
  ;
  int j = 0 ;
  int [ ] finalSequence = new int [ n ] ;
  for ( int x = 0 ;
  x < n ;
  x ++ ) {
    finalSequence [ j ] = a [ i ] ;
    finalSequence [ j + 1 ] = a [ n - i - 1 ] ;
    j = j + 2 ;
  }
  int MaximumSum = 0 ;
  for ( int i = 0 ;
  i <= n - 1 ;
  i ++ ) {
    MaximumSum = ( MaximumSum + Math . abs ( finalSequence [ i ] - finalSequence [ i + 1 ] ) ) ;
  }
  MaximumSum = ( MaximumSum + Math . abs ( finalSequence [ n - 1 ] - finalSequence [ 0 ] ) ) ;
  ;
  System . out . println ( MaximumSum ) ;
}
|||

PROGRAM_FIND_MID_POINT_LINE

public static void midpoint ( int x1 , int x2 , int y1 , int y2 ) {
  System . out . print ( ( x1 + x2 ) / 2 + " , " + ( y1 + y2 ) / 2 ) ;
}
|||

ALTERNATIVE_SORTING

public static void alternateSort ( int [ ] arr , int n ) {
  Arrays . sort ( arr ) ;
  int i = 0 ;
  int j = n - 1 ;
  while ( ( i < j ) && ( i < n ) ) {
    System . out . print ( arr [ j ] + " " ) ;
    j -- ;
    System . out . print ( arr [ i ] + " " ) ;
    i ++ ;
  }
  if ( ( n % 2 != 0 ) && ( n % 2 != 1 ) ) System . out . print ( arr [ i ] ) ;
}
|||

NUMBER_SUBARRAYS_SUM_EXACTLY_EQUAL_K

public static int findSubarraySum ( int [ ] arr , int n , int Sum ) {
  TreeMap < Integer , Integer > prevSum = new TreeMap < Integer , Integer > ( ) ;
  int res = 0 ;
  int currsum = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    currsum += arr [ i ] ;
    if ( currsum == Sum ) res ++ ;
    if ( ( currsum - Sum ) < prevSum . size ( ) ) res += prevSum . get ( currsum - Sum ) ;
    prevSum . put ( currsum , currsum ) ;
  }
  return res ;
}
|||

FIND_THE_ELEMENT_THAT_APPEARS_ONCE_IN_A_SORTED_ARRAY

public static int search ( int [ ] arr , int low , int high ) {
  if ( low > high ) return 0 ;
  if ( low == high ) return arr [ low ] ;
  int mid = low + ( high - low ) / 2 ;
  if ( mid % 2 == 0 ) {
    if ( arr [ mid ] == arr [ mid + 1 ] ) return search ( arr , mid + 2 , high ) ;
    else return search ( arr , low , mid ) ;
  }
  else {
    if ( arr [ mid ] == arr [ mid - 1 ] ) return search ( arr , mid + 1 , high ) ;
    else return search ( arr , low , mid - 1 ) ;
  }
}
|||

FORM_SMALLEST_NUMBER_USING_ONE_SWAP_OPERATION

public static String smallestNumber ( String num ) {
  num = Arrays . asList ( num ) ;
  int n = num . length ( ) ;
  int [ ] rightMin = new int [ n ] ;
  int right ;
  rightMin [ n - 1 ] = - 1 ;
  ;
  right = n - 1 ;
  for ( int i = n - 2 ;
  i > 0 ;
  i -- ) {
    if ( num . charAt ( i ) > num . charAt ( right ) ) {
      rightMin [ i ] = right ;
    }
    else {
      rightMin [ i ] = - 1 ;
      right = i ;
    }
  }
  int small = - 1 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( num . charAt ( i ) != '0' ) {
      if ( small == - 1 ) {
        if ( num . charAt ( i ) < num . charAt ( 0 ) ) {
          small = i ;
        }
      }
      else if ( num . charAt ( i ) < num . charAt ( small ) ) {
        small = i ;
      }
    }
  }
  if ( small != - 1 ) {
    num = num . substring ( 0 , small ) ;
  }
  else {
    for ( int i = 1 ;
    i < n ;
    i ++ ) {
      if ( rightMin [ i ] != - 1 ) {
        num = num . substring ( rightMin [ i ] ) ;
        break ;
      }
    }
  }
  return new String ( num ) ;
}
|||

PROGRAM_AREA_SQUARE

public static int areaSquare ( int side ) {
  int area = side * side ;
  return area ;
}
|||

FIND_DAY_OF_THE_WEEK_FOR_A_GIVEN_DATE

public static int dayofweek ( int d , int m , int y ) {
  int [ ] t = {
    0 , 3 , 2 , 5 , 0 , 3 , 5 , 1 , 4 , 6 , 2 , 4 };
    y -= m < 3 ? 1 : 0 ;
    return ( ( y + Integer . MIN_VALUE / 4 ) - Integer . MIN_VALUE / 100 + Integer . MIN_VALUE / 400 + t [ m - 1 ] + d ) % 7 ;
  }
  
|||

CHECK_QUEUE_CAN_SORTED_ANOTHER_QUEUE_USING_STACK

public static boolean checkSorted ( int n , Queue q ) {
  Stack < Integer > st = new Stack < Integer > ( ) ;
  int expected = 1 ;
  Integer fnt ;
  while ( ( ! q . isEmpty ( ) ) && ( ! q . peek ( ) . equals ( fnt ) ) ) {
    fnt = q . getQueue ( ) . peek ( ) ;
    q . poll ( ) ;
    if ( ( fnt == expected ) && ( st . size ( ) == 0 ) ) {
      expected ++ ;
    }
    else {
      if ( ( st . size ( ) == 0 ) || ( st . size ( ) != 0 && st . peek ( ) . compareTo ( fnt ) < 0 ) ) {
        return false ;
      }
      else {
        st . push ( fnt ) ;
      }
    }
    while ( ( st . size ( ) != 0 ) && ( st . peek ( ) . compareTo ( expected ) == 0 ) ) {
      st . pop ( ) ;
      expected ++ ;
    }
  }
  if ( ( expected - 1 == n && st . size ( ) == 0 ) || ( expected - 1 == n && st . size ( ) == 0 ) ) {
    return true ;
  }
  return false ;
}
|||

SORT_ARRAY_CONTAIN_1_N_VALUES

public static void sortit ( int [ ] arr , int n ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    arr [ i ] = i + 1 ;
  }
}
|||

LCS_LONGEST_COMMON_SUBSEQUENCE_THREE_STRINGS_1

public static int lcsOf3 ( int i , int j , int k ) {
  if ( ( i == - 1 || j == - 1 || k == - 1 ) && ( dp [ i ] [ j ] [ k ] != - 1 ) ) return 0 ;
  if ( ( X [ i ] == Y [ j ] && Y [ j ] == Z [ k ] ) || ( X [ i ] == Z [ j ] && X [ j ] == Y [ k ] && Z [ k ] == X [ k ] ) ) {
    dp [ i ] [ j ] [ k ] = 1 + lcsOf3 ( i - 1 , j - 1 , k - 1 ) ;
    return dp [ i ] [ j ] [ k ] ;
  }
  else {
    dp [ i ] [ j ] [ k ] = Math . max ( Math . max ( lcsOf3 ( i - 1 , j , k ) , lcsOf3 ( i , j - 1 , k ) ) , lcsOf3 ( i , j , k - 1 ) ) ;
    return dp [ i ] [ j ] [ k ] ;
  }
}
|||

LOWER_INSERTION_POINT

public static int LowerInsertionPoint ( int [ ] arr , int n , int X ) {
  if ( ( X < arr [ 0 ] ) && ( X > arr [ n - 1 ] ) ) return 0 ;
  ;
  else if ( ( X > arr [ n - 1 ] ) && ( X < arr [ n ] ) ) return n ;
  int lowerPnt = 0 ;
  int i = 1 ;
  while ( ( i < n ) && ( arr [ i ] < X ) ) {
    lowerPnt = i ;
    i = i * 2 ;
  }
  while ( ( lowerPnt < n ) && ( arr [ lowerPnt ] < X ) ) {
    lowerPnt ++ ;
  }
  return lowerPnt ;
}
|||

CONSTRUCT_LEXICOGRAPHICALLY_SMALLEST_PALINDROME

public static String constructPalin ( String string , int l ) {
  string = Arrays . asList ( string ) ;
  int i = - 1 ;
  int j = l ;
  while ( i < j ) {
    i ++ ;
    j -- ;
    if ( ( string . charAt ( i ) == string . charAt ( j ) && string . charAt ( i ) != '*' ) || ( string . charAt ( i ) == string . charAt ( j ) && string . charAt ( i ) == '*' ) ) {
      continue ;
    }
    else if ( ( string . charAt ( i ) == string . charAt ( j ) && string . charAt ( i ) == '*' ) || ( string . charAt ( i ) == '*' ) ) {
      string . charAt ( i ) = 'a' ;
      string . charAt ( j ) = 'a' ;
      continue ;
    }
    else if ( string . charAt ( i ) == '*' ) {
      string . charAt ( i ) = string . charAt ( j ) ;
      continue ;
    }
    else if ( string . charAt ( j ) == '*' ) {
      string . charAt ( j ) = string . charAt ( i ) ;
      continue ;
    }
    System . out . println ( "Not Possible" ) ;
    return "" ;
  }
  return string ;
}
|||

SECTION_FORMULA_POINT_DIVIDES_LINE_GIVEN_RATIO

public static void section ( double x1 , double x2 , double y1 , double y2 , double m , double n ) {
  double x = ( ( double ) ( ( n * x1 ) + ( m * x2 ) ) / ( m + n ) ) ;
  double y = ( ( double ) ( ( n * y1 ) + ( m * y2 ) ) / ( m + n ) ) ;
  System . out . println ( x + " " + y ) ;
}
|||

SQUARE_ROOT_NUMBER_USING_LOG

public static double squareRoot ( double n ) {
  return Math . pow ( 2 , 0.5 * Math . log2 ( n ) ) ;
}
|||

MAXIMIZE_SUM_ARRII

public static int maxSum ( int [ ] arr , int n ) {
  Arrays . sort ( arr ) ;
  int sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    sum += arr [ i ] * i ;
  }
  return sum ;
}
|||

STRING_K_DISTINCT_CHARACTERS_NO_CHARACTERS_ADJACENT

public static String findString ( int n , int k ) {
  String res = "" ;
  for ( int i = 0 ;
  i < k ;
  i ++ ) {
    res = res + ( char ) ( 'a' + i ) ;
  }
  int count = 0 ;
  for ( int i = 0 ;
  i < n - k ;
  i ++ ) {
    res = res + ( char ) ( 'a' + count ) ;
    count ++ ;
    if ( ( count == k ) && ( i == n - k ) ) {
      count = 0 ;
    };
  }
  return res ;
}
|||

COUNT_WORDS_WHOSE_TH_LETTER_EITHER_1_TH_TH_I1_TH_LETTER_GIVEN_WORD

public static int countWords ( String str , int l ) {
  int count = 1 ;
  ;
  if ( ( l == 1 ) || ( l == 2 ) ) return count ;
  if ( ( str . charAt ( 0 ) == str . charAt ( 1 ) ) && ( str . charAt ( 0 ) == str . charAt ( 1 ) ) ) count *= 1 ;
  else count *= 2 ;
  for ( int j = 1 ;
  j <= l - 1 ;
  j ++ ) {
    if ( ( str . charAt ( j ) == str . charAt ( j - 1 ) && str . charAt ( j ) == str . charAt ( j + 1 ) ) || ( str . charAt ( j ) == str . charAt ( j - 1 ) || str . charAt ( j ) == str . charAt ( j + 1 ) || str . charAt ( j - 1 ) == str . charAt ( j + 1 ) ) ) count *= 1 ;
    else if ( ( str . charAt ( j ) == str . charAt ( j - 1 ) || str . charAt ( j ) == str . charAt ( j + 1 ) || str . charAt ( j - 1 ) == str . charAt ( j + 1 ) ) && ( str . charAt ( j ) == str . charAt ( j + 1 ) ) ) count *= 2 ;
    else count *= 3 ;
  }
  if ( ( str . charAt ( l - 1 ) == str . charAt ( l - 2 ) ) && ( str . charAt ( l - 1 ) == str . charAt ( l - 2 ) ) ) count *= 1 ;
  else count *= 2 ;
  return count ;
}
|||

NUMBER_JUMP_REQUIRED_GIVEN_LENGTH_REACH_POINT_FORM_D_0_ORIGIN_2D_PLANE

public static int minJumps ( int a , int b , int d ) {
  int temp = a ;
  a = Math . min ( a , b ) ;
  b = Math . max ( temp , b ) ;
  if ( ( d >= b ) && ( d < a ) ) {
    return ( d + b - 1 ) / b ;
  }
  if ( ( d == 0 ) && ( d < a ) ) {
    return 0 ;
  }
  if ( ( d == a ) && ( d < b ) ) {
    return 1 ;
  }
  return 2 ;
}
|||

SUM_FACTORS_NUMBER_1

public static long sumofFactors ( long n ) {
  long res = 1 ;
  for ( int i = 2 ;
  i <= ( int ) ( m . sqrt ( n ) + 1 ) ;
  i ++ ) {
    long currSum = 1 ;
    long currTerm = 1 ;
    while ( n % i == 0 ) {
      n = n / i ;
      ;
      currTerm = currTerm * i ;
      ;
      currSum += currTerm ;
      ;
    }
    res = res * currSum ;
  }
  if ( n > 2 ) {
    res = res * ( 1 + n ) ;
  }
  return res ;
}
|||

DELETE_CONSECUTIVE_WORDS_SEQUENCE

public static int removeConsecutiveSame ( int [ ] v ) {
  int n = v . length ;
  int i = 0 ;
  while ( ( i < n - 1 ) && ( ( i + 1 ) < v . length ) ) {
    if ( ( ( i + 1 ) < v . length ) && ( v [ i ] == v [ i + 1 ] ) ) {
      v [ i ] = v [ i ] ;
      v [ i + 1 ] = v [ i ] ;
      if ( ( i > 0 ) && ( i < n - 2 ) ) i -- ;
      n = n - 2 ;
    }
    else i ++ ;
  }
  return v . length - i - 1 ;
}
|||

COUNT_NUMBER_BINARY_STRINGS_WITHOUT_CONSECUTIVE_1S

public static int countStrings ( int n ) {
  int [ ] a = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    a [ i ] = 0 ;
  }
  int [ ] b = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    a [ i ] = a [ i - 1 ] + b [ i - 1 ] ;
    b [ i ] = a [ i - 1 ] ;
  }
  return a [ n - 1 ] + b [ n - 1 ] ;
}
|||

FIND_THE_MISSING_NUMBER

public static int getMissingNo ( int [ ] A ) {
  int n = A . length ;
  int total = ( n + 1 ) * ( n + 2 ) / 2 ;
  int sumOfA = Arrays . stream ( A ) . mapToInt ( Integer :: sum ) . sum ( ) ;
  return total - sumOfA ;
}
|||

SQUARE_ROOT_OF_A_PERFECT_SQUARE

public static double squareRoot ( double n ) {
  double x = n ;
  double y = 1 ;
  double e = 0.000001 ;
  while ( ( x - y > e ) && ( x - y > e ) ) {
    x = ( x + y ) / 2 ;
    y = n / x ;
  }
  return x ;
}
|||

SUBSET_SUM_PROBLEM_OSUM_SPACE

public static boolean isSubsetSum ( int [ ] arr , int n , int sum ) {
  boolean [ ] [ ] subset = new boolean [ sum + 1 ] [ 3 ] ;
  for ( int i = 0 ;
  i < 3 ;
  i ++ ) {
    subset [ i ] = new boolean [ sum + 1 ] ;
    for ( int j = 0 ;
    j < sum + 1 ;
    j ++ ) {
      if ( ( j == 0 ) && ( arr [ i ] == 0 ) ) {
        subset [ i % 2 ] [ j ] = true ;
      }
      else if ( ( i == 0 ) && ( arr [ i ] == 0 ) ) {
        subset [ i % 2 ] [ j ] = subset [ ( i + 1 ) % 2 ] [ j - arr [ i - 1 ] ] || subset [ ( i + 1 ) % 2 ] [ j ] ;
      }
      else {
        subset [ i % 2 ] [ j ] = subset [ ( i + 1 ) % 2 ] [ j ] ;
      }
    }
  }
  return subset [ n % 2 ] [ sum ] ;
}
|||

MULTIPLICATIVE_INVERSE_UNDER_MODULO_M

static int modInverse ( int a , int m ) {
  a = a % m ;
  ;
  for ( int x = 1 ;
  x < m ;
  x ++ ) {
    if ( ( ( a * x ) % m == 1 ) && ( ( a * x ) % m == 0 ) ) {
      return x ;
    }
  }
  return 1 ;
}
|||

COMPUTE_AVERAGE_TWO_NUMBERS_WITHOUT_OVERFLOW

public static double computeAverage ( double a , double b ) {
  return Math . floor ( ( a + b ) / 2 ) ;
}
|||

REPRESENT_GIVEN_SET_POINTS_BEST_POSSIBLE_STRAIGHT_LINE

public static void bestApproximate ( double [ ] x , double [ ] y , int n ) {
  double sumX = 0 ;
  double sumY = 0 ;
  double sumXY = 0 ;
  double sumX2 = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    sumX += x [ i ] ;
    sumY += y [ i ] ;
    sumXY += x [ i ] * y [ i ] ;
    sumX2 += Math . pow ( x [ i ] , 2 ) ;
  }
  double m = ( double ) ( ( n * sumXY - sumX * sumY ) / ( n * sumX2 - Math . pow ( sumX , 2 ) ) ) ;
  ;
  double c = ( double ) ( sumY - m * sumX ) / n ;
  ;
  System . out . println ( "m = " + m ) ;
  ;
  System . out . println ( "c = " + c ) ;
  ;
}
|||

SPLIT_ARRAY_ADD_FIRST_PART_END

public static void splitArr ( int [ ] arr , int n , int k ) {
  for ( int i = 0 ;
  i <= k ;
  i ++ ) {
    int x = arr [ 0 ] ;
    for ( int j = 0 ;
    j <= n - 1 ;
    j ++ ) {
      arr [ j ] = arr [ j + 1 ] ;
    }
    arr [ n - 1 ] = x ;
  }
}
|||

MAXIMUM_POSSIBLE_DIFFERENCE_TWO_SUBSETS_ARRAY

public static int maxDiff ( int [ ] arr , int n ) {
  int SubsetSum_1 = 0 ;
  int SubsetSum_2 = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    boolean isSingleOccurance = true ;
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      if ( ( arr [ i ] == arr [ j ] ) && ( arr [ i ] > arr [ j ] ) ) {
        isSingleOccurance = false ;
        arr [ i ] = arr [ j ] = 0 ;
        break ;
      }
    }
    if ( ( isSingleOccurance == true ) && ( arr [ i ] > 0 ) ) {
      if ( ( arr [ i ] > 0 ) && ( arr [ j ] > 0 ) ) SubsetSum_1 += arr [ i ] ;
      else SubsetSum_2 += arr [ i ] ;
    }
  }
  return Math . abs ( SubsetSum_1 - SubsetSum_2 ) ;
}
|||

LONGEST_SUBSEQUENCE_DIFFERENCE_ADJACENTS_ONE_SET_2

public static int longLenSub ( int [ ] arr , int n ) {
  TreeMap < Integer , Integer > um = new TreeMap < Integer , Integer > ( ) ;
  int longLen = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int len1 = 0 ;
    if ( ( arr [ i - 1 ] < 0 ) && len1 < um . get ( arr [ i ] - 1 ) ) {
      len1 = um . get ( arr [ i ] - 1 ) ;
    }
    if ( ( arr [ i ] + 1 < 0 ) && len1 < um . get ( arr [ i ] + 1 ) ) {
      len1 = um . get ( arr [ i ] + 1 ) ;
    }
    um . put ( arr [ i ] , len1 + 1 ) ;
    if ( longLen < um . get ( arr [ i ] ) ) {
      longLen = um . get ( arr [ i ] ) ;
    }
  }
  return longLen ;
}
|||

LONGEST_REPEATED_SUBSEQUENCE_1

public static String longestRepeatedSubSeq ( String str ) {
  int n = str . length ( ) ;
  int [ ] [ ] dp = new int [ n + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    dp [ i ] [ i ] = new int [ n + 1 ] ;
  }
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int j = 1 ;
    j <= n ;
    j ++ ) {
      if ( ( str . charAt ( i - 1 ) == str . charAt ( j - 1 ) && i != j ) || ( str . charAt ( i ) == str . charAt ( j - 1 ) && i != j ) ) {
        dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ] ;
      }
      else {
        dp [ i ] [ j ] = Math . max ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] ) ;
      }
    }
  }
  String res = "" ;
  int i = n ;
  int j = n ;
  while ( ( i > 0 ) && ( j > 0 ) ) {
    if ( ( dp [ i ] [ j ] == dp [ i - 1 ] [ j - 1 ] + 1 ) && ( str . charAt ( i - 1 ) == str . charAt ( j - 1 ) && i != j ) ) {
      res += str . charAt ( i - 1 ) ;
      i -- ;
      j -- ;
    }
    else if ( ( dp [ i ] [ j ] == dp [ i - 1 ] [ j ] ) && ( str . charAt ( i - 1 ) == str . charAt ( j - 1 ) && i != j ) ) {
      i -- ;
    }
    else {
      j -- ;
    }
  }
  res = new String ( reverse ( res ) ) ;
  return res ;
}
|||

FIND_INDEX_MAXIMUM_OCCURRING_ELEMENT_EQUAL_PROBABILITY

public static void findRandomIndexOfMax ( int [ ] arr , int n ) {
  Map < Integer , Integer > mp = Maps . newHashMap ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( arr [ i ] < mp . size ( ) ) && ( mp . get ( arr [ i ] ) > 0 ) ) {
      mp . put ( arr [ i ] , mp . get ( arr [ i ] ) + 1 ) ;
    }
    else {
      mp . put ( arr [ i ] , 1 ) ;
    }
  }
  int maxElement = - 323567 ;
  int maxSoFar = - 323567 ;
  for ( int p = 0 ;
  p < mp . size ( ) ;
  p ++ ) {
    if ( ( mp . get ( p ) > maxSoFar ) && ( mp . get ( p ) < maxSoFar ) ) {
      maxSoFar = mp . get ( p ) ;
      maxElement = p ;
    }
  }
  int r = ( int ) ( ( ( Math . random ( ) * 1 + maxSoFar ) % maxSoFar ) + 1 ) ;
  int i = 0 ;
  int count = 0 ;
  while ( ( i < n ) && ( arr [ i ] == maxElement ) ) {
    if ( ( arr [ i ] == maxElement ) && ( count == r ) ) {
      System . out . println ( "Element with maximum frequency present at index " + i ) ;
      break ;
    }
    i = i + 1 ;
  }
}
|||

CHECK_NUMBER_IS_PERFECT_SQUARE_USING_ADDITIONSUBTRACTION

public static boolean isPerfectSquare ( int n ) {
  int i = 1 ;
  int theSum = 0 ;
  while ( theSum < n ) {
    theSum += i ;
    if ( theSum == n ) return true ;
    i += 2 ;
  }
  return false ;
}
|||

N_BONACCI_NUMBERS_1

public static void bonacciSeries ( int n , int m ) {
  int [ ] a = new int [ m ] ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) a [ i ] = 0 ;
  a [ n - 1 ] = 1 ;
  a [ n ] = 1 ;
  for ( int i = n + 1 ;
  i < m ;
  i ++ ) a [ i ] = 2 * a [ i - 1 ] - a [ i - n - 1 ] ;
  for ( int i = 0 ;
  i <= m ;
  i ++ ) System . out . print ( a [ i ] + " " ) ;
}
|||

COUNT_INDEX_PAIRS_EQUAL_ELEMENTS_ARRAY_1

public static int countPairs ( int [ ] arr , int n ) {
  Map < Integer , Integer > mp = Maps . newHashMap ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] < mp . keySet ( ) . size ( ) ) {
      mp . put ( arr [ i ] , ++ i ) ;
    }
    else {
      mp . put ( arr [ i ] , 1 ) ;
    }
  }
  int ans = 0 ;
  for ( Integer it : mp . keySet ( ) ) {
    int count = mp . get ( it ) ;
    ans += ( count * ( count - 1 ) ) / 2 ;
  }
  return ans ;
}
|||

SORT_EVEN_PLACED_ELEMENTS_INCREASING_ODD_PLACED_DECREASING_ORDER

public static void bitonicGenerator ( int [ ] arr , int n ) {
  int [ ] evenArr = new int [ n ] ;
  int [ ] oddArr = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( ( i % 2 ) == 0 ) && ( ( i % 2 ) == 1 ) ) {
      evenArr [ i ] = arr [ i ] ;
    }
    else {
      oddArr [ i ] = arr [ i ] ;
    }
  }
  Arrays . sort ( evenArr ) ;
  Arrays . sort ( oddArr ) ;
  oddArr = oddArr [ 0 ] ;
  int i = 0 ;
  for ( int j = 0 ;
  j < evenArr . length ;
  j ++ ) {
    arr [ i ] = evenArr [ j ] ;
    i ++ ;
  }
  for ( int j = 0 ;
  j < oddArr . length ;
  j ++ ) {
    arr [ i ] = oddArr [ j ] ;
    i ++ ;
  }
}
|||

DYNAMIC_PROGRAMMING_SET_9_BINOMIAL_COEFFICIENT

public static double binomialCoeff ( int n , int k ) {
  if ( k == 0 || k == n ) return 1 ;
  return binomialCoeff ( n - 1 , k - 1 ) + binomialCoeff ( n - 1 , k ) ;
}
|||

WRITE_A_C_PROGRAM_TO_FIND_THE_PARITY_OF_AN_UNSIGNED_INTEGER

public static int getParity ( int n ) {
  int parity = 0 ;
  while ( n > 0 ) {
    parity = ~ parity ;
    n = n & ( n - 1 ) ;
  }
  return parity ;
}
|||

CHECK_WHETHER_LARGE_NUMBER_DIVISIBLE_7

public static boolean isDivisible7 ( String num ) {
  int n = num . length ( ) ;
  if ( ( n == 0 ) && num . charAt ( 0 ) == '\n' ) return 1 ;
  if ( ( n % 3 == 1 ) && ( num . charAt ( n / 3 ) == '\n' ) ) {
    num = String . valueOf ( num ) + "00" ;
    n += 2 ;
  }
  else if ( ( n % 3 == 2 ) && ( num . charAt ( n / 3 ) == '0' ) ) {
    num = String . valueOf ( num ) + "0" ;
    n += 1 ;
  }
  int GSum = 0 ;
  int p = 1 ;
  for ( int i = n - 1 ;
  i >= 0 ;
  i -- ) {
    int group = 0 ;
    group += ( num . charAt ( i ) - '0' ) ;
    i -- ;
    group += ( num . charAt ( i ) - '0' ) * 10 ;
    i -- ;
    group += ( num . charAt ( i ) - '0' ) * 100 ;
    GSum = GSum + group * p ;
    p *= ( - 1 ) ;
  }
  return ( GSum % 7 == 0 ) ;
}
|||

PRODUCT_NODES_K_TH_LEVEL_TREE_REPRESENTED_STRING

public static int productAtKthLevel ( String tree , int k ) {
  int level = - 1 ;
  int product = 1 ;
  int n = tree . length ( ) ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( tree . charAt ( i ) == '(' ) && ( tree . charAt ( i + 1 ) == ')' ) ) {
      level ++ ;
    }
    else if ( ( tree . charAt ( i ) == ')' ) && ( tree . charAt ( i + 1 ) == '(' ) ) {
      level -- ;
    }
    else {
      if ( ( level == k ) && ( tree . charAt ( i + 1 ) == '(' ) ) {
        product *= ( Integer . parseInt ( tree . substring ( i + 1 , i + 2 ) ) - Integer . parseInt ( "0" ) ) ;
      }
    }
  }
  return product ;
}
|||

CHECK_WHETHER_GIVEN_NUMBER_EVEN_ODD

public static boolean isEven ( int n ) {
  return ( n % 2 == 0 ) ;
}
|||

COUNT_GROUPINGS_NUMBER_SUM_DIGITS_EVERY_SUB_GROUP_LESS_EQUALS_IMMEDIATE_RIGHT_SUB_GROUP

public static int countGroups ( int position , int previousSum , int length , int [ ] num ) {
  if ( ( position == length ) && ( previousSum == 0 ) ) return 1 ;
  int res = 0 ;
  int sum = 0 ;
  for ( int i = position ;
  i < length ;
  i ++ ) {
    sum = sum + Integer . bitCount ( num [ i ] ) ;
    if ( ( sum >= previousSum ) && ( sum < previousSum ) ) res = res + countGroups ( i + 1 , sum , length , num ) ;
  }
  return res ;
}
|||

FIND_THE_ELEMENT_THAT_ODD_NUMBER_OF_TIMES_IN_OLOG_N_TIME

public static int search ( int [ ] arr , int low , int high ) {
  if ( low > high ) return 0 ;
  if ( low == high ) return arr [ low ] ;
  int mid = ( low + high ) / 2 ;
  ;
  if ( mid % 2 == 0 ) {
    if ( arr [ mid ] == arr [ mid + 1 ] ) return search ( arr , mid + 2 , high ) ;
    else return search ( arr , low , mid ) ;
  }
  else {
    if ( arr [ mid ] == arr [ mid - 1 ] ) return search ( arr , mid + 1 , high ) ;
    else return search ( arr , low , mid - 1 ) ;
  }
}
|||

DELETE_CONSECUTIVE_WORDS_SEQUENCE_1

public static int removeConsecutiveSame ( String v ) {
  Stack < String > st = new Stack < String > ( ) ;
  for ( int i = 0 ;
  i < v . length ( ) ;
  i ++ ) {
    if ( ( st . size ( ) == 0 ) && ( st . peek ( ) . equals ( v ) ) ) {
      st . push ( v . substring ( i ) ) ;
    }
    else {
      String Str = st . pop ( ) ;
      if ( ( Str . equals ( v ) ) && ( Str . length ( ) == 0 ) ) {
        st . push ( v . substring ( i ) ) ;
      }
      else {
        st . push ( v . substring ( i ) ) ;
      }
    }
  }
  return st . size ( ) ;
}
|||

MINIMUM_NUMBER_OF_JUMPS_TO_REACH_END_OF_A_GIVEN_ARRAY_2

public static int minJumps ( int [ ] arr , int n ) {
  int [ ] jumps = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    jumps [ i ] = 0 ;
  }
  for ( int i = n - 2 ;
  i >= 0 ;
  i -- ) {
    if ( ( arr [ i ] == 0 ) && ( arr [ i ] >= n - i - 1 ) ) {
      jumps [ i ] = Integer . MAX_VALUE ;
    }
    else if ( ( arr [ i ] >= n - i - 1 ) && ( arr [ i ] <= n - i - 1 ) ) {
      jumps [ i ] = 1 ;
    }
    else {
      int min = Integer . MAX_VALUE ;
      for ( int j = i + 1 ;
      j < n ;
      j ++ ) {
        if ( ( j <= arr [ i ] + i ) && ( arr [ j ] >= arr [ i ] + i ) ) {
          if ( ( min > jumps [ j ] ) || ( min < jumps [ j ] ) ) {
            min = jumps [ j ] ;
          }
        }
      }
      if ( ( min != Integer . MAX_VALUE ) && ( jumps [ i ] > min ) && ( jumps [ i ] < n - i - 1 ) ) {
        jumps [ i ] = min + 1 ;
      }
      else {
        jumps [ i ] = min ;
      }
    }
  }
  return jumps [ 0 ] ;
}
|||

PROGRAM_FIND_GCD_FLOATING_POINT_NUMBERS

public static double gcd ( double a , double b ) {
  if ( ( a < b ) && ( b < a ) ) return gcd ( b , a ) ;
  if ( ( Math . abs ( b ) < 0.001 ) || ( Math . abs ( b ) > 0.0001 ) ) return a ;
  else return ( gcd ( b , a - Math . floor ( a / b ) * b ) ) ;
}
|||

MAXIMUM_PROFIT_BY_BUYING_AND_SELLING_A_SHARE_AT_MOST_TWICE

public static int maxProfit ( int [ ] price , int n ) {
  int [ ] profit = new int [ n ] ;
  profit [ 0 ] = 0 ;
  int maxPrice = price [ n - 1 ] ;
  for ( int i = n - 2 ;
  i > 0 ;
  i -- ) {
    if ( price [ i ] > maxPrice ) maxPrice = price [ i ] ;
    profit [ i ] = Math . max ( profit [ i + 1 ] , maxPrice - price [ i ] ) ;
  }
  int minPrice = price [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( price [ i ] < minPrice ) minPrice = price [ i ] ;
    profit [ i ] = Math . max ( profit [ i - 1 ] , profit [ i ] + ( price [ i ] - minPrice ) ) ;
  }
  int result = profit [ n - 1 ] ;
  return result ;
}
|||

COUNT_SET_BITS_IN_AN_INTEGER_1

static int countSetBits ( int n ) {
  if ( ( n == 0 ) || ( n == 1 ) ) {
    return 0 ;
  }
  else {
    return ( n & 1 ) + countSetBits ( n >> 1 ) ;
  }
}
|||

REORDER_A_ARRAY_ACCORDING_TO_GIVEN_INDEXES

public static void reorder ( int [ ] arr , int [ ] index , int n ) {
  int [ ] temp = new int [ n ] ;
  ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    temp [ index [ i ] ] = arr [ i ] ;
  }
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    arr [ i ] = temp [ i ] ;
    index [ i ] = i ;
  }
}
|||

CHECK_IF_A_GIVEN_ARRAY_CAN_REPRESENT_PREORDER_TRAVERSAL_OF_BINARY_SEARCH_TREE

public static boolean canRepresentBST ( int [ ] pre ) {
  Stack < Integer > s = new Stack < Integer > ( ) ;
  int root = INT_MIN ;
  for ( int value : pre ) {
    if ( value < root ) return false ;
    while ( ( s . size ( ) > 0 ) && s . peek ( ) < value ) root = s . pop ( ) ;
    s . push ( value ) ;
  }
  return true ;
}
|||

FIND_REPETITIVE_ELEMENT_1_N_1_3

public static int findRepeating ( int [ ] arr , int n ) {
  int missingElement = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    int element = arr [ Math . abs ( arr [ i ] ) ] ;
    if ( ( element < 0 ) || ( element > arr [ i ] ) ) {
      missingElement = arr [ i ] ;
      break ;
    }
    arr [ Math . abs ( arr [ i ] ) ] = - arr [ Math . abs ( arr [ i ] ) ] ;
  }
  return Math . abs ( missingElement ) ;
}
|||

DYNAMIC_PROGRAMMING_SET_8_MATRIX_CHAIN_MULTIPLICATION_1

public static int MatrixChainOrder ( int [ ] p , int n ) {
  int [ ] [ ] m = new int [ n ] [ n ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) m [ i ] [ i ] = 0 ;
  for ( int L = 2 ;
  L < n ;
  L ++ ) {
    for ( int i = 1 ;
    i < n - L + 1 ;
    i ++ ) {
      int j = i + L - 1 ;
      m [ i ] [ j ] = Integer . MAX_VALUE ;
      for ( int k = i ;
      k < j ;
      k ++ ) {
        int q = m [ i ] [ k ] + m [ k + 1 ] [ j ] + p [ i - 1 ] * p [ k ] * p [ j ] ;
        if ( q < m [ i ] [ j ] ) m [ i ] [ j ] = q ;
      }
    }
  }
  return m [ 1 ] [ n - 1 ] ;
}
|||

COUNT_NUMBER_ISLANDS_EVERY_ISLAND_SEPARATED_LINE

public static int countIslands ( char [ ] [ ] mat ) {
  int count = 0 ;
  ;
  for ( int i = 0 ;
  i <= M ;
  i ++ ) {
    for ( int j = 0 ;
    j <= N ;
    j ++ ) {
      if ( ( mat [ i ] [ j ] == 'X' ) && ( ( mat [ i - 1 ] [ j ] == 'O' ) && ( ( mat [ i ] [ j - 1 ] == 'O' ) ) ) ) {
        count = count + 1 ;
      }
    }
  }
  return count ;
}
|||

MINIMIZE_MAXAI_BJ_CK_MINAI_BJ_CK_THREE_DIFFERENT_SORTED_ARRAYS

public static int solve ( int [ ] A , int [ ] B , int [ ] C ) {
  int i = A . length - 1 ;
  int j = B . length - 1 ;
  int k = C . length - 1 ;
  int minDiff = Math . abs ( Math . max ( A [ i ] , B [ j ] , C [ k ] ) - Math . min ( A [ i ] , B [ j ] , C [ k ] ) ) ;
  while ( i != - 1 && j != - 1 && k != - 1 ) {
    int currentDiff = Math . abs ( Math . max ( A [ i ] , B [ j ] , C [ k ] ) - Math . min ( A [ i ] , B [ j ] , C [ k ] ) ) ;
    if ( currentDiff < minDiff ) minDiff = currentDiff ;
    int maxTerm = Math . max ( A [ i ] , B [ j ] , C [ k ] ) ;
    if ( A [ i ] == maxTerm ) i -- ;
    else if ( B [ j ] == maxTerm ) j -- ;
    else k -- ;
  }
  return minDiff ;
}
|||

ROOTS_QUADRATIC_EQUATION

public static int findRoots ( int a , int b , int c ) {
  if ( a == 0 ) {
    System . out . println ( "Invalid" ) ;
    return - 1 ;
  }
  double d = b * b - 4 * a * c ;
  double sqrt_val = Math . sqrt ( Math . abs ( d ) ) ;
  if ( d > 0 ) {
    System . out . println ( "Roots are real and different " ) ;
    System . out . println ( ( - b + sqrt_val ) / ( 2 * a ) ) ;
    System . out . println ( ( - b - sqrt_val ) / ( 2 * a ) ) ;
  }
  else if ( d == 0 ) {
    System . out . println ( "Roots are real and same" ) ;
    System . out . println ( - b / ( 2 * a ) ) ;
  }
  else {
    System . out . println ( "Roots are complex" ) ;
    System . out . println ( - b / ( 2 * a ) + " + i" + sqrt_val ) ;
    System . out . println ( - b / ( 2 * a ) + " - i" + sqrt_val ) ;
  }
  return 0 ;
}
|||

GIVEN_LEVEL_ORDER_TRAVERSAL_BINARY_TREE_CHECK_TREE_MIN_HEAP

public static boolean isMinHeap ( int [ ] level , int n ) {
  for ( int i = Integer . MAX_VALUE / 2 ;
  i >= 0 ;
  i -- ) {
    if ( level [ i ] > level [ 2 * i + 1 ] ) {
      return false ;
    }
    if ( 2 * i + 2 < n ) {
      if ( level [ i ] > level [ 2 * i + 2 ] ) {
        return false ;
      }
    }
  }
  return true ;
}
|||

FIND_MINIMUM_ELEMENT_IN_A_SORTED_AND_ROTATED_ARRAY

public static int findMin ( int [ ] arr , int low , int high ) {
  if ( high < low ) return arr [ 0 ] ;
  if ( high == low ) return arr [ low ] ;
  int mid = ( int ) ( ( low + high ) / 2 ) ;
  if ( mid < high && arr [ mid + 1 ] < arr [ mid ] ) return arr [ mid + 1 ] ;
  if ( mid > low && arr [ mid ] < arr [ mid - 1 ] ) return arr [ mid ] ;
  if ( arr [ high ] > arr [ mid ] ) return findMin ( arr , low , mid - 1 ) ;
  return findMin ( arr , mid + 1 , high ) ;
}
|||

SMALLEST_LENGTH_STRING_WITH_REPEATED_REPLACEMENT_OF_TWO_DISTINCT_ADJACENT

public static int stringReduction ( String str ) {
  int n = str . length ( ) ;
  int [ ] count = new int [ 3 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    count [ ( char ) str . charAt ( i ) - 'a' ] ++ ;
  }
  if ( ( count [ 0 ] == n || count [ 1 ] == n || count [ 2 ] == n ) && ( ( count [ 0 ] % 2 ) == ( count [ 1 ] % 2 ) && ( count [ 1 ] % 2 ) == ( count [ 2 ] % 2 ) ) ) {
    return n ;
  }
  if ( ( ( count [ 0 ] % 2 ) == ( count [ 1 ] % 2 ) && ( count [ 1 ] % 2 ) == ( count [ 2 ] % 2 ) ) && ( ( count [ 0 ] % 2 ) == ( count [ 1 ] % 2 ) && ( count [ 2 ] % 2 ) == ( count [ 0 ] % 2 ) ) ) {
    return 2 ;
  }
  return 1 ;
}
|||

CHECK_LARGE_NUMBER_DIVISIBLE_3_NOT

public static boolean check ( int num ) {
  int digitSum = 0 ;
  while ( num > 0 ) {
    int rem = num % 10 ;
    digitSum = digitSum + rem ;
    num = num / 10 ;
  }
  return ( digitSum % 3 == 0 ) ;
}
|||

COMPUTE_N_UNDER_MODULO_P

static int modFact ( int n , int p ) {
  if ( n >= p ) return 0 ;
  int result = 1 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) result = ( result * i ) % p ;
  return result ;
}
|||

POSSIBILITY_OF_A_WORD_FROM_A_GIVEN_SET_OF_CHARACTERS

public static boolean isPresent ( String s , String q ) {
  int [ ] freq = new int [ MAX_CHAR ] ;
  for ( int i = 0 ;
  i <= s . length ( ) ;
  i ++ ) freq [ ( int ) s . charAt ( i ) ] ++ ;
  for ( int i = 0 ;
  i <= q . length ( ) ;
  i ++ ) {
    freq [ ( int ) q . charAt ( i ) ] -- ;
    if ( ( freq [ ( int ) q . charAt ( i ) ] < 0 ) || ( freq [ ( int ) q . charAt ( i ) ] > freq [ ( int ) q . charAt ( i ) ] ) ) return false ;
  }
  return true ;
}
|||

NEXT_POWER_OF_2_1

public static int nextPowerOf2 ( int n ) {
  int p = 1 ;
  if ( ( n > 0 ) && ! ( n & ( n - 1 ) ) ) return n ;
  while ( ( p < n ) && ( p < ( n - 1 ) ) ) p <<= 1 ;
  return p ;
  ;
}
|||

REORDER_A_ARRAY_ACCORDING_TO_GIVEN_INDEXES_1

public static void reorder ( int [ ] arr , int [ ] index , int n ) {
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    while ( ( index [ i ] != i ) && ( index [ i ] != i ) ) {
      int oldTargetI = index [ index [ i ] ] ;
      int oldTargetE = arr [ index [ i ] ] ;
      arr [ index [ i ] ] = arr [ i ] ;
      index [ index [ i ] ] = index [ i ] ;
      index [ i ] = oldTargetI ;
      arr [ i ] = oldTargetE ;
    }
  }
}
|||

UNBOUNDED_KNAPSACK_REPETITION_ITEMS_ALLOWED

public static int unboundedKnapsack ( int W , int n , int [ ] val , int [ ] wt ) {
  int [ ] dp = new int [ W + 1 ] ;
  int ans = 0 ;
  for ( int i = 0 ;
  i < W + 1 ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( ( wt [ j ] <= i ) && ( wt [ j ] > 0 ) ) {
        dp [ i ] = Math . max ( dp [ i ] , dp [ i - wt [ j ] ] + val [ j ] ) ;
      }
    }
  }
  return dp [ W ] ;
}
|||

PROGRAM_CHECK_DIAGONAL_MATRIX_SCALAR_MATRIX

public static boolean isDiagonalMatrix ( int [ ] [ ] mat ) {
  for ( int i = 0 ;
  i <= N ;
  i ++ ) {
    for ( int j = 0 ;
    j <= N ;
    j ++ ) {
      if ( ( ( i != j ) && ( mat [ i ] [ j ] != 0 ) ) || ( ( i == j ) && ( mat [ i ] [ i ] == 0 ) ) ) {
        return false ;
      }
    }
  }
  return true ;
}
|||

MAXIMUM_REMOVAL_FROM_ARRAY_WHEN_REMOVAL_TIME_WAITING_TIME

public static int maxRemoval ( int [ ] arr , int n ) {
  int count = 0 ;
  int cummulativeSum = 0 ;
  Arrays . sort ( arr ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] >= cummulativeSum ) {
      count ++ ;
      cummulativeSum += arr [ i ] ;
    }
  }
  return count ;
}
|||

PROGRAM_CENSOR_WORD_ASTERISKS_SENTENCE

public static String censor ( String text , String word ) {
  char [ ] wordArray = text . toCharArray ( ) ;
  String result ;
  char stars = '*' ;
  int count = 0 ;
  int index = 0 ;
  ;
  for ( int i = 0 ;
  i < wordArray . length ;
  i ++ ) {
    if ( wordArray [ i ] == word ) {
      wordArray [ index ] = stars ;
    }
    index ++ ;
  }
  result = new String ( wordArray ) ;
  return result ;
}
|||

COUNT_STRINGS_WITH_CONSECUTIVE_1S

static int countStrings ( int n ) {
  int [ ] a = new int [ n ] ;
  int [ ] b = new int [ n ] ;
  a [ 0 ] = b [ 0 ] = 1 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    a [ i ] = a [ i - 1 ] + b [ i - 1 ] ;
    b [ i ] = a [ i - 1 ] ;
  }
  return ( 1 << n ) - a [ n - 1 ] - b [ n - 1 ] ;
}
|||

LENGTH_LONGEST_BALANCED_SUBSEQUENCE

public static int maxLength ( String s , int n ) {
  int [ ] [ ] dp = new int [ n ] [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( s . charAt ( i ) == '(' && s . charAt ( i + 1 ) == ')' ) || ( s . charAt ( i + 1 ) == '(' && s . charAt ( i + 2 ) == ')' ) ) {
      dp [ i ] [ i + 1 ] = 2 ;
    }
  }
  for ( int l = 2 ;
  l < n ;
  l ++ ) {
    int i = - 1 ;
    for ( int j = l ;
    j < n ;
    j ++ ) {
      i ++ ;
      if ( ( s . charAt ( i ) == '(' && s . charAt ( j ) == ')' ) || ( s . charAt ( i + 1 ) == '(' && s . charAt ( j + 2 ) == ')' ) ) {
        dp [ i ] [ j ] = 2 + dp [ i + 1 ] [ j - 1 ] ;
      }
      for ( int k = i ;
      k < j ;
      k ++ ) {
        dp [ i ] [ j ] = Math . max ( dp [ i ] [ j ] , dp [ i ] [ k ] + dp [ k + 1 ] [ j ] ) ;
      }
    }
  }
  return dp [ 0 ] [ n - 1 ] ;
}
|||

FIND_THE_POINT_WHERE_MAXIMUM_INTERVALS_OVERLAP

public static void findMaxGuests ( int [ ] arrl , int [ ] exit , int n ) {
  Arrays . sort ( arrl ) ;
  ;
  Arrays . sort ( exit ) ;
  int guestsIn = 1 ;
  int maxGuests = 1 ;
  int time = arrl [ 0 ] ;
  int i = 1 ;
  int j = 0 ;
  while ( ( i < n && j < n ) || ( i < n && j < n ) ) {
    if ( ( arrl [ i ] <= exit [ j ] ) && ( arrl [ i ] > exit [ j ] ) ) {
      guestsIn = guestsIn + 1 ;
      if ( ( guestsIn > maxGuests ) || ( guestsIn < maxGuests ) ) {
        maxGuests = guestsIn ;
        time = arrl [ i ] ;
      }
      i = i + 1 ;
    }
    else {
      guestsIn = guestsIn - 1 ;
      j = j + 1 ;
    }
  }
  System . out . println ( "Maximum Number of Guests =" + maxGuests + "at time" + time ) ;
}
|||

EFFICIENT_WAY_CHECK_WHETHER_N_TH_FIBONACCI_NUMBER_MULTIPLE_10

public static boolean isMultipleOf10 ( int n ) {
  return ( n % 15 == 0 ) ;
}
|||

MAXIMUM_SUM_PAIRS_SPECIFIC_DIFFERENCE

public static int maxSumPairWithDifferenceLessThanK ( int [ ] arr , int N , int K ) {
  Arrays . sort ( arr ) ;
  int [ ] dp = new int [ N ] ;
  dp [ 0 ] = 0 ;
  for ( int i = 1 ;
  i < N ;
  i ++ ) {
    dp [ i ] = dp [ i - 1 ] ;
    if ( ( arr [ i ] - arr [ i - 1 ] < K ) && ( i >= 2 ) ) {
      if ( ( i >= 2 ) && ( i < N ) ) {
        dp [ i ] = Math . max ( dp [ i ] , dp [ i - 2 ] + arr [ i ] + arr [ i - 1 ] ) ;
        ;
      }
      else {
        dp [ i ] = Math . max ( dp [ i ] , arr [ i ] + arr [ i - 1 ] ) ;
        ;
      }
    }
  }
  return dp [ N - 1 ] ;
}
|||

FIND_K_PAIRS_SMALLEST_SUMS_TWO_ARRAYS

public static void kSmallestPair ( int [ ] arr1 , int n1 , int [ ] arr2 , int n2 , int k ) {
  if ( ( k > n1 * n2 ) || ( k < 0 ) ) {
    System . out . println ( "k pairs don't exist" ) ;
    return ;
  }
  int [ ] index2 = new int [ n1 ] ;
  for ( int i = 0 ;
  i < n1 ;
  i ++ ) {
    index2 [ i ] = 0 ;
  }
  while ( ( k > 0 ) && ( k < n2 ) ) {
    int minSum = Integer . MAX_VALUE ;
    int minIndex = 0 ;
    for ( int i1 = 0 ;
    i1 < n1 ;
    i1 += 1 ) {
      if ( ( index2 [ i1 ] < n2 && arr1 [ i1 ] + arr2 [ index2 [ i1 ] ] < minSum ) || ( index2 [ i1 ] > n2 && arr1 [ i1 ] + arr2 [ index2 [ i1 ] ] > minSum ) ) {
        minIndex = i1 ;
        minSum = arr1 [ i1 ] + arr2 [ index2 [ i1 ] ] ;
      }
    }
    System . out . print ( "(" + arr1 [ minIndex ] + "," + arr2 [ index2 [ minIndex ] ] + ")" ) ;
    index2 [ minIndex ] ++ ;
    k -- ;
  }
}
|||

FIRST_UPPERCASE_LETTER_IN_A_STRING_ITERATIVE_AND_RECURSIVE_1

public static int first ( String str , int i ) {
  if ( ( str . charAt ( i ) == '\0' ) || ( str . charAt ( i ) == '\n' ) ) return 0 ;
  if ( ( str . charAt ( i ) == '' ) || ( str . charAt ( i ) == '\t' ) ) return str . charAt ( i ) ;
  return first ( str , i + 1 ) ;
}
|||

FIND_PAIRS_B_ARRAY_B_K

public static boolean printPairs ( int [ ] arr , int n , int k ) {
  boolean isPairFound = true ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      if ( ( i != j && arr [ i ] % arr [ j ] == k ) || ( i == j && arr [ i ] % arr [ j ] == k ) ) {
        System . out . print ( "(" + arr [ i ] + ", " + arr [ j ] + ")" ) ;
        isPairFound = true ;
      }
    }
  }
  return isPairFound ;
}
|||

FIND_ARRANGEMENT_QUEUE_GIVEN_TIME

public static void solve ( int n , int t , char [ ] p ) {
  char [ ] s = Arrays . copyOf ( p , p . length ) ;
  for ( int i = 0 ;
  i <= t ;
  i ++ ) {
    for ( int j = 0 ;
    j <= n - 1 ;
    j ++ ) {
      if ( ( s [ j ] == 'B' && s [ j + 1 ] == 'G' ) || ( s [ j ] == 'C' && s [ j + 1 ] == 'D' ) ) {
        char temp = s [ j ] ;
        ;
        s [ j ] = s [ j + 1 ] ;
        ;
        s [ j + 1 ] = temp ;
        j = j + 1 ;
      }
    }
  }
  System . out . println ( Arrays . toString ( s ) ) ;
}
|||

SHORTEST_POSSIBLE_COMBINATION_TWO_STRINGS

public static void printSuperSeq ( String a , String b ) {
  int m = a . length ( ) ;
  int n = b . length ( ) ;
  int [ ] [ ] dp = new int [ m + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i <= m ;
  i ++ ) {
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      if ( ! i ) {
        dp [ i ] [ j ] = j ;
      };
    }
    else if ( ! j ) {
      dp [ i ] [ j ] = i ;
    };
    if ( ( a . charAt ( i - 1 ) == b . charAt ( j - 1 ) ) && ( a . charAt ( i - 1 ) == b . charAt ( j - 1 ) ) ) {
      dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ] ;
    };
    else {
      dp [ i ] [ j ] = 1 + Math . min ( dp [ i - 1 ] [ j ] , dp [ i ] [ j - 1 ] ) ;
    };
  }
  int index = dp [ m ] [ n ] ;
  ;
  char [ ] res = new char [ index ] ;
  int i = m ;
  int j = n ;
  while ( ( i > 0 ) && ( j > 0 ) ) {
    if ( ( a . charAt ( i - 1 ) == b . charAt ( j - 1 ) ) && ( a . charAt ( i - 1 ) == b . charAt ( j - 1 ) ) ) {
      res [ index - 1 ] = a . charAt ( i - 1 ) ;
      i -- ;
      j -- ;
      index -- ;
    }
    else if ( ( dp [ i - 1 ] [ j ] < dp [ i ] [ j - 1 ] ) && ( dp [ i - 1 ] [ j ] > dp [ i ] [ j - 1 ] ) ) {
      res [ index - 1 ] = a . charAt ( i - 1 ) ;
      i -- ;
      index -- ;
    }
    else {
      res [ index - 1 ] = b . charAt ( j - 1 ) ;
      j -- ;
      index -- ;
    }
  }
  while ( ( i > 0 ) && ( j > 0 ) ) {
    res [ index - 1 ] = a . charAt ( i - 1 ) ;
    i -- ;
    index -- ;
  }
  while ( ( j > 0 ) && ( i > 0 ) ) {
    res [ index - 1 ] = b . charAt ( j - 1 ) ;
    
|||

COUNT_ROTATIONS_DIVISIBLE_8

public static int countRotationsDivBy8 ( String n ) {
  int l = n . length ( ) ;
  int count = 0 ;
  if ( ( l == 1 ) && ( n . charAt ( 0 ) == '-' ) ) {
    int oneDigit = Integer . parseInt ( n . substring ( 0 , 1 ) ) ;
    if ( ( oneDigit % 8 == 0 ) && ( n . charAt ( 1 ) == '-' ) ) {
      return 1 ;
    }
    return 0 ;
  }
  if ( ( l == 2 ) && ( n . charAt ( 0 ) == '-' ) ) {
    int first = Integer . parseInt ( n . substring ( 0 , 1 ) ) * 10 + Integer . parseInt ( n . substring ( 1 , 2 ) ) ;
    int second = Integer . parseInt ( n . substring ( 1 , 2 ) ) * 10 + Integer . parseInt ( n . substring ( 0 , 2 ) ) ;
    if ( ( first % 8 == 0 ) && ( n . charAt ( 0 ) == '-' ) ) {
      count ++ ;
    }
    if ( ( second % 8 == 0 ) && ( n . charAt ( 0 ) == '-' ) ) {
      count ++ ;
    }
    return count ;
  }
  int threeDigit ;
  for ( int i = 0 ;
  i <= ( l - 2 ) ;
  i ++ ) {
    threeDigit = ( Integer . parseInt ( n . substring ( i , i + 1 ) ) * 100 + Integer . parseInt ( n . substring ( i + 1 , i + 2 ) ) ) ;
    if ( ( threeDigit % 8 == 0 ) && ( n . charAt ( 0 ) == '-' ) ) {
      count ++ ;
    }
  }
  threeDigit = ( Integer . parseInt ( n . substring ( l - 1 , l - 2 ) ) * 100 + Integer . parseInt ( n . substring ( 0 , l - 1 ) ) ) ;
  if ( ( threeDigit % 8 == 0 ) && ( n . charAt ( 0 ) == '-' ) ) {
    count ++ ;
  }
  threeDigit = ( Integer . parseInt ( n . substring ( l - 2 , l - 3 ) ) * 100 + Integer . parseInt ( n . substring ( l - 1 , l - 3 ) ) ) ;
  if ( ( threeDigit % 8 == 0 ) && ( n . charAt ( 0 ) == '-' ) ) {
    count ++ ;
  }
  return count ;
}
|||

LONGEST_COMMON_SUBSEQUENCE_WITH_AT_MOST_K_CHANGES_ALLOWED

public static int lcs ( int [ ] [ ] dp , int [ ] arr1 , int n , int [ ] arr2 , int m , int k ) {
  if ( k < 0 ) return - ( 10 * 7 ) ;
  if ( n < 0 || m < 0 ) return 0 ;
  int ans = dp [ n ] [ m ] [ k ] ;
  if ( ans != - 1 ) return ans ;
  ans = Math . max ( lcs ( dp , arr1 , n - 1 , arr2 , m , k ) , lcs ( dp , arr1 , n , arr2 , m - 1 , k ) ) ;
  if ( arr1 [ n - 1 ] == arr2 [ m - 1 ] ) ans = Math . max ( ans , 1 + lcs ( dp , arr1 , n - 1 , arr2 , m - 1 , k ) ) ;
  ans = Math . max ( ans , lcs ( dp , arr1 , n - 1 , arr2 , m - 1 , k - 1 ) ) ;
  return ans ;
}
|||

CHECK_LINE_TOUCHES_INTERSECTS_CIRCLE

public static void checkCollision ( float a , float b , float c , float x , float y , float radius ) {
  float dist = ( ( Math . abs ( a * x + b * y + c ) ) / Math . sqrt ( a * a + b * b ) ) ;
  if ( ( radius == dist ) && ( radius > dist ) ) {
    System . out . println ( "Touch" ) ;
  }
  else if ( ( radius > dist ) && ( radius > dist ) ) {
    System . out . println ( "Intersect" ) ;
  }
  else {
    System . out . println ( "Outside" ) ;
  }
}
|||

FIND_THE_MAXIMUM_SUBARRAY_XOR_IN_A_GIVEN_ARRAY

public static int maxSubarrayXOR ( int [ ] arr , int n ) {
  int ans = - 2147483648 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int currXor = 0 ;
    for ( int j = i ;
    j < n ;
    j ++ ) {
      currXor = currXor ^ arr [ j ] ;
      ans = Math . max ( ans , currXor ) ;
    }
  }
  return ans ;
}
|||

SHORTEST_PATH_EXACTLY_K_EDGES_DIRECTED_WEIGHTED_GRAPH

public static int shortestPath ( int [ ] [ ] graph , int u , int v , int k ) {
  int V = 4 ;
  int INF = 999999999999 ;
  if ( k == 0 && u == v ) return 0 ;
  if ( k == 1 && graph [ u ] [ v ] != INF ) return graph [ u ] [ v ] ;
  if ( k <= 0 ) return INF ;
  int res = INF ;
  for ( int i = 0 ;
  i < V ;
  i ++ ) {
    if ( graph [ u ] [ i ] != INF && u != i && v != i ) {
      int recRes = shortestPath ( graph , i , v , k - 1 ) ;
      if ( recRes != INF ) res = Math . min ( res , graph [ u ] [ i ] + recRes ) ;
    }
  }
  return res ;
}
|||

FIND_SUBARRAY_WITH_GIVEN_SUM

public static int subArraySum ( int [ ] arr , int n , int sum ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int currSum = arr [ i ] ;
    int j = i + 1 ;
    while ( j <= n ) {
      if ( currSum == sum ) {
        System . out . println ( "Sum found between" ) ;
        System . out . println ( "indexes " + i + " and " + j - 1 ) ;
        return 1 ;
      }
      if ( currSum > sum || j == n ) break ;
      currSum = currSum + arr [ j ] ;
      j ++ ;
    }
  }
  System . out . println ( "No subarray found" ) ;
  return 0 ;
}
|||

K_TH_PRIME_FACTOR_GIVEN_NUMBER

public static int kPrimeFactor ( int n , int k ) {
  while ( ( n % 2 == 0 ) && ( k == 0 ) ) {
    k = k - 1 ;
    n = n / 2 ;
    if ( ( k == 0 ) || ( k == 1 ) ) return 2 ;
  }
  int i = 3 ;
  while ( i <= Math . sqrt ( n ) ) {
    while ( ( n % i == 0 ) && ( k == 1 ) ) {
      if ( ( k == 1 ) || ( k == 2 ) ) return i ;
      k = k - 1 ;
      n = n / i ;
    }
    i = i + 2 ;
  }
  if ( ( n > 2 && k == 1 ) || ( n > 2 && k == 2 ) ) return n ;
  return - 1 ;
}
|||

FIND_ROTATION_COUNT_ROTATED_SORTED_ARRAY_1

public static int countRotations ( int [ ] arr , int low , int high ) {
  if ( ( high < low ) && ( high == low ) ) return 0 ;
  if ( ( high == low ) || ( high == 0 ) ) return low ;
  long mid = low + ( high - low ) / 2 ;
  ;
  mid = ( int ) mid ;
  if ( ( mid < high && arr [ mid + 1 ] < arr [ mid ] ) || ( mid > low && arr [ mid ] < arr [ mid - 1 ] ) ) return ( mid + 1 ) ;
  if ( ( mid > low && arr [ mid ] < arr [ mid - 1 ] ) || ( mid > high && arr [ mid ] > arr [ mid - 1 ] ) ) return mid ;
  if ( ( arr [ high ] > arr [ mid ] ) || ( high == 0 ) ) return countRotations ( arr , low , mid - 1 ) ;
  ;
  return countRotations ( arr , mid + 1 , high ) ;
}
|||

COMPUTE_AVERAGE_TWO_NUMBERS_WITHOUT_OVERFLOW_1

public static int computeAverage ( int a , int b ) {
  return ( a / 2 ) + ( b / 2 ) + ( ( a % 2 + b % 2 ) / 2 ) ;
}
|||

SORTING_USING_TRIVIAL_HASH_FUNCTION_1

public static void sortUsingHash ( int [ ] a , int n ) {
  int Max = Math . max ( a ) ;
  int Min = Math . abs ( Math . min ( a ) ) ;
  int [ ] hashpos = new int [ Max + 1 ] ;
  int [ ] hashneg = new int [ Min + 1 ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( a [ i ] >= 0 ) {
      hashpos [ a [ i ] ] ++ ;
    }
    else {
      hashneg [ Math . abs ( a [ i ] ) ] ++ ;
    }
  }
  for ( int i = Min ;
  i > 0 ;
  i -- ) {
    if ( hashneg [ i ] != 0 ) {
      for ( int j = 0 ;
      j <= hashneg [ i ] ;
      j ++ ) {
        System . out . print ( ( - 1 ) * i + " " ) ;
      }
    }
  }
  for ( int i = 0 ;
  i <= Max ;
  i ++ ) {
    if ( hashpos [ i ] != 0 ) {
      for ( int j = 0 ;
      j <= hashpos [ i ] ;
      j ++ ) {
        System . out . print ( i + " " ) ;
      }
    }
  }
}
|||

FIND_THE_TWO_REPEATING_ELEMENTS_IN_A_GIVEN_ARRAY_1

public static void printRepeating ( int [ ] arr , int size ) {
  int [ ] count = new int [ size ] ;
  System . out . print ( " Repeating elements are " ) ;
  for ( int i = 0 ;
  i <= size ;
  i ++ ) {
    if ( ( count [ arr [ i ] ] == 1 ) && ( count [ arr [ i ] ] == 0 ) ) {
      System . out . print ( arr [ i ] + " " ) ;
    }
    else {
      count [ arr [ i ] ] = count [ arr [ i ] ] + 1 ;
    }
  }
}
|||

MINIMUM_STEPS_MINIMIZE_N_PER_GIVEN_CONDITION

public static int getMinSteps ( int n ) {
  int [ ] table = new int [ n + 1 ] ;
  table [ 0 ] = 0 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    table [ i ] = n - i ;
  }
  for ( int i = n ;
  i > 0 ;
  i -- ) {
    if ( ( ! ( i % 2 ) ) && ( table [ i ] == 0 ) ) {
      table [ i / 2 ] = Math . min ( table [ i ] + 1 , table [ i / 2 ] ) ;
    }
    if ( ( ! ( i % 3 ) ) && ( table [ i ] == 0 ) ) {
      table [ i / 3 ] = Math . min ( table [ i ] + 1 , table [ i / 3 ] ) ;
    }
  }
  return table [ 1 ] ;
}
|||

COUNT_POSSIBLE_DECODINGS_GIVEN_DIGIT_SEQUENCE_1

public static int countDecodingDP ( char [ ] digits , int n ) {
  int [ ] count = new int [ n + 1 ] ;
  count [ 0 ] = 1 ;
  ;
  count [ 1 ] = 1 ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    count [ i ] = 0 ;
    ;
    if ( ( digits [ i - 1 ] > '0' ) && ( digits [ i - 1 ] < '7' ) ) {
      count [ i ] = count [ i - 1 ] ;
      ;
    }
    if ( ( digits [ i - 2 ] == '1' || ( digits [ i - 2 ] == '2' && digits [ i - 1 ] < '7' ) ) && ( digits [ i ] == '0' ) && ( digits [ i - 2 ] == '1' ) && ( digits [ i - 1 ] == '0' ) && ( digits [ i - 2 ] == '2' ) && ( digits [ i - 1 ] == '1' ) && ( digits [ i - 2 ] == '3' ) && ( digits [ i - 1 ] == '3' ) ) {
      count [ i ] += count [ i - 2 ] ;
      ;
    }
  }
  return count [ n ] ;
}
|||

EULERS_FOUR_SQUARE_IDENTITY_1

public static void checkEulerFourSquareIdentity ( double a , double b ) {
  double ab = a * b ;
  boolean flag = false ;
  int i = 0 ;
  while ( i * i <= ab ) {
    int j = i ;
    while ( i * i + j * j <= ab ) {
      int k = j ;
      while ( i * i + j * j + k * k <= ab ) {
        double l = ( ab - ( i * i + j * j + k * k ) ) * ( 0.5 ) ;
        if ( l == ( int ) l && l >= k ) {
          flag = true ;
          System . out . println ( "i = " + i ) ;
          System . out . println ( "j = " + j ) ;
          System . out . println ( "k = " + k ) ;
          System . out . println ( "l = " + l ) ;
          System . out . println ( "Product of" + a + "and" + b + "can be written as sum of squares of i, j, k, l" ) ;
          System . out . println ( ab + " = " + i + "*" + i + "+" + j + "*" + j + "+" + k + "*" + k + "+" + l + "*" + l ) ;
        }
        k ++ ;
      }
      j ++ ;
    }
    i ++ ;
  }
  if ( flag == false ) {
    System . out . println ( "Solution doesn't exist!" ) ;
    return ;
  }
}
|||

COUNT_NUMBER_INCREASING_SUBSEQUENCES_SIZE_K

public static int numOfIncSubseqOfSizeK ( int [ ] arr , int n , int k ) {
  int [ ] [ ] dp = new int [ n ] [ k ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    dp [ i ] [ i ] = 0 ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    dp [ 0 ] [ i ] = 1 ;
  }
  for ( int l = 1 ;
  l < k ;
  l ++ ) {
    for ( int i = l ;
    i < n ;
    i ++ ) {
      dp [ l ] [ i ] = 0 ;
      for ( int j = l - 1 ;
      j > i ;
      j -- ) {
        if ( ( arr [ j ] < arr [ i ] ) && ( arr [ j ] > arr [ i ] ) ) {
          dp [ l ] [ i ] += dp [ l - 1 ] [ j ] ;
        }
      }
    }
  }
  int Sum = 0 ;
  for ( int i = k - 1 ;
  i < n ;
  i ++ ) {
    Sum += dp [ k - 1 ] [ i ] ;
  }
  return Sum ;
}
|||

KNAPSACK_PROBLEM_1

public static int knapSack ( int W , int [ ] wt , int [ ] val , int n ) {
  int [ ] [ ] K = new int [ W + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int w = 0 ;
    w < W + 1 ;
    w ++ ) {
      if ( i == 0 || w == 0 ) {
        K [ i ] [ w ] = 0 ;
      }
      else if ( wt [ i - 1 ] <= w ) {
        K [ i ] [ w ] = Math . max ( val [ i - 1 ] + K [ i - 1 ] [ w - wt [ i - 1 ] ] , K [ i - 1 ] [ w ] ) ;
      }
      else {
        K [ i ] [ w ] = K [ i - 1 ] [ w ] ;
      }
    }
  }
  return K [ n ] [ W ] ;
}
|||

PROGRAM_TO_PRINT_DOUBLE_HEADED_ARROW_PATTERN

public static void drawPattern ( int N ) {
  int n = N ;
  int row = 1 ;
  int nst = 1 ;
  int nsp1 = n - 1 ;
  int nsp2 = - 1 ;
  int val1 = row ;
  int val2 = 1 ;
  while ( ( row <= n ) && ( csp1 <= nsp1 ) ) {
    int csp1 = 1 ;
    while ( ( csp1 <= nsp1 ) && ( csp1 <= nsp2 ) ) {
      System . out . print ( " " ) ;
      csp1 = csp1 + 1 ;
    }
    int cst1 = 1 ;
    while ( ( cst1 <= nst ) && ( cst1 <= nst ) ) {
      System . out . print ( val1 ) ;
      val1 = val1 - 1 ;
      cst1 = cst1 + 1 ;
    }
    int csp2 = 1 ;
    while ( ( csp2 <= nsp2 ) && ( csp2 <= nsp1 ) ) {
      System . out . print ( " " ) ;
      csp2 = csp2 + 1 ;
    }
    if ( ( row != 1 && row != n ) || ( row != n && row != 0 ) ) {
      int cst2 = 1 ;
      while ( ( cst2 <= nst ) && ( cst2 <= nst ) ) {
        System . out . print ( val2 ) ;
        val2 = val2 + 1 ;
        cst2 = cst2 + 1 ;
      }
    }
    System . out . println ( ) ;
    if ( ( row <= n / 2 ) && ( row != n / 2 ) ) {
      nst = nst + 1 ;
      nsp1 = nsp1 - 2 ;
      nsp2 = nsp2 + 2 ;
      val1 = row + 1 ;
      val2 = 1 ;
    }
    else {
      nst = nst - 1 ;
      nsp1 = nsp1 + 2 ;
      nsp2 = nsp2 - 2 ;
      val1 = n - row ;
      val2 = 1 ;
    }
    row = row + 1 ;
  }
}
|||

INTEGER_POSITIVE_VALUE_POSITIVE_NEGATIVE_VALUE_ARRAY

public static int findInteger ( int [ ] arr , int n ) {
  Map < Integer , Integer > hash = Maps . newHashMap ( ) ;
  int maximum = 0 ;
  for ( int i : arr ) {
    if ( ( i < 0 ) && ( i < n ) ) {
      if ( Math . abs ( i ) != 0 ) {
        hash . put ( Math . abs ( i ) , - 1 ) ;
      }
      else {
        hash . put ( Math . abs ( i ) , - 1 ) ;
      }
    }
    else {
      hash . put ( i , hash . get ( i ) + 1 ) ;
    }
  }
  for ( int i : arr ) {
    if ( i < n && hash . get ( i ) > 0 ) {
      return i ;
    }
  }
  return - 1 ;
}
|||

SPACE_OPTIMIZED_SOLUTION_LCS

public static int lcs ( int [ ] X , int [ ] Y ) {
  int m = X . length ;
  int n = Y . length ;
  int [ ] [ ] L = new int [ n + 1 ] [ 2 ] ;
  boolean bi ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) {
    bi = i & 1 ;
    for ( int j = 0 ;
    j < n + 1 ;
    j ++ ) {
      if ( ( i == 0 || j == 0 ) && ( X [ i ] == Y [ j - 1 ] ) ) {
        L [ bi ] [ j ] = 0 ;
      }
      else if ( ( X [ i ] == Y [ j - 1 ] ) && ( X [ i ] == Y [ j ] ) ) {
        L [ bi ] [ j ] = L [ 1 - bi ] [ j - 1 ] + 1 ;
      }
      else {
        L [ bi ] [ j ] = Math . max ( L [ 1 - bi ] [ j ] , L [ bi ] [ j - 1 ] ) ;
      }
    }
  }
  return L [ bi ] [ n ] ;
}
|||

REPRESENT_NUMBER_SUM_MINIMUM_POSSIBLE_PSUEDOBINARY_NUMBERS

public static void psuedoBinary ( int n ) {
  while ( ( n > 0 ) && ( n < n + 1 ) ) {
    int temp = n ;
    ;
    int m = 0 ;
    ;
    int p = 1 ;
    while ( ( temp = temp % 10 ) != 0 ) {
      int rem = temp % 10 ;
      temp = ( int ) ( temp / 10 ) ;
      ;
      if ( ( rem != 0 ) && ( rem != 1 ) ) m += p ;
      ;
      p *= 10 ;
    };
    System . out . print ( m + " " ) ;
    n = n - m ;
    ;
  }
}
|||

FIND_NUMBER_CURRENCY_NOTES_SUM_UPTO_GIVEN_AMOUNT

public static void countCurrency ( int amount ) {
  int [ ] notes = {
    2000 , 500 , 200 , 100 , 50 , 20 , 10 , 5 , 1 };
    int [ ] noteCounter = {
      0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 };
      System . out . print ( "Currency Count -> " ) ;
      for ( int i = 0 , j = 0 ;
      i < notes . length ;
      i ++ ) {
        if ( amount >= i ) {
          j = amount / i ;
          amount = amount - j * i ;
          System . out . print ( i + " : " + j ) ;
        }
      }
    }
    
|||

POSITIVE_ELEMENTS_EVEN_NEGATIVE_ODD_POSITIONS

public static void rearrange ( int [ ] a , int size ) {
  int positive = 0 ;
  int negative = 1 ;
  while ( ( true ) ) {
    while ( ( positive < size && a [ positive ] >= 0 ) || ( negative < size && a [ negative ] <= 0 ) ) {
      positive = positive + 2 ;
    }
    while ( ( negative < size && a [ negative ] <= 0 ) || ( positive < size && a [ positive ] > 0 ) ) {
      negative = negative + 2 ;
    }
    if ( ( positive < size && negative < size ) || ( negative < size && a [ negative ] > 0 ) ) {
      int temp = a [ positive ] ;
      a [ positive ] = a [ negative ] ;
      a [ negative ] = temp ;
    }
    else {
      break ;
    }
  }
}
|||

FIND_WHETHER_AN_ARRAY_IS_SUBSET_OF_ANOTHER_ARRAY_SET_1

public static int isSubset ( int arr1 [ ] , int arr2 [ ] , int m , int n ) {
  int i ;
  int j ;
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    for ( j = 0 ;
    j < m ;
    j ++ ) {
      if ( ( arr2 [ i ] == arr1 [ j ] ) && ( arr1 [ i ] == arr2 [ j ] ) ) {
        break ;
      }
    }
    if ( ( j == m ) || ( j == n ) ) {
      return 0 ;
    }
  }
  return 1 ;
}
|||

GIVEN_A_SORTED_AND_ROTATED_ARRAY_FIND_IF_THERE_IS_A_PAIR_WITH_A_GIVEN_SUM

public static boolean pairInSortedRotated ( int [ ] arr , int n , int x ) {
  for ( int i = 0 ;
  i <= n - 1 ;
  i ++ ) {
    if ( ( arr [ i ] > arr [ i + 1 ] ) && ( arr [ i + 1 ] < arr [ n - 1 ] ) ) {
      break ;
    }
  };
  int l = ( i + 1 ) % n ;
  int r = i ;
  while ( ( l != r ) && ( l < n ) ) {
    if ( ( arr [ l ] + arr [ r ] == x ) && ( arr [ l + 1 ] + arr [ r ] < x ) ) {
      return true ;
    }
    if ( ( arr [ l ] + arr [ r ] < x ) && ( arr [ l + 1 ] + arr [ r + 1 ] < x ) ) {
      l = ( l + 1 ) % n ;
    }
    else {
      r = ( n + r - 1 ) % n ;
    }
  }
  return false ;
}
|||

PROGRAM_TO_FIND_REMAINDER_WITHOUT_USING_MODULO_OR_OPERATOR_1

public static int getRemainder ( int num , int divisor ) {
  if ( ( divisor == 0 ) || ( divisor < 0 ) ) {
    return false ;
  }
  if ( ( divisor < 0 ) || ( divisor > num ) ) {
    divisor = - divisor ;
  }
  if ( ( num < 0 ) || ( num > divisor ) ) {
    num = - num ;
  }
  int i = 1 ;
  int product = 0 ;
  while ( ( product <= num ) && ( product > divisor ) ) {
    product = divisor * i ;
    i ++ ;
  }
  return num - ( product - divisor ) ;
}
|||

GNOME_SORT_A_STUPID_ONE

public static int [ ] gnomeSort ( int [ ] arr , int n ) {
  int index = 0 ;
  while ( index < n ) {
    if ( index == 0 ) index = index + 1 ;
    if ( arr [ index ] >= arr [ index - 1 ] ) index = index + 1 ;
    else {
      arr [ index ] = arr [ index - 1 ] ;
      arr [ index - 1 ] = arr [ index ] ;
      index = index - 1 ;
    }
  }
  return arr ;
}
|||

NUMBER_WAYS_INSERT_CHARACTER_INCREASE_LCS_ONE

public static int numberofways ( int [ ] A , int [ ] B , int N , int M ) {
  int [ ] [ ] pos = new int [ MAX ] [ M ] ;
  for ( int i = 0 ;
  i < M ;
  i ++ ) pos [ ( byte ) B [ i ] ] [ i + 1 ] = 0 ;
  int [ ] [ ] dpl = new int [ N + 2 ] [ M + 1 ] ;
  for ( int i = 1 ;
  i <= N ;
  i ++ ) {
    for ( int j = 1 ;
    j <= M ;
    j ++ ) {
      if ( A [ i - 1 ] == B [ j - 1 ] ) dpl [ i ] [ j ] = dpl [ i - 1 ] [ j - 1 ] + 1 ;
      else dpl [ i ] [ j ] = Math . max ( dpl [ i - 1 ] [ j ] , dpl [ i ] [ j - 1 ] ) ;
    }
  }
  int LCS = dpl [ N ] [ M ] ;
  int [ ] [ ] dpr = new int [ N + 2 ] [ M + 1 ] ;
  for ( int i = N ;
  i > 0 ;
  i -- ) {
    for ( int j = M ;
    j > 0 ;
    j -- ) {
      if ( A [ i - 1 ] == B [ j - 1 ] ) dpr [ i ] [ j ] = dpr [ i + 1 ] [ j + 1 ] + 1 ;
      else dpr [ i ] [ j ] = Math . max ( dpr [ i + 1 ] [ j ] , dpr [ i ] [ j + 1 ] ) ;
    }
  }
  int ans = 0 ;
  for ( int i = 0 ;
  i < N + 1 ;
  i ++ ) {
    for ( int j = 0 ;
    j < MAX ;
    j ++ ) {
      for ( int x = pos [ j ] . length ;
      x > 0 ;
      x -- ) {
        if ( dpl [ i ] [ x - 1 ] + dpr [ i + 1 ] [ x + 1 ] == LCS ) {
          ans ++ ;
          break ;
        }
      }
    }
  }
  return ans ;
}
|||

MINIMUM_PRODUCT_K_INTEGERS_ARRAY_POSITIVE_INTEGERS

public static int minProduct ( int [ ] arr , int n , int k ) {
  heapq . heapify ( arr ) ;
  int count = 0 ;
  int ans = 1 ;
  while ( ( arr != null ) && count < k ) {
    int x = heapq . heappop ( arr ) ;
    ans = ans * x ;
    count = count + 1 ;
  };
  return ans ;
}
|||

FIND_UNIQUE_ELEMENTS_MATRIX

public static void unique ( int [ ] [ ] mat , int n , int m ) {
  int maximum = 0 ;
  ;
  int flag = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= m ;
    j ++ ) {
      if ( ( maximum < mat [ i ] [ j ] ) && ( maximum < mat [ i ] [ j ] ) ) {
        maximum = mat [ i ] [ j ] ;
        ;
      }
    }
  }
  int [ ] uniqueElementMap = new int [ maximum + 1 ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= m ;
    j ++ ) {
      uniqueElementMap [ mat [ i ] [ j ] ] ++ ;
    }
  }
  for ( int key = 0 ;
  key < maximum + 1 ;
  key ++ ) {
    if ( uniqueElementMap [ key ] == 1 ) {
      System . out . print ( key + " " ) ;
      flag = 1 ;
    }
  }
  if ( ( flag == 0 ) && ( maximum < mat [ 0 ] [ 0 ] ) ) {
    System . out . print ( "No unique element in the matrix" ) ;
  }
}
|||

LONGEST_SUBSEQUENCE_SUCH_THAT_DIFFERENCE_BETWEEN_ADJACENTS_IS_ONE

public static int longestSubseqWithDiffOne ( int [ ] arr , int n ) {
  int [ ] dp = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < i ;
    j ++ ) {
      if ( ( ( arr [ i ] == arr [ j ] + 1 ) || ( arr [ i ] == arr [ j ] - 1 ) ) && ( ( arr [ j ] == arr [ i ] ) || ( arr [ j ] == arr [ i ] - 1 ) ) ) {
        dp [ i ] = Math . max ( dp [ i ] , dp [ j ] + 1 ) ;
      }
    }
  }
  int result = 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( result < dp [ i ] ) && ( ( arr [ i ] == arr [ j ] ) || ( arr [ i ] == arr [ j ] - 1 ) ) ) {
      result = dp [ i ] ;
    }
  }
  return result ;
}
|||

C_PROGRAM_CONCATENATE_STRING_GIVEN_NUMBER_TIMES

public static String repeat ( String s , int n ) {
  String s1 = s ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    s += s1 ;
  }
  return s ;
}
|||

SEARCHING_FOR_PATTERNS_SET_1_NAIVE_PATTERN_SEARCHING

public static void search ( String pat , String txt ) {
  int M = pat . length ( ) ;
  int N = txt . length ( ) ;
  for ( int i = 0 ;
  i < N - M + 1 ;
  i ++ ) {
    int j = 0 ;
    while ( ( j < M ) && ( txt . charAt ( i + j ) != pat . charAt ( j ) ) ) {
      if ( ( txt . charAt ( i + j ) != pat . charAt ( j ) ) && ( txt . charAt ( i + j ) != pat . charAt ( j ) ) ) {
        break ;
      }
      j ++ ;
    }
    if ( ( j == M ) && ( txt . charAt ( i + j ) != pat . charAt ( j ) ) ) {
      System . out . println ( "Pattern found at index " + i ) ;
    }
  }
}
|||

COUNT_POSSIBLE_PATHS_SOURCE_DESTINATION_EXACTLY_K_EDGES

public static int countwalks ( int [ ] [ ] graph , int u , int v , int k ) {
  if ( ( k == 0 && u == v ) || ( k == 1 && graph [ u ] [ v ] ) ) return 1 ;
  if ( ( k == 0 && graph [ u ] [ v ] ) || ( k == 2 && graph [ u ] [ v ] ) ) return 1 ;
  if ( ( k <= 0 ) || ( k == 3 ) ) return 0 ;
  int count = 0 ;
  for ( int i = 0 ;
  i <= V ;
  i ++ ) {
    if ( ( graph [ u ] [ i ] == 1 ) && ( graph [ u ] [ i ] == 2 ) ) count += countwalks ( graph , i , v , k - 1 ) ;
  }
  return count ;
}
|||

COUNT_DIVISIBLE_PAIRS_ARRAY

public static int countDivisibles ( int [ ] arr , int n ) {
  int res = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= n ;
    j ++ ) {
      if ( ( arr [ i ] % arr [ j ] == 0 || arr [ j ] % arr [ i ] == 0 ) && ( arr [ i ] % arr [ j ] == 0 ) ) {
        res ++ ;
      }
    }
  }
  return res ;
}
|||

PROGRAM_TO_CHECK_IF_A_MATRIX_IS_SYMMETRIC

public static boolean isSymmetric ( int [ ] [ ] mat , int N ) {
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    for ( int j = 0 ;
    j < N ;
    j ++ ) {
      if ( ( mat [ i ] [ j ] != mat [ j ] [ i ] ) && ( mat [ i ] [ j ] != mat [ j ] [ i ] ) ) {
        return false ;
      }
    }
  }
  return true ;
}
|||

COUNT_PALINDROME_SUB_STRINGS_STRING

public static int CountPS ( String str , int n ) {
  int [ ] [ ] dp = new int [ n ] [ n ] ;
  for ( int y = 0 ;
  y < n ;
  y ++ ) dp [ y ] [ y ] = 0 ;
  boolean [ ] [ ] P = new boolean [ n ] [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) P [ i ] [ i ] = true ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) if ( ( str . charAt ( i ) == str . charAt ( i + 1 ) ) ) {
    P [ i ] [ i + 1 ] = true ;
    dp [ i ] [ i + 1 ] = 1 ;
  }
  for ( int gap = 2 ;
  gap < n ;
  gap ++ ) {
    for ( int i = 0 ;
    i < n - gap ;
    i ++ ) {
      int j = gap + i ;
      ;
      if ( ( str . charAt ( i ) == str . charAt ( j ) && P [ i + 1 ] [ j - 1 ] ) ) P [ i ] [ j ] = true ;
      if ( ( P [ i ] [ j ] == true ) || ( P [ i ] [ j ] == false ) ) dp [ i ] [ j ] = ( dp [ i ] [ j - 1 ] + dp [ i + 1 ] [ j ] + 1 - dp [ i + 1 ] [ j - 1 ] ) ;
      else dp [ i ] [ j ] = ( dp [ i ] [ j - 1 ] + dp [ i + 1 ] [ j ] - dp [ i + 1 ] [ j - 1 ] ) ;
    }
  }
  return dp [ 0 ] [ n - 1 ] ;
}
|||

WAYS_SUM_N_USING_ARRAY_ELEMENTS_REPETITION_ALLOWED

public static int countWays ( int [ ] arr , int m , int N ) {
  int [ ] count = new int [ N + 1 ] ;
  count [ 0 ] = 1 ;
  for ( int i = 1 ;
  i <= N ;
  i ++ ) {
    for ( int j = 0 ;
    j < m ;
    j ++ ) {
      if ( ( i >= arr [ j ] ) && ( i <= arr [ j + 1 ] ) ) {
        count [ i ] += count [ i - arr [ j ] ] ;
      }
    }
  }
  return count [ N ] ;
}
|||

MINIMUM_NUMBER_OF_OPERATIONS_TO_MOVE_ALL_UPPERCASE_CHARACTERS_BEFORE_ALL_LOWER_CASE_CHARACTERS

public static int minOperations ( String str , int n ) {
  int lastUpper = - 1 ;
  int firstLower = - 1 ;
  for ( int i = n - 1 ;
  i >= 0 ;
  i -- ) {
    if ( ( str . charAt ( i ) == ' ' ) || ( str . charAt ( i ) == '\t' ) ) {
      lastUpper = i ;
      break ;
    }
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( str . charAt ( i ) == ' ' ) || ( str . charAt ( i ) == '\t' ) ) {
      firstLower = i ;
      break ;
    }
  }
  if ( ( lastUpper == - 1 || firstLower == - 1 ) && ( str . charAt ( n - 1 ) == ' ' ) ) {
    return 0 ;
  }
  int countUpper = 0 ;
  for ( int i = firstLower ;
  i < n ;
  i ++ ) {
    if ( ( str . charAt ( i ) == ' ' ) || ( str . charAt ( i ) == '\t' ) ) {
      countUpper ++ ;
    }
  }
  int countLower = 0 ;
  for ( int i = 0 ;
  i < lastUpper ;
  i ++ ) {
    if ( ( str . charAt ( i ) == ' ' ) || ( str . charAt ( i ) == '\t' ) ) {
      countLower ++ ;
    }
  }
  return Math . min ( countLower , countUpper ) ;
}
|||

PRINT_A_GIVEN_MATRIX_IN_SPIRAL_FORM

public static void spiralPrint ( int m , int n , int [ ] [ ] a ) {
  int k = 0 ;
  int l = 0 ;
  while ( ( k < m && l < n ) || ( l < n ) ) {
    for ( int i = l ;
    i < n ;
    i ++ ) System . out . print ( a [ k ] [ i ] + " " ) ;
    k ++ ;
    for ( int i = k ;
    i < m ;
    i ++ ) System . out . print ( a [ i ] [ n - 1 ] + " " ) ;
    n -- ;
    if ( ( k < m ) || ( k > n ) ) {
      for ( int i = n - 1 ;
      i >= ( l - 1 ) ;
      i -- ) System . out . print ( a [ m - 1 ] [ i ] + " " ) ;
      m -- ;
    }
    if ( ( l < n ) || ( l > m ) ) {
      for ( int i = m - 1 ;
      i >= k - 1 ;
      i -- ) System . out . print ( a [ i ] [ l ] + " " ) ;
      l ++ ;
    }
  }
}
|||

FIND_DISTINCT_INTEGERS_FOR_A_TRIPLET_WITH_GIVEN_PRODUCT

public static void findTriplets ( int x ) {
  int [ ] fact = new int [ 2 ] ;
  ;
  HashSet factors = new HashSet ( ) ;
  for ( int i = 2 ;
  i <= Integer . MAX_VALUE ;
  i ++ ) {
    if ( ( x % i == 0 ) && ( x / i != 0 ) ) {
      fact [ i ] = i ;
      ;
      if ( ( x / i != i ) && ( x / i != 1 ) ) {
        fact [ i ] = x / i ;
        ;
      }
      factors . add ( i ) ;
      ;
      factors . add ( x / i ) ;
      ;
    }
  }
  boolean found = false ;
  int k = fact . length ;
  for ( int i = 0 ;
  i < k ;
  i ++ ) {
    int a = fact [ i ] ;
    for ( int j = 0 ;
    j < k ;
    j ++ ) {
      int b = fact [ j ] ;
      if ( ( ( a != b ) && ( x % ( a * b ) == 0 ) && ( x / ( a * b ) != a ) && ( x / ( a * b ) != b ) && ( x / ( a * b ) != 1 ) ) ) {
        System . out . println ( a + " " + b + " " + x / ( a * b ) ) ;
        ;
        found = true ;
        break ;
      }
    }
    if ( ( found ) && ( x % ( a * b ) == 0 ) && ( x / ( a * b ) != 0 ) ) {
      break ;
    }
  }
  if ( ( ! found ) && ( x % ( a * b ) == 0 ) && ( x / ( a * b ) != 0 ) ) {
    System . out . println ( "-1" ) ;
    ;
  }
}
|||

SUM_TWO_LARGE_NUMBERS_1

public static String findSum ( String str1 , String str2 ) {
  if ( str1 . length ( ) > str2 . length ( ) ) {
    String temp = str1 ;
    str1 = str2 ;
    str2 = temp ;
  }
  String str3 = "" ;
  int n1 = str1 . length ( ) ;
  int n2 = str2 . length ( ) ;
  int diff = n2 - n1 ;
  int carry = 0 ;
  for ( int i = n1 - 1 ;
  i >= 0 ;
  i -- ) {
    int sum = ( ( Character . digit ( str1 . charAt ( i ) , 16 ) - '0' ) + ( Character . digit ( str2 . charAt ( i + diff ) , 16 ) - '0' ) ) + carry ;
    str3 = str3 + Integer . toString ( sum % 10 , 16 ) ;
    carry = sum / 10 ;
  }
  for ( int i = n2 - n1 - 1 ;
  i >= 0 ;
  i -- ) {
    int sum = ( ( Character . digit ( str2 . charAt ( i ) , 16 ) - '0' ) + carry ) ;
    str3 = str3 + Integer . toString ( sum % 10 , 16 ) ;
    carry = sum / 10 ;
  }
  if ( ( carry > 0 ) && ( carry < 10 ) ) {
    str3 = str3 + Integer . toString ( carry + '0' , 16 ) ;
  }
  str3 = str3 . substring ( 0 , str3 . length ( ) - 1 ) ;
  return str3 ;
}
|||

COCKTAIL_SORT

public static void cocktailSort ( int [ ] a ) {
  int n = a . length ;
  boolean swapped = true ;
  int start = 0 ;
  int end = n - 1 ;
  while ( ( swapped == true ) && ( start < end ) ) {
    swapped = false ;
    for ( int i = start ;
    i < end ;
    i ++ ) {
      if ( ( a [ i ] > a [ i + 1 ] ) && ( a [ i + 1 ] < a [ i ] ) ) {
        a [ i ] = a [ i + 1 ] ;
        a [ i + 1 ] = a [ i ] ;
        swapped = true ;
      }
    }
    if ( ( swapped == false ) && ( end < start ) ) break ;
    swapped = false ;
    end = end - 1 ;
    for ( int i = end - 1 ;
    i >= start ;
    i -- ) {
      if ( ( a [ i ] > a [ i + 1 ] ) && ( a [ i + 1 ] < a [ i ] ) ) {
        a [ i ] = a [ i + 1 ] ;
        a [ i + 1 ] = a [ i ] ;
        swapped = true ;
      }
    }
    start = start + 1 ;
  }
}
|||

COUNT_DERANGEMENTS_PERMUTATION_SUCH_THAT_NO_ELEMENT_APPEARS_IN_ITS_ORIGINAL_POSITION_1

public static int countDer ( int n ) {
  int [ ] der = new int [ n + 1 ] ;
  der [ 0 ] = 1 ;
  der [ 1 ] = 0 ;
  der [ 2 ] = 1 ;
  for ( int i = 3 ;
  i <= n ;
  i ++ ) {
    der [ i ] = ( i - 1 ) * ( der [ i - 1 ] + der [ i - 2 ] ) ;
  }
  return der [ n ] ;
}
|||

MAXIMUM_PRODUCT_SUBARRAY_ADDED_NEGATIVE_PRODUCT_CASE

public static int findMaxProduct ( int [ ] arr , int n ) {
  int ans = - Integer . MAX_VALUE ;
  int maxval = 1 ;
  int minval = 1 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( arr [ i ] > 0 ) {
      maxval = maxval * arr [ i ] ;
      minval = Math . min ( 1 , minval * arr [ i ] ) ;
    }
    else if ( arr [ i ] == 0 ) {
      minval = 1 ;
      maxval = 0 ;
    }
    else if ( arr [ i ] < 0 ) {
      int prevMax = maxval ;
      maxval = minval * arr [ i ] ;
      minval = prevMax * arr [ i ] ;
    }
    ans = Math . max ( ans , maxval ) ;
    if ( maxval <= 0 ) {
      maxval = 1 ;
    }
  }
  return ans ;
}
|||

REARRANGE_ARRAY_SUCH_THAT_EVEN_POSITIONED_ARE_GREATER_THAN_ODD

public static void assign ( int [ ] a , int n ) {
  Arrays . sort ( a ) ;
  int [ ] ans = new int [ n ] ;
  int p = 0 ;
  int q = n - 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( i + 1 ) % 2 == 0 ) {
      ans [ i ] = a [ q ] ;
      q = q - 1 ;
    }
    else {
      ans [ i ] = a [ p ] ;
      p = p + 1 ;
    }
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    System . out . print ( ans [ i ] + " " ) ;
  }
}
|||

FRIENDS_PAIRING_PROBLEM

public static int countFriendsPairings ( int n ) {
  int [ ] dp = new int [ n + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( i <= 2 ) && ( i > 0 ) ) {
      dp [ i ] = i ;
    }
    else {
      dp [ i ] = dp [ i - 1 ] + ( i - 1 ) * dp [ i - 2 ] ;
    }
  }
  return dp [ n ] ;
}
|||

PRIME_NUMBERS

public static boolean isPrime ( int n ) {
  if ( ( n <= 1 ) || ( n > n ) ) return false ;
  for ( int i = 2 ;
  i < n ;
  i ++ ) if ( ( n % i == 0 ) || ( n % i == 1 ) ) return false ;
  return true ;
}
|||

PROBABILITY_REACHING_POINT_2_3_STEPS_TIME

public static int findProb ( int N , int P ) {
  int [ ] dp = new int [ n + 1 ] ;
  dp [ 0 ] = 1 ;
  dp [ 1 ] = 0 ;
  dp [ 2 ] = P ;
  dp [ 3 ] = 1 - P ;
  for ( int i = 4 ;
  i <= N ;
  i ++ ) {
    dp [ i ] = ( P ) * dp [ i - 2 ] + ( 1 - P ) * dp [ i - 3 ] ;
  }
  return dp [ N ] ;
}
|||

SMALLEST_OF_THREE_INTEGERS_WITHOUT_COMPARISON_OPERATORS_1

public static int smallest ( int x , int y , int z ) {
  if ( ( ! ( y / x ) ) && ( ! ( y / z ) ) ) {
    return y == 0 ? z : y ;
  }
  return x == 0 ? z : x ;
}
|||

COMMON_ELEMENTS_IN_ALL_ROWS_OF_A_GIVEN_MATRIX

public static void printCommonElements ( int [ ] [ ] mat ) {
  Map < Integer , Integer > mp = Maps . newHashMap ( ) ;
  for ( int j = 0 ;
  j < N ;
  j ++ ) mp . put ( mat [ 0 ] [ j ] , 1 ) ;
  for ( int i = 1 ;
  i < M ;
  i ++ ) for ( int j = 0 ;
  j < N ;
  j ++ ) if ( ( mat [ i ] [ j ] < mp . keySet ( ) . size ( ) && mp . get ( mat [ i ] [ j ] ) == i ) || ( mat [ i ] [ j ] < mp . get ( mat [ i ] [ j ] ) + 1 && mp . get ( mat [ i ] [ j ] ) == i ) ) {
    mp . put ( mat [ i ] [ j ] , i + 1 ) ;
    if ( i == M - 1 ) System . out . print ( mat [ i ] [ j ] + " " ) ;
  }
}
|||

DETECTING_NEGATIVE_CYCLE_USING_FLOYD_WARSHALL

public static boolean negCyclefloydWarshall ( int [ ] [ ] graph ) {
  int [ ] [ ] dist = new int [ V + 1 ] [ V + 1 ] ;
  for ( int i = 0 ;
  i < V ;
  i ++ ) {
    for ( int j = 0 ;
    j < V ;
    j ++ ) {
      dist [ i ] [ j ] = graph [ i ] [ j ] ;
    }
  }
  for ( int k = 0 ;
  k < V ;
  k ++ ) {
    for ( int i = 0 ;
    i < V ;
    i ++ ) {
      for ( int j = 0 ;
      j < V ;
      j ++ ) {
        if ( ( dist [ i ] [ k ] + dist [ k ] [ j ] < dist [ i ] [ j ] ) && ( dist [ i ] [ j ] + dist [ k ] [ j ] < dist [ i ] [ j ] ) ) {
          dist [ i ] [ j ] = dist [ i ] [ k ] + dist [ k ] [ j ] ;
        }
      }
    }
  }
  for ( int i = 0 ;
  i < V ;
  i ++ ) {
    if ( ( dist [ i ] [ i ] < 0 ) && ( dist [ i ] [ i ] < dist [ V - 1 ] ) ) {
      return true ;
    }
  }
  return false ;
}
|||

PROGRAM_SORT_STRING_DESCENDING_ORDER

public static void sortString ( String str ) {
  int charCount [ ] = new int [ MAX_CHAR ] ;
  ;
  for ( int i = 0 ;
  i < str . length ( ) ;
  i ++ ) charCount [ ( int ) str . charAt ( i ) - 'a' ] ++ ;
  ;
  for ( int i = MAX_CHAR - 1 ;
  i >= 0 ;
  i -- ) {
    for ( int j = 0 ;
    j < charCount [ i ] ;
    j ++ ) System . out . print ( ( char ) ( 97 + i ) ) ;
    ;
  }
}
|||

COUNT_PAIRS_WITH_GIVEN_SUM

public static int getPairsCount ( int [ ] arr , int n , int sum ) {
  int count = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= n ;
    j ++ ) {
      if ( arr [ i ] + arr [ j ] == sum ) {
        count ++ ;
      }
    }
  }
  return count ;
}
|||

SUM_SERIES_12_32_52_2N_12_1

static int sumOfSeries ( int n ) {
  return ( int ) ( ( n * ( 2 * n - 1 ) * ( 2 * n + 1 ) ) / 3 ) ;
}
|||

MAXIMUM_DIFFERENCE_BETWEEN_FREQUENCY_OF_TWO_ELEMENTS_SUCH_THAT_ELEMENT_HAVING_GREATER_FREQUENCY_IS_ALSO_GREATER

public static int maxdiff ( int arr [ ] , int n ) {
  int freq [ ] = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) freq [ arr [ i ] ] ++ ;
  int ans = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( freq [ arr [ i ] ] > freq [ arr [ j ] ] && arr [ i ] > arr [ j ] ) ans = Math . max ( ans , freq [ arr [ i ] ] - freq [ arr [ j ] ] ) ;
      else if ( freq [ arr [ i ] ] < freq [ arr [ j ] ] && arr [ i ] < arr [ j ] ) ans = Math . max ( ans , freq [ arr [ j ] ] - freq [ arr [ i ] ] ) ;
    }
  }
  return ans ;
}
|||

SHIFT_MATRIX_ELEMENTS_K

public static void shiftMatrixByK ( int [ ] [ ] mat , int k ) {
  if ( ( k > N ) || ( k < 0 ) ) {
    System . out . println ( "shifting is" + " not possible" ) ;
    return ;
  }
  int j = 0 ;
  while ( ( j < N ) && ( j < k ) ) {
    for ( int i = k ;
    i < N ;
    i ++ ) {
      System . out . print ( "{}
 " ) ;
    }
    for ( int i = 0 ;
    i <= k ;
    i ++ ) {
      System . out . print ( "{}
 " ) ;
    }
    System . out . println ( "" ) ;
    j = j + 1 ;
  }
}
|||

MAXIMUM_AND_MINIMUM_IN_A_SQUARE_MATRIX

public static void MAXMIN ( int [ ] [ ] arr , int n ) {
  int MIN = 10 * 9 ;
  int MAX = - 10 * 9 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n / 2 + 1 ;
    j ++ ) {
      if ( ( arr [ i ] [ j ] > arr [ i ] [ n - j - 1 ] ) && ( arr [ i ] [ j ] < arr [ i ] [ n - j - 1 ] ) ) {
        if ( ( MIN > arr [ i ] [ n - j - 1 ] ) && ( arr [ i ] [ j ] > arr [ i ] [ n - j - 1 ] ) ) {
          MIN = arr [ i ] [ n - j - 1 ] ;
        }
        if ( ( MAX < arr [ i ] [ j ] ) && ( arr [ i ] [ j ] > arr [ i ] [ n - j - 1 ] ) ) {
          MAX = arr [ i ] [ n - j - 1 ] ;
        }
      }
      else {
        if ( ( MIN > arr [ i ] [ j ] ) && ( arr [ i ] [ j ] < arr [ i ] [ n - j - 1 ] ) ) {
          MIN = arr [ i ] [ j ] ;
        }
        if ( ( MAX < arr [ i ] [ n - j - 1 ] ) && ( arr [ i ] [ j ] > arr [ i ] [ n - j - 1 ] ) ) {
          MAX = arr [ i ] [ n - j - 1 ] ;
        }
      }
    }
  }
  System . out . println ( "MAXimum =" + MAX + ", MINimum =" + MIN ) ;
}
|||

FIND_PAIR_WITH_GREATEST_PRODUCT_IN_ARRAY_1

public static int findGreatest ( int [ ] arr , int n ) {
  Map < Integer , Integer > m = new HashMap < Integer , Integer > ( ) ;
  for ( int i : arr ) m . put ( i , m . get ( i ) + 1 ) ;
  Arrays . sort ( arr ) ;
  for ( int i = n - 1 ;
  i > 0 ;
  i -- ) {
    int j = 0 ;
    while ( ( j < i ) && arr [ j ] <= Math . sqrt ( arr [ i ] ) ) {
      if ( ( arr [ i ] % arr [ j ] == 0 ) && ( m . get ( i ) > 0 ) ) {
        int result = arr [ i ] / arr [ j ] ;
        if ( ( result != arr [ j ] && ( result < m . keySet ( ) . size ( ) ) ) && m . get ( result ) > 0 ) {
          return arr [ i ] ;
        }
        else if ( ( result == arr [ j ] && ( result < m . keySet ( ) . size ( ) ) ) && m . get ( result ) > 1 ) {
          return arr [ i ] ;
        }
      }
      j ++ ;
    }
  }
  return - 1 ;
}
|||

0_1_KNAPSACK_PROBLEM_DP_10_1

public static int knapSack ( int W , int [ ] wt , int [ ] val , int n ) {
  int [ ] [ ] K = new int [ W + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int w = 0 ;
    w < W + 1 ;
    w ++ ) {
      if ( i == 0 || w == 0 ) {
        K [ i ] [ w ] = 0 ;
      }
      else if ( wt [ i - 1 ] <= w ) {
        K [ i ] [ w ] = Math . max ( val [ i - 1 ] + K [ i - 1 ] [ w - wt [ i - 1 ] ] , K [ i - 1 ] [ w ] ) ;
      }
      else {
        K [ i ] [ w ] = K [ i - 1 ] [ w ] ;
      }
    }
  }
  return K [ n ] [ W ] ;
}
|||

PROGRAM_DECIMAL_OCTAL_CONVERSION

public static void decToOctal ( int n ) {
  int [ ] octalNum = new int [ 100 ] ;
  ;
  int i = 0 ;
  ;
  while ( ( n != 0 ) && ( n % 8 == 0 ) ) {
    octalNum [ i ] = n % 8 ;
    ;
    n = ( int ) ( n / 8 ) ;
    ;
    i ++ ;
  };
  for ( int j = i - 1 ;
  j >= 0 ;
  j -- ) {
    System . out . print ( octalNum [ j ] + " " ) ;
    ;
  };
}
|||

SUBSEQUENCES_SIZE_THREE_ARRAY_WHOSE_SUM_DIVISIBLE_M_1

public static int countSubSeq ( int [ ] A , int N , int M ) {
  int ans = 0 ;
  int [ ] h = new int [ M ] ;
  for ( int i = 0 ;
  i <= N ;
  i ++ ) {
    A [ i ] = A [ i ] % M ;
    h [ A [ i ] ] = h [ A [ i ] ] + 1 ;
  }
  for ( int i = 0 ;
  i <= M ;
  i ++ ) {
    for ( int j = i ;
    j <= M ;
    j ++ ) {
      int rem = ( M - ( i + j ) % M ) % M ;
      if ( ( rem < j ) && ( rem == j ) ) {
        ans = ans + h [ i ] * ( h [ i ] - 1 ) * ( h [ i ] - 2 ) / 6 ;
      }
      else if ( ( i == j ) && ( rem == j ) ) {
        ans = ans + ( h [ i ] * ( h [ i ] - 1 ) * h [ rem ] / 2 ) ;
      }
      else if ( ( i == rem ) && ( j == j ) ) {
        ans = ans + h [ i ] * ( h [ i ] - 1 ) * h [ j ] / 2 ;
      }
      else if ( ( rem == j ) && ( i == j ) ) {
        ans = ans + h [ j ] * ( h [ j ] - 1 ) * h [ i ] / 2 ;
      }
      else {
        ans = ans + h [ i ] * h [ j ] * h [ rem ] ;
      }
    }
    return ans ;
  }
}
|||

COUNT_FIBONACCI_NUMBERS_GIVEN_RANGE_LOG_TIME

public static int countFibs ( int low , int high ) {
  int f1 = 0 , f2 = 1 , f3 = 1 ;
  int result = 0 ;
  while ( ( f1 <= high ) && ( f1 >= low ) ) {
    if ( ( f1 >= low ) && ( f1 <= high ) ) {
      result ++ ;
    }
    f1 = f2 ;
    f2 = f3 ;
    f3 = f1 + f2 ;
  }
  return result ;
}
|||

FIND_WHETHER_A_GIVEN_NUMBER_IS_A_POWER_OF_4_OR_NOT_1

public static boolean isPowerOfFour ( int n ) {
  int count = 0 ;
  if ( ( n > 0 ) && ( ! ( n & ( n - 1 ) ) ) ) {
    while ( ( n > 1 ) ) {
      n >>= 1 ;
      count ++ ;
    }
    if ( ( count % 2 == 0 ) && ( n > 0 ) ) {
      return true ;
    }
    else {
      return false ;
    }
  }
  return false ;
}
|||

FIND_SUM_EVEN_FACTORS_NUMBER

public static int sumofFactors ( int n ) {
  if ( ( n % 2 != 0 ) && ( n % 3 == 0 ) ) return 0 ;
  int res = 1 ;
  for ( int i = 2 ;
  i <= ( int ) ( Math . sqrt ( n ) ) ;
  i ++ ) {
    int count = 0 ;
    int currSum = 1 ;
    int currTerm = 1 ;
    while ( ( n % i == 0 ) && ( n % 3 == 0 ) ) {
      count = count + 1 ;
      n = n / i ;
      if ( ( i == 2 && count == 1 ) || ( i == 3 && count == 2 ) ) currSum = 0 ;
      currTerm = currTerm * i ;
      currSum = currSum + currTerm ;
    }
    res = res * currSum ;
  }
  if ( ( n >= 2 ) && ( n <= 3 ) ) res = res * ( 1 + n ) ;
  return res ;
}
|||

FIND_SUM_NON_REPEATING_DISTINCT_ELEMENTS_ARRAY

public static int findSum ( int [ ] arr , int n ) {
  Set < Integer > s = new HashSet < Integer > ( ) ;
  int sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] != 0 ) {
      s . add ( arr [ i ] ) ;
    }
  }
  for ( int i : s ) {
    sum = sum + i ;
  }
  return sum ;
}
|||

DYNAMIC_PROGRAMMING_SET_17_PALINDROME_PARTITIONING_1

public static int minPalPartion ( String str1 ) {
  int n = str1 . length ( ) ;
  ;
  int [ ] [ ] C = new int [ n + 1 ] [ n + 1 ] ;
  ;
  boolean [ ] [ ] P = new boolean [ n + 1 ] [ n + 1 ] ;
  ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) P [ i ] [ i ] = true ;
  ;
  for ( int L = 2 ;
  L <= n ;
  L ++ ) {
    for ( int i = 0 ;
    i < n - L + 1 ;
    i ++ ) {
      int j = i + L - 1 ;
      ;
      if ( ( L == 2 ) && ( str1 . charAt ( i ) == str1 . charAt ( j ) ) ) P [ i ] [ j ] = ( str1 . charAt ( i ) == str1 . charAt ( j ) ) ;
      ;
      else P [ i ] [ j ] = ( ( str1 . charAt ( i ) == str1 . charAt ( j ) ) && P [ i + 1 ] [ j - 1 ] ) ;
      ;
    }
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( P [ 0 ] [ i ] == true ) && ( C [ i ] [ 0 ] == true ) ) C [ i ] [ 0 ] = 0 ;
    else {
      C [ i ] = Integer . MAX_VALUE ;
      ;
      for ( int j = 0 ;
      j < i ;
      j ++ ) {
        if ( ( P [ j + 1 ] [ i ] == true ) && ( 1 + C [ j ] [ j ] < C [ i ] [ j ] ) ) C [ i ] [ j ] = 1 + C [ j ] ;
        ;
      }
    }
  }
  return C [ n - 1 ] [ 0 ] ;
}
|||

MINIMUM_POSITIVE_POINTS_TO_REACH_DESTINATION

public static int minInitialPoints ( int [ ] [ ] points ) {
  int [ ] [ ] dp = new int [ C + 1 ] [ R + 1 ] ;
  for ( int y = 0 ;
  y < R + 1 ;
  y ++ ) {
    dp [ y ] = new int [ R + 1 ] ;
  }
  int m = R , n = C ;
  if ( points [ m - 1 ] [ n - 1 ] > 0 ) {
    dp [ m - 1 ] [ n - 1 ] = 1 ;
  }
  else {
    dp [ m - 1 ] [ n - 1 ] = Math . abs ( points [ m - 1 ] [ n - 1 ] ) + 1 ;
  }
  for ( int i = m - 2 ;
  i >= 0 ;
  i -- ) {
    dp [ i ] [ n - 1 ] = Math . max ( dp [ i + 1 ] [ n - 1 ] - points [ i ] [ n - 1 ] , 1 ) ;
  }
  for ( int i = 2 ;
  i >= 0 ;
  i -- ) {
    dp [ m - 1 ] [ i ] = Math . max ( dp [ m - 1 ] [ i + 1 ] - points [ m - 1 ] [ i ] , 1 ) ;
  }
  for ( int i = m - 2 ;
  i >= 0 ;
  i -- ) {
    for ( int j = n - 2 ;
    j >= 0 ;
    j -- ) {
      int minPointsOnExit = Math . min ( dp [ i + 1 ] [ j ] , dp [ i ] [ j + 1 ] ) ;
      dp [ i ] [ j ] = Math . max ( minPointsOnExit - points [ i ] [ j ] , 1 ) ;
    }
  }
  return dp [ 0 ] [ 0 ] ;
}
|||

COUNT_OF_PAIRS_SATISFYING_THE_GIVEN_CONDITION

public static int countPair ( int a , int b ) {
  String s = Integer . toString ( b ) ;
  int i = 0 ;
  while ( i < ( s . length ( ) ) ) {
    if ( ( s . charAt ( i ) != '9' ) && ( s . charAt ( i ) != '.' ) ) break ;
    i ++ ;
  }
  int result ;
  if ( ( i == s . length ( ) ) && ( a == 0 ) ) result = a * s . length ( ) ;
  else result = a * ( s . length ( ) - 1 ) ;
  return result ;
}
|||

SURVIVAL

public static void survival ( int S , int N , int M ) {
  if ( ( ( ( N * 6 ) < ( M * 7 ) && S > 6 ) || M > N ) ) {
    System . out . println ( "No" ) ;
  }
  else {
    int days = ( M * S ) / N ;
    if ( ( ( ( M * S ) % N ) != 0 ) && ( ( ( M * S ) % N ) != 0 ) ) days ++ ;
    System . out . print ( "Yes " ) ;
    System . out . println ( days ) ;
  }
}
|||

INTERLEAVE_FIRST_HALF_QUEUE_SECOND_HALF

public static void interLeaveQueue ( Queue q ) {
  if ( ( q . qsize ( ) % 2 != 0 ) && ( q . qsize ( ) > 1 ) ) System . out . println ( "Input even number of integers." ) ;
  Stack < Integer > s = new Stack < Integer > ( ) ;
  int halfSize = ( int ) ( q . qsize ( ) / 2 ) ;
  for ( int i = 0 ;
  i < halfSize ;
  i ++ ) {
    s . push ( q . queue . get ( ) ) ;
    q . get ( ) ;
  }
  while ( s . size ( ) != 0 ) {
    q . put ( s . pop ( ) ) ;
    s . pop ( ) ;
  }
  for ( int i = 0 ;
  i < halfSize ;
  i ++ ) {
    q . put ( q . queue . get ( ) ) ;
    q . get ( ) ;
  }
  for ( int i = 0 ;
  i < halfSize ;
  i ++ ) {
    s . push ( q . queue . get ( ) ) ;
    q . get ( ) ;
  }
  while ( s . size ( ) != 0 ) {
    q . put ( s . pop ( ) ) ;
    s . pop ( ) ;
    q . put ( q . queue . get ( ) ) ;
    q . get ( ) ;
  }
}
|||

INTEGER_POSITIVE_VALUE_POSITIVE_NEGATIVE_VALUE_ARRAY_1

public static int findInteger ( int [ ] arr , int n ) {
  int neg = 0 ;
  int pos = 0 ;
  int sum = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    sum += arr [ i ] ;
    if ( ( arr [ i ] < 0 ) && ( arr [ i ] > 0 ) ) neg ++ ;
    else pos ++ ;
  }
  return ( sum / Math . abs ( neg - pos ) ) ;
}
|||

FIND_SUM_EVEN_INDEX_BINOMIAL_COEFFICIENTS

public static int evenSum ( int n ) {
  int [ ] [ ] C = new int [ n + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= Math . min ( i , n + 1 ) ;
    j ++ ) {
      if ( j == 0 || j == i ) {
        C [ i ] [ j ] = 1 ;
      }
      else {
        C [ i ] [ j ] = C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ] ;
      }
    }
  }
  int sum = 0 ;
  ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( n % 2 == 0 ) {
      sum = sum + C [ n ] [ i ] ;
    }
  }
  return sum ;
}
|||

DELANNOY_NUMBER

public static int dealnnoy ( int n , int m ) {
  if ( ( m == 0 || n == 0 ) && ( m > 0 ) ) return 1 ;
  return dealnnoy ( m - 1 , n ) + dealnnoy ( m - 1 , n - 1 ) + dealnnoy ( m , n - 1 ) ;
}
|||

FIND_THE_LARGEST_SUBARRAY_WITH_0_SUM

public static int maxLen ( int [ ] arr ) {
  int maxLen = 0 ;
  for ( int i = 0 ;
  i < arr . length ;
  i ++ ) {
    int currSum = 0 ;
    for ( int j = i ;
    j < arr . length ;
    j ++ ) {
      currSum += arr [ j ] ;
      if ( currSum == 0 ) {
        maxLen = Math . max ( maxLen , j - i + 1 ) ;
      }
    }
  }
  return maxLen ;
}
|||

NEXT_POWER_OF_2

public static int nextPowerOf2 ( int n ) {
  int count = 0 ;
  ;
  if ( ( n > 0 ) && ! ( n & ( n - 1 ) ) ) return n ;
  while ( ( n != 0 ) && ( n != 1 ) ) {
    n >>>= 1 ;
    count ++ ;
  }
  return 1 << count ;
  ;
}
|||

LONGEST_GEOMETRIC_PROGRESSION

public static int lenOfLongestGP ( int [ ] sett , int n ) {
  if ( n < 2 ) return n ;
  if ( n == 2 ) return ( sett [ 1 ] % sett [ 0 ] == 0 ? 0 : 1 ) ;
  Arrays . sort ( sett ) ;
  int [ ] [ ] L = new int [ n ] [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) L [ i ] [ i ] = 0 ;
  int llgp = 1 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( sett [ n - 1 ] % sett [ i ] == 0 ) L [ i ] [ n - 1 ] = 2 ;
    else L [ i ] [ n - 1 ] = 1 ;
  }
  for ( int j = n - 2 ;
  j > 0 ;
  j -- ) {
    int i = j - 1 ;
    int k = j + 1 ;
    while ( i >= 0 && k <= n - 1 ) {
      if ( sett [ i ] * sett [ k ] < sett [ j ] * sett [ j ] ) k ++ ;
      else if ( sett [ i ] * sett [ k ] > sett [ j ] * sett [ j ] ) {
        if ( sett [ j ] % sett [ i ] == 0 ) L [ i ] [ j ] = 2 ;
        else L [ i ] [ j ] = 1 ;
        i -- ;
      }
      else {
        L [ i ] [ j ] = L [ j ] [ k ] + 1 ;
        if ( L [ i ] [ j ] > llgp ) llgp = L [ i ] [ j ] ;
        i -- ;
        k ++ ;
      }
    }
    while ( i >= 0 ) {
      if ( sett [ j ] % sett [ i ] == 0 ) L [ i ] [ j ] = 2 ;
      else L [ i ] [ j ] = 1 ;
      i -- ;
    }
  }
  return llgp ;
}
|||

DYNAMIC_PROGRAMMING_SET_6_MIN_COST_PATH

public static int minCost ( int [ ] cost , int m , int n ) {
  int [ ] [ ] tc = new int [ C ] [ R ] ;
  for ( int i = 0 ;
  i < R ;
  i ++ ) tc [ i ] [ i ] = new int [ C ] ;
  tc [ 0 ] [ 0 ] = cost [ 0 ] [ 0 ] ;
  for ( int i = 1 ;
  i <= m ;
  i ++ ) tc [ i ] [ 0 ] = tc [ i - 1 ] [ 0 ] + cost [ i ] [ 0 ] ;
  for ( int j = 1 ;
  j <= n ;
  j ++ ) tc [ 0 ] [ j ] = tc [ 0 ] [ j - 1 ] + cost [ 0 ] [ j ] ;
  for ( int i = 1 ;
  i <= m ;
  i ++ ) {
    for ( int j = 1 ;
    j <= n ;
    j ++ ) tc [ i ] [ j ] = Math . min ( tc [ i - 1 ] [ j - 1 ] , tc [ i - 1 ] [ j ] , tc [ i ] [ j - 1 ] ) + cost [ i ] [ j ] ;
  }
  return tc [ m ] [ n ] ;
}
|||

PROGRAM_DISTANCE_TWO_POINTS_EARTH

public static double distance ( double lat1 , double lat2 , double lon1 , double lon2 ) {
  lon1 = Math . toRadians ( lon1 ) ;
  lon2 = Math . toRadians ( lon2 ) ;
  lat1 = Math . toRadians ( lat1 ) ;
  lat2 = Math . toRadians ( lat2 ) ;
  double dlon = lon2 - lon1 ;
  double dlat = lat2 - lat1 ;
  double a = Math . sin ( dlat / 2 ) * ( lat1 - lat2 ) + Math . cos ( lat1 ) * Math . cos ( lat2 ) * Math . sin ( dlon / 2 ) * ( lat2 - lat1 ) ;
  double c = 2 * Math . asin ( Math . sqrt ( a ) ) ;
  double r = 6371 ;
  return ( c * r ) ;
}
|||

BIN_PACKING_PROBLEM_MINIMIZE_NUMBER_OF_USED_BINS

public static int nextfit ( int [ ] weight , int c ) {
  int res = 0 ;
  int rem = c ;
  for ( ;
  ;
  ) {
    if ( rem >= weight [ weight . length - 1 ] ) {
      rem = rem - weight [ weight . length - 1 ] ;
    }
    else {
      res ++ ;
      rem = c - weight [ weight . length - 1 ] ;
    }
  }
  return res ;
}
|||

FIND_SUBARRAY_WITH_GIVEN_SUM_1

public static int subArraySum ( int [ ] arr , int n , int sum ) {
  int currSum = arr [ 0 ] ;
  int start = 0 ;
  int i = 1 ;
  while ( i <= n ) {
    while ( currSum > sum && start < i - 1 ) {
      currSum = currSum - arr [ start ] ;
      start ++ ;
    }
    if ( currSum == sum ) {
      System . out . println ( "Sum found between indexes" ) ;
      System . out . println ( start + " and " + i - 1 ) ;
      return 1 ;
    }
    if ( i < n ) currSum = currSum + arr [ i ] ;
    i ++ ;
  }
  System . out . println ( "No subarray found" ) ;
  return 0 ;
}
|||

SPACE_OPTIMIZED_DP_SOLUTION_0_1_KNAPSACK_PROBLEM_1

public static int KnapSack ( int [ ] val , int [ ] wt , int n , int W ) {
  int [ ] dp = new int [ W + 1 ] ;
  ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = W ;
    j > wt [ i ] ;
    j -- ) {
      dp [ j ] = Math . max ( dp [ j ] , val [ i ] + dp [ j - wt [ i ] ] ) ;
      ;
    }
  }
  return dp [ W ] ;
}
|||

FIND_VALUE_OF_Y_MOD_2_RAISED_TO_POWER_X

public static double yMod ( double y , double x ) {
  return ( y % Math . pow ( 2 , x ) ) ;
}
|||

SUM_SERIES_23_45_67_89_UPTO_N_TERMS

public static double seriesSum ( int n ) {
  int i = 1 ;
  double res = 0.0 ;
  ;
  boolean sign = true ;
  while ( ( n > 0 ) && ( i < n ) ) {
    n = n - 1 ;
    if ( ( sign ) || ( i < 0 ) ) {
      sign = false ;
      res = res + ( i + 1 ) / ( i + 2 ) ;
      i = i + 2 ;
    }
    else {
      sign = true ;
      res = res - ( i + 1 ) / ( i + 2 ) ;
      i = i + 2 ;
    }
  }
  return res ;
}
|||

LENGTH_LONGEST_STRICT_BITONIC_SUBSEQUENCE

public static int longLenStrictBitonicSub ( int [ ] arr , int n ) {
  Map < Integer , Integer > inc = Maps . newHashMap ( ) , dcr = Maps . newHashMap ( ) ;
  int [ ] lenInc = new int [ n ] , lenDcr = new int [ n ] ;
  int longLen = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int len = 0 ;
    if ( inc . get ( arr [ i ] - 1 ) . contains ( inc . get ( arr [ i ] - 1 ) ) ) len = inc . get ( arr [ i ] - 1 ) ;
    inc . put ( arr [ i ] , lenInc [ i ] = len + 1 ) ;
  }
  for ( int i = n - 1 ;
  i >= 0 ;
  i -- ) {
    int len = 0 ;
    if ( dcr . get ( arr [ i ] - 1 ) . contains ( dcr . get ( arr [ i ] - 1 ) ) ) len = dcr . get ( arr [ i ] - 1 ) ;
    dcr . put ( arr [ i ] , lenDcr [ i ] = len + 1 ) ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( longLen < ( lenInc [ i ] + lenDcr [ i ] - 1 ) ) longLen = lenInc [ i ] + lenDcr [ i ] - 1 ;
  }
  return longLen ;
}
|||

MAXIMUM_DISTANCE_TWO_OCCURRENCES_ELEMENT_ARRAY

public static int maxDistance ( int [ ] arr , int n ) {
  HashMap < Integer , Integer > mp = new HashMap < Integer , Integer > ( ) ;
  int maxMap = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] != null ) {
      mp . put ( arr [ i ] , i ) ;
    }
    else {
      maxMap = Math . max ( maxMap , i - mp . get ( arr [ i ] ) ) ;
    }
  }
  return maxMap ;
}
|||

FIND_RECTANGLE_BINARY_MATRIX_CORNERS_1_1

public static boolean isRectangle ( int [ ] [ ] matrix ) {
  int rows = matrix . length ;
  if ( ( rows == 0 ) || ( rows == 1 ) ) return false ;
  int columns = matrix [ 0 ] . length ;
  Set < Integer > table = new HashSet < Integer > ( ) ;
  for ( int i = 0 ;
  i < rows ;
  i ++ ) {
    for ( int j = 0 ;
    j < columns - 1 ;
    j ++ ) {
      for ( int k = j + 1 ;
      k < columns ;
      k ++ ) {
        if ( ( matrix [ i ] [ j ] == 1 && matrix [ i ] [ k ] == 1 ) || ( matrix [ i ] [ j ] == 0 && matrix [ i ] [ k ] == 0 ) ) {
          if ( ( j < table . size ( ) && k < table . size ( ) ) || ( k < table . size ( ) && j < table . size ( ) ) ) return true ;
          if ( j != 0 ) table . add ( j ) ;
          if ( k != 0 ) table . add ( k ) ;
          table . add ( j ) ;
          table . add ( k ) ;
        }
      }
    }
  }
  return false ;
}
|||

COUNT_MINIMUM_NUMBER_SUBSETS_SUBSEQUENCES_CONSECUTIVE_NUMBERS

public static int numofSubset ( int [ ] arr , int n ) {
  int [ ] x = new int [ n ] ;
  Arrays . fill ( x , 0 ) ;
  int count = 1 ;
  for ( int i = 0 ;
  i <= n - 1 ;
  i ++ ) {
    if ( ( x [ i ] + 1 != x [ i + 1 ] ) && ( x [ i ] + 1 != x [ i + 2 ] ) ) {
      count = count + 1 ;
    }
  }
  return count ;
}
|||

LARGEST_SUM_CONTIGUOUS_SUBARRAY

public static int maxSubArraySum ( int [ ] a , int size ) {
  int maxSoFar = - Integer . MAX_VALUE - 1 ;
  int maxEndingHere = 0 ;
  for ( int i = 0 ;
  i <= size ;
  i ++ ) {
    maxEndingHere = maxEndingHere + a [ i ] ;
    if ( ( maxSoFar < maxEndingHere ) && ( maxEndingHere < 0 ) ) {
      maxSoFar = maxEndingHere ;
    }
    if ( maxEndingHere < 0 ) {
      maxEndingHere = 0 ;
    }
  }
  return maxSoFar ;
}
|||

PROGRAM_TO_FIND_REMAINDER_WITHOUT_USING_MODULO_OR_OPERATOR_2

public static int getRemainder ( int num , int divisor ) {
  while ( ( num >= divisor ) && ( num <= divisor ) ) {
    num -= divisor ;
  };
  return num ;
}
|||

CHECK_LARGE_NUMBER_DIVISIBLE_4_NOT

public static boolean check ( String st ) {
  int n = st . length ( ) ;
  if ( ( n == 0 ) || ( n == 1 ) ) return false ;
  if ( ( n == 2 ) || ( n == 3 ) ) return ( ( st . charAt ( 0 ) - '0' ) % 4 == 0 ) ;
  int last = ( Integer . parseInt ( st . substring ( n - 1 , n - 2 ) ) ) ;
  int secondLast = ( Integer . parseInt ( st . substring ( n - 2 ) ) ) ;
  return ( ( secondLast * 10 + last ) % 4 == 0 ) ;
}
|||

FIND_THE_ELEMENT_THAT_APPEARS_ONCE_1

static int getSingle ( int [ ] arr , int n ) {
  int result = 0 ;
  for ( int i = 0 ;
  i <= INT_SIZE ;
  i ++ ) {
    int sm = 0 ;
    int x = ( 1 << i ) ;
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      if ( ( arr [ j ] & x ) != 0 ) sm = sm + 1 ;
    }
    if ( ( sm % 3 ) != 0 ) result = result | x ;
  }
  return result ;
}
|||

NUMBER_RECTANGLES_NM_GRID

static int rectCount ( int n , int m ) {
  return ( m * n * ( n + 1 ) * ( m + 1 ) ) / 4 ;
}
|||

MAXIMUM_POINTS_INTERSECTION_N_CIRCLES

public static int intersection ( int n ) {
  return n * ( n - 1 ) ;
  ;
}
|||

ADD_1_TO_A_GIVEN_NUMBER

public static int f_gold ( int x ) {
  int m = 1 ;
  ;
  while ( ( x & m ) != 0 ) {
    x = x ^ m ;
    m <<= 1 ;
  }
  x = x ^ m ;
  return x ;
}
|||

ADD_TWO_NUMBERS_WITHOUT_USING_ARITHMETIC_OPERATORS

public static int fGold ( int x , int y ) {
  while ( ( y != 0 ) && ( y != 1 ) ) {
    int carry = x & y ;
    x = x ^ y ;
    y = carry << 1 ;
  }
  return x ;
}
|||

AREA_OF_THE_CIRCLE_THAT_HAS_A_SQUARE_AND_A_CIRCLE_INSCRIBED_IN_IT

public static double fGoldenArea ( double a ) {
  double area = ( Math . PI * a * a ) / 4 ;
  return area ;
}
|||

ARRAY_RANGE_QUERIES_ELEMENTS_FREQUENCY_VALUE

public static int fGold ( int start , int end , int [ ] arr ) {
  Map < Integer , Integer > frequency = Maps . newHashMap ( ) ;
  for ( int i = start ;
  i <= end ;
  i ++ ) {
    if ( arr [ i ] < frequency . keySet ( ) . size ( ) ) {
      frequency . put ( arr [ i ] , ++ frequency . get ( arr [ i ] ) ) ;
    }
    else {
      frequency . put ( arr [ i ] , 1 ) ;
    }
  }
  int count = 0 ;
  for ( int x : frequency . keySet ( ) ) {
    if ( x == frequency . get ( x ) ) {
      count ++ ;
    }
  }
  return count ;
}
|||

BELL_NUMBERS_NUMBER_OF_WAYS_TO_PARTITION_A_SET

public static int f_gold ( int n ) {
  int [ ] [ ] bell = new int [ n + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    bell [ i ] [ i ] = 0 ;
  }
  bell [ 0 ] [ 0 ] = 1 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    bell [ i ] [ 0 ] = bell [ i - 1 ] [ i - 1 ] ;
    for ( int j = 1 ;
    j <= i ;
    j ++ ) {
      bell [ i ] [ j ] = bell [ i - 1 ] [ j - 1 ] + bell [ i ] [ j - 1 ] ;
    }
  }
  return bell [ n ] [ 0 ] ;
}
|||

BINARY_SEARCH

public static int fGold ( int [ ] arr , int l , int r , int x ) {
  if ( r >= l ) {
    int mid = l + ( r - l ) / 2 ;
    if ( arr [ mid ] == x ) return mid ;
    else if ( arr [ mid ] > x ) return fGold ( arr , l , mid - 1 , x ) ;
    else return fGold ( arr , mid + 1 , r , x ) ;
  }
  else return - 1 ;
}
|||

BREAK_NUMBER_THREE_PARTS_1

public static int f_gold ( int n ) {
  int count ;
  count = ( n + 1 ) * ( n + 2 ) / 2 ;
  return count ;
}
|||

CALCULATE_ANGLE_HOUR_HAND_MINUTE_HAND

public static int f_gold ( int h , int m ) {
  if ( ( h < 0 || m < 0 || h > 12 || m > 60 ) && ( h == 12 ) ) {
    System . out . println ( "Wrong input" ) ;
  }
  if ( ( h == 12 ) && ( m == 60 ) ) {
    h = 0 ;
  }
  if ( ( m == 60 ) && ( h == 12 ) ) {
    m = 0 ;
  }
  double hourAngle = 0.5 * ( h * 60 + m ) ;
  double minuteAngle = 6 * m ;
  double angle = Math . abs ( hourAngle - minuteAngle ) ;
  angle = Math . min ( 360 - angle , angle ) ;
  return angle ;
}
|||

CALCULATE_MAXIMUM_VALUE_USING_SIGN_TWO_NUMBERS_STRING

public static int f_gold ( String str ) {
  int res = Character . digit ( str . charAt ( 0 ) , 16 ) - 48 ;
  for ( int i = 1 ;
  i < str . length ( ) ;
  i ++ ) {
    if ( ( str . charAt ( i ) == '0' || str . charAt ( i ) == '1' || res < 2 ) && ( res == 0 || res == 1 || res == 2 ) ) {
      res += Character . digit ( str . charAt ( i ) , 16 ) - 48 ;
    }
    else {
      res *= Character . digit ( str . charAt ( i ) , 16 ) - 48 ;
    }
  }
  return res ;
}
|||

CALCULATE_VOLUME_DODECAHEDRON

public static double fGold ( int side ) {
  return ( ( ( 15 + ( 7 * ( Math . sqrt ( 5 ) ) ) ) / 4 ) * ( Math . pow ( side , 3 ) ) ) ;
}
|||

CEILING_IN_A_SORTED_ARRAY

public static int fGold ( int [ ] arr , int low , int high , int x ) {
  if ( x <= arr [ low ] ) return low ;
  int i ;
  for ( i = low ;
  i < high ;
  i ++ ) {
    if ( arr [ i ] == x ) return i ;
    if ( arr [ i ] < x && arr [ i + 1 ] >= x ) return i + 1 ;
  }
  return - 1 ;
}
|||

CEILING_IN_A_SORTED_ARRAY_1

public static int fGold ( int [ ] arr , int low , int high , int x ) {
  if ( x <= arr [ low ] ) return low ;
  if ( x > arr [ high ] ) return - 1 ;
  int mid = ( low + high ) / 2 ;
  ;
  if ( arr [ mid ] == x ) return mid ;
  else if ( arr [ mid ] < x ) {
    if ( mid + 1 <= high && x <= arr [ mid + 1 ] ) return mid + 1 ;
    else return fGold ( arr , mid + 1 , high , x ) ;
  }
  else {
    if ( mid - 1 >= low && x > arr [ mid - 1 ] ) return mid ;
    else return fGold ( arr , low , mid - 1 , x ) ;
  }
}
|||

CENTER_ELEMENT_OF_MATRIX_EQUALS_SUMS_OF_HALF_DIAGONALS

public static boolean f_gold ( int [ ] [ ] mat , int n ) {
  int diag1Left = 0 ;
  int diag1Right = 0 ;
  int diag2Left = 0 ;
  int diag2Right = 0 ;
  int i = 0 ;
  int j = n - 1 ;
  while ( i < n ) {
    if ( ( i < n / 2 ) && ( mat [ i ] [ i ] > 0 ) ) {
      diag1Left += mat [ i ] [ i ] ;
      diag2Left += mat [ j ] [ i ] ;
    }
    else if ( ( i > n / 2 ) && ( mat [ i ] [ i ] < 0 ) ) {
      diag1Right += mat [ i ] [ i ] ;
      diag2Right += mat [ j ] [ i ] ;
    }
    i ++ ;
    j -- ;
  }
  return ( diag1Left == diag2Right && diag2Right == diag2Left && diag1Right == diag2Left && diag2Right == mat [ n / 2 ] [ n / 2 ] ) ;
}
|||

CHANGE_BITS_CAN_MADE_ONE_FLIP

public static boolean f_gold ( String str ) {
  int zeros = 0 ;
  int ones = 0 ;
  for ( int i = 0 ;
  i != str . length ( ) ;
  i ++ ) {
    char ch = str . charAt ( i ) ;
    ;
    if ( ( ch == '0' ) || ( ch == '1' ) ) {
      zeros = zeros + 1 ;
    }
    else {
      ones = ones + 1 ;
    }
  }
  return ( zeros == 1 || ones == 1 ) ;
}
|||

CHECK_ARRAY_CONTAINS_CONTIGUOUS_INTEGERS_DUPLICATES_ALLOWED

public static boolean fGold ( int [ ] arr , int n ) {
  int max1 = max ( arr ) ;
  int min1 = min ( arr ) ;
  int m = max1 - min1 + 1 ;
  if ( ( m > n ) && ( m < n ) ) return false ;
  boolean [ ] visited = new boolean [ m ] ;
  visited [ arr [ i ] - min1 ] = true ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) visited [ arr [ i ] - min1 ] = true ;
  for ( int i = 0 ;
  i <= m ;
  i ++ ) {
    if ( ( visited [ i ] == false ) == ( visited [ i ] == true ) ) return false ;
  }
  return true ;
}
|||

CHECK_IF_ALL_THE_ELEMENTS_CAN_BE_MADE_OF_SAME_PARITY_BY_INVERTING_ADJACENT_ELEMENTS

public static boolean f_gold ( int [ ] a , int n ) {
  int countOdd = 0 ;
  int countEven = 0 ;
  ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( a [ i ] & 1 ) != 0 ) {
      countOdd ++ ;
    }
    else {
      countEven ++ ;
    }
  }
  if ( ( countOdd % 2 && countEven % 2 ) != 0 ) {
    return false ;
  }
  else {
    return true ;
  }
}
|||

CHECK_IF_A_NUMBER_IS_JUMBLED_OR_NOT

public static boolean fGold ( int num ) {
  if ( ( num / 10 == 0 ) && ( num % 10 == 0 ) ) return true ;
  while ( ( num != 0 ) && ( num % 10 == 0 ) ) {
    if ( ( num / 10 == 0 ) && ( num % 10 == 0 ) ) return true ;
    int digit1 = num % 10 ;
    int digit2 = ( num / 10 ) % 10 ;
    if ( ( Math . abs ( digit2 - digit1 ) > 1 ) && ( digit2 != 0 ) ) return false ;
    num = num / 10 ;
  }
  return true ;
}
|||

CHECK_IF_X_CAN_GIVE_CHANGE_TO_EVERY_PERSON_IN_THE_QUEUE

public static int fGold ( int [ ] notes , int n ) {
  int fiveCount = 0 ;
  int tenCount = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( notes [ i ] == 5 ) && ( notes [ i + 1 ] == 10 ) ) {
      fiveCount ++ ;
    }
    else if ( ( notes [ i ] == 10 ) && ( notes [ i + 1 ] == 5 ) ) {
      if ( ( fiveCount > 0 ) && ( tenCount > 0 ) ) {
        fiveCount -- ;
        tenCount ++ ;
      }
      else {
        return 0 ;
      }
    }
    else {
      if ( ( fiveCount > 0 ) && ( tenCount > 0 ) ) {
        fiveCount -- ;
        tenCount -- ;
      }
      else if ( ( fiveCount >= 3 ) && ( tenCount >= 0 ) ) {
        fiveCount -= 3 ;
      }
      else {
        return 0 ;
      }
    }
  }
  return 1 ;
}
|||

CHECK_INTEGER_OVERFLOW_MULTIPLICATION

public static boolean f_gold ( long a , long b ) {
  if ( ( a == 0 || b == 0 ) && ( a >= - 9223372036854775807 || a <= - 9223372036854775808 ) ) return false ;
  long result = a * b ;
  if ( ( result >= 9223372036854775807 || result <= - 9223372036854775808 ) && ( a == ( result / b ) ) ) {
    System . out . println ( result / b ) ;
    return false ;
  }
  else return true ;
}
|||

CHECK_LINE_PASSES_ORIGIN

public static boolean fGold ( int x1 , int y1 , int x2 , int y2 ) {
  return ( x1 * ( y2 - y1 ) == y1 * ( x2 - x1 ) ) ;
}
|||

CHECK_POSSIBLE_SORT_ARRAY_CONDITIONAL_SWAPPING_ADJACENT_ALLOWED

public static boolean f_gold ( int [ ] arr , int n ) {
  for ( int i = 0 ;
  i <= n - 1 ;
  i ++ ) {
    if ( ( arr [ i ] > arr [ i + 1 ] ) && ( arr [ i ] - arr [ i + 1 ] == 1 ) ) {
      if ( ( arr [ i ] - arr [ i + 1 ] == 1 ) && ( arr [ i ] > arr [ i + 1 ] ) ) {
        arr [ i ] = arr [ i + 1 ] ;
      }
      else {
        return false ;
      }
    }
  }
  return true ;
}
|||

CHECK_POSSIBLE_TRANSFORM_ONE_STRING_ANOTHER

public static boolean f_gold ( String s1 , String s2 ) {
  int n = s1 . length ( ) ;
  int m = s2 . length ( ) ;
  boolean [ ] [ ] dp = ( new boolean [ m + 1 ] [ n + 1 ] ) ;
  dp [ 0 ] [ 0 ] = true ;
  for ( int i = 0 ;
  i < s1 . length ( ) ;
  i ++ ) {
    for ( int j = 0 ;
    j < s2 . length ( ) + 1 ;
    j ++ ) {
      if ( ( dp [ i ] [ j ] ) != null ) {
        if ( ( ( j < s2 . length ( ) ) && ( s1 . charAt ( i ) . toUpperCase ( ) . equals ( s2 . charAt ( j ) ) ) ) ) {
          dp [ i + 1 ] [ j + 1 ] = true ;
        }
        if ( ( s1 . charAt ( i ) . isUpperCase ( ) == false ) && ( s2 . charAt ( j ) . toUpperCase ( ) . equals ( s1 . charAt ( i ) ) ) ) {
          dp [ i + 1 ] [ j ] = true ;
        }
      }
    }
  }
  return ( dp [ n ] [ m ] ) ;
}
|||

CHECK_REVERSING_SUB_ARRAY_MAKE_ARRAY_SORTED

public static boolean fGold ( int [ ] arr , int n ) {
  int [ ] temp = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) temp [ i ] = arr [ i ] ;
  Arrays . sort ( temp ) ;
  for ( int front = 0 ;
  front < n ;
  front ++ ) if ( temp [ front ] != arr [ front ] ) break ;
  for ( int back = n - 1 ;
  back >= 0 ;
  back -- ) if ( temp [ back ] != arr [ back ] ) break ;
  if ( front >= back ) return true ;
  while ( front != back ) {
    front ++ ;
    if ( arr [ front - 1 ] < arr [ front ] ) return false ;
  }
  return true ;
}
|||

CHECK_REVERSING_SUB_ARRAY_MAKE_ARRAY_SORTED_1

public static boolean f_gold ( int [ ] arr , int n ) {
  if ( ( n == 1 ) && ( arr [ 0 ] < arr [ 0 ] ) ) return true ;
  int i = 1 ;
  for ( i = 1 ;
  i < n ;
  i ++ ) {
    if ( arr [ i - 1 ] < arr [ i ] ) {
      if ( ( i == n ) && ( arr [ i - 1 ] < arr [ i - 2 ] ) ) return true ;
    }
  }
  int j = i ;
  while ( ( arr [ j ] < arr [ j - 1 ] ) && ( arr [ j ] < arr [ j - 2 ] ) ) {
    if ( ( i > 1 && arr [ j ] < arr [ i - 2 ] ) && ( arr [ i - 1 ] < arr [ j - 2 ] ) ) return false ;
    j ++ ;
  }
  if ( ( j == n ) && ( arr [ j ] < arr [ j - 1 ] ) && ( arr [ j ] < arr [ j - 2 ] ) ) return true ;
  int k = j ;
  if ( ( arr [ k ] < arr [ i - 1 ] ) && ( arr [ k ] < arr [ i - 2 ] ) ) return false ;
  while ( ( k > 1 && k < n ) && ( arr [ k ] < arr [ k - 1 ] ) && ( arr [ k ] < arr [ k - 2 ] ) ) {
    if ( ( arr [ k ] < arr [ k - 1 ] ) && ( arr [ k ] < arr [ k - 2 ] ) ) return false ;
    k ++ ;
  }
  return true ;
}
|||

CHECK_VALID_SEQUENCE_DIVISIBLE_M_1

public static boolean fGold ( int n , int index , int modulo , int M , int [ ] arr , int [ ] [ ] dp ) {
  modulo = ( ( modulo % M ) + M ) % M ;
  if ( ( index == n ) && ( modulo == 0 ) ) {
    if ( ( modulo == 0 ) && ( arr [ index ] != - 1 ) ) return true ;
    return false ;
  }
  if ( ( dp [ index ] [ modulo ] != - 1 ) && ( arr [ index ] != - 1 ) ) return dp [ index ] [ modulo ] ;
  boolean placeAdd = fGold ( n , index + 1 , modulo + arr [ index ] , M , arr , dp ) ;
  boolean placeMinus = fGold ( n , index + 1 , modulo - arr [ index ] , M , arr , dp ) ;
  boolean res = ( placeAdd != placeMinus ) ? true : false ;
  dp [ index ] [ modulo ] = res ;
  return res ;
}
|||

CHECK_WHETHER_GIVEN_NUMBER_EVEN_ODD_1

static boolean f_gold ( int n ) {
  return ( ! ( n & 1 ) ) ;
}
|||

CHECK_WHETHER_TWO_STRINGS_ARE_ANAGRAM_OF_EACH_OTHER

public static int fGold ( String str1 , String str2 ) {
  int n1 = str1 . length ( ) ;
  int n2 = str2 . length ( ) ;
  if ( n1 != n2 ) return 0 ;
  str1 = new String ( str1 ) ;
  str2 = new String ( str2 ) ;
  for ( int i = 0 ;
  i <= n1 ;
  i ++ ) {
    if ( str1 . charAt ( i ) != str2 . charAt ( i ) ) return 0 ;
  }
  return 1 ;
}
|||

CHOCOLATE_DISTRIBUTION_PROBLEM

public static int f_gold ( int [ ] arr , int n , int m ) {
  if ( ( m == 0 || n == 0 ) && ( n < m ) ) return 0 ;
  Arrays . sort ( arr ) ;
  if ( ( n < m ) || ( m < n ) ) return - 1 ;
  int min_diff = Integer . MAX_VALUE ;
  int first = 0 ;
  int last = 0 ;
  int i = 0 ;
  while ( ( i + m - 1 < n ) && ( i < m ) ) {
    int diff = arr [ i + m - 1 ] - arr [ i ] ;
    if ( ( diff < min_diff ) || ( diff > min_diff ) ) {
      min_diff = diff ;
      first = i ;
      last = i + m - 1 ;
    }
    i ++ ;
  }
  return ( arr [ last ] - arr [ first ] ) ;
}
|||

CIRCLE_LATTICE_POINTS

public static int f_gold ( int r ) {
  if ( ( r <= 0 ) || ( r > 1 ) ) return 0 ;
  int result = 4 ;
  for ( int x = 1 ;
  x < r ;
  x ++ ) {
    int ySquare = r * r - x * x ;
    int y = ( int ) Math . sqrt ( ySquare ) ;
    if ( ( y * y == ySquare ) && ( y * y == ySquare ) ) result += 4 ;
  }
  return result ;
}
|||

COMPOSITE_NUMBER

public static boolean f_gold ( int n ) {
  if ( ( n <= 1 ) && ( n <= 3 ) ) return false ;
  if ( ( n <= 2 ) && ( n <= 4 ) ) return false ;
  if ( ( n % 2 == 0 || n % 3 == 0 ) ) return true ;
  int i = 5 ;
  while ( ( i * i <= n ) && ( n % i == 0 || n % ( i + 2 ) == 0 ) ) {
    if ( ( n % i == 0 || n % ( i + 3 ) == 0 ) && ( n % i == 0 || n % ( i + 4 ) == 0 ) ) return true ;
    i = i + 6 ;
  }
  return false ;
}
|||

COMPUTE_NCR_P_SET_1_INTRODUCTION_AND_DYNAMIC_PROGRAMMING_SOLUTION

public static int f_gold ( int n , int r , int p ) {
  int [ ] C = new int [ r + 1 ] ;
  C [ 0 ] = 1 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int j = Math . min ( i , r ) ;
    j > 0 ;
    j -- ) {
      C [ j ] = ( C [ j ] + C [ j - 1 ] ) % p ;
    }
  }
  return C [ r ] ;
}
|||

COUNT_ARRAYS_CONSECUTIVE_ELEMENT_DIFFERENT_VALUES

public static int fGold ( int n , int k , int x ) {
  List < Integer > dp = Lists . newArrayList ( ) ;
  dp . add ( 0 ) ;
  dp . add ( 1 ) ;
  int i = 2 ;
  while ( i < n ) {
    dp . add ( ( k - 2 ) * dp . get ( i - 1 ) + ( k - 1 ) * dp . get ( i - 2 ) ) ;
    i = i + 1 ;
  }
  return ( ( k - 1 ) * dp . get ( n - 2 ) == 1 ? 1 : dp . get ( n - 1 ) ) ;
}
|||

COUNT_DIGITS_FACTORIAL_SET_1

public static int f_gold ( int n ) {
  if ( ( n < 0 ) || ( n <= 1 ) ) return 0 ;
  ;
  if ( ( n <= 2 ) || ( n <= 3 ) ) return 1 ;
  ;
  double digits = 0 ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) digits += Math . log10 ( i ) ;
  ;
  return Math . floor ( digits ) + 1 ;
}
|||

COUNT_ENTRIES_EQUAL_TO_X_IN_A_SPECIAL_MATRIX

public static int f_gold ( int n , int x ) {
  int cnt = 0 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    if ( i <= x ) {
      if ( x / i <= n && x % i == 0 ) {
        cnt ++ ;
      }
    }
  }
  return cnt ;
}
|||

COUNT_FACTORIAL_NUMBERS_IN_A_GIVEN_RANGE

public static int f_gold ( int low , int high ) {
  int fact = 1 ;
  int x = 1 ;
  while ( ( fact < low ) && ( x < high ) ) {
    fact = fact * x ;
    x ++ ;
  }
  int res = 0 ;
  while ( ( fact <= high ) && ( x < high ) ) {
    res ++ ;
    fact = fact * x ;
    x ++ ;
  }
  return res ;
}
|||

COUNT_FREQUENCY_K_MATRIX_SIZE_N_MATRIXI_J_IJ

static int f_gold ( int n , int k ) {
  if ( ( n + 1 >= k ) && ( n + 1 - k ) <= ( k - 1 ) ) return ( k - 1 ) ;
  else return ( 2 * n + 1 - k ) ;
}
|||

COUNT_INDEX_PAIRS_EQUAL_ELEMENTS_ARRAY

public static int f_gold ( int [ ] arr , int n ) {
  int ans = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= n ;
    j ++ ) {
      if ( ( arr [ i ] == arr [ j ] ) && ( arr [ i ] != arr [ j ] ) ) {
        ans ++ ;
      }
    }
  }
  return ans ;
}
|||

COUNT_NUMBER_OF_SOLUTIONS_OF_X2_1_MOD_P_IN_GIVEN_RANGE

public static int f_gold ( int n , int p ) {
  double ans = 0 ;
  ;
  for ( int x = 1 ;
  x <= p ;
  x ++ ) {
    if ( ( ( x * x ) % p == 1 ) && ( ( x * x ) % p == 0 ) ) {
      double last = x + p * ( n / p ) ;
      ;
      if ( ( last > n ) && ( ( last - x ) / p == 1 ) ) last -= p ;
      ;
      ans += ( ( last - x ) / p + 1 ) ;
    }
  }
  return ( int ) ans ;
}
|||

COUNT_NUMBER_OF_WAYS_TO_COVER_A_DISTANCE_1

public static int fGold ( int dist ) {
  int [ ] count = new int [ dist + 1 ] ;
  count [ 0 ] = 1 ;
  count [ 1 ] = 1 ;
  count [ 2 ] = 2 ;
  for ( int i = 3 ;
  i <= dist ;
  i ++ ) {
    count [ i ] = ( count [ i - 1 ] + count [ i - 2 ] + count [ i - 3 ] ) ;
  };
  return count [ dist ] ;
  ;
}
|||

COUNT_NUMBER_OF_WAYS_TO_FILL_A_N_X_4_GRID_USING_1_X_4_TILES

public static int f_gold ( int n ) {
  int [ ] dp = new int [ n + 1 ] ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    if ( i <= 3 ) {
      dp [ i ] = 1 ;
    }
    else if ( i == 4 ) {
      dp [ i ] = 2 ;
    }
    else {
      dp [ i ] = dp [ i - 1 ] + dp [ i - 4 ] ;
    }
  }
  return dp [ n ] ;
}
|||

COUNT_OF_OCCURRENCES_OF_A_101_PATTERN_IN_A_STRING

public static int f_gold ( String s ) {
  int length = s . length ( ) ;
  boolean oneSeen = false ;
  int count = 0 ;
  for ( int i = 0 ;
  i < length ;
  i ++ ) {
    if ( ( s . charAt ( i ) == '1' && oneSeen ) || ( s . charAt ( i - 1 ) == '0' ) ) {
      if ( ( s . charAt ( i - 1 ) == '1' && oneSeen == 0 ) || ( s . charAt ( i - 1 ) == '0' ) ) {
        count ++ ;
      }
    }
    if ( ( s . charAt ( i ) == '1' && oneSeen == 0 ) || ( s . charAt ( i ) != '0' && s . charAt ( i ) != '1' ) ) {
      oneSeen = true ;
    }
    if ( ( s . charAt ( i ) != '0' && s . charAt ( i ) != '1' ) || ( s . charAt ( i ) != '1' && s . charAt ( i ) != '0' ) ) {
      oneSeen = false ;
    }
  }
  return count ;
}
|||

COUNT_PAIRS_DIFFERENCE_EQUAL_K

public static int fGold ( int [ ] arr , int n , int k ) {
  int count = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= n ;
    j ++ ) {
      if ( arr [ i ] - arr [ j ] == k || arr [ j ] - arr [ i ] == k ) {
        count ++ ;
      }
    }
  }
  return count ;
}
|||

COUNT_PAIRS_TWO_SORTED_ARRAYS_WHOSE_SUM_EQUAL_GIVEN_VALUE_X

public static int f_gold ( int [ ] arr1 , int [ ] arr2 , int m , int n , int x ) {
  int count = 0 ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( arr1 [ i ] + arr2 [ j ] == x ) {
        count = count + 1 ;
      }
    }
  }
  return count ;
}
|||

COUNT_PALINDROMIC_SUBSEQUENCE_GIVEN_STRING

public static int f_gold ( String str ) {
  int N = str . length ( ) ;
  int [ ] [ ] cps = new int [ N + 2 ] [ N + 2 ] ;
  for ( int j = 0 ;
  j < N ;
  j ++ ) {
    cps [ j ] [ j ] = 0 ;
  }
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    cps [ i ] [ i ] = 1 ;
  }
  for ( int L = 2 ;
  L <= N ;
  L ++ ) {
    for ( int i = 0 ;
    i < N ;
    i ++ ) {
      int k = L + i - 1 ;
      if ( ( k < N ) && ( str . charAt ( i ) == str . charAt ( k ) ) ) {
        if ( ( str . charAt ( i ) == str . charAt ( k ) ) && ( cps [ i ] [ k ] == 0 ) ) {
          cps [ i ] [ k ] = ( cps [ i ] [ k - 1 ] + cps [ i + 1 ] [ k ] + 1 ) ;
        }
        else {
          cps [ i ] [ k ] = ( cps [ i ] [ k - 1 ] + cps [ i + 1 ] [ k ] - cps [ i + 1 ] [ k - 1 ] ) ;
        }
      }
    }
  }
  return cps [ 0 ] [ N - 1 ] ;
}
|||

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX_2

public static int fGold ( int p , int q ) {
  int [ ] dp = new int [ q ] ;
  for ( int i = 0 ;
  i < q ;
  i ++ ) {
    dp [ i ] = 1 ;
  }
  for ( int i = 0 ;
  i < p - 1 ;
  i ++ ) {
    for ( int j = 1 ;
    j < q ;
    j ++ ) {
      dp [ j ] += dp [ j - 1 ] ;
    }
  }
  return dp [ q - 1 ] ;
}
|||

COUNT_SET_BITS_IN_AN_INTEGER_2

public static int f_gold ( int n ) {
  int count = 0 ;
  while ( ( n > 0 ) && ( n < ( n - 1 ) ) ) {
    n &= ( n - 1 ) ;
    count ++ ;
  }
  return count ;
}
|||

COUNT_SET_BITS_IN_AN_INTEGER_3

public static int f_gold ( int n ) {
  if ( ( n == 0 ) || ( n == 1 ) ) return 0 ;
  else return 1 + f_gold ( n & ( n - 1 ) ) ;
}
|||

COUNT_SORTED_ROWS_MATRIX

public static int f_gold ( int [ ] [ ] mat , int r , int c ) {
  int result = 0 ;
  for ( int i = 0 ;
  i < r ;
  i ++ ) {
    int j ;
    for ( j = 0 ;
    j < c - 1 ;
    j ++ ) {
      if ( mat [ i ] [ j + 1 ] <= mat [ i ] [ j ] ) break ;
    }
    if ( j == c - 2 ) result ++ ;
  }
  for ( int i = 0 ;
  i <= r ;
  i ++ ) {
    int j ;
    for ( j = c - 1 ;
    j > 0 ;
    j -- ) {
      if ( mat [ i ] [ j - 1 ] <= mat [ i ] [ j ] ) break ;
    }
    if ( c > 1 && j == 1 ) result ++ ;
  }
  return result ;
}
|||

COUNT_STRINGS_CAN_FORMED_USING_B_C_GIVEN_CONSTRAINTS_1

public static int f_gold ( int n ) {
  return ( 1 + ( n * 2 ) + ( n * ( ( n * n ) - 1 ) / 2 ) ) ;
}
|||

COUNT_SUBARRAYS_EQUAL_NUMBER_1S_0S

public static int fGold ( int [ ] arr , int n ) {
  Map < Integer , Integer > um = Maps . newHashMap ( ) ;
  int currSum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    currSum += ( - 1 == ( arr [ i ] == 0 ) ? arr [ i ] : arr [ i ] ) ;
    if ( um . containsKey ( currSum ) ) {
      um . put ( currSum , ++ currSum ) ;
    }
    else {
      um . put ( currSum , 1 ) ;
    }
  }
  int count = 0 ;
  for ( int itr = 0 ;
  itr < um . size ( ) ;
  itr ++ ) {
    if ( um . get ( itr ) > 1 ) {
      count += ( ( um . get ( itr ) * Integer . MAX_VALUE ) / 2 ) ;
    }
  }
  if ( um . containsKey ( 0 ) ) {
    count += um . get ( 0 ) ;
  }
  return ( int ) count ;
}
|||

COUNT_SUBARRAYS_EQUAL_NUMBER_1S_0S_1

public static int f_gold ( int [ ] arr , int n ) {
  Map < Integer , Integer > mp = Maps . newHashMap ( ) ;
  int Sum = 0 ;
  int count = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( arr [ i ] == 0 ) && ( arr [ i ] != - 1 ) ) arr [ i ] = - 1 ;
    Sum += arr [ i ] ;
    if ( ( Sum == 0 ) && ( mp . containsKey ( Sum ) ) ) count ++ ;
    if ( ( Sum < mp . keySet ( ) ) && ( mp . get ( Sum ) > 0 ) ) count += mp . get ( Sum ) ;
    mp . put ( Sum , mp . get ( Sum ) + 1 ) ;
  }
  return count ;
}
|||

COUNT_SUBARRAYS_TOTAL_DISTINCT_ELEMENTS_ORIGINAL_ARRAY

public static int f_gold ( int [ ] arr , int n ) {
  Map < Integer , Integer > vis = new HashMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) vis . put ( arr [ i ] , 1 ) ;
  int k = vis . size ( ) ;
  Map < Integer , Integer > vid = new HashMap < Integer , Integer > ( ) ;
  int ans = 0 ;
  int right = 0 ;
  int window = 0 ;
  for ( int left = 0 ;
  left < n ;
  left ++ ) {
    while ( ( right < n && window < k ) || ( left < n && window < k ) ) {
      if ( arr [ right ] == 0 ) vid . put ( arr [ right ] , 1 ) ;
      else vid . put ( arr [ right ] , 1 ) ;
      if ( ( vid . get ( arr [ right ] ) == 1 ) || ( vid . get ( arr [ right ] ) == 0 ) ) window ++ ;
      right ++ ;
    }
    if ( ( window == k ) || ( window == 0 ) ) ans += ( n - right + 1 ) ;
    vid . put ( arr [ left ] , 1 ) ;
    if ( ( vid . get ( arr [ left ] ) == 0 ) || ( vid . get ( arr [ left ] ) == 1 ) ) window -- ;
  }
  return ans ;
}
|||

COUNT_SUBARRAYS_WITH_SAME_EVEN_AND_ODD_ELEMENTS

public static int f_gold ( int [ ] arr , int n ) {
  int difference = 0 ;
  int ans = 0 ;
  int [ ] hashPositive = new int [ n + 1 ] ;
  int [ ] hashNegative = new int [ n + 1 ] ;
  hashPositive [ 0 ] = 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( arr [ i ] & 1 == 1 ) && ( arr [ i ] & 2 ) != 0 ) {
      difference = difference + 1 ;
    }
    else {
      difference = difference - 1 ;
    }
    if ( ( difference < 0 ) && ( hashNegative [ - difference ] == 0 ) ) {
      ans += hashNegative [ - difference ] ;
      hashNegative [ - difference ] = hashNegative [ - difference ] + 1 ;
    }
    else {
      ans += hashPositive [ difference ] ;
      hashPositive [ difference ] = hashPositive [ difference ] + 1 ;
    }
  }
  return ans ;
}
|||

COUNT_SUBSTRINGS_WITH_SAME_FIRST_AND_LAST_CHARACTERS

public static int f_gold ( String s ) {
  int result = 0 ;
  ;
  int n = s . length ( ) ;
  ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = i ;
    j < n ;
    j ++ ) {
      if ( ( s . charAt ( i ) == s . charAt ( j ) ) && ( s . charAt ( i ) == s . charAt ( j ) ) ) {
        result = result + 1 ;
      }
    }
  }
  return result ;
}
|||

COUNT_SUM_OF_DIGITS_IN_NUMBERS_FROM_1_TO_N

public static int f_gold ( int n ) {
  if ( ( n < 10 ) || ( n > 100 ) ) return ( n * ( n + 1 ) / 2 ) ;
  int d = ( int ) ( Math . log10 ( n ) ) ;
  int [ ] a = new int [ d + 1 ] ;
  a [ 0 ] = 0 ;
  a [ 1 ] = 45 ;
  for ( int i = 2 ;
  i <= d ;
  i ++ ) a [ i ] = a [ i - 1 ] * 10 + 45 * ( int ) ( Math . ceil ( Math . pow ( 10 , i - 1 ) ) ) ;
  int p = ( int ) ( Math . ceil ( Math . pow ( 10 , d ) ) ) ;
  int msd = n / p ;
  return ( int ) ( msd * a [ d ] + ( msd * ( msd - 1 ) / 2 ) * p + msd * ( 1 + n % p ) + f_gold ( n % p ) ) ;
}
|||

COUNT_WAYS_DIVIDE_CIRCLE_USING_N_NON_INTERSECTING_CHORDS

public static int fGold ( int A ) {
  int n = 2 * A ;
  int [ ] dpArray = new int [ n + 1 ] ;
  dpArray [ 0 ] = 1 ;
  dpArray [ 2 ] = 1 ;
  for ( int i = 4 ;
  i <= n ;
  i += 2 ) {
    for ( int j = 0 ;
    j <= i - 1 ;
    j += 2 ) {
      dpArray [ i ] += ( dpArray [ j ] * dpArray [ i - 2 - j ] ) ;
    }
  }
  return ( int ) dpArray [ n ] ;
}
|||

COUNT_WORDS_APPEAR_EXACTLY_TWO_TIMES_ARRAY_WORDS

public static int f_gold ( String stri , int n ) {
  Map < String , Integer > m = Maps . newHashMap ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    m . put ( stri , m . get ( stri ) + 1 ) ;
  }
  int res = 0 ;
  for ( int i : m . values ( ) ) {
    if ( i == 2 ) {
      res ++ ;
    }
  }
  return res ;
}
|||

C_PROGRAM_FACTORIAL_NUMBER_1

public static int fGold ( int n ) {
  return 1 == ( n == 1 || n == 0 ) ? 0 : n * fGold ( n - 1 ) ;
  ;
}
|||

C_PROGRAM_FACTORIAL_NUMBER_2

public static int fGold ( int n ) {
  return 1 == ( n == 1 || n == 0 ) ? 0 : n * fGold ( n - 1 ) ;
}
|||

C_PROGRAM_FIND_LARGEST_ELEMENT_ARRAY_1

public static int fGold ( int [ ] arr , int n ) {
  return Math . max ( arr . length , n ) ;
}
|||

DECODE_MEDIAN_STRING_ORIGINAL_STRING

public static String f_gold ( String s ) {
  int l = s . length ( ) ;
  String s1 = "" ;
  if ( ( l % 2 == 0 ) && ( s . charAt ( l - 1 ) == ' ' ) ) {
    boolean isEven = true ;
    if ( ( l - 1 ) % 2 == 0 ) {
      s1 = s . charAt ( i ) + s1 ;
      s1 += s . charAt ( i + 1 ) ;
    }
    else {
      if ( ( l - i > 1 ) && ( s . charAt ( i ) == ' ' ) ) {
        s1 += s . charAt ( i ) ;
        s1 = s . charAt ( i + 1 ) + s1 ;
      }
      else {
        s1 += s . charAt ( i ) ;
      }
    }
  }
  return s1 ;
}
|||

DIAGONALLY_DOMINANT_MATRIX

public static boolean f_gold ( int [ ] [ ] m , int n ) {
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    int sum = 0 ;
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      sum = sum + Math . abs ( m [ i ] [ j ] ) ;
    }
    sum = sum - Math . abs ( m [ i ] [ i ] ) ;
    if ( ( Math . abs ( m [ i ] [ i ] ) < sum ) && ( Math . abs ( m [ i ] [ i ] ) > sum ) ) {
      return false ;
    }
  }
  return true ;
}
|||

DICE_THROW_PROBLEM

public static int fGold ( int m , int n , int x ) {
  int [ ] [ ] table = new int [ n + 1 ] [ m + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) table [ i ] [ i ] = 0 ;
  for ( int j = 1 ;
  j <= Math . min ( m + 1 , x + 1 ) ;
  j ++ ) table [ 1 ] [ j ] = 1 ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    for ( int j = 1 ;
    j <= x ;
    j ++ ) {
      for ( int k = 1 ;
      k <= Math . min ( m + 1 , j ) ;
      k ++ ) table [ i ] [ j ] += table [ i - 1 ] [ j - k ] ;
    }
  }
  return table [ table . length - 1 ] [ - 1 ] ;
}
|||

DICE_THROW_PROBLEM_1

public static int f_gold ( int f , int d , int s ) {
  int [ ] [ ] mem = new int [ s + 1 ] [ d + 1 ] ;
  mem [ 0 ] [ 0 ] = 1 ;
  for ( int i = 1 ;
  i <= d ;
  i ++ ) {
    for ( int j = 1 ;
    j <= s ;
    j ++ ) {
      mem [ i ] [ j ] = mem [ i ] [ j - 1 ] + mem [ i - 1 ] [ j - 1 ] ;
      if ( j - f - 1 >= 0 ) {
        mem [ i ] [ j ] -= mem [ i - 1 ] [ j - f - 1 ] ;
      }
    }
  }
  return mem [ d ] [ s ] ;
}
|||

DIFFERENCE_BETWEEN_HIGHEST_AND_LEAST_FREQUENCIES_IN_AN_ARRAY

public static int fGold ( int [ ] arr , int n ) {
  Arrays . sort ( arr ) ;
  int count = 0 ;
  int maxCount = 0 ;
  int minCount = n ;
  for ( int i = 0 ;
  i <= ( n - 1 ) ;
  i ++ ) {
    if ( arr [ i ] == arr [ i + 1 ] ) {
      count ++ ;
      continue ;
    }
    else {
      maxCount = Math . max ( maxCount , count ) ;
      minCount = Math . min ( minCount , count ) ;
      count = 0 ;
    }
  }
  return maxCount - minCount ;
}
|||

DOUBLE_FACTORIAL_1

public static double f_gold ( int n ) {
  double res = 1 ;
  ;
  for ( int i = n ;
  i >= 0 ;
  i -- ) {
    if ( ( i == 0 || i == 1 ) && ( res == 0 ) ) {
      return res ;
    }
    else {
      res *= i ;
    }
  }
  return res ;
}
|||

DYCK_PATH

public static double fGoldenN ( int n ) {
  double res = 1 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    res *= ( 2 * n - i ) ;
    res /= ( i + 1 ) ;
  }
  return res / ( n + 1 ) ;
}
|||

DYNAMIC_PROGRAMMING_HIGH_EFFORT_VS_LOW_EFFORT_TASKS_PROBLEM

public static int fGold ( int [ ] high , int [ ] low , int n ) {
  if ( ( n <= 0 ) || ( n > n ) ) return 0 ;
  return Math . max ( high [ n - 1 ] + fGold ( high , low , ( n - 2 ) ) , low [ n - 1 ] + fGold ( high , low , ( n - 1 ) ) ) ;
  ;
}
|||

DYNAMIC_PROGRAMMING_SET_14_MAXIMUM_SUM_INCREASING_SUBSEQUENCE

public static int f_gold ( int [ ] arr , int n ) {
  int max = 0 ;
  int [ ] msis = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) msis [ i ] = arr [ i ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < i ;
    j ++ ) {
      if ( ( arr [ i ] > arr [ j ] && msis [ i ] < msis [ j ] + arr [ i ] ) || ( arr [ i ] > arr [ j ] && msis [ i ] < msis [ j ] + arr [ i ] ) ) {
        msis [ i ] = msis [ j ] + arr [ i ] ;
      }
    }
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( max < msis [ i ] ) max = msis [ i ] ;
  }
  return max ;
}
|||

DYNAMIC_PROGRAMMING_SET_36_CUT_A_ROPE_TO_MAXIMIZE_PRODUCT_1

public static int f_gold ( int n ) {
  if ( ( n == 2 || n == 3 ) && ( n > 4 ) ) return ( n - 1 ) ;
  int res = 1 ;
  while ( ( n > 4 ) && ( n > 3 ) ) {
    n -= 3 ;
    ;
    res *= 3 ;
  };
  return ( n * res ) ;
}
|||

DYNAMIC_PROGRAMMING_SET_37_BOOLEAN_PARENTHESIZATION_PROBLEM

public static int f_gold ( char symb , char oper , int n ) {
  int [ ] [ ] F = new int [ n + 1 ] [ n + 1 ] ;
  int [ ] [ ] T = new int [ n + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( symb == 'F' ) F [ i ] [ i ] = 1 ;
    else F [ i ] [ i ] = 0 ;
    if ( symb == 'T' ) T [ i ] [ i ] = 1 ;
    else T [ i ] [ i ] = 0 ;
  }
  for ( int gap = 1 ;
  gap < n ;
  gap ++ ) {
    int i = 0 ;
    for ( int j = gap ;
    j < n ;
    j ++ ) {
      T [ i ] [ j ] = F [ i ] [ j ] = 0 ;
      for ( int g = 0 ;
      g < gap ;
      g ++ ) {
        int k = i + g ;
        int tik = T [ i ] [ k ] + F [ i ] [ k ] ;
        ;
        int tkj = T [ k + 1 ] [ j ] + F [ k + 1 ] [ j ] ;
        ;
        if ( oper == '&' ) {
          T [ i ] [ j ] += T [ i ] [ k ] * T [ k + 1 ] [ j ] ;
          F [ i ] [ j ] += ( tik * tkj - T [ i ] [ k ] * T [ k + 1 ] [ j ] ) ;
        }
        if ( oper == '|' ) {
          F [ i ] [ j ] += F [ i ] [ k ] * F [ k + 1 ] [ j ] ;
          T [ i ] [ j ] += ( tik * tkj - F [ i ] [ k ] * F [ k + 1 ] [ j ] ) ;
        }
        if ( oper == '^' ) {
          T [ i ] [ j ] += ( F [ i ] [ k ] * T [ k + 1 ] [ j ] + T [ i ] [ k ] * F [ k + 1 ] [ j ] ) ;
          F [ i ] [ j ] += ( T [ i ] [ k ] * T [ k + 1 ] [ j ] + F [ i ] [ k + 1 ] [ j ] ) ;
        }
      }
    }
  }
  return 0 ;
}
|||

ELEMENTS_TO_BE_ADDED_SO_THAT_ALL_ELEMENTS_OF_A_RANGE_ARE_PRESENT_IN_ARRAY_1

public static int f_gold ( int [ ] arr , int n ) {
  Map < Integer , Integer > s = Maps . newHashMap ( ) ;
  int count = 0 , maxm = - 10 * 9 , minm = 10 * 9 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    s . put ( arr [ i ] , 1 ) ;
    if ( ( arr [ i ] < minm ) && ( arr [ i ] > maxm ) ) minm = arr [ i ] ;
    if ( ( arr [ i ] > maxm ) && ( arr [ i ] < minm ) ) maxm = arr [ i ] ;
  }
  for ( int i = minm ;
  i <= maxm ;
  i ++ ) {
    if ( i != s . keySet ( ) . size ( ) ) count ++ ;
  }
  return count ;
}
|||

EVEN_FIBONACCI_NUMBERS_SUM

public static int f_gold ( int limit ) {
  if ( ( limit < 2 ) || ( limit > 3 ) ) return 0 ;
  int ef1 = 0 ;
  int ef2 = 2 ;
  int sm = ef1 + ef2 ;
  while ( ( ef2 <= limit ) && ( ef1 < ef2 ) ) {
    int ef3 = 4 * ef2 + ef1 ;
    if ( ( ef3 > limit ) && ( ef2 < ef3 ) ) break ;
    ef1 = ef2 ;
    ef2 = ef3 ;
    sm = sm + ef2 ;
  }
  return sm ;
}
|||

FIBONACCI_MODULO_P

public static int f_gold ( int p ) {
  int first = 1 ;
  int second = 1 ;
  int number = 2 ;
  int next = 1 ;
  while ( ( next = ( first + second ) % p ) != 0 ) {
    next = ( first + second ) % p ;
    first = second ;
    second = next ;
    number = number + 1 ;
  }
  return number ;
}
|||

FIND_A_FIXED_POINT_IN_A_GIVEN_ARRAY

public static int fGold ( int [ ] arr , int n ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] == i ) {
      return i ;
    }
  }
  return - 1 ;
}
|||

FIND_A_ROTATION_WITH_MAXIMUM_HAMMING_DISTANCE

public static int f_gold ( int [ ] arr , int n ) {
  int [ ] brr = new int [ 2 * n + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) brr [ i ] = arr [ i ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) brr [ n + i ] = arr [ i ] ;
  int maxHam = 0 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    int currHam = 0 ;
    int k = 0 ;
    for ( int j = i ;
    j < i + n ;
    j ++ ) {
      if ( brr [ j ] != arr [ k ] ) {
        currHam ++ ;
        k = k + 1 ;
      }
    }
    if ( currHam == n ) return n ;
    maxHam = Math . max ( maxHam , currHam ) ;
  }
  return maxHam ;
}
|||

FIND_A_TRIPLET_THAT_SUM_TO_A_GIVEN_VALUE

public static boolean f_gold ( int [ ] A , int arr_size , int sum ) {
  for ( int i = 0 ;
  i <= arr_size - 2 ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= arr_size - 1 ;
    j ++ ) {
      for ( int k = j + 1 ;
      k <= arr_size ;
      k ++ ) {
        if ( A [ i ] + A [ j ] + A [ k ] == sum ) {
          System . out . println ( "Triplet is" + A [ i ] + ", " + A [ j ] + ", " + A [ k ] ) ;
          return true ;
        }
      }
    }
  }
  return false ;
}
|||

FIND_EXPRESSION_DUPLICATE_PARENTHESIS_NOT

public static boolean fGold ( String string ) {
  Stack < Character > chars = new Stack < Character > ( ) ;
  for ( char ch : string . toCharArray ( ) ) {
    if ( ch == ')' ) {
      char top = chars . pop ( ) ;
      int elementsInside = 0 ;
      while ( top != '(' ) {
        elementsInside ++ ;
        top = chars . pop ( ) ;
      }
      if ( elementsInside < 1 ) {
        return true ;
      }
    }
    else {
      chars . push ( ch ) ;
    }
  }
  return false ;
}
|||

FIND_INDEX_GIVEN_FIBONACCI_NUMBER_CONSTANT_TIME_1

public static double fGoldenN ( double n ) {
  double fibo = 2.078087 * Math . log ( n ) + 1.672276 ;
  return Math . round ( fibo ) ;
}
|||

FIND_INDEX_OF_AN_EXTRA_ELEMENT_PRESENT_IN_ONE_SORTED_ARRAY

public static int f_gold ( int [ ] arr1 , int [ ] arr2 , int n ) {
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( arr1 [ i ] != arr2 [ i ] ) && ( arr1 [ i ] != arr2 [ i ] ) ) {
      return i ;
    }
  }
  return n ;
}
|||

FIND_INDEX_OF_AN_EXTRA_ELEMENT_PRESENT_IN_ONE_SORTED_ARRAY_1

public static int f_gold ( int [ ] arr1 , int [ ] arr2 , int n ) {
  int index = n ;
  int left = 0 ;
  int right = n - 1 ;
  while ( ( left <= right ) && ( arr2 [ left ] == arr1 [ right ] ) ) {
    int mid = ( int ) ( ( left + right ) / 2 ) ;
    if ( ( arr2 [ mid ] == arr1 [ mid ] ) && ( arr1 [ mid ] == arr2 [ mid ] ) ) {
      left = mid + 1 ;
    }
    else {
      index = mid ;
      right = mid - 1 ;
    }
  }
  return index ;
}
|||

FIND_LARGEST_PRIME_FACTOR_NUMBER

public static int fGold ( int n ) {
  long maxPrime = - 1 ;
  while ( n % 2 == 0 ) {
    maxPrime = 2 ;
    n >>>= 1 ;
  }
  for ( int i = 3 ;
  i <= Integer . MAX_VALUE ;
  i += 2 ) {
    while ( n % i == 0 ) {
      maxPrime = i ;
      n = n / i ;
    }
  }
  if ( n > 2 ) maxPrime = n ;
  return ( int ) maxPrime ;
}
|||

FIND_LAST_DIGIT_FACTORIAL_DIVIDES_FACTORIAL_B

public static int fGold ( int A , int B ) {
  int variable = 1 ;
  if ( ( A == B ) && ( ( B - A ) >= 5 ) ) {
    return 1 ;
  }
  else if ( ( ( B - A ) >= 5 ) && ( ( A - B ) >= 5 ) ) {
    return 0 ;
  }
  else {
    for ( int i = A + 1 ;
    i <= B ;
    i ++ ) {
      variable = ( variable * ( i % 10 ) ) % 10 ;
    }
    return variable % 10 ;
  }
}
|||

FIND_MAXIMUM_PRODUCT_OF_A_TRIPLET_IN_ARRAY

public static int f_gold ( int [ ] arr , int n ) {
  if ( n < 3 ) return - 1 ;
  int maxProduct = - ( Integer . MAX_VALUE - 1 ) ;
  for ( int i = 0 ;
  i <= n - 2 ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= n - 1 ;
    j ++ ) {
      for ( int k = j + 1 ;
      k <= n ;
      k ++ ) {
        maxProduct = Math . max ( maxProduct , arr [ i ] * arr [ j ] * arr [ k ] ) ;
      }
    }
  }
  return maxProduct ;
}
|||

FIND_MAXIMUM_SUM_POSSIBLE_EQUAL_SUM_THREE_STACKS

public static int f_gold ( int [ ] stack1 , int [ ] stack2 , int [ ] stack3 , int n1 , int n2 , int n3 ) {
  int sum1 = 0 , sum2 = 0 , sum3 = 0 ;
  for ( int i = 0 ;
  i < n1 ;
  i ++ ) sum1 += stack1 [ i ] ;
  for ( int i = 0 ;
  i < n2 ;
  i ++ ) sum2 += stack2 [ i ] ;
  for ( int i = 0 ;
  i < n3 ;
  i ++ ) sum3 += stack3 [ i ] ;
  int top1 = 0 , top2 = 0 , top3 = 0 ;
  int ans = 0 ;
  while ( ( 1 ) {
    if ( ( top1 == n1 || top2 == n2 || top3 == n3 ) && ( sum1 == sum2 && sum2 == sum3 ) ) return 0 ;
    if ( ( sum1 == sum2 && sum1 >= sum3 ) || ( sum2 >= sum3 && sum2 >= sum3 ) ) {
      sum1 -= stack1 [ top1 ] ;
      top1 = top1 + 1 ;
    }
    else if ( ( sum2 >= sum3 && sum2 >= sum3 ) || ( sum3 >= sum2 && sum3 >= sum1 ) ) {
      sum2 -= stack2 [ top2 ] ;
      top2 = top2 + 1 ;
    }
    else if ( ( sum3 >= sum2 && sum3 >= sum1 ) || ( sum3 >= sum3 && sum3 >= sum1 ) ) {
      sum3 -= stack3 [ top3 ] ;
      top3 = top3 + 1 ;
    }
  }
  return ans ;
}
|||

FIND_MINIMUM_DIFFERENCE_PAIR_1

public static int fGold ( int [ ] arr , int n ) {
  Arrays . sort ( arr ) ;
  int diff = 10 * 20 ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    if ( arr [ i + 1 ] - arr [ i ] < diff ) {
      diff = arr [ i + 1 ] - arr [ i ] ;
    }
  }
  return diff ;
}
|||

FIND_NUMBER_TIMES_STRING_OCCURS_GIVEN_STRING_1

public static int f_gold ( int [ ] a , int [ ] b ) {
  int m = a . length ;
  int n = b . length ;
  int [ ] [ ] lookup = new int [ m + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) lookup [ 0 ] [ i ] = 0 ;
  for ( int i = 0 ;
  i < m + 1 ;
  i ++ ) lookup [ i ] [ 0 ] = 1 ;
  for ( int i = 1 ;
  i < m ;
  i ++ ) {
    for ( int j = 1 ;
    j < n ;
    j ++ ) {
      if ( a [ i - 1 ] == b [ j - 1 ] ) lookup [ i ] [ j ] = lookup [ i - 1 ] [ j - 1 ] + lookup [ i - 1 ] [ j ] ;
      else lookup [ i ] [ j ] = lookup [ i - 1 ] [ j ] ;
    }
  }
  return lookup [ m ] [ n ] ;
}
|||

FIND_ONE_EXTRA_CHARACTER_STRING_1

public static byte fGold ( String strA , String strB ) {
  int res = 0 ;
  for ( int i = 0 ;
  i < strA . length ( ) ;
  i ++ ) {
    res = res ^ ( ( byte ) strA . charAt ( i ) ) ;
  }
  for ( int i = 0 ;
  i < strB . length ( ) ;
  i ++ ) {
    res = res ^ ( ( byte ) strB . charAt ( i ) ) ;
  }
  return ( ( byte ) res ) ;
  ;
}
|||

FIND_PERIMETER_CYLINDER

public static int fGold ( int diameter , int height ) {
  return 2 * ( diameter + height ) ;
}
|||

FIND_REPETITIVE_ELEMENT_1_N_1

public static int fGold ( int [ ] arr , int n ) {
  return Arrays . hashCode ( arr ) - ( ( ( n - 1 ) * n ) / 2 ) ;
}
|||

FIND_SUM_EVEN_INDEX_BINOMIAL_COEFFICIENTS_1

static int f_gold ( int n ) {
  return ( 1 << ( n - 1 ) ) ;
}
|||

FIND_SUM_MODULO_K_FIRST_N_NATURAL_NUMBER

public static int f_gold ( int N , int K ) {
  int ans = 0 ;
  ;
  for ( int i = 1 ;
  i <= N ;
  i ++ ) ans += ( i % K ) ;
  ;
  return ans ;
}
|||

FIND_SUM_ODD_FACTORS_NUMBER

public static int f_gold ( int n ) {
  int res = 1 ;
  while ( n % 2 == 0 ) {
    n = n / 2 ;
  }
  for ( int i = 3 ;
  i < Integer . MAX_VALUE ;
  i ++ ) {
    int count = 0 ;
    int currSum = 1 ;
    int currTerm = 1 ;
    while ( n % i == 0 ) {
      count ++ ;
      n = n / i ;
      currTerm *= i ;
      currSum += currTerm ;
    }
    res *= currSum ;
  }
  if ( n >= 2 ) {
    res *= ( 1 + n ) ;
  }
  return res ;
}
|||

FIND_SUM_UNIQUE_SUB_ARRAY_SUM_GIVEN_ARRAY

public static int f_gold ( int [ ] arr , int n ) {
  int res = 0 ;
  Map < Integer , Integer > m = Maps . newHashMap ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int Sum = 0 ;
    for ( int j = i ;
    j < n ;
    j ++ ) {
      Sum += arr [ j ] ;
      m . put ( Sum , m . get ( Sum ) + 1 ) ;
    }
  }
  for ( int x : m . keySet ( ) ) {
    if ( m . get ( x ) == 1 ) res += x ;
  }
  return res ;
}
|||

FIND_THE_ELEMENT_BEFORE_WHICH_ALL_THE_ELEMENTS_ARE_SMALLER_THAN_IT_AND_AFTER_WHICH_ALL_ARE_GREATER_THAN_IT

public static int fGold ( int [ ] arr , int n ) {
  int [ ] leftMax = new int [ n ] ;
  leftMax [ 0 ] = Integer . MIN_VALUE ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    leftMax [ i ] = Math . max ( leftMax [ i - 1 ] , arr [ i - 1 ] ) ;
  }
  int rightMin = Integer . MIN_VALUE ;
  for ( int i = n - 1 ;
  i >= 0 ;
  i -- ) {
    if ( leftMax [ i ] < arr [ i ] && rightMin > arr [ i ] ) {
      return i ;
    }
    rightMin = Math . min ( rightMin , arr [ i ] ) ;
  }
  return - 1 ;
}
|||

FIND_THE_MAXIMUM_ELEMENT_IN_AN_ARRAY_WHICH_IS_FIRST_INCREASING_AND_THEN_DECREASING

public static int fGold ( int [ ] arr , int low , int high ) {
  int max = arr [ low ] ;
  int i ;
  for ( i = low ;
  i < high + 1 ;
  i ++ ) {
    if ( arr [ i ] > max ) {
      max = arr [ i ] ;
    }
  }
  return max ;
}
|||

FIND_THE_MISSING_NUMBER_1

static int f_gold ( int [ ] a , int n ) {
  int i , total = 0 ;
  total = 1 ;
  for ( i = 2 ;
  i <= n ;
  i ++ ) {
    total += i ;
    total -= a [ i - 2 ] ;
  }
  return total ;
}
|||

FIND_THE_MISSING_NUMBER_2

static int f_gold ( int [ ] a , int n ) {
  int x1 = a [ 0 ] ;
  int x2 = 1 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) x1 = x1 ^ a [ i ] ;
  for ( int i = 2 ;
  i < n + 2 ;
  i ++ ) x2 = x2 ^ i ;
  return x1 ^ x2 ;
}
|||

FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES

public static int f_gold ( int [ ] arr , int arrSize ) {
  for ( int i = 0 ;
  i <= arrSize ;
  i ++ ) {
    int count = 0 ;
    for ( int j = 0 ;
    j <= arrSize ;
    j ++ ) {
      if ( arr [ i ] == arr [ j ] ) {
        count ++ ;
      }
    }
    if ( ( count % 2 != 0 ) && ( count % 2 != 0 ) ) {
      return arr [ i ] ;
    }
  }
  return - 1 ;
}
|||

FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES_1

public static int f_gold ( int arr [ ] , int size ) {
  Map < Integer , Integer > Hash = Maps . newHashMap ( ) ;
  for ( int i = 0 ;
  i < size ;
  i ++ ) {
    Hash . put ( arr [ i ] , Hash . get ( arr [ i ] ) + 1 ) ;
    ;
  }
  for ( int i = 0 ;
  i < Hash . size ( ) ;
  i ++ ) {
    if ( ( Hash . get ( i ) % 2 != 0 ) && ( Hash . get ( i ) % 2 != 0 ) ) {
      return i ;
    }
  }
  return - 1 ;
}
|||

FIND_WHETHER_A_GIVEN_NUMBER_IS_A_POWER_OF_4_OR_NOT_2

static boolean f_gold ( int n ) {
  return ( n != 0 && ( ( n & ( n - 1 ) ) == 0 ) && ! ( n & 0xAAAAAAAA ) ) ;
  ;
}
|||

FIRST_UPPERCASE_LETTER_IN_A_STRING_ITERATIVE_AND_RECURSIVE

public static int f_gold ( String str ) {
  for ( int i = 0 ;
  i != str . length ( ) ;
  i ++ ) {
    if ( ( str . charAt ( i ) ) . istitle ( ) ) {
      return str . charAt ( i ) ;
    }
  }
  return 0 ;
}
|||

FLOOR_IN_A_SORTED_ARRAY_1

public static int fGold ( int [ ] arr , int low , int high , int x ) {
  if ( ( low > high ) && ( x >= arr [ high ] ) ) return - 1 ;
  if ( ( x >= arr [ high ] ) && ( x < arr [ low ] ) ) return high ;
  int mid = ( int ) ( ( low + high ) / 2 ) ;
  if ( ( arr [ mid ] == x ) && ( arr [ mid - 1 ] <= x && x < arr [ mid ] ) ) return mid - 1 ;
  if ( ( x < arr [ mid ] ) && ( x > arr [ mid ] ) ) return fGold ( arr , low , mid - 1 , x ) ;
  return fGold ( arr , mid + 1 , high , x ) ;
}
|||

FUNCTION_COPY_STRING_ITERATIVE_RECURSIVE_1

public static void fGold ( String s1 , String s2 , int index ) {
  s2 . charAt ( index ) = s1 . charAt ( index ) ;
  ;
  if ( ( index == s1 . length ( ) - 1 ) && ( index < s2 . length ( ) ) ) return ;
  ;
  fGold ( s1 , s2 , index + 1 ) ;
  ;
}
|||

GIVEN_LARGE_NUMBER_CHECK_SUBSEQUENCE_DIGITS_DIVISIBLE_8

public static boolean f_gold ( String st ) {
  int l = st . length ( ) ;
  int arr [ ] = new int [ l ] ;
  for ( int i = 0 ;
  i <= l ;
  i ++ ) {
    for ( int j = i ;
    j <= l ;
    j ++ ) {
      for ( int k = j ;
      k <= l ;
      k ++ ) {
        if ( ( arr [ i ] % 8 == 0 ) && ( arr [ j ] % 8 == 0 ) && ( arr [ k ] % 8 == 0 ) ) {
          return true ;
        }
        else if ( ( ( arr [ i ] * 10 + arr [ j ] ) % 8 == 0 && i != j ) && ( i != j ) && ( j != k ) && ( i != k ) ) {
          return true ;
        }
      }
    }
  }
  return false ;
}
|||

GOOGLE_CASE_GIVEN_SENTENCE

public static String f_gold ( String s ) {
  int n = s . length ( ) ;
  String s1 = "" ;
  s1 = s1 + s . charAt ( 0 ) . toLowerCase ( ) ;
  int i = 1 ;
  while ( i < n ) {
    if ( ( s . charAt ( i ) == ' ' ) && i <= n ) {
      s1 = s1 + " " + ( s . charAt ( i + 1 ) ) . toLowerCase ( ) ;
      i = i + 1 ;
    }
    else {
      s1 = s1 + ( s . charAt ( i ) ) . toUpperCase ( ) ;
    }
    i = i + 1 ;
  }
  return s1 ;
}
|||

HEIGHT_COMPLETE_BINARY_TREE_HEAP_N_NODES

public static int f_gold ( int N ) {
  return Math . ceil ( Math . log2 ( N + 1 ) ) - 1 ;
}
|||

HEXAGONAL_NUMBER

static int f_gold ( int n ) {
  return n * ( 2 * n - 1 ) ;
}
|||

HOW_CAN_WE_SUM_THE_DIGITS_OF_A_GIVEN_NUMBER_IN_SINGLE_STATEMENT_2

public static int fGold ( int no ) {
  return no == 0 ? 0 : ( int ) ( no % 10 ) + fGold ( ( int ) ( no / 10 ) ) ;
}
|||

HOW_TO_CHECK_IF_A_GIVEN_ARRAY_REPRESENTS_A_BINARY_HEAP

public static boolean fGold ( int [ ] arr , int i , int n ) {
  if ( i > ( int ) ( ( n - 2 ) / 2 ) ) return true ;
  if ( ( arr [ i ] >= arr [ 2 * i + 1 ] && arr [ i ] >= arr [ 2 * i + 2 ] && fGold ( arr , 2 * i + 1 , n ) && fGold ( arr , 2 * i + 2 , n ) ) ) return true ;
  return false ;
}
|||

HOW_TO_CHECK_IF_A_GIVEN_ARRAY_REPRESENTS_A_BINARY_HEAP_1

public static boolean fGold ( int [ ] arr , int n ) {
  for ( int i = 0 ;
  i < ( int ) ( ( n - 2 ) / 2 ) + 1 ;
  i ++ ) {
    if ( arr [ 2 * i + 1 ] > arr [ i ] ) return false ;
    if ( ( 2 * i + 2 < n && arr [ 2 * i + 2 ] > arr [ i ] ) || ( 2 * i + 2 < n && arr [ 2 * i + 2 ] > arr [ i + 1 ] ) ) return false ;
  }
  return true ;
}
|||

HYPERCUBE_GRAPH

public static int fGold ( int n ) {
  if ( n == 1 ) return 2 ;
  return 2 * fGold ( n - 1 ) ;
}
|||

K_TH_DIGIT_RAISED_POWER_B

public static int fGold ( int a , int b , int k ) {
  int p = a * b ;
  int count = 0 ;
  while ( ( p > 0 ) && ( count < k ) ) {
    int rem = p % 10 ;
    count = count + 1 ;
    if ( ( count == k ) && ( p > 0 ) ) return rem ;
    p = p / 10 ;
    ;
  }
  return 0 ;
}
|||

K_TH_ELEMENT_TWO_SORTED_ARRAYS

public static int f_gold ( int arr1 [ ] , int arr2 [ ] , int m , int n , int k ) {
  int sorted1 [ ] = new int [ m + n ] ;
  int i = 0 ;
  int j = 0 ;
  int d = 0 ;
  while ( ( i < m && j < n ) || ( i < m && j < n ) ) {
    if ( ( arr1 [ i ] < arr2 [ j ] ) || ( arr1 [ i ] > arr2 [ j ] ) ) {
      sorted1 [ d ] = arr1 [ i ] ;
      i ++ ;
    }
    else {
      sorted1 [ d ] = arr2 [ j ] ;
      j ++ ;
    }
    d ++ ;
  }
  while ( ( i < m ) || ( i < n ) ) {
    sorted1 [ d ] = arr1 [ i ] ;
    d ++ ;
    i ++ ;
  }
  while ( ( j < n ) || ( j < m ) ) {
    sorted1 [ d ] = arr2 [ j ] ;
    d ++ ;
    j ++ ;
  }
  return sorted1 [ k - 1 ] ;
}
|||

K_TH_LARGEST_SUM_CONTIGUOUS_SUBARRAY

public static int f_gold ( int [ ] arr , int n , int k ) {
  int [ ] sum = new int [ n + 1 ] ;
  sum [ 0 ] = 0 ;
  sum [ 1 ] = arr [ 0 ] ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    sum [ i ] = sum [ i - 1 ] + arr [ i - 1 ] ;
  }
  int [ ] Q = new int [ n + 1 ] ;
  heapify ( Q ) ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int j = i ;
    j <= n ;
    j ++ ) {
      int x = sum [ j ] - sum [ i - 1 ] ;
      if ( Q . length < k ) {
        heapify ( Q , x ) ;
      }
      else {
        if ( Q [ 0 ] < x ) {
          heapify ( Q , x ) ;
          heappush ( Q , x ) ;
        }
      }
    }
  }
  return Q [ 0 ] ;
}
|||

K_TH_MISSING_ELEMENT_INCREASING_SEQUENCE_NOT_PRESENT_GIVEN_SEQUENCE

public static int fGold ( int [ ] a , int [ ] b , int k , int n1 , int n2 ) {
  Set < Integer > s = new HashSet < Integer > ( ) ;
  for ( int i = 0 ;
  i < n2 ;
  i ++ ) s . add ( b [ i ] ) ;
  int missing = 0 ;
  for ( int i = 0 ;
  i < n1 ;
  i ++ ) {
    if ( a [ i ] != s . contains ( b [ i ] ) ) missing ++ ;
    if ( missing == k ) return a [ i ] ;
  }
  return - 1 ;
}
|||

LCS_FORMED_CONSECUTIVE_SEGMENTS_LEAST_LENGTH_K

public static int f_gold ( int k , String s1 , String s2 ) {
  int n = s1 . length ( ) ;
  int m = s2 . length ( ) ;
  int [ ] [ ] lcs = new int [ m + 1 ] [ n + 1 ] ;
  int [ ] [ ] cnt = new int [ m + 1 ] [ n + 1 ] ;
  for ( int y = 0 ;
  y < n ;
  y ++ ) {
    lcs [ y ] [ 0 ] = y ;
    cnt [ y ] [ 0 ] = y ;
    cnt [ y ] [ 1 ] = y ;
  }
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int j = 1 ;
    j <= m ;
    j ++ ) {
      lcs [ i ] [ j ] = Math . max ( lcs [ i - 1 ] [ j ] , lcs [ i ] [ j - 1 ] ) ;
      if ( ( s1 . charAt ( i - 1 ) == s2 . charAt ( j - 1 ) ) && ( s1 . charAt ( i - 1 ) == s2 . charAt ( j - 1 ) ) ) {
        cnt [ i ] [ j ] = cnt [ i - 1 ] [ j - 1 ] + 1 ;
        ;
      }
      if ( ( cnt [ i ] [ j ] >= k ) && ( cnt [ i ] [ j ] <= k ) ) {
        for ( int a = k ;
        a <= cnt [ i ] [ j ] ;
        a ++ ) {
          lcs [ i ] [ j ] = Math . max ( lcs [ i ] [ j ] , lcs [ i - a ] [ j - a ] + a ) ;
        }
      }
    }
  }
  return lcs [ n ] [ m ] ;
}
|||

LONGEST_INCREASING_ODD_EVEN_SUBSEQUENCE

public static int f_gold ( int [ ] arr , int n ) {
  int [ ] lioes = Lists . newArrayList ( ) ;
  int maxLen = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    lioes . add ( 1 ) ;
  }
  int i = 1 ;
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < i ;
    j ++ ) {
      if ( ( arr [ i ] > arr [ j ] && ( arr [ i ] + arr [ j ] ) % 2 != 0 && lioes [ i ] < lioes [ j ] + 1 ) ) {
        lioes [ i ] = lioes [ j ] + 1 ;
      }
    }
  }
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    if ( maxLen < lioes [ i ] ) {
      maxLen = lioes [ i ] ;
    }
  }
  return maxLen ;
}
|||

LONGEST_PALINDROME_SUBSEQUENCE_SPACE

public static int f_gold ( String s ) {
  int n = s . length ( ) ;
  int [ ] a = new int [ n ] ;
  for ( int i = n - 1 ;
  i >= 0 ;
  i -- ) {
    int back_up = 0 ;
    for ( int j = i ;
    j < n ;
    j ++ ) {
      if ( j == i ) {
        a [ j ] = 1 ;
      }
      else if ( s . charAt ( i ) == s . charAt ( j ) ) {
        int temp = a [ j ] ;
        a [ j ] = back_up + 2 ;
        back_up = temp ;
      }
      else {
        back_up = a [ j ] ;
        a [ j ] = Math . max ( a [ j - 1 ] , a [ j ] ) ;
      }
    }
  }
  return a [ n - 1 ] ;
}
|||

LONGEST_PREFIX_ALSO_SUFFIX_1

public static int f_gold ( String s ) {
  int n = s . length ( ) ;
  int [ ] lps = new int [ n ] ;
  lps [ 0 ] = 0 ;
  int l = 0 ;
  int i = 1 ;
  while ( ( i < n ) && ( i < s . length ( ) ) ) {
    if ( ( s . charAt ( i ) == s . charAt ( l ) ) || ( s . charAt ( i ) == s . charAt ( l ) ) ) {
      l = l + 1 ;
      lps [ i ] = l ;
      i = i + 1 ;
    }
    else {
      if ( ( l != 0 ) && ( l < lps [ l - 1 ] ) ) {
        l = lps [ l - 1 ] ;
      }
      else {
        lps [ i ] = 0 ;
        i = i + 1 ;
      }
    }
  }
  int res = lps [ n - 1 ] ;
  if ( ( res > n / 2 ) || ( res < 0 ) ) {
    return n / 2 ;
  }
  else {
    return res ;
  }
}
|||

MAKING_ELEMENTS_OF_TWO_ARRAYS_SAME_WITH_MINIMUM_INCREMENTDECREMENT

public static int f_gold ( int [ ] a , int [ ] b , int n ) {
  Arrays . sort ( a , 0 , n ) ;
  Arrays . sort ( b , 0 , n ) ;
  int result = 0 ;
  for ( int i = 0 ;
  i < n ;
  i += 1 ) {
    if ( ( a [ i ] > b [ i ] ) && ( a [ i ] < b [ i ] ) ) {
      result = result + Math . abs ( a [ i ] - b [ i ] ) ;
    }
    else if ( ( a [ i ] < b [ i ] ) && ( a [ i ] > b [ i ] ) ) {
      result = result + Math . abs ( a [ i ] - b [ i ] ) ;
    }
  }
  return result ;
}
|||

MARKOV_MATRIX

public static boolean f_gold ( int [ ] [ ] m ) {
  for ( int i = 0 ;
  i != m . length ;
  i ++ ) {
    int sm = 0 ;
    for ( int j = 0 ;
    j != m [ i ] . length ;
    j ++ ) {
      sm = sm + m [ i ] [ j ] ;
    }
    if ( ( sm != 1 ) && ( sm != 0 ) ) return false ;
  }
  return true ;
}
|||

MAXIMIZE_SUM_CONSECUTIVE_DIFFERENCES_CIRCULAR_ARRAY

public static int f_gold ( int [ ] arr , int n ) {
  int sum = 0 ;
  Arrays . sort ( arr ) ;
  for ( int i = 0 ;
  i <= ( int ) ( n / 2 ) ;
  i ++ ) {
    sum -= ( 2 * arr [ i ] ) ;
    sum += ( 2 * arr [ n - i - 1 ] ) ;
  }
  return sum ;
}
|||

MAXIMUM_AREA_RECTANGLE_PICKING_FOUR_SIDES_ARRAY_1

public static int f_gold ( int [ ] arr , int n ) {
  int [ ] s = new int [ n ] ;
  int first = 0 ;
  int second = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] != 0 ) {
      s [ i ] = arr [ i ] ;
      continue ;
    }
    if ( ( arr [ i ] > first ) && ( arr [ i ] < second ) ) {
      second = first ;
      first = arr [ i ] ;
    }
    else if ( ( arr [ i ] > second ) && ( arr [ i ] < first ) ) {
      second = arr [ i ] ;
    }
  }
  return ( first * second ) ;
}
|||

MAXIMUM_AVERAGE_SUM_PARTITION_ARRAY

public static int f_gold ( int [ ] A , int K ) {
  int n = A . length ;
  ;
  int [ ] preSum = new int [ n + 1 ] ;
  preSum [ 0 ] = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) preSum [ i + 1 ] = preSum [ i ] + A [ i ] ;
  ;
  int [ ] dp = new int [ n ] ;
  int sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) dp [ i ] = ( preSum [ n ] - preSum [ i ] ) / ( n - i ) ;
  ;
  for ( int k = 0 ;
  k < K - 1 ;
  k ++ ) {
    for ( int i = 0 ;
    i < n ;
    i ++ ) {
      for ( int j = i + 1 ;
      j < n ;
      j ++ ) {
        dp [ i ] = Math . max ( dp [ i ] , ( preSum [ j ] - preSum [ i ] ) / ( j - i ) + dp [ j ] ) ;
      };
    }
  }
  return ( int ) dp [ 0 ] ;
}
|||

MAXIMUM_BINOMIAL_COEFFICIENT_TERM_VALUE

public static int f_gold ( int n ) {
  int [ ] [ ] C = new int [ n + 1 ] [ n + 1 ] ;
  ;
  for ( int i = 0 ;
  i < n + 1 ;
  i ++ ) {
    for ( int j = 0 ;
    j < Math . min ( i , n ) + 1 ;
    j ++ ) {
      if ( ( j == 0 || j == i ) && ( C [ i ] [ j ] == 0 ) ) {
        C [ i ] [ j ] = 1 ;
      };
    }
    else {
      C [ i ] [ j ] = ( C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ] ) ;
    }
  }
  int maxvalue = 0 ;
  ;
  for ( int i = 0 ;
  i < n + 1 ;
  i ++ ) {
    maxvalue = Math . max ( maxvalue , C [ n ] [ i ] ) ;
  };
  return maxvalue ;
}
|||

MAXIMUM_CONSECUTIVE_REPEATING_CHARACTER_STRING_1

public static String f_gold ( String str ) {
  int n = str . length ( ) ;
  int count = 0 ;
  String res = str . substring ( 0 , 1 ) ;
  int curCount = 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( i < n - 1 && str . charAt ( i ) == str . charAt ( i + 1 ) ) || ( i < n - 1 && str . charAt ( i + 1 ) == str . charAt ( i + 2 ) ) ) {
      curCount ++ ;
    }
    else {
      if ( curCount > count ) {
        count = curCount ;
        res = str . substring ( i , i + 1 ) ;
      }
      curCount = 1 ;
    }
  }
  return res ;
}
|||

MAXIMUM_DIFFERENCE_SUM_ELEMENTS_TWO_ROWS_MATRIX

public static int f_gold ( int [ ] [ ] mat , int m , int n ) {
  int [ ] rowSum = new int [ m ] ;
  for ( int i = 0 ;
  i <= m ;
  i ++ ) {
    int sum = 0 ;
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      sum += mat [ i ] [ j ] ;
    }
    rowSum [ i ] = sum ;
  }
  int maxDiff = rowSum [ 1 ] - rowSum [ 0 ] ;
  int minElement = rowSum [ 0 ] ;
  for ( int i = 1 ;
  i <= m ;
  i ++ ) {
    if ( ( rowSum [ i ] - minElement > maxDiff ) && ( rowSum [ i ] < minElement ) ) {
      maxDiff = rowSum [ i ] - minElement ;
    }
    if ( ( rowSum [ i ] < minElement ) && ( rowSum [ i ] > maxDiff ) && ( rowSum [ i ] > minElement ) ) {
      minElement = rowSum [ i ] ;
    }
  }
  return maxDiff ;
}
|||

MAXIMUM_GAMES_PLAYED_WINNER

public static int f_gold ( int N ) {
  int [ ] dp = new int [ N ] ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) dp [ i ] = 0 ;
  dp [ 0 ] = 1 ;
  dp [ 1 ] = 2 ;
  int i = 1 ;
  while ( dp [ i ] <= N ) {
    i = i + 1 ;
    dp [ i ] = dp [ i - 1 ] + dp [ i - 2 ] ;
  }
  return ( i - 1 ) ;
}
|||

MAXIMUM_HEIGHT_OF_TRIANGULAR_ARRANGEMENT_OF_ARRAY_VALUES

public static int f_gold ( int a , int n ) {
  int result = 1 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    int y = ( i * ( i + 1 ) ) / 2 ;
    if ( ( y < n ) && ( y > 0 ) ) {
      result = i ;
    }
    else {
      break ;
    }
  }
  return result ;
}
|||

MAXIMUM_LENGTH_PREFIX_ONE_STRING_OCCURS_SUBSEQUENCE_ANOTHER

public static int f_gold ( String s , String t ) {
  int count = 0 ;
  for ( int i = 0 ;
  ;
  i ++ ) {
    if ( ( count == s . length ( ) ) && ( t . charAt ( i ) == s . charAt ( count ) ) ) {
      break ;
    }
    if ( ( t . charAt ( i ) == s . charAt ( count ) ) && ( t . charAt ( i + 1 ) == s . charAt ( count ) ) ) {
      count = count + 1 ;
    }
  }
  return count ;
}
|||

MAXIMUM_NUMBER_CHOCOLATES_DISTRIBUTED_EQUALLY_AMONG_K_STUDENTS

public static int f_gold ( int [ ] arr , int n , int k ) {
  int [ ] um = new int [ n ] , currRem = 0 , maxSum = 0 ;
  int [ ] sm = new int [ n ] ;
  sm [ 0 ] = arr [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) sm [ i ] = sm [ i - 1 ] + arr [ i ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    currRem = sm [ i ] % k ;
    if ( ( ! currRem && maxSum < sm [ i ] ) || ( ! currRem && maxSum < um [ currRem ] ) ) maxSum = sm [ i ] ;
    else if ( ( ! currRem && maxSum < um [ currRem ] ) || ( ! currRem && maxSum < um [ currRem ] ) ) um [ currRem ] = i ;
    else if ( ( maxSum < ( sm [ i ] - sm [ um [ currRem ] ] ) ) || ( ! currRem && maxSum < um [ currRem ] ) ) maxSum = sm [ i ] - sm [ um [ currRem ] ] ;
  }
  return maxSum / k ;
}
|||

MAXIMUM_NUMBER_OF_SQUARES_THAT_CAN_BE_FIT_IN_A_RIGHT_ANGLE_ISOSCELES_TRIANGLE

public static double fGold ( double b , double m ) {
  return ( b / m - 1 ) * ( b / m ) / 2 ;
}
|||

MAXIMUM_PRODUCT_INCREASING_SUBSEQUENCE

public static int f_gold ( int [ ] arr , int n ) {
  int [ ] mpis = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) mpis [ i ] = arr [ i ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < i ;
    j ++ ) {
      if ( ( arr [ i ] > arr [ j ] && mpis [ i ] < ( mpis [ j ] * arr [ i ] ) ) || ( arr [ i ] > arr [ j ] && mpis [ i ] < ( mpis [ j ] * arr [ i ] ) ) ) {
        mpis [ i ] = mpis [ j ] * arr [ i ] ;
      }
    }
  }
  return Math . max ( mpis ) ;
}
|||

MAXIMUM_PRODUCT_OF_4_ADJACENT_ELEMENTS_IN_MATRIX

public static int f_gold ( int [ ] [ ] arr , int n ) {
  int max = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( ( ( j - 3 ) >= 0 ) && ( ( j - 3 ) < n ) ) {
        int result = ( arr [ i ] [ j ] * arr [ i ] [ j - 1 ] * arr [ i ] [ j - 2 ] * arr [ i ] [ j - 3 ] ) ;
        if ( ( max < result ) && ( max < result ) ) max = result ;
      }
      if ( ( ( i - 3 ) >= 0 ) && ( ( i - 3 ) < n ) ) {
        int result = ( arr [ i ] [ j ] * arr [ i - 1 ] [ j ] * arr [ i - 2 ] [ j ] * arr [ i - 3 ] [ j ] ) ;
        if ( ( max < result ) && ( max < result ) ) max = result ;
      }
      if ( ( ( i - 3 ) >= 0 ) && ( ( j - 3 ) >= 0 ) ) {
        int result = ( arr [ i ] [ j ] * arr [ i - 1 ] [ j - 1 ] * arr [ i - 2 ] [ j - 2 ] * arr [ i - 3 ] [ j - 3 ] ) ;
        if ( ( max < result ) && ( max < result ) ) max = result ;
      }
    }
  }
  return max ;
}
|||

MAXIMUM_PRODUCT_SUBSET_ARRAY

public static int f_gold ( int [ ] a , int n ) {
  if ( n == 1 ) return a [ 0 ] ;
  long maxNeg = - 999999999999 ;
  int countNeg = 0 ;
  int countZero = 0 ;
  long prod = 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( a [ i ] == 0 ) {
      countZero ++ ;
      continue ;
    }
    if ( a [ i ] < 0 ) {
      countNeg ++ ;
      maxNeg = Math . max ( maxNeg , a [ i ] ) ;
    }
    prod = prod * a [ i ] ;
  }
  if ( countZero == n ) return 0 ;
  if ( countNeg & 1 ) {
    if ( ( countNeg == 1 && countZero > 0 && countZero + countNeg == n ) || ( countNeg == 0 && countZero + countNeg == n ) ) return 0 ;
    prod = ( int ) ( prod / maxNeg ) ;
  }
  return prod ;
}
|||

MAXIMUM_SUM_IARRI_AMONG_ROTATIONS_GIVEN_ARRAY

public static int f_gold ( int [ ] arr , int n ) {
  int res = - Integer . MAX_VALUE ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    int currSum = 0 ;
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      int index = ( int ) ( ( i + j ) % n ) ;
      currSum += j * arr [ index ] ;
    }
    res = Math . max ( res , currSum ) ;
  }
  return res ;
}
|||

MAXIMUM_SUM_PAIRS_SPECIFIC_DIFFERENCE_1

public static int f_gold ( int [ ] arr , int N , int k ) {
  int maxSum = 0 ;
  ;
  Arrays . sort ( arr ) ;
  ;
  int i = N - 1 ;
  ;
  while ( ( i >= 0 ) && ( arr [ i ] - arr [ i - 1 ] < k ) ) {
    if ( ( arr [ i ] - arr [ i - 1 ] < k ) && ( arr [ i - 1 ] - arr [ i - 1 ] < k ) ) {
      maxSum += arr [ i ] ;
      ;
      maxSum += arr [ i - 1 ] ;
      ;
      i -- ;
    }
    i -- ;
  };
  return maxSum ;
}
|||

MAXIMUM_SUM_SUBSEQUENCE_LEAST_K_DISTANT_ELEMENTS

public static int f_gold ( int [ ] arr , int N , int k ) {
  int [ ] MS = new int [ N ] ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) MS [ N - 1 ] = arr [ N - 1 ] ;
  for ( int i = N - 2 ;
  i >= 0 ;
  i -- ) {
    if ( ( i + k + 1 >= N ) && ( MS [ i ] == 0 ) ) MS [ i ] = Math . max ( arr [ i ] , MS [ i + 1 ] ) ;
    else MS [ i ] = Math . max ( arr [ i ] + MS [ i + k + 1 ] , MS [ i + 1 ] ) ;
  }
  return MS [ 0 ] ;
}
|||

MAXIMUM_WEIGHT_PATH_ENDING_ELEMENT_LAST_ROW_MATRIX

public static int f_gold ( int [ ] [ ] mat , int N ) {
  int [ ] [ ] dp = new int [ N ] [ N ] ;
  for ( int j = 0 ;
  j < N ;
  j ++ ) dp [ j ] [ j ] = 0 ;
  dp [ 0 ] [ 0 ] = mat [ 0 ] [ 0 ] ;
  for ( int i = 1 ;
  i < N ;
  i ++ ) dp [ i ] [ 0 ] = mat [ i ] [ 0 ] + dp [ i - 1 ] [ 0 ] ;
  for ( int i = 1 ;
  i < N ;
  i ++ ) for ( int j = 1 ;
  j < Math . min ( i + 1 , N ) ;
  j ++ ) dp [ i ] [ j ] = mat [ i ] [ j ] + Math . max ( dp [ i - 1 ] [ j - 1 ] , dp [ i - 1 ] [ j ] ) ;
  int result = 0 ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) if ( ( result < dp [ N - 1 ] [ i ] ) && ( result > dp [ N - 1 ] [ i ] ) ) result = dp [ N - 1 ] [ i ] ;
  return result ;
}
|||

MINIMIZE_SUM_PRODUCT_TWO_ARRAYS_PERMUTATIONS_ALLOWED

public static double fGold ( double [ ] A , double [ ] B , int n ) {
  Arrays . sort ( A ) ;
  Arrays . sort ( B ) ;
  double result = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    result += ( A [ i ] * B [ n - i - 1 ] ) ;
  }
  return result ;
}
|||

MINIMUM_CHARACTERS_ADDED_FRONT_MAKE_STRING_PALINDROME

public static boolean f_gold ( String s ) {
  int l = s . length ( ) ;
  int i = 0 ;
  int j = l - 1 ;
  while ( i <= j ) {
    if ( ( s . charAt ( i ) != s . charAt ( j ) ) && ( s . charAt ( i ) != s . charAt ( j ) ) ) {
      return false ;
    }
    i ++ ;
    j -- ;
  }
  return true ;
}
|||

MINIMUM_COST_FOR_ACQUIRING_ALL_COINS_WITH_K_EXTRA_COINS_ALLOWED_WITH_EVERY_COIN

public static int fGold ( int [ ] coin , int n , int k ) {
  Arrays . sort ( coin ) ;
  int coinsNeeded = Math . ceil ( 1.0 * n / ( k + 1 ) ) ;
  ;
  int ans = 0 ;
  for ( int i = 0 ;
  i < coinsNeeded - 1 + 1 ;
  i ++ ) {
    ans += coin [ i ] ;
  }
  return ans ;
}
|||

MINIMUM_COST_MAKE_ARRAY_SIZE_1_REMOVING_LARGER_PAIRS

static double f_gold ( double [ ] a , int n ) {
  return ( ( n - 1 ) * Math . min ( a , a . length ) ) ;
}
|||

MINIMUM_DIFFERENCE_BETWEEN_GROUPS_OF_SIZE_TWO

public static int f_gold ( int [ ] a , int n ) {
  Arrays . sort ( a ) ;
  ;
  int [ ] s = new int [ n ] ;
  ;
  int i = 0 ;
  int j = n - 1 ;
  while ( ( i < j ) && ( i < n ) ) {
    s [ i ] = ( a [ i ] + a [ j ] ) ;
    i ++ ;
    j -- ;
  }
  int mini = Math . min ( s ) ;
  int maxi = Math . max ( s ) ;
  return Math . abs ( maxi - mini ) ;
}
|||

MINIMUM_DIFFERENCE_MAX_MIN_K_SIZE_SUBSETS

public static int fGold ( int [ ] arr , int N , int K ) {
  Arrays . sort ( arr ) ;
  int res = 2147483647 ;
  for ( int i = 0 ;
  i < ( N - K ) + 1 ;
  i ++ ) {
    int curSeqDiff = arr [ i + K - 1 ] - arr [ i ] ;
    res = Math . min ( res , curSeqDiff ) ;
  }
  return res ;
}
|||

MINIMUM_FLIP_REQUIRED_MAKE_BINARY_MATRIX_SYMMETRIC_1

public static int f_gold ( int [ ] [ ] mat , int n ) {
  int flip = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < i ;
    j ++ ) {
      if ( mat [ i ] [ j ] != mat [ j ] [ i ] ) {
        flip ++ ;
      }
    }
  }
  return flip ;
}
|||

MINIMUM_INCREMENT_K_OPERATIONS_MAKE_ELEMENTS_EQUAL

public static int fGold ( int [ ] arr , int n , int k ) {
  int max1 = max ( arr ) ;
  double res = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( ( max1 - arr [ i ] ) % k != 0 ) && ( ( max1 - arr [ i ] ) / k != 0 ) ) {
      return - 1 ;
    }
    else {
      res += ( max1 - arr [ i ] ) / k ;
    }
  }
  return ( int ) res ;
}
|||

MINIMUM_LENGTH_SUBARRAY_SUM_GREATER_GIVEN_VALUE_1

public static int f_gold ( int [ ] arr , int n , int x ) {
  int currSum = 0 ;
  ;
  int minLen = n + 1 ;
  ;
  int start = 0 ;
  int end = 0 ;
  while ( ( end < n ) && ( currSum <= x && end < n ) ) {
    while ( ( currSum <= 0 && x > 0 ) || ( currSum <= x && x < n ) ) {
      if ( ( currSum <= 0 && x > 0 ) || ( currSum <= x && x < n ) ) {
        start = end ;
        currSum = 0 ;
      }
      currSum += arr [ end ] ;
      end ++ ;
    }
    while ( ( currSum > x && start < n ) || ( currSum > x && start < n ) ) {
      if ( ( end - start < minLen ) || ( end - start < minLen ) ) {
        minLen = end - start ;
      }
      currSum -= arr [ start ] ;
      start ++ ;
    }
  }
  return minLen ;
}
|||

MINIMUM_NUMBER_PLATFORMS_REQUIRED_RAILWAYBUS_STATION

public static int f_gold ( int [ ] arr , int [ ] dep , int n ) {
  Arrays . sort ( arr ) ;
  Arrays . sort ( dep ) ;
  int platNeeded = 1 ;
  int result = 1 ;
  int i = 1 ;
  int j = 0 ;
  while ( ( i < n ) && ( j < n ) ) {
    if ( ( arr [ i ] < dep [ j ] ) && ( arr [ i ] > dep [ j ] ) ) {
      platNeeded ++ ;
      i ++ ;
      if ( ( platNeeded > result ) && ( arr [ i ] > dep [ j ] ) ) {
        result = platNeeded ;
      }
    }
    else {
      platNeeded -- ;
      j ++ ;
    }
  }
  return result ;
}
|||

MINIMUM_PRODUCT_SUBSET_ARRAY

public static int f_gold ( int [ ] a , int n ) {
  if ( ( n == 1 ) || ( n == 0 ) ) return a [ 0 ] ;
  long maxNeg = Long . MAX_VALUE ;
  long minPos = Long . MIN_VALUE ;
  int countNeg = 0 ;
  int countZero = 0 ;
  long prod = 1 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( a [ i ] == 0 ) && ( a [ i ] > 0 ) ) {
      countZero = countZero + 1 ;
      continue ;
    }
    if ( ( a [ i ] < 0 ) && ( a [ i ] > 0 ) ) {
      countNeg = countNeg + 1 ;
      maxNeg = Math . max ( maxNeg , a [ i ] ) ;
    }
    if ( ( a [ i ] > 0 ) && ( a [ i ] < 0 ) ) {
      minPos = Math . min ( minPos , a [ i ] ) ;
    }
    prod = prod * a [ i ] ;
  }
  if ( ( countZero == n || ( countNeg == 0 && countZero > 0 ) ) && ( countNeg == 0 ) ) return 0 ;
  ;
  if ( ( countNeg == 0 ) || ( countNeg == n ) ) return minPos ;
  ;
  if ( ( ( countNeg & 1 ) == 0 && countNeg != 0 ) ) prod = ( int ) ( prod / maxNeg ) ;
  ;
  return prod ;
}
|||

MINIMUM_ROTATIONS_UNLOCK_CIRCULAR_LOCK

public static int fGoldenCode ( int input , int unlockCode ) {
  int rotation = 0 ;
  ;
  while ( ( input > 0 || unlockCode > 0 ) && ( input < 0 || unlockCode < 0 ) ) {
    int inputDigit = input % 10 ;
    ;
    int codeDigit = unlockCode % 10 ;
    rotation += Math . min ( Math . abs ( inputDigit - codeDigit ) , 10 - Math . abs ( inputDigit - codeDigit ) ) ;
    input = ( int ) ( input / 10 ) ;
    unlockCode = ( int ) ( unlockCode / 10 ) ;
  }
  return rotation ;
}
|||

MINIMUM_SUM_SUBSEQUENCE_LEAST_ONE_EVERY_FOUR_CONSECUTIVE_ELEMENTS_PICKED_1

public static int f_gold ( int [ ] ar , int n ) {
  if ( ( n <= 4 ) && ( ar [ 0 ] == 0 ) && ( ar [ 1 ] == 0 ) && ( ar [ 2 ] == 0 ) && ( ar [ 3 ] == 0 ) ) return Math . min ( ar ) ;
  int [ ] sum = new int [ n ] ;
  sum [ 0 ] = ar [ 0 ] ;
  sum [ 1 ] = ar [ 1 ] ;
  sum [ 2 ] = ar [ 2 ] ;
  sum [ 3 ] = ar [ 3 ] ;
  for ( int i = 4 ;
  i < n ;
  i ++ ) sum [ i ] = ar [ i ] + Math . min ( sum [ i - 4 ] , sum [ i - 4 ] ) ;
  return Math . min ( sum [ n - 4 ] , sum [ n - 4 ] ) ;
}
|||

MINIMUM_SUM_TWO_NUMBERS_FORMED_DIGITS_ARRAY_2

public static int f_gold ( int [ ] a , int n ) {
  Arrays . sort ( a ) ;
  int num1 = 0 , num2 = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( i % 2 == 0 ) num1 = num1 * 10 + a [ i ] ;
    else num2 = num2 * 10 + a [ i ] ;
  }
  return num2 + num1 ;
}
|||

MINIMUM_SWAPS_REQUIRED_BRING_ELEMENTS_LESS_EQUAL_K_TOGETHER

public static int f_gold ( int arr [ ] , int n , int k ) {
  int count = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( arr [ i ] <= k ) && ( arr [ i ] > k ) ) {
      count = count + 1 ;
    }
  }
  int bad = 0 ;
  for ( int i = 0 ;
  i <= count ;
  i ++ ) {
    if ( ( arr [ i ] > k ) && ( arr [ i ] > k ) ) {
      bad = bad + 1 ;
    }
  }
  int ans = bad ;
  int j = count ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( j == n ) && ( arr [ i ] > k ) && ( arr [ i ] > k ) ) {
      bad = bad - 1 ;
    }
    if ( ( arr [ j ] > k ) && ( arr [ j ] > k ) ) {
      bad = bad + 1 ;
    }
    ans = Math . min ( ans , bad ) ;
    j = j + 1 ;
  }
  return ans ;
}
|||

MINIMUM_TIME_TO_FINISH_TASKS_WITHOUT_SKIPPING_TWO_CONSECUTIVE

public static int f_gold ( int [ ] arr , int n ) {
  if ( ( n <= 0 ) || ( n > n ) ) return 0 ;
  int incl = arr [ 0 ] ;
  int excl = 0 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    int inclNew = arr [ i ] + Math . min ( excl , incl ) ;
    exclNew = incl ;
    incl = inclNew ;
    excl = exclNew ;
  }
  return Math . min ( incl , excl ) ;
}
|||

MINIMUM_TIME_WRITE_CHARACTERS_USING_INSERT_DELETE_COPY_OPERATION

public static int f_gold ( int N , int insrt , int remov , int cpy ) {
  if ( N == 0 ) return 0 ;
  if ( N == 1 ) return insrt ;
  int [ ] dp = new int [ N + 1 ] ;
  for ( int i = 1 ;
  i <= N ;
  i ++ ) {
    if ( i % 2 == 0 ) dp [ i ] = Math . min ( dp [ i - 1 ] + insrt , dp [ i / 2 ] + cpy ) ;
    else dp [ i ] = Math . min ( dp [ i - 1 ] + insrt , dp [ ( i + 1 ) / 2 ] + cpy + remov ) ;
  }
  return dp [ N ] ;
}
|||

MOBILE_NUMERIC_KEYPAD_PROBLEM

public static int f_gold ( boolean keypad , int n ) {
  if ( ( ! keypad ) || n <= 0 ) return 0 ;
  if ( ( n == 1 ) ) return 10 ;
  int [ ] odd = new int [ 10 ] ;
  int [ ] even = new int [ 10 ] ;
  int i = 0 ;
  int j = 0 ;
  int useOdd = 0 ;
  int totalCount = 0 ;
  for ( i = 0 ;
  i < 10 ;
  i ++ ) odd [ i ] = 1 ;
  for ( j = 2 ;
  j <= n ;
  j ++ ) {
    useOdd = 1 - useOdd ;
    if ( ( useOdd == 1 ) && ( odd [ 0 ] == odd [ 8 ] ) ) {
      even [ 0 ] = odd [ 0 ] + odd [ 8 ] ;
      even [ 1 ] = odd [ 1 ] + odd [ 2 ] + odd [ 4 ] ;
      even [ 2 ] = odd [ 2 ] + odd [ 1 ] + odd [ 3 ] + odd [ 5 ] ;
      even [ 3 ] = odd [ 3 ] + odd [ 2 ] + odd [ 6 ] ;
      even [ 4 ] = odd [ 4 ] + odd [ 1 ] + odd [ 5 ] + odd [ 7 ] ;
      even [ 5 ] = odd [ 5 ] + odd [ 2 ] + odd [ 4 ] + odd [ 8 ] + odd [ 6 ] ;
      even [ 6 ] = odd [ 6 ] + odd [ 3 ] + odd [ 5 ] + odd [ 9 ] ;
      even [ 7 ] = odd [ 7 ] + odd [ 4 ] + odd [ 8 ] ;
      even [ 8 ] = odd [ 8 ] + odd [ 0 ] + odd [ 5 ] + odd [ 7 ] + odd [ 9 ] ;
      even [ 9 ] = odd [ 9 ] + odd [ 6 ] + odd [ 8 ] ;
    }
    else {
      odd [ 0 ] = even [ 0 ] + even [ 8 ] ;
      odd [ 1 ] = even [ 1 ] + even [ 2 ] + even [ 4 ] ;
      odd [ 2 ] = even [ 2 ] + even [ 1 ] + even [ 3 ] + even [ 5 ] ;
      odd [ 3 ] = even [ 3 ] + odd [ 2 ] + odd [ 6 ] ;
      even [ 4 ] = odd [ 4 ] + odd [ 1 ] + odd [ 5 ] + odd [ 7 ] ;
      even [ 5 ] = odd [ 5 ] + odd [ 2 ] + odd [ 8 ] ;
    }
    totalCount += even [
|||

MULTIPLY_AN_INTEGER_WITH_3_5

static int f_gold ( int x ) {
  return ( x << 1 ) + x + ( x >> 1 ) ;
}
|||

NUMBER_IS_DIVISIBLE_BY_29_OR_NOT

public static boolean fGold ( int n ) {
  while ( ( int ) ( n / 100 ) != 0 ) {
    int lastDigit = ( int ) ( n % 10 ) ;
    n = ( int ) ( n / 10 ) ;
    n += lastDigit * 3 ;
  }
  return ( n % 29 == 0 ) ;
}
|||

NUMBER_N_DIGIT_STEPPING_NUMBERS

public static int f_gold ( int n ) {
  int [ ] [ ] dp = new int [ 10 ] [ n + 1 ] ;
  for ( int y = 0 ;
  y < n ;
  y ++ ) {
    dp [ y ] [ y ] = 0 ;
  };
  if ( ( n == 1 ) && ( n > 0 ) ) return 10 ;
  ;
  for ( int j = 0 ;
  j < 10 ;
  j ++ ) dp [ 1 ] [ j ] = 1 ;
  ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j < 10 ;
    j ++ ) {
      if ( ( j == 0 ) && ( j > 0 ) ) dp [ i ] [ j ] = dp [ i - 1 ] [ j + 1 ] ;
      else if ( ( j == 9 ) && ( j > 0 ) ) dp [ i ] [ j ] = dp [ i - 1 ] [ j - 1 ] ;
      else dp [ i ] [ j ] = ( dp [ i - 1 ] [ j - 1 ] + dp [ i - 1 ] [ j + 1 ] ) ;
      ;
    }
  }
  int sum = 0 ;
  ;
  for ( int j = 1 ;
  j <= 10 ;
  j ++ ) sum = sum + dp [ n ] [ j ] ;
  ;
  return sum ;
}
|||

NUMBER_OF_SUBSTRINGS_WITH_ODD_DECIMAL_VALUE_IN_A_BINARY_STRING

public static int f_gold ( String s ) {
  int n = s . length ( ) ;
  int [ ] auxArr = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    auxArr [ i ] = 0 ;
  }
  if ( ( s . charAt ( 0 ) == '1' ) || ( s . charAt ( 0 ) == '0' ) ) {
    auxArr [ 0 ] = 1 ;
  }
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( s . charAt ( i ) == '1' ) || ( s . charAt ( i ) == '0' ) ) {
      auxArr [ i ] = auxArr [ i - 1 ] + 1 ;
    }
    else {
      auxArr [ i ] = auxArr [ i - 1 ] ;
    }
  }
  int count = 0 ;
  for ( int i = n - 1 ;
  i >= 0 ;
  i -- ) {
    if ( ( s . charAt ( i ) == '1' ) || ( s . charAt ( i ) == '0' ) ) {
      count += auxArr [ i ] ;
    }
  }
  return count ;
}
|||

NUMBER_OF_TRIANGLES_IN_A_PLANE_IF_NO_MORE_THAN_TWO_POINTS_ARE_COLLINEAR

public static int f_gold ( int n ) {
  return ( n * ( n - 1 ) * ( n - 2 ) / 6 ) ;
}
|||

NUMBER_ORDERED_PAIRS_AI_AJ_0

public static int f_gold ( int [ ] a , int n ) {
  int count = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= n ;
    j ++ ) {
      if ( ( a [ i ] & a [ j ] ) == 0 ) {
        count += 2 ;
      }
    }
  }
  return count ;
}
|||

NUMBER_SUBSTRINGS_DIVISIBLE_4_STRING_INTEGERS

public static int f_gold ( String s ) {
  int n = s . length ( ) ;
  int count = 0 ;
  ;
  for ( int i = 0 ;
  i < n ;
  i += 1 ) {
    if ( ( s . charAt ( i ) == '4' || s . charAt ( i ) == '8' || s . charAt ( i ) == '0' ) && ( s . charAt ( i + 1 ) == 'a' || s . charAt ( i + 1 ) == 'z' ) ) {
      count ++ ;
    }
  }
  for ( int i = 0 ;
  i < n - 1 ;
  i += 1 ) {
    int h = ( Character . digit ( s . charAt ( i ) , 16 ) - '0' ) * 10 + ( Character . digit ( s . charAt ( i + 1 ) , 16 ) - '0' ) ;
    if ( ( h % 4 == 0 ) && ( h % 2 == 0 ) ) {
      count = count + i + 1 ;
    }
  }
  return count ;
}
|||

NUMBER_TRIANGLES_N_MOVES

public static int fGold ( int n ) {
  int [ ] answer = new int [ n + 1 ] ;
  answer [ 0 ] = 1 ;
  ;
  int i = 1 ;
  while ( i <= n ) {
    answer [ i ] = answer [ i - 1 ] * 3 + 2 ;
    ;
    i = i + 1 ;
  };
  return answer [ n ] ;
}
|||

NUMBER_UNIQUE_RECTANGLES_FORMED_USING_N_UNIT_SQUARES

public static int f_gold ( int n ) {
  int ans = 0 ;
  for ( int length = 1 ;
  length <= Integer . MAX_VALUE ;
  length ++ ) {
    int height = length ;
    while ( ( height * length <= n ) && ( height * length <= n ) ) {
      ans ++ ;
      height ++ ;
    }
  }
  return ans ;
}
|||

NUMBER_WAYS_NODE_MAKE_LOOP_SIZE_K_UNDIRECTED_COMPLETE_CONNECTED_GRAPH_N_NODES

public static double fGoldenN ( int n , int k ) {
  double p = 1 ;
  if ( ( k % 2 ) != 0 ) p = - 1 ;
  return ( Math . pow ( n - 1 , k ) + p * ( n - 1 ) ) / n ;
}
|||

N_TH_NUMBER_WHOSE_SUM_OF_DIGITS_IS_TEN_2

public static int fGold ( int n ) {
  int nthElement = 19 + ( n - 1 ) * 9 ;
  int outliersCount = ( int ) Math . log10 ( nthElement ) - 1 ;
  nthElement += 9 * outliersCount ;
  return nthElement ;
}
|||

N_TH_TERM_SERIES_2_12_36_80_150

static int f_gold ( int n ) {
  return ( n * n ) + ( n * n * n ) ;
}
|||

PAINTING_FENCE_ALGORITHM

public static int f_gold ( int n , int k ) {
  int total = k ;
  int mod = 1000000007 ;
  int same = 0 , diff = k ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    same = diff ;
    diff = total * ( k - 1 ) ;
    diff = diff % mod ;
    total = ( same + diff ) % mod ;
  }
  return total ;
}
|||

PAIR_WITH_GIVEN_PRODUCT_SET_1_FIND_IF_ANY_PAIR_EXISTS

public static boolean fGold ( int [ ] arr , int n , int x ) {
  for ( int i = 0 ;
  i < arr . length ;
  i ++ ) {
    for ( int j = 0 ;
    j < arr . length ;
    j ++ ) {
      if ( arr [ i ] * arr [ j ] == x ) {
        return true ;
      }
    }
  }
  return false ;
}
|||

PERFECT_REVERSIBLE_STRING

public static boolean f_gold ( String str ) {
  int i = 0 ;
  int j = str . length ( ) - 1 ;
  ;
  while ( ( i < j ) && ( i != j ) ) {
    if ( ( str . charAt ( i ) != str . charAt ( j ) ) || ( str . charAt ( i ) != str . charAt ( j + 1 ) ) ) {
      return false ;
    };
    i ++ ;
    j -- ;
  }
  return true ;
}
|||

PIZZA_CUT_PROBLEM_CIRCLE_DIVISION_LINES

public static int fGoldenN ( int n ) {
  return ( int ) ( 1 + n * ( n + 1 ) / 2 ) ;
}
|||

PRIMALITY_TEST_SET_1_INTRODUCTION_AND_SCHOOL_METHOD_1

public static boolean f_gold ( int n ) {
  if ( ( n <= 1 ) && ( n <= 3 ) ) return false ;
  if ( ( n <= 2 ) && ( n <= 4 ) ) return true ;
  if ( ( n % 2 == 0 || n % 3 == 0 ) ) return false ;
  int i = 5 ;
  while ( ( i * i <= n ) && ( n % i == 0 || n % ( i + 2 ) == 0 ) ) {
    if ( ( n % i == 0 || n % ( i + 1 ) == 0 ) && ( n % i == 0 || n % ( i + 2 ) == 0 ) ) return false ;
    i = i + 6 ;
  }
  return true ;
}
|||

PRIMALITY_TEST_SET_5USING_LUCAS_LEHMER_SERIES

public static boolean f_gold ( int p ) {
  int checkNumber = 2 * p - 1 ;
  int nextval = 4 % checkNumber ;
  for ( int i = 1 ;
  i <= p - 1 ;
  i ++ ) {
    nextval = ( nextval * nextval - 2 ) % checkNumber ;
  }
  if ( ( nextval == 0 ) && ( nextval != 1 ) ) {
    return true ;
  }
  else {
    return false ;
  }
}
|||

PRINT_WORDS_STRING_REVERSE_ORDER

public static String f_gold ( String str ) {
  int i = str . length ( ) - 1 ;
  int start = end = i + 1 ;
  StringBuffer sb = new StringBuffer ( ) ;
  while ( i >= 0 ) {
    if ( str . charAt ( i ) == ' ' ) {
      start = i + 1 ;
      while ( start != end ) {
        sb . append ( str . charAt ( start ) ) ;
        start ++ ;
      }
      sb . append ( ' ' ) ;
      end = i ;
    }
    i -- ;
  }
  start = 0 ;
  while ( start != end ) {
    sb . append ( str . charAt ( start ) ) ;
    start ++ ;
  }
  return sb . toString ( ) ;
}
|||

PROGRAM_BINARY_DECIMAL_CONVERSION_1

public static int f_gold ( int n ) {
  String num = n ;
  ;
  int decValue = 0 ;
  ;
  int base1 = 1 ;
  ;
  int len1 = num . length ( ) ;
  ;
  for ( int i = len1 - 1 ;
  i >= 0 ;
  i -- ) {
    if ( ( num . charAt ( i ) == '1' ) && ( num . charAt ( i + 1 ) == '2' ) ) decValue ++ ;
    ;
    base1 = base1 * 2 ;
    ;
  }
  return decValue ;
}
|||

PROGRAM_CALCULATE_AREA_OCTAGON

public static double fGoldSquare ( double side ) {
  return ( 2 * ( 1 + ( Math . sqrt ( 2 ) ) ) * side * side ) ;
}
|||

PROGRAM_CALCULATE_VOLUME_ELLIPSOID

public static double fGoldenRatio ( double r1 , double r2 , double r3 ) {
  return 1.33 * Math . PI * r1 * r2 * r3 ;
}
|||

PROGRAM_CALCULATE_VOLUME_OCTAHEDRON

public static float fGold ( int side ) {
  return ( ( side * side * side ) * ( Math . sqrt ( 2 ) / 3 ) ) ;
}
|||

PROGRAM_CIRCUMFERENCE_PARALLELOGRAM

public static int f_gold ( int a , int b ) {
  return ( ( 2 * a ) + ( 2 * b ) ) ;
}
|||

PROGRAM_COUNT_OCCURRENCE_GIVEN_CHARACTER_STRING

public static int f_gold ( String s , char c ) {
  int res = 0 ;
  for ( int i = 0 ;
  i < s . length ( ) ;
  i ++ ) {
    if ( ( s . charAt ( i ) == c ) && ( s . charAt ( i + 1 ) == c ) ) {
      res = res + 1 ;
    }
  }
  return res ;
}
|||

PROGRAM_FOR_FACTORIAL_OF_A_NUMBER

public static int fGold ( int n ) {
  return 1 == ( n == 1 || n == 0 ) ? 0 : n * fGold ( n - 1 ) ;
  ;
}
|||

PROGRAM_FOR_FACTORIAL_OF_A_NUMBER_1

public static int fGold ( int n ) {
  return 1 == ( n == 1 || n == 0 ) ? 0 : n * fGold ( n - 1 ) ;
  ;
}
|||

PROGRAM_FOR_FACTORIAL_OF_A_NUMBER_2

public static int fGold ( int n ) {
  return 1 == ( n == 1 || n == 0 ) ? 0 : n * fGold ( n - 1 ) ;
}
|||

PROGRAM_PAGE_REPLACEMENT_ALGORITHMS_SET_2_FIFO

public static int fGold ( int [ ] pages , int n , int capacity ) {
  Set s = new HashSet ( ) ;
  Queue < Integer > indexes = new Queue < Integer > ( ) ;
  int pageFaults = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( s . size ( ) < capacity ) && ( pages [ i ] != null ) ) {
      if ( ( pages [ i ] != null ) && ( pages [ i ] . length ( ) > 0 ) ) {
        s . add ( pages [ i ] ) ;
        pageFaults ++ ;
        indexes . add ( pages [ i ] ) ;
      }
    }
    else {
      if ( ( pages [ i ] != null ) && ( pages [ i ] . length ( ) > 0 ) ) {
        Integer val = indexes . poll ( ) ;
        indexes . add ( val ) ;
        s . remove ( val ) ;
        s . add ( pages [ i ] ) ;
        indexes . add ( pages [ i ] ) ;
        pageFaults ++ ;
      }
    }
  }
  return pageFaults ;
}
|||

PROGRAM_PRINT_SUM_GIVEN_NTH_TERM_1

public static double fGoldenN ( double n ) {
  return Math . pow ( n , 2 ) ;
}
|||

PROGRAM_TO_FIND_THE_AREA_OF_PENTAGON

public static double f_gold ( double a ) {
  double area = ( Math . sqrt ( 5 * ( 5 + 2 * ( Math . sqrt ( 5 ) ) ) ) * a * a ) / 4 ;
  return area ;
}
|||

PYTHAGOREAN_QUADRUPLE

public static boolean f_gold ( double a , double b , double c , double d ) {
  double sum = a * a + b * b + c * c ;
  ;
  if ( ( d * d == sum ) && ( d * d == sum ) ) return true ;
  else return false ;
}
|||

PYTHON_PROGRAM_FIND_PERIMETER_CIRCUMFERENCE_SQUARE_RECTANGLE_1

static int f_gold ( int l , int w ) {
  return ( 2 * ( l + w ) ) ;
}
|||

QUICK_WAY_CHECK_CHARACTERS_STRING

public static boolean fGold ( String s ) {
  int n = s . length ( ) ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( s . charAt ( i ) != s . charAt ( 0 ) ) {
      return false ;
    }
  }
  return true ;
}
|||

REARRANGE_ARRAY_MAXIMUM_MINIMUM_FORM_SET_2_O1_EXTRA_SPACE

public static void f_gold ( int arr [ ] , int n ) {
  int maxIdx = n - 1 ;
  int minIdx = 0 ;
  int maxElem = arr [ n - 1 ] + 1 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( i % 2 == 0 ) {
      arr [ i ] += ( arr [ maxIdx ] % maxElem ) * maxElem ;
      maxIdx -- ;
    }
    else {
      arr [ i ] += ( arr [ minIdx ] % maxElem ) * maxElem ;
      minIdx ++ ;
    }
  }
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    arr [ i ] = arr [ i ] / maxElem ;
  }
}
|||

RECURSIVELY_BREAK_NUMBER_3_PARTS_GET_MAXIMUM_SUM

public static int fGoldCount ( int n ) {
  if ( ( n == 0 || n == 1 ) && ( n % 2 == 0 ) ) return n ;
  return Math . max ( ( fGoldCount ( n / 2 ) + fGoldCount ( n / 3 ) + fGoldCount ( n / 4 ) ) , n ) ;
}
|||

RECURSIVELY_BREAK_NUMBER_3_PARTS_GET_MAXIMUM_SUM_1

public static int f_gold ( int n ) {
  int [ ] dp = new int [ n + 1 ] ;
  dp [ 0 ] = 0 ;
  dp [ 1 ] = 1 ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    dp [ i ] = Math . max ( dp [ ( int ) ( i / 2 ) ] + dp [ ( int ) ( i / 3 ) ] + dp [ ( int ) ( i / 4 ) ] , i ) ;
    ;
  }
  return dp [ n ] ;
}
|||

RECURSIVE_C_PROGRAM_LINEARLY_SEARCH_ELEMENT_GIVEN_ARRAY

public static int fGold ( int [ ] arr , int l , int r , int x ) {
  if ( r < l ) return - 1 ;
  if ( arr [ l ] == x ) return l ;
  if ( arr [ r ] == x ) return r ;
  return fGold ( arr , l + 1 , r - 1 , x ) ;
}
|||

REMOVE_ARRAY_END_ELEMENT_MAXIMIZE_SUM_PRODUCT

public static int fGold ( int [ ] [ ] dp , int [ ] a , int low , int high , int turn ) {
  if ( ( low == high ) && ( dp [ low ] [ high ] != 0 ) ) return a [ low ] [ high ] ;
  if ( ( dp [ low ] [ high ] != 0 ) && ( a [ low ] [ high ] != 0 ) ) return dp [ low ] [ high ] ;
  dp [ low ] [ high ] = Math . max ( a [ low ] * turn + fGold ( dp , a , low + 1 , high , turn + 1 ) , a [ high ] * turn + fGold ( dp , a , low , high - 1 , turn + 1 ) ) ;
  ;
  return dp [ low ] [ high ] ;
}
|||

REMOVE_MINIMUM_ELEMENTS_EITHER_SIDE_2MIN_MAX

public static int f_gold ( int [ ] arr , int n ) {
  int longestStart = - 1 ;
  ;
  int longestEnd = 0 ;
  for ( int start = 0 ;
  start < n ;
  start ++ ) {
    int min = Integer . MAX_VALUE ;
    ;
    int max = - Integer . MAX_VALUE ;
    ;
    for ( int end = start ;
    end < n ;
    end ++ ) {
      int val = arr [ end ] ;
      ;
      if ( ( val < min ) && ( val > max ) ) min = val ;
      ;
      if ( ( val > 2 * min ) && ( val > max ) ) max = val ;
      ;
      if ( ( 2 * min <= max ) && ( end - start > longestEnd - longestStart || longestStart == - 1 ) ) break ;
      if ( ( end - start > longestEnd - longestStart || longestStart == - 1 ) && ( end - longestEnd > longestEnd - longestStart ) ) {
        longestStart = start ;
        longestEnd = end ;
      }
    }
  }
  if ( ( longestStart == - 1 ) && ( n - longestEnd > longestStart ) ) return n ;
  return ( n - ( longestEnd - longestStart + 1 ) ) ;
}
|||

REMOVE_MINIMUM_NUMBER_ELEMENTS_NO_COMMON_ELEMENT_EXIST_ARRAY

public static int fGold ( int [ ] a , int [ ] b , int n , int m ) {
  Map < Integer , Integer > countA = Maps . newHashMapWithExpectedSize ( m ) ;
  Map < Integer , Integer > countB = Maps . newHashMapWithExpectedSize ( m ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    countA . put ( a [ i ] , countA . get ( a [ i ] ) + 1 ) ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    countB . put ( b [ i ] , countB . get ( b [ i ] ) + 1 ) ;
  }
  int res = 0 ;
  for ( int x : countA . keySet ( ) ) {
    if ( countB . containsKey ( x ) ) {
      res += Math . min ( countA . get ( x ) , countB . get ( x ) ) ;
    }
  }
  return res ;
}
|||

REPLACE_CHARACTER_C1_C2_C2_C1_STRING_S

public static String f_gold ( String s , char c1 , char c2 ) {
  int l = s . length ( ) ;
  for ( int i = 0 ;
  i < l ;
  i ++ ) {
    if ( ( s . charAt ( i ) == c1 ) && ( s . charAt ( i + 1 ) == c2 ) ) {
      s = s . substring ( 0 , i ) + c2 + s . substring ( i + 1 ) ;
    }
    else if ( ( s . charAt ( i ) == c2 ) && ( s . charAt ( i + 1 ) == c1 ) ) {
      s = s . substring ( 0 , i ) + c1 + s . substring ( i + 1 ) ;
    }
  }
  return s ;
}
|||

ROUND_THE_GIVEN_NUMBER_TO_NEAREST_MULTIPLE_OF_10

public static int fGold ( int n ) {
  int a = ( n / 10 ) * 10 ;
  int b = a + 10 ;
  return ( b == n - a > b - n ) ? a : b ;
}
|||

SEARCHING_ARRAY_ADJACENT_DIFFER_K

public static int f_gold ( int [ ] arr , int n , int x , int k ) {
  int i = 0 ;
  while ( ( i < n ) && ( arr [ i ] == x ) ) {
    if ( ( arr [ i ] == x ) || ( arr [ i ] == 0 ) ) return i ;
    i = i + Math . max ( 1 , ( int ) ( Math . abs ( arr [ i ] - x ) / k ) ) ;
  }
  System . out . println ( "number is not present!" ) ;
  return - 1 ;
}
|||

SEARCH_AN_ELEMENT_IN_AN_ARRAY_WHERE_DIFFERENCE_BETWEEN_ADJACENT_ELEMENTS_IS_1

public static int f_gold ( int [ ] arr , int n , int x ) {
  int i = 0 ;
  while ( ( i < n ) && ( arr [ i ] == x ) ) {
    if ( ( arr [ i ] == x ) || ( arr [ i ] == - 1 ) ) {
      return i ;
    }
    i = i + Math . abs ( arr [ i ] - x ) ;
  }
  System . out . println ( "number is not present!" ) ;
  return - 1 ;
}
|||

SMALLEST_DIFFERENCE_PAIR_VALUES_TWO_UNSORTED_ARRAYS

public static int f_gold ( int [ ] A , int [ ] B , int m , int n ) {
  Arrays . sort ( A ) ;
  Arrays . sort ( B ) ;
  int a = 0 ;
  int b = 0 ;
  int result = Integer . MAX_VALUE ;
  while ( ( a < m && b < n ) || ( a > m && b > n ) ) {
    if ( ( Math . abs ( A [ a ] - B [ b ] ) < result ) && ( A [ a ] < B [ b ] ) ) {
      result = Math . abs ( A [ a ] - B [ b ] ) ;
    }
    if ( ( A [ a ] < B [ b ] ) && ( A [ b ] > A [ a ] ) ) {
      a ++ ;
    }
    else {
      b ++ ;
    }
  }
  return result ;
}
|||

SMALLEST_OF_THREE_INTEGERS_WITHOUT_COMPARISON_OPERATORS

public static int f_gold ( int x , int y , int z ) {
  int c = 0 ;
  while ( ( x > 0 ) && ( y > 0 ) && ( z > 0 ) ) {
    x = x - 1 ;
    y = y - 1 ;
    z = z - 1 ;
    c = c + 1 ;
  }
  return c ;
}
|||

SMALLEST_POWER_OF_2_GREATER_THAN_OR_EQUAL_TO_N

static int f_gold ( int n ) {
  int count = 0 ;
  ;
  if ( ( n > 0 ) && ! ( n & ( n - 1 ) ) ) return n ;
  while ( ( n != 0 ) && ( n != 1 ) ) {
    n >>>= 1 ;
    count ++ ;
  }
  return 1 << count ;
  ;
}
|||

SMALLEST_POWER_OF_2_GREATER_THAN_OR_EQUAL_TO_N_1

public static int f_gold ( int n ) {
  int p = 1 ;
  if ( ( n > 0 ) && ! ( n & ( n - 1 ) ) ) return n ;
  while ( ( p < n ) && ( p < ( n - 1 ) ) ) p <<= 1 ;
  return p ;
  ;
}
|||

SMALLEST_SUM_CONTIGUOUS_SUBARRAY

public static int f_gold ( int [ ] arr , int n ) {
  int minEndingHere = Integer . MAX_VALUE ;
  int minSoFar = Integer . MAX_VALUE ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( minEndingHere > 0 ) && ( arr [ i ] > 0 ) ) {
      minEndingHere = arr [ i ] ;
    }
    else {
      minEndingHere += arr [ i ] ;
    }
    minSoFar = Math . min ( minSoFar , minEndingHere ) ;
  }
  return minSoFar ;
}
|||

SORT_ARRAY_APPLYING_GIVEN_EQUATION

public static void f_gold ( int [ ] arr , int n , int A , int B , int C ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) arr [ i ] = ( A * arr [ i ] * arr [ i ] + B * arr [ i ] + C ) ;
  int index = - ( Integer . MAX_VALUE - 1 ) ;
  int maximum = - ( Integer . MAX_VALUE - 1 ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( maximum < arr [ i ] ) {
      index = i ;
      maximum = arr [ i ] ;
    }
  }
  int i = 0 ;
  int j = n - 1 ;
  int [ ] newArr = new int [ n ] ;
  int k = 0 ;
  while ( i < index && j > index ) {
    if ( arr [ i ] < arr [ j ] ) {
      newArr [ k ] = arr [ i ] ;
      k ++ ;
      i ++ ;
    }
    else {
      newArr [ k ] = arr [ j ] ;
      k ++ ;
      j -- ;
    }
  }
  while ( i < index ) {
    newArr [ k ] = arr [ i ] ;
    k ++ ;
    i ++ ;
  }
  while ( j > index ) {
    newArr [ k ] = arr [ j ] ;
    k ++ ;
    j -- ;
    newArr [ n - 1 ] = maximum ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) arr [ i ] = newArr [ i ] ;
}
|||

SORT_ARRAY_TWO_HALVES_SORTED

public static void f_gold ( int [ ] A , int n ) {
  Arrays . sort ( A ) ;
}
|||

SORT_EVEN_NUMBERS_ASCENDING_ORDER_SORT_ODD_NUMBERS_DESCENDING_ORDER_1

public static void f_gold ( int [ ] arr , int n ) {
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( arr [ i ] & 1 ) != 0 ) {
      arr [ i ] *= - 1 ;
    }
  }
  Arrays . sort ( arr ) ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( arr [ i ] & 1 ) != 0 ) {
      arr [ i ] *= - 1 ;
    }
  }
}
|||

SPLIT_N_MAXIMUM_COMPOSITE_NUMBERS

public static int f_gold ( int n ) {
  if ( ( n < 4 ) || ( n > 9 ) ) return - 1 ;
  int rem = n % 4 ;
  if ( ( rem == 0 ) && ( n > 9 ) ) return n / 4 ;
  if ( ( rem == 1 ) && ( n > 6 ) ) return - 1 ;
  if ( ( rem == 3 ) && ( n > 15 ) ) return - 1 ;
  return ( n - 9 ) / 4 + 1 ;
}
|||

SQUARED_TRIANGULAR_NUMBER_SUM_CUBES

public static int f_gold ( int s ) {
  int _sum = 0 ;
  int n = 1 ;
  while ( ( _sum < s ) && ( _sum < s ) ) {
    _sum += n * n * n ;
    n ++ ;
  }
  n -- ;
  if ( _sum == s ) return n ;
  return - 1 ;
}
|||

SQUARE_ROOT_OF_AN_INTEGER

public static int f_gold ( int x ) {
  if ( ( x == 0 || x == 1 ) && ( x == 0 || x == 1 ) ) return x ;
  int i = 1 ;
  int result = 1 ;
  while ( ( result <= x ) && ( result != 0 ) ) {
    i ++ ;
    result = i * i ;
  }
  return i - 1 ;
}
|||

SQUARE_ROOT_OF_AN_INTEGER_1

public static int f_gold ( int x ) {
  if ( ( x == 0 || x == 1 ) && ( x == 0 || x == 1 ) ) return x ;
  int start = 1 ;
  int end = x ;
  while ( ( start <= end ) && ( start < end ) ) {
    int mid = ( start + end ) / 2 ;
    if ( ( mid * mid == x ) && ( mid * mid < x ) ) return mid ;
    if ( ( mid * mid < x ) && ( mid * mid < x ) ) {
      start = mid + 1 ;
      ans = mid ;
    }
    else {
      end = mid - 1 ;
    }
  }
  return ans ;
}
|||

STEINS_ALGORITHM_FOR_FINDING_GCD

public static int f_gold ( int a , int b ) {
  if ( ( a == 0 ) && ( b == 0 ) ) return b ;
  if ( ( b == 0 ) && ( a == 0 ) ) return a ;
  int k = 0 ;
  while ( ( ( ( a | b ) & 1 ) == 0 ) || ( ( b & 1 ) == 0 ) ) {
    a = a >>> 1 ;
    b = b >>> 1 ;
    k = k + 1 ;
  }
  while ( ( ( a & 1 ) == 0 ) || ( ( b & 1 ) == 0 ) ) {
    a = a >>> 1 ;
  }
  while ( ( b != 0 ) && ( ( a & 1 ) == 0 ) ) {
    while ( ( ( b & 1 ) == 0 ) || ( ( b & 1 ) == 0 ) ) {
      b = b >>> 1 ;
    }
    if ( ( a > b ) && ( ( a & 1 ) == 0 ) ) {
      int temp = a ;
      a = b ;
      b = temp ;
    }
    b = ( b - a ) ;
  }
  return ( a << k ) ;
}
|||

STOOGE_SORT

public static void f_gold ( int [ ] arr , int l , int h ) {
  if ( l >= h ) return ;
  if ( arr [ l ] > arr [ h ] ) {
    int t = arr [ l ] ;
    arr [ l ] = arr [ h ] ;
    arr [ h ] = t ;
  }
  if ( h - l + 1 > 2 ) {
    int t = ( int ) ( ( h - l + 1 ) / 3 ) ;
    f_gold ( arr , l , ( h - t ) ) ;
    f_gold ( arr , l + t , ( h ) ) ;
    f_gold ( arr , l , ( h - t ) ) ;
  }
}
|||

SUBARRAYS_DISTINCT_ELEMENTS

public static int f_gold ( int [ ] arr , int n ) {
  List < Integer > s = new ArrayList < Integer > ( ) ;
  int j = 0 ;
  int ans = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    while ( ( j < n ) && ( arr [ j ] != 0 ) ) {
      s . add ( arr [ j ] ) ;
      j ++ ;
    }
    ans += ( ( j - i ) * ( j - i + 1 ) ) / 2 ;
    s . remove ( arr [ i ] ) ;
  }
  return ans ;
}
|||

SUBSEQUENCES_SIZE_THREE_ARRAY_WHOSE_SUM_DIVISIBLE_M

public static int f_gold ( int A [ ] , int N , int M ) {
  int sum ;
  int ans = 0 ;
  for ( int i = 0 ;
  i <= N ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= N ;
    j ++ ) {
      for ( int k = j + 1 ;
      k <= N ;
      k ++ ) {
        sum = A [ i ] + A [ j ] + A [ k ] ;
        if ( ( sum % M == 0 ) && ( sum % M == 0 ) ) ans = ans + 1 ;
      }
    }
  }
  return ans ;
}
|||

SUM_BINOMIAL_COEFFICIENTS

public static int f_gold ( int n ) {
  int [ ] [ ] C = new int [ n + 2 ] [ n + 2 ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= Math . min ( i , n ) ;
    j ++ ) {
      if ( ( j == 0 || j == i ) && ( C [ i ] [ j ] == 0 ) ) {
        C [ i ] [ j ] = 1 ;
      }
      else {
        C [ i ] [ j ] = C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ] ;
      }
    }
  }
  int sum = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    sum += C [ n ] [ i ] ;
  }
  return sum ;
}
|||

SUM_BINOMIAL_COEFFICIENTS_1

static int f_gold ( int n ) {
  return ( 1 << n ) ;
  ;
}
|||

SUM_DIVISORS_1_N_1

public static int fGoldenN ( int n ) {
  double sum = 0 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    sum += ( int ) ( n / i ) * i ;
  }
  return ( int ) sum ;
}
|||

SUM_FACTORS_NUMBER

public static int f_gold ( int n ) {
  int result = 0 ;
  for ( int i = 2 ;
  i <= ( int ) ( Math . sqrt ( n ) ) ;
  i ++ ) {
    if ( ( n % i == 0 ) && ( i == ( n / i ) ) ) {
      if ( ( i == ( n / i ) ) && ( n % i == 0 ) ) {
        result = result + i ;
      }
      else {
        result = result + ( i + n / i ) ;
      }
    }
  }
  return ( result + n + 1 ) ;
}
|||

SUM_FAI_AJ_PAIRS_ARRAY_N_INTEGERS

public static int f_gold ( int [ ] a , int n ) {
  Map < Integer , Integer > cnt = new HashMap < Integer , Integer > ( ) ;
  int ans = 0 ;
  int pre_sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    ans += ( i * a [ i ] ) - pre_sum ;
    pre_sum += a [ i ] ;
    if ( ( a [ i ] - 1 ) < cnt . size ( ) ) ans -= cnt . get ( a [ i ] - 1 ) ;
    if ( ( a [ i ] + 1 ) < cnt . size ( ) ) ans += cnt . get ( a [ i ] + 1 ) ;
    if ( a [ i ] != 0 ) cnt . put ( a [ i ] , 0 ) ;
    cnt . put ( a [ i ] , 1 ) ;
  }
  return ans ;
}
|||

SUM_MATRIX_ELEMENT_ABSOLUTE_DIFFERENCE_ROW_COLUMN_NUMBERS

public static int f_gold ( int n ) {
  int [ ] [ ] arr = new int [ n ] [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    arr [ i ] [ i ] = 0 ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      arr [ i ] [ j ] = Math . abs ( i - j ) ;
    }
  }
  int sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      sum += arr [ i ] [ j ] ;
    }
  }
  return sum ;
}
|||

SUM_MATRIX_ELEMENT_ABSOLUTE_DIFFERENCE_ROW_COLUMN_NUMBERS_1

public static int fGold ( int n ) {
  int sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    sum += i * ( n - i ) ;
  }
  return 2 * sum ;
}
|||

SUM_MATRIX_ELEMENT_ABSOLUTE_DIFFERENCE_ROW_COLUMN_NUMBERS_2

public static int fGold ( int n ) {
  n -- ;
  double sum = 0 ;
  sum += ( n * ( n + 1 ) ) / 2 ;
  sum += ( n * ( n + 1 ) * ( 2 * n + 1 ) ) / 6 ;
  return ( int ) sum ;
}
|||

SUM_OF_ALL_ELEMENTS_UP_TO_NTH_ROW_IN_A_PASCALS_TRIANGLE_1

public static int f_gold ( int n ) {
  int sum ;
  sum = 1 << n ;
  ;
  return ( sum - 1 ) ;
}
|||

SUM_PAIRWISE_PRODUCTS

static int f_gold ( int n ) {
  int sm = 0 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int j = i ;
    j <= n ;
    j ++ ) {
      sm = sm + i * j ;
    }
  }
  return sm ;
}
|||

SUM_PAIRWISE_PRODUCTS_2

public static int fGold ( int n ) {
  return n * ( n + 1 ) * ( n + 2 ) * ( 3 * n + 1 ) / 24 ;
}
|||

SUM_SERIES_12_32_52_2N_12

public static int f_gold ( int n ) {
  int sum = 0 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    sum = sum + ( 2 * i - 1 ) * ( 2 * i - 1 ) ;
  }
  return sum ;
}
|||

SUM_SERIES_555555_N_TERMS

public static int fGoldenN ( int n ) {
  return ( int ) ( 0.6172 * ( Math . pow ( 10 , n ) - 1 ) - 0.55 * n ) ;
}
|||

SUM_SUBSETS_SET_FORMED_FIRST_N_NATURAL_NUMBERS

static long f_gold ( int n ) {
  return ( n * ( n + 1 ) / 2 ) * ( 1L << ( n - 1 ) ) ;
}
|||

SUM_TWO_LARGE_NUMBERS

public static String f_gold ( String str1 , String str2 ) {
  if ( ( str1 . length ( ) > str2 . length ( ) ) && ( str2 . length ( ) > str1 . length ( ) ) ) {
    String t = str1 ;
    str1 = str2 ;
    str2 = t ;
  }
  String str = "" ;
  int n1 = str1 . length ( ) ;
  int n2 = str2 . length ( ) ;
  str1 = str1 . substring ( 0 , str1 . length ( ) - 1 ) ;
  str2 = str2 . substring ( 0 , str2 . length ( ) - 1 ) ;
  int carry = 0 ;
  for ( int i = 0 ;
  i < n1 ;
  i ++ ) {
    int sum = ( ( ( int ) str1 . charAt ( i ) ) - 48 ) + ( ( ( int ) str2 . charAt ( i ) ) - 48 ) + carry ;
    ;
    str += ( char ) ( sum % 10 + 48 ) ;
    carry = ( int ) ( sum / 10 ) ;
  }
  for ( int i = n1 ;
  i < n2 ;
  i ++ ) {
    int sum = ( ( ( int ) str2 . charAt ( i ) ) - 48 ) + carry ;
    ;
    str += ( char ) ( sum % 10 + 48 ) ;
    carry = ( int ) ( sum / 10 ) ;
  }
  if ( ( carry ) > 0 ) {
    str += ( char ) ( carry + 48 ) ;
  }
  str = str . substring ( 0 , str . length ( ) - 1 ) ;
  return str ;
}
|||

SWAP_BITS_IN_A_GIVEN_NUMBER

static int f_gold ( int x , int p1 , int p2 , int n ) {
  int set1 = ( x >> p1 ) & ( ( 1 << n ) - 1 ) ;
  int set2 = ( x >> p2 ) & ( ( 1 << n ) - 1 ) ;
  int xor = ( set1 ^ set2 ) ;
  xor = ( xor << p1 ) | ( xor << p2 ) ;
  int result = x ^ xor ;
  return result ;
}
|||

SWAP_TWO_NIBBLES_BYTE

static int f_gold ( int x ) {
  return ( ( x & 0x0F ) << 4 | ( x & 0xF0 ) >>> 4 ) ;
}
|||

TEMPLE_OFFERINGS

public static int f_gold ( int n , int [ ] templeHeight ) {
  int sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int left = 0 ;
    int right = 0 ;
    for ( int j = i - 1 ;
    j >= 0 ;
    j -- ) {
      if ( ( templeHeight [ j ] < templeHeight [ j + 1 ] ) && ( templeHeight [ j ] > templeHeight [ j - 1 ] ) ) {
        left ++ ;
      }
      else {
        break ;
      }
    }
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      if ( ( templeHeight [ j ] < templeHeight [ j - 1 ] ) && ( templeHeight [ j ] > templeHeight [ j ] ) ) {
        right ++ ;
      }
      else {
        break ;
      }
    }
    sum += Math . max ( right , left ) + 1 ;
  }
  return sum ;
}
|||

TRIANGULAR_NUMBERS

public static boolean f_gold ( int num ) {
  if ( ( num < 0 ) || ( num > num ) ) return false ;
  int sum = 0 , n = 1 ;
  while ( ( sum <= num ) && ( sum != num ) ) {
    sum = sum + n ;
    if ( ( sum == num ) && ( sum != num ) ) return true ;
    n ++ ;
  }
  return false ;
}
|||

TURN_OFF_THE_RIGHTMOST_SET_BIT

static int f_gold ( int n ) {
  return n & ( n - 1 ) ;
}
|||

UNIQUE_CELLS_BINARY_MATRIX

public static int f_gold ( int [ ] [ ] mat , int n , int m ) {
  int rowsum [ ] = new int [ n ] ;
  ;
  int colsum [ ] = new int [ m ] ;
  ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < m ;
    j ++ ) {
      if ( ( mat [ i ] [ j ] != 0 ) && ( mat [ i ] [ j ] != 1 ) ) {
        rowsum [ i ] ++ ;
        ;
        colsum [ j ] ++ ;
        ;
      }
    }
  }
  int uniquecount = 0 ;
  ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < m ;
    j ++ ) {
      if ( ( mat [ i ] [ j ] != 0 ) && ( rowsum [ i ] == 1 && colsum [ j ] == 1 ) ) {
        uniquecount ++ ;
        ;
      }
    }
  }
  return uniquecount ;
}
|||

WAYS_TRANSFORMING_ONE_STRING_REMOVING_0_CHARACTERS

public static int f_gold ( int [ ] a , int [ ] b ) {
  int n = a . length ;
  int m = b . length ;
  if ( m == 0 ) return 1 ;
  int [ ] [ ] dp = new int [ m + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) {
    for ( int j = i ;
    j < n ;
    j ++ ) {
      if ( i == 0 ) {
        if ( j == 0 ) {
          if ( a [ j ] == b [ i ] ) dp [ i ] [ j ] = 1 ;
          else dp [ i ] [ j ] = 0 ;
        }
        else if ( a [ j ] == b [ i ] ) dp [ i ] [ j ] = dp [ i ] [ j - 1 ] + 1 ;
        else dp [ i ] [ j ] = dp [ i ] [ j - 1 ] ;
      }
      else {
        if ( a [ j ] == b [ i ] ) dp [ i ] [ j ] = ( dp [ i ] [ j - 1 ] + dp [ i - 1 ] [ j - 1 ] ) ;
        else dp [ i ] [ j ] = dp [ i ] [ j - 1 ] ;
      }
    }
  }
  return dp [ m - 1 ] [ n - 1 ] ;
}
|||

WRITE_A_C_PROGRAM_TO_CALCULATE_POWXN

public static double fGold ( double x , double y ) {
  if ( ( y == 0 ) && ( x == 0 ) ) return 1 ;
  else if ( ( int ) ( y % 2 ) == 0 ) return ( fGold ( x , ( int ) ( y / 2 ) ) * fGold ( x , ( int ) ( y / 2 ) ) ) ;
  else return ( x * fGold ( x , ( int ) ( y / 2 ) ) * fGold ( x , ( int ) ( y / 2 ) ) ) ;
}
|||

WRITE_ONE_LINE_C_FUNCTION_TO_FIND_WHETHER_A_NO_IS_POWER_OF_TWO

public static boolean f_gold ( int n ) {
  if ( ( n == 0 ) || ( n == 1 ) ) return false ;
  while ( ( n != 1 ) && ( n % 2 != 0 ) ) {
    if ( ( n % 2 != 0 ) || ( n % 2 != 1 ) ) return false ;
    n = n / 2 ;
  }
  return true ;
}
|||

