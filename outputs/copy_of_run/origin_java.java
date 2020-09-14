MAXIMUM_NUMBER_CHARACTERS_TWO_CHARACTER_STRING

static int maximumChars ( String str ) {
  int n = str . length ( ) ;
  int res = - 1 ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) for ( int j = i + 1 ;
  j < n ;
  j ++ ) if ( str . charAt ( i ) == str . charAt ( j ) ) res = Math . max ( res , Math . abs ( j - i - 1 ) ) ;
  return res ;
}
|||

FIND_MIRROR_IMAGE_POINT_2_D_PLANE

static pair mirrorImage ( double a , double b , double c , double x1 , double y1 ) {
  double temp = - 2 * ( a * x1 + b * y1 + c ) / ( a * a + b * b ) ;
  double x = temp * a + x1 ;
  double y = temp * b + y1 ;
  return new pair ( x , y ) ;
}
|||

EFFICIENTLY_COMPUTE_SUMS_OF_DIAGONALS_OF_A_MATRIX

static void printDiagonalSums ( int [ ] [ ] mat , int n ) {
  int principal = 0 , secondary = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( i == j ) principal += mat [ i ] [ j ] ;
      if ( ( i + j ) == ( n - 1 ) ) secondary += mat [ i ] [ j ] ;
    }
  }
  System . out . println ( "Principal Diagonal:" + principal ) ;
  System . out . println ( "Secondary Diagonal:" + secondary ) ;
}
|||

COUNTS_PATHS_POINT_REACH_ORIGIN

static int countPaths ( int n , int m ) {
  if ( n == 0 || m == 0 ) return 1 ;
  return ( countPaths ( n - 1 , m ) + countPaths ( n , m - 1 ) ) ;
}
|||

FIND_A_TRIPLET_THAT_SUM_TO_A_GIVEN_VALUE_1

boolean find3Numbers ( int A [ ] , int arr_size , int sum ) {
  int l , r ;
  quickSort ( A , 0 , arr_size - 1 ) ;
  for ( int i = 0 ;
  i < arr_size - 2 ;
  i ++ ) {
    l = i + 1 ;
    r = arr_size - 1 ;
    while ( l < r ) {
      if ( A [ i ] + A [ l ] + A [ r ] == sum ) {
        System . out . print ( "Triplet is " + A [ i ] + ", " + A [ l ] + ", " + A [ r ] ) ;
        return true ;
      }
      else if ( A [ i ] + A [ l ] + A [ r ] < sum ) l ++ ;
      else r -- ;
    }
  }
  return false ;
}
|||

CHECK_GIVEN_MATRIX_IS_MAGIC_SQUARE_OR_NOT

static boolean isMagicSquare ( int mat [ ] [ ] ) {
  int sum = 0 , sum2 = 0 ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) sum = sum + mat [ i ] [ i ] ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) sum2 = sum2 + mat [ i ] [ N - 1 - i ] ;
  if ( sum != sum2 ) return false ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    int rowSum = 0 ;
    for ( int j = 0 ;
    j < N ;
    j ++ ) rowSum += mat [ i ] [ j ] ;
    if ( rowSum != sum ) return false ;
  }
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    int colSum = 0 ;
    for ( int j = 0 ;
    j < N ;
    j ++ ) colSum += mat [ j ] [ i ] ;
    if ( sum != colSum ) return false ;
  }
  return true ;
}
|||

SEQUENCES_GIVEN_LENGTH_EVERY_ELEMENT_EQUAL_TWICE_PREVIOUS_1

static int getTotalNumberOfSequences ( int m , int n ) {
  int T [ ] [ ] = new int [ m + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i < m + 1 ;
  i ++ ) {
    for ( int j = 0 ;
    j < n + 1 ;
    j ++ ) {
      if ( i == 0 || j == 0 ) T [ i ] [ j ] = 0 ;
      else if ( i < j ) T [ i ] [ j ] = 0 ;
      else if ( j == 1 ) T [ i ] [ j ] = i ;
      else T [ i ] [ j ] = T [ i - 1 ] [ j ] + T [ i / 2 ] [ j - 1 ] ;
    }
  }
  return T [ m ] [ n ] ;
}
|||

FIND_DIFFERENCE_BETWEEN_SUMS_OF_TWO_DIAGONALS_1

public static int difference ( int arr [ ] [ ] , int n ) {
  int d1 = 0 , d2 = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    d1 += arr [ i ] [ i ] ;
    d2 += arr [ i ] [ n - i - 1 ] ;
  }
  return Math . abs ( d1 - d2 ) ;
}
|||

MINIMUM_NUMBER_SUBSETS_DISTINCT_ELEMENTS

public static int subset ( int ar [ ] , int n ) {
  int res = 0 ;
  Arrays . sort ( ar ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int count = 1 ;
    for ( ;
    i < n - 1 ;
    i ++ ) {
      if ( ar [ i ] == ar [ i + 1 ] ) count ++ ;
      else break ;
    }
    res = Math . max ( res , count ) ;
  }
  return res ;
}
|||

DECIMAL_BINARY_CONVERSION_WITHOUT_USING_ARITHMETIC_OPERATORS

static String decToBin ( int n ) {
  if ( n == 0 ) return "0" ;
  String bin = "" ;
  while ( n > 0 ) {
    bin = ( ( n & 1 ) == 0 ? '0' : '1' ) + bin ;
    n >>= 1 ;
  }
  return bin ;
}
|||

FIND_NTH_TERM_DRAGON_CURVE_SEQUENCE

static String Dragon_Curve_Sequence ( int n ) {
  String s = "1" ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    String temp = "1" ;
    char prev = '1' , zero = '0' , one = '1' ;
    for ( int j = 0 ;
    j < s . length ( ) ;
    j ++ ) {
      temp += s . charAt ( j ) ;
      if ( prev == '0' ) {
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

static void reverse ( char str [ ] ) {
  int n = str . length , i ;
  for ( i = 0 ;
  i < n / 2 ;
  i ++ ) {
    swap ( str , i , n - i - 1 ) ;
  }
}
|||

SORT_EVEN_PLACED_ELEMENTS_INCREASING_ODD_PLACED_DECREASING_ORDER_1

static void bitonicGenerator ( int arr [ ] , int n ) {
  int i = 1 ;
  int j = n - 1 ;
  if ( j % 2 != 0 ) j -- ;
  while ( i < j ) {
    arr = swap ( arr , i , j ) ;
    i += 2 ;
    j -= 2 ;
  }
  Arrays . sort ( arr , 0 , ( n + 1 ) / 2 ) ;
  Arrays . sort ( arr , ( n + 1 ) / 2 , n ) ;
  int low = ( n + 1 ) / 2 , high = n - 1 ;
  while ( low < high ) {
    Integer temp = arr [ low ] ;
    arr [ low ] = arr [ high ] ;
    arr [ high ] = temp ;
    low ++ ;
    high -- ;
  }
}
|||

GIVEN_TWO_NUMBERS_B_FIND_X_X_B

static void modularEquation ( int a , int b ) {
  if ( a < b ) {
    System . out . println ( "No solution possible " ) ;
    return ;
  }
  if ( a == b ) {
    System . out . println ( "Infinite Solution possible " ) ;
    return ;
  }
  int count = 0 ;
  int n = a - b ;
  int y = ( int ) Math . sqrt ( a - b ) ;
  for ( int i = 1 ;
  i <= y ;
  ++ i ) {
    if ( n % i == 0 ) {
      if ( n / i > b ) count ++ ;
      if ( i > b ) count ++ ;
    }
  }
  if ( y * y == n && y > b ) count -- ;
  System . out . println ( count ) ;
}
|||

CHECK_CHARACTERS_GIVEN_STRING_CAN_REARRANGED_FORM_PALINDROME

static boolean canFormPalindrome ( String str ) {
  int count [ ] = new int [ NO_OF_CHARS ] ;
  Arrays . fill ( count , 0 ) ;
  for ( int i = 0 ;
  i < str . length ( ) ;
  i ++ ) count [ ( int ) ( str . charAt ( i ) ) ] ++ ;
  int odd = 0 ;
  for ( int i = 0 ;
  i < NO_OF_CHARS ;
  i ++ ) {
    if ( ( count [ i ] & 1 ) == 1 ) odd ++ ;
    if ( odd > 1 ) return false ;
  }
  return true ;
}
|||

MAXIMUM_TRIPLET_SUM_ARRAY_1

static int maxTripletSum ( int arr [ ] , int n ) {
  Arrays . sort ( arr ) ;
  return arr [ n - 1 ] + arr [ n - 2 ] + arr [ n - 3 ] ;
}
|||

FIND_MEDIAN_ROW_WISE_SORTED_MATRIX

static int binaryMedian ( int m [ ] [ ] , int r , int c ) {
  int max = Integer . MIN_VALUE ;
  int min = Integer . MAX_VALUE ;
  for ( int i = 0 ;
  i < r ;
  i ++ ) {
    if ( m [ i ] [ 0 ] < min ) min = m [ i ] [ 0 ] ;
    if ( m [ i ] [ c - 1 ] > max ) max = m [ i ] [ c - 1 ] ;
  }
  int desired = ( r * c + 1 ) / 2 ;
  while ( min < max ) {
    int mid = min + ( max - min ) / 2 ;
    int place = 0 ;
    int get = 0 ;
    for ( int i = 0 ;
    i < r ;
    ++ i ) {
      get = Arrays . binarySearch ( m [ i ] , mid ) ;
      if ( get < 0 ) get = Math . abs ( get ) - 1 ;
      else {
        while ( get < m [ i ] . length && m [ i ] [ get ] == mid ) get += 1 ;
      }
      place = place + get ;
    }
    if ( place < desired ) min = mid + 1 ;
    else max = mid ;
  }
  return min ;
}
|||

HEIGHT_N_ARY_TREE_PARENT_ARRAY_GIVEN

static int findHeight ( int [ ] parent , int n ) {
  int res = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int p = i , current = 1 ;
    while ( parent [ p ] != - 1 ) {
      current ++ ;
      p = parent [ p ] ;
    }
    res = Math . max ( res , current ) ;
  }
  return res ;
}
|||

CHECK_LARGE_NUMBER_DIVISIBLE_20

static Boolean divisibleBy20 ( String num ) {
  int lastTwoDigits = Integer . parseInt ( num . substring ( num . length ( ) - 2 , num . length ( ) ) ) ;
  return ( ( lastTwoDigits % 5 == 0 ) && ( lastTwoDigits % 4 == 0 ) ) ;
}
|||

MAXIMUM_VALUE_CHOICE_EITHER_DIVIDING_CONSIDERING

static int maxDP ( int n ) {
  int res [ ] = new int [ n + 1 ] ;
  res [ 0 ] = 0 ;
  res [ 1 ] = 1 ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) res [ i ] = Math . max ( i , ( res [ i / 2 ] + res [ i / 3 ] + res [ i / 4 ] + res [ i / 5 ] ) ) ;
  return res [ n ] ;
}
|||

QUERIES_ON_ARRAY_WITH_DISAPPEARING_AND_REAPPEARING_ELEMENTS

static void PerformQueries ( int [ ] a , int [ ] [ ] vec ) {
  Vector < Integer > ans = new Vector < > ( ) ;
  int n = ( int ) a . length - 1 ;
  int q = ( int ) vec . length ;
  for ( int i = 0 ;
  i < q ;
  ++ i ) {
    long t = vec [ i ] [ 0 ] ;
    int m = vec [ i ] [ 1 ] ;
    if ( m > n ) {
      ans . add ( - 1 ) ;
      continue ;
    }
    int turn = ( int ) ( t / n ) ;
    int rem = ( int ) ( t % n ) ;
    if ( rem == 0 && turn % 2 == 1 ) {
      ans . add ( - 1 ) ;
      continue ;
    }
    if ( rem == 0 && turn % 2 == 0 ) {
      ans . add ( a [ m ] ) ;
      continue ;
    }
    if ( turn % 2 == 0 ) {
      int cursize = n - rem ;
      if ( cursize < m ) {
        ans . add ( - 1 ) ;
        continue ;
      }
      ans . add ( a [ m + rem ] ) ;
    }
    else {
      int cursize = rem ;
      if ( cursize < m ) {
        ans . add ( - 1 ) ;
        continue ;
      }
      ans . add ( a [ m ] ) ;
    }
  }
  for ( int i : ans ) System . out . print ( i + "\n" ) ;
}
|||

FIND_THE_MINIMUM_DISTANCE_BETWEEN_TWO_NUMBERS_1

int minDist ( int arr [ ] , int n , int x , int y ) {
  int i = 0 ;
  int min_dist = Integer . MAX_VALUE ;
  int prev = 0 ;
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] == x || arr [ i ] == y ) {
      prev = i ;
      break ;
    }
  }
  for ( ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] == x || arr [ i ] == y ) {
      if ( arr [ prev ] != arr [ i ] && ( i - prev ) < min_dist ) {
        min_dist = i - prev ;
        prev = i ;
      }
      else prev = i ;
    }
  }
  return min_dist ;
}
|||

UNION_AND_INTERSECTION_OF_TWO_SORTED_ARRAYS_2

static int printUnion ( int arr1 [ ] , int arr2 [ ] , int m , int n ) {
  int i = 0 , j = 0 ;
  while ( i < m && j < n ) {
    if ( arr1 [ i ] < arr2 [ j ] ) System . out . print ( arr1 [ i ++ ] + " " ) ;
    else if ( arr2 [ j ] < arr1 [ i ] ) System . out . print ( arr2 [ j ++ ] + " " ) ;
    else {
      System . out . print ( arr2 [ j ++ ] + " " ) ;
      i ++ ;
    }
  }
  while ( i < m ) System . out . print ( arr1 [ i ++ ] + " " ) ;
  while ( j < n ) System . out . print ( arr2 [ j ++ ] + " " ) ;
  return 0 ;
}
|||

WORD_WRAP_PROBLEM_SPACE_OPTIMIZED_SOLUTION

static void solveWordWrap ( int arr [ ] , int n , int k ) {
  int i , j ;
  int currlen ;
  int cost ;
  int dp [ ] = new int [ n ] ;
  int ans [ ] = new int [ n ] ;
  dp [ n - 1 ] = 0 ;
  ans [ n - 1 ] = n - 1 ;
  for ( i = n - 2 ;
  i >= 0 ;
  i -- ) {
    currlen = - 1 ;
    dp [ i ] = Integer . MAX_VALUE ;
    for ( j = i ;
    j < n ;
    j ++ ) {
      currlen += ( arr [ j ] + 1 ) ;
      if ( currlen > k ) break ;
      if ( j == n - 1 ) cost = 0 ;
      else cost = ( k - currlen ) * ( k - currlen ) + dp [ j + 1 ] ;
      if ( cost < dp [ i ] ) {
        dp [ i ] = cost ;
        ans [ i ] = j ;
      }
    }
  }
  i = 0 ;
  while ( i < n ) {
    System . out . print ( ( i + 1 ) + " " + ( ans [ i ] + 1 ) + " " ) ;
    i = ans [ i ] + 1 ;
  }
}
|||

COUNT_DISTINCT_SUBSEQUENCES

static int countSub ( String str ) {
  int [ ] last = new int [ MAX_CHAR ] ;
  Arrays . fill ( last , - 1 ) ;
  int n = str . length ( ) ;
  int [ ] dp = new int [ n + 1 ] ;
  dp [ 0 ] = 1 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    dp [ i ] = 2 * dp [ i - 1 ] ;
    if ( last [ ( int ) str . charAt ( i - 1 ) ] != - 1 ) dp [ i ] = dp [ i ] - dp [ last [ ( int ) str . charAt ( i - 1 ) ] ] ;
    last [ ( int ) str . charAt ( i - 1 ) ] = ( i - 1 ) ;
  }
  return dp [ n ] ;
}
|||

LONGEST_EVEN_LENGTH_SUBSTRING_SUM_FIRST_SECOND_HALF_3

static int findLength ( String str , int n ) {
  int ans = 0 ;
  for ( int i = 0 ;
  i <= n - 2 ;
  i ++ ) {
    int l = i , r = i + 1 ;
    int lsum = 0 , rsum = 0 ;
    while ( r < n && l >= 0 ) {
      lsum += str . charAt ( l ) - '0' ;
      rsum += str . charAt ( r ) - '0' ;
      if ( lsum == rsum ) {
        ans = Math . max ( ans , r - l + 1 ) ;
      }
      l -- ;
      r ++ ;
    }
  }
  return ans ;
}
|||

MAXIMUM_PATH_SUM_MATRIX

static int findMaxPath ( int mat [ ] [ ] ) {
  int res = - 1 ;
  for ( int i = 0 ;
  i < M ;
  i ++ ) res = max ( res , mat [ 0 ] [ i ] ) ;
  for ( int i = 1 ;
  i < N ;
  i ++ ) {
    res = - 1 ;
    for ( int j = 0 ;
    j < M ;
    j ++ ) {
      if ( j > 0 && j < M - 1 ) mat [ i ] [ j ] += max ( mat [ i - 1 ] [ j ] , max ( mat [ i - 1 ] [ j - 1 ] , mat [ i - 1 ] [ j + 1 ] ) ) ;
      else if ( j > 0 ) mat [ i ] [ j ] += max ( mat [ i - 1 ] [ j ] , mat [ i - 1 ] [ j - 1 ] ) ;
      else if ( j < M - 1 ) mat [ i ] [ j ] += max ( mat [ i - 1 ] [ j ] , mat [ i - 1 ] [ j + 1 ] ) ;
      res = max ( mat [ i ] [ j ] , res ) ;
    }
  }
  return res ;
}
|||

MAXIMUM_CONSECUTIVE_REPEATING_CHARACTER_STRING

static char maxRepeating ( String str ) {
  int len = str . length ( ) ;
  int count = 0 ;
  char res = str . charAt ( 0 ) ;
  for ( int i = 0 ;
  i < len ;
  i ++ ) {
    int cur_count = 1 ;
    for ( int j = i + 1 ;
    j < len ;
    j ++ ) {
      if ( str . charAt ( i ) != str . charAt ( j ) ) break ;
      cur_count ++ ;
    }
    if ( cur_count > count ) {
      count = cur_count ;
      res = str . charAt ( i ) ;
    }
  }
  return res ;
}
|||

MAXIMUM_LENGTH_SUBSEQUENCE_DIFFERENCE_ADJACENT_ELEMENTS_EITHER_0_1

public static int maxLenSub ( int arr [ ] , int n ) {
  int mls [ ] = new int [ n ] , max = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) mls [ i ] = 1 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) for ( int j = 0 ;
  j < i ;
  j ++ ) if ( Math . abs ( arr [ i ] - arr [ j ] ) <= 1 && mls [ i ] < mls [ j ] + 1 ) mls [ i ] = mls [ j ] + 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( max < mls [ i ] ) max = mls [ i ] ;
  return max ;
}
|||

BREAKING_NUMBER_FIRST_PART_INTEGRAL_DIVISION_SECOND_POWER_10

static int calculate ( String N ) {
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
|||

PROGRAM_BINARY_DECIMAL_CONVERSION

static int binaryToDecimal ( int n ) {
  int num = n ;
  int dec_value = 0 ;
  int base = 1 ;
  int temp = num ;
  while ( temp > 0 ) {
    int last_digit = temp % 10 ;
    temp = temp / 10 ;
    dec_value += last_digit * base ;
    base = base * 2 ;
  }
  return dec_value ;
}
|||

HOW_CAN_WE_SUM_THE_DIGITS_OF_A_GIVEN_NUMBER_IN_SINGLE_STATEMENT

static int getSum ( int n ) {
  int sum = 0 ;
  while ( n != 0 ) {
    sum = sum + n % 10 ;
    n = n / 10 ;
  }
  return sum ;
}
|||

FIND_N_TH_ELEMENT_FROM_STERNS_DIATOMIC_SERIES

static int findSDSFunc ( int n ) {
  int DP [ ] = new int [ n + 1 ] ;
  DP [ 0 ] = 0 ;
  DP [ 1 ] = 1 ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    if ( i % 2 == 0 ) DP [ i ] = DP [ i / 2 ] ;
    else DP [ i ] = DP [ ( i - 1 ) / 2 ] + DP [ ( i + 1 ) / 2 ] ;
  }
  return DP [ n ] ;
}
|||

NUMBER_SINK_NODES_GRAPH

static int countSink ( int n , int m , int edgeFrom [ ] , int edgeTo [ ] ) {
  int [ ] mark = new int [ n + 1 ] ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) mark [ edgeFrom [ i ] ] = 1 ;
  int count = 0 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) if ( mark [ i ] == 0 ) count ++ ;
  return count ;
}
|||

BREAK_NUMBER_THREE_PARTS

static long count_of_ways ( long n ) {
  long count = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) for ( int j = 0 ;
  j <= n ;
  j ++ ) for ( int k = 0 ;
  k <= n ;
  k ++ ) if ( i + j + k == n ) count ++ ;
  return count ;
}
|||

PRINT_DISTINCT_ELEMENTS_GIVEN_INTEGER_ARRAY

static void printDistinct ( int arr [ ] , int n ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int j ;
    for ( j = 0 ;
    j < i ;
    j ++ ) if ( arr [ i ] == arr [ j ] ) break ;
    if ( i == j ) System . out . print ( arr [ i ] + " " ) ;
  }
}
|||

MAXIMUM_NUMBER_SEGMENTS_LENGTHS_B_C

static int maximumSegments ( int n , int a , int b , int c ) {
  int dp [ ] = new int [ n + 10 ] ;
  Arrays . fill ( dp , - 1 ) ;
  dp [ 0 ] = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( dp [ i ] != - 1 ) {
      if ( i + a <= n ) dp [ i + a ] = Math . max ( dp [ i ] + 1 , dp [ i + a ] ) ;
      if ( i + b <= n ) dp [ i + b ] = Math . max ( dp [ i ] + 1 , dp [ i + b ] ) ;
      if ( i + c <= n ) dp [ i + c ] = Math . max ( dp [ i ] + 1 , dp [ i + c ] ) ;
    }
  }
  return dp [ n ] ;
}
|||

CHECK_VALID_SEQUENCE_DIVISIBLE_M

static boolean isPossible ( int n , int index , int sum , int M , int arr [ ] , int dp [ ] [ ] ) {
  if ( index == n ) {
    if ( ( sum % M ) == 0 ) return true ;
    return false ;
  }
  else if ( sum < 0 || sum >= MAX ) return false ;
  if ( dp [ index ] [ sum ] != - 1 ) {
    if ( dp [ index ] [ sum ] == 0 ) return false ;
    return true ;
  }
  boolean placeAdd = isPossible ( n , index + 1 , sum + arr [ index ] , M , arr , dp ) ;
  boolean placeMinus = isPossible ( n , index + 1 , sum - arr [ index ] , M , arr , dp ) ;
  boolean res = ( placeAdd || placeMinus ) ;
  dp [ index ] [ sum ] = ( res ) ? 1 : 0 ;
  return res ;
}
|||

FIND_PAIR_WITH_GREATEST_PRODUCT_IN_ARRAY

static int findGreatest ( int [ ] arr , int n ) {
  int result = - 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) for ( int j = 0 ;
  j < n - 1 ;
  j ++ ) for ( int k = j + 1 ;
  k < n ;
  k ++ ) if ( arr [ j ] * arr [ k ] == arr [ i ] ) result = Math . max ( result , arr [ i ] ) ;
  return result ;
}
|||

MAXIMUM_SUBARRAY_SUM_ARRAY_CREATED_REPEATED_CONCATENATION

static int maxSubArraySumRepeated ( int a [ ] , int n , int k ) {
  int max_so_far = 0 ;
  int INT_MIN , max_ending_here = 0 ;
  for ( int i = 0 ;
  i < n * k ;
  i ++ ) {
    max_ending_here = max_ending_here + a [ i % n ] ;
    if ( max_so_far < max_ending_here ) max_so_far = max_ending_here ;
    if ( max_ending_here < 0 ) max_ending_here = 0 ;
  }
  return max_so_far ;
}
|||

LEONARDO_NUMBER_1

static int leonardo ( int n ) {
  int dp [ ] = new int [ n + 1 ] ;
  dp [ 0 ] = dp [ 1 ] = 1 ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) dp [ i ] = dp [ i - 1 ] + dp [ i - 2 ] + 1 ;
  return dp [ n ] ;
}
|||

SUM_OF_ALL_SUBSTRINGS_OF_A_STRING_REPRESENTING_A_NUMBER

public static int sumOfSubstrings ( String num ) {
  int n = num . length ( ) ;
  int sumofdigit [ ] = new int [ n ] ;
  sumofdigit [ 0 ] = num . charAt ( 0 ) - '0' ;
  int res = sumofdigit [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    int numi = num . charAt ( i ) - '0' ;
    sumofdigit [ i ] = ( i + 1 ) * numi + 10 * sumofdigit [ i - 1 ] ;
    res += sumofdigit [ i ] ;
  }
  return res ;
}
|||

PRUFER_CODE_TREE_CREATION

static void printTreeEdges ( int prufer [ ] , int m ) {
  int vertices = m + 2 ;
  int vertex_set [ ] = new int [ vertices ] ;
  for ( int i = 0 ;
  i < vertices ;
  i ++ ) vertex_set [ i ] = 0 ;
  for ( int i = 0 ;
  i < vertices - 2 ;
  i ++ ) vertex_set [ prufer [ i ] - 1 ] += 1 ;
  System . out . print ( "\nThe edge set E(G) is :\n" ) ;
  int j = 0 ;
  for ( int i = 0 ;
  i < vertices - 2 ;
  i ++ ) {
    for ( j = 0 ;
    j < vertices ;
    j ++ ) {
      if ( vertex_set [ j ] == 0 ) {
        vertex_set [ j ] = - 1 ;
        System . out . print ( "(" + ( j + 1 ) + ", " + prufer [ i ] + ") " ) ;
        vertex_set [ prufer [ i ] - 1 ] -- ;
        break ;
      }
    }
  }
  j = 0 ;
  for ( int i = 0 ;
  i < vertices ;
  i ++ ) {
    if ( vertex_set [ i ] == 0 && j == 0 ) {
      System . out . print ( "(" + ( i + 1 ) + ", " ) ;
      j ++ ;
    }
    else if ( vertex_set [ i ] == 0 && j == 1 ) System . out . print ( ( i + 1 ) + ")\n" ) ;
  }
}
|||

PROGRAM_FIND_SMALLEST_DIFFERENCE_ANGLES_TWO_PARTS_GIVEN_CIRCLE

public static int findMinimumAngle ( int arr [ ] , int n ) {
  int l = 0 , sum = 0 , ans = 360 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    sum += arr [ i ] ;
    while ( sum >= 180 ) {
      ans = Math . min ( ans , 2 * Math . abs ( 180 - sum ) ) ;
      sum -= arr [ l ] ;
      l ++ ;
    }
    ans = Math . min ( ans , 2 * Math . abs ( 180 - sum ) ) ;
  }
  return ans ;
}
|||

FIND_MAXIMUM_AVERAGE_SUBARRAY_OF_K_LENGTH

static int findMaxAverage ( int [ ] arr , int n , int k ) {
  if ( k > n ) return - 1 ;
  int [ ] csum = new int [ n ] ;
  csum [ 0 ] = arr [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) csum [ i ] = csum [ i - 1 ] + arr [ i ] ;
  int max_sum = csum [ k - 1 ] , max_end = k - 1 ;
  for ( int i = k ;
  i < n ;
  i ++ ) {
    int curr_sum = csum [ i ] - csum [ i - k ] ;
    if ( curr_sum > max_sum ) {
      max_sum = curr_sum ;
      max_end = i ;
    }
  }
  return max_end - k + 1 ;
}
|||

SQUARE_PYRAMIDAL_NUMBER_SUM_SQUARES

static int findS ( int s ) {
  int sum = 0 ;
  for ( int n = 1 ;
  sum < s ;
  n ++ ) {
    sum += n * n ;
    if ( sum == s ) return n ;
  }
  return - 1 ;
}
|||

PROGRAM_TO_CALCULATE_AREA_OF_AN_CIRCLE_INSCRIBED_IN_A_SQUARE

static double areaOfInscribedCircle ( float a ) {
  return ( PI / 4 ) * a * a ;
}
|||

MINIMUM_NUMBER_CHARACTERS_REMOVED_MAKE_BINARY_STRING_ALTERNATE

static int countToMake0lternate ( String s ) {
  int result = 0 ;
  for ( int i = 0 ;
  i < ( s . length ( ) - 1 ) ;
  i ++ ) if ( s . charAt ( i ) == s . charAt ( i + 1 ) ) result ++ ;
  return result ;
}
|||

FIND_ELEMENTS_PRESENT_FIRST_ARRAY_NOT_SECOND

static void findMissing ( int a [ ] , int b [ ] , int n , int m ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int j ;
    for ( j = 0 ;
    j < m ;
    j ++ ) if ( a [ i ] == b [ j ] ) break ;
    if ( j == m ) System . out . print ( a [ i ] + " " ) ;
  }
}
|||

REARRANGE_ARRAY_MAXIMUM_MINIMUM_FORM

static void rearrange ( int [ ] arr , int n ) {
  int temp [ ] = new int [ n ] ;
  int small = 0 , large = n - 1 ;
  boolean flag = true ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( flag ) temp [ i ] = arr [ large -- ] ;
    else temp [ i ] = arr [ small ++ ] ;
    flag = ! flag ;
  }
  arr = temp . clone ( ) ;
}
|||

DYNAMIC_PROGRAMMING_SET_15_LONGEST_BITONIC_SUBSEQUENCE

static int lbs ( int arr [ ] , int n ) {
  int i , j ;
  int [ ] lis = new int [ n ] ;
  for ( i = 0 ;
  i < n ;
  i ++ ) lis [ i ] = 1 ;
  for ( i = 1 ;
  i < n ;
  i ++ ) for ( j = 0 ;
  j < i ;
  j ++ ) if ( arr [ i ] > arr [ j ] && lis [ i ] < lis [ j ] + 1 ) lis [ i ] = lis [ j ] + 1 ;
  int [ ] lds = new int [ n ] ;
  for ( i = 0 ;
  i < n ;
  i ++ ) lds [ i ] = 1 ;
  for ( i = n - 2 ;
  i >= 0 ;
  i -- ) for ( j = n - 1 ;
  j > i ;
  j -- ) if ( arr [ i ] > arr [ j ] && lds [ i ] < lds [ j ] + 1 ) lds [ i ] = lds [ j ] + 1 ;
  int max = lis [ 0 ] + lds [ 0 ] - 1 ;
  for ( i = 1 ;
  i < n ;
  i ++ ) if ( lis [ i ] + lds [ i ] - 1 > max ) max = lis [ i ] + lds [ i ] - 1 ;
  return max ;
}
|||

COUNT_PAIRS_WHOSE_PRODUCTS_EXIST_IN_ARRAY

static int countPairs ( int arr [ ] , int n ) {
  int result = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      int product = arr [ i ] * arr [ j ] ;
      for ( int k = 0 ;
      k < n ;
      k ++ ) {
        if ( arr [ k ] == product ) {
          result ++ ;
          break ;
        }
      }
    }
  }
  return result ;
}
|||

COUNT_SINGLE_NODE_ISOLATED_SUB_GRAPHS_DISCONNECTED_GRAPH

static int compute ( int [ ] graph , int N ) {
  int count = 0 ;
  for ( int i = 1 ;
  i < 7 ;
  i ++ ) {
    if ( graph [ i ] == 0 ) count ++ ;
  }
  return count ;
}
|||

HARDY_RAMANUJAN_THEOREM

static int exactPrimeFactorCount ( int n ) {
  int count = 0 ;
  if ( n % 2 == 0 ) {
    count ++ ;
    while ( n % 2 == 0 ) n = n / 2 ;
  }
  for ( int i = 3 ;
  i <= Math . sqrt ( n ) ;
  i = i + 2 ) {
    if ( n % i == 0 ) {
      count ++ ;
      while ( n % i == 0 ) n = n / i ;
    }
  }
  if ( n > 2 ) count ++ ;
  return count ;
}
|||

SHORTEST_COMMON_SUPERSEQUENCE_1

static int superSeq ( String X , String Y , int m , int n ) {
  int [ ] [ ] dp = new int [ m + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i <= m ;
  i ++ ) {
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      if ( i == 0 ) dp [ i ] [ j ] = j ;
      else if ( j == 0 ) dp [ i ] [ j ] = i ;
      else if ( X . charAt ( i - 1 ) == Y . charAt ( j - 1 ) ) dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ] ;
      else dp [ i ] [ j ] = 1 + Math . min ( dp [ i - 1 ] [ j ] , dp [ i ] [ j - 1 ] ) ;
    }
  }
  return dp [ m ] [ n ] ;
}
|||

POWER_SET

static void printPowerSet ( char [ ] set , int set_size ) {
  long pow_set_size = ( long ) Math . pow ( 2 , set_size ) ;
  int counter , j ;
  for ( counter = 0 ;
  counter < pow_set_size ;
  counter ++ ) {
    for ( j = 0 ;
    j < set_size ;
    j ++ ) {
      if ( ( counter & ( 1 << j ) ) > 0 ) System . out . print ( set [ j ] ) ;
    }
    System . out . println ( ) ;
  }
}
|||

CHECK_ARRAY_MAJORITY_ELEMENT

static boolean isMajority ( int a [ ] , int n ) {
  HashMap < Integer , Integer > mp = new HashMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( mp . containsKey ( a [ i ] ) ) mp . put ( a [ i ] , mp . get ( a [ i ] ) + 1 ) ;
  else mp . put ( a [ i ] , 1 ) ;
  for ( Map . Entry < Integer , Integer > x : mp . entrySet ( ) ) if ( x . getValue ( ) >= n / 2 ) return true ;
  return false ;
}
|||

PRINT_GIVEN_MATRIX_COUNTER_CLOCK_WISE_SPIRAL_FORM

static void counterClockspiralPrint ( int m , int n , int arr [ ] [ ] ) {
  int i , k = 0 , l = 0 ;
  int cnt = 0 ;
  int total = m * n ;
  while ( k < m && l < n ) {
    if ( cnt == total ) break ;
    for ( i = k ;
    i < m ;
    ++ i ) {
      System . out . print ( arr [ i ] [ l ] + " " ) ;
      cnt ++ ;
    }
    l ++ ;
    if ( cnt == total ) break ;
    for ( i = l ;
    i < n ;
    ++ i ) {
      System . out . print ( arr [ m - 1 ] [ i ] + " " ) ;
      cnt ++ ;
    }
    m -- ;
    if ( cnt == total ) break ;
    if ( k < m ) {
      for ( i = m - 1 ;
      i >= k ;
      -- i ) {
        System . out . print ( arr [ i ] [ n - 1 ] + " " ) ;
        cnt ++ ;
      }
      n -- ;
    }
    if ( cnt == total ) break ;
    if ( l < n ) {
      for ( i = n - 1 ;
      i >= l ;
      -- i ) {
        System . out . print ( arr [ k ] [ i ] + " " ) ;
        cnt ++ ;
      }
      k ++ ;
    }
  }
}
|||

PRIMALITY_TEST_SET_1_INTRODUCTION_AND_SCHOOL_METHOD

static boolean isPrime ( int n ) {
  if ( n <= 1 ) return false ;
  for ( int i = 2 ;
  i < n ;
  i ++ ) if ( n % i == 0 ) return false ;
  return true ;
}
|||

FIND_CHARACTER_FIRST_STRING_PRESENT_MINIMUM_INDEX_SECOND_STRING

static void printMinIndexChar ( String str , String patt ) {
  int minIndex = Integer . MAX_VALUE ;
  int m = str . length ( ) ;
  int n = patt . length ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < m ;
    j ++ ) {
      if ( patt . charAt ( i ) == str . charAt ( j ) && j < minIndex ) {
        minIndex = j ;
        break ;
      }
    }
  }
  if ( minIndex != Integer . MAX_VALUE ) System . out . println ( "Minimum Index Character = " + str . charAt ( minIndex ) ) ;
  else System . out . println ( "No character present" ) ;
}
|||

PROGRAM_TO_FIND_TRANSPOSE_OF_A_MATRIX_1

static void transpose ( int A [ ] [ ] , int B [ ] [ ] ) {
  int i , j ;
  for ( i = 0 ;
  i < N ;
  i ++ ) for ( j = 0 ;
  j < M ;
  j ++ ) B [ i ] [ j ] = A [ j ] [ i ] ;
}
|||

COUNT_NATURAL_NUMBERS_WHOSE_PERMUTATION_GREATER_NUMBER

static int countNumber ( int n ) {
  int result = 0 ;
  for ( int i = 1 ;
  i <= 9 ;
  i ++ ) {
    Stack < Integer > s = new Stack < > ( ) ;
    if ( i <= n ) {
      s . push ( i ) ;
      result ++ ;
    }
    while ( ! s . empty ( ) ) {
      int tp = s . peek ( ) ;
      s . pop ( ) ;
      for ( int j = tp % 10 ;
      j <= 9 ;
      j ++ ) {
        int x = tp * 10 + j ;
        if ( x <= n ) {
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

static int firstFactorialDivisibleNumber ( int x ) {
  int i = 1 ;
  int fact = 1 ;
  for ( i = 1 ;
  i < x ;
  i ++ ) {
    fact = fact * i ;
    if ( fact % x == 0 ) break ;
  }
  return i ;
}
|||

PRINT_EQUAL_SUM_SETS_ARRAY_PARTITION_PROBLEM_SET_2

static void printEqualSumSets ( int [ ] arr , int n ) {
  int i , currSum , sum = 0 ;
  for ( i = 0 ;
  i < arr . length ;
  i ++ ) sum += arr [ i ] ;
  if ( ( sum & 1 ) == 1 ) {
    System . out . print ( "-1" ) ;
    return ;
  }
  int k = sum >> 1 ;
  boolean [ ] [ ] dp = new boolean [ n + 1 ] [ k + 1 ] ;
  for ( i = 1 ;
  i <= k ;
  i ++ ) dp [ 0 ] [ i ] = false ;
  for ( i = 0 ;
  i <= n ;
  i ++ ) dp [ i ] [ 0 ] = true ;
  for ( i = 1 ;
  i <= n ;
  i ++ ) {
    for ( currSum = 1 ;
    currSum <= k ;
    currSum ++ ) {
      dp [ i ] [ currSum ] = dp [ i - 1 ] [ currSum ] ;
      if ( arr [ i - 1 ] <= currSum ) dp [ i ] [ currSum ] = dp [ i ] [ currSum ] | dp [ i - 1 ] [ currSum - arr [ i - 1 ] ] ;
    }
  }
  List < Integer > set1 = new ArrayList < Integer > ( ) ;
  List < Integer > set2 = new ArrayList < Integer > ( ) ;
  if ( ! dp [ n ] [ k ] ) {
    System . out . print ( "-1\n" ) ;
    return ;
  }
  i = n ;
  currSum = k ;
  while ( i > 0 && currSum >= 0 ) {
    if ( dp [ i - 1 ] [ currSum ] ) {
      i -- ;
      set2 . add ( arr [ i ] ) ;
    }
    else if ( dp [ i - 1 ] [ currSum - arr [ i - 1 ] ] ) {
      i -- ;
      currSum -= arr [ i ] ;
      set1 . add ( arr [ i ] ) ;
    }
  }
  System . out . print ( "Set 1 elements: " ) ;
  for ( i = 0 ;
  i < set1 . size ( ) ;
  i ++ ) System . out . print ( set1 . get ( i ) + " " ) ;
  System . out . print ( "\nSet 2 elements: " ) ;
  for ( i = 0 ;
  i < set2 . size ( ) ;
  i ++ ) System . out . print ( set2 . get ( i ) + " " ) ;
}
|||

COUNTING_PAIRS_PERSON_CAN_FORM_PAIR_ONE_1

static int numberOfWays ( int x ) {
  int dp [ ] = new int [ x + 1 ] ;
  dp [ 0 ] = dp [ 1 ] = 1 ;
  for ( int i = 2 ;
  i <= x ;
  i ++ ) dp [ i ] = dp [ i - 1 ] + ( i - 1 ) * dp [ i - 2 ] ;
  return dp [ x ] ;
}
|||

COUNT_NEGATIVE_NUMBERS_IN_A_COLUMN_WISE_ROW_WISE_SORTED_MATRIX

static int countNegative ( int M [ ] [ ] , int n , int m ) {
  int count = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < m ;
    j ++ ) {
      if ( M [ i ] [ j ] < 0 ) count += 1 ;
      else break ;
    }
  }
  return count ;
}
|||

COUNT_SET_BITS_IN_AN_INTEGER

static int countSetBits ( int n ) {
  int count = 0 ;
  while ( n > 0 ) {
    count += n & 1 ;
    n >>= 1 ;
  }
  return count ;
}
|||

MODULUS_TWO_FLOAT_DOUBLE_NUMBERS

static double findMod ( double a , double b ) {
  if ( a < 0 ) a = - a ;
  if ( b < 0 ) b = - b ;
  double mod = a ;
  while ( mod >= b ) mod = mod - b ;
  if ( a < 0 ) return - mod ;
  return mod ;
}
|||

FIND_A_SPECIFIC_PAIR_IN_MATRIX_1

static int findMaxValue ( int N , int mat [ ] [ ] ) {
  int maxValue = Integer . MIN_VALUE ;
  int maxArr [ ] [ ] = new int [ N ] [ N ] ;
  maxArr [ N - 1 ] [ N - 1 ] = mat [ N - 1 ] [ N - 1 ] ;
  int maxv = mat [ N - 1 ] [ N - 1 ] ;
  for ( int j = N - 2 ;
  j >= 0 ;
  j -- ) {
    if ( mat [ N - 1 ] [ j ] > maxv ) maxv = mat [ N - 1 ] [ j ] ;
    maxArr [ N - 1 ] [ j ] = maxv ;
  }
  maxv = mat [ N - 1 ] [ N - 1 ] ;
  for ( int i = N - 2 ;
  i >= 0 ;
  i -- ) {
    if ( mat [ i ] [ N - 1 ] > maxv ) maxv = mat [ i ] [ N - 1 ] ;
    maxArr [ i ] [ N - 1 ] = maxv ;
  }
  for ( int i = N - 2 ;
  i >= 0 ;
  i -- ) {
    for ( int j = N - 2 ;
    j >= 0 ;
    j -- ) {
      if ( maxArr [ i + 1 ] [ j + 1 ] - mat [ i ] [ j ] > maxValue ) maxValue = maxArr [ i + 1 ] [ j + 1 ] - mat [ i ] [ j ] ;
      maxArr [ i ] [ j ] = Math . max ( mat [ i ] [ j ] , Math . max ( maxArr [ i ] [ j + 1 ] , maxArr [ i + 1 ] [ j ] ) ) ;
    }
  }
  return maxValue ;
}
|||

MINIMUM_SUM_TWO_NUMBERS_FORMED_DIGITS_ARRAY

static int solve ( int arr [ ] , int n ) {
  Arrays . sort ( arr ) ;
  int a = 0 , b = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( i % 2 != 0 ) a = a * 10 + arr [ i ] ;
    else b = b * 10 + arr [ i ] ;
  }
  return a + b ;
}
|||

COUNT_DISTINCT_NON_NEGATIVE_PAIRS_X_Y_SATISFY_INEQUALITY_XX_YY_N_2_1

static int countSolutions ( int n ) {
  int x = 0 , yCount , res = 0 ;
  for ( yCount = 0 ;
  yCount * yCount < n ;
  yCount ++ ) ;
  while ( yCount != 0 ) {
    res += yCount ;
    x ++ ;
    while ( yCount != 0 && ( x * x + ( yCount - 1 ) * ( yCount - 1 ) >= n ) ) yCount -- ;
  }
  return res ;
}
|||

FIND_INDEX_GIVEN_FIBONACCI_NUMBER_CONSTANT_TIME

static int findIndex ( int n ) {
  if ( n <= 1 ) return n ;
  int a = 0 , b = 1 , c = 1 ;
  int res = 1 ;
  while ( c < n ) {
    c = a + b ;
    res ++ ;
    a = b ;
    b = c ;
  }
  return res ;
}
|||

PROGRAM_OCTAL_DECIMAL_CONVERSION

static int octalToDecimal ( int n ) {
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
|||

FIND_PERMUTED_ROWS_GIVEN_ROW_MATRIX

static void permutatedRows ( int mat [ ] [ ] , int m , int n , int r ) {
  LinkedHashSet < Integer > s = new LinkedHashSet < > ( ) ;
  for ( int j = 0 ;
  j < n ;
  j ++ ) s . add ( mat [ r ] [ j ] ) ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) {
    if ( i == r ) continue ;
    int j ;
    for ( j = 0 ;
    j < n ;
    j ++ ) if ( ! s . contains ( mat [ i ] [ j ] ) ) break ;
    if ( j != n ) continue ;
    System . out . print ( i + ", " ) ;
  }
}
|||

PRINT_A_CLOSEST_STRING_THAT_DOES_NOT_CONTAIN_ADJACENT_DUPLICATES

public static String noAdjacentDup ( String s1 ) {
  int n = s1 . length ( ) ;
  char [ ] s = s1 . toCharArray ( ) ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( s [ i ] == s [ i - 1 ] ) {
      s [ i ] = 'a' ;
      while ( s [ i ] == s [ i - 1 ] || ( i + 1 < n && s [ i ] == s [ i + 1 ] ) ) s [ i ] ++ ;
      i ++ ;
    }
  }
  return ( new String ( s ) ) ;
}
|||

SUM_MANHATTAN_DISTANCES_PAIRS_POINTS

static int distancesum ( int x [ ] , int y [ ] , int n ) {
  int sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) for ( int j = i + 1 ;
  j < n ;
  j ++ ) sum += ( Math . abs ( x [ i ] - x [ j ] ) + Math . abs ( y [ i ] - y [ j ] ) ) ;
  return sum ;
}
|||

PROGRAM_FIND_STRING_START_END_GEEKS

static boolean isCornerPresent ( String str , String corner ) {
  int n = str . length ( ) ;
  int cl = corner . length ( ) ;
  if ( n < cl ) return false ;
  return ( str . substring ( 0 , cl ) . equals ( corner ) && str . substring ( n - cl , n ) . equals ( corner ) ) ;
}
|||

LONGEST_SUBARRAY_COUNT_1S_ONE_COUNT_0S

static int lenOfLongSubarr ( int arr [ ] , int n ) {
  HashMap < Integer , Integer > um = new HashMap < Integer , Integer > ( ) ;
  int sum = 0 , maxLen = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    sum += arr [ i ] == 0 ? - 1 : 1 ;
    if ( sum == 1 ) maxLen = i + 1 ;
    else if ( ! um . containsKey ( sum ) ) um . put ( sum , i ) ;
    if ( um . containsKey ( sum - 1 ) ) {
      if ( maxLen < ( i - um . get ( sum - 1 ) ) ) maxLen = i - um . get ( sum - 1 ) ;
    }
  }
  return maxLen ;
}
|||

DIVIDE_CONQUER_SET_6_SEARCH_ROW_WISE_COLUMN_WISE_SORTED_2D_ARRAY

public static void search ( int [ ] [ ] mat , int fromRow , int toRow , int fromCol , int toCol , int key ) {
  int i = fromRow + ( toRow - fromRow ) / 2 ;
  int j = fromCol + ( toCol - fromCol ) / 2 ;
  if ( mat [ i ] [ j ] == key ) System . out . println ( "Found " + key + " at " + i + " " + j ) ;
  else {
    if ( i != toRow || j != fromCol ) search ( mat , fromRow , i , j , toCol , key ) ;
    if ( fromRow == toRow && fromCol + 1 == toCol ) if ( mat [ fromRow ] [ toCol ] == key ) System . out . println ( "Found " + key + " at " + fromRow + " " + toCol ) ;
    if ( mat [ i ] [ j ] < key ) {
      if ( i + 1 <= toRow ) search ( mat , i + 1 , toRow , fromCol , toCol , key ) ;
    }
    else {
      if ( j - 1 >= fromCol ) search ( mat , fromRow , toRow , fromCol , j - 1 , key ) ;
    }
  }
}
|||

SHORTEST_COMMON_SUPERSEQUENCE

static int superSeq ( String X , String Y , int m , int n ) {
  if ( m == 0 ) return n ;
  if ( n == 0 ) return m ;
  if ( X . charAt ( m - 1 ) == Y . charAt ( n - 1 ) ) return 1 + superSeq ( X , Y , m - 1 , n - 1 ) ;
  return 1 + Math . min ( superSeq ( X , Y , m - 1 , n ) , superSeq ( X , Y , m , n - 1 ) ) ;
}
|||

URLIFY_GIVEN_STRING_REPLACE_SPACES

static char [ ] replaceSpaces ( char [ ] str ) {
  int space_count = 0 , i = 0 ;
  for ( i = 0 ;
  i < str . length ;
  i ++ ) if ( str [ i ] == ' ' ) space_count ++ ;
  while ( str [ i - 1 ] == ' ' ) {
    space_count -- ;
    i -- ;
  }
  int new_length = i + space_count * 2 ;
  if ( new_length > MAX ) return str ;
  int index = new_length - 1 ;
  char [ ] new_str = str ;
  str = new char [ new_length ] ;
  for ( int j = i - 1 ;
  j >= 0 ;
  j -- ) {
    if ( new_str [ j ] == ' ' ) {
      str [ index ] = '0' ;
      str [ index - 1 ] = '2' ;
      str [ index - 2 ] = '%' ;
      index = index - 3 ;
    }
    else {
      str [ index ] = new_str [ j ] ;
      index -- ;
    }
  }
  return str ;
}
|||

MAXIMUM_PATH_SUM_STARTING_CELL_0_TH_ROW_ENDING_CELL_N_1_TH_ROW

static int MaximumPath ( int Mat [ ] [ ] ) {
  int result = 0 ;
  int dp [ ] [ ] = new int [ N ] [ N + 2 ] ;
  for ( int [ ] rows : dp ) Arrays . fill ( rows , 0 ) ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) dp [ 0 ] [ i + 1 ] = Mat [ 0 ] [ i ] ;
  for ( int i = 1 ;
  i < N ;
  i ++ ) for ( int j = 1 ;
  j <= N ;
  j ++ ) dp [ i ] [ j ] = Math . max ( dp [ i - 1 ] [ j - 1 ] , Math . max ( dp [ i - 1 ] [ j ] , dp [ i - 1 ] [ j + 1 ] ) ) + Mat [ i ] [ j - 1 ] ;
  for ( int i = 0 ;
  i <= N ;
  i ++ ) result = Math . max ( result , dp [ N - 1 ] [ i ] ) ;
  return result ;
}
|||

COMPUTE_THE_INTEGER_ABSOLUTE_VALUE_ABS_WITHOUT_BRANCHING

static int getAbs ( int n ) {
  int mask = n >> ( SIZE_INT * CHAR_BIT - 1 ) ;
  return ( ( n + mask ) ^ mask ) ;
}
|||

COUNT_PALINDROMIC_SUBSEQUENCE_GIVEN_STRING_1

static int countPS ( int i , int j ) {
  if ( i >= n || j < 0 ) return 0 ;
  if ( dp [ i ] [ j ] != - 1 ) return dp [ i ] [ j ] ;
  if ( ( i - j == 1 ) || ( i - j == - 1 ) ) {
    if ( str . charAt ( i ) == str . charAt ( j ) ) return dp [ i ] [ j ] = 3 ;
    else return dp [ i ] [ j ] = 2 ;
  }
  if ( i == j ) return dp [ 1 ] [ j ] = 1 ;
  else if ( str . charAt ( i ) == str . charAt ( j ) ) return dp [ i ] [ j ] = countPS ( i + 1 , j ) + countPS ( i , j - 1 ) + 1 ;
  else return dp [ i ] [ j ] = countPS ( i + 1 , j ) + countPS ( i , j - 1 ) - countPS ( i + 1 , j - 1 ) ;
}
|||

LARGEST_SUM_CONTIGUOUS_SUBARRAY_2

static int maxSubArraySum ( int a [ ] , int size ) {
  int max_so_far = a [ 0 ] ;
  int curr_max = a [ 0 ] ;
  for ( int i = 1 ;
  i < size ;
  i ++ ) {
    curr_max = Math . max ( a [ i ] , curr_max + a [ i ] ) ;
    max_so_far = Math . max ( max_so_far , curr_max ) ;
  }
  return max_so_far ;
}
|||

COUNT_MINIMUM_STEPS_GET_GIVEN_DESIRED_ARRAY

static int countMinOperations ( int n ) {
  int result = 0 ;
  while ( true ) {
    int zero_count = 0 ;
    int i ;
    for ( i = 0 ;
    i < n ;
    i ++ ) {
      if ( arr [ i ] % 2 == 1 ) break ;
      else if ( arr [ i ] == 0 ) zero_count ++ ;
    }
    if ( zero_count == n ) return result ;
    if ( i == n ) {
      for ( int j = 0 ;
      j < n ;
      j ++ ) arr [ j ] = arr [ j ] / 2 ;
      result ++ ;
    }
    for ( int j = i ;
    j < n ;
    j ++ ) {
      if ( arr [ j ] % 2 == 1 ) {
        arr [ j ] -- ;
        result ++ ;
      }
    }
  }
}
|||

PRINT_FIBONACCI_SEQUENCE_USING_2_VARIABLES_1

static void fib ( int n ) {
  int a = 0 , b = 1 ;
  if ( n >= 0 ) System . out . print ( a + " " ) ;
  if ( n >= 1 ) System . out . print ( b + " " ) ;
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

static boolean isNumber ( String s ) {
  for ( int i = 0 ;
  i < s . length ( ) ;
  i ++ ) if ( Character . isDigit ( s . charAt ( i ) ) == false ) return false ;
  return true ;
}
|||

MINIMUM_HEIGHT_TRIANGLE_GIVEN_BASE_AREA

static double minHeight ( double base , double area ) {
  double d = ( 2 * area ) / base ;
  return Math . ceil ( d ) ;
}
|||

FIND_POSITION_GIVEN_NUMBER_AMONG_NUMBERS_MADE_4_7

static int findpos ( String n ) {
  int k = 0 , pos = 0 , i = 0 ;
  while ( k != n . length ( ) ) {
    switch ( n . charAt ( i ) ) {
      case '4' : pos = pos * 2 + 1 ;
      break ;
      case '7' : pos = pos * 2 + 2 ;
      break ;
    }
    i ++ ;
    k ++ ;
  }
  return pos ;
}
|||

MINIMUM_OPERATIONS_REQUIRED_SET_ELEMENTS_BINARY_MATRIX

static int minOperation ( boolean arr [ ] [ ] ) {
  int ans = 0 ;
  for ( int i = N - 1 ;
  i >= 0 ;
  i -- ) {
    for ( int j = M - 1 ;
    j >= 0 ;
    j -- ) {
      if ( arr [ i ] [ j ] == false ) {
        ans ++ ;
        for ( int k = 0 ;
        k <= i ;
        k ++ ) {
          for ( int h = 0 ;
          h <= j ;
          h ++ ) {
            if ( arr [ k ] [ h ] == true ) {
              arr [ k ] [ h ] = false ;
            }
            else {
              arr [ k ] [ h ] = true ;
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

static int findLength ( String str , int n ) {
  int sum [ ] = new int [ n + 1 ] ;
  sum [ 0 ] = 0 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) sum [ i ] = ( sum [ i - 1 ] + str . charAt ( i - 1 ) - '0' ) ;
  int ans = 0 ;
  for ( int len = 2 ;
  len <= n ;
  len += 2 ) {
    for ( int i = 0 ;
    i <= n - len ;
    i ++ ) {
      int j = i + len - 1 ;
      if ( sum [ i + len / 2 ] - sum [ i ] == sum [ i + len ] - sum [ i + len / 2 ] ) ans = Math . max ( ans , len ) ;
    }
  }
  return ans ;
}
|||

MULTIPLY_LARGE_NUMBERS_REPRESENTED_AS_STRINGS

static String multiply ( String num1 , String num2 ) {
  int len1 = num1 . length ( ) ;
  int len2 = num2 . length ( ) ;
  if ( len1 == 0 || len2 == 0 ) return "0" ;
  int result [ ] = new int [ len1 + len2 ] ;
  int i_n1 = 0 ;
  int i_n2 = 0 ;
  for ( int i = len1 - 1 ;
  i >= 0 ;
  i -- ) {
    int carry = 0 ;
    int n1 = num1 . charAt ( i ) - '0' ;
    i_n2 = 0 ;
    for ( int j = len2 - 1 ;
    j >= 0 ;
    j -- ) {
      int n2 = num2 . charAt ( j ) - '0' ;
      int sum = n1 * n2 + result [ i_n1 + i_n2 ] + carry ;
      carry = sum / 10 ;
      result [ i_n1 + i_n2 ] = sum % 10 ;
      i_n2 ++ ;
    }
    if ( carry > 0 ) result [ i_n1 + i_n2 ] += carry ;
    i_n1 ++ ;
  }
  int i = result . length - 1 ;
  while ( i >= 0 && result [ i ] == 0 ) i -- ;
  if ( i == - 1 ) return "0" ;
  String s = "" ;
  while ( i >= 0 ) s += ( result [ i -- ] ) ;
  return s ;
}
|||

PARTITION_NUMBER_TWO_DIVISBLE_PARTS

static void findDivision ( String str , int a , int b ) {
  int len = str . length ( ) ;
  int [ ] lr = new int [ len + 1 ] ;
  lr [ 0 ] = ( ( int ) str . charAt ( 0 ) - ( int ) '0' ) % a ;
  for ( int i = 1 ;
  i < len ;
  i ++ ) lr [ i ] = ( ( lr [ i - 1 ] * 10 ) % a + ( ( int ) str . charAt ( i ) - ( int ) '0' ) ) % a ;
  int [ ] rl = new int [ len + 1 ] ;
  rl [ len - 1 ] = ( ( int ) str . charAt ( len - 1 ) - ( int ) '0' ) % b ;
  int power10 = 10 ;
  for ( int i = len - 2 ;
  i >= 0 ;
  i -- ) {
    rl [ i ] = ( rl [ i + 1 ] + ( ( int ) str . charAt ( i ) - ( int ) '0' ) * power10 ) % b ;
    power10 = ( power10 * 10 ) % b ;
  }
  for ( int i = 0 ;
  i < len - 1 ;
  i ++ ) {
    if ( lr [ i ] != 0 ) continue ;
    if ( rl [ i + 1 ] == 0 ) {
      System . out . println ( "YES" ) ;
      for ( int k = 0 ;
      k <= i ;
      k ++ ) System . out . print ( str . charAt ( k ) ) ;
      System . out . print ( ", " ) ;
      for ( int k = i + 1 ;
      k < len ;
      k ++ ) System . out . print ( str . charAt ( k ) ) ;
      return ;
    }
  }
  System . out . println ( "NO" ) ;
}
|||

PROGRAM_BEST_FIT_ALGORITHM_MEMORY_MANAGEMENT

static void bestFit ( int blockSize [ ] , int m , int processSize [ ] , int n ) {
  int allocation [ ] = new int [ n ] ;
  for ( int i = 0 ;
  i < allocation . length ;
  i ++ ) allocation [ i ] = - 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int bestIdx = - 1 ;
    for ( int j = 0 ;
    j < m ;
    j ++ ) {
      if ( blockSize [ j ] >= processSize [ i ] ) {
        if ( bestIdx == - 1 ) bestIdx = j ;
        else if ( blockSize [ bestIdx ] > blockSize [ j ] ) bestIdx = j ;
      }
    }
    if ( bestIdx != - 1 ) {
      allocation [ i ] = bestIdx ;
      blockSize [ bestIdx ] -= processSize [ i ] ;
    }
  }
  System . out . println ( "\nProcess No.\tProcess Size\tBlock no." ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    System . out . print ( "   " + ( i + 1 ) + "\t\t" + processSize [ i ] + "\t\t" ) ;
    if ( allocation [ i ] != - 1 ) System . out . print ( allocation [ i ] + 1 ) ;
    else System . out . print ( "Not Allocated" ) ;
    System . out . println ( ) ;
  }
}
|||

FINDING_THE_MAXIMUM_SQUARE_SUB_MATRIX_WITH_ALL_EQUAL_ELEMENTS

static int largestKSubmatrix ( int [ ] [ ] a ) {
  int [ ] [ ] dp = new int [ Row ] [ Col ] ;
  int result = 0 ;
  for ( int i = 0 ;
  i < Row ;
  i ++ ) {
    for ( int j = 0 ;
    j < Col ;
    j ++ ) {
      if ( i == 0 || j == 0 ) dp [ i ] [ j ] = 1 ;
      else {
        if ( a [ i ] [ j ] == a [ i - 1 ] [ j ] && a [ i ] [ j ] == a [ i ] [ j - 1 ] && a [ i ] [ j ] == a [ i - 1 ] [ j - 1 ] ) {
          dp [ i ] [ j ] = ( dp [ i - 1 ] [ j ] > dp [ i ] [ j - 1 ] && dp [ i - 1 ] [ j ] > dp [ i - 1 ] [ j - 1 ] + 1 ) ? dp [ i - 1 ] [ j ] : ( dp [ i ] [ j - 1 ] > dp [ i - 1 ] [ j ] && dp [ i ] [ j - 1 ] > dp [ i - 1 ] [ j - 1 ] + 1 ) ? dp [ i ] [ j - 1 ] : dp [ i - 1 ] [ j - 1 ] + 1 ;
        }
        else dp [ i ] [ j ] = 1 ;
      }
      result = result > dp [ i ] [ j ] ? result : dp [ i ] [ j ] ;
    }
  }
  return result ;
}
|||

FRIENDS_PAIRING_PROBLEM_1

static int countFriendsPairings ( int n ) {
  if ( dp [ n ] != - 1 ) return dp [ n ] ;
  if ( n > 2 ) return dp [ n ] = countFriendsPairings ( n - 1 ) + ( n - 1 ) * countFriendsPairings ( n - 2 ) ;
  else return dp [ n ] = n ;
}
|||

FIRST_ELEMENT_OCCURRING_K_TIMES_ARRAY

static int firstElement ( int arr [ ] , int n , int k ) {
  HashMap < Integer , Integer > count_map = new HashMap < > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int a = 0 ;
    if ( count_map . get ( arr [ i ] ) != null ) {
      a = count_map . get ( arr [ i ] ) ;
    }
    count_map . put ( arr [ i ] , a + 1 ) ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( count_map . get ( arr [ i ] ) == k ) {
      return arr [ i ] ;
    }
  }
  return - 1 ;
}
|||

SUM_SERIES_0_6_0_06_0_006_0_0006_N_TERMS

static double sumOfSeries ( int n ) {
  return ( 0.666 ) * ( 1 - 1 / Math . pow ( 10 , n ) ) ;
}
|||

COUNT_WORDS_IN_A_GIVEN_STRING

static int countWords ( String str ) {
  int state = OUT ;
  int wc = 0 ;
  int i = 0 ;
  while ( i < str . length ( ) ) {
    if ( str . charAt ( i ) == ' ' || str . charAt ( i ) == '\n' || str . charAt ( i ) == '\t' ) state = OUT ;
    else if ( state == OUT ) {
      state = IN ;
      ++ wc ;
    }
    ++ i ;
  }
  return wc ;
}
|||

PARTITION_INTO_TWO_SUBARRAYS_OF_LENGTHS_K_AND_N_K_SUCH_THAT_THE_DIFFERENCE_OF_SUMS_IS_MAXIMUM

static int maxDifference ( int arr [ ] , int N , int k ) {
  int M , S = 0 , S1 = 0 , max_difference = 0 ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) S += arr [ i ] ;
  int temp ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < N ;
    j ++ ) {
      if ( arr [ i ] < arr [ j ] ) {
        temp = arr [ i ] ;
        arr [ i ] = arr [ j ] ;
        arr [ j ] = temp ;
      }
    }
  }
  M = Math . max ( k , N - k ) ;
  for ( int i = 0 ;
  i < M ;
  i ++ ) S1 += arr [ i ] ;
  max_difference = S1 - ( S - S1 ) ;
  return max_difference ;
}
|||

HOW_WILL_YOU_PRINT_NUMBERS_FROM_1_TO_200_WITHOUT_USING_LOOP

static void printNos ( int n ) {
  if ( n > 0 ) {
    printNos ( n - 1 ) ;
    System . out . print ( n + " " ) ;
  }
  return ;
}
|||

GIVEN_A_SORTED_AND_ROTATED_ARRAY_FIND_IF_THERE_IS_A_PAIR_WITH_A_GIVEN_SUM_1

static int pairsInSortedRotated ( int arr [ ] , int n , int x ) {
  int i ;
  for ( i = 0 ;
  i < n - 1 ;
  i ++ ) if ( arr [ i ] > arr [ i + 1 ] ) break ;
  int l = ( i + 1 ) % n ;
  int r = i ;
  int cnt = 0 ;
  while ( l != r ) {
    if ( arr [ l ] + arr [ r ] == x ) {
      cnt ++ ;
      if ( l == ( r - 1 + n ) % n ) {
        return cnt ;
      }
      l = ( l + 1 ) % n ;
      r = ( r - 1 + n ) % n ;
    }
    else if ( arr [ l ] + arr [ r ] < x ) l = ( l + 1 ) % n ;
    else r = ( n + r - 1 ) % n ;
  }
  return cnt ;
}
|||

FIND_THE_ELEMENT_THAT_APPEARS_ONCE

static int getSingle ( int arr [ ] , int n ) {
  int ones = 0 , twos = 0 ;
  int common_bit_mask ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    twos = twos | ( ones & arr [ i ] ) ;
    ones = ones ^ arr [ i ] ;
    common_bit_mask = ~ ( ones & twos ) ;
    ones &= common_bit_mask ;
    twos &= common_bit_mask ;
  }
  return ones ;
}
|||

CASSINIS_IDENTITY

static int cassini ( int n ) {
  return ( n & 1 ) != 0 ? - 1 : 1 ;
}
|||

DISTRIBUTING_ALL_BALLS_WITHOUT_REPETITION

static boolean distributingBalls ( long k , long n , String str ) {
  int [ ] a = new int [ MAX_CHAR ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    a [ str . charAt ( i ) - 'a' ] ++ ;
  }
  for ( int i = 0 ;
  i < MAX_CHAR ;
  i ++ ) if ( a [ i ] > k ) return false ;
  return true ;
}
|||

DISTRIBUTING_ITEMS_PERSON_CANNOT_TAKE_TWO_ITEMS_TYPE

static boolean checkCount ( int [ ] arr , int n , int k ) {
  int count ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    count = 0 ;
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( arr [ j ] == arr [ i ] ) count ++ ;
      if ( count > 2 * k ) return false ;
    }
  }
  return true ;
}
|||

MAXIMIZE_ARRJ_ARRI_ARRL_ARRK_SUCH_THAT_I_J_K_L

static int findMaxValue ( int [ ] arr , int n ) {
  if ( n < 4 ) {
    System . out . println ( "The array should have" + " atleast 4 elements" ) ;
  }
  int table1 [ ] = new int [ n + 1 ] ;
  int table2 [ ] = new int [ n ] ;
  int table3 [ ] = new int [ n - 1 ] ;
  int table4 [ ] = new int [ n - 2 ] ;
  Arrays . fill ( table1 , Integer . MIN_VALUE ) ;
  Arrays . fill ( table2 , Integer . MIN_VALUE ) ;
  Arrays . fill ( table3 , Integer . MIN_VALUE ) ;
  Arrays . fill ( table4 , Integer . MIN_VALUE ) ;
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
  i -- ) table3 [ i ] = Math . max ( table3 [ i + 1 ] , table2 [ i + 1 ] + arr [ i ] ) ;
  for ( int i = n - 4 ;
  i >= 0 ;
  i -- ) table4 [ i ] = Math . max ( table4 [ i + 1 ] , table3 [ i + 1 ] - arr [ i ] ) ;
  return table4 [ 0 ] ;
}
|||

COUNT_NEGATIVE_NUMBERS_IN_A_COLUMN_WISE_ROW_WISE_SORTED_MATRIX_1

static int countNegative ( int M [ ] [ ] , int n , int m ) {
  int count = 0 ;
  int i = 0 ;
  int j = m - 1 ;
  while ( j >= 0 && i < n ) {
    if ( M [ i ] [ j ] < 0 ) {
      count += j + 1 ;
      i += 1 ;
    }
    else j -= 1 ;
  }
  return count ;
}
|||

SORT_AN_ARRAY_OF_0S_1S_AND_2S

static void sort012 ( int a [ ] , int arr_size ) {
  int lo = 0 ;
  int hi = arr_size - 1 ;
  int mid = 0 , temp = 0 ;
  while ( mid <= hi ) {
    switch ( a [ mid ] ) {
      case 0 : {
        temp = a [ lo ] ;
        a [ lo ] = a [ mid ] ;
        a [ mid ] = temp ;
        lo ++ ;
        mid ++ ;
        break ;
      }
      case 1 : mid ++ ;
      break ;
      case 2 : {
        temp = a [ mid ] ;
        a [ mid ] = a [ hi ] ;
        a [ hi ] = temp ;
        hi -- ;
        break ;
      }
    }
  }
}
|||

NTH_EVEN_FIBONACCI_NUMBER

static long evenFib ( int n ) {
  if ( n < 1 ) return n ;
  if ( n == 1 ) return 2 ;
  return ( ( 4 * evenFib ( n - 1 ) ) + evenFib ( n - 2 ) ) ;
}
|||

NEXT_GREATER_ELEMENT

static void printNGE ( int arr [ ] , int n ) {
  int next , i , j ;
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    next = - 1 ;
    for ( j = i + 1 ;
    j < n ;
    j ++ ) {
      if ( arr [ i ] < arr [ j ] ) {
        next = arr [ j ] ;
        break ;
      }
    }
    System . out . println ( arr [ i ] + " -- " + next ) ;
  }
}
|||

CHECK_WHETHER_GIVEN_CIRCLE_RESIDE_BOUNDARY_MAINTAINED_OUTER_CIRCLE_INNER_CIRCLE

static void fitOrNotFit ( int R , int r , int x , int y , int rad ) {
  double val = Math . sqrt ( Math . pow ( x , 2 ) + Math . pow ( y , 2 ) ) ;
  if ( val + rad <= R && val - rad >= R - r ) System . out . println ( "Fits" ) ;
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
  int x1 = 1 , y1 = 1 ;
  int gcd = gcdExtended ( b % a , a , x1 , y1 ) ;
  x = y1 - ( b / a ) * x1 ;
  y = x1 ;
  return gcd ;
}
|||

FIND_SMALLEST_RANGE_CONTAINING_ELEMENTS_FROM_K_LISTS

static void findSmallestRange ( int arr [ ] [ ] , int n , int k ) {
  int i , minval , maxval , minrange , minel = 0 , maxel = 0 , flag , minind ;
  for ( i = 0 ;
  i <= k ;
  i ++ ) {
    ptr [ i ] = 0 ;
  }
  minrange = Integer . MAX_VALUE ;
  while ( true ) {
    minind = - 1 ;
    minval = Integer . MAX_VALUE ;
    maxval = Integer . MIN_VALUE ;
    flag = 0 ;
    for ( i = 0 ;
    i < k ;
    i ++ ) {
      if ( ptr [ i ] == n ) {
        flag = 1 ;
        break ;
      }
      if ( ptr [ i ] < n && arr [ i ] [ ptr [ i ] ] < minval ) {
        minind = i ;
        minval = arr [ i ] [ ptr [ i ] ] ;
      }
      if ( ptr [ i ] < n && arr [ i ] [ ptr [ i ] ] > maxval ) {
        maxval = arr [ i ] [ ptr [ i ] ] ;
      }
    }
    if ( flag == 1 ) {
      break ;
    }
    ptr [ minind ] ++ ;
    if ( ( maxval - minval ) < minrange ) {
      minel = minval ;
      maxel = maxval ;
      minrange = maxel - minel ;
    }
  }
  System . out . printf ( "The smallest range is [%d , %d]\n" , minel , maxel ) ;
}
|||

FIND_THE_MINIMUM_COST_TO_REACH_A_DESTINATION_WHERE_EVERY_STATION_IS_CONNECTED_IN_ONE_DIRECTION

static int minCost ( int cost [ ] [ ] ) {
  int dist [ ] = new int [ N ] ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) dist [ i ] = INF ;
  dist [ 0 ] = 0 ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) for ( int j = i + 1 ;
  j < N ;
  j ++ ) if ( dist [ j ] > dist [ i ] + cost [ i ] [ j ] ) dist [ j ] = dist [ i ] + cost [ i ] [ j ] ;
  return dist [ N - 1 ] ;
}
|||

MIDDLE_OF_THREE_USING_MINIMUM_COMPARISONS_1

public static int middleOfThree ( int a , int b , int c ) {
  if ( a > b ) {
    if ( b > c ) return b ;
    else if ( a > c ) return c ;
    else return a ;
  }
  else {
    if ( a > c ) return a ;
    else if ( b > c ) return c ;
    else return b ;
  }
}
|||

CHECK_LARGE_NUMBER_DIVISIBLE_11_NOT

static boolean check ( String str ) {
  int n = str . length ( ) ;
  int oddDigSum = 0 , evenDigSum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( i % 2 == 0 ) oddDigSum += ( str . charAt ( i ) - '0' ) ;
    else evenDigSum += ( str . charAt ( i ) - '0' ) ;
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

static int countStrings ( int n , int k ) {
  int dp [ ] [ ] [ ] = new int [ n + 1 ] [ k + 1 ] [ 2 ] ;
  dp [ 1 ] [ 0 ] [ 0 ] = 1 ;
  dp [ 1 ] [ 0 ] [ 1 ] = 1 ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j < i && j < k + 1 ;
    j ++ ) {
      dp [ i ] [ j ] [ 0 ] = dp [ i - 1 ] [ j ] [ 0 ] + dp [ i - 1 ] [ j ] [ 1 ] ;
      dp [ i ] [ j ] [ 1 ] = dp [ i - 1 ] [ j ] [ 0 ] ;
      if ( j - 1 >= 0 ) {
        dp [ i ] [ j ] [ 1 ] += dp [ i - 1 ] [ j - 1 ] [ 1 ] ;
      }
    }
  }
  return dp [ n ] [ k ] [ 0 ] + dp [ n ] [ k ] [ 1 ] ;
}
|||

FINDING_K_MODULUS_ARRAY_ELEMENT

static void printEqualModNumbers ( int arr [ ] , int n ) {
  Arrays . sort ( arr ) ;
  int d = arr [ n - 1 ] - arr [ 0 ] ;
  Vector < Integer > v = new Vector < > ( ) ;
  for ( int i = 1 ;
  i * i <= d ;
  i ++ ) {
    if ( d % i == 0 ) {
      v . add ( i ) ;
      if ( i != d / i ) v . add ( d / i ) ;
    }
  }
  for ( int i = 0 ;
  i < v . size ( ) ;
  i ++ ) {
    int temp = arr [ 0 ] % v . get ( i ) ;
    int j ;
    for ( j = 1 ;
    j < n ;
    j ++ ) if ( arr [ j ] % v . get ( i ) != temp ) break ;
    if ( j == n ) System . out . print ( v . get ( i ) + " " ) ;
  }
}
|||

CIRCULAR_MATRIX_CONSTRUCT_A_MATRIX_WITH_NUMBERS_1_TO_MN_IN_SPIRAL_WAY

static void spiralFill ( int m , int n , int a [ ] [ ] ) {
  int val = 1 ;
  int k = 0 , l = 0 ;
  while ( k < m && l < n ) {
    for ( int i = l ;
    i < n ;
    ++ i ) {
      a [ k ] [ i ] = val ++ ;
    }
    k ++ ;
    for ( int i = k ;
    i < m ;
    ++ i ) {
      a [ i ] [ n - 1 ] = val ++ ;
    }
    n -- ;
    if ( k < m ) {
      for ( int i = n - 1 ;
      i >= l ;
      -- i ) {
        a [ m - 1 ] [ i ] = val ++ ;
      }
      m -- ;
    }
    if ( l < n ) {
      for ( int i = m - 1 ;
      i >= k ;
      -- i ) {
        a [ i ] [ l ] = val ++ ;
      }
      l ++ ;
    }
  }
}
|||

FIND_THE_TWO_REPEATING_ELEMENTS_IN_A_GIVEN_ARRAY_2

void printRepeating ( int arr [ ] , int size ) {
  int xor = arr [ 0 ] ;
  int set_bit_no ;
  int i ;
  int n = size - 2 ;
  int x = 0 , y = 0 ;
  for ( i = 1 ;
  i < size ;
  i ++ ) xor ^= arr [ i ] ;
  for ( i = 1 ;
  i <= n ;
  i ++ ) xor ^= i ;
  set_bit_no = ( xor & ~ ( xor - 1 ) ) ;
  for ( i = 0 ;
  i < size ;
  i ++ ) {
    int a = arr [ i ] & set_bit_no ;
    if ( a != 0 ) x = x ^ arr [ i ] ;
    else y = y ^ arr [ i ] ;
  }
  for ( i = 1 ;
  i <= n ;
  i ++ ) {
    int a = i & set_bit_no ;
    if ( a != 0 ) x = x ^ i ;
    else y = y ^ i ;
  }
  System . out . println ( "The two reppeated elements are :" ) ;
  System . out . println ( x + " " + y ) ;
}
|||

COUNT_POSSIBLE_WAYS_TO_CONSTRUCT_BUILDINGS

static int countWays ( int N ) {
  if ( N == 1 ) return 4 ;
  int countB = 1 , countS = 1 , prev_countB , prev_countS ;
  for ( int i = 2 ;
  i <= N ;
  i ++ ) {
    prev_countB = countB ;
    prev_countS = countS ;
    countS = prev_countB + prev_countS ;
    countB = prev_countS ;
  }
  int result = countS + countB ;
  return ( result * result ) ;
}
|||

ONE_LINE_FUNCTION_FOR_FACTORIAL_OF_A_NUMBER

static int factorial ( int n ) {
  return ( n == 1 || n == 0 ) ? 1 : n * factorial ( n - 1 ) ;
}
|||

CHECK_GIVEN_MATRIX_SPARSE_NOT

static boolean isSparse ( int array [ ] [ ] , int m , int n ) {
  int counter = 0 ;
  for ( int i = 0 ;
  i < m ;
  ++ i ) for ( int j = 0 ;
  j < n ;
  ++ j ) if ( array [ i ] [ j ] == 0 ) ++ counter ;
  return ( counter > ( ( m * n ) / 2 ) ) ;
}
|||

DYNAMIC_PROGRAMMING_SET_10_0_1_KNAPSACK_PROBLEM

static int knapSack ( int W , int wt [ ] , int val [ ] , int n ) {
  if ( n == 0 || W == 0 ) return 0 ;
  if ( wt [ n - 1 ] > W ) return knapSack ( W , wt , val , n - 1 ) ;
  else return max ( val [ n - 1 ] + knapSack ( W - wt [ n - 1 ] , wt , val , n - 1 ) , knapSack ( W , wt , val , n - 1 ) ) ;
}
|||

FIND_SUBARRAY_LEAST_AVERAGE

static void findMinAvgSubarray ( int n , int k ) {
  if ( n < k ) return ;
  int res_index = 0 ;
  int curr_sum = 0 ;
  for ( int i = 0 ;
  i < k ;
  i ++ ) curr_sum += arr [ i ] ;
  int min_sum = curr_sum ;
  for ( int i = k ;
  i < n ;
  i ++ ) {
    curr_sum += arr [ i ] - arr [ i - k ] ;
    if ( curr_sum < min_sum ) {
      min_sum = curr_sum ;
      res_index = ( i - k + 1 ) ;
    }
  }
  System . out . println ( "Subarray between [" + res_index + ", " + ( res_index + k - 1 ) + "] has minimum average" ) ;
}
|||

QUERIES_FOR_CHARACTERS_IN_A_REPEATED_STRING

static void query ( String s , int i , int j ) {
  int n = s . length ( ) ;
  i %= n ;
  j %= n ;
  if ( s . charAt ( i ) == s . charAt ( j ) ) System . out . println ( "Yes" ) ;
  else System . out . println ( "No" ) ;
}
|||

A_PRODUCT_ARRAY_PUZZLE_1

void productArray ( int arr [ ] , int n ) {
  if ( n == 1 ) {
    System . out . print ( "0" ) ;
    return ;
  }
  int i , temp = 1 ;
  int prod [ ] = new int [ n ] ;
  for ( int j = 0 ;
  j < n ;
  j ++ ) prod [ j ] = 1 ;
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    prod [ i ] = temp ;
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
  i ++ ) System . out . print ( prod [ i ] + " " ) ;
  return ;
}
|||

FIND_PAIRS_GIVEN_SUM_ELEMENTS_PAIR_DIFFERENT_ROWS

static void pairSum ( int mat [ ] [ ] , int n , int sum ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) Arrays . sort ( mat [ i ] ) ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      int left = 0 , right = n - 1 ;
      while ( left < n && right >= 0 ) {
        if ( ( mat [ i ] [ left ] + mat [ j ] [ right ] ) == sum ) {
          System . out . print ( "(" + mat [ i ] [ left ] + ", " + mat [ j ] [ right ] + "), " ) ;
          left ++ ;
          right -- ;
        }
        else {
          if ( ( mat [ i ] [ left ] + mat [ j ] [ right ] ) < sum ) left ++ ;
          else right -- ;
        }
      }
    }
  }
}
|||

CHECK_STRING_CAN_OBTAINED_ROTATING_ANOTHER_STRING_2_PLACES

static boolean isRotated ( String str1 , String str2 ) {
  if ( str1 . length ( ) != str2 . length ( ) ) return false ;
  String clock_rot = "" ;
  String anticlock_rot = "" ;
  int len = str2 . length ( ) ;
  anticlock_rot = anticlock_rot + str2 . substring ( len - 2 , len ) + str2 . substring ( 0 , len - 2 ) ;
  clock_rot = clock_rot + str2 . substring ( 2 ) + str2 . substring ( 0 , 2 ) ;
  return ( str1 . equals ( clock_rot ) || str1 . equals ( anticlock_rot ) ) ;
}
|||

N_TH_NUMBER_WHOSE_SUM_OF_DIGITS_IS_TEN

public static int findNth ( int n ) {
  int count = 0 ;
  for ( int curr = 1 ;
  ;
  curr ++ ) {
    int sum = 0 ;
    for ( int x = curr ;
    x > 0 ;
    x = x / 10 ) sum = sum + x % 10 ;
    if ( sum == 10 ) count ++ ;
    if ( count == n ) return curr ;
  }
}
|||

PROGRAM_FIND_SLOPE_LINE

static float slope ( float x1 , float y1 , float x2 , float y2 ) {
  return ( y2 - y1 ) / ( x2 - x1 ) ;
}
|||

GCD_ELEMENTS_GIVEN_RANGE

static int rangeGCD ( int n , int m ) {
  return ( n == m ) ? n : 1 ;
}
|||

LONGEST_ALTERNATING_SUB_ARRAY_STARTING_EVERY_INDEX_BINARY_ARRAY_1

static void alternateSubarray ( boolean arr [ ] , int n ) {
  int count = 1 ;
  boolean prev = arr [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  ++ i ) {
    if ( ( arr [ i ] ^ prev ) == false ) {
      while ( count > 0 ) {
        System . out . print ( count -- + " " ) ;
      }
    }
    ++ count ;
    prev = arr [ i ] ;
  }
  while ( count != 0 ) {
    System . out . print ( count -- + " " ) ;
  }
}
|||

FIND_UNIT_DIGIT_X_RAISED_POWER_Y

static int unitDigitXRaisedY ( int x , int y ) {
  int res = 1 ;
  for ( int i = 0 ;
  i < y ;
  i ++ ) res = ( res * x ) % 10 ;
  return res ;
}
|||

MULTIPLY_LARGE_INTEGERS_UNDER_LARGE_MODULO

static long moduloMultiplication ( long a , long b , long mod ) {
  long res = 0 ;
  a %= mod ;
  while ( b > 0 ) {
    if ( ( b & 1 ) > 0 ) {
      res = ( res + a ) % mod ;
    }
    a = ( 2 * a ) % mod ;
    b >>= 1 ;
  }
  return res ;
}
|||

FIND_SMALLEST_NUMBER_WITH_GIVEN_NUMBER_OF_DIGITS_AND_DIGIT_SUM

static void findSmallest ( int m , int s ) {
  if ( s == 0 ) {
    System . out . print ( m == 1 ? "Smallest number is 0" : "Not possible" ) ;
    return ;
  }
  if ( s > 9 * m ) {
    System . out . println ( "Not possible" ) ;
    return ;
  }
  int [ ] res = new int [ m ] ;
  s -= 1 ;
  for ( int i = m - 1 ;
  i > 0 ;
  i -- ) {
    if ( s > 9 ) {
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
  i ++ ) System . out . print ( res [ i ] ) ;
}
|||

C_PROGRAM_FIND_LARGEST_ELEMENT_ARRAY

static int largest ( ) {
  int i ;
  int max = arr [ 0 ] ;
  for ( i = 1 ;
  i < arr . length ;
  i ++ ) if ( arr [ i ] > max ) max = arr [ i ] ;
  return max ;
}
|||

COUNT_NUMBERS_CAN_CONSTRUCTED_USING_TWO_NUMBERS

static int countNums ( int n , int x , int y ) {
  boolean [ ] arr = new boolean [ n + 1 ] ;
  if ( x <= n ) arr [ x ] = true ;
  if ( y <= n ) arr [ y ] = true ;
  int result = 0 ;
  for ( int i = Math . min ( x , y ) ;
  i <= n ;
  i ++ ) {
    if ( arr [ i ] ) {
      if ( i + x <= n ) arr [ i + x ] = true ;
      if ( i + y <= n ) arr [ i + y ] = true ;
      result ++ ;
    }
  }
  return result ;
}
|||

BUBBLE_SORT_1

static void bubbleSort ( int arr [ ] , int n ) {
  int i , j , temp ;
  boolean swapped ;
  for ( i = 0 ;
  i < n - 1 ;
  i ++ ) {
    swapped = false ;
    for ( j = 0 ;
    j < n - i - 1 ;
    j ++ ) {
      if ( arr [ j ] > arr [ j + 1 ] ) {
        temp = arr [ j ] ;
        arr [ j ] = arr [ j + 1 ] ;
        arr [ j + 1 ] = temp ;
        swapped = true ;
      }
    }
    if ( swapped == false ) break ;
  }
}
|||

MAXIMUM_SUM_2_X_N_GRID_NO_TWO_ELEMENTS_ADJACENT

public static int maxSum ( int grid [ ] [ ] , int n ) {
  int incl = Math . max ( grid [ 0 ] [ 0 ] , grid [ 1 ] [ 0 ] ) ;
  int excl = 0 , excl_new ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    excl_new = Math . max ( excl , incl ) ;
    incl = excl + Math . max ( grid [ 0 ] [ i ] , grid [ 1 ] [ i ] ) ;
    excl = excl_new ;
  }
  return Math . max ( excl , incl ) ;
}
|||

GCD_FACTORIALS_TWO_NUMBERS

static int gcdOfFactorial ( int m , int n ) {
  int min = m < n ? m : n ;
  return factorial ( min ) ;
}
|||

AREA_OF_A_SECTOR

static void SectorArea ( double radius , double angle ) {
  if ( angle >= 360 ) System . out . println ( "Angle not possible" ) ;
  else {
    double sector = ( ( 22 * radius * radius ) / 7 ) * ( angle / 360 ) ;
    System . out . println ( sector ) ;
  }
}
|||

COUNT_EVEN_LENGTH_BINARY_SEQUENCES_WITH_SAME_SUM_OF_FIRST_AND_SECOND_HALF_BITS_1

static int countSeq ( int n ) {
  int nCr = 1 , res = 1 ;
  for ( int r = 1 ;
  r <= n ;
  r ++ ) {
    nCr = ( nCr * ( n + 1 - r ) ) / r ;
    res += nCr * nCr ;
  }
  return res ;
}
|||

LONGEST_EVEN_LENGTH_SUBSTRING_SUM_FIRST_SECOND_HALF_1

static int findLength ( String str ) {
  int n = str . length ( ) ;
  int maxlen = 0 ;
  int sum [ ] [ ] = new int [ n ] [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) sum [ i ] [ i ] = str . charAt ( i ) - '0' ;
  for ( int len = 2 ;
  len <= n ;
  len ++ ) {
    for ( int i = 0 ;
    i < n - len + 1 ;
    i ++ ) {
      int j = i + len - 1 ;
      int k = len / 2 ;
      sum [ i ] [ j ] = sum [ i ] [ j - k ] + sum [ j - k + 1 ] [ j ] ;
      if ( len % 2 == 0 && sum [ i ] [ j - k ] == sum [ ( j - k + 1 ) ] [ j ] && len > maxlen ) maxlen = len ;
    }
  }
  return maxlen ;
}
|||

SWAP_ALL_ODD_AND_EVEN_BITS

static int swapBits ( int x ) {
  int even_bits = x & 0xAAAAAAAA ;
  int odd_bits = x & 0x55555555 ;
  even_bits >>= 1 ;
  odd_bits <<= 1 ;
  return ( even_bits | odd_bits ) ;
}
|||

SORT_ARRAY_WAVE_FORM_2

void sortInWave ( int arr [ ] , int n ) {
  Arrays . sort ( arr ) ;
  for ( int i = 0 ;
  i < n - 1 ;
  i += 2 ) swap ( arr , i , i + 1 ) ;
}
|||

FIND_HARMONIC_MEAN_USING_ARITHMETIC_MEAN_GEOMETRIC_MEAN

static double compute ( int a , int b ) {
  double AM , GM , HM ;
  AM = ( a + b ) / 2 ;
  GM = Math . sqrt ( a * b ) ;
  HM = ( GM * GM ) / AM ;
  return HM ;
}
|||

COUNT_BALANCED_BINARY_TREES_HEIGHT_H

public static long countBT ( int h ) {
  long [ ] dp = new long [ h + 1 ] ;
  dp [ 0 ] = 1 ;
  dp [ 1 ] = 1 ;
  for ( int i = 2 ;
  i <= h ;
  ++ i ) dp [ i ] = ( dp [ i - 1 ] * ( ( 2 * dp [ i - 2 ] ) % MOD + dp [ i - 1 ] ) % MOD ) % MOD ;
  return dp [ h ] ;
}
|||

MINIMUM_INSERTIONS_TO_FORM_A_PALINDROME_WITH_PERMUTATIONS_ALLOWED

static int minInsertion ( String str ) {
  int n = str . length ( ) ;
  int res = 0 ;
  int [ ] count = new int [ 26 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) count [ str . charAt ( i ) - 'a' ] ++ ;
  for ( int i = 0 ;
  i < 26 ;
  i ++ ) {
    if ( count [ i ] % 2 == 1 ) res ++ ;
  }
  return ( res == 0 ) ? 0 : res - 1 ;
}
|||

SHUFFLE_A_GIVEN_ARRAY

static void randomize ( int arr [ ] , int n ) {
  Random r = new Random ( ) ;
  for ( int i = n - 1 ;
  i > 0 ;
  i -- ) {
    int j = r . nextInt ( i + 1 ) ;
    int temp = arr [ i ] ;
    arr [ i ] = arr [ j ] ;
    arr [ j ] = temp ;
  }
  System . out . println ( Arrays . toString ( arr ) ) ;
}
|||

UGLY_NUMBERS

int getNthUglyNo ( int n ) {
  int ugly [ ] = new int [ n ] ;
  int i2 = 0 , i3 = 0 , i5 = 0 ;
  int next_multiple_of_2 = 2 ;
  int next_multiple_of_3 = 3 ;
  int next_multiple_of_5 = 5 ;
  int next_ugly_no = 1 ;
  ugly [ 0 ] = 1 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    next_ugly_no = Math . min ( next_multiple_of_2 , Math . min ( next_multiple_of_3 , next_multiple_of_5 ) ) ;
    ugly [ i ] = next_ugly_no ;
    if ( next_ugly_no == next_multiple_of_2 ) {
      i2 = i2 + 1 ;
      next_multiple_of_2 = ugly [ i2 ] * 2 ;
    }
    if ( next_ugly_no == next_multiple_of_3 ) {
      i3 = i3 + 1 ;
      next_multiple_of_3 = ugly [ i3 ] * 3 ;
    }
    if ( next_ugly_no == next_multiple_of_5 ) {
      i5 = i5 + 1 ;
      next_multiple_of_5 = ugly [ i5 ] * 5 ;
    }
  }
  return next_ugly_no ;
}
|||

MINIMUM_COST_CUT_BOARD_SQUARES

static int minimumCostOfBreaking ( Integer X [ ] , Integer Y [ ] , int m , int n ) {
  int res = 0 ;
  Arrays . sort ( X , Collections . reverseOrder ( ) ) ;
  Arrays . sort ( Y , Collections . reverseOrder ( ) ) ;
  int hzntl = 1 , vert = 1 ;
  int i = 0 , j = 0 ;
  while ( i < m && j < n ) {
    if ( X [ i ] > Y [ j ] ) {
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
  int total = 0 ;
  while ( i < m ) total += X [ i ++ ] ;
  res += total * vert ;
  total = 0 ;
  while ( j < n ) total += Y [ j ++ ] ;
  res += total * hzntl ;
  return res ;
}
|||

DYNAMIC_PROGRAMMING_SET_10_0_1_KNAPSACK_PROBLEM_1

static int knapSack ( int W , int wt [ ] , int val [ ] , int n ) {
  int i , w ;
  int K [ ] [ ] = new int [ n + 1 ] [ W + 1 ] ;
  for ( i = 0 ;
  i <= n ;
  i ++ ) {
    for ( w = 0 ;
    w <= W ;
    w ++ ) {
      if ( i == 0 || w == 0 ) K [ i ] [ w ] = 0 ;
      else if ( wt [ i - 1 ] <= w ) K [ i ] [ w ] = max ( val [ i - 1 ] + K [ i - 1 ] [ w - wt [ i - 1 ] ] , K [ i - 1 ] [ w ] ) ;
      else K [ i ] [ w ] = K [ i - 1 ] [ w ] ;
    }
  }
  return K [ n ] [ W ] ;
}
|||

STACK_PERMUTATIONS_CHECK_IF_AN_ARRAY_IS_STACK_PERMUTATION_OF_OTHER

static boolean checkStackPermutation ( int ip [ ] , int op [ ] , int n ) {
  Queue < Integer > input = new LinkedList < > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    input . add ( ip [ i ] ) ;
  }
  Queue < Integer > output = new LinkedList < > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    output . add ( op [ i ] ) ;
  }
  Stack < Integer > tempStack = new Stack < > ( ) ;
  while ( ! input . isEmpty ( ) ) {
    int ele = input . poll ( ) ;
    if ( ele == output . peek ( ) ) {
      output . poll ( ) ;
      while ( ! tempStack . isEmpty ( ) ) {
        if ( tempStack . peek ( ) == output . peek ( ) ) {
          tempStack . pop ( ) ;
          output . poll ( ) ;
        }
        else break ;
      }
    }
    else {
      tempStack . push ( ele ) ;
    }
  }
  return ( input . isEmpty ( ) && tempStack . isEmpty ( ) ) ;
}
|||

PROBABILITY_THREE_RANDOMLY_CHOSEN_NUMBERS_AP

static double procal ( int n ) {
  return ( 3.0 * n ) / ( 4.0 * ( n * n ) - 1 ) ;
}
|||

REMOVE_BRACKETS_ALGEBRAIC_STRING_CONTAINING_OPERATORS

static String simplify ( String str ) {
  int len = str . length ( ) ;
  char res [ ] = new char [ len ] ;
  int index = 0 , i = 0 ;
  Stack < Integer > s = new Stack < Integer > ( ) ;
  s . push ( 0 ) ;
  while ( i < len ) {
    if ( str . charAt ( i ) == '+' ) {
      if ( s . peek ( ) == 1 ) res [ index ++ ] = '-' ;
      if ( s . peek ( ) == 0 ) res [ index ++ ] = '+' ;
    }
    else if ( str . charAt ( i ) == '-' ) {
      if ( s . peek ( ) == 1 ) res [ index ++ ] = '+' ;
      else if ( s . peek ( ) == 0 ) res [ index ++ ] = '-' ;
    }
    else if ( str . charAt ( i ) == '(' && i > 0 ) {
      if ( str . charAt ( i - 1 ) == '-' ) {
        int x = ( s . peek ( ) == 1 ) ? 0 : 1 ;
        s . push ( x ) ;
      }
      else if ( str . charAt ( i - 1 ) == '+' ) s . push ( s . peek ( ) ) ;
    }
    else if ( str . charAt ( i ) == ')' ) s . pop ( ) ;
    else res [ index ++ ] = str . charAt ( i ) ;
    i ++ ;
  }
  return new String ( res ) ;
}
|||

FIND_NUMBER_PERFECT_SQUARES_TWO_GIVEN_NUMBERS

static int countSquares ( int a , int b ) {
  int cnt = 0 ;
  for ( int i = a ;
  i <= b ;
  i ++ ) for ( int j = 1 ;
  j * j <= i ;
  j ++ ) if ( j * j == i ) cnt ++ ;
  return cnt ;
}
|||

K_NUMBERS_DIFFERENCE_MAXIMUM_MINIMUM_K_NUMBER_MINIMIZED

static int minDiff ( int arr [ ] , int n , int k ) {
  int result = Integer . MAX_VALUE ;
  Arrays . sort ( arr ) ;
  for ( int i = 0 ;
  i <= n - k ;
  i ++ ) result = Math . min ( result , arr [ i + k - 1 ] - arr [ i ] ) ;
  return result ;
}
|||

CHECK_LARGE_NUMBER_DIVISIBLE_13_NOT

static boolean checkDivisibility ( String num ) {
  int length = num . length ( ) ;
  if ( length == 1 && num . charAt ( 0 ) == '0' ) return true ;
  if ( length % 3 == 1 ) {
    num += "00" ;
    length += 2 ;
  }
  else if ( length % 3 == 2 ) {
    num += "0" ;
    length += 1 ;
  }
  int sum = 0 , p = 1 ;
  for ( int i = length - 1 ;
  i >= 0 ;
  i -- ) {
    int group = 0 ;
    group += num . charAt ( i -- ) - '0' ;
    group += ( num . charAt ( i -- ) - '0' ) * 10 ;
    group += ( num . charAt ( i ) - '0' ) * 100 ;
    sum = sum + group * p ;
    p *= ( - 1 ) ;
  }
  sum = Math . abs ( sum ) ;
  return ( sum % 13 == 0 ) ;
}
|||

GIVEN_N_X_N_SQUARE_MATRIX_FIND_SUM_SUB_SQUARES_SIZE_K_X_K

static void printSumSimple ( int mat [ ] [ ] , int k ) {
  if ( k > n ) return ;
  for ( int i = 0 ;
  i < n - k + 1 ;
  i ++ ) {
    for ( int j = 0 ;
    j < n - k + 1 ;
    j ++ ) {
      int sum = 0 ;
      for ( int p = i ;
      p < k + i ;
      p ++ ) for ( int q = j ;
      q < k + j ;
      q ++ ) sum += mat [ p ] [ q ] ;
      System . out . print ( sum + " " ) ;
    }
    System . out . println ( ) ;
  }
}
|||

FIND_THE_POINT_WHERE_MAXIMUM_INTERVALS_OVERLAP_1

public static void maxOverlap ( int [ ] start , int [ ] end , int n ) {
  int maxa = Arrays . stream ( start ) . max ( ) . getAsInt ( ) ;
  int maxb = Arrays . stream ( end ) . max ( ) . getAsInt ( ) ;
  int maxc = Math . max ( maxa , maxb ) ;
  int [ ] x = new int [ maxc + 2 ] ;
  Arrays . fill ( x , 0 ) ;
  int cur = 0 , idx = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    ++ x [ start [ i ] ] ;
    -- x [ end [ i ] + 1 ] ;
  }
  int maxy = Integer . MIN_VALUE ;
  for ( int i = 0 ;
  i <= maxc ;
  i ++ ) {
    cur += x [ i ] ;
    if ( maxy < cur ) {
      maxy = cur ;
      idx = i ;
    }
  }
  System . out . println ( "Maximum value is:" + maxy + " at position: " + idx + "" ) ;
}
|||

MAXIMUM_SUBSEQUENCE_SUM_SUCH_THAT_NO_THREE_ARE_CONSECUTIVE_1

static int maxSumWO3Consec ( int n ) {
  if ( sum [ n ] != - 1 ) return sum [ n ] ;
  if ( n == 0 ) return sum [ n ] = 0 ;
  if ( n == 1 ) return sum [ n ] = arr [ 0 ] ;
  if ( n == 2 ) return sum [ n ] = arr [ 1 ] + arr [ 0 ] ;
  return sum [ n ] = Math . max ( Math . max ( maxSumWO3Consec ( n - 1 ) , maxSumWO3Consec ( n - 2 ) + arr [ n - 1 ] ) , arr [ n - 2 ] + arr [ n - 1 ] + maxSumWO3Consec ( n - 3 ) ) ;
}
|||

C_PROGRAM_ADDITION_TWO_MATRICES

static void add ( int A [ ] [ ] , int B [ ] [ ] , int C [ ] [ ] ) {
  int i , j ;
  for ( i = 0 ;
  i < N ;
  i ++ ) for ( j = 0 ;
  j < N ;
  j ++ ) C [ i ] [ j ] = A [ i ] [ j ] + B [ i ] [ j ] ;
}
|||

FIND_MAXIMUM_AVERAGE_SUBARRAY_OF_K_LENGTH_1

static int findMaxAverage ( int arr [ ] , int n , int k ) {
  if ( k > n ) return - 1 ;
  int sum = arr [ 0 ] ;
  for ( int i = 1 ;
  i < k ;
  i ++ ) sum += arr [ i ] ;
  int max_sum = sum , max_end = k - 1 ;
  for ( int i = k ;
  i < n ;
  i ++ ) {
    sum = sum + arr [ i ] - arr [ i - k ] ;
    if ( sum > max_sum ) {
      max_sum = sum ;
      max_end = i ;
    }
  }
  return max_end - k + 1 ;
}
|||

FIND_CENTER_CIRCLE_USING_ENDPOINTS_DIAMETER

static void center ( int x1 , int x2 , int y1 , int y2 ) {
  System . out . print ( ( float ) ( x1 + x2 ) / 2 + ", " + ( float ) ( y1 + y2 ) / 2 ) ;
}
|||

TOTAL_NUMBER_OF_NON_DECREASING_NUMBERS_WITH_N_DIGITS

static int countNonDecreasing ( int n ) {
  int dp [ ] [ ] = new int [ 10 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i < 10 ;
  i ++ ) dp [ i ] [ 1 ] = 1 ;
  for ( int digit = 0 ;
  digit <= 9 ;
  digit ++ ) {
    for ( int len = 2 ;
    len <= n ;
    len ++ ) {
      for ( int x = 0 ;
      x <= digit ;
      x ++ ) dp [ digit ] [ len ] += dp [ x ] [ len - 1 ] ;
    }
  }
  int count = 0 ;
  for ( int i = 0 ;
  i < 10 ;
  i ++ ) count += dp [ i ] [ n ] ;
  return count ;
}
|||

PRINT_REVERSE_STRING_REMOVING_VOWELS

static void replaceOriginal ( String s , int n ) {
  char r [ ] = new char [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    r [ i ] = s . charAt ( n - 1 - i ) ;
    if ( s . charAt ( i ) != 'a' && s . charAt ( i ) != 'e' && s . charAt ( i ) != 'i' && s . charAt ( i ) != 'o' && s . charAt ( i ) != 'u' ) {
      System . out . print ( r [ i ] ) ;
    }
  }
  System . out . println ( "" ) ;
}
|||

FIND_ELEMENTS_PRESENT_FIRST_ARRAY_NOT_SECOND_1

static void findMissing ( int a [ ] , int b [ ] , int n , int m ) {
  HashSet < Integer > s = new HashSet < > ( ) ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) s . add ( b [ i ] ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( ! s . contains ( a [ i ] ) ) System . out . print ( a [ i ] + " " ) ;
}
|||

COUNT_STRINGS_CAN_FORMED_USING_B_C_GIVEN_CONSTRAINTS

static int countStr ( int n , int bCount , int cCount ) {
  if ( bCount < 0 || cCount < 0 ) return 0 ;
  if ( n == 0 ) return 1 ;
  if ( bCount == 0 && cCount == 0 ) return 1 ;
  int res = countStr ( n - 1 , bCount , cCount ) ;
  res += countStr ( n - 1 , bCount - 1 , cCount ) ;
  res += countStr ( n - 1 , bCount , cCount - 1 ) ;
  return res ;
}
|||

GOLD_MINE_PROBLEM

static int getMaxGold ( int gold [ ] [ ] , int m , int n ) {
  int goldTable [ ] [ ] = new int [ m ] [ n ] ;
  for ( int [ ] rows : goldTable ) Arrays . fill ( rows , 0 ) ;
  for ( int col = n - 1 ;
  col >= 0 ;
  col -- ) {
    for ( int row = 0 ;
    row < m ;
    row ++ ) {
      int right = ( col == n - 1 ) ? 0 : goldTable [ row ] [ col + 1 ] ;
      int right_up = ( row == 0 || col == n - 1 ) ? 0 : goldTable [ row - 1 ] [ col + 1 ] ;
      int right_down = ( row == m - 1 || col == n - 1 ) ? 0 : goldTable [ row + 1 ] [ col + 1 ] ;
      goldTable [ row ] [ col ] = gold [ row ] [ col ] + Math . max ( right , Math . max ( right_up , right_down ) ) ;
      ;
    }
  }
  int res = goldTable [ 0 ] [ 0 ] ;
  for ( int i = 1 ;
  i < m ;
  i ++ ) res = Math . max ( res , goldTable [ i ] [ 0 ] ) ;
  return res ;
}
|||

COUNT_WAYS_BUILD_STREET_GIVEN_CONSTRAINTS

static long countWays ( int n ) {
  long dp [ ] [ ] = new long [ 2 ] [ n + 1 ] ;
  dp [ 0 ] [ 1 ] = 1 ;
  dp [ 1 ] [ 1 ] = 2 ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    dp [ 0 ] [ i ] = dp [ 0 ] [ i - 1 ] + dp [ 1 ] [ i - 1 ] ;
    dp [ 1 ] [ i ] = dp [ 0 ] [ i - 1 ] * 2 + dp [ 1 ] [ i - 1 ] ;
  }
  return dp [ 0 ] [ n ] + dp [ 1 ] [ n ] ;
}
|||

RETURN_A_PAIR_WITH_MAXIMUM_PRODUCT_IN_ARRAY_OF_INTEGERS_1

static void maxProduct ( int arr [ ] , int n ) {
  if ( n < 2 ) {
    System . out . println ( "No pairs exists" ) ;
    return ;
  }
  if ( n == 2 ) {
    System . out . println ( arr [ 0 ] + " " + arr [ 1 ] ) ;
    return ;
  }
  int posa = Integer . MIN_VALUE , posb = Integer . MIN_VALUE ;
  int nega = Integer . MIN_VALUE , negb = Integer . MIN_VALUE ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] > posa ) {
      posb = posa ;
      posa = arr [ i ] ;
    }
    else if ( arr [ i ] > posb ) posb = arr [ i ] ;
    if ( arr [ i ] < 0 && Math . abs ( arr [ i ] ) > Math . abs ( nega ) ) {
      negb = nega ;
      nega = arr [ i ] ;
    }
    else if ( arr [ i ] < 0 && Math . abs ( arr [ i ] ) > Math . abs ( negb ) ) negb = arr [ i ] ;
  }
  if ( nega * negb > posa * posb ) System . out . println ( "Max product pair is {
" + nega + ", " + negb + "}" ) ;
    else System . out . println ( "Max product pair is {
" + posa + ", " + posb + "}" ) ;
    }
    |||

POSITION_OF_RIGHTMOST_SET_BIT

public static int getFirstSetBitPos ( int n ) {
  return ( int ) ( ( Math . log10 ( n & - n ) ) / Math . log10 ( 2 ) ) + 1 ;
}
|||

LONGEST_SUBSEQUENCE_WHERE_EVERY_CHARACTER_APPEARS_AT_LEAST_K_TIMES

static void longestSubseqWithK ( String str , int k ) {
  int n = str . length ( ) ;
  int freq [ ] = new int [ MAX_CHARS ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    freq [ str . charAt ( i ) - 'a' ] ++ ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( freq [ str . charAt ( i ) - 'a' ] >= k ) {
      System . out . print ( str . charAt ( i ) ) ;
    }
  }
}
|||

POSSIBLE_TO_MAKE_A_DIVISIBLE_BY_3_NUMBER_USING_ALL_DIGITS_IN_AN_ARRAY

public static boolean isPossibleToMakeDivisible ( int arr [ ] , int n ) {
  int remainder = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) remainder = ( remainder + arr [ i ] ) % 3 ;
  return ( remainder == 0 ) ;
}
|||

AREA_SQUARE_CIRCUMSCRIBED_CIRCLE

static int find_Area ( int r ) {
  return ( 2 * r * r ) ;
}
|||

FIND_MAXIMUM_DOT_PRODUCT_TWO_ARRAYS_INSERTION_0S

static int MaxDotProduct ( int A [ ] , int B [ ] , int m , int n ) {
  int dp [ ] [ ] = new int [ n + 1 ] [ m + 1 ] ;
  for ( int [ ] row : dp ) Arrays . fill ( row , 0 ) ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) for ( int j = i ;
  j <= m ;
  j ++ ) dp [ i ] [ j ] = Math . max ( ( dp [ i - 1 ] [ j - 1 ] + ( A [ j - 1 ] * B [ i - 1 ] ) ) , dp [ i ] [ j - 1 ] ) ;
  return dp [ n ] [ m ] ;
}
|||

FIND_DISTINCT_SUBSET_SUBSEQUENCE_SUMS_ARRAY

static void printDistSum ( int arr [ ] , int n ) {
  int sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) sum += arr [ i ] ;
  boolean [ ] [ ] dp = new boolean [ n + 1 ] [ sum + 1 ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) dp [ i ] [ 0 ] = true ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    dp [ i ] [ arr [ i - 1 ] ] = true ;
    for ( int j = 1 ;
    j <= sum ;
    j ++ ) {
      if ( dp [ i - 1 ] [ j ] == true ) {
        dp [ i ] [ j ] = true ;
        dp [ i ] [ j + arr [ i - 1 ] ] = true ;
      }
    }
  }
  for ( int j = 0 ;
  j <= sum ;
  j ++ ) if ( dp [ n ] [ j ] == true ) System . out . print ( j + " " ) ;
}
|||

SPLIT_NUMERIC_ALPHABETIC_AND_SPECIAL_SYMBOLS_FROM_A_STRING

static void splitString ( String str ) {
  StringBuffer alpha = new StringBuffer ( ) , num = new StringBuffer ( ) , special = new StringBuffer ( ) ;
  for ( int i = 0 ;
  i < str . length ( ) ;
  i ++ ) {
    if ( Character . isDigit ( str . charAt ( i ) ) ) num . append ( str . charAt ( i ) ) ;
    else if ( Character . isAlphabetic ( str . charAt ( i ) ) ) alpha . append ( str . charAt ( i ) ) ;
    else special . append ( str . charAt ( i ) ) ;
  }
  System . out . println ( alpha ) ;
  System . out . println ( num ) ;
  System . out . println ( special ) ;
}
|||

MAXIMUM_SUM_ALTERNATING_SUBSEQUENCE_SUM

static int maxAlternateSum ( int arr [ ] , int n ) {
  if ( n == 1 ) return arr [ 0 ] ;
  int dec [ ] = new int [ n ] ;
  int inc [ ] = new int [ n ] ;
  dec [ 0 ] = inc [ 0 ] = arr [ 0 ] ;
  int flag = 0 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < i ;
    j ++ ) {
      if ( arr [ j ] > arr [ i ] ) {
        dec [ i ] = Math . max ( dec [ i ] , inc [ j ] + arr [ i ] ) ;
        flag = 1 ;
      }
      else if ( arr [ j ] < arr [ i ] && flag == 1 ) inc [ i ] = Math . max ( inc [ i ] , dec [ j ] + arr [ i ] ) ;
    }
  }
  int result = Integer . MIN_VALUE ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( result < inc [ i ] ) result = inc [ i ] ;
    if ( result < dec [ i ] ) result = dec [ i ] ;
  }
  return result ;
}
|||

FIND_PAIR_MAXIMUM_GCD_ARRAY

public static int findMaxGCD ( int arr [ ] , int n ) {
  int high = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) high = Math . max ( high , arr [ i ] ) ;
  int divisors [ ] = new int [ high + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 1 ;
    j <= Math . sqrt ( arr [ i ] ) ;
    j ++ ) {
      if ( arr [ i ] % j == 0 ) {
        divisors [ j ] ++ ;
        if ( j != arr [ i ] / j ) divisors [ arr [ i ] / j ] ++ ;
      }
    }
  }
  for ( int i = high ;
  i >= 1 ;
  i -- ) if ( divisors [ i ] > 1 ) return i ;
  return 1 ;
}
|||

FIND_MINIMUM_NUMBER_OF_COINS_THAT_MAKE_A_CHANGE_1

static int minCoins ( int coins [ ] , int m , int V ) {
  int table [ ] = new int [ V + 1 ] ;
  table [ 0 ] = 0 ;
  for ( int i = 1 ;
  i <= V ;
  i ++ ) table [ i ] = Integer . MAX_VALUE ;
  for ( int i = 1 ;
  i <= V ;
  i ++ ) {
    for ( int j = 0 ;
    j < m ;
    j ++ ) if ( coins [ j ] <= i ) {
      int sub_res = table [ i - coins [ j ] ] ;
      if ( sub_res != Integer . MAX_VALUE && sub_res + 1 < table [ i ] ) table [ i ] = sub_res + 1 ;
    }
  }
  return table [ V ] ;
}
|||

SUM_NODES_K_TH_LEVEL_TREE_REPRESENTED_STRING

static int sumAtKthLevel ( String tree , int k ) {
  int level = - 1 ;
  int sum = 0 ;
  int n = tree . length ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( tree . charAt ( i ) == '(' ) level ++ ;
    else if ( tree . charAt ( i ) == ')' ) level -- ;
    else {
      if ( level == k ) sum += ( tree . charAt ( i ) - '0' ) ;
    }
  }
  return sum ;
}
|||

DYNAMIC_PROGRAMMING_SET_4_LONGEST_COMMON_SUBSEQUENCE

int lcs ( char [ ] X , char [ ] Y , int m , int n ) {
  if ( m == 0 || n == 0 ) return 0 ;
  if ( X [ m - 1 ] == Y [ n - 1 ] ) return 1 + lcs ( X , Y , m - 1 , n - 1 ) ;
  else return max ( lcs ( X , Y , m , n - 1 ) , lcs ( X , Y , m - 1 , n ) ) ;
}
|||

CHECK_GIVEN_SENTENCE_GIVEN_SET_SIMPLE_GRAMMER_RULES

static boolean checkSentence ( char [ ] str ) {
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
|||

CHECK_DIVISIBILITY_LARGE_NUMBER_999

static boolean isDivisible999 ( String num ) {
  int n = num . length ( ) ;
  if ( n == 0 && num . charAt ( 0 ) == '0' ) return true ;
  if ( n % 3 == 1 ) num = "00" + num ;
  if ( n % 3 == 2 ) num = "0" + num ;
  int gSum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int group = 0 ;
    group += ( num . charAt ( i ++ ) - '0' ) * 100 ;
    group += ( num . charAt ( i ++ ) - '0' ) * 10 ;
    group += num . charAt ( i ) - '0' ;
    gSum += group ;
  }
  if ( gSum > 1000 ) {
    num = Integer . toString ( gSum ) ;
    n = num . length ( ) ;
    gSum = isDivisible999 ( num ) ? 1 : 0 ;
  }
  return ( gSum == 999 ) ;
}
|||

CHECK_LARGE_NUMBER_DIVISIBLE_9_NOT

static boolean check ( String str ) {
  int n = str . length ( ) ;
  int digitSum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) digitSum += ( str . charAt ( i ) - '0' ) ;
  return ( digitSum % 9 == 0 ) ;
}
|||

NUMBER_OF_BINARY_TREES_FOR_GIVEN_PREORDER_SEQUENCE_LENGTH

static int countTrees ( int n ) {
  int BT [ ] = new int [ n + 1 ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) BT [ i ] = 0 ;
  BT [ 0 ] = BT [ 1 ] = 1 ;
  for ( int i = 2 ;
  i <= n ;
  ++ i ) for ( int j = 0 ;
  j < i ;
  j ++ ) BT [ i ] += BT [ j ] * BT [ i - j - 1 ] ;
  return BT [ n ] ;
}
|||

PROGRAM_SWAP_UPPER_DIAGONAL_ELEMENTS_LOWER_DIAGONAL_ELEMENTS_MATRIX

static void swapUpperToLower ( int arr [ ] [ ] ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      int temp = arr [ i ] [ j ] ;
      arr [ i ] [ j ] = arr [ j ] [ i ] ;
      arr [ j ] [ i ] = temp ;
    }
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) System . out . print ( arr [ i ] [ j ] + " " ) ;
    System . out . println ( ) ;
  }
}
|||

FIND_SUM_MODULO_K_FIRST_N_NATURAL_NUMBER_1

static int findSum ( int N , int K ) {
  int ans = 0 ;
  int y = N / K ;
  int x = N % K ;
  ans = ( K * ( K - 1 ) / 2 ) * y + ( x * ( x + 1 ) ) / 2 ;
  return ans ;
}
|||

WAYS_REMOVE_ONE_ELEMENT_BINARY_STRING_XOR_BECOMES_ZERO

static int xorZero ( String s ) {
  int one_count = 0 , zero_count = 0 ;
  char [ ] str = s . toCharArray ( ) ;
  int n = str . length ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( str [ i ] == '1' ) one_count ++ ;
  else zero_count ++ ;
  if ( one_count % 2 == 0 ) return zero_count ;
  return one_count ;
}
|||

DYNAMIC_PROGRAMMING_SET_7_COIN_CHANGE

static int count ( int S [ ] , int m , int n ) {
  if ( n == 0 ) return 1 ;
  if ( n < 0 ) return 0 ;
  if ( m <= 0 && n >= 1 ) return 0 ;
  return count ( S , m - 1 , n ) + count ( S , m , n - S [ m - 1 ] ) ;
}
|||

MINIMUM_SUM_SUBSEQUENCE_LEAST_ONE_EVERY_FOUR_CONSECUTIVE_ELEMENTS_PICKED

static int minSum ( int [ ] arr , int n ) {
  int [ ] dp = new int [ n ] ;
  if ( n == 1 ) return arr [ 0 ] ;
  if ( n == 2 ) return Math . min ( arr [ 0 ] , arr [ 1 ] ) ;
  if ( n == 3 ) return Math . min ( arr [ 0 ] , Math . min ( arr [ 1 ] , arr [ 2 ] ) ) ;
  if ( n == 4 ) return Math . min ( Math . min ( arr [ 0 ] , arr [ 1 ] ) , Math . min ( arr [ 2 ] , arr [ 3 ] ) ) ;
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

static int maxPathSum ( int tri [ ] [ ] , int m , int n ) {
  for ( int i = m - 1 ;
  i >= 0 ;
  i -- ) {
    for ( int j = 0 ;
    j <= i ;
    j ++ ) {
      if ( tri [ i + 1 ] [ j ] > tri [ i + 1 ] [ j + 1 ] ) tri [ i ] [ j ] += tri [ i + 1 ] [ j ] ;
      else tri [ i ] [ j ] += tri [ i + 1 ] [ j + 1 ] ;
    }
  }
  return tri [ 0 ] [ 0 ] ;
}
|||

FIND_THREE_ELEMENT_FROM_DIFFERENT_THREE_ARRAYS_SUCH_THAT_THAT_A_B_C_K

static boolean findTriplet ( int a1 [ ] , int a2 [ ] , int a3 [ ] , int n1 , int n2 , int n3 , int sum ) {
  for ( int i = 0 ;
  i < n1 ;
  i ++ ) for ( int j = 0 ;
  j < n2 ;
  j ++ ) for ( int k = 0 ;
  k < n3 ;
  k ++ ) if ( a1 [ i ] + a2 [ j ] + a3 [ k ] == sum ) return true ;
  return false ;
}
|||

TAIL_RECURSION_FIBONACCI

static int fib ( int n , int a , int b ) {
  if ( n == 0 ) return a ;
  if ( n == 1 ) return b ;
  return fib ( n - 1 , b , a + b ) ;
}
|||

PROGRAM_TO_CHECK_IF_A_GIVEN_NUMBER_IS_LUCKY_ALL_DIGITS_ARE_DIFFERENT

static boolean isLucky ( int n ) {
  boolean arr [ ] = new boolean [ 10 ] ;
  for ( int i = 0 ;
  i < 10 ;
  i ++ ) arr [ i ] = false ;
  while ( n > 0 ) {
    int digit = n % 10 ;
    if ( arr [ digit ] ) return false ;
    arr [ digit ] = true ;
    n = n / 10 ;
  }
  return true ;
}
|||

GIVEN_N_X_N_SQUARE_MATRIX_FIND_SUM_SUB_SQUARES_SIZE_K_X_K_1

static void printSumTricky ( int mat [ ] [ ] , int k ) {
  if ( k > n ) return ;
  int stripSum [ ] [ ] = new int [ n ] [ n ] ;
  for ( int j = 0 ;
  j < n ;
  j ++ ) {
    int sum = 0 ;
    for ( int i = 0 ;
    i < k ;
    i ++ ) sum += mat [ i ] [ j ] ;
    stripSum [ 0 ] [ j ] = sum ;
    for ( int i = 1 ;
    i < n - k + 1 ;
    i ++ ) {
      sum += ( mat [ i + k - 1 ] [ j ] - mat [ i - 1 ] [ j ] ) ;
      stripSum [ i ] [ j ] = sum ;
    }
  }
  for ( int i = 0 ;
  i < n - k + 1 ;
  i ++ ) {
    int sum = 0 ;
    for ( int j = 0 ;
    j < k ;
    j ++ ) sum += stripSum [ i ] [ j ] ;
    System . out . print ( sum + " " ) ;
    for ( int j = 1 ;
    j < n - k + 1 ;
    j ++ ) {
      sum += ( stripSum [ i ] [ j + k - 1 ] - stripSum [ i ] [ j - 1 ] ) ;
      System . out . print ( sum + " " ) ;
    }
    System . out . println ( ) ;
  }
}
|||

SCHEDULE_ELEVATOR_TO_REDUCE_THE_TOTAL_TIME_TAKEN

static int minTime ( int n , int k , int a [ ] ) {
  int temp ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      if ( a [ i ] < a [ j ] ) {
        temp = a [ i ] ;
        a [ i ] = a [ j ] ;
        a [ j ] = temp ;
      }
    }
  }
  int minTime = 0 ;
  for ( int i = 0 ;
  i < n ;
  i += k ) minTime += ( 2 * a [ i ] ) ;
  return minTime ;
}
|||

ODD_EVEN_SORT_BRICK_SORT

public static void oddEvenSort ( int arr [ ] , int n ) {
  boolean isSorted = false ;
  while ( ! isSorted ) {
    isSorted = true ;
    int temp = 0 ;
    for ( int i = 1 ;
    i <= n - 2 ;
    i = i + 2 ) {
      if ( arr [ i ] > arr [ i + 1 ] ) {
        temp = arr [ i ] ;
        arr [ i ] = arr [ i + 1 ] ;
        arr [ i + 1 ] = temp ;
        isSorted = false ;
      }
    }
    for ( int i = 0 ;
    i <= n - 2 ;
    i = i + 2 ) {
      if ( arr [ i ] > arr [ i + 1 ] ) {
        temp = arr [ i ] ;
        arr [ i ] = arr [ i + 1 ] ;
        arr [ i + 1 ] = temp ;
        isSorted = false ;
      }
    }
  }
  return ;
}
|||

RETURN_MAXIMUM_OCCURRING_CHARACTER_IN_THE_INPUT_STRING

static char getMaxOccuringChar ( String str ) {
  int count [ ] = new int [ ASCII_SIZE ] ;
  int len = str . length ( ) ;
  for ( int i = 0 ;
  i < len ;
  i ++ ) count [ str . charAt ( i ) ] ++ ;
  int max = - 1 ;
  char result = ' ' ;
  for ( int i = 0 ;
  i < len ;
  i ++ ) {
    if ( max < count [ str . charAt ( i ) ] ) {
      max = count [ str . charAt ( i ) ] ;
      result = str . charAt ( i ) ;
    }
  }
  return result ;
}
|||

COUNT_NUMBER_PAIRS_N_B_N_GCD_B_B

static int CountPairs ( int n ) {
  int k = n ;
  int imin = 1 ;
  int ans = 0 ;
  while ( imin <= n ) {
    int imax = n / k ;
    ans += k * ( imax - imin + 1 ) ;
    imin = imax + 1 ;
    k = n / imin ;
  }
  return ans ;
}
|||

K_TH_DISTINCT_OR_NON_REPEATING_ELEMENT_IN_AN_ARRAY_1

static int printKDistinct ( int arr [ ] , int n , int k ) {
  Map < Integer , Integer > h = new HashMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( h . containsKey ( arr [ i ] ) ) h . put ( arr [ i ] , h . get ( arr [ i ] ) + 1 ) ;
    else h . put ( arr [ i ] , 1 ) ;
  }
  if ( h . size ( ) < k ) return - 1 ;
  int dist_count = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( h . get ( arr [ i ] ) == 1 ) dist_count ++ ;
    if ( dist_count == k ) return arr [ i ] ;
  }
  return - 1 ;
}
|||

GENERATE_BINARY_PERMUTATIONS_1S_0S_EVERY_POINT_PERMUTATIONS

static void generate ( int ones , int zeroes , String str , int len ) {
  if ( len == str . length ( ) ) {
    System . out . print ( str + " " ) ;
    return ;
  }
  generate ( ones + 1 , zeroes , str + "1" , len ) ;
  if ( ones > zeroes ) {
    generate ( ones , zeroes + 1 , str + "0" , len ) ;
  }
}
|||

SEARCH_INSERT_AND_DELETE_IN_AN_UNSORTED_ARRAY

static int findElement ( int arr [ ] , int n , int key ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( arr [ i ] == key ) return i ;
  return - 1 ;
}
|||

LCS_LONGEST_COMMON_SUBSEQUENCE_THREE_STRINGS

static int lcsOf3 ( String X , String Y , String Z , int m , int n , int o ) {
  int [ ] [ ] [ ] L = new int [ m + 1 ] [ n + 1 ] [ o + 1 ] ;
  for ( int i = 0 ;
  i <= m ;
  i ++ ) {
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      for ( int k = 0 ;
      k <= o ;
      k ++ ) {
        if ( i == 0 || j == 0 || k == 0 ) L [ i ] [ j ] [ k ] = 0 ;
        else if ( X . charAt ( i - 1 ) == Y . charAt ( j - 1 ) && X . charAt ( i - 1 ) == Z . charAt ( k - 1 ) ) L [ i ] [ j ] [ k ] = L [ i - 1 ] [ j - 1 ] [ k - 1 ] + 1 ;
        else L [ i ] [ j ] [ k ] = Math . max ( Math . max ( L [ i - 1 ] [ j ] [ k ] , L [ i ] [ j - 1 ] [ k ] ) , L [ i ] [ j ] [ k - 1 ] ) ;
      }
    }
  }
  return L [ m ] [ n ] [ o ] ;
}
|||

MAXIMUM_SUM_SUBARRAY_REMOVING_ONE_ELEMENT

static int maxSumSubarrayRemovingOneEle ( int arr [ ] , int n ) {
  int fw [ ] = new int [ n ] ;
  int bw [ ] = new int [ n ] ;
  int cur_max = arr [ 0 ] , max_so_far = arr [ 0 ] ;
  fw [ 0 ] = arr [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    cur_max = Math . max ( arr [ i ] , cur_max + arr [ i ] ) ;
    max_so_far = Math . max ( max_so_far , cur_max ) ;
    fw [ i ] = cur_max ;
  }
  cur_max = max_so_far = bw [ n - 1 ] = arr [ n - 1 ] ;
  for ( int i = n - 2 ;
  i >= 0 ;
  i -- ) {
    cur_max = Math . max ( arr [ i ] , cur_max + arr [ i ] ) ;
    max_so_far = Math . max ( max_so_far , cur_max ) ;
    bw [ i ] = cur_max ;
  }
  int fans = max_so_far ;
  for ( int i = 1 ;
  i < n - 1 ;
  i ++ ) fans = Math . max ( fans , fw [ i - 1 ] + bw [ i + 1 ] ) ;
  return fans ;
}
|||

COUNT_NUMBER_WAYS_TILE_FLOOR_SIZE_N_X_M_USING_1_X_M_SIZE_TILES

static int countWays ( int n , int m ) {
  int count [ ] = new int [ n + 1 ] ;
  count [ 0 ] = 0 ;
  int i ;
  for ( i = 1 ;
  i <= n ;
  i ++ ) {
    if ( i > m ) count [ i ] = count [ i - 1 ] + count [ i - m ] ;
    else if ( i < m ) count [ i ] = 1 ;
    else count [ i ] = 2 ;
  }
  return count [ n ] ;
}
|||

MIDDLE_OF_THREE_USING_MINIMUM_COMPARISONS

public static int middleOfThree ( int a , int b , int c ) {
  if ( ( a < b && b < c ) || ( c < b && b < a ) ) return b ;
  else if ( ( b < a && a < c ) || ( c < a && a < b ) ) return a ;
  else return c ;
}
|||

LONGEST_COMMON_INCREASING_SUBSEQUENCE_LCS_LIS

static int LCIS ( int arr1 [ ] , int n , int arr2 [ ] , int m ) {
  int table [ ] = new int [ m ] ;
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
      if ( arr1 [ i ] == arr2 [ j ] ) if ( current + 1 > table [ j ] ) table [ j ] = current + 1 ;
      if ( arr1 [ i ] > arr2 [ j ] ) if ( table [ j ] > current ) current = table [ j ] ;
    }
  }
  int result = 0 ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) if ( table [ i ] > result ) result = table [ i ] ;
  return result ;
}
|||

MAXIMUM_SUBSEQUENCE_SUM_SUCH_THAT_NO_THREE_ARE_CONSECUTIVE

static int maxSumWO3Consec ( int arr [ ] , int n ) {
  int sum [ ] = new int [ n ] ;
  if ( n >= 1 ) sum [ 0 ] = arr [ 0 ] ;
  if ( n >= 2 ) sum [ 1 ] = arr [ 0 ] + arr [ 1 ] ;
  if ( n > 2 ) sum [ 2 ] = Math . max ( sum [ 1 ] , Math . max ( arr [ 1 ] + arr [ 2 ] , arr [ 0 ] + arr [ 2 ] ) ) ;
  for ( int i = 3 ;
  i < n ;
  i ++ ) sum [ i ] = Math . max ( Math . max ( sum [ i - 1 ] , sum [ i - 2 ] + arr [ i ] ) , arr [ i ] + arr [ i - 1 ] + sum [ i - 3 ] ) ;
  return sum [ n - 1 ] ;
}
|||

EULERIAN_NUMBER_1

public static int eulerian ( int n , int m ) {
  int [ ] [ ] dp = new int [ n + 1 ] [ m + 1 ] ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= m ;
    j ++ ) {
      if ( i > j ) {
        if ( j == 0 ) dp [ i ] [ j ] = 1 ;
        else dp [ i ] [ j ] = ( ( i - j ) * dp [ i - 1 ] [ j - 1 ] ) + ( ( j + 1 ) * dp [ i - 1 ] [ j ] ) ;
      }
    }
  }
  return dp [ n ] [ m ] ;
}
|||

DOUBLE_FACTORIAL

static long doublefactorial ( long n ) {
  if ( n == 0 || n == 1 ) return 1 ;
  return n * doublefactorial ( n - 2 ) ;
}
|||

REARRANGE_POSITIVE_AND_NEGATIVE_NUMBERS_PUBLISH

static void rearrange ( int arr [ ] , int n ) {
  int i = - 1 , temp = 0 ;
  for ( int j = 0 ;
  j < n ;
  j ++ ) {
    if ( arr [ j ] < 0 ) {
      i ++ ;
      temp = arr [ i ] ;
      arr [ i ] = arr [ j ] ;
      arr [ j ] = temp ;
    }
  }
  int pos = i + 1 , neg = 0 ;
  while ( pos < n && neg < pos && arr [ neg ] < 0 ) {
    temp = arr [ neg ] ;
    arr [ neg ] = arr [ pos ] ;
    arr [ pos ] = temp ;
    pos ++ ;
    neg += 2 ;
  }
}
|||

MAXIMIZE_ARRAY_SUN_AFTER_K_NEGATION_OPERATIONS

static int maximumSum ( int arr [ ] , int n , int k ) {
  for ( int i = 1 ;
  i <= k ;
  i ++ ) {
    int min = + 2147483647 ;
    int index = - 1 ;
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( arr [ j ] < min ) {
        min = arr [ j ] ;
        index = j ;
      }
    }
    if ( min == 0 ) break ;
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

static int pre_compute ( int a [ ] , int n , int index , int k ) {
  int dp [ ] [ ] = new int [ n ] [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( a [ i ] > a [ 0 ] ) dp [ 0 ] [ i ] = a [ i ] + a [ 0 ] ;
    else dp [ 0 ] [ i ] = a [ i ] ;
  }
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( a [ j ] > a [ i ] && j > i ) {
        if ( dp [ i - 1 ] [ i ] + a [ j ] > dp [ i - 1 ] [ j ] ) dp [ i ] [ j ] = dp [ i - 1 ] [ i ] + a [ j ] ;
        else dp [ i ] [ j ] = dp [ i - 1 ] [ j ] ;
      }
      else dp [ i ] [ j ] = dp [ i - 1 ] [ j ] ;
    }
  }
  return dp [ index ] [ k ] ;
}
|||

FUNCTION_COPY_STRING_ITERATIVE_RECURSIVE

static void myCopy ( char s1 [ ] , char s2 [ ] ) {
  int i = 0 ;
  for ( i = 0 ;
  i < s1 . length ;
  i ++ ) s2 [ i ] = s1 [ i ] ;
}
|||

GIVEN_TWO_STRINGS_FIND_FIRST_STRING_SUBSEQUENCE_SECOND_1

static boolean isSubSequence ( String str1 , String str2 , int m , int n ) {
  int j = 0 ;
  for ( int i = 0 ;
  i < n && j < m ;
  i ++ ) if ( str1 . charAt ( j ) == str2 . charAt ( i ) ) j ++ ;
  return ( j == m ) ;
}
|||

FIND_UNIT_DIGIT_X_RAISED_POWER_Y_1

static int unitnumber ( int x , int y ) {
  x = x % 10 ;
  if ( y != 0 ) y = y % 4 + 4 ;
  return ( ( ( int ) ( Math . pow ( x , y ) ) ) % 10 ) ;
}
|||

PROGRAM_NEXT_FIT_ALGORITHM_MEMORY_MANAGEMENT

static void NextFit ( int blockSize [ ] , int m , int processSize [ ] , int n ) {
  int allocation [ ] = new int [ n ] , j = 0 ;
  Arrays . fill ( allocation , - 1 ) ;
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
  System . out . print ( "\nProcess No.\tProcess Size\tBlock no.\n" ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    System . out . print ( i + 1 + "\t\t" + processSize [ i ] + "\t\t" ) ;
    if ( allocation [ i ] != - 1 ) {
      System . out . print ( allocation [ i ] + 1 ) ;
    }
    else {
      System . out . print ( "Not Allocated" ) ;
    }
    System . out . println ( "" ) ;
  }
}
|||

NOBLE_INTEGERS_IN_AN_ARRAY_COUNT_OF_GREATER_ELEMENTS_IS_EQUAL_TO_VALUE

public static int nobleInteger ( int arr [ ] ) {
  int size = arr . length ;
  for ( int i = 0 ;
  i < size ;
  i ++ ) {
    int count = 0 ;
    for ( int j = 0 ;
    j < size ;
    j ++ ) if ( arr [ i ] < arr [ j ] ) count ++ ;
    if ( count == arr [ i ] ) return arr [ i ] ;
  }
  return - 1 ;
}
|||

MINIMUM_FLIP_REQUIRED_MAKE_BINARY_MATRIX_SYMMETRIC

static int minimumflip ( int mat [ ] [ ] , int n ) {
  int transpose [ ] [ ] = new int [ n ] [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) for ( int j = 0 ;
  j < n ;
  j ++ ) transpose [ i ] [ j ] = mat [ j ] [ i ] ;
  int flip = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) for ( int j = 0 ;
  j < n ;
  j ++ ) if ( transpose [ i ] [ j ] != mat [ i ] [ j ] ) flip ++ ;
  return flip / 2 ;
}
|||

SEGREGATE_EVEN_ODD_NUMBERS_SET_3

static void arrayEvenAndOdd ( int arr [ ] , int n ) {
  int i = - 1 , j = 0 ;
  while ( j != n ) {
    if ( arr [ j ] % 2 == 0 ) {
      i ++ ;
      int temp = arr [ i ] ;
      arr [ i ] = arr [ j ] ;
      arr [ j ] = temp ;
    }
    j ++ ;
  }
  for ( int k = 0 ;
  k < n ;
  k ++ ) System . out . print ( arr [ k ] + " " ) ;
}
|||

DFS_N_ARY_TREE_ACYCLIC_GRAPH_REPRESENTED_ADJACENCY_LIST

public static void dfs ( LinkedList < Integer > list [ ] , int node , int arrival ) {
  System . out . println ( node ) ;
  for ( int i = 0 ;
  i < list [ node ] . size ( ) ;
  i ++ ) {
    if ( list [ node ] . get ( i ) != arrival ) dfs ( list , list [ node ] . get ( i ) , node ) ;
  }
}
|||

HOW_TO_TURN_OFF_A_PARTICULAR_BIT_IN_A_NUMBER

static int turnOffK ( int n , int k ) {
  if ( k <= 0 ) return n ;
  return ( n & ~ ( 1 << ( k - 1 ) ) ) ;
}
|||

NUMBER_SUBSTRINGS_DIVISIBLE_8_NOT_3

static int count ( String s , int len ) {
  int MAX = 1000 ;
  int cur = 0 , dig = 0 ;
  int [ ] sum = new int [ MAX ] ;
  int [ ] [ ] dp = new int [ MAX ] [ 3 ] ;
  dp [ 0 ] [ 0 ] = 1 ;
  for ( int i = 1 ;
  i <= len ;
  i ++ ) {
    dig = ( int ) ( s . charAt ( i - 1 ) ) - 48 ;
    cur += dig ;
    cur %= 3 ;
    sum [ i ] = cur ;
    dp [ i ] [ 0 ] = dp [ i - 1 ] [ 0 ] ;
    dp [ i ] [ 1 ] = dp [ i - 1 ] [ 1 ] ;
    dp [ i ] [ 2 ] = dp [ i - 1 ] [ 2 ] ;
    dp [ i ] [ sum [ i ] ] ++ ;
  }
  int ans = 0 , dprev = 0 , value = 0 , dprev2 = 0 ;
  for ( int i = 1 ;
  i <= len ;
  i ++ ) {
    dig = ( int ) ( s . charAt ( i - 1 ) ) - 48 ;
    if ( dig == 8 ) ans ++ ;
    if ( i - 2 >= 0 ) {
      dprev = ( int ) ( s . charAt ( i - 2 ) ) - 48 ;
      value = dprev * 10 + dig ;
      if ( ( value % 8 == 0 ) && ( value % 3 != 0 ) ) ans ++ ;
    }
    if ( i - 3 >= 0 ) {
      dprev2 = ( int ) ( s . charAt ( i - 3 ) ) - 48 ;
      dprev = ( int ) ( s . charAt ( i - 2 ) ) - 48 ;
      value = dprev2 * 100 + dprev * 10 + dig ;
      if ( value % 8 != 0 ) continue ;
      ans += ( i - 2 ) ;
      ans -= ( dp [ i - 3 ] [ sum [ i ] ] ) ;
    }
  }
  return ans ;
}
|||

ADD_1_TO_A_GIVEN_NUMBER_1

static int addOne ( int x ) {
  return ( - ( ~ x ) ) ;
}
|||

CHECK_STRING_FOLLOWS_ANBN_PATTERN_NOT

public static boolean isAnBn ( String s ) {
  int l = s . length ( ) ;
  if ( l % 2 == 1 ) {
    return false ;
  }
  int i = 0 ;
  int j = l - 1 ;
  while ( i < j ) {
    if ( s . charAt ( i ) != 'a' || s . charAt ( j ) != 'b' ) {
      return false ;
    }
    i ++ ;
    j -- ;
  }
  return true ;
}
|||

FIND_FIRST_REPEATING_ELEMENT_ARRAY_INTEGERS

static void printFirstRepeating ( int arr [ ] ) {
  int min = - 1 ;
  HashSet < Integer > set = new HashSet < > ( ) ;
  for ( int i = arr . length - 1 ;
  i >= 0 ;
  i -- ) {
    if ( set . contains ( arr [ i ] ) ) min = i ;
    else set . add ( arr [ i ] ) ;
  }
  if ( min != - 1 ) System . out . println ( "The first repeating element is " + arr [ min ] ) ;
  else System . out . println ( "There are no repeating elements" ) ;
}
|||

COST_BALANCE_PARANTHESES

static int costToBalance ( String s ) {
  if ( s . length ( ) == 0 ) System . out . println ( 0 ) ;
  int ans = 0 ;
  int o = 0 , c = 0 ;
  for ( int i = 0 ;
  i < s . length ( ) ;
  i ++ ) {
    if ( s . charAt ( i ) == '(' ) o ++ ;
    if ( s . charAt ( i ) == ')' ) c ++ ;
  }
  if ( o != c ) return - 1 ;
  int [ ] a = new int [ s . length ( ) ] ;
  if ( s . charAt ( 0 ) == '(' ) a [ 0 ] = 1 ;
  else a [ 0 ] = - 1 ;
  if ( a [ 0 ] < 0 ) ans += Math . abs ( a [ 0 ] ) ;
  for ( int i = 1 ;
  i < s . length ( ) ;
  i ++ ) {
    if ( s . charAt ( i ) == '(' ) a [ i ] = a [ i - 1 ] + 1 ;
    else a [ i ] = a [ i - 1 ] - 1 ;
    if ( a [ i ] < 0 ) ans += Math . abs ( a [ i ] ) ;
  }
  return ans ;
}
|||

COIN_GAME_WINNER_EVERY_PLAYER_THREE_CHOICES

static boolean findWinner ( int x , int y , int n ) {
  boolean [ ] dp = new boolean [ n + 1 ] ;
  Arrays . fill ( dp , false ) ;
  dp [ 0 ] = false ;
  dp [ 1 ] = true ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    if ( i - 1 >= 0 && dp [ i - 1 ] == false ) dp [ i ] = true ;
    else if ( i - x >= 0 && dp [ i - x ] == false ) dp [ i ] = true ;
    else if ( i - y >= 0 && dp [ i - y ] == false ) dp [ i ] = true ;
    else dp [ i ] = false ;
  }
  return dp [ n ] ;
}
|||

SEQUENCES_GIVEN_LENGTH_EVERY_ELEMENT_EQUAL_TWICE_PREVIOUS

static int getTotalNumberOfSequences ( int m , int n ) {
  if ( m < n ) return 0 ;
  if ( n == 0 ) return 1 ;
  return getTotalNumberOfSequences ( m - 1 , n ) + getTotalNumberOfSequences ( m / 2 , n - 1 ) ;
}
|||

FIND_DUPLICATES_GIVEN_ARRAY_ELEMENTS_NOT_LIMITED_RANGE

private static void printDuplicates ( int [ ] arr , int n ) {
  Map < Integer , Integer > map = new HashMap < > ( ) ;
  int count = 0 ;
  boolean dup = false ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( map . containsKey ( arr [ i ] ) ) {
      count = map . get ( arr [ i ] ) ;
      map . put ( arr [ i ] , count + 1 ) ;
    }
    else {
      map . put ( arr [ i ] , 1 ) ;
    }
  }
  for ( Entry < Integer , Integer > entry : map . entrySet ( ) ) {
    if ( entry . getValue ( ) > 1 ) {
      System . out . print ( entry . getKey ( ) + " " ) ;
      dup = true ;
    }
  }
  if ( ! dup ) {
    System . out . println ( "-1" ) ;
  }
}
|||

LONGEST_REPEATING_SUBSEQUENCE_1

static int findLongestRepeatingSubSeq ( char X [ ] , int m , int n ) {
  if ( dp [ m ] [ n ] != - 1 ) {
    return dp [ m ] [ n ] ;
  }
  if ( m == 0 || n == 0 ) {
    return dp [ m ] [ n ] = 0 ;
  }
  if ( X [ m - 1 ] == X [ n - 1 ] && m != n ) {
    return dp [ m ] [ n ] = findLongestRepeatingSubSeq ( X , m - 1 , n - 1 ) + 1 ;
  }
  return dp [ m ] [ n ] = Math . max ( findLongestRepeatingSubSeq ( X , m , n - 1 ) , findLongestRepeatingSubSeq ( X , m - 1 , n ) ) ;
}
|||

COUNT_OF_N_DIGIT_NUMBERS_WHOSE_SUM_OF_DIGITS_EQUALS_TO_GIVEN_SUM

private static void findCount ( int n , int sum ) {
  int start = ( int ) Math . pow ( 10 , n - 1 ) ;
  int end = ( int ) Math . pow ( 10 , n ) - 1 ;
  int count = 0 ;
  int i = start ;
  while ( i < end ) {
    int cur = 0 ;
    int temp = i ;
    while ( temp != 0 ) {
      cur += temp % 10 ;
      temp = temp / 10 ;
    }
    if ( cur == sum ) {
      count ++ ;
      i += 9 ;
    }
    else i ++ ;
  }
  System . out . println ( count ) ;
}
|||

MINIMUM_COST_CONNECT_WEIGHTED_NODES_REPRESENTED_ARRAY

static int minimum_cost ( int a [ ] , int n ) {
  int mn = Integer . MAX_VALUE ;
  int sum = 0 ;
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

static void printDivisors ( int n ) {
  Vector < Integer > v = new Vector < > ( ) ;
  for ( int i = 1 ;
  i <= Math . sqrt ( n ) ;
  i ++ ) {
    if ( n % i == 0 ) {
      if ( n / i == i ) System . out . printf ( "%d " , i ) ;
      else {
        System . out . printf ( "%d " , i ) ;
        v . add ( n / i ) ;
      }
    }
  }
  for ( int i = v . size ( ) - 1 ;
  i >= 0 ;
  i -- ) System . out . printf ( "%d " , v . get ( i ) ) ;
}
|||

SQUARES_OF_MATRIX_DIAGONAL_ELEMENTS_1

static void diagonalsquare ( int mat [ ] [ ] , int row , int column ) {
  System . out . print ( " Diagonal one : " ) ;
  for ( int i = 0 ;
  i < row ;
  i ++ ) {
    System . out . print ( mat [ i ] [ i ] * mat [ i ] [ i ] + " " ) ;
  }
  System . out . println ( ) ;
  System . out . print ( " Diagonal two : " ) ;
  for ( int i = 0 ;
  i < row ;
  i ++ ) {
    System . out . print ( mat [ i ] [ row - i - 1 ] * mat [ i ] [ row - i - 1 ] + " " ) ;
  }
}
|||

C_PROGRAM_FIND_AREA_TRIANGLE_1

static double polygonArea ( double X [ ] , double Y [ ] , int n ) {
  double area = 0.0 ;
  int j = n - 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    area += ( X [ j ] + X [ i ] ) * ( Y [ j ] - Y [ i ] ) ;
    j = i ;
  }
  return Math . abs ( area / 2.0 ) ;
}
|||

RANGE_QUERIES_FOR_FREQUENCIES_OF_ARRAY_ELEMENTS

public static int findFrequency ( int arr [ ] , int n , int left , int right , int element ) {
  int count = 0 ;
  for ( int i = left - 1 ;
  i < right ;
  ++ i ) if ( arr [ i ] == element ) ++ count ;
  return count ;
}
|||

SERIES_LARGEST_GCD_SUM_EQUALS_N

static void print_sequence ( int n , int k ) {
  int b = n / ( k * ( k + 1 ) / 2 ) ;
  if ( b == 0 ) {
    System . out . println ( "-1" ) ;
  }
  else {
    int r = 1 ;
    for ( int x = 1 ;
    x * x <= n ;
    x ++ ) {
      if ( n % x != 0 ) continue ;
      if ( x <= b && x > r ) r = x ;
      if ( n / x <= b && n / x > r ) r = n / x ;
    }
    for ( int i = 1 ;
    i < k ;
    i ++ ) System . out . print ( r * i + " " ) ;
    int res = n - ( r * ( k * ( k - 1 ) / 2 ) ) ;
    System . out . println ( res ) ;
  }
}
|||

FIND_THREE_ELEMENT_FROM_DIFFERENT_THREE_ARRAYS_SUCH_THAT_THAT_A_B_C_K_1

static boolean findTriplet ( int a1 [ ] , int a2 [ ] , int a3 [ ] , int n1 , int n2 , int n3 , int sum ) {
  HashSet < Integer > s = new HashSet < Integer > ( ) ;
  for ( int i = 0 ;
  i < n1 ;
  i ++ ) {
    s . add ( a1 [ i ] ) ;
  }
  ArrayList < Integer > al = new ArrayList < > ( s ) ;
  for ( int i = 0 ;
  i < n2 ;
  i ++ ) {
    for ( int j = 0 ;
    j < n3 ;
    j ++ ) {
      if ( al . contains ( sum - a2 [ i ] - a3 [ j ] ) & al . indexOf ( sum - a2 [ i ] - a3 [ j ] ) != al . get ( al . size ( ) - 1 ) ) {
        return true ;
      }
    }
  }
  return false ;
}
|||

FIND_THE_MAXIMUM_ELEMENT_IN_AN_ARRAY_WHICH_IS_FIRST_INCREASING_AND_THEN_DECREASING_1

static int findMaximum ( int arr [ ] , int low , int high ) {
  if ( low == high ) return arr [ low ] ;
  if ( ( high == low + 1 ) && arr [ low ] >= arr [ high ] ) return arr [ low ] ;
  if ( ( high == low + 1 ) && arr [ low ] < arr [ high ] ) return arr [ high ] ;
  int mid = ( low + high ) / 2 ;
  if ( arr [ mid ] > arr [ mid + 1 ] && arr [ mid ] > arr [ mid - 1 ] ) return arr [ mid ] ;
  if ( arr [ mid ] > arr [ mid + 1 ] && arr [ mid ] < arr [ mid - 1 ] ) return findMaximum ( arr , low , mid - 1 ) ;
  else return findMaximum ( arr , mid + 1 , high ) ;
}
|||

DYNAMIC_PROGRAMMING_SET_1

int fib ( int n ) {
  if ( lookup [ n ] == NIL ) {
    if ( n <= 1 ) lookup [ n ] = n ;
    else lookup [ n ] = fib ( n - 1 ) + fib ( n - 2 ) ;
  }
  return lookup [ n ] ;
}
|||

MODULAR_EXPONENTIATION_POWER_IN_MODULAR_ARITHMETIC

static int power ( int x , int y , int p ) {
  int res = 1 ;
  x = x % p ;
  while ( y > 0 ) {
    if ( ( y & 1 ) == 1 ) res = ( res * x ) % p ;
    y = y >> 1 ;
    x = ( x * x ) % p ;
  }
  return res ;
}
|||

WRITE_ONE_LINE_C_FUNCTION_TO_FIND_WHETHER_A_NO_IS_POWER_OF_TWO_1

static boolean isPowerOfTwo ( int x ) {
  return x != 0 && ( ( x & ( x - 1 ) ) == 0 ) ;
}
|||

LONGEST_COMMON_SUBSEQUENCE_WITH_PERMUTATIONS_ALLOWED

static void longestString ( String str1 , String str2 ) {
  int count1 [ ] = new int [ 26 ] , count2 [ ] = new int [ 26 ] ;
  for ( int i = 0 ;
  i < str1 . length ( ) ;
  i ++ ) {
    count1 [ str1 . charAt ( i ) - 'a' ] ++ ;
  }
  for ( int i = 0 ;
  i < str2 . length ( ) ;
  i ++ ) {
    count2 [ str2 . charAt ( i ) - 'a' ] ++ ;
  }
  String result = "" ;
  for ( int i = 0 ;
  i < 26 ;
  i ++ ) {
    for ( int j = 1 ;
    j <= Math . min ( count1 [ i ] , count2 [ i ] ) ;
    j ++ ) {
      result += ( char ) ( 'a' + i ) ;
    }
  }
  System . out . println ( result ) ;
}
|||

DIFFERENCE_MAXIMUM_SUM_MINIMUM_SUM_N_M_ELEMENTSIN_REVIEW

static int find_difference ( int arr [ ] , int n , int m ) {
  int max = 0 , min = 0 ;
  Arrays . sort ( arr ) ;
  for ( int i = 0 , j = n - 1 ;
  i < m ;
  i ++ , j -- ) {
    min += arr [ i ] ;
    max += arr [ j ] ;
  }
  return ( max - min ) ;
}
|||

PRINT_NUMBER_ASCENDING_ORDER_CONTAINS_1_2_3_DIGITS

private static String printNumbers ( int [ ] numbers ) {
  ArrayList < Integer > array = new ArrayList < > ( ) ;
  for ( int number : numbers ) {
    if ( findContainsOneTwoThree ( number ) ) array . add ( number ) ;
  }
  Collections . sort ( array ) ;
  StringBuffer strbuf = new StringBuffer ( ) ;
  Iterator it = array . iterator ( ) ;
  while ( it . hasNext ( ) ) {
    int value = ( int ) it . next ( ) ;
    if ( strbuf . length ( ) > 0 ) strbuf . append ( ", " ) ;
    strbuf . append ( Integer . toString ( value ) ) ;
  }
  return ( strbuf . length ( ) > 0 ) ? strbuf . toString ( ) : "-1" ;
}
|||

DYNAMIC_PROGRAMMING_SET_3_LONGEST_INCREASING_SUBSEQUENCE

static int lis ( int arr [ ] , int n ) {
  max_ref = 1 ;
  _lis ( arr , n ) ;
  return max_ref ;
}
|||

MINIMUM_REVOLUTIONS_MOVE_CENTER_CIRCLE_TARGET

static double minRevolutions ( double r , int x1 , int y1 , int x2 , int y2 ) {
  double d = Math . sqrt ( ( x1 - x2 ) * ( x1 - x2 ) + ( y1 - y2 ) * ( y1 - y2 ) ) ;
  return Math . ceil ( d / ( 2 * r ) ) ;
}
|||

CHECK_TWO_GIVEN_SETS_DISJOINT

boolean aredisjoint ( int set1 [ ] , int set2 [ ] ) {
  for ( int i = 0 ;
  i < set1 . length ;
  i ++ ) {
    for ( int j = 0 ;
    j < set2 . length ;
    j ++ ) {
      if ( set1 [ i ] == set2 [ j ] ) return false ;
    }
  }
  return true ;
}
|||

FIND_MINIMUM_SUM_FACTORS_NUMBER

static int findMinSum ( int num ) {
  int sum = 0 ;
  for ( int i = 2 ;
  i * i <= num ;
  i ++ ) {
    while ( num % i == 0 ) {
      sum += i ;
      num /= i ;
    }
  }
  sum += num ;
  return sum ;
}
|||

FREQUENT_ELEMENT_ARRAY

static int mostFrequent ( int arr [ ] , int n ) {
  Arrays . sort ( arr ) ;
  int max_count = 1 , res = arr [ 0 ] ;
  int curr_count = 1 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] == arr [ i - 1 ] ) curr_count ++ ;
    else {
      if ( curr_count > max_count ) {
        max_count = curr_count ;
        res = arr [ i - 1 ] ;
      }
      curr_count = 1 ;
    }
  }
  if ( curr_count > max_count ) {
    max_count = curr_count ;
    res = arr [ n - 1 ] ;
  }
  return res ;
}
|||

MINIMUM_XOR_VALUE_PAIR_1

static int minXOR ( int arr [ ] , int n ) {
  Arrays . parallelSort ( arr ) ;
  int minXor = Integer . MAX_VALUE ;
  int val = 0 ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    val = arr [ i ] ^ arr [ i + 1 ] ;
    minXor = Math . min ( minXor , val ) ;
  }
  return minXor ;
}
|||

MINIMUM_SUM_PRODUCT_TWO_ARRAYS

static int minproduct ( int a [ ] , int b [ ] , int n , int k ) {
  int diff = 0 , res = 0 ;
  int temp = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int pro = a [ i ] * b [ i ] ;
    res = res + pro ;
    if ( pro < 0 && b [ i ] < 0 ) temp = ( a [ i ] + 2 * k ) * b [ i ] ;
    else if ( pro < 0 && a [ i ] < 0 ) temp = ( a [ i ] - 2 * k ) * b [ i ] ;
    else if ( pro > 0 && a [ i ] < 0 ) temp = ( a [ i ] + 2 * k ) * b [ i ] ;
    else if ( pro > 0 && a [ i ] > 0 ) temp = ( a [ i ] - 2 * k ) * b [ i ] ;
    int d = Math . abs ( pro - temp ) ;
    if ( d > diff ) diff = d ;
  }
  return res - diff ;
}
|||

FAST_MULTIPLICATION_METHOD_WITHOUT_USING_MULTIPLICATION_OPERATOR_RUSSIAN_PEASANTS_ALGORITHM

static int russianPeasant ( int a , int b ) {
  int res = 0 ;
  while ( b > 0 ) {
    if ( ( b & 1 ) != 0 ) res = res + a ;
    a = a << 1 ;
    b = b >> 1 ;
  }
  return res ;
}
|||

DIVISIBILITY_9_USING_BITWISE_OPERATORS

static boolean isDivBy9 ( int n ) {
  if ( n == 0 || n == 9 ) return true ;
  if ( n < 9 ) return false ;
  return isDivBy9 ( ( int ) ( n >> 3 ) - ( int ) ( n & 7 ) ) ;
}
|||

CHECK_ARRAY_REPRESENTS_INORDER_BINARY_SEARCH_TREE_NOT

static boolean isInorder ( int [ ] arr , int n ) {
  if ( n == 0 || n == 1 ) {
    return true ;
  }
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( arr [ i - 1 ] > arr [ i ] ) {
      return false ;
    }
  }
  return true ;
}
|||

GIVEN_TWO_UNSORTED_ARRAYS_FIND_PAIRS_WHOSE_SUM_X

static void findPairs ( int arr1 [ ] , int arr2 [ ] , int n , int m , int x ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) for ( int j = 0 ;
  j < m ;
  j ++ ) if ( arr1 [ i ] + arr2 [ j ] == x ) System . out . println ( arr1 [ i ] + " " + arr2 [ j ] ) ;
}
|||

BINARY_REPRESENTATION_OF_NEXT_NUMBER

static String nextGreater ( String num ) {
  int l = num . length ( ) ;
  int i ;
  for ( i = l - 1 ;
  i >= 0 ;
  i -- ) {
    if ( num . charAt ( i ) == '0' ) {
      num = num . substring ( 0 , i ) + '1' + num . substring ( i + 1 ) ;
      break ;
    }
    else {
      num = num . substring ( 0 , i ) + '0' + num . substring ( i + 1 ) ;
    }
  }
  if ( i < 0 ) {
    num = "1" + num ;
  }
  return num ;
}
|||

LARGEST_SUBARRAY_WITH_EQUAL_NUMBER_OF_0S_AND_1S

int findSubArray ( int arr [ ] , int n ) {
  int sum = 0 ;
  int maxsize = - 1 , startindex = 0 ;
  int endindex = 0 ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    sum = ( arr [ i ] == 0 ) ? - 1 : 1 ;
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      if ( arr [ j ] == 0 ) sum += - 1 ;
      else sum += 1 ;
      if ( sum == 0 && maxsize < j - i + 1 ) {
        maxsize = j - i + 1 ;
        startindex = i ;
      }
    }
  }
  endindex = startindex + maxsize - 1 ;
  if ( maxsize == - 1 ) System . out . println ( "No such subarray" ) ;
  else System . out . println ( startindex + " to " + endindex ) ;
  return maxsize ;
}
|||

COUNT_PAIRS_WHOSE_PRODUCTS_EXIST_IN_ARRAY_1

static int countPairs ( int arr [ ] , int n ) {
  int result = 0 ;
  HashSet < Integer > Hash = new HashSet < > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    Hash . add ( arr [ i ] ) ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      int product = arr [ i ] * arr [ j ] ;
      if ( Hash . contains ( product ) ) {
        result ++ ;
      }
    }
  }
  return result ;
}
|||

DYNAMIC_PROGRAMMING_SET_12_LONGEST_PALINDROMIC_SUBSEQUENCE

static int lps ( String seq ) {
  int n = seq . length ( ) ;
  int i , j , cl ;
  int L [ ] [ ] = new int [ n ] [ n ] ;
  for ( i = 0 ;
  i < n ;
  i ++ ) L [ i ] [ i ] = 1 ;
  for ( cl = 2 ;
  cl <= n ;
  cl ++ ) {
    for ( i = 0 ;
    i < n - cl + 1 ;
    i ++ ) {
      j = i + cl - 1 ;
      if ( seq . charAt ( i ) == seq . charAt ( j ) && cl == 2 ) L [ i ] [ j ] = 2 ;
      else if ( seq . charAt ( i ) == seq . charAt ( j ) ) L [ i ] [ j ] = L [ i + 1 ] [ j - 1 ] + 2 ;
      else L [ i ] [ j ] = max ( L [ i ] [ j - 1 ] , L [ i + 1 ] [ j ] ) ;
    }
  }
  return L [ 0 ] [ n - 1 ] ;
}
|||

COUNT_INVERSIONS_OF_SIZE_THREE_IN_A_GIVE_ARRAY_1

int getInvCount ( int arr [ ] , int n ) {
  int invcount = 0 ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    int small = 0 ;
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) if ( arr [ i ] > arr [ j ] ) small ++ ;
    int great = 0 ;
    for ( int j = i - 1 ;
    j >= 0 ;
    j -- ) if ( arr [ i ] < arr [ j ] ) great ++ ;
    invcount += great * small ;
  }
  return invcount ;
}
|||

DECIMAL_REPRESENTATION_GIVEN_BINARY_STRING_DIVISIBLE_10_NOT

static boolean isDivisibleBy10 ( String bin ) {
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
|||

FIND_WHETHER_AN_ARRAY_IS_SUBSET_OF_ANOTHER_ARRAY_SET_1_1

static boolean isSubset ( int arr1 [ ] , int arr2 [ ] , int m , int n ) {
  int i = 0 , j = 0 ;
  if ( m < n ) return false ;
  Arrays . sort ( arr1 ) ;
  Arrays . sort ( arr2 ) ;
  while ( i < n && j < m ) {
    if ( arr1 [ j ] < arr2 [ i ] ) j ++ ;
    else if ( arr1 [ j ] == arr2 [ i ] ) {
      j ++ ;
      i ++ ;
    }
    else if ( arr1 [ j ] > arr2 [ i ] ) return false ;
  }
  if ( i < n ) return false ;
  else return true ;
}
|||

DYNAMIC_PROGRAMMING_SUBSET_SUM_PROBLEM_1

static boolean isSubsetSum ( int set [ ] , int n , int sum ) {
  boolean subset [ ] [ ] = new boolean [ sum + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) subset [ 0 ] [ i ] = true ;
  for ( int i = 1 ;
  i <= sum ;
  i ++ ) subset [ i ] [ 0 ] = false ;
  for ( int i = 1 ;
  i <= sum ;
  i ++ ) {
    for ( int j = 1 ;
    j <= n ;
    j ++ ) {
      subset [ i ] [ j ] = subset [ i ] [ j - 1 ] ;
      if ( i >= set [ j - 1 ] ) subset [ i ] [ j ] = subset [ i ] [ j ] || subset [ i - set [ j - 1 ] ] [ j - 1 ] ;
    }
  }
  return subset [ sum ] [ n ] ;
}
|||

SUM_K_TH_GROUP_ODD_POSITIVE_NUMBERS_1

public static int kthgroupsum ( int k ) {
  return k * k * k ;
}
|||

THIRD_LARGEST_ELEMENT_ARRAY_DISTINCT_ELEMENTS

static void thirdLargest ( int arr [ ] , int arr_size ) {
  if ( arr_size < 3 ) {
    System . out . printf ( " Invalid Input " ) ;
    return ;
  }
  int first = arr [ 0 ] ;
  for ( int i = 1 ;
  i < arr_size ;
  i ++ ) if ( arr [ i ] > first ) first = arr [ i ] ;
  int second = Integer . MIN_VALUE ;
  for ( int i = 0 ;
  i < arr_size ;
  i ++ ) if ( arr [ i ] > second && arr [ i ] < first ) second = arr [ i ] ;
  int third = Integer . MIN_VALUE ;
  for ( int i = 0 ;
  i < arr_size ;
  i ++ ) if ( arr [ i ] > third && arr [ i ] < second ) third = arr [ i ] ;
  System . out . printf ( "The third Largest " + "element is %d\n" , third ) ;
}
|||

FIND_SUM_NODES_GIVEN_PERFECT_BINARY_TREE_1

static double sumNodes ( int l ) {
  double leafNodeCount = Math . pow ( 2 , l - 1 ) ;
  double sumLastLevel = 0 ;
  sumLastLevel = ( leafNodeCount * ( leafNodeCount + 1 ) ) / 2 ;
  double sum = sumLastLevel * l ;
  return sum ;
}
|||

MIDDLE_OF_THREE_USING_MINIMUM_COMPARISONS_2

public static int middleOfThree ( int a , int b , int c ) {
  int x = a - b ;
  int y = b - c ;
  int z = a - c ;
  if ( x * y > 0 ) return b ;
  else if ( x * z > 0 ) return c ;
  else return a ;
}
|||

MAXIMUM_TRIPLET_SUM_ARRAY_2

static int maxTripletSum ( int arr [ ] , int n ) {
  int maxA = - 100000000 , maxB = - 100000000 ;
  int maxC = - 100000000 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] > maxA ) {
      maxC = maxB ;
      maxB = maxA ;
      maxA = arr [ i ] ;
    }
    else if ( arr [ i ] > maxB ) {
      maxC = maxB ;
      maxB = arr [ i ] ;
    }
    else if ( arr [ i ] > maxC ) maxC = arr [ i ] ;
  }
  return ( maxA + maxB + maxC ) ;
}
|||

COUNT_PAIRS_TWO_SORTED_ARRAYS_WHOSE_SUM_EQUAL_GIVEN_VALUE_X_1

static int countPairs ( int arr1 [ ] , int arr2 [ ] , int m , int n , int x ) {
  int count = 0 ;
  HashSet < Integer > us = new HashSet < Integer > ( ) ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) us . add ( arr1 [ i ] ) ;
  for ( int j = 0 ;
  j < n ;
  j ++ ) if ( us . contains ( x - arr2 [ j ] ) ) count ++ ;
  return count ;
}
|||

MINIMUM_STEPS_REACH_END_ARRAY_CONSTRAINTS

static int getMinStepToReachEnd ( int arr [ ] , int N ) {
  boolean [ ] visit = new boolean [ N ] ;
  int [ ] distance = new int [ N ] ;
  Vector < Integer > [ ] digit = new Vector [ 10 ] ;
  for ( int i = 0 ;
  i < 10 ;
  i ++ ) digit [ i ] = new Vector < > ( ) ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) visit [ i ] = false ;
  for ( int i = 1 ;
  i < N ;
  i ++ ) digit [ arr [ i ] ] . add ( i ) ;
  distance [ 0 ] = 0 ;
  visit [ 0 ] = true ;
  Queue < Integer > q = new LinkedList < > ( ) ;
  q . add ( 0 ) ;
  while ( ! q . isEmpty ( ) ) {
    int idx = q . peek ( ) ;
    q . remove ( ) ;
    if ( idx == N - 1 ) break ;
    int d = arr [ idx ] ;
    for ( int i = 0 ;
    i < digit [ d ] . size ( ) ;
    i ++ ) {
      int nextidx = digit [ d ] . get ( i ) ;
      if ( ! visit [ nextidx ] ) {
        visit [ nextidx ] = true ;
        q . add ( nextidx ) ;
        distance [ nextidx ] = distance [ idx ] + 1 ;
      }
    }
    digit [ d ] . clear ( ) ;
    if ( idx - 1 >= 0 && ! visit [ idx - 1 ] ) {
      visit [ idx - 1 ] = true ;
      q . add ( idx - 1 ) ;
      distance [ idx - 1 ] = distance [ idx ] + 1 ;
    }
    if ( idx + 1 < N && ! visit [ idx + 1 ] ) {
      visit [ idx + 1 ] = true ;
      q . add ( idx + 1 ) ;
      distance [ idx + 1 ] = distance [ idx ] + 1 ;
    }
  }
  return distance [ N - 1 ] ;
}
|||

LEXICOGRAPHICALLY_SMALLEST_ARRAY_K_CONSECUTIVE_SWAPS

static void minimizeWithKSwaps ( int arr [ ] , int n , int k ) {
  for ( int i = 0 ;
  i < n - 1 && k > 0 ;
  ++ i ) {
    int pos = i ;
    for ( int j = i + 1 ;
    j < n ;
    ++ j ) {
      if ( j - i > k ) break ;
      if ( arr [ j ] < arr [ pos ] ) pos = j ;
    }
    int temp ;
    for ( int j = pos ;
    j > i ;
    -- j ) {
      temp = arr [ j ] ;
      arr [ j ] = arr [ j - 1 ] ;
      arr [ j - 1 ] = temp ;
    }
    k -= pos - i ;
  }
}
|||

CONVERT_SENTENCE_EQUIVALENT_MOBILE_NUMERIC_KEYPAD_SEQUENCE

static String printSequence ( String arr [ ] , String input ) {
  String output = "" ;
  int n = input . length ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( input . charAt ( i ) == ' ' ) output = output + "0" ;
    else {
      int position = input . charAt ( i ) - 'A' ;
      output = output + arr [ position ] ;
    }
  }
  return output ;
}
|||

PROGRAM_CHECK_ARRAY_SORTED_NOT_ITERATIVE_RECURSIVE

static int arraySortedOrNot ( int arr [ ] , int n ) {
  if ( n == 1 || n == 0 ) return 1 ;
  if ( arr [ n - 1 ] < arr [ n - 2 ] ) return 0 ;
  return arraySortedOrNot ( arr , n - 1 ) ;
}
|||

CHECK_TWO_GIVEN_CIRCLES_TOUCH_INTERSECT

static int circle ( int x1 , int y1 , int x2 , int y2 , int r1 , int r2 ) {
  int distSq = ( x1 - x2 ) * ( x1 - x2 ) + ( y1 - y2 ) * ( y1 - y2 ) ;
  int radSumSq = ( r1 + r2 ) * ( r1 + r2 ) ;
  if ( distSq == radSumSq ) return 1 ;
  else if ( distSq > radSumSq ) return - 1 ;
  else return 0 ;
}
|||

SMALLEST_POWER_OF_2_GREATER_THAN_OR_EQUAL_TO_N_2

static int nextPowerOf2 ( int n ) {
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

static int pad ( int n ) {
  int pPrevPrev = 1 , pPrev = 1 , pCurr = 1 , pNext = 1 ;
  for ( int i = 3 ;
  i <= n ;
  i ++ ) {
    pNext = pPrevPrev + pPrev ;
    pPrevPrev = pPrev ;
    pPrev = pCurr ;
    pCurr = pNext ;
  }
  return pNext ;
}
|||

CHECK_GIVEN_STRING_CAN_SPLIT_FOUR_DISTINCT_STRINGS

public static boolean check ( String s ) {
  if ( s . length ( ) >= 10 ) return true ;
  for ( int i = 1 ;
  i < s . length ( ) ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < s . length ( ) ;
    j ++ ) {
      for ( int k = j + 1 ;
      k < s . length ( ) ;
      k ++ ) {
        String s1 = "" , s2 = "" , s3 = "" , s4 = "" ;
        try {
          s1 = s . substring ( 0 , i ) ;
          s2 = s . substring ( i , j - i ) ;
          s3 = s . substring ( j , k - j ) ;
          s4 = s . substring ( k , s . length ( ) - k ) ;
        }
        catch ( StringIndexOutOfBoundsException e ) {
        }
        if ( strcheck ( s1 , s2 ) && strcheck ( s1 , s3 ) && strcheck ( s1 , s4 ) && strcheck ( s2 , s3 ) && strcheck ( s2 , s4 ) && strcheck ( s3 , s4 ) ) return true ;
      }
    }
  }
  return false ;
}
|||

PERMUTE_TWO_ARRAYS_SUM_EVERY_PAIR_GREATER_EQUAL_K

static boolean isPossible ( Integer a [ ] , int b [ ] , int n , int k ) {
  Arrays . sort ( a , Collections . reverseOrder ( ) ) ;
  Arrays . sort ( b ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( a [ i ] + b [ i ] < k ) return false ;
  return true ;
}
|||

ARRAY_ELEMENT_MOVED_K_USING_SINGLE_MOVES

static int winner ( int a [ ] , int n , int k ) {
  if ( k >= n - 1 ) return n ;
  int best = 0 , times = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( a [ i ] > best ) {
      best = a [ i ] ;
      if ( i == 1 ) times = 1 ;
    }
    else times += 1 ;
    if ( times >= k ) return best ;
  }
  return best ;
}
|||

DIRECTION_LAST_SQUARE_BLOCK

static void direction ( int R , int C ) {
  if ( R != C && R % 2 == 0 && C % 2 != 0 && R < C ) {
    System . out . println ( "Left" ) ;
    return ;
  }
  if ( R != C && R % 2 != 0 && C % 2 == 0 && R > C ) {
    System . out . println ( "Up" ) ;
    return ;
  }
  if ( R == C && R % 2 != 0 && C % 2 != 0 ) {
    System . out . println ( "Right" ) ;
    return ;
  }
  if ( R == C && R % 2 == 0 && C % 2 == 0 ) {
    System . out . println ( "Left" ) ;
    return ;
  }
  if ( R != C && R % 2 != 0 && C % 2 != 0 && R < C ) {
    System . out . println ( "Right" ) ;
    return ;
  }
  if ( R != C && R % 2 != 0 && C % 2 != 0 && R > C ) {
    System . out . println ( "Down" ) ;
    return ;
  }
  if ( R != C && R % 2 == 0 && C % 2 == 0 && R < C ) {
    System . out . println ( "Left" ) ;
    return ;
  }
  if ( R != C && R % 2 == 0 && C % 2 == 0 && R > C ) {
    System . out . println ( "Up" ) ;
    return ;
  }
  if ( R != C && R % 2 == 0 && C % 2 != 0 && R > C ) {
    System . out . println ( "Down" ) ;
    return ;
  }
  if ( R != C && R % 2 != 0 && C % 2 == 0 && R < C ) {
    System . out . println ( "Right" ) ;
    return ;
  }
}
|||

NUMBER_NON_NEGATIVE_INTEGRAL_SOLUTIONS_B_C_N

static int countIntegralSolutions ( int n ) {
  int result = 0 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) for ( int j = 0 ;
  j <= n - i ;
  j ++ ) for ( int k = 0 ;
  k <= ( n - i - j ) ;
  k ++ ) if ( i + j + k == n ) result ++ ;
  return result ;
}
|||

SWAP_MAJOR_MINOR_DIAGONALS_SQUARE_MATRIX

static void swapDiagonal ( int matrix [ ] [ ] ) {
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    int temp = matrix [ i ] [ i ] ;
    matrix [ i ] [ i ] = matrix [ i ] [ N - i - 1 ] ;
    matrix [ i ] [ N - i - 1 ] = temp ;
  }
}
|||

MINIMUM_OPERATIONS_MAKE_GCD_ARRAY_MULTIPLE_K

static int MinOperation ( int a [ ] , int n , int k ) {
  int result = 0 ;
  for ( int i = 0 ;
  i < n ;
  ++ i ) {
    if ( a [ i ] != 1 && a [ i ] > k ) {
      result = result + Math . min ( a [ i ] % k , k - a [ i ] % k ) ;
    }
    else {
      result = result + k - a [ i ] ;
    }
  }
  return result ;
}
|||

MAXIMUM_DECIMAL_VALUE_PATH_IN_A_BINARY_MATRIX

static int maxDecimalValue ( int mat [ ] [ ] , int i , int j , int p ) {
  if ( i >= N || j >= N ) {
    return 0 ;
  }
  int result = Math . max ( maxDecimalValue ( mat , i , j + 1 , p + 1 ) , maxDecimalValue ( mat , i + 1 , j , p + 1 ) ) ;
  if ( mat [ i ] [ j ] == 1 ) {
    return ( int ) ( Math . pow ( 2 , p ) + result ) ;
  }
  else {
    return result ;
  }
}
|||

SQUARE_ROOT_OF_A_PERFECT_SQUARE_1

static long squareRoot ( int n ) {
  int x = n ;
  int y = 1 ;
  while ( x > y ) {
    x = ( x + y ) / 2 ;
    y = n / x ;
  }
  return ( long ) x ;
}
|||

FIND_MINIMUM_SHIFT_LONGEST_COMMON_PREFIX

static void KMP ( int m , int n , String str2 , String str1 ) {
  int pos = 0 , len = 0 ;
  int [ ] p = new int [ m + 1 ] ;
  int k = 0 ;
  char [ ] ch1 = str1 . toCharArray ( ) ;
  char [ ] ch2 = str2 . toCharArray ( ) ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    while ( k > 0 && ch1 [ k ] != ch1 [ i - 1 ] ) k = p [ k ] ;
    if ( ch1 [ k ] == ch1 [ i - 1 ] ) ++ k ;
    p [ i ] = k ;
  }
  for ( int j = 0 , i = 0 ;
  i < m ;
  i ++ ) {
    while ( j > 0 && j < n && ch1 [ j ] != ch2 [ i ] ) j = p [ j ] ;
    if ( j < n && ch1 [ j ] == ch2 [ i ] ) j ++ ;
    if ( j > len ) {
      len = j ;
      pos = i - j + 1 ;
    }
  }
  System . out . println ( "Shift = " + pos ) ;
  System . out . println ( "Prefix = " + str1 . substring ( 0 , len ) ) ;
}
|||

SORTED_ORDER_PRINTING_OF_AN_ARRAY_THAT_REPRESENTS_A_BST

private static void printSorted ( int [ ] arr , int start , int end ) {
  if ( start > end ) return ;
  printSorted ( arr , start * 2 + 1 , end ) ;
  System . out . print ( arr [ start ] + " " ) ;
  printSorted ( arr , start * 2 + 2 , end ) ;
}
|||

CHECK_WHETHER_GIVEN_DEGREES_VERTICES_REPRESENT_GRAPH_TREE

static boolean check ( int degree [ ] , int n ) {
  int deg_sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    deg_sum += degree [ i ] ;
  }
  return ( 2 * ( n - 1 ) == deg_sum ) ;
}
|||

MOVE_ZEROES_END_ARRAY

static void pushZerosToEnd ( int arr [ ] , int n ) {
  int count = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( arr [ i ] != 0 ) arr [ count ++ ] = arr [ i ] ;
  while ( count < n ) arr [ count ++ ] = 0 ;
}
|||

COUNT_ELEMENTS_WHICH_DIVIDE_ALL_NUMBERS_IN_RANGE_L_R

static int answerQuery ( int a [ ] , int n , int l , int r ) {
  int count = 0 ;
  l = l - 1 ;
  for ( int i = l ;
  i < r ;
  i ++ ) {
    int element = a [ i ] ;
    int divisors = 0 ;
    for ( int j = l ;
    j < r ;
    j ++ ) {
      if ( a [ j ] % a [ i ] == 0 ) divisors ++ ;
      else break ;
    }
    if ( divisors == ( r - l ) ) count ++ ;
  }
  return count ;
}
|||

SUM_LARGEST_PRIME_FACTOR_NUMBER_LESS_EQUAL_N

static int sumOfLargePrimeFactor ( int n ) {
  int prime [ ] = new int [ n + 1 ] , sum = 0 ;
  Arrays . fill ( prime , 0 ) ;
  int max = n / 2 ;
  for ( int p = 2 ;
  p <= max ;
  p ++ ) {
    if ( prime [ p ] == 0 ) {
      for ( int i = p * 2 ;
      i <= n ;
      i += p ) prime [ i ] = p ;
    }
  }
  for ( int p = 2 ;
  p <= n ;
  p ++ ) {
    if ( prime [ p ] != 0 ) sum += prime [ p ] ;
    else sum += p ;
  }
  return sum ;
}
|||

REARRANGE_A_STRING_IN_SORTED_ORDER_FOLLOWED_BY_THE_INTEGER_SUM

static String arrangeString ( String str ) {
  int char_count [ ] = new int [ MAX_CHAR ] ;
  int sum = 0 ;
  for ( int i = 0 ;
  i < str . length ( ) ;
  i ++ ) {
    if ( Character . isUpperCase ( str . charAt ( i ) ) ) char_count [ str . charAt ( i ) - 'A' ] ++ ;
    else sum = sum + ( str . charAt ( i ) - '0' ) ;
  }
  String res = "" ;
  for ( int i = 0 ;
  i < MAX_CHAR ;
  i ++ ) {
    char ch = ( char ) ( 'A' + i ) ;
    while ( char_count [ i ] -- != 0 ) res = res + ch ;
  }
  if ( sum > 0 ) res = res + sum ;
  return res ;
}
|||

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX_1

static int numberOfPaths ( int m , int n ) {
  int count [ ] [ ] = new int [ m ] [ n ] ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) count [ i ] [ 0 ] = 1 ;
  for ( int j = 0 ;
  j < n ;
  j ++ ) count [ 0 ] [ j ] = 1 ;
  for ( int i = 1 ;
  i < m ;
  i ++ ) {
    for ( int j = 1 ;
    j < n ;
    j ++ ) count [ i ] [ j ] = count [ i - 1 ] [ j ] + count [ i ] [ j - 1 ] ;
  }
  return count [ m - 1 ] [ n - 1 ] ;
}
|||

DYNAMIC_PROGRAMMING_SET_5_EDIT_DISTANCE_1

static int editDistDP ( String str1 , String str2 , int m , int n ) {
  int dp [ ] [ ] = new int [ m + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i <= m ;
  i ++ ) {
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      if ( i == 0 ) dp [ i ] [ j ] = j ;
      else if ( j == 0 ) dp [ i ] [ j ] = i ;
      else if ( str1 . charAt ( i - 1 ) == str2 . charAt ( j - 1 ) ) dp [ i ] [ j ] = dp [ i - 1 ] [ j - 1 ] ;
      else dp [ i ] [ j ] = 1 + min ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] , dp [ i - 1 ] [ j - 1 ] ) ;
    }
  }
  return dp [ m ] [ n ] ;
}
|||

FIND_NUMBER_OF_SOLUTIONS_OF_A_LINEAR_EQUATION_OF_N_VARIABLES

static int countSol ( int coeff [ ] , int start , int end , int rhs ) {
  if ( rhs == 0 ) return 1 ;
  int result = 0 ;
  for ( int i = start ;
  i <= end ;
  i ++ ) if ( coeff [ i ] <= rhs ) result += countSol ( coeff , i , end , rhs - coeff [ i ] ) ;
  return result ;
}
|||

SUM_ELEMENTS_K1TH_K2TH_SMALLEST_ELEMENTS_1

static void minheapify ( int [ ] a , int index ) {
  int small = index ;
  int l = 2 * index + 1 ;
  int r = 2 * index + 2 ;
  if ( l < n && a [ l ] < a [ small ] ) small = l ;
  if ( r < n && a [ r ] < a [ small ] ) small = r ;
  if ( small != index ) {
    int t = a [ small ] ;
    a [ small ] = a [ index ] ;
    a [ index ] = t ;
    minheapify ( a , small ) ;
  }
}
|||

SEARCHING_FOR_PATTERNS_SET_2_KMP_ALGORITHM

void computeLPSArray ( String pat , int M , int lps [ ] ) {
  int len = 0 ;
  int i = 1 ;
  lps [ 0 ] = 0 ;
  while ( i < M ) {
    if ( pat . charAt ( i ) == pat . charAt ( len ) ) {
      len ++ ;
      lps [ i ] = len ;
      i ++ ;
    }
    else {
      if ( len != 0 ) {
        len = lps [ len - 1 ] ;
      }
      else {
        lps [ i ] = len ;
        i ++ ;
      }
    }
  }
}
|||

FIND_MINIMUM_DIFFERENCE_PAIR

static int findMinDiff ( int [ ] arr , int n ) {
  int diff = Integer . MAX_VALUE ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) for ( int j = i + 1 ;
  j < n ;
  j ++ ) if ( Math . abs ( ( arr [ i ] - arr [ j ] ) ) < diff ) diff = Math . abs ( ( arr [ i ] - arr [ j ] ) ) ;
  return diff ;
}
|||

PRINT_FIRST_K_DIGITS_1N_N_POSITIVE_INTEGER

static void print ( int n , int k ) {
  int rem = 1 ;
  for ( int i = 0 ;
  i < k ;
  i ++ ) {
    System . out . print ( ( 10 * rem ) / n ) ;
    rem = ( 10 * rem ) % n ;
  }
}
|||

GROUP_MULTIPLE_OCCURRENCE_OF_ARRAY_ELEMENTS_ORDERED_BY_FIRST_OCCURRENCE

static void groupElements ( int arr [ ] , int n ) {
  boolean visited [ ] = new boolean [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    visited [ i ] = false ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ! visited [ i ] ) {
      System . out . print ( arr [ i ] + " " ) ;
      for ( int j = i + 1 ;
      j < n ;
      j ++ ) {
        if ( arr [ i ] == arr [ j ] ) {
          System . out . print ( arr [ i ] + " " ) ;
          visited [ j ] = true ;
        }
      }
    }
  }
}
|||

CHECK_WHETHER_ARITHMETIC_PROGRESSION_CAN_FORMED_GIVEN_ARRAY

static boolean checkIsAP ( int arr [ ] , int n ) {
  if ( n == 1 ) return true ;
  Arrays . sort ( arr ) ;
  int d = arr [ 1 ] - arr [ 0 ] ;
  for ( int i = 2 ;
  i < n ;
  i ++ ) if ( arr [ i ] - arr [ i - 1 ] != d ) return false ;
  return true ;
}
|||

NTH_MULTIPLE_NUMBER_FIBONACCI_SERIES

public static int findPosition ( int k , int n ) {
  long f1 = 0 , f2 = 1 , f3 ;
  int i = 2 ;
  while ( i != 0 ) {
    f3 = f1 + f2 ;
    f1 = f2 ;
    f2 = f3 ;
    if ( f2 % k == 0 ) {
      return n * i ;
    }
    i ++ ;
  }
  return 0 ;
}
|||

COUNT_PAIRS_DIFFERENCE_EQUAL_K_1

static int countPairsWithDiffK ( int arr [ ] , int n , int k ) {
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
    else if ( arr [ r ] - arr [ l ] > k ) l ++ ;
    else r ++ ;
  }
  return count ;
}
|||

ELEMENTS_TO_BE_ADDED_SO_THAT_ALL_ELEMENTS_OF_A_RANGE_ARE_PRESENT_IN_ARRAY

static int countNum ( int [ ] arr , int n ) {
  int count = 0 ;
  Arrays . sort ( arr ) ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) if ( arr [ i ] != arr [ i + 1 ] && arr [ i ] != arr [ i + 1 ] - 1 ) count += arr [ i + 1 ] - arr [ i ] - 1 ;
  return count ;
}
|||

MAKE_LARGEST_PALINDROME_CHANGING_K_DIGITS

static String maximumPalinUsingKChanges ( String str , int k ) {
  char palin [ ] = str . toCharArray ( ) ;
  String ans = "" ;
  int l = 0 ;
  int r = str . length ( ) - 1 ;
  while ( l < r ) {
    if ( str . charAt ( l ) != str . charAt ( r ) ) {
      palin [ l ] = palin [ r ] = ( char ) Math . max ( str . charAt ( l ) , str . charAt ( r ) ) ;
      k -- ;
    }
    l ++ ;
    r -- ;
  }
  if ( k < 0 ) {
    return "Not possible" ;
  }
  l = 0 ;
  r = str . length ( ) - 1 ;
  while ( l <= r ) {
    if ( l == r ) {
      if ( k > 0 ) {
        palin [ l ] = '9' ;
      }
    }
    if ( palin [ l ] < '9' ) {
      if ( k >= 2 && palin [ l ] == str . charAt ( l ) && palin [ r ] == str . charAt ( r ) ) {
        k -= 2 ;
        palin [ l ] = palin [ r ] = '9' ;
      }
      else if ( k >= 1 && ( palin [ l ] != str . charAt ( l ) || palin [ r ] != str . charAt ( r ) ) ) {
        k -- ;
        palin [ l ] = palin [ r ] = '9' ;
      }
    }
    l ++ ;
    r -- ;
  }
  for ( int i = 0 ;
  i < palin . length ;
  i ++ ) ans += palin [ i ] ;
  return ans ;
}
|||

SUBARRAYSUBSTRING_VS_SUBSEQUENCE_AND_PROGRAMS_TO_GENERATE_THEM

static void subArray ( int n ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = i ;
    j < n ;
    j ++ ) {
      for ( int k = i ;
      k <= j ;
      k ++ ) System . out . print ( arr [ k ] + " " ) ;
    }
  }
}
|||

MAXIMUM_SUM_INCREASING_ORDER_ELEMENTS_N_ARRAYS

static int maximumSum ( int a [ ] [ ] , int n ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) sort ( a , i , n ) ;
  int sum = a [ n - 1 ] [ M - 1 ] ;
  int prev = a [ n - 1 ] [ M - 1 ] ;
  int i , j ;
  for ( i = n - 2 ;
  i >= 0 ;
  i -- ) {
    for ( j = M - 1 ;
    j >= 0 ;
    j -- ) {
      if ( a [ i ] [ j ] < prev ) {
        prev = a [ i ] [ j ] ;
        sum += prev ;
        break ;
      }
    }
    if ( j == - 1 ) return 0 ;
  }
  return sum ;
}
|||

C_PROGRAM_FACTORIAL_NUMBER

static int factorial ( int n ) {
  if ( n == 0 ) return 1 ;
  return n * factorial ( n - 1 ) ;
}
|||

PRINT_SQUARES_FIRST_N_NATURAL_NUMBERS_WITHOUT_USING

static void printSquares ( int n ) {
  int square = 0 , prev_x = 0 ;
  for ( int x = 0 ;
  x < n ;
  x ++ ) {
    square = ( square + x + prev_x ) ;
    System . out . print ( square + " " ) ;
    prev_x = x ;
  }
}
|||

ROPES_DATA_STRUCTURE_FAST_STRING_CONCATENATION

static void concatenate ( char a [ ] , char b [ ] , char c [ ] , int n1 , int n2 ) {
  int i ;
  for ( i = 0 ;
  i < n1 ;
  i ++ ) {
    c [ i ] = a [ i ] ;
  }
  for ( int j = 0 ;
  j < n2 ;
  j ++ ) {
    c [ i ++ ] = b [ j ] ;
  }
}
|||

GIVEN_TWO_SORTED_ARRAYS_NUMBER_X_FIND_PAIR_WHOSE_SUM_CLOSEST_X

void printClosest ( int ar1 [ ] , int ar2 [ ] , int m , int n , int x ) {
  int diff = Integer . MAX_VALUE ;
  int res_l = 0 , res_r = 0 ;
  int l = 0 , r = n - 1 ;
  while ( l < m && r >= 0 ) {
    if ( Math . abs ( ar1 [ l ] + ar2 [ r ] - x ) < diff ) {
      res_l = l ;
      res_r = r ;
      diff = Math . abs ( ar1 [ l ] + ar2 [ r ] - x ) ;
    }
    if ( ar1 [ l ] + ar2 [ r ] > x ) r -- ;
    else l ++ ;
  }
  System . out . print ( "The closest pair is [" + ar1 [ res_l ] + ", " + ar2 [ res_r ] + "]" ) ;
}
|||

CONVERT_STRICTLY_INCREASING_ARRAY_MINIMUM_CHANGES

static int minRemove ( int arr [ ] , int n ) {
  int LIS [ ] = new int [ n ] ;
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
      if ( arr [ i ] > arr [ j ] && ( i - j ) <= ( arr [ i ] - arr [ j ] ) ) LIS [ i ] = Math . max ( LIS [ i ] , LIS [ j ] + 1 ) ;
    }
    len = Math . max ( len , LIS [ i ] ) ;
  }
  return n - len ;
}
|||

TAIL_RECURSION

static int fact ( int n ) {
  if ( n == 0 ) return 1 ;
  return n * fact ( n - 1 ) ;
}
|||

RECURSIVE_FUNCTIONS

static void tower ( int n , char sourcePole , char destinationPole , char auxiliaryPole ) {
  if ( 0 == n ) return ;
  tower ( n - 1 , sourcePole , auxiliaryPole , destinationPole ) ;
  System . out . printf ( "Move the disk %d from %c to %c\n" , n , sourcePole , destinationPole ) ;
  tower ( n - 1 , auxiliaryPole , destinationPole , sourcePole ) ;
}
|||

FIND_X_Y_SATISFYING_AX_N

static void solution ( int a , int b , int n ) {
  for ( int i = 0 ;
  i * a <= n ;
  i ++ ) {
    if ( ( n - ( i * a ) ) % b == 0 ) {
      System . out . println ( "x = " + i + ", y = " + ( n - ( i * a ) ) / b ) ;
      return ;
    }
  }
  System . out . println ( "No solution" ) ;
}
|||

EXPONENTIAL_SQUARING_FAST_MODULO_MULTIPLICATION_1

static long exponentiation ( long base , long exp ) {
  long t = 1L ;
  while ( exp > 0 ) {
    if ( exp % 2 != 0 ) t = ( t * base ) % N ;
    base = ( base * base ) % N ;
    exp /= 2 ;
  }
  return t % N ;
}
|||

CHECK_OCCURRENCES_CHARACTER_APPEAR_TOGETHER

static boolean checkIfAllTogether ( String s , char c ) {
  boolean oneSeen = false ;
  int i = 0 , n = s . length ( ) ;
  while ( i < n ) {
    if ( s . charAt ( i ) == c ) {
      if ( oneSeen == true ) return false ;
      while ( i < n && s . charAt ( i ) == c ) i ++ ;
      oneSeen = true ;
    }
    else i ++ ;
  }
  return true ;
}
|||

MAXIMUM_AREA_RECTANGLE_PICKING_FOUR_SIDES_ARRAY

static int findArea ( Integer arr [ ] , int n ) {
  Arrays . sort ( arr , Collections . reverseOrder ( ) ) ;
  int [ ] dimension = {
    0 , 0 };
    for ( int i = 0 , j = 0 ;
    i < n - 1 && j < 2 ;
    i ++ ) if ( arr [ i ] == arr [ i + 1 ] ) dimension [ j ++ ] = arr [ i ++ ] ;
    return ( dimension [ 0 ] * dimension [ 1 ] ) ;
  }
  |||

PYTHON_PROGRAM_FIND_PERIMETER_CIRCUMFERENCE_SQUARE_RECTANGLE

int Circumference ( int a ) {
  return 4 * a ;
}
|||

CYCLE_SORT

public static void cycleSort ( int arr [ ] , int n ) {
  int writes = 0 ;
  for ( int cycle_start = 0 ;
  cycle_start <= n - 2 ;
  cycle_start ++ ) {
    int item = arr [ cycle_start ] ;
    int pos = cycle_start ;
    for ( int i = cycle_start + 1 ;
    i < n ;
    i ++ ) if ( arr [ i ] < item ) pos ++ ;
    if ( pos == cycle_start ) continue ;
    while ( item == arr [ pos ] ) pos += 1 ;
    if ( pos != cycle_start ) {
      int temp = item ;
      item = arr [ pos ] ;
      arr [ pos ] = temp ;
      writes ++ ;
    }
    while ( pos != cycle_start ) {
      pos = cycle_start ;
      for ( int i = cycle_start + 1 ;
      i < n ;
      i ++ ) if ( arr [ i ] < item ) pos += 1 ;
      while ( item == arr [ pos ] ) pos += 1 ;
      if ( item != arr [ pos ] ) {
        int temp = item ;
        item = arr [ pos ] ;
        arr [ pos ] = temp ;
        writes ++ ;
      }
    }
  }
}
|||

SELECT_A_RANDOM_NUMBER_FROM_STREAM_WITH_O1_SPACE

static int selectRandom ( int x ) {
  count ++ ;
  if ( count == 1 ) res = x ;
  else {
    Random r = new Random ( ) ;
    int i = r . nextInt ( count ) ;
    if ( i == count - 1 ) res = x ;
  }
  return res ;
}
|||

HOSOYAS_TRIANGLE

static void printHosoya ( int n ) {
  int dp [ ] [ ] = new int [ N ] [ N ] ;
  dp [ 0 ] [ 0 ] = dp [ 1 ] [ 0 ] = 1 ;
  dp [ 1 ] [ 1 ] = 1 ;
  for ( int i = 2 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( i > j ) dp [ i ] [ j ] = dp [ i - 1 ] [ j ] + dp [ i - 2 ] [ j ] ;
      else dp [ i ] [ j ] = dp [ i - 1 ] [ j - 1 ] + dp [ i - 2 ] [ j - 2 ] ;
    }
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= i ;
    j ++ ) System . out . print ( dp [ i ] [ j ] + "" ) ;
    System . out . println ( "" ) ;
  }
}
|||

DISTRIBUTING_M_ITEMS_CIRCLE_SIZE_N_STARTING_K_TH_POSITION

static int lastPosition ( int n , int m , int k ) {
  if ( m <= n - k + 1 ) return m + k - 1 ;
  m = m - ( n - k + 1 ) ;
  return ( m % n == 0 ) ? n : ( m % n ) ;
}
|||

PRINTING_LONGEST_INCREASING_CONSECUTIVE_SUBSEQUENCE

public static void longestSubsequence ( int [ ] a , int n ) {
  HashMap < Integer , Integer > mp = new HashMap < > ( ) ;
  int [ ] dp = new int [ n ] ;
  int maximum = Integer . MIN_VALUE ;
  int index = - 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( mp . get ( a [ i ] - 1 ) != null ) {
      int lastIndex = mp . get ( a [ i ] - 1 ) - 1 ;
      dp [ i ] = 1 + dp [ lastIndex ] ;
    }
    else dp [ i ] = 1 ;
    mp . put ( a [ i ] , i + 1 ) ;
    if ( maximum < dp [ i ] ) {
      maximum = dp [ i ] ;
      index = i ;
    }
  }
  for ( int curr = a [ index ] - maximum + 1 ;
  curr <= a [ index ] ;
  curr ++ ) System . out . print ( curr + " " ) ;
}
|||

NUMBER_OF_TRIANGLES_IN_DIRECTED_AND_UNDIRECTED_GRAPHS

int countTriangle ( int graph [ ] [ ] , boolean isDirected ) {
  int count_Triangle = 0 ;
  for ( int i = 0 ;
  i < V ;
  i ++ ) {
    for ( int j = 0 ;
    j < V ;
    j ++ ) {
      for ( int k = 0 ;
      k < V ;
      k ++ ) {
        if ( graph [ i ] [ j ] == 1 && graph [ j ] [ k ] == 1 && graph [ k ] [ i ] == 1 ) count_Triangle ++ ;
      }
    }
  }
  if ( isDirected == true ) {
    count_Triangle /= 3 ;
  }
  else {
    count_Triangle /= 6 ;
  }
  return count_Triangle ;
}
|||

CHECK_GIVEN_ARRAY_CONTAINS_DUPLICATE_ELEMENTS_WITHIN_K_DISTANCE

static boolean checkDuplicatesWithinK ( int arr [ ] , int k ) {
  HashSet < Integer > set = new HashSet < > ( ) ;
  for ( int i = 0 ;
  i < arr . length ;
  i ++ ) {
    if ( set . contains ( arr [ i ] ) ) return true ;
    set . add ( arr [ i ] ) ;
    if ( i >= k ) set . remove ( arr [ i - k ] ) ;
  }
  return false ;
}
|||

MINIMUM_INSERTIONS_SORT_ARRAY

static int minInsertionStepToSortArray ( int arr [ ] , int N ) {
  int [ ] lis = new int [ N ] ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) lis [ i ] = 1 ;
  for ( int i = 1 ;
  i < N ;
  i ++ ) for ( int j = 0 ;
  j < i ;
  j ++ ) if ( arr [ i ] >= arr [ j ] && lis [ i ] < lis [ j ] + 1 ) lis [ i ] = lis [ j ] + 1 ;
  int max = 0 ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) if ( max < lis [ i ] ) max = lis [ i ] ;
  return ( N - max ) ;
}
|||

GENERATE_TWO_OUTPUT_STRINGS_DEPENDING_UPON_OCCURRENCE_CHARACTER_INPUT_STRING

static void printDuo ( String str ) {
  int countChar [ ] = new int [ MAX_CHAR ] ;
  int n = str . length ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    countChar [ str . charAt ( i ) - 'a' ] ++ ;
  }
  String str1 = "" , str2 = "" ;
  for ( int i = 0 ;
  i < MAX_CHAR ;
  i ++ ) {
    if ( countChar [ i ] > 1 ) {
      str2 = str2 + ( char ) ( i + 'a' ) ;
    }
    else if ( countChar [ i ] == 1 ) {
      str1 = str1 + ( char ) ( i + 'a' ) ;
    }
  }
  System . out . print ( "String with characters occurring " + "once:\n" ) ;
  System . out . print ( str1 + "\n" ) ;
  System . out . print ( "String with characters occurring " + "multiple times:\n" ) ;
  System . out . print ( str2 + "\n" ) ;
  System . out . print ( "" ) ;
}
|||

NUMBER_DIGITS_PRODUCT_TWO_NUMBERS_1

public static int countDigits ( int a , int b ) {
  if ( a == 0 || b == 0 ) return 1 ;
  return ( int ) Math . floor ( Math . log10 ( Math . abs ( a ) ) + Math . log10 ( Math . abs ( b ) ) ) + 1 ;
}
|||

TOTAL_NUMBER_OF_NON_DECREASING_NUMBERS_WITH_N_DIGITS_1

static long countNonDecreasing ( int n ) {
  int N = 10 ;
  long count = 1 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    count *= ( N + i - 1 ) ;
    count /= i ;
  }
  return count ;
}
|||

COUNT_STRINGS_ADJACENT_CHARACTERS_DIFFERENCE_ONE

static long countStrs ( int n ) {
  long [ ] [ ] dp = new long [ n + 1 ] [ 27 ] ;
  for ( int i = 0 ;
  i < n + 1 ;
  i ++ ) {
    for ( int j = 0 ;
    j < 27 ;
    j ++ ) {
      dp [ i ] [ j ] = 0 ;
    }
  }
  for ( int i = 0 ;
  i <= 25 ;
  i ++ ) {
    dp [ 1 ] [ i ] = 1 ;
  }
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= 25 ;
    j ++ ) {
      if ( j == 0 ) {
        dp [ i ] [ j ] = dp [ i - 1 ] [ j + 1 ] ;
      }
      else {
        dp [ i ] [ j ] = ( dp [ i - 1 ] [ j - 1 ] + dp [ i - 1 ] [ j + 1 ] ) ;
      }
    }
  }
  long sum = 0 ;
  for ( int i = 0 ;
  i <= 25 ;
  i ++ ) {
    sum = ( sum + dp [ n ] [ i ] ) ;
  }
  return sum ;
}
|||

PROGRAM_TO_EFFICIENTLY_CALCULATE_EX

static float exponential ( int n , float x ) {
  float sum = 1 ;
  for ( int i = n - 1 ;
  i > 0 ;
  -- i ) sum = 1 + x * sum / i ;
  return sum ;
}
|||

EFFICIENTLY_COMPUTE_SUMS_OF_DIAGONALS_OF_A_MATRIX_1

static void printDiagonalSums ( int [ ] [ ] mat , int n ) {
  int principal = 0 , secondary = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    principal += mat [ i ] [ i ] ;
    secondary += mat [ i ] [ n - i - 1 ] ;
  }
  System . out . println ( "Principal Diagonal:" + principal ) ;
  System . out . println ( "Secondary Diagonal:" + secondary ) ;
}
|||

PRINT_WAYS_BREAK_STRING_BRACKET_FORM

static void findCombinations ( String str , int index , String out ) {
  if ( index == str . length ( ) ) System . out . println ( out ) ;
  for ( int i = index ;
  i < str . length ( ) ;
  i ++ ) findCombinations ( str , i + 1 , out + "(" + str . substring ( index , i + 1 ) + ")" ) ;
}
|||

LINEAR_SEARCH

public static int search ( int arr [ ] , int x ) {
  int n = arr . length ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] == x ) return i ;
  }
  return - 1 ;
}
|||

FIND_THE_ELEMENT_THAT_APPEARS_ONCE_2

static int singleNumber ( int a [ ] , int n ) {
  HashSet < Integer > s = new HashSet < Integer > ( ) ;
  for ( int i : a ) {
    s . add ( i ) ;
  }
  int arr_sum = 0 ;
  for ( int i : a ) {
    arr_sum += i ;
  }
  int set_sum = 0 ;
  for ( int i : s ) {
    set_sum += i ;
  }
  return ( 3 * set_sum - arr_sum ) / 2 ;
}
|||

SEARCH_ALMOST_SORTED_ARRAY

int binarySearch ( int arr [ ] , int l , int r , int x ) {
  if ( r >= l ) {
    int mid = l + ( r - l ) / 2 ;
    if ( arr [ mid ] == x ) return mid ;
    if ( mid > l && arr [ mid - 1 ] == x ) return ( mid - 1 ) ;
    if ( mid < r && arr [ mid + 1 ] == x ) return ( mid + 1 ) ;
    if ( arr [ mid ] > x ) return binarySearch ( arr , l , mid - 2 , x ) ;
    return binarySearch ( arr , mid + 2 , r , x ) ;
  }
  return - 1 ;
}
|||

EULERS_TOTIENT_FUNCTION_FOR_ALL_NUMBERS_SMALLER_THAN_OR_EQUAL_TO_N

static void computeTotient ( int n ) {
  long phi [ ] = new long [ n + 1 ] ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) phi [ i ] = i ;
  for ( int p = 2 ;
  p <= n ;
  p ++ ) {
    if ( phi [ p ] == p ) {
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
  i ++ ) System . out . println ( "Totient of " + i + " is " + phi [ i ] ) ;
}
|||

FIND_MINIMUM_NUMBER_DIVIDED_MAKE_NUMBER_PERFECT_SQUARE

static int findMinNumber ( int n ) {
  int count = 0 , ans = 1 ;
  while ( n % 2 == 0 ) {
    count ++ ;
    n /= 2 ;
  }
  if ( count % 2 == 1 ) ans *= 2 ;
  for ( int i = 3 ;
  i <= Math . sqrt ( n ) ;
  i += 2 ) {
    count = 0 ;
    while ( n % i == 0 ) {
      count ++ ;
      n /= i ;
    }
    if ( count % 2 == 1 ) ans *= i ;
  }
  if ( n > 2 ) ans *= n ;
  return ans ;
}
|||

COUNT_NUMBER_WAYS_JUMP_REACH_END

static void countWaysToJump ( int arr [ ] , int n ) {
  int count_jump [ ] = new int [ n ] ;
  Arrays . fill ( count_jump , 0 ) ;
  for ( int i = n - 2 ;
  i >= 0 ;
  i -- ) {
    if ( arr [ i ] >= n - i - 1 ) count_jump [ i ] ++ ;
    for ( int j = i + 1 ;
    j < n - 1 && j <= arr [ i ] + i ;
    j ++ ) if ( count_jump [ j ] != - 1 ) count_jump [ i ] += count_jump [ j ] ;
    if ( count_jump [ i ] == 0 ) count_jump [ i ] = - 1 ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) System . out . print ( count_jump [ i ] + " " ) ;
}
|||

CONVERT_SUBSTRINGS_LENGTH_K_BASE_B_DECIMAL_1

static void substringConversions ( String str , int k , int b ) {
  int i = 0 , sum = 0 , counter = k - 1 ;
  for ( i = 0 ;
  i < k ;
  i ++ ) {
    sum = ( int ) ( sum + ( ( str . charAt ( i ) - '0' ) * Math . pow ( b , counter ) ) ) ;
    counter -- ;
  }
  System . out . print ( sum + " " ) ;
  int prev = sum ;
  sum = 0 ;
  counter = 0 ;
  for ( ;
  i < str . length ( ) ;
  i ++ ) {
    sum = ( int ) ( prev - ( ( str . charAt ( i - k ) - '0' ) * Math . pow ( b , k - 1 ) ) ) ;
    sum = sum * b ;
    sum = sum + ( str . charAt ( i ) - '0' ) ;
    System . out . print ( sum + " " ) ;
    prev = sum ;
    counter ++ ;
  }
}
|||

TWO_ELEMENTS_WHOSE_SUM_IS_CLOSEST_TO_ZERO

static void minAbsSumPair ( int arr [ ] , int arr_size ) {
  int inv_count = 0 ;
  int l , r , min_sum , sum , min_l , min_r ;
  if ( arr_size < 2 ) {
    System . out . println ( "Invalid Input" ) ;
    return ;
  }
  min_l = 0 ;
  min_r = 1 ;
  min_sum = arr [ 0 ] + arr [ 1 ] ;
  for ( l = 0 ;
  l < arr_size - 1 ;
  l ++ ) {
    for ( r = l + 1 ;
    r < arr_size ;
    r ++ ) {
      sum = arr [ l ] + arr [ r ] ;
      if ( Math . abs ( min_sum ) > Math . abs ( sum ) ) {
        min_sum = sum ;
        min_l = l ;
        min_r = r ;
      }
    }
  }
  System . out . println ( " The two elements whose " + "sum is minimum are " + arr [ min_l ] + " and " + arr [ min_r ] ) ;
}
|||

HOW_TO_PRINT_MAXIMUM_NUMBER_OF_A_USING_GIVEN_FOUR_KEYS

static int findoptimal ( int N ) {
  if ( N <= 6 ) return N ;
  int [ ] screen = new int [ N ] ;
  int b ;
  int n ;
  for ( n = 1 ;
  n <= 6 ;
  n ++ ) screen [ n - 1 ] = n ;
  for ( n = 7 ;
  n <= N ;
  n ++ ) {
    screen [ n - 1 ] = Math . max ( 2 * screen [ n - 4 ] , Math . max ( 3 * screen [ n - 5 ] , 4 * screen [ n - 6 ] ) ) ;
  }
  return screen [ N - 1 ] ;
}
|||

PROGRAM_DECIMAL_BINARY_CONVERSION_2

static int decimalToBinary ( int N ) {
  int B_Number = 0 ;
  int cnt = 0 ;
  while ( N != 0 ) {
    int rem = N % 2 ;
    double c = Math . pow ( 10 , cnt ) ;
    B_Number += rem * c ;
    N /= 2 ;
    cnt ++ ;
  }
  return B_Number ;
}
|||

COUNTS_PATHS_POINT_REACH_ORIGIN_1

static int countPaths ( int n , int m ) {
  int dp [ ] [ ] = new int [ n + 1 ] [ m + 1 ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) dp [ i ] [ 0 ] = 1 ;
  for ( int i = 0 ;
  i <= m ;
  i ++ ) dp [ 0 ] [ i ] = 1 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) for ( int j = 1 ;
  j <= m ;
  j ++ ) dp [ i ] [ j ] = dp [ i - 1 ] [ j ] + dp [ i ] [ j - 1 ] ;
  return dp [ n ] [ m ] ;
}
|||

SUM_ELEMENTS_K1TH_K2TH_SMALLEST_ELEMENTS

static int sumBetweenTwoKth ( int arr [ ] , int k1 , int k2 ) {
  Arrays . sort ( arr ) ;
  int result = 0 ;
  for ( int i = k1 ;
  i < k2 - 1 ;
  i ++ ) result += arr [ i ] ;
  return result ;
}
|||

SMALLEST_SUBARRAY_K_DISTINCT_NUMBERS

static void minRange ( int arr [ ] , int n , int k ) {
  int l = 0 , r = n ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    Set < Integer > s = new HashSet < Integer > ( ) ;
    int j ;
    for ( j = i ;
    j < n ;
    j ++ ) {
      s . add ( arr [ j ] ) ;
      if ( s . size ( ) == k ) {
        if ( ( j - i ) < ( r - l ) ) {
          r = j ;
          l = i ;
        }
        break ;
      }
    }
    if ( j == n ) break ;
  }
  if ( l == 0 && r == n ) System . out . println ( "Invalid k" ) ;
  else System . out . println ( l + " " + r ) ;
}
|||

AREA_OF_A_HEXAGON

public static double hexagonArea ( double s ) {
  return ( ( 3 * Math . sqrt ( 3 ) * ( s * s ) ) / 2 ) ;
}
|||

NEXT_POWER_OF_2_2

static int nextPowerOf2 ( int n ) {
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

static int countOfSubstringWithKOnes ( String s , int K ) {
  int N = s . length ( ) ;
  int res = 0 ;
  int countOfOne = 0 ;
  int [ ] freq = new int [ N + 1 ] ;
  freq [ 0 ] = 1 ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    countOfOne += ( s . charAt ( i ) - '0' ) ;
    if ( countOfOne >= K ) {
      res += freq [ countOfOne - K ] ;
    }
    freq [ countOfOne ] ++ ;
  }
  return res ;
}
|||

NUMBER_INDEXES_EQUAL_ELEMENTS_GIVEN_RANGE

static int answer_query ( int a [ ] , int n , int l , int r ) {
  int count = 0 ;
  for ( int i = l ;
  i < r ;
  i ++ ) if ( a [ i ] == a [ i + 1 ] ) count += 1 ;
  return count ;
}
|||

CHECK_WHETHER_NUMBER_DUCK_NUMBER_NOT

static int check_duck ( String num ) {
  int len = num . length ( ) ;
  int count_zero = 0 ;
  char ch ;
  for ( int i = 1 ;
  i < len ;
  i ++ ) {
    ch = num . charAt ( i ) ;
    if ( ch == '0' ) count_zero ++ ;
  }
  return count_zero ;
}
|||

NUMBER_NON_NEGATIVE_INTEGRAL_SOLUTIONS_B_C_N_1

static int countIntegralSolutions ( int n ) {
  return ( ( n + 1 ) * ( n + 2 ) ) / 2 ;
}
|||

MAXIMUM_PROFIT_BY_BUYING_AND_SELLING_A_SHARE_AT_MOST_K_TIMES_1

static int maxProfit ( int price [ ] , int n , int k ) {
  int profit [ ] [ ] = new int [ k + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i <= k ;
  i ++ ) profit [ i ] [ 0 ] = 0 ;
  for ( int j = 0 ;
  j <= n ;
  j ++ ) profit [ 0 ] [ j ] = 0 ;
  for ( int i = 1 ;
  i <= k ;
  i ++ ) {
    int prevDiff = Integer . MIN_VALUE ;
    for ( int j = 1 ;
    j < n ;
    j ++ ) {
      prevDiff = Math . max ( prevDiff , profit [ i - 1 ] [ j - 1 ] - price [ j - 1 ] ) ;
      profit [ i ] [ j ] = Math . max ( profit [ i ] [ j - 1 ] , price [ j ] + prevDiff ) ;
    }
  }
  return profit [ k ] [ n - 1 ] ;
}
|||

COUNT_CHARACTERS_POSITION_ENGLISH_ALPHABETS

static int findCount ( String str ) {
  int result = 0 ;
  for ( int i = 0 ;
  i < str . length ( ) ;
  i ++ ) {
    if ( i == ( str . charAt ( i ) - 'a' ) || i == ( str . charAt ( i ) - 'A' ) ) {
      result ++ ;
    }
  }
  return result ;
}
|||

COUNT_GFG_SUBSEQUENCES_GIVEN_STRING

static void countSubsequence ( String s , int n ) {
  int cntG = 0 , cntF = 0 , result = 0 , C = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    switch ( s . charAt ( i ) ) {
      case 'G' : cntG ++ ;
      result += C ;
      break ;
      case 'F' : cntF ++ ;
      C += cntG ;
      break ;
      default : continue ;
    }
  }
  System . out . println ( result ) ;
}
|||

FIND_SMALLEST_VALUE_REPRESENTED_SUM_SUBSET_GIVEN_ARRAY

int findSmallest ( int arr [ ] , int n ) {
  int res = 1 ;
  for ( int i = 0 ;
  i < n && arr [ i ] <= res ;
  i ++ ) res = res + arr [ i ] ;
  return res ;
}
|||

MAXIMUM_POINTS_COLLECTED_BY_TWO_PERSONS_ALLOWED_TO_MEET_ONCE

static int findMaxPoints ( int A [ ] [ ] ) {
  int [ ] [ ] P1S = new int [ M + 2 ] [ N + 2 ] ;
  int [ ] [ ] P1E = new int [ M + 2 ] [ N + 2 ] ;
  int [ ] [ ] P2S = new int [ M + 2 ] [ N + 2 ] ;
  int [ ] [ ] P2E = new int [ M + 2 ] [ N + 2 ] ;
  for ( int i = 1 ;
  i <= N ;
  i ++ ) for ( int j = 1 ;
  j <= M ;
  j ++ ) P1S [ i ] [ j ] = Math . max ( P1S [ i - 1 ] [ j ] , P1S [ i ] [ j - 1 ] ) + A [ i - 1 ] [ j - 1 ] ;
  for ( int i = N ;
  i >= 1 ;
  i -- ) for ( int j = M ;
  j >= 1 ;
  j -- ) P1E [ i ] [ j ] = Math . max ( P1E [ i + 1 ] [ j ] , P1E [ i ] [ j + 1 ] ) + A [ i - 1 ] [ j - 1 ] ;
  for ( int i = N ;
  i >= 1 ;
  i -- ) for ( int j = 1 ;
  j <= M ;
  j ++ ) P2S [ i ] [ j ] = Math . max ( P2S [ i + 1 ] [ j ] , P2S [ i ] [ j - 1 ] ) + A [ i - 1 ] [ j - 1 ] ;
  for ( int i = 1 ;
  i <= N ;
  i ++ ) for ( int j = M ;
  j >= 1 ;
  j -- ) P2E [ i ] [ j ] = Math . max ( P2E [ i - 1 ] [ j ] , P2E [ i ] [ j + 1 ] ) + A [ i - 1 ] [ j - 1 ] ;
  int ans = 0 ;
  for ( int i = 2 ;
  i < N ;
  i ++ ) {
    for ( int j = 2 ;
    j < M ;
    j ++ ) {
      int op1 = P1S [ i ] [ j - 1 ] + P1E [ i ] [ j + 1 ] + P2S [ i + 1 ] [ j ] + P2E [ i - 1 ] [ j ] ;
      int op2 = P1S [ i - 1 ] [ j ] + P1E [ i + 1 ] [ j ] + P2S [ i ] [ j - 1 ] + P2E [ i ] [ j + 1 ] ;
      ans = Math . max ( ans , Math . max ( op1 , op2 ) ) ;
    }
  }
  return ans ;
}
|||

PROGRAM_FIND_CIRCUMFERENCE_CIRCLE

static double circumference ( double r ) {
  double PI = 3.1415 ;
  double cir = 2 * PI * r ;
  return cir ;
}
|||

QUICKLY_FIND_MULTIPLE_LEFT_ROTATIONS_OF_AN_ARRAY

static void leftRotate ( int arr [ ] , int n , int k ) {
  for ( int i = k ;
  i < k + n ;
  i ++ ) System . out . print ( arr [ i % n ] + " " ) ;
}
|||

MINIMUM_SUM_CHOOSING_MINIMUM_PAIRS_ARRAY

static int minSum ( int [ ] A , int n ) {
  int min_val = Arrays . stream ( A ) . min ( ) . getAsInt ( ) ;
  return ( min_val * ( n - 1 ) ) ;
}
|||

RECURSIVE_PROGRAM_PRIME_NUMBER

static boolean isPrime ( int n , int i ) {
  if ( n <= 2 ) return ( n == 2 ) ? true : false ;
  if ( n % i == 0 ) return false ;
  if ( i * i > n ) return true ;
  return isPrime ( n , i + 1 ) ;
}
|||

SPARSE_SEARCH

static int sparseSearch ( String arr [ ] , String x , int n ) {
  return binarySearch ( arr , 0 , n - 1 , x ) ;
}
|||

FIND_NUMBER_TIMES_STRING_OCCURS_GIVEN_STRING

static int count ( String a , String b , int m , int n ) {
  if ( ( m == 0 && n == 0 ) || n == 0 ) return 1 ;
  if ( m == 0 ) return 0 ;
  if ( a . charAt ( m - 1 ) == b . charAt ( n - 1 ) ) return count ( a , b , m - 1 , n - 1 ) + count ( a , b , m - 1 , n ) ;
  else return count ( a , b , m - 1 , n ) ;
}
|||

PROGRAM_CHECK_ARRAY_SORTED_NOT_ITERATIVE_RECURSIVE_1

static boolean arraySortedOrNot ( int arr [ ] , int n ) {
  if ( n == 0 || n == 1 ) return true ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) if ( arr [ i - 1 ] > arr [ i ] ) return false ;
  return true ;
}
|||

FIND_INDEX_0_REPLACED_1_GET_LONGEST_CONTINUOUS_SEQUENCE_1S_BINARY_ARRAY

static int maxOnesIndex ( int arr [ ] , int n ) {
  int max_count = 0 ;
  int max_index = 0 ;
  int prev_zero = - 1 ;
  int prev_prev_zero = - 1 ;
  for ( int curr = 0 ;
  curr < n ;
  ++ curr ) {
    if ( arr [ curr ] == 0 ) {
      if ( curr - prev_prev_zero > max_count ) {
        max_count = curr - prev_prev_zero ;
        max_index = prev_zero ;
      }
      prev_prev_zero = prev_zero ;
      prev_zero = curr ;
    }
  }
  if ( n - prev_prev_zero > max_count ) max_index = prev_zero ;
  return max_index ;
}
|||

FIND_MAXIMUM_PRODUCT_OF_A_TRIPLET_IN_ARRAY_1

static int maxProduct ( int arr [ ] , int n ) {
  if ( n < 3 ) {
    return - 1 ;
  }
  Arrays . sort ( arr ) ;
  return Math . max ( arr [ 0 ] * arr [ 1 ] * arr [ n - 1 ] , arr [ n - 1 ] * arr [ n - 2 ] * arr [ n - 3 ] ) ;
}
|||

COORDINATES_RECTANGLE_GIVEN_POINTS_LIE_INSIDE

static void printRect ( Integer X [ ] , Integer Y [ ] , int n ) {
  int Xmax = Collections . max ( Arrays . asList ( X ) ) ;
  int Xmin = Collections . min ( Arrays . asList ( X ) ) ;
  int Ymax = Collections . max ( Arrays . asList ( Y ) ) ;
  int Ymin = Collections . min ( Arrays . asList ( Y ) ) ;
  System . out . println ( "{" + Xmin + ", " + Ymin + "}" ) ;
  System . out . println ( "{" + Xmin + ", " + Ymax + "}" ) ;
  System . out . println ( "{" + Xmax + ", " + Ymax + "}" ) ;
  System . out . println ( "{" + Xmax + ", " + Ymin + "}" ) ;
}
|||

COUNT_BINARY_DIGIT_NUMBERS_SMALLER_N

static int countOfBinaryNumberLessThanN ( int N ) {
  Queue < Integer > q = new LinkedList < > ( ) ;
  q . add ( 1 ) ;
  int cnt = 0 ;
  int t ;
  while ( q . size ( ) > 0 ) {
    t = q . peek ( ) ;
    q . remove ( ) ;
    if ( t <= N ) {
      cnt ++ ;
      q . add ( t * 10 ) ;
      q . add ( t * 10 + 1 ) ;
    }
  }
  return cnt ;
}
|||

CONVERT_DECIMAL_FRACTION_BINARY_NUMBER

static String decimalToBinary ( double num , int k_prec ) {
  String binary = "" ;
  int Integral = ( int ) num ;
  double fractional = num - Integral ;
  while ( Integral > 0 ) {
    int rem = Integral % 2 ;
    binary += ( ( char ) ( rem + '0' ) ) ;
    Integral /= 2 ;
  }
  binary = reverse ( binary ) ;
  binary += ( '.' ) ;
  while ( k_prec -- > 0 ) {
    fractional *= 2 ;
    int fract_bit = ( int ) fractional ;
    if ( fract_bit == 1 ) {
      fractional -= fract_bit ;
      binary += ( char ) ( 1 + '0' ) ;
    }
    else {
      binary += ( char ) ( 0 + '0' ) ;
    }
  }
  return binary ;
}
|||

MAXIMUM_NUMBER_OF_TRAILING_ZEROS_IN_THE_PRODUCT_OF_THE_SUBSETS_OF_SIZE_K

static int maximumZeros ( int arr [ ] , int n , int k ) {
  int subset [ ] [ ] = new int [ k + 1 ] [ MAX5 + 5 ] ;
  for ( int [ ] row : subset ) {
    Arrays . fill ( row , - 1 ) ;
  }
  subset [ 0 ] [ 0 ] = 0 ;
  for ( int p = 0 ;
  p < n ;
  p ++ ) {
    int pw2 = 0 , pw5 = 0 ;
    while ( arr [ p ] % 2 == 0 ) {
      pw2 ++ ;
      arr [ p ] /= 2 ;
    }
    while ( arr [ p ] % 5 == 0 ) {
      pw5 ++ ;
      arr [ p ] /= 5 ;
    }
    for ( int i = k - 1 ;
    i >= 0 ;
    i -- ) {
      for ( int j = 0 ;
      j < MAX5 ;
      j ++ ) {
        if ( subset [ i ] [ j ] != - 1 ) {
          subset [ i + 1 ] [ j + pw5 ] = Math . max ( subset [ i + 1 ] [ j + pw5 ] , subset [ i ] [ j ] + pw2 ) ;
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

static int search ( int arr [ ] , int l , int h , int key ) {
  if ( l > h ) return - 1 ;
  int mid = ( l + h ) / 2 ;
  if ( arr [ mid ] == key ) return mid ;
  if ( arr [ l ] <= arr [ mid ] ) {
    if ( key >= arr [ l ] && key <= arr [ mid ] ) return search ( arr , l , mid - 1 , key ) ;
    return search ( arr , mid + 1 , h , key ) ;
  }
  if ( key >= arr [ mid ] && key <= arr [ h ] ) return search ( arr , mid + 1 , h , key ) ;
  return search ( arr , l , mid - 1 , key ) ;
}
|||

PROGRAM_FIND_AREA_CIRCULAR_SEGMENT

static float area_of_segment ( float radius , float angle ) {
  float area_of_sector = pi * ( radius * radius ) * ( angle / 360 ) ;
  float area_of_triangle = ( float ) 1 / 2 * ( radius * radius ) * ( float ) Math . sin ( ( angle * pi ) / 180 ) ;
  return area_of_sector - area_of_triangle ;
}
|||

K_SMALLEST_ELEMENTS_ORDER_USING_O1_EXTRA_SPACE

public static void printSmall ( int arr [ ] , int n , int k ) {
  for ( int i = k ;
  i < n ;
  ++ i ) {
    int max_var = arr [ k - 1 ] ;
    int pos = k - 1 ;
    for ( int j = k - 2 ;
    j >= 0 ;
    j -- ) {
      if ( arr [ j ] > max_var ) {
        max_var = arr [ j ] ;
        pos = j ;
      }
    }
    if ( max_var > arr [ i ] ) {
      int j = pos ;
      while ( j < k - 1 ) {
        arr [ j ] = arr [ j + 1 ] ;
        j ++ ;
      }
      arr [ k - 1 ] = arr [ i ] ;
    }
  }
  for ( int i = 0 ;
  i < k ;
  i ++ ) System . out . print ( arr [ i ] + " " ) ;
}
|||

NTH_NON_FIBONACCI_NUMBER

static int nonFibonacci ( int n ) {
  int prevPrev = 1 , prev = 2 , curr = 3 ;
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

static int search ( int arr [ ] , int n , int x ) {
  int i ;
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] == x ) {
      return i ;
    }
  }
  return - 1 ;
}
|||

ZECKENDORFS_THEOREM_NON_NEIGHBOURING_FIBONACCI_REPRESENTATION

public static int nearestSmallerEqFib ( int n ) {
  if ( n == 0 || n == 1 ) return n ;
  int f1 = 0 , f2 = 1 , f3 = 1 ;
  while ( f3 <= n ) {
    f1 = f2 ;
    f2 = f3 ;
    f3 = f1 + f2 ;
  }
  return f2 ;
}
|||

PRINT_MAXIMUM_SHORTEST_DISTANCE

static int find_maximum ( int a [ ] , int n , int k ) {
  HashMap < Integer , Integer > b = new HashMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int x = a [ i ] ;
    int d = Math . min ( 1 + i , n - i ) ;
    if ( ! b . containsKey ( x ) ) b . put ( x , d ) ;
    else {
      b . put ( x , Math . min ( d , b . get ( x ) ) ) ;
    }
  }
  int ans = Integer . MAX_VALUE ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int x = a [ i ] ;
    if ( x != k - x && b . containsKey ( k - x ) ) ans = Math . min ( Math . max ( b . get ( x ) , b . get ( k - x ) ) , ans ) ;
  }
  return ans ;
}
|||

GENERATING_DISTINCT_SUBSEQUENCES_OF_A_GIVEN_STRING_IN_LEXICOGRAPHIC_ORDER

static void generate ( Set < String > st , String s ) {
  if ( s . length ( ) == 0 ) {
    return ;
  }
  if ( ! st . contains ( s ) ) {
    st . add ( s ) ;
    for ( int i = 0 ;
    i < s . length ( ) ;
    i ++ ) {
      String t = s ;
      t = t . substring ( 0 , i ) + t . substring ( i + 1 ) ;
      generate ( st , t ) ;
    }
  }
  return ;
}
|||

WRITE_YOU_OWN_POWER_WITHOUT_USING_MULTIPLICATION_AND_DIVISION

static int pow ( int a , int b ) {
  if ( b == 0 ) return 1 ;
  int answer = a ;
  int increment = a ;
  int i , j ;
  for ( i = 1 ;
  i < b ;
  i ++ ) {
    for ( j = 1 ;
    j < a ;
    j ++ ) {
      answer += increment ;
    }
    increment = answer ;
  }
  return answer ;
}
|||

MAXIMIZE_VOLUME_CUBOID_GIVEN_SUM_SIDES_1

static int maxvolume ( int s ) {
  int length = s / 3 ;
  s -= length ;
  int breadth = s / 2 ;
  int height = s - breadth ;
  return length * breadth * height ;
}
|||

HORNERS_METHOD_POLYNOMIAL_EVALUATION

static int horner ( int poly [ ] , int n , int x ) {
  int result = poly [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) result = result * x + poly [ i ] ;
  return result ;
}
|||

MINIMUM_TIME_REQUIRED_PRODUCE_M_ITEMS

static int minTime ( int [ ] arr , int n , int m ) {
  int t = 0 ;
  while ( true ) {
    int items = 0 ;
    for ( int i = 0 ;
    i < n ;
    i ++ ) items += ( t / arr [ i ] ) ;
    if ( items >= m ) return t ;
    t ++ ;
  }
}
|||

FIND_DIFFERENCE_BETWEEN_SUMS_OF_TWO_DIAGONALS

public static int difference ( int arr [ ] [ ] , int n ) {
  int d1 = 0 , d2 = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( i == j ) d1 += arr [ i ] [ j ] ;
      if ( i == n - j - 1 ) d2 += arr [ i ] [ j ] ;
    }
  }
  return Math . abs ( d1 - d2 ) ;
}
|||

SHORTEST_UNCOMMON_SUBSEQUENCE

static int shortestSeq ( char [ ] S , char [ ] T ) {
  int m = S . length , n = T . length ;
  int dp [ ] [ ] = new int [ m + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i <= m ;
  i ++ ) {
    dp [ i ] [ 0 ] = 1 ;
  }
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    dp [ 0 ] [ i ] = MAX ;
  }
  for ( int i = 1 ;
  i <= m ;
  i ++ ) {
    for ( int j = 1 ;
    j <= n ;
    j ++ ) {
      char ch = S [ i - 1 ] ;
      int k ;
      for ( k = j - 1 ;
      k >= 0 ;
      k -- ) {
        if ( T [ k ] == ch ) {
          break ;
        }
      }
      if ( k == - 1 ) {
        dp [ i ] [ j ] = 1 ;
      }
      else {
        dp [ i ] [ j ] = Math . min ( dp [ i - 1 ] [ j ] , dp [ i - 1 ] [ k ] + 1 ) ;
      }
    }
  }
  int ans = dp [ m ] [ n ] ;
  if ( ans >= MAX ) {
    ans = - 1 ;
  }
  return ans ;
}
|||

MIN_FLIPS_OF_CONTINUOUS_CHARACTERS_TO_MAKE_ALL_CHARACTERS_SAME_IN_A_STRING

static int findFlips ( String str , int n ) {
  char last = ' ' ;
  int res = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( last != str . charAt ( i ) ) res ++ ;
    last = str . charAt ( i ) ;
  }
  return res / 2 ;
}
|||

DYNAMIC_PROGRAMMING_SET_28_MINIMUM_INSERTIONS_TO_FORM_A_PALINDROME

static int findMinInsertions ( char str [ ] , int l , int h ) {
  if ( l > h ) return Integer . MAX_VALUE ;
  if ( l == h ) return 0 ;
  if ( l == h - 1 ) return ( str [ l ] == str [ h ] ) ? 0 : 1 ;
  return ( str [ l ] == str [ h ] ) ? findMinInsertions ( str , l + 1 , h - 1 ) : ( Integer . min ( findMinInsertions ( str , l , h - 1 ) , findMinInsertions ( str , l + 1 , h ) ) + 1 ) ;
}
|||

COUNT_CHARACTERS_STRING_DISTANCE_ENGLISH_ALPHABETS

static int countPairs ( String str ) {
  int result = 0 ;
  int n = str . length ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) for ( int j = i + 1 ;
  j < n ;
  j ++ ) if ( Math . abs ( str . charAt ( i ) - str . charAt ( j ) ) == Math . abs ( i - j ) ) result ++ ;
  return result ;
}
|||

MULTISTAGE_GRAPH_SHORTEST_PATH

public static int shortestDist ( int [ ] [ ] graph ) {
  int [ ] dist = new int [ N ] ;
  dist [ N - 1 ] = 0 ;
  for ( int i = N - 2 ;
  i >= 0 ;
  i -- ) {
    dist [ i ] = INF ;
    for ( int j = i ;
    j < N ;
    j ++ ) {
      if ( graph [ i ] [ j ] == INF ) {
        continue ;
      }
      dist [ i ] = Math . min ( dist [ i ] , graph [ i ] [ j ] + dist [ j ] ) ;
    }
  }
  return dist [ 0 ] ;
}
|||

MAXIMUM_SIZE_SUB_MATRIX_WITH_ALL_1S_IN_A_BINARY_MATRIX

static void printMaxSubSquare ( int M [ ] [ ] ) {
  int i , j ;
  int R = M . length ;
  int C = M [ 0 ] . length ;
  int S [ ] [ ] = new int [ R ] [ C ] ;
  int max_of_s , max_i , max_j ;
  for ( i = 0 ;
  i < R ;
  i ++ ) S [ i ] [ 0 ] = M [ i ] [ 0 ] ;
  for ( j = 0 ;
  j < C ;
  j ++ ) S [ 0 ] [ j ] = M [ 0 ] [ j ] ;
  for ( i = 1 ;
  i < R ;
  i ++ ) {
    for ( j = 1 ;
    j < C ;
    j ++ ) {
      if ( M [ i ] [ j ] == 1 ) S [ i ] [ j ] = Math . min ( S [ i ] [ j - 1 ] , Math . min ( S [ i - 1 ] [ j ] , S [ i - 1 ] [ j - 1 ] ) ) + 1 ;
      else S [ i ] [ j ] = 0 ;
    }
  }
  max_of_s = S [ 0 ] [ 0 ] ;
  max_i = 0 ;
  max_j = 0 ;
  for ( i = 0 ;
  i < R ;
  i ++ ) {
    for ( j = 0 ;
    j < C ;
    j ++ ) {
      if ( max_of_s < S [ i ] [ j ] ) {
        max_of_s = S [ i ] [ j ] ;
        max_i = i ;
        max_j = j ;
      }
    }
  }
  System . out . println ( "Maximum size sub-matrix is: " ) ;
  for ( i = max_i ;
  i > max_i - max_of_s ;
  i -- ) {
    for ( j = max_j ;
    j > max_j - max_of_s ;
    j -- ) {
      System . out . print ( M [ i ] [ j ] + " " ) ;
    }
    System . out . println ( ) ;
  }
}
|||

GIVEN_SORTED_ARRAY_NUMBER_X_FIND_PAIR_ARRAY_WHOSE_SUM_CLOSEST_X

static void printClosest ( int arr [ ] , int n , int x ) {
  int res_l = 0 , res_r = 0 ;
  int l = 0 , r = n - 1 , diff = Integer . MAX_VALUE ;
  while ( r > l ) {
    if ( Math . abs ( arr [ l ] + arr [ r ] - x ) < diff ) {
      res_l = l ;
      res_r = r ;
      diff = Math . abs ( arr [ l ] + arr [ r ] - x ) ;
    }
    if ( arr [ l ] + arr [ r ] > x ) r -- ;
    else l ++ ;
  }
  System . out . println ( " The closest pair is " + arr [ res_l ] + " and " + arr [ res_r ] ) ;
}
|||

SORT_1_N_SWAPPING_ADJACENT_ELEMENTS_1

static int sortedAfterSwap ( int [ ] A , int [ ] B , int n ) {
  int t = 0 ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    if ( B [ i ] != 0 ) {
      if ( A [ i ] != i + 1 ) t = A [ i ] ;
      A [ i ] = A [ i + 1 ] ;
      A [ i + 1 ] = t ;
    }
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( A [ i ] != i + 1 ) return 0 ;
  }
  return 1 ;
}
|||

TILE_STACKING_PROBLEM

static int possibleWays ( int n , int m , int k ) {
  int [ ] [ ] dp = new int [ N ] [ N ] ;
  int [ ] [ ] presum = new int [ N ] [ N ] ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    for ( int j = 0 ;
    j < N ;
    j ++ ) {
      dp [ i ] [ j ] = 0 ;
      presum [ i ] [ j ] = 0 ;
    }
  }
  for ( int i = 1 ;
  i < n + 1 ;
  i ++ ) {
    dp [ 0 ] [ i ] = 0 ;
    presum [ 0 ] [ i ] = 1 ;
  }
  for ( int i = 0 ;
  i < m + 1 ;
  i ++ ) {
    presum [ i ] [ 0 ] = dp [ i ] [ 0 ] = 1 ;
  }
  for ( int i = 1 ;
  i < m + 1 ;
  i ++ ) {
    for ( int j = 1 ;
    j < n + 1 ;
    j ++ ) {
      dp [ i ] [ j ] = presum [ i - 1 ] [ j ] ;
      if ( j > k ) {
        dp [ i ] [ j ] -= presum [ i - 1 ] [ j - k - 1 ] ;
      }
    }
    for ( int j = 1 ;
    j < n + 1 ;
    j ++ ) {
      presum [ i ] [ j ] = dp [ i ] [ j ] + presum [ i ] [ j - 1 ] ;
    }
  }
  return dp [ m ] [ n ] ;
}
|||

NUMBER_OF_PAIRS_IN_AN_ARRAY_HAVING_SUM_EQUAL_TO_PRODUCT

static int sumEqualProduct ( int a [ ] , int n ) {
  int zero = 0 , two = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( a [ i ] == 0 ) {
      zero ++ ;
    }
    if ( a [ i ] == 2 ) {
      two ++ ;
    }
  }
  int cnt = ( zero * ( zero - 1 ) ) / 2 + ( two * ( two - 1 ) ) / 2 ;
  return cnt ;
}
|||

DYNAMIC_PROGRAMMING_SET_17_PALINDROME_PARTITIONING

static int minPalPartion ( String str ) {
  int n = str . length ( ) ;
  int [ ] [ ] C = new int [ n ] [ n ] ;
  boolean [ ] [ ] P = new boolean [ n ] [ n ] ;
  int i , j , k , L ;
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    P [ i ] [ i ] = true ;
    C [ i ] [ i ] = 0 ;
  }
  for ( L = 2 ;
  L <= n ;
  L ++ ) {
    for ( i = 0 ;
    i < n - L + 1 ;
    i ++ ) {
      j = i + L - 1 ;
      if ( L == 2 ) P [ i ] [ j ] = ( str . charAt ( i ) == str . charAt ( j ) ) ;
      else P [ i ] [ j ] = ( str . charAt ( i ) == str . charAt ( j ) ) && P [ i + 1 ] [ j - 1 ] ;
      if ( P [ i ] [ j ] == true ) C [ i ] [ j ] = 0 ;
      else {
        C [ i ] [ j ] = Integer . MAX_VALUE ;
        for ( k = i ;
        k <= j - 1 ;
        k ++ ) C [ i ] [ j ] = Integer . min ( C [ i ] [ j ] , C [ i ] [ k ] + C [ k + 1 ] [ j ] + 1 ) ;
      }
    }
  }
  return C [ 0 ] [ n - 1 ] ;
}
|||

FIND_ONE_MULTIPLE_REPEATING_ELEMENTS_READ_ARRAY

static int findRepeatingNumber ( int [ ] arr , int n ) {
  int sq = ( int ) Math . sqrt ( n ) ;
  int range = ( n / sq ) + 1 ;
  int [ ] count = new int [ range ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    count [ ( arr [ i ] - 1 ) / sq ] ++ ;
  }
  int selected_block = range - 1 ;
  for ( int i = 0 ;
  i < range - 1 ;
  i ++ ) {
    if ( count [ i ] > sq ) {
      selected_block = i ;
      break ;
    }
  }
  HashMap < Integer , Integer > m = new HashMap < > ( ) ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( ( ( selected_block * sq ) < arr [ i ] ) && ( arr [ i ] <= ( ( selected_block + 1 ) * sq ) ) ) {
      m . put ( arr [ i ] , 1 ) ;
      if ( m . get ( arr [ i ] ) == 1 ) return arr [ i ] ;
    }
  }
  return - 1 ;
}
|||

MINIMUM_SUM_PATH_TRIANGLE

static int minSumPath ( ) {
  int [ ] memo = new int [ A . length ] ;
  int n = A . length - 1 ;
  for ( int i = 0 ;
  i < A [ n ] . length ;
  i ++ ) memo [ i ] = A [ n ] [ i ] ;
  for ( int i = A . length - 2 ;
  i >= 0 ;
  i -- ) for ( int j = 0 ;
  j < A [ i ] . length ;
  j ++ ) memo [ j ] = A [ i ] [ j ] + ( int ) Math . min ( memo [ j ] , memo [ j + 1 ] ) ;
  return memo [ 0 ] ;
}
|||

HOW_CAN_WE_SUM_THE_DIGITS_OF_A_GIVEN_NUMBER_IN_SINGLE_STATEMENT_1

static int getSum ( int n ) {
  int sum ;
  for ( sum = 0 ;
  n > 0 ;
  sum += n % 10 , n /= 10 ) ;
  return sum ;
}
|||

RECURSION

static void printFun ( int test ) {
  if ( test < 1 ) return ;
  else {
    System . out . printf ( "%d " , test ) ;
    printFun ( test - 1 ) ;
    System . out . printf ( "%d " , test ) ;
    return ;
  }
}
|||

MAXIMUM_TRIPLET_SUM_ARRAY

static int maxTripletSum ( int arr [ ] , int n ) {
  int sum = - 1000000 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) for ( int j = i + 1 ;
  j < n ;
  j ++ ) for ( int k = j + 1 ;
  k < n ;
  k ++ ) if ( sum < arr [ i ] + arr [ j ] + arr [ k ] ) sum = arr [ i ] + arr [ j ] + arr [ k ] ;
  return sum ;
}
|||

MINIMUM_NUMBER_OF_JUMPS_TO_REACH_END_OF_A_GIVEN_ARRAY_1

private static int minJumps ( int [ ] arr , int n ) {
  int jumps [ ] = new int [ n ] ;
  int i , j ;
  if ( n == 0 || arr [ 0 ] == 0 ) return Integer . MAX_VALUE ;
  jumps [ 0 ] = 0 ;
  for ( i = 1 ;
  i < n ;
  i ++ ) {
    jumps [ i ] = Integer . MAX_VALUE ;
    for ( j = 0 ;
    j < i ;
    j ++ ) {
      if ( i <= j + arr [ j ] && jumps [ j ] != Integer . MAX_VALUE ) {
        jumps [ i ] = Math . min ( jumps [ i ] , jumps [ j ] + 1 ) ;
        break ;
      }
    }
  }
  return jumps [ n - 1 ] ;
}
|||

MAXIMIZE_ARRAY_ELEMENTS_UPTO_GIVEN_NUMBER

static int findMaxVal ( int [ ] arr , int n , int num , int maxLimit ) {
  int ind ;
  int val ;
  int [ ] [ ] dp = new int [ n ] [ maxLimit + 1 ] ;
  for ( ind = 0 ;
  ind < n ;
  ind ++ ) {
    for ( val = 0 ;
    val <= maxLimit ;
    val ++ ) {
      if ( ind == 0 ) {
        if ( num - arr [ ind ] == val || num + arr [ ind ] == val ) {
          dp [ ind ] [ val ] = 1 ;
        }
        else {
          dp [ ind ] [ val ] = 0 ;
        }
      }
      else {
        if ( val - arr [ ind ] >= 0 && val + arr [ ind ] <= maxLimit ) {
          if ( dp [ ind - 1 ] [ val - arr [ ind ] ] == 1 || dp [ ind - 1 ] [ val + arr [ ind ] ] == 1 ) dp [ ind ] [ val ] = 1 ;
        }
        else if ( val - arr [ ind ] >= 0 ) {
          dp [ ind ] [ val ] = dp [ ind - 1 ] [ val - arr [ ind ] ] ;
        }
        else if ( val + arr [ ind ] <= maxLimit ) {
          dp [ ind ] [ val ] = dp [ ind - 1 ] [ val + arr [ ind ] ] ;
        }
        else {
          dp [ ind ] [ val ] = 0 ;
        }
      }
    }
  }
  for ( val = maxLimit ;
  val >= 0 ;
  val -- ) {
    if ( dp [ n - 1 ] [ val ] == 1 ) {
      return val ;
    }
  }
  return - 1 ;
}
|||

PROGRAM_FOR_DEADLOCK_FREE_CONDITION_IN_OPERATING_SYSTEM

static int Resources ( int process , int need ) {
  int minResources = 0 ;
  minResources = process * ( need - 1 ) + 1 ;
  return minResources ;
}
|||

NUMBER_DIGITS_PRODUCT_TWO_NUMBERS

static int countDigits ( int a , int b ) {
  int count = 0 ;
  int p = Math . abs ( a * b ) ;
  if ( p == 0 ) return 1 ;
  while ( p > 0 ) {
    count ++ ;
    p = p / 10 ;
  }
  return count ;
}
|||

FLOOR_IN_A_SORTED_ARRAY

static int floorSearch ( int arr [ ] , int n , int x ) {
  if ( x >= arr [ n - 1 ] ) return n - 1 ;
  if ( x < arr [ 0 ] ) return - 1 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) if ( arr [ i ] > x ) return ( i - 1 ) ;
  return - 1 ;
}
|||

CHECK_WHETHER_TRIANGLE_VALID_NOT_SIDES_GIVEN

public static int checkValidity ( int a , int b , int c ) {
  if ( a + b <= c || a + c <= b || b + c <= a ) return 0 ;
  else return 1 ;
}
|||

PRINT_N_X_N_SPIRAL_MATRIX_USING_O1_EXTRA_SPACE

static void printSpiral ( int n ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      int x ;
      x = Math . min ( Math . min ( i , j ) , Math . min ( n - 1 - i , n - 1 - j ) ) ;
      if ( i <= j ) System . out . print ( ( n - 2 * x ) * ( n - 2 * x ) - ( i - x ) - ( j - x ) + "\t" ) ;
      else System . out . print ( ( n - 2 * x - 2 ) * ( n - 2 * x - 2 ) + ( i - x ) + ( j - x ) + "\t" ) ;
    }
    System . out . println ( ) ;
  }
}
|||

POSITION_ELEMENT_STABLE_SORT

static int getIndexInSortedArray ( int arr [ ] , int n , int idx ) {
  int result = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] < arr [ idx ] ) result ++ ;
    if ( arr [ i ] == arr [ idx ] && i < idx ) result ++ ;
  }
  return result ;
}
|||

MAXIMUM_SEGMENT_VALUE_PUTTING_K_BREAKPOINTS_NUMBER

static int findMaxSegment ( String s , int k ) {
  int seg_len = s . length ( ) - k ;
  int res = 0 ;
  for ( int i = 0 ;
  i < seg_len ;
  i ++ ) res = res * 10 + ( s . charAt ( i ) - '0' ) ;
  int seg_len_pow = ( int ) Math . pow ( 10 , seg_len - 1 ) ;
  int curr_val = res ;
  for ( int i = 1 ;
  i <= ( s . length ( ) - seg_len ) ;
  i ++ ) {
    curr_val = curr_val - ( s . charAt ( i - 1 ) - '0' ) * seg_len_pow ;
    curr_val = curr_val * 10 + ( s . charAt ( i + seg_len - 1 ) - '0' ) ;
    res = Math . max ( res , curr_val ) ;
  }
  return res ;
}
|||

FINDING_POWER_PRIME_NUMBER_P_N_1

static int PowerOFPINnfactorial ( int n , int p ) {
  int ans = 0 ;
  int temp = p ;
  while ( temp <= n ) {
    ans += n / temp ;
    temp = temp * p ;
  }
  return ans ;
}
|||

PROGRAM_PRINT_IDENTITY_MATRIX

static int identity ( int num ) {
  int row , col ;
  for ( row = 0 ;
  row < num ;
  row ++ ) {
    for ( col = 0 ;
    col < num ;
    col ++ ) {
      if ( row == col ) System . out . print ( 1 + " " ) ;
      else System . out . print ( 0 + " " ) ;
    }
    System . out . println ( ) ;
  }
  return 0 ;
}
|||

SUM_MATRIX_ELEMENT_ELEMENT_INTEGER_DIVISION_ROW_COLUMN

static int findSum ( int n ) {
  int ans = 0 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) for ( int j = 1 ;
  j <= n ;
  j ++ ) ans += ( i / j ) ;
  return ans ;
}
|||

TILING_WITH_DOMINOES

static int countWays ( int n ) {
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

static int countDer ( int n ) {
  if ( n == 1 ) return 0 ;
  if ( n == 0 ) return 1 ;
  if ( n == 2 ) return 1 ;
  return ( n - 1 ) * ( countDer ( n - 1 ) + countDer ( n - 2 ) ) ;
}
|||

FREQUENCY_ELEMENT_UNSORTED_ARRAY_1

static void countFreq ( int a [ ] , int n ) {
  int hm [ ] = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) hm [ a [ i ] ] ++ ;
  int cumul = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    cumul += hm [ a [ i ] ] ;
    if ( hm [ a [ i ] ] != 0 ) {
      System . out . println ( a [ i ] + "->" + cumul ) ;
    }
    hm [ a [ i ] ] = 0 ;
  }
}
|||

MINIMIZE_THE_SUM_OF_DIGITS_OF_A_AND_B_SUCH_THAT_A_B_N

static int minSum ( int n ) {
  int sum = 0 ;
  while ( n > 0 ) {
    sum += ( n % 10 ) ;
    n /= 10 ;
  }
  if ( sum == 1 ) return 10 ;
  return sum ;
}
|||

DIVIDE_CUBOID_CUBES_SUM_VOLUMES_MAXIMUM

static void maximizecube ( int l , int b , int h ) {
  int side = gcd ( l , gcd ( b , h ) ) ;
  int num = l / side ;
  num = ( num * b / side ) ;
  num = ( num * h / side ) ;
  System . out . println ( side + " " + num ) ;
}
|||

CHECK_NUMBER_POWER_K_USING_BASE_CHANGING_METHOD

static boolean isPowerOfK ( int n , int k ) {
  boolean oneSeen = false ;
  while ( n > 0 ) {
    int digit = n % k ;
    if ( digit > 1 ) return false ;
    if ( digit == 1 ) {
      if ( oneSeen ) return false ;
      oneSeen = true ;
    }
    n /= k ;
  }
  return true ;
}
|||

POSITION_OF_RIGHTMOST_SET_BIT_1

static int PositionRightmostSetbit ( int n ) {
  int position = 1 ;
  int m = 1 ;
  while ( ( n & m ) == 0 ) {
    m = m << 1 ;
    position ++ ;
  }
  return position ;
}
|||

SEARCH_INSERT_AND_DELETE_IN_A_SORTED_ARRAY_1

static int insertSorted ( int arr [ ] , int n , int key , int capacity ) {
  if ( n >= capacity ) return n ;
  int i ;
  for ( i = n - 1 ;
  ( i >= 0 && arr [ i ] > key ) ;
  i -- ) arr [ i + 1 ] = arr [ i ] ;
  arr [ i + 1 ] = key ;
  return ( n + 1 ) ;
}
|||

FIND_THE_MAXIMUM_OF_MINIMUMS_FOR_EVERY_WINDOW_SIZE_IN_A_GIVEN_ARRAY_1

static void printMaxOfMin ( int n ) {
  Stack < Integer > s = new Stack < > ( ) ;
  int left [ ] = new int [ n + 1 ] ;
  int right [ ] = new int [ n + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    left [ i ] = - 1 ;
    right [ i ] = n ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    while ( ! s . empty ( ) && arr [ s . peek ( ) ] >= arr [ i ] ) s . pop ( ) ;
    if ( ! s . empty ( ) ) left [ i ] = s . peek ( ) ;
    s . push ( i ) ;
  }
  while ( ! s . empty ( ) ) s . pop ( ) ;
  for ( int i = n - 1 ;
  i >= 0 ;
  i -- ) {
    while ( ! s . empty ( ) && arr [ s . peek ( ) ] >= arr [ i ] ) s . pop ( ) ;
    if ( ! s . empty ( ) ) right [ i ] = s . peek ( ) ;
    s . push ( i ) ;
  }
  int ans [ ] = new int [ n + 1 ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) ans [ i ] = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int len = right [ i ] - left [ i ] - 1 ;
    ans [ len ] = Math . max ( ans [ len ] , arr [ i ] ) ;
  }
  for ( int i = n - 1 ;
  i >= 1 ;
  i -- ) ans [ i ] = Math . max ( ans [ i ] , ans [ i + 1 ] ) ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) System . out . print ( ans [ i ] + " " ) ;
}
|||

MAXIMUM_DECIMAL_VALUE_PATH_IN_A_BINARY_MATRIX_1

static int MaximumDecimalValue ( int mat [ ] [ ] , int n ) {
  int dp [ ] [ ] = new int [ n ] [ n ] ;
  if ( mat [ 0 ] [ 0 ] == 1 ) {
    dp [ 0 ] [ 0 ] = 1 ;
  }
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( mat [ 0 ] [ i ] == 1 ) {
      dp [ 0 ] [ i ] = ( int ) ( dp [ 0 ] [ i - 1 ] + Math . pow ( 2 , i ) ) ;
    }
    else {
      dp [ 0 ] [ i ] = dp [ 0 ] [ i - 1 ] ;
    }
  }
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( mat [ i ] [ 0 ] == 1 ) {
      dp [ i ] [ 0 ] = ( int ) ( dp [ i - 1 ] [ 0 ] + Math . pow ( 2 , i ) ) ;
    }
    else {
      dp [ i ] [ 0 ] = dp [ i - 1 ] [ 0 ] ;
    }
  }
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    for ( int j = 1 ;
    j < n ;
    j ++ ) {
      if ( mat [ i ] [ j ] == 1 ) {
        dp [ i ] [ j ] = ( int ) ( Math . max ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] ) + Math . pow ( 2 , i + j ) ) ;
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

static int printCountRec ( int dist ) {
  if ( dist < 0 ) return 0 ;
  if ( dist == 0 ) return 1 ;
  return printCountRec ( dist - 1 ) + printCountRec ( dist - 2 ) + printCountRec ( dist - 3 ) ;
}
|||

MOVE_VE_ELEMENTS_END_ORDER_EXTRA_SPACE_ALLOWED

static void segregateElements ( int arr [ ] , int n ) {
  int temp [ ] = new int [ n ] ;
  int j = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( arr [ i ] >= 0 ) temp [ j ++ ] = arr [ i ] ;
  if ( j == n || j == 0 ) return ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( arr [ i ] < 0 ) temp [ j ++ ] = arr [ i ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) arr [ i ] = temp [ i ] ;
}
|||

MINIMUM_PERIMETER_N_BLOCKS

public static long minPerimeter ( int n ) {
  int l = ( int ) Math . sqrt ( n ) ;
  int sq = l * l ;
  if ( sq == n ) return l * 4 ;
  else {
    long row = n / l ;
    long perimeter = 2 * ( l + row ) ;
    if ( n % l != 0 ) perimeter += 2 ;
    return perimeter ;
  }
}
|||

DYNAMIC_PROGRAMMING_SET_36_CUT_A_ROPE_TO_MAXIMIZE_PRODUCT

static int maxProd ( int n ) {
  if ( n == 0 || n == 1 ) return 0 ;
  int max_val = 0 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) max_val = Math . max ( max_val , Math . max ( i * ( n - i ) , maxProd ( n - i ) * i ) ) ;
  return max_val ;
}
|||

LONGEST_COMMON_SUBSTRING_SPACE_OPTIMIZED_DP_SOLUTION

static int LCSubStr ( String X , String Y ) {
  int m = X . length ( ) ;
  int n = Y . length ( ) ;
  int result = 0 ;
  int [ ] [ ] len = new int [ 2 ] [ n ] ;
  int currRow = 0 ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( i == 0 || j == 0 ) {
        len [ currRow ] [ j ] = 0 ;
      }
      else if ( X . charAt ( i - 1 ) == Y . charAt ( j - 1 ) ) {
        len [ currRow ] [ j ] = len [ ( 1 - currRow ) ] [ ( j - 1 ) ] + 1 ;
        result = Math . max ( result , len [ currRow ] [ j ] ) ;
      }
      else {
        len [ currRow ] [ j ] = 0 ;
      }
    }
    currRow = 1 - currRow ;
  }
  return result ;
}
|||

CHECK_GIVEN_STRING_ROTATION_PALINDROME

static boolean isPalindrome ( String str ) {
  int l = 0 ;
  int h = str . length ( ) - 1 ;
  while ( h > l ) if ( str . charAt ( l ++ ) != str . charAt ( h -- ) ) return false ;
  return true ;
}
|||

FIND_NUMBER_OF_SOLUTIONS_OF_A_LINEAR_EQUATION_OF_N_VARIABLES_1

static int countSol ( int coeff [ ] , int n , int rhs ) {
  int dp [ ] = new int [ rhs + 1 ] ;
  Arrays . fill ( dp , 0 ) ;
  dp [ 0 ] = 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) for ( int j = coeff [ i ] ;
  j <= rhs ;
  j ++ ) dp [ j ] += dp [ j - coeff [ i ] ] ;
  return dp [ rhs ] ;
}
|||

FIND_THE_LARGEST_PAIR_SUM_IN_AN_UNSORTED_ARRAY

static int findLargestSumPair ( ) {
  int first , second ;
  if ( arr [ 0 ] > arr [ 1 ] ) {
    first = arr [ 0 ] ;
    second = arr [ 1 ] ;
  }
  else {
    first = arr [ 1 ] ;
    second = arr [ 0 ] ;
  }
  for ( int i = 2 ;
  i < arr . length ;
  i ++ ) {
    if ( arr [ i ] > first ) {
      second = first ;
      first = arr [ i ] ;
    }
    else if ( arr [ i ] > second && arr [ i ] != first ) second = arr [ i ] ;
  }
  return ( first + second ) ;
}
|||

FIND_BITONIC_POINT_GIVEN_BITONIC_SEQUENCE

static int binarySearch ( int arr [ ] , int left , int right ) {
  if ( left <= right ) {
    int mid = ( left + right ) / 2 ;
    if ( arr [ mid - 1 ] < arr [ mid ] && arr [ mid ] > arr [ mid + 1 ] ) return mid ;
    if ( arr [ mid ] < arr [ mid + 1 ] ) return binarySearch ( arr , mid + 1 , right ) ;
    else return binarySearch ( arr , left , mid - 1 ) ;
  }
  return - 1 ;
}
|||

PRINT_ALL_DISTINCT_CHARACTERS_OF_A_STRING_IN_ORDER_3_METHODS_1

static void printDistinct ( String str ) {
  int n = str . length ( ) ;
  int [ ] count = new int [ MAX_CHAR ] ;
  int [ ] index = new int [ MAX_CHAR ] ;
  for ( int i = 0 ;
  i < MAX_CHAR ;
  i ++ ) {
    count [ i ] = 0 ;
    index [ i ] = n ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    char x = str . charAt ( i ) ;
    ++ count [ x ] ;
    if ( count [ x ] == 1 && x != ' ' ) index [ x ] = i ;
    if ( count [ x ] == 2 ) index [ x ] = n ;
  }
  Arrays . sort ( index ) ;
  for ( int i = 0 ;
  i < MAX_CHAR && index [ i ] != n ;
  i ++ ) System . out . print ( str . charAt ( index [ i ] ) ) ;
}
|||

FIND_TWO_SIDES_RIGHT_ANGLE_TRIANGLE

static void printOtherSides ( int n ) {
  if ( n % 2 != 0 ) {
    if ( n == 1 ) System . out . println ( "-1" ) ;
    else {
      int b = ( n * n - 1 ) / 2 ;
      int c = ( n * n + 1 ) / 2 ;
      System . out . println ( "b = " + b + ", c = " + c ) ;
    }
  }
  else {
    if ( n == 2 ) System . out . println ( "-1" ) ;
    else {
      int b = n * n / 4 - 1 ;
      int c = n * n / 4 + 1 ;
      System . out . println ( "b = " + b + ", c = " + c ) ;
    }
  }
}
|||

COUNT_NUMBER_OF_STRINGS_MADE_OF_R_G_AND_B_USING_GIVEN_COMBINATION

static int possibleStrings ( int n , int r , int b , int g ) {
  int fact [ ] = new int [ n + 1 ] ;
  fact [ 0 ] = 1 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) fact [ i ] = fact [ i - 1 ] * i ;
  int left = n - ( r + g + b ) ;
  int sum = 0 ;
  for ( int i = 0 ;
  i <= left ;
  i ++ ) {
    for ( int j = 0 ;
    j <= left - i ;
    j ++ ) {
      int k = left - ( i + j ) ;
      sum = sum + fact [ n ] / ( fact [ i + r ] * fact [ j + b ] * fact [ k + g ] ) ;
    }
  }
  return sum ;
}
|||

REARRANGE_ARRAY_MAXIMUM_MINIMUM_FORM_SET_2_O1_EXTRA_SPACE_1

public static void rearrange ( int arr [ ] , int n ) {
  int max_ele = arr [ n - 1 ] ;
  int min_ele = arr [ 0 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( i % 2 == 0 ) {
      arr [ i ] = max_ele ;
      max_ele -= 1 ;
    }
    else {
      arr [ i ] = min_ele ;
      min_ele += 1 ;
    }
  }
}
|||

EVALUATE_AN_ARRAY_EXPRESSION_WITH_NUMBERS_AND

public static int calculateSum ( String arr [ ] , int n ) {
  if ( n == 0 ) return 0 ;
  String s = arr [ 0 ] ;
  int value = Integer . parseInt ( s ) ;
  int sum = value ;
  for ( int i = 2 ;
  i < n ;
  i = i + 2 ) {
    s = arr [ i ] ;
    value = Integer . parseInt ( s ) ;
    char operation = arr [ i - 1 ] . charAt ( 0 ) ;
    if ( operation == '+' ) sum += value ;
    else sum -= value ;
  }
  return sum ;
}
|||

SUM_MATRIX_ELEMENT_ELEMENT_INTEGER_DIVISION_ROW_COLUMN_1

static int findSum ( int n ) {
  int ans = 0 , temp = 0 , num ;
  for ( int i = 1 ;
  i <= n && temp < n ;
  i ++ ) {
    temp = i - 1 ;
    num = 1 ;
    while ( temp < n ) {
      if ( temp + i <= n ) ans += ( i * num ) ;
      else ans += ( ( n - temp ) * num ) ;
      temp += i ;
      num ++ ;
    }
  }
  return ans ;
}
|||

SHUFFLE_A_DECK_OF_CARDS_3

public static void shuffle ( int card [ ] , int n ) {
  Random rand = new Random ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int r = i + rand . nextInt ( 52 - i ) ;
    int temp = card [ r ] ;
    card [ r ] = card [ i ] ;
    card [ i ] = temp ;
  }
}
|||

DOOLITTLE_ALGORITHM_LU_DECOMPOSITION

static void luDecomposition ( int [ ] [ ] mat , int n ) {
  int [ ] [ ] lower = new int [ n ] [ n ] ;
  int [ ] [ ] upper = new int [ n ] [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int k = i ;
    k < n ;
    k ++ ) {
      int sum = 0 ;
      for ( int j = 0 ;
      j < i ;
      j ++ ) sum += ( lower [ i ] [ j ] * upper [ j ] [ k ] ) ;
      upper [ i ] [ k ] = mat [ i ] [ k ] - sum ;
    }
    for ( int k = i ;
    k < n ;
    k ++ ) {
      if ( i == k ) lower [ i ] [ i ] = 1 ;
      else {
        int sum = 0 ;
        for ( int j = 0 ;
        j < i ;
        j ++ ) sum += ( lower [ k ] [ j ] * upper [ j ] [ i ] ) ;
        lower [ k ] [ i ] = ( mat [ k ] [ i ] - sum ) / upper [ i ] [ i ] ;
      }
    }
  }
  System . out . println ( setw ( 2 ) + "     Lower Triangular" + setw ( 10 ) + "Upper Triangular" ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) System . out . print ( setw ( 4 ) + lower [ i ] [ j ] + "\t" ) ;
    System . out . print ( "\t" ) ;
    for ( int j = 0 ;
    j < n ;
    j ++ ) System . out . print ( setw ( 4 ) + upper [ i ] [ j ] + "\t" ) ;
    System . out . print ( "\n" ) ;
  }
}
|||

PROGRAM_NTH_CATALAN_NUMBER

int catalan ( int n ) {
  int res = 0 ;
  if ( n <= 1 ) {
    return 1 ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    res += catalan ( i ) * catalan ( n - i - 1 ) ;
  }
  return res ;
}
|||

NUMBER_DIGITS_REMOVED_MAKE_NUMBER_DIVISIBLE_3

static int divisible ( String num ) {
  int n = num . length ( ) ;
  int sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) sum += ( int ) ( num . charAt ( i ) ) ;
  if ( sum % 3 == 0 ) return 0 ;
  if ( n == 1 ) return - 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( sum % 3 == ( num . charAt ( i ) - '0' ) % 3 ) return 1 ;
  if ( n == 2 ) return - 1 ;
  return 2 ;
}
|||

CHECK_IF_A_NUMBER_IS_POWER_OF_ANOTHER_NUMBER_1

static boolean isPower ( int x , int y ) {
  int res1 = ( int ) Math . log ( y ) / ( int ) Math . log ( x ) ;
  double res2 = Math . log ( y ) / Math . log ( x ) ;
  return ( res1 == res2 ) ;
}
|||

LARGEST_SUBSEQUENCE_GCD_GREATER_1

static int largestGCDSubsequence ( int arr [ ] , int n ) {
  int ans = 0 ;
  int maxele = Arrays . stream ( arr ) . max ( ) . getAsInt ( ) ;
  ;
  for ( int i = 2 ;
  i <= maxele ;
  ++ i ) {
    int count = 0 ;
    for ( int j = 0 ;
    j < n ;
    ++ j ) {
      if ( arr [ j ] % i == 0 ) ++ count ;
    }
    ans = Math . max ( ans , count ) ;
  }
  return ans ;
}
|||

FIND_COMMON_ELEMENT_ROWS_ROW_WISE_SORTED_MATRIX

static int findCommon ( int mat [ ] [ ] ) {
  int column [ ] = new int [ M ] ;
  int min_row ;
  int i ;
  for ( i = 0 ;
  i < M ;
  i ++ ) column [ i ] = N - 1 ;
  min_row = 0 ;
  while ( column [ min_row ] >= 0 ) {
    for ( i = 0 ;
    i < M ;
    i ++ ) {
      if ( mat [ i ] [ column [ i ] ] < mat [ min_row ] [ column [ min_row ] ] ) min_row = i ;
    }
    int eq_count = 0 ;
    for ( i = 0 ;
    i < M ;
    i ++ ) {
      if ( mat [ i ] [ column [ i ] ] > mat [ min_row ] [ column [ min_row ] ] ) {
        if ( column [ i ] == 0 ) return - 1 ;
        column [ i ] -= 1 ;
      }
      else eq_count ++ ;
    }
    if ( eq_count == M ) return mat [ min_row ] [ column [ min_row ] ] ;
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

static int countSetBits ( int n ) {
  int i = 0 ;
  int ans = 0 ;
  while ( ( 1 << i ) <= n ) {
    boolean k = false ;
    int change = 1 << i ;
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      if ( k == true ) ans += 1 ;
      else ans += 0 ;
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

static int findLongestRepeatingSubSeq ( String str ) {
  int n = str . length ( ) ;
  int [ ] [ ] dp = new int [ n + 1 ] [ n + 1 ] ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int j = 1 ;
    j <= n ;
    j ++ ) {
      if ( str . charAt ( i - 1 ) == str . charAt ( j - 1 ) && i != j ) dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ] ;
      else dp [ i ] [ j ] = Math . max ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] ) ;
    }
  }
  return dp [ n ] [ n ] ;
}
|||

FIND_THE_FIRST_MISSING_NUMBER

int findFirstMissing ( int array [ ] , int start , int end ) {
  if ( start > end ) return end + 1 ;
  if ( start != array [ start ] ) return start ;
  int mid = ( start + end ) / 2 ;
  if ( array [ mid ] == mid ) return findFirstMissing ( array , mid + 1 , end ) ;
  return findFirstMissing ( array , start , mid ) ;
}
|||

SORT_ARRAY_CONVERTING_ELEMENTS_SQUARES_1

public static void sortSquares ( int arr [ ] ) {
  int n = arr . length ;
  int k ;
  for ( k = 0 ;
  k < n ;
  k ++ ) {
    if ( arr [ k ] >= 0 ) break ;
  }
  int i = k - 1 ;
  int j = k ;
  int ind = 0 ;
  int [ ] temp = new int [ n ] ;
  while ( i >= 0 && j < n ) {
    if ( arr [ i ] * arr [ i ] < arr [ j ] * arr [ j ] ) {
      temp [ ind ] = arr [ i ] * arr [ i ] ;
      i -- ;
    }
    else {
      temp [ ind ] = arr [ j ] * arr [ j ] ;
      j ++ ;
    }
    ind ++ ;
  }
  while ( i >= 0 ) {
    temp [ ind ++ ] = arr [ i ] * arr [ i ] ;
    i -- ;
  }
  while ( j < n ) {
    temp [ ind ++ ] = arr [ j ] * arr [ j ] ;
    j ++ ;
  }
  for ( int x = 0 ;
  x < n ;
  x ++ ) arr [ x ] = temp [ x ] ;
}
|||

PROGRAM_TO_FIND_REMAINDER_WITHOUT_USING_MODULO_OR_OPERATOR

static int getRemainder ( int num , int divisor ) {
  return ( num - divisor * ( num / divisor ) ) ;
}
|||

MINIMUM_COST_TO_FILL_GIVEN_WEIGHT_IN_A_BAG

public static int MinimumCost ( int cost [ ] , int n , int W ) {
  Vector < Integer > val = new Vector < Integer > ( ) ;
  Vector < Integer > wt = new Vector < Integer > ( ) ;
  int size = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( cost [ i ] != - 1 ) {
      val . add ( cost [ i ] ) ;
      wt . add ( i + 1 ) ;
      size ++ ;
    }
  }
  n = size ;
  int min_cost [ ] [ ] = new int [ n + 1 ] [ W + 1 ] ;
  for ( int i = 0 ;
  i <= W ;
  i ++ ) min_cost [ 0 ] [ i ] = Integer . MAX_VALUE ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) min_cost [ i ] [ 0 ] = 0 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int j = 1 ;
    j <= W ;
    j ++ ) {
      if ( wt . get ( i - 1 ) > j ) min_cost [ i ] [ j ] = min_cost [ i - 1 ] [ j ] ;
      else min_cost [ i ] [ j ] = Math . min ( min_cost [ i - 1 ] [ j ] , min_cost [ i ] [ j - wt . get ( i - 1 ) ] + val . get ( i - 1 ) ) ;
    }
  }
  return ( min_cost [ n ] [ W ] == Integer . MAX_VALUE ) ? - 1 : min_cost [ n ] [ W ] ;
}
|||

COUNT_CHARACTERS_STRING_DISTANCE_ENGLISH_ALPHABETS_1

static int countPairs ( String str ) {
  int result = 0 ;
  int n = str . length ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) for ( int j = 1 ;
  ( i + j ) < n && j <= MAX_CHAR ;
  j ++ ) if ( ( Math . abs ( str . charAt ( i + j ) - str . charAt ( i ) ) == j ) ) result ++ ;
  return result ;
}
|||

A_PRODUCT_ARRAY_PUZZLE

void productArray ( int arr [ ] , int n ) {
  if ( n == 1 ) {
    System . out . print ( 0 ) ;
    return ;
  }
  int left [ ] = new int [ n ] ;
  int right [ ] = new int [ n ] ;
  int prod [ ] = new int [ n ] ;
  int i , j ;
  left [ 0 ] = 1 ;
  right [ n - 1 ] = 1 ;
  for ( i = 1 ;
  i < n ;
  i ++ ) left [ i ] = arr [ i - 1 ] * left [ i - 1 ] ;
  for ( j = n - 2 ;
  j >= 0 ;
  j -- ) right [ j ] = arr [ j + 1 ] * right [ j + 1 ] ;
  for ( i = 0 ;
  i < n ;
  i ++ ) prod [ i ] = left [ i ] * right [ i ] ;
  for ( i = 0 ;
  i < n ;
  i ++ ) System . out . print ( prod [ i ] + " " ) ;
  return ;
}
|||

FREQUENT_ELEMENT_ARRAY_1

static int mostFrequent ( int arr [ ] , int n ) {
  Map < Integer , Integer > hp = new HashMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int key = arr [ i ] ;
    if ( hp . containsKey ( key ) ) {
      int freq = hp . get ( key ) ;
      freq ++ ;
      hp . put ( key , freq ) ;
    }
    else {
      hp . put ( key , 1 ) ;
    }
  }
  int max_count = 0 , res = - 1 ;
  for ( Entry < Integer , Integer > val : hp . entrySet ( ) ) {
    if ( max_count < val . getValue ( ) ) {
      res = val . getKey ( ) ;
      max_count = val . getValue ( ) ;
    }
  }
  return res ;
}
|||

PRINT_UNIQUE_ROWS

public static void printArray ( int arr [ ] [ ] , int row , int col ) {
  HashSet < String > set = new HashSet < String > ( ) ;
  for ( int i = 0 ;
  i < row ;
  i ++ ) {
    String s = "" ;
    for ( int j = 0 ;
    j < col ;
    j ++ ) s += String . valueOf ( arr [ i ] [ j ] ) ;
    if ( ! set . contains ( s ) ) {
      set . add ( s ) ;
      System . out . println ( s ) ;
    }
  }
}
|||

COUNT_1S_SORTED_BINARY_ARRAY

int countOnes ( int arr [ ] , int low , int high ) {
  if ( high >= low ) {
    int mid = low + ( high - low ) / 2 ;
    if ( ( mid == high || arr [ mid + 1 ] == 0 ) && ( arr [ mid ] == 1 ) ) return mid + 1 ;
    if ( arr [ mid ] == 1 ) return countOnes ( arr , ( mid + 1 ) , high ) ;
    return countOnes ( arr , low , ( mid - 1 ) ) ;
  }
  return 0 ;
}
|||

POSSIBLE_MOVES_KNIGHT

static int findPossibleMoves ( int mat [ ] [ ] , int p , int q ) {
  int X [ ] = {
    2 , 1 , - 1 , - 2 , - 2 , - 1 , 1 , 2 };
    int Y [ ] = {
      1 , 2 , 2 , 1 , - 1 , - 2 , - 2 , - 1 };
      int count = 0 ;
      for ( int i = 0 ;
      i < 8 ;
      i ++ ) {
        int x = p + X [ i ] ;
        int y = q + Y [ i ] ;
        if ( x >= 0 && y >= 0 && x < n && y < m && mat [ x ] [ y ] == 0 ) count ++ ;
      }
      return count ;
    }
    |||

ROTATE_MATRIX_ELEMENTS

static void rotatematrix ( int m , int n , int mat [ ] [ ] ) {
  int row = 0 , col = 0 ;
  int prev , curr ;
  while ( row < m && col < n ) {
    if ( row + 1 == m || col + 1 == n ) break ;
    prev = mat [ row + 1 ] [ col ] ;
    for ( int i = col ;
    i < n ;
    i ++ ) {
      curr = mat [ row ] [ i ] ;
      mat [ row ] [ i ] = prev ;
      prev = curr ;
    }
    row ++ ;
    for ( int i = row ;
    i < m ;
    i ++ ) {
      curr = mat [ i ] [ n - 1 ] ;
      mat [ i ] [ n - 1 ] = prev ;
      prev = curr ;
    }
    n -- ;
    if ( row < m ) {
      for ( int i = n - 1 ;
      i >= col ;
      i -- ) {
        curr = mat [ m - 1 ] [ i ] ;
        mat [ m - 1 ] [ i ] = prev ;
        prev = curr ;
      }
    }
    m -- ;
    if ( col < n ) {
      for ( int i = m - 1 ;
      i >= row ;
      i -- ) {
        curr = mat [ i ] [ col ] ;
        mat [ i ] [ col ] = prev ;
        prev = curr ;
      }
    }
    col ++ ;
  }
  for ( int i = 0 ;
  i < R ;
  i ++ ) {
    for ( int j = 0 ;
    j < C ;
    j ++ ) System . out . print ( mat [ i ] [ j ] + " " ) ;
    System . out . print ( "\n" ) ;
  }
}
|||

FIND_KTH_CHARACTER_OF_DECRYPTED_STRING

static char encodedChar ( String str , int k ) {
  String expand = "" ;
  String temp = "" ;
  int freq = 0 ;
  for ( int i = 0 ;
  i < str . length ( ) ;
  ) {
    temp = "" ;
    freq = 0 ;
    while ( i < str . length ( ) && str . charAt ( i ) >= 'a' && str . charAt ( i ) <= 'z' ) {
      temp += str . charAt ( i ) ;
      i ++ ;
    }
    while ( i < str . length ( ) && str . charAt ( i ) >= '1' && str . charAt ( i ) <= '9' ) {
      freq = freq * 10 + str . charAt ( i ) - '0' ;
      i ++ ;
    }
    for ( int j = 1 ;
    j <= freq ;
    j ++ ) expand += temp ;
  }
  if ( freq == 0 ) expand += temp ;
  return expand . charAt ( k - 1 ) ;
}
|||

EFFICIENT_SEARCH_IN_AN_ARRAY_WHERE_DIFFERENCE_BETWEEN_ADJACENT_IS_1

static int search ( int arr [ ] , int n , int x ) {
  int i = 0 ;
  while ( i <= n - 1 ) {
    if ( arr [ i ] == x ) return i ;
    i += Math . abs ( arr [ i ] - x ) ;
  }
  return - 1 ;
}
|||

MAXIMUM_POSSIBLE_SUM_WINDOW_ARRAY_ELEMENTS_WINDOW_ARRAY_UNIQUE

static int returnMaxSum ( int A [ ] , int B [ ] , int n ) {
  Set < Integer > mp = new HashSet < Integer > ( ) ;
  int result = 0 ;
  int curr_sum = 0 , curr_begin = 0 ;
  for ( int i = 0 ;
  i < n ;
  ++ i ) {
    while ( mp . contains ( A [ i ] ) ) {
      mp . remove ( A [ curr_begin ] ) ;
      curr_sum -= B [ curr_begin ] ;
      curr_begin ++ ;
    }
    mp . add ( A [ i ] ) ;
    curr_sum += B [ i ] ;
    result = Integer . max ( result , curr_sum ) ;
  }
  return result ;
}
|||

WRITE_AN_EFFICIENT_METHOD_TO_CHECK_IF_A_NUMBER_IS_MULTIPLE_OF_3

static int isMultipleOf3 ( int n ) {
  int odd_count = 0 ;
  int even_count = 0 ;
  if ( n < 0 ) n = - n ;
  if ( n == 0 ) return 1 ;
  if ( n == 1 ) return 0 ;
  while ( n != 0 ) {
    if ( ( n & 1 ) != 0 ) odd_count ++ ;
    if ( ( n & 2 ) != 0 ) even_count ++ ;
    n = n >> 2 ;
  }
  return isMultipleOf3 ( Math . abs ( odd_count - even_count ) ) ;
}
|||

MAXIMUM_SUM_IARRI_AMONG_ROTATIONS_GIVEN_ARRAY_1

static int maxSum ( int arr [ ] , int n ) {
  int cum_sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) cum_sum += arr [ i ] ;
  int curr_val = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) curr_val += i * arr [ i ] ;
  int res = curr_val ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    int next_val = curr_val - ( cum_sum - arr [ i - 1 ] ) + arr [ i - 1 ] * ( n - 1 ) ;
    curr_val = next_val ;
    res = Math . max ( res , next_val ) ;
  }
  return res ;
}
|||

DYNAMIC_PROGRAMMING_SET_34_ASSEMBLY_LINE_SCHEDULING

static int carAssembly ( int a [ ] [ ] , int t [ ] [ ] , int e [ ] , int x [ ] ) {
  int T1 [ ] = new int [ NUM_STATION ] ;
  int T2 [ ] = new int [ NUM_STATION ] ;
  int i ;
  T1 [ 0 ] = e [ 0 ] + a [ 0 ] [ 0 ] ;
  T2 [ 0 ] = e [ 1 ] + a [ 1 ] [ 0 ] ;
  for ( i = 1 ;
  i < NUM_STATION ;
  ++ i ) {
    T1 [ i ] = min ( T1 [ i - 1 ] + a [ 0 ] [ i ] , T2 [ i - 1 ] + t [ 1 ] [ i ] + a [ 0 ] [ i ] ) ;
    T2 [ i ] = min ( T2 [ i - 1 ] + a [ 1 ] [ i ] , T1 [ i - 1 ] + t [ 0 ] [ i ] + a [ 1 ] [ i ] ) ;
  }
  return min ( T1 [ NUM_STATION - 1 ] + x [ 0 ] , T2 [ NUM_STATION - 1 ] + x [ 1 ] ) ;
}
|||

PRINT_MATRIX_SPIRAL_FORM_STARTING_POINT

static void printSpiral ( int [ ] [ ] mat , int r , int c ) {
  int i , a = 0 , b = 2 ;
  int low_row = ( 0 > a ) ? 0 : a ;
  int low_column = ( 0 > b ) ? 0 : b - 1 ;
  int high_row = ( ( a + 1 ) >= r ) ? r - 1 : a + 1 ;
  int high_column = ( ( b + 1 ) >= c ) ? c - 1 : b + 1 ;
  while ( ( low_row > 0 - r && low_column > 0 - c ) ) {
    for ( i = low_column + 1 ;
    i <= high_column && i < c && low_row >= 0 ;
    ++ i ) System . out . print ( mat [ low_row ] [ i ] + " " ) ;
    low_row -= 1 ;
    for ( i = low_row + 2 ;
    i <= high_row && i < r && high_column < c ;
    ++ i ) System . out . print ( mat [ i ] [ high_column ] + " " ) ;
    high_column += 1 ;
    for ( i = high_column - 2 ;
    i >= low_column && i >= 0 && high_row < r ;
    -- i ) System . out . print ( mat [ high_row ] [ i ] + " " ) ;
    high_row += 1 ;
    for ( i = high_row - 2 ;
    i > low_row && i >= 0 && low_column >= 0 ;
    -- i ) System . out . print ( mat [ i ] [ low_column ] + " " ) ;
    low_column -= 1 ;
  }
  System . out . println ( ) ;
}
|||

MID_POINT_CIRCLE_DRAWING_ALGORITHM

static void midPointCircleDraw ( int x_centre , int y_centre , int r ) {
  int x = r , y = 0 ;
  System . out . print ( "(" + ( x + x_centre ) + ", " + ( y + y_centre ) + ")" ) ;
  if ( r > 0 ) {
    System . out . print ( "(" + ( x + x_centre ) + ", " + ( - y + y_centre ) + ")" ) ;
    System . out . print ( "(" + ( y + x_centre ) + ", " + ( x + y_centre ) + ")" ) ;
    System . out . println ( "(" + ( - y + x_centre ) + ", " + ( x + y_centre ) + ")" ) ;
  }
  int P = 1 - r ;
  while ( x > y ) {
    y ++ ;
    if ( P <= 0 ) P = P + 2 * y + 1 ;
    else {
      x -- ;
      P = P + 2 * y - 2 * x + 1 ;
    }
    if ( x < y ) break ;
    System . out . print ( "(" + ( x + x_centre ) + ", " + ( y + y_centre ) + ")" ) ;
    System . out . print ( "(" + ( - x + x_centre ) + ", " + ( y + y_centre ) + ")" ) ;
    System . out . print ( "(" + ( x + x_centre ) + ", " + ( - y + y_centre ) + ")" ) ;
    System . out . println ( "(" + ( - x + x_centre ) + ", " + ( - y + y_centre ) + ")" ) ;
    if ( x != y ) {
      System . out . print ( "(" + ( y + x_centre ) + ", " + ( x + y_centre ) + ")" ) ;
      System . out . print ( "(" + ( - y + x_centre ) + ", " + ( x + y_centre ) + ")" ) ;
      System . out . print ( "(" + ( y + x_centre ) + ", " + ( - x + y_centre ) + ")" ) ;
      System . out . println ( "(" + ( - y + x_centre ) + ", " + ( - x + y_centre ) + ")" ) ;
    }
  }
}
|||

SMALLEST_ELEMENT_REPEATED_EXACTLY_K_TIMES_NOT_LIMITED_SMALL_RANGE

public static int smallestKFreq ( int a [ ] , int n , int k ) {
  HashMap < Integer , Integer > m = new HashMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( m . containsKey ( a [ i ] ) ) m . put ( a [ i ] , m . get ( a [ i ] ) + 1 ) ;
  else m . put ( a [ i ] , 1 ) ;
  int res = Integer . MAX_VALUE ;
  Set < Integer > s = m . keySet ( ) ;
  for ( int temp : s ) if ( m . get ( temp ) == k ) res = Math . min ( res , temp ) ;
  return ( res != Integer . MAX_VALUE ) ? res : - 1 ;
}
|||

MINIMUM_XOR_VALUE_PAIR

static int minXOR ( int arr [ ] , int n ) {
  int min_xor = Integer . MAX_VALUE ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) for ( int j = i + 1 ;
  j < n ;
  j ++ ) min_xor = Math . min ( min_xor , arr [ i ] ^ arr [ j ] ) ;
  return min_xor ;
}
|||

MIRROR_CHARACTERS_STRING

static String compute ( String str , int n ) {
  String reverseAlphabet = "zyxwvutsrqponmlkjihgfedcba" ;
  int l = str . length ( ) ;
  String answer = "" ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) answer = answer + str . charAt ( i ) ;
  for ( int i = n ;
  i < l ;
  i ++ ) answer = answer + reverseAlphabet . charAt ( str . charAt ( i ) - 'a' ) ;
  return answer ;
}
|||

PROGRAM_CHECK_PLUS_PERFECT_NUMBER

static boolean checkplusperfect ( int x ) {
  int temp = x ;
  int n = 0 ;
  while ( x != 0 ) {
    x /= 10 ;
    n ++ ;
  }
  x = temp ;
  int sum = 0 ;
  while ( x != 0 ) {
    sum += Math . pow ( x % 10 , n ) ;
    x /= 10 ;
  }
  return ( sum == temp ) ;
}
|||

ARC_LENGTH_ANGLE

static double arcLength ( double diameter , double angle ) {
  double pi = 22.0 / 7.0 ;
  double arc ;
  if ( angle >= 360 ) {
    System . out . println ( "Angle cannot" + " be formed" ) ;
    return 0 ;
  }
  else {
    arc = ( pi * diameter ) * ( angle / 360.0 ) ;
    return arc ;
  }
}
|||

FIND_LAST_INDEX_CHARACTER_STRING

static int findLastIndex ( String str , Character x ) {
  int index = - 1 ;
  for ( int i = 0 ;
  i < str . length ( ) ;
  i ++ ) if ( str . charAt ( i ) == x ) index = i ;
  return index ;
}
|||

COUNT_TRAILING_ZEROES_FACTORIAL_NUMBER

static int findTrailingZeros ( int n ) {
  int count = 0 ;
  for ( int i = 5 ;
  n / i >= 1 ;
  i *= 5 ) count += n / i ;
  return count ;
}
|||

ROTATE_MATRIX_180_DEGREE

static void rotateMatrix ( int mat [ ] [ ] ) {
  for ( int i = N - 1 ;
  i >= 0 ;
  i -- ) {
    for ( int j = N - 1 ;
    j >= 0 ;
    j -- ) System . out . print ( mat [ i ] [ j ] + " " ) ;
    System . out . println ( ) ;
  }
}
|||

SUM_FIBONACCI_NUMBERS

static int calculateSum ( int n ) {
  if ( n <= 0 ) return 0 ;
  int fibo [ ] = new int [ n + 1 ] ;
  fibo [ 0 ] = 0 ;
  fibo [ 1 ] = 1 ;
  int sum = fibo [ 0 ] + fibo [ 1 ] ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    fibo [ i ] = fibo [ i - 1 ] + fibo [ i - 2 ] ;
    sum += fibo [ i ] ;
  }
  return sum ;
}
|||

LARGEST_LEXICOGRAPHIC_ARRAY_WITH_AT_MOST_K_CONSECUTIVE_SWAPS

static void KSwapMaximum ( int [ ] arr , int n , int k ) {
  for ( int i = 0 ;
  i < n - 1 && k > 0 ;
  ++ i ) {
    int indexPosition = i ;
    for ( int j = i + 1 ;
    j < n ;
    ++ j ) {
      if ( k <= j - i ) break ;
      if ( arr [ j ] > arr [ indexPosition ] ) indexPosition = j ;
    }
    for ( int j = indexPosition ;
    j > i ;
    -- j ) SwapInts ( arr , j , j - 1 ) ;
    k -= indexPosition - i ;
  }
}
|||

FIND_WHETHER_GIVEN_INTEGER_POWER_3_NOT

static boolean check ( int n ) {
  return 1162261467 % n == 0 ;
}
|||

FIND_THE_TWO_REPEATING_ELEMENTS_IN_A_GIVEN_ARRAY

void printRepeating ( int arr [ ] , int size ) {
  int i , j ;
  System . out . println ( "Repeated Elements are :" ) ;
  for ( i = 0 ;
  i < size ;
  i ++ ) {
    for ( j = i + 1 ;
    j < size ;
    j ++ ) {
      if ( arr [ i ] == arr [ j ] ) System . out . print ( arr [ i ] + " " ) ;
    }
  }
}
|||

C_PROGRAM_FIND_AREA_TRIANGLE

static float findArea ( float a , float b , float c ) {
  if ( a < 0 || b < 0 || c < 0 || ( a + b <= c ) || a + c <= b || b + c <= a ) {
    System . out . println ( "Not a valid triangle" ) ;
    System . exit ( 0 ) ;
  }
  float s = ( a + b + c ) / 2 ;
  return ( float ) Math . sqrt ( s * ( s - a ) * ( s - b ) * ( s - c ) ) ;
}
|||

GIVEN_LARGE_NUMBER_CHECK_SUBSEQUENCE_DIGITS_DIVISIBLE_8_1

static boolean isSubSeqDivisible ( String str ) {
  int n = str . length ( ) ;
  int dp [ ] [ ] = new int [ n + 1 ] [ 10 ] ;
  int arr [ ] = new int [ n + 1 ] ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) arr [ i ] = ( int ) ( str . charAt ( i - 1 ) - '0' ) ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    dp [ i ] [ arr [ i ] % 8 ] = 1 ;
    for ( int j = 0 ;
    j < 8 ;
    j ++ ) {
      if ( dp [ i - 1 ] [ j ] > dp [ i ] [ ( j * 10 + arr [ i ] ) % 8 ] ) dp [ i ] [ ( j * 10 + arr [ i ] ) % 8 ] = dp [ i - 1 ] [ j ] ;
      if ( dp [ i - 1 ] [ j ] > dp [ i ] [ j ] ) dp [ i ] [ j ] = dp [ i - 1 ] [ j ] ;
    }
  }
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    if ( dp [ i ] [ 0 ] == 1 ) return true ;
  }
  return false ;
}
|||

DELETE_ARRAY_ELEMENTS_WHICH_ARE_SMALLER_THAN_NEXT_OR_BECOME_SMALLER

static void deleteElements ( int arr [ ] , int n , int k ) {
  Stack < Integer > s = new Stack < > ( ) ;
  s . push ( arr [ 0 ] ) ;
  int count = 0 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    while ( ! s . empty ( ) && s . peek ( ) < arr [ i ] && count < k ) {
      s . pop ( ) ;
      count ++ ;
    }
    s . push ( arr [ i ] ) ;
  }
  int m = s . size ( ) ;
  Integer [ ] v = new Integer [ m ] ;
  while ( ! s . empty ( ) ) {
    v [ -- m ] = s . peek ( ) ;
    s . pop ( ) ;
  }
  for ( Integer x : v ) {
    System . out . print ( x + "" ) ;
  };
  System . out . println ( "" ) ;
}
|||

MINIMUM_LENGTH_SUBARRAY_SUM_GREATER_GIVEN_VALUE

static int smallestSubWithSum ( int arr [ ] , int n , int x ) {
  int curr_sum = 0 , min_len = n + 1 ;
  int start = 0 , end = 0 ;
  while ( end < n ) {
    while ( curr_sum <= x && end < n ) curr_sum += arr [ end ++ ] ;
    while ( curr_sum > x && start < n ) {
      if ( end - start < min_len ) min_len = end - start ;
      curr_sum -= arr [ start ++ ] ;
    }
  }
  return min_len ;
}
|||

FIND_PAIRS_IN_ARRAY_WHOSE_SUMS_ALREADY_EXIST_IN_ARRAY_1

public static void findPair ( int [ ] arr , int n ) {
  HashSet < Integer > s = new HashSet < Integer > ( ) ;
  for ( Integer i : arr ) {
    s . add ( i ) ;
  }
  boolean found = false ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      int sum = arr [ i ] + arr [ j ] ;
      if ( s . contains ( sum ) ) {
        found = true ;
        System . out . println ( arr [ i ] + " " + arr [ j ] ) ;
      }
    }
  }
  if ( found == false ) System . out . println ( "Not Exist " ) ;
}
|||

COUNT_ARITHMETIC_PROGRESSION_SUBSEQUENCES_ARRAY

static int numofAP ( int a [ ] , int n ) {
  int minarr = + 2147483647 ;
  int maxarr = - 2147483648 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    minarr = Math . min ( minarr , a [ i ] ) ;
    maxarr = Math . max ( maxarr , a [ i ] ) ;
  }
  int dp [ ] = new int [ n ] ;
  int sum [ ] = new int [ MAX ] ;
  int ans = n + 1 ;
  for ( int d = ( minarr - maxarr ) ;
  d <= ( maxarr - minarr ) ;
  d ++ ) {
    Arrays . fill ( sum , 0 ) ;
    for ( int i = 0 ;
    i < n ;
    i ++ ) {
      dp [ i ] = 1 ;
      if ( a [ i ] - d >= 1 && a [ i ] - d <= 1000000 ) dp [ i ] += sum [ a [ i ] - d ] ;
      ans += dp [ i ] - 1 ;
      sum [ a [ i ] ] += dp [ i ] ;
    }
  }
  return ans ;
}
|||

COUNT_NUMBERS_THAT_DONT_CONTAIN_3

static int count ( int n ) {
  if ( n < 3 ) return n ;
  if ( n >= 3 && n < 10 ) return n - 1 ;
  int po = 1 ;
  while ( n / po > 9 ) po = po * 10 ;
  int msd = n / po ;
  if ( msd != 3 ) return count ( msd ) * count ( po - 1 ) + count ( msd ) + count ( n % po ) ;
  else return count ( msd * po - 1 ) ;
}
|||

PROGRAM_TO_FIND_TRANSPOSE_OF_A_MATRIX_2

static void transpose ( int A [ ] [ ] ) {
  for ( int i = 0 ;
  i < N ;
  i ++ ) for ( int j = i + 1 ;
  j < N ;
  j ++ ) {
    int temp = A [ i ] [ j ] ;
    A [ i ] [ j ] = A [ j ] [ i ] ;
    A [ j ] [ i ] = temp ;
  }
}
|||

SUM_DIAGONALS_SPIRAL_ODD_ORDER_SQUARE_MATRIX

static int spiralDiaSum ( int n ) {
  if ( n == 1 ) return 1 ;
  return ( 4 * n * n - 6 * n + 6 + spiralDiaSum ( n - 2 ) ) ;
}
|||

COUNT_INVERSIONS_OF_SIZE_THREE_IN_A_GIVE_ARRAY

int getInvCount ( int arr [ ] , int n ) {
  int invcount = 0 ;
  for ( int i = 0 ;
  i < n - 2 ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n - 1 ;
    j ++ ) {
      if ( arr [ i ] > arr [ j ] ) {
        for ( int k = j + 1 ;
        k < n ;
        k ++ ) {
          if ( arr [ j ] > arr [ k ] ) invcount ++ ;
        }
      }
    }
  }
  return invcount ;
}
|||

FIND_SUM_NODES_GIVEN_PERFECT_BINARY_TREE

static int sumNodes ( int l ) {
  int leafNodeCount = ( int ) Math . pow ( 2 , l - 1 ) ;
  Vector < Vector < Integer >> vec = new Vector < Vector < Integer >> ( ) ;
  for ( int i = 1 ;
  i <= l ;
  i ++ ) vec . add ( new Vector < Integer > ( ) ) ;
  for ( int i = 1 ;
  i <= leafNodeCount ;
  i ++ ) vec . get ( l - 1 ) . add ( i ) ;
  for ( int i = l - 2 ;
  i >= 0 ;
  i -- ) {
    int k = 0 ;
    while ( k < vec . get ( i + 1 ) . size ( ) - 1 ) {
      vec . get ( i ) . add ( vec . get ( i + 1 ) . get ( k ) + vec . get ( i + 1 ) . get ( k + 1 ) ) ;
      k += 2 ;
    }
  }
  int sum = 0 ;
  for ( int i = 0 ;
  i < l ;
  i ++ ) {
    for ( int j = 0 ;
    j < vec . get ( i ) . size ( ) ;
    j ++ ) sum += vec . get ( i ) . get ( j ) ;
  }
  return sum ;
}
|||

SUM_OF_ALL_PROPER_DIVISORS_OF_A_NATURAL_NUMBER

static int divSum ( int num ) {
  int result = 0 ;
  for ( int i = 2 ;
  i <= Math . sqrt ( num ) ;
  i ++ ) {
    if ( num % i == 0 ) {
      if ( i == ( num / i ) ) result += i ;
      else result += ( i + num / i ) ;
    }
  }
  return ( result + 1 ) ;
}
|||

FIND_A_TRIPLET_THAT_SUM_TO_A_GIVEN_VALUE_2

static boolean find3Numbers ( int A [ ] , int arr_size , int sum ) {
  for ( int i = 0 ;
  i < arr_size - 2 ;
  i ++ ) {
    HashSet < Integer > s = new HashSet < Integer > ( ) ;
    int curr_sum = sum - A [ i ] ;
    for ( int j = i + 1 ;
    j < arr_size ;
    j ++ ) {
      if ( s . contains ( curr_sum - A [ j ] ) && curr_sum - A [ j ] != ( int ) s . toArray ( ) [ s . size ( ) - 1 ] ) {
        System . out . printf ( "Triplet is %d, %d, %d" , A [ i ] , A [ j ] , curr_sum - A [ j ] ) ;
        return true ;
      }
      s . add ( A [ j ] ) ;
    }
  }
  return false ;
}
|||

NTH_EVEN_LENGTH_PALINDROME

static String evenlength ( String n ) {
  String res = n ;
  for ( int j = n . length ( ) - 1 ;
  j >= 0 ;
  -- j ) res += n . charAt ( j ) ;
  return res ;
}
|||

FINDING_POWER_PRIME_NUMBER_P_N

static int PowerOFPINnfactorial ( int n , int p ) {
  int ans = 0 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    int count = 0 , temp = i ;
    while ( temp % p == 0 ) {
      count ++ ;
      temp = temp / p ;
    }
    ans += count ;
  }
  return ans ;
}
|||

MINIMUM_COST_MAKE_LONGEST_COMMON_SUBSEQUENCE_LENGTH_K

static int solve ( char X [ ] , char Y [ ] , int l , int r , int k , int dp [ ] [ ] [ ] ) {
  if ( k == 0 ) {
    return 0 ;
  }
  if ( l < 0 | r < 0 ) {
    return ( int ) 1e9 ;
  }
  if ( dp [ l ] [ r ] [ k ] != - 1 ) {
    return dp [ l ] [ r ] [ k ] ;
  }
  int cost = ( X [ l ] - 'a' ) ^ ( Y [ r ] - 'a' ) ;
  return dp [ l ] [ r ] [ k ] = Math . min ( Math . min ( cost + solve ( X , Y , l - 1 , r - 1 , k - 1 , dp ) , solve ( X , Y , l - 1 , r , k , dp ) ) , solve ( X , Y , l , r - 1 , k , dp ) ) ;
}
|||

PRINT_STRING_SPECIFIED_CHARACTER_OCCURRED_GIVEN_NO_TIMES

static void printString ( String str , char ch , int count ) {
  int occ = 0 , i ;
  if ( count == 0 ) {
    System . out . println ( str ) ;
    return ;
  }
  for ( i = 0 ;
  i < str . length ( ) ;
  i ++ ) {
    if ( str . charAt ( i ) == ch ) occ ++ ;
    if ( occ == count ) break ;
  }
  if ( i < str . length ( ) - 1 ) System . out . println ( str . substring ( i + 1 ) ) ;
  else System . out . println ( "Empty string" ) ;
}
|||

SORT_1_N_SWAPPING_ADJACENT_ELEMENTS

static boolean sortedAfterSwap ( int A [ ] , boolean B [ ] , int n ) {
  int i , j ;
  for ( i = 0 ;
  i < n - 1 ;
  i ++ ) {
    if ( B [ i ] ) {
      j = i ;
      while ( B [ j ] ) {
        j ++ ;
      }
      Arrays . sort ( A , i , 1 + j ) ;
      i = j ;
    }
  }
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    if ( A [ i ] != i + 1 ) {
      return false ;
    }
  }
  return true ;
}
|||

GENERATE_PYTHAGOREAN_TRIPLETS

static void pythagoreanTriplets ( int limit ) {
  int a , b , c = 0 ;
  int m = 2 ;
  while ( c < limit ) {
    for ( int n = 1 ;
    n < m ;
    ++ n ) {
      a = m * m - n * n ;
      b = 2 * m * n ;
      c = m * m + n * n ;
      if ( c > limit ) break ;
      System . out . println ( a + " " + b + " " + c ) ;
    }
    m ++ ;
  }
}
|||

COUNT_EVEN_LENGTH_BINARY_SEQUENCES_WITH_SAME_SUM_OF_FIRST_AND_SECOND_HALF_BITS

static int countSeq ( int n , int diff ) {
  if ( Math . abs ( diff ) > n ) return 0 ;
  if ( n == 1 && diff == 0 ) return 2 ;
  if ( n == 1 && Math . abs ( diff ) == 1 ) return 1 ;
  int res = countSeq ( n - 1 , diff + 1 ) + 2 * countSeq ( n - 1 , diff ) + countSeq ( n - 1 , diff - 1 ) ;
  return res ;
}
|||

POSSIBLE_FORM_TRIANGLE_ARRAY_VALUES

static boolean isPossibleTriangle ( int [ ] arr , int N ) {
  if ( N < 3 ) return false ;
  Arrays . sort ( arr ) ;
  for ( int i = 0 ;
  i < N - 2 ;
  i ++ ) if ( arr [ i ] + arr [ i + 1 ] > arr [ i + 2 ] ) return true ;
  return false ;
}
|||

PRINT_ARRAY_STRINGS_SORTED_ORDER_WITHOUT_COPYING_ONE_STRING_ANOTHER

static void printInSortedOrder ( String arr [ ] , int n ) {
  int index [ ] = new int [ n ] ;
  int i , j , min ;
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    index [ i ] = i ;
  }
  for ( i = 0 ;
  i < n - 1 ;
  i ++ ) {
    min = i ;
    for ( j = i + 1 ;
    j < n ;
    j ++ ) {
      if ( arr [ index [ min ] ] . compareTo ( arr [ index [ j ] ] ) > 0 ) {
        min = j ;
      }
    }
    if ( min != i ) {
      int temp = index [ min ] ;
      index [ min ] = index [ i ] ;
      index [ i ] = temp ;
    }
  }
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    System . out . print ( arr [ index [ i ] ] + " " ) ;
  }
}
|||

GAME_REPLACING_ARRAY_ELEMENTS

public static int playGame ( int arr [ ] ) {
  HashSet < Integer > set = new HashSet < > ( ) ;
  for ( int i : arr ) set . add ( i ) ;
  return ( set . size ( ) % 2 == 0 ) ? 1 : 2 ;
}
|||

BASIC_AND_EXTENDED_EUCLIDEAN_ALGORITHMS

public static int gcd ( int a , int b ) {
  if ( a == 0 ) return b ;
  return gcd ( b % a , a ) ;
}
|||

SORT_ARRAY_WAVE_FORM_2_1

void sortInWave ( int arr [ ] , int n ) {
  for ( int i = 0 ;
  i < n ;
  i += 2 ) {
    if ( i > 0 && arr [ i - 1 ] > arr [ i ] ) swap ( arr , i - 1 , i ) ;
    if ( i < n - 1 && arr [ i ] < arr [ i + 1 ] ) swap ( arr , i , i + 1 ) ;
  }
}
|||

MAXIMUM_SUBARRAY_SUM_USING_PREFIX_SUM

static int maximumSumSubarray ( int arr [ ] , int n ) {
  int min_prefix_sum = 0 ;
  int res = Integer . MIN_VALUE ;
  int prefix_sum [ ] = new int [ n ] ;
  prefix_sum [ 0 ] = arr [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) prefix_sum [ i ] = prefix_sum [ i - 1 ] + arr [ i ] ;
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

static String firstLetterWord ( String str ) {
  String result = "" ;
  boolean v = true ;
  for ( int i = 0 ;
  i < str . length ( ) ;
  i ++ ) {
    if ( str . charAt ( i ) == ' ' ) {
      v = true ;
    }
    else if ( str . charAt ( i ) != ' ' && v == true ) {
      result += ( str . charAt ( i ) ) ;
      v = false ;
    }
  }
  return result ;
}
|||

SUM_PAIRWISE_PRODUCTS_1

static int findSum ( int n ) {
  int multiTerms = n * ( n + 1 ) / 2 ;
  int sum = multiTerms ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    multiTerms = multiTerms - ( i - 1 ) ;
    sum = sum + multiTerms * i ;
  }
  return sum ;
}
|||

CLUSTERINGPARTITIONING_AN_ARRAY_SUCH_THAT_SUM_OF_SQUARE_DIFFERENCES_IS_MINIMUM_1

static int minCost ( int a [ ] , int n , int k ) {
  int dp [ ] [ ] = new int [ n + 1 ] [ k + 1 ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) for ( int j = 0 ;
  j <= k ;
  j ++ ) dp [ i ] [ j ] = inf ;
  dp [ 0 ] [ 0 ] = 0 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) for ( int j = 1 ;
  j <= k ;
  j ++ ) for ( int m = i - 1 ;
  m >= 0 ;
  m -- ) dp [ i ] [ j ] = Math . min ( dp [ i ] [ j ] , dp [ m ] [ j - 1 ] + ( a [ i - 1 ] - a [ m ] ) * ( a [ i - 1 ] - a [ m ] ) ) ;
  return dp [ n ] [ k ] ;
}
|||

LEIBNIZ_HARMONIC_TRIANGLE

static void LeibnizHarmonicTriangle ( int n ) {
  int C [ ] [ ] = new int [ n + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= Math . min ( i , n ) ;
    j ++ ) {
      if ( j == 0 || j == i ) C [ i ] [ j ] = 1 ;
      else C [ i ] [ j ] = C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ] ;
    }
  }
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int j = 1 ;
    j <= i ;
    j ++ ) System . out . print ( "1/" + i * C [ i - 1 ] [ j - 1 ] + " " ) ;
    System . out . println ( ) ;
  }
}
|||

CHECK_WHETHER_SECOND_STRING_CAN_FORMED_FIRST_STRING_USING_COUNT_ARRAY

static boolean canMakeStr2 ( String str1 , String str2 ) {
  int [ ] count = new int [ MAX ] ;
  char [ ] str3 = str1 . toCharArray ( ) ;
  for ( int i = 0 ;
  i < str3 . length ;
  i ++ ) count [ str3 [ i ] ] ++ ;
  char [ ] str4 = str2 . toCharArray ( ) ;
  for ( int i = 0 ;
  i < str4 . length ;
  i ++ ) {
    if ( count [ str4 [ i ] ] == 0 ) return false ;
    count [ str4 [ i ] ] -- ;
  }
  return true ;
}
|||

SUM_MINIMUM_MAXIMUM_ELEMENTS_SUBARRAYS_SIZE_K

public static int SumOfKsubArray ( int arr [ ] , int k ) {
  int sum = 0 ;
  Deque < Integer > S = new LinkedList < > ( ) , G = new LinkedList < > ( ) ;
  int i = 0 ;
  for ( i = 0 ;
  i < k ;
  i ++ ) {
    while ( ! S . isEmpty ( ) && arr [ S . peekLast ( ) ] >= arr [ i ] ) S . removeLast ( ) ;
    while ( ! G . isEmpty ( ) && arr [ G . peekLast ( ) ] <= arr [ i ] ) G . removeLast ( ) ;
    G . addLast ( i ) ;
    S . addLast ( i ) ;
  }
  for ( ;
  i < arr . length ;
  i ++ ) {
    sum += arr [ S . peekFirst ( ) ] + arr [ G . peekFirst ( ) ] ;
    while ( ! S . isEmpty ( ) && S . peekFirst ( ) <= i - k ) S . removeFirst ( ) ;
    while ( ! G . isEmpty ( ) && G . peekFirst ( ) <= i - k ) G . removeFirst ( ) ;
    while ( ! S . isEmpty ( ) && arr [ S . peekLast ( ) ] >= arr [ i ] ) S . removeLast ( ) ;
    while ( ! G . isEmpty ( ) && arr [ G . peekLast ( ) ] <= arr [ i ] ) G . removeLast ( ) ;
    G . addLast ( i ) ;
    S . addLast ( i ) ;
  }
  sum += arr [ S . peekFirst ( ) ] + arr [ G . peekFirst ( ) ] ;
  return sum ;
}
|||

LONGEST_COMMON_SUBSEQUENCE

int lcs ( char [ ] X , char [ ] Y , int m , int n ) {
  if ( m == 0 || n == 0 ) return 0 ;
  if ( X [ m - 1 ] == Y [ n - 1 ] ) return 1 + lcs ( X , Y , m - 1 , n - 1 ) ;
  else return max ( lcs ( X , Y , m , n - 1 ) , lcs ( X , Y , m - 1 , n ) ) ;
}
|||

MINIMUM_SUM_ABSOLUTE_DIFFERENCE_PAIRS_TWO_ARRAYS

static long findMinSum ( long a [ ] , long b [ ] , long n ) {
  Arrays . sort ( a ) ;
  Arrays . sort ( b ) ;
  long sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) sum = sum + Math . abs ( a [ i ] - b [ i ] ) ;
  return sum ;
}
|||

COUNT_DISTINCT_NON_NEGATIVE_PAIRS_X_Y_SATISFY_INEQUALITY_XX_YY_N_2

static int countSolutions ( int n ) {
  int res = 0 ;
  for ( int x = 0 ;
  x * x < n ;
  x ++ ) for ( int y = 0 ;
  x * x + y * y < n ;
  y ++ ) res ++ ;
  return res ;
}
|||

FIND_NUMBER_TRANSFORMATION_MAKE_TWO_MATRIX_EQUAL

static int countOps ( int A [ ] [ ] , int B [ ] [ ] , int m , int n ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) for ( int j = 0 ;
  j < m ;
  j ++ ) A [ i ] [ j ] -= B [ i ] [ j ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) for ( int j = 1 ;
  j < m ;
  j ++ ) if ( A [ i ] [ j ] - A [ i ] [ 0 ] - A [ 0 ] [ j ] + A [ 0 ] [ 0 ] != 0 ) return - 1 ;
  int result = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) result += Math . abs ( A [ i ] [ 0 ] ) ;
  for ( int j = 0 ;
  j < m ;
  j ++ ) result += Math . abs ( A [ 0 ] [ j ] - A [ 0 ] [ 0 ] ) ;
  return ( result ) ;
}
|||

EFFICIENTLY_FIND_FIRST_REPEATED_CHARACTER_STRING_WITHOUT_USING_ADDITIONAL_DATA_STRUCTURE_ONE_TRAVERSAL

static int FirstRepeated ( String str ) {
  int checker = 0 ;
  for ( int i = 0 ;
  i < str . length ( ) ;
  ++ i ) {
    int val = ( str . charAt ( i ) - 'a' ) ;
    if ( ( checker & ( 1 << val ) ) > 0 ) return i ;
    checker |= ( 1 << val ) ;
  }
  return - 1 ;
}
|||

MAXIMUM_UNIQUE_ELEMENT_EVERY_SUBARRAY_SIZE_K

static void find_max ( int [ ] A , int N , int K ) {
  HashMap < Integer , Integer > Count = new HashMap < > ( ) ;
  for ( int i = 0 ;
  i < K - 1 ;
  i ++ ) if ( Count . containsKey ( A [ i ] ) ) Count . put ( A [ i ] , 1 + Count . get ( A [ i ] ) ) ;
  else Count . put ( A [ i ] , 1 ) ;
  TreeSet < Integer > Myset = new TreeSet < Integer > ( ) ;
  for ( Map . Entry x : Count . entrySet ( ) ) {
    if ( Integer . parseInt ( String . valueOf ( x . getValue ( ) ) ) == 1 ) Myset . add ( Integer . parseInt ( String . valueOf ( x . getKey ( ) ) ) ) ;
  }
  for ( int i = K - 1 ;
  i < N ;
  i ++ ) {
    if ( Count . containsKey ( A [ i ] ) ) Count . put ( A [ i ] , 1 + Count . get ( A [ i ] ) ) ;
    else Count . put ( A [ i ] , 1 ) ;
    if ( Integer . parseInt ( String . valueOf ( Count . get ( A [ i ] ) ) ) == 1 ) Myset . add ( A [ i ] ) ;
    else Myset . remove ( A [ i ] ) ;
    if ( Myset . size ( ) == 0 ) System . out . println ( "Nothing" ) ;
    else System . out . println ( Myset . last ( ) ) ;
    int x = A [ i - K + 1 ] ;
    Count . put ( x , Count . get ( x ) - 1 ) ;
    if ( Integer . parseInt ( String . valueOf ( Count . get ( x ) ) ) == 1 ) Myset . add ( x ) ;
    if ( Integer . parseInt ( String . valueOf ( Count . get ( x ) ) ) == 0 ) Myset . remove ( x ) ;
  }
}
|||

MINIMUM_COST_SORT_MATRIX_NUMBERS_0_N2_1

public static int calculateEnergy ( int mat [ ] [ ] , int n ) {
  int i_des , j_des , q ;
  int tot_energy = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      q = mat [ i ] [ j ] / n ;
      i_des = q ;
      j_des = mat [ i ] [ j ] - ( n * q ) ;
      tot_energy += Math . abs ( i_des - i ) + Math . abs ( j_des - j ) ;
    }
  }
  return tot_energy ;
}
|||

LONGEST_COMMON_SUBSTRING

static int LCSubStr ( char X [ ] , char Y [ ] , int m , int n ) {
  int LCStuff [ ] [ ] = new int [ m + 1 ] [ n + 1 ] ;
  int result = 0 ;
  for ( int i = 0 ;
  i <= m ;
  i ++ ) {
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      if ( i == 0 || j == 0 ) LCStuff [ i ] [ j ] = 0 ;
      else if ( X [ i - 1 ] == Y [ j - 1 ] ) {
        LCStuff [ i ] [ j ] = LCStuff [ i - 1 ] [ j - 1 ] + 1 ;
        result = Integer . max ( result , LCStuff [ i ] [ j ] ) ;
      }
      else LCStuff [ i ] [ j ] = 0 ;
    }
  }
  return result ;
}
|||

MAXIMUM_SUM_BITONIC_SUBARRAY

static int maxSumBitonicSubArr ( int arr [ ] , int n ) {
  int [ ] msis = new int [ n ] ;
  int [ ] msds = new int [ n ] ;
  int max_sum = Integer . MIN_VALUE ;
  msis [ 0 ] = arr [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) if ( arr [ i ] > arr [ i - 1 ] ) msis [ i ] = msis [ i - 1 ] + arr [ i ] ;
  else msis [ i ] = arr [ i ] ;
  msds [ n - 1 ] = arr [ n - 1 ] ;
  for ( int i = n - 2 ;
  i >= 0 ;
  i -- ) if ( arr [ i ] > arr [ i + 1 ] ) msds [ i ] = msds [ i + 1 ] + arr [ i ] ;
  else msds [ i ] = arr [ i ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( max_sum < ( msis [ i ] + msds [ i ] - arr [ i ] ) ) max_sum = msis [ i ] + msds [ i ] - arr [ i ] ;
  return max_sum ;
}
|||

NEWMAN_CONWAY_SEQUENCE

static int sequence ( int n ) {
  if ( n == 1 || n == 2 ) return 1 ;
  else return sequence ( sequence ( n - 1 ) ) + sequence ( n - sequence ( n - 1 ) ) ;
}
|||

PRINT_TRIPLETS_SORTED_ARRAY_FORM_AP

static void printAllAPTriplets ( int [ ] arr , int n ) {
  ArrayList < Integer > s = new ArrayList < Integer > ( ) ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      int diff = arr [ j ] - arr [ i ] ;
      boolean exists = s . contains ( arr [ i ] - diff ) ;
      if ( exists ) System . out . println ( arr [ i ] - diff + " " + arr [ i ] + " " + arr [ j ] ) ;
    }
    s . add ( arr [ i ] ) ;
  }
}
|||

QUERIES_COUNTS_ARRAY_ELEMENTS_VALUES_GIVEN_RANGE

static int countInRange ( int arr [ ] , int n , int x , int y ) {
  int count = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] >= x && arr [ i ] <= y ) count ++ ;
  }
  return count ;
}
|||

HIGHWAY_BILLBOARD_PROBLEM

static int maxRevenue ( int m , int [ ] x , int [ ] revenue , int n , int t ) {
  int [ ] maxRev = new int [ m + 1 ] ;
  for ( int i = 0 ;
  i < m + 1 ;
  i ++ ) maxRev [ i ] = 0 ;
  int nxtbb = 0 ;
  for ( int i = 1 ;
  i <= m ;
  i ++ ) {
    if ( nxtbb < n ) {
      if ( x [ nxtbb ] != i ) maxRev [ i ] = maxRev [ i - 1 ] ;
      else {
        if ( i <= t ) maxRev [ i ] = Math . max ( maxRev [ i - 1 ] , revenue [ nxtbb ] ) ;
        else maxRev [ i ] = Math . max ( maxRev [ i - t - 1 ] + revenue [ nxtbb ] , maxRev [ i - 1 ] ) ;
        nxtbb ++ ;
      }
    }
    else maxRev [ i ] = maxRev [ i - 1 ] ;
  }
  return maxRev [ m ] ;
}
|||

CONSTRUCT_GRAPH_GIVEN_DEGREES_VERTICES

static void printMat ( int degseq [ ] , int n ) {
  int [ ] [ ] mat = new int [ n ] [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      if ( degseq [ i ] > 0 && degseq [ j ] > 0 ) {
        degseq [ i ] -- ;
        degseq [ j ] -- ;
        mat [ i ] [ j ] = 1 ;
        mat [ j ] [ i ] = 1 ;
      }
    }
  }
  System . out . print ( "\n" + setw ( 3 ) + "     " ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) System . out . print ( setw ( 3 ) + "(" + i + ")" ) ;
  System . out . print ( "\n\n" ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    System . out . print ( setw ( 4 ) + "(" + i + ")" ) ;
    for ( int j = 0 ;
    j < n ;
    j ++ ) System . out . print ( setw ( 5 ) + mat [ i ] [ j ] ) ;
    System . out . print ( "\n" ) ;
  }
}
|||

DETECT_IF_TWO_INTEGERS_HAVE_OPPOSITE_SIGNS

static boolean oppositeSigns ( int x , int y ) {
  return ( ( x ^ y ) < 0 ) ;
}
|||

TRIANGULAR_NUMBERS_1

static boolean isTriangular ( int num ) {
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
|||

FIND_WHETHER_A_GIVEN_NUMBER_IS_A_POWER_OF_4_OR_NOT

static int isPowerOfFour ( int n ) {
  if ( n == 0 ) return 0 ;
  while ( n != 1 ) {
    if ( n % 4 != 0 ) return 0 ;
    n = n / 4 ;
  }
  return 1 ;
}
|||

LAST_NON_ZERO_DIGIT_FACTORIAL

static int lastNon0Digit ( int n ) {
  if ( n < 10 ) return dig [ n ] ;
  if ( ( ( n / 10 ) % 10 ) % 2 == 0 ) return ( 6 * lastNon0Digit ( n / 5 ) * dig [ n % 10 ] ) % 10 ;
  else return ( 4 * lastNon0Digit ( n / 5 ) * dig [ n % 10 ] ) % 10 ;
}
|||

SORT_STRING_ACCORDING_ORDER_DEFINED_ANOTHER_STRING

static void sortByPattern ( char [ ] str , char [ ] pat ) {
  int count [ ] = new int [ MAX_CHAR ] ;
  for ( int i = 0 ;
  i < str . length ;
  i ++ ) {
    count [ str [ i ] - 'a' ] ++ ;
  }
  int index = 0 ;
  for ( int i = 0 ;
  i < pat . length ;
  i ++ ) {
    for ( int j = 0 ;
    j < count [ pat [ i ] - 'a' ] ;
    j ++ ) {
      str [ index ++ ] = pat [ i ] ;
    }
  }
}
|||

NUMBER_VISIBLE_BOXES_PUTTING_ONE_INSIDE_ANOTHER

static int minimumBox ( int [ ] arr , int n ) {
  Queue < Integer > q = new LinkedList < > ( ) ;
  Arrays . sort ( arr ) ;
  q . add ( arr [ 0 ] ) ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    int now = q . element ( ) ;
    if ( arr [ i ] >= 2 * now ) q . remove ( ) ;
    q . add ( arr [ i ] ) ;
  }
  return q . size ( ) ;
}
|||

SEARCH_INSERT_AND_DELETE_IN_A_SORTED_ARRAY

static int binarySearch ( int arr [ ] , int low , int high , int key ) {
  if ( high < low ) return - 1 ;
  int mid = ( low + high ) / 2 ;
  if ( key == arr [ mid ] ) return mid ;
  if ( key > arr [ mid ] ) return binarySearch ( arr , ( mid + 1 ) , high , key ) ;
  return binarySearch ( arr , low , ( mid - 1 ) , key ) ;
}
|||

FIND_THE_TWO_REPEATING_ELEMENTS_IN_A_GIVEN_ARRAY_3

void printRepeating ( int arr [ ] , int size ) {
  int i ;
  System . out . println ( "The repeating elements are : " ) ;
  for ( i = 0 ;
  i < size ;
  i ++ ) {
    if ( arr [ Math . abs ( arr [ i ] ) ] > 0 ) arr [ Math . abs ( arr [ i ] ) ] = - arr [ Math . abs ( arr [ i ] ) ] ;
    else System . out . print ( Math . abs ( arr [ i ] ) + " " ) ;
  }
}
|||

COUNT_POSSIBLE_GROUPS_SIZE_2_3_SUM_MULTIPLE_3

int findgroups ( int arr [ ] , int n ) {
  int c [ ] = new int [ ] {
    0 , 0 , 0 };
    int i ;
    int res = 0 ;
    for ( i = 0 ;
    i < n ;
    i ++ ) c [ arr [ i ] % 3 ] ++ ;
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

static void printStringAlternate ( String str ) {
  int [ ] occ = new int [ 122 ] ;
  String s = str . toLowerCase ( ) ;
  for ( int i = 0 ;
  i < str . length ( ) ;
  i ++ ) {
    char temp = s . charAt ( i ) ;
    occ [ temp ] ++ ;
    if ( occ [ temp ] % 2 != 0 ) System . out . print ( str . charAt ( i ) ) ;
  }
  System . out . println ( ) ;
}
|||

NUMBER_DAYS_TANK_WILL_BECOME_EMPTY

static int minDaysToEmpty ( int C , int l ) {
  if ( l >= C ) return C ;
  double eq_root = ( Math . sqrt ( 1 + 8 * ( C - l ) ) - 1 ) / 2 ;
  return ( int ) ( Math . ceil ( eq_root ) + l ) ;
}
|||

REVERSE_STRING_WITHOUT_USING_ANY_TEMPORARY_VARIABLE

static String reversingString ( char [ ] str , int start , int end ) {
  while ( start < end ) {
    str [ start ] ^= str [ end ] ;
    str [ end ] ^= str [ start ] ;
    str [ start ] ^= str [ end ] ;
    ++ start ;
    -- end ;
  }
  return String . valueOf ( str ) ;
}
|||

FREQUENCY_ELEMENT_UNSORTED_ARRAY

static void countFreq ( int [ ] a , int n ) {
  HashMap < Integer , Integer > hm = new HashMap < > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) hm . put ( a [ i ] , hm . get ( a [ i ] ) == null ? 1 : hm . get ( a [ i ] ) + 1 ) ;
  SortedMap < Integer , Integer > st = new TreeMap < > ( ) ;
  for ( HashMap . Entry < Integer , Integer > x : hm . entrySet ( ) ) {
    st . put ( x . getKey ( ) , x . getValue ( ) ) ;
  }
  int cumul = 0 ;
  for ( SortedMap . Entry < Integer , Integer > x : st . entrySet ( ) ) {
    cumul += x . getValue ( ) ;
    System . out . println ( x . getKey ( ) + " " + cumul ) ;
  }
}
|||

FIND_ROTATION_COUNT_ROTATED_SORTED_ARRAY

static int countRotations ( int arr [ ] , int n ) {
  int min = arr [ 0 ] , min_index = - 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( min > arr [ i ] ) {
      min = arr [ i ] ;
      min_index = i ;
    }
  }
  return min_index ;
}
|||

LONGEST_INCREASING_SUBSEQUENCE_1

static int lis ( int arr [ ] , int n ) {
  int lis [ ] = new int [ n ] ;
  int i , j , max = 0 ;
  for ( i = 0 ;
  i < n ;
  i ++ ) lis [ i ] = 1 ;
  for ( i = 1 ;
  i < n ;
  i ++ ) for ( j = 0 ;
  j < i ;
  j ++ ) if ( arr [ i ] > arr [ j ] && lis [ i ] < lis [ j ] + 1 ) lis [ i ] = lis [ j ] + 1 ;
  for ( i = 0 ;
  i < n ;
  i ++ ) if ( max < lis [ i ] ) max = lis [ i ] ;
  return max ;
}
|||

MEDIAN_OF_TWO_SORTED_ARRAYS

static int getMedian ( int ar1 [ ] , int ar2 [ ] , int n ) {
  int i = 0 ;
  int j = 0 ;
  int count ;
  int m1 = - 1 , m2 = - 1 ;
  for ( count = 0 ;
  count <= n ;
  count ++ ) {
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

static String minLexRotation ( String str ) {
  int n = str . length ( ) ;
  String arr [ ] = new String [ n ] ;
  String concat = str + str ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    arr [ i ] = concat . substring ( i , i + n ) ;
  }
  Arrays . sort ( arr ) ;
  return arr [ 0 ] ;
}
|||

INTERPOLATION_SEARCH

static int interpolationSearch ( int x ) {
  int lo = 0 , hi = ( arr . length - 1 ) ;
  while ( lo <= hi && x >= arr [ lo ] && x <= arr [ hi ] ) {
    if ( lo == hi ) {
      if ( arr [ lo ] == x ) return lo ;
      return - 1 ;
    }
    int pos = lo + ( ( ( hi - lo ) / ( arr [ hi ] - arr [ lo ] ) ) * ( x - arr [ lo ] ) ) ;
    if ( arr [ pos ] == x ) return pos ;
    if ( arr [ pos ] < x ) lo = pos + 1 ;
    else hi = pos - 1 ;
  }
  return - 1 ;
}
|||

COUNT_PAIRS_TWO_SORTED_ARRAYS_WHOSE_SUM_EQUAL_GIVEN_VALUE_X_2

static int countPairs ( int arr1 [ ] , int arr2 [ ] , int m , int n , int x ) {
  int count = 0 ;
  int l = 0 , r = n - 1 ;
  while ( l < m && r >= 0 ) {
    if ( ( arr1 [ l ] + arr2 [ r ] ) == x ) {
      l ++ ;
      r -- ;
      count ++ ;
    }
    else if ( ( arr1 [ l ] + arr2 [ r ] ) < x ) l ++ ;
    else r -- ;
  }
  return count ;
}
|||

COUNT_SUBSETS_DISTINCT_EVEN_NUMBERS

static int countSubsets ( int arr [ ] , int n ) {
  HashSet < Integer > us = new HashSet < > ( ) ;
  int even_count = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( arr [ i ] % 2 == 0 ) us . add ( arr [ i ] ) ;
  even_count = us . size ( ) ;
  return ( int ) ( Math . pow ( 2 , even_count ) - 1 ) ;
}
|||

COUNT_NUMBER_OF_OCCURRENCES_OR_FREQUENCY_IN_A_SORTED_ARRAY

static int countOccurrences ( int arr [ ] , int n , int x ) {
  int res = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( x == arr [ i ] ) res ++ ;
  return res ;
}
|||

CONSTRUCT_THE_ROOTED_TREE_BY_USING_START_AND_FINISH_TIME_OF_ITS_DFS_TRAVERSAL

static int [ ] Restore_Tree ( int [ ] S , int [ ] End ) {
  int [ ] Identity = new int [ N ] ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) Identity [ S [ i ] ] = i ;
  int [ ] parent = new int [ N ] ;
  Arrays . fill ( parent , - 1 ) ;
  int curr_parent = Identity [ 0 ] ;
  for ( int j = 1 ;
  j < N ;
  j ++ ) {
    int child = Identity [ j ] ;
    if ( End [ child ] - j > 1 ) {
      parent [ child ] = curr_parent ;
      curr_parent = child ;
    }
    else {
      parent [ child ] = curr_parent ;
      while ( parent [ child ] > - 1 && End [ child ] == End [ parent [ child ] ] ) {
        child = parent [ child ] ;
        curr_parent = parent [ child ] ;
        if ( curr_parent == Identity [ 0 ] ) break ;
      }
    }
  }
  for ( int i = 0 ;
  i < N ;
  i ++ ) parent [ i ] += 1 ;
  return parent ;
}
|||

NUMBER_SUBSEQUENCES_AB_STRING_REPEATED_K_TIMES

static int countOccurrences ( String s , int K ) {
  int n = s . length ( ) ;
  int C = 0 , c1 = 0 , c2 = 0 ;
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

static int countNonEmptySubstr ( String str ) {
  int n = str . length ( ) ;
  return n * ( n + 1 ) / 2 ;
}
|||

MAXIMUM_NUMBER_CHARACTERS_TWO_CHARACTER_STRING_1

static int maximumChars ( String str ) {
  int n = str . length ( ) ;
  int res = - 1 ;
  int [ ] firstInd = new int [ MAX_CHAR ] ;
  for ( int i = 0 ;
  i < MAX_CHAR ;
  i ++ ) firstInd [ i ] = - 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int first_ind = firstInd [ str . charAt ( i ) ] ;
    if ( first_ind == - 1 ) firstInd [ str . charAt ( i ) ] = i ;
    else res = Math . max ( res , Math . abs ( i - first_ind - 1 ) ) ;
  }
  return res ;
}
|||

SUM_SQUARES_BINOMIAL_COEFFICIENTS

static int sumofsquare ( int n ) {
  int [ ] [ ] C = new int [ n + 1 ] [ n + 1 ] ;
  int i , j ;
  for ( i = 0 ;
  i <= n ;
  i ++ ) {
    for ( j = 0 ;
    j <= min ( i , n ) ;
    j ++ ) {
      if ( j == 0 || j == i ) C [ i ] [ j ] = 1 ;
      else C [ i ] [ j ] = C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ] ;
    }
  }
  int sum = 0 ;
  for ( i = 0 ;
  i <= n ;
  i ++ ) sum += ( C [ n ] [ i ] * C [ n ] [ i ] ) ;
  return sum ;
}
|||

PRINT_POSSIBLE_STRINGS_CAN_MADE_PLACING_SPACES_2

static void printSubsequences ( String s ) {
  char [ ] str = s . toCharArray ( ) ;
  int n = str . length ;
  int opsize = ( int ) ( Math . pow ( 2 , n - 1 ) ) ;
  for ( int counter = 0 ;
  counter < opsize ;
  counter ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      System . out . print ( str [ j ] ) ;
      if ( ( counter & ( 1 << j ) ) > 0 ) System . out . print ( " " ) ;
    }
    System . out . println ( ) ;
  }
}
|||

NON_REPEATING_ELEMENT

static int firstNonRepeating ( int arr [ ] , int n ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int j ;
    for ( j = 0 ;
    j < n ;
    j ++ ) if ( i != j && arr [ i ] == arr [ j ] ) break ;
    if ( j == n ) return arr [ i ] ;
  }
  return - 1 ;
}
|||

SUM_OF_ALL_ELEMENTS_UP_TO_NTH_ROW_IN_A_PASCALS_TRIANGLE

static long calculateSum ( int n ) {
  long sum = 0 ;
  for ( int row = 0 ;
  row < n ;
  row ++ ) {
    sum = sum + ( 1 << row ) ;
  }
  return sum ;
}
|||

CHECK_TWO_STRINGS_K_ANAGRAMS_NOT

static boolean arekAnagrams ( String str1 , String str2 , int k ) {
  int n = str1 . length ( ) ;
  if ( str2 . length ( ) != n ) return false ;
  int [ ] count1 = new int [ MAX_CHAR ] ;
  int [ ] count2 = new int [ MAX_CHAR ] ;
  int count = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) count1 [ str1 . charAt ( i ) - 'a' ] ++ ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) count2 [ str2 . charAt ( i ) - 'a' ] ++ ;
  for ( int i = 0 ;
  i < MAX_CHAR ;
  i ++ ) if ( count1 [ i ] > count2 [ i ] ) count = count + Math . abs ( count1 [ i ] - count2 [ i ] ) ;
  return ( count <= k ) ;
}
|||

LONGEST_SPAN_SUM_TWO_BINARY_ARRAYS

static int longestCommonSum ( int n ) {
  int maxLen = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int sum1 = 0 , sum2 = 0 ;
    for ( int j = i ;
    j < n ;
    j ++ ) {
      sum1 += arr1 [ j ] ;
      sum2 += arr2 [ j ] ;
      if ( sum1 == sum2 ) {
        int len = j - i + 1 ;
        if ( len > maxLen ) maxLen = len ;
      }
    }
  }
  return maxLen ;
}
|||

REMAINDER_7_LARGE_NUMBERS

static int remainderWith7 ( String num ) {
  int series [ ] = {
    1 , 3 , 2 , - 1 , - 3 , - 2 };
    int series_index = 0 ;
    int result = 0 ;
    for ( int i = num . length ( ) - 1 ;
    i >= 0 ;
    i -- ) {
      int digit = num . charAt ( i ) - '0' ;
      result += digit * series [ series_index ] ;
      series_index = ( series_index + 1 ) % 6 ;
      result %= 7 ;
    }
    if ( result < 0 ) result = ( result + 7 ) % 7 ;
    return result ;
  }
  |||

LEXICOGRAPHICALLY_PREVIOUS_PERMUTATION_IN_C

static boolean prevPermutation ( char [ ] str ) {
  int n = str . length - 1 ;
  int i = n ;
  while ( i > 0 && str [ i - 1 ] <= str [ i ] ) {
    i -- ;
  }
  if ( i <= 0 ) {
    return false ;
  }
  int j = i - 1 ;
  while ( j + 1 <= n && str [ j + 1 ] <= str [ i - 1 ] ) {
    j ++ ;
  }
  swap ( str , i - 1 , j ) ;
  StringBuilder sb = new StringBuilder ( String . valueOf ( str ) ) ;
  sb . reverse ( ) ;
  str = sb . toString ( ) . toCharArray ( ) ;
  return true ;
}
|||

NUMBER_SUBSEQUENCES_FORM_AI_BJ_CK

static int countSubsequences ( String s ) {
  int aCount = 0 ;
  int bCount = 0 ;
  int cCount = 0 ;
  for ( int i = 0 ;
  i < s . length ( ) ;
  i ++ ) {
    if ( s . charAt ( i ) == 'a' ) aCount = ( 1 + 2 * aCount ) ;
    else if ( s . charAt ( i ) == 'b' ) bCount = ( aCount + 2 * bCount ) ;
    else if ( s . charAt ( i ) == 'c' ) cCount = ( bCount + 2 * cCount ) ;
  }
  return cCount ;
}
|||

PROGRAM_PRINT_IDENTITY_MATRIX_1

static boolean isIdentity ( int mat [ ] [ ] , int N ) {
  for ( int row = 0 ;
  row < N ;
  row ++ ) {
    for ( int col = 0 ;
    col < N ;
    col ++ ) {
      if ( row == col && mat [ row ] [ col ] != 1 ) return false ;
      else if ( row != col && mat [ row ] [ col ] != 0 ) return false ;
    }
  }
  return true ;
}
|||

MAXIMUM_POSSIBLE_DIFFERENCE_TWO_SUBSETS_ARRAY_1

static int maxDiff ( int [ ] arr , int n ) {
  int result = 0 ;
  Arrays . sort ( arr ) ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    if ( arr [ i ] != arr [ i + 1 ] ) result += Math . abs ( arr [ i ] ) ;
    else i ++ ;
  }
  if ( arr [ n - 2 ] != arr [ n - 1 ] ) result += Math . abs ( arr [ n - 1 ] ) ;
  return result ;
}
|||

PROGRAM_PRINT_SUM_GIVEN_NTH_TERM

static int summingSeries ( long n ) {
  int S = 0 ;
  for ( i = 1 ;
  i <= n ;
  i ++ ) S += i * i - ( i - 1 ) * ( i - 1 ) ;
  return S ;
}
|||

PREFIX_SUM_2D_ARRAY

public static void prefixSum2D ( int a [ ] [ ] ) {
  int R = a . length ;
  int C = a [ 0 ] . length ;
  int psa [ ] [ ] = new int [ R ] [ C ] ;
  psa [ 0 ] [ 0 ] = a [ 0 ] [ 0 ] ;
  for ( int i = 1 ;
  i < C ;
  i ++ ) psa [ 0 ] [ i ] = psa [ 0 ] [ i - 1 ] + a [ 0 ] [ i ] ;
  for ( int i = 1 ;
  i < R ;
  i ++ ) psa [ i ] [ 0 ] = psa [ i - 1 ] [ 0 ] + a [ i ] [ 0 ] ;
  for ( int i = 1 ;
  i < R ;
  i ++ ) for ( int j = 1 ;
  j < C ;
  j ++ ) psa [ i ] [ j ] = psa [ i - 1 ] [ j ] + psa [ i ] [ j - 1 ] - psa [ i - 1 ] [ j - 1 ] + a [ i ] [ j ] ;
  for ( int i = 0 ;
  i < R ;
  i ++ ) {
    for ( int j = 0 ;
    j < C ;
    j ++ ) System . out . print ( psa [ i ] [ j ] + " " ) ;
    System . out . println ( ) ;
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

int countSubStr ( char str [ ] , int n ) {
  int m = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( str [ i ] == '1' ) m ++ ;
  }
  return m * ( m - 1 ) / 2 ;
}
|||

CONVERTING_ONE_STRING_USING_APPEND_DELETE_LAST_OPERATIONS

static boolean isConvertible ( String str1 , String str2 , int k ) {
  if ( ( str1 . length ( ) + str2 . length ( ) ) < k ) return true ;
  int commonLength = 0 ;
  for ( int i = 0 ;
  i < Math . min ( str1 . length ( ) , str2 . length ( ) ) ;
  i ++ ) {
    if ( str1 == str2 ) commonLength ++ ;
    else break ;
  }
  if ( ( k - str1 . length ( ) - str2 . length ( ) + 2 * commonLength ) % 2 == 0 ) return true ;
  return false ;
}
|||

FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES_2

int getOddOccurrence ( int ar [ ] , int ar_size ) {
  int i ;
  int res = 0 ;
  for ( i = 0 ;
  i < ar_size ;
  i ++ ) {
    res = res ^ ar [ i ] ;
  }
  return res ;
}
|||

SUM_MIDDLE_ROW_COLUMN_MATRIX

static void middlesum ( int mat [ ] [ ] , int n ) {
  int row_sum = 0 , col_sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) row_sum += mat [ n / 2 ] [ i ] ;
  System . out . println ( "Sum of middle row = " + row_sum ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) col_sum += mat [ i ] [ n / 2 ] ;
  System . out . println ( "Sum of middle column = " + col_sum ) ;
}
|||

K_TH_DISTINCT_OR_NON_REPEATING_ELEMENT_IN_AN_ARRAY

static int printKDistinct ( int arr [ ] , int n , int k ) {
  int dist_count = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int j ;
    for ( j = 0 ;
    j < n ;
    j ++ ) if ( i != j && arr [ j ] == arr [ i ] ) break ;
    if ( j == n ) dist_count ++ ;
    if ( dist_count == k ) return arr [ i ] ;
  }
  return - 1 ;
}
|||

MERGING_INTERVALS

public static void mergeIntervals ( Interval arr [ ] ) {
  Arrays . sort ( arr , new Comparator < Interval > ( ) {
    public int compare ( Interval i1 , Interval i2 ) {
      return i2 . start - i1 . start ;
    }
  }
  ) ;
  int index = 0 ;
  for ( int i = 1 ;
  i < arr . length ;
  i ++ ) {
    if ( arr [ index ] . end >= arr [ i ] . start ) {
      arr [ index ] . end = Math . max ( arr [ index ] . end , arr [ i ] . end ) ;
      arr [ index ] . start = Math . min ( arr [ index ] . start , arr [ i ] . start ) ;
    }
    else {
      arr [ index ] = arr [ i ] ;
      index ++ ;
    }
  }
  System . out . print ( "The Merged Intervals are: " ) ;
  for ( int i = 0 ;
  i <= index ;
  i ++ ) {
    System . out . print ( "[" + arr [ i ] . start + "," + arr [ i ] . end + "]" ) ;
  }
}
|||

FIND_NUMBER_PERFECT_SQUARES_TWO_GIVEN_NUMBERS_1

double countSquares ( int a , int b ) {
  return ( Math . floor ( Math . sqrt ( b ) ) - Math . ceil ( Math . sqrt ( a ) ) + 1 ) ;
}
|||

LARGEST_SUBSET_WHOSE_ALL_ELEMENTS_ARE_FIBONACCI_NUMBERS

public static void findFibSubset ( Integer [ ] x ) {
  Integer max = Collections . max ( Arrays . asList ( x ) ) ;
  List < Integer > fib = new ArrayList < Integer > ( ) ;
  List < Integer > result = new ArrayList < Integer > ( ) ;
  Integer a = 0 ;
  Integer b = 1 ;
  while ( b < max ) {
    Integer c = a + b ;
    a = b ;
    b = c ;
    fib . add ( c ) ;
  }
  for ( Integer i = 0 ;
  i < x . length ;
  i ++ ) {
    if ( fib . contains ( x [ i ] ) ) {
      result . add ( x [ i ] ) ;
    }
  }
  System . out . println ( result ) ;
}
|||

LEXICOGRAPHICAL_CONCATENATION_SUBSTRINGS_STRING

static String lexicographicSubConcat ( String s ) {
  int n = s . length ( ) ;
  int sub_count = n * ( n + 1 ) / 2 ;
  String [ ] arr = new String [ sub_count ] ;
  int index = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) for ( int len = 1 ;
  len <= n - i ;
  len ++ ) {
    arr [ index ++ ] = s . substring ( i , i + len ) ;
  }
  Arrays . sort ( arr ) ;
  String res = "" ;
  for ( int i = 0 ;
  i < sub_count ;
  i ++ ) res += arr [ i ] ;
  return res ;
}
|||

COUNT_OPERATIONS_MAKE_STRINGAB_FREE

static int abFree ( char [ ] s ) {
  int b_count = 0 ;
  int res = 0 ;
  for ( int i = 0 ;
  i < s . length ;
  i ++ ) {
    if ( s [ s . length - i - 1 ] == 'a' ) {
      res = ( res + b_count ) ;
      b_count = ( b_count * 2 ) ;
    }
    else {
      b_count += 1 ;
    }
  }
  return res ;
}
|||

MAXIMUM_HEIGHT_OF_TRIANGULAR_ARRANGEMENT_OF_ARRAY_VALUES_1

static int MaximumHeight ( int a [ ] , int n ) {
  return ( int ) Math . floor ( ( - 1 + Math . sqrt ( 1 + ( 8 * n ) ) ) / 2 ) ;
}
|||

MAXIMIZE_VOLUME_CUBOID_GIVEN_SUM_SIDES

static int maxvolume ( int s ) {
  int maxvalue = 0 ;
  for ( int i = 1 ;
  i <= s - 2 ;
  i ++ ) {
    for ( int j = 1 ;
    j <= s - 1 ;
    j ++ ) {
      int k = s - i - j ;
      maxvalue = Math . max ( maxvalue , i * j * k ) ;
    }
  }
  return maxvalue ;
}
|||

PROGRAM_DECIMAL_HEXADECIMAL_CONVERSION

static void decToHexa ( int n ) {
  char [ ] hexaDeciNum = new char [ 100 ] ;
  int i = 0 ;
  while ( n != 0 ) {
    int temp = 0 ;
    temp = n % 16 ;
    if ( temp < 10 ) {
      hexaDeciNum [ i ] = ( char ) ( temp + 48 ) ;
      i ++ ;
    }
    else {
      hexaDeciNum [ i ] = ( char ) ( temp + 55 ) ;
      i ++ ;
    }
    n = n / 16 ;
  }
  for ( int j = i - 1 ;
  j >= 0 ;
  j -- ) System . out . print ( hexaDeciNum [ j ] ) ;
}
|||

SMALLEST_SUBARRAY_WITH_ALL_OCCURRENCES_OF_A_MOST_FREQUENT_ELEMENT

static void smallestSubsegment ( int a [ ] , int n ) {
  HashMap < Integer , Integer > left = new HashMap < Integer , Integer > ( ) ;
  HashMap < Integer , Integer > count = new HashMap < Integer , Integer > ( ) ;
  int mx = 0 ;
  int mn = - 1 , strindex = - 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int x = a [ i ] ;
    if ( count . get ( x ) == null ) {
      left . put ( x , i ) ;
      count . put ( x , 1 ) ;
    }
    else count . put ( x , count . get ( x ) + 1 ) ;
    if ( count . get ( x ) > mx ) {
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
  i ++ ) System . out . print ( a [ i ] + " " ) ;
}
|||

FIND_LAST_INDEX_CHARACTER_STRING_1

static int findLastIndex ( String str , Character x ) {
  for ( int i = str . length ( ) - 1 ;
  i >= 0 ;
  i -- ) if ( str . charAt ( i ) == x ) return i ;
  return - 1 ;
}
|||

RECAMANS_SEQUENCE

static void recaman ( int n ) {
  int arr [ ] = new int [ n ] ;
  arr [ 0 ] = 0 ;
  System . out . print ( arr [ 0 ] + " ," ) ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    int curr = arr [ i - 1 ] - i ;
    int j ;
    for ( j = 0 ;
    j < i ;
    j ++ ) {
      if ( ( arr [ j ] == curr ) || curr < 0 ) {
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

static char getSecondMostFreq ( String str ) {
  int [ ] count = new int [ NO_OF_CHARS ] ;
  int i ;
  for ( i = 0 ;
  i < str . length ( ) ;
  i ++ ) ( count [ str . charAt ( i ) ] ) ++ ;
  int first = 0 , second = 0 ;
  for ( i = 0 ;
  i < NO_OF_CHARS ;
  i ++ ) {
    if ( count [ i ] > count [ first ] ) {
      second = first ;
      first = i ;
    }
    else if ( count [ i ] > count [ second ] && count [ i ] != count [ first ] ) second = i ;
  }
  return ( char ) second ;
}
|||

FIND_MAXIMUM_HEIGHT_PYRAMID_FROM_THE_GIVEN_ARRAY_OF_OBJECTS

static int maxLevel ( int [ ] boxes , int n ) {
  Arrays . sort ( boxes ) ;
  int ans = 1 ;
  int prev_width = boxes [ 0 ] ;
  int prev_count = 1 ;
  int curr_count = 0 ;
  int curr_width = 0 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    curr_width += boxes [ i ] ;
    curr_count += 1 ;
    if ( curr_width > prev_width && curr_count > prev_count ) {
      prev_width = curr_width ;
      prev_count = curr_count ;
      curr_count = 0 ;
      curr_width = 0 ;
      ans ++ ;
    }
  }
  return ans ;
}
|||

COUNTING_INVERSIONS

static int getInvCount ( int n ) {
  int inv_count = 0 ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) for ( int j = i + 1 ;
  j < n ;
  j ++ ) if ( arr [ i ] > arr [ j ] ) inv_count ++ ;
  return inv_count ;
}
|||

SQUARES_OF_MATRIX_DIAGONAL_ELEMENTS

static void diagonalsquare ( int mat [ ] [ ] , int row , int column ) {
  System . out . print ( "Diagonal one : " ) ;
  for ( int i = 0 ;
  i < row ;
  i ++ ) {
    for ( int j = 0 ;
    j < column ;
    j ++ ) if ( i == j ) System . out . print ( mat [ i ] [ j ] * mat [ i ] [ j ] + " " ) ;
  }
  System . out . println ( ) ;
  System . out . print ( "Diagonal two : " ) ;
  for ( int i = 0 ;
  i < row ;
  i ++ ) {
    for ( int j = 0 ;
    j < column ;
    j ++ ) if ( i + j == column - 1 ) System . out . print ( mat [ i ] [ j ] * mat [ i ] [ j ] + " " ) ;
  }
}
|||

ROW_WISE_COMMON_ELEMENTS_TWO_DIAGONALS_SQUARE_MATRIX

static int countCommon ( int mat [ ] [ ] , int n ) {
  int res = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( mat [ i ] [ i ] == mat [ i ] [ n - i - 1 ] ) res ++ ;
  return res ;
}
|||

EULERIAN_NUMBER

public static int eulerian ( int n , int m ) {
  if ( m >= n || n == 0 ) return 0 ;
  if ( m == 0 ) return 1 ;
  return ( n - m ) * eulerian ( n - 1 , m - 1 ) + ( m + 1 ) * eulerian ( n - 1 , m ) ;
}
|||

EULERS_CRITERION_CHECK_IF_SQUARE_ROOT_UNDER_MODULO_P_EXISTS

static boolean squareRootExists ( int n , int p ) {
  n = n % p ;
  for ( int x = 2 ;
  x < p ;
  x ++ ) if ( ( x * x ) % p == n ) return true ;
  return false ;
}
|||

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX_3

static int numberOfPaths ( int m , int n ) {
  int path = 1 ;
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

static int maximumDifferenceSum ( int arr [ ] , int N ) {
  int dp [ ] [ ] = new int [ N ] [ 2 ] ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) dp [ i ] [ 0 ] = dp [ i ] [ 1 ] = 0 ;
  for ( int i = 0 ;
  i < ( N - 1 ) ;
  i ++ ) {
    dp [ i + 1 ] [ 0 ] = Math . max ( dp [ i ] [ 0 ] , dp [ i ] [ 1 ] + Math . abs ( 1 - arr [ i ] ) ) ;
    dp [ i + 1 ] [ 1 ] = Math . max ( dp [ i ] [ 0 ] + Math . abs ( arr [ i + 1 ] - 1 ) , dp [ i ] [ 1 ] + Math . abs ( arr [ i + 1 ] - arr [ i ] ) ) ;
  }
  return Math . max ( dp [ N - 1 ] [ 0 ] , dp [ N - 1 ] [ 1 ] ) ;
}
|||

STERN_BROCOT_SEQUENCE

static void SternSequenceFunc ( Vector < Integer > BrocotSequence , int n ) {
  for ( int i = 1 ;
  BrocotSequence . size ( ) < n ;
  i ++ ) {
    int considered_element = BrocotSequence . get ( i ) ;
    int precedent = BrocotSequence . get ( i - 1 ) ;
    BrocotSequence . add ( considered_element + precedent ) ;
    BrocotSequence . add ( considered_element ) ;
  }
  for ( int i = 0 ;
  i < 15 ;
  ++ i ) System . out . print ( BrocotSequence . get ( i ) + " " ) ;
}
|||

NUMBER_SUBSEQUENCES_STRING_DIVISIBLE_N

static int countDivisibleSubseq ( String str , int n ) {
  int len = str . length ( ) ;
  int dp [ ] [ ] = new int [ len ] [ n ] ;
  dp [ 0 ] [ ( str . charAt ( 0 ) - '0' ) % n ] ++ ;
  for ( int i = 1 ;
  i < len ;
  i ++ ) {
    dp [ i ] [ ( str . charAt ( i ) - '0' ) % n ] ++ ;
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      dp [ i ] [ j ] += dp [ i - 1 ] [ j ] ;
      dp [ i ] [ ( j * 10 + ( str . charAt ( i ) - '0' ) ) % n ] += dp [ i - 1 ] [ j ] ;
    }
  }
  return dp [ len - 1 ] [ 0 ] ;
}
|||

HOW_TO_BEGIN_WITH_COMPETITIVE_PROGRAMMING

static int search ( int arr [ ] , int n , int x ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] == x ) return i ;
  }
  return - 1 ;
}
|||

COUNT_PAIRS_WITH_GIVEN_SUM_1

static int getPairsCount ( int n , int sum ) {
  HashMap < Integer , Integer > hm = new HashMap < > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ! hm . containsKey ( arr [ i ] ) ) hm . put ( arr [ i ] , 0 ) ;
    hm . put ( arr [ i ] , hm . get ( arr [ i ] ) + 1 ) ;
  }
  int twice_count = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( hm . get ( sum - arr [ i ] ) != null ) twice_count += hm . get ( sum - arr [ i ] ) ;
    if ( sum - arr [ i ] == arr [ i ] ) twice_count -- ;
  }
  return twice_count / 2 ;
}
|||

FIND_THE_MINIMUM_DISTANCE_BETWEEN_TWO_NUMBERS

int minDist ( int arr [ ] , int n , int x , int y ) {
  int i , j ;
  int min_dist = Integer . MAX_VALUE ;
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    for ( j = i + 1 ;
    j < n ;
    j ++ ) {
      if ( ( x == arr [ i ] && y == arr [ j ] || y == arr [ i ] && x == arr [ j ] ) && min_dist > Math . abs ( i - j ) ) min_dist = Math . abs ( i - j ) ;
    }
  }
  return min_dist ;
}
|||

FIND_REPETITIVE_ELEMENT_1_N_1_2

static int findRepeating ( int arr [ ] , int n ) {
  int res = 0 ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) res = res ^ ( i + 1 ) ^ arr [ i ] ;
  res = res ^ arr [ n - 1 ] ;
  return res ;
}
|||

SHORTEST_PATH_EXACTLY_K_EDGES_DIRECTED_WEIGHTED_GRAPH_1

int shortestPath ( int graph [ ] [ ] , int u , int v , int k ) {
  int sp [ ] [ ] [ ] = new int [ V ] [ V ] [ k + 1 ] ;
  for ( int e = 0 ;
  e <= k ;
  e ++ ) {
    for ( int i = 0 ;
    i < V ;
    i ++ ) {
      for ( int j = 0 ;
      j < V ;
      j ++ ) {
        sp [ i ] [ j ] [ e ] = INF ;
        if ( e == 0 && i == j ) sp [ i ] [ j ] [ e ] = 0 ;
        if ( e == 1 && graph [ i ] [ j ] != INF ) sp [ i ] [ j ] [ e ] = graph [ i ] [ j ] ;
        if ( e > 1 ) {
          for ( int a = 0 ;
          a < V ;
          a ++ ) {
            if ( graph [ i ] [ a ] != INF && i != a && j != a && sp [ a ] [ j ] [ e - 1 ] != INF ) sp [ i ] [ j ] [ e ] = Math . min ( sp [ i ] [ j ] [ e ] , graph [ i ] [ a ] + sp [ a ] [ j ] [ e - 1 ] ) ;
          }
        }
      }
    }
  }
  return sp [ u ] [ v ] [ k ] ;
}
|||

LONGEST_SUBARRAY_NOT_K_DISTINCT_ELEMENTS

static void longest ( int a [ ] , int n , int k ) {
  int [ ] freq = new int [ 7 ] ;
  int start = 0 , end = 0 , now = 0 , l = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    freq [ a [ i ] ] ++ ;
    if ( freq [ a [ i ] ] == 1 ) now ++ ;
    while ( now > k ) {
      freq [ a [ l ] ] -- ;
      if ( freq [ a [ l ] ] == 0 ) now -- ;
      l ++ ;
    }
    if ( i - l + 1 >= end - start + 1 ) {
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

static int maxXOR ( int mat [ ] [ ] , int N ) {
  int r_xor , c_xor ;
  int max_xor = 0 ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    r_xor = 0 ;
    c_xor = 0 ;
    for ( int j = 0 ;
    j < N ;
    j ++ ) {
      r_xor = r_xor ^ mat [ i ] [ j ] ;
      c_xor = c_xor ^ mat [ j ] [ i ] ;
    }
    if ( max_xor < Math . max ( r_xor , c_xor ) ) max_xor = Math . max ( r_xor , c_xor ) ;
  }
  return max_xor ;
}
|||

LENGTH_LONGEST_SUB_STRING_CAN_MAKE_REMOVED

static int longestNull ( String str ) {
  ArrayList < Pair > arr = new ArrayList < > ( ) ;
  arr . add ( new Pair ( '@' , - 1 ) ) ;
  int maxlen = 0 ;
  for ( int i = 0 ;
  i < str . length ( ) ;
  ++ i ) {
    arr . add ( new Pair ( str . charAt ( i ) , i ) ) ;
    while ( arr . size ( ) >= 3 && arr . get ( arr . size ( ) - 3 ) . first == '1' && arr . get ( arr . size ( ) - 2 ) . first == '0' && arr . get ( arr . size ( ) - 1 ) . first == '0' ) {
      arr . remove ( arr . size ( ) - 3 ) ;
      arr . remove ( arr . size ( ) - 2 ) ;
      arr . remove ( arr . size ( ) - 1 ) ;
    }
    int tmp = arr . get ( arr . size ( ) - 1 ) . second ;
    maxlen = Math . max ( maxlen , i - tmp ) ;
  }
  return maxlen ;
}
|||

LONGEST_ALTERNATING_SUB_ARRAY_STARTING_EVERY_INDEX_BINARY_ARRAY

static void alternateSubarray ( boolean arr [ ] , int n ) {
  int len [ ] = new int [ n ] ;
  len [ n - 1 ] = 1 ;
  for ( int i = n - 2 ;
  i >= 0 ;
  -- i ) {
    if ( arr [ i ] ^ arr [ i + 1 ] == true ) len [ i ] = len [ i + 1 ] + 1 ;
    else len [ i ] = 1 ;
  }
  for ( int i = 0 ;
  i < n ;
  ++ i ) System . out . print ( len [ i ] + " " ) ;
}
|||

WILDCARD_CHARACTER_MATCHING

static boolean match ( String first , String second ) {
  if ( first . length ( ) == 0 && second . length ( ) == 0 ) return true ;
  if ( first . length ( ) > 1 && first . charAt ( 0 ) == '*' && second . length ( ) == 0 ) return false ;
  if ( ( first . length ( ) > 1 && first . charAt ( 0 ) == '?' ) || ( first . length ( ) != 0 && second . length ( ) != 0 && first . charAt ( 0 ) == second . charAt ( 0 ) ) ) return match ( first . substring ( 1 ) , second . substring ( 1 ) ) ;
  if ( first . length ( ) > 0 && first . charAt ( 0 ) == '*' ) return match ( first . substring ( 1 ) , second ) || match ( first , second . substring ( 1 ) ) ;
  return false ;
}
|||

FIND_FACTORIAL_NUMBERS_LESS_EQUAL_N

static void printFactorialNums ( int n ) {
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

static int countFriendsPairings ( int n ) {
  int a = 1 , b = 2 , c = 0 ;
  if ( n <= 2 ) {
    return n ;
  }
  for ( int i = 3 ;
  i <= n ;
  i ++ ) {
    c = b + ( i - 1 ) * a ;
    a = b ;
    b = c ;
  }
  return c ;
}
|||

FIND_THE_LARGEST_RECTANGLE_OF_1S_WITH_SWAPPING_OF_COLUMNS_ALLOWED

static int maxArea ( int mat [ ] [ ] ) {
  int hist [ ] [ ] = new int [ R + 1 ] [ C + 1 ] ;
  for ( int i = 0 ;
  i < C ;
  i ++ ) {
    hist [ 0 ] [ i ] = mat [ 0 ] [ i ] ;
    for ( int j = 1 ;
    j < R ;
    j ++ ) {
      hist [ j ] [ i ] = ( mat [ j ] [ i ] == 0 ) ? 0 : hist [ j - 1 ] [ i ] + 1 ;
    }
  }
  for ( int i = 0 ;
  i < R ;
  i ++ ) {
    int count [ ] = new int [ R + 1 ] ;
    for ( int j = 0 ;
    j < C ;
    j ++ ) {
      count [ hist [ i ] [ j ] ] ++ ;
    }
    int col_no = 0 ;
    for ( int j = R ;
    j >= 0 ;
    j -- ) {
      if ( count [ j ] > 0 ) {
        for ( int k = 0 ;
        k < count [ j ] ;
        k ++ ) {
          hist [ i ] [ col_no ] = j ;
          col_no ++ ;
        }
      }
    }
  }
  int curr_area , max_area = 0 ;
  for ( int i = 0 ;
  i < R ;
  i ++ ) {
    for ( int j = 0 ;
    j < C ;
    j ++ ) {
      curr_area = ( j + 1 ) * hist [ i ] [ j ] ;
      if ( curr_area > max_area ) {
        max_area = curr_area ;
      }
    }
  }
  return max_area ;
}
|||

SUM_SEQUENCE_2_22_222

static double sumOfSeries ( int n ) {
  return 0.0246 * ( Math . pow ( 10 , n ) - 1 - ( 9 * n ) ) ;
}
|||

PROGRAM_FIRST_FIT_ALGORITHM_MEMORY_MANAGEMENT

static void firstFit ( int blockSize [ ] , int m , int processSize [ ] , int n ) {
  int allocation [ ] = new int [ n ] ;
  for ( int i = 0 ;
  i < allocation . length ;
  i ++ ) allocation [ i ] = - 1 ;
  for ( int i = 0 ;
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
  System . out . println ( "\nProcess No.\tProcess Size\tBlock no." ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    System . out . print ( " " + ( i + 1 ) + "\t\t" + processSize [ i ] + "\t\t" ) ;
    if ( allocation [ i ] != - 1 ) System . out . print ( allocation [ i ] + 1 ) ;
    else System . out . print ( "Not Allocated" ) ;
    System . out . println ( ) ;
  }
}
|||

CHECK_IF_A_NUMBER_IS_POWER_OF_ANOTHER_NUMBER

public static boolean isPower ( int x , int y ) {
  if ( x == 1 ) return ( y == 1 ) ;
  int pow = 1 ;
  while ( pow < y ) pow = pow * x ;
  return ( pow == y ) ;
}
|||

DIVIDE_LARGE_NUMBER_REPRESENTED_STRING

static String longDivision ( String number , int divisor ) {
  String ans = "" ;
  int idx = 0 ;
  char [ ] num = number . toCharArray ( ) ;
  int temp = num [ idx ] - '0' ;
  while ( temp < divisor ) temp = temp * 10 + ( num [ ++ idx ] - '0' ) ;
  idx += 1 ;
  while ( num . length > idx ) {
    ans += ( temp / divisor ) ;
    temp = ( temp % divisor ) * 10 + num [ idx ++ ] - '0' ;
  }
  if ( ans . length ( ) == 0 ) return "0" ;
  return ans ;
}
|||

FIND_ROW_NUMBER_BINARY_MATRIX_MAXIMUM_NUMBER_1S

static void findMax ( int arr [ ] [ ] ) {
  int row = 0 , i , j ;
  for ( i = 0 , j = N - 1 ;
  i < N ;
  i ++ ) {
    while ( j >= 0 && arr [ i ] [ j ] == 1 ) {
      row = i ;
      j -- ;
    }
  }
  System . out . print ( "Row number = " + ( row + 1 ) ) ;
  System . out . print ( ", MaxCount = " + ( N - 1 - j ) ) ;
}
|||

MINIMUM_ROTATIONS_REQUIRED_GET_STRING

static int findRotations ( String str ) {
  String tmp = str + str ;
  int n = str . length ( ) ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) {
    String substring = tmp . substring ( i , str . length ( ) ) ;
    if ( str == substring ) return i ;
  }
  return n ;
}
|||

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX

static int numberOfPaths ( int m , int n ) {
  if ( m == 1 || n == 1 ) return 1 ;
  return numberOfPaths ( m - 1 , n ) + numberOfPaths ( m , n - 1 ) ;
}
|||

N_TH_NUMBER_WHOSE_SUM_OF_DIGITS_IS_TEN_1

public static int findNth ( int n ) {
  int count = 0 ;
  for ( int curr = 19 ;
  ;
  curr += 9 ) {
    int sum = 0 ;
    for ( int x = curr ;
    x > 0 ;
    x = x / 10 ) sum = sum + x % 10 ;
    if ( sum == 10 ) count ++ ;
    if ( count == n ) return curr ;
  }
}
|||

SUM_NODES_K_TH_LEVEL_TREE_REPRESENTED_STRING_1

static int sumAtKthLevel ( String tree , int k , int level ) {
  if ( tree . charAt ( i ++ ) == '(' ) {
    if ( tree . charAt ( i ) == ')' ) return 0 ;
    int sum = 0 ;
    if ( level == k ) sum = tree . charAt ( i ) - '0' ;
    ++ i ;
    int leftsum = sumAtKthLevel ( tree , k , level + 1 ) ;
    ++ i ;
    int rightsum = sumAtKthLevel ( tree , k , level + 1 ) ;
    ++ i ;
    return sum + leftsum + rightsum ;
  }
  return Integer . MIN_VALUE ;
}
|||

COUNT_OFDIFFERENT_WAYS_EXPRESS_N_SUM_1_3_4

static int countWays ( int n ) {
  int DP [ ] = new int [ n + 1 ] ;
  DP [ 0 ] = DP [ 1 ] = DP [ 2 ] = 1 ;
  DP [ 3 ] = 2 ;
  for ( int i = 4 ;
  i <= n ;
  i ++ ) DP [ i ] = DP [ i - 1 ] + DP [ i - 3 ] + DP [ i - 4 ] ;
  return DP [ n ] ;
}
|||

MAXIMUM_EQULIBRIUM_SUM_ARRAY

static int findMaxSum ( int [ ] arr , int n ) {
  int res = Integer . MIN_VALUE ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int prefix_sum = arr [ i ] ;
    for ( int j = 0 ;
    j < i ;
    j ++ ) prefix_sum += arr [ j ] ;
    int suffix_sum = arr [ i ] ;
    for ( int j = n - 1 ;
    j > i ;
    j -- ) suffix_sum += arr [ j ] ;
    if ( prefix_sum == suffix_sum ) res = Math . max ( res , prefix_sum ) ;
  }
  return res ;
}
|||

STEINS_ALGORITHM_FOR_FINDING_GCD_1

static int gcd ( int a , int b ) {
  if ( a == b ) return a ;
  if ( a == 0 ) return b ;
  if ( b == 0 ) return a ;
  if ( ( ~ a & 1 ) == 1 ) {
    if ( ( b & 1 ) == 1 ) return gcd ( a >> 1 , b ) ;
    else return gcd ( a >> 1 , b >> 1 ) << 1 ;
  }
  if ( ( ~ b & 1 ) == 1 ) return gcd ( a , b >> 1 ) ;
  if ( a > b ) return gcd ( ( a - b ) >> 1 , b ) ;
  return gcd ( ( b - a ) >> 1 , a ) ;
}
|||

PROGRAM_TO_FIND_THE_VOLUME_OF_A_TRIANGULAR_PRISM

static float findVolume ( float l , float b , float h ) {
  float volume = ( l * b * h ) / 2 ;
  return volume ;
}
|||

FIND_RECTANGLE_BINARY_MATRIX_CORNERS_1

static boolean isRectangle ( int m [ ] [ ] ) {
  int rows = m . length ;
  if ( rows == 0 ) return false ;
  int columns = m [ 0 ] . length ;
  for ( int y1 = 0 ;
  y1 < rows ;
  y1 ++ ) for ( int x1 = 0 ;
  x1 < columns ;
  x1 ++ ) if ( m [ y1 ] [ x1 ] == 1 ) for ( int y2 = y1 + 1 ;
  y2 < rows ;
  y2 ++ ) for ( int x2 = x1 + 1 ;
  x2 < columns ;
  x2 ++ ) if ( m [ y1 ] [ x2 ] == 1 && m [ y2 ] [ x1 ] == 1 && m [ y2 ] [ x2 ] == 1 ) return true ;
  return false ;
}
|||

CHECK_IF_STRING_REMAINS_PALINDROME_AFTER_REMOVING_GIVEN_NUMBER_OF_CHARACTERS

static boolean isPossible ( String str , int n ) {
  int len = str . length ( ) ;
  if ( len >= n ) return true ;
  return false ;
}
|||

CHECK_STAR_GRAPH

static boolean checkStar ( int mat [ ] [ ] ) {
  int vertexD1 = 0 , vertexDn_1 = 0 ;
  if ( size == 1 ) return ( mat [ 0 ] [ 0 ] == 0 ) ;
  if ( size == 2 ) return ( mat [ 0 ] [ 0 ] == 0 && mat [ 0 ] [ 1 ] == 1 && mat [ 1 ] [ 0 ] == 1 && mat [ 1 ] [ 1 ] == 0 ) ;
  for ( int i = 0 ;
  i < size ;
  i ++ ) {
    int degreeI = 0 ;
    for ( int j = 0 ;
    j < size ;
    j ++ ) if ( mat [ i ] [ j ] == 1 ) degreeI ++ ;
    if ( degreeI == 1 ) vertexD1 ++ ;
    else if ( degreeI == size - 1 ) vertexDn_1 ++ ;
  }
  return ( vertexD1 == ( size - 1 ) && vertexDn_1 == 1 ) ;
}
|||

ROOTS_OF_UNITY

static void printRoots ( int n ) {
  double theta = 3.14 * 2 / n ;
  for ( int k = 0 ;
  k < n ;
  k ++ ) {
    double real = Math . cos ( k * theta ) ;
    double img = Math . sin ( k * theta ) ;
    System . out . println ( real ) ;
    if ( img >= 0 ) System . out . println ( " + i " ) ;
    else System . out . println ( " - i " ) ;
    System . out . println ( Math . abs ( img ) ) ;
  }
}
|||

FIND_LARGEST_D_IN_ARRAY_SUCH_THAT_A_B_C_D

static int findLargestd ( int [ ] S , int n ) {
  boolean found = false ;
  Arrays . sort ( S ) ;
  for ( int i = n - 1 ;
  i >= 0 ;
  i -- ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( i == j ) continue ;
      for ( int k = j + 1 ;
      k < n ;
      k ++ ) {
        if ( i == k ) continue ;
        for ( int l = k + 1 ;
        l < n ;
        l ++ ) {
          if ( i == l ) continue ;
          if ( S [ i ] == S [ j ] + S [ k ] + S [ l ] ) {
            found = true ;
            return S [ i ] ;
          }
        }
      }
    }
  }
  if ( found == false ) return Integer . MAX_VALUE ;
  return - 1 ;
}
|||

GIVEN_NUMBER_STRING_FIND_NUMBER_CONTIGUOUS_SUBSEQUENCES_RECURSIVELY_ADD_9_SET_2

static int count9s ( char number [ ] ) {
  int n = number . length ;
  int d [ ] = new int [ 9 ] ;
  d [ 0 ] = 1 ;
  int result = 0 ;
  int mod_sum = 0 , continuous_zero = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( number [ i ] - '0' ) == 0 ) {
      continuous_zero ++ ;
    }
    else {
      continuous_zero = 0 ;
    }
    mod_sum += ( number [ i ] - '0' ) ;
    mod_sum %= 9 ;
    result += d [ mod_sum ] ;
    d [ mod_sum ] ++ ;
    result -= continuous_zero ;
  }
  return result ;
}
|||

LEXICOGRAPHICAL_MAXIMUM_SUBSTRING_STRING

static String LexicographicalMaxString ( String str ) {
  String mx = "" ;
  for ( int i = 0 ;
  i < str . length ( ) ;
  ++ i ) {
    if ( mx . compareTo ( str . substring ( i ) ) <= 0 ) {
      mx = str . substring ( i ) ;
    }
  }
  return mx ;
}
|||

CHECK_TWO_GIVEN_SETS_DISJOINT_1

boolean aredisjoint ( int set1 [ ] , int set2 [ ] ) {
  int i = 0 , j = 0 ;
  Arrays . sort ( set1 ) ;
  Arrays . sort ( set2 ) ;
  while ( i < set1 . length && j < set2 . length ) {
    if ( set1 [ i ] < set2 [ j ] ) i ++ ;
    else if ( set1 [ i ] > set2 [ j ] ) j ++ ;
    else return false ;
  }
  return true ;
}
|||

EQUILIBRIUM_INDEX_OF_AN_ARRAY_1

int equilibrium ( int arr [ ] , int n ) {
  int sum = 0 ;
  int leftsum = 0 ;
  for ( int i = 0 ;
  i < n ;
  ++ i ) sum += arr [ i ] ;
  for ( int i = 0 ;
  i < n ;
  ++ i ) {
    sum -= arr [ i ] ;
    if ( leftsum == sum ) return i ;
    leftsum += arr [ i ] ;
  }
  return - 1 ;
}
|||

AREA_CIRCUMSCRIBED_CIRCLE_SQUARE

static float areacircumscribed ( float a ) {
  float PI = 3.14159265f ;
  return ( a * a * ( PI / 2 ) ) ;
}
|||

LONGEST_REPEATING_AND_NON_OVERLAPPING_SUBSTRING

static String longestRepeatedSubstring ( String str ) {
  int n = str . length ( ) ;
  int LCSRe [ ] [ ] = new int [ n + 1 ] [ n + 1 ] ;
  String res = "" ;
  int res_length = 0 ;
  int i , index = 0 ;
  for ( i = 1 ;
  i <= n ;
  i ++ ) {
    for ( int j = i + 1 ;
    j <= n ;
    j ++ ) {
      if ( str . charAt ( i - 1 ) == str . charAt ( j - 1 ) && LCSRe [ i - 1 ] [ j - 1 ] < ( j - i ) ) {
        LCSRe [ i ] [ j ] = LCSRe [ i - 1 ] [ j - 1 ] + 1 ;
        if ( LCSRe [ i ] [ j ] > res_length ) {
          res_length = LCSRe [ i ] [ j ] ;
          index = Math . max ( i , index ) ;
        }
      }
      else {
        LCSRe [ i ] [ j ] = 0 ;
      }
    }
  }
  if ( res_length > 0 ) {
    for ( i = index - res_length + 1 ;
    i <= index ;
    i ++ ) {
      res += str . charAt ( i - 1 ) ;
    }
  }
  return res ;
}
|||

HOW_TO_AVOID_OVERFLOW_IN_MODULAR_MULTIPLICATION

static long mulmod ( long a , long b , long mod ) {
  long res = 0 ;
  a = a % mod ;
  while ( b > 0 ) {
    if ( b % 2 == 1 ) {
      res = ( res + a ) % mod ;
    }
    a = ( a * 2 ) % mod ;
    b /= 2 ;
  }
  return res % mod ;
}
|||

PAIR_WITH_GIVEN_PRODUCT_SET_1_FIND_IF_ANY_PAIR_EXISTS_1

static boolean isProduct ( int arr [ ] , int n , int x ) {
  HashSet < Integer > hset = new HashSet < > ( ) ;
  if ( n < 2 ) return false ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] == 0 ) {
      if ( x == 0 ) return true ;
      else continue ;
    }
    if ( x % arr [ i ] == 0 ) {
      if ( hset . contains ( x / arr [ i ] ) ) return true ;
      hset . add ( arr [ i ] ) ;
    }
  }
  return false ;
}
|||

SUM_K_TH_GROUP_ODD_POSITIVE_NUMBERS

public static int kthgroupsum ( int k ) {
  int cur = ( k * ( k - 1 ) ) + 1 ;
  int sum = 0 ;
  while ( k -- > 0 ) {
    sum += cur ;
    cur += 2 ;
  }
  return sum ;
}
|||

FIND_ELEMENTS_ARRAY_LEAST_TWO_GREATER_ELEMENTS_1

static void findElements ( int arr [ ] , int n ) {
  Arrays . sort ( arr ) ;
  for ( int i = 0 ;
  i < n - 2 ;
  i ++ ) System . out . print ( arr [ i ] + " " ) ;
}
|||

MINIMUM_STEPS_TO_DELETE_A_STRING_AFTER_REPEATED_DELETION_OF_PALINDROME_SUBSTRINGS

static int minStepToDeleteString ( String str ) {
  int N = str . length ( ) ;
  int [ ] [ ] dp = new int [ N + 1 ] [ N + 1 ] ;
  for ( int i = 0 ;
  i <= N ;
  i ++ ) for ( int j = 0 ;
  j <= N ;
  j ++ ) dp [ i ] [ j ] = 0 ;
  for ( int len = 1 ;
  len <= N ;
  len ++ ) {
    for ( int i = 0 , j = len - 1 ;
    j < N ;
    i ++ , j ++ ) {
      if ( len == 1 ) dp [ i ] [ j ] = 1 ;
      else {
        dp [ i ] [ j ] = 1 + dp [ i + 1 ] [ j ] ;
        if ( str . charAt ( i ) == str . charAt ( i + 1 ) ) dp [ i ] [ j ] = Math . min ( 1 + dp [ i + 2 ] [ j ] , dp [ i ] [ j ] ) ;
        for ( int K = i + 2 ;
        K <= j ;
        K ++ ) if ( str . charAt ( i ) == str . charAt ( K ) ) dp [ i ] [ j ] = Math . min ( dp [ i + 1 ] [ K - 1 ] + dp [ K + 1 ] [ j ] , dp [ i ] [ j ] ) ;
      }
    }
  }
  return dp [ 0 ] [ N - 1 ] ;
}
|||

CALCULATE_AREA_TETRAHEDRON

static double vol_tetra ( int side ) {
  double volume = ( Math . pow ( side , 3 ) / ( 6 * Math . sqrt ( 2 ) ) ) ;
  return volume ;
}
|||

SIEVE_OF_ATKIN

static int SieveOfAtkin ( int limit ) {
  if ( limit > 2 ) System . out . print ( 2 + " " ) ;
  if ( limit > 3 ) System . out . print ( 3 + " " ) ;
  boolean sieve [ ] = new boolean [ limit ] ;
  for ( int i = 0 ;
  i < limit ;
  i ++ ) sieve [ i ] = false ;
  for ( int x = 1 ;
  x * x < limit ;
  x ++ ) {
    for ( int y = 1 ;
    y * y < limit ;
    y ++ ) {
      int n = ( 4 * x * x ) + ( y * y ) ;
      if ( n <= limit && ( n % 12 == 1 || n % 12 == 5 ) ) sieve [ n ] ^= true ;
      n = ( 3 * x * x ) + ( y * y ) ;
      if ( n <= limit && n % 12 == 7 ) sieve [ n ] ^= true ;
      n = ( 3 * x * x ) - ( y * y ) ;
      if ( x > y && n <= limit && n % 12 == 11 ) sieve [ n ] ^= true ;
    }
  }
  for ( int r = 5 ;
  r * r < limit ;
  r ++ ) {
    if ( sieve [ r ] ) {
      for ( int i = r * r ;
      i < limit ;
      i += r * r ) sieve [ i ] = false ;
    }
  }
  for ( int a = 5 ;
  a < limit ;
  a ++ ) if ( sieve [ a ] ) System . out . print ( a + " " ) ;
  return 0 ;
}
|||

LENGTH_OF_THE_LONGEST_ARITHMATIC_PROGRESSION_IN_A_SORTED_ARRAY

static int lenghtOfLongestAP ( int set [ ] , int n ) {
  if ( n <= 2 ) return n ;
  int L [ ] [ ] = new int [ n ] [ n ] ;
  int llap = 2 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) L [ i ] [ n - 1 ] = 2 ;
  for ( int j = n - 2 ;
  j >= 1 ;
  j -- ) {
    int i = j - 1 , k = j + 1 ;
    while ( i >= 0 && k <= n - 1 ) {
      if ( set [ i ] + set [ k ] < 2 * set [ j ] ) k ++ ;
      else if ( set [ i ] + set [ k ] > 2 * set [ j ] ) {
        L [ i ] [ j ] = 2 ;
        i -- ;
      }
      else {
        L [ i ] [ j ] = L [ j ] [ k ] + 1 ;
        llap = Math . max ( llap , L [ i ] [ j ] ) ;
        i -- ;
        k ++ ;
      }
    }
    while ( i >= 0 ) {
      L [ i ] [ j ] = 2 ;
      i -- ;
    }
  }
  return llap ;
}
|||

COUNT_GROUPINGS_NUMBER_SUM_DIGITS_EVERY_SUB_GROUP_LESS_EQUALS_IMMEDIATE_RIGHT_SUB_GROUP_1

static int countGroups ( int position , int previous_sum , int length , char [ ] num ) {
  if ( position == length ) return 1 ;
  if ( dp [ position ] [ previous_sum ] != - 1 ) return dp [ position ] [ previous_sum ] ;
  dp [ position ] [ previous_sum ] = 0 ;
  int res = 0 ;
  int sum = 0 ;
  for ( int i = position ;
  i < length ;
  i ++ ) {
    sum += ( num [ i ] - '0' ) ;
    if ( sum >= previous_sum ) res += countGroups ( i + 1 , sum , length , num ) ;
  }
  dp [ position ] [ previous_sum ] = res ;
  return res ;
}
|||

LONGEST_SPAN_SUM_TWO_BINARY_ARRAYS_1

static int longestCommonSum ( int n ) {
  int maxLen = 0 ;
  int preSum1 = 0 , preSum2 = 0 ;
  int diff [ ] = new int [ 2 * n + 1 ] ;
  for ( int i = 0 ;
  i < diff . length ;
  i ++ ) {
    diff [ i ] = - 1 ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    preSum1 += arr1 [ i ] ;
    preSum2 += arr2 [ i ] ;
    int curr_diff = preSum1 - preSum2 ;
    int diffIndex = n + curr_diff ;
    if ( curr_diff == 0 ) maxLen = i + 1 ;
    else if ( diff [ diffIndex ] == - 1 ) diff [ diffIndex ] = i ;
    else {
      int len = i - diff [ diffIndex ] ;
      if ( len > maxLen ) maxLen = len ;
    }
  }
  return maxLen ;
}
|||

PROGRAM_TO_PRINT_FIRST_N_FIBONACCI_NUMBERS

static void printFibonacciNumbers ( int n ) {
  int f1 = 0 , f2 = 1 , i ;
  if ( n < 1 ) return ;
  for ( i = 1 ;
  i <= n ;
  i ++ ) {
    System . out . print ( f2 + " " ) ;
    int next = f1 + f2 ;
    f1 = f2 ;
    f2 = next ;
  }
}
|||

LARGEST_SUM_CONTIGUOUS_SUBARRAY_3

static void maxSubArraySum ( int a [ ] , int size ) {
  int max_so_far = Integer . MIN_VALUE , max_ending_here = 0 , start = 0 , end = 0 , s = 0 ;
  for ( int i = 0 ;
  i < size ;
  i ++ ) {
    max_ending_here += a [ i ] ;
    if ( max_so_far < max_ending_here ) {
      max_so_far = max_ending_here ;
      start = s ;
      end = i ;
    }
    if ( max_ending_here < 0 ) {
      max_ending_here = 0 ;
      s = i + 1 ;
    }
  }
  System . out . println ( "Maximum contiguous sum is " + max_so_far ) ;
  System . out . println ( "Starting index " + start ) ;
  System . out . println ( "Ending index " + end ) ;
}
|||

FIND_EQUAL_POINT_STRING_BRACKETS

static int findIndex ( String str ) {
  int len = str . length ( ) ;
  int open [ ] = new int [ len + 1 ] ;
  int close [ ] = new int [ len + 1 ] ;
  int index = - 1 ;
  open [ 0 ] = 0 ;
  close [ len ] = 0 ;
  if ( str . charAt ( 0 ) == '(' ) open [ 1 ] = 1 ;
  if ( str . charAt ( len - 1 ) == ')' ) close [ len - 1 ] = 1 ;
  for ( int i = 1 ;
  i < len ;
  i ++ ) {
    if ( str . charAt ( i ) == '(' ) open [ i + 1 ] = open [ i ] + 1 ;
    else open [ i + 1 ] = open [ i ] ;
  }
  for ( int i = len - 2 ;
  i >= 0 ;
  i -- ) {
    if ( str . charAt ( i ) == ')' ) close [ i ] = close [ i + 1 ] + 1 ;
    else close [ i ] = close [ i + 1 ] ;
  }
  if ( open [ len ] == 0 ) return len ;
  if ( close [ 0 ] == 0 ) return 0 ;
  for ( int i = 0 ;
  i <= len ;
  i ++ ) if ( open [ i ] == close [ i ] ) index = i ;
  return index ;
}
|||

COUNT_NUMBER_OF_WAYS_TO_PARTITION_A_SET_INTO_K_SUBSETS_1

static int countP ( int n , int k ) {
  int [ ] [ ] dp = new int [ n + 1 ] [ k + 1 ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) dp [ i ] [ 0 ] = 0 ;
  for ( int i = 0 ;
  i <= k ;
  i ++ ) dp [ 0 ] [ k ] = 0 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) for ( int j = 1 ;
  j <= k ;
  j ++ ) if ( j == 1 || i == j ) dp [ i ] [ j ] = 1 ;
  else dp [ i ] [ j ] = j * dp [ i - 1 ] [ j ] + dp [ i - 1 ] [ j - 1 ] ;
  return dp [ n ] [ k ] ;
}
|||

LONGEST_INCREASING_SUBSEQUENCE

static int lis ( int arr [ ] , int n ) {
  max_ref = 1 ;
  _lis ( arr , n ) ;
  return max_ref ;
}
|||

FIND_REPEATED_CHARACTER_PRESENT_FIRST_STRING

static int findRepeatFirstN2 ( String s ) {
  int p = - 1 , i , j ;
  for ( i = 0 ;
  i < s . length ( ) ;
  i ++ ) {
    for ( j = i + 1 ;
    j < s . length ( ) ;
    j ++ ) {
      if ( s . charAt ( i ) == s . charAt ( j ) ) {
        p = i ;
        break ;
      }
    }
    if ( p != - 1 ) break ;
  }
  return p ;
}
|||

K_TH_SMALLEST_ELEMENT_REMOVING_INTEGERS_NATURAL_NUMBERS

static int ksmallest ( int arr [ ] , int n , int k ) {
  int b [ ] = new int [ MAX ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    b [ arr [ i ] ] = 1 ;
  }
  for ( int j = 1 ;
  j < MAX ;
  j ++ ) {
    if ( b [ j ] != 1 ) {
      k -- ;
    }
    if ( k != 1 ) {
      return j ;
    }
  }
  return Integer . MAX_VALUE ;
}
|||

CHECK_IF_STACK_ELEMENTS_ARE_PAIRWISE_CONSECUTIVE

static boolean pairWiseConsecutive ( Stack < Integer > s ) {
  Stack < Integer > aux = new Stack < Integer > ( ) ;
  while ( ! s . isEmpty ( ) ) {
    aux . push ( s . peek ( ) ) ;
    s . pop ( ) ;
  }
  boolean result = true ;
  while ( aux . size ( ) > 1 ) {
    int x = aux . peek ( ) ;
    aux . pop ( ) ;
    int y = aux . peek ( ) ;
    aux . pop ( ) ;
    if ( Math . abs ( x - y ) != 1 ) result = false ;
    s . push ( x ) ;
    s . push ( y ) ;
  }
  if ( aux . size ( ) == 1 ) s . push ( aux . peek ( ) ) ;
  return result ;
}
|||

BINARY_SEARCH_1

int binarySearch ( int arr [ ] , int x ) {
  int l = 0 , r = arr . length - 1 ;
  while ( l <= r ) {
    int m = l + ( r - l ) / 2 ;
    if ( arr [ m ] == x ) return m ;
    if ( arr [ m ] < x ) l = m + 1 ;
    else r = m - 1 ;
  }
  return - 1 ;
}
|||

COUNT_DISTINCT_OCCURRENCES_AS_A_SUBSEQUENCE

static int findSubsequenceCount ( String S , String T ) {
  int m = T . length ( ) ;
  int n = S . length ( ) ;
  if ( m > n ) return 0 ;
  int mat [ ] [ ] = new int [ m + 1 ] [ n + 1 ] ;
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
      else mat [ i ] [ j ] = mat [ i ] [ j - 1 ] + mat [ i - 1 ] [ j - 1 ] ;
    }
  }
  return mat [ m ] [ n ] ;
}
|||

SWAP_TWO_NUMBERS_WITHOUT_USING_TEMPORARY_VARIABLE

static void swap ( int [ ] xp , int [ ] yp ) {
  xp [ 0 ] = xp [ 0 ] ^ yp [ 0 ] ;
  yp [ 0 ] = xp [ 0 ] ^ yp [ 0 ] ;
  xp [ 0 ] = xp [ 0 ] ^ yp [ 0 ] ;
}
|||

POLICEMEN_CATCH_THIEVES

static int policeThief ( char arr [ ] , int n , int k ) {
  int res = 0 ;
  ArrayList < Integer > thi = new ArrayList < Integer > ( ) ;
  ArrayList < Integer > pol = new ArrayList < Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] == 'P' ) pol . add ( i ) ;
    else if ( arr [ i ] == 'T' ) thi . add ( i ) ;
  }
  int l = 0 , r = 0 ;
  while ( l < thi . size ( ) && r < pol . size ( ) ) {
    if ( Math . abs ( thi . get ( l ) - pol . get ( r ) ) <= k ) {
      res ++ ;
      l ++ ;
      r ++ ;
    }
    else if ( thi . get ( l ) < pol . get ( r ) ) l ++ ;
    else r ++ ;
  }
  return res ;
}
|||

LARGEST_SUBARRAY_WITH_EQUAL_NUMBER_OF_0S_AND_1S_1

int maxLen ( int arr [ ] , int n ) {
  HashMap < Integer , Integer > hM = new HashMap < Integer , Integer > ( ) ;
  int sum = 0 ;
  int max_len = 0 ;
  int ending_index = - 1 ;
  int start_index = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    arr [ i ] = ( arr [ i ] == 0 ) ? - 1 : 1 ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    sum += arr [ i ] ;
    if ( sum == 0 ) {
      max_len = i + 1 ;
      ending_index = i ;
    }
    if ( hM . containsKey ( sum + n ) ) {
      if ( max_len < i - hM . get ( sum + n ) ) {
        max_len = i - hM . get ( sum + n ) ;
        ending_index = i ;
      }
    }
    else hM . put ( sum + n , i ) ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    arr [ i ] = ( arr [ i ] == - 1 ) ? 0 : 1 ;
  }
  int end = ending_index - max_len + 1 ;
  System . out . println ( end + " to " + ending_index ) ;
  return max_len ;
}
|||

MAXIMUM_DIFFERENCE_ZEROS_ONES_BINARY_STRING_SET_2_TIME

public static int findLength ( String str , int n ) {
  int current_sum = 0 ;
  int max_sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    current_sum += ( str . charAt ( i ) == '0' ? 1 : - 1 ) ;
    if ( current_sum < 0 ) current_sum = 0 ;
    max_sum = Math . max ( current_sum , max_sum ) ;
  }
  return max_sum == 0 ? - 1 : max_sum ;
}
|||

MAXIMUM_CONSECUTIVE_NUMBERS_PRESENT_ARRAY

static int findLongestConseqSubseq ( int arr [ ] , int n ) {
  HashSet < Integer > S = new HashSet < Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) S . add ( arr [ i ] ) ;
  int ans = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( S . contains ( arr [ i ] ) ) {
      int j = arr [ i ] ;
      while ( S . contains ( j ) ) j ++ ;
      ans = Math . max ( ans , j - arr [ i ] ) ;
    }
  }
  return ans ;
}
|||

LEXICOGRAPHICALLY_NEXT_STRING

public static String nextWord ( String str ) {
  if ( str == "" ) return "a" ;
  int i = str . length ( ) - 1 ;
  while ( str . charAt ( i ) == 'z' && i >= 0 ) i -- ;
  if ( i == - 1 ) str = str + 'a' ;
  else str = str . substring ( 0 , i ) + ( char ) ( ( int ) ( str . charAt ( i ) ) + 1 ) + str . substring ( i + 1 ) ;
  return str ;
}
|||

SCHEDULE_JOBS_SERVER_GETS_EQUAL_LOAD

static int solve ( int a [ ] , int b [ ] , int n ) {
  int i ;
  int s = 0 ;
  for ( i = 0 ;
  i < n ;
  i ++ ) s += ( a [ i ] + b [ i ] ) ;
  if ( n == 1 ) return a [ 0 ] + b [ 0 ] ;
  if ( s % n != 0 ) return - 1 ;
  int x = s / n ;
  for ( i = 0 ;
  i < n ;
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
  for ( i = 0 ;
  i < n ;
  i ++ ) if ( b [ i ] != 0 ) return - 1 ;
  return x ;
}
|||

FORM_MINIMUM_NUMBER_FROM_GIVEN_SEQUENCE_1

static String getMinNumberForPattern ( String seq ) {
  int n = seq . length ( ) ;
  if ( n >= 9 ) return "-1" ;
  char result [ ] = new char [ n + 1 ] ;
  int count = 1 ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( i == n || seq . charAt ( i ) == 'I' ) {
      for ( int j = i - 1 ;
      j >= - 1 ;
      j -- ) {
        result [ j + 1 ] = ( char ) ( ( int ) '0' + count ++ ) ;
        if ( j >= 0 && seq . charAt ( j ) == 'I' ) break ;
      }
    }
  }
  return new String ( result ) ;
}
|||

SHUFFLE_2N_INTEGERS_FORMAT_A1_B1_A2_B2_A3_B3_BN_WITHOUT_USING_EXTRA_SPACE

static void shuffleArray ( int a [ ] , int n ) {
  for ( int i = 0 , q = 1 , k = n ;
  i < n ;
  i ++ , k ++ , q ++ ) for ( int j = k ;
  j > i + q ;
  j -- ) {
    int temp = a [ j - 1 ] ;
    a [ j - 1 ] = a [ j ] ;
    a [ j ] = temp ;
  }
}
|||

FIND_REPETITIVE_ELEMENT_1_N_1_1

static int findRepeating ( int arr [ ] , int n ) {
  HashSet < Integer > s = new HashSet < Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( s . contains ( arr [ i ] ) ) return arr [ i ] ;
    s . add ( arr [ i ] ) ;
  }
  return - 1 ;
}
|||

C_PROGRAM_SUBTRACTION_MATICES

static void multiply ( int A [ ] [ ] , int B [ ] [ ] , int C [ ] [ ] ) {
  int i , j ;
  for ( i = 0 ;
  i < N ;
  i ++ ) for ( j = 0 ;
  j < N ;
  j ++ ) C [ i ] [ j ] = A [ i ] [ j ] - B [ i ] [ j ] ;
}
|||

FIRST_NEGATIVE_INTEGER_EVERY_WINDOW_SIZE_K

static void printFirstNegativeInteger ( int arr [ ] , int n , int k ) {
  boolean flag ;
  for ( int i = 0 ;
  i < ( n - k + 1 ) ;
  i ++ ) {
    flag = false ;
    for ( int j = 0 ;
    j < k ;
    j ++ ) {
      if ( arr [ i + j ] < 0 ) {
        System . out . print ( ( arr [ i + j ] ) + " " ) ;
        flag = true ;
        break ;
      }
    }
    if ( ! flag ) System . out . print ( "0" + " " ) ;
  }
}
|||

NUMBER_FULL_BINARY_TREES_NODE_PRODUCT_CHILDREN

static int numoffbt ( int arr [ ] , int n ) {
  int maxvalue = - 2147483647 ;
  int minvalue = 2147483647 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    maxvalue = Math . max ( maxvalue , arr [ i ] ) ;
    minvalue = Math . min ( minvalue , arr [ i ] ) ;
  }
  int mark [ ] = new int [ maxvalue + 2 ] ;
  int value [ ] = new int [ maxvalue + 2 ] ;
  Arrays . fill ( mark , 0 ) ;
  Arrays . fill ( value , 0 ) ;
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
    if ( mark [ i ] != 0 ) {
      for ( int j = i + i ;
      j <= maxvalue && j / i <= i ;
      j += i ) {
        if ( mark [ j ] == 0 ) continue ;
        value [ j ] = value [ j ] + ( value [ i ] * value [ j / i ] ) ;
        if ( i != j / i ) value [ j ] = value [ j ] + ( value [ i ] * value [ j / i ] ) ;
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

static void KMaxCombinations ( int A [ ] , int B [ ] , int N , int K ) {
  PriorityQueue < Integer > pq = new PriorityQueue < Integer > ( Collections . reverseOrder ( ) ) ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) for ( int j = 0 ;
  j < N ;
  j ++ ) pq . add ( A [ i ] + B [ j ] ) ;
  int count = 0 ;
  while ( count < K ) {
    System . out . println ( pq . peek ( ) ) ;
    pq . remove ( ) ;
    count ++ ;
  }
}
|||

CONSTRUCT_ARRAY_PAIR_SUM_ARRAY

static void constructArr ( int arr [ ] , int pair [ ] , int n ) {
  arr [ 0 ] = ( pair [ 0 ] + pair [ 1 ] - pair [ n - 1 ] ) / 2 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) arr [ i ] = pair [ i - 1 ] - arr [ 0 ] ;
}
|||

CHECK_HALF_STRING_CHARACTER_FREQUENCY_CHARACTER

static boolean checkCorrectOrNot ( String s ) {
  int [ ] count1 = new int [ MAX_CHAR ] ;
  int [ ] count2 = new int [ MAX_CHAR ] ;
  int n = s . length ( ) ;
  if ( n == 1 ) return true ;
  for ( int i = 0 , j = n - 1 ;
  i < j ;
  i ++ , j -- ) {
    count1 [ s . charAt ( i ) - 'a' ] ++ ;
    count2 [ s . charAt ( j ) - 'a' ] ++ ;
  }
  for ( int i = 0 ;
  i < MAX_CHAR ;
  i ++ ) if ( count1 [ i ] != count2 [ i ] ) return false ;
  return true ;
}
|||

MINIMIZE_THE_MAXIMUM_DIFFERENCE_BETWEEN_THE_HEIGHTS

static int getMinDiff ( int arr [ ] , int n , int k ) {
  if ( n == 1 ) return 0 ;
  Arrays . sort ( arr ) ;
  int ans = arr [ n - 1 ] - arr [ 0 ] ;
  int small = arr [ 0 ] + k ;
  int big = arr [ n - 1 ] - k ;
  int temp = 0 ;
  if ( small > big ) {
    temp = small ;
    small = big ;
    big = temp ;
  }
  for ( int i = 1 ;
  i < n - 1 ;
  i ++ ) {
    int subtract = arr [ i ] - k ;
    int add = arr [ i ] + k ;
    if ( subtract >= small || add <= big ) continue ;
    if ( big - subtract <= add - small ) small = subtract ;
    else big = add ;
  }
  return Math . min ( ans , big - small ) ;
}
|||

MINIMUM_POSSIBLE_VALUE_AI_AJ_K_GIVEN_ARRAY_K

static void pairs ( int arr [ ] , int n , int k ) {
  int smallest = Integer . MAX_VALUE ;
  int count = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) for ( int j = i + 1 ;
  j < n ;
  j ++ ) {
    if ( Math . abs ( arr [ i ] + arr [ j ] - k ) < smallest ) {
      smallest = Math . abs ( arr [ i ] + arr [ j ] - k ) ;
      count = 1 ;
    }
    else if ( Math . abs ( arr [ i ] + arr [ j ] - k ) == smallest ) count ++ ;
  }
  System . out . println ( "Minimal Value = " + smallest ) ;
  System . out . println ( "Total Pairs = " + count ) ;
}
|||

SIZE_SUBARRAY_MAXIMUM_SUM

static int maxSubArraySum ( int a [ ] , int size ) {
  int max_so_far = Integer . MIN_VALUE , max_ending_here = 0 , start = 0 , end = 0 , s = 0 ;
  for ( int i = 0 ;
  i < size ;
  i ++ ) {
    max_ending_here += a [ i ] ;
    if ( max_so_far < max_ending_here ) {
      max_so_far = max_ending_here ;
      start = s ;
      end = i ;
    }
    if ( max_ending_here < 0 ) {
      max_ending_here = 0 ;
      s = i + 1 ;
    }
  }
  return ( end - start + 1 ) ;
}
|||

MINIMUM_NUMBER_OF_SQUARES_WHOSE_SUM_EQUALS_TO_GIVEN_NUMBER_N_1

static int getMinSquares ( int n ) {
  if ( n <= 3 ) return n ;
  int dp [ ] = new int [ n + 1 ] ;
  dp [ 0 ] = 0 ;
  dp [ 1 ] = 1 ;
  dp [ 2 ] = 2 ;
  dp [ 3 ] = 3 ;
  for ( int i = 4 ;
  i <= n ;
  i ++ ) {
    dp [ i ] = i ;
    for ( int x = 1 ;
    x <= Math . ceil ( Math . sqrt ( i ) ) ;
    x ++ ) {
      int temp = x * x ;
      if ( temp > i ) break ;
      else dp [ i ] = Math . min ( dp [ i ] , 1 + dp [ i - temp ] ) ;
    }
  }
  int res = dp [ n ] ;
  return res ;
}
|||

DIVISIBILITY_BY_7

static boolean isDivisibleBy7 ( int num ) {
  if ( num < 0 ) return isDivisibleBy7 ( - num ) ;
  if ( num == 0 || num == 7 ) return true ;
  if ( num < 10 ) return false ;
  return isDivisibleBy7 ( num / 10 - 2 * ( num - num / 10 * 10 ) ) ;
}
|||

POSITION_OF_RIGHTMOST_SET_BIT_2

static int Right_most_setbit ( int num ) {
  int pos = 1 ;
  for ( int i = 0 ;
  i < INT_SIZE ;
  i ++ ) {
    if ( ( num & ( 1 << i ) ) == 0 ) pos ++ ;
    else break ;
  }
  return pos ;
}
|||

EFFICIENT_WAY_TO_MULTIPLY_WITH_7

static int multiplyBySeven ( int n ) {
  return ( ( n << 3 ) - n ) ;
}
|||

NEXT_HIGHER_NUMBER_WITH_SAME_NUMBER_OF_SET_BITS

static int snoob ( int x ) {
  int rightOne , nextHigherOneBit , rightOnesPattern , next = 0 ;
  if ( x > 0 ) {
    rightOne = x & - x ;
    nextHigherOneBit = x + rightOne ;
    rightOnesPattern = x ^ nextHigherOneBit ;
    rightOnesPattern = ( rightOnesPattern ) / rightOne ;
    rightOnesPattern >>= 2 ;
    next = nextHigherOneBit | rightOnesPattern ;
  }
  return next ;
}
|||

CHANGE_ARRAY_PERMUTATION_NUMBERS_1_N

static void makePermutation ( int [ ] a , int n ) {
  HashMap < Integer , Integer > count = new HashMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( count . containsKey ( a [ i ] ) ) {
      count . put ( a [ i ] , count . get ( a [ i ] ) + 1 ) ;
    }
    else {
      count . put ( a [ i ] , 1 ) ;
    }
  }
  int next_missing = 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( count . containsKey ( a [ i ] ) && count . get ( a [ i ] ) != 1 || a [ i ] > n || a [ i ] < 1 ) {
      count . put ( a [ i ] , count . get ( a [ i ] ) - 1 ) ;
      while ( count . containsKey ( next_missing ) ) next_missing ++ ;
      a [ i ] = next_missing ;
      count . put ( next_missing , 1 ) ;
    }
  }
}
|||

MAXIMUM_AREA_QUADRILATERAL

static double maxArea ( double a , double b , double c , double d ) {
  double semiperimeter = ( a + b + c + d ) / 2 ;
  return Math . sqrt ( ( semiperimeter - a ) * ( semiperimeter - b ) * ( semiperimeter - c ) * ( semiperimeter - d ) ) ;
}
|||

REPLACE_OCCURRENCES_STRING_AB_C_WITHOUT_USING_EXTRA_SPACE_1

static void translate ( char str [ ] ) {
  int len = str . length ;
  if ( len < 2 ) return ;
  int i = 0 ;
  int j = 0 ;
  while ( j < len - 1 ) {
    if ( str [ j ] == 'A' && str [ j + 1 ] == 'B' ) {
      j = j + 2 ;
      str [ i ++ ] = 'C' ;
      continue ;
    }
    str [ i ++ ] = str [ j ++ ] ;
  }
  if ( j == len - 1 ) str [ i ++ ] = str [ j ] ;
  str [ i ] = ' ' ;
  str [ len - 1 ] = ' ' ;
}
|||

FIND_POWER_POWER_MOD_PRIME

static int Calculate ( int A , int B , int C , int M ) {
  int res , ans ;
  res = power ( B , C , M - 1 ) ;
  ans = power ( A , res , M ) ;
  return ans ;
}
|||

CHECK_EXIST_TWO_ELEMENTS_ARRAY_WHOSE_SUM_EQUAL_SUM_REST_ARRAY

static boolean checkPair ( int arr [ ] , int n ) {
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
  HashSet < Integer > s = new HashSet < Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int val = sum - arr [ i ] ;
    if ( s . contains ( val ) && val == ( int ) s . toArray ( ) [ s . size ( ) - 1 ] ) {
      System . out . printf ( "Pair elements are %d and %d\n" , arr [ i ] , val ) ;
      return true ;
    }
    s . add ( arr [ i ] ) ;
  }
  return false ;
}
|||

PROGRAM_FOR_SURFACE_AREA_OF_OCTAHEDRON

static double surface_area_octahedron ( double side ) {
  return ( 2 * ( Math . sqrt ( 3 ) ) * ( side * side ) ) ;
}
|||

FIND_A_SPECIFIC_PAIR_IN_MATRIX

static int findMaxValue ( int N , int mat [ ] [ ] ) {
  int maxValue = Integer . MIN_VALUE ;
  for ( int a = 0 ;
  a < N - 1 ;
  a ++ ) for ( int b = 0 ;
  b < N - 1 ;
  b ++ ) for ( int d = a + 1 ;
  d < N ;
  d ++ ) for ( int e = b + 1 ;
  e < N ;
  e ++ ) if ( maxValue < ( mat [ d ] [ e ] - mat [ a ] [ b ] ) ) maxValue = mat [ d ] [ e ] - mat [ a ] [ b ] ;
  return maxValue ;
}
|||

MULTIPLY_TWO_NUMBERS_WITHOUT_USING_MULTIPLY_DIVISION_BITWISE_OPERATORS_AND_NO_LOOPS

static int multiply ( int x , int y ) {
  if ( y == 0 ) return 0 ;
  if ( y > 0 ) return ( x + multiply ( x , y - 1 ) ) ;
  if ( y < 0 ) return - multiply ( x , - y ) ;
  return - 1 ;
}
|||

FIND_TRIPLETS_ARRAY_WHOSE_SUM_EQUAL_ZERO_1

static void findTriplets ( int arr [ ] , int n ) {
  boolean found = false ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    HashSet < Integer > s = new HashSet < Integer > ( ) ;
    for ( int j = i + 1 ;
    j < n ;
    j ++ ) {
      int x = - ( arr [ i ] + arr [ j ] ) ;
      if ( s . contains ( x ) ) {
        System . out . printf ( "%d %d %d\n" , x , arr [ i ] , arr [ j ] ) ;
        found = true ;
      }
      else {
        s . add ( arr [ j ] ) ;
      }
    }
  }
  if ( found == false ) {
    System . out . printf ( " No Triplet Found\n" ) ;
  }
}
|||

FIND_MAXIMUM_VALUE_OF_SUM_IARRI_WITH_ONLY_ROTATIONS_ON_GIVEN_ARRAY_ALLOWED

static int maxSum ( ) {
  int arrSum = 0 ;
  int currVal = 0 ;
  for ( int i = 0 ;
  i < arr . length ;
  i ++ ) {
    arrSum = arrSum + arr [ i ] ;
    currVal = currVal + ( i * arr [ i ] ) ;
  }
  int maxVal = currVal ;
  for ( int j = 1 ;
  j < arr . length ;
  j ++ ) {
    currVal = currVal + arrSum - arr . length * arr [ arr . length - j ] ;
    if ( currVal > maxVal ) maxVal = currVal ;
  }
  return maxVal ;
}
|||

PROGRAM_FOR_SCALAR_MULTIPLICATION_OF_A_MATRIX

static void scalarProductMat ( int mat [ ] [ ] , int k ) {
  for ( int i = 0 ;
  i < N ;
  i ++ ) for ( int j = 0 ;
  j < N ;
  j ++ ) mat [ i ] [ j ] = mat [ i ] [ j ] * k ;
}
|||

PRINT_SQUARES_FIRST_N_NATURAL_NUMBERS_WITHOUT_USING_1

static void printSquares ( int n ) {
  int square = 0 , odd = 1 ;
  for ( int x = 0 ;
  x < n ;
  x ++ ) {
    System . out . print ( square + " " ) ;
    square = square + odd ;
    odd = odd + 2 ;
  }
}
|||

NTH_PENTAGONAL_NUMBER

int pentagonalNum ( int n ) {
  return ( 3 * n * n - n ) / 2 ;
}
|||

COUNT_ARRAYS_ADJACENT_ELEMENTS_ONE_DIVIDE_ANOTHER

static int numofArray ( int n , int m ) {
  int [ ] [ ] dp = new int [ MAX ] [ MAX ] ;
  Vector < Integer > [ ] di = new Vector [ MAX ] ;
  Vector < Integer > [ ] mu = new Vector [ MAX ] ;
  for ( int i = 0 ;
  i < MAX ;
  i ++ ) {
    for ( int j = 0 ;
    j < MAX ;
    j ++ ) {
      dp [ i ] [ j ] = 0 ;
    }
  }
  for ( int i = 0 ;
  i < MAX ;
  i ++ ) {
    di [ i ] = new Vector < > ( ) ;
    mu [ i ] = new Vector < > ( ) ;
  }
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
  i ++ ) dp [ 1 ] [ i ] = 1 ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    for ( int j = 1 ;
    j <= m ;
    j ++ ) {
      dp [ i ] [ j ] = 0 ;
      for ( Integer x : di [ j ] ) dp [ i ] [ j ] += dp [ i - 1 ] [ x ] ;
      for ( Integer x : mu [ j ] ) dp [ i ] [ j ] += dp [ i - 1 ] [ x ] ;
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

static int knapSack ( int W , int wt [ ] , int val [ ] , int n ) {
  if ( n == 0 || W == 0 ) return 0 ;
  if ( wt [ n - 1 ] > W ) return knapSack ( W , wt , val , n - 1 ) ;
  else return max ( val [ n - 1 ] + knapSack ( W - wt [ n - 1 ] , wt , val , n - 1 ) , knapSack ( W , wt , val , n - 1 ) ) ;
}
|||

FIND_TRIPLETS_ARRAY_WHOSE_SUM_EQUAL_ZERO

static void findTriplets ( int [ ] arr , int n ) {
  boolean found = true ;
  for ( int i = 0 ;
  i < n - 2 ;
  i ++ ) {
    for ( int j = i + 1 ;
    j < n - 1 ;
    j ++ ) {
      for ( int k = j + 1 ;
      k < n ;
      k ++ ) {
        if ( arr [ i ] + arr [ j ] + arr [ k ] == 0 ) {
          System . out . print ( arr [ i ] ) ;
          System . out . print ( " " ) ;
          System . out . print ( arr [ j ] ) ;
          System . out . print ( " " ) ;
          System . out . print ( arr [ k ] ) ;
          System . out . print ( "\n" ) ;
          found = true ;
        }
      }
    }
  }
  if ( found == false ) System . out . println ( " not exist " ) ;
}
|||

COUNT_NUMBER_WAYS_REACH_GIVEN_SCORE_GAME

static int count ( int n ) {
  int table [ ] = new int [ n + 1 ] , i ;
  Arrays . fill ( table , 0 ) ;
  table [ 0 ] = 1 ;
  for ( i = 3 ;
  i <= n ;
  i ++ ) table [ i ] += table [ i - 3 ] ;
  for ( i = 5 ;
  i <= n ;
  i ++ ) table [ i ] += table [ i - 5 ] ;
  for ( i = 10 ;
  i <= n ;
  i ++ ) table [ i ] += table [ i - 10 ] ;
  return table [ n ] ;
}
|||

MAXIMUM_SUM_ABSOLUTE_DIFFERENCE_ARRAY

static int MaxSumDifference ( Integer [ ] a , int n ) {
  List < Integer > finalSequence = new ArrayList < Integer > ( ) ;
  Arrays . sort ( a ) ;
  for ( int i = 0 ;
  i < n / 2 ;
  ++ i ) {
    finalSequence . add ( a [ i ] ) ;
    finalSequence . add ( a [ n - i - 1 ] ) ;
  }
  int MaximumSum = 0 ;
  for ( int i = 0 ;
  i < n - 1 ;
  ++ i ) {
    MaximumSum = MaximumSum + Math . abs ( finalSequence . get ( i ) - finalSequence . get ( i + 1 ) ) ;
  }
  MaximumSum = MaximumSum + Math . abs ( finalSequence . get ( n - 1 ) - finalSequence . get ( 0 ) ) ;
  return MaximumSum ;
}
|||

PROGRAM_FIND_MID_POINT_LINE

static void midpoint ( int x1 , int x2 , int y1 , int y2 ) {
  System . out . print ( ( x1 + x2 ) / 2 + " , " + ( y1 + y2 ) / 2 ) ;
}
|||

ALTERNATIVE_SORTING

static void alternateSort ( int arr [ ] , int n ) {
  Arrays . sort ( arr ) ;
  int i = 0 , j = n - 1 ;
  while ( i < j ) {
    System . out . print ( arr [ j -- ] + " " ) ;
    System . out . print ( arr [ i ++ ] + " " ) ;
  }
  if ( n % 2 != 0 ) System . out . print ( arr [ i ] ) ;
}
|||

NUMBER_SUBARRAYS_SUM_EXACTLY_EQUAL_K

static int findSubarraySum ( int arr [ ] , int n , int sum ) {
  HashMap < Integer , Integer > prevSum = new HashMap < > ( ) ;
  int res = 0 ;
  int currsum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    currsum += arr [ i ] ;
    if ( currsum == sum ) res ++ ;
    if ( prevSum . containsKey ( currsum - sum ) ) res += prevSum . get ( currsum - sum ) ;
    Integer count = prevSum . get ( currsum ) ;
    if ( count == null ) prevSum . put ( currsum , 1 ) ;
    else prevSum . put ( currsum , count + 1 ) ;
  }
  return res ;
}
|||

FIND_THE_ELEMENT_THAT_APPEARS_ONCE_IN_A_SORTED_ARRAY

public static void search ( int [ ] arr , int low , int high ) {
  if ( low > high ) return ;
  if ( low == high ) {
    System . out . println ( "The required element is " + arr [ low ] ) ;
    return ;
  }
  int mid = ( low + high ) / 2 ;
  if ( mid % 2 == 0 ) {
    if ( arr [ mid ] == arr [ mid + 1 ] ) search ( arr , mid + 2 , high ) ;
    else search ( arr , low , mid ) ;
  }
  else if ( mid % 2 == 1 ) {
    if ( arr [ mid ] == arr [ mid - 1 ] ) search ( arr , mid + 1 , high ) ;
    else search ( arr , low , mid - 1 ) ;
  }
}
|||

FORM_SMALLEST_NUMBER_USING_ONE_SWAP_OPERATION

public static String smallestNumber ( String str ) {
  char [ ] num = str . toCharArray ( ) ;
  int n = str . length ( ) ;
  int [ ] rightMin = new int [ n ] ;
  rightMin [ n - 1 ] = - 1 ;
  int right = n - 1 ;
  for ( int i = n - 2 ;
  i >= 1 ;
  i -- ) {
    if ( num [ i ] > num [ right ] ) rightMin [ i ] = right ;
    else {
      rightMin [ i ] = - 1 ;
      right = i ;
    }
  }
  int small = - 1 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) if ( num [ i ] != '0' ) {
    if ( small == - 1 ) {
      if ( num [ i ] < num [ 0 ] ) small = i ;
    }
    else if ( num [ i ] < num [ small ] ) small = i ;
  }
  if ( small != - 1 ) {
    char temp ;
    temp = num [ 0 ] ;
    num [ 0 ] = num [ small ] ;
    num [ small ] = temp ;
  }
  else {
    for ( int i = 1 ;
    i < n ;
    i ++ ) {
      if ( rightMin [ i ] != - 1 ) {
        char temp ;
        temp = num [ i ] ;
        num [ i ] = num [ rightMin [ i ] ] ;
        num [ rightMin [ i ] ] = temp ;
        break ;
      }
    }
  }
  return ( new String ( num ) ) ;
}
|||

PROGRAM_AREA_SQUARE

static int areaSquare ( int side ) {
  int area = side * side ;
  return area ;
}
|||

FIND_DAY_OF_THE_WEEK_FOR_A_GIVEN_DATE

static int dayofweek ( int d , int m , int y ) {
  int t [ ] = {
    0 , 3 , 2 , 5 , 0 , 3 , 5 , 1 , 4 , 6 , 2 , 4 };
    y -= ( m < 3 ) ? 1 : 0 ;
    return ( y + y / 4 - y / 100 + y / 400 + t [ m - 1 ] + d ) % 7 ;
  }
  |||

CHECK_QUEUE_CAN_SORTED_ANOTHER_QUEUE_USING_STACK

static boolean checkSorted ( int n ) {
  Stack < Integer > st = new Stack < Integer > ( ) ;
  int expected = 1 ;
  int fnt ;
  while ( q . size ( ) != 0 ) {
    fnt = q . peek ( ) ;
    q . poll ( ) ;
    if ( fnt == expected ) expected ++ ;
    else {
      if ( st . size ( ) == 0 ) {
        st . push ( fnt ) ;
      }
      else if ( st . size ( ) != 0 && st . peek ( ) < fnt ) {
        return false ;
      }
      else st . push ( fnt ) ;
    }
    while ( st . size ( ) != 0 && st . peek ( ) == expected ) {
      st . pop ( ) ;
      expected ++ ;
    }
  }
  if ( expected - 1 == n && st . size ( ) == 0 ) return true ;
  return false ;
}
|||

SORT_ARRAY_CONTAIN_1_N_VALUES

static void sortit ( int [ ] arr , int n ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    arr [ i ] = i + 1 ;
  }
}
|||

LCS_LONGEST_COMMON_SUBSEQUENCE_THREE_STRINGS_1

static int lcsOf3 ( int i , int j , int k ) {
  if ( i == - 1 || j == - 1 || k == - 1 ) {
    return 0 ;
  }
  if ( dp [ i ] [ j ] [ k ] != - 1 ) {
    return dp [ i ] [ j ] [ k ] ;
  }
  if ( X . charAt ( i ) == Y . charAt ( j ) && Y . charAt ( j ) == Z . charAt ( k ) ) {
    return dp [ i ] [ j ] [ k ] = 1 + lcsOf3 ( i - 1 , j - 1 , k - 1 ) ;
  }
  else {
    return dp [ i ] [ j ] [ k ] = Math . max ( Math . max ( lcsOf3 ( i - 1 , j , k ) , lcsOf3 ( i , j - 1 , k ) ) , lcsOf3 ( i , j , k - 1 ) ) ;
  }
}
|||

LOWER_INSERTION_POINT

static int LowerInsertionPoint ( int arr [ ] , int n , int X ) {
  if ( X < arr [ 0 ] ) return 0 ;
  else if ( X > arr [ n - 1 ] ) return n ;
  int lowerPnt = 0 ;
  int i = 1 ;
  while ( i < n && arr [ i ] < X ) {
    lowerPnt = i ;
    i = i * 2 ;
  }
  while ( lowerPnt < n && arr [ lowerPnt ] < X ) lowerPnt ++ ;
  return lowerPnt ;
}
|||

CONSTRUCT_LEXICOGRAPHICALLY_SMALLEST_PALINDROME

static String constructPalin ( char [ ] str , int len ) {
  int i = 0 , j = len - 1 ;
  for ( ;
  i < j ;
  i ++ , j -- ) {
    if ( str [ i ] == str [ j ] && str [ i ] != '*' ) continue ;
    else if ( str [ i ] == str [ j ] && str [ i ] == '*' ) {
      str [ i ] = 'a' ;
      str [ j ] = 'a' ;
      continue ;
    }
    else if ( str [ i ] == '*' ) {
      str [ i ] = str [ j ] ;
      continue ;
    }
    else if ( str [ j ] == '*' ) {
      str [ j ] = str [ i ] ;
      continue ;
    }
    System . out . println ( "Not Possible" ) ;
    return "" ;
  }
  return String . valueOf ( str ) ;
}
|||

SECTION_FORMULA_POINT_DIVIDES_LINE_GIVEN_RATIO

static void section ( double x1 , double x2 , double y1 , double y2 , double m , double n ) {
  double x = ( ( n * x1 ) + ( m * x2 ) ) / ( m + n ) ;
  double y = ( ( n * y1 ) + ( m * y2 ) ) / ( m + n ) ;
  System . out . println ( "(" + x + ", " + y + ")" ) ;
}
|||

SQUARE_ROOT_NUMBER_USING_LOG

static double squareRoot ( double n ) {
  return Math . pow ( 2 , 0.5 * ( Math . log ( n ) / Math . log ( 2 ) ) ) ;
}
|||

MAXIMIZE_SUM_ARRII

static int maxSum ( int arr [ ] , int n ) {
  Arrays . sort ( arr ) ;
  int sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) sum += ( arr [ i ] * i ) ;
  return sum ;
}
|||

STRING_K_DISTINCT_CHARACTERS_NO_CHARACTERS_ADJACENT

static String findString ( int n , int k ) {
  String res = "" ;
  for ( int i = 0 ;
  i < k ;
  i ++ ) res = res + ( char ) ( 'a' + i ) ;
  int count = 0 ;
  for ( int i = 0 ;
  i < n - k ;
  i ++ ) {
    res = res + ( char ) ( 'a' + count ) ;
    count ++ ;
    if ( count == k ) count = 0 ;
  }
  return res ;
}
|||

COUNT_WORDS_WHOSE_TH_LETTER_EITHER_1_TH_TH_I1_TH_LETTER_GIVEN_WORD

static int countWords ( String str , int len ) {
  int count = 1 ;
  if ( len == 1 ) return count ;
  if ( str . charAt ( 0 ) == str . charAt ( 1 ) ) count *= 1 ;
  else count *= 2 ;
  for ( int j = 1 ;
  j < len - 1 ;
  j ++ ) {
    if ( str . charAt ( j ) == str . charAt ( j - 1 ) && str . charAt ( j ) == str . charAt ( j + 1 ) ) count *= 1 ;
    else if ( str . charAt ( j ) == str . charAt ( j - 1 ) || str . charAt ( j ) == str . charAt ( j + 1 ) || str . charAt ( j - 1 ) == str . charAt ( j + 1 ) ) count *= 2 ;
    else count *= 3 ;
  }
  if ( str . charAt ( len - 1 ) == str . charAt ( len - 2 ) ) count *= 1 ;
  else count *= 2 ;
  return count ;
}
|||

NUMBER_JUMP_REQUIRED_GIVEN_LENGTH_REACH_POINT_FORM_D_0_ORIGIN_2D_PLANE

static int minJumps ( int a , int b , int d ) {
  int temp = a ;
  a = Math . min ( a , b ) ;
  b = Math . max ( temp , b ) ;
  if ( d >= b ) return ( d + b - 1 ) / b ;
  if ( d == 0 ) return 0 ;
  if ( d == a ) return 1 ;
  return 2 ;
}
|||

SUM_FACTORS_NUMBER_1

static int sumofFactors ( int n ) {
  int res = 1 ;
  for ( int i = 2 ;
  i <= Math . sqrt ( n ) ;
  i ++ ) {
    int curr_sum = 1 ;
    int curr_term = 1 ;
    while ( n % i == 0 ) {
      n = n / i ;
      curr_term *= i ;
      curr_sum += curr_term ;
    }
    res *= curr_sum ;
  }
  if ( n > 2 ) res *= ( 1 + n ) ;
  return res ;
}
|||

DELETE_CONSECUTIVE_WORDS_SEQUENCE

static int removeConsecutiveSame ( Vector < String > v ) {
  int n = v . size ( ) ;
  for ( int i = 0 ;
  i < n - 1 ;
  ) {
    if ( v . get ( i ) . equals ( v . get ( i + 1 ) ) ) {
      v . remove ( i ) ;
      v . remove ( i ) ;
      if ( i > 0 ) i -- ;
      n = n - 2 ;
    }
    else i ++ ;
  }
  return v . size ( ) ;
}
|||

COUNT_NUMBER_BINARY_STRINGS_WITHOUT_CONSECUTIVE_1S

static int countStrings ( int n ) {
  int a [ ] = new int [ n ] ;
  int b [ ] = new int [ n ] ;
  a [ 0 ] = b [ 0 ] = 1 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    a [ i ] = a [ i - 1 ] + b [ i - 1 ] ;
    b [ i ] = a [ i - 1 ] ;
  }
  return a [ n - 1 ] + b [ n - 1 ] ;
}
|||

FIND_THE_MISSING_NUMBER

static int getMissingNo ( int a [ ] , int n ) {
  int i , total ;
  total = ( n + 1 ) * ( n + 2 ) / 2 ;
  for ( i = 0 ;
  i < n ;
  i ++ ) total -= a [ i ] ;
  return total ;
}
|||

SQUARE_ROOT_OF_A_PERFECT_SQUARE

static float squareRoot ( float n ) {
  float x = n ;
  float y = 1 ;
  double e = 0.000001 ;
  while ( x - y > e ) {
    x = ( x + y ) / 2 ;
    y = n / x ;
  }
  return x ;
}
|||

SUBSET_SUM_PROBLEM_OSUM_SPACE

static boolean isSubsetSum ( int arr [ ] , int n , int sum ) {
  boolean subset [ ] [ ] = new boolean [ 2 ] [ sum + 1 ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= sum ;
    j ++ ) {
      if ( j == 0 ) subset [ i % 2 ] [ j ] = true ;
      else if ( i == 0 ) subset [ i % 2 ] [ j ] = false ;
      else if ( arr [ i - 1 ] <= j ) subset [ i % 2 ] [ j ] = subset [ ( i + 1 ) % 2 ] [ j - arr [ i - 1 ] ] || subset [ ( i + 1 ) % 2 ] [ j ] ;
      else subset [ i % 2 ] [ j ] = subset [ ( i + 1 ) % 2 ] [ j ] ;
    }
  }
  return subset [ n % 2 ] [ sum ] ;
}
|||

MULTIPLICATIVE_INVERSE_UNDER_MODULO_M

static int modInverse ( int a , int m ) {
  a = a % m ;
  for ( int x = 1 ;
  x < m ;
  x ++ ) if ( ( a * x ) % m == 1 ) return x ;
  return 1 ;
}
|||

COMPUTE_AVERAGE_TWO_NUMBERS_WITHOUT_OVERFLOW

static int compute_average ( int a , int b ) {
  return ( a + b ) / 2 ;
}
|||

REPRESENT_GIVEN_SET_POINTS_BEST_POSSIBLE_STRAIGHT_LINE

static void bestApproximate ( int x [ ] , int y [ ] ) {
  int n = x . length ;
  double m , c , sum_x = 0 , sum_y = 0 , sum_xy = 0 , sum_x2 = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    sum_x += x [ i ] ;
    sum_y += y [ i ] ;
    sum_xy += x [ i ] * y [ i ] ;
    sum_x2 += pow ( x [ i ] , 2 ) ;
  }
  m = ( n * sum_xy - sum_x * sum_y ) / ( n * sum_x2 - pow ( sum_x , 2 ) ) ;
  c = ( sum_y - m * sum_x ) / n ;
  System . out . println ( "m = " + m ) ;
  System . out . println ( "c = " + c ) ;
}
|||

SPLIT_ARRAY_ADD_FIRST_PART_END

public static void splitArr ( int arr [ ] , int n , int k ) {
  for ( int i = 0 ;
  i < k ;
  i ++ ) {
    int x = arr [ 0 ] ;
    for ( int j = 0 ;
    j < n - 1 ;
    ++ j ) arr [ j ] = arr [ j + 1 ] ;
    arr [ n - 1 ] = x ;
  }
}
|||

MAXIMUM_POSSIBLE_DIFFERENCE_TWO_SUBSETS_ARRAY

static int maxDiff ( int [ ] arr , int n ) {
  int SubsetSum_1 = 0 , SubsetSum_2 = 0 ;
  for ( int i = 0 ;
  i <= n - 1 ;
  i ++ ) {
    boolean isSingleOccurance = true ;
    for ( int j = i + 1 ;
    j <= n - 1 ;
    j ++ ) {
      if ( arr [ i ] == arr [ j ] ) {
        isSingleOccurance = false ;
        arr [ i ] = arr [ j ] = 0 ;
        break ;
      }
    }
    if ( isSingleOccurance ) {
      if ( arr [ i ] > 0 ) SubsetSum_1 += arr [ i ] ;
      else SubsetSum_2 += arr [ i ] ;
    }
  }
  return Math . abs ( SubsetSum_1 - SubsetSum_2 ) ;
}
|||

LONGEST_SUBSEQUENCE_DIFFERENCE_ADJACENTS_ONE_SET_2

static int longLenSub ( int [ ] arr , int n ) {
  HashMap < Integer , Integer > um = new HashMap < Integer , Integer > ( ) ;
  int longLen = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int len = 0 ;
    if ( um . containsKey ( arr [ i ] - 1 ) && len < um . get ( arr [ i ] - 1 ) ) len = um . get ( arr [ i ] - 1 ) ;
    if ( um . containsKey ( arr [ i ] + 1 ) && len < um . get ( arr [ i ] + 1 ) ) len = um . get ( arr [ i ] + 1 ) ;
    um . put ( arr [ i ] , len + 1 ) ;
    if ( longLen < um . get ( arr [ i ] ) ) longLen = um . get ( arr [ i ] ) ;
  }
  return longLen ;
}
|||

LONGEST_REPEATED_SUBSEQUENCE_1

static String longestRepeatedSubSeq ( String str ) {
  int n = str . length ( ) ;
  int [ ] [ ] dp = new int [ n + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) for ( int j = 0 ;
  j <= n ;
  j ++ ) dp [ i ] [ j ] = 0 ;
  for ( int i = 1 ;
  i <= n ;
  i ++ ) for ( int j = 1 ;
  j <= n ;
  j ++ ) if ( str . charAt ( i - 1 ) == str . charAt ( j - 1 ) && i != j ) dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ] ;
  else dp [ i ] [ j ] = Math . max ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] ) ;
  String res = "" ;
  int i = n , j = n ;
  while ( i > 0 && j > 0 ) {
    if ( dp [ i ] [ j ] == dp [ i - 1 ] [ j - 1 ] + 1 ) {
      res = res + str . charAt ( i - 1 ) ;
      i -- ;
      j -- ;
    }
    else if ( dp [ i ] [ j ] == dp [ i - 1 ] [ j ] ) i -- ;
    else j -- ;
  }
  String reverse = "" ;
  for ( int k = res . length ( ) - 1 ;
  k >= 0 ;
  k -- ) {
    reverse = reverse + res . charAt ( k ) ;
  }
  return reverse ;
}
|||

FIND_INDEX_MAXIMUM_OCCURRING_ELEMENT_EQUAL_PROBABILITY

static void findRandomIndexOfMax ( int arr [ ] , int n ) {
  HashMap < Integer , Integer > mp = new HashMap < Integer , Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( mp . containsKey ( arr [ i ] ) ) {
    mp . put ( arr [ i ] , mp . get ( arr [ i ] ) + 1 ) ;
  }
  else {
    mp . put ( arr [ i ] , 1 ) ;
  }
  int max_element = Integer . MIN_VALUE ;
  int max_so_far = Integer . MIN_VALUE ;
  for ( Map . Entry < Integer , Integer > p : mp . entrySet ( ) ) {
    if ( p . getValue ( ) > max_so_far ) {
      max_so_far = p . getValue ( ) ;
      max_element = p . getKey ( ) ;
    }
  }
  int r = ( int ) ( ( new Random ( ) . nextInt ( max_so_far ) % max_so_far ) + 1 ) ;
  for ( int i = 0 , count = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] == max_element ) count ++ ;
    if ( count == r ) {
      System . out . print ( "Element with maximum frequency present " + "at index " + i + "\n" ) ;
      break ;
    }
  }
}
|||

CHECK_NUMBER_IS_PERFECT_SQUARE_USING_ADDITIONSUBTRACTION

static boolean isPerfectSquare ( int n ) {
  for ( int sum = 0 , i = 1 ;
  sum < n ;
  i += 2 ) {
    sum += i ;
    if ( sum == n ) return true ;
  }
  return false ;
}
|||

N_BONACCI_NUMBERS_1

static void bonacciseries ( int n , int m ) {
  int a [ ] = new int [ m ] ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) a [ i ] = 0 ;
  a [ n - 1 ] = 1 ;
  a [ n ] = 1 ;
  for ( int i = n + 1 ;
  i < m ;
  i ++ ) a [ i ] = 2 * a [ i - 1 ] - a [ i - n - 1 ] ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) System . out . print ( a [ i ] + " " ) ;
}
|||

COUNT_INDEX_PAIRS_EQUAL_ELEMENTS_ARRAY_1

public static int countPairs ( int arr [ ] , int n ) {
  HashMap < Integer , Integer > hm = new HashMap < > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( hm . containsKey ( arr [ i ] ) ) hm . put ( arr [ i ] , hm . get ( arr [ i ] ) + 1 ) ;
    else hm . put ( arr [ i ] , 1 ) ;
  }
  int ans = 0 ;
  for ( Map . Entry < Integer , Integer > it : hm . entrySet ( ) ) {
    int count = it . getValue ( ) ;
    ans += ( count * ( count - 1 ) ) / 2 ;
  }
  return ans ;
}
|||

SORT_EVEN_PLACED_ELEMENTS_INCREASING_ODD_PLACED_DECREASING_ORDER

static void bitonicGenerator ( int arr [ ] , int n ) {
  Vector < Integer > evenArr = new Vector < Integer > ( ) ;
  Vector < Integer > oddArr = new Vector < Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( i % 2 != 1 ) {
      evenArr . add ( arr [ i ] ) ;
    }
    else {
      oddArr . add ( arr [ i ] ) ;
    }
  }
  Collections . sort ( evenArr ) ;
  Collections . sort ( oddArr , Collections . reverseOrder ( ) ) ;
  int i = 0 ;
  for ( int j = 0 ;
  j < evenArr . size ( ) ;
  j ++ ) {
    arr [ i ++ ] = evenArr . get ( j ) ;
  }
  for ( int j = 0 ;
  j < oddArr . size ( ) ;
  j ++ ) {
    arr [ i ++ ] = oddArr . get ( j ) ;
  }
}
|||

DYNAMIC_PROGRAMMING_SET_9_BINOMIAL_COEFFICIENT

static int binomialCoeff ( int n , int k ) {
  if ( k == 0 || k == n ) return 1 ;
  return binomialCoeff ( n - 1 , k - 1 ) + binomialCoeff ( n - 1 , k ) ;
}
|||

WRITE_A_C_PROGRAM_TO_FIND_THE_PARITY_OF_AN_UNSIGNED_INTEGER

static boolean getParity ( int n ) {
  boolean parity = false ;
  while ( n != 0 ) {
    parity = ! parity ;
    n = n & ( n - 1 ) ;
  }
  return parity ;
}
|||

CHECK_WHETHER_LARGE_NUMBER_DIVISIBLE_7

static boolean isDivisible7 ( String num ) {
  int n = num . length ( ) ;
  if ( n == 0 && num . charAt ( 0 ) == '0' ) return true ;
  if ( n % 3 == 1 ) num = "00" + num ;
  if ( n % 3 == 2 ) num = "0" + num ;
  n = num . length ( ) ;
  int gSum = 0 , p = 1 ;
  for ( int i = n - 1 ;
  i >= 0 ;
  i -- ) {
    int group = 0 ;
    group += num . charAt ( i -- ) - '0' ;
    group += ( num . charAt ( i -- ) - '0' ) * 10 ;
    group += ( num . charAt ( i ) - '0' ) * 100 ;
    gSum = gSum + group * p ;
    p = p * - 1 ;
  }
  return ( gSum % 7 == 0 ) ;
}
|||

PRODUCT_NODES_K_TH_LEVEL_TREE_REPRESENTED_STRING

static int productAtKthLevel ( String tree , int k ) {
  int level = - 1 ;
  int product = 1 ;
  int n = tree . length ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( tree . charAt ( i ) == '(' ) level ++ ;
    else if ( tree . charAt ( i ) == ')' ) level -- ;
    else {
      if ( level == k ) product *= ( tree . charAt ( i ) - '0' ) ;
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

static int countGroups ( int position , int previous_sum , int length , String num ) {
  if ( position == length ) return 1 ;
  int res = 0 ;
  int sum = 0 ;
  for ( int i = position ;
  i < length ;
  i ++ ) {
    sum += ( num . charAt ( i ) - '0' ) ;
    if ( sum >= previous_sum ) res += countGroups ( i + 1 , sum , length , num ) ;
  }
  return res ;
}
|||

FIND_THE_ELEMENT_THAT_ODD_NUMBER_OF_TIMES_IN_OLOG_N_TIME

static void search ( int arr [ ] , int low , int high ) {
  if ( low > high ) return ;
  if ( low == high ) {
    System . out . printf ( "The required element is %d " , arr [ low ] ) ;
    return ;
  }
  int mid = ( low + high ) / 2 ;
  if ( mid % 2 == 0 ) {
    if ( arr [ mid ] == arr [ mid + 1 ] ) search ( arr , mid + 2 , high ) ;
    else search ( arr , low , mid ) ;
  }
  else {
    if ( arr [ mid ] == arr [ mid - 1 ] ) search ( arr , mid + 1 , high ) ;
    else search ( arr , low , mid - 1 ) ;
  }
}
|||

DELETE_CONSECUTIVE_WORDS_SEQUENCE_1

static int removeConsecutiveSame ( Vector < String > v ) {
  Stack < String > st = new Stack < > ( ) ;
  for ( int i = 0 ;
  i < v . size ( ) ;
  i ++ ) {
    if ( st . empty ( ) ) st . push ( v . get ( i ) ) ;
    else {
      String str = st . peek ( ) ;
      if ( str . equals ( v . get ( i ) ) ) st . pop ( ) ;
      else st . push ( v . get ( i ) ) ;
    }
  }
  return st . size ( ) ;
}
|||

MINIMUM_NUMBER_OF_JUMPS_TO_REACH_END_OF_A_GIVEN_ARRAY_2

static int minJumps ( int arr [ ] , int n ) {
  int [ ] jumps = new int [ n ] ;
  int min ;
  jumps [ n - 1 ] = 0 ;
  for ( int i = n - 2 ;
  i >= 0 ;
  i -- ) {
    if ( arr [ i ] == 0 ) jumps [ i ] = Integer . MAX_VALUE ;
    else if ( arr [ i ] >= n - i - 1 ) jumps [ i ] = 1 ;
    else {
      min = Integer . MAX_VALUE ;
      for ( int j = i + 1 ;
      j < n && j <= arr [ i ] + i ;
      j ++ ) {
        if ( min > jumps [ j ] ) min = jumps [ j ] ;
      }
      if ( min != Integer . MAX_VALUE ) jumps [ i ] = min + 1 ;
      else jumps [ i ] = min ;
    }
  }
  return jumps [ 0 ] ;
}
|||

PROGRAM_FIND_GCD_FLOATING_POINT_NUMBERS

static double gcd ( double a , double b ) {
  if ( a < b ) return gcd ( b , a ) ;
  if ( Math . abs ( b ) < 0.001 ) return a ;
  else return ( gcd ( b , a - Math . floor ( a / b ) * b ) ) ;
}
|||

MAXIMUM_PROFIT_BY_BUYING_AND_SELLING_A_SHARE_AT_MOST_TWICE

static int maxProfit ( int price [ ] , int n ) {
  int profit [ ] = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) profit [ i ] = 0 ;
  int max_price = price [ n - 1 ] ;
  for ( int i = n - 2 ;
  i >= 0 ;
  i -- ) {
    if ( price [ i ] > max_price ) max_price = price [ i ] ;
    profit [ i ] = Math . max ( profit [ i + 1 ] , max_price - price [ i ] ) ;
  }
  int min_price = price [ 0 ] ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    if ( price [ i ] < min_price ) min_price = price [ i ] ;
    profit [ i ] = Math . max ( profit [ i - 1 ] , profit [ i ] + ( price [ i ] - min_price ) ) ;
  }
  int result = profit [ n - 1 ] ;
  return result ;
}
|||

COUNT_SET_BITS_IN_AN_INTEGER_1

public static int countSetBits ( int n ) {
  if ( n == 0 ) return 0 ;
  else return ( n & 1 ) + countSetBits ( n >> 1 ) ;
}
|||

REORDER_A_ARRAY_ACCORDING_TO_GIVEN_INDEXES

static void reorder ( ) {
  int temp [ ] = new int [ arr . length ] ;
  for ( int i = 0 ;
  i < arr . length ;
  i ++ ) temp [ index [ i ] ] = arr [ i ] ;
  for ( int i = 0 ;
  i < arr . length ;
  i ++ ) {
    arr [ i ] = temp [ i ] ;
    index [ i ] = i ;
  }
}
|||

CHECK_IF_A_GIVEN_ARRAY_CAN_REPRESENT_PREORDER_TRAVERSAL_OF_BINARY_SEARCH_TREE

boolean canRepresentBST ( int pre [ ] , int n ) {
  Stack < Integer > s = new Stack < Integer > ( ) ;
  int root = Integer . MIN_VALUE ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( pre [ i ] < root ) {
      return false ;
    }
    while ( ! s . empty ( ) && s . peek ( ) < pre [ i ] ) {
      root = s . peek ( ) ;
      s . pop ( ) ;
    }
    s . push ( pre [ i ] ) ;
  }
  return true ;
}
|||

FIND_REPETITIVE_ELEMENT_1_N_1_3

static int findRepeating ( int arr [ ] , int n ) {
  int missingElement = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int element = arr [ Math . abs ( arr [ i ] ) ] ;
    if ( element < 0 ) {
      missingElement = arr [ i ] ;
      break ;
    }
    arr [ Math . abs ( arr [ i ] ) ] = - arr [ Math . abs ( arr [ i ] ) ] ;
  }
  return Math . abs ( missingElement ) ;
}
|||

DYNAMIC_PROGRAMMING_SET_8_MATRIX_CHAIN_MULTIPLICATION_1

static int MatrixChainOrder ( int p [ ] , int n ) {
  int m [ ] [ ] = new int [ n ] [ n ] ;
  int i , j , k , L , q ;
  for ( i = 1 ;
  i < n ;
  i ++ ) m [ i ] [ i ] = 0 ;
  for ( L = 2 ;
  L < n ;
  L ++ ) {
    for ( i = 1 ;
    i < n - L + 1 ;
    i ++ ) {
      j = i + L - 1 ;
      if ( j == n ) continue ;
      m [ i ] [ j ] = Integer . MAX_VALUE ;
      for ( k = i ;
      k <= j - 1 ;
      k ++ ) {
        q = m [ i ] [ k ] + m [ k + 1 ] [ j ] + p [ i - 1 ] * p [ k ] * p [ j ] ;
        if ( q < m [ i ] [ j ] ) m [ i ] [ j ] = q ;
      }
    }
  }
  return m [ 1 ] [ n - 1 ] ;
}
|||

COUNT_NUMBER_ISLANDS_EVERY_ISLAND_SEPARATED_LINE

static int countIslands ( int mat [ ] [ ] , int m , int n ) {
  int count = 0 ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( mat [ i ] [ j ] == 'X' ) {
        if ( ( i == 0 || mat [ i - 1 ] [ j ] == 'O' ) && ( j == 0 || mat [ i ] [ j - 1 ] == 'O' ) ) count ++ ;
      }
    }
  }
  return count ;
}
|||

MINIMIZE_MAXAI_BJ_CK_MINAI_BJ_CK_THREE_DIFFERENT_SORTED_ARRAYS

static int solve ( int [ ] A , int [ ] B , int [ ] C ) {
  int i , j , k ;
  i = A . length - 1 ;
  j = B . length - 1 ;
  k = C . length - 1 ;
  int min_diff , current_diff , max_term ;
  min_diff = Math . abs ( Math . max ( A [ i ] , Math . max ( B [ j ] , C [ k ] ) ) - Math . min ( A [ i ] , Math . min ( B [ j ] , C [ k ] ) ) ) ;
  while ( i != - 1 && j != - 1 && k != - 1 ) {
    current_diff = Math . abs ( Math . max ( A [ i ] , Math . max ( B [ j ] , C [ k ] ) ) - Math . min ( A [ i ] , Math . min ( B [ j ] , C [ k ] ) ) ) ;
    if ( current_diff < min_diff ) min_diff = current_diff ;
    max_term = Math . max ( A [ i ] , Math . max ( B [ j ] , C [ k ] ) ) ;
    if ( A [ i ] == max_term ) i -= 1 ;
    else if ( B [ j ] == max_term ) j -= 1 ;
    else k -= 1 ;
  }
  return min_diff ;
}
|||

ROOTS_QUADRATIC_EQUATION

void findRoots ( int a , int b , int c ) {
  if ( a == 0 ) {
    System . out . println ( "Invalid" ) ;
    return ;
  }
  int d = b * b - 4 * a * c ;
  double sqrt_val = sqrt ( abs ( d ) ) ;
  if ( d > 0 ) {
    System . out . println ( "Roots are real and different \n" ) ;
    System . out . println ( ( double ) ( - b + sqrt_val ) / ( 2 * a ) + "\n" + ( double ) ( - b - sqrt_val ) / ( 2 * a ) ) ;
  }
  else {
    System . out . println ( "Roots are complex \n" ) ;
    System . out . println ( - ( double ) b / ( 2 * a ) + " + i" + sqrt_val + "\n" + - ( double ) b / ( 2 * a ) + " - i" + sqrt_val ) ;
  }
}
|||

GIVEN_LEVEL_ORDER_TRAVERSAL_BINARY_TREE_CHECK_TREE_MIN_HEAP

static boolean isMinHeap ( int [ ] level ) {
  int n = level . length - 1 ;
  for ( int i = ( n / 2 - 1 ) ;
  i >= 0 ;
  i -- ) {
    if ( level [ i ] > level [ 2 * i + 1 ] ) return false ;
    if ( 2 * i + 2 < n ) {
      if ( level [ i ] > level [ 2 * i + 2 ] ) return false ;
    }
  }
  return true ;
}
|||

FIND_MINIMUM_ELEMENT_IN_A_SORTED_AND_ROTATED_ARRAY

static int findMin ( int arr [ ] , int low , int high ) {
  if ( high < low ) return arr [ 0 ] ;
  if ( high == low ) return arr [ low ] ;
  int mid = low + ( high - low ) / 2 ;
  if ( mid < high && arr [ mid + 1 ] < arr [ mid ] ) return arr [ mid + 1 ] ;
  if ( mid > low && arr [ mid ] < arr [ mid - 1 ] ) return arr [ mid ] ;
  if ( arr [ high ] > arr [ mid ] ) return findMin ( arr , low , mid - 1 ) ;
  return findMin ( arr , mid + 1 , high ) ;
}
|||

SMALLEST_LENGTH_STRING_WITH_REPEATED_REPLACEMENT_OF_TWO_DISTINCT_ADJACENT

static int stringReduction ( String str ) {
  int n = str . length ( ) ;
  int count [ ] = new int [ 3 ] ;
  for ( int i = 0 ;
  i < n ;
  ++ i ) {
    count [ str . charAt ( i ) - 'a' ] ++ ;
  }
  if ( count [ 0 ] == n || count [ 1 ] == n || count [ 2 ] == n ) {
    return n ;
  }
  if ( ( count [ 0 ] % 2 ) == ( count [ 1 ] % 2 ) && ( count [ 1 ] % 2 ) == ( count [ 2 ] % 2 ) ) {
    return 2 ;
  }
  return 1 ;
}
|||

CHECK_LARGE_NUMBER_DIVISIBLE_3_NOT

static boolean check ( String str ) {
  int n = str . length ( ) ;
  int digitSum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) digitSum += ( str . charAt ( i ) - '0' ) ;
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

static boolean isPresent ( String s , String q ) {
  int [ ] freq = new int [ MAX_CHAR ] ;
  for ( int i = 0 ;
  i < s . length ( ) ;
  i ++ ) freq [ s . charAt ( i ) ] ++ ;
  for ( int i = 0 ;
  i < q . length ( ) ;
  i ++ ) {
    freq [ q . charAt ( i ) ] -- ;
    if ( freq [ q . charAt ( i ) ] < 0 ) return false ;
  }
  return true ;
}
|||

NEXT_POWER_OF_2_1

static int nextPowerOf2 ( int n ) {
  int p = 1 ;
  if ( n > 0 && ( n & ( n - 1 ) ) == 0 ) return n ;
  while ( p < n ) p <<= 1 ;
  return p ;
}
|||

REORDER_A_ARRAY_ACCORDING_TO_GIVEN_INDEXES_1

static void reorder ( ) {
  for ( int i = 0 ;
  i < arr . length ;
  i ++ ) {
    while ( index [ i ] != i ) {
      int oldTargetI = index [ index [ i ] ] ;
      char oldTargetE = ( char ) arr [ index [ i ] ] ;
      arr [ index [ i ] ] = arr [ i ] ;
      index [ index [ i ] ] = index [ i ] ;
      index [ i ] = oldTargetI ;
      arr [ i ] = oldTargetE ;
    }
  }
}
|||

UNBOUNDED_KNAPSACK_REPETITION_ITEMS_ALLOWED

private static int unboundedKnapsack ( int W , int n , int [ ] val , int [ ] wt ) {
  int dp [ ] = new int [ W + 1 ] ;
  for ( int i = 0 ;
  i <= W ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( wt [ j ] <= i ) {
        dp [ i ] = max ( dp [ i ] , dp [ i - wt [ j ] ] + val [ j ] ) ;
      }
    }
  }
  return dp [ W ] ;
}
|||

PROGRAM_CHECK_DIAGONAL_MATRIX_SCALAR_MATRIX

static boolean isDiagonalMatrix ( int mat [ ] [ ] ) {
  for ( int i = 0 ;
  i < N ;
  i ++ ) for ( int j = 0 ;
  j < N ;
  j ++ ) if ( ( i != j ) && ( mat [ i ] [ j ] != 0 ) ) return false ;
  return true ;
}
|||

MAXIMUM_REMOVAL_FROM_ARRAY_WHEN_REMOVAL_TIME_WAITING_TIME

static int maxRemoval ( int arr [ ] , int n ) {
  int count = 0 ;
  int cummulative_sum = 0 ;
  Arrays . sort ( arr ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] >= cummulative_sum ) {
      count ++ ;
      cummulative_sum += arr [ i ] ;
    }
  }
  return count ;
}
|||

PROGRAM_CENSOR_WORD_ASTERISKS_SENTENCE

static String censor ( String text , String word ) {
  String [ ] word_list = text . split ( "\\s+" ) ;
  String result = "" ;
  String stars = "" ;
  for ( int i = 0 ;
  i < word . length ( ) ;
  i ++ ) stars += '*' ;
  int index = 0 ;
  for ( String i : word_list ) {
    if ( i . compareTo ( word ) == 0 ) word_list [ index ] = stars ;
    index ++ ;
  }
  for ( String i : word_list ) result += i + ' ' ;
  return result ;
}
|||

COUNT_STRINGS_WITH_CONSECUTIVE_1S

static int countStrings ( int n ) {
  int a [ ] = new int [ n ] , b [ ] = new int [ n ] ;
  a [ 0 ] = b [ 0 ] = 1 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    a [ i ] = a [ i - 1 ] + b [ i - 1 ] ;
    b [ i ] = a [ i - 1 ] ;
  }
  from 2 ^ n return ( 1 << n ) - a [ n - 1 ] - b [ n - 1 ] ;
}
|||

LENGTH_LONGEST_BALANCED_SUBSEQUENCE

static int maxLength ( String s , int n ) {
  int dp [ ] [ ] = new int [ n ] [ n ] ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) if ( s . charAt ( i ) == '(' && s . charAt ( i + 1 ) == ')' ) dp [ i ] [ i + 1 ] = 2 ;
  for ( int l = 2 ;
  l < n ;
  l ++ ) {
    for ( int i = 0 , j = l ;
    j < n ;
    i ++ , j ++ ) {
      if ( s . charAt ( i ) == '(' && s . charAt ( j ) == ')' ) dp [ i ] [ j ] = 2 + dp [ i + 1 ] [ j - 1 ] ;
      for ( int k = i ;
      k < j ;
      k ++ ) dp [ i ] [ j ] = Math . max ( dp [ i ] [ j ] , dp [ i ] [ k ] + dp [ k + 1 ] [ j ] ) ;
    }
  }
  return dp [ 0 ] [ n - 1 ] ;
}
|||

FIND_THE_POINT_WHERE_MAXIMUM_INTERVALS_OVERLAP

static void findMaxGuests ( int arrl [ ] , int exit [ ] , int n ) {
  Arrays . sort ( arrl ) ;
  Arrays . sort ( exit ) ;
  int guests_in = 1 , max_guests = 1 , time = arrl [ 0 ] ;
  int i = 1 , j = 0 ;
  while ( i < n && j < n ) {
    if ( arrl [ i ] <= exit [ j ] ) {
      guests_in ++ ;
      if ( guests_in > max_guests ) {
        max_guests = guests_in ;
        time = arrl [ i ] ;
      }
      i ++ ;
    }
    else {
      guests_in -- ;
      j ++ ;
    }
  }
  System . out . println ( "Maximum Number of Guests = " + max_guests + " at time " + time ) ;
}
|||

EFFICIENT_WAY_CHECK_WHETHER_N_TH_FIBONACCI_NUMBER_MULTIPLE_10

static boolean isMultipleOf10 ( int n ) {
  if ( n % 15 == 0 ) return true ;
  return false ;
}
|||

MAXIMUM_SUM_PAIRS_SPECIFIC_DIFFERENCE

static int maxSumPairWithDifferenceLessThanK ( int arr [ ] , int N , int K ) {
  Arrays . sort ( arr ) ;
  int dp [ ] = new int [ N ] ;
  dp [ 0 ] = 0 ;
  for ( int i = 1 ;
  i < N ;
  i ++ ) {
    dp [ i ] = dp [ i - 1 ] ;
    if ( arr [ i ] - arr [ i - 1 ] < K ) {
      if ( i >= 2 ) dp [ i ] = Math . max ( dp [ i ] , dp [ i - 2 ] + arr [ i ] + arr [ i - 1 ] ) ;
      else dp [ i ] = Math . max ( dp [ i ] , arr [ i ] + arr [ i - 1 ] ) ;
    }
  }
  return dp [ N - 1 ] ;
}
|||

FIND_K_PAIRS_SMALLEST_SUMS_TWO_ARRAYS

static void kSmallestPair ( int arr1 [ ] , int n1 , int arr2 [ ] , int n2 , int k ) {
  if ( k > n1 * n2 ) {
    System . out . print ( "k pairs don't exist" ) ;
    return ;
  }
  int index2 [ ] = new int [ n1 ] ;
  while ( k > 0 ) {
    int min_sum = Integer . MAX_VALUE ;
    int min_index = 0 ;
    for ( int i1 = 0 ;
    i1 < n1 ;
    i1 ++ ) {
      if ( index2 [ i1 ] < n2 && arr1 [ i1 ] + arr2 [ index2 [ i1 ] ] < min_sum ) {
        min_index = i1 ;
        min_sum = arr1 [ i1 ] + arr2 [ index2 [ i1 ] ] ;
      }
    }
    System . out . print ( "(" + arr1 [ min_index ] + ", " + arr2 [ index2 [ min_index ] ] + ") " ) ;
    index2 [ min_index ] ++ ;
    k -- ;
  }
}
|||

FIRST_UPPERCASE_LETTER_IN_A_STRING_ITERATIVE_AND_RECURSIVE_1

static char first ( String str , int i ) {
  if ( str . charAt ( i ) == '\0' ) return 0 ;
  if ( Character . isUpperCase ( str . charAt ( i ) ) ) return str . charAt ( i ) ;
  return first ( str , i + 1 ) ;
}
|||

FIND_PAIRS_B_ARRAY_B_K

static boolean printPairs ( int arr [ ] , int n , int k ) {
  boolean isPairFound = true ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( i != j && arr [ i ] % arr [ j ] == k ) {
        System . out . print ( "(" + arr [ i ] + ", " + arr [ j ] + ")" + " " ) ;
        isPairFound = true ;
      }
    }
  }
  return isPairFound ;
}
|||

FIND_ARRANGEMENT_QUEUE_GIVEN_TIME

static void solve ( int n , int t , char s [ ] ) {
  for ( int i = 0 ;
  i < t ;
  i ++ ) for ( int j = 0 ;
  j < n - 1 ;
  j ++ ) if ( s [ j ] == 'B' && s [ j + 1 ] == 'G' ) {
    char temp = s [ j ] ;
    s [ j ] = s [ j + 1 ] ;
    s [ j + 1 ] = temp ;
    j ++ ;
  }
  System . out . print ( s ) ;
}
|||

SHORTEST_POSSIBLE_COMBINATION_TWO_STRINGS

static void printSuperSeq ( String a , String b ) {
  int m = a . length ( ) , n = b . length ( ) ;
  int [ ] [ ] dp = new int [ m + 1 ] [ n + 1 ] ;
  for ( int i = 0 ;
  i <= m ;
  i ++ ) {
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      if ( i == 0 ) dp [ i ] [ j ] = j ;
      else if ( j == 0 ) dp [ i ] [ j ] = i ;
      else if ( a . charAt ( i - 1 ) == b . charAt ( j - 1 ) ) dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ] ;
      else dp [ i ] [ j ] = 1 + Math . min ( dp [ i - 1 ] [ j ] , dp [ i ] [ j - 1 ] ) ;
    }
  }
  String res = "" ;
  int i = m , j = n ;
  while ( i > 0 && j > 0 ) {
    if ( a . charAt ( i - 1 ) == b . charAt ( j - 1 ) ) {
      res = a . charAt ( i - 1 ) + res ;
      i -- ;
      j -- ;
    }
    else if ( dp [ i - 1 ] [ j ] < dp [ i ] [ j - 1 ] ) {
      res = a . charAt ( i - 1 ) + res ;
      i -- ;
    }
    else {
      res = b . charAt ( j - 1 ) + res ;
      j -- ;
    }
  }
  while ( i > 0 ) {
    res = a . charAt ( i - 1 ) + res ;
    i -- ;
  }
  while ( j > 0 ) {
    res = b . charAt ( j - 1 ) + res ;
    j -- ;
  }
  System . out . println ( res ) ;
}
|||

COUNT_ROTATIONS_DIVISIBLE_8

static int countRotationsDivBy8 ( String n ) {
  int len = n . length ( ) ;
  int count = 0 ;
  if ( len == 1 ) {
    int oneDigit = n . charAt ( 0 ) - '0' ;
    if ( oneDigit % 8 == 0 ) return 1 ;
    return 0 ;
  }
  if ( len == 2 ) {
    int first = ( n . charAt ( 0 ) - '0' ) * 10 + ( n . charAt ( 1 ) - '0' ) ;
    int second = ( n . charAt ( 1 ) - '0' ) * 10 + ( n . charAt ( 0 ) - '0' ) ;
    if ( first % 8 == 0 ) count ++ ;
    if ( second % 8 == 0 ) count ++ ;
    return count ;
  }
  int threeDigit ;
  for ( int i = 0 ;
  i < ( len - 2 ) ;
  i ++ ) {
    threeDigit = ( n . charAt ( i ) - '0' ) * 100 + ( n . charAt ( i + 1 ) - '0' ) * 10 + ( n . charAt ( i + 2 ) - '0' ) ;
    if ( threeDigit % 8 == 0 ) count ++ ;
  }
  threeDigit = ( n . charAt ( len - 1 ) - '0' ) * 100 + ( n . charAt ( 0 ) - '0' ) * 10 + ( n . charAt ( 1 ) - '0' ) ;
  if ( threeDigit % 8 == 0 ) count ++ ;
  threeDigit = ( n . charAt ( len - 2 ) - '0' ) * 100 + ( n . charAt ( len - 1 ) - '0' ) * 10 + ( n . charAt ( 0 ) - '0' ) ;
  if ( threeDigit % 8 == 0 ) count ++ ;
  return count ;
}
|||

LONGEST_COMMON_SUBSEQUENCE_WITH_AT_MOST_K_CHANGES_ALLOWED

static int lcs ( int [ ] [ ] [ ] dp , int [ ] arr1 , int n , int [ ] arr2 , int m , int k ) {
  if ( k < 0 ) return - 10000000 ;
  if ( n < 0 || m < 0 ) return 0 ;
  int ans = dp [ n ] [ m ] [ k ] ;
  if ( ans != - 1 ) return ans ;
  try {
    ans = Math . max ( lcs ( dp , arr1 , n - 1 , arr2 , m , k ) , lcs ( dp , arr1 , n , arr2 , m - 1 , k ) ) ;
    if ( arr1 [ n - 1 ] == arr2 [ m - 1 ] ) ans = Math . max ( ans , 1 + lcs ( dp , arr1 , n - 1 , arr2 , m - 1 , k ) ) ;
    ans = Math . max ( ans , 1 + lcs ( dp , arr1 , n - 1 , arr2 , m - 1 , k - 1 ) ) ;
  }
  catch ( Exception e ) {
  }
  return ans ;
}
|||

CHECK_LINE_TOUCHES_INTERSECTS_CIRCLE

static void checkCollision ( int a , int b , int c , int x , int y , int radius ) {
  double dist = ( Math . abs ( a * x + b * y + c ) ) / Math . sqrt ( a * a + b * b ) ;
  if ( radius == dist ) System . out . println ( "Touch" ) ;
  else if ( radius > dist ) System . out . println ( "Intersect" ) ;
  else System . out . println ( "Outside" ) ;
}
|||

FIND_THE_MAXIMUM_SUBARRAY_XOR_IN_A_GIVEN_ARRAY

static int maxSubarrayXOR ( int arr [ ] , int n ) {
  int ans = Integer . MIN_VALUE ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int curr_xor = 0 ;
    for ( int j = i ;
    j < n ;
    j ++ ) {
      curr_xor = curr_xor ^ arr [ j ] ;
      ans = Math . max ( ans , curr_xor ) ;
    }
  }
  return ans ;
}
|||

SHORTEST_PATH_EXACTLY_K_EDGES_DIRECTED_WEIGHTED_GRAPH

int shortestPath ( int graph [ ] [ ] , int u , int v , int k ) {
  if ( k == 0 && u == v ) return 0 ;
  if ( k == 1 && graph [ u ] [ v ] != INF ) return graph [ u ] [ v ] ;
  if ( k <= 0 ) return INF ;
  int res = INF ;
  for ( int i = 0 ;
  i < V ;
  i ++ ) {
    if ( graph [ u ] [ i ] != INF && u != i && v != i ) {
      int rec_res = shortestPath ( graph , i , v , k - 1 ) ;
      if ( rec_res != INF ) res = Math . min ( res , graph [ u ] [ i ] + rec_res ) ;
    }
  }
  return res ;
}
|||

FIND_SUBARRAY_WITH_GIVEN_SUM

int subArraySum ( int arr [ ] , int n , int sum ) {
  int curr_sum , i , j ;
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    curr_sum = arr [ i ] ;
    for ( j = i + 1 ;
    j <= n ;
    j ++ ) {
      if ( curr_sum == sum ) {
        int p = j - 1 ;
        System . out . println ( "Sum found between indexes " + i + " and " + p ) ;
        return 1 ;
      }
      if ( curr_sum > sum || j == n ) break ;
      curr_sum = curr_sum + arr [ j ] ;
    }
  }
  System . out . println ( "No subarray found" ) ;
  return 0 ;
}
|||

K_TH_PRIME_FACTOR_GIVEN_NUMBER

static int kPrimeFactor ( int n , int k ) {
  while ( n % 2 == 0 ) {
    k -- ;
    n = n / 2 ;
    if ( k == 0 ) return 2 ;
  }
  for ( int i = 3 ;
  i <= Math . sqrt ( n ) ;
  i = i + 2 ) {
    while ( n % i == 0 ) {
      if ( k == 1 ) return i ;
      k -- ;
      n = n / i ;
    }
  }
  if ( n > 2 && k == 1 ) return n ;
  return - 1 ;
}
|||

FIND_ROTATION_COUNT_ROTATED_SORTED_ARRAY_1

static int countRotations ( int arr [ ] , int low , int high ) {
  if ( high < low ) return 0 ;
  if ( high == low ) return low ;
  int mid = low + ( high - low ) / 2 ;
  if ( mid < high && arr [ mid + 1 ] < arr [ mid ] ) return ( mid + 1 ) ;
  if ( mid > low && arr [ mid ] < arr [ mid - 1 ] ) return mid ;
  if ( arr [ high ] > arr [ mid ] ) return countRotations ( arr , low , mid - 1 ) ;
  return countRotations ( arr , mid + 1 , high ) ;
}
|||

COMPUTE_AVERAGE_TWO_NUMBERS_WITHOUT_OVERFLOW_1

static int compute_average ( int a , int b ) {
  return ( a / 2 ) + ( b / 2 ) + ( ( a % 2 + b % 2 ) / 2 ) ;
}
|||

SORTING_USING_TRIVIAL_HASH_FUNCTION_1

static void sortUsingHash ( int a [ ] , int n ) {
  int max = Arrays . stream ( a ) . max ( ) . getAsInt ( ) ;
  int min = Math . abs ( Arrays . stream ( a ) . min ( ) . getAsInt ( ) ) ;
  int hashpos [ ] = new int [ max + 1 ] ;
  int hashneg [ ] = new int [ min + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( a [ i ] >= 0 ) hashpos [ a [ i ] ] += 1 ;
    else hashneg [ Math . abs ( a [ i ] ) ] += 1 ;
  }
  for ( int i = min ;
  i > 0 ;
  i -- ) {
    if ( hashneg [ i ] > 0 ) {
      for ( int j = 0 ;
      j < hashneg [ i ] ;
      j ++ ) {
        System . out . print ( ( - 1 ) * i + " " ) ;
      }
    }
  }
  for ( int i = 0 ;
  i <= max ;
  i ++ ) {
    if ( hashpos [ i ] > 0 ) {
      for ( int j = 0 ;
      j < hashpos [ i ] ;
      j ++ ) {
        System . out . print ( i + " " ) ;
      }
    }
  }
}
|||

FIND_THE_TWO_REPEATING_ELEMENTS_IN_A_GIVEN_ARRAY_1

void printRepeating ( int arr [ ] , int size ) {
  int count [ ] = new int [ size ] ;
  int i ;
  System . out . println ( "Repeated elements are : " ) ;
  for ( i = 0 ;
  i < size ;
  i ++ ) {
    if ( count [ arr [ i ] ] == 1 ) System . out . print ( arr [ i ] + " " ) ;
    else count [ arr [ i ] ] ++ ;
  }
}
|||

MINIMUM_STEPS_MINIMIZE_N_PER_GIVEN_CONDITION

static int getMinSteps ( int n ) {
  int table [ ] = new int [ n + 1 ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) table [ i ] = n - i ;
  for ( int i = n ;
  i >= 1 ;
  i -- ) {
    if ( ! ( i % 2 > 0 ) ) table [ i / 2 ] = Math . min ( table [ i ] + 1 , table [ i / 2 ] ) ;
    if ( ! ( i % 3 > 0 ) ) table [ i / 3 ] = Math . min ( table [ i ] + 1 , table [ i / 3 ] ) ;
  }
  return table [ 1 ] ;
  |||

COUNT_POSSIBLE_DECODINGS_GIVEN_DIGIT_SEQUENCE_1

static int countDecodingDP ( char digits [ ] , int n ) {
  int count [ ] = new int [ n + 1 ] ;
  count [ 0 ] = 1 ;
  count [ 1 ] = 1 ;
  if ( digits [ 0 ] == '0' ) return 0 ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    count [ i ] = 0 ;
    if ( digits [ i - 1 ] > '0' ) count [ i ] = count [ i - 1 ] ;
    if ( digits [ i - 2 ] == '1' || ( digits [ i - 2 ] == '2' && digits [ i - 1 ] < '7' ) ) count [ i ] += count [ i - 2 ] ;
  }
  return count [ n ] ;
}
|||

EULERS_FOUR_SQUARE_IDENTITY_1

public static void checkEulerFourSquareIdentity ( int a , int b ) {
  int ab = a * b ;
  boolean flag = false ;
  int i = 0 ;
  while ( i * i <= ab ) {
    int j = i ;
    while ( i * i + j * j <= ab ) {
      int k = j ;
      while ( i * i + j * j + k * k <= ab ) {
        double l = Math . sqrt ( ab - ( i * i + j * j + k * k ) ) ;
        if ( Math . floor ( l ) == Math . ceil ( l ) && l >= k ) {
          flag = true ;
          System . out . print ( "i = " + i + "\n" ) ;
          System . out . print ( "j = " + j + "\n" ) ;
          System . out . print ( "k = " + k + "\n" ) ;
          System . out . print ( "l = " + ( int ) l + "\n" ) ;
          System . out . print ( "Product of " + a + " and " + b + " can be written as sum of squares" + " of i, j, k, l \n" ) ;
          System . out . print ( ab + " = " + i + "*" + i + " + " + j + "*" + j + " + " + k + "*" + k + " + " + ( int ) l + "*" + ( int ) l + "\n" ) ;
        }
        k += 1 ;
      }
      j += 1 ;
    }
    i += 1 ;
  }
  if ( flag == false ) {
    System . out . println ( "Solution doesn't exist!" ) ;
    return ;
  }
}
|||

COUNT_NUMBER_INCREASING_SUBSEQUENCES_SIZE_K

static int numOfIncSubseqOfSizeK ( int arr [ ] , int n , int k ) {
  int dp [ ] [ ] = new int [ k ] [ n ] , sum = 0 ;
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
      j < i ;
      j ++ ) {
        if ( arr [ j ] < arr [ i ] ) {
          dp [ l ] [ i ] += dp [ l - 1 ] [ j ] ;
        }
      }
    }
  }
  for ( int i = k - 1 ;
  i < n ;
  i ++ ) {
    sum += dp [ k - 1 ] [ i ] ;
  }
  return sum ;
}
|||

KNAPSACK_PROBLEM_1

static int knapSack ( int W , int wt [ ] , int val [ ] , int n ) {
  int i , w ;
  int K [ ] [ ] = new int [ n + 1 ] [ W + 1 ] ;
  for ( i = 0 ;
  i <= n ;
  i ++ ) {
    for ( w = 0 ;
    w <= W ;
    w ++ ) {
      if ( i == 0 || w == 0 ) K [ i ] [ w ] = 0 ;
      else if ( wt [ i - 1 ] <= w ) K [ i ] [ w ] = max ( val [ i - 1 ] + K [ i - 1 ] [ w - wt [ i - 1 ] ] , K [ i - 1 ] [ w ] ) ;
      else K [ i ] [ w ] = K [ i - 1 ] [ w ] ;
    }
  }
  return K [ n ] [ W ] ;
}
|||

PROGRAM_TO_PRINT_DOUBLE_HEADED_ARROW_PATTERN

static void drawPattern ( int N ) {
  int n = N ;
  int row = 1 ;
  int nst = 1 ;
  int nsp1 = n - 1 ;
  int nsp2 = - 1 ;
  int val1 = row ;
  int val2 = 1 ;
  while ( row <= n ) {
    int csp1 = 1 ;
    while ( csp1 <= nsp1 ) {
      System . out . print ( "  " ) ;
      csp1 = csp1 + 1 ;
    }
    int cst1 = 1 ;
    while ( cst1 <= nst ) {
      System . out . print ( val1 + " " ) ;
      val1 = val1 - 1 ;
      cst1 = cst1 + 1 ;
    }
    int csp2 = 1 ;
    while ( csp2 <= nsp2 ) {
      System . out . print ( "  " ) ;
      csp2 = csp2 + 1 ;
    }
    if ( row != 1 && row != n ) {
      int cst2 = 1 ;
      while ( cst2 <= nst ) {
        System . out . print ( val2 + " " ) ;
        val2 = val2 + 1 ;
        cst2 = cst2 + 1 ;
      }
    }
    System . out . println ( ) ;
    if ( row <= n / 2 ) {
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

static int findInteger ( int arr [ ] , int n ) {
  HashMap < Integer , Integer > hash = new HashMap < > ( ) ;
  int maximum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] < 0 ) hash . put ( Math . abs ( arr [ i ] ) , ( hash . get ( Math . abs ( arr [ i ] ) ) == null ? 0 : hash . get ( Math . abs ( arr [ i ] ) ) ) - 1 ) ;
    else hash . put ( Math . abs ( arr [ i ] ) , ( hash . get ( Math . abs ( arr [ i ] ) ) == null ? 0 : hash . get ( Math . abs ( arr [ i ] ) ) ) + 1 ) ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( hash . get ( arr [ i ] ) > 0 ) return arr [ i ] ;
  return - 1 ;
}
|||

SPACE_OPTIMIZED_SOLUTION_LCS

public static int lcs ( String X , String Y ) {
  int m = X . length ( ) , n = Y . length ( ) ;
  int L [ ] [ ] = new int [ 2 ] [ n + 1 ] ;
  int bi = 0 ;
  for ( int i = 0 ;
  i <= m ;
  i ++ ) {
    bi = i & 1 ;
    for ( int j = 0 ;
    j <= n ;
    j ++ ) {
      if ( i == 0 || j == 0 ) L [ bi ] [ j ] = 0 ;
      else if ( X . charAt ( i - 1 ) == Y . charAt ( j - 1 ) ) L [ bi ] [ j ] = L [ 1 - bi ] [ j - 1 ] + 1 ;
      else L [ bi ] [ j ] = Math . max ( L [ 1 - bi ] [ j ] , L [ bi ] [ j - 1 ] ) ;
    }
  }
  return L [ bi ] [ n ] ;
}
|||

REPRESENT_NUMBER_SUM_MINIMUM_POSSIBLE_PSUEDOBINARY_NUMBERS

public static void psuedoBinary ( int n ) {
  while ( n != 0 ) {
    int temp = n , m = 0 , p = 1 ;
    while ( temp != 0 ) {
      int rem = temp % 10 ;
      temp = temp / 10 ;
      if ( rem != 0 ) m += p ;
      p *= 10 ;
    }
    System . out . print ( m + " " ) ;
    n = n - m ;
  }
  System . out . println ( " " ) ;
}
|||

FIND_NUMBER_CURRENCY_NOTES_SUM_UPTO_GIVEN_AMOUNT

public static void countCurrency ( int amount ) {
  int [ ] notes = new int [ ] {
    2000 , 500 , 200 , 100 , 50 , 20 , 10 , 5 , 1 };
    int [ ] noteCounter = new int [ 9 ] ;
    for ( int i = 0 ;
    i < 9 ;
    i ++ ) {
      if ( amount >= notes [ i ] ) {
        noteCounter [ i ] = amount / notes [ i ] ;
        amount = amount - noteCounter [ i ] * notes [ i ] ;
      }
    }
    System . out . println ( "Currency Count ->" ) ;
    for ( int i = 0 ;
    i < 9 ;
    i ++ ) {
      if ( noteCounter [ i ] != 0 ) {
        System . out . println ( notes [ i ] + " : " + noteCounter [ i ] ) ;
      }
    }
  }
  |||

POSITIVE_ELEMENTS_EVEN_NEGATIVE_ODD_POSITIONS

static void rearrange ( int a [ ] , int size ) {
  int positive = 0 , negative = 1 , temp ;
  while ( true ) {
    while ( positive < size && a [ positive ] >= 0 ) positive += 2 ;
    while ( negative < size && a [ negative ] <= 0 ) negative += 2 ;
    if ( positive < size && negative < size ) {
      temp = a [ positive ] ;
      a [ positive ] = a [ negative ] ;
      a [ negative ] = temp ;
    }
    else break ;
  }
}
|||

FIND_WHETHER_AN_ARRAY_IS_SUBSET_OF_ANOTHER_ARRAY_SET_1

static boolean isSubset ( int arr1 [ ] , int arr2 [ ] , int m , int n ) {
  int i = 0 ;
  int j = 0 ;
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    for ( j = 0 ;
    j < m ;
    j ++ ) if ( arr2 [ i ] == arr1 [ j ] ) break ;
    if ( j == m ) return false ;
  }
  return true ;
}
|||

GIVEN_A_SORTED_AND_ROTATED_ARRAY_FIND_IF_THERE_IS_A_PAIR_WITH_A_GIVEN_SUM

static boolean pairInSortedRotated ( int arr [ ] , int n , int x ) {
  int i ;
  for ( i = 0 ;
  i < n - 1 ;
  i ++ ) if ( arr [ i ] > arr [ i + 1 ] ) break ;
  int l = ( i + 1 ) % n ;
  int r = i ;
  while ( l != r ) {
    if ( arr [ l ] + arr [ r ] == x ) return true ;
    if ( arr [ l ] + arr [ r ] < x ) l = ( l + 1 ) % n ;
    else r = ( n + r - 1 ) % n ;
  }
  return false ;
}
|||

PROGRAM_TO_FIND_REMAINDER_WITHOUT_USING_MODULO_OR_OPERATOR_1

static int getRemainder ( int num , int divisor ) {
  if ( divisor == 0 ) {
    System . out . println ( "Error: divisor " + "can't be zero \n" ) ;
    return - 1 ;
  }
  if ( divisor < 0 ) divisor = - divisor ;
  if ( num < 0 ) num = - num ;
  int i = 1 ;
  int product = 0 ;
  while ( product <= num ) {
    product = divisor * i ;
    i ++ ;
  }
  return num - ( product - divisor ) ;
}
|||

GNOME_SORT_A_STUPID_ONE

static void gnomeSort ( int arr [ ] , int n ) {
  int index = 0 ;
  while ( index < n ) {
    if ( index == 0 ) index ++ ;
    if ( arr [ index ] >= arr [ index - 1 ] ) index ++ ;
    else {
      int temp = 0 ;
      temp = arr [ index ] ;
      arr [ index ] = arr [ index - 1 ] ;
      arr [ index - 1 ] = temp ;
      index -- ;
    }
  }
  return ;
}
|||

NUMBER_WAYS_INSERT_CHARACTER_INCREASE_LCS_ONE

static int numberofways ( String A , String B , int N , int M ) {
  Vector < Integer > [ ] pos = new Vector [ MAX ] ;
  for ( int i = 0 ;
  i < MAX ;
  i ++ ) pos [ i ] = new Vector < > ( ) ;
  for ( int i = 0 ;
  i < M ;
  i ++ ) pos [ B . charAt ( i ) ] . add ( i + 1 ) ;
  int [ ] [ ] dpl = new int [ N + 2 ] [ M + 2 ] ;
  for ( int i = 1 ;
  i <= N ;
  i ++ ) {
    for ( int j = 1 ;
    j <= M ;
    j ++ ) {
      if ( A . charAt ( i - 1 ) == B . charAt ( j - 1 ) ) dpl [ i ] [ j ] = dpl [ i - 1 ] [ j - 1 ] + 1 ;
      else dpl [ i ] [ j ] = Math . max ( dpl [ i - 1 ] [ j ] , dpl [ i ] [ j - 1 ] ) ;
    }
  }
  int LCS = dpl [ N ] [ M ] ;
  int [ ] [ ] dpr = new int [ N + 2 ] [ M + 2 ] ;
  for ( int i = N ;
  i >= 1 ;
  i -- ) {
    for ( int j = M ;
    j >= 1 ;
    j -- ) {
      if ( A . charAt ( i - 1 ) == B . charAt ( j - 1 ) ) dpr [ i ] [ j ] = dpr [ i + 1 ] [ j + 1 ] + 1 ;
      else dpr [ i ] [ j ] = Math . max ( dpr [ i + 1 ] [ j ] , dpr [ i ] [ j + 1 ] ) ;
    }
  }
  int ans = 0 ;
  for ( int i = 0 ;
  i <= N ;
  i ++ ) {
    for ( int j = 0 ;
    j < MAX ;
    j ++ ) {
      for ( int x : pos [ j ] ) {
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
  PriorityQueue < Integer > pq = new PriorityQueue < > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) pq . add ( arr [ i ] ) ;
  int count = 0 , ans = 1 ;
  while ( pq . isEmpty ( ) == false && count < k ) {
    ans = ans * pq . element ( ) ;
    pq . remove ( ) ;
    count ++ ;
  }
  return ans ;
}
|||

FIND_UNIQUE_ELEMENTS_MATRIX

static void unique ( int mat [ ] [ ] , int n , int m ) {
  int maximum = 0 , flag = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) for ( int j = 0 ;
  j < m ;
  j ++ ) if ( maximum < mat [ i ] [ j ] ) maximum = mat [ i ] [ j ] ;
  int b [ ] = new int [ maximum + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) for ( int j = 0 ;
  j < m ;
  j ++ ) b [ mat [ i ] [ j ] ] ++ ;
  for ( int i = 1 ;
  i <= maximum ;
  i ++ ) if ( b [ i ] == 1 ) System . out . print ( i + " " ) ;
  flag = 1 ;
  if ( flag == 0 ) {
    System . out . println ( "No unique element " + "in the matrix" ) ;
  }
}
|||

LONGEST_SUBSEQUENCE_SUCH_THAT_DIFFERENCE_BETWEEN_ADJACENTS_IS_ONE

static int longestSubseqWithDiffOne ( int arr [ ] , int n ) {
  int dp [ ] = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) dp [ i ] = 1 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < i ;
    j ++ ) {
      if ( ( arr [ i ] == arr [ j ] + 1 ) || ( arr [ i ] == arr [ j ] - 1 ) ) dp [ i ] = Math . max ( dp [ i ] , dp [ j ] + 1 ) ;
    }
  }
  int result = 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( result < dp [ i ] ) result = dp [ i ] ;
  return result ;
}
|||

C_PROGRAM_CONCATENATE_STRING_GIVEN_NUMBER_TIMES

static String repeat ( String s , int n ) {
  String s1 = s ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) s += s1 ;
  return s ;
}
|||

SEARCHING_FOR_PATTERNS_SET_1_NAIVE_PATTERN_SEARCHING

public static void search ( String txt , String pat ) {
  int M = pat . length ( ) ;
  int N = txt . length ( ) ;
  for ( int i = 0 ;
  i <= N - M ;
  i ++ ) {
    int j ;
    for ( j = 0 ;
    j < M ;
    j ++ ) if ( txt . charAt ( i + j ) != pat . charAt ( j ) ) break ;
    if ( j == M ) System . out . println ( "Pattern found at index " + i ) ;
  }
}
|||

COUNT_POSSIBLE_PATHS_SOURCE_DESTINATION_EXACTLY_K_EDGES

int countwalks ( int graph [ ] [ ] , int u , int v , int k ) {
  if ( k == 0 && u == v ) return 1 ;
  if ( k == 1 && graph [ u ] [ v ] == 1 ) return 1 ;
  if ( k <= 0 ) return 0 ;
  int count = 0 ;
  for ( int i = 0 ;
  i < V ;
  i ++ ) if ( graph [ u ] [ i ] == 1 ) count += countwalks ( graph , i , v , k - 1 ) ;
  return count ;
}
|||

COUNT_DIVISIBLE_PAIRS_ARRAY

static int countDivisibles ( int arr [ ] , int n ) {
  int res = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) for ( int j = i + 1 ;
  j < n ;
  j ++ ) if ( arr [ i ] % arr [ j ] == 0 || arr [ j ] % arr [ i ] == 0 ) res ++ ;
  return res ;
}
|||

PROGRAM_TO_CHECK_IF_A_MATRIX_IS_SYMMETRIC

static boolean isSymmetric ( int mat [ ] [ ] , int N ) {
  for ( int i = 0 ;
  i < N ;
  i ++ ) for ( int j = 0 ;
  j < N ;
  j ++ ) if ( mat [ i ] [ j ] != mat [ j ] [ i ] ) return false ;
  return true ;
}
|||

COUNT_PALINDROME_SUB_STRINGS_STRING

static int CountPS ( char str [ ] , int n ) {
  int dp [ ] [ ] = new int [ n ] [ n ] ;
  boolean P [ ] [ ] = new boolean [ n ] [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) P [ i ] [ i ] = true ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    if ( str [ i ] == str [ i + 1 ] ) {
      P [ i ] [ i + 1 ] = true ;
      dp [ i ] [ i + 1 ] = 1 ;
    }
  }
  for ( int gap = 2 ;
  gap < n ;
  gap ++ ) {
    for ( int i = 0 ;
    i < n - gap ;
    i ++ ) {
      int j = gap + i ;
      if ( str [ i ] == str [ j ] && P [ i + 1 ] [ j - 1 ] ) P [ i ] [ j ] = true ;
      if ( P [ i ] [ j ] == true ) dp [ i ] [ j ] = dp [ i ] [ j - 1 ] + dp [ i + 1 ] [ j ] + 1 - dp [ i + 1 ] [ j - 1 ] ;
      else dp [ i ] [ j ] = dp [ i ] [ j - 1 ] + dp [ i + 1 ] [ j ] - dp [ i + 1 ] [ j - 1 ] ;
    }
  }
  return dp [ 0 ] [ n - 1 ] ;
}
|||

WAYS_SUM_N_USING_ARRAY_ELEMENTS_REPETITION_ALLOWED

static int countWays ( int N ) {
  int count [ ] = new int [ N + 1 ] ;
  count [ 0 ] = 1 ;
  for ( int i = 1 ;
  i <= N ;
  i ++ ) for ( int j = 0 ;
  j < arr . length ;
  j ++ ) if ( i >= arr [ j ] ) count [ i ] += count [ i - arr [ j ] ] ;
  return count [ N ] ;
}
|||

MINIMUM_NUMBER_OF_OPERATIONS_TO_MOVE_ALL_UPPERCASE_CHARACTERS_BEFORE_ALL_LOWER_CASE_CHARACTERS

static int minOperations ( String str , int n ) {
  int i , lastUpper = - 1 , firstLower = - 1 ;
  for ( i = n - 1 ;
  i >= 0 ;
  i -- ) {
    if ( Character . isUpperCase ( str . charAt ( i ) ) ) {
      lastUpper = i ;
      break ;
    }
  }
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    if ( Character . isLowerCase ( str . charAt ( i ) ) ) {
      firstLower = i ;
      break ;
    }
  }
  if ( lastUpper == - 1 || firstLower == - 1 ) return 0 ;
  int countUpper = 0 ;
  for ( i = firstLower ;
  i < n ;
  i ++ ) {
    if ( Character . isUpperCase ( str . charAt ( i ) ) ) {
      countUpper ++ ;
    }
  }
  int countLower = 0 ;
  for ( i = 0 ;
  i < lastUpper ;
  i ++ ) {
    if ( Character . isLowerCase ( str . charAt ( i ) ) ) {
      countLower ++ ;
    }
  }
  return Math . min ( countLower , countUpper ) ;
}
|||

PRINT_A_GIVEN_MATRIX_IN_SPIRAL_FORM

static void spiralPrint ( int m , int n , int a [ ] [ ] ) {
  int i , k = 0 , l = 0 ;
  while ( k < m && l < n ) {
    for ( i = l ;
    i < n ;
    ++ i ) {
      System . out . print ( a [ k ] [ i ] + " " ) ;
    }
    k ++ ;
    for ( i = k ;
    i < m ;
    ++ i ) {
      System . out . print ( a [ i ] [ n - 1 ] + " " ) ;
    }
    n -- ;
    if ( k < m ) {
      for ( i = n - 1 ;
      i >= l ;
      -- i ) {
        System . out . print ( a [ m - 1 ] [ i ] + " " ) ;
      }
      m -- ;
    }
    if ( l < n ) {
      for ( i = m - 1 ;
      i >= k ;
      -- i ) {
        System . out . print ( a [ i ] [ l ] + " " ) ;
      }
      l ++ ;
    }
  }
}
|||

FIND_DISTINCT_INTEGERS_FOR_A_TRIPLET_WITH_GIVEN_PRODUCT

static void findTriplets ( int x ) {
  Vector < Integer > fact = new Vector < Integer > ( ) ;
  HashSet < Integer > factors = new HashSet < Integer > ( ) ;
  for ( int i = 2 ;
  i <= Math . sqrt ( x ) ;
  i ++ ) {
    if ( x % i == 0 ) {
      fact . add ( i ) ;
      if ( x / i != i ) fact . add ( x / i ) ;
      factors . add ( i ) ;
      factors . add ( x / i ) ;
    }
  }
  boolean found = false ;
  int k = fact . size ( ) ;
  for ( int i = 0 ;
  i < k ;
  i ++ ) {
    int a = fact . get ( i ) ;
    for ( int j = 0 ;
    j < k ;
    j ++ ) {
      int b = fact . get ( j ) ;
      if ( ( a != b ) && ( x % ( a * b ) == 0 ) && ( x / ( a * b ) != a ) && ( x / ( a * b ) != b ) && ( x / ( a * b ) != 1 ) ) {
        System . out . print ( a + " " + b + " " + ( x / ( a * b ) ) ) ;
        found = true ;
        break ;
      }
    }
    if ( found ) break ;
  }
  if ( ! found ) System . out . print ( "-1" ) ;
}
|||

SUM_TWO_LARGE_NUMBERS_1

static String findSum ( String str1 , String str2 ) {
  if ( str1 . length ( ) > str2 . length ( ) ) {
    String t = str1 ;
    str1 = str2 ;
    str2 = t ;
  }
  String str = "" ;
  int n1 = str1 . length ( ) , n2 = str2 . length ( ) ;
  int diff = n2 - n1 ;
  int carry = 0 ;
  for ( int i = n1 - 1 ;
  i >= 0 ;
  i -- ) {
    int sum = ( ( int ) ( str1 . charAt ( i ) - '0' ) + ( int ) ( str2 . charAt ( i + diff ) - '0' ) + carry ) ;
    str += ( char ) ( sum % 10 + '0' ) ;
    carry = sum / 10 ;
  }
  for ( int i = n2 - n1 - 1 ;
  i >= 0 ;
  i -- ) {
    int sum = ( ( int ) ( str2 . charAt ( i ) - '0' ) + carry ) ;
    str += ( char ) ( sum % 10 + '0' ) ;
    carry = sum / 10 ;
  }
  if ( carry > 0 ) str += ( char ) ( carry + '0' ) ;
  return new StringBuilder ( str ) . reverse ( ) . toString ( ) ;
}
|||

COCKTAIL_SORT

void cocktailSort ( int a [ ] ) {
  boolean swapped = true ;
  int start = 0 ;
  int end = a . length ;
  while ( swapped == true ) {
    swapped = false ;
    for ( int i = start ;
    i < end - 1 ;
    ++ i ) {
      if ( a [ i ] > a [ i + 1 ] ) {
        int temp = a [ i ] ;
        a [ i ] = a [ i + 1 ] ;
        a [ i + 1 ] = temp ;
        swapped = true ;
      }
    }
    if ( swapped == false ) break ;
    swapped = false ;
    end = end - 1 ;
    for ( int i = end - 1 ;
    i >= start ;
    i -- ) {
      if ( a [ i ] > a [ i + 1 ] ) {
        int temp = a [ i ] ;
        a [ i ] = a [ i + 1 ] ;
        a [ i + 1 ] = temp ;
        swapped = true ;
      }
    }
    start = start + 1 ;
  }
}
|||

COUNT_DERANGEMENTS_PERMUTATION_SUCH_THAT_NO_ELEMENT_APPEARS_IN_ITS_ORIGINAL_POSITION_1

static int countDer ( int n ) {
  int der [ ] = new int [ n + 1 ] ;
  der [ 0 ] = 1 ;
  der [ 1 ] = 0 ;
  der [ 2 ] = 1 ;
  for ( int i = 3 ;
  i <= n ;
  ++ i ) der [ i ] = ( i - 1 ) * ( der [ i - 1 ] + der [ i - 2 ] ) ;
  return der [ n ] ;
}
|||

MAXIMUM_PRODUCT_SUBARRAY_ADDED_NEGATIVE_PRODUCT_CASE

static int findMaxProduct ( int arr [ ] , int n ) {
  int i ;
  int ans = Integer . MIN_VALUE ;
  int maxval = 1 ;
  int minval = 1 ;
  int prevMax ;
  for ( i = 0 ;
  i < n ;
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
      prevMax = maxval ;
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

static void assign ( int a [ ] , int n ) {
  Arrays . sort ( a ) ;
  int ans [ ] = new int [ n ] ;
  int p = 0 , q = n - 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( i + 1 ) % 2 == 0 ) ans [ i ] = a [ q -- ] ;
    else ans [ i ] = a [ p ++ ] ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) System . out . print ( ans [ i ] + " " ) ;
}
|||

FRIENDS_PAIRING_PROBLEM

static int countFriendsPairings ( int n ) {
  int dp [ ] = new int [ n + 1 ] ;
  for ( int i = 0 ;
  i <= n ;
  i ++ ) {
    if ( i <= 2 ) dp [ i ] = i ;
    else dp [ i ] = dp [ i - 1 ] + ( i - 1 ) * dp [ i - 2 ] ;
  }
  return dp [ n ] ;
}
|||

PRIME_NUMBERS

static boolean isPrime ( int n ) {
  if ( n <= 1 ) return false ;
  for ( int i = 2 ;
  i < n ;
  i ++ ) if ( n % i == 0 ) return false ;
  return true ;
}
|||

PROBABILITY_REACHING_POINT_2_3_STEPS_TIME

static float find_prob ( int N , float P ) {
  double dp [ ] = new double [ N + 1 ] ;
  dp [ 0 ] = 1 ;
  dp [ 1 ] = 0 ;
  dp [ 2 ] = P ;
  dp [ 3 ] = 1 - P ;
  for ( int i = 4 ;
  i <= N ;
  ++ i ) dp [ i ] = ( P ) * dp [ i - 2 ] + ( 1 - P ) * dp [ i - 3 ] ;
  return ( ( float ) ( dp [ N ] ) ) ;
}
|||

SMALLEST_OF_THREE_INTEGERS_WITHOUT_COMPARISON_OPERATORS_1

static int smallest ( int x , int y , int z ) {
  if ( ( y / x ) != 1 ) return ( ( y / z ) != 1 ) ? y : z ;
  return ( ( x / z ) != 1 ) ? x : z ;
}
|||

COMMON_ELEMENTS_IN_ALL_ROWS_OF_A_GIVEN_MATRIX

static void printCommonElements ( int mat [ ] [ ] ) {
  Map < Integer , Integer > mp = new HashMap < > ( ) ;
  for ( int j = 0 ;
  j < N ;
  j ++ ) mp . put ( mat [ 0 ] [ j ] , 1 ) ;
  for ( int i = 1 ;
  i < M ;
  i ++ ) {
    for ( int j = 0 ;
    j < N ;
    j ++ ) {
      if ( mp . get ( mat [ i ] [ j ] ) != null && mp . get ( mat [ i ] [ j ] ) == i ) {
        mp . put ( mat [ i ] [ j ] , i + 1 ) ;
        if ( i == M - 1 ) System . out . print ( mat [ i ] [ j ] + " " ) ;
      }
    }
  }
}
|||

DETECTING_NEGATIVE_CYCLE_USING_FLOYD_WARSHALL

static boolean negCyclefloydWarshall ( int graph [ ] [ ] ) {
  int dist [ ] [ ] = new int [ V ] [ V ] , i , j , k ;
  for ( i = 0 ;
  i < V ;
  i ++ ) for ( j = 0 ;
  j < V ;
  j ++ ) dist [ i ] [ j ] = graph [ i ] [ j ] ;
  for ( k = 0 ;
  k < V ;
  k ++ ) {
    for ( i = 0 ;
    i < V ;
    i ++ ) {
      for ( j = 0 ;
      j < V ;
      j ++ ) {
        if ( dist [ i ] [ k ] + dist [ k ] [ j ] < dist [ i ] [ j ] ) dist [ i ] [ j ] = dist [ i ] [ k ] + dist [ k ] [ j ] ;
      }
    }
  }
  for ( i = 0 ;
  i < V ;
  i ++ ) if ( dist [ i ] [ i ] < 0 ) return true ;
  return false ;
}
|||

PROGRAM_SORT_STRING_DESCENDING_ORDER

static void sortString ( String str ) {
  int charCount [ ] = new int [ MAX_CHAR ] ;
  for ( int i = 0 ;
  i < str . length ( ) ;
  i ++ ) {
    charCount [ str . charAt ( i ) - 'a' ] ++ ;
  }
  for ( int i = MAX_CHAR - 1 ;
  i >= 0 ;
  i -- ) {
    for ( int j = 0 ;
    j < charCount [ i ] ;
    j ++ ) {
      System . out . print ( ( char ) ( 'a' + i ) ) ;
    }
  }
}
|||

COUNT_PAIRS_WITH_GIVEN_SUM

public static void getPairsCount ( int [ ] arr , int sum ) {
  int count = 0 ;
  for ( int i = 0 ;
  i < arr . length ;
  i ++ ) for ( int j = i + 1 ;
  j < arr . length ;
  j ++ ) if ( ( arr [ i ] + arr [ j ] ) == sum ) count ++ ;
  System . out . printf ( "Count of pairs is %d" , count ) ;
}
|||

SUM_SERIES_12_32_52_2N_12_1

static int sumOfSeries ( int n ) {
  return ( n * ( 2 * n - 1 ) * ( 2 * n + 1 ) ) / 3 ;
}
|||

MAXIMUM_DIFFERENCE_BETWEEN_FREQUENCY_OF_TWO_ELEMENTS_SUCH_THAT_ELEMENT_HAVING_GREATER_FREQUENCY_IS_ALSO_GREATER

static int maxdiff ( int arr [ ] , int n ) {
  Map < Integer , Integer > freq = new HashMap < > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) freq . put ( arr [ i ] , freq . get ( arr [ i ] ) == null ? 1 : freq . get ( arr [ i ] ) + 1 ) ;
  int ans = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( freq . get ( arr [ i ] ) > freq . get ( arr [ j ] ) && arr [ i ] > arr [ j ] ) ans = Math . max ( ans , freq . get ( arr [ i ] ) - freq . get ( arr [ j ] ) ) ;
      else if ( freq . get ( arr [ i ] ) < freq . get ( arr [ j ] ) && arr [ i ] < arr [ j ] ) ans = Math . max ( ans , freq . get ( arr [ j ] ) - freq . get ( arr [ i ] ) ) ;
    }
  }
  return ans ;
}
|||

SHIFT_MATRIX_ELEMENTS_K

static void shiftMatrixByK ( int [ ] [ ] mat , int k ) {
  if ( k > N ) {
    System . out . print ( "Shifting is" + " not possible" ) ;
    return ;
  }
  int j = 0 ;
  while ( j < N ) {
    for ( int i = k ;
    i < N ;
    i ++ ) System . out . print ( mat [ j ] [ i ] + " " ) ;
    for ( int i = 0 ;
    i < k ;
    i ++ ) System . out . print ( mat [ j ] [ i ] + " " ) ;
    System . out . println ( ) ;
    j ++ ;
  }
}
|||

MAXIMUM_AND_MINIMUM_IN_A_SQUARE_MATRIX

static void maxMin ( int arr [ ] [ ] , int n ) {
  int min = + 2147483647 ;
  int max = - 2147483648 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= n / 2 ;
    j ++ ) {
      if ( arr [ i ] [ j ] > arr [ i ] [ n - j - 1 ] ) {
        if ( min > arr [ i ] [ n - j - 1 ] ) min = arr [ i ] [ n - j - 1 ] ;
        if ( max < arr [ i ] [ j ] ) max = arr [ i ] [ j ] ;
      }
      else {
        if ( min > arr [ i ] [ j ] ) min = arr [ i ] [ j ] ;
        if ( max < arr [ i ] [ n - j - 1 ] ) max = arr [ i ] [ n - j - 1 ] ;
      }
    }
  }
  System . out . print ( "Maximum = " + max + ", Minimum = " + min ) ;
}
|||

FIND_PAIR_WITH_GREATEST_PRODUCT_IN_ARRAY_1

static int findGreatest ( int arr [ ] , int n ) {
  Map < Integer , Integer > m = new HashMap < > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( m . containsKey ( arr [ i ] ) ) {
      m . put ( arr [ i ] , m . get ( arr [ i ] ) + 1 ) ;
    }
    else {
      m . put ( arr [ i ] , m . get ( arr [ i ] ) ) ;
    }
  }
  Arrays . sort ( arr ) ;
  for ( int i = n - 1 ;
  i > 1 ;
  i -- ) {
    for ( int j = 0 ;
    j < i && arr [ j ] <= Math . sqrt ( arr [ i ] ) ;
    j ++ ) {
      if ( arr [ i ] % arr [ j ] == 0 ) {
        int result = arr [ i ] / arr [ j ] ;
        if ( result != arr [ j ] && m . get ( result ) == null || m . get ( result ) > 0 ) {
          return arr [ i ] ;
        }
        else if ( result == arr [ j ] && m . get ( result ) > 1 ) {
          return arr [ i ] ;
        }
      }
    }
  }
  return - 1 ;
}
|||

0_1_KNAPSACK_PROBLEM_DP_10_1

static int knapSack ( int W , int wt [ ] , int val [ ] , int n ) {
  int i , w ;
  int K [ ] [ ] = new int [ n + 1 ] [ W + 1 ] ;
  for ( i = 0 ;
  i <= n ;
  i ++ ) {
    for ( w = 0 ;
    w <= W ;
    w ++ ) {
      if ( i == 0 || w == 0 ) K [ i ] [ w ] = 0 ;
      else if ( wt [ i - 1 ] <= w ) K [ i ] [ w ] = max ( val [ i - 1 ] + K [ i - 1 ] [ w - wt [ i - 1 ] ] , K [ i - 1 ] [ w ] ) ;
      else K [ i ] [ w ] = K [ i - 1 ] [ w ] ;
    }
  }
  return K [ n ] [ W ] ;
}
|||

PROGRAM_DECIMAL_OCTAL_CONVERSION

static void decToOctal ( int n ) {
  int [ ] octalNum = new int [ 100 ] ;
  int i = 0 ;
  while ( n != 0 ) {
    octalNum [ i ] = n % 8 ;
    n = n / 8 ;
    i ++ ;
  }
  for ( int j = i - 1 ;
  j >= 0 ;
  j -- ) System . out . print ( octalNum [ j ] ) ;
}
|||

SUBSEQUENCES_SIZE_THREE_ARRAY_WHOSE_SUM_DIVISIBLE_M_1

static int countSubSeq ( int A [ ] , int N , int M ) {
  int ans = 0 ;
  int h [ ] = new int [ M ] ;
  Arrays . fill ( h , 0 ) ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) {
    A [ i ] = A [ i ] % M ;
    h [ A [ i ] ] ++ ;
  }
  for ( int i = 0 ;
  i < M ;
  i ++ ) {
    for ( int j = i ;
    j < M ;
    j ++ ) {
      int rem = ( M - ( i + j ) % M ) % M ;
      if ( rem < j ) continue ;
      if ( i == j && rem == j ) ans += h [ i ] * ( h [ i ] - 1 ) * ( h [ i ] - 2 ) / 6 ;
      else if ( i == j ) ans += h [ i ] * ( h [ i ] - 1 ) * h [ rem ] / 2 ;
      else if ( i == rem ) ans += h [ i ] * ( h [ i ] - 1 ) * h [ j ] / 2 ;
      else if ( rem == j ) ans += h [ j ] * ( h [ j ] - 1 ) * h [ i ] / 2 ;
      else ans = ans + h [ i ] * h [ j ] * h [ rem ] ;
    }
  }
  return ans ;
}
|||

COUNT_FIBONACCI_NUMBERS_GIVEN_RANGE_LOG_TIME

static int countFibs ( int low , int high ) {
  int f1 = 0 , f2 = 1 , f3 = 1 ;
  int result = 0 ;
  while ( f1 <= high ) {
    if ( f1 >= low ) result ++ ;
    f1 = f2 ;
    f2 = f3 ;
    f3 = f1 + f2 ;
  }
  return result ;
}
|||

FIND_WHETHER_A_GIVEN_NUMBER_IS_A_POWER_OF_4_OR_NOT_1

static int isPowerOfFour ( int n ) {
  int count = 0 ;
  int x = n & ( n - 1 ) ;
  if ( n > 0 && x == 0 ) {
    while ( n > 1 ) {
      n >>= 1 ;
      count += 1 ;
    }
    return ( count % 2 == 0 ) ? 1 : 0 ;
  }
  return 0 ;
}
|||

FIND_SUM_EVEN_FACTORS_NUMBER

public static int sumofFactors ( int n ) {
  if ( n % 2 != 0 ) return 0 ;
  int res = 1 ;
  for ( int i = 2 ;
  i <= Math . sqrt ( n ) ;
  i ++ ) {
    int count = 0 , curr_sum = 1 ;
    int curr_term = 1 ;
    while ( n % i == 0 ) {
      count ++ ;
      n = n / i ;
      if ( i == 2 && count == 1 ) curr_sum = 0 ;
      curr_term *= i ;
      curr_sum += curr_term ;
    }
    res *= curr_sum ;
  }
  if ( n >= 2 ) res *= ( 1 + n ) ;
  return res ;
}
|||

FIND_SUM_NON_REPEATING_DISTINCT_ELEMENTS_ARRAY

static int findSum ( int arr [ ] , int n ) {
  int sum = 0 ;
  HashSet < Integer > s = new HashSet < Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ! s . contains ( arr [ i ] ) ) {
      sum += arr [ i ] ;
      s . add ( arr [ i ] ) ;
    }
  }
  return sum ;
}
|||

DYNAMIC_PROGRAMMING_SET_17_PALINDROME_PARTITIONING_1

static int minPalPartion ( String str ) {
  int n = str . length ( ) ;
  int [ ] C = new int [ n ] ;
  boolean [ ] [ ] P = new boolean [ n ] [ n ] ;
  int i , j , k , L ;
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    P [ i ] [ i ] = true ;
  }
  for ( L = 2 ;
  L <= n ;
  L ++ ) {
    for ( i = 0 ;
    i < n - L + 1 ;
    i ++ ) {
      j = i + L - 1 ;
      if ( L == 2 ) P [ i ] [ j ] = ( str . charAt ( i ) == str . charAt ( j ) ) ;
      else P [ i ] [ j ] = ( str . charAt ( i ) == str . charAt ( j ) ) && P [ i + 1 ] [ j - 1 ] ;
    }
  }
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    if ( P [ 0 ] [ i ] == true ) C [ i ] = 0 ;
    else {
      C [ i ] = Integer . MAX_VALUE ;
      for ( j = 0 ;
      j < i ;
      j ++ ) {
        if ( P [ j + 1 ] [ i ] == true && 1 + C [ j ] < C [ i ] ) C [ i ] = 1 + C [ j ] ;
      }
    }
  }
  return C [ n - 1 ] ;
}
|||

MINIMUM_POSITIVE_POINTS_TO_REACH_DESTINATION

static int minInitialPoints ( int points [ ] [ ] , int R , int C ) {
  int dp [ ] [ ] = new int [ R ] [ C ] ;
  int m = R , n = C ;
  dp [ m - 1 ] [ n - 1 ] = points [ m - 1 ] [ n - 1 ] > 0 ? 1 : Math . abs ( points [ m - 1 ] [ n - 1 ] ) + 1 ;
  for ( int i = m - 2 ;
  i >= 0 ;
  i -- ) dp [ i ] [ n - 1 ] = Math . max ( dp [ i + 1 ] [ n - 1 ] - points [ i ] [ n - 1 ] , 1 ) ;
  for ( int j = n - 2 ;
  j >= 0 ;
  j -- ) dp [ m - 1 ] [ j ] = Math . max ( dp [ m - 1 ] [ j + 1 ] - points [ m - 1 ] [ j ] , 1 ) ;
  for ( int i = m - 2 ;
  i >= 0 ;
  i -- ) {
    for ( int j = n - 2 ;
    j >= 0 ;
    j -- ) {
      int min_points_on_exit = Math . min ( dp [ i + 1 ] [ j ] , dp [ i ] [ j + 1 ] ) ;
      dp [ i ] [ j ] = Math . max ( min_points_on_exit - points [ i ] [ j ] , 1 ) ;
    }
  }
  return dp [ 0 ] [ 0 ] ;
}
|||

COUNT_OF_PAIRS_SATISFYING_THE_GIVEN_CONDITION

static int countPair ( int a , int b ) {
  String s = String . valueOf ( b ) ;
  int i ;
  for ( i = 0 ;
  i < s . length ( ) ;
  i ++ ) {
    if ( s . charAt ( i ) != '9' ) break ;
  }
  int result ;
  if ( i == s . length ( ) ) result = a * s . length ( ) ;
  else result = a * ( s . length ( ) - 1 ) ;
  return result ;
}
|||

SURVIVAL

static void survival ( int S , int N , int M ) {
  if ( ( ( N * 6 ) < ( M * 7 ) && S > 6 ) || M > N ) System . out . println ( "No" ) ;
  else {
    int days = ( M * S ) / N ;
    if ( ( ( M * S ) % N ) != 0 ) days ++ ;
    System . out . println ( "Yes " + days ) ;
  }
}
|||

INTERLEAVE_FIRST_HALF_QUEUE_SECOND_HALF

static void interLeaveQueue ( Queue < Integer > q ) {
  if ( q . size ( ) % 2 != 0 ) System . out . println ( "Input even number of integers." ) ;
  Stack < Integer > s = new Stack < > ( ) ;
  int halfSize = q . size ( ) / 2 ;
  for ( int i = 0 ;
  i < halfSize ;
  i ++ ) {
    s . push ( q . peek ( ) ) ;
    q . poll ( ) ;
  }
  while ( ! s . empty ( ) ) {
    q . add ( s . peek ( ) ) ;
    s . pop ( ) ;
  }
  for ( int i = 0 ;
  i < halfSize ;
  i ++ ) {
    q . add ( q . peek ( ) ) ;
    q . poll ( ) ;
  }
  for ( int i = 0 ;
  i < halfSize ;
  i ++ ) {
    s . push ( q . peek ( ) ) ;
    q . poll ( ) ;
  }
  while ( ! s . empty ( ) ) {
    q . add ( s . peek ( ) ) ;
    s . pop ( ) ;
    q . add ( q . peek ( ) ) ;
    q . poll ( ) ;
  }
}
|||

INTEGER_POSITIVE_VALUE_POSITIVE_NEGATIVE_VALUE_ARRAY_1

static int findInteger ( int arr [ ] , int n ) {
  int neg = 0 , pos = 0 ;
  int sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    sum += arr [ i ] ;
    if ( arr [ i ] < 0 ) neg ++ ;
    else pos ++ ;
  }
  return ( sum / Math . abs ( neg - pos ) ) ;
}
|||

FIND_SUM_EVEN_INDEX_BINOMIAL_COEFFICIENTS

static int evenSum ( int n ) {
  int C [ ] [ ] = new int [ n + 1 ] [ n + 1 ] ;
  int i , j ;
  for ( i = 0 ;
  i <= n ;
  i ++ ) {
    for ( j = 0 ;
    j <= Math . min ( i , n ) ;
    j ++ ) {
      if ( j == 0 || j == i ) C [ i ] [ j ] = 1 ;
      else C [ i ] [ j ] = C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ] ;
    }
  }
  int sum = 0 ;
  for ( i = 0 ;
  i <= n ;
  i += 2 ) sum += C [ n ] [ i ] ;
  return sum ;
}
|||

DELANNOY_NUMBER

public static int dealnnoy ( int n , int m ) {
  if ( m == 0 || n == 0 ) return 1 ;
  return dealnnoy ( m - 1 , n ) + dealnnoy ( m - 1 , n - 1 ) + dealnnoy ( m , n - 1 ) ;
}
|||

FIND_THE_LARGEST_SUBARRAY_WITH_0_SUM

static int maxLen ( int arr [ ] , int n ) {
  int max_len = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int curr_sum = 0 ;
    for ( int j = i ;
    j < n ;
    j ++ ) {
      curr_sum += arr [ j ] ;
      if ( curr_sum == 0 ) max_len = Math . max ( max_len , j - i + 1 ) ;
    }
  }
  return max_len ;
}
|||

NEXT_POWER_OF_2

static int nextPowerOf2 ( int n ) {
  int count = 0 ;
  if ( n > 0 && ( n & ( n - 1 ) ) == 0 ) return n ;
  while ( n != 0 ) {
    n >>= 1 ;
    count += 1 ;
  }
  return 1 << count ;
}
|||

LONGEST_GEOMETRIC_PROGRESSION

static int lenOfLongestGP ( int set [ ] , int n ) {
  if ( n < 2 ) {
    return n ;
  }
  if ( n == 2 ) {
    return ( set [ 1 ] % set [ 0 ] == 0 ? 1 : 0 ) ;
  }
  Arrays . sort ( set ) ;
  int L [ ] [ ] = new int [ n ] [ n ] ;
  int llgp = 1 ;
  for ( int i = 0 ;
  i < n ;
  ++ i ) {
    if ( set [ n - 1 ] % set [ i ] == 0 ) {
      L [ i ] [ n - 1 ] = 2 ;
    }
    else {
      L [ i ] [ n - 1 ] = 1 ;
    }
  }
  for ( int j = n - 2 ;
  j >= 1 ;
  -- j ) {
    int i = j - 1 , k = j + 1 ;
    while ( i >= 0 && k <= n - 1 ) {
      if ( set [ i ] * set [ k ] < set [ j ] * set [ j ] ) {
        ++ k ;
      }
      else if ( set [ i ] * set [ k ] > set [ j ] * set [ j ] ) {
        if ( set [ j ] % set [ i ] == 0 ) {
          L [ i ] [ j ] = 2 ;
        }
        else {
          L [ i ] [ j ] = 1 ;
        }
        -- i ;
      }
      else {
        L [ i ] [ j ] = L [ j ] [ k ] + 1 ;
        if ( L [ i ] [ j ] > llgp ) {
          llgp = L [ i ] [ j ] ;
        }
        -- i ;
        ++ k ;
      }
    }
    while ( i >= 0 ) {
      if ( set [ j ] % set [ i ] == 0 ) {
        L [ i ] [ j ] = 2 ;
      }
      else {
        L [ i ] [ j ] = 1 ;
      }
      -- i ;
    }
  }
  return llgp ;
}
|||

DYNAMIC_PROGRAMMING_SET_6_MIN_COST_PATH

private static int minCost ( int cost [ ] [ ] , int m , int n ) {
  int i , j ;
  int tc [ ] [ ] = new int [ m + 1 ] [ n + 1 ] ;
  tc [ 0 ] [ 0 ] = cost [ 0 ] [ 0 ] ;
  for ( i = 1 ;
  i <= m ;
  i ++ ) tc [ i ] [ 0 ] = tc [ i - 1 ] [ 0 ] + cost [ i ] [ 0 ] ;
  for ( j = 1 ;
  j <= n ;
  j ++ ) tc [ 0 ] [ j ] = tc [ 0 ] [ j - 1 ] + cost [ 0 ] [ j ] ;
  for ( i = 1 ;
  i <= m ;
  i ++ ) for ( j = 1 ;
  j <= n ;
  j ++ ) tc [ i ] [ j ] = min ( tc [ i - 1 ] [ j - 1 ] , tc [ i - 1 ] [ j ] , tc [ i ] [ j - 1 ] ) + cost [ i ] [ j ] ;
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
  double a = Math . pow ( Math . sin ( dlat / 2 ) , 2 ) + Math . cos ( lat1 ) * Math . cos ( lat2 ) * Math . pow ( Math . sin ( dlon / 2 ) , 2 ) ;
  double c = 2 * Math . asin ( Math . sqrt ( a ) ) ;
  double r = 6371 ;
  return ( c * r ) ;
}
|||

BIN_PACKING_PROBLEM_MINIMIZE_NUMBER_OF_USED_BINS

static int nextFit ( int weight [ ] , int n , int c ) {
  int res = 0 , bin_rem = c ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( weight [ i ] > bin_rem ) {
      res ++ ;
      bin_rem = c - weight [ i ] ;
    }
    else bin_rem -= weight [ i ] ;
  }
  return res ;
}
|||

FIND_SUBARRAY_WITH_GIVEN_SUM_1

int subArraySum ( int arr [ ] , int n , int sum ) {
  int curr_sum = arr [ 0 ] , start = 0 , i ;
  for ( i = 1 ;
  i <= n ;
  i ++ ) {
    while ( curr_sum > sum && start < i - 1 ) {
      curr_sum = curr_sum - arr [ start ] ;
      start ++ ;
    }
    if ( curr_sum == sum ) {
      int p = i - 1 ;
      System . out . println ( "Sum found between indexes " + start + " and " + p ) ;
      return 1 ;
    }
    if ( i < n ) curr_sum = curr_sum + arr [ i ] ;
  }
  System . out . println ( "No subarray found" ) ;
  return 0 ;
}
|||

SPACE_OPTIMIZED_DP_SOLUTION_0_1_KNAPSACK_PROBLEM_1

static int KnapSack ( int val [ ] , int wt [ ] , int n , int W ) {
  int [ ] dp = new int [ W + 1 ] ;
  Arrays . fill ( dp , 0 ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) for ( int j = W ;
  j >= wt [ i ] ;
  j -- ) dp [ j ] = Math . max ( dp [ j ] , val [ i ] + dp [ j - wt [ i ] ] ) ;
  return dp [ W ] ;
}
|||

FIND_VALUE_OF_Y_MOD_2_RAISED_TO_POWER_X

static long yMod ( long y , long x ) {
  if ( ( Math . log ( y ) / Math . log ( 2 ) ) < x ) return y ;
  if ( x > 63 ) return y ;
  return ( y % ( 1 << ( int ) x ) ) ;
}
|||

SUM_SERIES_23_45_67_89_UPTO_N_TERMS

static double seriesSum ( int n ) {
  int i = 1 ;
  double res = 0.0 ;
  boolean sign = true ;
  while ( n > 0 ) {
    n -- ;
    if ( sign ) {
      sign = ! sign ;
      res = res + ( double ) ++ i / ++ i ;
    }
    else {
      sign = ! sign ;
      res = res - ( double ) ++ i / ++ i ;
    }
  }
  return res ;
}
|||

LENGTH_LONGEST_STRICT_BITONIC_SUBSEQUENCE

static int longLenStrictBitonicSub ( int arr [ ] , int n ) {
  HashMap < Integer , Integer > inc = new HashMap < Integer , Integer > ( ) ;
  HashMap < Integer , Integer > dcr = new HashMap < Integer , Integer > ( ) ;
  int len_inc [ ] = new int [ n ] ;
  int len_dcr [ ] = new int [ n ] ;
  int longLen = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    int len = 0 ;
    if ( inc . containsKey ( arr [ i ] - 1 ) ) len = inc . get ( arr [ i ] - 1 ) ;
    len_inc [ i ] = len + 1 ;
    inc . put ( arr [ i ] , len_inc [ i ] ) ;
  }
  for ( int i = n - 1 ;
  i >= 0 ;
  i -- ) {
    int len = 0 ;
    if ( dcr . containsKey ( arr [ i ] - 1 ) ) len = dcr . get ( arr [ i ] - 1 ) ;
    len_dcr [ i ] = len + 1 ;
    dcr . put ( arr [ i ] , len_dcr [ i ] ) ;
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( longLen < ( len_inc [ i ] + len_dcr [ i ] - 1 ) ) longLen = len_inc [ i ] + len_dcr [ i ] - 1 ;
  return longLen ;
}
|||

MAXIMUM_DISTANCE_TWO_OCCURRENCES_ELEMENT_ARRAY

static int maxDistance ( int [ ] arr , int n ) {
  HashMap < Integer , Integer > map = new HashMap < > ( ) ;
  int max_dist = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ! map . containsKey ( arr [ i ] ) ) map . put ( arr [ i ] , i ) ;
    else max_dist = Math . max ( max_dist , i - map . get ( arr [ i ] ) ) ;
  }
  return max_dist ;
}
|||

FIND_RECTANGLE_BINARY_MATRIX_CORNERS_1_1

static boolean isRectangle ( int matrix [ ] [ ] ) {
  int rows = matrix . length ;
  if ( rows == 0 ) return false ;
  int columns = matrix [ 0 ] . length ;
  HashMap < Integer , HashSet < Integer >> table = new HashMap < > ( ) ;
  for ( int i = 0 ;
  i < rows ;
  i ++ ) {
    for ( int j = 0 ;
    j < columns - 1 ;
    j ++ ) {
      for ( int k = j + 1 ;
      k < columns ;
      k ++ ) {
        if ( matrix [ i ] [ j ] == 1 && matrix [ i ] [ k ] == 1 ) {
          if ( table . containsKey ( j ) && table . get ( j ) . contains ( k ) ) {
            return true ;
          }
          if ( table . containsKey ( k ) && table . get ( k ) . contains ( j ) ) {
            return true ;
          }
          if ( ! table . containsKey ( j ) ) {
            HashSet < Integer > x = new HashSet < > ( ) ;
            x . add ( k ) ;
            table . put ( j , x ) ;
          }
          else {
            table . get ( j ) . add ( k ) ;
          }
          if ( ! table . containsKey ( k ) ) {
            HashSet < Integer > x = new HashSet < > ( ) ;
            x . add ( j ) ;
            table . put ( k , x ) ;
          }
          else {
            table . get ( k ) . add ( j ) ;
          }
        }
      }
    }
  }
  return false ;
}
|||

COUNT_MINIMUM_NUMBER_SUBSETS_SUBSEQUENCES_CONSECUTIVE_NUMBERS

static int numofsubset ( int arr [ ] , int n ) {
  Arrays . sort ( arr ) ;
  int count = 1 ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    if ( arr [ i ] + 1 != arr [ i + 1 ] ) count ++ ;
  }
  return count ;
}
|||

LARGEST_SUM_CONTIGUOUS_SUBARRAY

static int maxSubArraySum ( int a [ ] ) {
  int size = a . length ;
  int max_so_far = Integer . MIN_VALUE , max_ending_here = 0 ;
  for ( int i = 0 ;
  i < size ;
  i ++ ) {
    max_ending_here = max_ending_here + a [ i ] ;
    if ( max_so_far < max_ending_here ) max_so_far = max_ending_here ;
    if ( max_ending_here < 0 ) max_ending_here = 0 ;
  }
  return max_so_far ;
}
|||

PROGRAM_TO_FIND_REMAINDER_WITHOUT_USING_MODULO_OR_OPERATOR_2

static int getRemainder ( int num , int divisor ) {
  while ( num >= divisor ) num -= divisor ;
  return num ;
}
|||

CHECK_LARGE_NUMBER_DIVISIBLE_4_NOT

static boolean check ( String str ) {
  int n = str . length ( ) ;
  if ( n == 0 ) return false ;
  if ( n == 1 ) return ( ( str . charAt ( 0 ) - '0' ) % 4 == 0 ) ;
  int last = str . charAt ( n - 1 ) - '0' ;
  int second_last = str . charAt ( n - 2 ) - '0' ;
  return ( ( second_last * 10 + last ) % 4 == 0 ) ;
}
|||

FIND_THE_ELEMENT_THAT_APPEARS_ONCE_1

static int getSingle ( int arr [ ] , int n ) {
  int result = 0 ;
  int x , sum ;
  for ( int i = 0 ;
  i < INT_SIZE ;
  i ++ ) {
    sum = 0 ;
    x = ( 1 << i ) ;
    for ( int j = 0 ;
    j < n ;
    j ++ ) {
      if ( ( arr [ j ] & x ) == 0 ) sum ++ ;
    }
    if ( ( sum % 3 ) == 0 ) result |= x ;
  }
  return result ;
}
|||

NUMBER_RECTANGLES_NM_GRID

public static long rectCount ( int n , int m ) {
  return ( m * n * ( n + 1 ) * ( m + 1 ) ) / 4 ;
}
|||

MAXIMUM_POINTS_INTERSECTION_N_CIRCLES

static int intersection ( int n ) {
  return n * ( n - 1 ) ;
}
|||

