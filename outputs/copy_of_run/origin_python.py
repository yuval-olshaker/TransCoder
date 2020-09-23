MAXIMUM_NUMBER_CHARACTERS_TWO_CHARACTER_STRING

def maximumChars ( str ) :
    n = len ( str )
    res = - 1
    for i in range ( 0 , n - 1 ) :
        for j in range ( i + 1 , n ) :
            if ( str [ i ] == str [ j ] ) :
                res = max ( res , abs ( j - i - 1 ) )
    return res
|||

FIND_MIRROR_IMAGE_POINT_2_D_PLANE

def mirrorImage ( a , b , c , x1 , y1 ) :
    temp = - 2 * ( a * x1 + b * y1 + c ) / ( a * a + b * b )
    x = temp * a + x1
    y = temp * b + y1
    return ( x , y )
|||

EFFICIENTLY_COMPUTE_SUMS_OF_DIAGONALS_OF_A_MATRIX

def printDiagonalSums ( mat , n ) :
    principal = 0
    secondary = 0 
    for i in range ( 0 , n ) :
        for j in range ( 0 , n ) :
            if ( i == j ) :
                principal += mat [ i ] [ j ]
            if ( ( i + j ) == ( n - 1 ) ) :
                secondary += mat [ i ] [ j ]
    print ( "Principal Diagonal:" , principal )
    print ( "Secondary Diagonal:" , secondary )
|||

COUNTS_PATHS_POINT_REACH_ORIGIN

def countPaths ( n , m ) :
    if ( n == 0 or m == 0 ) :
        return 1
    return ( countPaths ( n - 1 , m ) + countPaths ( n , m - 1 ) )
|||

FIND_A_TRIPLET_THAT_SUM_TO_A_GIVEN_VALUE_1

def find3Numbers ( A , arr_size , sum ) :
    A.sort ( )
    for i in range ( 0 , arr_size - 2 ) :
        l = i + 1
        r = arr_size - 1
        while ( l < r ) :
            if ( A [ i ] + A [ l ] + A [ r ] == sum ) :
                print ( "Triplet is" , A [ i ] , ', ' , A [ l ] , ', ' , A [ r ] ) 
                return True
            elif ( A [ i ] + A [ l ] + A [ r ] < sum ) :
                l += 1
            else :
                r -= 1
    return False
|||

CHECK_GIVEN_MATRIX_IS_MAGIC_SQUARE_OR_NOT

def isMagicSquare ( mat ) :
    s = 0
    for i in range ( 0 , N ) :
        s = s + mat [ i ] [ i ]
    s2 = 0
    for i in range ( 0 , N ) :
        s2 = s2 + mat [ i ] [ N - i - 1 ]
    if ( s != s2 ) :
        return False
    for i in range ( 0 , N ) :
        rowSum = 0 
        for j in range ( 0 , N ) :
            rowSum += mat [ i ] [ j ]
        if ( rowSum != s ) :
            return False
    for i in range ( 0 , N ) :
        colSum = 0
        for j in range ( 0 , N ) :
            colSum += mat [ j ] [ i ]
        if ( s != colSum ) :
            return False
    return True
|||

SEQUENCES_GIVEN_LENGTH_EVERY_ELEMENT_EQUAL_TWICE_PREVIOUS_1

def getTotalNumberOfSequences ( m , n ) :
    T = [ [ 0 for i in range ( n + 1 ) ] for i in range ( m + 1 ) ]
    for i in range ( m + 1 ) :
        for j in range ( n + 1 ) :
            if i == 0 or j == 0 :
                T [ i ] [ j ] = 0
            elif i < j :
                T [ i ] [ j ] = 0
            elif j == 1 :
                T [ i ] [ j ] = i
            else :
                T [ i ] [ j ] = T [ i - 1 ] [ j ] + T [ i // 2 ] [ j - 1 ]
    return T [ m ] [ n ]
|||

FIND_DIFFERENCE_BETWEEN_SUMS_OF_TWO_DIAGONALS_1

def difference ( arr , n ) :
    d1 = 0
    d2 = 0
    for i in range ( 0 , n ) :
        d1 = d1 + arr [ i ] [ i ]
        d2 = d2 + arr [ i ] [ n - i - 1 ]
    return abs ( d1 - d2 )
|||

MINIMUM_NUMBER_SUBSETS_DISTINCT_ELEMENTS

def subset ( ar , n ) :
    res = 0
    ar.sort ( )
    for i in range ( 0 , n ) :
        count = 1
        for i in range ( n - 1 ) :
            if ar [ i ] == ar [ i + 1 ] :
                count += 1
            else :
                break
        res = max ( res , count )
    return res
|||

DECIMAL_BINARY_CONVERSION_WITHOUT_USING_ARITHMETIC_OPERATORS

def decToBin ( n ) :
    if ( n == 0 ) :
        return "0" 
    bin = "" 
    while ( n > 0 ) :
        if ( n & 1 == 0 ) :
            bin = '0' + bin 
        else :
            bin = '1' + bin 
        n = n >> 1 
    return bin 
|||

FIND_NTH_TERM_DRAGON_CURVE_SEQUENCE

def Dragon_Curve_Sequence ( n ) :
    s = "1"
    for i in range ( 2 , n + 1 ) :
        temp = "1"
        prev = '1'
        zero = '0'
        one = '1'
        for j in range ( len ( s ) ) :
            temp += s [ j ]
            if ( prev == '0' ) :
                temp += one
                prev = one
            else :
                temp += zero
                prev = zero
        s = temp
    return s
|||

STACK_SET_3_REVERSE_STRING_USING_STACK

def reverse ( string ) :
    string = string [ : : - 1 ]
    return string
|||

SORT_EVEN_PLACED_ELEMENTS_INCREASING_ODD_PLACED_DECREASING_ORDER_1

def bitonicGenerator ( arr , n ) :
    i = 1
    j = n - 1
    if ( j % 2 != 0 ) :
        j = j - 1
    while ( i < j ) :
        arr [ j ] , arr [ i ] = arr [ i ] , arr [ j ]
        i = i + 2
        j = j - 2
    arr_f = [ ]
    arr_s = [ ]
    for i in range ( int ( ( n + 1 ) / 2 ) ) :
        arr_f.append ( arr [ i ] )
    i = int ( ( n + 1 ) / 2 )
    while ( i < n ) :
        arr_s.append ( arr [ i ] )
        i = i + 1
    arr_f.sort ( )
    arr_s.sort ( reverse = True )
    for i in arr_s :
        arr_f.append ( i )
    return arr_f
|||

GIVEN_TWO_NUMBERS_B_FIND_X_X_B

def modularEquation ( a , b ) :
    if ( a < b ) :
        print ( "No solution possible " )
        return
    if ( a == b ) :
        print ( "Infinite Solution possible " )
        return
    count = 0
    n = a - b
    y = ( int ) ( math.sqrt ( a - b ) )
    for i in range ( 1 , y + 1 ) :
        if ( n % i == 0 ) :
            if ( n / i > b ) :
                count = count + 1
            if ( i > b ) :
                count = count + 1
    if ( y * y == n and y > b ) :
        count = count - 1
    print ( count )
|||

CHECK_CHARACTERS_GIVEN_STRING_CAN_REARRANGED_FORM_PALINDROME

def canFormPalindrome ( st ) :
    count = [ 0 ] * ( NO_OF_CHARS )
    for i in range ( 0 , len ( st ) ) :
        count [ ord ( st [ i ] ) ] = count [ ord ( st [ i ] ) ] + 1
    odd = 0
    for i in range ( 0 , NO_OF_CHARS ) :
        if ( count [ i ] & 1 ) :
            odd = odd + 1
        if ( odd > 1 ) :
            return False
    return True
|||

MAXIMUM_TRIPLET_SUM_ARRAY_1

def maxTripletSum ( arr , n ) :
    arr.sort ( )
    return ( arr [ n - 1 ] + arr [ n - 2 ] + arr [ n - 3 ] )
|||

FIND_MEDIAN_ROW_WISE_SORTED_MATRIX

def binaryMedian ( m , r , d ) :
    mi = m [ 0 ] [ 0 ]
    mx = 0
    for i in range ( r ) :
        if m [ i ] [ 0 ] < mi :
            mi = m [ i ] [ 0 ]
        if m [ i ] [ d - 1 ] > mx :
            mx = m [ i ] [ d - 1 ]
    desired = ( r * d + 1 ) // 2
    while ( mi < mx ) :
        mid = mi + ( mx - mi ) // 2
        place = [ 0 ] 
        for i in range ( r ) :
            j = upper_bound ( m [ i ] , mid )
            place [ 0 ] = place [ 0 ] + j
        if place [ 0 ] < desired :
            mi = mid + 1
        else :
            mx = mid
    print ( "Median is" , mi )
    return
|||

HEIGHT_N_ARY_TREE_PARENT_ARRAY_GIVEN

def findHeight ( parent , n ) :
    res = 0
    for i in range ( n ) :
        p = i
        current = 1
        while ( parent [ p ] != - 1 ) :
            current += 1
            p = parent [ p ]
        res = max ( res , current )
    return res
|||

CHECK_LARGE_NUMBER_DIVISIBLE_20

def divisibleBy20 ( num ) :
    lastTwoDigits = int ( num [ - 2 : ] )
    return ( ( lastTwoDigits % 5 == 0 and lastTwoDigits % 4 == 0 ) )
|||

MAXIMUM_VALUE_CHOICE_EITHER_DIVIDING_CONSIDERING

def maxDP ( n ) :
    res = list ( )
    res.append ( 0 )
    res.append ( 1 )
    i = 2
    while i < n + 1 :
        res.append ( max ( i , ( res [ int ( i / 2 ) ] + res [ int ( i / 3 ) ] + res [ int ( i / 4 ) ] + res [ int ( i / 5 ) ] ) ) )
        i = i + 1
    return res [ n ]
|||

QUERIES_ON_ARRAY_WITH_DISAPPEARING_AND_REAPPEARING_ELEMENTS

def PerformQueries ( a , vec ) :
    ans = [ ] 
    n = len ( a ) - 1 
    q = len ( vec ) 
    for i in range ( q ) :
        t = vec [ i ] [ 0 ] 
        m = vec [ i ] [ 1 ] 
        if ( m > n ) :
            ans.append ( - 1 ) 
            continue 
        turn = t // n 
        rem = t % n 
        if ( rem == 0 and turn % 2 == 1 ) :
            ans.append ( - 1 ) 
            continue 
        if ( rem == 0 and turn % 2 == 0 ) :
            ans.append ( a [ m ] ) 
            continue 
        if ( turn % 2 == 0 ) :
            cursize = n - rem 
            if ( cursize < m ) :
                ans.append ( - 1 ) 
                continue 
            ans.append ( a [ m + rem ] ) 
        else :
            cursize = rem 
            if ( cursize < m ) :
                ans.append ( - 1 ) 
                continue 
            ans.append ( a [ m ] ) 
    for i in ans :
        print ( i ) 
|||

FIND_THE_MINIMUM_DISTANCE_BETWEEN_TWO_NUMBERS_1

def minDist ( arr , n , x , y ) :
    min_dist = sys.maxsize
    for i in range ( n ) :
        if arr [ i ] == x or arr [ i ] == y :
            prev = i
            break
    while i < n :
        if arr [ i ] == x or arr [ i ] == y :
            if arr [ prev ] != arr [ i ] and ( i - prev ) < min_dist :
                min_dist = i - prev
                prev = i
            else :
                prev = i
        i += 1
    return min_dist
|||

UNION_AND_INTERSECTION_OF_TWO_SORTED_ARRAYS_2

def printUnion ( arr1 , arr2 , m , n ) :
    i , j = 0 , 0
    while i < m and j < n :
        if arr1 [ i ] < arr2 [ j ] :
            print ( arr1 [ i ] )
            i += 1
        elif arr2 [ j ] < arr1 [ i ] :
            print ( arr2 [ j ] )
            j += 1
        else :
            print ( arr2 [ j ] )
            j += 1
            i += 1
    while i < m :
        print ( arr1 [ i ] )
        i += 1
    while j < n :
        print ( arr2 [ j ] )
        j += 1
|||

WORD_WRAP_PROBLEM_SPACE_OPTIMIZED_SOLUTION

def solveWordWrap ( arr , n , k ) :
    dp = [ 0 ] * n
    ans = [ 0 ] * n
    dp [ n - 1 ] = 0
    ans [ n - 1 ] = n - 1
    for i in range ( n - 2 , - 1 , - 1 ) :
        currlen = - 1
        dp [ i ] = sys.maxsize
        for j in range ( i , n ) :
            currlen += ( arr [ j ] + 1 )
            if ( currlen > k ) :
                break
            if ( j == n - 1 ) :
                cost = 0
            else :
                cost = ( ( k - currlen ) * ( k - currlen ) + dp [ j + 1 ] )
            if ( cost < dp [ i ] ) :
                dp [ i ] = cost
                ans [ i ] = j
    i = 0
    while ( i < n ) :
        print ( i + 1 , ans [ i ] + 1 , end = " " )
        i = ans [ i ] + 1
|||

COUNT_DISTINCT_SUBSEQUENCES

def countSub ( ss ) :
    last = [ - 1 for i in range ( MAX_CHAR + 1 ) ]
    n = len ( ss )
    dp = [ - 2 for i in range ( n + 1 ) ]
    dp [ 0 ] = 1
    for i in range ( 1 , n + 1 ) :
        dp [ i ] = 2 * dp [ i - 1 ]
        if last [ ord ( ss [ i - 1 ] ) ] != - 1 :
            dp [ i ] = dp [ i ] - dp [ last [ ord ( ss [ i - 1 ] ) ] ]
        last [ ord ( ss [ i - 1 ] ) ] = i - 1
    return dp [ n ]
|||

LONGEST_EVEN_LENGTH_SUBSTRING_SUM_FIRST_SECOND_HALF_3

def findLength ( st , n ) :
    total = [ 0 ] * ( n + 1 )
    for i in range ( 1 , n + 1 ) :
        total [ i ] = ( total [ i - 1 ] + int ( st [ i - 1 ] ) - int ( '0' ) )
    ans = 0
    l = 2
    while ( l <= n ) :
        for i in range ( n - l + 1 ) :
            j = i + l - 1
            if ( total [ i + int ( l / 2 ) ] - total [ i ] == total [ i + l ] - total [ i + int ( l / 2 ) ] ) :
                ans = max ( ans , l )
        l = l + 2
    return ans
|||

MAXIMUM_PATH_SUM_MATRIX

def findMaxPath ( mat ) :
    res = - 1
    for i in range ( M ) :
        res = max ( res , mat [ 0 ] [ i ] )
    for i in range ( 1 , N ) :
        res = - 1
        for j in range ( M ) :
            if ( j > 0 and j < M - 1 ) :
                mat [ i ] [ j ] += max ( mat [ i - 1 ] [ j ] , max ( mat [ i - 1 ] [ j - 1 ] , mat [ i - 1 ] [ j + 1 ] ) )
            elif ( j > 0 ) :
                mat [ i ] [ j ] += max ( mat [ i - 1 ] [ j ] , mat [ i - 1 ] [ j - 1 ] )
            elif ( j < M - 1 ) :
                mat [ i ] [ j ] += max ( mat [ i - 1 ] [ j ] , mat [ i - 1 ] [ j + 1 ] )
            res = max ( mat [ i ] [ j ] , res )
    return res
|||

MAXIMUM_CONSECUTIVE_REPEATING_CHARACTER_STRING

def maxRepeating ( str ) :
    l = len ( str )
    count = 0
    res = str [ 0 ]
    for i in range ( l ) :
        cur_count = 1
        for j in range ( i + 1 , l ) :
            if ( str [ i ] != str [ j ] ) :
                break
            cur_count += 1
        if cur_count > count :
            count = cur_count
            res = str [ i ]
    return res
|||

MAXIMUM_LENGTH_SUBSEQUENCE_DIFFERENCE_ADJACENT_ELEMENTS_EITHER_0_1

def maxLenSub ( arr , n ) :
    mls = [ ]
    max = 0
    for i in range ( n ) :
        mls.append ( 1 )
    for i in range ( n ) :
        for j in range ( i ) :
            if ( abs ( arr [ i ] - arr [ j ] ) <= 1 and mls [ i ] < mls [ j ] + 1 ) :
                mls [ i ] = mls [ j ] + 1
    for i in range ( n ) :
        if ( max < mls [ i ] ) :
            max = mls [ i ]
    return max
|||

BREAKING_NUMBER_FIRST_PART_INTEGRAL_DIVISION_SECOND_POWER_10

def calculate ( N ) :
    length = len ( N )
    l = int ( ( length ) / 2 )
    count = 0
    for i in range ( l + 1 ) :
        s = N [ 0 : 0 + i ]
        l1 = len ( s )
        t = N [ i : l1 + i ]
        try :
            if s [ 0 ] == '0' or t [ 0 ] == '0' :
                continue
        except :
            continue
        if s == t :
            count += 1
    return count
|||

PROGRAM_BINARY_DECIMAL_CONVERSION

def binaryToDecimal ( n ) :
    num = n 
    dec_value = 0 
    base = 1 
    temp = num 
    while ( temp ) :
        last_digit = temp % 10 
        temp = int ( temp / 10 ) 
        dec_value += last_digit * base 
        base = base * 2 
    return dec_value 
|||

HOW_CAN_WE_SUM_THE_DIGITS_OF_A_GIVEN_NUMBER_IN_SINGLE_STATEMENT

def getSum ( n ) :
    sum = 0
    while ( n != 0 ) :
        sum = sum + int ( n % 10 )
        n = int ( n / 10 )
    return sum
|||

FIND_N_TH_ELEMENT_FROM_STERNS_DIATOMIC_SERIES

def findSDSFunc ( n ) :
    DP = [ 0 ] * ( n + 1 )
    DP [ 0 ] = 0
    DP [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        if ( int ( i % 2 ) == 0 ) :
            DP [ i ] = DP [ int ( i / 2 ) ]
        else :
            DP [ i ] = ( DP [ int ( ( i - 1 ) / 2 ) ] + DP [ int ( ( i + 1 ) / 2 ) ] )
    return DP [ n ]
|||

NUMBER_SINK_NODES_GRAPH

def countSink ( n , m , edgeFrom , edgeTo ) :
    mark = [ 0 ] * ( n + 1 )
    for i in range ( m ) :
        mark [ edgeFrom [ i ] ] = 1
    count = 0
    for i in range ( 1 , n + 1 ) :
        if ( not mark [ i ] ) :
            count += 1
    return count
|||

BREAK_NUMBER_THREE_PARTS

def count_of_ways ( n ) :
    count = 0
    for i in range ( 0 , n + 1 ) :
        for j in range ( 0 , n + 1 ) :
            for k in range ( 0 , n + 1 ) :
                if ( i + j + k == n ) :
                    count = count + 1
    return count
|||

PRINT_DISTINCT_ELEMENTS_GIVEN_INTEGER_ARRAY

def printDistinct ( arr , n ) :
    for i in range ( 0 , n ) :
        d = 0
        for j in range ( 0 , i ) :
            if ( arr [ i ] == arr [ j ] ) :
                d = 1
                break
        if ( d == 0 ) :
            print ( arr [ i ] )
|||

MAXIMUM_NUMBER_SEGMENTS_LENGTHS_B_C

def maximumSegments ( n , a , b , c ) :
    dp = [ - 1 ] * ( n + 10 )
    dp [ 0 ] = 0
    for i in range ( 0 , n ) :
        if ( dp [ i ] != - 1 ) :
            if ( i + a <= n ) :
                dp [ i + a ] = max ( dp [ i ] + 1 , dp [ i + a ] )
            if ( i + b <= n ) :
                dp [ i + b ] = max ( dp [ i ] + 1 , dp [ i + b ] )
            if ( i + c <= n ) :
                dp [ i + c ] = max ( dp [ i ] + 1 , dp [ i + c ] )
    return dp [ n ]
|||

CHECK_VALID_SEQUENCE_DIVISIBLE_M

def isPossible ( n , index , Sum , M , arr , dp ) :
    global MAX
    if index == n :
        if ( Sum % M ) == 0 :
            return True
        return False
    if dp [ index ] [ Sum ] != - 1 :
        return dp [ index ] [ Sum ]
    placeAdd = isPossible ( n , index + 1 , Sum + arr [ index ] , M , arr , dp )
    placeMinus = isPossible ( n , index + 1 , Sum - arr [ index ] , M , arr , dp )
    res = placeAdd or placeMinus
    dp [ index ] [ Sum ] = res
    return res
|||

FIND_PAIR_WITH_GREATEST_PRODUCT_IN_ARRAY

def findGreatest ( arr , n ) :
    result = - 1
    for i in range ( n ) :
        for j in range ( n - 1 ) :
            for k in range ( j + 1 , n ) :
                if ( arr [ j ] * arr [ k ] == arr [ i ] ) :
                    result = max ( result , arr [ i ] )
    return result
|||

MAXIMUM_SUBARRAY_SUM_ARRAY_CREATED_REPEATED_CONCATENATION

def maxSubArraySumRepeated ( a , n , k ) :
    max_so_far = - 2147483648
    max_ending_here = 0
    for i in range ( n * k ) :
        max_ending_here = max_ending_here + a [ i % n ]
        if ( max_so_far < max_ending_here ) :
            max_so_far = max_ending_here
        if ( max_ending_here < 0 ) :
            max_ending_here = 0
    return max_so_far
|||

LEONARDO_NUMBER_1

def leonardo ( n ) :
    dp = [ ] 
    dp.append ( 1 ) 
    dp.append ( 1 ) 
    for i in range ( 2 , n + 1 ) :
        dp.append ( dp [ i - 1 ] + dp [ i - 2 ] + 1 ) 
    return dp [ n ] 
|||

SUM_OF_ALL_SUBSTRINGS_OF_A_STRING_REPRESENTING_A_NUMBER

def sumOfSubstrings ( num ) :
    n = len ( num )
    sumofdigit = [ ]
    sumofdigit.append ( int ( num [ 0 ] ) )
    res = sumofdigit [ 0 ]
    for i in range ( 1 , n ) :
        numi = int ( num [ i ] )
        sumofdigit.append ( ( i + 1 ) * numi + 10 * sumofdigit [ i - 1 ] )
        res += sumofdigit [ i ]
    return res
|||

PRUFER_CODE_TREE_CREATION

def printTreeEdges ( prufer , m ) :
    vertices = m + 2
    vertex_set = [ 0 ] * vertices
    for i in range ( vertices - 2 ) :
        vertex_set [ prufer [ i ] - 1 ] += 1
    print ( "The edge set E(G) is :" )
    j = 0
    for i in range ( vertices - 2 ) :
        for j in range ( vertices ) :
            if ( vertex_set [ j ] == 0 ) :
                vertex_set [ j ] = - 1
                print ( "(" , ( j + 1 ) , ", " , prufer [ i ] , ") " , sep = "" , end = "" )
                vertex_set [ prufer [ i ] - 1 ] -= 1
                break
    j = 0
    for i in range ( vertices ) :
        if ( vertex_set [ i ] == 0 and j == 0 ) :
            print ( "(" , ( i + 1 ) , ", " , sep = "" , end = "" )
            j += 1
        elif ( vertex_set [ i ] == 0 and j == 1 ) :
            print ( ( i + 1 ) , ")" )
|||

PROGRAM_FIND_SMALLEST_DIFFERENCE_ANGLES_TWO_PARTS_GIVEN_CIRCLE

def findMinimumAngle ( arr , n ) :
    l = 0
    _sum = 0
    ans = 360
    for i in range ( n ) :
        _sum += arr [ i ]
        while _sum >= 180 :
            ans = min ( ans , 2 * abs ( 180 - _sum ) )
            _sum -= arr [ l ]
            l += 1
        ans = min ( ans , 2 * abs ( 180 - _sum ) )
    return ans
|||

FIND_MAXIMUM_AVERAGE_SUBARRAY_OF_K_LENGTH

def findMaxAverage ( arr , n , k ) :
    if k > n :
        return - 1
    csum = [ 0 ] * n
    csum [ 0 ] = arr [ 0 ]
    for i in range ( 1 , n ) :
        csum [ i ] = csum [ i - 1 ] + arr [ i ] 
    max_sum = csum [ k - 1 ]
    max_end = k - 1
    for i in range ( k , n ) :
        curr_sum = csum [ i ] - csum [ i - k ]
        if curr_sum > max_sum :
            max_sum = curr_sum
            max_end = i
    return max_end - k + 1
|||

SQUARE_PYRAMIDAL_NUMBER_SUM_SQUARES

def findS ( s ) :
    _sum = 0
    n = 1
    while ( _sum < s ) :
        _sum += n * n
        n += 1
    n -= 1
    if _sum == s :
        return n
    return - 1
|||

PROGRAM_TO_CALCULATE_AREA_OF_AN_CIRCLE_INSCRIBED_IN_A_SQUARE

def areaOfInscribedCircle ( a ) :
    return ( PI / 4 ) * a * a
|||

MINIMUM_NUMBER_CHARACTERS_REMOVED_MAKE_BINARY_STRING_ALTERNATE

def countToMake0lternate ( s ) :
    result = 0
    for i in range ( len ( s ) - 1 ) :
        if ( s [ i ] == s [ i + 1 ] ) :
            result += 1
    return result
|||

FIND_ELEMENTS_PRESENT_FIRST_ARRAY_NOT_SECOND

def findMissing ( a , b , n , m ) :
    for i in range ( n ) :
        for j in range ( m ) :
            if ( a [ i ] == b [ j ] ) :
                break
        if ( j == m - 1 ) :
            print ( a [ i ] , end = " " )
|||

REARRANGE_ARRAY_MAXIMUM_MINIMUM_FORM

def rearrange ( arr , n ) :
    temp = n * [ None ]
    small , large = 0 , n - 1
    flag = True
    for i in range ( n ) :
        if flag is True :
            temp [ i ] = arr [ large ]
            large -= 1
        else :
            temp [ i ] = arr [ small ]
            small += 1
        flag = bool ( 1 - flag )
    for i in range ( n ) :
        arr [ i ] = temp [ i ]
    return arr
|||

DYNAMIC_PROGRAMMING_SET_15_LONGEST_BITONIC_SUBSEQUENCE

def lbs ( arr ) :
    n = len ( arr )
    lis = [ 1 for i in range ( n + 1 ) ]
    for i in range ( 1 , n ) :
        for j in range ( 0 , i ) :
            if ( ( arr [ i ] > arr [ j ] ) and ( lis [ i ] < lis [ j ] + 1 ) ) :
                lis [ i ] = lis [ j ] + 1
    lds = [ 1 for i in range ( n + 1 ) ]
    for i in reversed ( range ( n - 1 ) ) :
        for j in reversed ( range ( i - 1 , n ) ) :
            if ( arr [ i ] > arr [ j ] and lds [ i ] < lds [ j ] + 1 ) :
                lds [ i ] = lds [ j ] + 1
    maximum = lis [ 0 ] + lds [ 0 ] - 1
    for i in range ( 1 , n ) :
        maximum = max ( ( lis [ i ] + lds [ i ] - 1 ) , maximum )
    return maximum
|||

COUNT_PAIRS_WHOSE_PRODUCTS_EXIST_IN_ARRAY

def countPairs ( arr , n ) :
    result = 0 
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            product = arr [ i ] * arr [ j ] 
            for k in range ( 0 , n ) :
                if ( arr [ k ] == product ) :
                    result = result + 1 
                    break 
    return result 
|||

COUNT_SINGLE_NODE_ISOLATED_SUB_GRAPHS_DISCONNECTED_GRAPH

def compute ( graph , N ) :
    count = 0
    for i in range ( 1 , N + 1 ) :
        if ( len ( graph [ i ] ) == 0 ) :
            count += 1
    return count
|||

HARDY_RAMANUJAN_THEOREM

def exactPrimeFactorCount ( n ) :
    count = 0
    if ( n % 2 == 0 ) :
        count = count + 1
        while ( n % 2 == 0 ) :
            n = int ( n / 2 )
    i = 3
    while ( i <= int ( math.sqrt ( n ) ) ) :
        if ( n % i == 0 ) :
            count = count + 1
            while ( n % i == 0 ) :
                n = int ( n / i )
        i = i + 2
    if ( n > 2 ) :
        count = count + 1
    return count
|||

SHORTEST_COMMON_SUPERSEQUENCE_1

def superSeq ( X , Y , m , n ) :
    dp = [ [ 0 ] * ( n + 2 ) for i in range ( m + 2 ) ]
    for i in range ( m + 1 ) :
        for j in range ( n + 1 ) :
            if ( not i ) : dp [ i ] [ j ] = j
            elif ( not j ) : dp [ i ] [ j ] = i
            elif ( X [ i - 1 ] == Y [ j - 1 ] ) :
                dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ]
            else : dp [ i ] [ j ] = 1 + min ( dp [ i - 1 ] [ j ] , dp [ i ] [ j - 1 ] )
    return dp [ m ] [ n ]
|||

POWER_SET

def printPowerSet ( set , set_size ) :
    pow_set_size = ( int ) ( math.pow ( 2 , set_size ) ) 
    counter = 0 
    j = 0 
    for counter in range ( 0 , pow_set_size ) :
        for j in range ( 0 , set_size ) :
            if ( ( counter & ( 1 << j ) ) > 0 ) :
                print ( set [ j ] , end = "" ) 
        print ( "" ) 
|||

CHECK_ARRAY_MAJORITY_ELEMENT

def isMajority ( a ) :
    mp = { }
    for i in a :
        if i in mp : mp [ i ] += 1
        else : mp [ i ] = 1
    for x in mp :
        if mp [ x ] >= len ( a ) // 2 :
            return True
    return False
|||

PRINT_GIVEN_MATRIX_COUNTER_CLOCK_WISE_SPIRAL_FORM

def counterClockspiralPrint ( m , n , arr ) :
    k = 0 ; l = 0
    cnt = 0
    total = m * n
    while ( k < m and l < n ) :
        if ( cnt == total ) :
            break
        for i in range ( k , m ) :
            print ( arr [ i ] [ l ] , end = " " )
            cnt += 1
        l += 1
        if ( cnt == total ) :
            break
        for i in range ( l , n ) :
            print ( arr [ m - 1 ] [ i ] , end = " " )
            cnt += 1
        m -= 1
        if ( cnt == total ) :
            break
        if ( k < m ) :
            for i in range ( m - 1 , k - 1 , - 1 ) :
                print ( arr [ i ] [ n - 1 ] , end = " " )
                cnt += 1
            n -= 1
        if ( cnt == total ) :
            break
        if ( l < n ) :
            for i in range ( n - 1 , l - 1 , - 1 ) :
                print ( arr [ k ] [ i ] , end = " " )
                cnt += 1
            k += 1
|||

PRIMALITY_TEST_SET_1_INTRODUCTION_AND_SCHOOL_METHOD

def isPrime ( n ) :
    if n <= 1 :
        return False
    for i in range ( 2 , n ) :
        if n % i == 0 :
            return False 
    return True
|||

FIND_CHARACTER_FIRST_STRING_PRESENT_MINIMUM_INDEX_SECOND_STRING

def printMinIndexChar ( Str , patt ) :
    minIndex = 10 ** 9
    m = len ( Str )
    n = len ( patt )
    for i in range ( n ) :
        for j in range ( m ) :
            if ( patt [ i ] == Str [ j ] and j < minIndex ) :
                minIndex = j
                break
    if ( minIndex != 10 ** 9 ) :
        print ( "Minimum Index Character = " , Str [ minIndex ] )
    else :
        print ( "No character present" )
|||

PROGRAM_TO_FIND_TRANSPOSE_OF_A_MATRIX_1

def transpose ( A , B ) :
    for i in range ( N ) :
        for j in range ( M ) :
            B [ i ] [ j ] = A [ j ] [ i ]
|||

COUNT_NATURAL_NUMBERS_WHOSE_PERMUTATION_GREATER_NUMBER

def countNumber ( n ) :
    result = 0
    for i in range ( 1 , 10 ) :
        s = [ ]
        if ( i <= n ) :
            s.append ( i )
            result += 1
        while len ( s ) != 0 :
            tp = s [ - 1 ]
            s.pop ( )
            for j in range ( tp % 10 , 10 ) :
                x = tp * 10 + j
                if ( x <= n ) :
                    s.append ( x )
                    result += 1
    return result
|||

FIND_FIRST_NATURAL_NUMBER_WHOSE_FACTORIAL_DIVISIBLE_X

def firstFactorialDivisibleNumber ( x ) :
    i = 1 
    fact = 1 
    for i in range ( 1 , x ) :
        fact = fact * i
        if ( fact % x == 0 ) :
            break
    return i
|||

PRINT_EQUAL_SUM_SETS_ARRAY_PARTITION_PROBLEM_SET_2

def printEqualSumSets ( arr , n ) :
    sum_array = sum ( arr )
    if ( sum_array & 1 ) :
        print ( "-1" )
        return
    k = sum_array >> 1
    dp = np.zeros ( ( n + 1 , k + 1 ) )
    for i in range ( 1 , k + 1 ) :
        dp [ 0 ] [ i ] = False
    for i in range ( n + 1 ) :
        dp [ i ] [ 0 ] = True
    for i in range ( 1 , n + 1 ) :
        for currSum in range ( 1 , k + 1 ) :
            dp [ i ] [ currSum ] = dp [ i - 1 ] [ currSum ]
            if ( arr [ i - 1 ] <= currSum ) :
                dp [ i ] [ currSum ] = ( dp [ i ] [ currSum ] or dp [ i - 1 ] [ currSum - arr [ i - 1 ] ] )
    set1 , set2 = [ ] , [ ]
    if ( not dp [ n ] [ k ] ) :
        print ( "-1" )
        return
    i = n
    currSum = k
    while ( i > 0 and currSum >= 0 ) :
        if ( dp [ i - 1 ] [ currSum ] ) :
            i -= 1
            set2.append ( arr [ i ] )
        elif ( dp [ i - 1 ] [ currSum - arr [ i - 1 ] ] ) :
            i -= 1
            currSum -= arr [ i ]
            set1.append ( arr [ i ] )
    print ( "Set 1 elements:" , end = " " )
    for i in range ( len ( set1 ) ) :
        print ( set1 [ i ] , end = " " )
    print ( "\nSet 2 elements:" , end = " " )
    for i in range ( len ( set2 ) ) :
        print ( set2 [ i ] , end = " " )
|||

COUNTING_PAIRS_PERSON_CAN_FORM_PAIR_ONE_1

def numberOfWays ( x ) :
    if x == 0 or x == 1 :
        return 1
    else :
        return ( numberOfWays ( x - 1 ) + ( x - 1 ) * numberOfWays ( x - 2 ) )
|||

COUNT_NEGATIVE_NUMBERS_IN_A_COLUMN_WISE_ROW_WISE_SORTED_MATRIX

def countNegative ( M , n , m ) :
    count = 0
    for i in range ( n ) :
        for j in range ( m ) :
            if M [ i ] [ j ] < 0 :
                count += 1
            else :
                break
    return count
|||

COUNT_SET_BITS_IN_AN_INTEGER

def countSetBits ( n ) :
    count = 0
    while ( n ) :
        count += n & 1
        n >>= 1
    return count
|||

MODULUS_TWO_FLOAT_DOUBLE_NUMBERS

def findMod ( a , b ) :
    if ( a < 0 ) :
        a = - a
    if ( b < 0 ) :
        b = - b
    mod = a
    while ( mod >= b ) :
        mod = mod - b
    if ( a < 0 ) :
        return - mod
    return mod
|||

FIND_A_SPECIFIC_PAIR_IN_MATRIX_1

def findMaxValue ( mat ) :
    maxValue = - sys.maxsize - 1
    maxArr = [ [ 0 for x in range ( N ) ] for y in range ( N ) ]
    maxArr [ N - 1 ] [ N - 1 ] = mat [ N - 1 ] [ N - 1 ]
    maxv = mat [ N - 1 ] [ N - 1 ] 
    for j in range ( N - 2 , - 1 , - 1 ) :
        if ( mat [ N - 1 ] [ j ] > maxv ) :
            maxv = mat [ N - 1 ] [ j ]
        maxArr [ N - 1 ] [ j ] = maxv
    maxv = mat [ N - 1 ] [ N - 1 ]
    for i in range ( N - 2 , - 1 , - 1 ) :
        if ( mat [ i ] [ N - 1 ] > maxv ) :
            maxv = mat [ i ] [ N - 1 ]
        maxArr [ i ] [ N - 1 ] = maxv
    for i in range ( N - 2 , - 1 , - 1 ) :
        for j in range ( N - 2 , - 1 , - 1 ) :
            if ( maxArr [ i + 1 ] [ j + 1 ] - mat [ i ] [ j ] > maxValue ) :
                maxValue = ( maxArr [ i + 1 ] [ j + 1 ] - mat [ i ] [ j ] )
            maxArr [ i ] [ j ] = max ( mat [ i ] [ j ] , max ( maxArr [ i ] [ j + 1 ] , maxArr [ i + 1 ] [ j ] ) )
    return maxValue
|||

MINIMUM_SUM_TWO_NUMBERS_FORMED_DIGITS_ARRAY

def solve ( arr , n ) :
    arr.sort ( )
    a = 0 ; b = 0
    for i in range ( n ) :
        if ( i % 2 != 0 ) :
            a = a * 10 + arr [ i ]
        else :
            b = b * 10 + arr [ i ]
    return a + b
|||

COUNT_DISTINCT_NON_NEGATIVE_PAIRS_X_Y_SATISFY_INEQUALITY_XX_YY_N_2_1

def countSolutions ( n ) :
    x = 0
    res = 0
    yCount = 0
    while ( yCount * yCount < n ) :
        yCount = yCount + 1
    while ( yCount != 0 ) :
        res = res + yCount
        x = x + 1
        while ( yCount != 0 and ( x * x + ( yCount - 1 ) * ( yCount - 1 ) >= n ) ) :
            yCount = yCount - 1
    return res
|||

FIND_INDEX_GIVEN_FIBONACCI_NUMBER_CONSTANT_TIME

def findIndex ( n ) :
    if ( n <= 1 ) :
        return n
    a = 0
    b = 1
    c = 1
    res = 1
    while ( c < n ) :
        c = a + b
        res = res + 1
        a = b
        b = c
    return res
|||

PROGRAM_OCTAL_DECIMAL_CONVERSION

def octalToDecimal ( n ) :
    num = n 
    dec_value = 0 
    base = 1 
    temp = num 
    while ( temp ) :
        last_digit = temp % 10 
        temp = int ( temp / 10 ) 
        dec_value += last_digit * base 
        base = base * 8 
    return dec_value 
|||

FIND_PERMUTED_ROWS_GIVEN_ROW_MATRIX

def permutatedRows ( mat , m , n , r ) :
    s = set ( )
    for j in range ( n ) :
        s.add ( mat [ r ] [ j ] )
    for i in range ( m ) :
        if i == r :
            continue
        for j in range ( n ) :
            if mat [ i ] [ j ] not in s :
                j = j - 2
                break 
        if j + 1 != n :
            continue
        print ( i )
|||

PRINT_A_CLOSEST_STRING_THAT_DOES_NOT_CONTAIN_ADJACENT_DUPLICATES

def noAdjacentDup ( s ) :
    n = len ( s )
    for i in range ( 1 , n ) :
        if ( s [ i ] == s [ i - 1 ] ) :
            s [ i ] = "a"
            while ( s [ i ] == s [ i - 1 ] or ( i + 1 < n and s [ i ] == s [ i + 1 ] ) ) :
                s [ i ] += 1
            i += 1
    return s
|||

SUM_MANHATTAN_DISTANCES_PAIRS_POINTS

def distancesum ( x , y , n ) :
    sum = 0
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            sum += ( abs ( x [ i ] - x [ j ] ) + abs ( y [ i ] - y [ j ] ) )
    return sum
|||

PROGRAM_FIND_STRING_START_END_GEEKS

def isCornerPresent ( str , corner ) :
    n = len ( str )
    cl = len ( corner )
    if ( n < cl ) :
        return False
    return ( ( str [ : cl ] == corner ) and ( str [ n - cl : ] == corner ) )
|||

LONGEST_SUBARRAY_COUNT_1S_ONE_COUNT_0S

def lenOfLongSubarr ( arr , n ) :
    um = { i : 0 for i in range ( 10 ) }
    sum = 0
    maxLen = 0
    for i in range ( n ) :
        if arr [ i ] == 0 :
            sum += - 1
        else :
            sum += 1
        if ( sum == 1 ) :
            maxLen = i + 1
        elif ( sum not in um ) :
            um [ sum ] = i
        if ( ( sum - 1 ) in um ) :
            if ( maxLen < ( i - um [ sum - 1 ] ) ) :
                maxLen = i - um [ sum - 1 ]
    return maxLen
|||

DIVIDE_CONQUER_SET_6_SEARCH_ROW_WISE_COLUMN_WISE_SORTED_2D_ARRAY

def search ( mat , fromRow , toRow , fromCol , toCol , key ) :
    i = fromRow + ( toRow - fromRow ) // 2 
    j = fromCol + ( toCol - fromCol ) // 2 
    if ( mat [ i ] [ j ] == key ) :
        print ( "Found " , key , " at " , i , " " , j ) 
    else :
        if ( i != toRow or j != fromCol ) :
            search ( mat , fromRow , i , j , toCol , key ) 
        if ( fromRow == toRow and fromCol + 1 == toCol ) :
            if ( mat [ fromRow ] [ toCol ] == key ) :
                print ( "Found " , key , " at " , fromRow , " " , toCol ) 
        if ( mat [ i ] [ j ] < key ) :
            if ( i + 1 <= toRow ) :
                search ( mat , i + 1 , toRow , fromCol , toCol , key ) 
        else :
            if ( j - 1 >= fromCol ) :
                search ( mat , fromRow , toRow , fromCol , j - 1 , key ) 
|||

SHORTEST_COMMON_SUPERSEQUENCE

def superSeq ( X , Y , m , n ) :
    if ( not m ) : return n
    if ( not n ) : return m
    if ( X [ m - 1 ] == Y [ n - 1 ] ) :
        return 1 + superSeq ( X , Y , m - 1 , n - 1 )
    return 1 + min ( superSeq ( X , Y , m - 1 , n ) , superSeq ( X , Y , m , n - 1 ) )
|||

URLIFY_GIVEN_STRING_REPLACE_SPACES

def replaceSpaces ( string ) :
    string = string.strip ( )
    i = len ( string )
    space_count = string.count ( '' )
    new_length = i + space_count * 2
    if new_length > MAX :
        return - 1
    index = new_length - 1
    string = list ( string )
    for f in range ( i - 2 , new_length - 2 ) :
        string.append ( '0' )
    for j in range ( i - 1 , 0 , - 1 ) :
        if string [ j ] == '' :
            string [ index ] = '0'
            string [ index - 1 ] = '2'
            string [ index - 2 ] = '%'
            index = index - 3
        else :
            string [ index ] = string [ j ]
            index -= 1
    return ''.join ( string )
|||

MAXIMUM_PATH_SUM_STARTING_CELL_0_TH_ROW_ENDING_CELL_N_1_TH_ROW

def MaximumPath ( Mat ) :
    result = 0
    dp = [ [ 0 for i in range ( N + 2 ) ] for j in range ( N ) ]
    for i in range ( N ) :
        for j in range ( 1 , N + 1 ) :
            dp [ i ] [ j ] = max ( dp [ i - 1 ] [ j - 1 ] , max ( dp [ i - 1 ] [ j ] , dp [ i - 1 ] [ j + 1 ] ) ) + \
                Mat [ i ] [ j - 1 ]
    for i in range ( N + 1 ) :
        result = max ( result , dp [ N - 1 ] [ i ] )
    return result
|||

COMPUTE_THE_INTEGER_ABSOLUTE_VALUE_ABS_WITHOUT_BRANCHING

def getAbs ( n ) :
    mask = n >> ( SIZE_INT * CHARBIT - 1 ) 
    return ( ( n + mask ) ^ mask ) 
|||

COUNT_PALINDROMIC_SUBSEQUENCE_GIVEN_STRING_1

def countPS ( i , j ) :
    if ( i >= n or j < 0 ) :
        return 0
    if ( dp [ i ] [ j ] != - 1 ) :
        return dp [ i ] [ j ]
    if ( abs ( i - j ) == 1 ) :
        if ( str [ i ] == str [ j ] ) :
            dp [ i ] [ j ] = 3
            return dp [ i ] [ j ]
        else :
            dp [ i ] [ j ] = 2
            return dp [ i ] [ j ]
    if ( i == j ) :
        dp [ 1 ] [ j ] = 1
        return dp [ 1 ] [ j ]
    elif ( str [ i ] == str [ j ] ) :
        dp [ i ] [ j ] = ( countPS ( i + 1 , j ) + countPS ( i , j - 1 ) + 1 )
        return dp [ i ] [ j ]
    else :
        dp [ i ] [ j ] = ( countPS ( i + 1 , j ) + countPS ( i , j - 1 ) - countPS ( i + 1 , j - 1 ) )
        return dp [ i ] [ j ]
|||

LARGEST_SUM_CONTIGUOUS_SUBARRAY_2

def maxSubArraySum ( a , size ) :
    max_so_far = a [ 0 ]
    curr_max = a [ 0 ]
    for i in range ( 1 , size ) :
        curr_max = max ( a [ i ] , curr_max + a [ i ] )
        max_so_far = max ( max_so_far , curr_max )
    return max_so_far
|||

COUNT_MINIMUM_STEPS_GET_GIVEN_DESIRED_ARRAY

def countMinOperations ( target , n ) :
    result = 0 
    while ( True ) :
        zero_count = 0 
        i = 0 
        while ( i < n ) :
            if ( ( target [ i ] & 1 ) > 0 ) :
                break 
            elif ( target [ i ] == 0 ) :
                zero_count += 1 
            i += 1 
        if ( zero_count == n ) :
            return result 
        if ( i == n ) :
            for j in range ( n ) :
                target [ j ] = target [ j ] // 2 
            result += 1 
        for j in range ( i , n ) :
            if ( target [ j ] & 1 ) :
                target [ j ] -= 1 
                result += 1 
|||

PRINT_FIBONACCI_SEQUENCE_USING_2_VARIABLES_1

def fib ( n ) :
    a = 0
    b = 1
    if ( n >= 0 ) :
        print ( a , end = ' ' )
    if ( n >= 1 ) :
        print ( b , end = ' ' )
    for i in range ( 2 , n + 1 ) :
        print ( a + b , end = ' ' )
        b = a + b
        a = b - a
|||

PROGRAM_CHECK_INPUT_INTEGER_STRING

def isNumber ( s ) :
    for i in range ( len ( s ) ) :
        if s [ i ].isdigit ( ) != True :
            return False
    return True
|||

MINIMUM_HEIGHT_TRIANGLE_GIVEN_BASE_AREA

def minHeight ( area , base ) :
    return math.ceil ( ( 2 * area ) / base )
|||

FIND_POSITION_GIVEN_NUMBER_AMONG_NUMBERS_MADE_4_7

def findpos ( n ) :
    i = 0
    j = len ( n )
    pos = 0
    while ( i < j ) :
        if ( n [ i ] == '4' ) :
            pos = pos * 2 + 1
        if ( n [ i ] == '7' ) :
            pos = pos * 2 + 2
        i = i + 1
    return pos
|||

MINIMUM_OPERATIONS_REQUIRED_SET_ELEMENTS_BINARY_MATRIX

def minOperation ( arr ) :
    ans = 0
    for i in range ( N - 1 , - 1 , - 1 ) :
        for j in range ( M - 1 , - 1 , - 1 ) :
            if ( arr [ i ] [ j ] == 0 ) :
                ans += 1
                for k in range ( i + 1 ) :
                    for h in range ( j + 1 ) :
                        if ( arr [ k ] [ h ] == 1 ) :
                            arr [ k ] [ h ] = 0
                        else :
                            arr [ k ] [ h ] = 1
    return ans
|||

LONGEST_EVEN_LENGTH_SUBSTRING_SUM_FIRST_SECOND_HALF_2

def findLength ( string , n ) :
    Sum = [ 0 ] * ( n + 1 )
    for i in range ( 1 , n + 1 ) :
        Sum [ i ] = ( Sum [ i - 1 ] + int ( string [ i - 1 ] ) )
    ans = 0
    for length in range ( 2 , n + 1 , 2 ) :
        for i in range ( 0 , n - length + 1 ) :
            j = i + length - 1
            if ( Sum [ i + length // 2 ] - Sum [ i ] == Sum [ i + length ] - Sum [ i + length // 2 ] ) :
                ans = max ( ans , length )
    return ans
|||

MULTIPLY_LARGE_NUMBERS_REPRESENTED_AS_STRINGS

def multiply ( num1 , num2 ) :
    len1 = len ( num1 )
    len2 = len ( num2 )
    if len1 == 0 or len2 == 0 :
        return "0"
    result = [ 0 ] * ( len1 + len2 )
    i_n1 = 0
    i_n2 = 0
    for i in range ( len1 - 1 , - 1 , - 1 ) :
        carry = 0
        n1 = ord ( num1 [ i ] ) - 48
        i_n2 = 0
        for j in range ( len2 - 1 , - 1 , - 1 ) :
            n2 = ord ( num2 [ j ] ) - 48
            summ = n1 * n2 + result [ i_n1 + i_n2 ] + carry
            carry = summ // 10
            result [ i_n1 + i_n2 ] = summ % 10
            i_n2 += 1
        if ( carry > 0 ) :
            result [ i_n1 + i_n2 ] += carry
        i_n1 += 1
    i = len ( result ) - 1
    while ( i >= 0 and result [ i ] == 0 ) :
        i -= 1
    if ( i == - 1 ) :
        return "0"
    s = ""
    while ( i >= 0 ) :
        s += chr ( result [ i ] + 48 )
        i -= 1
    return s
|||

PARTITION_NUMBER_TWO_DIVISBLE_PARTS

def findDivision ( str , a , b ) :
    lenn = len ( str )
    lr = [ 0 ] * ( lenn + 1 )
    lr [ 0 ] = ( int ( str [ 0 ] ) ) % a
    for i in range ( 1 , lenn ) :
        lr [ i ] = ( ( lr [ i - 1 ] * 10 ) % a + \ int ( str [ i ] ) ) % a
    rl = [ 0 ] * ( lenn + 1 )
    rl [ lenn - 1 ] = int ( str [ lenn - 1 ] ) % b
    power10 = 10
    for i in range ( lenn - 2 , - 1 , - 1 ) :
        rl [ i ] = ( rl [ i + 1 ] + int ( str [ i ] ) * power10 ) % b
        power10 = ( power10 * 10 ) % b
    for i in range ( 0 , lenn - 1 ) :
        if ( lr [ i ] != 0 ) :
            continue
        if ( rl [ i + 1 ] == 0 ) :
            print ( "YES" )
            for k in range ( 0 , i + 1 ) :
                print ( str [ k ] , end = "" )
            print ( "," , end = "" )
            for i in range ( i + 1 , lenn ) :
                print ( str [ k ] , end = "" )
                return
    print ( "NO" )
|||

PROGRAM_BEST_FIT_ALGORITHM_MEMORY_MANAGEMENT

def bestFit ( blockSize , m , processSize , n ) :
    allocation = [ - 1 ] * n
    for i in range ( n ) :
        bestIdx = - 1
        for j in range ( m ) :
            if blockSize [ j ] >= processSize [ i ] :
                if bestIdx == - 1 :
                    bestIdx = j
                elif blockSize [ bestIdx ] > blockSize [ j ] :
                    bestIdx = j
        if bestIdx != - 1 :
            allocation [ i ] = bestIdx
            blockSize [ bestIdx ] -= processSize [ i ]
    print ( "Process No.Process Size     Block no." )
    for i in range ( n ) :
        print ( i + 1 , "         " , processSize [ i ] , end = "         " )
        if allocation [ i ] != - 1 :
            print ( allocation [ i ] + 1 )
        else :
            print ( "Not Allocated" )
|||

FINDING_THE_MAXIMUM_SQUARE_SUB_MATRIX_WITH_ALL_EQUAL_ELEMENTS

def largestKSubmatrix ( a ) :
    dp = [ [ 0 for x in range ( Row ) ] for y in range ( Col ) ]
    result = 0
    for i in range ( Row ) :
        for j in range ( Col ) :
            if ( i == 0 or j == 0 ) :
                dp [ i ] [ j ] = 1
            else :
                if ( a [ i ] [ j ] == a [ i - 1 ] [ j ] and a [ i ] [ j ] == a [ i ] [ j - 1 ] and a [ i ] [ j ] == a [ i - 1 ] [ j - 1 ] ) :
                    dp [ i ] [ j ] = min ( min ( dp [ i - 1 ] [ j ] , dp [ i ] [ j - 1 ] ) , dp [ i - 1 ] [ j - 1 ] ) + 1
                else :
                    dp [ i ] [ j ] = 1
            result = max ( result , dp [ i ] [ j ] )
    return result
|||

FRIENDS_PAIRING_PROBLEM_1

def countFriendsPairings ( n ) :
    dp = [ - 1 ] * 100
    if ( dp [ n ] != - 1 ) :
        return dp [ n ]
    if ( n > 2 ) :
        dp [ n ] = ( countFriendsPairings ( n - 1 ) + ( n - 1 ) * countFriendsPairings ( n - 2 ) )
        return dp [ n ]
    else :
        dp [ n ] = n
        return dp [ n ]
|||

FIRST_ELEMENT_OCCURRING_K_TIMES_ARRAY

def firstElement ( arr , n , k ) :
    count_map = { } 
    for i in range ( 0 , n ) :
        if ( arr [ i ] in count_map.keys ( ) ) :
            count_map [ arr [ i ] ] += 1
        else :
            count_map [ arr [ i ] ] = 1
        i += 1
    for i in range ( 0 , n ) :
        if ( count_map [ arr [ i ] ] == k ) :
            return arr [ i ]
        i += 1
    return - 1
|||

SUM_SERIES_0_6_0_06_0_006_0_0006_N_TERMS

def sumOfSeries ( n ) :
    return ( ( 0.666 ) * ( 1 - 1 / pow ( 10 , n ) ) ) 
|||

COUNT_WORDS_IN_A_GIVEN_STRING

def countWords ( string ) :
    state = OUT
    wc = 0
    for i in range ( len ( string ) ) :
        if ( string [ i ] == ' ' or string [ i ] == '\n' or string [ i ] == '\t' ) :
            state = OUT
        elif state == OUT :
            state = IN
            wc += 1
    return wc
|||

PARTITION_INTO_TWO_SUBARRAYS_OF_LENGTHS_K_AND_N_K_SUCH_THAT_THE_DIFFERENCE_OF_SUMS_IS_MAXIMUM

def maxDifference ( arr , N , k ) :
    S = 0
    S1 = 0
    max_difference = 0
    for i in range ( N ) :
        S += arr [ i ]
    arr.sort ( reverse = True )
    M = max ( k , N - k )
    for i in range ( M ) :
        S1 += arr [ i ]
    max_difference = S1 - ( S - S1 )
    return max_difference
|||

HOW_WILL_YOU_PRINT_NUMBERS_FROM_1_TO_200_WITHOUT_USING_LOOP

def printNos ( n ) :
    if n > 0 :
        printNos ( n - 1 )
        print ( n , end = ' ' )
|||

GIVEN_A_SORTED_AND_ROTATED_ARRAY_FIND_IF_THERE_IS_A_PAIR_WITH_A_GIVEN_SUM_1

def pairsInSortedRotated ( arr , n , x ) :
    for i in range ( n ) :
        if arr [ i ] > arr [ i + 1 ] :
            break
    l = ( i + 1 ) % n
    r = i
    cnt = 0
    while ( l != r ) :
        if arr [ l ] + arr [ r ] == x :
            cnt += 1
            if l == ( r - 1 + n ) % n :
                return cnt
            l = ( l + 1 ) % n
            r = ( r - 1 + n ) % n
        elif arr [ l ] + arr [ r ] < x :
            l = ( l + 1 ) % n
        else :
            r = ( n + r - 1 ) % n
    return cnt
|||

FIND_THE_ELEMENT_THAT_APPEARS_ONCE

def getSingle ( arr , n ) :
    ones = 0
    twos = 0
    for i in range ( n ) :
        twos = twos | ( ones & arr [ i ] )
        ones = ones ^ arr [ i ]
        common_bit_mask = ~ ( ones & twos )
        ones &= common_bit_mask
        twos &= common_bit_mask
    return ones
|||

CASSINIS_IDENTITY

def cassini ( n ) :
    return - 1 if ( n & 1 ) else 1
|||

DISTRIBUTING_ALL_BALLS_WITHOUT_REPETITION

def distributingBalls ( k , n , string ) :
    a = [ 0 ] * MAX_CHAR
    for i in range ( n ) :
        a [ ord ( string [ i ] ) - ord ( 'a' ) ] += 1
    for i in range ( MAX_CHAR ) :
        if ( a [ i ] > k ) :
            return False
    return True
|||

DISTRIBUTING_ITEMS_PERSON_CANNOT_TAKE_TWO_ITEMS_TYPE

def checkCount ( arr , n , k ) :
    for i in range ( n ) :
        count = 0
        for j in range ( n ) :
            if arr [ j ] == arr [ i ] :
                count += 1
            if count > 2 * k :
                return False
    return True
|||

MAXIMIZE_ARRJ_ARRI_ARRL_ARRK_SUCH_THAT_I_J_K_L

def findMaxValue ( arr , n ) :
    if n < 4 :
        print ( "The array should have atlest 4 elements" )
        return MIN
    table1 , table2 = [ MIN ] * ( n + 1 ) , [ MIN ] * n
    table3 , table4 = [ MIN ] * ( n - 1 ) , [ MIN ] * ( n - 2 )
    for i in range ( n - 1 , - 1 , - 1 ) :
        table1 [ i ] = max ( table1 [ i + 1 ] , arr [ i ] )
    for i in range ( n - 2 , - 1 , - 1 ) :
        table2 [ i ] = max ( table2 [ i + 1 ] , table1 [ i + 1 ] - arr [ i ] )
    for i in range ( n - 3 , - 1 , - 1 ) :
        table3 [ i ] = max ( table3 [ i + 1 ] , table2 [ i + 1 ] + arr [ i ] )
    for i in range ( n - 4 , - 1 , - 1 ) :
        table4 [ i ] = max ( table4 [ i + 1 ] , table3 [ i + 1 ] - arr [ i ] )
    return table4 [ 0 ]
|||

COUNT_NEGATIVE_NUMBERS_IN_A_COLUMN_WISE_ROW_WISE_SORTED_MATRIX_1

def countNegative ( M , n , m ) :
    count = 0
    i = 0
    j = m - 1
    while j >= 0 and i < n :
        if M [ i ] [ j ] < 0 :
            count += ( j + 1 )
            i += 1
        else :
            j -= 1
    return count
|||

SORT_AN_ARRAY_OF_0S_1S_AND_2S

def sort012 ( a , arr_size ) :
    lo = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi :
        if a [ mid ] == 0 :
            a [ lo ] , a [ mid ] = a [ mid ] , a [ lo ]
            lo = lo + 1
            mid = mid + 1
        elif a [ mid ] == 1 :
            mid = mid + 1
        else :
            a [ mid ] , a [ hi ] = a [ hi ] , a [ mid ]
            hi = hi - 1
|||

NTH_EVEN_FIBONACCI_NUMBER

def evenFib ( n ) :
    if ( n < 1 ) :
        return n
    if ( n == 1 ) :
        return 2
    return ( ( 4 * evenFib ( n - 1 ) ) + evenFib ( n - 2 ) )
|||

NEXT_GREATER_ELEMENT

def printNGE ( arr ) :
    for i in range ( 0 , len ( arr ) , 1 ) :
        next = - 1
        for j in range ( i + 1 , len ( arr ) , 1 ) :
            if arr [ i ] < arr [ j ] :
                next = arr [ j ]
                break
        print ( str ( arr [ i ] ) + " -- " + str ( next ) )
|||

CHECK_WHETHER_GIVEN_CIRCLE_RESIDE_BOUNDARY_MAINTAINED_OUTER_CIRCLE_INNER_CIRCLE

def fitOrNotFit ( R , r , x , y , rad ) :
    val = math.sqrt ( math.pow ( x , 2 ) + math.pow ( y , 2 ) )
    if ( val + rad <= R and val - rad >= R - r ) :
        print ( "Fits\n" )
    else :
        print ( "Doesn't Fit" )
|||

BASIC_AND_EXTENDED_EUCLIDEAN_ALGORITHMS_1

def gcdExtended ( a , b , x , y ) :
    if a == 0 :
        x = 0
        y = 1
        return b
    x1 = 1
    y1 = 1
    gcd = gcdExtended ( b % a , a , x1 , y1 )
    x = y1 - ( b / a ) * x1
    y = x1
    return gcd
|||

FIND_SMALLEST_RANGE_CONTAINING_ELEMENTS_FROM_K_LISTS

def findSmallestRange ( arr , n , k ) :
    i , minval , maxval , minrange , minel , maxel , flag , minind = 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0
    for i in range ( k + 1 ) :
        ptr [ i ] = 0
    minrange = 10 ** 9
    while ( 1 ) :
        minind = - 1
        minval = 10 ** 9
        maxval = - 10 ** 9
        flag = 0
        for i in range ( k ) :
            if ( ptr [ i ] == n ) :
                flag = 1
                break
            if ( ptr [ i ] < n and arr [ i ] [ ptr [ i ] ] < minval ) :
                minind = i
                minval = arr [ i ] [ ptr [ i ] ]
            if ( ptr [ i ] < n and arr [ i ] [ ptr [ i ] ] > maxval ) :
                maxval = arr [ i ] [ ptr [ i ] ]
        if ( flag ) :
            break
        ptr [ minind ] += 1
        if ( ( maxval - minval ) < minrange ) :
            minel = minval
            maxel = maxval
            minrange = maxel - minel
    print ( "The smallest range is [" , minel , maxel , "]" )
|||

FIND_THE_MINIMUM_COST_TO_REACH_A_DESTINATION_WHERE_EVERY_STATION_IS_CONNECTED_IN_ONE_DIRECTION

def minCost ( cost ) :
    dist = [ 0 for i in range ( N ) ]
    for i in range ( N ) :
        dist [ i ] = INF
    dist [ 0 ] = 0
    for i in range ( N ) :
        for j in range ( i + 1 , N ) :
            if ( dist [ j ] > dist [ i ] + cost [ i ] [ j ] ) :
                dist [ j ] = dist [ i ] + cost [ i ] [ j ]
    return dist [ N - 1 ]
|||

MIDDLE_OF_THREE_USING_MINIMUM_COMPARISONS_1

def middleOfThree ( a , b , c ) :
    if a > b :
        if ( b > c ) :
            return b
        elif ( a > c ) :
            return c
        else :
            return a
    else :
        if ( a > c ) :
            return a
        elif ( b > c ) :
            return c
        else :
            return b
|||

CHECK_LARGE_NUMBER_DIVISIBLE_11_NOT

def check ( st ) :
    n = len ( st )
    oddDigSum = 0
    evenDigSum = 0
    for i in range ( 0 , n ) :
        if ( i % 2 == 0 ) :
            oddDigSum = oddDigSum + ( ( int ) ( st [ i ] ) )
        else :
            evenDigSum = evenDigSum + ( ( int ) ( st [ i ] ) )
    return ( ( oddDigSum - evenDigSum ) % 11 == 0 )
|||

COMPUTE_MODULUS_DIVISION_BY_A_POWER_OF_2_NUMBER

def getModulo ( n , d ) :
    return ( n & ( d - 1 ) )
|||

COUNT_BINARY_STRINGS_K_TIMES_APPEARING_ADJACENT_TWO_SET_BITS

def countStrings ( n , k ) :
    dp = [ [ [ 0 , 0 ] for __ in range ( k + 1 ) ] for _ in range ( n + 1 ) ]
    dp [ 1 ] [ 0 ] [ 0 ] = 1
    dp [ 1 ] [ 0 ] [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        for j in range ( k + 1 ) :
            dp [ i ] [ j ] [ 0 ] = ( dp [ i - 1 ] [ j ] [ 0 ] + dp [ i - 1 ] [ j ] [ 1 ] )
            dp [ i ] [ j ] [ 1 ] = dp [ i - 1 ] [ j ] [ 0 ]
            if j >= 1 :
                dp [ i ] [ j ] [ 1 ] += dp [ i - 1 ] [ j - 1 ] [ 1 ]
    return dp [ n ] [ k ] [ 0 ] + dp [ n ] [ k ] [ 1 ]
|||

FINDING_K_MODULUS_ARRAY_ELEMENT

def printEqualModNumbers ( arr , n ) :
    arr.sort ( ) 
    d = arr [ n - 1 ] - arr [ 0 ] 
    v = [ ] 
    i = 1 
    while ( i * i <= d ) :
        if ( d % i == 0 ) :
            v.append ( i ) 
            if ( i != d / i ) :
                v.append ( d / i ) 
        i += 1 
    for i in range ( len ( v ) ) :
        temp = arr [ 0 ] % v [ i ] 
        j = 1 
        while ( j < n ) :
            if ( arr [ j ] % v [ i ] != temp ) :
                break 
            j += 1 
        if ( j == n ) :
            print ( v [ i ] , end = " " ) 
|||

CIRCULAR_MATRIX_CONSTRUCT_A_MATRIX_WITH_NUMBERS_1_TO_MN_IN_SPIRAL_WAY

def spiralFill ( m , n , a ) :
    val = 1
    k , l = 0 , 0
    while ( k < m and l < n ) :
        for i in range ( l , n ) :
            a [ k ] [ i ] = val
            val += 1
        k += 1
        for i in range ( k , m ) :
            a [ i ] [ n - 1 ] = val
            val += 1
        n -= 1
        if ( k < m ) :
            for i in range ( n - 1 , l - 1 , - 1 ) :
                a [ m - 1 ] [ i ] = val
                val += 1
            m -= 1
        if ( l < n ) :
            for i in range ( m - 1 , k - 1 , - 1 ) :
                a [ i ] [ l ] = val
                val += 1
            l += 1
|||

FIND_THE_TWO_REPEATING_ELEMENTS_IN_A_GIVEN_ARRAY_2

def printRepeating ( arr , size ) :
    xor = arr [ 0 ]
    n = size - 2
    x = 0
    y = 0
    for i in range ( 1 , size ) :
        xor ^= arr [ i ]
    for i in range ( 1 , n + 1 ) :
        xor ^= i
    set_bit_no = xor & ~ ( xor - 1 )
    for i in range ( 0 , size ) :
        if ( arr [ i ] & set_bit_no ) :
            x = x ^ arr [ i ]
        else :
            y = y ^ arr [ i ]
    for i in range ( 1 , n + 1 ) :
        if ( i & set_bit_no ) :
            x = x ^ i
        else :
            y = y ^ i
    print ( "The two repeating" , "elements are" , y , x )
|||

COUNT_POSSIBLE_WAYS_TO_CONSTRUCT_BUILDINGS

def countWays ( N ) :
    if ( N == 1 ) :
        return 4
    countB = 1
    countS = 1
    for i in range ( 2 , N + 1 ) :
        prev_countB = countB
        prev_countS = countS
        countS = prev_countB + prev_countS
        countB = prev_countS
    result = countS + countB
    return ( result * result )
|||

ONE_LINE_FUNCTION_FOR_FACTORIAL_OF_A_NUMBER

def factorial ( n ) :
    return 1 if ( n == 1 or n == 0 ) else n * factorial ( n - 1 ) 
|||

CHECK_GIVEN_MATRIX_SPARSE_NOT

def isSparse ( array , m , n ) :
    counter = 0
    for i in range ( 0 , m ) :
        for j in range ( 0 , n ) :
            if ( array [ i ] [ j ] == 0 ) :
                counter = counter + 1
    return ( counter > ( ( m * n ) // 2 ) )
|||

DYNAMIC_PROGRAMMING_SET_10_0_1_KNAPSACK_PROBLEM

def knapSack ( W , wt , val , n ) :
    if n == 0 or W == 0 :
        return 0
    if ( wt [ n - 1 ] > W ) :
        return knapSack ( W , wt , val , n - 1 )
    else :
        return max ( val [ n - 1 ] + knapSack ( W - wt [ n - 1 ] , wt , val , n - 1 ) , knapSack ( W , wt , val , n - 1 ) )
|||

FIND_SUBARRAY_LEAST_AVERAGE

def findMinAvgSubarray ( arr , n , k ) :
    if ( n < k ) : return 0
    res_index = 0
    curr_sum = 0
    for i in range ( k ) :
        curr_sum += arr [ i ]
    min_sum = curr_sum
    for i in range ( k , n ) :
        curr_sum += arr [ i ] - arr [ i - k ]
        if ( curr_sum < min_sum ) :
            min_sum = curr_sum
            res_index = ( i - k + 1 )
    print ( "Subarray between [" , res_index , ", " , ( res_index + k - 1 ) , "] has minimum average" )
|||

QUERIES_FOR_CHARACTERS_IN_A_REPEATED_STRING

def query ( s , i , j ) :
    n = len ( s )
    i %= n
    j %= n
    print ( "Yes" ) if s [ i ] == s [ j ] else print ( "No" )
|||

A_PRODUCT_ARRAY_PUZZLE_1

def productArray ( arr , n ) :
    if n == 1 :
        print ( 0 )
        return
    i , temp = 1 , 1
    prod = [ 1 for i in range ( n ) ]
    for i in range ( n ) :
        prod [ i ] = temp
        temp *= arr [ i ]
    temp = 1
    for i in range ( n - 1 , - 1 , - 1 ) :
        prod [ i ] *= temp
        temp *= arr [ i ]
    for i in range ( n ) :
        print ( prod [ i ] , end = " " )
    return
|||

FIND_PAIRS_GIVEN_SUM_ELEMENTS_PAIR_DIFFERENT_ROWS

def pairSum ( mat , n , sum ) :
    for i in range ( n ) :
        mat [ i ].sort ( )
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            left = 0
            right = n - 1
            while ( left < n and right >= 0 ) :
                if ( ( mat [ i ] [ left ] + mat [ j ] [ right ] ) == sum ) :
                    print ( "(" , mat [ i ] [ left ] , ", " , mat [ j ] [ right ] , "), " , end = " " )
                    left += 1
                    right -= 1
                else :
                    if ( ( mat [ i ] [ left ] + mat [ j ] [ right ] ) < sum ) :
                        left += 1
                    else :
                        right -= 1
|||

CHECK_STRING_CAN_OBTAINED_ROTATING_ANOTHER_STRING_2_PLACES

def isRotated ( str1 , str2 ) :
    if ( len ( str1 ) != len ( str2 ) ) :
        return False
    clock_rot = ""
    anticlock_rot = ""
    l = len ( str2 )
    anticlock_rot = ( anticlock_rot + str2 [ l - 2 : ] + str2 [ 0 : l - 2 ] )
    clock_rot = clock_rot + str2 [ 2 : ] + str2 [ 0 : 2 ]
    return ( str1 == clock_rot or str1 == anticlock_rot )
|||

N_TH_NUMBER_WHOSE_SUM_OF_DIGITS_IS_TEN

def findNth ( n ) :
    count = 0
    for curr in itertools.count ( ) :
        sum = 0
        x = curr
        while ( x ) :
            sum = sum + x % 10
            x = x // 10
        if ( sum == 10 ) :
            count = count + 1
        if ( count == n ) :
            return curr
    return - 1
|||

PROGRAM_FIND_SLOPE_LINE

def slope ( x1 , y1 , x2 , y2 ) :
    return ( float ) ( y2 - y1 ) / ( x2 - x1 )
|||

GCD_ELEMENTS_GIVEN_RANGE

def rangeGCD ( n , m ) :
    return n if ( n == m ) else 1
|||

LONGEST_ALTERNATING_SUB_ARRAY_STARTING_EVERY_INDEX_BINARY_ARRAY_1

def alternateSubarray ( arr , n ) :
    count = 1
    prev = arr [ 0 ]
    for i in range ( 1 , n ) :
        if ( ( arr [ i ] ^ prev ) == 0 ) :
            while ( count ) :
                print ( count , end = " " )
                count -= 1
        count += 1
        prev = arr [ i ]
    while ( count ) :
        print ( count , end = " " )
        count -= 1
|||

FIND_UNIT_DIGIT_X_RAISED_POWER_Y

def unitDigitXRaisedY ( x , y ) :
    res = 1
    for i in range ( y ) :
        res = ( res * x ) % 10
    return res
|||

MULTIPLY_LARGE_INTEGERS_UNDER_LARGE_MODULO

def moduloMultiplication ( a , b , mod ) :
    res = 0 
    a = a % mod 
    while ( b ) :
        if ( b & 1 ) :
            res = ( res + a ) % mod 
        a = ( 2 * a ) % mod 
        b >>= 1 
    return res 
|||

FIND_SMALLEST_NUMBER_WITH_GIVEN_NUMBER_OF_DIGITS_AND_DIGIT_SUM

def findSmallest ( m , s ) :
    if ( s == 0 ) :
        if ( m == 1 ) :
            print ( "Smallest number is 0" )
        else :
            print ( "Not possible" )
        return
    if ( s > 9 * m ) :
        print ( "Not possible" )
        return
    res = [ 0 for i in range ( m + 1 ) ]
    s -= 1
    for i in range ( m - 1 , 0 , - 1 ) :
        if ( s > 9 ) :
            res [ i ] = 9
            s -= 9
        else :
            res [ i ] = s
            s = 0
    res [ 0 ] = s + 1
    print ( "Smallest number is " , end = "" )
    for i in range ( m ) :
        print ( res [ i ] , end = "" )
|||

C_PROGRAM_FIND_LARGEST_ELEMENT_ARRAY

def largest ( arr , n ) :
    max = arr [ 0 ]
    for i in range ( 1 , n ) :
        if arr [ i ] > max :
            max = arr [ i ]
    return max
|||

COUNT_NUMBERS_CAN_CONSTRUCTED_USING_TWO_NUMBERS

def countNums ( n , x , y ) :
    arr = [ False for i in range ( n + 2 ) ]
    if ( x <= n ) :
        arr [ x ] = True
    if ( y <= n ) :
        arr [ y ] = True
    result = 0
    for i in range ( min ( x , y ) , n + 1 ) :
        if ( arr [ i ] ) :
            if ( i + x <= n ) :
                arr [ i + x ] = True
            if ( i + y <= n ) :
                arr [ i + y ] = True
            result = result + 1
    return result
|||

BUBBLE_SORT_1

def bubbleSort ( arr ) :
    n = len ( arr )
    for i in range ( n ) :
        swapped = False
        for j in range ( 0 , n - i - 1 ) :
            if arr [ j ] > arr [ j + 1 ] :
                arr [ j ] , arr [ j + 1 ] = arr [ j + 1 ] , arr [ j ]
                swapped = True
        if swapped == False :
            break
|||

MAXIMUM_SUM_2_X_N_GRID_NO_TWO_ELEMENTS_ADJACENT

def maxSum ( grid , n ) :
    incl = max ( grid [ 0 ] [ 0 ] , grid [ 1 ] [ 0 ] )
    excl = 0
    for i in range ( 1 , n ) :
        excl_new = max ( excl , incl )
        incl = excl + max ( grid [ 0 ] [ i ] , grid [ 1 ] [ i ] )
        excl = excl_new
    return max ( excl , incl )
|||

GCD_FACTORIALS_TWO_NUMBERS

def gcdOfFactorial ( m , n ) :
    return math.factorial ( min ( m , n ) )
|||

AREA_OF_A_SECTOR

def SectorArea ( radius , angle ) :
    pi = 22 / 7
    if angle >= 360 :
        print ( "Angle not possible" )
        return
    else :
        sector = ( pi * radius ** 2 ) * ( angle / 360 )
        print ( sector )
        return
|||

COUNT_EVEN_LENGTH_BINARY_SEQUENCES_WITH_SAME_SUM_OF_FIRST_AND_SECOND_HALF_BITS_1

def countSeq ( n ) :
    nCr = 1
    res = 1
    for r in range ( 1 , n + 1 ) :
        nCr = ( nCr * ( n + 1 - r ) ) / r 
        res += nCr * nCr 
    return res 
|||

LONGEST_EVEN_LENGTH_SUBSTRING_SUM_FIRST_SECOND_HALF_1

def findLength ( string ) :
    n = len ( string )
    maxlen = 0
    Sum = [ [ 0 for x in range ( n ) ] for y in range ( n ) ]
    for i in range ( 0 , n ) :
        Sum [ i ] [ i ] = int ( string [ i ] )
    for length in range ( 2 , n + 1 ) :
        for i in range ( 0 , n - length + 1 ) :
            j = i + length - 1
            k = length // 2
            Sum [ i ] [ j ] = ( Sum [ i ] [ j - k ] + Sum [ j - k + 1 ] [ j ] )
            if ( length % 2 == 0 and Sum [ i ] [ j - k ] == Sum [ ( j - k + 1 ) ] [ j ] and length > maxlen ) :
                maxlen = length
    return maxlen
|||

SWAP_ALL_ODD_AND_EVEN_BITS

def swapBits ( x ) :
    even_bits = x & 0xAAAAAAAA
    odd_bits = x & 0x55555555
    even_bits >>= 1
    odd_bits <<= 1
    return ( even_bits | odd_bits )
|||

SORT_ARRAY_WAVE_FORM_2

def sortInWave ( arr , n ) :
    arr.sort ( )
    for i in range ( 0 , n - 1 , 2 ) :
        arr [ i ] , arr [ i + 1 ] = arr [ i + 1 ] , arr [ i ]
|||

FIND_HARMONIC_MEAN_USING_ARITHMETIC_MEAN_GEOMETRIC_MEAN

def compute ( a , b ) :
    AM = ( a + b ) / 2
    GM = math.sqrt ( a * b )
    HM = ( GM * GM ) / AM
    return HM
|||

COUNT_BALANCED_BINARY_TREES_HEIGHT_H

def countBT ( h ) :
    MOD = 1000000007
    dp = [ 0 for i in range ( h + 1 ) ]
    dp [ 0 ] = 1
    dp [ 1 ] = 1
    for i in range ( 2 , h + 1 ) :
        dp [ i ] = ( dp [ i - 1 ] * ( ( 2 * dp [ i - 2 ] ) % MOD + dp [ i - 1 ] ) % MOD ) % MOD
    return dp [ h ]
|||

MINIMUM_INSERTIONS_TO_FORM_A_PALINDROME_WITH_PERMUTATIONS_ALLOWED

def minInsertion ( tr1 ) :
    n = len ( str1 )
    res = 0
    count = [ 0 for i in range ( 26 ) ]
    for i in range ( n ) :
        count [ ord ( str1 [ i ] ) - ord ( 'a' ) ] += 1
    for i in range ( 26 ) :
        if ( count [ i ] % 2 == 1 ) :
            res += 1
    if ( res == 0 ) :
        return 0
    else :
        return res - 1
|||

SHUFFLE_A_GIVEN_ARRAY

def randomize ( arr , n ) :
    for i in range ( n - 1 , 0 , - 1 ) :
        j = random.randint ( 0 , i + 1 )
        arr [ i ] , arr [ j ] = arr [ j ] , arr [ i ]
    return arr
|||

UGLY_NUMBERS

def getNthUglyNo ( n ) :
    ugly = [ 0 ] * n
    ugly [ 0 ] = 1
    i2 = i3 = i5 = 0
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    for l in range ( 1 , n ) :
        ugly [ l ] = min ( next_multiple_of_2 , next_multiple_of_3 , next_multiple_of_5 )
        if ugly [ l ] == next_multiple_of_2 :
            i2 += 1
            next_multiple_of_2 = ugly [ i2 ] * 2
        if ugly [ l ] == next_multiple_of_3 :
            i3 += 1
            next_multiple_of_3 = ugly [ i3 ] * 3
        if ugly [ l ] == next_multiple_of_5 :
            i5 += 1
            next_multiple_of_5 = ugly [ i5 ] * 5
    return ugly [ - 1 ]
|||

MINIMUM_COST_CUT_BOARD_SQUARES

def minimumCostOfBreaking ( X , Y , m , n ) :
    res = 0
    X.sort ( reverse = True )
    Y.sort ( reverse = True )
    hzntl = 1 ; vert = 1
    i = 0 ; j = 0
    while ( i < m and j < n ) :
        if ( X [ i ] > Y [ j ] ) :
            res += X [ i ] * vert
            hzntl += 1
            i += 1
        else :
            res += Y [ j ] * hzntl
            vert += 1
            j += 1
    total = 0
    while ( i < m ) :
        total += X [ i ]
        i += 1
    res += total * vert
    total = 0
    while ( j < n ) :
        total += Y [ j ]
        j += 1
    res += total * hzntl
    return res
|||

DYNAMIC_PROGRAMMING_SET_10_0_1_KNAPSACK_PROBLEM_1

def knapSack ( W , wt , val , n ) :
    K = [ [ 0 for x in range ( W + 1 ) ] for x in range ( n + 1 ) ]
    for i in range ( n + 1 ) :
        for w in range ( W + 1 ) :
            if i == 0 or w == 0 :
                K [ i ] [ w ] = 0
            elif wt [ i - 1 ] <= w :
                K [ i ] [ w ] = max ( val [ i - 1 ] + K [ i - 1 ] [ w - wt [ i - 1 ] ] , K [ i - 1 ] [ w ] )
            else :
                K [ i ] [ w ] = K [ i - 1 ] [ w ]
    return K [ n ] [ W ]
|||

STACK_PERMUTATIONS_CHECK_IF_AN_ARRAY_IS_STACK_PERMUTATION_OF_OTHER

def checkStackPermutation ( ip , op , n ) :
    Input = Queue ( )
    for i in range ( n ) :
        Input.put ( ip [ i ] )
    output = Queue ( )
    for i in range ( n ) :
        output.put ( op [ i ] )
    tempStack = [ ]
    while ( not Input.empty ( ) ) :
        ele = Input.queue [ 0 ]
        Input.get ( )
        if ( ele == output.queue [ 0 ] ) :
            output.get ( )
            while ( len ( tempStack ) != 0 ) :
                if ( tempStack [ - 1 ] == output.queue [ 0 ] ) :
                    tempStack.pop ( )
                    output.get ( )
                else :
                    break
        else :
            tempStack.append ( ele )
    return ( Input.empty ( ) and len ( tempStack ) == 0 )
|||

PROBABILITY_THREE_RANDOMLY_CHOSEN_NUMBERS_AP

def procal ( n ) :
    return ( 3.0 * n ) / ( 4.0 * ( n * n ) - 1 )
|||

REMOVE_BRACKETS_ALGEBRAIC_STRING_CONTAINING_OPERATORS

def simplify ( Str ) :
    Len = len ( Str )
    res = [ None ] * Len
    index = 0
    i = 0
    s = [ ]
    s.append ( 0 )
    while ( i < Len ) :
        if ( Str [ i ] == '+' ) :
            if ( s [ - 1 ] == 1 ) :
                res [ index ] = '-'
                index += 1
            if ( s [ - 1 ] == 0 ) :
                res [ index ] = '+'
                index += 1
        elif ( Str [ i ] == '-' ) :
            if ( s [ - 1 ] == 1 ) :
                res [ index ] = '+'
                index += 1
            elif ( s [ - 1 ] == 0 ) :
                res [ index ] = '-'
                index += 1
        elif ( Str [ i ] == '(' and i > 0 ) :
            if ( Str [ i - 1 ] == '-' ) :
                x = 0 if ( s [ - 1 ] == 1 ) else 1
                s.append ( x )
            elif ( Str [ i - 1 ] == '+' ) :
                s.append ( s [ - 1 ] )
        elif ( Str [ i ] == ')' ) :
            s.pop ( )
        else :
            res [ index ] = Str [ i ]
            index += 1
        i += 1
    return res
|||

FIND_NUMBER_PERFECT_SQUARES_TWO_GIVEN_NUMBERS

def CountSquares ( a , b ) :
    cnt = 0
    for i in range ( a , b + 1 ) :
        j = 1 
        while j * j <= i :
            if j * j == i :
                cnt = cnt + 1
            j = j + 1
        i = i + 1
    return cnt
|||

K_NUMBERS_DIFFERENCE_MAXIMUM_MINIMUM_K_NUMBER_MINIMIZED

def minDiff ( arr , n , k ) :
    result = + 2147483647
    arr.sort ( )
    for i in range ( n - k + 1 ) :
        result = int ( min ( result , arr [ i + k - 1 ] - arr [ i ] ) )
    return result
|||

CHECK_LARGE_NUMBER_DIVISIBLE_13_NOT

def checkDivisibility ( num ) :
    length = len ( num )
    if ( length == 1 and num [ 0 ] == '0' ) :
        return True
    if ( length % 3 == 1 ) :
        num = str ( num ) + "00"
        length += 2
    elif ( length % 3 == 2 ) :
        num = str ( num ) + "0"
        length += 1
    sum = 0
    p = 1
    for i in range ( length - 1 , - 1 , - 1 ) :
        group = 0
        group += ord ( num [ i ] ) - ord ( '0' )
        i -= 1
        group += ( ord ( num [ i ] ) - ord ( '0' ) ) * 10
        i -= 1
        group += ( ord ( num [ i ] ) - ord ( '0' ) ) * 100
        sum = sum + group * p
        p *= ( - 1 )
    sum = abs ( sum )
    return ( sum % 13 == 0 )
|||

GIVEN_N_X_N_SQUARE_MATRIX_FIND_SUM_SUB_SQUARES_SIZE_K_X_K

def printSumSimple ( mat , k ) :
    if ( k > n ) :
        return
    for i in range ( n - k + 1 ) :
        for j in range ( n - k + 1 ) :
            sum = 0
            for p in range ( i , k + i ) :
                for q in range ( j , k + j ) :
                    sum += mat [ p ] [ q ]
            print ( sum , end = " " )
        print ( )
|||

FIND_THE_POINT_WHERE_MAXIMUM_INTERVALS_OVERLAP_1

def maxOverlap ( start , end ) :
    n = len ( start )
    maxa = max ( start )
    maxb = max ( end )
    maxc = max ( maxa , maxb )
    x = ( maxc + 2 ) * [ 0 ]
    cur = 0 ; idx = 0
    for i in range ( 0 , n ) :
        x [ start [ i ] ] += 1
        x [ end [ i ] + 1 ] -= 1
    maxy = - 1
    for i in range ( 0 , maxc + 1 ) :
        cur += x [ i ]
        if maxy < cur :
            maxy = cur
            idx = i
    print ( "Maximum value is: {0:d}".format ( maxy ) , " at position: {0:d}".format ( idx ) )
|||

MAXIMUM_SUBSEQUENCE_SUM_SUCH_THAT_NO_THREE_ARE_CONSECUTIVE_1

def maxSumWO3Consec ( n ) :
    if ( sum [ n ] != - 1 ) :
        return sum [ n ]
    if ( n == 0 ) :
        sum [ n ] = 0
        return sum [ n ]
    if ( n == 1 ) :
        sum [ n ] = arr [ 0 ]
        return sum [ n ]
    if ( n == 2 ) :
        sum [ n ] = arr [ 1 ] + arr [ 0 ]
        return sum [ n ]
    sum [ n ] = max ( max ( maxSumWO3Consec ( n - 1 ) , maxSumWO3Consec ( n - 2 ) + arr [ n - 1 ] ) , arr [ n - 2 ] + arr [ n - 1 ] + maxSumWO3Consec ( n - 3 ) )
    return sum [ n ]
|||

C_PROGRAM_ADDITION_TWO_MATRICES

def add ( A , B , C ) :
    for i in range ( N ) :
        for j in range ( N ) :
            C [ i ] [ j ] = A [ i ] [ j ] + B [ i ] [ j ]
|||

FIND_MAXIMUM_AVERAGE_SUBARRAY_OF_K_LENGTH_1

def findMaxAverage ( arr , n , k ) :
    if ( k > n ) :
        return - 1
    sum = arr [ 0 ]
    for i in range ( 1 , k ) :
        sum += arr [ i ]
    max_sum = sum
    max_end = k - 1
    for i in range ( k , n ) :
        sum = sum + arr [ i ] - arr [ i - k ]
        if ( sum > max_sum ) :
            max_sum = sum
            max_end = i
    return max_end - k + 1
|||

FIND_CENTER_CIRCLE_USING_ENDPOINTS_DIAMETER

def center ( x1 , x2 , y1 , y2 ) :
    print ( int ( ( x1 + x2 ) / 2 ) , end = "" )
    print ( "," , int ( ( y1 + y2 ) / 2 ) )
|||

TOTAL_NUMBER_OF_NON_DECREASING_NUMBERS_WITH_N_DIGITS

def countNonDecreasing ( n ) :
    dp = [ [ 0 for i in range ( n + 1 ) ] for i in range ( 10 ) ]
    for i in range ( 10 ) :
        dp [ i ] [ 1 ] = 1
    for digit in range ( 10 ) :
        for len in range ( 2 , n + 1 ) :
            for x in range ( digit + 1 ) :
                dp [ digit ] [ len ] += dp [ x ] [ len - 1 ]
    count = 0
    for i in range ( 10 ) :
        count += dp [ i ] [ n ]
    return count
|||

PRINT_REVERSE_STRING_REMOVING_VOWELS

def replaceOriginal ( s , n ) :
    r = [ ' ' ] * n
    for i in range ( n ) :
        r [ i ] = s [ n - 1 - i ]
        if ( s [ i ] != 'a' and s [ i ] != 'e' and s [ i ] != 'i' and s [ i ] != 'o' and s [ i ] != 'u' ) :
            print ( r [ i ] , end = "" )
    print ( )
|||

FIND_ELEMENTS_PRESENT_FIRST_ARRAY_NOT_SECOND_1

def findMissing ( a , b , n , m ) :
    s = dict ( )
    for i in range ( m ) :
        s [ b [ i ] ] = 1
    for i in range ( n ) :
        if a [ i ] not in s.keys ( ) :
            print ( a [ i ] , end = " " )
|||

COUNT_STRINGS_CAN_FORMED_USING_B_C_GIVEN_CONSTRAINTS

def countStr ( n , bCount , cCount ) :
    if ( bCount < 0 or cCount < 0 ) :
        return 0
    if ( n == 0 ) :
        return 1
    if ( bCount == 0 and cCount == 0 ) :
        return 1
    res = countStr ( n - 1 , bCount , cCount )
    res += countStr ( n - 1 , bCount - 1 , cCount )
    res += countStr ( n - 1 , bCount , cCount - 1 )
    return res
|||

GOLD_MINE_PROBLEM

def getMaxGold ( gold , m , n ) :
    goldTable = [ [ 0 for i in range ( n ) ] for j in range ( m ) ]
    for col in range ( n - 1 , - 1 , - 1 ) :
        for row in range ( m ) :
            if ( col == n - 1 ) :
                right = 0
            else :
                right = goldTable [ row ] [ col + 1 ]
            if ( row == 0 or col == n - 1 ) :
                right_up = 0
            else :
                right_up = goldTable [ row - 1 ] [ col + 1 ]
            if ( row == m - 1 or col == n - 1 ) :
                right_down = 0
            else :
                right_down = goldTable [ row + 1 ] [ col + 1 ]
            goldTable [ row ] [ col ] = gold [ row ] [ col ] + max ( right , right_up , right_down )
    res = goldTable [ 0 ] [ 0 ]
    for i in range ( 1 , m ) :
        res = max ( res , goldTable [ i ] [ 0 ] )
    return res
|||

COUNT_WAYS_BUILD_STREET_GIVEN_CONSTRAINTS

def countWays ( n ) :
    dp = [ [ 0 ] * ( n + 1 ) for i in range ( 2 ) ]
    dp [ 0 ] [ 1 ] = 1
    dp [ 1 ] [ 1 ] = 2
    for i in range ( 2 , n + 1 ) :
        dp [ 0 ] [ i ] = dp [ 0 ] [ i - 1 ] + dp [ 1 ] [ i - 1 ]
        dp [ 1 ] [ i ] = ( dp [ 0 ] [ i - 1 ] * 2 + dp [ 1 ] [ i - 1 ] )
    return dp [ 0 ] [ n ] + dp [ 1 ] [ n ]
|||

RETURN_A_PAIR_WITH_MAXIMUM_PRODUCT_IN_ARRAY_OF_INTEGERS_1

def maxProduct ( arr , n ) :
    if ( n < 2 ) :
        print ( "No pairs exists" )
        return
    if ( n == 2 ) :
        print ( arr [ 0 ] , " " , arr [ 1 ] )
        return
    posa = 0
    posb = 0
    nega = 0
    negb = 0
    for i in range ( n ) :
        if ( arr [ i ] > posa ) :
            posb = posa
            posa = arr [ i ]
        elif ( arr [ i ] > posb ) :
            posb = arr [ i ]
        if ( arr [ i ] < 0 and abs ( arr [ i ] ) > abs ( nega ) ) :
            negb = nega
            nega = arr [ i ]
        elif ( arr [ i ] < 0 and abs ( arr [ i ] ) > abs ( negb ) ) :
            negb = arr [ i ]
    if ( nega * negb > posa * posb ) :
        print ( "Max product pair is {" , nega , ", " , negb , "}" )
    else :
        print ( "Max product pair is {" , posa , ", " , posb , "}" )
|||

POSITION_OF_RIGHTMOST_SET_BIT

def getFirstSetBitPos ( n ) :
    return math.log2 ( n & - n ) + 1
|||

LONGEST_SUBSEQUENCE_WHERE_EVERY_CHARACTER_APPEARS_AT_LEAST_K_TIMES

def longestSubseqWithK ( str , k ) :
    n = len ( str )
    freq = [ 0 ] * MAX_CHARS
    for i in range ( n ) :
        freq [ ord ( str [ i ] ) - ord ( 'a' ) ] += 1
    for i in range ( n ) :
        if ( freq [ ord ( str [ i ] ) - ord ( 'a' ) ] >= k ) :
            print ( str [ i ] , end = "" )
|||

POSSIBLE_TO_MAKE_A_DIVISIBLE_BY_3_NUMBER_USING_ALL_DIGITS_IN_AN_ARRAY

def isPossibleToMakeDivisible ( arr , n ) :
    remainder = 0
    for i in range ( 0 , n ) :
        remainder = ( remainder + arr [ i ] ) % 3
    return ( remainder == 0 )
|||

AREA_SQUARE_CIRCUMSCRIBED_CIRCLE

def find_Area ( r ) :
    return ( 2 * r * r )
|||

FIND_MAXIMUM_DOT_PRODUCT_TWO_ARRAYS_INSERTION_0S

def MaxDotProduct ( A , B , m , n ) :
    dp = [ [ 0 for i in range ( m + 1 ) ] for j in range ( n + 1 ) ]
    for i in range ( 1 , n + 1 , 1 ) :
        for j in range ( i , m + 1 , 1 ) :
            dp [ i ] [ j ] = max ( ( dp [ i - 1 ] [ j - 1 ] + ( A [ j - 1 ] * B [ i - 1 ] ) ) , dp [ i ] [ j - 1 ] )
    return dp [ n ] [ m ]
|||

FIND_DISTINCT_SUBSET_SUBSEQUENCE_SUMS_ARRAY

def printDistSum ( arr , n ) :
    Sum = sum ( arr )
    dp = [ [ False for i in range ( Sum + 1 ) ] for i in range ( n + 1 ) ]
    for i in range ( n + 1 ) :
        dp [ i ] [ 0 ] = True
    for i in range ( 1 , n + 1 ) :
        dp [ i ] [ arr [ i - 1 ] ] = True
        for j in range ( 1 , Sum + 1 ) :
            if ( dp [ i - 1 ] [ j ] == True ) :
                dp [ i ] [ j ] = True
                dp [ i ] [ j + arr [ i - 1 ] ] = True
    for j in range ( Sum + 1 ) :
        if ( dp [ n ] [ j ] == True ) :
            print ( j , end = " " )
|||

SPLIT_NUMERIC_ALPHABETIC_AND_SPECIAL_SYMBOLS_FROM_A_STRING

def splitString ( str ) :
    alpha = ""
    num = ""
    special = ""
    for i in range ( len ( str ) ) :
        if ( str [ i ].isdigit ( ) ) :
            num = num + str [ i ]
        elif ( ( str [ i ] >= 'A' and str [ i ] <= 'Z' ) or ( str [ i ] >= 'a' and str [ i ] <= 'z' ) ) :
            alpha += str [ i ]
        else :
            special += str [ i ]
    print ( alpha )
    print ( num )
    print ( special )
|||

MAXIMUM_SUM_ALTERNATING_SUBSEQUENCE_SUM

def maxAlternateSum ( arr , n ) :
    if ( n == 1 ) :
        return arr [ 0 ]
    dec = [ 0 for i in range ( n + 1 ) ]
    inc = [ 0 for i in range ( n + 1 ) ]
    dec [ 0 ] = inc [ 0 ] = arr [ 0 ]
    flag = 0
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if ( arr [ j ] > arr [ i ] ) :
                dec [ i ] = max ( dec [ i ] , inc [ j ] + arr [ i ] )
                flag = 1
            elif ( arr [ j ] < arr [ i ] and flag == 1 ) :
                inc [ i ] = max ( inc [ i ] , dec [ j ] + arr [ i ] )
    result = - 2147483648
    for i in range ( n ) :
        if ( result < inc [ i ] ) :
            result = inc [ i ]
        if ( result < dec [ i ] ) :
            result = dec [ i ]
    return result
|||

FIND_PAIR_MAXIMUM_GCD_ARRAY

def findMaxGCD ( arr , n ) :
    high = 0
    i = 0
    while i < n :
        high = max ( high , arr [ i ] )
        i = i + 1
    divisors = [ 0 ] * ( high + 1 )
    i = 0
    while i < n :
        j = 1
        while j <= math.sqrt ( arr [ i ] ) :
            if ( arr [ i ] % j == 0 ) :
                divisors [ j ] = divisors [ j ] + 1
                if ( j != arr [ i ] / j ) :
                    divisors [ arr [ i ] / j ] = divisors [ arr [ i ] / j ]
                        + 1
            j = j + 1
        i = i + 1
    i = high
    while i >= 1 :
        if ( divisors [ i ] > 1 ) :
            return i
        i = i - 1
    return 1
|||

FIND_MINIMUM_NUMBER_OF_COINS_THAT_MAKE_A_CHANGE_1

def minCoins ( coins , m , V ) :
    table = [ 0 for i in range ( V + 1 ) ]
    table [ 0 ] = 0
    for i in range ( 1 , V + 1 ) :
        table [ i ] = sys.maxsize
    for i in range ( 1 , V + 1 ) :
        for j in range ( m ) :
            if ( coins [ j ] <= i ) :
                sub_res = table [ i - coins [ j ] ]
                if ( sub_res != sys.maxsize and sub_res + 1 < table [ i ] ) :
                    table [ i ] = sub_res + 1
    return table [ V ]
|||

SUM_NODES_K_TH_LEVEL_TREE_REPRESENTED_STRING

def sumAtKthLevel ( tree , k ) :
    level = - 1
    sum = 0
    n = len ( tree )
    for i in range ( n ) :
        if ( tree [ i ] == '(' ) :
            level += 1
        elif ( tree [ i ] == ')' ) :
            level -= 1
        else :
            if ( level == k ) :
                sum += ( ord ( tree [ i ] ) - ord ( '0' ) )
    return sum
|||

DYNAMIC_PROGRAMMING_SET_4_LONGEST_COMMON_SUBSEQUENCE

def lcs ( X , Y , m , n ) :
    if m == 0 or n == 0 :
        return 0 
    elif X [ m - 1 ] == Y [ n - 1 ] :
        return 1 + lcs ( X , Y , m - 1 , n - 1 ) 
    else :
        return max ( lcs ( X , Y , m , n - 1 ) , lcs ( X , Y , m - 1 , n ) ) 
|||

CHECK_GIVEN_SENTENCE_GIVEN_SET_SIMPLE_GRAMMER_RULES

def checkSentence ( string ) :
    length = len ( string )
    if string [ 0 ] < 'A' or string [ 0 ] > 'Z' :
        return False
    if string [ length - 1 ] != '.' :
        return False
    prev_state = 0
    curr_state = 0
    index = 1
    while ( string [ index ] ) :
        if string [ index ] >= 'A' and string [ index ] <= 'Z' :
            curr_state = 0
        elif string [ index ] == ' ' :
            curr_state = 1
        elif string [ index ] >= 'a' and string [ index ] <= 'z' :
            curr_state = 2
        elif string [ index ] == '.' :
            curr_state = 3
        if prev_state == curr_state and curr_state != 2 :
            return False
        if prev_state == 2 and curr_state == 0 :
            return False
        if curr_state == 3 and prev_state != 1 :
            return True
        index += 1
        prev_state = curr_state
    return False
|||

CHECK_DIVISIBILITY_LARGE_NUMBER_999

def isDivisible999 ( num ) :
    n = len ( num ) 
    if ( n == 0 or num [ 0 ] == '0' ) :
        return true
    if ( ( n % 3 ) == 1 ) :
        num = "00" + num
    if ( ( n % 3 ) == 2 ) :
        num = "0" + num
    gSum = 0
    for i in range ( 0 , n , 3 ) :
        group = 0
        group += ( ord ( num [ i ] ) - 48 ) * 100
        group += ( ord ( num [ i + 1 ] ) - 48 ) * 10
        group += ( ord ( num [ i + 2 ] ) - 48 )
        gSum += group
    if ( gSum > 1000 ) :
        num = str ( gSum )
        n = len ( num )
        gSum = isDivisible999 ( num )
    return ( gSum == 999 )
|||

CHECK_LARGE_NUMBER_DIVISIBLE_9_NOT

def check ( st ) :
    n = len ( st )
    digitSum = 0
    for i in range ( 0 , n ) :
        digitSum = digitSum + ( int ) ( st [ i ] )
    return ( digitSum % 9 == 0 )
|||

NUMBER_OF_BINARY_TREES_FOR_GIVEN_PREORDER_SEQUENCE_LENGTH

def countTrees ( n ) :
    BT = [ 0 ] * ( n + 1 )
    BT [ 0 ] = BT [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        for j in range ( i ) :
            BT [ i ] += BT [ j ] * BT [ i - j - 1 ]
    return BT [ n ]
|||

PROGRAM_SWAP_UPPER_DIAGONAL_ELEMENTS_LOWER_DIAGONAL_ELEMENTS_MATRIX

def swapUpperToLower ( arr ) :
    n = 4 
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            temp = arr [ i ] [ j ] 
            arr [ i ] [ j ] = arr [ j ] [ i ] 
            arr [ j ] [ i ] = temp 
    for i in range ( 0 , n ) :
        for j in range ( 0 , n ) :
            print ( arr [ i ] [ j ] , end = " " ) 
        print ( " " ) 
|||

FIND_SUM_MODULO_K_FIRST_N_NATURAL_NUMBER_1

def findSum ( N , K ) :
    ans = 0 
    y = N / K 
    x = N % K 
    ans = ( ( K * ( K - 1 ) / 2 ) * y + ( x * ( x + 1 ) ) / 2 ) 
    return int ( ans ) 
|||

WAYS_REMOVE_ONE_ELEMENT_BINARY_STRING_XOR_BECOMES_ZERO

def xorZero ( str ) :
    one_count = 0
    zero_count = 0
    n = len ( str )
    for i in range ( 0 , n , 1 ) :
        if ( str [ i ] == '1' ) :
            one_count += 1
        else :
            zero_count += 1
    if ( one_count % 2 == 0 ) :
        return zero_count
    return one_count
|||

DYNAMIC_PROGRAMMING_SET_7_COIN_CHANGE

def count ( S , m , n ) :
    if ( n == 0 ) :
        return 1
    if ( n < 0 ) :
        return 0 
    if ( m <= 0 and n >= 1 ) :
        return 0
    return count ( S , m - 1 , n ) + count ( S , m , n - S [ m - 1 ] ) 
|||

MINIMUM_SUM_SUBSEQUENCE_LEAST_ONE_EVERY_FOUR_CONSECUTIVE_ELEMENTS_PICKED

def minSum ( arr , n ) :
    dp = [ 0 ] * n
    if ( n == 1 ) :
        return arr [ 0 ]
    if ( n == 2 ) :
        return min ( arr [ 0 ] , arr [ 1 ] )
    if ( n == 3 ) :
        return min ( arr [ 0 ] , min ( arr [ 1 ] , arr [ 2 ] ) )
    if ( n == 4 ) :
        return min ( min ( arr [ 0 ] , arr [ 1 ] ) , min ( arr [ 2 ] , arr [ 3 ] ) )
    dp [ 0 ] = arr [ 0 ]
    dp [ 1 ] = arr [ 1 ]
    dp [ 2 ] = arr [ 2 ]
    dp [ 3 ] = arr [ 3 ]
    for i in range ( 4 , n ) :
        dp [ i ] = arr [ i ] + min ( min ( dp [ i - 1 ] , dp [ i - 2 ] ) , min ( dp [ i - 3 ] , dp [ i - 4 ] ) )
    return min ( min ( dp [ n - 1 ] , dp [ n - 2 ] ) , min ( dp [ n - 4 ] , dp [ n - 3 ] ) )
|||

MAXIMUM_PATH_SUM_TRIANGLE

def maxPathSum ( tri , m , n ) :
    for i in range ( m - 1 , - 1 , - 1 ) :
        for j in range ( i + 1 ) :
            if ( tri [ i + 1 ] [ j ] > tri [ i + 1 ] [ j + 1 ] ) :
                tri [ i ] [ j ] += tri [ i + 1 ] [ j ]
            else :
                tri [ i ] [ j ] += tri [ i + 1 ] [ j + 1 ]
    return tri [ 0 ] [ 0 ]
|||

FIND_THREE_ELEMENT_FROM_DIFFERENT_THREE_ARRAYS_SUCH_THAT_THAT_A_B_C_K

def findTriplet ( a1 , a2 , a3 , n1 , n2 , n3 , sum ) :
    for i in range ( 0 , n1 ) :
        for j in range ( 0 , n2 ) :
            for k in range ( 0 , n3 ) :
                if ( a1 [ i ] + a2 [ j ] + a3 [ k ] == sum ) :
                    return True
    return False
|||

TAIL_RECURSION_FIBONACCI

def fib ( n , a = 0 , b = 1 ) :
    if n == 0 :
        return a
    if n == 1 :
        return b
    return fib ( n - 1 , b , a + b ) 
|||

PROGRAM_TO_CHECK_IF_A_GIVEN_NUMBER_IS_LUCKY_ALL_DIGITS_ARE_DIFFERENT

def isLucky ( n ) :
    ar = [ 0 ] * 10
    while ( n > 0 ) :
        digit = math.floor ( n % 10 )
        if ( ar [ digit ] ) :
            return 0
        ar [ digit ] = 1
        n = n / 10
    return 1
|||

GIVEN_N_X_N_SQUARE_MATRIX_FIND_SUM_SUB_SQUARES_SIZE_K_X_K_1

def printSumTricky ( mat , k ) :
    global n
    if k > n :
        return
    stripSum = [ [ None ] * n for i in range ( n ) ]
    for j in range ( n ) :
        Sum = 0
        for i in range ( k ) :
            Sum += mat [ i ] [ j ]
        stripSum [ 0 ] [ j ] = Sum
        for i in range ( 1 , n - k + 1 ) :
            Sum += ( mat [ i + k - 1 ] [ j ] - mat [ i - 1 ] [ j ] )
            stripSum [ i ] [ j ] = Sum
    for i in range ( n - k + 1 ) :
        Sum = 0
        for j in range ( k ) :
            Sum += stripSum [ i ] [ j ]
        print ( Sum , end = " " )
        for j in range ( 1 , n - k + 1 ) :
            Sum += ( stripSum [ i ] [ j + k - 1 ] - stripSum [ i ] [ j - 1 ] )
            print ( Sum , end = " " )
        print ( )
|||

SCHEDULE_ELEVATOR_TO_REDUCE_THE_TOTAL_TIME_TAKEN

def minTime ( n , k , a ) :
    a.sort ( reverse = True ) 
    minTime = 0 
    for i in range ( 0 , n , k ) :
        minTime += ( 2 * a [ i ] ) 
    return minTime 
|||

ODD_EVEN_SORT_BRICK_SORT

def oddEvenSort ( arr , n ) :
    isSorted = 0
    while isSorted == 0 :
        isSorted = 1
        temp = 0
        for i in range ( 1 , n - 1 , 2 ) :
            if arr [ i ] > arr [ i + 1 ] :
                arr [ i ] , arr [ i + 1 ] = arr [ i + 1 ] , arr [ i ]
                isSorted = 0
        for i in range ( 0 , n - 1 , 2 ) :
            if arr [ i ] > arr [ i + 1 ] :
                arr [ i ] , arr [ i + 1 ] = arr [ i + 1 ] , arr [ i ]
                isSorted = 0
    return
|||

RETURN_MAXIMUM_OCCURRING_CHARACTER_IN_THE_INPUT_STRING

def getMaxOccuringChar ( str ) :
    count = [ 0 ] * ASCII_SIZE
    max = - 1
    c = ''
    for i in str :
        count [ ord ( i ) ] += 1 
    for i in str :
        if max < count [ ord ( i ) ] :
            max = count [ ord ( i ) ]
            c = i
    return c
|||

COUNT_NUMBER_PAIRS_N_B_N_GCD_B_B

def CountPairs ( n ) :
    k = n
    imin = 1
    ans = 0
    while ( imin <= n ) :
        imax = n / k
        ans += k * ( imax - imin + 1 )
        imin = imax + 1
        k = n / imin
    return ans
|||

K_TH_DISTINCT_OR_NON_REPEATING_ELEMENT_IN_AN_ARRAY_1

def printKDistinct ( arr , size , KthIndex ) :
    dict = { }
    vect = [ ]
    for i in range ( size ) :
        if ( arr [ i ] in dict ) :
            dict [ arr [ i ] ] = dict [ arr [ i ] ] + 1
        else :
            dict [ arr [ i ] ] = 1
    for i in range ( size ) :
        if ( dict [ arr [ i ] ] > 1 ) :
            continue
        else :
            KthIndex = KthIndex - 1
        if ( KthIndex == 0 ) :
            return arr [ i ]
    return - 1
|||

GENERATE_BINARY_PERMUTATIONS_1S_0S_EVERY_POINT_PERMUTATIONS

def generate ( ones , zeroes , str , len1 ) :
    if ( len1 == len ( str ) ) :
        print ( str , end = " " )
        return
    generate ( ones + 1 , zeroes , str + "1" , len1 )
    if ( ones > zeroes ) :
        generate ( ones , zeroes + 1 , str + "0" , len1 )
|||

SEARCH_INSERT_AND_DELETE_IN_AN_UNSORTED_ARRAY

def findElement ( arr , n , key ) :
    for i in range ( n ) :
        if ( arr [ i ] == key ) :
            return i
    return - 1
|||

LCS_LONGEST_COMMON_SUBSEQUENCE_THREE_STRINGS

def lcsOf3 ( X , Y , Z , m , n , o ) :
    L = [ [ [ 0 for i in range ( o + 1 ) ] for j in range ( n + 1 ) ] for k in range ( m + 1 ) ]
    for i in range ( m + 1 ) :
        for j in range ( n + 1 ) :
            for k in range ( o + 1 ) :
                if ( i == 0 or j == 0 or k == 0 ) :
                    L [ i ] [ j ] [ k ] = 0
                elif ( X [ i - 1 ] == Y [ j - 1 ] and X [ i - 1 ] == Z [ k - 1 ] ) :
                    L [ i ] [ j ] [ k ] = L [ i - 1 ] [ j - 1 ] [ k - 1 ] + 1
                else :
                    L [ i ] [ j ] [ k ] = max ( max ( L [ i - 1 ] [ j ] [ k ] , L [ i ] [ j - 1 ] [ k ] ) , L [ i ] [ j ] [ k - 1 ] )
    return L [ m ] [ n ] [ o ]
|||

MAXIMUM_SUM_SUBARRAY_REMOVING_ONE_ELEMENT

def maxSumSubarrayRemovingOneEle ( arr , n ) :
    fw = [ 0 for k in range ( n ) ]
    bw = [ 0 for k in range ( n ) ]
    cur_max , max_so_far = arr [ 0 ] , arr [ 0 ]
    for i in range ( n ) :
        cur_max = max ( arr [ i ] , cur_max + arr [ i ] )
        max_so_far = max ( max_so_far , cur_max )
        fw [ i ] = cur_max
    cur_max = max_so_far = bw [ n - 1 ] = arr [ n - 1 ]
    i = n - 2
    while i >= 0 :
        cur_max = max ( arr [ i ] , cur_max + arr [ i ] )
        max_so_far = max ( max_so_far , cur_max )
        bw [ i ] = cur_max
        i -= 1
    fans = max_so_far
    for i in range ( 1 , n - 1 ) :
        fans = max ( fans , fw [ i - 1 ] + bw [ i + 1 ] )
    return fans
|||

COUNT_NUMBER_WAYS_TILE_FLOOR_SIZE_N_X_M_USING_1_X_M_SIZE_TILES

def countWays ( n , m ) :
    count = [ ]
    for i in range ( n + 2 ) :
        count.append ( 0 )
    count [ 0 ] = 0
    for i in range ( 1 , n + 1 ) :
        if ( i > m ) :
            count [ i ] = count [ i - 1 ] + count [ i - m ]
        elif ( i < m ) :
            count [ i ] = 1
        else :
            count [ i ] = 2
    return count [ n ]
|||

MIDDLE_OF_THREE_USING_MINIMUM_COMPARISONS

def middleOfThree ( a , b , c ) :
    if ( ( a < b and b < c ) or ( c < b and b < a ) ) :
        return b 
    if ( ( b < a and a < c ) or ( c < a and a < b ) ) :
        return a 
    else :
        return c
|||

LONGEST_COMMON_INCREASING_SUBSEQUENCE_LCS_LIS

def LCIS ( arr1 , n , arr2 , m ) :
    table = [ 0 ] * m
    for j in range ( m ) :
        table [ j ] = 0
    for i in range ( n ) :
        current = 0
        for j in range ( m ) :
            if ( arr1 [ i ] == arr2 [ j ] ) :
                if ( current + 1 > table [ j ] ) :
                    table [ j ] = current + 1
            if ( arr1 [ i ] > arr2 [ j ] ) :
                if ( table [ j ] > current ) :
                    current = table [ j ]
    result = 0
    for i in range ( m ) :
        if ( table [ i ] > result ) :
            result = table [ i ]
    return result
|||

MAXIMUM_SUBSEQUENCE_SUM_SUCH_THAT_NO_THREE_ARE_CONSECUTIVE

def maxSumWO3Consec ( arr , n ) :
    sum = [ 0 for k in range ( n ) ]
    if n >= 1 :
        sum [ 0 ] = arr [ 0 ]
    if n >= 2 :
        sum [ 1 ] = arr [ 0 ] + arr [ 1 ]
    if n > 2 :
        sum [ 2 ] = max ( sum [ 1 ] , max ( arr [ 1 ] + arr [ 2 ] , arr [ 0 ] + arr [ 2 ] ) )
    for i in range ( 3 , n ) :
        sum [ i ] = max ( max ( sum [ i - 1 ] , sum [ i - 2 ] + arr [ i ] ) , arr [ i ] + arr [ i - 1 ] + sum [ i - 3 ] )
    return sum [ n - 1 ]
|||

EULERIAN_NUMBER_1

def eulerian ( n , m ) :
    dp = [ [ 0 for x in range ( m + 1 ) ] for y in range ( n + 1 ) ]
    for i in range ( 1 , n + 1 ) :
        for j in range ( 0 , m + 1 ) :
            if ( i > j ) :
                if ( j == 0 ) :
                    dp [ i ] [ j ] = 1
                else :
                    dp [ i ] [ j ] = ( ( ( i - j ) * dp [ i - 1 ] [ j - 1 ] ) + ( ( j + 1 ) * dp [ i - 1 ] [ j ] ) )
    return dp [ n ] [ m ]
|||

DOUBLE_FACTORIAL

def doublefactorial ( n ) :
    if ( n == 0 or n == 1 ) :
        return 1 
    return n * doublefactorial ( n - 2 ) 
|||

REARRANGE_POSITIVE_AND_NEGATIVE_NUMBERS_PUBLISH

def rearrange ( arr , n ) :
    i = - 1
    for j in range ( n ) :
        if ( arr [ j ] < 0 ) :
            i += 1
            arr [ i ] , arr [ j ] = arr [ j ] , arr [ i ]
    pos , neg = i + 1 , 0
    while ( pos < n and neg < pos and arr [ neg ] < 0 ) :
        arr [ neg ] , arr [ pos ] = arr [ pos ] , arr [ neg ]
        pos += 1
        neg += 2
|||

MAXIMIZE_ARRAY_SUN_AFTER_K_NEGATION_OPERATIONS

def maximumSum ( arr , n , k ) :
    for i in range ( 1 , k + 1 ) :
        min = + 2147483647
        index = - 1
        for j in range ( n ) :
            if ( arr [ j ] < min ) :
                min = arr [ j ]
                index = j
        if ( min == 0 ) :
            break
        arr [ index ] = - arr [ index ]
    sum = 0
    for i in range ( n ) :
        sum += arr [ i ]
    return sum
|||

MAXIMUM_SUM_INCREASING_SUBSEQUENCE_FROM_A_PREFIX_AND_A_GIVEN_ELEMENT_AFTER_PREFIX_IS_MUST

def pre_compute ( a , n , index , k ) :
    dp = [ [ 0 for i in range ( n ) ] for i in range ( n ) ]
    for i in range ( n ) :
        if a [ i ] > a [ 0 ] :
            dp [ 0 ] [ i ] = a [ i ] + a [ 0 ]
        else :
            dp [ 0 ] [ i ] = a [ i ]
    for i in range ( 1 , n ) :
        for j in range ( n ) :
            if a [ j ] > a [ i ] and j > i :
                if dp [ i - 1 ] [ i ] + a [ j ] > dp [ i - 1 ] [ j ] :
                    dp [ i ] [ j ] = dp [ i - 1 ] [ i ] + a [ j ]
                else :
                    dp [ i ] [ j ] = dp [ i - 1 ] [ j ]
            else :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j ]
    return dp [ index ] [ k ]
|||

FUNCTION_COPY_STRING_ITERATIVE_RECURSIVE

def myCopy ( s1 , s2 ) :
    for i in range ( len ( s1 ) ) :
        s2 [ i ] = s1 [ i ] 
|||

GIVEN_TWO_STRINGS_FIND_FIRST_STRING_SUBSEQUENCE_SECOND_1

def isSubSequence ( str1 , str2 , m , n ) :
    j = 0
    i = 0
    while j < m and i < n :
        if str1 [ j ] == str2 [ i ] :
            j = j + 1
        i = i + 1
    return j == m
|||

FIND_UNIT_DIGIT_X_RAISED_POWER_Y_1

def unitnumber ( x , y ) :
    x = x % 10
    if y != 0 :
        y = y % 4 + 4
    return ( ( ( int ) ( math.pow ( x , y ) ) ) % 10 )
|||

PROGRAM_NEXT_FIT_ALGORITHM_MEMORY_MANAGEMENT

def NextFit ( blockSize , m , processSize , n ) :
    allocation = [ - 1 ] * n
    j = 0
    for i in range ( n ) :
        while j < m :
            if blockSize [ j ] >= processSize [ i ] :
                allocation [ i ] = j
                blockSize [ j ] -= processSize [ i ]
                break
            j = ( j + 1 ) % m
    print ( "Process No.Process Size Block no." )
    for i in range ( n ) :
        print ( i + 1 , "         " , processSize [ i ] , end = "     " )
        if allocation [ i ] != - 1 :
            print ( allocation [ i ] + 1 )
        else :
            print ( "Not Allocated" )
|||

NOBLE_INTEGERS_IN_AN_ARRAY_COUNT_OF_GREATER_ELEMENTS_IS_EQUAL_TO_VALUE

def nobleInteger ( arr , size ) :
    for i in range ( 0 , size ) :
        count = 0
        for j in range ( 0 , size ) :
            if ( arr [ i ] < arr [ j ] ) :
                count += 1
        if ( count == arr [ i ] ) :
            return arr [ i ]
    return - 1
|||

MINIMUM_FLIP_REQUIRED_MAKE_BINARY_MATRIX_SYMMETRIC

def minimumflip ( mat , n ) :
    transpose = [ [ 0 ] * n ] * n
    for i in range ( n ) :
        for j in range ( n ) :
            transpose [ i ] [ j ] = mat [ j ] [ i ]
    flip = 0
    for i in range ( n ) :
        for j in range ( n ) :
            if transpose [ i ] [ j ] != mat [ i ] [ j ] :
                flip += 1
    return int ( flip / 2 )
|||

SEGREGATE_EVEN_ODD_NUMBERS_SET_3

def arrayEvenAndOdd ( arr , n ) :
    i = - 1
    j = 0
    while ( j != n ) :
        if ( arr [ j ] % 2 == 0 ) :
            i = i + 1
            arr [ i ] , arr [ j ] = arr [ j ] , arr [ i ]
        j = j + 1
    for i in arr :
        print ( str ( i ) + " " , end = '' )
|||

DFS_N_ARY_TREE_ACYCLIC_GRAPH_REPRESENTED_ADJACENCY_LIST

def dfs ( List , node , arrival ) :
    print ( node )
    for i in range ( len ( List [ node ] ) ) :
        if ( List [ node ] [ i ] != arrival ) :
            dfs ( List , List [ node ] [ i ] , node )
|||

HOW_TO_TURN_OFF_A_PARTICULAR_BIT_IN_A_NUMBER

def turnOffK ( n , k ) :
    if ( k <= 0 ) :
        return n
    return ( n & ~ ( 1 << ( k - 1 ) ) )
|||

NUMBER_SUBSTRINGS_DIVISIBLE_8_NOT_3

def count ( s , Len ) :
    global MAX
    cur = 0
    dig = 0
    Sum = [ 0 ] * MAX
    dp = [ [ 0 , 0 , 0 ] for i in range ( MAX ) ]
    dp [ 0 ] [ 0 ] = 1
    for i in range ( 1 , Len + 1 ) :
        dig = int ( s [ i - 1 ] ) - 48
        cur += dig
        cur %= 3
        Sum [ i ] = cur
        dp [ i ] [ 0 ] = dp [ i - 1 ] [ 0 ]
        dp [ i ] [ 1 ] = dp [ i - 1 ] [ 1 ]
        dp [ i ] [ 2 ] = dp [ i - 1 ] [ 2 ]
        dp [ i ] [ Sum [ i ] ] += 1
    ans = 0
    dprev = 0
    value = 0
    dprev2 = 0
    for i in range ( 1 , Len + 1 ) :
        dig = int ( s [ i - 1 ] ) - 48
        if dig == 8 :
            ans += 1
        if i - 2 >= 0 :
            dprev = int ( s [ i - 2 ] ) - 48
            value = dprev * 10 + dig
            if ( value % 8 == 0 ) and ( value % 3 != 0 ) :
                ans += 1
        if i - 3 >= 0 :
            dprev2 = int ( s [ i - 3 ] ) - 48
            dprev = int ( s [ i - 2 ] ) - 48
            value = ( dprev2 * 100 + dprev * 10 + dig )
            if value % 8 != 0 :
                continue
            ans += ( i - 2 )
            ans -= ( dp [ i - 3 ] [ Sum [ i ] ] )
    return ans
|||

ADD_1_TO_A_GIVEN_NUMBER_1

def addOne ( x ) :
    return ( - ( ~ x ) ) 
|||

CHECK_STRING_FOLLOWS_ANBN_PATTERN_NOT

def isAnBn ( str ) :
    n = len ( str )
    for i in range ( n ) :
        if ( str [ i ] != 'a' ) :
            break
    if ( i * 2 != n ) :
        return False
    for j in range ( i , n ) :
        if ( str [ j ] != 'b' ) :
            return False
    return True
|||

FIND_FIRST_REPEATING_ELEMENT_ARRAY_INTEGERS

def printFirstRepeating ( arr , n ) :
    Min = - 1
    myset = dict ( )
    for i in range ( n - 1 , - 1 , - 1 ) :
        if arr [ i ] in myset.keys ( ) :
            Min = i
        else :
            myset [ arr [ i ] ] = 1
    if ( Min != - 1 ) :
        print ( "The first repeating element is" , arr [ Min ] )
    else :
        print ( "There are no repeating elements" )
|||

COST_BALANCE_PARANTHESES

def costToBalance ( s ) :
    if ( len ( s ) == 0 ) :
        print ( 0 )
    ans = 0
    o = 0
    c = 0
    for i in range ( len ( s ) ) :
        if ( s [ i ] == '(' ) :
            o += 1
        if ( s [ i ] == ')' ) :
            c += 1
    if ( o != c ) :
        return - 1
    a = [ 0 for i in range ( len ( s ) ) ]
    if ( s [ 0 ] == '(' ) :
        a [ 0 ] = 1
    else :
        a [ 0 ] = - 1
    if ( a [ 0 ] < 0 ) :
        ans += abs ( a [ 0 ] )
    for i in range ( 1 , len ( s ) ) :
        if ( s [ i ] == '(' ) :
            a [ i ] = a [ i - 1 ] + 1
        else :
            a [ i ] = a [ i - 1 ] - 1
        if ( a [ i ] < 0 ) :
            ans += abs ( a [ i ] )
    return ans
|||

COIN_GAME_WINNER_EVERY_PLAYER_THREE_CHOICES

def findWinner ( x , y , n ) :
    dp = [ 0 for i in range ( n + 1 ) ]
    dp [ 0 ] = False
    dp [ 1 ] = True
    for i in range ( 2 , n + 1 ) :
        if ( i - 1 >= 0 and not dp [ i - 1 ] ) :
            dp [ i ] = True
        elif ( i - x >= 0 and not dp [ i - x ] ) :
            dp [ i ] = True
        elif ( i - y >= 0 and not dp [ i - y ] ) :
            dp [ i ] = True
        else :
            dp [ i ] = False
    return dp [ n ]
|||

SEQUENCES_GIVEN_LENGTH_EVERY_ELEMENT_EQUAL_TWICE_PREVIOUS

def getTotalNumberOfSequences ( m , n ) :
    if m < n :
        return 0
    if n == 0 :
        return 1
    res = ( getTotalNumberOfSequences ( m - 1 , n ) + getTotalNumberOfSequences ( m // 2 , n - 1 ) )
    return res
|||

FIND_DUPLICATES_GIVEN_ARRAY_ELEMENTS_NOT_LIMITED_RANGE

def printDuplicates ( arr ) :
    dict = { }
    for ele in arr :
        try :
            dict [ ele ] += 1
        except :
            dict [ ele ] = 1
    for item in dict :
        if ( dict [ item ] > 1 ) :
            print ( item , end = " " )
    print ( "\n" )
|||

LONGEST_REPEATING_SUBSEQUENCE_1

def findLongestRepeatingSubSeq ( X , m , n ) :
    if ( dp [ m ] [ n ] != - 1 ) :
        return dp [ m ] [ n ]
    if ( m == 0 or n == 0 ) :
        dp [ m ] [ n ] = 0
        return dp [ m ] [ n ]
    if ( X [ m - 1 ] == X [ n - 1 ] and m != n ) :
        dp [ m ] [ n ] = findLongestRepeatingSubSeq ( X , m - 1 , n - 1 ) + 1
        return dp [ m ] [ n ]
    dp [ m ] [ n ] = max ( findLongestRepeatingSubSeq ( X , m , n - 1 ) , findLongestRepeatingSubSeq ( X , m - 1 , n ) )
    return dp [ m ] [ n ]
|||

COUNT_OF_N_DIGIT_NUMBERS_WHOSE_SUM_OF_DIGITS_EQUALS_TO_GIVEN_SUM

def findCount ( n , sum ) :
    start = math.pow ( 10 , n - 1 ) 
    end = math.pow ( 10 , n ) - 1 
    count = 0 
    i = start 
    while ( i <= end ) :
        cur = 0 
        temp = i 
        while ( temp != 0 ) :
            cur += temp % 10 
            temp = temp // 10 
        if ( cur == sum ) :
            count = count + 1 
            i += 9 
        else :
            i = i + 1 
    print ( count ) 
|||

MINIMUM_COST_CONNECT_WEIGHTED_NODES_REPRESENTED_ARRAY

def minimum_cost ( a , n ) :
    mn = sys.maxsize
    sum = 0
    for i in range ( n ) :
        mn = min ( a [ i ] , mn )
        sum += a [ i ]
    return mn * ( sum - mn )
|||

FIND_ALL_DIVISORS_OF_A_NATURAL_NUMBER_SET_2

def printDivisors ( n ) :
    list = [ ]
    for i in range ( 1 , int ( math.sqrt ( n ) + 1 ) ) :
        if ( n % i == 0 ) :
            if ( n / i == i ) :
                print ( i , end = " " )
            else :
                print ( i , end = " " )
                list.append ( int ( n / i ) )
    for i in list [ : : - 1 ] :
        print ( i , end = " " )
|||

SQUARES_OF_MATRIX_DIAGONAL_ELEMENTS_1

def diagonalsquare ( mat , row , column ) :
    print ( "Diagonal one : " , end = "" )
    for i in range ( 0 , row ) :
        print ( mat [ i ] [ i ] * mat [ i ] [ i ] , end = "" )
    print ( "\n\nDiagonal two : " , end = "" )
    for i in range ( 0 , row ) :
        print ( mat [ i ] [ row - i - 1 ] * mat [ i ] [ row - i - 1 ] , end = "" )
|||

C_PROGRAM_FIND_AREA_TRIANGLE_1

def polygonArea ( X , Y , n ) :
    area = 0.0
    j = n - 1
    for i in range ( 0 , n ) :
        area = area + ( X [ j ] + X [ i ] ) * ( Y [ j ] - Y [ i ] )
        j = i
    return abs ( area // 2.0 )
|||

RANGE_QUERIES_FOR_FREQUENCIES_OF_ARRAY_ELEMENTS

def findFrequency ( arr , n , left , right , element ) :
    count = 0
    for i in range ( left - 1 , right ) :
        if ( arr [ i ] == element ) :
            count += 1
    return count
|||

SERIES_LARGEST_GCD_SUM_EQUALS_N

def print_sequence ( n , k ) :
    b = int ( n / ( k * ( k + 1 ) / 2 ) ) 
    if b == 0 :
        print ( "-1" )
    else :
        r = 1 
        x = 1
        while x ** 2 <= n :
            if n % x != 0 :
                continue 
            elif x <= b and x > r :
                r = x
            elif n / x <= b and n / x > r :
                r = n / x
            x = x + 1
        i = 1
        while i < k :
            print ( r * i , end = " " )
            i = i + 1
        last_term = n - ( r * ( k * ( k - 1 ) / 2 ) )
        print ( last_term )
|||

FIND_THREE_ELEMENT_FROM_DIFFERENT_THREE_ARRAYS_SUCH_THAT_THAT_A_B_C_K_1

def findTriplet ( a1 , a2 , a3 , n1 , n2 , n3 , sum ) :
    s = set ( )
    for i in range ( n1 ) :
        s.add ( a1 [ i ] )
    for i in range ( n2 ) :
        for j in range ( n3 ) :
            if sum - a2 [ i ] - a3 [ j ] in s :
                return True
    return False
|||

FIND_THE_MAXIMUM_ELEMENT_IN_AN_ARRAY_WHICH_IS_FIRST_INCREASING_AND_THEN_DECREASING_1

def findMaximum ( arr , low , high ) :
    if low == high :
        return arr [ low ]
    if high == low + 1 and arr [ low ] >= arr [ high ] :
        return arr [ low ] 
    if high == low + 1 and arr [ low ] < arr [ high ] :
        return arr [ high ]
    mid = ( low + high ) // 2
    if arr [ mid ] > arr [ mid + 1 ] and arr [ mid ] > arr [ mid - 1 ] :
        return arr [ mid ]
    if arr [ mid ] > arr [ mid + 1 ] and arr [ mid ] < arr [ mid - 1 ] :
        return findMaximum ( arr , low , mid - 1 )
    else :
        return findMaximum ( arr , mid + 1 , high )
|||

DYNAMIC_PROGRAMMING_SET_1

def fib ( n , lookup ) :
    if n == 0 or n == 1 :
        lookup [ n ] = n
    if lookup [ n ] is None :
        lookup [ n ] = fib ( n - 1 , lookup ) + fib ( n - 2 , lookup )
    return lookup [ n ]
|||

MODULAR_EXPONENTIATION_POWER_IN_MODULAR_ARITHMETIC

def power ( x , y , p ) :
    res = 1
    x = x % p
    while ( y > 0 ) :
        if ( ( y & 1 ) == 1 ) :
            res = ( res * x ) % p
        y = y >> 1
        x = ( x * x ) % p
    return res
|||

WRITE_ONE_LINE_C_FUNCTION_TO_FIND_WHETHER_A_NO_IS_POWER_OF_TWO_1

def isPowerOfTwo ( x ) :
    return ( x and ( not ( x & ( x - 1 ) ) ) )
|||

LONGEST_COMMON_SUBSEQUENCE_WITH_PERMUTATIONS_ALLOWED

def longestString ( str1 , str2 ) :
    count1 = [ 0 ] * 26
    count2 = [ 0 ] * 26
    for i in range ( len ( str1 ) ) :
        count1 [ ord ( str1 [ i ] ) - ord ( 'a' ) ] += 1
    for i in range ( len ( str2 ) ) :
        count2 [ ord ( str2 [ i ] ) - ord ( 'a' ) ] += 1
    result = ""
    for i in range ( 26 ) :
        for j in range ( 1 , min ( count1 [ i ] , count2 [ i ] ) + 1 ) :
            result = result + chr ( ord ( 'a' ) + i )
    print ( result )
|||

DIFFERENCE_MAXIMUM_SUM_MINIMUM_SUM_N_M_ELEMENTSIN_REVIEW

def find_difference ( arr , n , m ) :
    max = 0 ; min = 0
    arr.sort ( ) 
    j = n - 1
    for i in range ( m ) :
        min += arr [ i ]
        max += arr [ j ]
        j = j - 1
    return ( max - min )
|||

PRINT_NUMBER_ASCENDING_ORDER_CONTAINS_1_2_3_DIGITS

def printNumbers ( numbers ) :
    numbers = map ( str , numbers )
    result = [ ]
    for num in numbers :
        if ( '1' in num and '2' in num and '3' in num ) :
            result.append ( num )
    if not result :
        result = [ '-1' ]
    return sorted ( result ) 
|||

DYNAMIC_PROGRAMMING_SET_3_LONGEST_INCREASING_SUBSEQUENCE

def lis ( arr ) :
    global maximum
    n = len ( arr )
    maximum = 1
    _lis ( arr , n )
    return maximum
|||

MINIMUM_REVOLUTIONS_MOVE_CENTER_CIRCLE_TARGET

def minRevolutions ( r , x1 , y1 , x2 , y2 ) :
    d = math.sqrt ( ( x1 - x2 ) * ( x1 - x2 ) + ( y1 - y2 ) * ( y1 - y2 ) )
    return math.ceil ( d // ( 2 * r ) )
|||

CHECK_TWO_GIVEN_SETS_DISJOINT

def areDisjoint ( set1 , set2 , m , n ) :
    for i in range ( 0 , m ) :
        for j in range ( 0 , n ) :
            if ( set1 [ i ] == set2 [ j ] ) :
                return False
    return True
|||

FIND_MINIMUM_SUM_FACTORS_NUMBER

def findMinSum ( num ) :
    sum = 0
    i = 2
    while ( i * i <= num ) :
        while ( num % i == 0 ) :
            sum += i
            num /= i
        i += 1
    sum += num
    return sum
|||

FREQUENT_ELEMENT_ARRAY

def mostFrequent ( arr , n ) :
    arr.sort ( )
    max_count = 1 ; res = arr [ 0 ] ; curr_count = 1
    for i in range ( 1 , n ) :
        if ( arr [ i ] == arr [ i - 1 ] ) :
            curr_count += 1
        else :
            if ( curr_count > max_count ) :
                max_count = curr_count
                res = arr [ i - 1 ]
            curr_count = 1
    if ( curr_count > max_count ) :
        max_count = curr_count
        res = arr [ n - 1 ]
    return res
|||

MINIMUM_XOR_VALUE_PAIR_1

def minXOR ( arr , n ) :
    arr.sort ( )
    minXor = int ( sys.float_info.max )
    val = 0
    for i in range ( 0 , n - 1 ) :
        val = arr [ i ] ^ arr [ i + 1 ] 
        minXor = min ( minXor , val ) 
    return minXor
|||

MINIMUM_SUM_PRODUCT_TWO_ARRAYS

def minproduct ( a , b , n , k ) :
    diff = 0
    res = 0
    for i in range ( n ) :
        pro = a [ i ] * b [ i ]
        res = res + pro
        if ( pro < 0 and b [ i ] < 0 ) :
            temp = ( a [ i ] + 2 * k ) * b [ i ]
        elif ( pro < 0 and a [ i ] < 0 ) :
            temp = ( a [ i ] - 2 * k ) * b [ i ]
        elif ( pro > 0 and a [ i ] < 0 ) :
            temp = ( a [ i ] + 2 * k ) * b [ i ]
        elif ( pro > 0 and a [ i ] > 0 ) :
            temp = ( a [ i ] - 2 * k ) * b [ i ]
        d = abs ( pro - temp )
        if ( d > diff ) :
            diff = d
    return res - diff
|||

FAST_MULTIPLICATION_METHOD_WITHOUT_USING_MULTIPLICATION_OPERATOR_RUSSIAN_PEASANTS_ALGORITHM

def russianPeasant ( a , b ) :
    res = 0
    while ( b > 0 ) :
        if ( b & 1 ) :
            res = res + a
        a = a << 1
        b = b >> 1
    return res
|||

DIVISIBILITY_9_USING_BITWISE_OPERATORS

def isDivBy9 ( n ) :
    if ( n == 0 or n == 9 ) :
        return True
    if ( n < 9 ) :
        return False
    return isDivBy9 ( ( int ) ( n >> 3 ) - ( int ) ( n & 7 ) )
|||

CHECK_ARRAY_REPRESENTS_INORDER_BINARY_SEARCH_TREE_NOT

def isInorder ( arr , n ) :
    if ( n == 0 or n == 1 ) :
        return True
    for i in range ( 1 , n , 1 ) :
        if ( arr [ i - 1 ] > arr [ i ] ) :
            return False
    return True
|||

GIVEN_TWO_UNSORTED_ARRAYS_FIND_PAIRS_WHOSE_SUM_X

def findPairs ( arr1 , arr2 , n , m , x ) :
    for i in range ( 0 , n ) :
        for j in range ( 0 , m ) :
            if ( arr1 [ i ] + arr2 [ j ] == x ) :
                print ( arr1 [ i ] , arr2 [ j ] )
|||

BINARY_REPRESENTATION_OF_NEXT_NUMBER

def nextGreater ( num1 ) :
    l = len ( num1 ) 
    num = list ( num1 ) 
    i = l - 1 
    while ( i >= 0 ) :
        if ( num [ i ] == '0' ) :
            num [ i ] = '1' 
            break 
        else :
            num [ i ] = '0' 
        i -= 1 
    num1 = ''.join ( num ) 
    if ( i < 0 ) :
        num1 = '1' + num1 
    return num1 
|||

LARGEST_SUBARRAY_WITH_EQUAL_NUMBER_OF_0S_AND_1S

def findSubArray ( arr , n ) :
    sum = 0
    maxsize = - 1
    for i in range ( 0 , n - 1 ) :
        sum = - 1 if ( arr [ i ] == 0 ) else 1
        for j in range ( i + 1 , n ) :
            sum = sum + ( - 1 ) if ( arr [ j ] == 0 ) else sum + 1
            if ( sum == 0 and maxsize < j - i + 1 ) :
                maxsize = j - i + 1
                startindex = i
    if ( maxsize == - 1 ) :
        print ( "No such subarray" ) 
    else :
        print ( startindex , "to" , startindex + maxsize - 1 ) 
    return maxsize
|||

COUNT_PAIRS_WHOSE_PRODUCTS_EXIST_IN_ARRAY_1

def countPairs ( arr , n ) :
    result = 0
    Hash = set ( )
    for i in range ( n ) :
        Hash.add ( arr [ i ] )
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            product = arr [ i ] * arr [ j ]
            if product in ( Hash ) :
                result += 1
    return result
|||

DYNAMIC_PROGRAMMING_SET_12_LONGEST_PALINDROMIC_SUBSEQUENCE

def lps ( str ) :
    n = len ( str )
    L = [ [ 0 for x in range ( n ) ] for x in range ( n ) ]
    for i in range ( n ) :
        L [ i ] [ i ] = 1
    for cl in range ( 2 , n + 1 ) :
        for i in range ( n - cl + 1 ) :
            j = i + cl - 1
            if str [ i ] == str [ j ] and cl == 2 :
                L [ i ] [ j ] = 2
            elif str [ i ] == str [ j ] :
                L [ i ] [ j ] = L [ i + 1 ] [ j - 1 ] + 2
            else :
                L [ i ] [ j ] = max ( L [ i ] [ j - 1 ] , L [ i + 1 ] [ j ] ) 
    return L [ 0 ] [ n - 1 ]
|||

COUNT_INVERSIONS_OF_SIZE_THREE_IN_A_GIVE_ARRAY_1

def getInvCount ( arr , n ) :
    invcount = 0
    for i in range ( 1 , n - 1 ) :
        small = 0
        for j in range ( i + 1 , n ) :
            if ( arr [ i ] > arr [ j ] ) :
                small += 1
        great = 0 
        for j in range ( i - 1 , - 1 , - 1 ) :
            if ( arr [ i ] < arr [ j ] ) :
                great += 1
        invcount += great * small
    return invcount
|||

DECIMAL_REPRESENTATION_GIVEN_BINARY_STRING_DIVISIBLE_10_NOT

def isDivisibleBy10 ( bin ) :
    n = len ( bin )
    if ( bin [ n - 1 ] == '1' ) :
        return False
    sum = 0
    i = n - 2
    while i >= 0 :
        if ( bin [ i ] == '1' ) :
            posFromRight = n - i - 1
            if ( posFromRight % 4 == 1 ) :
                sum = sum + 2
            elif ( posFromRight % 4 == 2 ) :
                sum = sum + 4
            elif ( posFromRight % 4 == 3 ) :
                sum = sum + 8
            elif ( posFromRight % 4 == 0 ) :
                sum = sum + 6
        i = i - 1
    if ( sum % 10 == 0 ) :
        return True
    return False
|||

FIND_WHETHER_AN_ARRAY_IS_SUBSET_OF_ANOTHER_ARRAY_SET_1_1

def isSubset ( arr1 , arr2 , m , n ) :
    i = 0
    j = 0
    if m < n :
        return 0
    arr1.sort ( )
    arr2.sort ( )
    while i < n and j < m :
        if arr1 [ j ] < arr2 [ i ] :
            j += 1
        elif arr1 [ j ] == arr2 [ i ] :
            j += 1
            i += 1
        elif arr1 [ j ] > arr2 [ i ] :
            return 0
    return False if i < n else True
|||

DYNAMIC_PROGRAMMING_SUBSET_SUM_PROBLEM_1

def isSubsetSum ( set , n , sum ) :
    subset = ( [ [ False for i in range ( sum + 1 ) ] for i in range ( n + 1 ) ] )
    for i in range ( n + 1 ) :
        subset [ i ] [ 0 ] = True
        for i in range ( 1 , sum + 1 ) :
            subset [ 0 ] [ i ] = False
        for i in range ( 1 , n + 1 ) :
            for j in range ( 1 , sum + 1 ) :
                if j < set [ i - 1 ] :
                    subset [ i ] [ j ] = subset [ i - 1 ] [ j ]
                if j >= set [ i - 1 ] :
                    subset [ i ] [ j ] = ( subset [ i - 1 ] [ j ] or subset [ i - 1 ] [ j - set [ i - 1 ] ] )
    return subset [ n ] [ sum ]
|||

SUM_K_TH_GROUP_ODD_POSITIVE_NUMBERS_1

def kthgroupsum ( k ) :
    return k * k * k
|||

THIRD_LARGEST_ELEMENT_ARRAY_DISTINCT_ELEMENTS

def thirdLargest ( arr , arr_size ) :
    if ( arr_size < 3 ) :
        print ( " Invalid Input " )
        return
    first = arr [ 0 ]
    for i in range ( 1 , arr_size ) :
        if ( arr [ i ] > first ) :
            first = arr [ i ]
    second = - sys.maxsize
    for i in range ( 0 , arr_size ) :
        if ( arr [ i ] > second and arr [ i ] < first ) :
            second = arr [ i ]
    third = - sys.maxsize
    for i in range ( 0 , arr_size ) :
        if ( arr [ i ] > third and arr [ i ] < second ) :
            third = arr [ i ]
    print ( "The Third Largest" , "element is" , third )
|||

FIND_SUM_NODES_GIVEN_PERFECT_BINARY_TREE_1

def sumNodes ( l ) :
    leafNodeCount = math.pow ( 2 , l - 1 ) 
    sumLastLevel = 0 
    sumLastLevel = ( ( leafNodeCount * ( leafNodeCount + 1 ) ) / 2 ) 
    sum = sumLastLevel * l 
    return int ( sum ) 
|||

MIDDLE_OF_THREE_USING_MINIMUM_COMPARISONS_2

def middleOfThree ( a , b , c ) :
    x = a - b
    y = b - c
    z = a - c
    if x * y > 0 :
        return b
    elif ( x * z > 0 ) :
        return
    else :
        return a
|||

MAXIMUM_TRIPLET_SUM_ARRAY_2

def maxTripletSum ( arr , n ) :
    maxA = - 100000000
    maxB = - 100000000
    maxC = - 100000000
    for i in range ( 0 , n ) :
        if ( arr [ i ] > maxA ) :
            maxC = maxB
            maxB = maxA
            maxA = arr [ i ]
        elif ( arr [ i ] > maxB ) :
            maxC = maxB
            maxB = arr [ i ]
        elif ( arr [ i ] > maxC ) :
            maxC = arr [ i ]
    return ( maxA + maxB + maxC )
|||

COUNT_PAIRS_TWO_SORTED_ARRAYS_WHOSE_SUM_EQUAL_GIVEN_VALUE_X_1

def countPairs ( arr1 , arr2 , m , n , x ) :
    count = 0
    us = set ( )
    for i in range ( m ) :
        us.add ( arr1 [ i ] )
    for j in range ( n ) :
        if x - arr2 [ j ] in us :
            count += 1
    return count
|||

MINIMUM_STEPS_REACH_END_ARRAY_CONSTRAINTS

def getMinStepToReachEnd ( arr , N ) :
    visit = [ False for i in range ( N ) ]
    distance = [ 0 for i in range ( N ) ]
    digit = [ [ 0 for i in range ( N ) ] for j in range ( 10 ) ]
    for i in range ( 1 , N ) :
        digit [ arr [ i ] ].append ( i )
    distance [ 0 ] = 0
    visit [ 0 ] = True
    q = [ ]
    q.append ( 0 )
    while ( len ( q ) > 0 ) :
        idx = q [ 0 ]
        q.remove ( q [ 0 ] )
        if ( idx == N - 1 ) :
            break
        d = arr [ idx ]
        for i in range ( len ( digit [ d ] ) ) :
            nextidx = digit [ d ] [ i ]
            if ( visit [ nextidx ] == False ) :
                visit [ nextidx ] = True
                q.append ( nextidx )
                distance [ nextidx ] = distance [ idx ] + 1
        if ( idx - 1 >= 0 and visit [ idx - 1 ] == False ) :
            visit [ idx - 1 ] = True
            q.append ( idx - 1 )
            distance [ idx - 1 ] = distance [ idx ] + 1
        if ( idx + 1 < N and visit [ idx + 1 ] == False ) :
            visit [ idx + 1 ] = True
            q.append ( idx + 1 )
            distance [ idx + 1 ] = distance [ idx ] + 1
    return distance [ N - 1 ]
|||

LEXICOGRAPHICALLY_SMALLEST_ARRAY_K_CONSECUTIVE_SWAPS

def minimizeWithKSwaps ( arr , n , k ) :
    for i in range ( n - 1 ) :
        pos = i
        for j in range ( i + 1 , n ) :
            if ( j - i > k ) :
                break
            if ( arr [ j ] < arr [ pos ] ) :
                pos = j
        for j in range ( pos , i , - 1 ) :
            arr [ j ] , arr [ j - 1 ] = arr [ j - 1 ] , arr [ j ]
        k -= pos - i
|||

CONVERT_SENTENCE_EQUIVALENT_MOBILE_NUMERIC_KEYPAD_SEQUENCE

def printSequence ( arr , input ) :
    n = len ( input )
    output = ""
    for i in range ( n ) :
        if ( input [ i ] == ' ' ) :
            output = output + "0"
        else :
            position = ord ( input [ i ] ) - ord ( 'A' )
            output = output + arr [ position ]
    return output
|||

PROGRAM_CHECK_ARRAY_SORTED_NOT_ITERATIVE_RECURSIVE

def arraySortedOrNot ( arr ) :
    n = len ( arr )
    if n == 1 or n == 0 :
        return True
    return arr [ 0 ] <= arr [ 1 ] and arraySortedOrNot ( arr [ 1 : ] )
|||

CHECK_TWO_GIVEN_CIRCLES_TOUCH_INTERSECT

def circle ( x1 , y1 , x2 , y2 , r1 , r2 ) :
    distSq = ( x1 - x2 ) * ( x1 - x2 ) + ( y1 - y2 ) * ( y1 - y2 ) 
    radSumSq = ( r1 + r2 ) * ( r1 + r2 ) 
    if ( distSq == radSumSq ) :
        return 1
    elif ( distSq > radSumSq ) :
        return - 1
    else :
        return 0
|||

SMALLEST_POWER_OF_2_GREATER_THAN_OR_EQUAL_TO_N_2

def nextPowerOf2 ( n ) :
    n -= 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    n += 1
    return n
|||

PADOVAN_SEQUENCE

def pad ( n ) :
    pPrevPrev , pPrev , pCurr , pNext = 1 , 1 , 1 , 1
    for i in range ( 3 , n + 1 ) :
        pNext = pPrevPrev + pPrev
        pPrevPrev = pPrev
        pPrev = pCurr
        pCurr = pNext
    return pNext 
|||

CHECK_GIVEN_STRING_CAN_SPLIT_FOUR_DISTINCT_STRINGS

def check ( s ) :
    if ( len ( s ) >= 10 ) :
        return True
    for i in range ( 1 , len ( s ) ) :
        for j in range ( i + 1 , len ( s ) ) :
            for k in range ( j + 1 , len ( s ) ) :
                s1 = s [ 0 : i ]
                s2 = s [ i : j - i ]
                s3 = s [ j : k - j ]
                s4 = s [ k : len ( s ) - k ]
                if ( s1 != s2 and s1 != s3 and s1 != s4 and s2 != s3 and s2 != s4 and s3 != s4 ) :
                    return True
    return False
|||

PERMUTE_TWO_ARRAYS_SUM_EVERY_PAIR_GREATER_EQUAL_K

def isPossible ( a , b , n , k ) :
    a.sort ( reverse = True )
    b.sort ( )
    for i in range ( n ) :
        if ( a [ i ] + b [ i ] < k ) :
            return False
    return True
|||

ARRAY_ELEMENT_MOVED_K_USING_SINGLE_MOVES

def winner ( a , n , k ) :
    if k >= n - 1 :
        return n
    best = 0
    times = 0
    for i in range ( n ) :
        if a [ i ] > best :
            best = a [ i ]
            if i == True :
                times = 1
        else :
            times += 1
        if times >= k :
            return best
    return best
|||

DIRECTION_LAST_SQUARE_BLOCK

def direction ( R , C ) :
    if ( R != C and R % 2 == 0 and C % 2 != 0 and R < C ) :
        print ( "Left" )
        return
    if ( R != C and R % 2 == 0 and C % 2 == 0 and R > C ) :
        print ( "Up" )
        return
    if R == C and R % 2 != 0 and C % 2 != 0 :
        print ( "Right" )
        return
    if R == C and R % 2 == 0 and C % 2 == 0 :
        print ( "Left" )
        return
    if ( R != C and R % 2 != 0 and C % 2 != 0 and R < C ) :
        print ( "Right" )
        return
    if ( R != C and R % 2 != 0 and C % 2 != 0 and R > C ) :
        print ( "Down" )
        return
    if ( R != C and R % 2 == 0 and C % 2 != 0 and R < C ) :
        print ( "Left" )
        return
    if ( R != C and R % 2 == 0 and C % 2 == 0 and R > C ) :
        print ( "Up" )
        return
    if ( R != C and R % 2 != 0 and C % 2 != 0 and R > C ) :
        print ( "Down" )
        return
    if ( R != C and R % 2 != 0 and C % 2 != 0 and R < C ) :
        print ( "Right" )
        return
|||

NUMBER_NON_NEGATIVE_INTEGRAL_SOLUTIONS_B_C_N

def countIntegralSolutions ( n ) :
    result = 0
    for i in range ( n + 1 ) :
        for j in range ( n + 1 ) :
            for k in range ( n + 1 ) :
                if i + j + k == n :
                    result += 1
    return result
|||

SWAP_MAJOR_MINOR_DIAGONALS_SQUARE_MATRIX

def swapDiagonal ( matrix ) :
    for i in range ( N ) :
        matrix [ i ] [ i ] , matrix [ i ] [ N - i - 1 ] = \
            matrix [ i ] [ N - i - 1 ] , matrix [ i ] [ i ]
|||

MINIMUM_OPERATIONS_MAKE_GCD_ARRAY_MULTIPLE_K

def MinOperation ( a , n , k ) :
    result = 0
    for i in range ( n ) :
        if ( a [ i ] != 1 and a [ i ] > k ) :
            result = ( result + min ( a [ i ] % k , k - a [ i ] % k ) )
        else :
            result = result + k - a [ i ]
    return result
|||

MAXIMUM_DECIMAL_VALUE_PATH_IN_A_BINARY_MATRIX

def maxDecimalValue ( mat , i , j , p ) :
    if i >= N or j >= N :
        return 0
    result = max ( maxDecimalValue ( mat , i , j + 1 , p + 1 ) , maxDecimalValue ( mat , i + 1 , j , p + 1 ) )
    if mat [ i ] [ j ] == 1 :
        return pow ( 2 , p ) + result
    else :
        return result
|||

SQUARE_ROOT_OF_A_PERFECT_SQUARE_1

def squareRoot ( n ) :
    x = n 
    y = 1 
    while ( x > y ) :
        x = ( x + y ) / 2 
        y = n / x 
    return x 
|||

FIND_MINIMUM_SHIFT_LONGEST_COMMON_PREFIX

def KMP ( m , n , str2 , str1 ) :
    pos = 0
    Len = 0
    p = [ 0 for i in range ( m + 1 ) ]
    k = 0
    for i in range ( 2 , n + 1 ) :
        while ( k > 0 and str1 [ k ] != str1 [ i - 1 ] ) :
            k = p [ k ]
        if ( str1 [ k ] == str1 [ i - 1 ] ) :
            k += 1
        p [ i ] = k
    j = 0
    for i in range ( m ) :
        while ( j > 0 and j < n and str1 [ j ] != str2 [ i ] ) :
            j = p [ j ]
        if ( j < n and str1 [ j ] == str2 [ i ] ) :
            j += 1
        if ( j > Len ) :
            Len = j
            pos = i - j + 1
    print ( "Shift = " , pos )
    print ( "Prefix = " , str1 [ : Len ] )
|||

SORTED_ORDER_PRINTING_OF_AN_ARRAY_THAT_REPRESENTS_A_BST

def printSorted ( arr , start , end ) :
    if start > end :
        return
    printSorted ( arr , start * 2 + 1 , end )
    print ( arr [ start ] , end = " " )
    printSorted ( arr , start * 2 + 2 , end )
|||

CHECK_WHETHER_GIVEN_DEGREES_VERTICES_REPRESENT_GRAPH_TREE

def check ( degree , n ) :
    deg_sum = sum ( degree )
    if ( 2 * ( n - 1 ) == deg_sum ) :
        return True
    else :
        return False
|||

MOVE_ZEROES_END_ARRAY

def pushZerosToEnd ( arr , n ) :
    count = 0
    for i in range ( n ) :
        if arr [ i ] != 0 :
            arr [ count ] = arr [ i ]
            count += 1
    while count < n :
        arr [ count ] = 0
        count += 1
|||

COUNT_ELEMENTS_WHICH_DIVIDE_ALL_NUMBERS_IN_RANGE_L_R

def answerQuery ( a , n , l , r ) :
    count = 0
    l = l - 1
    for i in range ( l , r , 1 ) :
        element = a [ i ]
        divisors = 0
        for j in range ( l , r , 1 ) :
            if ( a [ j ] % a [ i ] == 0 ) :
                divisors += 1
            else :
                break
        if ( divisors == ( r - l ) ) :
            count += 1
    return count
|||

SUM_LARGEST_PRIME_FACTOR_NUMBER_LESS_EQUAL_N

def sumOfLargePrimeFactor ( n ) :
    prime = [ 0 ] * ( n + 1 )
    sum = 0
    max = int ( n / 2 )
    for p in range ( 2 , max + 1 ) :
        if prime [ p ] == 0 :
            for i in range ( p * 2 , n + 1 , p ) :
                prime [ i ] = p
    for p in range ( 2 , n + 1 ) :
        if prime [ p ] :
            sum += prime [ p ]
        else :
            sum += p
    return sum
|||

REARRANGE_A_STRING_IN_SORTED_ORDER_FOLLOWED_BY_THE_INTEGER_SUM

def arrangeString ( string ) :
    char_count = [ 0 ] * MAX_CHAR
    s = 0
    for i in range ( len ( string ) ) :
        if string [ i ] >= "A" and string [ i ] <= "Z" :
            char_count [ ord ( string [ i ] ) - ord ( "A" ) ] += 1
        else :
            s += ord ( string [ i ] ) - ord ( "0" )
    res = ""
    for i in range ( MAX_CHAR ) :
        ch = chr ( ord ( "A" ) + i )
        while char_count [ i ] :
            res += ch
            char_count [ i ] -= 1
    if s > 0 :
        res += str ( s )
    return res
|||

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX_1

def numberOfPaths ( m , n ) :
    count = [ [ 0 for x in range ( m ) ] for y in range ( n ) ]
    for i in range ( m ) :
        count [ i ] [ 0 ] = 1 
    for j in range ( n ) :
        count [ 0 ] [ j ] = 1 
    for i in range ( 1 , m ) :
        for j in range ( n ) :
            count [ i ] [ j ] = count [ i - 1 ] [ j ] + count [ i ] [ j - 1 ]
    return count [ m - 1 ] [ n - 1 ]
|||

DYNAMIC_PROGRAMMING_SET_5_EDIT_DISTANCE_1

def editDistDP ( str1 , str2 , m , n ) :
    dp = [ [ 0 for x in range ( n + 1 ) ] for x in range ( m + 1 ) ]
    for i in range ( m + 1 ) :
        for j in range ( n + 1 ) :
            if i == 0 :
                dp [ i ] [ j ] = j
            elif j == 0 :
                dp [ i ] [ j ] = i
            elif str1 [ i - 1 ] == str2 [ j - 1 ] :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j - 1 ]
            else :
                dp [ i ] [ j ] = 1 + min ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] , dp [ i - 1 ] [ j - 1 ] )
    return dp [ m ] [ n ]
|||

FIND_NUMBER_OF_SOLUTIONS_OF_A_LINEAR_EQUATION_OF_N_VARIABLES

def countSol ( coeff , start , end , rhs ) :
    if ( rhs == 0 ) :
        return 1
    result = 0
    for i in range ( start , end + 1 ) :
        if ( coeff [ i ] <= rhs ) :
            result += countSol ( coeff , i , end , rhs - coeff [ i ] )
    return result
|||

SUM_ELEMENTS_K1TH_K2TH_SMALLEST_ELEMENTS_1

def minheapify ( a , index ) :
    small = index
    l = 2 * index + 1
    r = 2 * index + 2
    if ( l < n and a [ l ] < a [ small ] ) :
        small = l
    if ( r < n and a [ r ] < a [ small ] ) :
        small = r
    if ( small != index ) :
        ( a [ small ] , a [ index ] ) = ( a [ index ] , a [ small ] )
        minheapify ( a , small )
|||

SEARCHING_FOR_PATTERNS_SET_2_KMP_ALGORITHM

def computeLPSArray ( pat , M , lps ) :
    len = 0
    lps [ 0 ]
    i = 1
    while i < M :
        if pat [ i ] == pat [ len ] :
            len += 1
            lps [ i ] = len
            i += 1
        else :
            if len != 0 :
                len = lps [ len - 1 ]
            else :
                lps [ i ] = 0
                i += 1
|||

FIND_MINIMUM_DIFFERENCE_PAIR

def findMinDiff ( arr , n ) :
    diff = 10 ** 20
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            if abs ( arr [ i ] - arr [ j ] ) < diff :
                diff = abs ( arr [ i ] - arr [ j ] )
    return diff
|||

PRINT_FIRST_K_DIGITS_1N_N_POSITIVE_INTEGER

def Print ( n , k ) :
    rem = 1
    for i in range ( 0 , k ) :
        print ( math.floor ( ( ( 10 * rem ) / n ) ) , end = "" )
        rem = ( 10 * rem ) % n
|||

GROUP_MULTIPLE_OCCURRENCE_OF_ARRAY_ELEMENTS_ORDERED_BY_FIRST_OCCURRENCE

def groupElements ( arr , n ) :
    visited = [ False ] * n
    for i in range ( 0 , n ) :
        visited [ i ] = False
    for i in range ( 0 , n ) :
        if ( visited [ i ] == False ) :
            print ( arr [ i ] , end = " " )
            for j in range ( i + 1 , n ) :
                if ( arr [ i ] == arr [ j ] ) :
                    print ( arr [ i ] , end = " " )
                    visited [ j ] = True
|||

CHECK_WHETHER_ARITHMETIC_PROGRESSION_CAN_FORMED_GIVEN_ARRAY

def checkIsAP ( arr , n ) :
    if ( n == 1 ) : return True
    arr.sort ( )
    d = arr [ 1 ] - arr [ 0 ]
    for i in range ( 2 , n ) :
        if ( arr [ i ] - arr [ i - 1 ] != d ) :
            return False
    return True
|||

NTH_MULTIPLE_NUMBER_FIBONACCI_SERIES

def findPosition ( k , n ) :
    f1 = 0
    f2 = 1
    i = 2 
    while i != 0 :
        f3 = f1 + f2 
        f1 = f2 
        f2 = f3 
        if f2 % k == 0 :
            return n * i
        i += 1
    return
|||

COUNT_PAIRS_DIFFERENCE_EQUAL_K_1

def countPairsWithDiffK ( arr , n , k ) :
    count = 0
    arr.sort ( )
    l = 0
    r = 0
    while r < n :
        if arr [ r ] - arr [ l ] == k :
            count += 1
            l += 1
            r += 1
        elif arr [ r ] - arr [ l ] > k :
            l += 1
        else :
            r += 1
    return count
|||

ELEMENTS_TO_BE_ADDED_SO_THAT_ALL_ELEMENTS_OF_A_RANGE_ARE_PRESENT_IN_ARRAY

def countNum ( arr , n ) :
    count = 0
    arr.sort ( )
    for i in range ( 0 , n - 1 ) :
        if ( arr [ i ] != arr [ i + 1 ] and arr [ i ] != arr [ i + 1 ] - 1 ) :
            count += arr [ i + 1 ] - arr [ i ] - 1 
    return count
|||

MAKE_LARGEST_PALINDROME_CHANGING_K_DIGITS

def maximumPalinUsingKChanges ( strr , k ) :
    palin = strr
    l = 0
    r = len ( strr ) - 1
    while ( l <= r ) :
        if ( strr [ l ] != strr [ r ] ) :
            palin [ l ] = palin [ r ] = max ( strr [ l ] , strr [ r ] )
            k -= 1
        l += 1
        r -= 1
    if ( k < 0 ) :
        return "Not possible"
    l = 0
    r = len ( strr ) - 1
    while ( l <= r ) :
        if ( l == r ) :
            if ( k > 0 ) :
                palin [ l ] = '9'
        if ( palin [ l ] < '9' ) :
            if ( k >= 2 and palin [ l ] == strr [ l ] and palin [ r ] == strr [ r ] ) :
                k -= 1
                palin [ l ] = palin [ r ] = '9'
            elif ( k >= 1 and ( palin [ l ] != strr [ l ] or palin [ r ] != strr [ r ] ) ) :
                k -= 1
                palin [ l ] = palin [ r ] = '9'
        l += 1
        r -= 1
    return palin
|||

SUBARRAYSUBSTRING_VS_SUBSEQUENCE_AND_PROGRAMS_TO_GENERATE_THEM

def subArray ( arr , n ) :
    for i in range ( 0 , n ) :
        for j in range ( i , n ) :
            for k in range ( i , j + 1 ) :
                print ( arr [ k ] , end = "" )
            print ( "\n" , end = "" )
|||

MAXIMUM_SUM_INCREASING_ORDER_ELEMENTS_N_ARRAYS

def maximumSum ( a , n ) :
    global M 
    for i in range ( 0 , n ) :
        a [ i ].sort ( ) 
    sum = a [ n - 1 ] [ M - 1 ] 
    prev = a [ n - 1 ] [ M - 1 ] 
    for i in range ( n - 2 , - 1 , - 1 ) :
        for j in range ( M - 1 , - 1 , - 1 ) :
            if ( a [ i ] [ j ] < prev ) :
                prev = a [ i ] [ j ] 
                sum += prev 
                break 
        if ( j == - 1 ) :
            return 0 
    return sum 
|||

C_PROGRAM_FACTORIAL_NUMBER

def factorial ( n ) :
    return 1 if ( n == 1 or n == 0 ) else n * factorial ( n - 1 ) 
|||

PRINT_SQUARES_FIRST_N_NATURAL_NUMBERS_WITHOUT_USING

def printSquares ( n ) :
    square = 0 ; prev_x = 0 
    for x in range ( 0 , n ) :
        square = ( square + x + prev_x )
        print ( square , end = " " )
        prev_x = x
|||

ROPES_DATA_STRUCTURE_FAST_STRING_CONCATENATION

def concatenate ( a , b , c , n1 , n2 ) :
    i = - 1
    for i in range ( n1 ) :
        c [ i ] = a [ i ]
    for j in range ( n2 ) :
        c [ i ] = b [ j ]
        i += 1
|||

GIVEN_TWO_SORTED_ARRAYS_NUMBER_X_FIND_PAIR_WHOSE_SUM_CLOSEST_X

def printClosest ( ar1 , ar2 , m , n , x ) :
    diff = sys.maxsize
    l = 0
    r = n - 1
    while ( l < m and r >= 0 ) :
        if abs ( ar1 [ l ] + ar2 [ r ] - x ) < diff :
            res_l = l
            res_r = r
            diff = abs ( ar1 [ l ] + ar2 [ r ] - x )
        if ar1 [ l ] + ar2 [ r ] > x :
            r = r - 1
        else :
            l = l + 1
    print ( "The closest pair is [" , ar1 [ res_l ] , "," , ar2 [ res_r ] , "]" )
|||

CONVERT_STRICTLY_INCREASING_ARRAY_MINIMUM_CHANGES

def minRemove ( arr , n ) :
    LIS = [ 0 for i in range ( n ) ]
    len = 0
    for i in range ( n ) :
        LIS [ i ] = 1
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if ( arr [ i ] > arr [ j ] and ( i - j ) <= ( arr [ i ] - arr [ j ] ) ) :
                LIS [ i ] = max ( LIS [ i ] , LIS [ j ] + 1 )
        len = max ( len , LIS [ i ] )
    return ( n - len )
|||

TAIL_RECURSION

def fact ( n ) :
    if ( n == 0 ) :
        return 1
    return n * fact ( n - 1 )
|||

RECURSIVE_FUNCTIONS

def tower ( n , sourcePole , destinationPole , auxiliaryPole ) :
    if ( 0 == n ) :
        return
    tower ( n - 1 , sourcePole , auxiliaryPole , destinationPole )
    print ( "Move the disk" , sourcePole , "from" , sourcePole , "to" , destinationPole )
    tower ( n - 1 , auxiliaryPole , destinationPole , sourcePole )
|||

FIND_X_Y_SATISFYING_AX_N

def solution ( a , b , n ) :
    i = 0
    while i * a <= n :
        if ( n - ( i * a ) ) % b == 0 :
            print ( "x = " , i , ", y = " , int ( ( n - ( i * a ) ) / b ) )
            return 0
        i = i + 1
    print ( "No solution" )
|||

EXPONENTIAL_SQUARING_FAST_MODULO_MULTIPLICATION_1

def exponentiation ( bas , exp ) :
    t = 1 
    while ( exp > 0 ) :
        if ( exp % 2 != 0 ) :
            t = ( t * bas ) % N 
        bas = ( bas * bas ) % N 
        exp = int ( exp / 2 ) 
    return t % N 
|||

CHECK_OCCURRENCES_CHARACTER_APPEAR_TOGETHER

def checkIfAllTogether ( s , c ) :
    oneSeen = False
    i = 0
    n = len ( s )
    while ( i < n ) :
        if ( s [ i ] == c ) :
            if ( oneSeen == True ) :
                return False
            while ( i < n and s [ i ] == c ) :
                i = i + 1
            oneSeen = True
        else :
            i = i + 1
    return True
|||

MAXIMUM_AREA_RECTANGLE_PICKING_FOUR_SIDES_ARRAY

def findArea ( arr , n ) :
    arr.sort ( reverse = True )
    dimension = [ 0 , 0 ]
    i = 0
    j = 0
    while ( i < n - 1 and j < 2 ) :
        if ( arr [ i ] == arr [ i + 1 ] ) :
            dimension [ j ] = arr [ i ]
            j += 1
            i += 1
        i += 1
    return ( dimension [ 0 ] * dimension [ 1 ] )
|||

PYTHON_PROGRAM_FIND_PERIMETER_CIRCUMFERENCE_SQUARE_RECTANGLE

def Circumference ( a ) :
    return ( 4 * a )
|||

CYCLE_SORT

def cycleSort ( array ) :
    writes = 0
    for cycleStart in range ( 0 , len ( array ) - 1 ) :
        item = array [ cycleStart ]
        pos = cycleStart
        for i in range ( cycleStart + 1 , len ( array ) ) :
            if array [ i ] < item :
                pos += 1
        if pos == cycleStart :
            continue
        while item == array [ pos ] :
            pos += 1
        array [ pos ] , item = item , array [ pos ]
        writes += 1
        while pos != cycleStart :
            pos = cycleStart
            for i in range ( cycleStart + 1 , len ( array ) ) :
                if array [ i ] < item :
                    pos += 1
            while item == array [ pos ] :
                pos += 1
            array [ pos ] , item = item , array [ pos ]
            writes += 1
    return writes
|||

SELECT_A_RANDOM_NUMBER_FROM_STREAM_WITH_O1_SPACE

def selectRandom ( x ) :
    res = 0 
    count = 0 
    count += 1 
    if ( count == 1 ) :
        res = x 
    else :
        i = random.randrange ( count ) 
        if ( i == count - 1 ) :
            res = x 
    return res 
|||

HOSOYAS_TRIANGLE

def printHosoya ( n ) :
    dp = [ [ 0 for i in range ( N ) ] for i in range ( N ) ]
    dp [ 0 ] [ 0 ] = dp [ 1 ] [ 0 ] = dp [ 1 ] [ 1 ] = 1
    for i in range ( 2 , n ) :
        for j in range ( n ) :
            if ( i > j ) :
                dp [ i ] [ j ] = ( dp [ i - 1 ] [ j ] + dp [ i - 2 ] [ j ] )
            else :
                dp [ i ] [ j ] = ( dp [ i - 1 ] [ j - 1 ] + dp [ i - 2 ] [ j - 2 ] )
    for i in range ( n ) :
        for j in range ( i + 1 ) :
            print ( dp [ i ] [ j ] , end = ' ' )
        print ( )
|||

DISTRIBUTING_M_ITEMS_CIRCLE_SIZE_N_STARTING_K_TH_POSITION

def lastPosition ( n , m , k ) :
    if ( m <= n - k + 1 ) :
        return m + k - 1
    m = m - ( n - k + 1 )
    if ( m % n == 0 ) :
        return n
    else :
        return m % n
|||

PRINTING_LONGEST_INCREASING_CONSECUTIVE_SUBSEQUENCE

def longestSubsequence ( a , n ) :
    mp = { i : 0 for i in range ( 13 ) }
    dp = [ 0 for i in range ( n ) ]
    maximum = - sys.maxsize - 1
    index = - 1
    for i in range ( n ) :
        if ( ( a [ i ] - 1 ) in mp ) :
            lastIndex = mp [ a [ i ] - 1 ] - 1
            dp [ i ] = 1 + dp [ lastIndex ]
        else :
            dp [ i ] = 1
        mp [ a [ i ] ] = i + 1
        if ( maximum < dp [ i ] ) :
            maximum = dp [ i ]
            index = i
    for curr in range ( a [ index ] - maximum + 1 , a [ index ] + 1 , 1 ) :
        print ( curr , end = " " )
|||

NUMBER_OF_TRIANGLES_IN_DIRECTED_AND_UNDIRECTED_GRAPHS

def countTriangle ( g , isDirected ) :
    nodes = len ( g )
    count_Triangle = 0
    for i in range ( nodes ) :
        for j in range ( nodes ) :
            for k in range ( nodes ) :
                if ( i != j and i != k and j != k and g [ i ] [ j ] and g [ j ] [ k ] and g [ k ] [ i ] ) :
                    count_Triangle += 1
    return count_Triangle / 3 if isDirected else count_Triangle / 6
|||

CHECK_GIVEN_ARRAY_CONTAINS_DUPLICATE_ELEMENTS_WITHIN_K_DISTANCE

def checkDuplicatesWithinK ( arr , n , k ) :
    myset = [ ]
    for i in range ( n ) :
        if arr [ i ] in myset :
            return True
        myset.append ( arr [ i ] )
        if ( i >= k ) :
            myset.remove ( arr [ i - k ] )
    return False
|||

MINIMUM_INSERTIONS_SORT_ARRAY

def minInsertionStepToSortArray ( arr , N ) :
    lis = [ 0 ] * N
    for i in range ( N ) :
        lis [ i ] = 1
    for i in range ( 1 , N ) :
        for j in range ( i ) :
            if ( arr [ i ] >= arr [ j ] and lis [ i ] < lis [ j ] + 1 ) :
                lis [ i ] = lis [ j ] + 1
    max = 0
    for i in range ( N ) :
        if ( max < lis [ i ] ) :
            max = lis [ i ]
    return ( N - max )
|||

GENERATE_TWO_OUTPUT_STRINGS_DEPENDING_UPON_OCCURRENCE_CHARACTER_INPUT_STRING

def printDuo ( string ) :
    countChar = [ 0 for i in range ( MAX_CHAR ) ]
    n = len ( string )
    for i in range ( n ) :
        countChar [ ord ( string [ i ] ) - ord ( 'a' ) ] += 1
    str1 = ""
    str2 = ""
    for i in range ( MAX_CHAR ) :
        if ( countChar [ i ] > 1 ) :
            str2 = str2 + chr ( i + ord ( 'a' ) )
        elif ( countChar [ i ] == 1 ) :
            str1 = str1 + chr ( i + ord ( 'a' ) )
    print ( "String with characters occurring once:" , "\n" , str1 )
    print ( "String with characters occurring" , "multiple times:" , "\n" , str2 )
|||

NUMBER_DIGITS_PRODUCT_TWO_NUMBERS_1

def countDigits ( a , b ) :
    if ( a == 0 or b == 0 ) :
        return 1
    return math.floor ( math.log10 ( abs ( a ) ) + math.log10 ( abs ( b ) ) ) + 1
|||

TOTAL_NUMBER_OF_NON_DECREASING_NUMBERS_WITH_N_DIGITS_1

def countNonDecreasing ( n ) :
    N = 10
    count = 1
    for i in range ( 1 , n + 1 ) :
        count = int ( count * ( N + i - 1 ) )
        count = int ( count / i )
    return count
|||

COUNT_STRINGS_ADJACENT_CHARACTERS_DIFFERENCE_ONE

def countStrs ( n ) :
    dp = [ [ 0 for j in range ( 27 ) ] for i in range ( n + 1 ) ]
    for i in range ( 0 , 26 ) :
        dp [ 1 ] [ i ] = 1
    for i in range ( 2 , n + 1 ) :
        for j in range ( 0 , 26 ) :
            if ( j == 0 ) :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j + 1 ] 
            else :
                dp [ i ] [ j ] = ( dp [ i - 1 ] [ j - 1 ] + dp [ i - 1 ] [ j + 1 ] )
    sum = 0
    for i in range ( 0 , 26 ) :
        sum = sum + dp [ n ] [ i ]
    return sum
|||

PROGRAM_TO_EFFICIENTLY_CALCULATE_EX

def exponential ( n , x ) :
    sum = 1.0
    for i in range ( n , 0 , - 1 ) :
        sum = 1 + x * sum / i
    print ( "e^x =" , sum )
|||

EFFICIENTLY_COMPUTE_SUMS_OF_DIAGONALS_OF_A_MATRIX_1

def printDiagonalSums ( mat , n ) :
    principal = 0
    secondary = 0
    for i in range ( 0 , n ) :
        principal += mat [ i ] [ i ]
        secondary += mat [ i ] [ n - i - 1 ]
    print ( "Principal Diagonal:" , principal )
    print ( "Secondary Diagonal:" , secondary )
|||

PRINT_WAYS_BREAK_STRING_BRACKET_FORM

def findCombinations ( string , index , out ) :
    if index == len ( string ) :
        print ( out )
    for i in range ( index , len ( string ) , 1 ) :
        findCombinations ( string , i + 1 , out + "(" + string [ index : i + 1 ] + ")" )
|||

LINEAR_SEARCH

def search ( arr , n , x ) :
    for i in range ( 0 , n ) :
        if ( arr [ i ] == x ) :
            return i 
    return - 1 
|||

FIND_THE_ELEMENT_THAT_APPEARS_ONCE_2

def singleNumber ( nums ) :
    return ( 3 * sum ( set ( nums ) ) - sum ( nums ) ) / 2
|||

SEARCH_ALMOST_SORTED_ARRAY

def binarySearch ( arr , l , r , x ) :
    if ( r >= l ) :
        mid = int ( l + ( r - l ) / 2 )
        if ( arr [ mid ] == x ) : return mid
        if ( mid > l and arr [ mid - 1 ] == x ) :
            return ( mid - 1 )
        if ( mid < r and arr [ mid + 1 ] == x ) :
            return ( mid + 1 )
        if ( arr [ mid ] > x ) :
            return binarySearch ( arr , l , mid - 2 , x )
        return binarySearch ( arr , mid + 2 , r , x )
    return - 1
|||

EULERS_TOTIENT_FUNCTION_FOR_ALL_NUMBERS_SMALLER_THAN_OR_EQUAL_TO_N

def computeTotient ( n ) :
    phi = [ ]
    for i in range ( n + 2 ) :
        phi.append ( 0 )
    for i in range ( 1 , n + 1 ) :
        phi [ i ] = i
    for p in range ( 2 , n + 1 ) :
        if ( phi [ p ] == p ) :
            phi [ p ] = p - 1
            for i in range ( 2 * p , n + 1 , p ) :
                phi [ i ] = ( phi [ i ] // p ) * ( p - 1 )
    for i in range ( 1 , n + 1 ) :
        print ( "Totient of " , i , " is " , phi [ i ] )
|||

FIND_MINIMUM_NUMBER_DIVIDED_MAKE_NUMBER_PERFECT_SQUARE

def findMinNumber ( n ) :
    count = 0
    ans = 1
    while n % 2 == 0 :
        count += 1
        n //= 2
    if count % 2 is not 0 :
        ans *= 2
    for i in range ( 3 , ( int ) ( math.sqrt ( n ) ) + 1 , 2 ) :
        count = 0
        while n % i == 0 :
            count += 1
            n //= i
        if count % 2 is not 0 :
            ans *= i
    if n > 2 :
        ans *= n
    return ans
|||

COUNT_NUMBER_WAYS_JUMP_REACH_END

def countWaysToJump ( arr , n ) :
    count_jump = [ 0 for i in range ( n ) ]
    for i in range ( n - 2 , - 1 , - 1 ) :
        if ( arr [ i ] >= n - i - 1 ) :
            count_jump [ i ] += 1
        j = i + 1
        while ( j < n - 1 and j <= arr [ i ] + i ) :
            if ( count_jump [ j ] != - 1 ) :
                count_jump [ i ] += count_jump [ j ]
            j += 1
        if ( count_jump [ i ] == 0 ) :
            count_jump [ i ] = - 1
    for i in range ( n ) :
        print ( count_jump [ i ] , end = " " )
|||

CONVERT_SUBSTRINGS_LENGTH_K_BASE_B_DECIMAL_1

def substringConversions ( str1 , k , b ) :
    for i in range ( 0 , len ( str1 ) - k + 1 ) :
        sub = str1 [ i : k + i ]
        Sum = 0
        counter = 0
        for i in range ( len ( sub ) - 1 , - 1 , - 1 ) :
            Sum = ( Sum + ( ( ord ( sub [ i ] ) - ord ( '0' ) ) * pow ( b , counter ) ) )
            counter += 1
        print ( Sum , end = " " )
|||

TWO_ELEMENTS_WHOSE_SUM_IS_CLOSEST_TO_ZERO

def minAbsSumPair ( arr , arr_size ) :
    inv_count = 0
    if arr_size < 2 :
        print ( "Invalid Input" )
        return
    min_l = 0
    min_r = 1
    min_sum = arr [ 0 ] + arr [ 1 ]
    for l in range ( 0 , arr_size - 1 ) :
        for r in range ( l + 1 , arr_size ) :
            sum = arr [ l ] + arr [ r ]
            if abs ( min_sum ) > abs ( sum ) :
                min_sum = sum
                min_l = l
                min_r = r
    print ( "The two elements whose sum is minimum are" , arr [ min_l ] , "and " , arr [ min_r ] )
|||

HOW_TO_PRINT_MAXIMUM_NUMBER_OF_A_USING_GIVEN_FOUR_KEYS

def findoptimal ( N ) :
    if ( N <= 6 ) :
        return N
    screen = [ 0 ] * N
    for n in range ( 1 , 7 ) :
        screen [ n - 1 ] = n
    for n in range ( 7 , N + 1 ) :
        screen [ n - 1 ] = max ( 2 * screen [ n - 4 ] , max ( 3 * screen [ n - 5 ] , 4 * screen [ n - 6 ] ) ) 
    return screen [ N - 1 ]
|||

PROGRAM_DECIMAL_BINARY_CONVERSION_2

def decimalToBinary ( N ) :
    B_Number = 0
    cnt = 0
    while ( N != 0 ) :
        rem = N % 2
        c = pow ( 10 , cnt )
        B_Number += rem * c
        N //= 2
        cnt += 1
    return B_Number
|||

COUNTS_PATHS_POINT_REACH_ORIGIN_1

def countPaths ( n , m ) :
    if ( n == 0 or m == 0 ) :
        return 1
    return ( countPaths ( n - 1 , m ) + countPaths ( n , m - 1 ) )
|||

SUM_ELEMENTS_K1TH_K2TH_SMALLEST_ELEMENTS

def sumBetweenTwoKth ( arr , n , k1 , k2 ) :
    arr.sort ( )
    result = 0
    for i in range ( k1 , k2 - 1 ) :
        result += arr [ i ]
    return result
|||

SMALLEST_SUBARRAY_K_DISTINCT_NUMBERS

def minRange ( arr , n , k ) :
    l = 0
    r = n
    for i in range ( n ) :
        s = [ ]
        for j in range ( i , n ) :
            s.append ( arr [ j ] )
            if ( len ( s ) == k ) :
                if ( ( j - i ) < ( r - l ) ) :
                    r = j
                    l = i
                break
        if ( j == n ) :
            break
    if ( l == 0 and r == n ) :
        print ( "Invalid k" )
    else :
        print ( l , r )
|||

AREA_OF_A_HEXAGON

def hexagonArea ( s ) :
    return ( ( 3 * math.sqrt ( 3 ) * ( s * s ) ) / 2 ) 
|||

NEXT_POWER_OF_2_2

def nextPowerOf2 ( n ) :
    n -= 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    n += 1
    return n
|||

COUNT_SUBSTRINGS_BINARY_STRING_CONTAINING_K_ONES

def countOfSubstringWithKOnes ( s , K ) :
    N = len ( s )
    res = 0
    countOfOne = 0
    freq = [ 0 for i in range ( N + 1 ) ]
    freq [ 0 ] = 1
    for i in range ( 0 , N , 1 ) :
        countOfOne += ord ( s [ i ] ) - ord ( '0' )
        if ( countOfOne >= K ) :
            res += freq [ countOfOne - K ]
        freq [ countOfOne ] += 1
    return res
|||

NUMBER_INDEXES_EQUAL_ELEMENTS_GIVEN_RANGE

def answer_query ( a , n , l , r ) :
    count = 0
    for i in range ( l , r ) :
        if ( a [ i ] == a [ i + 1 ] ) :
            count += 1
    return count
|||

CHECK_WHETHER_NUMBER_DUCK_NUMBER_NOT

def check_duck ( num ) :
    l = len ( num )
    count_zero = 0
    i = 1
    while i < l :
        ch = num [ i ]
        if ( ch == "0" ) :
            count_zero = count_zero + 1
        i = i + 1
    return count_zero
|||

NUMBER_NON_NEGATIVE_INTEGRAL_SOLUTIONS_B_C_N_1

def countIntegralSolutions ( n ) :
    return int ( ( ( n + 1 ) * ( n + 2 ) ) / 2 )
|||

MAXIMUM_PROFIT_BY_BUYING_AND_SELLING_A_SHARE_AT_MOST_K_TIMES_1

def maxProfit ( price , n , k ) :
    profit = [ [ 0 for i in range ( n + 1 ) ] for j in range ( k + 1 ) ]
    for i in range ( 1 , k + 1 ) :
        prevDiff = float ( '-inf' )
        for j in range ( 1 , n ) :
            prevDiff = max ( prevDiff , profit [ i - 1 ] [ j - 1 ] - price [ j - 1 ] )
            profit [ i ] [ j ] = max ( profit [ i ] [ j - 1 ] , price [ j ] + prevDiff )
    return profit [ k ] [ n - 1 ]
|||

COUNT_CHARACTERS_POSITION_ENGLISH_ALPHABETS

def findCount ( str ) :
    result = 0
    for i in range ( len ( str ) ) :
        if ( ( i == ord ( str [ i ] ) - ord ( 'a' ) ) or ( i == ord ( str [ i ] ) - ord ( 'A' ) ) ) :
            result += 1
    return result
|||

COUNT_GFG_SUBSEQUENCES_GIVEN_STRING

def countSubsequence ( s , n ) :
    cntG = 0
    cntF = 0
    result = 0
    C = 0
    for i in range ( n ) :
        if ( s [ i ] == 'G' ) :
            cntG += 1
            result += C
            continue
        if ( s [ i ] == 'F' ) :
            cntF += 1
            C += cntG
            continue
        else :
            continue
    print ( result )
|||

FIND_SMALLEST_VALUE_REPRESENTED_SUM_SUBSET_GIVEN_ARRAY

def findSmallest ( arr , n ) :
    res = 1
    for i in range ( 0 , n ) :
        if arr [ i ] <= res :
            res = res + arr [ i ]
        else :
            break
    return res
|||

MAXIMUM_POINTS_COLLECTED_BY_TWO_PERSONS_ALLOWED_TO_MEET_ONCE

def findMaxPoints ( A ) :
    P1S = [ [ 0 for i in range ( N + 2 ) ] for j in range ( M + 2 ) ]
    P1E = [ [ 0 for i in range ( N + 2 ) ] for j in range ( M + 2 ) ]
    P2S = [ [ 0 for i in range ( N + 2 ) ] for j in range ( M + 2 ) ]
    P2E = [ [ 0 for i in range ( N + 2 ) ] for j in range ( M + 2 ) ]
    for i in range ( 1 , N + 1 ) :
        for j in range ( 1 , M + 1 ) :
            P1S [ i ] [ j ] = max ( P1S [ i - 1 ] [ j ] , P1S [ i ] [ j - 1 ] ) + A [ i - 1 ] [ j - 1 ]
    for i in range ( N , 0 , - 1 ) :
        for j in range ( M , 0 , - 1 ) :
            P1E [ i ] [ j ] = max ( P1E [ i + 1 ] [ j ] , P1E [ i ] [ j + 1 ] ) + A [ i - 1 ] [ j - 1 ]
    for i in range ( N , 0 , - 1 ) :
        for j in range ( 1 , M + 1 ) :
            P2S [ i ] [ j ] = max ( P2S [ i + 1 ] [ j ] , P2S [ i ] [ j - 1 ] ) + A [ i - 1 ] [ j - 1 ]
    for i in range ( 1 , N + 1 ) :
        for j in range ( M , 0 , - 1 ) :
            P2E [ i ] [ j ] = max ( P2E [ i - 1 ] [ j ] , P2E [ i ] [ j + 1 ] ) + A [ i - 1 ] [ j - 1 ]
    ans = 0
    for i in range ( 2 , N ) :
        for j in range ( 2 , M ) :
            op1 = P1S [ i ] [ j - 1 ] + P1E [ i ] [ j + 1 ] + \
                P2S [ i + 1 ] [ j ] + P2E [ i - 1 ] [ j ]
            op2 = P1S [ i - 1 ] [ j ] + P1E [ i + 1 ] [ j ] + \
                P2S [ i ] [ j - 1 ] + P2E [ i ] [ j + 1 ]
            ans = max ( ans , max ( op1 , op2 ) )
    return ans
|||

PROGRAM_FIND_CIRCUMFERENCE_CIRCLE

def circumference ( r ) :
    return ( 2 * PI * r )
|||

QUICKLY_FIND_MULTIPLE_LEFT_ROTATIONS_OF_AN_ARRAY

def leftRotate ( arr , n , k ) :
    for i in range ( k , k + n ) :
        print ( str ( arr [ i % n ] ) , end = " " )
|||

MINIMUM_SUM_CHOOSING_MINIMUM_PAIRS_ARRAY

def minSum ( A ) :
    min_val = min ( A ) 
    return min_val * ( len ( A ) - 1 )
|||

RECURSIVE_PROGRAM_PRIME_NUMBER

def isPrime ( n , i = 2 ) :
    if ( n <= 2 ) :
        return True if ( n == 2 ) else False
    if ( n % i == 0 ) :
        return False
    if ( i * i > n ) :
        return true
    return isPrime ( n , i + 1 )
|||

SPARSE_SEARCH

def sparseSearch ( arr , key , low , high ) :
    left = 0 ; right = 0
    while low <= high :
        mid = ( low + high ) // 2
        if arr [ mid ] == '' :
            left = mid - 1
            right = mid + 1
            if left < low and right > high :
                return - 1
            elif right <= high and arr [ right ] != '' :
                mid = right
            elif left >= low and arr [ left ] != '' :
                mid = left
        if arr [ mid ] == key :
            print ( 'Found string {} at index {}'.format ( arr [ mid ] , mid ) )
            return
        elif arr [ mid ] > key :
            high = mid - 1
        elif arr [ mid ] < key :
            low = mid + 1
        left -= 1
        right += 1
    return - 1
|||

FIND_NUMBER_TIMES_STRING_OCCURS_GIVEN_STRING

def count ( a , b , m , n ) :
    if ( ( m == 0 and n == 0 ) or n == 0 ) :
        return 1
    if ( m == 0 ) :
        return 0
    if ( a [ m - 1 ] == b [ n - 1 ] ) :
        return ( count ( a , b , m - 1 , n - 1 ) + count ( a , b , m - 1 , n ) )
    else :
        return count ( a , b , m - 1 , n )
|||

PROGRAM_CHECK_ARRAY_SORTED_NOT_ITERATIVE_RECURSIVE_1

def arraySortedOrNot ( arr , n ) :
    if ( n == 0 or n == 1 ) :
        return True
    for i in range ( 1 , n ) :
        if ( arr [ i - 1 ] > arr [ i ] ) :
            return False
    return True
|||

FIND_INDEX_0_REPLACED_1_GET_LONGEST_CONTINUOUS_SEQUENCE_1S_BINARY_ARRAY

def maxOnesIndex ( arr , n ) :
    max_count = 0
    max_index = 0
    prev_zero = - 1
    prev_prev_zero = - 1
    for curr in range ( n ) :
        if ( arr [ curr ] == 0 ) :
            if ( curr - prev_prev_zero > max_count ) :
                max_count = curr - prev_prev_zero
                max_index = prev_zero
            prev_prev_zero = prev_zero
            prev_zero = curr
    if ( n - prev_prev_zero > max_count ) :
        max_index = prev_zero
    return max_index
|||

FIND_MAXIMUM_PRODUCT_OF_A_TRIPLET_IN_ARRAY_1

def maxProduct ( arr , n ) :
    if n < 3 :
        return - 1
    arr.sort ( )
    return max ( arr [ 0 ] * arr [ 1 ] * arr [ n - 1 ] , arr [ n - 1 ] * arr [ n - 2 ] * arr [ n - 3 ] )
|||

COORDINATES_RECTANGLE_GIVEN_POINTS_LIE_INSIDE

def printRect ( X , Y , n ) :
    Xmax = max ( X )
    Xmin = min ( X )
    Ymax = max ( Y )
    Ymin = min ( Y )
    print ( "{" , Xmin , ", " , Ymin , "}" , sep = "" )
    print ( "{" , Xmin , ", " , Ymax , "}" , sep = "" )
    print ( "{" , Xmax , ", " , Ymax , "}" , sep = "" )
    print ( "{" , Xmax , ", " , Ymin , "}" , sep = "" )
|||

COUNT_BINARY_DIGIT_NUMBERS_SMALLER_N

def countOfBinaryNumberLessThanN ( N ) :
    q = deque ( )
    q.append ( 1 )
    cnt = 0
    while ( q ) :
        t = q.popleft ( )
        if ( t <= N ) :
            cnt = cnt + 1
            q.append ( t * 10 )
            q.append ( t * 10 + 1 )
    return cnt
|||

CONVERT_DECIMAL_FRACTION_BINARY_NUMBER

def decimalToBinary ( num , k_prec ) :
    binary = ""
    Integral = int ( num )
    fractional = num - Integral
    while ( Integral ) :
        rem = Integral % 2
        binary += str ( rem ) 
        Integral //= 2
    binary = binary [ : : - 1 ]
    binary += '.'
    while ( k_prec ) :
        fractional *= 2
        fract_bit = int ( fractional )
        if ( fract_bit == 1 ) :
            fractional -= fract_bit
            binary += '1'
        else :
            binary += '0'
        k_prec -= 1
    return binary
|||

MAXIMUM_NUMBER_OF_TRAILING_ZEROS_IN_THE_PRODUCT_OF_THE_SUBSETS_OF_SIZE_K

def maximumZeros ( arr , n , k ) :
    global MAX5
    subset = [ [ - 1 ] * ( MAX5 + 5 ) for _ in range ( k + 1 ) ]
    subset [ 0 ] [ 0 ] = 0
    for p in arr :
        pw2 , pw5 = 0 , 0
        while not p % 2 :
            pw2 += 1
            p //= 2
        while not p % 5 :
            pw5 += 1
            p //= 5
        for i in range ( k - 1 , - 1 , - 1 ) :
            for j in range ( MAX5 ) :
                if subset [ i ] [ j ] != - 1 :
                    subset [ i + 1 ] [ j + pw5 ] = ( max ( subset [ i + 1 ] [ j + pw5 ] , ( subset [ i ] [ j ] + pw2 ) ) )
    ans = 0
    for i in range ( MAX5 ) :
        ans = max ( ans , min ( i , subset [ k ] [ i ] ) )
    return ans
|||

SEARCH_AN_ELEMENT_IN_A_SORTED_AND_PIVOTED_ARRAY

def search ( arr , l , h , key ) :
    if l > h :
        return - 1
    mid = ( l + h ) // 2
    if arr [ mid ] == key :
        return mid
    if arr [ l ] <= arr [ mid ] :
        if key >= arr [ l ] and key <= arr [ mid ] :
            return search ( arr , l , mid - 1 , key )
        return search ( arr , mid + 1 , h , key )
    if key >= arr [ mid ] and key <= arr [ h ] :
        return search ( a , mid + 1 , h , key )
    return search ( arr , l , mid - 1 , key )
|||

PROGRAM_FIND_AREA_CIRCULAR_SEGMENT

def area_of_segment ( radius , angle ) :
    area_of_sector = pi *
        ( radius * radius )
        * ( angle / 360 )
    area_of_triangle = 1 / 2 *
        ( radius * radius ) *
        math.sin ( ( angle * pi ) / 180 )
    return area_of_sector - area_of_triangle 
|||

K_SMALLEST_ELEMENTS_ORDER_USING_O1_EXTRA_SPACE

def printSmall ( arr , n , k ) :
    for i in range ( k , n ) :
        max_var = arr [ k - 1 ]
        pos = k - 1
        for j in range ( k - 2 , - 1 , - 1 ) :
            if ( arr [ j ] > max_var ) :
                max_var = arr [ j ]
                pos = j
        if ( max_var > arr [ i ] ) :
            j = pos
            while ( j < k - 1 ) :
                arr [ j ] = arr [ j + 1 ]
                j += 1
            arr [ k - 1 ] = arr [ i ]
    for i in range ( 0 , k ) :
        print ( arr [ i ] , end = " " )
|||

NTH_NON_FIBONACCI_NUMBER

def nonFibonacci ( n ) :
    prevPrev = 1
    prev = 2
    curr = 3
    while n > 0 :
        prevPrev = prev
        prev = curr
        curr = prevPrev + prev
        n = n - ( curr - prev - 1 )
    n = n + ( curr - prev - 1 )
    return prev + n
|||

ANALYSIS_OF_ALGORITHMS_SET_2_ASYMPTOTIC_ANALYSIS

def search ( arr , n , x ) :
    i = 0
    for i in range ( i , n ) :
        if ( arr [ i ] == x ) :
            return i
    return - 1
|||

ZECKENDORFS_THEOREM_NON_NEIGHBOURING_FIBONACCI_REPRESENTATION

def nearestSmallerEqFib ( n ) :
    if ( n == 0 or n == 1 ) :
        return n
    f1 , f2 , f3 = 0 , 1 , 1
    while ( f3 <= n ) :
        f1 = f2 
        f2 = f3 
        f3 = f1 + f2 
    return f2 
|||

PRINT_MAXIMUM_SHORTEST_DISTANCE

def find_maximum ( a , n , k ) :
    b = dict ( )
    for i in range ( n ) :
        x = a [ i ]
        d = min ( 1 + i , n - i )
        if x not in b.keys ( ) :
            b [ x ] = d
        else :
            b [ x ] = min ( d , b [ x ] )
    ans = 10 ** 9
    for i in range ( n ) :
        x = a [ i ]
        if ( x != ( k - x ) and ( k - x ) in b.keys ( ) ) :
            ans = min ( max ( b [ x ] , b [ k - x ] ) , ans )
    return ans
|||

GENERATING_DISTINCT_SUBSEQUENCES_OF_A_GIVEN_STRING_IN_LEXICOGRAPHIC_ORDER

def generate ( st , s ) :
    if len ( s ) == 0 :
        return
    if s not in st :
        st.add ( s )
        for i in range ( len ( s ) ) :
            t = list ( s ).copy ( )
            t.remove ( s [ i ] )
            t = ''.join ( t )
            generate ( st , t )
    return
|||

WRITE_YOU_OWN_POWER_WITHOUT_USING_MULTIPLICATION_AND_DIVISION

def pow ( a , b ) :
    if ( b == 0 ) :
        return 1
    answer = a
    increment = a
    for i in range ( 1 , b ) :
        for j in range ( 1 , a ) :
            answer += increment
        increment = answer
    return answer
|||

MAXIMIZE_VOLUME_CUBOID_GIVEN_SUM_SIDES_1

def maxvolume ( s ) :
    length = int ( s / 3 )
    s -= length
    breadth = s / 2
    height = s - breadth
    return int ( length * breadth * height )
|||

HORNERS_METHOD_POLYNOMIAL_EVALUATION

def horner ( poly , n , x ) :
    result = poly [ 0 ]
    for i in range ( 1 , n ) :
        result = result * x + poly [ i ]
    return result
|||

MINIMUM_TIME_REQUIRED_PRODUCE_M_ITEMS

def minTime ( arr , n , m ) :
    t = 0
    while ( 1 ) :
        items = 0
        for i in range ( n ) :
            items += ( t // arr [ i ] )
        if ( items >= m ) :
            return t
        t += 1
|||

FIND_DIFFERENCE_BETWEEN_SUMS_OF_TWO_DIAGONALS

def difference ( arr , n ) :
    d1 = 0
    d2 = 0
    for i in range ( 0 , n ) :
        for j in range ( 0 , n ) :
            if ( i == j ) :
                d1 += arr [ i ] [ j ]
            if ( i == n - j - 1 ) :
                d2 += arr [ i ] [ j ]
    return abs ( d1 - d2 ) 
|||

SHORTEST_UNCOMMON_SUBSEQUENCE

def shortestSeq ( S : list , T : list ) :
    m = len ( S )
    n = len ( T )
    dp = [ [ 0 for i in range ( n + 1 ) ] for j in range ( m + 1 ) ]
    for i in range ( m + 1 ) :
        dp [ i ] [ 0 ] = 1
    for i in range ( n + 1 ) :
        dp [ 0 ] [ i ] = MAX
    for i in range ( 1 , m + 1 ) :
        for j in range ( 1 , n + 1 ) :
            ch = S [ i - 1 ]
            k = j - 1
            while k >= 0 :
                if T [ k ] == ch :
                    break
                k -= 1
            if k == - 1 :
                dp [ i ] [ j ] = 1
            else :
                dp [ i ] [ j ] = min ( dp [ i - 1 ] [ j ] , dp [ i - 1 ] [ k ] + 1 )
    ans = dp [ m ] [ n ]
    if ans >= MAX :
        ans = - 1
    return ans
|||

MIN_FLIPS_OF_CONTINUOUS_CHARACTERS_TO_MAKE_ALL_CHARACTERS_SAME_IN_A_STRING

def findFlips ( str , n ) :
    last = ' '
    res = 0
    for i in range ( n ) :
        if ( last != str [ i ] ) :
            res += 1
        last = str [ i ]
    return res // 2
|||

DYNAMIC_PROGRAMMING_SET_28_MINIMUM_INSERTIONS_TO_FORM_A_PALINDROME

def findMinInsertions ( str , l , h ) :
    if ( l > h ) :
        return sys.maxsize
    if ( l == h ) :
        return 0
    if ( l == h - 1 ) :
        return 0 if ( str [ l ] == str [ h ] ) else 1
    if ( str [ l ] == str [ h ] ) :
        return findMinInsertions ( str , l + 1 , h - 1 )
    else :
        return ( min ( findMinInsertions ( str , l , h - 1 ) , findMinInsertions ( str , l + 1 , h ) ) + 1 )
|||

COUNT_CHARACTERS_STRING_DISTANCE_ENGLISH_ALPHABETS

def countPairs ( str1 ) :
    result = 0 
    n = len ( str1 )
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            if ( abs ( ord ( str1 [ i ] ) - ord ( str1 [ j ] ) ) == abs ( i - j ) ) :
                result += 1 
    return result 
|||

MULTISTAGE_GRAPH_SHORTEST_PATH

def shortestDist ( graph ) :
    global INF
    dist = [ 0 ] * N
    dist [ N - 1 ] = 0
    for i in range ( N - 2 , - 1 , - 1 ) :
        dist [ i ] = INF
        for j in range ( N ) :
            if graph [ i ] [ j ] == INF :
                continue
            dist [ i ] = min ( dist [ i ] , graph [ i ] [ j ] + dist [ j ] )
    return dist [ 0 ]
|||

MAXIMUM_SIZE_SUB_MATRIX_WITH_ALL_1S_IN_A_BINARY_MATRIX

def printMaxSubSquare ( M ) :
    R = len ( M )
    C = len ( M [ 0 ] )
    S = [ [ 0 for k in range ( C ) ] for l in range ( R ) ]
    for i in range ( 1 , R ) :
        for j in range ( 1 , C ) :
            if ( M [ i ] [ j ] == 1 ) :
                S [ i ] [ j ] = min ( S [ i ] [ j - 1 ] , S [ i - 1 ] [ j ] , S [ i - 1 ] [ j - 1 ] ) + 1
            else :
                S [ i ] [ j ] = 0
    max_of_s = S [ 0 ] [ 0 ]
    max_i = 0
    max_j = 0
    for i in range ( R ) :
        for j in range ( C ) :
            if ( max_of_s < S [ i ] [ j ] ) :
                max_of_s = S [ i ] [ j ]
                max_i = i
                max_j = j
    print ( "Maximum size sub-matrix is: " )
    for i in range ( max_i , max_i - max_of_s , - 1 ) :
        for j in range ( max_j , max_j - max_of_s , - 1 ) :
            print ( M [ i ] [ j ] , end = "" )
        print ( "" )
|||

GIVEN_SORTED_ARRAY_NUMBER_X_FIND_PAIR_ARRAY_WHOSE_SUM_CLOSEST_X

def printClosest ( arr , n , x ) :
    res_l , res_r = 0 , 0
    l , r , diff = 0 , n - 1 , MAX_VAL
    while r > l :
        if abs ( arr [ l ] + arr [ r ] - x ) < diff :
            res_l = l
            res_r = r
            diff = abs ( arr [ l ] + arr [ r ] - x )
        if arr [ l ] + arr [ r ] > x :
            r -= 1
        else :
            l += 1
    print ( 'The closest pair is {} and {}'.format ( arr [ res_l ] , arr [ res_r ] ) )
|||

SORT_1_N_SWAPPING_ADJACENT_ELEMENTS_1

def sortedAfterSwap ( A , B , n ) :
    for i in range ( 0 , n - 1 ) :
        if B [ i ] :
            if A [ i ] != i + 1 :
                A [ i ] , A [ i + 1 ] = A [ i + 1 ] , A [ i ]
    for i in range ( n ) :
        if A [ i ] != i + 1 :
            return False
    return True
|||

TILE_STACKING_PROBLEM

def possibleWays ( n , m , k ) :
    dp = [ [ 0 for i in range ( 10 ) ] for j in range ( 10 ) ]
    presum = [ [ 0 for i in range ( 10 ) ] for j in range ( 10 ) ]
    for i in range ( 1 , n + 1 ) :
        dp [ 0 ] [ i ] = 0
        presum [ 0 ] [ i ] = 1
    for i in range ( 0 , m + 1 ) :
        presum [ i ] [ 0 ] = 1
        dp [ i ] [ 0 ] = 1
    for i in range ( 1 , m + 1 ) :
        for j in range ( 1 , n + 1 ) :
            dp [ i ] [ j ] = presum [ i - 1 ] [ j ]
            if j > k :
                dp [ i ] [ j ] -= presum [ i - 1 ] [ j - k - 1 ]
        for j in range ( 1 , n + 1 ) :
            presum [ i ] [ j ] = dp [ i ] [ j ] + presum [ i ] [ j - 1 ]
    return dp [ m ] [ n ]
|||

NUMBER_OF_PAIRS_IN_AN_ARRAY_HAVING_SUM_EQUAL_TO_PRODUCT

def sumEqualProduct ( a , n ) :
    zero = 0
    two = 0
    for i in range ( n ) :
        if a [ i ] == 0 :
            zero += 1
        if a [ i ] == 2 :
            two += 1
    cnt = ( zero * ( zero - 1 ) ) // 2 + \
        ( two * ( two - 1 ) ) // 2
    return cnt
|||

DYNAMIC_PROGRAMMING_SET_17_PALINDROME_PARTITIONING

def minPalPartion ( str ) :
    n = len ( str )
    C = [ [ 0 for i in range ( n ) ] for i in range ( n ) ]
    P = [ [ False for i in range ( n ) ] for i in range ( n ) ]
    j = 0
    k = 0
    L = 0
    for i in range ( n ) :
        P [ i ] [ i ] = True 
        C [ i ] [ i ] = 0 
    for L in range ( 2 , n + 1 ) :
        for i in range ( n - L + 1 ) :
            j = i + L - 1
            if L == 2 :
                P [ i ] [ j ] = ( str [ i ] == str [ j ] )
            else :
                P [ i ] [ j ] = ( ( str [ i ] == str [ j ] ) and P [ i + 1 ] [ j - 1 ] )
            if P [ i ] [ j ] == True :
                C [ i ] [ j ] = 0
            else :
                C [ i ] [ j ] = 100000000
                for k in range ( i , j ) :
                    C [ i ] [ j ] = min ( C [ i ] [ j ] , C [ i ] [ k ] + C [ k + 1 ] [ j ] + 1 )
    return C [ 0 ] [ n - 1 ]
|||

FIND_ONE_MULTIPLE_REPEATING_ELEMENTS_READ_ARRAY

def findRepeatingNumber ( arr , n ) :
    sq = sqrt ( n )
    range__ = int ( ( n / sq ) + 1 )
    count = [ 0 for i in range ( range__ ) ]
    for i in range ( 0 , n + 1 , 1 ) :
        count [ int ( ( arr [ i ] - 1 ) / sq ) ] += 1
    selected_block = range__ - 1
    for i in range ( 0 , range__ - 1 , 1 ) :
        if ( count [ i ] > sq ) :
            selected_block = i
            break
    m = { i : 0 for i in range ( n ) }
    for i in range ( 0 , n + 1 , 1 ) :
        if ( ( ( selected_block * sq ) < arr [ i ] ) and ( arr [ i ] <= ( ( selected_block + 1 ) * sq ) ) ) :
            m [ arr [ i ] ] += 1
            if ( m [ arr [ i ] ] > 1 ) :
                return arr [ i ]
    return - 1
|||

MINIMUM_SUM_PATH_TRIANGLE

def minSumPath ( A ) :
    memo = [ None ] * len ( A )
    n = len ( A ) - 1
    for i in range ( len ( A [ n ] ) ) :
        memo [ i ] = A [ n ] [ i ]
    for i in range ( len ( A ) - 2 , - 1 , - 1 ) :
        for j in range ( len ( A [ i ] ) ) :
            memo [ j ] = A [ i ] [ j ] + min ( memo [ j ] , memo [ j + 1 ] ) 
    return memo [ 0 ]
|||

HOW_CAN_WE_SUM_THE_DIGITS_OF_A_GIVEN_NUMBER_IN_SINGLE_STATEMENT_1

def getSum ( n ) :
    sum = 0
    while ( n > 0 ) :
        sum += int ( n % 10 )
        n = int ( n / 10 )
    return sum
|||

RECURSION

def printFun ( test ) :
    if ( test < 1 ) :
        return
    else :
        print ( test , end = " " )
        printFun ( test - 1 )
        print ( test , end = " " )
        return
|||

MAXIMUM_TRIPLET_SUM_ARRAY

def maxTripletSum ( arr , n ) :
    sm = - 1000000
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            for k in range ( j + 1 , n ) :
                if ( sm < ( arr [ i ] + arr [ j ] + arr [ k ] ) ) :
                    sm = arr [ i ] + arr [ j ] + arr [ k ]
    return sm
|||

MINIMUM_NUMBER_OF_JUMPS_TO_REACH_END_OF_A_GIVEN_ARRAY_1

def minJumps ( arr , n ) :
    jumps = [ 0 for i in range ( n ) ]
    if ( n == 0 ) or ( arr [ 0 ] == 0 ) :
        return float ( 'inf' )
    jumps [ 0 ] = 0
    for i in range ( 1 , n ) :
        jumps [ i ] = float ( 'inf' )
        for j in range ( i ) :
            if ( i <= j + arr [ j ] ) and ( jumps [ j ] != float ( 'inf' ) ) :
                jumps [ i ] = min ( jumps [ i ] , jumps [ j ] + 1 )
                break
    return jumps [ n - 1 ]
|||

MAXIMIZE_ARRAY_ELEMENTS_UPTO_GIVEN_NUMBER

def findMaxVal ( arr , n , num , maxLimit ) :
    ind = - 1 
    val = - 1 
    dp = [ [ 0 for i in range ( maxLimit + 1 ) ] for j in range ( n ) ] 
    for ind in range ( n ) :
        for val in range ( maxLimit + 1 ) :
            if ( ind == 0 ) :
                if ( num - arr [ ind ] == val or num + arr [ ind ] == val ) :
                    dp [ ind ] [ val ] = 1 
                else :
                    dp [ ind ] [ val ] = 0 
            else :
                if ( val - arr [ ind ] >= 0 and val + arr [ ind ] <= maxLimit ) :
                    if ( dp [ ind - 1 ] [ val - arr [ ind ] ] == 1 or dp [ ind - 1 ] [ val + arr [ ind ] ] == 1 ) :
                        dp [ ind ] [ val ] = 1 
                elif ( val - arr [ ind ] >= 0 ) :
                    dp [ ind ] [ val ] = dp [ ind - 1 ] [ val - arr [ ind ] ] 
                elif ( val + arr [ ind ] <= maxLimit ) :
                    dp [ ind ] [ val ] = dp [ ind - 1 ] [ val + arr [ ind ] ] 
                else :
                    dp [ ind ] [ val ] = 0 
    for val in range ( maxLimit , - 1 , - 1 ) :
        if ( dp [ n - 1 ] [ val ] == 1 ) :
            return val 
    return - 1 
|||

PROGRAM_FOR_DEADLOCK_FREE_CONDITION_IN_OPERATING_SYSTEM

def Resources ( process , need ) :
    minResources = 0
    minResources = process * ( need - 1 ) + 1
    return minResources
|||

NUMBER_DIGITS_PRODUCT_TWO_NUMBERS

def countDigits ( a , b ) :
    count = 0
    p = abs ( a * b )
    if ( p == 0 ) :
        return 1
    while ( p > 0 ) :
        count = count + 1
        p = p // 10
    return count
|||

FLOOR_IN_A_SORTED_ARRAY

def floorSearch ( arr , low , high , x ) :
    if ( low > high ) :
        return - 1
    if ( x >= arr [ high ] ) :
        return high
    mid = int ( ( low + high ) / 2 )
    if ( arr [ mid ] == x ) :
        return mid
    if ( mid > 0 and arr [ mid - 1 ] <= x and x < arr [ mid ] ) :
        return mid - 1
    if ( x < arr [ mid ] ) :
        return floorSearch ( arr , low , mid - 1 , x )
    return floorSearch ( arr , mid + 1 , high , x )
|||

CHECK_WHETHER_TRIANGLE_VALID_NOT_SIDES_GIVEN

def checkValidity ( a , b , c ) :
    if ( a + b <= c ) or ( a + c <= b ) or ( b + c <= a ) :
        return False
    else :
        return True
|||

PRINT_N_X_N_SPIRAL_MATRIX_USING_O1_EXTRA_SPACE

def printSpiral ( n ) :
    for i in range ( 0 , n ) :
        for j in range ( 0 , n ) :
            x = min ( min ( i , j ) , min ( n - 1 - i , n - 1 - j ) )
            if ( i <= j ) :
                print ( ( n - 2 * x ) * ( n - 2 * x ) - ( i - x ) - ( j - x ) , end = "\t" )
            else :
                print ( ( ( n - 2 * x - 2 ) * ( n - 2 * x - 2 ) + ( i - x ) + ( j - x ) ) , end = "\t" )
        print ( )
|||

POSITION_ELEMENT_STABLE_SORT

def getIndexInSortedArray ( arr , n , idx ) :
    result = 0
    for i in range ( n ) :
        if ( arr [ i ] < arr [ idx ] ) :
            result += 1
        if ( arr [ i ] == arr [ idx ] and i < idx ) :
            result += 1
    return result 
|||

MAXIMUM_SEGMENT_VALUE_PUTTING_K_BREAKPOINTS_NUMBER

def findMaxSegment ( s , k ) :
    seg_len = len ( s ) - k
    res = 0
    for i in range ( seg_len ) :
        res = res * 10 + ( ord ( s [ i ] ) - ord ( '0' ) )
    seg_len_pow = pow ( 10 , seg_len - 1 )
    curr_val = res
    for i in range ( 1 , len ( s ) - seg_len ) :
        curr_val = curr_val - ( ord ( s [ i - 1 ] ) - ord ( '0' ) ) * seg_len_pow
        curr_val = ( curr_val * 10 + ( ord ( s [ i + seg_len - 1 ] ) - ord ( '0' ) ) )
        res = max ( res , curr_val )
    return res
|||

FINDING_POWER_PRIME_NUMBER_P_N_1

def PowerOFPINnfactorial ( n , p ) :
    ans = 0
    temp = p
    while ( temp <= n ) :
        ans += n / temp
        temp = temp * p
    return int ( ans )
|||

PROGRAM_PRINT_IDENTITY_MATRIX

def Identity ( size ) :
    for row in range ( 0 , size ) :
        for col in range ( 0 , size ) :
            if ( row == col ) :
                print ( "1 " , end = " " )
            else :
                print ( "0 " , end = " " )
        print ( )
|||

SUM_MATRIX_ELEMENT_ELEMENT_INTEGER_DIVISION_ROW_COLUMN

def findSum ( N ) :
    ans = 0
    for i in range ( 1 , N + 1 ) :
        for j in range ( 1 , N + 1 ) :
            ans += i // j
    return ans
|||

TILING_WITH_DOMINOES

def countWays ( n ) :
    A = [ 0 ] * ( n + 1 )
    B = [ 0 ] * ( n + 1 )
    A [ 0 ] = 1
    A [ 1 ] = 0
    B [ 0 ] = 0
    B [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        A [ i ] = A [ i - 2 ] + 2 * B [ i - 1 ]
        B [ i ] = A [ i - 1 ] + B [ i - 2 ]
    return A [ n ]
|||

COUNT_DERANGEMENTS_PERMUTATION_SUCH_THAT_NO_ELEMENT_APPEARS_IN_ITS_ORIGINAL_POSITION

def countDer ( n ) :
    if ( n == 1 ) : return 0
    if ( n == 0 ) : return 1
    if ( n == 2 ) : return 1
    return ( n - 1 ) * ( countDer ( n - 1 ) + countDer ( n - 2 ) )
|||

FREQUENCY_ELEMENT_UNSORTED_ARRAY_1

def countFreq ( a , n ) :
    hm = dict ( )
    for i in range ( n ) :
        hm [ a [ i ] ] = hm.get ( a [ i ] , 0 ) + 1
    cumul = 0
    for i in range ( n ) :
        cumul += hm [ a [ i ] ]
        if ( hm [ a [ i ] ] > 0 ) :
            print ( a [ i ] , "->" , cumul )
        hm [ a [ i ] ] = 0
|||

MINIMIZE_THE_SUM_OF_DIGITS_OF_A_AND_B_SUCH_THAT_A_B_N

def minSum ( n ) :
    sum = 0 
    while ( n > 0 ) :
        sum += ( n % 10 ) 
        n //= 10 
    if ( sum == 1 ) :
        return 10 
    return sum 
|||

DIVIDE_CUBOID_CUBES_SUM_VOLUMES_MAXIMUM

def maximizecube ( l , b , h ) :
    side = gcd ( l , gcd ( b , h ) )
    num = int ( l / side )
    num = int ( num * b / side )
    num = int ( num * h / side )
    print ( side , num )
|||

CHECK_NUMBER_POWER_K_USING_BASE_CHANGING_METHOD

def isPowerOfK ( n , k ) :
    oneSeen = False
    while ( n > 0 ) :
        digit = n % k
        if ( digit > 1 ) :
            return False
        if ( digit == 1 ) :
            if ( oneSeen ) :
                return False
            oneSeen = True
        n //= k
    return True
|||

POSITION_OF_RIGHTMOST_SET_BIT_1

def PositionRightmostSetbit ( n ) :
    position = 1
    m = 1
    while ( not ( n & m ) ) :
        m = m << 1
        position += 1
    return position
|||

SEARCH_INSERT_AND_DELETE_IN_A_SORTED_ARRAY_1

def insertSorted ( arr , n , key , capacity ) :
    if ( n >= capacity ) :
        return n
    i = n - 1
    while i >= 0 and arr [ i ] > key :
        arr [ i + 1 ] = arr [ i ]
        i -= 1
    arr [ i + 1 ] = key
    return ( n + 1 )
|||

FIND_THE_MAXIMUM_OF_MINIMUMS_FOR_EVERY_WINDOW_SIZE_IN_A_GIVEN_ARRAY_1

def printMaxOfMin ( arr , n ) :
    s = [ ]
    left = [ - 1 ] * ( n + 1 )
    right = [ n ] * ( n + 1 )
    for i in range ( n ) :
        while ( len ( s ) != 0 and arr [ s [ - 1 ] ] >= arr [ i ] ) :
            s.pop ( )
        if ( len ( s ) != 0 ) :
            left [ i ] = s [ - 1 ]
        s.append ( i )
    while ( len ( s ) != 0 ) :
        s.pop ( )
    for i in range ( n - 1 , - 1 , - 1 ) :
        while ( len ( s ) != 0 and arr [ s [ - 1 ] ] >= arr [ i ] ) :
            s.pop ( )
        if ( len ( s ) != 0 ) :
            right [ i ] = s [ - 1 ]
        s.append ( i )
    ans = [ 0 ] * ( n + 1 )
    for i in range ( n + 1 ) :
        ans [ i ] = 0
    for i in range ( n ) :
        Len = right [ i ] - left [ i ] - 1
        ans [ Len ] = max ( ans [ Len ] , arr [ i ] )
    for i in range ( n - 1 , 0 , - 1 ) :
        ans [ i ] = max ( ans [ i ] , ans [ i + 1 ] )
    for i in range ( 1 , n + 1 ) :
        print ( ans [ i ] , end = " " )
|||

MAXIMUM_DECIMAL_VALUE_PATH_IN_A_BINARY_MATRIX_1

def MaximumDecimalValue ( mat , n ) :
    dp = [ [ 0 for i in range ( n ) ] for i in range ( n ) ]
    if ( mat [ 0 ] [ 0 ] == 1 ) :
        dp [ 0 ] [ 0 ] = 1
    for i in range ( 1 , n ) :
        if ( mat [ 0 ] [ i ] == 1 ) :
            dp [ 0 ] [ i ] = dp [ 0 ] [ i - 1 ] + 2 ** i
        else :
            dp [ 0 ] [ i ] = dp [ 0 ] [ i - 1 ]
    for i in range ( 1 , n ) :
        if ( mat [ i ] [ 0 ] == 1 ) :
            dp [ i ] [ 0 ] = dp [ i - 1 ] [ 0 ] + 2 ** i
    else :
        dp [ i ] [ 0 ] = dp [ i - 1 ] [ 0 ]
    for i in range ( 1 , n ) :
        for j in range ( 1 , n ) :
            if ( mat [ i ] [ j ] == 1 ) :
                dp [ i ] [ j ] = max ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] ) + ( 2 ** ( i + j ) )
            else :
                dp [ i ] [ j ] = max ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] )
    return dp [ n - 1 ] [ n - 1 ]
|||

COUNT_NUMBER_OF_WAYS_TO_COVER_A_DISTANCE

def printCountRec ( dist ) :
    if dist < 0 :
        return 0
    if dist == 0 :
        return 1
    return ( printCountRec ( dist - 1 ) + printCountRec ( dist - 2 ) + printCountRec ( dist - 3 ) )
|||

MOVE_VE_ELEMENTS_END_ORDER_EXTRA_SPACE_ALLOWED

def segregateElements ( arr , n ) :
    temp = [ 0 for k in range ( n ) ]
    j = 0
    for i in range ( n ) :
        if ( arr [ i ] >= 0 ) :
            temp [ j ] = arr [ i ]
            j += 1
    if ( j == n or j == 0 ) :
        return
    for i in range ( n ) :
        if ( arr [ i ] < 0 ) :
            temp [ j ] = arr [ i ]
            j += 1
    for k in range ( n ) :
        arr [ k ] = temp [ k ]
|||

MINIMUM_PERIMETER_N_BLOCKS

def minPerimeter ( n ) :
    l = math.sqrt ( n )
    sq = l * l
    if ( sq == n ) :
        return l * 4
    else :
        row = n / l
        perimeter = 2 * ( l + row )
        if ( n % l != 0 ) :
            perimeter += 2
        return perimeter
|||

DYNAMIC_PROGRAMMING_SET_36_CUT_A_ROPE_TO_MAXIMIZE_PRODUCT

def maxProd ( n ) :
    if ( n == 0 or n == 1 ) :
        return 0
    max_val = 0
    for i in range ( 1 , n - 1 ) :
        max_val = max ( max_val , max ( i * ( n - i ) , maxProd ( n - i ) * i ) )
    return max_val 
|||

LONGEST_COMMON_SUBSTRING_SPACE_OPTIMIZED_DP_SOLUTION

def LCSubStr ( X , Y ) :
    m = len ( X )
    n = len ( Y )
    result = 0
    len_mat = np.zeros ( ( 2 , n ) )
    currRow = 0
    for i in range ( m ) :
        for j in range ( n ) :
            if ( i == 0 | j == 0 ) :
                len_mat [ currRow ] [ j ] = 0
            elif ( X [ i - 1 ] == Y [ j - 1 ] ) :
                len_mat [ currRow ] [ j ] = len_mat [ 1 - currRow ] [ j - 1 ] + 1
                result = max ( result , len_mat [ currRow ] [ j ] )
            else :
                len_mat [ currRow ] [ j ] = 0
        currRow = 1 - currRow
    return result
|||

CHECK_GIVEN_STRING_ROTATION_PALINDROME

def isPalindrome ( string ) :
    l = 0
    h = len ( string ) - 1
    while h > l :
        l += 1
        h -= 1
        if string [ l - 1 ] != string [ h + 1 ] :
            return False
    return True
|||

FIND_NUMBER_OF_SOLUTIONS_OF_A_LINEAR_EQUATION_OF_N_VARIABLES_1

def countSol ( coeff , n , rhs ) :
    dp = [ 0 for i in range ( rhs + 1 ) ]
    dp [ 0 ] = 1
    for i in range ( n ) :
        for j in range ( coeff [ i ] , rhs + 1 ) :
            dp [ j ] += dp [ j - coeff [ i ] ]
    return dp [ rhs ]
|||

FIND_THE_LARGEST_PAIR_SUM_IN_AN_UNSORTED_ARRAY

def findLargestSumPair ( arr , n ) :
    if arr [ 0 ] > arr [ 1 ] :
        first = arr [ 0 ]
        second = arr [ 1 ]
    else :
        first = arr [ 1 ]
        second = arr [ 0 ]
    for i in range ( 2 , n ) :
        if arr [ i ] > first :
            second = first
            first = arr [ i ]
        elif arr [ i ] > second and arr [ i ] != first :
            second = arr [ i ]
    return ( first + second )
|||

FIND_BITONIC_POINT_GIVEN_BITONIC_SEQUENCE

def binarySearch ( arr , left , right ) :
    if ( left <= right ) :
        mid = ( left + right ) // 2 
        if ( arr [ mid - 1 ] < arr [ mid ] and arr [ mid ] > arr [ mid + 1 ] ) :
            return mid 
        if ( arr [ mid ] < arr [ mid + 1 ] ) :
            return binarySearch ( arr , mid + 1 , right ) 
        else :
            return binarySearch ( arr , left , mid - 1 ) 
    return - 1 
|||

PRINT_ALL_DISTINCT_CHARACTERS_OF_A_STRING_IN_ORDER_3_METHODS_1

def printDistinct ( Str ) :
    n = len ( Str )
    count = [ 0 for i in range ( MAX_CHAR ) ]
    index = [ n for i in range ( MAX_CHAR ) ]
    for i in range ( n ) :
        x = ord ( Str [ i ] )
        count [ x ] += 1
        if ( count [ x ] == 1 and x != ' ' ) :
            index [ x ] = i
        if ( count [ x ] == 2 ) :
            index [ x ] = n
    index = sorted ( index )
    for i in range ( MAX_CHAR ) :
        if index [ i ] == n :
            break
        print ( Str [ index [ i ] ] , end = "" )
|||

FIND_TWO_SIDES_RIGHT_ANGLE_TRIANGLE

def printOtherSides ( n ) :
    if ( n & 1 ) :
        if ( n == 1 ) :
            print ( - 1 )
        else :
            b = ( n * n - 1 ) // 2
            c = ( n * n + 1 ) // 2
            print ( "b =" , b , ", c =" , c )
    else :
        if ( n == 2 ) :
            print ( - 1 )
        else :
            b = n * n // 4 - 1
            c = n * n // 4 + 1
            print ( "b =" , b ", c =" , c )
|||

COUNT_NUMBER_OF_STRINGS_MADE_OF_R_G_AND_B_USING_GIVEN_COMBINATION

def possibleStrings ( n , r , b , g ) :
    fact = [ 0 for i in range ( n + 1 ) ]
    fact [ 0 ] = 1
    for i in range ( 1 , n + 1 , 1 ) :
        fact [ i ] = fact [ i - 1 ] * i
    left = n - ( r + g + b )
    sum = 0
    for i in range ( 0 , left + 1 , 1 ) :
        for j in range ( 0 , left - i + 1 , 1 ) :
            k = left - ( i + j )
            sum = ( sum + fact [ n ] / ( fact [ i + r ] * fact [ j + b ] * fact [ k + g ] ) )
    return sum
|||

REARRANGE_ARRAY_MAXIMUM_MINIMUM_FORM_SET_2_O1_EXTRA_SPACE_1

def rearrange ( arr , n ) :
    max_ele = arr [ n - 1 ]
    min_ele = arr [ 0 ]
    for i in range ( n ) :
        if i % 2 == 0 :
            arr [ i ] = max_ele
            max_ele -= 1
        else :
            arr [ i ] = min_ele
            min_ele += 1
|||

EVALUATE_AN_ARRAY_EXPRESSION_WITH_NUMBERS_AND

def calculateSum ( arr , n ) :
    if ( n == 0 ) :
        return 0
    s = arr [ 0 ]
    value = int ( s )
    sum = value
    for i in range ( 2 , n , 2 ) :
        s = arr [ i ]
        value = int ( s )
        operation = arr [ i - 1 ] [ 0 ]
        if ( operation == '+' ) :
            sum += value
        else :
            sum -= value
    return sum
|||

SUM_MATRIX_ELEMENT_ELEMENT_INTEGER_DIVISION_ROW_COLUMN_1

def findSum ( n ) :
    ans = 0 ; temp = 0 
    for i in range ( 1 , n + 1 ) :
        if temp < n :
            temp = i - 1
            num = 1
            while temp < n :
                if temp + i <= n :
                    ans += i * num
                else :
                    ans += ( n - temp ) * num
                temp += i
                num += 1
    return ans
|||

SHUFFLE_A_DECK_OF_CARDS_3

def shuffle ( card , n ) :
    for i in range ( n ) :
        r = i + ( random.randint ( 0 , 55 ) % ( 52 - i ) )
        tmp = card [ i ]
        card [ i ] = card [ r ]
        card [ r ] = tmp
|||

DOOLITTLE_ALGORITHM_LU_DECOMPOSITION

def luDecomposition ( mat , n ) :
    lower = [ [ 0 for x in range ( n ) ] for y in range ( n ) ] 
    upper = [ [ 0 for x in range ( n ) ] for y in range ( n ) ] 
    for i in range ( n ) :
        for k in range ( i , n ) :
            sum = 0 
            for j in range ( i ) :
                sum += ( lower [ i ] [ j ] * upper [ j ] [ k ] ) 
            upper [ i ] [ k ] = mat [ i ] [ k ] - sum 
        for k in range ( i , n ) :
            if ( i == k ) :
                lower [ i ] [ i ] = 1 
            else :
                sum = 0 
                for j in range ( i ) :
                    sum += ( lower [ k ] [ j ] * upper [ j ] [ i ] ) 
                lower [ k ] [ i ] = int ( ( mat [ k ] [ i ] - sum ) / upper [ i ] [ i ] ) 
    print ( "Lower Triangular\t\tUpper Triangular" ) 
    for i in range ( n ) :
        for j in range ( n ) :
            print ( lower [ i ] [ j ] , end = "\t" ) 
        print ( "" , end = "\t" ) 
        for j in range ( n ) :
            print ( upper [ i ] [ j ] , end = "\t" ) 
        print ( "" ) 
|||

PROGRAM_NTH_CATALAN_NUMBER

def catalan ( n ) :
    if n <= 1 :
        return 1
    res = 0
    for i in range ( n ) :
        res += catalan ( i ) * catalan ( n - i - 1 )
    return res
|||

NUMBER_DIGITS_REMOVED_MAKE_NUMBER_DIVISIBLE_3

def divisible ( num ) :
    n = len ( num ) 
    sum = 0 
    for i in range ( n ) :
        sum += int ( num [ i ] ) 
    if ( sum % 3 == 0 ) :
        return 0 
    if ( n == 1 ) :
        return - 1 
    for i in range ( n ) :
        if ( sum % 3 == int ( num [ i ] ) % 3 ) :
            return 1 
    if ( n == 2 ) :
        return - 1 
    return 2 
|||

CHECK_IF_A_NUMBER_IS_POWER_OF_ANOTHER_NUMBER_1

def isPower ( x , y ) :
    res1 = math.log ( y ) / math.log ( x ) 
    res2 = math.log ( y ) / math.log ( x ) 
    return 1 if ( res1 == res2 ) else 0 
|||

LARGEST_SUBSEQUENCE_GCD_GREATER_1

def largestGCDSubsequence ( arr , n ) :
    ans = 0
    maxele = max ( arr )
    for i in range ( 2 , maxele + 1 ) :
        count = 0
        for j in range ( n ) :
            if ( arr [ j ] % i == 0 ) :
                count += 1
        ans = max ( ans , count )
    return ans
|||

FIND_COMMON_ELEMENT_ROWS_ROW_WISE_SORTED_MATRIX

def findCommon ( mat ) :
    column = [ N - 1 ] * M
    min_row = 0
    while ( column [ min_row ] >= 0 ) :
        for i in range ( M ) :
            if ( mat [ i ] [ column [ i ] ] < mat [ min_row ] [ column [ min_row ] ] ) :
                min_row = i
        eq_count = 0
        for i in range ( M ) :
            if ( mat [ i ] [ column [ i ] ] > mat [ min_row ] [ column [ min_row ] ] ) :
                if ( column [ i ] == 0 ) :
                    return - 1
                column [ i ] -= 1
            else :
                eq_count += 1
        if ( eq_count == M ) :
            return mat [ min_row ] [ column [ min_row ] ]
    return - 1
|||

CHECK_GIVEN_CIRCLE_LIES_COMPLETELY_INSIDE_RING_FORMED_TWO_CONCENTRIC_CIRCLES

def checkcircle ( r , R , r1 , x1 , y1 ) :
    dis = int ( math.sqrt ( x1 * x1 + y1 * y1 ) )
    return ( dis - r1 >= R and dis + r1 <= r )
|||

COUNT_TOTAL_SET_BITS_IN_ALL_NUMBERS_FROM_1_TO_N

def countSetBits ( n ) :
    i = 0
    ans = 0
    while ( ( 1 << i ) <= n ) :
        k = 0
        change = 1 << i
        for j in range ( 0 , n + 1 ) :
            ans += k
            if change == 1 :
                k = not k
                change = 1 << i
            else :
                change -= 1
        i += 1
    return ans
|||

LONGEST_REPEATING_SUBSEQUENCE

def findLongestRepeatingSubSeq ( str ) :
    n = len ( str )
    dp = [ [ 0 ] * ( n + 1 ) ] * ( n + 1 )
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , n + 1 ) :
            if ( str [ i - 1 ] == str [ j - 1 ] and i != j ) :
                dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ]
            else :
                dp [ i ] [ j ] = max ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] )
    return dp [ n ] [ n ]
|||

FIND_THE_FIRST_MISSING_NUMBER

def findFirstMissing ( array , start , end ) :
    if ( start > end ) :
        return end + 1
    if ( start != array [ start ] ) :
        return start 
    mid = int ( ( start + end ) / 2 )
    if ( array [ mid ] == mid ) :
        return findFirstMissing ( array , mid + 1 , end )
    return findFirstMissing ( array , start , mid )
|||

SORT_ARRAY_CONVERTING_ELEMENTS_SQUARES_1

def sortSquares ( arr , n ) :
    K = 0
    for K in range ( n ) :
        if ( arr [ K ] >= 0 ) :
            break
    i = K - 1
    j = K
    ind = 0
    temp = [ 0 ] * n
    while ( i >= 0 and j < n ) :
        if ( arr [ i ] * arr [ i ] < arr [ j ] * arr [ j ] ) :
            temp [ ind ] = arr [ i ] * arr [ i ]
            i -= 1
        else :
            temp [ ind ] = arr [ j ] * arr [ j ]
            j += 1
        ind += 1
    while ( i >= 0 ) :
        temp [ ind ] = arr [ i ] * arr [ i ]
        i -= 1
        ind += 1
    while ( j < n ) :
        temp [ ind ] = arr [ j ] * arr [ j ]
        j += 1
        ind += 1
    for i in range ( n ) :
        arr [ i ] = temp [ i ]
|||

PROGRAM_TO_FIND_REMAINDER_WITHOUT_USING_MODULO_OR_OPERATOR

def getRemainder ( num , divisor ) :
    return ( num - divisor * ( num // divisor ) )
|||

MINIMUM_COST_TO_FILL_GIVEN_WEIGHT_IN_A_BAG

def MinimumCost ( cost , n , W ) :
    val = list ( )
    wt = list ( )
    size = 0
    for i in range ( n ) :
        if ( cost [ i ] != - 1 ) :
            val.append ( cost [ i ] )
            wt.append ( i + 1 )
            size += 1
    n = size
    min_cost = [ [ 0 for i in range ( W + 1 ) ] for j in range ( n + 1 ) ]
    for i in range ( W + 1 ) :
        min_cost [ 0 ] [ i ] = INF
    for i in range ( 1 , n + 1 ) :
        min_cost [ i ] [ 0 ] = 0
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , W + 1 ) :
            if ( wt [ i - 1 ] > j ) :
                min_cost [ i ] [ j ] = min_cost [ i - 1 ] [ j ]
            else :
                min_cost [ i ] [ j ] = min ( min_cost [ i - 1 ] [ j ] , min_cost [ i ] [ j - wt [ i - 1 ] ] + val [ i - 1 ] )
    if ( min_cost [ n ] [ W ] == INF ) :
        return - 1
    else :
        return min_cost [ n ] [ W ]
|||

COUNT_CHARACTERS_STRING_DISTANCE_ENGLISH_ALPHABETS_1

def countPairs ( str1 ) :
    result = 0 
    n = len ( str1 )
    for i in range ( 0 , n ) :
        for j in range ( 1 , MAX_CHAR + 1 ) :
            if ( ( i + j ) < n ) :
                if ( ( abs ( ord ( str1 [ i + j ] ) - ord ( str1 [ i ] ) ) == j ) ) :
                    result += 1 
    return result
|||

A_PRODUCT_ARRAY_PUZZLE

def productArray ( arr , n ) :
    if ( n == 1 ) :
        print ( 0 )
        return
    left = [ 0 ] * n
    right = [ 0 ] * n
    prod = [ 0 ] * n
    left [ 0 ] = 1
    right [ n - 1 ] = 1
    for i in range ( 1 , n ) :
        left [ i ] = arr [ i - 1 ] * left [ i - 1 ]
    for j in range ( n - 2 , - 1 , - 1 ) :
        right [ j ] = arr [ j + 1 ] * right [ j + 1 ]
    for i in range ( n ) :
        prod [ i ] = left [ i ] * right [ i ]
    for i in range ( n ) :
        print ( prod [ i ] , end = ' ' )
|||

FREQUENT_ELEMENT_ARRAY_1

def mostFrequent ( arr , n ) :
    Hash = dict ( )
    for i in range ( n ) :
        if arr [ i ] in Hash.keys ( ) :
            Hash [ arr [ i ] ] += 1
        else :
            Hash [ arr [ i ] ] = 1
    max_count = 0
    res = - 1
    for i in Hash :
        if ( max_count < Hash [ i ] ) :
            res = i
            max_count = Hash [ i ]
    return res
|||

PRINT_UNIQUE_ROWS

def printArray ( matrix ) :
    rowCount = len ( matrix )
    if rowCount == 0 :
        return
    columnCount = len ( matrix [ 0 ] )
    if columnCount == 0 :
        return
    row_output_format = " ".join ( [ "%s" ] * columnCount )
    printed = { }
    for row in matrix :
        routput = row_output_format % tuple ( row )
        if routput not in printed :
            printed [ routput ] = True
            print ( routput )
|||

COUNT_1S_SORTED_BINARY_ARRAY

def countOnes ( arr , low , high ) :
    if high >= low :
        mid = low + ( high - low ) / 2
        if ( ( mid == high or arr [ mid + 1 ] == 0 ) and ( arr [ mid ] == 1 ) ) :
            return mid + 1
        if arr [ mid ] == 1 :
            return countOnes ( arr , ( mid + 1 ) , high )
        return countOnes ( arr , low , mid - 1 )
    return 0
|||

POSSIBLE_MOVES_KNIGHT

def findPossibleMoves ( mat , p , q ) :
    global n , m 
    X = [ 2 , 1 , - 1 , - 2 , - 2 , - 1 , 1 , 2 ] 
    Y = [ 1 , 2 , 2 , 1 , - 1 , - 2 , - 2 , - 1 ] 
    count = 0 
    for i in range ( 8 ) :
        x = p + X [ i ] 
        y = q + Y [ i ] 
        if ( x >= 0 and y >= 0 and x < n and y < m and mat [ x ] [ y ] == 0 ) :
            count += 1 
    return count 
|||

ROTATE_MATRIX_ELEMENTS

def rotateMatrix ( mat ) :
    if not len ( mat ) :
        return
    top = 0
    bottom = len ( mat ) - 1
    left = 0
    right = len ( mat [ 0 ] ) - 1
    while left < right and top < bottom :
        prev = mat [ top + 1 ] [ left ]
        for i in range ( left , right + 1 ) :
            curr = mat [ top ] [ i ]
            mat [ top ] [ i ] = prev
            prev = curr
        top += 1
        for i in range ( top , bottom + 1 ) :
            curr = mat [ i ] [ right ]
            mat [ i ] [ right ] = prev
            prev = curr
        right -= 1
        for i in range ( right , left - 1 , - 1 ) :
            curr = mat [ bottom ] [ i ]
            mat [ bottom ] [ i ] = prev
            prev = curr
        bottom -= 1
        for i in range ( bottom , top - 1 , - 1 ) :
            curr = mat [ i ] [ left ]
            mat [ i ] [ left ] = prev
            prev = curr
        left += 1
    return mat
|||

FIND_KTH_CHARACTER_OF_DECRYPTED_STRING

def encodedChar ( str , k ) :
    expand = ""
    freq = 0
    i = 0
    while ( i < len ( str ) ) :
        temp = ""
        freq = 0
        while ( i < len ( str ) and ord ( str [ i ] ) >= ord ( 'a' ) and ord ( str [ i ] ) <= ord ( 'z' ) ) :
            temp += str [ i ]
            i += 1
        while ( i < len ( str ) and ord ( str [ i ] ) >= ord ( '1' ) and ord ( str [ i ] ) <= ord ( '9' ) ) :
            freq = freq * 10 + ord ( str [ i ] ) - ord ( '0' )
            i += 1
        for j in range ( 1 , freq + 1 , 1 ) :
            expand += temp
    if ( freq == 0 ) :
        expand += temp
    return expand [ k - 1 ]
|||

EFFICIENT_SEARCH_IN_AN_ARRAY_WHERE_DIFFERENCE_BETWEEN_ADJACENT_IS_1

def search ( arr , n , x ) :
    i = 0
    while ( i <= n - 1 ) :
        if ( arr [ i ] == x ) :
            return i
        i += abs ( arr [ i ] - x )
    return - 1
|||

MAXIMUM_POSSIBLE_SUM_WINDOW_ARRAY_ELEMENTS_WINDOW_ARRAY_UNIQUE

def returnMaxSum ( A , B , n ) :
    mp = set ( )
    result = 0
    curr_sum = curr_begin = 0
    for i in range ( 0 , n ) :
        while A [ i ] in mp :
            mp.remove ( A [ curr_begin ] )
            curr_sum -= B [ curr_begin ]
            curr_begin += 1
        mp.add ( A [ i ] )
        curr_sum += B [ i ]
        result = max ( result , curr_sum )
    return result
|||

WRITE_AN_EFFICIENT_METHOD_TO_CHECK_IF_A_NUMBER_IS_MULTIPLE_OF_3

def isMultipleOf3 ( n ) :
    odd_count = 0
    even_count = 0
    if ( n < 0 ) :
        n = - n
    if ( n == 0 ) :
        return 1
    if ( n == 1 ) :
        return 0
    while ( n ) :
        if ( n & 1 ) :
            odd_count += 1
        if ( n & 2 ) :
            even_count += 1
        n = n >> 2
    return isMultipleOf3 ( abs ( odd_count - even_count ) )
|||

MAXIMUM_SUM_IARRI_AMONG_ROTATIONS_GIVEN_ARRAY_1

def maxSum ( arr , n ) :
    cum_sum = 0
    for i in range ( 0 , n ) :
        cum_sum += arr [ i ]
    curr_val = 0
    for i in range ( 0 , n ) :
        curr_val += i * arr [ i ]
    res = curr_val
    for i in range ( 1 , n ) :
        next_val = ( curr_val - ( cum_sum - arr [ i - 1 ] ) + arr [ i - 1 ] * ( n - 1 ) )
        curr_val = next_val
        res = max ( res , next_val )
    return res
|||

DYNAMIC_PROGRAMMING_SET_34_ASSEMBLY_LINE_SCHEDULING

def carAssembly ( a , t , e , x ) :
    NUM_STATION = len ( a [ 0 ] )
    T1 = [ 0 for i in range ( NUM_STATION ) ]
    T2 = [ 0 for i in range ( NUM_STATION ) ]
    T1 [ 0 ] = e [ 0 ] + a [ 0 ] [ 0 ]
    T2 [ 0 ] = e [ 1 ] + a [ 1 ] [ 0 ]
    for i in range ( 1 , NUM_STATION ) :
        T1 [ i ] = min ( T1 [ i - 1 ] + a [ 0 ] [ i ] , T2 [ i - 1 ] + t [ 1 ] [ i ] + a [ 0 ] [ i ] )
        T2 [ i ] = min ( T2 [ i - 1 ] + a [ 1 ] [ i ] , T1 [ i - 1 ] + t [ 0 ] [ i ] + a [ 1 ] [ i ] )
    return min ( T1 [ NUM_STATION - 1 ] + x [ 0 ] , T2 [ NUM_STATION - 1 ] + x [ 1 ] )
|||

PRINT_MATRIX_SPIRAL_FORM_STARTING_POINT

def printSpiral ( mat , r , c ) :
    a = 0
    b = 2
    low_row = 0 if ( 0 > a ) else a
    low_column = 0 if ( 0 > b ) else b - 1
    high_row = r - 1 if ( ( a + 1 ) >= r ) else a + 1
    high_column = c - 1 if ( ( b + 1 ) >= c ) else b + 1
    while ( ( low_row > 0 - r and low_column > 0 - c ) ) :
        i = low_column + 1
        while ( i <= high_column and i < c and low_row >= 0 ) :
            print ( mat [ low_row ] [ i ] , end = " " )
            i += 1
        low_row -= 1
        i = low_row + 2
        while ( i <= high_row and i < r and high_column < c ) :
            print ( mat [ i ] [ high_column ] , end = " " )
            i += 1
        high_column += 1
        i = high_column - 2
        while ( i >= low_column and i >= 0 and high_row < r ) :
            print ( mat [ high_row ] [ i ] , end = " " )
            i -= 1
        high_row += 1
        i = high_row - 2
        while ( i > low_row and i >= 0 and low_column >= 0 ) :
            print ( mat [ i ] [ low_column ] , end = " " )
            i -= 1
        low_column -= 1
    print ( )
|||

MID_POINT_CIRCLE_DRAWING_ALGORITHM

def midPointCircleDraw ( x_centre , y_centre , r ) :
    x = r
    y = 0
    print ( "(" , x + x_centre , ", " , y + y_centre , ")" , sep = "" , end = "" )
    if ( r > 0 ) :
        print ( "(" , x + x_centre , ", " , - y + y_centre , ")" , sep = "" , end = "" )
        print ( "(" , y + x_centre , ", " , x + y_centre , ")" , sep = "" , end = "" )
        print ( "(" , - y + x_centre , ", " , x + y_centre , ")" , sep = "" )
    P = 1 - r
    while ( x > y ) :
        y += 1
        if ( P <= 0 ) :
            P = P + 2 * y + 1
        else :
            x -= 1
            P = P + 2 * y - 2 * x + 1
        if ( x < y ) :
            break
        print ( "(" , x + x_centre , ", " , y + y_centre , ")" , sep = "" , end = "" )
        print ( "(" , - x + x_centre , ", " , y + y_centre , ")" , sep = "" , end = "" )
        print ( "(" , x + x_centre , ", " , - y + y_centre , ")" , sep = "" , end = "" )
        print ( "(" , - x + x_centre , ", " , - y + y_centre , ")" , sep = "" )
        if ( x != y ) :
            print ( "(" , y + x_centre , ", " , x + y_centre , ")" , sep = "" , end = "" )
            print ( "(" , - y + x_centre , ", " , x + y_centre , ")" , sep = "" , end = "" )
            print ( "(" , y + x_centre , ", " , - x + y_centre , ")" , sep = "" , end = "" )
            print ( "(" , - y + x_centre , ", " , - x + y_centre , ")" , sep = "" )
|||

SMALLEST_ELEMENT_REPEATED_EXACTLY_K_TIMES_NOT_LIMITED_SMALL_RANGE

def smallestKFreq ( arr , n , k ) :
    mp = defaultdict ( lambda : 0 )
    for i in range ( n ) :
        mp [ arr [ i ] ] += 1
    res = sys.maxsize
    res1 = sys.maxsize
    for key , values in mp.items ( ) :
        if values == k :
            res = min ( res , key )
    return res if res != res1 else - 1
|||

MINIMUM_XOR_VALUE_PAIR

def minXOR ( arr , n ) :
    arr.sort ( ) 
    min_xor = 999999
    val = 0
    for i in range ( 0 , n - 1 ) :
        for j in range ( i + 1 , n - 1 ) :
            val = arr [ i ] ^ arr [ j ]
            min_xor = min ( min_xor , val )
    return min_xor
|||

MIRROR_CHARACTERS_STRING

def compute ( st , n ) :
    reverseAlphabet = "zyxwvutsrqponmlkjihgfedcba"
    l = len ( st )
    answer = ""
    for i in range ( 0 , n ) :
        answer = answer + st [ i ] 
    for i in range ( n , l ) :
        answer = ( answer + reverseAlphabet [ ord ( st [ i ] ) - ord ( 'a' ) ] ) 
    return answer 
|||

PROGRAM_CHECK_PLUS_PERFECT_NUMBER

def checkplusperfect ( x ) :
    temp = x
    n = 0
    while ( x != 0 ) :
        x = x // 10
        n = n + 1
    x = temp
    sm = 0
    while ( x != 0 ) :
        sm = sm + ( int ) ( math.pow ( x % 10 , n ) )
        x = x // 10
    return ( sm == temp )
|||

ARC_LENGTH_ANGLE

def arcLength ( diameter , angle ) :
    if angle >= 360 :
        print ( "Angle cannot be formed" )
        return 0
    else :
        arc = ( 3.142857142857143 * diameter ) * ( angle / 360.0 )
        return arc
|||

FIND_LAST_INDEX_CHARACTER_STRING

def findLastIndex ( str , x ) :
    index = - 1
    for i in range ( 0 , len ( str ) ) :
        if str [ i ] == x :
            index = i
    return index
|||

COUNT_TRAILING_ZEROES_FACTORIAL_NUMBER

def findTrailingZeros ( n ) :
    count = 0
    i = 5
    while ( n / i >= 1 ) :
        count += int ( n / i )
        i *= 5
    return int ( count )
|||

ROTATE_MATRIX_180_DEGREE

def rotateMatrix ( mat ) :
    i = N - 1 
    while ( i >= 0 ) :
        j = N - 1 
        while ( j >= 0 ) :
            print ( mat [ i ] [ j ] , end = " " ) 
            j = j - 1 
        print ( ) 
        i = i - 1 
|||

SUM_FIBONACCI_NUMBERS

def calculateSum ( n ) :
    if ( n <= 0 ) :
        return 0
    fibo = [ 0 ] * ( n + 1 )
    fibo [ 1 ] = 1
    sm = fibo [ 0 ] + fibo [ 1 ]
    for i in range ( 2 , n + 1 ) :
        fibo [ i ] = fibo [ i - 1 ] + fibo [ i - 2 ]
        sm = sm + fibo [ i ]
    return sm
|||

LARGEST_LEXICOGRAPHIC_ARRAY_WITH_AT_MOST_K_CONSECUTIVE_SWAPS

def KSwapMaximum ( n , k ) :
    global arr
    for i in range ( 0 , n - 1 ) :
        if ( k > 0 ) :
            indexPosition = i
            for j in range ( i + 1 , n ) :
                if ( k <= j - i ) :
                    break
                if ( arr [ j ] > arr [ indexPosition ] ) :
                    indexPosition = j
            for j in range ( indexPosition , i , - 1 ) :
                t = arr [ j ]
                arr [ j ] = arr [ j - 1 ]
                arr [ j - 1 ] = t
            k = k - indexPosition - i
|||

FIND_WHETHER_GIVEN_INTEGER_POWER_3_NOT

def check ( n ) :
    return 1162261467 % n == 0
|||

FIND_THE_TWO_REPEATING_ELEMENTS_IN_A_GIVEN_ARRAY

def printRepeating ( arr , size ) :
    print ( "Repeating elements are " , end = '' )
    for i in range ( 0 , size ) :
        for j in range ( i + 1 , size ) :
            if arr [ i ] == arr [ j ] :
                print ( arr [ i ] , end = ' ' )
|||

C_PROGRAM_FIND_AREA_TRIANGLE

def findArea ( a , b , c ) :
    if ( a < 0 or b < 0 or c < 0 or ( a + b <= c ) or ( a + c <= b ) or ( b + c <= a ) ) :
        print ( 'Not a valid trianglen' )
        return
    s = ( a + b + c ) / 2
    area = ( s * ( s - a ) * ( s - b ) * ( s - c ) ) ** 0.5
    print ( 'Area of a traingle is %f' % area )
|||

GIVEN_LARGE_NUMBER_CHECK_SUBSEQUENCE_DIGITS_DIVISIBLE_8_1

def isSubSeqDivisible ( str ) :
    n = len ( str )
    dp = [ [ 0 for i in range ( 10 ) ] for i in range ( n + 1 ) ]
    arr = [ 0 for i in range ( n + 1 ) ]
    for i in range ( 1 , n + 1 ) :
        arr [ i ] = int ( str [ i - 1 ] ) 
    for i in range ( 1 , n + 1 ) :
        dp [ i ] [ arr [ i ] % 8 ] = 1 
        for j in range ( 8 ) :
            if ( dp [ i - 1 ] [ j ] > dp [ i ] [ ( j * 10 + arr [ i ] ) % 8 ] ) :
                dp [ i ] [ ( j * 10 + arr [ i ] ) % 8 ] = dp [ i - 1 ] [ j ]
            if ( dp [ i - 1 ] [ j ] > dp [ i ] [ j ] ) :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j ]
    for i in range ( 1 , n + 1 ) :
        if ( dp [ i ] [ 0 ] == 1 ) :
            return True
    return False
|||

DELETE_ARRAY_ELEMENTS_WHICH_ARE_SMALLER_THAN_NEXT_OR_BECOME_SMALLER

def deleteElements ( arr , n , k ) :
    st = [ ]
    st.append ( arr [ 0 ] )
    top = 0
    count = 0
    for i in range ( 1 , n ) :
        while ( len ( st ) != 0 and count < k and st [ top ] < arr [ i ] ) :
            st.pop ( )
            count += 1
            top -= 1
        st.append ( arr [ i ] )
        top += 1
    for i in range ( 0 , len ( st ) ) :
        print ( st [ i ] , "" , end = "" )
|||

MINIMUM_LENGTH_SUBARRAY_SUM_GREATER_GIVEN_VALUE

def smallestSubWithSum ( arr , n , x ) :
    curr_sum = 0
    min_len = n + 1
    start = 0
    end = 0
    while ( end < n ) :
        while ( curr_sum <= x and end < n ) :
            curr_sum += arr [ end ]
            end += 1
        while ( curr_sum > x and start < n ) :
            if ( end - start < min_len ) :
                min_len = end - start
            curr_sum -= arr [ start ]
            start += 1
    return min_len
|||

FIND_PAIRS_IN_ARRAY_WHOSE_SUMS_ALREADY_EXIST_IN_ARRAY_1

def findPair ( arr , n ) :
    s = { i : 1 for i in arr }
    found = False
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if arr [ i ] + arr [ j ] in s.keys ( ) :
                print ( arr [ i ] , arr [ j ] )
                found = True
    if found == False :
        print ( "Not exist" )
|||

COUNT_ARITHMETIC_PROGRESSION_SUBSEQUENCES_ARRAY

def numofAP ( a , n ) :
    minarr = + 2147483647
    maxarr = - 2147483648
    for i in range ( n ) :
        minarr = min ( minarr , a [ i ] )
        maxarr = max ( maxarr , a [ i ] )
    dp = [ 0 for i in range ( n + 1 ) ]
    ans = n + 1
    for d in range ( ( minarr - maxarr ) , ( maxarr - minarr ) + 1 ) :
        sum = [ 0 for i in range ( MAX + 1 ) ]
        for i in range ( n ) :
            dp [ i ] = 1
            if ( a [ i ] - d >= 1 and a [ i ] - d <= 1000000 ) :
                dp [ i ] += sum [ a [ i ] - d ]
            ans += dp [ i ] - 1
            sum [ a [ i ] ] += dp [ i ]
    return ans
|||

COUNT_NUMBERS_THAT_DONT_CONTAIN_3

def count ( n ) :
    if n < 3 :
        return n
    elif n >= 3 and n < 10 :
        return n - 1
    po = 1
    while n / po > 9 :
        po = po * 10
    msd = n / po
    if msd != 3 :
        return count ( msd ) * count ( po - 1 ) + count ( msd ) + count ( n % po )
    else :
        return count ( msd * po - 1 )
|||

PROGRAM_TO_FIND_TRANSPOSE_OF_A_MATRIX_2

def transpose ( A ) :
    for i in range ( N ) :
        for j in range ( i + 1 , N ) :
            A [ i ] [ j ] , A [ j ] [ i ] = A [ j ] [ i ] , A [ i ] [ j ]
|||

SUM_DIAGONALS_SPIRAL_ODD_ORDER_SQUARE_MATRIX

def spiralDiaSum ( n ) :
    if n == 1 :
        return 1
    return ( 4 * n * n - 6 * n + 6 + spiralDiaSum ( n - 2 ) )
|||

COUNT_INVERSIONS_OF_SIZE_THREE_IN_A_GIVE_ARRAY

def getInvCount ( arr ) :
    n = len ( arr )
    invcount = 0
    for i in range ( 0 , n - 1 ) :
        for j in range ( i + 1 , n ) :
            if arr [ i ] > arr [ j ] :
                for k in range ( j + 1 , n ) :
                    if arr [ j ] > arr [ k ] :
                        invcount += 1
    return invcount
|||

FIND_SUM_NODES_GIVEN_PERFECT_BINARY_TREE

def SumNodes ( l ) :
    leafNodeCount = pow ( 2 , l - 1 )
    vec = [ [ ] for i in range ( l ) ]
    for i in range ( 1 , leafNodeCount + 1 ) :
        vec [ l - 1 ].append ( i )
    for i in range ( l - 2 , - 1 , - 1 ) :
        k = 0
        while ( k < len ( vec [ i + 1 ] ) - 1 ) :
            vec [ i ].append ( vec [ i + 1 ] [ k ] + vec [ i + 1 ] [ k + 1 ] )
            k += 2
    Sum = 0
    for i in range ( l ) :
        for j in range ( len ( vec [ i ] ) ) :
            Sum += vec [ i ] [ j ]
    return Sum
|||

SUM_OF_ALL_PROPER_DIVISORS_OF_A_NATURAL_NUMBER

def divSum ( num ) :
    result = 0
    i = 2
    while i <= ( math.sqrt ( num ) ) :
        if ( num % i == 0 ) :
            if ( i == ( num / i ) ) :
                result = result + i 
            else :
                result = result + ( i + num / i ) 
        i = i + 1
    return ( result + 1 ) 
|||

FIND_A_TRIPLET_THAT_SUM_TO_A_GIVEN_VALUE_2

def find3Numbers ( A , arr_size , sum ) :
    for i in range ( 0 , arr_size - 1 ) :
        s = set ( )
        curr_sum = sum - A [ i ]
        for j in range ( i + 1 , arr_size ) :
            if ( curr_sum - A [ j ] ) in s :
                print ( "Triplet is" , A [ i ] , ", " , A [ j ] , ", " , curr_sum - A [ j ] )
                return True
            s.add ( A [ j ] )
    return False
|||

NTH_EVEN_LENGTH_PALINDROME

def evenlength ( n ) :
    res = n
    for j in range ( len ( n ) - 1 , - 1 , - 1 ) :
        res += n [ j ]
    return res
|||

FINDING_POWER_PRIME_NUMBER_P_N

def PowerOFPINnfactorial ( n , p ) :
    ans = 0 
    temp = p 
    while ( temp <= n ) :
        ans += n / temp 
        temp = temp * p 
    return ans 
|||

MINIMUM_COST_MAKE_LONGEST_COMMON_SUBSEQUENCE_LENGTH_K

def solve ( X , Y , l , r , k , dp ) :
    if k == 0 :
        return 0
    if l < 0 or r < 0 :
        return 1000000000
    if dp [ l ] [ r ] [ k ] != - 1 :
        return dp [ l ] [ r ] [ k ]
    cost = ( ( ord ( X [ l ] ) - ord ( 'a' ) ) ^ ( ord ( Y [ r ] ) - ord ( 'a' ) ) )
    dp [ l ] [ r ] [ k ] = min ( [ cost + solve ( X , Y , l - 1 , r - 1 , k - 1 , dp ) , solve ( X , Y , l - 1 , r , k , dp ) , solve ( X , Y , l , r - 1 , k , dp ) ] )
    return dp [ l ] [ r ] [ k ]
|||

PRINT_STRING_SPECIFIED_CHARACTER_OCCURRED_GIVEN_NO_TIMES

def printString ( str , ch , count ) :
    occ , i = 0 , 0
    if ( count == 0 ) :
        print ( str )
    for i in range ( len ( str ) ) :
        if ( str [ i ] == ch ) :
            occ += 1
        if ( occ == count ) :
            break
    if ( i < len ( str ) - 1 ) :
        print ( str [ i + 1 : len ( str ) - i + 2 ] )
    else :
        print ( "Empty string" )
|||

SORT_1_N_SWAPPING_ADJACENT_ELEMENTS

def sortedAfterSwap ( A , B , n ) :
    for i in range ( 0 , n - 1 ) :
        if ( B [ i ] == 1 ) :
            j = i
            while ( B [ j ] == 1 ) :
                j = j + 1
            A = A [ 0 : i ] + sorted ( A [ i : j + 1 ] ) + A [ j + 1 : ]
            i = j
    for i in range ( 0 , n ) :
        if ( A [ i ] != i + 1 ) :
            return False
    return True
|||

GENERATE_PYTHAGOREAN_TRIPLETS

def pythagoreanTriplets ( limits ) :
    c , m = 0 , 2
    while c < limits :
        for n in range ( 1 , m ) :
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            if c > limits :
                break
            print ( a , b , c )
        m = m + 1
|||

COUNT_EVEN_LENGTH_BINARY_SEQUENCES_WITH_SAME_SUM_OF_FIRST_AND_SECOND_HALF_BITS

def countSeq ( n , diff ) :
    if ( abs ( diff ) > n ) :
        return 0
    if ( n == 1 and diff == 0 ) :
        return 2
    if ( n == 1 and abs ( diff ) == 1 ) :
        return 1
    res = ( countSeq ( n - 1 , diff + 1 ) + 2 * countSeq ( n - 1 , diff ) + countSeq ( n - 1 , diff - 1 ) )
    return res
|||

POSSIBLE_FORM_TRIANGLE_ARRAY_VALUES

def isPossibleTriangle ( arr , N ) :
    if N < 3 :
        return False
    arr.sort ( )
    for i in range ( N - 2 ) :
        if arr [ i ] + arr [ i + 1 ] > arr [ i + 2 ] :
            return True
|||

PRINT_ARRAY_STRINGS_SORTED_ORDER_WITHOUT_COPYING_ONE_STRING_ANOTHER

def printInSortedOrder ( arr , n ) :
    index = [ 0 ] * n
    for i in range ( n ) :
        index [ i ] = i
    for i in range ( n - 1 ) :
        min = i
        for j in range ( i + 1 , n ) :
            if ( arr [ index [ min ] ] > arr [ index [ j ] ] ) :
                min = j
        if ( min != i ) :
            index [ min ] , index [ i ] = index [ i ] , index [ min ]
    for i in range ( n ) :
        print ( arr [ index [ i ] ] , end = " " )
|||

GAME_REPLACING_ARRAY_ELEMENTS

def playGame ( arr , n ) :
    s = set ( )
    for i in range ( n ) :
        s.add ( arr [ i ] )
    return 1 if len ( s ) % 2 == 0 else 2
|||

BASIC_AND_EXTENDED_EUCLIDEAN_ALGORITHMS

def gcd ( a , b ) :
    if a == 0 :
        return b
    return gcd ( b % a , a )
|||

SORT_ARRAY_WAVE_FORM_2_1

def sortInWave ( arr , n ) :
    for i in range ( 0 , n , 2 ) :
        if ( i > 0 and arr [ i ] < arr [ i - 1 ] ) :
            arr [ i ] , arr [ i - 1 ] = arr [ i - 1 ] , arr [ i ]
        if ( i < n - 1 and arr [ i ] < arr [ i + 1 ] ) :
            arr [ i ] , arr [ i + 1 ] = arr [ i + 1 ] , arr [ i ]
|||

MAXIMUM_SUBARRAY_SUM_USING_PREFIX_SUM

def maximumSumSubarray ( arr , n ) :
    min_prefix_sum = 0
    res = - math.inf
    prefix_sum = [ ]
    prefix_sum.append ( arr [ 0 ] )
    for i in range ( 1 , n ) :
        prefix_sum.append ( prefix_sum [ i - 1 ] + arr [ i ] )
    for i in range ( n ) :
        res = max ( res , prefix_sum [ i ] - min_prefix_sum )
        min_prefix_sum = min ( min_prefix_sum , prefix_sum [ i ] )
    return res
|||

STRING_CONTAINING_FIRST_LETTER_EVERY_WORD_GIVEN_STRING_SPACES

def firstLetterWord ( str ) :
    result = ""
    v = True
    for i in range ( len ( str ) ) :
        if ( str [ i ] == ' ' ) :
            v = True
        elif ( str [ i ] != ' ' and v == True ) :
            result += ( str [ i ] )
            v = False
    return result
|||

SUM_PAIRWISE_PRODUCTS_1

def findSum ( n ) :
    multiTerms = n * ( n + 1 ) // 2
    sm = multiTerms
    for i in range ( 2 , n + 1 ) :
        multiTerms = multiTerms - ( i - 1 )
        sm = sm + multiTerms * i
    return sm
|||

CLUSTERINGPARTITIONING_AN_ARRAY_SUCH_THAT_SUM_OF_SQUARE_DIFFERENCES_IS_MINIMUM_1

def minCost ( a , n , k ) :
    dp = [ [ inf for i in range ( k + 1 ) ] for j in range ( n + 1 ) ] 
    dp [ 0 ] [ 0 ] = 0 
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , k + 1 ) :
            for m in range ( i - 1 , - 1 , - 1 ) :
                dp [ i ] [ j ] = min ( dp [ i ] [ j ] , dp [ m ] [ j - 1 ] + ( a [ i - 1 ] - a [ m ] ) * ( a [ i - 1 ] - a [ m ] ) ) 
    return dp [ n ] [ k ] 
|||

LEIBNIZ_HARMONIC_TRIANGLE

def LeibnizHarmonicTriangle ( n ) :
    C = [ [ 0 for x in range ( n + 1 ) ] for y in range ( n + 1 ) ] 
    for i in range ( 0 , n + 1 ) :
        for j in range ( 0 , min ( i , n ) + 1 ) :
            if ( j == 0 or j == i ) :
                C [ i ] [ j ] = 1 
            else :
                C [ i ] [ j ] = ( C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ] ) 
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , i + 1 ) :
            print ( "1/" , end = "" ) 
            print ( i * C [ i - 1 ] [ j - 1 ] , end = " " ) 
        print ( ) 
|||

CHECK_WHETHER_SECOND_STRING_CAN_FORMED_FIRST_STRING_USING_COUNT_ARRAY

def canMakeStr2 ( s1 , s2 ) :
    count = { s1 [ i ] : 0 for i in range ( len ( s1 ) ) }
    for i in range ( len ( s1 ) ) :
        count [ s1 [ i ] ] += 1
    for i in range ( len ( s2 ) ) :
        if count [ s2 [ i ] ] == 0 :
            return False
        count [ s2 [ i ] ] -= 1
    return True
|||

SUM_MINIMUM_MAXIMUM_ELEMENTS_SUBARRAYS_SIZE_K

def SumOfKsubArray ( arr , n , k ) :
    Sum = 0
    S = deque ( )
    G = deque ( )
    for i in range ( k ) :
        while ( len ( S ) > 0 and arr [ S [ - 1 ] ] >= arr [ i ] ) :
            S.pop ( )
        while ( len ( G ) > 0 and arr [ G [ - 1 ] ] <= arr [ i ] ) :
            G.pop ( )
        G.append ( i )
        S.append ( i )
    for i in range ( k , n ) :
        Sum += arr [ S [ 0 ] ] + arr [ G [ 0 ] ]
        while ( len ( S ) > 0 and S [ 0 ] <= i - k ) :
            S.popleft ( )
        while ( len ( G ) > 0 and G [ 0 ] <= i - k ) :
            G.popleft ( )
        while ( len ( S ) > 0 and arr [ S [ - 1 ] ] >= arr [ i ] ) :
            S.pop ( )
        while ( len ( G ) > 0 and arr [ G [ - 1 ] ] <= arr [ i ] ) :
            G.pop ( )
        G.append ( i )
        S.append ( i )
    Sum += arr [ S [ 0 ] ] + arr [ G [ 0 ] ]
    return Sum
|||

LONGEST_COMMON_SUBSEQUENCE

def lcs ( X , Y , m , n ) :
    if m == 0 or n == 0 :
        return 0 
    elif X [ m - 1 ] == Y [ n - 1 ] :
        return 1 + lcs ( X , Y , m - 1 , n - 1 ) 
    else :
        return max ( lcs ( X , Y , m , n - 1 ) , lcs ( X , Y , m - 1 , n ) ) 
|||

MINIMUM_SUM_ABSOLUTE_DIFFERENCE_PAIRS_TWO_ARRAYS

def findMinSum ( a , b , n ) :
    a.sort ( )
    b.sort ( )
    sum = 0
    for i in range ( n ) :
        sum = sum + abs ( a [ i ] - b [ i ] )
    return sum
|||

COUNT_DISTINCT_NON_NEGATIVE_PAIRS_X_Y_SATISFY_INEQUALITY_XX_YY_N_2

def countSolutions ( n ) :
    res = 0
    x = 0
    while ( x * x < n ) :
        y = 0
        while ( x * x + y * y < n ) :
            res = res + 1
            y = y + 1
        x = x + 1
    return res
|||

FIND_NUMBER_TRANSFORMATION_MAKE_TWO_MATRIX_EQUAL

def countOps ( A , B , m , n ) :
    for i in range ( n ) :
        for j in range ( m ) :
            A [ i ] [ j ] -= B [ i ] [ j ] 
    for i in range ( 1 , n ) :
        for j in range ( 1 , n ) :
            if ( A [ i ] [ j ] - A [ i ] [ 0 ] - A [ 0 ] [ j ] + A [ 0 ] [ 0 ] != 0 ) :
                return - 1 
    result = 0 
    for i in range ( n ) :
        result += abs ( A [ i ] [ 0 ] ) 
    for j in range ( m ) :
        result += abs ( A [ 0 ] [ j ] - A [ 0 ] [ 0 ] ) 
    return ( result ) 
|||

EFFICIENTLY_FIND_FIRST_REPEATED_CHARACTER_STRING_WITHOUT_USING_ADDITIONAL_DATA_STRUCTURE_ONE_TRAVERSAL

def FirstRepeated ( string ) :
    checker = 0
    pos = 0
    for i in string :
        val = ord ( i ) - ord ( 'a' ) 
        if ( ( checker & ( 1 << val ) ) > 0 ) :
            return pos
        checker |= ( 1 << val )
        pos += 1
    return - 1
|||

MAXIMUM_UNIQUE_ELEMENT_EVERY_SUBARRAY_SIZE_K

def find_max ( A , N , K ) :
    Count = dict ( )
    for i in range ( K - 1 ) :
        Count [ A [ i ] ] = Count.get ( A [ i ] , 0 ) + 1
    Myset = dict ( )
    for x in Count :
        if ( Count [ x ] == 1 ) :
            Myset [ x ] = 1
    for i in range ( K - 1 , N ) :
        Count [ A [ i ] ] = Count.get ( A [ i ] , 0 ) + 1
        if ( Count [ A [ i ] ] == 1 ) :
            Myset [ A [ i ] ] = 1
        else :
            del Myset [ A [ i ] ]
        if ( len ( Myset ) == 0 ) :
            print ( "Nothing" )
        else :
            maxm = - 10 ** 9
            for i in Myset :
                maxm = max ( i , maxm )
            print ( maxm )
        x = A [ i - K + 1 ]
        if x in Count.keys ( ) :
            Count [ x ] -= 1
            if ( Count [ x ] == 1 ) :
                Myset [ x ] = 1
            if ( Count [ x ] == 0 ) :
                del Myset [ x ]
|||

MINIMUM_COST_SORT_MATRIX_NUMBERS_0_N2_1

def calculateEnergy ( mat , n ) :
    tot_energy = 0
    for i in range ( n ) :
        for j in range ( n ) :
            q = mat [ i ] [ j ] // n
            i_des = q
            j_des = mat [ i ] [ j ] - ( n * q )
            tot_energy += ( abs ( i_des - i ) + abs ( j_des - j ) )
    return tot_energy
|||

LONGEST_COMMON_SUBSTRING

def LCSubStr ( X , Y , m , n ) :
    LCSuff = [ [ 0 for k in range ( n + 1 ) ] for l in range ( m + 1 ) ]
    result = 0
    for i in range ( m + 1 ) :
        for j in range ( n + 1 ) :
            if ( i == 0 or j == 0 ) :
                LCSuff [ i ] [ j ] = 0
            elif ( X [ i - 1 ] == Y [ j - 1 ] ) :
                LCSuff [ i ] [ j ] = LCSuff [ i - 1 ] [ j - 1 ] + 1
                result = max ( result , LCSuff [ i ] [ j ] )
            else :
                LCSuff [ i ] [ j ] = 0
    return result
|||

MAXIMUM_SUM_BITONIC_SUBARRAY

def maxSumBitonicSubArr ( arr , n ) :
    msis = [ None ] * n
    msds = [ None ] * n
    max_sum = 0
    msis [ 0 ] = arr [ 0 ]
    for i in range ( 1 , n ) :
        if ( arr [ i ] > arr [ i - 1 ] ) :
            msis [ i ] = msis [ i - 1 ] + arr [ i ]
        else :
            msis [ i ] = arr [ i ]
    msds [ n - 1 ] = arr [ n - 1 ]
    for i in range ( n - 2 , - 1 , - 1 ) :
        if ( arr [ i ] > arr [ i + 1 ] ) :
            msds [ i ] = msds [ i + 1 ] + arr [ i ]
        else :
            msds [ i ] = arr [ i ]
    for i in range ( n ) :
        if ( max_sum < ( msis [ i ] + msds [ i ] - arr [ i ] ) ) :
            max_sum = ( msis [ i ] + msds [ i ] - arr [ i ] )
    return max_sum
|||

NEWMAN_CONWAY_SEQUENCE

def sequence ( n ) :
    if n == 1 or n == 2 :
        return 1
    else :
        return sequence ( sequence ( n - 1 ) ) + sequence ( n - sequence ( n - 1 ) ) 
|||

PRINT_TRIPLETS_SORTED_ARRAY_FORM_AP

def printAllAPTriplets ( arr , n ) :
    s = [ ] 
    for i in range ( 0 , n - 1 ) :
        for j in range ( i + 1 , n ) :
            diff = arr [ j ] - arr [ i ] 
            if ( ( arr [ i ] - diff ) in arr ) :
                print ( "{} {} {}".format ( ( arr [ i ] - diff ) , arr [ i ] , arr [ j ] ) , end = "\n" ) 
    s.append ( arr [ i ] ) 
|||

QUERIES_COUNTS_ARRAY_ELEMENTS_VALUES_GIVEN_RANGE

def countInRange ( arr , n , x , y ) :
    count = 0 
    for i in range ( n ) :
        if ( arr [ i ] >= x and arr [ i ] <= y ) :
            count += 1
    return count
|||

HIGHWAY_BILLBOARD_PROBLEM

def maxRevenue ( m , x , revenue , n , t ) :
    maxRev = [ 0 ] * ( m + 1 )
    nxtbb = 0 
    for i in range ( 1 , m + 1 ) :
        if ( nxtbb < n ) :
            if ( x [ nxtbb ] != i ) :
                maxRev [ i ] = maxRev [ i - 1 ]
            else :
                if ( i <= t ) :
                    maxRev [ i ] = max ( maxRev [ i - 1 ] , revenue [ nxtbb ] )
                else :
                    maxRev [ i ] = max ( maxRev [ i - t - 1 ] + revenue [ nxtbb ] , maxRev [ i - 1 ] ) 
                nxtbb += 1
        else :
            maxRev [ i ] = maxRev [ i - 1 ]
    return maxRev [ m ]
|||

CONSTRUCT_GRAPH_GIVEN_DEGREES_VERTICES

def printMat ( degseq , n ) :
    mat = [ [ 0 ] * n for i in range ( n ) ]
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if ( degseq [ i ] > 0 and degseq [ j ] > 0 ) :
                degseq [ i ] -= 1
                degseq [ j ] -= 1
                mat [ i ] [ j ] = 1
                mat [ j ] [ i ] = 1
    print ( "      " , end = "" )
    for i in range ( n ) :
        print ( "" , "(" , i , ")" , end = "" )
    print ( )
    print ( )
    for i in range ( n ) :
        print ( "" , "(" , i , ")" , end = "" )
        for j in range ( n ) :
            print ( "     " , mat [ i ] [ j ] , end = "" )
        print ( )
|||

DETECT_IF_TWO_INTEGERS_HAVE_OPPOSITE_SIGNS

def oppositeSigns ( x , y ) :
    return ( ( x ^ y ) < 0 ) 
|||

TRIANGULAR_NUMBERS_1

def isTriangular ( num ) :
    if ( num < 0 ) :
        return False
    c = ( - 2 * num )
    b , a = 1 , 1
    d = ( b * b ) - ( 4 * a * c )
    if ( d < 0 ) :
        return False
    root1 = ( - b + math.sqrt ( d ) ) / ( 2 * a )
    root2 = ( - b - math.sqrt ( d ) ) / ( 2 * a )
    if ( root1 > 0 and math.floor ( root1 ) == root1 ) :
        return True
    if ( root2 > 0 and math.floor ( root2 ) == root2 ) :
        return True
    return False
|||

FIND_WHETHER_A_GIVEN_NUMBER_IS_A_POWER_OF_4_OR_NOT

def isPowerOfFour ( n ) :
    if ( n == 0 ) :
        return False
    while ( n != 1 ) :
        if ( n % 4 != 0 ) :
            return False
        n = n // 4
    return True
|||

LAST_NON_ZERO_DIGIT_FACTORIAL

def lastNon0Digit ( n ) :
    if ( n < 10 ) :
        return dig [ n ]
    if ( ( ( n // 10 ) % 10 ) % 2 == 0 ) :
        return ( 6 * lastNon0Digit ( n // 5 ) * dig [ n % 10 ] ) % 10
    else :
        return ( 4 * lastNon0Digit ( n // 5 ) * dig [ n % 10 ] ) % 10
    return 0
|||

SORT_STRING_ACCORDING_ORDER_DEFINED_ANOTHER_STRING

def sortByPattern ( str , pat ) :
    global MAX_CHAR
    count = [ 0 ] * MAX_CHAR
    for i in range ( 0 , len ( str ) ) :
        count [ ord ( str [ i ] ) - 97 ] += 1
    index = 0 
    str = ""
    for i in range ( 0 , len ( pat ) ) :
        j = 0
        while ( j < count [ ord ( pat [ i ] ) - ord ( 'a' ) ] ) :
            str += pat [ i ]
            j = j + 1
            index += 1
    return str
|||

NUMBER_VISIBLE_BOXES_PUTTING_ONE_INSIDE_ANOTHER

def minimumBox ( arr , n ) :
    q = collections.deque ( [ ] )
    arr.sort ( )
    q.append ( arr [ 0 ] )
    for i in range ( 1 , n ) :
        now = q [ 0 ]
        if ( arr [ i ] >= 2 * now ) :
            q.popleft ( )
        q.append ( arr [ i ] )
    return len ( q )
|||

SEARCH_INSERT_AND_DELETE_IN_A_SORTED_ARRAY

def binarySearch ( arr , low , high , key ) :
    if ( high < low ) :
        return - 1
    mid = ( low + high ) / 2
    if ( key == arr [ int ( mid ) ] ) :
        return mid
    if ( key > arr [ int ( mid ) ] ) :
        return binarySearch ( arr , ( mid + 1 ) , high , key )
    return ( binarySearch ( arr , low , ( mid - 1 ) , key ) )
|||

FIND_THE_TWO_REPEATING_ELEMENTS_IN_A_GIVEN_ARRAY_3

def printRepeating ( arr , size ) :
    print ( " The repeating elements are" , end = " " )
    for i in range ( 0 , size ) :
        if ( arr [ abs ( arr [ i ] ) ] > 0 ) :
            arr [ abs ( arr [ i ] ) ] = ( - 1 ) * arr [ abs ( arr [ i ] ) ]
        else :
            print ( abs ( arr [ i ] ) , end = " " )
|||

COUNT_POSSIBLE_GROUPS_SIZE_2_3_SUM_MULTIPLE_3

def findgroups ( arr , n ) :
    c = [ 0 , 0 , 0 ]
    res = 0
    for i in range ( 0 , n ) :
        c [ arr [ i ] % 3 ] += 1
    res += ( ( c [ 0 ] * ( c [ 0 ] - 1 ) ) >> 1 )
    res += c [ 1 ] * c [ 2 ]
    res += ( c [ 0 ] * ( c [ 0 ] - 1 ) * ( c [ 0 ] - 2 ) ) / 6
    res += ( c [ 1 ] * ( c [ 1 ] - 1 ) * ( c [ 1 ] - 2 ) ) / 6
    res += ( ( c [ 2 ] * ( c [ 2 ] - 1 ) * ( c [ 2 ] - 2 ) ) / 6 )
    res += c [ 0 ] * c [ 1 ] * c [ 2 ]
    return res
|||

PRINT_STRING_IGNORING_ALTERNATE_OCCURRENCES_CHARACTER

def printStringAlternate ( string ) :
    occ = { }
    for i in range ( 0 , len ( string ) ) :
        temp = string [ i ].lower ( )
        occ [ temp ] = occ.get ( temp , 0 ) + 1
        if occ [ temp ] & 1 :
            print ( string [ i ] , end = "" )
    print ( )
|||

NUMBER_DAYS_TANK_WILL_BECOME_EMPTY

def minDaysToEmpty ( C , l ) :
    if ( l >= C ) : return C
    eq_root = ( math.sqrt ( 1 + 8 * ( C - l ) ) - 1 ) / 2
    return math.ceil ( eq_root ) + l
|||

REVERSE_STRING_WITHOUT_USING_ANY_TEMPORARY_VARIABLE

def reversingString ( str , start , end ) :
    while ( start < end ) :
        str = ( str [ : start ] + chr ( ord ( str [ start ] ) ^ ord ( str [ end ] ) ) + str [ start + 1 : ] ) 
        str = ( str [ : end ] + chr ( ord ( str [ start ] ) ^ ord ( str [ end ] ) ) + str [ end + 1 : ] ) 
        str = ( str [ : start ] + chr ( ord ( str [ start ] ) ^ ord ( str [ end ] ) ) + str [ start + 1 : ] ) 
        start += 1 
        end -= 1 
    return str 
|||

FREQUENCY_ELEMENT_UNSORTED_ARRAY

def countFreq ( a , n ) :
    hm = { }
    for i in range ( 0 , n ) :
        hm [ a [ i ] ] = hm.get ( a [ i ] , 0 ) + 1
    st = set ( )
    for x in hm :
        st.add ( ( x , hm [ x ] ) )
    cumul = 0
    for x in sorted ( st ) :
        cumul += x [ 1 ]
        print ( x [ 0 ] , cumul )
|||

FIND_ROTATION_COUNT_ROTATED_SORTED_ARRAY

def countRotations ( arr , n ) :
    min = arr [ 0 ]
    for i in range ( 0 , n ) :
        if ( min > arr [ i ] ) :
            min = arr [ i ]
            min_index = i
    return min_index 
|||

LONGEST_INCREASING_SUBSEQUENCE_1

def lis ( arr ) :
    n = len ( arr )
    lis = [ 1 ] * n
    for i in range ( 1 , n ) :
        for j in range ( 0 , i ) :
            if arr [ i ] > arr [ j ] and lis [ i ] < lis [ j ] + 1 :
                lis [ i ] = lis [ j ] + 1
    maximum = 0
    for i in range ( n ) :
        maximum = max ( maximum , lis [ i ] )
    return maximum
|||

MEDIAN_OF_TWO_SORTED_ARRAYS

def getMedian ( ar1 , ar2 , n ) :
    i = 0
    j = 0
    m1 = - 1
    m2 = - 1
    count = 0
    while count < n + 1 :
        count += 1
        if i == n :
            m1 = m2
            m2 = ar2 [ 0 ]
            break
        elif j == n :
            m1 = m2
            m2 = ar1 [ 0 ]
            break
        if ar1 [ i ] < ar2 [ j ] :
            m1 = m2
            m2 = ar1 [ i ]
            i += 1
        else :
            m1 = m2
            m2 = ar2 [ j ]
            j += 1
    return ( m1 + m2 ) / 2
|||

LEXICOGRAPHICALLY_MINIMUM_STRING_ROTATION

def minLexRotation ( str_ ) :
    n = len ( str_ )
    arr = [ 0 ] * n
    concat = str_ + str_
    for i in range ( n ) :
        arr [ i ] = concat [ i : n + i ]
    arr.sort ( )
    return arr [ 0 ]
|||

INTERPOLATION_SEARCH

def interpolationSearch ( arr , n , x ) :
    lo = 0
    hi = ( n - 1 )
    while lo <= hi and x >= arr [ lo ] and x <= arr [ hi ] :
        if lo == hi :
            if arr [ lo ] == x :
                return lo 
            return - 1 
        pos = lo + int ( ( ( float ( hi - lo ) / ( arr [ hi ] - arr [ lo ] ) ) * ( x - arr [ lo ] ) ) )
        if arr [ pos ] == x :
            return pos
        if arr [ pos ] < x :
            lo = pos + 1 
        else :
            hi = pos - 1 
    return - 1
|||

COUNT_PAIRS_TWO_SORTED_ARRAYS_WHOSE_SUM_EQUAL_GIVEN_VALUE_X_2

def countPairs ( arr1 , arr2 , m , n , x ) :
    count , l , r = 0 , 0 , n - 1
    while ( l < m and r >= 0 ) :
        if ( ( arr1 [ l ] + arr2 [ r ] ) == x ) :
            l += 1
            r -= 1
            count += 1
        elif ( ( arr1 [ l ] + arr2 [ r ] ) < x ) :
            l += 1
        else :
            r -= 1
    return count
|||

COUNT_SUBSETS_DISTINCT_EVEN_NUMBERS

def countSubSets ( arr , n ) :
    us = set ( )
    even_count = 0
    for i in range ( n ) :
        if arr [ i ] % 2 == 0 :
            us.add ( arr [ i ] )
    for i in us :
        even_count += 1
    return pow ( 2 , even_count ) - 1
|||

COUNT_NUMBER_OF_OCCURRENCES_OR_FREQUENCY_IN_A_SORTED_ARRAY

def countOccurrences ( arr , n , x ) :
    res = 0
    for i in range ( n ) :
        if x == arr [ i ] :
            res += 1
    return res
|||

CONSTRUCT_THE_ROOTED_TREE_BY_USING_START_AND_FINISH_TIME_OF_ITS_DFS_TRAVERSAL

def Restore_Tree ( S , E ) :
    Identity = N * [ 0 ]
    for i in range ( N ) :
        Identity [ Start [ i ] ] = i
    parent = N * [ - 1 ]
    curr_parent = Identity [ 0 ]
    for j in range ( 1 , N ) :
        child = Identity [ j ]
        if End [ child ] - j > 1 :
            parent [ child ] = curr_parent
            curr_parent = child
        else :
            parent [ child ] = curr_parent
            while End [ child ] == End [ parent [ child ] ] :
                child = parent [ child ]
                curr_parent = parent [ child ]
                if curr_parent == Identity [ 0 ] :
                    break
    for i in range ( N ) :
        parent [ i ] += 1
    return parent
|||

NUMBER_SUBSEQUENCES_AB_STRING_REPEATED_K_TIMES

def countOccurrences ( s , K ) :
    n = len ( s )
    c1 = 0
    c2 = 0
    C = 0
    for i in range ( n ) :
        if s [ i ] == 'a' :
            c1 += 1
        if s [ i ] == 'b' :
            c2 += 1
            C += c1
    return C * K + ( K * ( K - 1 ) / 2 ) * c1 * c2
|||

NUMBER_SUBSTRINGS_STRING

def countNonEmptySubstr ( str ) :
    n = len ( str ) 
    return int ( n * ( n + 1 ) / 2 ) 
|||

MAXIMUM_NUMBER_CHARACTERS_TWO_CHARACTER_STRING_1

def maximumChars ( str1 ) :
    n = len ( str1 )
    res = - 1
    firstInd = [ - 1 for i in range ( MAX_CHAR ) ]
    for i in range ( n ) :
        first_ind = firstInd [ ord ( str1 [ i ] ) ]
        if ( first_ind == - 1 ) :
            firstInd [ ord ( str1 [ i ] ) ] = i
        else :
            res = max ( res , abs ( i - first_ind - 1 ) )
    return res
|||

SUM_SQUARES_BINOMIAL_COEFFICIENTS

def sumofsquare ( n ) :
    C = [ [ 0 for i in range ( n + 1 ) ] for j in range ( n + 1 ) ]
    for i in range ( 0 , n + 1 ) :
        for j in range ( 0 , min ( i , n ) + 1 ) :
            if ( j == 0 or j == i ) :
                C [ i ] [ j ] = 1
            else :
                C [ i ] [ j ] = ( C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ] )
    sum = 0
    for i in range ( 0 , n + 1 ) :
        sum = sum + ( C [ n ] [ i ] * C [ n ] [ i ] )
    return sum
|||

PRINT_POSSIBLE_STRINGS_CAN_MADE_PLACING_SPACES_2

def printSubsequences ( str ) :
    n = len ( str )
    opsize = int ( pow ( 2 , n - 1 ) )
    for counter in range ( opsize ) :
        for j in range ( n ) :
            print ( str [ j ] , end = "" )
            if ( counter & ( 1 << j ) ) :
                print ( "" , end = "" )
        print ( "\n" , end = "" )
|||

NON_REPEATING_ELEMENT

def firstNonRepeating ( arr , n ) :
    for i in range ( n ) :
        j = 0
        while ( j < n ) :
            if ( i != j and arr [ i ] == arr [ j ] ) :
                break
            j += 1
        if ( j == n ) :
            return arr [ i ]
    return - 1
|||

SUM_OF_ALL_ELEMENTS_UP_TO_NTH_ROW_IN_A_PASCALS_TRIANGLE

def calculateSum ( n ) :
    sum = 0
    for row in range ( n ) :
        sum = sum + ( 1 << row )
    return sum
|||

CHECK_TWO_STRINGS_K_ANAGRAMS_NOT

def arekAnagrams ( str1 , str2 , k ) :
    n = len ( str1 )
    if ( len ( str2 ) != n ) :
        return False
    count1 = [ 0 ] * MAX_CHAR
    count2 = [ 0 ] * MAX_CHAR
    for i in range ( n ) :
        count1 [ ord ( str1 [ i ] ) - ord ( 'a' ) ] += 1
    for i in range ( n ) :
        count2 [ ord ( str2 [ i ] ) - ord ( 'a' ) ] += 1
    count = 0
    for i in range ( MAX_CHAR ) :
        if ( count1 [ i ] > count2 [ i ] ) :
            count = count + abs ( count1 [ i ] - count2 [ i ] )
    return ( count <= k )
|||

LONGEST_SPAN_SUM_TWO_BINARY_ARRAYS

def longestCommonSum ( arr1 , arr2 , n ) :
    maxLen = 0
    for i in range ( 0 , n ) :
        sum1 = 0
        sum2 = 0
        for j in range ( i , n ) :
            sum1 += arr1 [ j ]
            sum2 += arr2 [ j ]
            if ( sum1 == sum2 ) :
                len = j - i + 1
                if ( len > maxLen ) :
                    maxLen = len
    return maxLen
|||

REMAINDER_7_LARGE_NUMBERS

def remainderWith7 ( num ) :
    series = [ 1 , 3 , 2 , - 1 , - 3 , - 2 ] 
    series_index = 0 
    result = 0 
    for i in range ( ( len ( num ) - 1 ) , - 1 , - 1 ) :
        digit = ord ( num [ i ] ) - 48 
        result += digit * series [ series_index ] 
        series_index = ( series_index + 1 ) % 6 
        result %= 7 
    if ( result < 0 ) :
        result = ( result + 7 ) % 7 
    return result 
|||

LEXICOGRAPHICALLY_PREVIOUS_PERMUTATION_IN_C

def prevPermutation ( str ) :
    n = len ( str ) - 1
    i = n
    while ( i > 0 and str [ i - 1 ] <= str [ i ] ) :
        i -= 1
    if ( i <= 0 ) :
        return False
    j = i - 1
    while ( j + 1 <= n and str [ j + 1 ] <= str [ i - 1 ] ) :
        j += 1
    str = list ( str )
    temp = str [ i - 1 ]
    str [ i - 1 ] = str [ j ]
    str [ j ] = temp
    str = ''.join ( str )
    str [ : : - 1 ]
    return True , str
|||

NUMBER_SUBSEQUENCES_FORM_AI_BJ_CK

def countSubsequences ( s ) :
    aCount = 0
    bCount = 0
    cCount = 0
    for i in range ( len ( s ) ) :
        if ( s [ i ] == 'a' ) :
            aCount = ( 1 + 2 * aCount )
        elif ( s [ i ] == 'b' ) :
            bCount = ( aCount + 2 * bCount )
        elif ( s [ i ] == 'c' ) :
            cCount = ( bCount + 2 * cCount )
    return cCount
|||

PROGRAM_PRINT_IDENTITY_MATRIX_1

def isIdentity ( mat , N ) :
    for row in range ( N ) :
        for col in range ( N ) :
            if ( row == col and mat [ row ] [ col ] != 1 ) :
                return False 
            elif ( row != col and mat [ row ] [ col ] != 0 ) :
                return False 
    return True 
|||

MAXIMUM_POSSIBLE_DIFFERENCE_TWO_SUBSETS_ARRAY_1

def maxDiff ( arr , n ) :
    result = 0
    arr.sort ( )
    for i in range ( n - 1 ) :
        if ( abs ( arr [ i ] ) != abs ( arr [ i + 1 ] ) ) :
            result += abs ( arr [ i ] )
        else :
            pass
    if ( arr [ n - 2 ] != arr [ n - 1 ] ) :
        result += abs ( arr [ n - 1 ] )
    return result
|||

PROGRAM_PRINT_SUM_GIVEN_NTH_TERM

def summingSeries ( n ) :
    S = 0
    for i in range ( 1 , n + 1 ) :
        S += i * i - ( i - 1 ) * ( i - 1 )
    return S
|||

PREFIX_SUM_2D_ARRAY

def prefixSum2D ( a ) :
    global C , R
    psa = [ [ 0 for x in range ( C ) ] for y in range ( R ) ]
    psa [ 0 ] [ 0 ] = a [ 0 ] [ 0 ]
    for i in range ( 1 , C ) :
        psa [ 0 ] [ i ] = ( psa [ 0 ] [ i - 1 ] + a [ 0 ] [ i ] )
    for i in range ( 0 , R ) :
        psa [ i ] [ 0 ] = ( psa [ i - 1 ] [ 0 ] + a [ i ] [ 0 ] )
    for i in range ( 1 , R ) :
        for j in range ( 1 , C ) :
            psa [ i ] [ j ] = ( psa [ i - 1 ] [ j ] + psa [ i ] [ j - 1 ] - psa [ i - 1 ] [ j - 1 ] + a [ i ] [ j ] )
    for i in range ( 0 , R ) :
        for j in range ( 0 , C ) :
            print ( psa [ i ] [ j ] , end = " " )
        print ( )
|||

MAXIMUM_NUMBER_2X2_SQUARES_CAN_FIT_INSIDE_RIGHT_ISOSCELES_TRIANGLE

def numberOfSquares ( base ) :
    base = ( base - 2 )
    base = base / 2
    return base * ( base + 1 ) / 2
|||

GIVEN_BINARY_STRING_COUNT_NUMBER_SUBSTRINGS_START_END_1_1

def countSubStr ( st , n ) :
    m = 0
    for i in range ( 0 , n ) :
        if ( st [ i ] == '1' ) :
            m = m + 1
    return m * ( m - 1 ) // 2
|||

CONVERTING_ONE_STRING_USING_APPEND_DELETE_LAST_OPERATIONS

def isConvertible ( str1 , str2 , k ) :
    if ( ( len ( str1 ) + len ( str2 ) ) < k ) :
        return True
    commonLength = 0
    for i in range ( 0 , min ( len ( str1 ) , len ( str2 ) ) , 1 ) :
        if ( str1 [ i ] == str2 [ i ] ) :
            commonLength += 1
        else :
            break
    if ( ( k - len ( str1 ) - len ( str2 ) + 2 * commonLength ) % 2 == 0 ) :
        return True
    return False
|||

FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES_2

def getOddOccurrence ( arr ) :
    res = 0
    for element in arr :
        res = res ^ element
    return res
|||

SUM_MIDDLE_ROW_COLUMN_MATRIX

def middlesum ( mat , n ) :
    row_sum = 0
    col_sum = 0
    for i in range ( n ) :
        row_sum += mat [ n // 2 ] [ i ]
    print ( "Sum of middle row = " , row_sum )
    for i in range ( n ) :
        col_sum += mat [ i ] [ n // 2 ]
    print ( "Sum of middle column = " , col_sum )
|||

K_TH_DISTINCT_OR_NON_REPEATING_ELEMENT_IN_AN_ARRAY

def printKDistinct ( arr , n , k ) :
    dist_count = 0
    for i in range ( n ) :
        j = 0
        while j < n :
            if ( i != j and arr [ j ] == arr [ i ] ) :
                break
            j += 1
        if ( j == n ) :
            dist_count += 1
        if ( dist_count == k ) :
            return arr [ i ]
    return - 1
|||

MERGING_INTERVALS

def mergeIntervals ( arr ) :
    arr.sort ( key = lambda x : x [ 0 ] )
    m = [ ]
    s = - 10000
    max = - 100000
    for i in range ( len ( arr ) ) :
        a = arr [ i ]
        if a [ 0 ] > max :
            if i != 0 :
                m.append ( [ s , max ] )
            max = a [ 1 ]
            s = a [ 0 ]
        else :
            if a [ 1 ] >= max :
                max = a [ 1 ]
    if max != - 100000 and [ s , max ] not in m :
        m.append ( [ s , max ] )
    print ( "The Merged Intervals are :" , end = " " )
    for i in range ( len ( m ) ) :
        print ( m [ i ] , end = " " )
|||

FIND_NUMBER_PERFECT_SQUARES_TWO_GIVEN_NUMBERS_1

def CountSquares ( a , b ) :
    return ( math.floor ( math.sqrt ( b ) ) - math.ceil ( math.sqrt ( a ) ) + 1 )
|||

LARGEST_SUBSET_WHOSE_ALL_ELEMENTS_ARE_FIBONACCI_NUMBERS

def findFibSubset ( arr , n ) :
    m = max ( arr )
    a = 0
    b = 1
    hash = [ ]
    hash.append ( a )
    hash.append ( b )
    while ( b < m ) :
        c = a + b
        a = b
        b = c
        hash.append ( b )
    for i in range ( n ) :
        if arr [ i ] in hash :
            print ( arr [ i ] , end = " " )
|||

LEXICOGRAPHICAL_CONCATENATION_SUBSTRINGS_STRING

def lexicographicSubConcat ( s ) :
    n = len ( s ) 
    sub_count = ( n * ( n + 1 ) ) // 2 
    arr = [ 0 ] * sub_count 
    index = 0 
    for i in range ( n ) :
        for j in range ( 1 , n - i + 1 ) :
            arr [ index ] = s [ i : i + j ] 
            index += 1 
    arr.sort ( ) 
    res = "" 
    for i in range ( sub_count ) :
        res += arr [ i ] 
    return res 
|||

COUNT_OPERATIONS_MAKE_STRINGAB_FREE

def abFree ( s ) :
    b_count = 0
    res = 0
    for i in range ( len ( s ) ) :
        if s [ ~ i ] == 'a' :
            res = ( res + b_count )
            b_count = ( b_count * 2 )
        else :
            b_count += 1
    return res
|||

MAXIMUM_HEIGHT_OF_TRIANGULAR_ARRANGEMENT_OF_ARRAY_VALUES_1

def MaximumHeight ( a , n ) :
    return ( - 1 + int ( math.sqrt ( 1 + ( 8 * n ) ) ) ) // 2
|||

MAXIMIZE_VOLUME_CUBOID_GIVEN_SUM_SIDES

def maxvolume ( s ) :
    maxvalue = 0
    i = 1
    for i in range ( s - 1 ) :
        j = 1
        for j in range ( s ) :
            k = s - i - j
            maxvalue = max ( maxvalue , i * j * k )
    return maxvalue
|||

PROGRAM_DECIMAL_HEXADECIMAL_CONVERSION

def decToHexa ( n ) :
    hexaDeciNum = [ '0' ] * 100 
    i = 0 
    while ( n != 0 ) :
        temp = 0 
        temp = n % 16 
        if ( temp < 10 ) :
            hexaDeciNum [ i ] = chr ( temp + 48 ) 
            i = i + 1 
        else :
            hexaDeciNum [ i ] = chr ( temp + 55 ) 
            i = i + 1 
        n = int ( n / 16 ) 
    j = i - 1 
    while ( j >= 0 ) :
        print ( ( hexaDeciNum [ j ] ) , end = "" ) 
        j = j - 1 
|||

SMALLEST_SUBARRAY_WITH_ALL_OCCURRENCES_OF_A_MOST_FREQUENT_ELEMENT

def smallestSubsegment ( a , n ) :
    left = dict ( )
    count = dict ( )
    mx = 0
    mn , strindex = 0 , 0
    for i in range ( n ) :
        x = a [ i ]
        if ( x not in count.keys ( ) ) :
            left [ x ] = i
            count [ x ] = 1
        else :
            count [ x ] += 1
        if ( count [ x ] > mx ) :
            mx = count [ x ]
            mn = i - left [ x ] + 1
            strindex = left [ x ]
        elif ( count [ x ] == mx and i - left [ x ] + 1 < mn ) :
            mn = i - left [ x ] + 1
            strindex = left [ x ]
    for i in range ( strindex , strindex + mn ) :
        print ( a [ i ] , end = " " )
|||

FIND_LAST_INDEX_CHARACTER_STRING_1

def findLastIndex ( str , x ) :
    for i in range ( len ( str ) - 1 , - 1 , - 1 ) :
        if ( str [ i ] == x ) :
            return i
    return - 1
|||

RECAMANS_SEQUENCE

def recaman ( n ) :
    arr = [ 0 ] * n
    arr [ 0 ] = 0
    print ( arr [ 0 ] , end = ", " )
    for i in range ( 1 , n ) :
        curr = arr [ i - 1 ] - i
        for j in range ( 0 , i ) :
            if ( ( arr [ j ] == curr ) or curr < 0 ) :
                curr = arr [ i - 1 ] + i
                break
        arr [ i ] = curr
        print ( arr [ i ] , end = ", " )
|||

C_PROGRAM_FIND_SECOND_FREQUENT_CHARACTER

def getSecondMostFreq ( str ) :
    NO_OF_CHARS = 256
    count = [ 0 ] * NO_OF_CHARS
    for i in range ( len ( str ) ) :
        count [ ord ( str [ i ] ) ] += 1
    first , second = 0 , 0
    for i in range ( NO_OF_CHARS ) :
        if count [ i ] > count [ first ] :
            second = first
            first = i
        elif ( count [ i ] > count [ second ] and count [ i ] != count [ first ] ) :
            second = i
    return chr ( second )
|||

FIND_MAXIMUM_HEIGHT_PYRAMID_FROM_THE_GIVEN_ARRAY_OF_OBJECTS

def maxLevel ( boxes , n ) :
    boxes.sort ( )
    ans = 1
    prev_width = boxes [ 0 ]
    prev_count = 1
    curr_count = 0
    curr_width = 0
    for i in range ( 1 , n ) :
        curr_width += boxes [ i ]
        curr_count += 1
        if ( curr_width > prev_width and curr_count > prev_count ) :
            prev_width = curr_width
            prev_count = curr_count
            curr_count = 0
            curr_width = 0
            ans += 1
    return ans
|||

COUNTING_INVERSIONS

def getInvCount ( arr , n ) :
    inv_count = 0
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if ( arr [ i ] > arr [ j ] ) :
                inv_count += 1
    return inv_count
|||

SQUARES_OF_MATRIX_DIAGONAL_ELEMENTS

def diagonalsquare ( mat , row , column ) :
    print ( "Diagonal one : " , end = "" )
    for i in range ( 0 , row ) :
        for j in range ( 0 , column ) :
            if ( i == j ) :
                print ( "{} ".format ( mat [ i ] [ j ] * mat [ i ] [ j ] ) , end = "" )
    print ( " \n\nDiagonal two : " , end = "" )
    for i in range ( 0 , row ) :
        for j in range ( 0 , column ) :
            if ( i + j == column - 1 ) :
                print ( "{} ".format ( mat [ i ] [ j ] * mat [ i ] [ j ] ) , end = "" )
|||

ROW_WISE_COMMON_ELEMENTS_TWO_DIAGONALS_SQUARE_MATRIX

def countCommon ( mat , n ) :
    res = 0
    for i in range ( n ) :
        if mat [ i ] [ i ] == mat [ i ] [ n - i - 1 ] :
            res = res + 1
    return res
|||

EULERIAN_NUMBER

def eulerian ( n , m ) :
    if ( m >= n or n == 0 ) :
        return 0 
    if ( m == 0 ) :
        return 1 
    return ( ( n - m ) * eulerian ( n - 1 , m - 1 ) + ( m + 1 ) * eulerian ( n - 1 , m ) )
|||

EULERS_CRITERION_CHECK_IF_SQUARE_ROOT_UNDER_MODULO_P_EXISTS

def squareRootExists ( n , p ) :
    n = n % p
    for x in range ( 2 , p , 1 ) :
        if ( ( x * x ) % p == n ) :
            return True
    return False
|||

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX_3

def numberOfPaths ( m , n ) :
    for i in range ( n , ( m + n - 1 ) ) :
        path *= i 
        path //= ( i - n + 1 ) 
    return path 
|||

MODIFY_ARRAY_TO_MAXIMIZE_SUM_OF_ADJACENT_DIFFERENCES

def maximumDifferenceSum ( arr , N ) :
    dp = [ [ 0 , 0 ] for i in range ( N ) ]
    for i in range ( N ) :
        dp [ i ] [ 0 ] = dp [ i ] [ 1 ] = 0
    for i in range ( N - 1 ) :
        dp [ i + 1 ] [ 0 ] = max ( dp [ i ] [ 0 ] , dp [ i ] [ 1 ] + abs ( 1 - arr [ i ] ) )
        dp [ i + 1 ] [ 1 ] = max ( dp [ i ] [ 0 ] + abs ( arr [ i + 1 ] - 1 ) , dp [ i ] [ 1 ] + abs ( arr [ i + 1 ] - arr [ i ] ) )
    return max ( dp [ N - 1 ] [ 0 ] , dp [ N - 1 ] [ 1 ] )
|||

STERN_BROCOT_SEQUENCE

def SternSequenceFunc ( BrocotSequence , n ) :
    for i in range ( 1 , n ) :
        considered_element = BrocotSequence [ i ]
        precedent = BrocotSequence [ i - 1 ]
        BrocotSequence.append ( considered_element + precedent )
        BrocotSequence.append ( considered_element )
    for i in range ( 0 , 15 ) :
        print ( BrocotSequence [ i ] , end = " " )
|||

NUMBER_SUBSEQUENCES_STRING_DIVISIBLE_N

def countDivisibleSubseq ( str , n ) :
    l = len ( str )
    dp = [ [ 0 for x in range ( l ) ] for y in range ( n ) ]
    dp [ 0 ] [ ( ord ( str [ 0 ] ) - ord ( '0' ) ) % n ] += 1
    for i in range ( 1 , l ) :
        dp [ i ] [ ( ord ( str [ i ] ) - ord ( '0' ) ) % n ] += 1
        for j in range ( n ) :
            dp [ i ] [ j ] += dp [ i - 1 ] [ j ]
            dp [ i ] [ ( j * 10 + ( ord ( str [ i ] ) - ord ( '0' ) ) ) % n ] += dp [ i - 1 ] [ j ]
    return dp [ l - 1 ] [ 0 ]
|||

HOW_TO_BEGIN_WITH_COMPETITIVE_PROGRAMMING

def search ( arr , x ) :
    n = len ( arr )
    for j in range ( 0 , n ) :
        if ( x == arr [ j ] ) :
            return j
    return - 1
|||

COUNT_PAIRS_WITH_GIVEN_SUM_1

def getPairsCount ( arr , n , sum ) :
    m = [ 0 ] * 1000
    for i in range ( 0 , n ) :
        m [ arr [ i ] ]
        m [ arr [ i ] ] += 1
    twice_count = 0
    for i in range ( 0 , n ) :
        twice_count += m [ sum - arr [ i ] ]
        if ( sum - arr [ i ] == arr [ i ] ) :
            twice_count -= 1
    return int ( twice_count / 2 )
|||

FIND_THE_MINIMUM_DISTANCE_BETWEEN_TWO_NUMBERS

def minDist ( arr , n , x , y ) :
    min_dist = 99999999
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if ( x == arr [ i ] and y == arr [ j ] or y == arr [ i ] and x == arr [ j ] ) and min_dist > abs ( i - j ) :
                min_dist = abs ( i - j )
        return min_dist
|||

FIND_REPETITIVE_ELEMENT_1_N_1_2

def findRepeating ( arr , n ) :
    res = 0
    for i in range ( 0 , n - 1 ) :
        res = res ^ ( i + 1 ) ^ arr [ i ]
    res = res ^ arr [ n - 1 ]
    return res
|||

SHORTEST_PATH_EXACTLY_K_EDGES_DIRECTED_WEIGHTED_GRAPH_1

def shortestPath ( graph , u , v , k ) :
    global V , INF
    sp = [ [ None ] * V for i in range ( V ) ]
    for i in range ( V ) :
        for j in range ( V ) :
            sp [ i ] [ j ] = [ None ] * ( k + 1 )
    for e in range ( k + 1 ) :
        for i in range ( V ) :
            for j in range ( V ) :
                sp [ i ] [ j ] [ e ] = INF
                if ( e == 0 and i == j ) :
                    sp [ i ] [ j ] [ e ] = 0
                if ( e == 1 and graph [ i ] [ j ] != INF ) :
                    sp [ i ] [ j ] [ e ] = graph [ i ] [ j ]
                if ( e > 1 ) :
                    for a in range ( V ) :
                        if ( graph [ i ] [ a ] != INF and i != a and j != a and sp [ a ] [ j ] [ e - 1 ] != INF ) :
                            sp [ i ] [ j ] [ e ] = min ( sp [ i ] [ j ] [ e ] , graph [ i ] [ a ] + sp [ a ] [ j ] [ e - 1 ] )
    return sp [ u ] [ v ] [ k ]
|||

LONGEST_SUBARRAY_NOT_K_DISTINCT_ELEMENTS

def longest ( a , n , k ) :
    freq = [ 0 ] * n
    start = 0
    end = 0
    now = 0
    l = 0
    for i in range ( n ) :
        freq [ a [ i ] ] += 1
        if ( freq [ a [ i ] ] == 1 ) :
            now += 1
        while ( now > k ) :
            freq [ a [ l ] ] -= 1
            if ( freq [ a [ l ] ] == 0 ) :
                now -= 1
            l += 1
        if ( i - l + 1 >= end - start + 1 ) :
            end = i
            start = l
    for i in range ( start , end + 1 ) :
        print ( a [ i ] , end = " " )
|||

MAXIMUM_XOR_VALUE_MATRIX

def maxXOR ( mat , N ) :
    max_xor = 0
    for i in range ( N ) :
        r_xor = 0
        c_xor = 0
        for j in range ( N ) :
            r_xor = r_xor ^ mat [ i ] [ j ]
            c_xor = c_xor ^ mat [ j ] [ i ]
        if ( max_xor < max ( r_xor , c_xor ) ) :
            max_xor = max ( r_xor , c_xor )
    return max_xor
|||

LENGTH_LONGEST_SUB_STRING_CAN_MAKE_REMOVED

def longestNull ( S ) :
    arr = [ ]
    arr.append ( [ '@' , - 1 ] )
    maxlen = 0
    for i in range ( len ( S ) ) :
        arr.append ( [ S [ i ] , i ] )
        while ( len ( arr ) >= 3 and arr [ len ( arr ) - 3 ] [ 0 ] == '1' and arr [ len ( arr ) - 2 ] [ 0 ] == '0' and arr [ len ( arr ) - 1 ] [ 0 ] == '0' ) :
            arr.pop ( )
            arr.pop ( )
            arr.pop ( )
        tmp = arr [ - 1 ]
        maxlen = max ( maxlen , i - tmp [ 1 ] )
    return maxlen
|||

LONGEST_ALTERNATING_SUB_ARRAY_STARTING_EVERY_INDEX_BINARY_ARRAY

def alternateSubarray ( arr , n ) :
    len = [ ]
    for i in range ( n + 1 ) :
        len.append ( 0 )
    len [ n - 1 ] = 1
    for i in range ( n - 2 , - 1 , - 1 ) :
        if ( arr [ i ] ^ arr [ i + 1 ] == True ) :
            len [ i ] = len [ i + 1 ] + 1
        else :
            len [ i ] = 1
    for i in range ( n ) :
        print ( len [ i ] , "" , end = "" )
|||

WILDCARD_CHARACTER_MATCHING

def match ( first , second ) :
    if len ( first ) == 0 and len ( second ) == 0 :
        return True
    if len ( first ) > 1 and first [ 0 ] == '*' and len ( second ) == 0 :
        return False
    if ( len ( first ) > 1 and first [ 0 ] == '?' ) or ( len ( first ) != 0 and len ( second ) != 0 and first [ 0 ] == second [ 0 ] ) :
        return match ( first [ 1 : ] , second [ 1 : ] ) 
    if len ( first ) != 0 and first [ 0 ] == '*' :
        return match ( first [ 1 : ] , second ) or match ( first , second [ 1 : ] )
    return False
|||

FIND_FACTORIAL_NUMBERS_LESS_EQUAL_N

def printFactorialNums ( n ) :
    fact = 1
    x = 2
    while fact <= n :
        print ( fact , end = " " )
        fact = fact * x
        x += 1
|||

FRIENDS_PAIRING_PROBLEM_2

def countFriendsPairings ( n ) :
    a , b , c = 1 , 2 , 0 
    if ( n <= 2 ) :
        return n 
    for i in range ( 3 , n + 1 ) :
        c = b + ( i - 1 ) * a 
        a = b 
        b = c 
    return c 
|||

FIND_THE_LARGEST_RECTANGLE_OF_1S_WITH_SWAPPING_OF_COLUMNS_ALLOWED

def maxArea ( mat ) :
    hist = [ [ 0 for i in range ( C + 1 ) ] for i in range ( R + 1 ) ]
    for i in range ( 0 , C , 1 ) :
        hist [ 0 ] [ i ] = mat [ 0 ] [ i ]
        for j in range ( 1 , R , 1 ) :
            if ( ( mat [ j ] [ i ] == 0 ) ) :
                hist [ j ] [ i ] = 0
            else :
                hist [ j ] [ i ] = hist [ j - 1 ] [ i ] + 1
    for i in range ( 0 , R , 1 ) :
        count = [ 0 for i in range ( R + 1 ) ]
        for j in range ( 0 , C , 1 ) :
            count [ hist [ i ] [ j ] ] += 1
        col_no = 0
        j = R
        while ( j >= 0 ) :
            if ( count [ j ] > 0 ) :
                for k in range ( 0 , count [ j ] , 1 ) :
                    hist [ i ] [ col_no ] = j
                    col_no += 1
            j -= 1
    max_area = 0
    for i in range ( 0 , R , 1 ) :
        for j in range ( 0 , C , 1 ) :
            curr_area = ( j + 1 ) * hist [ i ] [ j ]
            if ( curr_area > max_area ) :
                max_area = curr_area
    return max_area
|||

SUM_SEQUENCE_2_22_222

def sumOfSeries ( n ) :
    return 0.0246 * ( math.pow ( 10 , n ) - 1 - ( 9 * n ) )
|||

PROGRAM_FIRST_FIT_ALGORITHM_MEMORY_MANAGEMENT

def firstFit ( blockSize , m , processSize , n ) :
    allocation = [ - 1 ] * n
    for i in range ( n ) :
        for j in range ( m ) :
            if blockSize [ j ] >= processSize [ i ] :
                allocation [ i ] = j
                blockSize [ j ] -= processSize [ i ]
                break
    print ( " Process No.Process Size      Block no." )
    for i in range ( n ) :
        print ( " " , i + 1 , "         " , processSize [ i ] , "         " , end = " " )
        if allocation [ i ] != - 1 :
            print ( allocation [ i ] + 1 )
        else :
            print ( "Not Allocated" )
|||

CHECK_IF_A_NUMBER_IS_POWER_OF_ANOTHER_NUMBER

def isPower ( x , y ) :
    if ( x == 1 ) :
        return ( y == 1 )
    pow = 1
    while ( pow < y ) :
        pow = pow * x
    return ( pow == y )
|||

DIVIDE_LARGE_NUMBER_REPRESENTED_STRING

def longDivision ( number , divisor ) :
    ans = "" 
    idx = 0 
    temp = ord ( number [ idx ] ) - ord ( '0' ) 
    while ( temp < divisor ) :
        temp = ( temp * 10 + ord ( number [ idx + 1 ] ) - ord ( '0' ) ) 
        idx += 1 
    idx += 1 
    while ( ( len ( number ) ) > idx ) :
        ans += chr ( math.floor ( temp // divisor ) + ord ( '0' ) ) 
        temp = ( ( temp % divisor ) * 10 + ord ( number [ idx ] ) - ord ( '0' ) ) 
        idx += 1 
    ans += chr ( math.floor ( temp // divisor ) + ord ( '0' ) ) 
    if ( len ( ans ) == 0 ) :
        return "0" 
    return ans 
|||

FIND_ROW_NUMBER_BINARY_MATRIX_MAXIMUM_NUMBER_1S

def findMax ( arr ) :
    row = 0
    j = N - 1
    for i in range ( 0 , N ) :
        while ( arr [ i ] [ j ] == 1 and j >= 0 ) :
            row = i
            j -= 1
    print ( "Row number = " , row + 1 , ", MaxCount = " , N - 1 - j )
|||

MINIMUM_ROTATIONS_REQUIRED_GET_STRING

def findRotations ( str ) :
    tmp = str + str
    n = len ( str )
    for i in range ( 1 , n + 1 ) :
        substring = tmp [ i : n ]
        if ( str == substring ) :
            return i
    return n
|||

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX

def numberOfPaths ( m , n ) :
    if ( m == 1 or n == 1 ) :
        return 1
    return numberOfPaths ( m - 1 , n ) + numberOfPaths ( m , n - 1 )
|||

N_TH_NUMBER_WHOSE_SUM_OF_DIGITS_IS_TEN_1

def findNth ( n ) :
    count = 0 
    curr = 19 
    while ( True ) :
        sum = 0 
        x = curr 
        while ( x > 0 ) :
            sum = sum + x % 10 
            x = int ( x / 10 ) 
        if ( sum == 10 ) :
            count += 1 
        if ( count == n ) :
            return curr 
        curr += 9 
    return - 1 
|||

SUM_NODES_K_TH_LEVEL_TREE_REPRESENTED_STRING_1

def sumAtKthLevel ( tree , k , i , level ) :
    if ( tree [ i [ 0 ] ] == '(' ) :
        i [ 0 ] += 1
        if ( tree [ i [ 0 ] ] == ')' ) :
            return 0
        sum = 0
        if ( level == k ) :
            sum = int ( tree [ i [ 0 ] ] )
        i [ 0 ] += 1
        leftsum = sumAtKthLevel ( tree , k , i , level + 1 )
        i [ 0 ] += 1
        rightsum = sumAtKthLevel ( tree , k , i , level + 1 )
        i [ 0 ] += 1
        return sum + leftsum + rightsum
|||

COUNT_OFDIFFERENT_WAYS_EXPRESS_N_SUM_1_3_4

def countWays ( n ) :
    DP = [ 0 for i in range ( 0 , n + 1 ) ]
    DP [ 0 ] = DP [ 1 ] = DP [ 2 ] = 1
    DP [ 3 ] = 2
    for i in range ( 4 , n + 1 ) :
        DP [ i ] = DP [ i - 1 ] + DP [ i - 3 ] + DP [ i - 4 ]
    return DP [ n ]
|||

MAXIMUM_EQULIBRIUM_SUM_ARRAY

def findMaxSum ( arr , n ) :
    res = - sys.maxsize - 1
    for i in range ( n ) :
        prefix_sum = arr [ i ]
        for j in range ( i ) :
            prefix_sum += arr [ j ]
        suffix_sum = arr [ i ]
        j = n - 1
        while ( j > i ) :
            suffix_sum += arr [ j ]
            j -= 1
        if ( prefix_sum == suffix_sum ) :
            res = max ( res , prefix_sum )
    return res
|||

STEINS_ALGORITHM_FOR_FINDING_GCD_1

def gcd ( a , b ) :
    if ( a == b ) :
        return a
    if ( a == 0 ) :
        return b
    if ( b == 0 ) :
        return a
    if ( ( ~ a & 1 ) == 1 ) :
        if ( ( b & 1 ) == 1 ) :
            return gcd ( a >> 1 , b )
        else :
            return ( gcd ( a >> 1 , b >> 1 ) << 1 )
    if ( ( ~ b & 1 ) == 1 ) :
        return gcd ( a , b >> 1 )
    if ( a > b ) :
        return gcd ( ( a - b ) >> 1 , b )
    return gcd ( ( b - a ) >> 1 , a )
|||

PROGRAM_TO_FIND_THE_VOLUME_OF_A_TRIANGULAR_PRISM

def findVolume ( l , b , h ) :
    return ( ( l * b * h ) / 2 )
|||

FIND_RECTANGLE_BINARY_MATRIX_CORNERS_1

def isRectangle ( m ) :
    rows = len ( m )
    if ( rows == 0 ) :
        return False
    columns = len ( m [ 0 ] )
    for y1 in range ( rows ) :
        for x1 in range ( columns ) :
            if ( m [ y1 ] [ x1 ] == 1 ) :
                for y2 in range ( y1 + 1 , rows ) :
                    for x2 in range ( x1 + 1 , columns ) :
                        if ( m [ y1 ] [ x2 ] == 1 and m [ y2 ] [ x1 ] == 1 and m [ y2 ] [ x2 ] == 1 ) :
                            return True
    return False
|||

CHECK_IF_STRING_REMAINS_PALINDROME_AFTER_REMOVING_GIVEN_NUMBER_OF_CHARACTERS

def isPossible ( str , n ) :
    l = len ( str )
    if ( l >= n ) :
        return True
    return False
|||

CHECK_STAR_GRAPH

def checkStar ( mat ) :
    global size
    vertexD1 = 0
    vertexDn_1 = 0
    if ( size == 1 ) :
        return ( mat [ 0 ] [ 0 ] == 0 )
    if ( size == 2 ) :
        return ( mat [ 0 ] [ 0 ] == 0 and mat [ 0 ] [ 1 ] == 1 and mat [ 1 ] [ 0 ] == 1 and mat [ 1 ] [ 1 ] == 0 )
    for i in range ( 0 , size ) :
        degreeI = 0
        for j in range ( 0 , size ) :
            if ( mat [ i ] [ j ] ) :
                degreeI = degreeI + 1
        if ( degreeI == 1 ) :
            vertexD1 = vertexD1 + 1
        elif ( degreeI == size - 1 ) :
            vertexDn_1 = vertexDn_1 + 1
    return ( vertexD1 == ( size - 1 ) and vertexDn_1 == 1 )
|||

ROOTS_OF_UNITY

def printRoots ( n ) :
    theta = math.pi * 2 / n
    for k in range ( 0 , n ) :
        real = math.cos ( k * theta )
        img = math.sin ( k * theta )
        print ( real , end = " " )
        if ( img >= 0 ) :
            print ( " + i " , end = " " )
        else :
            print ( " - i " , end = " " )
        print ( abs ( img ) )
|||

FIND_LARGEST_D_IN_ARRAY_SUCH_THAT_A_B_C_D

def findLargestd ( S , n ) :
    found = False
    S.sort ( )
    for i in range ( n - 1 , - 1 , - 1 ) :
        for j in range ( 0 , n ) :
            if ( i == j ) :
                continue
            for k in range ( j + 1 , n ) :
                if ( i == k ) :
                    continue
                for l in range ( k + 1 , n ) :
                    if ( i == l ) :
                        continue
                    if ( S [ i ] == S [ j ] + S [ k ] + S [ l ] ) :
                        found = True
                        return S [ i ]
    if ( found == False ) :
        return - 1
|||

GIVEN_NUMBER_STRING_FIND_NUMBER_CONTIGUOUS_SUBSEQUENCES_RECURSIVELY_ADD_9_SET_2

def count9s ( number ) :
    n = len ( number )
    d = [ 0 for i in range ( 9 ) ]
    d [ 0 ] = 1
    result = 0
    mod_sum = 0
    continuous_zero = 0
    for i in range ( n ) :
        if ( ord ( number [ i ] ) - ord ( '0' ) == 0 ) :
            continuous_zero += 1
        else :
            continuous_zero = 0
        mod_sum += ord ( number [ i ] ) - ord ( '0' )
        mod_sum %= 9
        result += d [ mod_sum ]
        d [ mod_sum ] += 1
        result -= continuous_zero
    return result
|||

LEXICOGRAPHICAL_MAXIMUM_SUBSTRING_STRING

def LexicographicalMaxString ( str ) :
    mx = ""
    for i in range ( len ( str ) ) :
        mx = max ( mx , str [ i : ] )
    return mx
|||

CHECK_TWO_GIVEN_SETS_DISJOINT_1

def areDisjoint ( set1 , set2 , m , n ) :
    set1.sort ( )
    set2.sort ( )
    i = 0 ; j = 0
    while ( i < m and j < n ) :
        if ( set1 [ i ] < set2 [ j ] ) :
            i += 1
        elif ( set2 [ j ] < set1 [ i ] ) :
            j += 1
        else :
            return False
    return True
|||

EQUILIBRIUM_INDEX_OF_AN_ARRAY_1

def equilibrium ( arr ) :
    total_sum = sum ( arr )
    leftsum = 0
    for i , num in enumerate ( arr ) :
        total_sum -= num
        if leftsum == total_sum :
            return i
        leftsum += num
    return - 1
|||

AREA_CIRCUMSCRIBED_CIRCLE_SQUARE

def areacircumscribed ( a ) :
    return ( a * a * ( PI / 2 ) )
|||

LONGEST_REPEATING_AND_NON_OVERLAPPING_SUBSTRING

def longestRepeatedSubstring ( str ) :
    n = len ( str )
    LCSRe = [ [ 0 for x in range ( n + 1 ) ] for y in range ( n + 1 ) ]
    res = ""
    res_length = 0
    index = 0
    for i in range ( 1 , n + 1 ) :
        for j in range ( i + 1 , n + 1 ) :
            if ( str [ i - 1 ] == str [ j - 1 ] and LCSRe [ i - 1 ] [ j - 1 ] < ( j - i ) ) :
                LCSRe [ i ] [ j ] = LCSRe [ i - 1 ] [ j - 1 ] + 1
                if ( LCSRe [ i ] [ j ] > res_length ) :
                    res_length = LCSRe [ i ] [ j ]
                    index = max ( i , index )
            else :
                LCSRe [ i ] [ j ] = 0
    if ( res_length > 0 ) :
        for i in range ( index - res_length + 1 , index + 1 ) :
            res = res + str [ i - 1 ]
    return res
|||

HOW_TO_AVOID_OVERFLOW_IN_MODULAR_MULTIPLICATION

def mulmod ( a , b , mod ) :
    res = 0 
    a = a % mod 
    while ( b > 0 ) :
        if ( b % 2 == 1 ) :
            res = ( res + a ) % mod 
        a = ( a * 2 ) % mod 
        b //= 2 
    return res % mod 
|||

PAIR_WITH_GIVEN_PRODUCT_SET_1_FIND_IF_ANY_PAIR_EXISTS_1

def isProduct ( arr , n , x ) :
    if n < 2 :
        return False
    s = set ( )
    for i in range ( 0 , n ) :
        if arr [ i ] == 0 :
            if x == 0 :
                return True
            else :
                continue
        if x % arr [ i ] == 0 :
            if x // arr [ i ] in s :
                return True
            s.add ( arr [ i ] )
    return False
|||

SUM_K_TH_GROUP_ODD_POSITIVE_NUMBERS

def kthgroupsum ( k ) :
    cur = int ( ( k * ( k - 1 ) ) + 1 )
    sum = 0
    while k :
        sum += cur
        cur += 2
        k = k - 1
    return sum
|||

FIND_ELEMENTS_ARRAY_LEAST_TWO_GREATER_ELEMENTS_1

def findElements ( arr , n ) :
    arr.sort ( )
    for i in range ( 0 , n - 2 ) :
        print ( arr [ i ] , end = " " )
|||

MINIMUM_STEPS_TO_DELETE_A_STRING_AFTER_REPEATED_DELETION_OF_PALINDROME_SUBSTRINGS

def minStepToDeleteString ( str ) :
    N = len ( str )
    dp = [ [ 0 for x in range ( N + 1 ) ] for y in range ( N + 1 ) ]
    for l in range ( 1 , N + 1 ) :
        i = 0
        j = l - 1
        while j < N :
            if ( l == 1 ) :
                dp [ i ] [ j ] = 1
            else :
                dp [ i ] [ j ] = 1 + dp [ i + 1 ] [ j ]
                if ( str [ i ] == str [ i + 1 ] ) :
                    dp [ i ] [ j ] = min ( 1 + dp [ i + 2 ] [ j ] , dp [ i ] [ j ] )
                for K in range ( i + 2 , j + 1 ) :
                    if ( str [ i ] == str [ K ] ) :
                        dp [ i ] [ j ] = min ( dp [ i + 1 ] [ K - 1 ] + dp [ K + 1 ] [ j ] , dp [ i ] [ j ] )
            i += 1
            j += 1
    return dp [ 0 ] [ N - 1 ]
|||

CALCULATE_AREA_TETRAHEDRON

def vol_tetra ( side ) :
    volume = ( side ** 3 / ( 6 * math.sqrt ( 2 ) ) )
    return round ( volume , 2 )
|||

SIEVE_OF_ATKIN

def SieveOfAtkin ( limit ) :
    if ( limit > 2 ) :
        print ( 2 , end = " " )
    if ( limit > 3 ) :
        print ( 3 , end = " " )
    sieve = [ False ] * limit
    for i in range ( 0 , limit ) :
        sieve [ i ] = False
    x = 1
    while ( x * x < limit ) :
        y = 1
        while ( y * y < limit ) :
            n = ( 4 * x * x ) + ( y * y )
            if ( n <= limit and ( n % 12 == 1 or n % 12 == 5 ) ) :
                sieve [ n ] ^= True
            n = ( 3 * x * x ) + ( y * y )
            if ( n <= limit and n % 12 == 7 ) :
                sieve [ n ] ^= True
            n = ( 3 * x * x ) - ( y * y )
            if ( x > y and n <= limit and n % 12 == 11 ) :
                sieve [ n ] ^= True
            y += 1
        x += 1
    r = 5
    while ( r * r < limit ) :
        if ( sieve [ r ] ) :
            for i in range ( r * r , limit , r * r ) :
                sieve [ i ] = False
    for a in range ( 5 , limit ) :
        if ( sieve [ a ] ) :
            print ( a , end = " " )
|||

LENGTH_OF_THE_LONGEST_ARITHMATIC_PROGRESSION_IN_A_SORTED_ARRAY

def lenghtOfLongestAP ( set , n ) :
    if ( n <= 2 ) :
        return n
    L = [ [ 0 for x in range ( n ) ] for y in range ( n ) ]
    llap = 2
    for i in range ( n ) :
        L [ i ] [ n - 1 ] = 2
    for j in range ( n - 2 , 0 , - 1 ) :
        i = j - 1
        k = j + 1
        while ( i >= 0 and k <= n - 1 ) :
            if ( set [ i ] + set [ k ] < 2 * set [ j ] ) :
                k += 1
            elif ( set [ i ] + set [ k ] > 2 * set [ j ] ) :
                L [ i ] [ j ] = 2
                i -= 1
            else :
                L [ i ] [ j ] = L [ j ] [ k ] + 1
                llap = max ( llap , L [ i ] [ j ] )
                i -= 1
                k += 1
                while ( i >= 0 ) :
                    L [ i ] [ j ] = 2
                    i -= 1
    return llap
|||

COUNT_GROUPINGS_NUMBER_SUM_DIGITS_EVERY_SUB_GROUP_LESS_EQUALS_IMMEDIATE_RIGHT_SUB_GROUP_1

def countGroups ( position , previous_sum , length , num ) :
    if ( position == length ) :
        return 1
    if ( dp [ position ] [ previous_sum ] != - 1 ) :
        return dp [ position ] [ previous_sum ]
    dp [ position ] [ previous_sum ] = 0
    res = 0
    sum = 0
    for i in range ( position , length ) :
        sum += ( ord ( num [ i ] ) - ord ( '0' ) )
        if ( sum >= previous_sum ) :
            res += countGroups ( i + 1 , sum , length , num )
    dp [ position ] [ previous_sum ] = res
    return res
|||

LONGEST_SPAN_SUM_TWO_BINARY_ARRAYS_1

def longestCommonSum ( arr1 , arr2 , n ) :
    maxLen = 0
    presum1 = presum2 = 0
    diff = { }
    for i in range ( n ) :
        presum1 += arr1 [ i ]
        presum2 += arr2 [ i ]
        curr_diff = presum1 - presum2
        if curr_diff == 0 :
            maxLen = i + 1
        elif curr_diff not in diff :
            diff [ curr_diff ] = i
        else :
            length = i - diff [ curr_diff ]
            maxLen = max ( maxLen , length )
    return maxLen
|||

PROGRAM_TO_PRINT_FIRST_N_FIBONACCI_NUMBERS

def printFibonacciNumbers ( n ) :
    f1 = 0
    f2 = 1
    if ( n < 1 ) :
        return
    for x in range ( 0 , n ) :
        print ( f2 , end = " " )
        next = f1 + f2
        f1 = f2
        f2 = next
|||

LARGEST_SUM_CONTIGUOUS_SUBARRAY_3

def maxSubArraySum ( a , size ) :
    max_so_far = - maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    for i in range ( 0 , size ) :
        max_ending_here += a [ i ]
        if max_so_far < max_ending_here :
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0 :
            max_ending_here = 0
            s = i + 1
    print ( "Maximum contiguous sum is %d" % ( max_so_far ) )
    print ( "Starting Index %d" % ( start ) )
    print ( "Ending Index %d" % ( end ) )
|||

FIND_EQUAL_POINT_STRING_BRACKETS

def findIndex ( str ) :
    l = len ( str )
    open = [ None ] * ( l + 1 )
    close = [ None ] * ( l + 1 )
    index = - 1
    open [ 0 ] = 0
    close [ l ] = 0
    if ( str [ 0 ] == '(' ) :
        open [ 1 ] = 1
    if ( str [ l - 1 ] == ')' ) :
        close [ l - 1 ] = 1
    for i in range ( 1 , l ) :
        if ( str [ i ] == '(' ) :
            open [ i + 1 ] = open [ i ] + 1
        else :
            open [ i + 1 ] = open [ i ]
    for i in range ( l - 2 , - 1 , - 1 ) :
        if ( str [ i ] == ')' ) :
            close [ i ] = close [ i + 1 ] + 1
        else :
            close [ i ] = close [ i + 1 ]
    if ( open [ l ] == 0 ) :
        return len
    if ( close [ 0 ] == 0 ) :
        return 0
    for i in range ( l + 1 ) :
        if ( open [ i ] == close [ i ] ) :
            index = i
    return index
|||

COUNT_NUMBER_OF_WAYS_TO_PARTITION_A_SET_INTO_K_SUBSETS_1

def countP ( n , k ) :
    dp = [ [ 0 for i in range ( k + 1 ) ] for j in range ( n + 1 ) ]
    for i in range ( n + 1 ) :
        dp [ i ] [ 0 ] = 0
    for i in range ( k + 1 ) :
        dp [ 0 ] [ k ] = 0
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , k + 1 ) :
            if ( j == 1 or i == j ) :
                dp [ i ] [ j ] = 1
            else :
                dp [ i ] [ j ] = ( j * dp [ i - 1 ] [ j ] + dp [ i - 1 ] [ j - 1 ] )
    return dp [ n ] [ k ]
|||

LONGEST_INCREASING_SUBSEQUENCE

def lis ( arr ) :
    global maximum
    n = len ( arr )
    maximum = 1
    _lis ( arr , n )
    return maximum
|||

FIND_REPEATED_CHARACTER_PRESENT_FIRST_STRING

def findRepeatFirstN2 ( s ) :
    p = - 1
    for i in range ( len ( s ) ) :
        for j in range ( i + 1 , len ( s ) ) :
            if ( s [ i ] == s [ j ] ) :
                p = i
                break
        if ( p != - 1 ) :
            break
    return p
|||

K_TH_SMALLEST_ELEMENT_REMOVING_INTEGERS_NATURAL_NUMBERS

def ksmallest ( arr , n , k ) :
    b = [ 0 ] * MAX 
    for i in range ( n ) :
        b [ arr [ i ] ] = 1 
    for j in range ( 1 , MAX ) :
        if ( b [ j ] != 1 ) :
            k -= 1 
        if ( k is not 1 ) :
            return j 
|||

CHECK_IF_STACK_ELEMENTS_ARE_PAIRWISE_CONSECUTIVE

def pairWiseConsecutive ( s ) :
    aux = [ ]
    while ( len ( s ) != 0 ) :
        aux.append ( s [ - 1 ] )
        s.pop ( )
    result = True
    while ( len ( aux ) > 1 ) :
        x = aux [ - 1 ]
        aux.pop ( )
        y = aux [ - 1 ]
        aux.pop ( )
        if ( abs ( x - y ) != 1 ) :
            result = False
        s.append ( x )
        s.append ( y )
    if ( len ( aux ) == 1 ) :
        s.append ( aux [ - 1 ] )
    return result
|||

BINARY_SEARCH_1

def binarySearch ( arr , l , r , x ) :
    while l <= r :
        mid = l + ( r - l ) // 2 
        if arr [ mid ] == x :
            return mid
        elif arr [ mid ] < x :
            l = mid + 1
        else :
            r = mid - 1
    return - 1
|||

COUNT_DISTINCT_OCCURRENCES_AS_A_SUBSEQUENCE

def findSubsequenceCount ( S , T ) :
    m = len ( T )
    n = len ( S )
    if m > n :
        return 0
    mat = [ [ 0 for _ in range ( n + 1 ) ] for __ in range ( m + 1 ) ]
    for i in range ( 1 , m + 1 ) :
        mat [ i ] [ 0 ] = 0
    for j in range ( n + 1 ) :
        mat [ 0 ] [ j ] = 1
    for i in range ( 1 , m + 1 ) :
        for j in range ( 1 , n + 1 ) :
            if T [ i - 1 ] != S [ j - 1 ] :
                mat [ i ] [ j ] = mat [ i ] [ j - 1 ]
            else :
                mat [ i ] [ j ] = ( mat [ i ] [ j - 1 ] + mat [ i - 1 ] [ j - 1 ] )
    return mat [ m ] [ n ]
|||

SWAP_TWO_NUMBERS_WITHOUT_USING_TEMPORARY_VARIABLE

def swap ( xp , yp ) :
    xp [ 0 ] = xp [ 0 ] ^ yp [ 0 ]
    yp [ 0 ] = xp [ 0 ] ^ yp [ 0 ]
    xp [ 0 ] = xp [ 0 ] ^ yp [ 0 ]
|||

POLICEMEN_CATCH_THIEVES

def policeThief ( arr , n , k ) :
    i = 0
    l = 0
    r = 0
    res = 0
    thi = [ ]
    pol = [ ]
    while i < n :
        if arr [ i ] == 'P' :
            pol.append ( i )
        elif arr [ i ] == 'T' :
            thi.append ( i )
        i += 1
    while l < len ( thi ) and r < len ( pol ) :
        if ( abs ( thi [ l ] - pol [ r ] ) <= k ) :
            res += 1
            l += 1
            r += 1
        elif thi [ l ] < pol [ r ] :
            l += 1
        else :
            r += 1
    return res
|||

LARGEST_SUBARRAY_WITH_EQUAL_NUMBER_OF_0S_AND_1S_1

def maxLen ( arr , n ) :
    hash_map = { } 
    curr_sum = 0 
    max_len = 0 
    ending_index = - 1 
    for i in range ( 0 , n ) :
        if ( arr [ i ] == 0 ) :
            arr [ i ] = - 1 
        else :
            arr [ i ] = 1 
    for i in range ( 0 , n ) :
        curr_sum = curr_sum + arr [ i ] 
        if ( curr_sum == 0 ) :
            max_len = i + 1 
            ending_index = i 
        if ( curr_sum + n ) in hash_map :
            max_len = max ( max_len , i - hash_map [ curr_sum + n ] )
        else :
            hash_map [ curr_sum ] = i 
    for i in range ( 0 , n ) :
        if ( arr [ i ] == - 1 ) :
            arr [ i ] = 0 
        else :
            arr [ i ] = 1 
    print ( ending_index - max_len + 1 , end = " " ) 
    print ( "to" , end = " " ) 
    print ( ending_index ) 
    return max_len 
|||

MAXIMUM_DIFFERENCE_ZEROS_ONES_BINARY_STRING_SET_2_TIME

def findLength ( string , n ) :
    current_sum = 0
    max_sum = 0
    for i in range ( n ) :
        current_sum += ( 1 if string [ i ] == '0' else - 1 )
        if current_sum < 0 :
            current_sum = 0
        max_sum = max ( current_sum , max_sum )
    return max_sum if max_sum else 0
|||

MAXIMUM_CONSECUTIVE_NUMBERS_PRESENT_ARRAY

def findLongestConseqSubseq ( arr , n ) :
    S = set ( ) 
    for i in range ( n ) :
        S.add ( arr [ i ] ) 
    ans = 0 
    for i in range ( n ) :
        if S.__contains__ ( arr [ i ] ) :
            j = arr [ i ] 
            while ( S.__contains__ ( j ) ) :
                j += 1 
            ans = max ( ans , j - arr [ i ] ) 
    return ans 
|||

LEXICOGRAPHICALLY_NEXT_STRING

def nextWord ( s ) :
    if ( s == " " ) :
        return "a"
    i = len ( s ) - 1
    while ( s [ i ] == 'z' and i >= 0 ) :
        i -= 1
    if ( i == - 1 ) :
        s = s + 'a'
    else :
        s = s.replace ( s [ i ] , chr ( ord ( s [ i ] ) + 1 ) , 1 )
    return s
|||

SCHEDULE_JOBS_SERVER_GETS_EQUAL_LOAD

def solve ( a , b , n ) :
    s = 0
    for i in range ( 0 , n ) :
        s += a [ i ] + b [ i ]
    if n == 1 :
        return a [ 0 ] + b [ 0 ]
    if s % n != 0 :
        return - 1
    x = s // n
    for i in range ( 0 , n ) :
        if a [ i ] > x :
            return - 1
        if i > 0 :
            a [ i ] += b [ i - 1 ]
            b [ i - 1 ] = 0
        if a [ i ] == x :
            continue
        y = a [ i ] + b [ i ]
        if i + 1 < n :
            y += b [ i + 1 ]
        if y == x :
            a [ i ] = y
            b [ i ] = 0
            if i + 1 < n : b [ i + 1 ] = 0
            continue
        if a [ i ] + b [ i ] == x :
            a [ i ] += b [ i ]
            b [ i ] = 0
            continue
        if i + 1 < n and a [ i ] + b [ i + 1 ] == x :
            a [ i ] += b [ i + 1 ]
            b [ i + 1 ] = 0
            continue
        return - 1
    for i in range ( 0 , n ) :
        if b [ i ] != 0 :
            return - 1
    return x
|||

FORM_MINIMUM_NUMBER_FROM_GIVEN_SEQUENCE_1

def getMinNumberForPattern ( seq ) :
    n = len ( seq )
    if ( n >= 9 ) :
        return "-1"
    result = [ None ] * ( n + 1 )
    count = 1
    for i in range ( n + 1 ) :
        if ( i == n or seq [ i ] == 'I' ) :
            for j in range ( i - 1 , - 2 , - 1 ) :
                result [ j + 1 ] = int ( '0' + str ( count ) )
                count += 1
                if ( j >= 0 and seq [ j ] == 'I' ) :
                    break
    return result
|||

SHUFFLE_2N_INTEGERS_FORMAT_A1_B1_A2_B2_A3_B3_BN_WITHOUT_USING_EXTRA_SPACE

def shuffleArray ( a , n ) :
    i , q , k = 0 , 1 , n
    while ( i < n ) :
        j = k
        while ( j > i + q ) :
            a [ j - 1 ] , a [ j ] = a [ j ] , a [ j - 1 ]
            j -= 1
        i += 1
        k += 1
        q += 1
|||

FIND_REPETITIVE_ELEMENT_1_N_1_1

def findRepeating ( arr , n ) :
    s = set ( )
    for i in range ( n ) :
        if arr [ i ] in s :
            return arr [ i ]
        s.add ( arr [ i ] )
    rteurn - 1
|||

C_PROGRAM_SUBTRACTION_MATICES

def multiply ( A , B , C ) :
    for i in range ( N ) :
        for j in range ( N ) :
            C [ i ] [ j ] = A [ i ] [ j ] - B [ i ] [ j ]
|||

FIRST_NEGATIVE_INTEGER_EVERY_WINDOW_SIZE_K

def printFirstNegativeInteger ( arr , n , k ) :
    for i in range ( 0 , ( n - k + 1 ) ) :
        flag = False
        for j in range ( 0 , k ) :
            if ( arr [ i + j ] < 0 ) :
                print ( arr [ i + j ] , end = " " )
                flag = True
                break
        if ( not ( flag ) ) :
            print ( "0" , end = " " )
|||

NUMBER_FULL_BINARY_TREES_NODE_PRODUCT_CHILDREN

def numoffbt ( arr , n ) :
    maxvalue = - 2147483647
    minvalue = 2147483647
    for i in range ( n ) :
        maxvalue = max ( maxvalue , arr [ i ] )
        minvalue = min ( minvalue , arr [ i ] )
    mark = [ 0 for i in range ( maxvalue + 2 ) ]
    value = [ 0 for i in range ( maxvalue + 2 ) ]
    for i in range ( n ) :
        mark [ arr [ i ] ] = 1
        value [ arr [ i ] ] = 1
    ans = 0
    for i in range ( minvalue , maxvalue + 1 ) :
        if ( mark [ i ] != 0 ) :
            j = i + i
            while ( j <= maxvalue and j // i <= i ) :
                if ( mark [ j ] == 0 ) :
                    continue
                value [ j ] = value [ j ] + ( value [ i ] * value [ j // i ] )
                if ( i != j // i ) :
                    value [ j ] = value [ j ] + ( value [ i ] * value [ j // i ] )
                j += i
        ans += value [ i ]
    return ans
|||

TRIANGULAR_MATCHSTICK_NUMBER

def numberOfSticks ( x ) :
    return ( 3 * x * ( x + 1 ) ) / 2
|||

K_MAXIMUM_SUM_COMBINATIONS_TWO_ARRAYS

def KMaxCombinations ( A , B , N , K ) :
    pq = PriorityQueue ( )
    for i in range ( 0 , N ) :
        for j in range ( 0 , N ) :
            a = A [ i ] + B [ j ]
            pq.put ( ( - a , a ) )
    count = 0
    while ( count < K ) :
        print ( pq.get ( ) [ 1 ] )
        count = count + 1
|||

CONSTRUCT_ARRAY_PAIR_SUM_ARRAY

def constructArr ( arr , pair , n ) :
    arr [ 0 ] = ( pair [ 0 ] + pair [ 1 ] - pair [ n - 1 ] ) // 2
    for i in range ( 1 , n ) :
        arr [ i ] = pair [ i - 1 ] - arr [ 0 ]
|||

CHECK_HALF_STRING_CHARACTER_FREQUENCY_CHARACTER

def checkCorrectOrNot ( s ) :
    global MAX_CHAR
    count1 = [ 0 ] * MAX_CHAR
    count2 = [ 0 ] * MAX_CHAR
    n = len ( s )
    if n == 1 :
        return true
    i = 0 ; j = n - 1
    while ( i < j ) :
        count1 [ ord ( s [ i ] ) - ord ( 'a' ) ] += 1
        count2 [ ord ( s [ j ] ) - ord ( 'a' ) ] += 1
        i += 1 ; j -= 1
    for i in range ( MAX_CHAR ) :
        if count1 [ i ] != count2 [ i ] :
            return False
    return True
|||

MINIMIZE_THE_MAXIMUM_DIFFERENCE_BETWEEN_THE_HEIGHTS

def getMinDiff ( arr , n , k ) :
    if ( n == 1 ) :
        return 0
    arr.sort ( )
    ans = arr [ n - 1 ] - arr [ 0 ]
    small = arr [ 0 ] + k
    big = arr [ n - 1 ] - k
    if ( small > big ) :
        small , big = big , small
    for i in range ( 1 , n - 1 ) :
        subtract = arr [ i ] - k
        add = arr [ i ] + k
        if ( subtract >= small or add <= big ) :
            continue
        if ( big - subtract <= add - small ) :
            small = subtract
        else :
            big = add
    return min ( ans , big - small )
|||

MINIMUM_POSSIBLE_VALUE_AI_AJ_K_GIVEN_ARRAY_K

def pairs ( arr , n , k ) :
    smallest = 999999999999
    count = 0
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if abs ( arr [ i ] + arr [ j ] - k ) < smallest :
                smallest = abs ( arr [ i ] + arr [ j ] - k )
                count = 1
            elif abs ( arr [ i ] + arr [ j ] - k ) == smallest :
                count += 1
    print ( "Minimal Value = " , smallest )
    print ( "Total Pairs = " , count )
|||

SIZE_SUBARRAY_MAXIMUM_SUM

def maxSubArraySum ( a , size ) :
    max_so_far = - maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    for i in range ( 0 , size ) :
        max_ending_here += a [ i ]
        if max_so_far < max_ending_here :
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0 :
            max_ending_here = 0
            s = i + 1
    return ( end - start + 1 )
|||

MINIMUM_NUMBER_OF_SQUARES_WHOSE_SUM_EQUALS_TO_GIVEN_NUMBER_N_1

def getMinSquares ( n ) :
    dp = [ 0 , 1 , 2 , 3 ]
    for i in range ( 4 , n + 1 ) :
        dp.append ( i )
        for x in range ( 1 , int ( ceil ( sqrt ( i ) ) ) + 1 ) :
            temp = x * x 
            if temp > i :
                break
            else :
                dp [ i ] = min ( dp [ i ] , 1 + dp [ i - temp ] )
    return dp [ n ]
|||

DIVISIBILITY_BY_7

def isDivisibleBy7 ( num ) :
    if num < 0 :
        return isDivisibleBy7 ( - num )
    if ( num == 0 or num == 7 ) :
        return True
    if ( num < 10 ) :
        return False
    return isDivisibleBy7 ( num / 10 - 2 * ( num - num / 10 * 10 ) )
|||

POSITION_OF_RIGHTMOST_SET_BIT_2

def Right_most_setbit ( num ) :
    pos = 1
    for i in range ( INT_SIZE ) :
        if not ( num & ( 1 << i ) ) :
            pos += 1
        else :
            break
    return pos
|||

EFFICIENT_WAY_TO_MULTIPLY_WITH_7

def multiplyBySeven ( n ) :
    return ( ( n << 3 ) - n )
|||

NEXT_HIGHER_NUMBER_WITH_SAME_NUMBER_OF_SET_BITS

def snoob ( x ) :
    next = 0
    if ( x ) :
        rightOne = x & - ( x )
        nextHigherOneBit = x + int ( rightOne )
        rightOnesPattern = x ^ int ( nextHigherOneBit )
        rightOnesPattern = ( int ( rightOnesPattern ) / int ( rightOne ) )
        rightOnesPattern = int ( rightOnesPattern ) >> 2
        next = nextHigherOneBit | rightOnesPattern
    return next
|||

CHANGE_ARRAY_PERMUTATION_NUMBERS_1_N

def makePermutation ( a , n ) :
    count = dict ( )
    for i in range ( n ) :
        if count.get ( a [ i ] ) :
            count [ a [ i ] ] += 1
        else :
            count [ a [ i ] ] = 1 
    next_missing = 1
    for i in range ( n ) :
        if count [ a [ i ] ] != 1 or a [ i ] > n or a [ i ] < 1 :
            count [ a [ i ] ] -= 1
            while count.get ( next_missing ) :
                next_missing += 1
            a [ i ] = next_missing
            count [ next_missing ] = 1
|||

MAXIMUM_AREA_QUADRILATERAL

def maxArea ( a , b , c , d ) :
    semiperimeter = ( a + b + c + d ) / 2
    return math.sqrt ( ( semiperimeter - a ) * ( semiperimeter - b ) * ( semiperimeter - c ) * ( semiperimeter - d ) )
|||

REPLACE_OCCURRENCES_STRING_AB_C_WITHOUT_USING_EXTRA_SPACE_1

def translate ( st ) :
    l = len ( st )
    if ( l < 2 ) :
        return
    i = 0
    j = 0
    while ( j < l - 1 ) :
        if ( st [ j ] == 'A' and st [ j + 1 ] == 'B' ) :
            j += 2
            st [ i ] = 'C'
            i += 1
            continue
        st [ i ] = st [ j ]
        i += 1
        j += 1
    if ( j == l - 1 ) :
        st [ i ] = st [ j ]
        i += 1
    st [ i ] = ' '
    st [ l - 1 ] = ' '
|||

FIND_POWER_POWER_MOD_PRIME

def calculate ( A , B , C , M ) :
    res = pow ( B , C , M - 1 )
    ans = pow ( A , res , M )
    return ans
|||

CHECK_EXIST_TWO_ELEMENTS_ARRAY_WHOSE_SUM_EQUAL_SUM_REST_ARRAY

def checkPair ( arr , n ) :
    s = set ( )
    sum = 0
    for i in range ( n ) :
        sum += arr [ i ]
    if sum % 2 != 0 :
        return False
    sum = sum / 2
    for i in range ( n ) :
        val = sum - arr [ i ]
        if arr [ i ] not in s :
            s.add ( arr [ i ] )
        if val in s :
            print ( "Pair elements are" , arr [ i ] , "and" , int ( val ) )
|||

PROGRAM_FOR_SURFACE_AREA_OF_OCTAHEDRON

def surface_area_octahedron ( side ) :
    return ( 2 * ( math.sqrt ( 3 ) ) * ( side * side ) )
|||

FIND_A_SPECIFIC_PAIR_IN_MATRIX

def findMaxValue ( mat ) :
    maxValue = 0
    for a in range ( N - 1 ) :
        for b in range ( N - 1 ) :
            for d in range ( a + 1 , N ) :
                for e in range ( b + 1 , N ) :
                    if maxValue < int ( mat [ d ] [ e ] - mat [ a ] [ b ] ) :
                        maxValue = int ( mat [ d ] [ e ] - mat [ a ] [ b ] ) 
    return maxValue 
|||

MULTIPLY_TWO_NUMBERS_WITHOUT_USING_MULTIPLY_DIVISION_BITWISE_OPERATORS_AND_NO_LOOPS

def multiply ( x , y ) :
    if ( y == 0 ) :
        return 0
    if ( y > 0 ) :
        return ( x + multiply ( x , y - 1 ) )
    if ( y < 0 ) :
        return - multiply ( x , - y )
|||

FIND_TRIPLETS_ARRAY_WHOSE_SUM_EQUAL_ZERO_1

def findTriplets ( arr , n ) :
    found = False
    for i in range ( n - 1 ) :
        s = set ( )
        for j in range ( i + 1 , n ) :
            x = - ( arr [ i ] + arr [ j ] )
            if x in s :
                print ( x , arr [ i ] , arr [ j ] )
                found = True
            else :
                s.add ( arr [ j ] )
    if found == False :
        print ( "No Triplet Found" )
|||

FIND_MAXIMUM_VALUE_OF_SUM_IARRI_WITH_ONLY_ROTATIONS_ON_GIVEN_ARRAY_ALLOWED

def maxSum ( arr ) :
    arrSum = 0
    currVal = 0
    n = len ( arr )
    for i in range ( 0 , n ) :
        arrSum = arrSum + arr [ i ]
        currVal = currVal + ( i * arr [ i ] )
    maxVal = currVal
    for j in range ( 1 , n ) :
        currVal = currVal + arrSum - n * arr [ n - j ]
        if currVal > maxVal :
            maxVal = currVal
    return maxVal
|||

PROGRAM_FOR_SCALAR_MULTIPLICATION_OF_A_MATRIX

def scalarProductMat ( mat , k ) :
    for i in range ( N ) :
        for j in range ( N ) :
            mat [ i ] [ j ] = mat [ i ] [ j ] * k
|||

PRINT_SQUARES_FIRST_N_NATURAL_NUMBERS_WITHOUT_USING_1

def printSquares ( n ) :
    square = 0
    odd = 1
    for x in range ( 0 , n ) :
        print ( square , end = " " )
        square = square + odd
        odd = odd + 2
|||

NTH_PENTAGONAL_NUMBER

def pentagonalNum ( n ) :
    return ( 3 * n * n - n ) / 2
|||

COUNT_ARRAYS_ADJACENT_ELEMENTS_ONE_DIVIDE_ANOTHER

def numofArray ( n , m ) :
    dp = [ [ 0 for i in range ( MAX ) ] for j in range ( MAX ) ]
    di = [ [ ] for i in range ( MAX ) ]
    mu = [ [ ] for i in range ( MAX ) ]
    for i in range ( 1 , m + 1 ) :
        for j in range ( 2 * i , m + 1 , i ) :
            di [ j ].append ( i )
            mu [ i ].append ( j )
        di [ i ].append ( i )
    for i in range ( 1 , m + 1 ) :
        dp [ 1 ] [ i ] = 1
    for i in range ( 2 , n + 1 ) :
        for j in range ( 1 , m + 1 ) :
            dp [ i ] [ j ] = 0
            for x in di [ j ] :
                dp [ i ] [ j ] += dp [ i - 1 ] [ x ]
            for x in mu [ j ] :
                dp [ i ] [ j ] += dp [ i - 1 ] [ x ]
    ans = 0
    for i in range ( 1 , m + 1 ) :
        ans += dp [ n ] [ i ]
        di [ i ].clear ( )
        mu [ i ].clear ( )
    return ans
|||

0_1_KNAPSACK_PROBLEM_DP_10

def knapSack ( W , wt , val , n ) :
    if n == 0 or W == 0 :
        return 0
    if ( wt [ n - 1 ] > W ) :
        return knapSack ( W , wt , val , n - 1 )
    else :
        return max ( val [ n - 1 ] + knapSack ( W - wt [ n - 1 ] , wt , val , n - 1 ) , knapSack ( W , wt , val , n - 1 ) )
|||

FIND_TRIPLETS_ARRAY_WHOSE_SUM_EQUAL_ZERO

def findTriplets ( arr , n ) :
    found = True
    for i in range ( 0 , n - 2 ) :
        for j in range ( i + 1 , n - 1 ) :
            for k in range ( j + 1 , n ) :
                if ( arr [ i ] + arr [ j ] + arr [ k ] == 0 ) :
                    print ( arr [ i ] , arr [ j ] , arr [ k ] )
                    found = True
    if ( found == False ) :
        print ( " not exist " )
|||

COUNT_NUMBER_WAYS_REACH_GIVEN_SCORE_GAME

def count ( n ) :
    table = [ 0 for i in range ( n + 1 ) ]
    table [ 0 ] = 1
    for i in range ( 3 , n + 1 ) :
        table [ i ] += table [ i - 3 ]
    for i in range ( 5 , n + 1 ) :
        table [ i ] += table [ i - 5 ]
    for i in range ( 10 , n + 1 ) :
        table [ i ] += table [ i - 10 ]
    return table [ n ]
|||

MAXIMUM_SUM_ABSOLUTE_DIFFERENCE_ARRAY

def MaxSumDifference ( a , n ) :
    np.sort ( a ) 
    j = 0
    finalSequence = [ 0 for x in range ( n ) ]
    for i in range ( 0 , int ( n / 2 ) ) :
        finalSequence [ j ] = a [ i ]
        finalSequence [ j + 1 ] = a [ n - i - 1 ]
        j = j + 2
    MaximumSum = 0
    for i in range ( 0 , n - 1 ) :
        MaximumSum = ( MaximumSum + abs ( finalSequence [ i ] - finalSequence [ i + 1 ] ) )
    MaximumSum = ( MaximumSum + abs ( finalSequence [ n - 1 ] - finalSequence [ 0 ] ) ) 
    print ( MaximumSum )
|||

PROGRAM_FIND_MID_POINT_LINE

def midpoint ( x1 , x2 , y1 , y2 ) :
    print ( ( x1 + x2 ) // 2 , " , " , ( y1 + y2 ) // 2 )
|||

ALTERNATIVE_SORTING

def alternateSort ( arr , n ) :
    arr.sort ( )
    i = 0
    j = n - 1
    while ( i < j ) :
        print ( arr [ j ] , end = " " )
        j -= 1
        print ( arr [ i ] , end = " " )
        i += 1
    if ( n % 2 != 0 ) :
        print ( arr [ i ] )
|||

NUMBER_SUBARRAYS_SUM_EXACTLY_EQUAL_K

def findSubarraySum ( arr , n , Sum ) :
    prevSum = defaultdict ( lambda : 0 )
    res = 0
    currsum = 0
    for i in range ( 0 , n ) :
        currsum += arr [ i ]
        if currsum == Sum :
            res += 1
        if ( currsum - Sum ) in prevSum :
            res += prevSum [ currsum - Sum ]
        prevSum [ currsum ] += 1
    return res
|||

FIND_THE_ELEMENT_THAT_APPEARS_ONCE_IN_A_SORTED_ARRAY

def search ( arr , low , high ) :
    if low > high :
        return None
    if low == high :
        return arr [ low ]
    mid = low + ( high - low ) / 2
    if mid % 2 == 0 :
        if arr [ mid ] == arr [ mid + 1 ] :
            return search ( arr , mid + 2 , high )
        else :
            return search ( arr , low , mid )
    else :
        if arr [ mid ] == arr [ mid - 1 ] :
            return search ( arr , mid + 1 , high )
        else :
            return search ( arr , low , mid - 1 )
|||

FORM_SMALLEST_NUMBER_USING_ONE_SWAP_OPERATION

def smallestNumber ( num ) :
    num = list ( num )
    n = len ( num )
    rightMin = [ 0 ] * n
    right = 0
    rightMin [ n - 1 ] = - 1 
    right = n - 1 
    for i in range ( n - 2 , 0 , - 1 ) :
        if num [ i ] > num [ right ] :
            rightMin [ i ] = right
        else :
            rightMin [ i ] = - 1
            right = i
    small = - 1
    for i in range ( 1 , n ) :
        if num [ i ] != '0' :
            if small == - 1 :
                if num [ i ] < num [ 0 ] :
                    small = i
            elif num [ i ] < num [ small ] :
                small = i
    if small != - 1 :
        num [ 0 ] , num [ small ] = num [ small ] , num [ 0 ]
    else :
        for i in range ( 1 , n ) :
            if rightMin [ i ] != - 1 :
                num [ i ] , num [ rightMin [ i ] ] = num [ rightMin [ i ] ] , num [ i ]
                break
    return ''.join ( num )
|||

PROGRAM_AREA_SQUARE

def areaSquare ( side ) :
    area = side * side
    return area
|||

FIND_DAY_OF_THE_WEEK_FOR_A_GIVEN_DATE

def dayofweek ( d , m , y ) :
    t = [ 0 , 3 , 2 , 5 , 0 , 3 , 5 , 1 , 4 , 6 , 2 , 4 ]
    y -= m < 3
    return ( ( y + int ( y / 4 ) - int ( y / 100 ) + int ( y / 400 ) + t [ m - 1 ] + d ) % 7 )
|||

CHECK_QUEUE_CAN_SORTED_ANOTHER_QUEUE_USING_STACK

def checkSorted ( n , q ) :
    st = [ ]
    expected = 1
    fnt = None
    while ( not q.empty ( ) ) :
        fnt = q.queue [ 0 ]
        q.get ( )
        if ( fnt == expected ) :
            expected += 1
        else :
            if ( len ( st ) == 0 ) :
                st.append ( fnt )
            elif ( len ( st ) != 0 and st [ - 1 ] < fnt ) :
                return False
            else :
                st.append ( fnt )
        while ( len ( st ) != 0 and st [ - 1 ] == expected ) :
            st.pop ( )
            expected += 1
    if ( expected - 1 == n and len ( st ) == 0 ) :
        return True
    return False
|||

SORT_ARRAY_CONTAIN_1_N_VALUES

def sortit ( arr , n ) :
    for i in range ( n ) :
        arr [ i ] = i + 1
|||

LCS_LONGEST_COMMON_SUBSEQUENCE_THREE_STRINGS_1

def lcsOf3 ( i , j , k ) :
    if ( i == - 1 or j == - 1 or k == - 1 ) :
        return 0
    if ( dp [ i ] [ j ] [ k ] != - 1 ) :
        return dp [ i ] [ j ] [ k ]
    if ( X [ i ] == Y [ j ] and Y [ j ] == Z [ k ] ) :
        dp [ i ] [ j ] [ k ] = 1 + lcsOf3 ( i - 1 , j - 1 , k - 1 )
        return dp [ i ] [ j ] [ k ]
    else :
        dp [ i ] [ j ] [ k ] = max ( max ( lcsOf3 ( i - 1 , j , k ) , lcsOf3 ( i , j - 1 , k ) ) , lcsOf3 ( i , j , k - 1 ) )
        return dp [ i ] [ j ] [ k ]
|||

LOWER_INSERTION_POINT

def LowerInsertionPoint ( arr , n , X ) :
    if ( X < arr [ 0 ] ) :
        return 0 
    elif ( X > arr [ n - 1 ] ) :
        return n
    lowerPnt = 0
    i = 1
    while ( i < n and arr [ i ] < X ) :
        lowerPnt = i
        i = i * 2
    while ( lowerPnt < n and arr [ lowerPnt ] < X ) :
        lowerPnt += 1
    return lowerPnt
|||

CONSTRUCT_LEXICOGRAPHICALLY_SMALLEST_PALINDROME

def constructPalin ( string , l ) :
    string = list ( string )
    i = - 1
    j = l
    while i < j :
        i += 1
        j -= 1
        if ( string [ i ] == string [ j ] and string [ i ] != '*' ) :
            continue
        elif ( string [ i ] == string [ j ] and string [ i ] == '*' ) :
            string [ i ] = 'a'
            string [ j ] = 'a'
            continue
        elif string [ i ] == '*' :
            string [ i ] = string [ j ]
            continue
        elif string [ j ] == '*' :
            string [ j ] = string [ i ]
            continue
        print ( "Not Possible" )
        return ""
    return ''.join ( string )
|||

SECTION_FORMULA_POINT_DIVIDES_LINE_GIVEN_RATIO

def section ( x1 , x2 , y1 , y2 , m , n ) :
    x = ( float ) ( ( n * x1 ) + ( m * x2 ) ) / ( m + n )
    y = ( float ) ( ( n * y1 ) + ( m * y2 ) ) / ( m + n )
    print ( x , y )
|||

SQUARE_ROOT_NUMBER_USING_LOG

def squareRoot ( n ) :
    return pow ( 2 , 0.5 * math.log2 ( n ) )
|||

MAXIMIZE_SUM_ARRII

def maxSum ( arr , n ) :
    arr.sort ( )
    sum = 0
    for i in range ( n ) :
        sum += arr [ i ] * i
    return sum
|||

STRING_K_DISTINCT_CHARACTERS_NO_CHARACTERS_ADJACENT

def findString ( n , k ) :
    res = ""
    for i in range ( k ) :
        res = res + chr ( ord ( 'a' ) + i )
    count = 0
    for i in range ( n - k ) :
        res = res + chr ( ord ( 'a' ) + count )
        count += 1
        if ( count == k ) :
            count = 0 
    return res
|||

COUNT_WORDS_WHOSE_TH_LETTER_EITHER_1_TH_TH_I1_TH_LETTER_GIVEN_WORD

def countWords ( str , l ) :
    count = 1 
    if ( l == 1 ) :
        return count
    if ( str [ 0 ] == str [ 1 ] ) :
        count *= 1
    else :
        count *= 2
    for j in range ( 1 , l - 1 ) :
        if ( str [ j ] == str [ j - 1 ] and str [ j ] == str [ j + 1 ] ) :
            count *= 1
        elif ( str [ j ] == str [ j - 1 ] or str [ j ] == str [ j + 1 ] or str [ j - 1 ] == str [ j + 1 ] ) :
            count *= 2
        else :
            count *= 3
    if ( str [ l - 1 ] == str [ l - 2 ] ) :
        count *= 1
    else :
        count *= 2
    return count
|||

NUMBER_JUMP_REQUIRED_GIVEN_LENGTH_REACH_POINT_FORM_D_0_ORIGIN_2D_PLANE

def minJumps ( a , b , d ) :
    temp = a
    a = min ( a , b )
    b = max ( temp , b )
    if ( d >= b ) :
        return ( d + b - 1 ) / b
    if ( d == 0 ) :
        return 0
    if ( d == a ) :
        return 1
    return 2
|||

SUM_FACTORS_NUMBER_1

def sumofFactors ( n ) :
    res = 1
    for i in range ( 2 , int ( m.sqrt ( n ) + 1 ) ) :
        curr_sum = 1
        curr_term = 1
        while n % i == 0 :
            n = n / i 
            curr_term = curr_term * i 
            curr_sum += curr_term 
        res = res * curr_sum
    if n > 2 :
        res = res * ( 1 + n )
    return res 
|||

DELETE_CONSECUTIVE_WORDS_SEQUENCE

def removeConsecutiveSame ( v ) :
    n = len ( v )
    i = 0
    while ( i < n - 1 ) :
        if ( ( i + 1 ) < len ( v ) ) and ( v [ i ] == v [ i + 1 ] ) :
            v = v [ : i ]
            v = v [ : i ]
            if ( i > 0 ) :
                i -= 1
            n = n - 2
        else :
            i += 1
    return len ( v [ : i - 1 ] )
|||

COUNT_NUMBER_BINARY_STRINGS_WITHOUT_CONSECUTIVE_1S

def countStrings ( n ) :
    a = [ 0 for i in range ( n ) ]
    b = [ 0 for i in range ( n ) ]
    a [ 0 ] = b [ 0 ] = 1
    for i in range ( 1 , n ) :
        a [ i ] = a [ i - 1 ] + b [ i - 1 ]
        b [ i ] = a [ i - 1 ]
    return a [ n - 1 ] + b [ n - 1 ]
|||

FIND_THE_MISSING_NUMBER

def getMissingNo ( A ) :
    n = len ( A )
    total = ( n + 1 ) * ( n + 2 ) / 2
    sum_of_A = sum ( A )
    return total - sum_of_A
|||

SQUARE_ROOT_OF_A_PERFECT_SQUARE

def squareRoot ( n ) :
    x = n
    y = 1
    e = 0.000001
    while ( x - y > e ) :
        x = ( x + y ) / 2
        y = n / x
    return x
|||

SUBSET_SUM_PROBLEM_OSUM_SPACE

def isSubsetSum ( arr , n , sum ) :
    subset = [ [ False for j in range ( sum + 1 ) ] for i in range ( 3 ) ]
    for i in range ( n + 1 ) :
        for j in range ( sum + 1 ) :
            if ( j == 0 ) :
                subset [ i % 2 ] [ j ] = True
            elif ( i == 0 ) :
                subset [ i % 2 ] [ j ] = False
            elif ( arr [ i - 1 ] <= j ) :
                subset [ i % 2 ] [ j ] = subset [ ( i + 1 ) % 2 ] [ j - arr [ i - 1 ] ] or subset [ ( i + 1 ) % 2 ] [ j ]
            else :
                subset [ i % 2 ] [ j ] = subset [ ( i + 1 ) % 2 ] [ j ]
    return subset [ n % 2 ] [ sum ]
|||

MULTIPLICATIVE_INVERSE_UNDER_MODULO_M

def modInverse ( a , m ) :
    a = a % m 
    for x in range ( 1 , m ) :
        if ( ( a * x ) % m == 1 ) :
            return x
    return 1
|||

COMPUTE_AVERAGE_TWO_NUMBERS_WITHOUT_OVERFLOW

def compute_average ( a , b ) :
    return floor ( ( a + b ) / 2 )
|||

REPRESENT_GIVEN_SET_POINTS_BEST_POSSIBLE_STRAIGHT_LINE

def bestApproximate ( x , y , n ) :
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x2 = 0
    for i in range ( 0 , n ) :
        sum_x += x [ i ]
        sum_y += y [ i ]
        sum_xy += x [ i ] * y [ i ]
        sum_x2 += pow ( x [ i ] , 2 )
    m = ( float ) ( ( n * sum_xy - sum_x * sum_y ) / ( n * sum_x2 - pow ( sum_x , 2 ) ) ) 
    c = ( float ) ( sum_y - m * sum_x ) / n 
    print ( "m = " , m ) 
    print ( "c = " , c ) 
|||

SPLIT_ARRAY_ADD_FIRST_PART_END

def splitArr ( arr , n , k ) :
    for i in range ( 0 , k ) :
        x = arr [ 0 ]
        for j in range ( 0 , n - 1 ) :
            arr [ j ] = arr [ j + 1 ]
        arr [ n - 1 ] = x
|||

MAXIMUM_POSSIBLE_DIFFERENCE_TWO_SUBSETS_ARRAY

def maxDiff ( arr , n ) :
    SubsetSum_1 = 0
    SubsetSum_2 = 0
    for i in range ( 0 , n ) :
        isSingleOccurance = True
        for j in range ( i + 1 , n ) :
            if ( arr [ i ] == arr [ j ] ) :
                isSingleOccurance = False
                arr [ i ] = arr [ j ] = 0
                break
        if ( isSingleOccurance == True ) :
            if ( arr [ i ] > 0 ) :
                SubsetSum_1 += arr [ i ]
            else :
                SubsetSum_2 += arr [ i ]
    return abs ( SubsetSum_1 - SubsetSum_2 )
|||

LONGEST_SUBSEQUENCE_DIFFERENCE_ADJACENTS_ONE_SET_2

def longLenSub ( arr , n ) :
    um = defaultdict ( lambda : 0 )
    longLen = 0
    for i in range ( n ) :
        len1 = 0
        if ( arr [ i - 1 ] in um and len1 < um [ arr [ i ] - 1 ] ) :
            len1 = um [ arr [ i ] - 1 ]
        if ( arr [ i ] + 1 in um and len1 < um [ arr [ i ] + 1 ] ) :
            len1 = um [ arr [ i ] + 1 ]
        um [ arr [ i ] ] = len1 + 1
        if longLen < um [ arr [ i ] ] :
            longLen = um [ arr [ i ] ]
    return longLen
|||

LONGEST_REPEATED_SUBSEQUENCE_1

def longestRepeatedSubSeq ( str ) :
    n = len ( str )
    dp = [ [ 0 for i in range ( n + 1 ) ] for j in range ( n + 1 ) ]
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , n + 1 ) :
            if ( str [ i - 1 ] == str [ j - 1 ] and i != j ) :
                dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ]
            else :
                dp [ i ] [ j ] = max ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] )
    res = ''
    i = n
    j = n
    while ( i > 0 and j > 0 ) :
        if ( dp [ i ] [ j ] == dp [ i - 1 ] [ j - 1 ] + 1 ) :
            res += str [ i - 1 ]
            i -= 1
            j -= 1
        elif ( dp [ i ] [ j ] == dp [ i - 1 ] [ j ] ) :
            i -= 1
        else :
            j -= 1
    res = ''.join ( reversed ( res ) )
    return res
|||

FIND_INDEX_MAXIMUM_OCCURRING_ELEMENT_EQUAL_PROBABILITY

def findRandomIndexOfMax ( arr , n ) :
    mp = dict ( )
    for i in range ( n ) :
        if ( arr [ i ] in mp ) :
            mp [ arr [ i ] ] = mp [ arr [ i ] ] + 1
        else :
            mp [ arr [ i ] ] = 1
    max_element = - 323567
    max_so_far = - 323567
    for p in mp :
        if ( mp [ p ] > max_so_far ) :
            max_so_far = mp [ p ]
            max_element = p
    r = int ( ( ( random.randrange ( 1 , max_so_far , 2 ) % max_so_far ) + 1 ) )
    i = 0
    count = 0
    while ( i < n ) :
        if ( arr [ i ] == max_element ) :
            count = count + 1
        if ( count == r ) :
            print ( "Element with maximum frequency present at index " , i )
            break
        i = i + 1
|||

CHECK_NUMBER_IS_PERFECT_SQUARE_USING_ADDITIONSUBTRACTION

def isPerfectSquare ( n ) :
    i = 1
    the_sum = 0
    while the_sum < n :
        the_sum += i
        if the_sum == n :
            return True
        i += 2
    return False
|||

N_BONACCI_NUMBERS_1

def bonacciseries ( n , m ) :
    a = [ 0 for i in range ( m ) ]
    a [ n - 1 ] = 1
    a [ n ] = 1
    for i in range ( n + 1 , m ) :
        a [ i ] = 2 * a [ i - 1 ] - a [ i - n - 1 ]
    for i in range ( 0 , m ) :
        print ( a [ i ] , end = " " )
|||

COUNT_INDEX_PAIRS_EQUAL_ELEMENTS_ARRAY_1

def countPairs ( arr , n ) :
    mp = dict ( )
    for i in range ( n ) :
        if arr [ i ] in mp.keys ( ) :
            mp [ arr [ i ] ] += 1
        else :
            mp [ arr [ i ] ] = 1
    ans = 0
    for it in mp :
        count = mp [ it ]
        ans += ( count * ( count - 1 ) ) // 2
    return ans
|||

SORT_EVEN_PLACED_ELEMENTS_INCREASING_ODD_PLACED_DECREASING_ORDER

def bitonicGenerator ( arr , n ) :
    evenArr = [ ]
    oddArr = [ ]
    for i in range ( n ) :
        if ( ( i % 2 ) == 0 ) :
            evenArr.append ( arr [ i ] )
        else :
            oddArr.append ( arr [ i ] )
    evenArr = sorted ( evenArr )
    oddArr = sorted ( oddArr )
    oddArr = oddArr [ : : - 1 ]
    i = 0
    for j in range ( len ( evenArr ) ) :
        arr [ i ] = evenArr [ j ]
        i += 1
    for j in range ( len ( oddArr ) ) :
        arr [ i ] = oddArr [ j ]
        i += 1
|||

DYNAMIC_PROGRAMMING_SET_9_BINOMIAL_COEFFICIENT

def binomialCoeff ( n , k ) :
    if k == 0 or k == n :
        return 1
    return binomialCoeff ( n - 1 , k - 1 ) + binomialCoeff ( n - 1 , k )
|||

WRITE_A_C_PROGRAM_TO_FIND_THE_PARITY_OF_AN_UNSIGNED_INTEGER

def getParity ( n ) :
    parity = 0
    while n :
        parity = ~ parity
        n = n & ( n - 1 )
    return parity
|||

CHECK_WHETHER_LARGE_NUMBER_DIVISIBLE_7

def isdivisible7 ( num ) :
    n = len ( num )
    if ( n == 0 and num [ 0 ] == '\n' ) :
        return 1
    if ( n % 3 == 1 ) :
        num = str ( num ) + "00"
        n += 2
    elif ( n % 3 == 2 ) :
        num = str ( num ) + "0"
        n += 1
    GSum = 0
    p = 1
    for i in range ( n - 1 , - 1 , - 1 ) :
        group = 0
        group += ord ( num [ i ] ) - ord ( '0' )
        i -= 1
        group += ( ord ( num [ i ] ) - ord ( '0' ) ) * 10
        i -= 1
        group += ( ord ( num [ i ] ) - ord ( '0' ) ) * 100
        GSum = GSum + group * p
        p *= ( - 1 )
    return ( GSum % 7 == 0 )
|||

PRODUCT_NODES_K_TH_LEVEL_TREE_REPRESENTED_STRING

def productAtKthLevel ( tree , k ) :
    level = - 1
    product = 1
    n = len ( tree )
    for i in range ( 0 , n ) :
        if ( tree [ i ] == '(' ) :
            level += 1
        elif ( tree [ i ] == ')' ) :
            level -= 1
        else :
            if ( level == k ) :
                product *= ( int ( tree [ i ] ) - int ( '0' ) )
    return product
|||

CHECK_WHETHER_GIVEN_NUMBER_EVEN_ODD

def isEven ( n ) :
    return ( n % 2 == 0 )
|||

COUNT_GROUPINGS_NUMBER_SUM_DIGITS_EVERY_SUB_GROUP_LESS_EQUALS_IMMEDIATE_RIGHT_SUB_GROUP

def countGroups ( position , previous_sum , length , num ) :
    if ( position == length ) :
        return 1
    res = 0
    sum = 0
    for i in range ( position , length ) :
        sum = sum + int ( num [ i ] )
        if ( sum >= previous_sum ) :
            res = res + countGroups ( i + 1 , sum , length , num )
    return res
|||

FIND_THE_ELEMENT_THAT_ODD_NUMBER_OF_TIMES_IN_OLOG_N_TIME

def search ( arr , low , high ) :
    if low > high :
        return None
    if low == high :
        return arr [ low ]
    mid = ( low + high ) / 2 
    if mid % 2 == 0 :
        if arr [ mid ] == arr [ mid + 1 ] :
            return search ( arr , mid + 2 , high )
        else :
            return search ( arr , low , mid )
    else :
        if arr [ mid ] == arr [ mid - 1 ] :
            return search ( arr , mid + 1 , high )
        else :
            return search ( arr , low , mid - 1 )
|||

DELETE_CONSECUTIVE_WORDS_SEQUENCE_1

def removeConsecutiveSame ( v ) :
    st = [ ]
    for i in range ( len ( v ) ) :
        if ( len ( st ) == 0 ) :
            st.append ( v [ i ] )
        else :
            Str = st [ - 1 ]
            if ( Str == v [ i ] ) :
                st.pop ( )
            else :
                st.append ( v [ i ] )
    return len ( st )
|||

MINIMUM_NUMBER_OF_JUMPS_TO_REACH_END_OF_A_GIVEN_ARRAY_2

def minJumps ( arr , n ) :
    jumps = [ 0 for i in range ( n ) ]
    for i in range ( n - 2 , - 1 , - 1 ) :
        if ( arr [ i ] == 0 ) :
            jumps [ i ] = float ( 'inf' )
        elif ( arr [ i ] >= n - i - 1 ) :
            jumps [ i ] = 1
        else :
            min = float ( 'inf' )
            for j in range ( i + 1 , n ) :
                if ( j <= arr [ i ] + i ) :
                    if ( min > jumps [ j ] ) :
                        min = jumps [ j ]
            if ( min != float ( 'inf' ) ) :
                jumps [ i ] = min + 1
            else :
                jumps [ i ] = min
    return jumps [ 0 ]
|||

PROGRAM_FIND_GCD_FLOATING_POINT_NUMBERS

def gcd ( a , b ) :
    if ( a < b ) :
        return gcd ( b , a )
    if ( abs ( b ) < 0.001 ) :
        return a
    else :
        return ( gcd ( b , a - math.floor ( a / b ) * b ) )
|||

MAXIMUM_PROFIT_BY_BUYING_AND_SELLING_A_SHARE_AT_MOST_TWICE

def maxProfit ( price , n ) :
    profit = [ 0 ] * n
    max_price = price [ n - 1 ]
    for i in range ( n - 2 , 0 , - 1 ) :
        if price [ i ] > max_price :
            max_price = price [ i ]
        profit [ i ] = max ( profit [ i + 1 ] , max_price - price [ i ] )
    min_price = price [ 0 ]
    for i in range ( 1 , n ) :
        if price [ i ] < min_price :
            min_price = price [ i ]
        profit [ i ] = max ( profit [ i - 1 ] , profit [ i ] + ( price [ i ] - min_price ) )
    result = profit [ n - 1 ]
    return result
|||

COUNT_SET_BITS_IN_AN_INTEGER_1

def countSetBits ( n ) :
    if ( n == 0 ) :
        return 0
    else :
        return ( n & 1 ) + countSetBits ( n >> 1 )
|||

REORDER_A_ARRAY_ACCORDING_TO_GIVEN_INDEXES

def reorder ( arr , index , n ) :
    temp = [ 0 ] * n 
    for i in range ( 0 , n ) :
        temp [ index [ i ] ] = arr [ i ]
    for i in range ( 0 , n ) :
        arr [ i ] = temp [ i ]
        index [ i ] = i
|||

CHECK_IF_A_GIVEN_ARRAY_CAN_REPRESENT_PREORDER_TRAVERSAL_OF_BINARY_SEARCH_TREE

def canRepresentBST ( pre ) :
    s = [ ]
    root = INT_MIN
    for value in pre :
        if value < root :
            return False
        while ( len ( s ) > 0 and s [ - 1 ] < value ) :
            root = s.pop ( )
        s.append ( value )
    return True
|||

FIND_REPETITIVE_ELEMENT_1_N_1_3

def findRepeating ( arr , n ) :
    missingElement = 0
    for i in range ( 0 , n ) :
        element = arr [ abs ( arr [ i ] ) ]
        if ( element < 0 ) :
            missingElement = arr [ i ]
            break
        arr [ abs ( arr [ i ] ) ] = - arr [ abs ( arr [ i ] ) ]
    return abs ( missingElement )
|||

DYNAMIC_PROGRAMMING_SET_8_MATRIX_CHAIN_MULTIPLICATION_1

def MatrixChainOrder ( p , n ) :
    m = [ [ 0 for x in range ( n ) ] for x in range ( n ) ]
    for i in range ( 1 , n ) :
        m [ i ] [ i ] = 0
    for L in range ( 2 , n ) :
        for i in range ( 1 , n - L + 1 ) :
            j = i + L - 1
            m [ i ] [ j ] = sys.maxint
            for k in range ( i , j ) :
                q = m [ i ] [ k ] + m [ k + 1 ] [ j ] + p [ i - 1 ] * p [ k ] * p [ j ]
                if q < m [ i ] [ j ] :
                    m [ i ] [ j ] = q
    return m [ 1 ] [ n - 1 ]
|||

COUNT_NUMBER_ISLANDS_EVERY_ISLAND_SEPARATED_LINE

def countIslands ( mat ) :
    count = 0 
    for i in range ( 0 , M ) :
        for j in range ( 0 , N ) :
            if ( mat [ i ] [ j ] == 'X' ) :
                if ( ( i == 0 or mat [ i - 1 ] [ j ] == 'O' ) and ( j == 0 or mat [ i ] [ j - 1 ] == 'O' ) ) :
                    count = count + 1
    return count
|||

MINIMIZE_MAXAI_BJ_CK_MINAI_BJ_CK_THREE_DIFFERENT_SORTED_ARRAYS

def solve ( A , B , C ) :
    i = len ( A ) - 1
    j = len ( B ) - 1
    k = len ( C ) - 1
    min_diff = abs ( max ( A [ i ] , B [ j ] , C [ k ] ) - min ( A [ i ] , B [ j ] , C [ k ] ) )
    while i != - 1 and j != - 1 and k != - 1 :
        current_diff = abs ( max ( A [ i ] , B [ j ] , C [ k ] ) - min ( A [ i ] , B [ j ] , C [ k ] ) )
        if current_diff < min_diff :
            min_diff = current_diff
        max_term = max ( A [ i ] , B [ j ] , C [ k ] )
        if A [ i ] == max_term :
            i -= 1
        elif B [ j ] == max_term :
            j -= 1
        else :
            k -= 1
    return min_diff
|||

ROOTS_QUADRATIC_EQUATION

def findRoots ( a , b , c ) :
    if a == 0 :
        print ( "Invalid" )
        return - 1
    d = b * b - 4 * a * c
    sqrt_val = math.sqrt ( abs ( d ) )
    if d > 0 :
        print ( "Roots are real and different " )
        print ( ( - b + sqrt_val ) / ( 2 * a ) )
        print ( ( - b - sqrt_val ) / ( 2 * a ) )
    elif d == 0 :
        print ( "Roots are real and same" )
        print ( - b / ( 2 * a ) )
    else :
        print ( "Roots are complex" )
        print ( - b / ( 2 * a ) , " + i" , sqrt_val )
        print ( - b / ( 2 * a ) , " - i" , sqrt_val )
|||

GIVEN_LEVEL_ORDER_TRAVERSAL_BINARY_TREE_CHECK_TREE_MIN_HEAP

def isMinHeap ( level , n ) :
    for i in range ( int ( n / 2 ) - 1 , - 1 , - 1 ) :
        if level [ i ] > level [ 2 * i + 1 ] :
            return False
        if 2 * i + 2 < n :
            if level [ i ] > level [ 2 * i + 2 ] :
                return False
    return True
|||

FIND_MINIMUM_ELEMENT_IN_A_SORTED_AND_ROTATED_ARRAY

def findMin ( arr , low , high ) :
    if high < low :
        return arr [ 0 ]
    if high == low :
        return arr [ low ]
    mid = int ( ( low + high ) / 2 )
    if mid < high and arr [ mid + 1 ] < arr [ mid ] :
        return arr [ mid + 1 ]
    if mid > low and arr [ mid ] < arr [ mid - 1 ] :
        return arr [ mid ]
    if arr [ high ] > arr [ mid ] :
        return findMin ( arr , low , mid - 1 )
    return findMin ( arr , mid + 1 , high )
|||

SMALLEST_LENGTH_STRING_WITH_REPEATED_REPLACEMENT_OF_TWO_DISTINCT_ADJACENT

def stringReduction ( str ) :
    n = len ( str )
    count = [ 0 ] * 3
    for i in range ( n ) :
        count [ ord ( str [ i ] ) - ord ( 'a' ) ] += 1
    if ( count [ 0 ] == n or count [ 1 ] == n or count [ 2 ] == n ) :
        return n
    if ( ( count [ 0 ] % 2 ) == ( count [ 1 ] % 2 ) and ( count [ 1 ] % 2 ) == ( count [ 2 ] % 2 ) ) :
        return 2
    return 1
|||

CHECK_LARGE_NUMBER_DIVISIBLE_3_NOT

def check ( num ) :
    digitSum = 0
    while num > 0 :
        rem = num % 10
        digitSum = digitSum + rem
        num = num / 10
    return ( digitSum % 3 == 0 )
|||

COMPUTE_N_UNDER_MODULO_P

def modFact ( n , p ) :
    if n >= p :
        return 0
    result = 1
    for i in range ( 1 , n + 1 ) :
        result = ( result * i ) % p
    return result
|||

POSSIBILITY_OF_A_WORD_FROM_A_GIVEN_SET_OF_CHARACTERS

def isPresent ( s , q ) :
    freq = [ 0 ] * MAX_CHAR
    for i in range ( 0 , len ( s ) ) :
        freq [ ord ( s [ i ] ) ] += 1
    for i in range ( 0 , len ( q ) ) :
        freq [ ord ( q [ i ] ) ] -= 1
        if ( freq [ ord ( q [ i ] ) ] < 0 ) :
            return False
    return True
|||

NEXT_POWER_OF_2_1

def nextPowerOf2 ( n ) :
    p = 1
    if ( n and not ( n & ( n - 1 ) ) ) :
        return n
    while ( p < n ) :
        p <<= 1
    return p 
|||

REORDER_A_ARRAY_ACCORDING_TO_GIVEN_INDEXES_1

def reorder ( arr , index , n ) :
    for i in range ( 0 , n ) :
        while ( index [ i ] != i ) :
            oldTargetI = index [ index [ i ] ]
            oldTargetE = arr [ index [ i ] ]
            arr [ index [ i ] ] = arr [ i ]
            index [ index [ i ] ] = index [ i ]
            index [ i ] = oldTargetI
            arr [ i ] = oldTargetE
|||

UNBOUNDED_KNAPSACK_REPETITION_ITEMS_ALLOWED

def unboundedKnapsack ( W , n , val , wt ) :
    dp = [ 0 for i in range ( W + 1 ) ]
    ans = 0
    for i in range ( W + 1 ) :
        for j in range ( n ) :
            if ( wt [ j ] <= i ) :
                dp [ i ] = max ( dp [ i ] , dp [ i - wt [ j ] ] + val [ j ] )
    return dp [ W ]
|||

PROGRAM_CHECK_DIAGONAL_MATRIX_SCALAR_MATRIX

def isDiagonalMatrix ( mat ) :
    for i in range ( 0 , N ) :
        for j in range ( 0 , N ) :
            if ( ( i != j ) and ( mat [ i ] [ j ] != 0 ) ) :
                return False
    return True
|||

MAXIMUM_REMOVAL_FROM_ARRAY_WHEN_REMOVAL_TIME_WAITING_TIME

def maxRemoval ( arr , n ) :
    count = 0
    cummulative_sum = 0
    arr.sort ( )
    for i in range ( n ) :
        if arr [ i ] >= cummulative_sum :
            count += 1
            cummulative_sum += arr [ i ]
    return count
|||

PROGRAM_CENSOR_WORD_ASTERISKS_SENTENCE

def censor ( text , word ) :
    word_list = text.split ( )
    result = ''
    stars = '*' * len ( word )
    count = 0
    index = 0 
    for i in word_list :
        if i == word :
            word_list [ index ] = stars
        index += 1
    result = ' '.join ( word_list )
    return result
|||

COUNT_STRINGS_WITH_CONSECUTIVE_1S

def countStrings ( n ) :
    a = [ 0 ] * n
    b = [ 0 ] * n
    a [ 0 ] = b [ 0 ] = 1
    for i in range ( 1 , n ) :
        a [ i ] = a [ i - 1 ] + b [ i - 1 ]
        b [ i ] = a [ i - 1 ]
    return ( 1 << n ) - a [ n - 1 ] - b [ n - 1 ]
|||

LENGTH_LONGEST_BALANCED_SUBSEQUENCE

def maxLength ( s , n ) :
    dp = [ [ 0 for i in range ( n ) ] for i in range ( n ) ]
    for i in range ( n - 1 ) :
        if ( s [ i ] == '(' and s [ i + 1 ] == ')' ) :
            dp [ i ] [ i + 1 ] = 2
    for l in range ( 2 , n ) :
        i = - 1
        for j in range ( l , n ) :
            i += 1
            if ( s [ i ] == '(' and s [ j ] == ')' ) :
                dp [ i ] [ j ] = 2 + dp [ i + 1 ] [ j - 1 ]
            for k in range ( i , j ) :
                dp [ i ] [ j ] = max ( dp [ i ] [ j ] , dp [ i ] [ k ] + dp [ k + 1 ] [ j ] )
    return dp [ 0 ] [ n - 1 ]
|||

FIND_THE_POINT_WHERE_MAXIMUM_INTERVALS_OVERLAP

def findMaxGuests ( arrl , exit , n ) :
    arrl.sort ( ) 
    exit.sort ( ) 
    guests_in = 1 
    max_guests = 1 
    time = arrl [ 0 ] 
    i = 1 
    j = 0 
    while ( i < n and j < n ) :
        if ( arrl [ i ] <= exit [ j ] ) :
            guests_in = guests_in + 1 
            if ( guests_in > max_guests ) :
                max_guests = guests_in 
                time = arrl [ i ] 
            i = i + 1 
        else :
            guests_in = guests_in - 1 
            j = j + 1 
    print ( "Maximum Number of Guests =" , max_guests , "at time" , time )
|||

EFFICIENT_WAY_CHECK_WHETHER_N_TH_FIBONACCI_NUMBER_MULTIPLE_10

def isMultipleOf10 ( n ) :
    return ( n % 15 == 0 )
|||

MAXIMUM_SUM_PAIRS_SPECIFIC_DIFFERENCE

def maxSumPairWithDifferenceLessThanK ( arr , N , K ) :
    arr.sort ( )
    dp = [ 0 ] * N
    dp [ 0 ] = 0
    for i in range ( 1 , N ) :
        dp [ i ] = dp [ i - 1 ]
        if ( arr [ i ] - arr [ i - 1 ] < K ) :
            if ( i >= 2 ) :
                dp [ i ] = max ( dp [ i ] , dp [ i - 2 ] + arr [ i ] + arr [ i - 1 ] ) 
            else :
                dp [ i ] = max ( dp [ i ] , arr [ i ] + arr [ i - 1 ] ) 
    return dp [ N - 1 ]
|||

FIND_K_PAIRS_SMALLEST_SUMS_TWO_ARRAYS

def kSmallestPair ( arr1 , n1 , arr2 , n2 , k ) :
    if ( k > n1 * n2 ) :
        print ( "k pairs don't exist" )
        return
    index2 = [ 0 for i in range ( n1 ) ]
    while ( k > 0 ) :
        min_sum = sys.maxsize
        min_index = 0
        for i1 in range ( 0 , n1 , 1 ) :
            if ( index2 [ i1 ] < n2 and arr1 [ i1 ] + arr2 [ index2 [ i1 ] ] < min_sum ) :
                min_index = i1
                min_sum = arr1 [ i1 ] + arr2 [ index2 [ i1 ] ]
        print ( "(" , arr1 [ min_index ] , "," , arr2 [ index2 [ min_index ] ] , ")" , end = " " )
        index2 [ min_index ] += 1
        k -= 1
|||

FIRST_UPPERCASE_LETTER_IN_A_STRING_ITERATIVE_AND_RECURSIVE_1

def first ( str , i ) :
    if ( str [ i ] == '\0' ) :
        return 0
    if ( str [ i ].isupper ( ) ) :
        return str [ i ]
    return first ( str , i + 1 )
|||

FIND_PAIRS_B_ARRAY_B_K

def printPairs ( arr , n , k ) :
    isPairFound = True
    for i in range ( 0 , n ) :
        for j in range ( 0 , n ) :
            if ( i != j and arr [ i ] % arr [ j ] == k ) :
                print ( "(" , arr [ i ] , ", " , arr [ j ] , ")" , sep = "" , end = " " )
                isPairFound = True
    return isPairFound
|||

FIND_ARRANGEMENT_QUEUE_GIVEN_TIME

def solve ( n , t , p ) :
    s = list ( p )
    for i in range ( 0 , t ) :
        for j in range ( 0 , n - 1 ) :
            if ( s [ j ] == 'B' and s [ j + 1 ] == 'G' ) :
                temp = s [ j ] 
                s [ j ] = s [ j + 1 ] 
                s [ j + 1 ] = temp 
                j = j + 1
    print ( ''.join ( s ) )
|||

SHORTEST_POSSIBLE_COMBINATION_TWO_STRINGS

def printSuperSeq ( a , b ) :
    m = len ( a )
    n = len ( b )
    dp = [ [ 0 ] * ( n + 1 ) for i in range ( m + 1 ) ]
    for i in range ( 0 , m + 1 ) :
        for j in range ( 0 , n + 1 ) :
            if not i :
                dp [ i ] [ j ] = j 
            elif not j :
                dp [ i ] [ j ] = i 
            elif ( a [ i - 1 ] == b [ j - 1 ] ) :
                dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ] 
            else :
                dp [ i ] [ j ] = 1 + min ( dp [ i - 1 ] [ j ] , dp [ i ] [ j - 1 ] ) 
    index = dp [ m ] [ n ] 
    res = [ "" ] * ( index )
    i = m
    j = n 
    while ( i > 0 and j > 0 ) :
        if ( a [ i - 1 ] == b [ j - 1 ] ) :
            res [ index - 1 ] = a [ i - 1 ] 
            i -= 1
            j -= 1
            index -= 1
        elif ( dp [ i - 1 ] [ j ] < dp [ i ] [ j - 1 ] ) :
            res [ index - 1 ] = a [ i - 1 ]
            i -= 1
            index -= 1
        else :
            res [ index - 1 ] = b [ j - 1 ]
            j -= 1
            index -= 1
    while ( i > 0 ) :
        res [ index - 1 ] = a [ i - 1 ]
        i -= 1
        index -= 1
    while ( j > 0 ) :
        res [ index - 1 ] = b [ j - 1 ]
        j -= 1
        index -= 1
    print ( "".join ( res ) )
|||

COUNT_ROTATIONS_DIVISIBLE_8

def countRotationsDivBy8 ( n ) :
    l = len ( n )
    count = 0
    if ( l == 1 ) :
        oneDigit = int ( n [ 0 ] )
        if ( oneDigit % 8 == 0 ) :
            return 1
        return 0
    if ( l == 2 ) :
        first = int ( n [ 0 ] ) * 10 + int ( n [ 1 ] )
        second = int ( n [ 1 ] ) * 10 + int ( n [ 0 ] )
        if ( first % 8 == 0 ) :
            count += 1
        if ( second % 8 == 0 ) :
            count += 1
        return count
    threeDigit = 0
    for i in range ( 0 , ( l - 2 ) ) :
        threeDigit = ( int ( n [ i ] ) * 100 + int ( n [ i + 1 ] ) * 10 + int ( n [ i + 2 ] ) )
        if ( threeDigit % 8 == 0 ) :
            count += 1
    threeDigit = ( int ( n [ l - 1 ] ) * 100 + int ( n [ 0 ] ) * 10 + int ( n [ 1 ] ) )
    if ( threeDigit % 8 == 0 ) :
        count += 1
    threeDigit = ( int ( n [ l - 2 ] ) * 100 + int ( n [ l - 1 ] ) * 10 + int ( n [ 0 ] ) )
    if ( threeDigit % 8 == 0 ) :
        count += 1
    return count
|||

LONGEST_COMMON_SUBSEQUENCE_WITH_AT_MOST_K_CHANGES_ALLOWED

def lcs ( dp , arr1 , n , arr2 , m , k ) :
    if k < 0 :
        return - ( 10 ** 7 )
    if n < 0 or m < 0 :
        return 0
    ans = dp [ n ] [ m ] [ k ]
    if ans != - 1 :
        return ans
    ans = max ( lcs ( dp , arr1 , n - 1 , arr2 , m , k ) , lcs ( dp , arr1 , n , arr2 , m - 1 , k ) )
    if arr1 [ n - 1 ] == arr2 [ m - 1 ] :
        ans = max ( ans , 1 + lcs ( dp , arr1 , n - 1 , arr2 , m - 1 , k ) )
    ans = max ( ans , lcs ( dp , arr1 , n - 1 , arr2 , m - 1 , k - 1 ) )
    return ans
|||

CHECK_LINE_TOUCHES_INTERSECTS_CIRCLE

def checkCollision ( a , b , c , x , y , radius ) :
    dist = ( ( abs ( a * x + b * y + c ) ) / math.sqrt ( a * a + b * b ) )
    if ( radius == dist ) :
        print ( "Touch" )
    elif ( radius > dist ) :
        print ( "Intersect" )
    else :
        print ( "Outside" )
|||

FIND_THE_MAXIMUM_SUBARRAY_XOR_IN_A_GIVEN_ARRAY

def maxSubarrayXOR ( arr , n ) :
    ans = - 2147483648
    for i in range ( n ) :
        curr_xor = 0
        for j in range ( i , n ) :
            curr_xor = curr_xor ^ arr [ j ]
            ans = max ( ans , curr_xor )
    return ans
|||

SHORTEST_PATH_EXACTLY_K_EDGES_DIRECTED_WEIGHTED_GRAPH

def shortestPath ( graph , u , v , k ) :
    V = 4
    INF = 999999999999
    if k == 0 and u == v :
        return 0
    if k == 1 and graph [ u ] [ v ] != INF :
        return graph [ u ] [ v ]
    if k <= 0 :
        return INF
    res = INF
    for i in range ( V ) :
        if graph [ u ] [ i ] != INF and u != i and v != i :
            rec_res = shortestPath ( graph , i , v , k - 1 )
            if rec_res != INF :
                res = min ( res , graph [ u ] [ i ] + rec_res )
    return res
|||

FIND_SUBARRAY_WITH_GIVEN_SUM

def subArraySum ( arr , n , sum ) :
    for i in range ( n ) :
        curr_sum = arr [ i ]
        j = i + 1
        while j <= n :
            if curr_sum == sum :
                print ( "Sum found between" )
                print ( "indexes %d and %d" % ( i , j - 1 ) )
                return 1
            if curr_sum > sum or j == n :
                break
            curr_sum = curr_sum + arr [ j ]
            j += 1
    print ( "No subarray found" )
    return 0
|||

K_TH_PRIME_FACTOR_GIVEN_NUMBER

def kPrimeFactor ( n , k ) :
    while ( n % 2 == 0 ) :
        k = k - 1
        n = n / 2
        if ( k == 0 ) :
            return 2
    i = 3
    while i <= math.sqrt ( n ) :
        while ( n % i == 0 ) :
            if ( k == 1 ) :
                return i
            k = k - 1
            n = n / i
        i = i + 2
    if ( n > 2 and k == 1 ) :
        return n
    return - 1
|||

FIND_ROTATION_COUNT_ROTATED_SORTED_ARRAY_1

def countRotations ( arr , low , high ) :
    if ( high < low ) :
        return 0
    if ( high == low ) :
        return low
    mid = low + ( high - low ) / 2 
    mid = int ( mid )
    if ( mid < high and arr [ mid + 1 ] < arr [ mid ] ) :
        return ( mid + 1 )
    if ( mid > low and arr [ mid ] < arr [ mid - 1 ] ) :
        return mid
    if ( arr [ high ] > arr [ mid ] ) :
        return countRotations ( arr , low , mid - 1 ) 
    return countRotations ( arr , mid + 1 , high )
|||

COMPUTE_AVERAGE_TWO_NUMBERS_WITHOUT_OVERFLOW_1

def compute_average ( a , b ) :
    return ( a // 2 ) + ( b // 2 ) + ( ( a % 2 + b % 2 ) // 2 )
|||

SORTING_USING_TRIVIAL_HASH_FUNCTION_1

def sortUsingHash ( a , n ) :
    Max = max ( a )
    Min = abs ( min ( a ) )
    hashpos = [ 0 ] * ( Max + 1 )
    hashneg = [ 0 ] * ( Min + 1 )
    for i in range ( 0 , n ) :
        if a [ i ] >= 0 :
            hashpos [ a [ i ] ] += 1
        else :
            hashneg [ abs ( a [ i ] ) ] += 1
    for i in range ( Min , 0 , - 1 ) :
        if hashneg [ i ] != 0 :
            for j in range ( 0 , hashneg [ i ] ) :
                print ( ( - 1 ) * i , end = " " )
    for i in range ( 0 , Max + 1 ) :
        if hashpos [ i ] != 0 :
            for j in range ( 0 , hashpos [ i ] ) :
                print ( i , end = " " )
|||

FIND_THE_TWO_REPEATING_ELEMENTS_IN_A_GIVEN_ARRAY_1

def printRepeating ( arr , size ) :
    count = [ 0 ] * size
    print ( " Repeating elements are " , end = "" )
    for i in range ( 0 , size ) :
        if ( count [ arr [ i ] ] == 1 ) :
            print ( arr [ i ] , end = " " )
        else :
            count [ arr [ i ] ] = count [ arr [ i ] ] + 1
|||

MINIMUM_STEPS_MINIMIZE_N_PER_GIVEN_CONDITION

def getMinSteps ( n ) :
    table = [ 0 ] * ( n + 1 )
    for i in range ( n + 1 ) :
        table [ i ] = n - i
    for i in range ( n , 0 , - 1 ) :
        if ( not ( i % 2 ) ) :
            table [ i // 2 ] = min ( table [ i ] + 1 , table [ i // 2 ] )
        if ( not ( i % 3 ) ) :
            table [ i // 3 ] = min ( table [ i ] + 1 , table [ i // 3 ] )
    return table [ 1 ]
    
|||

COUNT_POSSIBLE_DECODINGS_GIVEN_DIGIT_SEQUENCE_1

def countDecodingDP ( digits , n ) :
    count = [ 0 ] * ( n + 1 ) 
    count [ 0 ] = 1 
    count [ 1 ] = 1 
    for i in range ( 2 , n + 1 ) :
        count [ i ] = 0 
        if ( digits [ i - 1 ] > '0' ) :
            count [ i ] = count [ i - 1 ] 
        if ( digits [ i - 2 ] == '1' or ( digits [ i - 2 ] == '2' and digits [ i - 1 ] < '7' ) ) :
            count [ i ] += count [ i - 2 ] 
    return count [ n ] 
|||

EULERS_FOUR_SQUARE_IDENTITY_1

def checkEulerFourSquareIdentity ( a , b ) :
    ab = a * b
    flag = False
    i = 0
    while i * i <= ab :
        j = i
        while i * i + j * j <= ab :
            k = j
            while i * i + j * j + k * k <= ab :
                l = ( ab - ( i * i + j * j + k * k ) ) ** ( 0.5 )
                if l == int ( l ) and l >= k :
                    flag = True
                    print ( "i = " , i )
                    print ( "j = " , j )
                    print ( "k = " , k )
                    print ( "l = " , l )
                    print ( "Product of" , a , "and" , b , "can be written as sum of squares of i, j, k, l" )
                    print ( ab , " = " , i , "*" , i , "+" , j , "*" , j , "+" , k , "*" , k , "+" , l , "*" , l )
                k += 1
            j += 1
        i += 1
    if flag == False :
        print ( "Solution doesn't exist!" )
        return
|||

COUNT_NUMBER_INCREASING_SUBSEQUENCES_SIZE_K

def numOfIncSubseqOfSizeK ( arr , n , k ) :
    dp = [ [ 0 for i in range ( n ) ] for i in range ( k ) ]
    for i in range ( n ) :
        dp [ 0 ] [ i ] = 1
    for l in range ( 1 , k ) :
        for i in range ( l , n ) :
            dp [ l ] [ i ] = 0
            for j in range ( l - 1 , i ) :
                if ( arr [ j ] < arr [ i ] ) :
                    dp [ l ] [ i ] += dp [ l - 1 ] [ j ]
    Sum = 0
    for i in range ( k - 1 , n ) :
        Sum += dp [ k - 1 ] [ i ]
    return Sum
|||

KNAPSACK_PROBLEM_1

def knapSack ( W , wt , val , n ) :
    K = [ [ 0 for x in range ( W + 1 ) ] for x in range ( n + 1 ) ]
    for i in range ( n + 1 ) :
        for w in range ( W + 1 ) :
            if i == 0 or w == 0 :
                K [ i ] [ w ] = 0
            elif wt [ i - 1 ] <= w :
                K [ i ] [ w ] = max ( val [ i - 1 ] + K [ i - 1 ] [ w - wt [ i - 1 ] ] , K [ i - 1 ] [ w ] )
            else :
                K [ i ] [ w ] = K [ i - 1 ] [ w ]
    return K [ n ] [ W ]
|||

PROGRAM_TO_PRINT_DOUBLE_HEADED_ARROW_PATTERN

def drawPattern ( N ) :
    n = N 
    row = 1 
    nst = 1 
    nsp1 = n - 1 
    nsp2 = - 1 
    val1 = row 
    val2 = 1 
    while ( row <= n ) :
        csp1 = 1 
        while ( csp1 <= nsp1 ) :
            print ( " " , end = " " ) 
            csp1 = csp1 + 1 
        cst1 = 1 
        while ( cst1 <= nst ) :
            print ( val1 , end = " " ) 
            val1 = val1 - 1 
            cst1 = cst1 + 1 
        csp2 = 1 
        while ( csp2 <= nsp2 ) :
            print ( " " , end = " " ) 
            csp2 = csp2 + 1 
        if ( row != 1 and row != n ) :
            cst2 = 1 
            while ( cst2 <= nst ) :
                print ( val2 , end = " " ) 
                val2 = val2 + 1 
                cst2 = cst2 + 1 
        print ( )
        if ( row <= n // 2 ) :
            nst = nst + 1 
            nsp1 = nsp1 - 2 
            nsp2 = nsp2 + 2 
            val1 = row + 1 
            val2 = 1 
        else :
            nst = nst - 1 
            nsp1 = nsp1 + 2 
            nsp2 = nsp2 - 2 
            val1 = n - row 
            val2 = 1 
        row = row + 1 
|||

INTEGER_POSITIVE_VALUE_POSITIVE_NEGATIVE_VALUE_ARRAY

def findInteger ( arr , n ) :
    hash = dict ( )
    maximum = 0
    for i in arr :
        if ( i < 0 ) :
            if abs ( i ) not in hash.keys ( ) :
                hash [ abs ( i ) ] = - 1
            else :
                hash [ abs ( i ) ] -= 1
        else :
            hash [ i ] = hash.get ( i , 0 ) + 1
    for i in arr :
        if i in hash.keys ( ) and hash [ i ] > 0 :
            return i
    return - 1
|||

SPACE_OPTIMIZED_SOLUTION_LCS

def lcs ( X , Y ) :
    m = len ( X )
    n = len ( Y )
    L = [ [ 0 for i in range ( n + 1 ) ] for j in range ( 2 ) ]
    bi = bool
    for i in range ( m ) :
        bi = i & 1
        for j in range ( n + 1 ) :
            if ( i == 0 or j == 0 ) :
                L [ bi ] [ j ] = 0
            elif ( X [ i ] == Y [ j - 1 ] ) :
                L [ bi ] [ j ] = L [ 1 - bi ] [ j - 1 ] + 1
            else :
                L [ bi ] [ j ] = max ( L [ 1 - bi ] [ j ] , L [ bi ] [ j - 1 ] )
    return L [ bi ] [ n ]
|||

REPRESENT_NUMBER_SUM_MINIMUM_POSSIBLE_PSUEDOBINARY_NUMBERS

def psuedoBinary ( n ) :
    while ( n > 0 ) :
        temp = n 
        m = 0 
        p = 1 
        while ( temp ) :
            rem = temp % 10 
            temp = int ( temp / 10 ) 
            if ( rem != 0 ) :
                m += p 
            p *= 10 
        print ( m , end = " " ) 
        n = n - m 
|||

FIND_NUMBER_CURRENCY_NOTES_SUM_UPTO_GIVEN_AMOUNT

def countCurrency ( amount ) :
    notes = [ 2000 , 500 , 200 , 100 , 50 , 20 , 10 , 5 , 1 ]
    noteCounter = [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
    print ( "Currency Count -> " )
    for i , j in zip ( notes , noteCounter ) :
        if amount >= i :
            j = amount // i
            amount = amount - j * i
            print ( i , " : " , j )
|||

POSITIVE_ELEMENTS_EVEN_NEGATIVE_ODD_POSITIONS

def rearrange ( a , size ) :
    positive = 0
    negative = 1
    while ( True ) :
        while ( positive < size and a [ positive ] >= 0 ) :
            positive = positive + 2
        while ( negative < size and a [ negative ] <= 0 ) :
            negative = negative + 2
        if ( positive < size and negative < size ) :
            temp = a [ positive ]
            a [ positive ] = a [ negative ]
            a [ negative ] = temp
        else :
            break
|||

FIND_WHETHER_AN_ARRAY_IS_SUBSET_OF_ANOTHER_ARRAY_SET_1

def isSubset ( arr1 , arr2 , m , n ) :
    i = 0
    j = 0
    for i in range ( n ) :
        for j in range ( m ) :
            if ( arr2 [ i ] == arr1 [ j ] ) :
                break
        if ( j == m ) :
            return 0
    return 1
|||

GIVEN_A_SORTED_AND_ROTATED_ARRAY_FIND_IF_THERE_IS_A_PAIR_WITH_A_GIVEN_SUM

def pairInSortedRotated ( arr , n , x ) :
    for i in range ( 0 , n - 1 ) :
        if ( arr [ i ] > arr [ i + 1 ] ) :
            break 
    l = ( i + 1 ) % n
    r = i
    while ( l != r ) :
        if ( arr [ l ] + arr [ r ] == x ) :
            return True 
        if ( arr [ l ] + arr [ r ] < x ) :
            l = ( l + 1 ) % n 
        else :
            r = ( n + r - 1 ) % n 
    return False 
|||

PROGRAM_TO_FIND_REMAINDER_WITHOUT_USING_MODULO_OR_OPERATOR_1

def getRemainder ( num , divisor ) :
    if ( divisor == 0 ) :
        return False
    if ( divisor < 0 ) :
        divisor = - divisor
    if ( num < 0 ) :
        num = - num
    i = 1
    product = 0
    while ( product <= num ) :
        product = divisor * i
        i += 1
    return num - ( product - divisor )
|||

GNOME_SORT_A_STUPID_ONE

def gnomeSort ( arr , n ) :
    index = 0
    while index < n :
        if index == 0 :
            index = index + 1
        if arr [ index ] >= arr [ index - 1 ] :
            index = index + 1
        else :
            arr [ index ] , arr [ index - 1 ] = arr [ index - 1 ] , arr [ index ]
            index = index - 1
    return arr
|||

NUMBER_WAYS_INSERT_CHARACTER_INCREASE_LCS_ONE

def numberofways ( A , B , N , M ) :
    pos = [ [ ] for _ in range ( MAX ) ]
    for i in range ( M ) :
        pos [ ord ( B [ i ] ) ].append ( i + 1 )
    dpl = [ [ 0 ] * ( M + 2 ) for _ in range ( N + 2 ) ]
    for i in range ( 1 , N + 1 ) :
        for j in range ( 1 , M + 1 ) :
            if A [ i - 1 ] == B [ j - 1 ] :
                dpl [ i ] [ j ] = dpl [ i - 1 ] [ j - 1 ] + 1
            else :
                dpl [ i ] [ j ] = max ( dpl [ i - 1 ] [ j ] , dpl [ i ] [ j - 1 ] )
    LCS = dpl [ N ] [ M ]
    dpr = [ [ 0 ] * ( M + 2 ) for _ in range ( N + 2 ) ]
    for i in range ( N , 0 , - 1 ) :
        for j in range ( M , 0 , - 1 ) :
            if A [ i - 1 ] == B [ j - 1 ] :
                dpr [ i ] [ j ] = dpr [ i + 1 ] [ j + 1 ] + 1
            else :
                dpr [ i ] [ j ] = max ( dpr [ i + 1 ] [ j ] , dpr [ i ] [ j + 1 ] )
    ans = 0
    for i in range ( N + 1 ) :
        for j in range ( MAX ) :
            for x in pos [ j ] :
                if dpl [ i ] [ x - 1 ] + dpr [ i + 1 ] [ x + 1 ] == LCS :
                    ans += 1
                    break
    return ans
|||

MINIMUM_PRODUCT_K_INTEGERS_ARRAY_POSITIVE_INTEGERS

def minProduct ( arr , n , k ) :
    heapq.heapify ( arr )
    count = 0
    ans = 1
    while ( arr ) and count < k :
        x = heapq.heappop ( arr )
        ans = ans * x
        count = count + 1
    return ans 
|||

FIND_UNIQUE_ELEMENTS_MATRIX

def unique ( mat , n , m ) :
    maximum = 0 ; flag = 0
    for i in range ( 0 , n ) :
        for j in range ( 0 , m ) :
            if ( maximum < mat [ i ] [ j ] ) :
                maximum = mat [ i ] [ j ] 
    uniqueElementDict = [ 0 ] * ( maximum + 1 )
    for i in range ( 0 , n ) :
        for j in range ( 0 , m ) :
            uniqueElementDict [ mat [ i ] [ j ] ] += 1
    for key in range ( maximum + 1 ) :
        if uniqueElementDict [ key ] == 1 :
            print ( key , end = " " )
            flag = 1
    if ( flag == 0 ) :
        print ( "No unique element in the matrix" )
|||

LONGEST_SUBSEQUENCE_SUCH_THAT_DIFFERENCE_BETWEEN_ADJACENTS_IS_ONE

def longestSubseqWithDiffOne ( arr , n ) :
    dp = [ 1 for i in range ( n ) ]
    for i in range ( n ) :
        for j in range ( i ) :
            if ( ( arr [ i ] == arr [ j ] + 1 ) or ( arr [ i ] == arr [ j ] - 1 ) ) :
                dp [ i ] = max ( dp [ i ] , dp [ j ] + 1 )
    result = 1
    for i in range ( n ) :
        if ( result < dp [ i ] ) :
            result = dp [ i ]
    return result
|||

C_PROGRAM_CONCATENATE_STRING_GIVEN_NUMBER_TIMES

def repeat ( s , n ) :
    s1 = s
    for i in range ( 1 , n ) :
        s += s1
    return s
|||

SEARCHING_FOR_PATTERNS_SET_1_NAIVE_PATTERN_SEARCHING

def search ( pat , txt ) :
    M = len ( pat )
    N = len ( txt )
    for i in range ( N - M + 1 ) :
        j = 0
        while ( j < M ) :
            if ( txt [ i + j ] != pat [ j ] ) :
                break
            j += 1
        if ( j == M ) :
            print ( "Pattern found at index " , i )
|||

COUNT_POSSIBLE_PATHS_SOURCE_DESTINATION_EXACTLY_K_EDGES

def countwalks ( graph , u , v , k ) :
    if ( k == 0 and u == v ) :
        return 1
    if ( k == 1 and graph [ u ] [ v ] ) :
        return 1
    if ( k <= 0 ) :
        return 0
    count = 0
    for i in range ( 0 , V ) :
        if ( graph [ u ] [ i ] == 1 ) :
            count += countwalks ( graph , i , v , k - 1 )
    return count
|||

COUNT_DIVISIBLE_PAIRS_ARRAY

def countDivisibles ( arr , n ) :
    res = 0
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            if ( arr [ i ] % arr [ j ] == 0 or arr [ j ] % arr [ i ] == 0 ) :
                res += 1
    return res
|||

PROGRAM_TO_CHECK_IF_A_MATRIX_IS_SYMMETRIC

def isSymmetric ( mat , N ) :
    for i in range ( N ) :
        for j in range ( N ) :
            if ( mat [ i ] [ j ] != mat [ j ] [ i ] ) :
                return False
    return True
|||

COUNT_PALINDROME_SUB_STRINGS_STRING

def CountPS ( str , n ) :
    dp = [ [ 0 for x in range ( n ) ] for y in range ( n ) ]
    P = [ [ False for x in range ( n ) ] for y in range ( n ) ]
    for i in range ( n ) :
        P [ i ] [ i ] = True
    for i in range ( n - 1 ) :
        if ( str [ i ] == str [ i + 1 ] ) :
            P [ i ] [ i + 1 ] = True
            dp [ i ] [ i + 1 ] = 1
    for gap in range ( 2 , n ) :
        for i in range ( n - gap ) :
            j = gap + i 
            if ( str [ i ] == str [ j ] and P [ i + 1 ] [ j - 1 ] ) :
                P [ i ] [ j ] = True
            if ( P [ i ] [ j ] == True ) :
                dp [ i ] [ j ] = ( dp [ i ] [ j - 1 ] + dp [ i + 1 ] [ j ] + 1 - dp [ i + 1 ] [ j - 1 ] )
            else :
                dp [ i ] [ j ] = ( dp [ i ] [ j - 1 ] + dp [ i + 1 ] [ j ] - dp [ i + 1 ] [ j - 1 ] )
    return dp [ 0 ] [ n - 1 ]
|||

WAYS_SUM_N_USING_ARRAY_ELEMENTS_REPETITION_ALLOWED

def countWays ( arr , m , N ) :
    count = [ 0 for i in range ( N + 1 ) ]
    count [ 0 ] = 1
    for i in range ( 1 , N + 1 ) :
        for j in range ( m ) :
            if ( i >= arr [ j ] ) :
                count [ i ] += count [ i - arr [ j ] ]
    return count [ N ]
|||

MINIMUM_NUMBER_OF_OPERATIONS_TO_MOVE_ALL_UPPERCASE_CHARACTERS_BEFORE_ALL_LOWER_CASE_CHARACTERS

def minOperations ( str , n ) :
    lastUpper = - 1
    firstLower = - 1
    for i in range ( n - 1 , - 1 , - 1 ) :
        if ( str [ i ].isupper ( ) ) :
            lastUpper = i
            break
    for i in range ( n ) :
        if ( str [ i ].islower ( ) ) :
            firstLower = i
            break
    if ( lastUpper == - 1 or firstLower == - 1 ) :
        return 0
    countUpper = 0
    for i in range ( firstLower , n ) :
        if ( str [ i ].isupper ( ) ) :
            countUpper += 1
    countLower = 0
    for i in range ( lastUpper ) :
        if ( str [ i ].islower ( ) ) :
            countLower += 1
    return min ( countLower , countUpper )
|||

PRINT_A_GIVEN_MATRIX_IN_SPIRAL_FORM

def spiralPrint ( m , n , a ) :
    k = 0 ; l = 0
    while ( k < m and l < n ) :
        for i in range ( l , n ) :
            print ( a [ k ] [ i ] , end = " " )
        k += 1
        for i in range ( k , m ) :
            print ( a [ i ] [ n - 1 ] , end = " " )
        n -= 1
        if ( k < m ) :
            for i in range ( n - 1 , ( l - 1 ) , - 1 ) :
                print ( a [ m - 1 ] [ i ] , end = " " )
            m -= 1
        if ( l < n ) :
            for i in range ( m - 1 , k - 1 , - 1 ) :
                print ( a [ i ] [ l ] , end = " " )
            l += 1
|||

FIND_DISTINCT_INTEGERS_FOR_A_TRIPLET_WITH_GIVEN_PRODUCT

def findTriplets ( x ) :
    fact = [ ] 
    factors = set ( ) 
    for i in range ( 2 , int ( sqrt ( x ) ) ) :
        if ( x % i == 0 ) :
            fact.append ( i ) 
            if ( x / i != i ) :
                fact.append ( x // i ) 
            factors.add ( i ) 
            factors.add ( x // i ) 
    found = False 
    k = len ( fact ) 
    for i in range ( k ) :
        a = fact [ i ] 
        for j in range ( k ) :
            b = fact [ j ] 
            if ( ( a != b ) and ( x % ( a * b ) == 0 ) and ( x / ( a * b ) != a ) and ( x / ( a * b ) != b ) and ( x / ( a * b ) != 1 ) ) :
                print ( a , b , x // ( a * b ) ) 
                found = True 
                break 
        if ( found ) :
            break 
    if ( not found ) :
        print ( "-1" ) 
|||

SUM_TWO_LARGE_NUMBERS_1

def findSum ( str1 , str2 ) :
    if len ( str1 ) > len ( str2 ) :
        temp = str1
        str1 = str2
        str2 = temp
    str3 = ""
    n1 = len ( str1 )
    n2 = len ( str2 )
    diff = n2 - n1
    carry = 0
    for i in range ( n1 - 1 , - 1 , - 1 ) :
        sum = ( ( ord ( str1 [ i ] ) - ord ( '0' ) ) + int ( ( ord ( str2 [ i + diff ] ) - ord ( '0' ) ) ) + carry )
        str3 = str3 + str ( sum % 10 )
        carry = sum // 10
    for i in range ( n2 - n1 - 1 , - 1 , - 1 ) :
        sum = ( ( ord ( str2 [ i ] ) - ord ( '0' ) ) + carry )
        str3 = str3 + str ( sum % 10 )
        carry = sum // 10
    if ( carry ) :
        str3 + str ( carry + '0' )
    str3 = str3 [ : : - 1 ]
    return str3
|||

COCKTAIL_SORT

def cocktailSort ( a ) :
    n = len ( a )
    swapped = True
    start = 0
    end = n - 1
    while ( swapped == True ) :
        swapped = False
        for i in range ( start , end ) :
            if ( a [ i ] > a [ i + 1 ] ) :
                a [ i ] , a [ i + 1 ] = a [ i + 1 ] , a [ i ]
                swapped = True
        if ( swapped == False ) :
            break
        swapped = False
        end = end - 1
        for i in range ( end - 1 , start - 1 , - 1 ) :
            if ( a [ i ] > a [ i + 1 ] ) :
                a [ i ] , a [ i + 1 ] = a [ i + 1 ] , a [ i ]
                swapped = True
        start = start + 1
|||

COUNT_DERANGEMENTS_PERMUTATION_SUCH_THAT_NO_ELEMENT_APPEARS_IN_ITS_ORIGINAL_POSITION_1

def countDer ( n ) :
    der = [ 0 for i in range ( n + 1 ) ]
    der [ 0 ] = 1
    der [ 1 ] = 0
    der [ 2 ] = 1
    for i in range ( 3 , n + 1 ) :
        der [ i ] = ( i - 1 ) * ( der [ i - 1 ] + der [ i - 2 ] )
    return der [ n ]
|||

MAXIMUM_PRODUCT_SUBARRAY_ADDED_NEGATIVE_PRODUCT_CASE

def findMaxProduct ( arr , n ) :
    ans = - float ( 'inf' )
    maxval = 1
    minval = 1
    for i in range ( 0 , n ) :
        if arr [ i ] > 0 :
            maxval = maxval * arr [ i ]
            minval = min ( 1 , minval * arr [ i ] )
        elif arr [ i ] == 0 :
            minval = 1
            maxval = 0
        elif arr [ i ] < 0 :
            prevMax = maxval
            maxval = minval * arr [ i ]
            minval = prevMax * arr [ i ]
        ans = max ( ans , maxval )
        if maxval <= 0 :
            maxval = 1
    return ans
|||

REARRANGE_ARRAY_SUCH_THAT_EVEN_POSITIONED_ARE_GREATER_THAN_ODD

def assign ( a , n ) :
    a.sort ( )
    ans = [ 0 ] * n
    p = 0
    q = n - 1
    for i in range ( n ) :
        if ( i + 1 ) % 2 == 0 :
            ans [ i ] = a [ q ]
            q = q - 1
        else :
            ans [ i ] = a [ p ]
            p = p + 1
    for i in range ( n ) :
        print ( ans [ i ] , end = " " )
|||

FRIENDS_PAIRING_PROBLEM

def countFriendsPairings ( n ) :
    dp = [ 0 for i in range ( n + 1 ) ]
    for i in range ( n + 1 ) :
        if ( i <= 2 ) :
            dp [ i ] = i
        else :
            dp [ i ] = dp [ i - 1 ] + ( i - 1 ) * dp [ i - 2 ]
    return dp [ n ]
|||

PRIME_NUMBERS

def isPrime ( n ) :
    if ( n <= 1 ) :
        return False
    for i in range ( 2 , n ) :
        if ( n % i == 0 ) :
            return False
    return True
|||

PROBABILITY_REACHING_POINT_2_3_STEPS_TIME

def find_prob ( N , P ) :
    dp = [ 0 ] * ( n + 1 )
    dp [ 0 ] = 1
    dp [ 1 ] = 0
    dp [ 2 ] = P
    dp [ 3 ] = 1 - P
    for i in range ( 4 , N + 1 ) :
        dp [ i ] = ( P ) * dp [ i - 2 ] + ( 1 - P ) * dp [ i - 3 ]
    return dp [ N ]
|||

SMALLEST_OF_THREE_INTEGERS_WITHOUT_COMPARISON_OPERATORS_1

def smallest ( x , y , z ) :
    if ( not ( y / x ) ) :
        return y if ( not ( y / z ) ) else z
    return x if ( not ( x / z ) ) else z
|||

COMMON_ELEMENTS_IN_ALL_ROWS_OF_A_GIVEN_MATRIX

def printCommonElements ( mat ) :
    mp = dict ( )
    for j in range ( N ) :
        mp [ mat [ 0 ] [ j ] ] = 1
    for i in range ( 1 , M ) :
        for j in range ( N ) :
            if ( mat [ i ] [ j ] in mp.keys ( ) and mp [ mat [ i ] [ j ] ] == i ) :
                mp [ mat [ i ] [ j ] ] = i + 1
                if i == M - 1 :
                    print ( mat [ i ] [ j ] , end = " " )
|||

DETECTING_NEGATIVE_CYCLE_USING_FLOYD_WARSHALL

def negCyclefloydWarshall ( graph ) :
    dist = [ [ 0 for i in range ( V + 1 ) ] for j in range ( V + 1 ) ]
    for i in range ( V ) :
        for j in range ( V ) :
            dist [ i ] [ j ] = graph [ i ] [ j ]
    for k in range ( V ) :
        for i in range ( V ) :
            for j in range ( V ) :
                if ( dist [ i ] [ k ] + dist [ k ] [ j ] < dist [ i ] [ j ] ) :
                    dist [ i ] [ j ] = dist [ i ] [ k ] + dist [ k ] [ j ]
    for i in range ( V ) :
        if ( dist [ i ] [ i ] < 0 ) :
            return True
    return False
|||

PROGRAM_SORT_STRING_DESCENDING_ORDER

def sortString ( str ) :
    charCount = [ 0 ] * MAX_CHAR 
    for i in range ( len ( str ) ) :
        charCount [ ord ( str [ i ] ) - ord ( 'a' ) ] += 1 
    for i in range ( MAX_CHAR - 1 , - 1 , - 1 ) :
        for j in range ( charCount [ i ] ) :
            print ( chr ( 97 + i ) , end = "" ) 
|||

COUNT_PAIRS_WITH_GIVEN_SUM

def getPairsCount ( arr , n , sum ) :
    count = 0
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            if arr [ i ] + arr [ j ] == sum :
                count += 1
    return count
|||

SUM_SERIES_12_32_52_2N_12_1

def sumOfSeries ( n ) :
    return int ( ( n * ( 2 * n - 1 ) * ( 2 * n + 1 ) ) / 3 )
|||

MAXIMUM_DIFFERENCE_BETWEEN_FREQUENCY_OF_TWO_ELEMENTS_SUCH_THAT_ELEMENT_HAVING_GREATER_FREQUENCY_IS_ALSO_GREATER

def maxdiff ( arr , n ) :
    freq = defaultdict ( lambda : 0 )
    for i in range ( n ) :
        freq [ arr [ i ] ] += 1
    ans = 0
    for i in range ( n ) :
        for j in range ( n ) :
            if freq [ arr [ i ] ] > freq [ arr [ j ] ] and arr [ i ] > arr [ j ] :
                ans = max ( ans , freq [ arr [ i ] ] - freq [ arr [ j ] ] )
            elif freq [ arr [ i ] ] < freq [ arr [ j ] ] and arr [ i ] < arr [ j ] :
                ans = max ( ans , freq [ arr [ j ] ] - freq [ arr [ i ] ] )
    return ans
|||

SHIFT_MATRIX_ELEMENTS_K

def shiftMatrixByK ( mat , k ) :
    if ( k > N ) :
        print ( "shifting is"" not possible" )
        return
    j = 0
    while ( j < N ) :
        for i in range ( k , N ) :
            print ( "{} ".format ( mat [ j ] [ i ] ) , end = "" )
        for i in range ( 0 , k ) :
            print ( "{} ".format ( mat [ j ] [ i ] ) , end = "" )
        print ( "" )
        j = j + 1
|||

MAXIMUM_AND_MINIMUM_IN_A_SQUARE_MATRIX

def MAXMIN ( arr , n ) :
    MIN = 10 ** 9
    MAX = - 10 ** 9
    for i in range ( n ) :
        for j in range ( n // 2 + 1 ) :
            if ( arr [ i ] [ j ] > arr [ i ] [ n - j - 1 ] ) :
                if ( MIN > arr [ i ] [ n - j - 1 ] ) :
                    MIN = arr [ i ] [ n - j - 1 ]
                if ( MAX < arr [ i ] [ j ] ) :
                    MAX = arr [ i ] [ j ]
            else :
                if ( MIN > arr [ i ] [ j ] ) :
                    MIN = arr [ i ] [ j ]
                if ( MAX < arr [ i ] [ n - j - 1 ] ) :
                    MAX = arr [ i ] [ n - j - 1 ]
    print ( "MAXimum =" , MAX , ", MINimum =" , MIN )
|||

FIND_PAIR_WITH_GREATEST_PRODUCT_IN_ARRAY_1

def findGreatest ( arr , n ) :
    m = dict ( )
    for i in arr :
        m [ i ] = m.get ( i , 0 ) + 1
    arr = sorted ( arr )
    for i in range ( n - 1 , 0 , - 1 ) :
        j = 0
        while ( j < i and arr [ j ] <= sqrt ( arr [ i ] ) ) :
            if ( arr [ i ] % arr [ j ] == 0 ) :
                result = arr [ i ] // arr [ j ]
                if ( result != arr [ j ] and ( result in m.keys ( ) ) and m [ result ] > 0 ) :
                    return arr [ i ]
                elif ( result == arr [ j ] and ( result in m.keys ( ) ) and m [ result ] > 1 ) :
                    return arr [ i ]
            j += 1
    return - 1
|||

0_1_KNAPSACK_PROBLEM_DP_10_1

def knapSack ( W , wt , val , n ) :
    K = [ [ 0 for x in range ( W + 1 ) ] for x in range ( n + 1 ) ]
    for i in range ( n + 1 ) :
        for w in range ( W + 1 ) :
            if i == 0 or w == 0 :
                K [ i ] [ w ] = 0
            elif wt [ i - 1 ] <= w :
                K [ i ] [ w ] = max ( val [ i - 1 ] + K [ i - 1 ] [ w - wt [ i - 1 ] ] , K [ i - 1 ] [ w ] )
            else :
                K [ i ] [ w ] = K [ i - 1 ] [ w ]
    return K [ n ] [ W ]
|||

PROGRAM_DECIMAL_OCTAL_CONVERSION

def decToOctal ( n ) :
    octalNum = [ 0 ] * 100 
    i = 0 
    while ( n != 0 ) :
        octalNum [ i ] = n % 8 
        n = int ( n / 8 ) 
        i += 1 
    for j in range ( i - 1 , - 1 , - 1 ) :
        print ( octalNum [ j ] , end = "" ) 
|||

SUBSEQUENCES_SIZE_THREE_ARRAY_WHOSE_SUM_DIVISIBLE_M_1

def countSubSeq ( A , N , M ) :
    ans = 0
    h = [ 0 ] * M
    for i in range ( 0 , N ) :
        A [ i ] = A [ i ] % M
        h [ A [ i ] ] = h [ A [ i ] ] + 1
    for i in range ( 0 , M ) :
        for j in range ( i , M ) :
            rem = ( M - ( i + j ) % M ) % M
            if ( rem < j ) :
                continue
            if ( i == j and rem == j ) :
                ans = ans + h [ i ] * ( h [ i ] - 1 ) * ( h [ i ] - 2 ) / 6
            elif ( i == j ) :
                ans = ans + ( h [ i ] * ( h [ i ] - 1 ) * h [ rem ] / 2 )
            elif ( i == rem ) :
                ans = ans + h [ i ] * ( h [ i ] - 1 ) * h [ j ] / 2
            elif ( rem == j ) :
                ans = ans + h [ j ] * ( h [ j ] - 1 ) * h [ i ] / 2
            else :
                ans = ans + h [ i ] * h [ j ] * h [ rem ]
        return ans
|||

COUNT_FIBONACCI_NUMBERS_GIVEN_RANGE_LOG_TIME

def countFibs ( low , high ) :
    f1 , f2 , f3 = 0 , 1 , 1
    result = 0
    while ( f1 <= high ) :
        if ( f1 >= low ) :
            result += 1
        f1 = f2
        f2 = f3
        f3 = f1 + f2
    return result
|||

FIND_WHETHER_A_GIVEN_NUMBER_IS_A_POWER_OF_4_OR_NOT_1

def isPowerOfFour ( n ) :
    count = 0
    if ( n and ( not ( n & ( n - 1 ) ) ) ) :
        while ( n > 1 ) :
            n >>= 1
            count += 1
        if ( count % 2 == 0 ) :
            return True
        else :
            return False
|||

FIND_SUM_EVEN_FACTORS_NUMBER

def sumofFactors ( n ) :
    if ( n % 2 != 0 ) :
        return 0
    res = 1
    for i in range ( 2 , ( int ) ( math.sqrt ( n ) ) + 1 ) :
        count = 0
        curr_sum = 1
        curr_term = 1
        while ( n % i == 0 ) :
            count = count + 1
            n = n // i
            if ( i == 2 and count == 1 ) :
                curr_sum = 0
            curr_term = curr_term * i
            curr_sum = curr_sum + curr_term
        res = res * curr_sum
    if ( n >= 2 ) :
        res = res * ( 1 + n )
    return res
|||

FIND_SUM_NON_REPEATING_DISTINCT_ELEMENTS_ARRAY

def findSum ( arr , n ) :
    s = set ( )
    sum = 0
    for i in range ( n ) :
        if arr [ i ] not in s :
            s.add ( arr [ i ] )
    for i in s :
        sum = sum + i
    return sum
|||

DYNAMIC_PROGRAMMING_SET_17_PALINDROME_PARTITIONING_1

def minPalPartion ( str1 ) :
    n = len ( str1 ) 
    C = [ 0 ] * ( n + 1 ) 
    P = [ [ False for x in range ( n + 1 ) ] for y in range ( n + 1 ) ] 
    for i in range ( n ) :
        P [ i ] [ i ] = True 
    for L in range ( 2 , n + 1 ) :
        for i in range ( n - L + 1 ) :
            j = i + L - 1 
            if ( L == 2 ) :
                P [ i ] [ j ] = ( str1 [ i ] == str1 [ j ] ) 
            else :
                P [ i ] [ j ] = ( ( str1 [ i ] == str1 [ j ] ) and P [ i + 1 ] [ j - 1 ] ) 
    for i in range ( n ) :
        if ( P [ 0 ] [ i ] == True ) :
            C [ i ] = 0 
        else :
            C [ i ] = sys.maxsize 
            for j in range ( i ) :
                if ( P [ j + 1 ] [ i ] == True and 1 + C [ j ] < C [ i ] ) :
                    C [ i ] = 1 + C [ j ] 
    return C [ n - 1 ] 
|||

MINIMUM_POSITIVE_POINTS_TO_REACH_DESTINATION

def minInitialPoints ( points ) :
    dp = [ [ 0 for x in range ( C + 1 ) ] for y in range ( R + 1 ) ]
    m , n = R , C
    if points [ m - 1 ] [ n - 1 ] > 0 :
        dp [ m - 1 ] [ n - 1 ] = 1
    else :
        dp [ m - 1 ] [ n - 1 ] = abs ( points [ m - 1 ] [ n - 1 ] ) + 1
    for i in range ( m - 2 , - 1 , - 1 ) :
        dp [ i ] [ n - 1 ] = max ( dp [ i + 1 ] [ n - 1 ] - points [ i ] [ n - 1 ] , 1 )
    for i in range ( 2 , - 1 , - 1 ) :
        dp [ m - 1 ] [ i ] = max ( dp [ m - 1 ] [ i + 1 ] - points [ m - 1 ] [ i ] , 1 )
    for i in range ( m - 2 , - 1 , - 1 ) :
        for j in range ( n - 2 , - 1 , - 1 ) :
            min_points_on_exit = min ( dp [ i + 1 ] [ j ] , dp [ i ] [ j + 1 ] )
            dp [ i ] [ j ] = max ( min_points_on_exit - points [ i ] [ j ] , 1 )
    return dp [ 0 ] [ 0 ]
|||

COUNT_OF_PAIRS_SATISFYING_THE_GIVEN_CONDITION

def countPair ( a , b ) :
    s = str ( b )
    i = 0
    while i < ( len ( s ) ) :
        if ( s [ i ] != '9' ) :
            break
        i += 1
    result = 0
    if ( i == len ( s ) ) :
        result = a * len ( s )
    else :
        result = a * ( len ( s ) - 1 )
    return result
|||

SURVIVAL

def survival ( S , N , M ) :
    if ( ( ( N * 6 ) < ( M * 7 ) and S > 6 ) or M > N ) :
        print ( "No" )
    else :
        days = ( M * S ) / N
        if ( ( ( M * S ) % N ) != 0 ) :
            days += 1
        print ( "Yes " ) ,
        print ( days )
|||

INTERLEAVE_FIRST_HALF_QUEUE_SECOND_HALF

def interLeaveQueue ( q ) :
    if ( q.qsize ( ) % 2 != 0 ) :
        print ( "Input even number of integers." )
    s = [ ]
    halfSize = int ( q.qsize ( ) / 2 )
    for i in range ( halfSize ) :
        s.append ( q.queue [ 0 ] )
        q.get ( )
    while len ( s ) != 0 :
        q.put ( s [ - 1 ] )
        s.pop ( )
    for i in range ( halfSize ) :
        q.put ( q.queue [ 0 ] )
        q.get ( )
    for i in range ( halfSize ) :
        s.append ( q.queue [ 0 ] )
        q.get ( )
    while len ( s ) != 0 :
        q.put ( s [ - 1 ] )
        s.pop ( )
        q.put ( q.queue [ 0 ] )
        q.get ( )
|||

INTEGER_POSITIVE_VALUE_POSITIVE_NEGATIVE_VALUE_ARRAY_1

def findInteger ( arr , n ) :
    neg = 0
    pos = 0
    sum = 0
    for i in range ( 0 , n ) :
        sum += arr [ i ]
        if ( arr [ i ] < 0 ) :
            neg += 1
        else :
            pos += 1
    return ( sum / abs ( neg - pos ) )
|||

FIND_SUM_EVEN_INDEX_BINOMIAL_COEFFICIENTS

def evenSum ( n ) :
    C = [ [ 0 for x in range ( n + 1 ) ] for y in range ( n + 1 ) ]
    for i in range ( 0 , n + 1 ) :
        for j in range ( 0 , min ( i , n + 1 ) ) :
            if j == 0 or j == i :
                C [ i ] [ j ] = 1
            else :
                C [ i ] [ j ] = C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ]
    sum = 0 
    for i in range ( 0 , n + 1 ) :
        if n % 2 == 0 :
            sum = sum + C [ n ] [ i ]
    return sum
|||

DELANNOY_NUMBER

def dealnnoy ( n , m ) :
    if ( m == 0 or n == 0 ) :
        return 1
    return dealnnoy ( m - 1 , n ) + dealnnoy ( m - 1 , n - 1 ) + dealnnoy ( m , n - 1 )
|||

FIND_THE_LARGEST_SUBARRAY_WITH_0_SUM

def maxLen ( arr ) :
    max_len = 0
    for i in range ( len ( arr ) ) :
        curr_sum = 0
        for j in range ( i , len ( arr ) ) :
            curr_sum += arr [ j ]
            if curr_sum == 0 :
                max_len = max ( max_len , j - i + 1 )
    return max_len
|||

NEXT_POWER_OF_2

def nextPowerOf2 ( n ) :
    count = 0 
    if ( n and not ( n & ( n - 1 ) ) ) :
        return n
    while ( n != 0 ) :
        n >>= 1
        count += 1
    return 1 << count 
|||

LONGEST_GEOMETRIC_PROGRESSION

def lenOfLongestGP ( sett , n ) :
    if n < 2 :
        return n
    if n == 2 :
        return ( sett [ 1 ] % sett [ 0 ] == 0 )
    sett.sort ( )
    L = [ [ 0 for i in range ( n ) ] for i in range ( n ) ]
    llgp = 1
    for i in range ( 0 , n ) :
        if sett [ n - 1 ] % sett [ i ] == 0 :
            L [ i ] [ n - 1 ] = 2
        else :
            L [ i ] [ n - 1 ] = 1
    for j in range ( n - 2 , 0 , - 1 ) :
        i = j - 1
        k = j + 1
        while i >= 0 and k <= n - 1 :
            if sett [ i ] * sett [ k ] < sett [ j ] * sett [ j ] :
                k += 1
            elif sett [ i ] * sett [ k ] > sett [ j ] * sett [ j ] :
                if sett [ j ] % sett [ i ] == 0 :
                    L [ i ] [ j ] = 2
                else :
                    L [ i ] [ j ] = 1
                i -= 1
            else :
                L [ i ] [ j ] = L [ j ] [ k ] + 1
                if L [ i ] [ j ] > llgp :
                    llgp = L [ i ] [ j ]
                i -= 1
                k + 1
        while i >= 0 :
            if sett [ j ] % sett [ i ] == 0 :
                L [ i ] [ j ] = 2
            else :
                L [ i ] [ j ] = 1
            i -= 1
    return llgp
|||

DYNAMIC_PROGRAMMING_SET_6_MIN_COST_PATH

def minCost ( cost , m , n ) :
    tc = [ [ 0 for x in range ( C ) ] for x in range ( R ) ]
    tc [ 0 ] [ 0 ] = cost [ 0 ] [ 0 ]
    for i in range ( 1 , m + 1 ) :
        tc [ i ] [ 0 ] = tc [ i - 1 ] [ 0 ] + cost [ i ] [ 0 ]
    for j in range ( 1 , n + 1 ) :
        tc [ 0 ] [ j ] = tc [ 0 ] [ j - 1 ] + cost [ 0 ] [ j ]
    for i in range ( 1 , m + 1 ) :
        for j in range ( 1 , n + 1 ) :
            tc [ i ] [ j ] = min ( tc [ i - 1 ] [ j - 1 ] , tc [ i - 1 ] [ j ] , tc [ i ] [ j - 1 ] ) + cost [ i ] [ j ]
    return tc [ m ] [ n ]
|||

PROGRAM_DISTANCE_TWO_POINTS_EARTH

def distance ( lat1 , lat2 , lon1 , lon2 ) :
    lon1 = radians ( lon1 )
    lon2 = radians ( lon2 )
    lat1 = radians ( lat1 )
    lat2 = radians ( lat2 )
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin ( dlat / 2 ) ** 2 + cos ( lat1 ) * cos ( lat2 ) * sin ( dlon / 2 ) ** 2
    c = 2 * asin ( sqrt ( a ) )
    r = 6371
    return ( c * r )
|||

BIN_PACKING_PROBLEM_MINIMIZE_NUMBER_OF_USED_BINS

def nextfit ( weight , c ) :
    res = 0
    rem = c
    for _ in range ( len ( weight ) ) :
        if rem >= weight [ _ ] :
            rem = rem - weight [ _ ]
        else :
            res += 1
            rem = c - weight [ _ ]
    return res
|||

FIND_SUBARRAY_WITH_GIVEN_SUM_1

def subArraySum ( arr , n , sum ) :
    curr_sum = arr [ 0 ]
    start = 0
    i = 1
    while i <= n :
        while curr_sum > sum and start < i - 1 :
            curr_sum = curr_sum - arr [ start ]
            start += 1
        if curr_sum == sum :
            print ( "Sum found between indexes" )
            print ( "%d and %d" % ( start , i - 1 ) )
            return 1
        if i < n :
            curr_sum = curr_sum + arr [ i ]
        i += 1
    print ( "No subarray found" )
    return 0
|||

SPACE_OPTIMIZED_DP_SOLUTION_0_1_KNAPSACK_PROBLEM_1

def KnapSack ( val , wt , n , W ) :
    dp = [ 0 ] * ( W + 1 ) 
    for i in range ( n ) :
        for j in range ( W , wt [ i ] , - 1 ) :
            dp [ j ] = max ( dp [ j ] , val [ i ] + dp [ j - wt [ i ] ] ) 
    return dp [ W ] 
|||

FIND_VALUE_OF_Y_MOD_2_RAISED_TO_POWER_X

def yMod ( y , x ) :
    return ( y % pow ( 2 , x ) )
|||

SUM_SERIES_23_45_67_89_UPTO_N_TERMS

def seriesSum ( n ) :
    i = 1 
    res = 0.0 
    sign = True 
    while ( n > 0 ) :
        n = n - 1 
        if ( sign ) :
            sign = False 
            res = res + ( i + 1 ) / ( i + 2 ) 
            i = i + 2 
        else :
            sign = True 
            res = res - ( i + 1 ) / ( i + 2 ) 
            i = i + 2 
    return res 
|||

LENGTH_LONGEST_STRICT_BITONIC_SUBSEQUENCE

def longLenStrictBitonicSub ( arr , n ) :
    inc , dcr = dict ( ) , dict ( )
    len_inc , len_dcr = [ 0 ] * n , [ 0 ] * n
    longLen = 0
    for i in range ( n ) :
        len = 0
        if inc.get ( arr [ i ] - 1 ) in inc.values ( ) :
            len = inc.get ( arr [ i ] - 1 )
        inc [ arr [ i ] ] = len_inc [ i ] = len + 1
    for i in range ( n - 1 , - 1 , - 1 ) :
        len = 0
        if dcr.get ( arr [ i ] - 1 ) in dcr.values ( ) :
            len = dcr.get ( arr [ i ] - 1 )
        dcr [ arr [ i ] ] = len_dcr [ i ] = len + 1
    for i in range ( n ) :
        if longLen < ( len_inc [ i ] + len_dcr [ i ] - 1 ) :
            longLen = len_inc [ i ] + len_dcr [ i ] - 1
    return longLen
|||

MAXIMUM_DISTANCE_TWO_OCCURRENCES_ELEMENT_ARRAY

def maxDistance ( arr , n ) :
    mp = { }
    maxDict = 0
    for i in range ( n ) :
        if arr [ i ] not in mp.keys ( ) :
            mp [ arr [ i ] ] = i
        else :
            maxDict = max ( maxDict , i - mp [ arr [ i ] ] )
    return maxDict
|||

FIND_RECTANGLE_BINARY_MATRIX_CORNERS_1_1

def isRectangle ( matrix ) :
    rows = len ( matrix )
    if ( rows == 0 ) :
        return False
    columns = len ( matrix [ 0 ] )
    table = { }
    for i in range ( rows ) :
        for j in range ( columns - 1 ) :
            for k in range ( j + 1 , columns ) :
                if ( matrix [ i ] [ j ] == 1 and matrix [ i ] [ k ] == 1 ) :
                    if ( j in table and k in table [ j ] ) :
                        return True
                    if ( k in table and j in table [ k ] ) :
                        return True
                    if j not in table :
                        table [ j ] = set ( )
                    if k not in table :
                        table [ k ] = set ( )
                    table [ j ].add ( k )
                    table [ k ].add ( j )
    return False
|||

COUNT_MINIMUM_NUMBER_SUBSETS_SUBSEQUENCES_CONSECUTIVE_NUMBERS

def numofsubset ( arr , n ) :
    x = sorted ( arr )
    count = 1
    for i in range ( 0 , n - 1 ) :
        if ( x [ i ] + 1 != x [ i + 1 ] ) :
            count = count + 1
    return count
|||

LARGEST_SUM_CONTIGUOUS_SUBARRAY

def maxSubArraySum ( a , size ) :
    max_so_far = - maxint - 1
    max_ending_here = 0
    for i in range ( 0 , size ) :
        max_ending_here = max_ending_here + a [ i ]
        if ( max_so_far < max_ending_here ) :
            max_so_far = max_ending_here
        if max_ending_here < 0 :
            max_ending_here = 0
    return max_so_far
|||

PROGRAM_TO_FIND_REMAINDER_WITHOUT_USING_MODULO_OR_OPERATOR_2

def getRemainder ( num , divisor ) :
    while ( num >= divisor ) :
        num -= divisor 
    return num 
|||

CHECK_LARGE_NUMBER_DIVISIBLE_4_NOT

def check ( st ) :
    n = len ( st )
    if ( n == 0 ) :
        return False
    if ( n == 1 ) :
        return ( ( st [ 0 ] - '0' ) % 4 == 0 )
    last = ( int ) ( st [ n - 1 ] )
    second_last = ( int ) ( st [ n - 2 ] )
    return ( ( second_last * 10 + last ) % 4 == 0 )
|||

FIND_THE_ELEMENT_THAT_APPEARS_ONCE_1

def getSingle ( arr , n ) :
    result = 0
    for i in range ( 0 , INT_SIZE ) :
        sm = 0
        x = ( 1 << i )
        for j in range ( 0 , n ) :
            if ( arr [ j ] & x ) :
                sm = sm + 1
        if ( sm % 3 ) :
            result = result | x
    return result
|||

NUMBER_RECTANGLES_NM_GRID

def rectCount ( n , m ) :
    return ( m * n * ( n + 1 ) * ( m + 1 ) ) // 4
|||

MAXIMUM_POINTS_INTERSECTION_N_CIRCLES

def intersection ( n ) :
    return n * ( n - 1 ) 
|||

ADD_1_TO_A_GIVEN_NUMBER

def f_gold ( x ) :
    m = 1 
    while ( x & m ) :
        x = x ^ m
        m <<= 1
    x = x ^ m
    return x
|||

ADD_TWO_NUMBERS_WITHOUT_USING_ARITHMETIC_OPERATORS

def f_gold ( x , y ) :
    while ( y != 0 ) :
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x
|||

AREA_OF_THE_CIRCLE_THAT_HAS_A_SQUARE_AND_A_CIRCLE_INSCRIBED_IN_IT

def f_gold ( a ) :
    area = ( math.pi * a * a ) / 4
    return area
|||

ARRAY_RANGE_QUERIES_ELEMENTS_FREQUENCY_VALUE

def f_gold ( start , end , arr ) :
    frequency = dict ( )
    for i in range ( start , end + 1 ) :
        if arr [ i ] in frequency.keys ( ) :
            frequency [ arr [ i ] ] += 1
        else :
            frequency [ arr [ i ] ] = 1
    count = 0
    for x in frequency :
        if x == frequency [ x ] :
            count += 1
    return count
|||

BELL_NUMBERS_NUMBER_OF_WAYS_TO_PARTITION_A_SET

def f_gold ( n ) :
    bell = [ [ 0 for i in range ( n + 1 ) ] for j in range ( n + 1 ) ]
    bell [ 0 ] [ 0 ] = 1
    for i in range ( 1 , n + 1 ) :
        bell [ i ] [ 0 ] = bell [ i - 1 ] [ i - 1 ]
        for j in range ( 1 , i + 1 ) :
            bell [ i ] [ j ] = bell [ i - 1 ] [ j - 1 ] + bell [ i ] [ j - 1 ]
    return bell [ n ] [ 0 ]
|||

BINARY_SEARCH

def f_gold ( arr , l , r , x ) :
    if r >= l :
        mid = l + ( r - l ) // 2
        if arr [ mid ] == x :
            return mid
        elif arr [ mid ] > x :
            return f_gold ( arr , l , mid - 1 , x )
        else :
            return f_gold ( arr , mid + 1 , r , x )
    else :
        return - 1
|||

BREAK_NUMBER_THREE_PARTS_1

def f_gold ( n ) :
    count = 0
    count = ( n + 1 ) * ( n + 2 ) // 2
    return count
|||

CALCULATE_ANGLE_HOUR_HAND_MINUTE_HAND

def f_gold ( h , m ) :
    if ( h < 0 or m < 0 or h > 12 or m > 60 ) :
        print ( 'Wrong input' )
    if ( h == 12 ) :
        h = 0
    if ( m == 60 ) :
        m = 0
    hour_angle = 0.5 * ( h * 60 + m )
    minute_angle = 6 * m
    angle = abs ( hour_angle - minute_angle )
    angle = min ( 360 - angle , angle )
    return angle
|||

CALCULATE_MAXIMUM_VALUE_USING_SIGN_TWO_NUMBERS_STRING

def f_gold ( str ) :
    res = ord ( str [ 0 ] ) - 48
    for i in range ( 1 , len ( str ) ) :
        if ( str [ i ] == '0' or str [ i ] == '1' or res < 2 ) :
            res += ord ( str [ i ] ) - 48
        else :
            res *= ord ( str [ i ] ) - 48
    return res
|||

CALCULATE_VOLUME_DODECAHEDRON

def f_gold ( side ) :
    return ( ( ( 15 + ( 7 * ( math.sqrt ( 5 ) ) ) ) / 4 ) * ( math.pow ( side , 3 ) ) )
|||

CEILING_IN_A_SORTED_ARRAY

def f_gold ( arr , low , high , x ) :
    if x <= arr [ low ] :
        return low
    i = low
    for i in range ( high ) :
        if arr [ i ] == x :
            return i
        if arr [ i ] < x and arr [ i + 1 ] >= x :
            return i + 1
    return - 1
|||

CEILING_IN_A_SORTED_ARRAY_1

def f_gold ( arr , low , high , x ) :
    if x <= arr [ low ] :
        return low
    if x > arr [ high ] :
        return - 1
    mid = ( low + high ) / 2 
    if arr [ mid ] == x :
        return mid
    elif arr [ mid ] < x :
        if mid + 1 <= high and x <= arr [ mid + 1 ] :
            return mid + 1
        else :
            return f_gold ( arr , mid + 1 , high , x )
    else :
        if mid - 1 >= low and x > arr [ mid - 1 ] :
            return mid
        else :
            return f_gold ( arr , low , mid - 1 , x )
|||

CENTER_ELEMENT_OF_MATRIX_EQUALS_SUMS_OF_HALF_DIAGONALS

def f_gold ( mat , n ) :
    diag1_left = 0
    diag1_right = 0
    diag2_left = 0
    diag2_right = 0
    i = 0
    j = n - 1
    while i < n :
        if ( i < n // 2 ) :
            diag1_left += mat [ i ] [ i ]
            diag2_left += mat [ j ] [ i ]
        elif ( i > n // 2 ) :
            diag1_right += mat [ i ] [ i ]
            diag2_right += mat [ j ] [ i ]
        i += 1
        j -= 1
    return ( diag1_left == diag2_right and diag2_right == diag2_left and diag1_right == diag2_left and diag2_right == mat [ n // 2 ] [ n // 2 ] )
|||

CHANGE_BITS_CAN_MADE_ONE_FLIP

def f_gold ( str ) :
    zeros = 0
    ones = 0
    for i in range ( 0 , len ( str ) ) :
        ch = str [ i ] 
        if ( ch == '0' ) :
            zeros = zeros + 1
        else :
            ones = ones + 1
    return ( zeros == 1 or ones == 1 ) 
|||

CHECK_ARRAY_CONTAINS_CONTIGUOUS_INTEGERS_DUPLICATES_ALLOWED

def f_gold ( arr , n ) :
    max1 = max ( arr )
    min1 = min ( arr )
    m = max1 - min1 + 1
    if ( m > n ) :
        return False
    visited = [ 0 ] * m
    for i in range ( 0 , n ) :
        visited [ arr [ i ] - min1 ] = True
    for i in range ( 0 , m ) :
        if ( visited [ i ] == False ) :
            return False
    return True
|||

CHECK_IF_ALL_THE_ELEMENTS_CAN_BE_MADE_OF_SAME_PARITY_BY_INVERTING_ADJACENT_ELEMENTS

def f_gold ( a , n ) :
    count_odd = 0 ; count_even = 0 
    for i in range ( n ) :
        if ( a [ i ] & 1 ) :
            count_odd += 1 
        else :
            count_even += 1 
    if ( count_odd % 2 and count_even % 2 ) :
        return False 
    else :
        return True 
|||

CHECK_IF_A_NUMBER_IS_JUMBLED_OR_NOT

def f_gold ( num ) :
    if ( num // 10 == 0 ) :
        return True
    while ( num != 0 ) :
        if ( num // 10 == 0 ) :
            return True
        digit1 = num % 10
        digit2 = ( num // 10 ) % 10
        if ( abs ( digit2 - digit1 ) > 1 ) :
            return False
        num = num // 10
    return True
|||

CHECK_IF_X_CAN_GIVE_CHANGE_TO_EVERY_PERSON_IN_THE_QUEUE

def f_gold ( notes , n ) :
    fiveCount = 0
    tenCount = 0
    for i in range ( n ) :
        if ( notes [ i ] == 5 ) :
            fiveCount += 1
        elif ( notes [ i ] == 10 ) :
            if ( fiveCount > 0 ) :
                fiveCount -= 1
                tenCount += 1
            else :
                return 0
        else :
            if ( fiveCount > 0 and tenCount > 0 ) :
                fiveCount -= 1
                tenCount -= 1
            elif ( fiveCount >= 3 ) :
                fiveCount -= 3
            else :
                return 0
    return 1
|||

CHECK_INTEGER_OVERFLOW_MULTIPLICATION

def f_gold ( a , b ) :
    if ( a == 0 or b == 0 ) :
        return False
    result = a * b
    if ( result >= 9223372036854775807 or result <= - 9223372036854775808 ) :
        result = 0
    if ( a == ( result // b ) ) :
        print ( result // b )
        return False
    else :
        return True
|||

CHECK_LINE_PASSES_ORIGIN

def f_gold ( x1 , y1 , x2 , y2 ) :
    return ( x1 * ( y2 - y1 ) == y1 * ( x2 - x1 ) )
|||

CHECK_POSSIBLE_SORT_ARRAY_CONDITIONAL_SWAPPING_ADJACENT_ALLOWED

def f_gold ( arr , n ) :
    for i in range ( 0 , n - 1 ) :
        if ( arr [ i ] > arr [ i + 1 ] ) :
            if ( arr [ i ] - arr [ i + 1 ] == 1 ) :
                arr [ i ] , arr [ i + 1 ] = arr [ i + 1 ] , arr [ i ]
            else :
                return False
    return True
|||

CHECK_POSSIBLE_TRANSFORM_ONE_STRING_ANOTHER

def f_gold ( s1 , s2 ) :
    n = len ( s1 )
    m = len ( s2 )
    dp = ( [ [ False for i in range ( m + 1 ) ] for i in range ( n + 1 ) ] )
    dp [ 0 ] [ 0 ] = True
    for i in range ( len ( s1 ) ) :
        for j in range ( len ( s2 ) + 1 ) :
            if ( dp [ i ] [ j ] ) :
                if ( ( j < len ( s2 ) and ( s1 [ i ].upper ( ) == s2 [ j ] ) ) ) :
                    dp [ i + 1 ] [ j + 1 ] = True
                if ( s1 [ i ].isupper ( ) == False ) :
                    dp [ i + 1 ] [ j ] = True
    return ( dp [ n ] [ m ] )
|||

CHECK_REVERSING_SUB_ARRAY_MAKE_ARRAY_SORTED

def f_gold ( arr , n ) :
    temp = [ 0 ] * n
    for i in range ( n ) :
        temp [ i ] = arr [ i ]
    temp.sort ( )
    for front in range ( n ) :
        if temp [ front ] != arr [ front ] :
            break
    for back in range ( n - 1 , - 1 , - 1 ) :
        if temp [ back ] != arr [ back ] :
            break
    if front >= back :
        return True
    while front != back :
        front += 1
        if arr [ front - 1 ] < arr [ front ] :
            return False
    return True
|||

CHECK_REVERSING_SUB_ARRAY_MAKE_ARRAY_SORTED_1

def f_gold ( arr , n ) :
    if ( n == 1 ) :
        return True
    i = 1
    for i in range ( 1 , n ) :
        if arr [ i - 1 ] < arr [ i ] :
            if ( i == n ) :
                return True
    j = i
    while ( arr [ j ] < arr [ j - 1 ] ) :
        if ( i > 1 and arr [ j ] < arr [ i - 2 ] ) :
            return False
        j += 1
    if ( j == n ) :
        return True
    k = j
    if ( arr [ k ] < arr [ i - 1 ] ) :
        return False
    while ( k > 1 and k < n ) :
        if ( arr [ k ] < arr [ k - 1 ] ) :
            return False
        k += 1
    return True
|||

CHECK_VALID_SEQUENCE_DIVISIBLE_M_1

def f_gold ( n , index , modulo , M , arr , dp ) :
    modulo = ( ( modulo % M ) + M ) % M
    if ( index == n ) :
        if ( modulo == 0 ) :
            return 1
        return 0
    if ( dp [ index ] [ modulo ] != - 1 ) :
        return dp [ index ] [ modulo ]
    placeAdd = f_gold ( n , index + 1 , modulo + arr [ index ] , M , arr , dp )
    placeMinus = f_gold ( n , index + 1 , modulo - arr [ index ] , M , arr , dp )
    res = bool ( placeAdd or placeMinus )
    dp [ index ] [ modulo ] = res
    return res
|||

CHECK_WHETHER_GIVEN_NUMBER_EVEN_ODD_1

def f_gold ( n ) :
    return ( not ( n & 1 ) )
|||

CHECK_WHETHER_TWO_STRINGS_ARE_ANAGRAM_OF_EACH_OTHER

def f_gold ( str1 , str2 ) :
    n1 = len ( str1 )
    n2 = len ( str2 )
    if n1 != n2 :
        return 0
    str1 = sorted ( str1 )
    str2 = sorted ( str2 )
    for i in range ( 0 , n1 ) :
        if str1 [ i ] != str2 [ i ] :
            return 0
    return 1
|||

CHOCOLATE_DISTRIBUTION_PROBLEM

def f_gold ( arr , n , m ) :
    if ( m == 0 or n == 0 ) :
        return 0
    arr.sort ( )
    if ( n < m ) :
        return - 1
    min_diff = sys.maxsize
    first = 0
    last = 0
    i = 0
    while ( i + m - 1 < n ) :
        diff = arr [ i + m - 1 ] - arr [ i ]
        if ( diff < min_diff ) :
            min_diff = diff
            first = i
            last = i + m - 1
        i += 1
    return ( arr [ last ] - arr [ first ] )
|||

CIRCLE_LATTICE_POINTS

def f_gold ( r ) :
    if ( r <= 0 ) :
        return 0
    result = 4
    for x in range ( 1 , r ) :
        ySquare = r * r - x * x
        y = int ( math.sqrt ( ySquare ) )
        if ( y * y == ySquare ) :
            result += 4
    return result
|||

COMPOSITE_NUMBER

def f_gold ( n ) :
    if ( n <= 1 ) :
        return False
    if ( n <= 3 ) :
        return False
    if ( n % 2 == 0 or n % 3 == 0 ) :
        return True
    i = 5
    while ( i * i <= n ) :
        if ( n % i == 0 or n % ( i + 2 ) == 0 ) :
            return True
        i = i + 6
    return False
|||

COMPUTE_NCR_P_SET_1_INTRODUCTION_AND_DYNAMIC_PROGRAMMING_SOLUTION

def f_gold ( n , r , p ) :
    C = [ 0 for i in range ( r + 1 ) ]
    C [ 0 ] = 1
    for i in range ( 1 , n + 1 ) :
        for j in range ( min ( i , r ) , 0 , - 1 ) :
            C [ j ] = ( C [ j ] + C [ j - 1 ] ) % p
    return C [ r ]
|||

COUNT_ARRAYS_CONSECUTIVE_ELEMENT_DIFFERENT_VALUES

def f_gold ( n , k , x ) :
    dp = list ( )
    dp.append ( 0 )
    dp.append ( 1 )
    i = 2
    while i < n :
        dp.append ( ( k - 2 ) * dp [ i - 1 ] + ( k - 1 ) * dp [ i - 2 ] )
        i = i + 1
    return ( ( k - 1 ) * dp [ n - 2 ] if x == 1 else dp [ n - 1 ] )
|||

COUNT_DIGITS_FACTORIAL_SET_1

def f_gold ( n ) :
    if ( n < 0 ) :
        return 0 
    if ( n <= 1 ) :
        return 1 
    digits = 0 
    for i in range ( 2 , n + 1 ) :
        digits += math.log10 ( i ) 
    return math.floor ( digits ) + 1 
|||

COUNT_ENTRIES_EQUAL_TO_X_IN_A_SPECIAL_MATRIX

def f_gold ( n , x ) :
    cnt = 0
    for i in range ( 1 , n + 1 ) :
        if i <= x :
            if x // i <= n and x % i == 0 :
                cnt += 1
    return cnt
|||

COUNT_FACTORIAL_NUMBERS_IN_A_GIVEN_RANGE

def f_gold ( low , high ) :
    fact = 1
    x = 1
    while ( fact < low ) :
        fact = fact * x
        x += 1
    res = 0
    while ( fact <= high ) :
        res += 1
        fact = fact * x
        x += 1
    return res
|||

COUNT_FREQUENCY_K_MATRIX_SIZE_N_MATRIXI_J_IJ

def f_gold ( n , k ) :
    if ( n + 1 >= k ) :
        return ( k - 1 )
    else :
        return ( 2 * n + 1 - k )
|||

COUNT_INDEX_PAIRS_EQUAL_ELEMENTS_ARRAY

def f_gold ( arr , n ) :
    ans = 0
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            if ( arr [ i ] == arr [ j ] ) :
                ans += 1
    return ans
|||

COUNT_NUMBER_OF_SOLUTIONS_OF_X2_1_MOD_P_IN_GIVEN_RANGE

def f_gold ( n , p ) :
    ans = 0 
    for x in range ( 1 , p ) :
        if ( ( x * x ) % p == 1 ) :
            last = x + p * ( n / p ) 
            if ( last > n ) :
                last -= p 
            ans += ( ( last - x ) / p + 1 ) 
    return int ( ans ) 
|||

COUNT_NUMBER_OF_WAYS_TO_COVER_A_DISTANCE_1

def f_gold ( dist ) :
    count = [ 0 ] * ( dist + 1 )
    count [ 0 ] = 1
    count [ 1 ] = 1
    count [ 2 ] = 2
    for i in range ( 3 , dist + 1 ) :
        count [ i ] = ( count [ i - 1 ] + count [ i - 2 ] + count [ i - 3 ] )
    return count [ dist ] 
|||

COUNT_NUMBER_OF_WAYS_TO_FILL_A_N_X_4_GRID_USING_1_X_4_TILES

def f_gold ( n ) :
    dp = [ 0 for _ in range ( n + 1 ) ]
    for i in range ( 1 , n + 1 ) :
        if i <= 3 :
            dp [ i ] = 1
        elif i == 4 :
            dp [ i ] = 2
        else :
            dp [ i ] = dp [ i - 1 ] + dp [ i - 4 ]
    return dp [ n ]
|||

COUNT_OF_OCCURRENCES_OF_A_101_PATTERN_IN_A_STRING

def f_gold ( s ) :
    length = len ( s )
    oneSeen = False
    count = 0
    for i in range ( length ) :
        if ( s [ i ] == '1' and oneSeen ) :
            if ( s [ i - 1 ] == '0' ) :
                count += 1
        if ( s [ i ] == '1' and oneSeen == 0 ) :
            oneSeen = True
        if ( s [ i ] != '0' and s [ i ] != '1' ) :
            oneSeen = False
    return count
|||

COUNT_PAIRS_DIFFERENCE_EQUAL_K

def f_gold ( arr , n , k ) :
    count = 0
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            if arr [ i ] - arr [ j ] == k or arr [ j ] - arr [ i ] == k :
                count += 1
    return count
|||

COUNT_PAIRS_TWO_SORTED_ARRAYS_WHOSE_SUM_EQUAL_GIVEN_VALUE_X

def f_gold ( arr1 , arr2 , m , n , x ) :
    count = 0
    for i in range ( m ) :
        for j in range ( n ) :
            if arr1 [ i ] + arr2 [ j ] == x :
                count = count + 1
    return count
|||

COUNT_PALINDROMIC_SUBSEQUENCE_GIVEN_STRING

def f_gold ( str ) :
    N = len ( str )
    cps = [ [ 0 for i in range ( N + 2 ) ] for j in range ( N + 2 ) ]
    for i in range ( N ) :
        cps [ i ] [ i ] = 1
    for L in range ( 2 , N + 1 ) :
        for i in range ( N ) :
            k = L + i - 1
            if ( k < N ) :
                if ( str [ i ] == str [ k ] ) :
                    cps [ i ] [ k ] = ( cps [ i ] [ k - 1 ] + cps [ i + 1 ] [ k ] + 1 )
                else :
                    cps [ i ] [ k ] = ( cps [ i ] [ k - 1 ] + cps [ i + 1 ] [ k ] - cps [ i + 1 ] [ k - 1 ] )
    return cps [ 0 ] [ N - 1 ]
|||

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX_2

def f_gold ( p , q ) :
    dp = [ 1 for i in range ( q ) ]
    for i in range ( p - 1 ) :
        for j in range ( 1 , q ) :
            dp [ j ] += dp [ j - 1 ]
    return dp [ q - 1 ]
|||

COUNT_SET_BITS_IN_AN_INTEGER_2

def f_gold ( n ) :
    count = 0
    while ( n ) :
        n &= ( n - 1 )
        count += 1
    return count
|||

COUNT_SET_BITS_IN_AN_INTEGER_3

def f_gold ( n ) :
    if ( n == 0 ) :
        return 0
    else :
        return 1 + f_gold ( n & ( n - 1 ) )
|||

COUNT_SORTED_ROWS_MATRIX

def f_gold ( mat , r , c ) :
    result = 0
    for i in range ( r ) :
        j = 0
        for j in range ( c - 1 ) :
            if mat [ i ] [ j + 1 ] <= mat [ i ] [ j ] :
                break
        if j == c - 2 :
            result += 1
    for i in range ( 0 , r ) :
        j = 0
        for j in range ( c - 1 , 0 , - 1 ) :
            if mat [ i ] [ j - 1 ] <= mat [ i ] [ j ] :
                break
        if c > 1 and j == 1 :
            result += 1
    return result
|||

COUNT_STRINGS_CAN_FORMED_USING_B_C_GIVEN_CONSTRAINTS_1

def f_gold ( n ) :
    return ( 1 + ( n * 2 ) + ( n * ( ( n * n ) - 1 ) // 2 ) )
|||

COUNT_SUBARRAYS_EQUAL_NUMBER_1S_0S

def f_gold ( arr , n ) :
    um = dict ( )
    curr_sum = 0
    for i in range ( n ) :
        curr_sum += ( - 1 if ( arr [ i ] == 0 ) else arr [ i ] )
        if um.get ( curr_sum ) :
            um [ curr_sum ] += 1
        else :
            um [ curr_sum ] = 1
    count = 0
    for itr in um :
        if um [ itr ] > 1 :
            count += ( ( um [ itr ] * int ( um [ itr ] - 1 ) ) / 2 )
    if um.get ( 0 ) :
        count += um [ 0 ]
    return int ( count )
|||

COUNT_SUBARRAYS_EQUAL_NUMBER_1S_0S_1

def f_gold ( arr , n ) :
    mp = dict ( )
    Sum = 0
    count = 0
    for i in range ( n ) :
        if ( arr [ i ] == 0 ) :
            arr [ i ] = - 1
        Sum += arr [ i ]
        if ( Sum == 0 ) :
            count += 1
        if ( Sum in mp.keys ( ) ) :
            count += mp [ Sum ]
        mp [ Sum ] = mp.get ( Sum , 0 ) + 1
    return count
|||

COUNT_SUBARRAYS_TOTAL_DISTINCT_ELEMENTS_ORIGINAL_ARRAY

def f_gold ( arr , n ) :
    vis = dict ( )
    for i in range ( n ) :
        vis [ arr [ i ] ] = 1
    k = len ( vis )
    vid = dict ( )
    ans = 0
    right = 0
    window = 0
    for left in range ( n ) :
        while ( right < n and window < k ) :
            if arr [ right ] in vid.keys ( ) :
                vid [ arr [ right ] ] += 1
            else :
                vid [ arr [ right ] ] = 1
            if ( vid [ arr [ right ] ] == 1 ) :
                window += 1
            right += 1
        if ( window == k ) :
            ans += ( n - right + 1 )
        vid [ arr [ left ] ] -= 1
        if ( vid [ arr [ left ] ] == 0 ) :
            window -= 1
    return ans
|||

COUNT_SUBARRAYS_WITH_SAME_EVEN_AND_ODD_ELEMENTS

def f_gold ( arr , n ) :
    difference = 0
    ans = 0
    hash_positive = [ 0 ] * ( n + 1 )
    hash_negative = [ 0 ] * ( n + 1 )
    hash_positive [ 0 ] = 1
    for i in range ( n ) :
        if ( arr [ i ] & 1 == 1 ) :
            difference = difference + 1
        else :
            difference = difference - 1
        if ( difference < 0 ) :
            ans += hash_negative [ - difference ]
            hash_negative [ - difference ] = hash_negative [ - difference ] + 1
        else :
            ans += hash_positive [ difference ]
            hash_positive [ difference ] = hash_positive [ difference ] + 1
    return ans
|||

COUNT_SUBSTRINGS_WITH_SAME_FIRST_AND_LAST_CHARACTERS

def f_gold ( s ) :
    result = 0 
    n = len ( s ) 
    for i in range ( n ) :
        for j in range ( i , n ) :
            if ( s [ i ] == s [ j ] ) :
                result = result + 1
    return result
|||

COUNT_SUM_OF_DIGITS_IN_NUMBERS_FROM_1_TO_N

def f_gold ( n ) :
    if ( n < 10 ) :
        return ( n * ( n + 1 ) / 2 )
    d = ( int ) ( math.log10 ( n ) )
    a = [ 0 ] * ( d + 1 )
    a [ 0 ] = 0
    a [ 1 ] = 45
    for i in range ( 2 , d + 1 ) :
        a [ i ] = a [ i - 1 ] * 10 + 45 * ( int ) ( math.ceil ( math.pow ( 10 , i - 1 ) ) )
    p = ( int ) ( math.ceil ( math.pow ( 10 , d ) ) )
    msd = n // p
    return ( int ) ( msd * a [ d ] + ( msd * ( msd - 1 ) // 2 ) * p + msd * ( 1 + n % p ) + f_gold ( n % p ) )
|||

COUNT_WAYS_DIVIDE_CIRCLE_USING_N_NON_INTERSECTING_CHORDS

def f_gold ( A ) :
    n = 2 * A
    dpArray = [ 0 ] * ( n + 1 )
    dpArray [ 0 ] = 1
    dpArray [ 2 ] = 1
    for i in range ( 4 , n + 1 , 2 ) :
        for j in range ( 0 , i - 1 , 2 ) :
            dpArray [ i ] += ( dpArray [ j ] * dpArray [ i - 2 - j ] )
    return int ( dpArray [ n ] )
|||

COUNT_WORDS_APPEAR_EXACTLY_TWO_TIMES_ARRAY_WORDS

def f_gold ( stri , n ) :
    m = dict ( )
    for i in range ( n ) :
        m [ stri [ i ] ] = m.get ( stri [ i ] , 0 ) + 1
    res = 0
    for i in m.values ( ) :
        if i == 2 :
            res += 1
    return res
|||

C_PROGRAM_FACTORIAL_NUMBER_1

def f_gold ( n ) :
    return 1 if ( n == 1 or n == 0 ) else n * f_gold ( n - 1 ) 
|||

C_PROGRAM_FACTORIAL_NUMBER_2

def f_gold ( n ) :
    return 1 if ( n == 1 or n == 0 ) else n * f_gold ( n - 1 )
|||

C_PROGRAM_FIND_LARGEST_ELEMENT_ARRAY_1

def f_gold ( arr , n ) :
    return max ( arr )
|||

DECODE_MEDIAN_STRING_ORIGINAL_STRING

def f_gold ( s ) :
    l = len ( s )
    s1 = ""
    if ( l % 2 == 0 ) :
        isEven = True
    else :
        isEven = False
    for i in range ( 0 , l , 2 ) :
        if ( isEven ) :
            s1 = s [ i ] + s1
            s1 += s [ i + 1 ]
        else :
            if ( l - i > 1 ) :
                s1 += s [ i ]
                s1 = s [ i + 1 ] + s1
            else :
                s1 += s [ i ]
    return s1
|||

DIAGONALLY_DOMINANT_MATRIX

def f_gold ( m , n ) :
    for i in range ( 0 , n ) :
        sum = 0
        for j in range ( 0 , n ) :
            sum = sum + abs ( m [ i ] [ j ] )
        sum = sum - abs ( m [ i ] [ i ] )
        if ( abs ( m [ i ] [ i ] ) < sum ) :
            return False
    return True
|||

DICE_THROW_PROBLEM

def f_gold ( m , n , x ) :
    table = [ [ 0 ] * ( x + 1 ) for i in range ( n + 1 ) ]
    for j in range ( 1 , min ( m + 1 , x + 1 ) ) :
        table [ 1 ] [ j ] = 1
    for i in range ( 2 , n + 1 ) :
        for j in range ( 1 , x + 1 ) :
            for k in range ( 1 , min ( m + 1 , j ) ) :
                table [ i ] [ j ] += table [ i - 1 ] [ j - k ]
    return table [ - 1 ] [ - 1 ]
|||

DICE_THROW_PROBLEM_1

def f_gold ( f , d , s ) :
    mem = [ [ 0 for i in range ( s + 1 ) ] for j in range ( d + 1 ) ]
    mem [ 0 ] [ 0 ] = 1
    for i in range ( 1 , d + 1 ) :
        for j in range ( 1 , s + 1 ) :
            mem [ i ] [ j ] = mem [ i ] [ j - 1 ] + mem [ i - 1 ] [ j - 1 ]
            if j - f - 1 >= 0 :
                mem [ i ] [ j ] -= mem [ i - 1 ] [ j - f - 1 ]
    return mem [ d ] [ s ]
|||

DIFFERENCE_BETWEEN_HIGHEST_AND_LEAST_FREQUENCIES_IN_AN_ARRAY

def f_gold ( arr , n ) :
    arr.sort ( )
    count = 0 ; max_count = 0 ; min_count = n
    for i in range ( 0 , ( n - 1 ) ) :
        if arr [ i ] == arr [ i + 1 ] :
            count += 1
            continue
        else :
            max_count = max ( max_count , count )
            min_count = min ( min_count , count )
            count = 0
    return max_count - min_count
|||

DOUBLE_FACTORIAL_1

def f_gold ( n ) :
    res = 1 
    for i in range ( n , - 1 , - 2 ) :
        if ( i == 0 or i == 1 ) :
            return res 
        else :
            res *= i 
|||

DYCK_PATH

def f_gold ( n ) :
    res = 1
    for i in range ( 0 , n ) :
        res *= ( 2 * n - i )
        res /= ( i + 1 )
    return res / ( n + 1 )
|||

DYNAMIC_PROGRAMMING_HIGH_EFFORT_VS_LOW_EFFORT_TASKS_PROBLEM

def f_gold ( high , low , n ) :
    if ( n <= 0 ) :
        return 0
    return max ( high [ n - 1 ] + f_gold ( high , low , ( n - 2 ) ) , low [ n - 1 ] + f_gold ( high , low , ( n - 1 ) ) ) 
|||

DYNAMIC_PROGRAMMING_SET_14_MAXIMUM_SUM_INCREASING_SUBSEQUENCE

def f_gold ( arr , n ) :
    max = 0
    msis = [ 0 for x in range ( n ) ]
    for i in range ( n ) :
        msis [ i ] = arr [ i ]
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if ( arr [ i ] > arr [ j ] and msis [ i ] < msis [ j ] + arr [ i ] ) :
                msis [ i ] = msis [ j ] + arr [ i ]
    for i in range ( n ) :
        if max < msis [ i ] :
            max = msis [ i ]
    return max
|||

DYNAMIC_PROGRAMMING_SET_36_CUT_A_ROPE_TO_MAXIMIZE_PRODUCT_1

def f_gold ( n ) :
    if ( n == 2 or n == 3 ) :
        return ( n - 1 )
    res = 1
    while ( n > 4 ) :
        n -= 3 
        res *= 3 
    return ( n * res )
|||

DYNAMIC_PROGRAMMING_SET_37_BOOLEAN_PARENTHESIZATION_PROBLEM

def f_gold ( symb , oper , n ) :
    F = [ [ 0 for i in range ( n + 1 ) ] for i in range ( n + 1 ) ]
    T = [ [ 0 for i in range ( n + 1 ) ] for i in range ( n + 1 ) ]
    for i in range ( n ) :
        if symb [ i ] == 'F' :
            F [ i ] [ i ] = 1
        else :
            F [ i ] [ i ] = 0
        if symb [ i ] == 'T' :
            T [ i ] [ i ] = 1
        else :
            T [ i ] [ i ] = 0
    for gap in range ( 1 , n ) :
        i = 0
        for j in range ( gap , n ) :
            T [ i ] [ j ] = F [ i ] [ j ] = 0
            for g in range ( gap ) :
                k = i + g
                tik = T [ i ] [ k ] + F [ i ] [ k ] 
                tkj = T [ k + 1 ] [ j ] + F [ k + 1 ] [ j ] 
                if oper [ k ] == '&' :
                    T [ i ] [ j ] += T [ i ] [ k ] * T [ k + 1 ] [ j ]
                    F [ i ] [ j ] += ( tik * tkj - T [ i ] [ k ] * T [ k + 1 ] [ j ] )
                if oper [ k ] == '|' :
                    F [ i ] [ j ] += F [ i ] [ k ] * F [ k + 1 ] [ j ]
                    T [ i ] [ j ] += ( tik * tkj - F [ i ] [ k ] * F [ k + 1 ] [ j ] )
                if oper [ k ] == '^' :
                    T [ i ] [ j ] += ( F [ i ] [ k ] * T [ k + 1 ] [ j ] + T [ i ] [ k ] * F [ k + 1 ] [ j ] )
                    F [ i ] [ j ] += ( T [ i ] [ k ] * T [ k + 1 ] [ j ] + F [ i ] [ k ] * F [ k + 1 ] [ j ] )
            i += 1
    return T [ 0 ] [ n - 1 ]
|||

ELEMENTS_TO_BE_ADDED_SO_THAT_ALL_ELEMENTS_OF_A_RANGE_ARE_PRESENT_IN_ARRAY_1

def f_gold ( arr , n ) :
    s = dict ( )
    count , maxm , minm = 0 , - 10 ** 9 , 10 ** 9
    for i in range ( n ) :
        s [ arr [ i ] ] = 1
        if ( arr [ i ] < minm ) :
            minm = arr [ i ]
        if ( arr [ i ] > maxm ) :
            maxm = arr [ i ]
    for i in range ( minm , maxm + 1 ) :
        if i not in s.keys ( ) :
            count += 1
    return count
|||

EVEN_FIBONACCI_NUMBERS_SUM

def f_gold ( limit ) :
    if ( limit < 2 ) :
        return 0
    ef1 = 0
    ef2 = 2
    sm = ef1 + ef2
    while ( ef2 <= limit ) :
        ef3 = 4 * ef2 + ef1
        if ( ef3 > limit ) :
            break
        ef1 = ef2
        ef2 = ef3
        sm = sm + ef2
    return sm
|||

FIBONACCI_MODULO_P

def f_gold ( p ) :
    first = 1
    second = 1
    number = 2
    next = 1
    while ( next ) :
        next = ( first + second ) % p
        first = second
        second = next
        number = number + 1
    return number
|||

FIND_A_FIXED_POINT_IN_A_GIVEN_ARRAY

def f_gold ( arr , n ) :
    for i in range ( n ) :
        if arr [ i ] is i :
            return i
    return - 1
|||

FIND_A_ROTATION_WITH_MAXIMUM_HAMMING_DISTANCE

def f_gold ( arr , n ) :
    brr = [ 0 ] * ( 2 * n + 1 )
    for i in range ( n ) :
        brr [ i ] = arr [ i ]
    for i in range ( n ) :
        brr [ n + i ] = arr [ i ]
    maxHam = 0
    for i in range ( 1 , n ) :
        currHam = 0
        k = 0
        for j in range ( i , i + n ) :
            if brr [ j ] != arr [ k ] :
                currHam += 1
                k = k + 1
        if currHam == n :
            return n
        maxHam = max ( maxHam , currHam )
    return maxHam
|||

FIND_A_TRIPLET_THAT_SUM_TO_A_GIVEN_VALUE

def f_gold ( A , arr_size , sum ) :
    for i in range ( 0 , arr_size - 2 ) :
        for j in range ( i + 1 , arr_size - 1 ) :
            for k in range ( j + 1 , arr_size ) :
                if A [ i ] + A [ j ] + A [ k ] == sum :
                    print ( "Triplet is" , A [ i ] , ", " , A [ j ] , ", " , A [ k ] )
                    return True
    return False
|||

FIND_EXPRESSION_DUPLICATE_PARENTHESIS_NOT

def f_gold ( string ) :
    Stack = [ ]
    for ch in string :
        if ch == ')' :
            top = Stack.pop ( )
            elementsInside = 0
            while top != '(' :
                elementsInside += 1
                top = Stack.pop ( )
            if elementsInside < 1 :
                return True
        else :
            Stack.append ( ch )
    return False
|||

FIND_INDEX_GIVEN_FIBONACCI_NUMBER_CONSTANT_TIME_1

def f_gold ( n ) :
    fibo = 2.078087 * math.log ( n ) + 1.672276
    return round ( fibo )
|||

FIND_INDEX_OF_AN_EXTRA_ELEMENT_PRESENT_IN_ONE_SORTED_ARRAY

def f_gold ( arr1 , arr2 , n ) :
    for i in range ( 0 , n ) :
        if ( arr1 [ i ] != arr2 [ i ] ) :
            return i
    return n
|||

FIND_INDEX_OF_AN_EXTRA_ELEMENT_PRESENT_IN_ONE_SORTED_ARRAY_1

def f_gold ( arr1 , arr2 , n ) :
    index = n
    left = 0
    right = n - 1
    while ( left <= right ) :
        mid = ( int ) ( ( left + right ) / 2 )
        if ( arr2 [ mid ] == arr1 [ mid ] ) :
            left = mid + 1
        else :
            index = mid
            right = mid - 1
    return index
|||

FIND_LARGEST_PRIME_FACTOR_NUMBER

def f_gold ( n ) :
    maxPrime = - 1
    while n % 2 == 0 :
        maxPrime = 2
        n >>= 1
    for i in range ( 3 , int ( math.sqrt ( n ) ) + 1 , 2 ) :
        while n % i == 0 :
            maxPrime = i
            n = n / i
    if n > 2 :
        maxPrime = n
    return int ( maxPrime )
|||

FIND_LAST_DIGIT_FACTORIAL_DIVIDES_FACTORIAL_B

def f_gold ( A , B ) :
    variable = 1
    if ( A == B ) :
        return 1
    elif ( ( B - A ) >= 5 ) :
        return 0
    else :
        for i in range ( A + 1 , B + 1 ) :
            variable = ( variable * ( i % 10 ) ) % 10
        return variable % 10
|||

FIND_MAXIMUM_PRODUCT_OF_A_TRIPLET_IN_ARRAY

def f_gold ( arr , n ) :
    if n < 3 :
        return - 1
    max_product = - ( sys.maxsize - 1 )
    for i in range ( 0 , n - 2 ) :
        for j in range ( i + 1 , n - 1 ) :
            for k in range ( j + 1 , n ) :
                max_product = max ( max_product , arr [ i ] * arr [ j ] * arr [ k ] )
    return max_product
|||

FIND_MAXIMUM_SUM_POSSIBLE_EQUAL_SUM_THREE_STACKS

def f_gold ( stack1 , stack2 , stack3 , n1 , n2 , n3 ) :
    sum1 , sum2 , sum3 = 0 , 0 , 0
    for i in range ( n1 ) :
        sum1 += stack1 [ i ]
    for i in range ( n2 ) :
        sum2 += stack2 [ i ]
    for i in range ( n3 ) :
        sum3 += stack3 [ i ]
    top1 , top2 , top3 = 0 , 0 , 0
    ans = 0
    while ( 1 ) :
        if ( top1 == n1 or top2 == n2 or top3 == n3 ) :
            return 0
        if ( sum1 == sum2 and sum2 == sum3 ) :
            return sum1
        if ( sum1 >= sum2 and sum1 >= sum3 ) :
            sum1 -= stack1 [ top1 ]
            top1 = top1 + 1
        elif ( sum2 >= sum3 and sum2 >= sum3 ) :
            sum2 -= stack2 [ top2 ]
            top2 = top2 + 1
        elif ( sum3 >= sum2 and sum3 >= sum1 ) :
            sum3 -= stack3 [ top3 ]
            top3 = top3 + 1
|||

FIND_MINIMUM_DIFFERENCE_PAIR_1

def f_gold ( arr , n ) :
    arr = sorted ( arr )
    diff = 10 ** 20
    for i in range ( n - 1 ) :
        if arr [ i + 1 ] - arr [ i ] < diff :
            diff = arr [ i + 1 ] - arr [ i ]
    return diff
|||

FIND_NUMBER_TIMES_STRING_OCCURS_GIVEN_STRING_1

def f_gold ( a , b ) :
    m = len ( a )
    n = len ( b )
    lookup = [ [ 0 ] * ( n + 1 ) for i in range ( m + 1 ) ]
    for i in range ( n + 1 ) :
        lookup [ 0 ] [ i ] = 0
    for i in range ( m + 1 ) :
        lookup [ i ] [ 0 ] = 1
    for i in range ( 1 , m + 1 ) :
        for j in range ( 1 , n + 1 ) :
            if a [ i - 1 ] == b [ j - 1 ] :
                lookup [ i ] [ j ] = lookup [ i - 1 ] [ j - 1 ] + lookup [ i - 1 ] [ j ]
            else :
                lookup [ i ] [ j ] = lookup [ i - 1 ] [ j ]
    return lookup [ m ] [ n ]
|||

FIND_ONE_EXTRA_CHARACTER_STRING_1

def f_gold ( strA , strB ) :
    res = 0
    for i in range ( 0 , len ( strA ) ) :
        res = res ^ ( ord ) ( strA [ i ] )
    for i in range ( 0 , len ( strB ) ) :
        res = res ^ ( ord ) ( strB [ i ] )
    return ( ( chr ) ( res ) ) 
|||

FIND_PERIMETER_CYLINDER

def f_gold ( diameter , height ) :
    return 2 * ( diameter + height )
|||

FIND_REPETITIVE_ELEMENT_1_N_1

def f_gold ( arr , n ) :
    return sum ( arr ) - ( ( ( n - 1 ) * n ) // 2 )
|||

FIND_SUM_EVEN_INDEX_BINOMIAL_COEFFICIENTS_1

def f_gold ( n ) :
    return ( 1 << ( n - 1 ) )
|||

FIND_SUM_MODULO_K_FIRST_N_NATURAL_NUMBER

def f_gold ( N , K ) :
    ans = 0 
    for i in range ( 1 , N + 1 ) :
        ans += ( i % K ) 
    return ans 
|||

FIND_SUM_ODD_FACTORS_NUMBER

def f_gold ( n ) :
    res = 1
    while n % 2 == 0 :
        n = n // 2
    for i in range ( 3 , int ( math.sqrt ( n ) + 1 ) ) :
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0 :
            count += 1
            n = n // i
            curr_term *= i
            curr_sum += curr_term
        res *= curr_sum
    if n >= 2 :
        res *= ( 1 + n )
    return res
|||

FIND_SUM_UNIQUE_SUB_ARRAY_SUM_GIVEN_ARRAY

def f_gold ( arr , n ) :
    res = 0
    m = dict ( )
    for i in range ( n ) :
        Sum = 0
        for j in range ( i , n ) :
            Sum += arr [ j ]
            m [ Sum ] = m.get ( Sum , 0 ) + 1
    for x in m :
        if m [ x ] == 1 :
            res += x
    return res
|||

FIND_THE_ELEMENT_BEFORE_WHICH_ALL_THE_ELEMENTS_ARE_SMALLER_THAN_IT_AND_AFTER_WHICH_ALL_ARE_GREATER_THAN_IT

def f_gold ( arr , n ) :
    leftMax = [ None ] * n
    leftMax [ 0 ] = float ( '-inf' )
    for i in range ( 1 , n ) :
        leftMax [ i ] = max ( leftMax [ i - 1 ] , arr [ i - 1 ] )
    rightMin = float ( 'inf' )
    for i in range ( n - 1 , - 1 , - 1 ) :
        if leftMax [ i ] < arr [ i ] and rightMin > arr [ i ] :
            return i
        rightMin = min ( rightMin , arr [ i ] )
    return - 1
|||

FIND_THE_MAXIMUM_ELEMENT_IN_AN_ARRAY_WHICH_IS_FIRST_INCREASING_AND_THEN_DECREASING

def f_gold ( arr , low , high ) :
    max = arr [ low ]
    i = low
    for i in range ( high + 1 ) :
        if arr [ i ] > max :
            max = arr [ i ]
    return max
|||

FIND_THE_MISSING_NUMBER_1

def f_gold ( a , n ) :
    i , total = 0 , 1
    for i in range ( 2 , n + 2 ) :
        total += i
        total -= a [ i - 2 ]
    return total
|||

FIND_THE_MISSING_NUMBER_2

def f_gold ( a , n ) :
    x1 = a [ 0 ]
    x2 = 1
    for i in range ( 1 , n ) :
        x1 = x1 ^ a [ i ]
    for i in range ( 2 , n + 2 ) :
        x2 = x2 ^ i
    return x1 ^ x2
|||

FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES

def f_gold ( arr , arr_size ) :
    for i in range ( 0 , arr_size ) :
        count = 0
        for j in range ( 0 , arr_size ) :
            if arr [ i ] == arr [ j ] :
                count += 1
        if ( count % 2 != 0 ) :
            return arr [ i ]
    return - 1
|||

FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES_1

def f_gold ( arr , size ) :
    Hash = dict ( )
    for i in range ( size ) :
        Hash [ arr [ i ] ] = Hash.get ( arr [ i ] , 0 ) + 1 
    for i in Hash :
        if ( Hash [ i ] % 2 != 0 ) :
            return i
    return - 1
|||

FIND_WHETHER_A_GIVEN_NUMBER_IS_A_POWER_OF_4_OR_NOT_2

def f_gold ( n ) :
    return ( n != 0 and ( ( n & ( n - 1 ) ) == 0 ) and not ( n & 0xAAAAAAAA ) ) 
|||

FIRST_UPPERCASE_LETTER_IN_A_STRING_ITERATIVE_AND_RECURSIVE

def f_gold ( str ) :
    for i in range ( 0 , len ( str ) ) :
        if ( str [ i ].istitle ( ) ) :
            return str [ i ]
    return 0
|||

FLOOR_IN_A_SORTED_ARRAY_1

def f_gold ( arr , low , high , x ) :
    if ( low > high ) :
        return - 1
    if ( x >= arr [ high ] ) :
        return high
    mid = int ( ( low + high ) / 2 )
    if ( arr [ mid ] == x ) :
        return mid
    if ( mid > 0 and arr [ mid - 1 ] <= x and x < arr [ mid ] ) :
        return mid - 1
    if ( x < arr [ mid ] ) :
        return f_gold ( arr , low , mid - 1 , x )
    return f_gold ( arr , mid + 1 , high , x )
|||

FUNCTION_COPY_STRING_ITERATIVE_RECURSIVE_1

def f_gold ( s1 , s2 , index ) :
    s2 [ index ] = s1 [ index ] 
    if ( index == len ( s1 ) - 1 ) :
        return 
    f_gold ( s1 , s2 , index + 1 ) 
|||

GIVEN_LARGE_NUMBER_CHECK_SUBSEQUENCE_DIGITS_DIVISIBLE_8

def f_gold ( st ) :
    l = len ( st )
    arr = [ 0 ] * l
    for i in range ( 0 , l ) :
        for j in range ( i , l ) :
            for k in range ( j , l ) :
                if ( arr [ i ] % 8 == 0 ) :
                    return True
                elif ( ( arr [ i ] * 10 + arr [ j ] ) % 8 == 0 and i != j ) :
                    return True
                elif ( ( arr [ i ] * 100 + arr [ j ] * 10 + arr [ k ] ) % 8 == 0 and i != j and j != k and i != k ) :
                    return True
    return False
|||

GOOGLE_CASE_GIVEN_SENTENCE

def f_gold ( s ) :
    n = len ( s )
    s1 = ""
    s1 = s1 + s [ 0 ].lower ( )
    i = 1
    while i < n :
        if ( s [ i ] == ' ' and i <= n ) :
            s1 = s1 + " " + ( s [ i + 1 ] ).lower ( )
            i = i + 1
        else :
            s1 = s1 + ( s [ i ] ).upper ( )
        i = i + 1
    return s1
|||

HEIGHT_COMPLETE_BINARY_TREE_HEAP_N_NODES

def f_gold ( N ) :
    return math.ceil ( math.log2 ( N + 1 ) ) - 1
|||

HEXAGONAL_NUMBER

def f_gold ( n ) :
    return n * ( 2 * n - 1 )
|||

HOW_CAN_WE_SUM_THE_DIGITS_OF_A_GIVEN_NUMBER_IN_SINGLE_STATEMENT_2

def f_gold ( no ) :
    return 0 if no == 0 else int ( no % 10 ) + f_gold ( int ( no / 10 ) )
|||

HOW_TO_CHECK_IF_A_GIVEN_ARRAY_REPRESENTS_A_BINARY_HEAP

def f_gold ( arr , i , n ) :
    if i > int ( ( n - 2 ) / 2 ) :
        return True
    if ( arr [ i ] >= arr [ 2 * i + 1 ] and arr [ i ] >= arr [ 2 * i + 2 ] and f_gold ( arr , 2 * i + 1 , n ) and f_gold ( arr , 2 * i + 2 , n ) ) :
        return True
    return False
|||

HOW_TO_CHECK_IF_A_GIVEN_ARRAY_REPRESENTS_A_BINARY_HEAP_1

def f_gold ( arr , n ) :
    for i in range ( int ( ( n - 2 ) / 2 ) + 1 ) :
        if arr [ 2 * i + 1 ] > arr [ i ] :
            return False
        if ( 2 * i + 2 < n and arr [ 2 * i + 2 ] > arr [ i ] ) :
            return False
    return True
|||

HYPERCUBE_GRAPH

def f_gold ( n ) :
    if n == 1 :
        return 2
    return 2 * f_gold ( n - 1 )
|||

K_TH_DIGIT_RAISED_POWER_B

def f_gold ( a , b , k ) :
    p = a ** b
    count = 0
    while ( p > 0 and count < k ) :
        rem = p % 10
        count = count + 1
        if ( count == k ) :
            return rem
        p = p / 10 
|||

K_TH_ELEMENT_TWO_SORTED_ARRAYS

def f_gold ( arr1 , arr2 , m , n , k ) :
    sorted1 = [ 0 ] * ( m + n )
    i = 0
    j = 0
    d = 0
    while ( i < m and j < n ) :
        if ( arr1 [ i ] < arr2 [ j ] ) :
            sorted1 [ d ] = arr1 [ i ]
            i += 1
        else :
            sorted1 [ d ] = arr2 [ j ]
            j += 1
        d += 1
    while ( i < m ) :
        sorted1 [ d ] = arr1 [ i ]
        d += 1
        i += 1
    while ( j < n ) :
        sorted1 [ d ] = arr2 [ j ]
        d += 1
        j += 1
    return sorted1 [ k - 1 ]
|||

K_TH_LARGEST_SUM_CONTIGUOUS_SUBARRAY

def f_gold ( arr , n , k ) :
    sum = [ ]
    sum.append ( 0 )
    sum.append ( arr [ 0 ] )
    for i in range ( 2 , n + 1 ) :
        sum.append ( sum [ i - 1 ] + arr [ i - 1 ] )
    Q = [ ]
    heapq.heapify ( Q )
    for i in range ( 1 , n + 1 ) :
        for j in range ( i , n + 1 ) :
            x = sum [ j ] - sum [ i - 1 ]
            if len ( Q ) < k :
                heapq.heappush ( Q , x )
            else :
                if Q [ 0 ] < x :
                    heapq.heappop ( Q )
                    heapq.heappush ( Q , x )
    return Q [ 0 ]
|||

K_TH_MISSING_ELEMENT_INCREASING_SEQUENCE_NOT_PRESENT_GIVEN_SEQUENCE

def f_gold ( a , b , k , n1 , n2 ) :
    s = set ( )
    for i in range ( n2 ) :
        s.add ( b [ i ] )
    missing = 0
    for i in range ( n1 ) :
        if a [ i ] not in s :
            missing += 1
        if missing == k :
            return a [ i ]
    return - 1
|||

LCS_FORMED_CONSECUTIVE_SEGMENTS_LEAST_LENGTH_K

def f_gold ( k , s1 , s2 ) :
    n = len ( s1 )
    m = len ( s2 )
    lcs = [ [ 0 for x in range ( m + 1 ) ] for y in range ( n + 1 ) ]
    cnt = [ [ 0 for x in range ( m + 1 ) ] for y in range ( n + 1 ) ]
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , m + 1 ) :
            lcs [ i ] [ j ] = max ( lcs [ i - 1 ] [ j ] , lcs [ i ] [ j - 1 ] )
            if ( s1 [ i - 1 ] == s2 [ j - 1 ] ) :
                cnt [ i ] [ j ] = cnt [ i - 1 ] [ j - 1 ] + 1 
            if ( cnt [ i ] [ j ] >= k ) :
                for a in range ( k , cnt [ i ] [ j ] + 1 ) :
                    lcs [ i ] [ j ] = max ( lcs [ i ] [ j ] , lcs [ i - a ] [ j - a ] + a )
    return lcs [ n ] [ m ]
|||

LONGEST_INCREASING_ODD_EVEN_SUBSEQUENCE

def f_gold ( arr , n ) :
    lioes = list ( )
    maxLen = 0
    for i in range ( n ) :
        lioes.append ( 1 )
    i = 1
    for i in range ( n ) :
        for j in range ( i ) :
            if ( arr [ i ] > arr [ j ] and ( arr [ i ] + arr [ j ] ) % 2 != 0 and lioes [ i ] < lioes [ j ] + 1 ) :
                lioes [ i ] = lioes [ j ] + 1
    for i in range ( n ) :
        if maxLen < lioes [ i ] :
            maxLen = lioes [ i ]
    return maxLen
|||

LONGEST_PALINDROME_SUBSEQUENCE_SPACE

def f_gold ( s ) :
    n = len ( s )
    a = [ 0 ] * n
    for i in range ( n - 1 , - 1 , - 1 ) :
        back_up = 0
        for j in range ( i , n ) :
            if j == i :
                a [ j ] = 1
            elif s [ i ] == s [ j ] :
                temp = a [ j ]
                a [ j ] = back_up + 2
                back_up = temp
            else :
                back_up = a [ j ]
                a [ j ] = max ( a [ j - 1 ] , a [ j ] )
    return a [ n - 1 ]
|||

LONGEST_PREFIX_ALSO_SUFFIX_1

def f_gold ( s ) :
    n = len ( s )
    lps = [ 0 ] * n
    l = 0
    i = 1
    while ( i < n ) :
        if ( s [ i ] == s [ l ] ) :
            l = l + 1
            lps [ i ] = l
            i = i + 1
        else :
            if ( l != 0 ) :
                l = lps [ l - 1 ]
            else :
                lps [ i ] = 0
                i = i + 1
    res = lps [ n - 1 ]
    if ( res > n / 2 ) :
        return n // 2
    else :
        return res
|||

MAKING_ELEMENTS_OF_TWO_ARRAYS_SAME_WITH_MINIMUM_INCREMENTDECREMENT

def f_gold ( a , b , n ) :
    a.sort ( reverse = False )
    b.sort ( reverse = False )
    result = 0
    for i in range ( 0 , n , 1 ) :
        if ( a [ i ] > b [ i ] ) :
            result = result + abs ( a [ i ] - b [ i ] )
        elif ( a [ i ] < b [ i ] ) :
            result = result + abs ( a [ i ] - b [ i ] )
    return result
|||

MARKOV_MATRIX

def f_gold ( m ) :
    for i in range ( 0 , len ( m ) ) :
        sm = 0
        for j in range ( 0 , len ( m [ i ] ) ) :
            sm = sm + m [ i ] [ j ]
        if ( sm != 1 ) :
            return False
    return True
|||

MAXIMIZE_SUM_CONSECUTIVE_DIFFERENCES_CIRCULAR_ARRAY

def f_gold ( arr , n ) :
    sum = 0
    arr.sort ( )
    for i in range ( 0 , int ( n / 2 ) ) :
        sum -= ( 2 * arr [ i ] )
        sum += ( 2 * arr [ n - i - 1 ] )
    return sum
|||

MAXIMUM_AREA_RECTANGLE_PICKING_FOUR_SIDES_ARRAY_1

def f_gold ( arr , n ) :
    s = [ ]
    first = 0
    second = 0
    for i in range ( n ) :
        if arr [ i ] not in s :
            s.append ( arr [ i ] )
            continue
        if ( arr [ i ] > first ) :
            second = first
            first = arr [ i ]
        elif ( arr [ i ] > second ) :
            second = arr [ i ]
    return ( first * second )
|||

MAXIMUM_AVERAGE_SUM_PARTITION_ARRAY

def f_gold ( A , K ) :
    n = len ( A ) 
    pre_sum = [ 0 ] * ( n + 1 ) 
    pre_sum [ 0 ] = 0 
    for i in range ( n ) :
        pre_sum [ i + 1 ] = pre_sum [ i ] + A [ i ] 
    dp = [ 0 ] * n 
    sum = 0 
    for i in range ( n ) :
        dp [ i ] = ( pre_sum [ n ] - pre_sum [ i ] ) / ( n - i ) 
    for k in range ( K - 1 ) :
        for i in range ( n ) :
            for j in range ( i + 1 , n ) :
                dp [ i ] = max ( dp [ i ] , ( pre_sum [ j ] - pre_sum [ i ] ) / ( j - i ) + dp [ j ] ) 
    return int ( dp [ 0 ] ) 
|||

MAXIMUM_BINOMIAL_COEFFICIENT_TERM_VALUE

def f_gold ( n ) :
    C = [ [ 0 for x in range ( n + 1 ) ] for y in range ( n + 1 ) ] 
    for i in range ( n + 1 ) :
        for j in range ( min ( i , n ) + 1 ) :
            if ( j == 0 or j == i ) :
                C [ i ] [ j ] = 1 
            else :
                C [ i ] [ j ] = ( C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ] ) 
    maxvalue = 0 
    for i in range ( n + 1 ) :
        maxvalue = max ( maxvalue , C [ n ] [ i ] ) 
    return maxvalue 
|||

MAXIMUM_CONSECUTIVE_REPEATING_CHARACTER_STRING_1

def f_gold ( str ) :
    n = len ( str )
    count = 0
    res = str [ 0 ]
    cur_count = 1
    for i in range ( n ) :
        if ( i < n - 1 and str [ i ] == str [ i + 1 ] ) :
            cur_count += 1
        else :
            if cur_count > count :
                count = cur_count
                res = str [ i ]
            cur_count = 1
    return res
|||

MAXIMUM_DIFFERENCE_SUM_ELEMENTS_TWO_ROWS_MATRIX

def f_gold ( mat , m , n ) :
    rowSum = [ 0 ] * m
    for i in range ( 0 , m ) :
        sum = 0
        for j in range ( 0 , n ) :
            sum += mat [ i ] [ j ]
        rowSum [ i ] = sum
    max_diff = rowSum [ 1 ] - rowSum [ 0 ]
    min_element = rowSum [ 0 ]
    for i in range ( 1 , m ) :
        if ( rowSum [ i ] - min_element > max_diff ) :
            max_diff = rowSum [ i ] - min_element
        if ( rowSum [ i ] < min_element ) :
            min_element = rowSum [ i ]
    return max_diff
|||

MAXIMUM_GAMES_PLAYED_WINNER

def f_gold ( N ) :
    dp = [ 0 for i in range ( N ) ]
    dp [ 0 ] = 1
    dp [ 1 ] = 2
    i = 1
    while dp [ i ] <= N :
        i = i + 1
        dp [ i ] = dp [ i - 1 ] + dp [ i - 2 ]
    return ( i - 1 )
|||

MAXIMUM_HEIGHT_OF_TRIANGULAR_ARRANGEMENT_OF_ARRAY_VALUES

def f_gold ( a , n ) :
    result = 1
    for i in range ( 1 , n ) :
        y = ( i * ( i + 1 ) ) / 2
        if ( y < n ) :
            result = i
        else :
            break
    return result
|||

MAXIMUM_LENGTH_PREFIX_ONE_STRING_OCCURS_SUBSEQUENCE_ANOTHER

def f_gold ( s , t ) :
    count = 0
    for i in range ( 0 , len ( t ) ) :
        if ( count == len ( s ) ) :
            break
        if ( t [ i ] == s [ count ] ) :
            count = count + 1
    return count
|||

MAXIMUM_NUMBER_CHOCOLATES_DISTRIBUTED_EQUALLY_AMONG_K_STUDENTS

def f_gold ( arr , n , k ) :
    um , curr_rem , maxSum = { } , 0 , 0
    sm = [ 0 ] * n
    sm [ 0 ] = arr [ 0 ]
    for i in range ( 1 , n ) :
        sm [ i ] = sm [ i - 1 ] + arr [ i ]
    for i in range ( n ) :
        curr_rem = sm [ i ] % k
        if ( not curr_rem and maxSum < sm [ i ] ) :
            maxSum = sm [ i ]
        elif ( not curr_rem in um ) :
            um [ curr_rem ] = i
        elif ( maxSum < ( sm [ i ] - sm [ um [ curr_rem ] ] ) ) :
            maxSum = sm [ i ] - sm [ um [ curr_rem ] ]
    return maxSum // k
|||

MAXIMUM_NUMBER_OF_SQUARES_THAT_CAN_BE_FIT_IN_A_RIGHT_ANGLE_ISOSCELES_TRIANGLE

def f_gold ( b , m ) :
    return ( b / m - 1 ) * ( b / m ) / 2
|||

MAXIMUM_PRODUCT_INCREASING_SUBSEQUENCE

def f_gold ( arr , n ) :
    mpis = [ 0 ] * ( n )
    for i in range ( n ) :
        mpis [ i ] = arr [ i ]
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if ( arr [ i ] > arr [ j ] and mpis [ i ] < ( mpis [ j ] * arr [ i ] ) ) :
                mpis [ i ] = mpis [ j ] * arr [ i ]
    return max ( mpis )
|||

MAXIMUM_PRODUCT_OF_4_ADJACENT_ELEMENTS_IN_MATRIX

def f_gold ( arr , n ) :
    max = 0
    for i in range ( n ) :
        for j in range ( n ) :
            if ( ( j - 3 ) >= 0 ) :
                result = ( arr [ i ] [ j ] * arr [ i ] [ j - 1 ] * arr [ i ] [ j - 2 ] * arr [ i ] [ j - 3 ] )
                if ( max < result ) :
                    max = result
            if ( ( i - 3 ) >= 0 ) :
                result = ( arr [ i ] [ j ] * arr [ i - 1 ] [ j ] * arr [ i - 2 ] [ j ] * arr [ i - 3 ] [ j ] )
                if ( max < result ) :
                    max = result
            if ( ( i - 3 ) >= 0 and ( j - 3 ) >= 0 ) :
                result = ( arr [ i ] [ j ] * arr [ i - 1 ] [ j - 1 ] * arr [ i - 2 ] [ j - 2 ] * arr [ i - 3 ] [ j - 3 ] )
                if ( max < result ) :
                    max = result
    return max
|||

MAXIMUM_PRODUCT_SUBSET_ARRAY

def f_gold ( a , n ) :
    if n == 1 :
        return a [ 0 ]
    max_neg = - 999999999999
    count_neg = 0
    count_zero = 0
    prod = 1
    for i in range ( n ) :
        if a [ i ] == 0 :
            count_zero += 1
            continue
        if a [ i ] < 0 :
            count_neg += 1
            max_neg = max ( max_neg , a [ i ] )
        prod = prod * a [ i ]
    if count_zero == n :
        return 0
    if count_neg & 1 :
        if ( count_neg == 1 and count_zero > 0 and count_zero + count_neg == n ) :
            return 0
        prod = int ( prod / max_neg )
    return prod
|||

MAXIMUM_SUM_IARRI_AMONG_ROTATIONS_GIVEN_ARRAY

def f_gold ( arr , n ) :
    res = - sys.maxsize
    for i in range ( 0 , n ) :
        curr_sum = 0
        for j in range ( 0 , n ) :
            index = int ( ( i + j ) % n )
            curr_sum += j * arr [ index ]
        res = max ( res , curr_sum )
    return res
|||

MAXIMUM_SUM_PAIRS_SPECIFIC_DIFFERENCE_1

def f_gold ( arr , N , k ) :
    maxSum = 0 
    arr.sort ( ) 
    i = N - 1 
    while ( i >= 0 ) :
        if ( arr [ i ] - arr [ i - 1 ] < k ) :
            maxSum += arr [ i ] 
            maxSum += arr [ i - 1 ] 
            i -= 1 
        i -= 1 
    return maxSum 
|||

MAXIMUM_SUM_SUBSEQUENCE_LEAST_K_DISTANT_ELEMENTS

def f_gold ( arr , N , k ) :
    MS = [ 0 for i in range ( N ) ]
    MS [ N - 1 ] = arr [ N - 1 ]
    for i in range ( N - 2 , - 1 , - 1 ) :
        if ( i + k + 1 >= N ) :
            MS [ i ] = max ( arr [ i ] , MS [ i + 1 ] )
        else :
            MS [ i ] = max ( arr [ i ] + MS [ i + k + 1 ] , MS [ i + 1 ] )
    return MS [ 0 ]
|||

MAXIMUM_WEIGHT_PATH_ENDING_ELEMENT_LAST_ROW_MATRIX

def f_gold ( mat , N ) :
    dp = [ [ 0 for i in range ( N ) ] for j in range ( N ) ]
    dp [ 0 ] [ 0 ] = mat [ 0 ] [ 0 ]
    for i in range ( 1 , N ) :
        dp [ i ] [ 0 ] = mat [ i ] [ 0 ] + dp [ i - 1 ] [ 0 ]
    for i in range ( 1 , N ) :
        for j in range ( 1 , min ( i + 1 , N ) ) :
            dp [ i ] [ j ] = mat [ i ] [ j ] + \
                max ( dp [ i - 1 ] [ j - 1 ] , dp [ i - 1 ] [ j ] )
    result = 0
    for i in range ( N ) :
        if ( result < dp [ N - 1 ] [ i ] ) :
            result = dp [ N - 1 ] [ i ]
    return result
|||

MINIMIZE_SUM_PRODUCT_TWO_ARRAYS_PERMUTATIONS_ALLOWED

def f_gold ( A , B , n ) :
    sorted ( A )
    sorted ( B )
    result = 0
    for i in range ( n ) :
        result += ( A [ i ] * B [ n - i - 1 ] )
    return result
|||

MINIMUM_CHARACTERS_ADDED_FRONT_MAKE_STRING_PALINDROME

def f_gold ( s ) :
    l = len ( s )
    i = 0
    j = l - 1
    while i <= j :
        if ( s [ i ] != s [ j ] ) :
            return False
        i += 1
        j -= 1
    return True
|||

MINIMUM_COST_FOR_ACQUIRING_ALL_COINS_WITH_K_EXTRA_COINS_ALLOWED_WITH_EVERY_COIN

def f_gold ( coin , n , k ) :
    coin.sort ( )
    coins_needed = math.ceil ( 1.0 * n // ( k + 1 ) ) 
    ans = 0
    for i in range ( coins_needed - 1 + 1 ) :
        ans += coin [ i ]
    return ans
|||

MINIMUM_COST_MAKE_ARRAY_SIZE_1_REMOVING_LARGER_PAIRS

def f_gold ( a , n ) :
    return ( ( n - 1 ) * min ( a ) )
|||

MINIMUM_DIFFERENCE_BETWEEN_GROUPS_OF_SIZE_TWO

def f_gold ( a , n ) :
    a.sort ( ) 
    s = [ ] 
    i = 0 
    j = n - 1 
    while ( i < j ) :
        s.append ( ( a [ i ] + a [ j ] ) ) 
        i += 1 
        j -= 1 
    mini = min ( s ) 
    maxi = max ( s ) 
    return abs ( maxi - mini ) 
|||

MINIMUM_DIFFERENCE_MAX_MIN_K_SIZE_SUBSETS

def f_gold ( arr , N , K ) :
    arr.sort ( )
    res = 2147483647
    for i in range ( ( N - K ) + 1 ) :
        curSeqDiff = arr [ i + K - 1 ] - arr [ i ]
        res = min ( res , curSeqDiff )
    return res
|||

MINIMUM_FLIP_REQUIRED_MAKE_BINARY_MATRIX_SYMMETRIC_1

def f_gold ( mat , n ) :
    flip = 0
    for i in range ( n ) :
        for j in range ( i ) :
            if mat [ i ] [ j ] != mat [ j ] [ i ] :
                flip += 1
    return flip
|||

MINIMUM_INCREMENT_K_OPERATIONS_MAKE_ELEMENTS_EQUAL

def f_gold ( arr , n , k ) :
    max1 = max ( arr )
    res = 0
    for i in range ( 0 , n ) :
        if ( ( max1 - arr [ i ] ) % k != 0 ) :
            return - 1
        else :
            res += ( max1 - arr [ i ] ) / k
    return int ( res )
|||

MINIMUM_LENGTH_SUBARRAY_SUM_GREATER_GIVEN_VALUE_1

def f_gold ( arr , n , x ) :
    curr_sum = 0 
    min_len = n + 1 
    start = 0 
    end = 0 
    while ( end < n ) :
        while ( curr_sum <= x and end < n ) :
            if ( curr_sum <= 0 and x > 0 ) :
                start = end 
                curr_sum = 0 
            curr_sum += arr [ end ] 
            end += 1 
        while ( curr_sum > x and start < n ) :
            if ( end - start < min_len ) :
                min_len = end - start 
            curr_sum -= arr [ start ] 
            start += 1 
    return min_len 
|||

MINIMUM_NUMBER_PLATFORMS_REQUIRED_RAILWAYBUS_STATION

def f_gold ( arr , dep , n ) :
    arr.sort ( )
    dep.sort ( )
    plat_needed = 1
    result = 1
    i = 1
    j = 0
    while ( i < n and j < n ) :
        if ( arr [ i ] < dep [ j ] ) :
            plat_needed += 1
            i += 1
            if ( plat_needed > result ) :
                result = plat_needed
        else :
            plat_needed -= 1
            j += 1
    return result
|||

MINIMUM_PRODUCT_SUBSET_ARRAY

def f_gold ( a , n ) :
    if ( n == 1 ) :
        return a [ 0 ]
    max_neg = float ( '-inf' )
    min_pos = float ( 'inf' )
    count_neg = 0
    count_zero = 0
    prod = 1
    for i in range ( 0 , n ) :
        if ( a [ i ] == 0 ) :
            count_zero = count_zero + 1
            continue
        if ( a [ i ] < 0 ) :
            count_neg = count_neg + 1
            max_neg = max ( max_neg , a [ i ] )
        if ( a [ i ] > 0 ) :
            min_pos = min ( min_pos , a [ i ] )
        prod = prod * a [ i ]
    if ( count_zero == n or ( count_neg == 0 and count_zero > 0 ) ) :
        return 0 
    if ( count_neg == 0 ) :
        return min_pos
    if ( ( count_neg & 1 ) == 0 and count_neg != 0 ) :
        prod = int ( prod / max_neg )
    return prod 
|||

MINIMUM_ROTATIONS_UNLOCK_CIRCULAR_LOCK

def f_gold ( input , unlock_code ) :
    rotation = 0 
    while ( input > 0 or unlock_code > 0 ) :
        input_digit = input % 10 
        code_digit = unlock_code % 10 
        rotation += min ( abs ( input_digit - code_digit ) , 10 - abs ( input_digit - code_digit ) ) 
        input = int ( input / 10 ) 
        unlock_code = int ( unlock_code / 10 ) 
    return rotation 
|||

MINIMUM_SUM_SUBSEQUENCE_LEAST_ONE_EVERY_FOUR_CONSECUTIVE_ELEMENTS_PICKED_1

def f_gold ( ar , n ) :
    if ( n <= 4 ) :
        return min ( ar )
    sum = [ 0 for i in range ( n ) ]
    sum [ 0 ] = ar [ 0 ]
    sum [ 1 ] = ar [ 1 ]
    sum [ 2 ] = ar [ 2 ]
    sum [ 3 ] = ar [ 3 ]
    for i in range ( 4 , n ) :
        sum [ i ] = ar [ i ] + min ( sum [ i - 4 : i ] )
    return min ( sum [ n - 4 : n ] )
|||

MINIMUM_SUM_TWO_NUMBERS_FORMED_DIGITS_ARRAY_2

def f_gold ( a , n ) :
    a = sorted ( a )
    num1 , num2 = 0 , 0
    for i in range ( n ) :
        if i % 2 == 0 :
            num1 = num1 * 10 + a [ i ]
        else :
            num2 = num2 * 10 + a [ i ]
    return num2 + num1
|||

MINIMUM_SWAPS_REQUIRED_BRING_ELEMENTS_LESS_EQUAL_K_TOGETHER

def f_gold ( arr , n , k ) :
    count = 0
    for i in range ( 0 , n ) :
        if ( arr [ i ] <= k ) :
            count = count + 1
    bad = 0
    for i in range ( 0 , count ) :
        if ( arr [ i ] > k ) :
            bad = bad + 1
    ans = bad
    j = count
    for i in range ( 0 , n ) :
        if ( j == n ) :
            break
        if ( arr [ i ] > k ) :
            bad = bad - 1
        if ( arr [ j ] > k ) :
            bad = bad + 1
        ans = min ( ans , bad )
        j = j + 1
    return ans
|||

MINIMUM_TIME_TO_FINISH_TASKS_WITHOUT_SKIPPING_TWO_CONSECUTIVE

def f_gold ( arr , n ) :
    if ( n <= 0 ) : return 0
    incl = arr [ 0 ]
    excl = 0
    for i in range ( 1 , n ) :
        incl_new = arr [ i ] + min ( excl , incl )
        excl_new = incl
        incl = incl_new
        excl = excl_new
    return min ( incl , excl )
|||

MINIMUM_TIME_WRITE_CHARACTERS_USING_INSERT_DELETE_COPY_OPERATION

def f_gold ( N , insrt , remov , cpy ) :
    if N == 0 :
        return 0
    if N == 1 :
        return insrt
    dp = [ 0 ] * ( N + 1 )
    for i in range ( 1 , N + 1 ) :
        if i % 2 == 0 :
            dp [ i ] = min ( dp [ i - 1 ] + insrt , dp [ i // 2 ] + cpy )
        else :
            dp [ i ] = min ( dp [ i - 1 ] + insrt , dp [ ( i + 1 ) // 2 ] + cpy + remov )
    return dp [ N ]
|||

MOBILE_NUMERIC_KEYPAD_PROBLEM

def f_gold ( keypad , n ) :
    if ( not keypad or n <= 0 ) :
        return 0
    if ( n == 1 ) :
        return 10
    odd = [ 0 ] * 10
    even = [ 0 ] * 10
    i = 0
    j = 0
    useOdd = 0
    totalCount = 0
    for i in range ( 10 ) :
        odd [ i ] = 1
    for j in range ( 2 , n + 1 ) :
        useOdd = 1 - useOdd
        if ( useOdd == 1 ) :
            even [ 0 ] = odd [ 0 ] + odd [ 8 ]
            even [ 1 ] = odd [ 1 ] + odd [ 2 ] + odd [ 4 ]
            even [ 2 ] = odd [ 2 ] + odd [ 1 ] + odd [ 3 ] + odd [ 5 ]
            even [ 3 ] = odd [ 3 ] + odd [ 2 ] + odd [ 6 ]
            even [ 4 ] = odd [ 4 ] + odd [ 1 ] + odd [ 5 ] + odd [ 7 ]
            even [ 5 ] = odd [ 5 ] + odd [ 2 ] + odd [ 4 ] + odd [ 8 ] + odd [ 6 ]
            even [ 6 ] = odd [ 6 ] + odd [ 3 ] + odd [ 5 ] + odd [ 9 ]
            even [ 7 ] = odd [ 7 ] + odd [ 4 ] + odd [ 8 ]
            even [ 8 ] = odd [ 8 ] + odd [ 0 ] + odd [ 5 ] + odd [ 7 ] + odd [ 9 ]
            even [ 9 ] = odd [ 9 ] + odd [ 6 ] + odd [ 8 ]
        else :
            odd [ 0 ] = even [ 0 ] + even [ 8 ]
            odd [ 1 ] = even [ 1 ] + even [ 2 ] + even [ 4 ]
            odd [ 2 ] = even [ 2 ] + even [ 1 ] + even [ 3 ] + even [ 5 ]
            odd [ 3 ] = even [ 3 ] + even [ 2 ] + even [ 6 ]
            odd [ 4 ] = even [ 4 ] + even [ 1 ] + even [ 5 ] + even [ 7 ]
            odd [ 5 ] = even [ 5 ] + even [ 2 ] + even [ 4 ] + even [ 8 ] + even [ 6 ]
            odd [ 6 ] = even [ 6 ] + even [ 3 ] + even [ 5 ] + even [ 9 ]
            odd [ 7 ] = even [ 7 ] + even [ 4 ] + even [ 8 ]
            odd [ 8 ] = even [ 8 ] + even [ 0 ] + even [ 5 ] + even [ 7 ] + even [ 9 ]
            odd [ 9 ] = even [ 9 ] + even [ 6 ] + even [ 8 ]
    totalCount = 0
    if ( useOdd == 1 ) :
        for i in range ( 10 ) :
            totalCount += even [ i ]
    else :
        for i in range ( 10 ) :
            totalCount += odd [ i ]
    return totalCount
|||

MULTIPLY_AN_INTEGER_WITH_3_5

def f_gold ( x ) :
    return ( x << 1 ) + x + ( x >> 1 )
|||

NUMBER_IS_DIVISIBLE_BY_29_OR_NOT

def f_gold ( n ) :
    while ( int ( n / 100 ) ) :
        last_digit = int ( n % 10 )
        n = int ( n / 10 )
        n += last_digit * 3
    return ( n % 29 == 0 )
|||

NUMBER_N_DIGIT_STEPPING_NUMBERS

def f_gold ( n ) :
    dp = [ [ 0 for x in range ( 10 ) ] for y in range ( n + 1 ) ] 
    if ( n == 1 ) :
        return 10 
    for j in range ( 10 ) :
        dp [ 1 ] [ j ] = 1 
    for i in range ( 2 , n + 1 ) :
        for j in range ( 10 ) :
            if ( j == 0 ) :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j + 1 ] 
            elif ( j == 9 ) :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j - 1 ] 
            else :
                dp [ i ] [ j ] = ( dp [ i - 1 ] [ j - 1 ] + dp [ i - 1 ] [ j + 1 ] ) 
    sum = 0 
    for j in range ( 1 , 10 ) :
        sum = sum + dp [ n ] [ j ] 
    return sum 
|||

NUMBER_OF_SUBSTRINGS_WITH_ODD_DECIMAL_VALUE_IN_A_BINARY_STRING

def f_gold ( s ) :
    n = len ( s )
    auxArr = [ 0 for i in range ( n ) ]
    if ( s [ 0 ] == '1' ) :
        auxArr [ 0 ] = 1
    for i in range ( 0 , n ) :
        if ( s [ i ] == '1' ) :
            auxArr [ i ] = auxArr [ i - 1 ] + 1
        else :
            auxArr [ i ] = auxArr [ i - 1 ]
    count = 0
    for i in range ( n - 1 , - 1 , - 1 ) :
        if ( s [ i ] == '1' ) :
            count += auxArr [ i ]
    return count
|||

NUMBER_OF_TRIANGLES_IN_A_PLANE_IF_NO_MORE_THAN_TWO_POINTS_ARE_COLLINEAR

def f_gold ( n ) :
    return ( n * ( n - 1 ) * ( n - 2 ) // 6 )
|||

NUMBER_ORDERED_PAIRS_AI_AJ_0

def f_gold ( a , n ) :
    count = 0
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            if ( a [ i ] & a [ j ] ) == 0 :
                count += 2
    return count
|||

NUMBER_SUBSTRINGS_DIVISIBLE_4_STRING_INTEGERS

def f_gold ( s ) :
    n = len ( s )
    count = 0 
    for i in range ( 0 , n , 1 ) :
        if ( s [ i ] == '4' or s [ i ] == '8' or s [ i ] == '0' ) :
            count += 1
    for i in range ( 0 , n - 1 , 1 ) :
        h = ( ord ( s [ i ] ) - ord ( '0' ) ) * 10 + ( ord ( s [ i + 1 ] ) - ord ( '0' ) )
        if ( h % 4 == 0 ) :
            count = count + i + 1
    return count
|||

NUMBER_TRIANGLES_N_MOVES

def f_gold ( n ) :
    answer = [ None ] * ( n + 1 ) 
    answer [ 0 ] = 1 
    i = 1
    while i <= n :
        answer [ i ] = answer [ i - 1 ] * 3 + 2 
        i = i + 1
    return answer [ n ] 
|||

NUMBER_UNIQUE_RECTANGLES_FORMED_USING_N_UNIT_SQUARES

def f_gold ( n ) :
    ans = 0
    for length in range ( 1 , int ( math.sqrt ( n ) ) + 1 ) :
        height = length
        while ( height * length <= n ) :
            ans += 1
            height += 1
    return ans
|||

NUMBER_WAYS_NODE_MAKE_LOOP_SIZE_K_UNDIRECTED_COMPLETE_CONNECTED_GRAPH_N_NODES

def f_gold ( n , k ) :
    p = 1
    if ( k % 2 ) :
        p = - 1
    return ( pow ( n - 1 , k ) + p * ( n - 1 ) ) / n
|||

N_TH_NUMBER_WHOSE_SUM_OF_DIGITS_IS_TEN_2

def f_gold ( n ) :
    nthElement = 19 + ( n - 1 ) * 9
    outliersCount = int ( math.log10 ( nthElement ) ) - 1
    nthElement += 9 * outliersCount
    return nthElement
|||

N_TH_TERM_SERIES_2_12_36_80_150

def f_gold ( n ) :
    return ( n * n ) + ( n * n * n )
|||

PAINTING_FENCE_ALGORITHM

def f_gold ( n , k ) :
    total = k
    mod = 1000000007
    same , diff = 0 , k
    for i in range ( 2 , n + 1 ) :
        same = diff
        diff = total * ( k - 1 )
        diff = diff % mod
        total = ( same + diff ) % mod
    return total
|||

PAIR_WITH_GIVEN_PRODUCT_SET_1_FIND_IF_ANY_PAIR_EXISTS

def f_gold ( arr , n , x ) :
    for i in arr :
        for j in arr :
            if i * j == x :
                return True
    return False
|||

PERFECT_REVERSIBLE_STRING

def f_gold ( str ) :
    i = 0 ; j = len ( str ) - 1 
    while ( i < j ) :
        if ( str [ i ] != str [ j ] ) :
            return False 
        i += 1 
        j -= 1 
    return True 
|||

PIZZA_CUT_PROBLEM_CIRCLE_DIVISION_LINES

def f_gold ( n ) :
    return int ( 1 + n * ( n + 1 ) / 2 )
|||

PRIMALITY_TEST_SET_1_INTRODUCTION_AND_SCHOOL_METHOD_1

def f_gold ( n ) :
    if ( n <= 1 ) :
        return False
    if ( n <= 3 ) :
        return True
    if ( n % 2 == 0 or n % 3 == 0 ) :
        return False
    i = 5
    while ( i * i <= n ) :
        if ( n % i == 0 or n % ( i + 2 ) == 0 ) :
            return False
        i = i + 6
    return True
|||

PRIMALITY_TEST_SET_5USING_LUCAS_LEHMER_SERIES

def f_gold ( p ) :
    checkNumber = 2 ** p - 1
    nextval = 4 % checkNumber
    for i in range ( 1 , p - 1 ) :
        nextval = ( nextval * nextval - 2 ) % checkNumber
    if ( nextval == 0 ) : return True
    else : return False
|||

PRINT_WORDS_STRING_REVERSE_ORDER

def f_gold ( str ) :
    i = len ( str ) - 1
    start = end = i + 1
    result = ''
    while i >= 0 :
        if str [ i ] == ' ' :
            start = i + 1
            while start != end :
                result += str [ start ]
                start += 1
            result += ' '
            end = i
        i -= 1
    start = 0
    while start != end :
        result += str [ start ]
        start += 1
    return result
|||

PROGRAM_BINARY_DECIMAL_CONVERSION_1

def f_gold ( n ) :
    num = n 
    dec_value = 0 
    base1 = 1 
    len1 = len ( num ) 
    for i in range ( len1 - 1 , - 1 , - 1 ) :
        if ( num [ i ] == '1' ) :
            dec_value += base1 
        base1 = base1 * 2 
    return dec_value 
|||

PROGRAM_CALCULATE_AREA_OCTAGON

def f_gold ( side ) :
    return ( 2 * ( 1 + ( math.sqrt ( 2 ) ) ) * side * side )
|||

PROGRAM_CALCULATE_VOLUME_ELLIPSOID

def f_gold ( r1 , r2 , r3 ) :
    return 1.33 * math.pi * r1 * r2 * r3
|||

PROGRAM_CALCULATE_VOLUME_OCTAHEDRON

def f_gold ( side ) :
    return ( ( side * side * side ) * ( math.sqrt ( 2 ) / 3 ) )
|||

PROGRAM_CIRCUMFERENCE_PARALLELOGRAM

def f_gold ( a , b ) :
    return ( ( 2 * a ) + ( 2 * b ) )
|||

PROGRAM_COUNT_OCCURRENCE_GIVEN_CHARACTER_STRING

def f_gold ( s , c ) :
    res = 0
    for i in range ( len ( s ) ) :
        if ( s [ i ] == c ) :
            res = res + 1
    return res
|||

PROGRAM_FOR_FACTORIAL_OF_A_NUMBER

def f_gold ( n ) :
    return 1 if ( n == 1 or n == 0 ) else n * f_gold ( n - 1 ) 
|||

PROGRAM_FOR_FACTORIAL_OF_A_NUMBER_1

def f_gold ( n ) :
    return 1 if ( n == 1 or n == 0 ) else n * f_gold ( n - 1 ) 
|||

PROGRAM_FOR_FACTORIAL_OF_A_NUMBER_2

def f_gold ( n ) :
    return 1 if ( n == 1 or n == 0 ) else n * f_gold ( n - 1 )
|||

PROGRAM_PAGE_REPLACEMENT_ALGORITHMS_SET_2_FIFO

def f_gold ( pages , n , capacity ) :
    s = set ( )
    indexes = Queue ( )
    page_faults = 0
    for i in range ( n ) :
        if ( len ( s ) < capacity ) :
            if ( pages [ i ] not in s ) :
                s.add ( pages [ i ] )
                page_faults += 1
                indexes.put ( pages [ i ] )
        else :
            if ( pages [ i ] not in s ) :
                val = indexes.queue [ 0 ]
                indexes.get ( )
                s.remove ( val )
                s.add ( pages [ i ] )
                indexes.put ( pages [ i ] )
                page_faults += 1
    return page_faults
|||

PROGRAM_PRINT_SUM_GIVEN_NTH_TERM_1

def f_gold ( n ) :
    return math.pow ( n , 2 )
|||

PROGRAM_TO_FIND_THE_AREA_OF_PENTAGON

def f_gold ( a ) :
    area = ( sqrt ( 5 * ( 5 + 2 * ( sqrt ( 5 ) ) ) ) * a * a ) / 4
    return area
|||

PYTHAGOREAN_QUADRUPLE

def f_gold ( a , b , c , d ) :
    sum = a * a + b * b + c * c 
    if ( d * d == sum ) :
        return True
    else :
        return False
|||

PYTHON_PROGRAM_FIND_PERIMETER_CIRCUMFERENCE_SQUARE_RECTANGLE_1

def f_gold ( l , w ) :
    return ( 2 * ( l + w ) )
|||

QUICK_WAY_CHECK_CHARACTERS_STRING

def f_gold ( s ) :
    n = len ( s )
    for i in range ( 1 , n ) :
        if s [ i ] != s [ 0 ] :
            return False
    return True
|||

REARRANGE_ARRAY_MAXIMUM_MINIMUM_FORM_SET_2_O1_EXTRA_SPACE

def f_gold ( arr , n ) :
    max_idx = n - 1
    min_idx = 0
    max_elem = arr [ n - 1 ] + 1
    for i in range ( 0 , n ) :
        if i % 2 == 0 :
            arr [ i ] += ( arr [ max_idx ] % max_elem ) * max_elem
            max_idx -= 1
        else :
            arr [ i ] += ( arr [ min_idx ] % max_elem ) * max_elem
            min_idx += 1
    for i in range ( 0 , n ) :
        arr [ i ] = arr [ i ] / max_elem
|||

RECURSIVELY_BREAK_NUMBER_3_PARTS_GET_MAXIMUM_SUM

def f_gold ( n ) :
    if ( n == 0 or n == 1 ) :
        return n
    return max ( ( f_gold ( n // 2 ) + f_gold ( n // 3 ) + f_gold ( n // 4 ) ) , n )
|||

RECURSIVELY_BREAK_NUMBER_3_PARTS_GET_MAXIMUM_SUM_1

def f_gold ( n ) :
    dp = [ 0 ] * ( n + 1 )
    dp [ 0 ] = 0
    dp [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        dp [ i ] = max ( dp [ int ( i / 2 ) ] + dp [ int ( i / 3 ) ] + dp [ int ( i / 4 ) ] , i ) 
    return dp [ n ]
|||

RECURSIVE_C_PROGRAM_LINEARLY_SEARCH_ELEMENT_GIVEN_ARRAY

def f_gold ( arr , l , r , x ) :
    if r < l :
        return - 1
    if arr [ l ] == x :
        return l
    if arr [ r ] == x :
        return r
    return f_gold ( arr , l + 1 , r - 1 , x )
|||

REMOVE_ARRAY_END_ELEMENT_MAXIMIZE_SUM_PRODUCT

def f_gold ( dp , a , low , high , turn ) :
    if ( low == high ) :
        return a [ low ] * turn
    if ( dp [ low ] [ high ] != 0 ) :
        return dp [ low ] [ high ]
    dp [ low ] [ high ] = max ( a [ low ] * turn + f_gold ( dp , a , low + 1 , high , turn + 1 ) , a [ high ] * turn + f_gold ( dp , a , low , high - 1 , turn + 1 ) ) 
    return dp [ low ] [ high ]
|||

REMOVE_MINIMUM_ELEMENTS_EITHER_SIDE_2MIN_MAX

def f_gold ( arr , n ) :
    longest_start = - 1 
    longest_end = 0 
    for start in range ( n ) :
        min = sys.maxsize 
        max = - sys.maxsize 
        for end in range ( start , n ) :
            val = arr [ end ] 
            if ( val < min ) :
                min = val 
            if ( val > max ) :
                max = val 
            if ( 2 * min <= max ) :
                break 
            if ( end - start > longest_end - longest_start or longest_start == - 1 ) :
                longest_start = start 
                longest_end = end 
    if ( longest_start == - 1 ) :
        return n 
    return ( n - ( longest_end - longest_start + 1 ) ) 
|||

REMOVE_MINIMUM_NUMBER_ELEMENTS_NO_COMMON_ELEMENT_EXIST_ARRAY

def f_gold ( a , b , n , m ) :
    countA = dict ( )
    countB = dict ( )
    for i in range ( n ) :
        countA [ a [ i ] ] = countA.get ( a [ i ] , 0 ) + 1
    for i in range ( n ) :
        countB [ b [ i ] ] = countB.get ( b [ i ] , 0 ) + 1
    res = 0
    for x in countA :
        if x in countB.keys ( ) :
            res += min ( countA [ x ] , countB [ x ] )
    return res
|||

REPLACE_CHARACTER_C1_C2_C2_C1_STRING_S

def f_gold ( s , c1 , c2 ) :
    l = len ( s )
    for i in range ( l ) :
        if ( s [ i ] == c1 ) :
            s = s [ 0 : i ] + c2 + s [ i + 1 : ]
        elif ( s [ i ] == c2 ) :
            s = s [ 0 : i ] + c1 + s [ i + 1 : ]
    return s
|||

ROUND_THE_GIVEN_NUMBER_TO_NEAREST_MULTIPLE_OF_10

def f_gold ( n ) :
    a = ( n // 10 ) * 10
    b = a + 10
    return ( b if n - a > b - n else a )
|||

SEARCHING_ARRAY_ADJACENT_DIFFER_K

def f_gold ( arr , n , x , k ) :
    i = 0
    while ( i < n ) :
        if ( arr [ i ] == x ) :
            return i
        i = i + max ( 1 , int ( abs ( arr [ i ] - x ) / k ) )
    print ( "number is not present!" )
    return - 1
|||

SEARCH_AN_ELEMENT_IN_AN_ARRAY_WHERE_DIFFERENCE_BETWEEN_ADJACENT_ELEMENTS_IS_1

def f_gold ( arr , n , x ) :
    i = 0
    while ( i < n ) :
        if ( arr [ i ] == x ) :
            return i
        i = i + abs ( arr [ i ] - x )
    print ( "number is not present!" )
    return - 1
|||

SMALLEST_DIFFERENCE_PAIR_VALUES_TWO_UNSORTED_ARRAYS

def f_gold ( A , B , m , n ) :
    A.sort ( )
    B.sort ( )
    a = 0
    b = 0
    result = sys.maxsize
    while ( a < m and b < n ) :
        if ( abs ( A [ a ] - B [ b ] ) < result ) :
            result = abs ( A [ a ] - B [ b ] )
        if ( A [ a ] < B [ b ] ) :
            a += 1
        else :
            b += 1
    return result
|||

SMALLEST_OF_THREE_INTEGERS_WITHOUT_COMPARISON_OPERATORS

def f_gold ( x , y , z ) :
    c = 0
    while ( x and y and z ) :
        x = x - 1
        y = y - 1
        z = z - 1
        c = c + 1
    return c
|||

SMALLEST_POWER_OF_2_GREATER_THAN_OR_EQUAL_TO_N

def f_gold ( n ) :
    count = 0 
    if ( n and not ( n & ( n - 1 ) ) ) :
        return n
    while ( n != 0 ) :
        n >>= 1
        count += 1
    return 1 << count 
|||

SMALLEST_POWER_OF_2_GREATER_THAN_OR_EQUAL_TO_N_1

def f_gold ( n ) :
    p = 1
    if ( n and not ( n & ( n - 1 ) ) ) :
        return n
    while ( p < n ) :
        p <<= 1
    return p 
|||

SMALLEST_SUM_CONTIGUOUS_SUBARRAY

def f_gold ( arr , n ) :
    min_ending_here = sys.maxsize
    min_so_far = sys.maxsize
    for i in range ( n ) :
        if ( min_ending_here > 0 ) :
            min_ending_here = arr [ i ]
        else :
            min_ending_here += arr [ i ]
        min_so_far = min ( min_so_far , min_ending_here )
    return min_so_far
|||

SORT_ARRAY_APPLYING_GIVEN_EQUATION

def f_gold ( arr , n , A , B , C ) :
    for i in range ( n ) :
        arr [ i ] = ( A * arr [ i ] * arr [ i ] + B * arr [ i ] + C )
    index = - ( sys.maxsize - 1 )
    maximum = - ( sys.maxsize - 1 )
    for i in range ( n ) :
        if maximum < arr [ i ] :
            index = i
            maximum = arr [ i ]
    i = 0 ; j = n - 1 
    new_arr = [ 0 ] * n
    k = 0
    while i < index and j > index :
        if arr [ i ] < arr [ j ] :
            new_arr [ k ] = arr [ i ]
            k += 1
            i += 1
        else :
            new_arr [ k ] = arr [ j ]
            k += 1
            j -= 1
    while i < index :
        new_arr [ k ] = arr [ i ]
        k += 1
        i += 1
    while j > index :
        new_arr [ k ] = arr [ j ]
        k += 1
        j -= 1
        new_arr [ n - 1 ] = maximum
    for i in range ( n ) :
        arr [ i ] = new_arr [ i ]
|||

SORT_ARRAY_TWO_HALVES_SORTED

def f_gold ( A , n ) :
    A.sort ( )
|||

SORT_EVEN_NUMBERS_ASCENDING_ORDER_SORT_ODD_NUMBERS_DESCENDING_ORDER_1

def f_gold ( arr , n ) :
    for i in range ( 0 , n ) :
        if ( arr [ i ] & 1 ) :
            arr [ i ] *= - 1
    arr.sort ( )
    for i in range ( 0 , n ) :
        if ( arr [ i ] & 1 ) :
            arr [ i ] *= - 1
|||

SPLIT_N_MAXIMUM_COMPOSITE_NUMBERS

def f_gold ( n ) :
    if ( n < 4 ) :
        return - 1
    rem = n % 4
    if ( rem == 0 ) :
        return n // 4
    if ( rem == 1 ) :
        if ( n < 9 ) :
            return - 1
        return ( n - 9 ) // 4 + 1
    if ( rem == 2 ) :
        return ( n - 6 ) // 4 + 1
    if ( rem == 3 ) :
        if ( n < 15 ) :
            return - 1
        return ( n - 15 ) // 4 + 2
|||

SQUARED_TRIANGULAR_NUMBER_SUM_CUBES

def f_gold ( s ) :
    _sum = 0
    n = 1
    while ( _sum < s ) :
        _sum += n * n * n
        n += 1
    n -= 1
    if _sum == s :
        return n
    return - 1
|||

SQUARE_ROOT_OF_AN_INTEGER

def f_gold ( x ) :
    if ( x == 0 or x == 1 ) :
        return x
    i = 1 ; result = 1
    while ( result <= x ) :
        i += 1
        result = i * i
    return i - 1
|||

SQUARE_ROOT_OF_AN_INTEGER_1

def f_gold ( x ) :
    if ( x == 0 or x == 1 ) :
        return x
    start = 1
    end = x
    while ( start <= end ) :
        mid = ( start + end ) // 2
        if ( mid * mid == x ) :
            return mid
        if ( mid * mid < x ) :
            start = mid + 1
            ans = mid
        else :
            end = mid - 1
    return ans
|||

STEINS_ALGORITHM_FOR_FINDING_GCD

def f_gold ( a , b ) :
    if ( a == 0 ) :
        return b
    if ( b == 0 ) :
        return a
    k = 0
    while ( ( ( a | b ) & 1 ) == 0 ) :
        a = a >> 1
        b = b >> 1
        k = k + 1
    while ( ( a & 1 ) == 0 ) :
        a = a >> 1
    while ( b != 0 ) :
        while ( ( b & 1 ) == 0 ) :
            b = b >> 1
        if ( a > b ) :
            temp = a
            a = b
            b = temp
        b = ( b - a )
    return ( a << k )
|||

STOOGE_SORT

def f_gold ( arr , l , h ) :
    if l >= h :
        return
    if arr [ l ] > arr [ h ] :
        t = arr [ l ]
        arr [ l ] = arr [ h ]
        arr [ h ] = t
    if h - l + 1 > 2 :
        t = ( int ) ( ( h - l + 1 ) / 3 )
        f_gold ( arr , l , ( h - t ) )
        f_gold ( arr , l + t , ( h ) )
        f_gold ( arr , l , ( h - t ) )
|||

SUBARRAYS_DISTINCT_ELEMENTS

def f_gold ( arr , n ) :
    s = [ ]
    j = 0
    ans = 0
    for i in range ( n ) :
        while ( j < n and ( arr [ j ] not in s ) ) :
            s.append ( arr [ j ] )
            j += 1
        ans += ( ( j - i ) * ( j - i + 1 ) ) // 2
        s.remove ( arr [ i ] )
    return ans
|||

SUBSEQUENCES_SIZE_THREE_ARRAY_WHOSE_SUM_DIVISIBLE_M

def f_gold ( A , N , M ) :
    sum = 0
    ans = 0
    for i in range ( 0 , N ) :
        for j in range ( i + 1 , N ) :
            for k in range ( j + 1 , N ) :
                sum = A [ i ] + A [ j ] + A [ k ]
                if ( sum % M == 0 ) :
                    ans = ans + 1
    return ans
|||

SUM_BINOMIAL_COEFFICIENTS

def f_gold ( n ) :
    C = [ [ 0 ] * ( n + 2 ) for i in range ( 0 , n + 2 ) ]
    for i in range ( 0 , n + 1 ) :
        for j in range ( 0 , min ( i , n ) + 1 ) :
            if ( j == 0 or j == i ) :
                C [ i ] [ j ] = 1
            else :
                C [ i ] [ j ] = C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ]
    sum = 0
    for i in range ( 0 , n + 1 ) :
        sum += C [ n ] [ i ]
    return sum
|||

SUM_BINOMIAL_COEFFICIENTS_1

def f_gold ( n ) :
    return ( 1 << n ) 
|||

SUM_DIVISORS_1_N_1

def f_gold ( n ) :
    sum = 0
    for i in range ( 1 , n + 1 ) :
        sum += int ( n / i ) * i
    return int ( sum )
|||

SUM_FACTORS_NUMBER

def f_gold ( n ) :
    result = 0
    for i in range ( 2 , ( int ) ( math.sqrt ( n ) ) + 1 ) :
        if ( n % i == 0 ) :
            if ( i == ( n / i ) ) :
                result = result + i
            else :
                result = result + ( i + n // i )
    return ( result + n + 1 )
|||

SUM_FAI_AJ_PAIRS_ARRAY_N_INTEGERS

def f_gold ( a , n ) :
    cnt = dict ( )
    ans = 0
    pre_sum = 0
    for i in range ( n ) :
        ans += ( i * a [ i ] ) - pre_sum
        pre_sum += a [ i ]
        if ( a [ i ] - 1 ) in cnt :
            ans -= cnt [ a [ i ] - 1 ]
        if ( a [ i ] + 1 ) in cnt :
            ans += cnt [ a [ i ] + 1 ]
        if a [ i ] not in cnt :
            cnt [ a [ i ] ] = 0
        cnt [ a [ i ] ] += 1
    return ans
|||

SUM_MATRIX_ELEMENT_ABSOLUTE_DIFFERENCE_ROW_COLUMN_NUMBERS

def f_gold ( n ) :
    arr = [ [ 0 for x in range ( n ) ] for y in range ( n ) ]
    for i in range ( n ) :
        for j in range ( n ) :
            arr [ i ] [ j ] = abs ( i - j )
    sum = 0
    for i in range ( n ) :
        for j in range ( n ) :
            sum += arr [ i ] [ j ]
    return sum
|||

SUM_MATRIX_ELEMENT_ABSOLUTE_DIFFERENCE_ROW_COLUMN_NUMBERS_1

def f_gold ( n ) :
    sum = 0
    for i in range ( n ) :
        sum += i * ( n - i )
    return 2 * sum
|||

SUM_MATRIX_ELEMENT_ABSOLUTE_DIFFERENCE_ROW_COLUMN_NUMBERS_2

def f_gold ( n ) :
    n -= 1
    sum = 0
    sum += ( n * ( n + 1 ) ) / 2
    sum += ( n * ( n + 1 ) * ( 2 * n + 1 ) ) / 6
    return int ( sum )
|||

SUM_OF_ALL_ELEMENTS_UP_TO_NTH_ROW_IN_A_PASCALS_TRIANGLE_1

def f_gold ( n ) :
    sum = 0
    sum = 1 << n 
    return ( sum - 1 )
|||

SUM_PAIRWISE_PRODUCTS

def f_gold ( n ) :
    sm = 0
    for i in range ( 1 , n + 1 ) :
        for j in range ( i , n + 1 ) :
            sm = sm + i * j
    return sm
|||

SUM_PAIRWISE_PRODUCTS_2

def f_gold ( n ) :
    return n * ( n + 1 ) * ( n + 2 ) * ( 3 * n + 1 ) / 24
|||

SUM_SERIES_12_32_52_2N_12

def f_gold ( n ) :
    sum = 0
    for i in range ( 1 , n + 1 ) :
        sum = sum + ( 2 * i - 1 ) * ( 2 * i - 1 )
    return sum
|||

SUM_SERIES_555555_N_TERMS

def f_gold ( n ) :
    return ( int ) ( 0.6172 * ( pow ( 10 , n ) - 1 ) - 0.55 * n )
|||

SUM_SUBSETS_SET_FORMED_FIRST_N_NATURAL_NUMBERS

def f_gold ( n ) :
    return ( n * ( n + 1 ) / 2 ) * ( 1 << ( n - 1 ) )
|||

SUM_TWO_LARGE_NUMBERS

def f_gold ( str1 , str2 ) :
    if ( len ( str1 ) > len ( str2 ) ) :
        t = str1 
        str1 = str2 
        str2 = t 
    str = "" 
    n1 = len ( str1 ) 
    n2 = len ( str2 ) 
    str1 = str1 [ : : - 1 ] 
    str2 = str2 [ : : - 1 ] 
    carry = 0 
    for i in range ( n1 ) :
        sum = ( ( ord ( str1 [ i ] ) - 48 ) + ( ( ord ( str2 [ i ] ) - 48 ) + carry ) ) 
        str += chr ( sum % 10 + 48 ) 
        carry = int ( sum / 10 ) 
    for i in range ( n1 , n2 ) :
        sum = ( ( ord ( str2 [ i ] ) - 48 ) + carry ) 
        str += chr ( sum % 10 + 48 ) 
        carry = ( int ) ( sum / 10 ) 
    if ( carry ) :
        str += chr ( carry + 48 ) 
    str = str [ : : - 1 ] 
    return str 
|||

SWAP_BITS_IN_A_GIVEN_NUMBER

def f_gold ( x , p1 , p2 , n ) :
    set1 = ( x >> p1 ) & ( ( 1 << n ) - 1 )
    set2 = ( x >> p2 ) & ( ( 1 << n ) - 1 )
    xor = ( set1 ^ set2 )
    xor = ( xor << p1 ) | ( xor << p2 )
    result = x ^ xor
    return result
|||

SWAP_TWO_NIBBLES_BYTE

def f_gold ( x ) :
    return ( ( x & 0x0F ) << 4 | ( x & 0xF0 ) >> 4 )
|||

TEMPLE_OFFERINGS

def f_gold ( n , templeHeight ) :
    sum = 0
    for i in range ( n ) :
        left = 0
        right = 0
        for j in range ( i - 1 , - 1 , - 1 ) :
            if ( templeHeight [ j ] < templeHeight [ j + 1 ] ) :
                left += 1
            else :
                break
        for j in range ( i + 1 , n ) :
            if ( templeHeight [ j ] < templeHeight [ j - 1 ] ) :
                right += 1
            else :
                break
        sum += max ( right , left ) + 1
    return sum
|||

TRIANGULAR_NUMBERS

def f_gold ( num ) :
    if ( num < 0 ) :
        return False
    sum , n = 0 , 1
    while ( sum <= num ) :
        sum = sum + n
        if ( sum == num ) :
            return True
        n += 1
    return False
|||

TURN_OFF_THE_RIGHTMOST_SET_BIT

def f_gold ( n ) :
    return n & ( n - 1 )
|||

UNIQUE_CELLS_BINARY_MATRIX

def f_gold ( mat , n , m ) :
    rowsum = [ 0 ] * n 
    colsum = [ 0 ] * m 
    for i in range ( n ) :
        for j in range ( m ) :
            if ( mat [ i ] [ j ] != 0 ) :
                rowsum [ i ] += 1 
                colsum [ j ] += 1 
    uniquecount = 0 
    for i in range ( n ) :
        for j in range ( m ) :
            if ( mat [ i ] [ j ] != 0 and rowsum [ i ] == 1 and colsum [ j ] == 1 ) :
                uniquecount += 1 
    return uniquecount 
|||

WAYS_TRANSFORMING_ONE_STRING_REMOVING_0_CHARACTERS

def f_gold ( a , b ) :
    n = len ( a )
    m = len ( b )
    if m == 0 :
        return 1
    dp = [ [ 0 ] * ( n + 1 ) for _ in range ( m + 1 ) ]
    for i in range ( m ) :
        for j in range ( i , n ) :
            if i == 0 :
                if j == 0 :
                    if a [ j ] == b [ i ] :
                        dp [ i ] [ j ] = 1
                    else :
                        dp [ i ] [ j ] = 0
                elif a [ j ] == b [ i ] :
                    dp [ i ] [ j ] = dp [ i ] [ j - 1 ] + 1
                else :
                    dp [ i ] [ j ] = dp [ i ] [ j - 1 ]
            else :
                if a [ j ] == b [ i ] :
                    dp [ i ] [ j ] = ( dp [ i ] [ j - 1 ] + dp [ i - 1 ] [ j - 1 ] )
                else :
                    dp [ i ] [ j ] = dp [ i ] [ j - 1 ]
    return dp [ m - 1 ] [ n - 1 ]
|||

WRITE_A_C_PROGRAM_TO_CALCULATE_POWXN

def f_gold ( x , y ) :
    if ( y == 0 ) : return 1
    elif ( int ( y % 2 ) == 0 ) :
        return ( f_gold ( x , int ( y / 2 ) ) * f_gold ( x , int ( y / 2 ) ) )
    else :
        return ( x * f_gold ( x , int ( y / 2 ) ) * f_gold ( x , int ( y / 2 ) ) )
|||

WRITE_ONE_LINE_C_FUNCTION_TO_FIND_WHETHER_A_NO_IS_POWER_OF_TWO

def f_gold ( n ) :
    if ( n == 0 ) :
        return False
    while ( n != 1 ) :
        if ( n % 2 != 0 ) :
            return False
        n = n // 2
    return True
|||

