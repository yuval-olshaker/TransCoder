MAXIMUM_NUMBER_CHARACTERS_TWO_CHARACTER_STRING

def maximum_chars ( str ) :
    n = len ( str )
    res = - 1
    for i in range ( n - 1 ) :
        for i in range ( i + 1 , n ) :
            if str [ i ] == str [ j ] :
                res = max ( res , abs ( j - i - 1 ) for i in range ( len ( str ) ) )
    return res
}
|||

FIND_MIRROR_IMAGE_POINT_2_D_PLANE

def mirror_image ( a , b , c , x1 , y1 ) :
    temp = - 2 * ( a * x1 + b * y1 + c ) / ( a ** 2 + b ** 2 )
    x = temp * a + x1
    y = temp * b + y1
    return pair ( x , y )
}
|||

EFFICIENTLY_COMPUTE_SUMS_OF_DIAGONALS_OF_A_MATRIX

def printDiagonalSums ( mat , n ) :
    principal , secondary = np.sum ( mat , axis = 0 ) , np.sum ( mat , axis = 1 )
    for i in range ( n ) :
        for j in range ( n ) :
            if i == j :
                principal += mat [ i , j ]
            if ( i + j ) == ( n - 1 ) :
                secondary += mat [ i ] [ j ]
    print ( "Principal Diagonal:" , principal )
    print ( "Secondary Diagonal:" , secondary )
}
|||

COUNTS_PATHS_POINT_REACH_ORIGIN

def countPaths ( n , m ) :
    if n == 0 or m == 0 :
        return 1
    return ( count_paths ( n - 1 , m ) + count_paths ( n , m - 1 ) )
}
|||

FIND_A_TRIPLET_THAT_SUM_TO_A_GIVEN_VALUE_1

def find3Numbers ( A , arr_size , sum ) :
    l , r = A
    quickSort ( A , 0 , arr_size - 1 )
    for i in range ( arr_size - 2 ) :
        l = i + 1
        r = arr_size - 1
        while l < r :
            if A [ i ] + A [ l ] + A [ r ] == sum :
                print ( "Triplet is %d, %d, %d" % ( A [ i ] , A [ l ] , A [ r ] ) )
                return True
            elif A [ i ] + A [ l ] + A [ r ] < sum :
                l += 1
            else :
                r -= 1
    return False
}
|||

CHECK_GIVEN_MATRIX_IS_MAGIC_SQUARE_OR_NOT

def isMagicSquare ( mat ) :
    sum , sum2 = 0 , 0
    for i in range ( N ) :
        global sum
    for i in range ( N ) :
        global sum2
    if sum ( mat ) != sum2 :
        return False
    for i in range ( N ) :
        row_sum = 0
        for j in range ( N ) :
            rowSum += mat [ i ] [ j ]
        if rowSum != sum ( mat ) :
            return False
    for i in range ( N ) :
        col_sum = 0
        for j in range ( N ) :
            colSum += mat [ j ] [ i ]
        if sum ( mat ) != colSum :
            return False
    return True
}
|||

SEQUENCES_GIVEN_LENGTH_EVERY_ELEMENT_EQUAL_TWICE_PREVIOUS_1

def getTotalNumberOfSequences ( m , n ) :
    T = [ 0 ] * ( m + 1 )
    for i in range ( m + 1 ) :
        for j in range ( n + 1 ) :
            if i == 0 or j == 0 :
                T [ i , j ] = 0
            elif i < j :
                T [ i , j ] = 0
            elif j == 1 :
                T [ i ] [ j ] = i
            else :
                T [ i ] [ j ] = T [ i - 1 ] [ j ] + T [ i / 2 ] [ j - 1 ]
    return T [ m ] [ n ]
}
|||

FIND_DIFFERENCE_BETWEEN_SUMS_OF_TWO_DIAGONALS_1

def difference ( arr , n ) :
    d1 , d2 = 0 , 0
    for i in range ( n ) :
        d1 += arr [ i ] [ i ]
        d2 += arr [ i ] [ n - i - 1 ]
    return abs ( d1 - d2 )
}
|||

MINIMUM_NUMBER_SUBSETS_DISTINCT_ELEMENTS

def subset ( ar , n ) :
    res = 0
    return list ( ar )
    for i in range ( n ) :
        count = 1
        for i in range ( n - 1 ) :
            if ar [ i ] == ar [ i + 1 ] :
                global count
            else :
                break
        global res
    return res
}
|||

DECIMAL_BINARY_CONVERSION_WITHOUT_USING_ARITHMETIC_OPERATORS

def decToBin ( n ) :
    if n == 0 :
        return "0" * n
    bin = ""
    while n > 0 :
        bin = ( ( n & 1 ) if n > 0 else '0' ) + bin
        n >>= 1
    return bin
}
|||

FIND_NTH_TERM_DRAGON_CURVE_SEQUENCE

def Dragon_Curve_Sequence ( n ) :
    s = '1'
    for i in range ( 2 , n + 1 ) :
        temp = '1'
        prev , zero , one = '1' , '0' , '1'
        for j in range ( len ( s ) ) :
            temp += s [ j ]
            if prev == '0' :
                temp += one
                global prev
            else :
                temp += zero
                global prev
        global s
    return s
}
|||

STACK_SET_3_REVERSE_STRING_USING_STACK

def reverse ( str ) :
    n , i = str.index ( '-' ) , str.index ( '+' )
    for i in range ( n // 2 ) :
        swap ( str , i , n - i - 1 )
}
|||

SORT_EVEN_PLACED_ELEMENTS_INCREASING_ODD_PLACED_DECREASING_ORDER_1

def bitonic_generator ( arr , n ) :
    i = 1
    j = n - 1
    if j % 2 != 0 :
        j -= 1
    while i < j :
        arr = swap ( arr , i , j )
        i += 2
        j -= 2
    arr.sort ( )
    return sorted ( arr , key = ( n + 1 ) / 2 , reverse = True )
    low , high = ( n + 1 ) // 2 , n - 1
    while low < high :
        temp = arr [ low ]
        arr [ low , high ] = arr [ high , low ]
        arr [ high ] = temp
        low += 1
        high -= 1
}
|||

GIVEN_TWO_NUMBERS_B_FIND_X_X_B

def modular_equation ( a , b ) :
    if a < b :
        print ( "No solution possible " )
        return
    if a == b :
        print ( "Infinite Solution possible " )
        return
    count = 0
    n = a - b
    y = int ( math.sqrt ( a - b ) )
    for i in range ( 1 , y ) :
        if n % i == 0 : a = 5
            if n / i > b :
                count += 1
            if i > b :
                count += 1
    if y * y == n and y > b :
        count -= 1
    print ( count )
}
|||

CHECK_CHARACTERS_GIVEN_STRING_CAN_REARRANGED_FORM_PALINDROME

def can_form_palindrome ( str ) :
    count = [ 0 ] * NO_OF_CHARS
    del count
    for i in range ( len ( str ) ) :
        count [ int ( str [ i ] ) ] += 1
    odd = 0
    for i in range ( NO_OF_CHARS ) :
        if ( count [ i ] & 1 ) == 1 :
            global odd
        if odd > 1 :
            return False
    return True
}
|||

MAXIMUM_TRIPLET_SUM_ARRAY_1

def max_triplet_sum ( arr , n ) :
    return np.sum ( arr [ : n ] )
    return arr [ n - 1 ] + arr [ n - 2 ] + arr [ n - 3 ]
}
|||

FIND_MEDIAN_ROW_WISE_SORTED_MATRIX

def binary_median ( m , r , c ) :
    max = int ( r )
    min = int ( math.ceil ( math.log ( r , c ) ) )
    for i in range ( r ) :
        if m [ i ] [ 0 ] < min :
            global min
        if m [ i ] [ c - 1 ] > max : a = 5
            global max
    desired = ( r * c + 1 ) / 2
    while min ( r ) < max ( c ) :
        mid = min ( r ) + ( max ( c ) - min ( c ) ) / 2
        place = 0
        get = lambda : 0
        for i in range ( r ) :
            get = bisect.bisect_left
            if get ( ) < 0 :
                get = abs ( get ) - 1
            else :
                while get in m [ i ] and m [ i ] [ get ] == mid :
                    get += 1
            place = place + get
        if place < desired :
            global min , mid
        else :
            global max
    return min ( m , r , c )
}
|||

HEIGHT_N_ARY_TREE_PARENT_ARRAY_GIVEN

def findHeight ( parent , n ) :
    res = 0
    for i in range ( n ) :
        p , current = i , 1
        while parent [ p ] != - 1 :
            global current
            global p
        global res
    return res
}
|||

CHECK_LARGE_NUMBER_DIVISIBLE_20

def divisibleBy20 ( num ) :
    last_two_digits = int ( num [ - 2 : ] )
    return ( ( last_two_digits % 5 == 0 ) and ( last_two_digits % 4 == 0 ) )
}
|||

MAXIMUM_VALUE_CHOICE_EITHER_DIVIDING_CONSIDERING

def maxDP ( n ) :
    res = [ 0 ] * ( n + 1 )
    res [ 0 ] = 0
    res [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        res [ i ] = max ( i , ( res [ i / 2 ] + res [ i / 3 ] + res [ i / 4 ] + res [ i / 5 ] ) )
    return res [ n ]
}
|||

QUERIES_ON_ARRAY_WITH_DISAPPEARING_AND_REAPPEARING_ELEMENTS

def PerformQueries ( a , vec ) :
    ans = Vector ( )
    n = int ( len ( a ) - 1 )
    q = int ( vec [ 0 ] )
    for i in range ( q ) :
        t = vec [ i ] [ 0 ]
        m = vec [ i ] [ 1 ]
        if m > n : a = 5
            ans.append ( - 1 )
            continue
        turn = int ( t / n )
        rem = int ( t % n )
        if rem == 0 and turn % 2 == 1 :
            ans.append ( - 1 )
            continue
        if rem == 0 and turn % 2 == 0 : a = 5
            ans.append ( a [ m ] )
            continue
        if turn % 2 == 0 : a = 5
            cursize = n - rem
            if cursize < m : a = 5
                ans.append ( - 1 )
                continue
            ans.append ( a [ m + rem ] )
        else :
            cursize = rem
            if cursize < m : a = 5
                ans.append ( - 1 )
                continue
            ans.append ( a [ m ] )
    for i in ans :
        print ( i , end = '' )
}
|||

FIND_THE_MINIMUM_DISTANCE_BETWEEN_TWO_NUMBERS_1

def minDist ( arr , n , x , y ) :
    i = 0
    min_dist = int ( arr [ n ] )
    prev = 0
    for i in range ( n ) :
        if arr [ i ] == x or arr [ i ] == y :
            prev = i
            break
    for i in range ( n ) :
        if arr [ i ] == x or arr [ i ] == y :
            if arr [ prev ] != arr [ i ] and ( i - prev ) < min_dist :
                min_dist = i - prev
                prev = i
            else :
                prev = i
    return min_dist
}
|||

UNION_AND_INTERSECTION_OF_TWO_SORTED_ARRAYS_2

def printUnion ( arr1 , arr2 , m , n ) :
    i , j = arr1
    while i < m and j < n :
        if arr1 [ i ] < arr2 [ j ] :
            print ( arr1 [ i ] + " " for i in range ( m , n ) )
        elif arr2 [ j ] < arr1 [ i ] : a = 5
            print ( arr2 [ j ] + " " for j in range ( m ) )
        else :
            print ( arr2 [ j ] + " " for j in range ( m ) )
            i += 1
    while i < m :
        print ( arr1 [ i ] + " " for i in range ( m , n ) )
    while j < n :
        print ( arr2 [ j ] + " " for j in range ( m ) )
    return 0
}
|||

WORD_WRAP_PROBLEM_SPACE_OPTIMIZED_SOLUTION

def solve_word_wrap ( arr , n , k ) :
    i , j = arr [ : n ] , arr [ n : ]
    currlen = 0
    cost = 0
    dp = np.zeros ( ( n , k ) )
    ans = np.zeros ( ( n , k ) )
    dp [ n - 1 ] = 0
    ans = [ n - 1 , n - 1 ]
    for i in range ( n - 2 , - 1 , - 1 ) :
        global currlen
        dp [ i ] = int ( arr [ i ] )
        for j in range ( i , n ) :
            currlen += ( arr [ j ] + 1 for j in range ( n ) )
            if currlen ( arr ) > k :
                break
            if j == n - 1 :
                cost = 0
            a = 5
                cost = ( k - currlen ) * ( k - currlen ) + dp [ j + 1 ]
            if cost < dp [ i ] :
                dp [ i ] = cost
                ans [ i ] = j
    i = 0
    while i < n :
        print ( ( i + 1 for i in ans ) , end = ' ' )
        i = ans [ i ] + 1
}
|||

COUNT_DISTINCT_SUBSEQUENCES

def count_sub ( str ) :
    last = [ 0 ] * MAX_CHAR
    del last [ : ]
    n = len ( str )
    dp = [ n + 1 for n in str.split ( '.' ) ]
    dp [ 0 ] = 1
    for i in range ( 1 , n ) :
        dp [ i ] = 2 * dp [ i - 1 ]
        if last [ int ( str [ i - 1 ] ) ] != - 1 :
            dp [ i ] = dp [ i ] - dp [ last [ int ( str [ i - 1 ] ) ] ]
        last [ int ( str [ i - 1 ] ) ] = ( i - 1 )
    return dp [ n ]
}
|||

LONGEST_EVEN_LENGTH_SUBSTRING_SUM_FIRST_SECOND_HALF_3

def find_length ( str , n ) :
    ans = 0
    for i in range ( 0 , n - 2 ) :
        l , r = i , i + 1
        lsum , rsum = 0 , 0
        while r < n and l >= 0 :
            global lsum
            global rsum
            if lsum == rsum :
                global ans
            l -= 1
            r += 1
    ans = 0
}
|||

MAXIMUM_PATH_SUM_MATRIX

def findMaxPath ( mat ) :
    res = - 1
    for i in range ( M ) :
        res = max ( res , mat [ 0 ] [ i ] for i in range ( len ( mat ) ) )
    for i in range ( 1 , N ) :
        global res
        for j in range ( M ) :
            if j > 0 and j < M - 1 :
                mat [ i ] [ j ] += max ( mat [ i - 1 ] [ j ] , max ( mat [ i - 1 ] [ j - 1 ] , mat [ i - 1 ] [ j + 1 ] ) )
            elif j > 0 :
                mat [ i ] [ j ] += max ( mat [ i - 1 ] [ j ] , mat [ i - 1 ] [ j - 1 ] )
            elif j < M - 1 :
                mat [ i ] [ j ] += max ( mat [ i - 1 ] [ j ] , mat [ i - 1 ] [ j + 1 ] )
            res = max ( mat [ i , j ] for i , j in zip ( range ( len ( mat ) ) , range ( len ( mat ) ) ) )
    res = 0
}
|||

MAXIMUM_CONSECUTIVE_REPEATING_CHARACTER_STRING

def max_repeated ( str ) :
    len ( str )
    count = 0
    res = str [ 0 ]
    for i in range ( len ( str ) ) :
        global cur_count
        for j in range ( i + 1 , len ( str ) ) :
            if str [ i ] != str [ j ] :
                break
            global cur_count
        if cur_count > count :
            global count
            global res
    return res
}
|||

MAXIMUM_LENGTH_SUBSEQUENCE_DIFFERENCE_ADJACENT_ELEMENTS_EITHER_0_1

def maxLenSub ( arr , n ) :
    mls , max = np.mgrid [ 0 : n , 0 : n ]
    for i in range ( n ) :
        mls [ i ] = 1
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if abs ( arr [ i ] - arr [ j ] ) <= 1 and mls [ i ] < mls [ j ] + 1 :
                mls [ i ] = mls [ j ] + 1
    for i in range ( n ) :
        if max < mls [ i ] :
            global max
    return max
}
|||

BREAKING_NUMBER_FIRST_PART_INTEGRAL_DIVISION_SECOND_POWER_10

def calculate ( N ) :
    len ( N )
    l = len ( N ) / 2
    count = 0
    for i in range ( 1 , l ) :
        s = N [ : i ]
        l1 = len ( s )
        t = N [ i : l1 + i ]
        if s [ 0 ] == '0' or t [ 0 ] == '0' :
            continue
        if s.lower ( ) == t.lower ( ) :
            global count
    return count
}
|||

PROGRAM_BINARY_DECIMAL_CONVERSION

def binary_to_decimal ( n ) :
    num = n
    dec_value = 0
    base = 1
    temp = num
    while temp > 0 :
        last_digit = temp % 10
        global temp
        dec_value += last_digit * base
        global base
    return dec_value
}
|||

HOW_CAN_WE_SUM_THE_DIGITS_OF_A_GIVEN_NUMBER_IN_SINGLE_STATEMENT

def getSum ( n ) :
    sum = 0
    while n != 0 :
        global sum
        n = n / 10
    return sum
}
|||

FIND_N_TH_ELEMENT_FROM_STERNS_DIATOMIC_SERIES

def findSDSFunc ( n ) :
    DP = [ ]
    DP [ 0 ] = 0
    DP [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        if i % 2 == 0 :
            DP [ i ] = DP [ i / 2 ]
        else :
            DP [ i ] = DP [ ( i - 1 ) / 2 ] + DP [ ( i + 1 ) / 2 ]
    return DP [ n ]
}
|||

NUMBER_SINK_NODES_GRAPH

def count_sink ( n , m , edge_from , edge_to ) :
    mark = [ 0 ] * n + [ 0 ] * ( n + 1 )
    for i in range ( m ) :
        mark [ edge_from [ i ] for i in edge_to ] = 1
    count = 0
    for i in range ( 1 , n + 1 ) :
        if mark [ i ] == 0 :
            count += 1
    return count
}
|||

BREAK_NUMBER_THREE_PARTS

def count_of_ways ( n ) :
    count = 0
    for i in range ( 0 , n ) :
        for j in range ( 0 , n ) :
            for k in range ( 0 , n ) :
                if i + j + k == n :
                    global count
    return count
}
|||

PRINT_DISTINCT_ELEMENTS_GIVEN_INTEGER_ARRAY

def printDistinct ( arr , n ) :
    for i in range ( n ) :
        j = 0
        for j in range ( i ) :
            if arr [ i ] == arr [ j ] :
                break
        if i == j :
            print ( arr [ i ] , end = ' ' )
}
|||

MAXIMUM_NUMBER_SEGMENTS_LENGTHS_B_C

def maximum_segments ( n , a , b , c ) :
    dp = np.arange ( n + 10 )
    del dp [ - 1 ]
    dp [ 0 ] = 0
    for i in range ( n ) :
        if dp [ i ] != - 1 : a = 5
            if i + a <= n : a = 5
                dp [ i + a ] = max ( dp [ i ] + 1 for i in range ( n ) )
            if i + b <= n : a = 5
                dp [ i + b ] = max ( dp [ i ] + 1 for i in range ( n ) )
            if i + c <= n : a = 5
                dp [ i + c ] = max ( dp [ i ] + 1 for i in range ( n ) )
    return dp [ n ]
}
|||

CHECK_VALID_SEQUENCE_DIVISIBLE_M

def isPossible ( n , index , sum , M , arr , dp ) :
    if index == n :
        if ( sum % M ) == 0 :
            return True
        return False
    elif sum < 0 or sum >= MAX :
        return False
    if dp [ index ] [ sum ] != - 1 :
        if dp [ index ] [ sum ] == 0 :
            return False
        return True
    place_add = is_possible ( n , index + 1 , sum + arr [ index ] , M , arr , dp )
    place_minus = is_possible ( n , index + 1 , sum - arr [ index ] , M , arr , dp )
    res = ( place_add or place_minus )
    dp [ index ] [ sum ] = ( res ) if res else 1
    res = False
}
|||

FIND_PAIR_WITH_GREATEST_PRODUCT_IN_ARRAY

def findGreatest ( arr , n ) :
    result = - 1
    for i in range ( n ) :
        for j in range ( n - 1 ) :
            for k in range ( j + 1 , n ) :
                if arr [ j ] * arr [ k ] == arr [ i ] :
                    global result
    return result
}
|||

MAXIMUM_SUBARRAY_SUM_ARRAY_CREATED_REPEATED_CONCATENATION

def max_subarray_sum_repeated ( a , n , k ) :
    max_so_far = 0
    INT_MIN , max_ending_here = 0 , 0
    for i in range ( n * k ) :
        global max_ending_here
        if max_so_far < max_ending_here :
            global max_so_far
        if max_ending_here < 0 :
            global max_ending_here
    return max_so_far
}
|||

LEONARDO_NUMBER_1

def leonardo ( n ) :
    dp = [ 0 ] * ( n + 1 )
    dp [ 0 ] = dp [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        dp [ i ] = dp [ i - 1 ] + dp [ i - 2 ] + 1
    return dp [ n ]
}
|||

SUM_OF_ALL_SUBSTRINGS_OF_A_STRING_REPRESENTING_A_NUMBER

def sum_of_substrings ( num ) :
    n = len ( num )
    sumofdigit = [ n for n in range ( len ( num ) ) if num [ n ] == num [ - 1 ] ]
    sumofdigit [ 0 ] = num [ 0 ] - '0'
    res = sumofdigit [ 0 ]
    for i in range ( 1 , n ) :
        numi = num [ i ] - '0'
        sumofdigit [ i ] = ( i + 1 ) * numi + 10 * sumofdigit [ i - 1 ]
        global res
    return res
}
|||

PRUFER_CODE_TREE_CREATION

def print_tree_edges ( prufer , m ) :
    vertices = m + 2
    vertex_set = range ( vertices )
    for i in range ( vertices ) :
        vertex_set [ i ] = 0
    for i in range ( vertices - 2 ) :
        vertex_set [ prufer [ i ] - 1 ] += 1
    print ( "\nThe edge set E(G) is :\n" )
    j = 0
    for i in range ( vertices - 2 ) :
        for j in range ( vertices ) :
            if vertex_set [ j ] == 0 :
                vertex_set [ j ] = - 1
                print ( "(%d, %d) " % ( j + 1 , prufer [ i ] ) for i in range ( m ) )
                vertex_set [ prufer [ i ] - 1 ] -= 1
                break
    j = 0
    for i in range ( vertices ) :
        if vertex_set [ i ] == 0 and j == 0 :
            print ( "(%d, " % ( i + 1 ) for i in prufer )
            j += 1
        elif vertex_set [ i ] == 0 and j == 1 :
            print ( ( i + 1 , j + 1 ) for i , j in prufer )
}
|||

PROGRAM_FIND_SMALLEST_DIFFERENCE_ANGLES_TWO_PARTS_GIVEN_CIRCLE

def find_minimum_angle ( arr , n ) :
    l , sum , ans = 0 , 0 , 360
    for i in range ( n ) :
        global sum
        while sum >= 180 :
            ans = min ( ans , 2 * abs ( 180 - sum ( arr ) ) )
            global sum
            l += 1
        ans = min ( ans , 2 * abs ( 180 - sum ( arr ) ) )
    ans = 0
}
|||

FIND_MAXIMUM_AVERAGE_SUBARRAY_OF_K_LENGTH

def find_max_average ( arr , n , k ) :
    if k > n :
        return - 1
    csum = np.zeros ( n )
    csum [ 0 ] = arr [ 0 ]
    for i in range ( 1 , n ) :
        csum [ i ] = csum [ i - 1 ] + arr [ i ]
    max_sum , max_end = csum [ k - 1 ] , k - 1
    for i in range ( k , n ) :
        curr_sum = csum [ i ] - csum [ i - k ]
        if curr_sum > max_sum :
            global max_sum
            global max_end
    return max_end - k + 1
}
|||

SQUARE_PYRAMIDAL_NUMBER_SUM_SQUARES

def find_S ( s ) :
    sum = 0
    for n in range ( 1 , sum ( s ) ) :
        global sum
        if sum ( s ) == s :
            return n
    return - 1
}
|||

PROGRAM_TO_CALCULATE_AREA_OF_AN_CIRCLE_INSCRIBED_IN_A_SQUARE

def area_of_inscribed_circle ( a ) :
    return ( PI / 4 ) * a * a
}
|||

MINIMUM_NUMBER_CHARACTERS_REMOVED_MAKE_BINARY_STRING_ALTERNATE

def count_to_make_0lternate ( s ) :
    result = 0
    for i in ( 0 , 1 ) :
        if s [ i ] == s [ i + 1 ] :
            global result
    return result
}
|||

FIND_ELEMENTS_PRESENT_FIRST_ARRAY_NOT_SECOND

def find_missing ( a , b , n , m ) :
    for i in range ( n ) :
        pass
        for j in range ( m ) :
            if a [ i ] == b [ j ] :
                break
        if j == m :
            print ( a [ i ] , end = ' ' )
}
|||

REARRANGE_ARRAY_MAXIMUM_MINIMUM_FORM

def rearrange ( arr , n ) :
    temp = np.arange ( n )
    small , large = 0 , n - 1
    flag = True
    for i in range ( n ) :
        if flag :
            temp [ i ] = arr [ large : large + n ]
        else :
            temp [ i ] = arr [ small ]
        global flag
    arr = temp [ : n ]
}
|||

DYNAMIC_PROGRAMMING_SET_15_LONGEST_BITONIC_SUBSEQUENCE

def lbs ( arr , n ) :
    i , j = arr.shape
    lis = [ ]
    for i in range ( n ) :
        lis [ i ] = 1
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if arr [ i ] > arr [ j ] and lis [ i ] < lis [ j ] + 1 :
                lis [ i ] = lis [ j ] + 1
    lds = [ ]
    for i in range ( n ) :
        lds [ i ] = 1
    for i in range ( n - 2 , - 1 , - 1 ) :
        for j in range ( n - 1 , i , - 1 ) :
            if arr [ i ] > arr [ j ] and lds [ i ] < lds [ j ] + 1 :
                lds [ i ] = lds [ j ] + 1
    max = lis [ 0 ] + lds [ 0 ] - 1
    for i in range ( 1 , n ) :
        if lis [ i ] + lds [ i ] - 1 > max :
            global max
    return max ( arr )
}
|||

COUNT_PAIRS_WHOSE_PRODUCTS_EXIST_IN_ARRAY

def count_pairs ( arr , n ) :
    result = 0
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            product = arr [ i ] * arr [ j ]
            for k in range ( n ) :
                if arr [ k ] == product :
                    global result
                    break
    return result
}
|||

COUNT_SINGLE_NODE_ISOLATED_SUB_GRAPHS_DISCONNECTED_GRAPH

def compute ( graph , N ) :
    count = 0
    for i in range ( 1 , 7 ) :
        if graph [ i ] == 0 :
            global count
    return count
}
|||

HARDY_RAMANUJAN_THEOREM

def exact_prime_factor_count ( n ) :
    count = 0
    if n % 2 == 0 :
        global count
        while n % 2 == 0 :
            n = n / 2
    for i in range ( 3 , math.sqrt ( n ) + 1 ) :
        if n % i == 0 :
            global count
            while n % i == 0 :
                n = n / i
    if n > 2 :
        global count
    return count
}
|||

SHORTEST_COMMON_SUPERSEQUENCE_1

def superSeq ( X , Y , m , n ) :
    dp = [ m + 1 , n + 1 ]
    for i in range ( 0 , m ) :
        for j in range ( 0 , n ) :
            if i == 0 :
                dp [ i , j ] = j
            elif j == 0 :
                dp [ i , j ] = i
            elif X [ i - 1 ] == Y [ j - 1 ] :
                dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ]
            else :
                dp [ i ] [ j ] = 1 + min ( dp [ i - 1 ] [ j ] for j in range ( m , n ) )
    return dp [ m ] [ n ]
}
|||

POWER_SET

def print_power_set ( set , set_size ) :
    pow_set_size = int ( math.pow ( 2 , set_size ) )
    counter , j = divmod ( set_size , 2 )
    for counter in range ( pow_set_size ) :
        for j in range ( set_size ) :
            if ( counter & ( 1 << j ) ) > 0 :
                print ( set [ j ] for j in range ( set_size ) )
        print ( )
}
|||

CHECK_ARRAY_MAJORITY_ELEMENT

def isMajority ( a , n ) :
    mp = { }
    for i in range ( n ) :
        if mp.has_key ( a [ i ] ) :
            mp [ a [ i ] ] = mp [ a [ i ] ] + 1
    else :
        mp [ a [ i ] ] = 1
    for x in mp.items ( ) :
        if x.value >= n / 2 :
            return True
    return False
}
|||

PRINT_GIVEN_MATRIX_COUNTER_CLOCK_WISE_SPIRAL_FORM

def counterClockspiralPrint ( m , n , arr ) :
    i , k , l = 0 , 0 , 0
    cnt = 0
    total = m * n
    while k < m and l < n :
        if cnt == total :
            break
        for i in range ( k , m ) :
            print ( arr [ i ] [ l ] + " " for i in range ( m ) for l in range ( n ) )
            cnt += 1
        l += 1
        if cnt == total :
            break
        for i in l :
            print ( arr [ m - 1 ] [ i ] + " " for i in range ( m - 1 , n ) )
            cnt += 1
        m -= 1
        if cnt == total :
            break
        if k < m : a = 5
            for i in range ( m - 1 , k + 1 ) :
                print ( arr [ i ] [ n - 1 ] + " " for i in range ( m , n ) )
                cnt += 1
            n -= 1
        if cnt == total :
            break
        if l < n :
            for i in range ( n - 1 , l + 1 ) :
                print ( arr [ k ] [ i ] + " " for k in range ( m , n ) )
                cnt += 1
            k += 1
}
|||

PRIMALITY_TEST_SET_1_INTRODUCTION_AND_SCHOOL_METHOD

def isPrime ( n ) :
    if n <= 1 :
        return False
    for i in range ( 2 , n ) :
        if n % i == 0 :
            return False
    return True
}
|||

FIND_CHARACTER_FIRST_STRING_PRESENT_MINIMUM_INDEX_SECOND_STRING

def printMinIndexChar ( str , patt ) :
    min_index = int ( str.split ( patt ) [ 0 ] )
    m = re.search ( patt , str )
    n = len ( patt )
    for i in range ( n ) :
        for j in range ( m ) :
            if patt [ i ] == str [ j ] and j < minIndex :
                global minIndex
                break
    if min_index != int ( str ) :
        print ( "Minimum Index Character = " + str [ min_index ] )
    else :
        print ( "No character present" )
}
|||

PROGRAM_TO_FIND_TRANSPOSE_OF_A_MATRIX_1

def transpose ( A , B ) :
    i , j = B.shape
    for i in range ( N ) :
        for j in range ( M ) :
            B [ i , j ] = A [ j , i ]
}
|||

COUNT_NATURAL_NUMBERS_WHOSE_PERMUTATION_GREATER_NUMBER

def count_number ( n ) :
    result = 0
    for i in range ( 1 , 9 ) :
        s = Stack ( )
        if i <= n :
            s.push ( i )
            global result
        while not s.empty ( ) :
            tp = s.peek ( )
            s.pop ( )
            for j in tp % 10 :
                x = tp * 10 + j
                if x <= n :
                    s.push ( x )
                    global result
    return result
}
|||

FIND_FIRST_NATURAL_NUMBER_WHOSE_FACTORIAL_DIVISIBLE_X

def first_factorial_divisible_number ( x ) :
    i = 1
    fact = 1
    for i in range ( 1 , x ) :
        global fact
        if fact % x == 0 :
            break
    return i
}
|||

PRINT_EQUAL_SUM_SETS_ARRAY_PARTITION_PROBLEM_SET_2

def printEqualSumSets ( arr , n ) :
    i , currSum , sum = 0 , 0 , 0
    for i in range ( len ( arr ) ) :
        global sum
    if ( sum & 1 ) == 1 :
        print ( '-1' )
        return
    k = sum ( arr ) >> 1
    dp = np.zeros ( ( n + 1 , k + 1 ) )
    for i in range ( 1 , k + 1 ) :
        dp [ 0 ] [ i ] = False
    for i in range ( 0 , n ) :
        dp [ i ] [ 0 ] = True
    for i in range ( 1 , n + 1 ) :
        for curr_sum in range ( 1 , k ) :
            dp [ i ] [ curr_sum ] = dp [ i - 1 ] [ curr_sum ]
            if arr [ i - 1 ] <= currSum :
                dp [ i ] [ curr_sum ] = dp [ i ] [ curr_sum ] | dp [ i - 1 ] [ curr_sum - arr [ i - 1 ] ]
    set1 = [ ]
    set2 = [ ]
    if not dp [ n ] [ k ] :
        print ( '-1\n' )
        return
    i = n
    global currSum
    while i > 0 and curr_sum >= 0 :
        if dp [ i - 1 ] [ curr_sum ] :
            i -= 1
            set2.add ( arr [ i ] )
        elif dp [ i - 1 ] [ curr_sum - arr [ i - 1 ] ] :
            i -= 1
            global currSum
            set1.append ( arr [ i ] )
    print ( "Set 1 elements: " )
    for i in range ( len ( set1 ) ) :
        print ( set1 [ i ] , end = ' ' )
    print ( "\nSet 2 elements: " )
    for i in range ( len ( set2 ) ) :
        print ( set2 [ i ] , end = ' ' )
}
|||

COUNTING_PAIRS_PERSON_CAN_FORM_PAIR_ONE_1

def number_of_ways ( x ) :
    dp = [ 0 ] * x + 1
    dp [ 0 ] = dp [ 1 ] = 1
    for i in range ( 2 , x + 1 ) :
        dp [ i ] = dp [ i - 1 ] + ( i - 1 ) * dp [ i - 2 ]
    return dp [ x ]
}
|||

COUNT_NEGATIVE_NUMBERS_IN_A_COLUMN_WISE_ROW_WISE_SORTED_MATRIX

def count_negative ( M , n , m ) :
    count = 0
    for i in range ( n ) :
        for j in range ( m ) :
            if M [ i ] [ j ] < 0 :
                count += 1
            else :
                break
    return count
}
|||

COUNT_SET_BITS_IN_AN_INTEGER

def count_set_bits ( n ) :
    count = 0
    while n > 0 :
        global count
        n >>= 1
    return count
}
|||

MODULUS_TWO_FLOAT_DOUBLE_NUMBERS

def findMod ( a , b ) :
    if a < 0 :
        a = - a
    if b < 0 :
        b = - b
    mod = a
    while mod >= b :
        global mod
    if a < 0 :
        return - mod
    return mod
}
|||

FIND_A_SPECIFIC_PAIR_IN_MATRIX_1

def findMaxValue ( N , mat ) :
    max_value = int ( mat [ 'max_value' ] )
    max_arr = np.zeros ( ( N , N ) )
    maxArr [ N - 1 ] [ N - 1 ] = mat [ N - 1 ] [ N - 1 ]
    maxv = mat [ N - 1 ] [ N - 1 ]
    for j in range ( N - 2 , - 1 , - 1 ) :
        if mat [ N - 1 ] [ j ] > maxv :
            global maxv
        maxArr [ N - 1 ] [ j ] = maxv
    global maxv
    for i in range ( N - 2 , - 1 , - 1 ) :
        if mat [ i ] [ N - 1 ] > maxv : a = 5
            global maxv
        maxArr [ i ] [ N - 1 ] = maxv
    for i in range ( N - 2 , - 1 , - 1 ) :
        for j in range ( N - 2 , - 1 , - 1 ) :
            if maxArr [ i + 1 ] [ j + 1 ] - mat [ i ] [ j ] > maxValue :
                global maxValue
            maxArr [ i ] [ j ] = max ( mat [ i ] [ j ] , max ( maxArr [ i ] [ j + 1 ] , maxArr [ i + 1 ] [ j ] ) )
    return maxValue
}
|||

MINIMUM_SUM_TWO_NUMBERS_FORMED_DIGITS_ARRAY

def solve ( arr , n ) :
    return np.argsort ( arr ) [ : n ]
    a , b = arr
    for i in range ( n ) :
        if i % 2 != 0 :
            global a
        else :
            global b
    return a + b
}
|||

COUNT_DISTINCT_NON_NEGATIVE_PAIRS_X_Y_SATISFY_INEQUALITY_XX_YY_N_2_1

def count_solutions ( n ) :
    x , y_count , res = count_solutions ( n )
    for y_count in range ( 0 , y_count * y_count ) :
        pass
    while yCount != 0 :
        global res
        global x
        while y_count != 0 and ( x ** 2 + ( y_count - 1 ) ** 2 >= n ) :
            global y_count
    return res
}
|||

FIND_INDEX_GIVEN_FIBONACCI_NUMBER_CONSTANT_TIME

def find_index ( n ) :
    if n <= 1 :
        return n
    a , b , c = 0 , 1 , 1
    res = 1
    while c < n :
        global c
        global res
        global a , b
        global b , c
    return res
}
|||

PROGRAM_OCTAL_DECIMAL_CONVERSION

def octal_to_decimal ( n ) :
    num = n
    dec_value = 0
    base = 1
    temp = num
    while temp > 0 :
        last_digit = temp % 10
        global temp
        dec_value += last_digit * base
        global base
    return dec_value
}
|||

FIND_PERMUTED_ROWS_GIVEN_ROW_MATRIX

def permutated_rows ( mat , m , n , r ) :
    s = LinkedHashSet ( )
    for j in range ( n ) :
        s.append ( mat [ r ] [ j ] )
    for i in range ( m ) :
        if i == r :
            continue
        j = 0
        for j in range ( n ) :
            if not s.has_key ( mat [ i ] [ j ] ) :
                break
        if j != n :
            continue
        print ( i , ', '.join ( [ str ( j ) for j in range ( m ) ] ) for i in range ( n ) )
}
|||

PRINT_A_CLOSEST_STRING_THAT_DOES_NOT_CONTAIN_ADJACENT_DUPLICATES

def no_adjacent_dup ( s1 ) :
    n = len ( s1 )
    s = s1.split ( )
    for i in range ( 1 , n ) :
        if s [ i ] == s [ i - 1 ] :
            s [ i ] = 'a'
            while s [ i ] == s [ i - 1 ] or ( i + 1 < n and s [ i ] == s [ i + 1 ] ) :
                s [ i ] += 1
            global i
    return ( [ s for s in s1 if s != '' ] )
}
|||

SUM_MANHATTAN_DISTANCES_PAIRS_POINTS

def distancesum ( x , y , n ) :
    sum = 0
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            sum += ( abs ( x [ i ] - x [ j ] ) + abs ( y [ i ] - y [ j ] ) )
    return sum ( x )
}
|||

PROGRAM_FIND_STRING_START_END_GEEKS

def isCornerPresent ( str , corner ) :
    """Returns True if the arguments are not the same value."""
    cl = len ( corner )
    if n < cl : a = 5
        return False
    return ( str [ 0 : cl ] == corner and str [ n - cl : n ] == corner )
}
|||

LONGEST_SUBARRAY_COUNT_1S_ONE_COUNT_0S

def lenOfLongSubarr ( arr , n ) :
    um = { }
    sum , maxLen = 0 , 0
    for i in range ( n ) :
        sum += arr [ i ] if i in arr else - 1
        if sum ( arr ) == 1 :
            global maxLen
        elif not um.has_key ( sum ( arr ) ) :
            um [ sum ] = i
        if um.has_key ( sum - 1 ) :
            if maxLen < ( i - um [ sum - 1 ] ) :
                global max_len
    return maxLen
}
|||

DIVIDE_CONQUER_SET_6_SEARCH_ROW_WISE_COLUMN_WISE_SORTED_2D_ARRAY

def search ( mat , from_row , to_row , from_col , to_col , key ) :
    i = from_row + ( to_row - from_row ) / 2
    j = from_col + ( to_col - from_col ) / 2
    if mat [ i , j ] == key :
        print ( "Found " + str ( key ) + " at " + str ( i ) + " " + str ( j ) )
    a = 5
        if i != to_row or j != from_col :
            return mat [ from_row , i , j , to_col , key ]
        if from_row == to_row and from_col + 1 == to_col :
            if mat [ from_row ] [ to_col ] == key :
                print ( "Found " + str ( key ) + " at " + str ( from_row ) + " " + str ( to_col ) )
        if mat [ i , j ] < key :
            if i + 1 <= to_row :
                return mat [ i + 1 : i + 2 ]
        a = 5
            if j - 1 >= from_col :
                return [ from_row , to_row , from_col , j - 1 , key for j in range ( len ( mat ) ) ]
}
|||

SHORTEST_COMMON_SUPERSEQUENCE

def superSeq ( X , Y , m , n ) :
    if m == 0 :
        return n
    if n == 0 :
        return m
    if X [ m - 1 ] == Y [ n - 1 ] :
        return 1 + superSeq ( X , Y , m - 1 , n - 1 )
    return 1 + min ( superSeq ( X , Y , m - 1 , n ) , superSeq ( X , Y , m , n - 1 ) )
}
|||

URLIFY_GIVEN_STRING_REPLACE_SPACES

def replace_spaces ( str ) :
    space_count , i = 0 , 0
    for i in range ( len ( str ) ) :
        if str [ i ] == ' ' :
            global space_count
    while str [ i - 1 ] == ' ' :
        space_count -= 1
        i = 0
    new_length = i + space_count * 2
    if len ( new_args ) > MAX :
        return str
    index = new_length - 1
    new_args = [ ]
    return [ x for x in args if x != '' ]
    for i in range ( i - 1 , - 1 , - 1 ) :
        if new_str [ j ] == ' ' :
            str [ index ] = '0'
            str [ index - 1 ] = '2'
            str [ index - 2 ] = '%'
            global index
        else :
            str [ index ] = new_str [ j ]
            index = str.index ( ' ' )
    return str
}
|||

MAXIMUM_PATH_SUM_STARTING_CELL_0_TH_ROW_ENDING_CELL_N_1_TH_ROW

def MaximumPath ( Mat ) :
    """MaximumPath(Mat[, int]) -> int"""
    dp = np.zeros ( ( N , N + 2 ) )
    for rows , cols in dp :
        pass
    for i in range ( N ) :
        dp [ 0 ] [ i + 1 ] = Mat [ 0 ] [ i ]
    for i in range ( 1 , N ) :
        for j in range ( 1 , N ) :
            dp [ i ] [ j ] = max ( dp [ i - 1 ] [ j - 1 ] , max ( dp [ i - 1 ] [ j ] , dp [ i - 1 ] [ j + 1 ] ) ) + Mat [ i ] [ j - 1 ]
    for i in range ( 0 , N ) :
        result = max ( result , dp [ N - 1 ] [ i ] for i in range ( N - 1 ) )
    return result
}
|||

COMPUTE_THE_INTEGER_ABSOLUTE_VALUE_ABS_WITHOUT_BRANCHING

def get_abs ( n ) :
    mask = n >> ( SIZE_INT * CHAR_BIT - 1 )
    return ( ( n + mask ) ^ mask )
}
|||

COUNT_PALINDROMIC_SUBSEQUENCE_GIVEN_STRING_1

def countPS ( i , j ) :
    if i >= n or j < 0 :
        return 0
    if dp [ i ] [ j ] != - 1 :
        return dp [ i ] [ j ]
    if ( i - j == 1 ) :
        if str ( i ) == str ( j ) :
            return dp [ i ] [ j ] = 3
        else :
            return dp [ i ] [ j ] = 2
    if i == j :
        return dp [ 1 ] [ j ] = 1
    elif str ( i ) == str ( j ) :
        return dp [ i ] [ j ] = count_ps ( i + 1 , j ) + count_ps ( i , j - 1 ) + 1
    else :
        return dp [ i ] [ j ] = count_ps ( i + 1 , j ) + count_ps ( i , j - 1 ) - count_ps ( i + 1 , j - 1 )
}
|||

LARGEST_SUM_CONTIGUOUS_SUBARRAY_2

def max_subarray_sum ( a , size ) :
    max_so_far = a [ 0 ]
    curr_max = a [ 0 ]
    for i in range ( 1 , size ) :
        global curr_max
        global max_so_far
    return max_so_far
}
|||

COUNT_MINIMUM_STEPS_GET_GIVEN_DESIRED_ARRAY

def count_min_operations ( n ) :
    result = 0
    while True :
        zero_count = 0
        i = 1
        for i in range ( n ) :
            if arr [ i ] % 2 == 1 :
                break
            elif arr [ i ] == 0 :
                global zero_count
        if zero_count == n :
            return result
        if i == n :
            for j in range ( n ) :
                arr [ j ] = arr [ j ] / 2
            global result
        for j in range ( i , n ) :
            if arr [ j ] % 2 == 1 :
                arr [ j ] -= 1
                global result
}
|||

PRINT_FIBONACCI_SEQUENCE_USING_2_VARIABLES_1

def fib ( n ) :
    a , b = 0 , 1
    if n >= 0 :
        print ( a , end = ' ' )
    if n >= 1 :
        sys.stdout.write ( b '%d ' % n )
    for i in range ( 2 , n + 1 ) :
        print ( a , b , n )
        b = a + b
        a = b - a
}
|||

PROGRAM_CHECK_INPUT_INTEGER_STRING

def isNumber ( s ) :
    for i in s :
        if type ( s ) == str :
            return False
    return True
}
|||

MINIMUM_HEIGHT_TRIANGLE_GIVEN_BASE_AREA

def minHeight ( base , area ) :
    d = ( 2 * area ) / base
    return math.ceil ( d )
}
|||

FIND_POSITION_GIVEN_NUMBER_AMONG_NUMBERS_MADE_4_7

def findpos ( n ) :
    k , pos , i = findpos ( n )
    while k != len ( n ) :
    i += 1
    global k
return pos
pass
}
|||

MINIMUM_OPERATIONS_REQUIRED_SET_ELEMENTS_BINARY_MATRIX

def minOperation ( arr ) :
    ans = 0
    for i in range ( N - 1 , - 1 , - 1 ) :
        for j in range ( M - 1 , - 1 , - 1 ) :
            if arr [ i ] [ j ] == False :
                global ans
                for k in range ( 0 , i ) :
                    for h in range ( 0 , j ) :
                        if arr [ k ] [ h ] == True :
                            arr [ k ] [ h ] = False
                        else :
                            arr [ k ] [ h ] = True
    return ans
}
|||

LONGEST_EVEN_LENGTH_SUBSTRING_SUM_FIRST_SECOND_HALF_2

def find_length ( str , n ) :
    sum = [ 0 ] * n + [ 0 ] * n
    sum [ 0 ] = 0
    for i in range ( 1 , n + 1 ) :
        sum [ i ] = ( sum [ i - 1 ] + str [ i - 1 ] - '0' )
    ans = 0
    for len in range ( 2 , n + 1 , 2 ) :
        for i in range ( 0 , n - len ( str ) ) :
            j = i + len ( str ) - 1
            if sum [ i + len / 2 ] - sum [ i ] == sum [ i + len ] - sum [ i + len / 2 ] :
                global ans
    ans = 0
}
|||

MULTIPLY_LARGE_NUMBERS_REPRESENTED_AS_STRINGS

def multiply ( num1 , num2 ) :
    len1 = len ( num1 )
    len2 = len ( num2 )
    if len1 == 0 or len2 == 0 :
        return "0" * num2
    result = [ num1 * num2 ]
    i_n1 = 0
    i_n2 = 0
    for i in range ( len1 - 1 , - 1 , - 1 ) :
        carry = 0
        n1 = num1 [ i ] - '0'
        global i_n2
        for j in len2 - 1 :
            n2 = num2 [ j ] - '0'
            sum = n1 * n2 + result [ i_n1 + i_n2 ] + carry
            global carry
            result [ i_n1 + i_n2 ] = sum % 10
            i_n2 += 1
        if carry > 0 :
            result [ i_n1 + i_n2 ] += carry
        global i_n1
    i = len ( result ) - 1
    while i >= 0 and result [ i ] == 0 :
        i -= 1
    if i == - 1 :
        return "0" * num2
    s = ""
    while i >= 0 :
        s += ( result [ i ] for i in range ( len ( result ) ) )
    return s
}
|||

PARTITION_NUMBER_TWO_DIVISBLE_PARTS

def find_division ( str , a , b ) :
    len ( str )
    lr = [ ]
    lr [ 0 ] = ( ord ( str [ 0 ] ) - ord ( '0' ) ) % a
    for i in range ( 1 , len ( str ) ) :
        lr [ i ] = ( ( lr [ i - 1 ] * 10 ) % a + ( int ( str [ i ] ) - int ( '0' ) ) ) % a
    rl = [ ]
    rl [ len ( str ) - 1 ] = ( ord ( str [ len ( str ) - 1 ] ) - ord ( '0' ) ) % b
    power10 = 10
    for i in range ( len ( str ) - 2 , - 1 , - 1 ) :
        rl [ i ] = ( rl [ i + 1 ] + ( int ( str [ i ] ) - int ( '0' ) ) * power10 ) % b
        power10 = ( power10 ** 10 ) % b
    for i in range ( len ( str ) - 1 ) :
        if lr [ i ] != 0 :
            continue
        if rl [ i + 1 ] == 0 :
            print ( 'YES' )
            for k in range ( 0 , i ) :
                print ( str [ k ] )
            print ( ", ".join ( str.split ( "/" ) [ a : b ] ) )
            for k in range ( i + 1 , len ( str ) ) :
                print ( str [ k ] )
            return
    print ( 'NO' )
}
|||

PROGRAM_BEST_FIT_ALGORITHM_MEMORY_MANAGEMENT

def bestFit ( blockSize , m , processSize , n ) :
    allocation = np.zeros ( ( n , m ) )
    for i in range ( len ( allocation ) ) :
        allocation [ i ] = - 1
    for i in range ( n ) :
        best_idx = - 1
        for j in range ( m ) :
            if blockSize [ j ] >= processSize [ i ] :
                if best_idx == - 1 :
                    bestIdx = j
                elif blockSize [ bestIdx ] > blockSize [ j ] :
                    bestIdx = j
        if best_idx != - 1 :
            allocation [ i ] = bestIdx
            blockSize [ bestIdx ] -= processSize [ i ]
    print ( "\nProcess No.\tProcess Size\tBlock no." )
    for i in range ( n ) :
        print ( "   %d\t\t%d\n" % ( i + 1 , processSize [ i ] ) )
        if allocation [ i ] != - 1 :
            print ( allocation [ i ] + 1 )
        a = 5
            print ( "Not Allocated" )
        print ( )
}
|||

FINDING_THE_MAXIMUM_SQUARE_SUB_MATRIX_WITH_ALL_EQUAL_ELEMENTS

def largestKSubmatrix ( a ) :
    dp = np.zeros ( ( Row , Col ) )
    result = 0
    for i in range ( Row ) :
        for j in range ( Col ) :
            if i == 0 or j == 0 :
                dp [ i ] [ j ] = 1
            else :
                if a [ i ] [ j ] == a [ i - 1 ] [ j ] and a [ i ] [ j ] == a [ i ] [ j - 1 ] and a [ i ] [ j ] == a [ i - 1 ] [ j - 1 ] :
                    dp = [ i for i in a if ( dp [ i - 1 ] [ j ] > dp [ i ] [ j - 1 ] and dp [ i - 1 ] [ j ] > dp [ i - 1 ] [ j - 1 ] + 1 ) ]
                else :
                    dp [ i ] [ j ] = 1
            global result
    return result
}
|||

FRIENDS_PAIRING_PROBLEM_1

def countFriendsPairings ( n ) :
    if dp [ n ] != - 1 :
        return dp [ n ]
    if n > 2 :
        return dp [ n ] = countFriendsPairings ( n - 1 ) + ( n - 1 ) * countFriendsPairings ( n - 2 )
    else :
        return dp [ n ] = n
}
|||

FIRST_ELEMENT_OCCURRING_K_TIMES_ARRAY

def first_element ( arr , n , k ) :
    count_dict = { }
    for i in range ( n ) :
        a = 0
        if count_dict [ arr [ i ] ] :
            global a
        count_dict [ arr [ i ] ] = a + 1
    for i in range ( n ) :
        if count_dict [ arr [ i ] ] == k :
            return arr [ i ]
    return - 1
}
|||

SUM_SERIES_0_6_0_06_0_006_0_0006_N_TERMS

def sum_of_series ( n ) :
    return ( 0.666 ) * ( 1 - 1 / math.pow ( 10 , n ) )
}
|||

COUNT_WORDS_IN_A_GIVEN_STRING

def countWords ( str ) :
    state = OUT
    wc = 0
    i = 0
    while i < len ( str ) :
        if str [ i ] in [ ' ' , '\n' , '\t' ] :
            global state
        elif state == OUT :
            global state
            global wc
        yield i
    return wc
}
|||

PARTITION_INTO_TWO_SUBARRAYS_OF_LENGTHS_K_AND_N_K_SUCH_THAT_THE_DIFFERENCE_OF_SUMS_IS_MAXIMUM

def maxDifference ( arr , N , k ) :
    M , S , S1 , max_difference = np.unique ( arr , return_inverse = True )
    for i in range ( N ) :
        S += arr [ i ]
    temp = 0
    for i in range ( N ) :
        for j in range ( i + 1 , N ) :
            if arr [ i ] < arr [ j ] :
                global temp
                arr [ i , j ] = arr [ j , i ]
                arr [ j ] = temp
    global M
    for i in range ( M ) :
        S1 += arr [ i ]
    global max_difference
    return max_difference
}
|||

HOW_WILL_YOU_PRINT_NUMBERS_FROM_1_TO_200_WITHOUT_USING_LOOP

def print_nos ( n ) :
    if n > 0 :
        print ( n - 1 )
        print ( n , end = ' ' )
    return
}
|||

GIVEN_A_SORTED_AND_ROTATED_ARRAY_FIND_IF_THERE_IS_A_PAIR_WITH_A_GIVEN_SUM_1

def pairs_in_sorted_rotated ( arr , n , x ) :
    i = 0
    for i in range ( n - 1 ) :
        if arr [ i ] > arr [ i + 1 ] :
            break
    l = ( i + 1 ) % n
    r = i
    cnt = 0
    while l != r :
        if arr [ l ] + arr [ r ] == x :
            global cnt
            if l == ( r - 1 + n ) % n : a = 5
                return cnt
            global l
            r = ( r - 1 + n ) % n
        elif arr [ l ] + arr [ r ] < x : a = 5
            global l
        else :
            global r
    return cnt
}
|||

FIND_THE_ELEMENT_THAT_APPEARS_ONCE

def getSingle ( arr , n ) :
    ones , twos = 0 , 0
    common_bit_mask = 0
    for i in range ( n ) :
        global twos
        global ones
        common_bit_mask = ~ ( ones & twos )
        ones &= common_bit_mask
        global twos
    return ones
}
|||

CASSINIS_IDENTITY

def cassini ( n ) :
    return ( n & 1 ) or - 1
}
|||

DISTRIBUTING_ALL_BALLS_WITHOUT_REPETITION

def distributingBalls ( k , n , str ) :
    a = range ( MAX_CHAR )
    for i in range ( n ) :
        a [ str [ i ] - 'a' ] += 1
    for i in range ( MAX_CHAR ) :
        if a [ i ] > k :
            return False
    return True
}
|||

DISTRIBUTING_ITEMS_PERSON_CANNOT_TAKE_TWO_ITEMS_TYPE

def check_count ( arr , n , k ) :
    count = 0
    for i in range ( n ) :
        count = 0
        for j in range ( n ) :
            if arr [ j ] == arr [ i ] :
                count += 1
            if count > 2 ** k :
                return False
    return True
}
|||

MAXIMIZE_ARRJ_ARRI_ARRL_ARRK_SUCH_THAT_I_J_K_L

def find_max_value ( arr , n ) :
    if n < 4 :
        print ( "The array should have" , " atleast 4 elements" )
    table1 = np.arange ( n + 1 )
    table2 = np.zeros ( ( n , ) )
    table3 = [ 0 ] * ( n - 1 )
    table4 = np.zeros ( ( n - 2 , ) )
    np.fill_with ( table1 , int ( n ) )
    del table2 [ int ( n ) ]
    del table3 [ int ( n ) ]
    del table4 [ int ( n ) ]
    for i in range ( n - 1 , - 1 , - 1 ) :
        table1 [ i ] = max ( table1 [ i + 1 ] , arr [ i ] )
    for i in range ( n - 2 , - 1 , - 1 ) :
        table2 [ i ] = max ( table2 [ i + 1 ] , table1 [ i + 1 ] - arr [ i ] )
    for i in range ( n - 3 , - 1 , - 1 ) :
        table3 [ i ] = max ( table3 [ i + 1 ] , table2 [ i + 1 ] + arr [ i ] for i in range ( n ) )
    for i in range ( n - 4 , - 1 , - 1 ) :
        table4 [ i ] = max ( table4 [ i + 1 ] , table3 [ i + 1 ] - arr [ i ] )
    return table4 [ 0 ]
}
|||

COUNT_NEGATIVE_NUMBERS_IN_A_COLUMN_WISE_ROW_WISE_SORTED_MATRIX_1

def count_negative ( M , n , m ) :
    count = 0
    i = 0
    j = m - 1
    while j >= 0 and i < n :
        if M [ i ] [ j ] < 0 :
            count += j + 1
            i += 1
        else :
            j -= 1
    return count
}
|||

SORT_AN_ARRAY_OF_0S_1S_AND_2S

def sort012 ( a , arr_size ) :
    lo = 0
    hi = arr_size - 1
    mid , temp = divmod ( arr_size , 2 )
    while mid <= hi :
    case 1 :
    break
pass
pass
pass
}
|||

NTH_EVEN_FIBONACCI_NUMBER

def evenFib ( n ) :
    if n < 1 :
        return n
    if n == 1 :
        return 2
    return ( ( 4 * evenFib ( n - 1 ) ) + evenFib ( n - 2 ) )
}
|||

NEXT_GREATER_ELEMENT

def printNGE ( arr , n ) :
    next , i , j = arr
    for i in range ( n ) :
        global next
        for j in range ( i + 1 , n ) :
            if arr [ i ] < arr [ j ] :
                global next
                break
        print ( arr [ i ] , " -- " + next ( arr ) )
}
|||

CHECK_WHETHER_GIVEN_CIRCLE_RESIDE_BOUNDARY_MAINTAINED_OUTER_CIRCLE_INNER_CIRCLE

def fit_or_not_fit ( R , r , x , y , rad ) :
    val = np.sqrt ( np.power ( x , 2 ) + np.power ( y , 2 ) )
    if val + rad <= R and val - rad >= R - r :
        print ( 'Fits' )
    else :
        print ( "Doesn't Fit" )
}
|||

BASIC_AND_EXTENDED_EUCLIDEAN_ALGORITHMS_1

def gcdExtended ( a , b , x , y ) :
    if a == 0 : a = 5
        x = 0
        y = 1
        return b
    x1 , y1 = 1 , 1
    gcd , x1 , y1 = gcdExtended ( b % a , a , x1 , y1 )
    x = y1 - ( b / a ) * x1
    y = x1
    return gcd
}
|||

FIND_SMALLEST_RANGE_CONTAINING_ELEMENTS_FROM_K_LISTS

def findSmallestRange ( arr , n , k ) :
    i , minval , maxval , minrange , minel = arr
    for i in range ( 0 , k ) :
        ptr [ i ] = 0
    minrange = int ( arr [ 0 ] )
    while True :
        minind = - 1
        minval = int ( arr [ n ] )
        maxval = int ( arr [ n ] )
        flag = 0
        for i in range ( k ) :
            if ptr [ i ] == n :
                flag = 1
                break
            if ptr [ i ] < n and arr [ i ] [ ptr [ i ] ] < minval :
                minind = i
                minval = arr [ i ] [ ptr [ i ] ]
            if ptr [ i ] < n and arr [ i ] [ ptr [ i ] ] > maxval :
                maxval = arr [ i ] [ ptr [ i ] ]
        if flag == 1 :
            break
        ptr [ minind ] += 1
        if ( maxval - minval ) < minrange :
            minel = minval
            maxel = maxval
            minrange = maxel - minel
    print ( "The smallest range is [%d , %d]" % ( minel , maxel ) )
}
|||

FIND_THE_MINIMUM_COST_TO_REACH_A_DESTINATION_WHERE_EVERY_STATION_IS_CONNECTED_IN_ONE_DIRECTION

def minCost ( cost ) :
    dist = [ 0 ] * N
    for i in range ( N ) :
        dist [ i ] = INF
    dist [ 0 ] = 0
    for i in range ( N ) :
        for j in range ( i + 1 , N ) :
            if dist [ j ] > dist [ i ] + cost [ i ] :
                dist [ j ] = dist [ i ] + cost [ i ]
    return dist [ N - 1 ]
}
|||

MIDDLE_OF_THREE_USING_MINIMUM_COMPARISONS_1

def middle_of_three ( a , b , c ) :
    if a > b :
        if b > c :
            return b
        elif a > c :
            return c
        else :
            return a , b , c
    else :
        if a > c :
            return a , b , c
        elif b > c :
            return c
        else :
            return b
}
|||

CHECK_LARGE_NUMBER_DIVISIBLE_11_NOT

def check ( str ) :
    n = len ( str )
    oddDigSum , evenDigSum = 0 , 0
    for i in range ( n ) :
        if i % 2 == 0 :
            oddDigSum += ( str [ i ] - '0' )
        else :
            evenDigSum += ( str [ i ] - '0' )
    return ( ( oddDigSum - evenDigSum ) % 11 == 0 )
}
|||

COMPUTE_MODULUS_DIVISION_BY_A_POWER_OF_2_NUMBER

def getModulo ( n , d ) :
    return ( n & ( d - 1 ) )
}
|||

COUNT_BINARY_STRINGS_K_TIMES_APPEARING_ADJACENT_TWO_SET_BITS

def count_strings ( n , k ) :
    dp = [ 0 ] * ( n + 1 ) + [ k + 1 ] * ( n + 1 ) + [ 2 ] * ( n + 1 )
    dp [ 1 ] [ 0 ] [ 0 ] = 1
    dp [ 1 ] [ 0 ] [ 1 ] = 1
    for i in range ( 2 , n ) :
        for j in range ( i , n + 1 ) :
            dp [ i ] [ j ] [ 0 ] = dp [ i - 1 ] [ j ] [ 0 ] + dp [ i - 1 ] [ j ] [ 1 ]
            dp [ i ] [ j ] [ 1 ] = dp [ i - 1 ] [ j ] [ 0 ]
            if j - 1 >= 0 :
                dp [ i ] [ j ] [ 1 ] += dp [ i - 1 ] [ j - 1 ] [ 1 ]
    return dp [ n ] [ k ] [ 0 ] + dp [ n ] [ k ] [ 1 ]
}
|||

FINDING_K_MODULUS_ARRAY_ELEMENT

def print_equal_mod_numbers ( arr , n ) :
    print ( sorted ( arr ) )
    d = arr [ n - 1 ] - arr [ 0 ]
    v = Vector ( )
    for i in range ( 1 , n * i <= d ) :
        if d % i == 0 :
            v.append ( i )
            if i != d / i :
                v.append ( d / i )
    for i in v :
        temp = arr [ 0 ] % v [ i ]
        j = 0
        for j in range ( 1 , n ) :
            if arr [ j ] % v [ i ] != temp :
                break
        if j == n :
            print ( v [ i ] , end = ' ' )
}
|||

CIRCULAR_MATRIX_CONSTRUCT_A_MATRIX_WITH_NUMBERS_1_TO_MN_IN_SPIRAL_WAY

def spiral_fill ( m , n , a ) :
    val = 1
    k , l = a
    while k < m and l < n :
        for i in l ( m , n ) :
            a [ k ] [ i ] = val + 1
        k += 1
        for i in range ( k , m ) :
            a [ i ] [ n - 1 ] = val
        n -= 1
        if k < m :
            for i in range ( n - 1 , l + 1 ) :
                a [ m - 1 ] [ i ] = val + 1
            m -= 1
        if l < n :
            for i in range ( m - 1 , k + 1 , - 1 ) :
                a [ i ] [ l ] = val + 1
            l += 1
}
|||

FIND_THE_TWO_REPEATING_ELEMENTS_IN_A_GIVEN_ARRAY_2

def printRepeating ( arr , size ) :
    xor = arr [ 0 ]
    set_bit_no = 0
    i = 0
    n = size - 2
    x , y = arr
    for i in range ( 1 , size ) :
        xor ^= arr [ i ]
    for i in range ( 1 , n ) :
        xor ^= i
    global set_bit_no
    for i in range ( size ) :
        a = arr & set_bit_no
        if a != 0 :
            x = x ^ arr [ i ]
        else :
            y = y ^ arr [ i ]
    for i in range ( 1 , n ) :
        a = i & set_bit_no
        if a != 0 :
            x = x ^ i
        else :
            y = y ^ i
    print ( "The two reppeated elements are :" )
    print ( x , y )
}
|||

COUNT_POSSIBLE_WAYS_TO_CONSTRUCT_BUILDINGS

def countWays ( N ) :
    if N == 1 :
        return 4
    count_b , count_s , prev_count_b , prev_count_s = N
    for i in range ( 2 , N + 1 ) :
        global prev_countB
        global prev_count_s
        global count_s
        global count_b , prev_count_s
    result = count_s + count_b
    return ( result * result )
}
|||

ONE_LINE_FUNCTION_FOR_FACTORIAL_OF_A_NUMBER

def factorial ( n ) :
    return ( n if n == 1 or n == 0 else 1 ) * factorial ( n - 1 )
}
|||

CHECK_GIVEN_MATRIX_SPARSE_NOT

def isSparse ( array , m , n ) :
    counter = 0
    for i in range ( m ) :
        for j in range ( n ) :
            if array [ i , j ] == 0 :
                global counter
    return ( counter > ( ( m * n ) / 2 ) )
}
|||

DYNAMIC_PROGRAMMING_SET_10_0_1_KNAPSACK_PROBLEM

def knapSack ( W , wt , val , n ) :
    if n == 0 or W == 0 :
        return 0
    if wt [ - 1 ] > W :
        return n - 1
    else :
        return max ( val [ n - 1 ] + knap_sack ( W - wt [ n - 1 ] , wt , val , n - 1 ) , knap_sack ( W , wt , val , n - 1 ) )
}
|||

FIND_SUBARRAY_LEAST_AVERAGE

def find_min_avg_subarray ( n , k ) :
    if n < k :
        return
    res_index = 0
    curr_sum = 0
    for i in range ( k ) :
        curr_sum += arr [ i ]
    min_sum = curr_sum
    for i in range ( k , n ) :
        curr_sum += arr [ i ] - arr [ i - k ]
        if curr_sum < min_sum :
            global min_sum
            global res_index
    print ( "Subarray between [%d, %d] has minimum average" % ( res_index , ( res_index + k - 1 ) ) )
}
|||

QUERIES_FOR_CHARACTERS_IN_A_REPEATED_STRING

def query ( s , i , j ) :
    n = len ( s )
    i %= n
    j %= n
    if s [ i ] == s [ j ] :
        print ( "Yes" )
    else :
        print ( "No" )
}
|||

A_PRODUCT_ARRAY_PUZZLE_1

def productArray ( arr , n ) :
    if n == 1 :
        print ( '0' * n )
        return
    i , temp = 1 , 1
    prod = np.prod ( arr , n )
    for j in range ( n ) :
        prod [ j ] = 1
    for i in range ( n ) :
        prod [ i ] = temp
        temp *= arr [ i ]
    global temp
    for i in range ( n - 1 , - 1 , - 1 ) :
        prod [ i ] *= temp
        temp *= arr [ i ]
    for i in range ( n ) :
        print ( prod [ i ] , end = ' ' )
    return
}
|||

FIND_PAIRS_GIVEN_SUM_ELEMENTS_PAIR_DIFFERENT_ROWS

def pairSum ( mat , n , sum ) :
    for i in range ( n ) :
        return sum ( [ i for i in range ( n ) if sum == i ] )
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            left , right = 0 , n - 1
            while left < n and right >= 0 :
                if ( mat [ i ] [ left ] + mat [ j ] [ right ] ) == sum :
                    print ( "(%d, %d), " % ( mat [ i ] [ left ] , mat [ j ] [ right ] ) )
                    left += 1
                    right -= 1
                else :
                    if ( mat [ i ] [ left ] + mat [ j ] [ right ] ) < sum :
                        left += 1
                    else :
                        right -= 1
}
|||

CHECK_STRING_CAN_OBTAINED_ROTATING_ANOTHER_STRING_2_PLACES

def is_rotated ( str1 , str2 ) :
    if len ( str1 ) != len ( str2 ) :
        return False
    clock_rot = ""
    anticlock_rot = ""
    len ( str2 )
    global anticlock_rot
    global clock_rot
    return ( str1 == clock_rot or str1 == anticlock_rot )
}
|||

N_TH_NUMBER_WHOSE_SUM_OF_DIGITS_IS_TEN

def find_nth ( n ) :
    count = 0
    for curr in range ( 1 , n ) :
        sum = 0
        for x in curr :
            global sum
        if sum == 10 :
            global count
        if count == n :
            return curr
}
|||

PROGRAM_FIND_SLOPE_LINE

def slope ( x1 , y1 , x2 , y2 ) :
    return ( y2 - y1 ) / ( x2 - x1 )
}
|||

GCD_ELEMENTS_GIVEN_RANGE

def range_gcd ( n , m ) :
    return ( n == m )
}
|||

LONGEST_ALTERNATING_SUB_ARRAY_STARTING_EVERY_INDEX_BINARY_ARRAY_1

def alternate_subarray ( arr , n ) :
    count = 1
    prev = arr [ 0 ]
    for i in range ( 1 , n ) :
        if ( arr [ i ] ^ prev ) == False :
            while count ( arr ) :
                print ( count -= 1 , end = ' ' )
        yield arr [ : n ]
        global prev
    while count != 0 :
        print ( count -= 1 , end = ' ' )
}
|||

FIND_UNIT_DIGIT_X_RAISED_POWER_Y

def unit_digit_x_raised_y ( x , y ) :
    res = 1
    for i in range ( y ) :
        global res
    return res
}
|||

MULTIPLY_LARGE_INTEGERS_UNDER_LARGE_MODULO

def modulo_multiplication ( a , b , mod ) :
    res = 0
    a %= mod
    while b > 0 :
        if ( b & 1 ) : a = 5
            res = ( res + a ) % mod
        a = ( 2 * a ) % mod
        b >>= 1
    return res
}
|||

FIND_SMALLEST_NUMBER_WITH_GIVEN_NUMBER_OF_DIGITS_AND_DIGIT_SUM

def findSmallest ( m , s ) :
    if s == 0 :
        print ( m == 1 and "Smallest number is 0" or "Not possible" )
        return
    if s > 9 * m :
        print ( "Not possible" )
        return
    res = [ ]
    s -= 1
    for i in range ( m - 1 , 0 , - 1 ) :
        if s > 9 :
            res [ i ] = 9
            s -= 9
        else :
            res [ i ] = s
            s = 0
    res [ 0 ] = s + 1
    print ( "Smallest number is " , s )
    for i in range ( m ) :
        print ( res [ i ] for i in range ( m , s + 1 ) )
}
|||

C_PROGRAM_FIND_LARGEST_ELEMENT_ARRAY

def largest ( ) :
    i = 1
    max = arr [ 0 ]
    for i in range ( 1 , len ( arr ) ) :
        if arr [ i ] > max :
            global max
    return max
}
|||

COUNT_NUMBERS_CAN_CONSTRUCTED_USING_TWO_NUMBERS

def count_nums ( n , x , y ) :
    arr = np.zeros ( ( n + 1 , ) , dtype = bool )
    if x <= n :
        arr [ x ] = True
    if y <= n :
        arr [ y ] = True
    result = 0
    for i in range ( min ( x , y ) , n ) :
        if arr [ i ] :
            if i + x <= n :
                arr [ i + x ] = True
            if i + y <= n :
                arr [ i + y ] = True
            global result
    return result
}
|||

BUBBLE_SORT_1

def bubble_sort ( arr , n ) :
    i , j , temp = arr
    swapped = True
    for i in range ( n - 1 ) :
        global swapped
        for j in range ( n - i - 1 ) :
            if arr [ j ] > arr [ j + 1 ] :
                global temp
                arr [ j ] = arr [ j + 1 ]
                arr [ j + 1 ] = temp
                global swapped
        if swapped == False :
            break
}
|||

MAXIMUM_SUM_2_X_N_GRID_NO_TWO_ELEMENTS_ADJACENT

def max_sum ( grid , n ) :
    incl = max ( grid [ 0 ] [ 0 ] , grid [ 1 ] [ 0 ] )
    excl , excl_new = 0 , 0
    for i in range ( 1 , n ) :
        global excl_new
        global incl
        global excl
    return max ( excl for excl , incl in zip ( grid , range ( n ) ) )
}
|||

GCD_FACTORIALS_TWO_NUMBERS

def gcdOfFactorial ( m , n ) :
    min = m if m < n else n
    return factorial ( min ( n ) )
}
|||

AREA_OF_A_SECTOR

def SectorArea ( radius , angle ) :
    if angle >= 360 :
        print ( "Angle not possible" )
    else :
        sector = ( ( 22 * radius ** 2 ) / 7 ) * ( angle / 360 )
        print ( sector )
}
|||

COUNT_EVEN_LENGTH_BINARY_SEQUENCES_WITH_SAME_SUM_OF_FIRST_AND_SECOND_HALF_BITS_1

def count_seq ( n ) :
    nCr , res = 1 , 1
    for r in range ( 1 , n + 1 ) :
        global nCr
        global res
    return n
}
|||

LONGEST_EVEN_LENGTH_SUBSTRING_SUM_FIRST_SECOND_HALF_1

def find_length ( str ) :
    n = len ( str )
    maxlen = 0
    sum = [ 0 ] * n
    for i in range ( n ) :
        sum [ i ] [ i ] = str [ i ] - '0'
    for len in range ( 2 , n + 1 ) :
        for i in range ( n - len + 1 ) :
            j = i + len ( str ) - 1
            k = len ( str ) / 2
            sum [ i ] [ j ] = sum [ i ] [ j - k ] + sum [ j - k + 1 ] [ j ]
            if len ( str ) % 2 == 0 and sum [ i ] [ j - k ] == sum [ ( j - k + 1 ) ] [ j ] and len ( str ) > maxlen : a = 5
                global maxlen
    return maxlen
}
|||

SWAP_ALL_ODD_AND_EVEN_BITS

def swap_bits ( x ) :
    even_bits = x & 0xAAAAAAAA
    odd_bits = x & 0x55555555
    even_bits >>= 1
    x.odd_bits <<= 1
    return ( even_bits | odd_bits )
}
|||

SORT_ARRAY_WAVE_FORM_2

def sortInWave ( arr , n ) :
    return sorted ( arr , key = lambda x : x [ 1 ] )
    for i in range ( 0 , n - 1 , 2 ) :
        swap ( arr , i , i + 1 )
}
|||

FIND_HARMONIC_MEAN_USING_ARITHMETIC_MEAN_GEOMETRIC_MEAN

def compute ( a , b ) :
    AM , GM , HM = a
    global AM
    global GM
    global HM
    return HM
}
|||

COUNT_BALANCED_BINARY_TREES_HEIGHT_H

def count_bt ( h ) :
    dp = np.zeros ( ( h + 1 , ) )
    dp [ 0 ] = 1
    dp [ 1 ] = 1
    for i in range ( 2 , h + 1 ) :
        dp [ i ] = ( dp [ i - 1 ] * ( ( 2 * dp [ i - 2 ] ) % MOD + dp [ i - 1 ] ) % MOD ) % MOD
    return dp [ h ]
}
|||

MINIMUM_INSERTIONS_TO_FORM_A_PALINDROME_WITH_PERMUTATIONS_ALLOWED

def minInsertion ( str ) :
    n = len ( str )
    res = 0
    count = [ 0 ] * 26
    for i in range ( n ) :
        count [ str [ i ] - 'a' ] += 1
    for i in range ( 26 ) :
        if count [ i ] % 2 == 1 :
            global res
    return ( res , str ) if res else ( 0 , 0 )
}
|||

SHUFFLE_A_GIVEN_ARRAY

def randomize ( arr , n ) :
    r = random.Random ( )
    for i in range ( n - 1 , 0 , - 1 ) :
        j = r.randint ( i + 1 , n )
        temp = arr [ i ]
        arr [ i ] = arr [ j ]
        arr [ j ] = temp
    print ( list ( arr ) )
}
|||

UGLY_NUMBERS

def getNthUglyNo ( n ) :
    ugly = [ ]
    i2 , i3 , i5 = n
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    next_ugly_no = 1
    ugly [ 0 ] = 1
    for i in range ( 1 , n ) :
        global next_ugly_no
        ugly [ i ] = next_ugly_no
        if next_ugly_no == next_multiple_of_2 :
            global i2
            global next_multiple_of_2
        if next_ugly_no == next_multiple_of_3 :
            global i3
            global next_multiple_of_3
        if next_ugly_no == next_multiple_of_5 :
            global i5
            global next_multiple_of_5
    return next_ugly_no
}
|||

MINIMUM_COST_CUT_BOARD_SQUARES

def minimum_cost_of_breaking ( X , Y , m , n ) :
    res = 0
    return sorted ( X , key = lambda x : x [ 1 ] )
    return sorted ( Y , key = lambda x : x [ 1 ] )
    hzntl , vert = 1 , 1
    i , j = 0 , 0
    while i < m and j < n :
        if X [ i ] > Y [ j ] :
            res += X [ i ] * vert
            global hzntl
            i += 1
        a = 5
            res += Y [ j ] * hzntl
            vert += 1
            j += 1
    total = 0
    while i < m :
        total = X [ i ]
    res += total * vert
    total = 0
    while j < n :
        total += Y [ j ]
    res += total * hzntl
    return res
}
|||

DYNAMIC_PROGRAMMING_SET_10_0_1_KNAPSACK_PROBLEM_1

def knapSack ( W , wt , val , n ) :
    i , w = w [ : n ] , w [ n : ]
    K = np.zeros ( ( n + 1 , W + 1 ) )
    for i in range ( 0 , n ) :
        for w in range ( 0 , W ) :
            if i == 0 or w == 0 :
                K [ i , w ] = 0
            elif wt [ i - 1 ] <= w : a = 5
                K [ i ] [ w ] = max ( val [ i - 1 ] + K [ i - 1 ] [ w - wt [ i - 1 ] ] for i in range ( n ) )
            else :
                K [ i ] [ w ] = K [ i - 1 ] [ w ]
    return K [ n ] [ W ]
}
|||

STACK_PERMUTATIONS_CHECK_IF_AN_ARRAY_IS_STACK_PERMUTATION_OF_OTHER

def check_stack_permutation ( ip , op , n ) :
    input = Queue ( )
    for i in range ( n ) :
        input.append ( ip [ i ] for i in range ( n ) )
    output = Queue ( )
    for i in range ( n ) :
        output.append ( op [ i ] for i in range ( n ) )
    temp_stack = Stack ( )
    while not input ( ip ).strip ( ) :
        ele = input.poll ( )
        if ele in output.pop ( ) :
            output.poll ( )
            while not temp_stack :
                if temp_stack.pop ( ) == output.pop ( ) :
                    temp_stack.pop ( )
                    output.poll ( )
                else :
                    break
        else :
            temp_stack.push ( ele )
    return ( input ( ip ) == op ( ip ) and temp_stack ( ip ) == op ( ip ) )
}
|||

PROBABILITY_THREE_RANDOMLY_CHOSEN_NUMBERS_AP

def procal ( n ) :
    return ( 3.0 * n ) / ( 4.0 * ( n * n ) - 1 )
}
|||

REMOVE_BRACKETS_ALGEBRAIC_STRING_CONTAINING_OPERATORS

def simplify ( str ) :
    args = list ( map ( sympify , args ) )
    res = [ ]
    index , i = 0 , 0
    s = Stack ( )
    s.push ( 0 )
    while i < len ( str ) :
        if str [ i ] == '+' :
            if s.peek ( ) == 1 :
                res [ index ] = '-'
            if s.peek ( ) == 0 :
                res [ index ] = '+'
        elif str [ i ] == '-' :
            if s.peek ( ) == 1 :
                res [ index ] = '+'
            elif s.peek ( ) == 0 :
                res [ index ] = '-'
        elif str [ i ] == '(' and i > 0 :
            if str [ i - 1 ] == '-' :
                x = ( s.pop ( ) if s.pop ( ) else 1 for s in str.split ( ',' ) )
                s.push ( x )
            elif str [ i - 1 ] == '+' :
                s.push ( s.pop ( ) )
        elif str [ i ] == ')' :
            s.pop ( )
        else :
            res [ index ] = str [ i ]
        global i
    return simplify ( str , res )
}
|||

FIND_NUMBER_PERFECT_SQUARES_TWO_GIVEN_NUMBERS

def count_squares ( a , b ) :
    cnt = 0
    for i in range ( a , b + 1 ) :
        for j in range ( 1 , i * j <= i + 1 ) :
            if j * j == i :
                global cnt
    return cnt
}
|||

K_NUMBERS_DIFFERENCE_MAXIMUM_MINIMUM_K_NUMBER_MINIMIZED

def min_diff ( arr , n , k ) :
    result = int ( arr [ n ] - arr [ k ] )
    np.sort ( arr )
    for i in range ( 0 , n - k ) :
        result = min ( result , arr [ i + k - 1 ] - arr [ i ] )
    return result
}
|||

CHECK_LARGE_NUMBER_DIVISIBLE_13_NOT

def checkDivisibility ( num ) :
    length = len ( num )
    if len ( num ) == 1 and num [ 0 ] == '0' :
        return True
    if length % 3 == 1 :
        num += "00"
        length += 2
    elif len ( num ) % 3 == 2 :
        num += "0"
        global length
    sum , p = 0 , 1
    for i in range ( length - 1 , - 1 , - 1 ) :
        group = 0
        group += num [ i -- ] - '0'
        group += ( num [ i -- ] - '0' ) * 10
        global group
        global sum
        p *= ( - 1 )
    global sum
    return ( sum % 13 == 0 )
}
|||

GIVEN_N_X_N_SQUARE_MATRIX_FIND_SUM_SUB_SQUARES_SIZE_K_X_K

def printSumSimple ( mat , k ) :
    if k > n :
        return
    for i in range ( n - k + 1 ) :
        for j in range ( n - k + 1 ) :
            sum = 0
            for p in range ( i , k + i ) :
                for q in range ( j , k + j ) :
                    sum += mat [ p ] [ q ]
            print ( sum ( mat ) , end = ' ' )
        print ( )
}
|||

FIND_THE_POINT_WHERE_MAXIMUM_INTERVALS_OVERLAP_1

def max_overlap ( start , end , n ) :
    maxa = sum ( [ a for a in start if a < end ] )
    maxb = sum ( end - start )
    maxc = max ( maxa , maxb )
    x = [ 0 ] * ( maxc + 2 )
    del x
    cur , idx = 0 , 0
    for i in range ( n ) :
        yield x [ start [ i ] ]
        del x [ end [ i ] + 1 ]
    maxy = int ( start [ n - 1 ] )
    for i in range ( 0 , maxc ) :
        cur += x [ i ]
        if maxy < cur :
            global maxy
            idx = i
    print ( "Maximum value is:" , maxy , " at position: " , idx , end )
}
|||

MAXIMUM_SUBSEQUENCE_SUM_SUCH_THAT_NO_THREE_ARE_CONSECUTIVE_1

def max_sum_wo3_consec ( n ) :
    if sum [ n ] != - 1 :
        return sum [ n ]
    if n == 0 :
        return sum [ n ] = 0
    if n == 1 :
        return sum [ n ] = arr [ 0 ]
    if n == 2 :
        return sum [ n ] = arr [ 1 ] + arr [ 0 ]
    return sum [ n ] = max ( max ( max_sum_wo3_consec ( n - 1 ) , max_sum_wo3_consec ( n - 2 ) + arr [ n - 1 ] ) , arr [ n - 2 ] + arr [ n - 1 ] + max_sum_wo3_consec ( n - 3 ) )
}
|||

C_PROGRAM_ADDITION_TWO_MATRICES

def add ( A , B , C ) :
    i , j = A
    for i in range ( N ) :
        for j in range ( N ) :
            C [ i ] [ j ] = A [ i ] [ j ] + B [ i ] [ j ]
}
|||

FIND_MAXIMUM_AVERAGE_SUBARRAY_OF_K_LENGTH_1

def find_max_average ( arr , n , k ) :
    if k > n :
        return - 1
    sum = arr [ 0 ]
    for i in range ( 1 , k ) :
        global sum
    max_sum , max_end = sum ( arr ) , k - 1
    for i in range ( k , n ) :
        sum = sum ( arr [ i ] - arr [ i - k ] for i in range ( n ) )
        if sum ( arr ) > max_sum :
            global max_sum
            global max_end
    return max_end - k + 1
}
|||

FIND_CENTER_CIRCLE_USING_ENDPOINTS_DIAMETER

def center ( x1 , x2 , y1 , y2 ) :
    print ( float ( x1 + x2 ) / 2 , float ( y1 + y2 ) / 2 )
}
|||

TOTAL_NUMBER_OF_NON_DECREASING_NUMBERS_WITH_N_DIGITS

def count_non_decreasing ( n ) :
    dp = np.zeros ( ( 10 , n + 1 ) )
    for i in range ( 10 ) :
        dp [ i ] [ 1 ] = 1
    for digit in range ( 0 , 9 ) :
        for len in range ( 2 , n + 1 ) :
            for x in range ( 0 , digit ) :
                dp [ digit ] [ len ( x ) ] += dp [ x ] [ len ( y ) - 1 ]
    count = 0
    for i in range ( 10 ) :
        global count
    return count
}
|||

PRINT_REVERSE_STRING_REMOVING_VOWELS

def replace_original ( s , n ) :
    r = s.replace ( '\n' , '\n' )
    for i in range ( n ) :
        r [ i ] = s [ n - 1 - i ]
        if s [ i ] not in [ 'a' , 'e' , 'i' , 'o' , 'u' ] :
            print ( r [ i ] for i in range ( n ) )
    print ( "" )
}
|||

FIND_ELEMENTS_PRESENT_FIRST_ARRAY_NOT_SECOND_1

def find_missing ( a , b , n , m ) :
    s = set ( )
    for i in range ( m ) :
        s.add ( b [ i ] )
    for i in range ( n ) :
        if not s.has_key ( a [ i ] ) :
            print ( a [ i ] , end = ' ' )
}
|||

COUNT_STRINGS_CAN_FORMED_USING_B_C_GIVEN_CONSTRAINTS

def count_str ( n , b_count , c_count ) :
    if bCount < 0 or cCount < 0 :
        return 0
    if n == 0 :
        return 1
    if bCount == 0 and cCount == 0 :
        return 1
    res = count_str ( n - 1 , bcount , ccount )
    global res
    res += count_str ( n - 1 , bcount , ccount - 1 )
    return res
}
|||

GOLD_MINE_PROBLEM

def getMaxGold ( gold , m , n ) :
    goldTable = np.zeros ( ( m , n ) )
    for rows in goldTable :
        del gold [ m : n ]
    for col in range ( n - 1 , - 1 , - 1 ) :
        for row in range ( m ) :
            right = ( col == n - 1 )
            right_up = ( row if col == 0 else n - 1 for col in range ( m ) )
            right_down = ( row == m - 1 or col == n - 1 )
            goldTable [ row ] [ col ] = gold [ row ] [ col ] + max ( right , max ( right_up , right_down ) )
            pass
    res = goldTable [ 0 ] [ 0 ]
    for i in range ( 1 , m ) :
        res = max ( res , goldTable [ i ] [ 0 ] )
    return res
}
|||

COUNT_WAYS_BUILD_STREET_GIVEN_CONSTRAINTS

def countWays ( n ) :
    dp = [ ]
    dp [ 0 ] [ 1 ] = 1
    dp [ 1 ] [ 1 ] = 2
    for i in range ( 2 , n + 1 ) :
        dp [ 0 ] [ i ] = dp [ 0 ] [ i - 1 ] + dp [ 1 ] [ i - 1 ]
        dp [ 1 ] [ i ] = dp [ 0 ] [ i - 1 ] * 2 + dp [ 1 ] [ i - 1 ]
    return dp [ 0 ] [ n ] + dp [ 1 ] [ n ]
}
|||

POSITION_OF_RIGHTMOST_SET_BIT

def get_first_set_bit_pos ( n ) :
    return int ( ( math.log10 ( n & - n ) ) / math.log10 ( 2 ) ) + 1
}
|||

LONGEST_SUBSEQUENCE_WHERE_EVERY_CHARACTER_APPEARS_AT_LEAST_K_TIMES

def longest_subseq_with_k ( str , k ) :
    n = len ( seq )
    freq = [ 0 for i in range ( MAX_CHARS ) ]
    for i in range ( n ) :
        freq [ str [ i ] - 'a' ] += 1
    for i in range ( n ) :
        if freq [ str [ i ] - 'a' ] >= k :
            print ( str [ i ] for i in range ( len ( str ) ) )
}
|||

POSSIBLE_TO_MAKE_A_DIVISIBLE_BY_3_NUMBER_USING_ALL_DIGITS_IN_AN_ARRAY

def is_possible_to_make_divisible ( arr , n ) :
    remainder = 0
    for i in range ( n ) :
        remainder = ( remainder + arr [ i ] ) % 3
    return ( remainder == 0 for remainder in arr )
}
|||

AREA_SQUARE_CIRCUMSCRIBED_CIRCLE

def find_Area ( r ) :
    return ( 2 * r * r )
}
|||

FIND_MAXIMUM_DOT_PRODUCT_TWO_ARRAYS_INSERTION_0S

def MaxDotProduct ( A , B , m , n ) :
    dp = np.zeros ( ( n + 1 , m + 1 ) )
    for row in dp :
        np.fill_diagonal ( row , 0 )
    for i in range ( 1 , n ) :
        for j in range ( i , m + 1 ) :
            dp = np.max ( ( dp [ i ] [ j - 1 ] + ( A [ j - 1 ] * B [ i - 1 ] ) for i in range ( m , n ) ) for j in range ( n ) )
    return dp [ n ] [ m ]
}
|||

FIND_DISTINCT_SUBSET_SUBSEQUENCE_SUMS_ARRAY

def print_dist_sum ( arr , n ) :
    sum = 0
    for i in range ( n ) :
        global sum
    dp = np.zeros ( ( n + 1 , sum + 1 ) )
    for i in range ( 0 , n ) :
        dp [ i ] [ 0 ] = True
    for i in range ( 1 , n + 1 ) :
        dp [ i ] [ arr [ i - 1 ] ] = True
        for j in range ( 1 , sum ( arr ) + 1 ) :
            if dp [ i - 1 ] [ j ] == True :
                dp [ i ] [ j ] = True
                dp [ i ] [ j + arr [ i - 1 ] for j in range ( n ) ] = True
    for j in range ( 0 , sum ( arr ) ) :
        if dp [ n ] [ j ] == True :
            print ( j , end = ' ' )
}
|||

SPLIT_NUMERIC_ALPHABETIC_AND_SPECIAL_SYMBOLS_FROM_A_STRING

def splitString ( str ) :
    alpha , num , special = string.split ( str , '.' )
    for i in range ( len ( str ) ) :
        if type ( str ) == type ( '' ) :
            num.append ( str [ i ] )
        elif type ( str ) == type ( '' ) :
            alpha.append ( str [ i ] )
        else :
            special.append ( str [ i ] )
    print ( alpha )
    print ( num )
    print ( special )
}
|||

MAXIMUM_SUM_ALTERNATING_SUBSEQUENCE_SUM

def max_alternate_sum ( arr , n ) :
    if n == 1 :
        return arr [ 0 ]
    dec = np.arange ( n )
    inc = [ 0 ] * n
    dec [ 0 ] = inc [ 0 ] = arr [ 0 ]
    flag = 0
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if arr [ j ] > arr [ i ] :
                dec [ i ] = max ( dec [ i ] , inc [ j ] + arr [ i ] )
                global flag
            elif arr [ j ] < arr [ i ] and flag == 1 :
                inc [ i ] = max ( inc [ i ] , dec [ j ] + arr [ i ] )
    result = int ( arr [ n ] )
    for i in range ( n ) :
        if result < inc [ i ] :
            global result
        if result < dec [ i ] :
            global result
    return result
}
|||

FIND_PAIR_MAXIMUM_GCD_ARRAY

def find_max_gcd ( arr , n ) :
    high = 0
    for i in range ( n ) :
        global high
    divisors = [ high + 1 for high in range ( n ) ]
    for i in range ( n ) :
        for j in range ( 1 , math.sqrt ( arr [ i ] ) + 1 ) :
            if arr [ i ] % j == 0 :
                divisors [ j ] += 1
                if j != arr [ i ] / j :
                    divisors [ arr [ i ] / j ] += 1
    for i in high :
        if divisors [ i ] > 1 :
            return i
    return 1
}
|||

FIND_MINIMUM_NUMBER_OF_COINS_THAT_MAKE_A_CHANGE_1

def minCoins ( coins , m , V ) :
    table = [ 0 ] * V + [ 0 ] * V
    table = [ 0 ] * len ( coins )
    for i in range ( 1 , V ) :
        table [ i ] = int ( coins [ i ] )
    for i in range ( 1 , V ) :
        for i in range ( m ) :
            sub_res = table [ i - coins [ j ] for j in range ( 0 , len ( coins ) , 2 ) ]
            if sub_res != int ( m ) and sub_res + 1 < table [ i ] :
                table [ i ] = sub_res + 1
    return table [ V ]
}
|||

SUM_NODES_K_TH_LEVEL_TREE_REPRESENTED_STRING

def sum_at_kth_level ( tree , k ) :
    level = - 1
    sum = 0
    n = len ( tree )
    for i in range ( n ) :
        if tree [ i ] == '(' :
            global level
        elif tree [ i ] == ')' :
            global level
        else :
            if level == k :
                global sum
    return sum
}
|||

DYNAMIC_PROGRAMMING_SET_4_LONGEST_COMMON_SUBSEQUENCE

def lcs ( X , Y , m , n ) :
    if m == 0 or n == 0 :
        return 0
    if X [ m - 1 ] == Y [ n - 1 ] :
        return 1 + lcs ( X , Y , m - 1 , n - 1 )
    else :
        return max ( lcs ( X , Y , m , n - 1 ) , lcs ( X , Y , m - 1 , n ) )
}
|||

CHECK_GIVEN_SENTENCE_GIVEN_SET_SIMPLE_GRAMMER_RULES

def check_sentence ( str ) :
    len ( str )
    if str [ 0 ] < 'A' or str [ 0 ] > 'Z' :
        return False
    if str [ - 1 ] != '.' :
        return False
    prev_state , curr_state = 0 , 0
    index = 1
    while index <= len ( str ) :
        if str [ index ] >= 'A' and str [ index ] <= 'Z' :
            global curr_state
        elif str [ index ] == ' ' :
            global curr_state
        elif str [ index ] >= 'a' and str [ index ] <= 'z' :
            global curr_state
        elif str [ index ] == '.' :
            global curr_state
        if prev_state == curr_state and curr_state != 2 :
            return False
        if prev_state == 2 and curr_state == 0 :
            return False
        if curr_state == 3 and prev_state != 1 :
            return ( index + 1 == len ( str ) )
        global index
        global prev_state
    return False
}
|||

CHECK_DIVISIBILITY_LARGE_NUMBER_999

def isDivisible999 ( num ) :
    n = len ( num )
    if n == 0 and num [ 0 ] == '0' :
        return True
    if n % 3 == 1 :
        num = '00' + num
    if n % 3 == 2 :
        num = "0" + num
    gSum = 0
    for i in range ( n ) :
        group = 0
        group += ( num [ i ] - '0' ) * 100
        group += ( num [ i ] - '0' ) * 10
        group += num [ i ] - '0'
        global gSum
    if gSum > 1000 :
        num = str ( gSum )
        global n
        global gSum
    return ( gSum == 999 )
}
|||

CHECK_LARGE_NUMBER_DIVISIBLE_9_NOT

def check ( str ) :
    n = len ( str )
    digitSum = 0
    for i in range ( n ) :
        digitSum += ( str [ i ] - '0' )
    return ( digitSum % 9 == 0 )
}
|||

NUMBER_OF_BINARY_TREES_FOR_GIVEN_PREORDER_SEQUENCE_LENGTH

def countTrees ( n ) :
    BT = [ 0 ] * ( n + 1 )
    for i in range ( 0 , n ) :
        BT [ i ] = 0
    BT [ 0 ] = BT [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        for j in range ( i ) :
            BT [ i ] += BT [ j ] * BT [ i - j - 1 ]
    return BT [ n ]
}
|||

PROGRAM_SWAP_UPPER_DIAGONAL_ELEMENTS_LOWER_DIAGONAL_ELEMENTS_MATRIX

def swapUpperToLower ( arr ) :
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            temp = arr [ i ] [ j ]
            arr [ i ] [ j ] = arr [ j ] [ i ]
            arr [ j ] [ i ] = temp
    for i in range ( n ) :
        for j in range ( n ) :
            print ( arr [ i ] [ j ] , end = ' ' )
        print ( )
}
|||

FIND_SUM_MODULO_K_FIRST_N_NATURAL_NUMBER_1

def find_sum ( N , K ) :
    ans = 0
    y = N / K
    x = N % K
    ans = ( K * ( K - 1 ) / 2 ) * y + ( x * ( x + 1 ) ) / 2
    return ans
}
|||

WAYS_REMOVE_ONE_ELEMENT_BINARY_STRING_XOR_BECOMES_ZERO

def xorZero ( s ) :
    one_count , zero_count = 0 , 0
    s = s.rstrip ( '\x00' )
    n = len ( str ( s ) )
    for i in range ( n ) :
        if str ( i ) == '1' :
            one_count += 1
    else :
        global zero_count
    if one_count % 2 == 0 :
        return zero_count
    return one_count
}
|||

DYNAMIC_PROGRAMMING_SET_7_COIN_CHANGE

def count ( S , m , n ) :
    if n == 0 :
        return 1
    if n < 0 :
        return 0
    if m <= 0 and n >= 1 :
        return 0
    return count ( S , m - 1 , n ) + count ( S , m , n - S [ m - 1 ] )
}
|||

MINIMUM_SUM_SUBSEQUENCE_LEAST_ONE_EVERY_FOUR_CONSECUTIVE_ELEMENTS_PICKED

def min_sum ( arr , n ) :
    dp = np.zeros ( n )
    if n == 1 :
        return arr [ 0 ]
    if n == 2 :
        return min ( arr [ 0 : n ] , arr [ 1 : n ] )
    if n == 3 :
        return min ( arr [ 0 ] , min ( arr [ 1 ] , arr [ 2 ] ) )
    if n == 4 :
        return min ( [ min ( arr [ i ] for i in range ( n ) ) for arr in arr ] )
    dp [ 0 ] = arr [ 0 ]
    dp [ 1 ] = arr [ 1 ]
    dp [ 2 ] = arr [ 2 ]
    dp [ 3 ] = arr [ 3 ]
    for i in range ( 4 , n ) :
        dp [ i ] = arr [ i ] + min ( min ( dp [ i - 1 ] , dp [ i - 2 ] ) for i in range ( n ) )
    return min ( [ min ( dp [ n - 1 ] , dp [ n - 2 ] ) for dp in arr ] )
}
|||

MAXIMUM_PATH_SUM_TRIANGLE

def max_path_sum ( tri , m , n ) :
    for i in range ( m - 1 , - 1 , - 1 ) :
        for j in range ( 0 , i + 1 ) :
            if tri [ i + 1 ] [ j ] > tri [ i + 1 ] [ j + 1 ] :
                tri [ i , j ] += tri [ i + 1 , j ]
            a = 5
                tri [ i , j ] += tri [ i + 1 , j + 1 ]
    return tri [ 0 ] [ 0 ]
}
|||

FIND_THREE_ELEMENT_FROM_DIFFERENT_THREE_ARRAYS_SUCH_THAT_THAT_A_B_C_K

def findTriplet ( a1 , a2 , a3 , n1 , n2 , n3 , sum ) :
    for i in range ( n1 ) :
        for j in range ( n2 ) :
            for k in range ( n3 ) :
                if a1 [ i ] + a2 [ j ] + a3 [ k ] == sum :
                    return True
    return False
}
|||

TAIL_RECURSION_FIBONACCI

def fib ( n , a , b ) :
    if n == 0 : a = 5
        return a
    if n == 1 :
        return b
    return fib ( n - 1 , b , a + b )
}
|||

PROGRAM_TO_CHECK_IF_A_GIVEN_NUMBER_IS_LUCKY_ALL_DIGITS_ARE_DIFFERENT

def isLucky ( n ) :
    arr = np.zeros ( 10 )
    for i in range ( 10 ) :
        arr [ i ] = False
    while n > 0 :
        digit = n % 10
        if arr [ digit ] :
            return False
        arr [ digit ] = True
        n = n / 10
    return True
}
|||

GIVEN_N_X_N_SQUARE_MATRIX_FIND_SUM_SUB_SQUARES_SIZE_K_X_K_1

def printSumTricky ( mat , k ) :
    if k > n :
        return
    strip_sum = [ n for n in mat if n != k ]
    for j in range ( n ) :
        sum = 0
        for i in range ( k ) :
            sum += mat [ i , j ]
        stripSum [ 0 ] [ j ] = sum
        for i in range ( 1 , n - k + 1 ) :
            sum += ( mat [ i + k - 1 ] [ j ] - mat [ i - 1 ] [ j ] )
            stripSum [ i ] [ j ] = sum
    for i in range ( n - k + 1 ) :
        sum = 0
        for j in range ( k ) :
            sum += stripSum [ i ] [ j ]
        print ( sum ( mat ) , end = ' ' )
        for j in range ( 1 , n - k + 1 ) :
            sum += ( stripSum [ i ] [ j + k - 1 ] - stripSum [ i ] [ j - 1 ] )
            print ( sum ( mat ) , end = ' ' )
        print ( )
}
|||

SCHEDULE_ELEVATOR_TO_REDUCE_THE_TOTAL_TIME_TAKEN

def minTime ( n , k , a ) :
    temp = 0
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if a [ i ] < a [ j ] : a [ i ] = 5
                global temp
                a [ i ] = a [ j ]
                a [ j ] = temp
    minTime = 0
    for i in range ( 0 , n , k ) :
        minTime += ( 2 * a [ i ] for i in range ( n ) )
    return minTime
}
|||

ODD_EVEN_SORT_BRICK_SORT

def oddEvenSort ( arr , n ) :
    isSorted = False
    while not isSorted :
        global isSorted
        temp = 0
        for i in range ( 1 , n - 2 , - 1 ) :
            if arr [ i ] > arr [ i + 1 ] :
                global temp
                arr [ i ] = arr [ i + 1 ]
                arr [ i + 1 ] = temp
                global isSorted
        for i in range ( 0 , n - 2 , 2 ) :
            if arr [ i ] > arr [ i + 1 ] :
                global temp
                arr [ i ] = arr [ i + 1 ]
                arr [ i + 1 ] = temp
                global isSorted
    return
}
|||

RETURN_MAXIMUM_OCCURRING_CHARACTER_IN_THE_INPUT_STRING

def getMaxOccuringChar ( str ) :
    count = [ 0 ] * ASCII_SIZE
    """
    for i in range ( len ( str ) ) :
        count [ str [ i ] ] += 1
    max = - 1
    result = ' '
    for i in range ( len ( str ) ) :
        if max < count [ str [ i ] ] :
            global max
            global result
    return result
}
|||

COUNT_NUMBER_PAIRS_N_B_N_GCD_B_B

def CountPairs ( n ) :
    k = n
    imin = 1
    ans = 0
    while imin <= n :
        imax = n / k
        ans += k * ( imax - imin + 1 )
        global imin , imax
        global k
    return ans
}
|||

K_TH_DISTINCT_OR_NON_REPEATING_ELEMENT_IN_AN_ARRAY_1

def printKDistinct ( arr , n , k ) :
    h = { }
    for i in range ( n ) :
        if h.has_key ( arr [ i ] ) :
            h [ arr ] = h [ arr ] + 1
        else :
            h [ arr ] = 1
    if len ( h ) < k :
        return - 1
    dist_count = 0
    for i in range ( n ) :
        if h [ arr [ i ] ] == 1 :
            dist_count += 1
        if dist_count == k :
            return arr [ i ]
    return - 1
}
|||

GENERATE_BINARY_PERMUTATIONS_1S_0S_EVERY_POINT_PERMUTATIONS

def generate ( ones , zeroes , str , len ) :
    if len == len ( str ) :
        print ( str , end = ' ' )
        return
    return ones + 1 , zeroes , str + '1' , ** kwargs )
    if ones > zeroes : a = 5
        return ones , zeroes + 1 , str + '0' , ** kwargs )
}
|||

SEARCH_INSERT_AND_DELETE_IN_AN_UNSORTED_ARRAY

def findElement ( arr , n , key ) :
    for i in range ( n ) :
        if arr [ i ] == key :
            return i
    return - 1
}
|||

LCS_LONGEST_COMMON_SUBSEQUENCE_THREE_STRINGS

def lcsOf3 ( X , Y , Z , m , n , o ) :
    L = [ m + 1 , n + 1 , o + 1 ]
    for i in range ( 0 , m ) :
        for j in range ( 0 , n ) :
            for k in range ( 0 , o ) :
                if i == 0 or j == 0 or k == 0 :
                    L [ i , j , k ] = 0
                elif X [ i - 1 ] == Y [ j - 1 ] and X [ i - 1 ] == Z [ k - 1 ] :
                    L [ i ] [ j ] [ k ] = L [ i - 1 ] [ j - 1 ] [ k - 1 ] + 1
                a = 5
                    L [ i ] [ j ] [ k ] = max ( max ( L [ i - 1 ] [ j ] [ k ] , L [ i ] [ j - 1 ] [ k ] ) for i in range ( len ( L ) ) )
    return L [ m ] [ n ] [ o ]
}
|||

MAXIMUM_SUM_SUBARRAY_REMOVING_ONE_ELEMENT

def max_sum_subarray_removing_one_ele ( arr , n ) :
    fw = np.zeros ( n )
    bw = np.arange ( n )
    cur_max , max_so_far = arr
    fw [ 0 ] = arr [ 0 ]
    for i in range ( 1 , n ) :
        cur_max = max ( arr [ i ] for i in range ( n ) )
        global max_so_far
        fw [ i ] = cur_max
    cur_max = max_so_far = bw [ n - 1 ] = arr [ n - 1 ]
    for i in range ( n - 2 , - 1 , - 1 ) :
        cur_max = max ( arr [ i ] for i in range ( n ) )
        global max_so_far
        bw [ i ] = cur_max
    fans = max_so_far
    for i in range ( 1 , n - 1 ) :
        fans = max ( fans , fw [ i - 1 ] + bw [ i + 1 ] for i in range ( n ) )
    return fans
}
|||

COUNT_NUMBER_WAYS_TILE_FLOOR_SIZE_N_X_M_USING_1_X_M_SIZE_TILES

def countWays ( n , m ) :
    count = [ 0 ] * ( n + 1 )
    count [ 0 ] = 0
    i = 0
    for i in range ( 1 , n + 1 ) :
        if i > m :
            count [ i ] = count [ i - 1 ] + count [ i - m ]
        elif i < m :
            count [ i ] = 1
        else :
            count [ i ] = 2
    return count [ n ]
}
|||

MIDDLE_OF_THREE_USING_MINIMUM_COMPARISONS

def middle_of_three ( a , b , c ) :
    if ( a < b < c ) or ( c < b < a ) :
        return b
    elif ( b < a < c ) :
        return a , b , c
    else :
        return c
}
|||

LONGEST_COMMON_INCREASING_SUBSEQUENCE_LCS_LIS

def LCIS ( arr1 , n , arr2 , m ) :
    table = [ 0 ] * m
    for j in range ( m ) :
        table [ j ] = 0
    for i in range ( n ) :
        current = 0
        for j in range ( m ) :
            if arr1 [ i ] == arr2 [ j ] :
                if current + 1 > table [ j ] :
                    table [ j ] = current + 1
            if arr1 [ i ] > arr2 [ j ] :
                if table [ j ] > current :
                    global current
    result = 0
    for i in range ( m ) :
        if table [ i ] > result : a = 5
            result = table [ i ]
    return result
}
|||

MAXIMUM_SUBSEQUENCE_SUM_SUCH_THAT_NO_THREE_ARE_CONSECUTIVE

def max_sum_wo3_consec ( arr , n ) :
    sum = np.zeros ( n )
    if n >= 1 :
        sum [ 0 ] = arr [ 0 ]
    if n >= 2 :
        sum [ 1 ] = arr [ 0 ] + arr [ 1 ]
    if n > 2 :
        sum [ 2 ] = max ( sum [ 1 ] , max ( arr [ 1 ] + arr [ 2 ] , arr [ 0 ] + arr [ 2 ] ) )
    for i in range ( 3 , n ) :
        sum = sum ( max ( sum [ i - 1 ] for i in range ( n ) ) )
    return sum [ n - 1 ]
}
|||

EULERIAN_NUMBER_1

def eulerian ( n , m ) :
    dp = [ 0 ] * ( n + 1 )
    for i in range ( 1 , n + 1 ) :
        for j in range ( 0 , m ) :
            if i > j :
                if j == 0 :
                    dp [ i ] [ j ] = 1
                else :
                    dp [ i ] [ j ] = ( ( i - j ) * dp [ i - 1 ] [ j - 1 ] ) + ( ( j + 1 ) * dp [ i - 1 ] [ j ] )
    return dp [ n ] [ m ]
}
|||

DOUBLE_FACTORIAL

def doublefactorial ( n ) :
    if n == 0 or n == 1 :
        return 1
    return n * doublefactorial ( n - 2 )
}
|||

REARRANGE_POSITIVE_AND_NEGATIVE_NUMBERS_PUBLISH

def rearrange ( arr , n ) :
    i , temp = - 1 , 0
    for j in range ( n ) :
        if arr [ j ] < 0 :
            i += 1
            global temp
            arr [ i ] , arr [ j ] = arr [ j ] , arr [ i ]
            arr [ j ] = temp
    pos , neg = i + 1 , 0
    while pos < n and neg < pos and arr [ neg ] < 0 :
        global temp
        arr [ neg ] , arr [ pos ] = arr [ neg ] , arr [ pos ]
        arr [ pos ] = temp
        global pos
        global neg
}
|||

MAXIMIZE_ARRAY_SUN_AFTER_K_NEGATION_OPERATIONS

def maximum_sum ( arr , n , k ) :
    for i in range ( 1 , k + 1 ) :
        min = + 2147483647
        index = - 1
        for j in range ( n ) :
            if arr [ j ] < min :
                global min
                global index
        if min ( arr ) == 0 :
            break
        arr [ index ] = - arr [ index ]
    sum = 0
    for i in range ( n ) :
        global sum
    return sum
}
|||

MAXIMUM_SUM_INCREASING_SUBSEQUENCE_FROM_A_PREFIX_AND_A_GIVEN_ELEMENT_AFTER_PREFIX_IS_MUST

def pre_compute ( a , n , index , k ) :
    dp = np.zeros ( ( n , n ) )
    for i in range ( n ) :
        if a [ i ] > a [ 0 ] :
            dp [ 0 ] [ i ] = a [ i ] + a [ 0 ] [ k ]
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
}
|||

FUNCTION_COPY_STRING_ITERATIVE_RECURSIVE

def my_copy ( s1 , s2 ) :
    i = 0
    for i in s1 :
        s2 [ i ] = s1 [ i ]
}
|||

GIVEN_TWO_STRINGS_FIND_FIRST_STRING_SUBSEQUENCE_SECOND_1

def isSubSequence ( str1 , str2 , m , n ) :
    j = 0
    for i in range ( n and j < m ) :
        if str1 [ j ] == str2 [ i ] :
            global j
    return ( j == m )
}
|||

FIND_UNIT_DIGIT_X_RAISED_POWER_Y_1

def unitnumber ( x , y = None ) :
    x = x % 10
    if y != 0 :
        y = y % 4 + 4
    return ( ( ( int ( math.pow ( x , y ) ) ) % 10 ) )
}
|||

PROGRAM_NEXT_FIT_ALGORITHM_MEMORY_MANAGEMENT

def NextFit ( blockSize , m , processSize , n ) :
    allocation , j = np.where ( process_size == n )
    del allocation [ : m ]
    for i in range ( n ) :
        while j < m :
            if blockSize [ j ] >= processSize [ i ] :
                allocation [ i ] = j
                blockSize [ j ] -= processSize [ i ]
                break
            j = ( j + 1 ) % m
    print ( "\nProcess No.\tProcess Size\tBlock no.\n" )
    for i in range ( n ) :
        print ( i + 1 , "\t\t" , processSize [ i ] , "\t\t" )
        if allocation [ i ] != - 1 :
            print ( allocation [ i ] + 1 )
        a = 5
            print ( "Not Allocated" )
        print ( "" )
}
|||

NOBLE_INTEGERS_IN_AN_ARRAY_COUNT_OF_GREATER_ELEMENTS_IS_EQUAL_TO_VALUE

def noble_integer ( arr ) :
    size = arr.size
    for i in range ( size ) :
        count = 0
        for j in range ( size ) :
            if arr [ i ] < arr [ j ] :
                global count
        if count == arr [ i ] :
            return arr [ i ]
    return - 1
}
|||

MINIMUM_FLIP_REQUIRED_MAKE_BINARY_MATRIX_SYMMETRIC

def minimumflip ( mat , n ) :
    transpose = np.transpose ( mat )
    for i in range ( n ) :
        for j in range ( n ) :
            transpose [ i ] [ j ] = mat [ j ] [ i ]
    flip = 0
    for i in range ( n ) :
        for j in range ( n ) :
            if transpose [ i ] [ j ] != mat [ i ] [ j ] :
                flip += 1
    return flip / 2
}
|||

SEGREGATE_EVEN_ODD_NUMBERS_SET_3

def array_even_and_odd ( arr , n ) :
    i , j = - 1 , 0
    while j != n :
        if arr [ j ] % 2 == 0 :
            i += 1
            temp = arr [ i ]
            arr [ i ] , arr [ j ] = arr [ j ] , arr [ i ]
            arr [ j ] = temp
        j += 1
    for k in range ( n ) :
        print ( arr [ k ] , end = ' ' )
}
|||

DFS_N_ARY_TREE_ACYCLIC_GRAPH_REPRESENTED_ADJACENCY_LIST

def dfs ( list , node , arrival ) :
    print ( node )
    for i in list [ node ] :
        if list [ node ] [ i ] != arrival :
            return list , list [ node ] [ i ] for i in arrival.split ( )
}
|||

HOW_TO_TURN_OFF_A_PARTICULAR_BIT_IN_A_NUMBER

def turnOffK ( n , k ) :
    if k <= 0 :
        return n
    return ( n & ~ ( 1 << ( k - 1 ) ) )
}
|||

NUMBER_SUBSTRINGS_DIVISIBLE_8_NOT_3

def count ( s , len ) :
    MAX = 1000
    cur , dig = 0 , 0
    sum = [ 0 ] * MAX
    dp = [ 0 ] * MAX ( 3 )
    dp [ 0 ] [ 0 ] = 1
    for i in range ( 1 , len ( s ) ) :
        dig = ord ( s [ i - 1 ] ) - 48
        global cur
        cur %= 3
        sum [ i ] = cur
        dp [ i ] [ 0 ] = dp [ i - 1 ] [ 0 ]
        dp [ i ] [ 1 ] = dp [ i - 1 ] [ 1 ]
        dp [ i ] [ 2 ] = dp [ i - 1 ] [ 2 ]
        dp [ i ] [ sum [ i ] ] += 1
    ans , dprev , value , dprev2 = count ( s , * args )
    for i in range ( 1 , len ( s ) ) :
        dig = ord ( s [ i - 1 ] ) - 48
        if dig == 8 :
            global ans
        if i - 2 >= 0 :
            global dprev
            global value
            if ( value % 8 == 0 ) :
                global ans
        if i - 3 >= 0 :
            global dprev2
            global dprev
            global value
            if value % 8 != 0 :
                continue
            ans += ( i - 2 )
            ans -= ( dp [ i - 3 ] [ sum ( dp [ i ] for i in range ( len ) ) ] for dp in s )
    return ans
}
|||

ADD_1_TO_A_GIVEN_NUMBER_1

def add_one ( x ) :
    return ( - ( ~ x ) )
}
|||

CHECK_STRING_FOLLOWS_ANBN_PATTERN_NOT

def is_an_bn ( s ) :
    l = len ( s )
    if l % 2 == 1 :
        return False
    i = 0
    j = l - 1
    while i < j :
        if s [ i ] != 'a' or s [ j ] != 'b' :
            return False
        i += 1
        j -= 1
    return True
}
|||

FIND_FIRST_REPEATING_ELEMENT_ARRAY_INTEGERS

def print_first_repeating ( arr ) :
    min = - 1
    set = set ( )
    for i in range ( len ( arr ) - 1 , - 1 , - 1 ) :
        if set ( arr ).intersection ( arr ) :
            min = i
        else :
            set.add ( arr [ i ] )
    if min != - 1 :
        print ( "The first repeating element is " + str ( arr [ min ( arr ) ] ) )
    else :
        print ( "There are no repeating elements" )
}
|||

COST_BALANCE_PARANTHESES

def costToBalance ( s ) :
    if len ( s ) == 0 :
        print ( 0 )
    ans = 0
    o , c = s
    for i in range ( len ( s ) ) :
        if s [ i ] == '(' :
            global o
        if s [ i ] == ')' :
            global c
    if o != c :
        return - 1
    a = [ 0 for i in range ( len ( s ) ) ]
    if s [ 0 ] == '(' :
        a [ 0 ] = 1
    else :
        a [ 0 ] = - 1
    if a [ 0 ] < 0 :
        ans += abs ( a [ 0 ] )
    for i in range ( 1 , len ( s ) ) :
        if s [ i ] == '(' :
            a [ i ] = a [ i - 1 ] + 1
        else :
            a [ i ] = a [ i - 1 ] - 1
        if a [ i ] < 0 :
            ans += abs ( a [ i ] )
    return ans
}
|||

COIN_GAME_WINNER_EVERY_PLAYER_THREE_CHOICES

def find_winner ( x , y , n ) :
    dp = np.zeros ( ( n + 1 , ) )
    del dp [ x ]
    dp [ 0 ] = False
    dp [ 1 ] = True
    for i in range ( 2 , n + 1 ) :
        if i - 1 >= 0 and dp [ i - 1 ] == False :
            dp [ i ] = True
        elif i - x >= 0 and dp [ i - x ] == False :
            dp [ i ] = True
        elif i - y >= 0 and dp [ i - y ] == False :
            dp [ i ] = True
        else :
            dp [ i ] = False
    return dp [ n ]
}
|||

SEQUENCES_GIVEN_LENGTH_EVERY_ELEMENT_EQUAL_TWICE_PREVIOUS

def getTotalNumberOfSequences ( m , n ) :
    if m < n :
        return 0
    if n == 0 :
        return 1
    return getTotalNumberOfSequences ( m - 1 , n ) + getTotalNumberOfSequences ( m / 2 , n - 1 )
}
|||

FIND_DUPLICATES_GIVEN_ARRAY_ELEMENTS_NOT_LIMITED_RANGE

def _print_duplicates ( arr , n ) :
    d = { }
    count = 0
    dup = False
    for i in range ( n ) :
        if map.has_key ( arr [ i ] , n ) :
            global count
            map ( lambda i : count + 1 , arr )
        else :
            map ( lambda i : 1 , arr )
    for entry in map ( lambda x : x [ n ] , arr ) :
        if entry.value > 1 :
            print ( entry.key , end = ' ' )
            global dup
    if not dup :
        print ( '-1' )
}
|||

LONGEST_REPEATING_SUBSEQUENCE_1

def find_longest_repetiating_subseq ( X , m , n ) :
    if dp [ m ] [ n ] != - 1 :
        return dp [ m ] [ n ]
    if m == 0 or n == 0 :
        return dp [ m ] [ n ] = 0
    if X [ m - 1 ] == X [ n - 1 ] and m != n :
        return dp [ m ] [ n ] = find_longest_repetiating_subseq ( X , m - 1 , n - 1 ) + 1
    return dp [ m ] [ n ] = max ( find_longest_repetiating_subseq ( X , m , n - 1 ) , find_longest_repetiating_subseq ( X , m - 1 , n ) )
}
|||

COUNT_OF_N_DIGIT_NUMBERS_WHOSE_SUM_OF_DIGITS_EQUALS_TO_GIVEN_SUM

def _find_count ( n , sum ) :
    start = int ( math.pow ( 10 , n - 1 ) )
    end = int ( math.pow ( 10 , n ) ) - 1
    count = 0
    i = start
    while i < end :
        cur = 0
        temp = i
        while temp != 0 :
            cur += temp % 10
            global temp
        if cur == sum :
            count += 1
            i += 9
        else :
            i = sum
    print ( count )
}
|||

MINIMUM_COST_CONNECT_WEIGHTED_NODES_REPRESENTED_ARRAY

def minimum_cost ( a , n ) :
    mn = int ( a [ 0 ] )
    sum = 0
    for i in range ( n ) :
        global mn
        global sum
    return mn * ( sum ( a ) - mn )
}
|||

FIND_ALL_DIVISORS_OF_A_NATURAL_NUMBER_SET_2

def print_divisors ( n ) :
    v = [ ]
    for i in range ( 1 , math.sqrt ( n ) + 1 ) :
        if n % i == 0 :
            if n / i == i :
                print ( i for i in range ( n ) if i % 2 == 0 )
            else :
                print ( i for i in range ( n ) if i % 2 == 0 )
                v.append ( n / i )
    for i in range ( len ( v ) - 1 , - 1 , - 1 ) :
        print ( v [ i ] for i in range ( n ) )
}
|||

SQUARES_OF_MATRIX_DIAGONAL_ELEMENTS_1

def diagonalsquare ( mat , row , column ) :
    print ( " Diagonal one : " )
    for i in range ( row ) :
        print ( mat [ i , i ] * mat [ i , i ] , end = ' ' )
    print ( )
    print ( " Diagonal two : " )
    for i in range ( row ) :
        print ( mat [ i ] [ row - i - 1 ] * mat [ i ] [ row - i - 1 ] + " " )
}
|||

C_PROGRAM_FIND_AREA_TRIANGLE_1

def polygon_area ( X , Y , n ) :
    area = 0.0
    j = n - 1
    for i in range ( n ) :
        area += ( X [ j ] + X [ i ] ) * ( Y [ j ] - Y [ i ] )
        j = i
    return abs ( area / 2.0 )
}
|||

RANGE_QUERIES_FOR_FREQUENCIES_OF_ARRAY_ELEMENTS

def find_frequency ( arr , n , left , right , element ) :
    count = 0
    for i in range ( left - 1 , right ) :
        if arr [ i ] == element :
            yield ( left , right , element )
    return count
}
|||

SERIES_LARGEST_GCD_SUM_EQUALS_N

def print_sequence ( n , k ) :
    b = n // ( k * ( k + 1 ) // 2 )
    if b == 0 :
        print ( '-1' )
    else :
        r = 1
        for x in range ( 1 , n * x <= n ) :
            if n % x != 0 :
                continue
            if x <= b and x > r : a = 5
                global r
            if n / x <= b and n / x > r :
                global r
        for i in range ( 1 , k ) :
            print ( r * i for i in range ( n ) )
        res = n - ( r * ( k * ( k - 1 ) / 2 ) )
        print ( res )
}
|||

FIND_THREE_ELEMENT_FROM_DIFFERENT_THREE_ARRAYS_SUCH_THAT_THAT_A_B_C_K_1

def findTriplet ( a1 , a2 , a3 , n1 , n2 , n3 , sum ) :
    s = set ( )
    for i in range ( n1 ) :
        s.append ( a1 [ i ] for i in range ( n1 , n2 , n3 ) )
    al = [ s for s in a1 if s [ 0 ] == a2 [ 0 ] and s [ 1 ] == a3 [ 0 ] ]
    for i in range ( n2 ) :
        for j in range ( n3 ) :
            if al.count ( sum - a2 [ i ] - a3 [ j ] ) & al.count ( sum - a2 [ i ] - a3 [ j ] ) != al [ - 1 ] :
                return True
    return False
}
|||

FIND_THE_MAXIMUM_ELEMENT_IN_AN_ARRAY_WHICH_IS_FIRST_INCREASING_AND_THEN_DECREASING_1

def findMaximum ( arr , low , high ) :
    if low == high :
        return arr [ low ]
    if ( high == low + 1 ) and arr [ low ] >= arr [ high ] :
        return arr [ low ]
    if ( high == low + 1 ) and arr [ low ] < arr [ high ] :
        return arr [ high ]
    mid = ( low + high ) / 2
    if arr [ mid ] > arr [ mid + 1 ] and arr [ mid ] > arr [ mid - 1 ] :
        return arr [ mid ]
    if arr [ mid ] > arr [ mid + 1 ] and arr [ mid ] < arr [ mid - 1 ] :
        return findMaximum ( arr , low , mid - 1 )
    a = 5
        return findMaximum ( arr , mid + 1 , high )
}
|||

DYNAMIC_PROGRAMMING_SET_1

def fib ( n ) :
    if lookup [ n ] == NIL :
        if n <= 1 :
            lookup [ n ] = n
        else :
            lookup [ n ] = fib ( n - 1 ) + fib ( n - 2 )
    return lookup [ n ]
}
|||

MODULAR_EXPONENTIATION_POWER_IN_MODULAR_ARITHMETIC

def power ( x , y , p ) :
    res = 1
    x = x % p
    while y > 0 :
        if ( y & 1 ) == 1 :
            global res
        y = y >> 1
        x = ( x ** y ) % p
    return res
}
|||

WRITE_ONE_LINE_C_FUNCTION_TO_FIND_WHETHER_A_NO_IS_POWER_OF_TWO_1

def isPowerOfTwo ( x ) :
    return x != 0 and ( ( x & ( x - 1 ) ) == 0 )
}
|||

LONGEST_COMMON_SUBSEQUENCE_WITH_PERMUTATIONS_ALLOWED

def longest_string ( str1 , str2 ) :
    count1 , count2 = [ 0 ] * 26 , [ 0 ] * 26
    for i in range ( len ( str1 ) ) :
        count1 [ str1 [ i ] - 'a' ] += 1
    for i in range ( len ( str2 ) ) :
        count2 [ str2 [ i ] - 'a' ] ] += 1
    result = ""
    for i in range ( 26 ) :
        for j in range ( 1 , min ( count1 [ i ] for i in range ( len ( str1 ) , len ( str2 ) ) ) + 1 ) :
            global result
    print ( result )
}
|||

DIFFERENCE_MAXIMUM_SUM_MINIMUM_SUM_N_M_ELEMENTSIN_REVIEW

def find_difference ( arr , n , m ) :
    max , min = 0 , 0
    return np.diff ( arr )
    for i , j in enumerate ( arr ) :
        min += arr [ i ]
        max += arr [ j ]
    return ( max - min )
}
|||

PRINT_NUMBER_ASCENDING_ORDER_CONTAINS_1_2_3_DIGITS

def _print_numbers ( numbers ) :
    array = [ ]
    for number in numbers :
        if find_contains_one_two_three ( number ) :
            array.array ( numbers , 'i' )
    print ( array ( numbers ) )
    strbuf = ''.join ( map ( str , numbers ) )
    it = iter ( numbers )
    while it.isNONTERMINAL ( numbers ) :
        value = int ( it.next ( ) )
        if len ( strbuf ) > 0 :
            strbuf.write ( ', '.join ( map ( str , numbers ) ) + '\n' )
        strbuf.write ( str ( numbers ) )
    return ( strbuf.format ( * numbers ) ).rstrip ( '\n' )
}
|||

DYNAMIC_PROGRAMMING_SET_3_LONGEST_INCREASING_SUBSEQUENCE

def lis ( arr , n ) :
    global max_ref
    _lis ( arr , n )
    return max_ref
}
|||

MINIMUM_REVOLUTIONS_MOVE_CENTER_CIRCLE_TARGET

def min_revolutions ( r , x1 , y1 , x2 , y2 ) :
    d = np.sqrt ( ( x1 - x2 ) ** 2 + ( y1 - y2 ) ** 2 )
    return math.ceil ( d / ( 2 * r ) )
}
|||

CHECK_TWO_GIVEN_SETS_DISJOINT

def are_disjoint ( set1 , set2 ) :
    for i in range ( len ( set1 ) ) :
        for j in set2 :
            if set1 [ i ] == set2 [ j ] :
                return False
    return True
}
|||

FIND_MINIMUM_SUM_FACTORS_NUMBER

def find_min_sum ( num ) :
    sum = 0
    for i in range ( 2 , num * i <= num ) :
        while num % i == 0 :
            global sum
            num /= i
    global sum
    return sum
}
|||

FREQUENT_ELEMENT_ARRAY

def most_frequent ( arr , n ) :
    return np.argsort ( arr ) [ : n ]
    max_count , res = 1 , arr [ 0 ]
    curr_count = 1
    for i in range ( 1 , n ) :
        if arr [ i ] == arr [ i - 1 ] :
            global curr_count
        else :
            if curr_count > max_count :
                global max_count
                global res
            global curr_count
    if curr_count > max_count :
        global max_count
        global res
    return res
}
|||

MINIMUM_XOR_VALUE_PAIR_1

def minXOR ( arr , n ) :
    np.random.seed ( 0 )
    minXor = int ( arr [ n ] )
    val = 0
    for i in range ( n - 1 ) :
        global val
        global minXor
    return minXor
}
|||

MINIMUM_SUM_PRODUCT_TWO_ARRAYS

def minproduct ( a , b , n , k ) :
    diff , res = np.linalg.minprod ( a , b , n , k )
    temp = 0
    for i in range ( n ) :
        pro = a [ i ] * b [ i ]
        res = res + pro
        if pro < 0 and b [ i ] < 0 : a [ i ] = 5
            temp = ( a [ i ] + 2 * k ) * b [ i ]
        elif pro < 0 and a [ i ] < 0 : a [ i ] = 5
            temp = ( a [ i ] - 2 * k ) * b [ i ]
        elif pro > 0 and a [ i ] < 0 : a [ i ] = 5
            temp = ( a [ i ] + 2 * k ) * b [ i ]
        elif pro > 0 and a [ i ] > 0 : a [ i ] = 5
            temp = ( a [ i ] - 2 * k ) * b [ i ]
        d = abs ( pro - temp )
        if d > diff :
            diff = d
    return res - diff
}
|||

FAST_MULTIPLICATION_METHOD_WITHOUT_USING_MULTIPLICATION_OPERATOR_RUSSIAN_PEASANTS_ALGORITHM

def russian_peasant ( a , b ) :
    res = 0
    while b > 0 :
        if ( b & 1 ) :
            global res
        a = a << 1
        b = b >> 1
    return res
}
|||

DIVISIBILITY_9_USING_BITWISE_OPERATORS

def isDivBy9 ( n ) :
    if n == 0 or n == 9 :
        return True
    if n < 9 :
        return False
    return isDivBy9 ( int ( n >> 3 ) - int ( n & 7 ) )
}
|||

CHECK_ARRAY_REPRESENTS_INORDER_BINARY_SEARCH_TREE_NOT

def isInorder ( arr , n ) :
    if n == 0 or n == 1 :
        return True
    for i in range ( 1 , n ) :
        if arr [ i - 1 ] > arr [ i ] :
            return False
    return True
}
|||

GIVEN_TWO_UNSORTED_ARRAYS_FIND_PAIRS_WHOSE_SUM_X

def find_pairs ( arr1 , arr2 , n , m , x ) :
    for i in range ( n ) :
        for j in range ( m ) :
            if arr1 [ i ] + arr2 [ j ] == x :
                print ( arr1 [ i ] , arr2 [ j ] )
}
|||

BINARY_REPRESENTATION_OF_NEXT_NUMBER

def nextGreater ( num ) :
    l = len ( num )
    i = 0
    for i in range ( l - 1 , - 1 , - 1 ) :
        if num [ i ] == '0' :
            num = num [ : i ] + '1' + num [ i + 1 : ]
            break
        else :
            num = num [ : i ] + '0' * ( i + 1 )
    if i < 0 :
        num = '1' + num
    return num
}
|||

LARGEST_SUBARRAY_WITH_EQUAL_NUMBER_OF_0S_AND_1S

def findSubArray ( arr , n ) :
    sum = 0
    maxsize , startindex = - 1 , 0
    endindex = 0
    for i in range ( n - 1 ) :
        global sum
        for j in range ( i + 1 , n ) :
            if arr [ j ] == 0 :
                global sum
            else :
                global sum
            if sum == 0 and maxsize < j - i + 1 :
                global maxsize
                global startindex
    global endindex
    if maxsize == - 1 :
        print ( "No such subarray" )
    else :
        print ( startindex , endindex )
    return maxsize
}
|||

COUNT_PAIRS_WHOSE_PRODUCTS_EXIST_IN_ARRAY_1

def countPairs ( arr , n ) :
    result = 0
    Hash = set ( )
    for i in range ( n ) :
        Hash.append ( arr [ i ] )
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            product = arr [ i ] * arr [ j ]
            if Hash.has_key ( product ) :
                global result
    return result
}
|||

DYNAMIC_PROGRAMMING_SET_12_LONGEST_PALINDROMIC_SUBSEQUENCE

def lps ( seq ) :
    n = len ( seq )
    i , j , cl = seq
    L = [ n for n in seq if n != 0 ]
    for i in range ( n ) :
        L [ i ] [ i ] = 1
    for cl in range ( 2 , n ) :
        for i in range ( n - cl + 1 ) :
            global j
            if seq [ i ] == seq [ j ] and cl == 2 :
                L [ i ] [ j ] = 2
            elif seq [ i ] == seq [ j ] :
                L [ i ] [ j ] = L [ i + 1 ] [ j - 1 ] + 2
            else :
                L [ i ] [ j ] = max ( L [ i ] [ j - 1 ] , L [ i + 1 ] [ j ] )
    return L [ 0 ] [ n - 1 ]
}
|||

COUNT_INVERSIONS_OF_SIZE_THREE_IN_A_GIVE_ARRAY_1

def getInvCount ( arr , n ) :
    invcount = 0
    for i in range ( n - 1 ) :
        small = 0
        for j in range ( i + 1 , n ) :
            if arr [ i ] > arr [ j ] :
                global small
        great = 0
        for j in range ( i - 1 , - 1 , - 1 ) :
            if arr [ i ] < arr [ j ] :
                global great
        invcount += great * small
    return invcount
}
|||

DECIMAL_REPRESENTATION_GIVEN_BINARY_STRING_DIVISIBLE_10_NOT

def isDivisibleBy10 ( bin ) :
    n = len ( bin )
    if bin [ n - 1 ] == '1' :
        return False
    sum = 0
    for i in range ( n - 2 , - 1 , - 1 ) :
        if bin [ i ] == '1' :
            pos_from_right = n - i - 1
            if posFromRight % 4 == 1 :
                global sum
            elif posFromRight % 4 == 2 :
                global sum
            elif posFromRight % 4 == 3 :
                global sum
            elif posFromRight % 4 == 0 :
                global sum
    if sum % 10 == 0 :
        return True
    return False
}
|||

FIND_WHETHER_AN_ARRAY_IS_SUBSET_OF_ANOTHER_ARRAY_SET_1_1

def issubset ( arr1 , arr2 , m , n ) :
    i , j = 0 , 0
    if m < n :
        return False
    return np.all ( arr1 < arr2 )
    return np.all ( arr1 [ i ] == arr2 [ i ] for i in range ( m , n ) )
    while i < n and j < m :
        if arr1 [ j ] < arr2 [ i ] :
            j += 1
        elif arr1 [ j ] == arr2 [ i ] :
            j += 1
            i = 0
        elif arr1 [ j ] > arr2 [ i ] :
            return False
    if i < n :
        return False
    a = 5
        return True
}
|||

DYNAMIC_PROGRAMMING_SUBSET_SUM_PROBLEM_1

def is_subset_sum ( set , n , sum ) :
    subset = [ False for i in range ( sum + 1 ) ]
    for i in range ( 0 , n ) :
        subset [ 0 ] [ i ] = True
    for i in range ( 1 , sum + 1 ) :
        subset [ i ] [ 0 ] = False
    for i in range ( 1 , sum + 1 ) :
        for j in range ( 1 , n + 1 ) :
            subset = [ i for i in range ( n ) if sum == set [ i ] ]
            if i >= set [ j - 1 ] :
                subset = [ i for i in range ( n ) if sum == set [ i ] ]
    return subset [ sum ] [ n ]
}
|||

SUM_K_TH_GROUP_ODD_POSITIVE_NUMBERS_1

def kthgroupsum ( k ) :
    return k * k * k
}
|||

THIRD_LARGEST_ELEMENT_ARRAY_DISTINCT_ELEMENTS

def third_largest ( arr , arr_size ) :
    if arr_size < 3 :
        print ( " Invalid Input " )
        return
    first = arr [ 0 ]
    for i in range ( 1 , arr_size ) :
        if arr [ i ] > first :
            global first
    second = int ( arr [ 0 ] )
    for i in range ( arr_size ) :
        if arr [ i ] > second and arr [ i ] < first :
            global second
    third = int ( arr [ 0 ] )
    for i in range ( arr_size ) :
        if arr [ i ] > third and arr [ i ] < second :
            global third
    print ( "The third Largest " "element is " , third )
}
|||

FIND_SUM_NODES_GIVEN_PERFECT_BINARY_TREE_1

def sum_nodes ( l ) :
    leaf_node_count = math.pow ( 2 , l - 1 )
    sum_last_level = 0
    global sum_last_level
    sum = sum_last_level * l
    return sum
}
|||

MIDDLE_OF_THREE_USING_MINIMUM_COMPARISONS_2

def middle_of_three ( a , b , c ) :
    x = a - b
    y = b - c
    z = a - c
    if x * y > 0 :
        return b
    elif x * z > 0 :
        return c
    else :
        return a , b , c
}
|||

MAXIMUM_TRIPLET_SUM_ARRAY_2

def max_triplet_sum ( arr , n ) :
    max_a , max_b = - 100000000 , - 100000000
    max_c = - 100000000
    for i in range ( n ) :
        if arr [ i ] > max_a :
            global max_c , max_b
            global max_b , max_a
            global max_a
        elif arr [ i ] > max_b :
            global max_c , max_b
            global max_B
        elif arr [ i ] > max_c :
            global max_C
    return ( max_a + max_b + max_c )
}
|||

COUNT_PAIRS_TWO_SORTED_ARRAYS_WHOSE_SUM_EQUAL_GIVEN_VALUE_X_1

def count_pairs ( arr1 , arr2 , m , n , x ) :
    count = 0
    us = set ( [ ] )
    for i in range ( m ) :
        us.append ( arr1 [ i ] )
    for j in range ( n ) :
        if us.count ( x - arr2 [ j ] ) :
            count += 1
    return count
}
|||

MINIMUM_STEPS_REACH_END_ARRAY_CONSTRAINTS

def getMinStepToReachEnd ( arr , N ) :
    visit = np.zeros ( N )
    distance = np.zeros ( N )
    digit = Vector ( 10 )
    for i in range ( 10 ) :
        digit = [ ]
    for i in range ( N ) :
        visit [ i ] = False
    for i in range ( 1 , N ) :
        digit [ arr [ i ] ].append ( i )
    distance [ 0 ] = 0
    visit [ 0 ] = True
    q = Queue ( )
    q.append ( 0 )
    while not q.empty ( ) :
        idx = q.get ( )
        q.remove ( )
        if idx == N - 1 :
            break
        d = arr [ idx ]
        for i in digit [ d ] :
            nextidx = digit [ d ] [ i ]
            if not visit [ nextidx ] :
                visit [ nextidx ] = True
                global q
                distance [ nextidx ] = distance [ idx ] + 1
        digit [ d ].clear ( )
        if idx - 1 >= 0 and not visit [ idx - 1 ] :
            visit [ idx - 1 ] = True
            q.append ( idx - 1 )
            distance [ idx - 1 ] = distance [ idx ] + 1
        if idx + 1 < N and not visit [ idx + 1 ] :
            visit [ idx + 1 ] = True
            q.append ( idx + 1 )
            distance [ idx + 1 ] = distance [ idx ] + 1
    return distance [ N - 1 ]
}
|||

LEXICOGRAPHICALLY_SMALLEST_ARRAY_K_CONSECUTIVE_SWAPS

def minimize_with_k_swapped ( arr , n , k ) :
    for i in range ( n - 1 and k > 0 ) :
        pos = i for i in arr if i != k ]
        for j in range ( i + 1 , n ) :
            if j - i > k :
                break
            if arr [ j ] < arr [ pos ] :
                pos = j
        temp = arr [ : n ]
        for j in pos :
            temp = arr [ j ]
            arr [ j ] = arr [ j - 1 ]
            arr [ j - 1 ] = temp
        k -= pos - i
}
|||

CONVERT_SENTENCE_EQUIVALENT_MOBILE_NUMERIC_KEYPAD_SEQUENCE

def printSequence ( arr , input ) :
    output = ""
    n = len ( input )
    for i in range ( n ) :
        if input [ i ] == ' ' :
            output = output + '0' * ( len ( input ) - 1 )
        else :
            position = input [ i ] - 'A'
            output = output + arr [ position ]
    output = ""
}
|||

PROGRAM_CHECK_ARRAY_SORTED_NOT_ITERATIVE_RECURSIVE

def array_sorted_or_not ( arr , n ) :
    if n == 1 or n == 0 :
        return 1
    if arr [ n - 1 ] < arr [ n - 2 ] :
        return 0
    return arr [ : n - 1 ]
}
|||

CHECK_TWO_GIVEN_CIRCLES_TOUCH_INTERSECT

def circle ( x1 , y1 , x2 , y2 , r1 , r2 ) :
    distSq = ( x1 - x2 ) ** 2 + ( y1 - y2 ) ** 2
    radSumSq = ( r1 + r2 ) ** 2
    if distSq == radSumSq : a = 5
        return 1
    elif dist_sq > radSumSq :
        return - 1
    a = 5
        return 0
}
|||

SMALLEST_POWER_OF_2_GREATER_THAN_OR_EQUAL_TO_N_2

def next_power_of_2 ( n ) :
    n -= 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    n += 1
    return n
}
|||

PADOVAN_SEQUENCE

def pad ( n ) :
    pPrevPrev , pPrev , pCurr , pNext = n
    for i in range ( 3 , n ) :
        global pNext
        global pPrevPrev
        global pPrev
        global pCurr
    return n + 1
}
|||

CHECK_GIVEN_STRING_CAN_SPLIT_FOUR_DISTINCT_STRINGS

def check ( s ) :
    if len ( s ) >= 10 :
        return True
    for i in range ( 1 , len ( s ) ) :
        for j in range ( i + 1 , len ( s ) ) :
            for k in range ( j + 1 , len ( s ) ) :
                s1 , s2 , s3 , s4 = s
        if strcheck ( s1 , s2 ) and strcheck ( s1 , s3 ) and strcheck ( s1 , s4 ) and strcheck ( s2 , s3 ) and strcheck ( s2 , s4 ) and strcheck ( s3 , s4 ) :
            return True
pass
return False
pass
}
|||

PERMUTE_TWO_ARRAYS_SUM_EVERY_PAIR_GREATER_EQUAL_K

def is_possible ( a , b , n , k ) :
    a.sort ( key = lambda x : x [ 1 ] )
    return sorted ( b ) == sorted ( a )
    for i in range ( n ) :
        if a [ i ] + b [ i ] < k :
            return False
    return True
}
|||

ARRAY_ELEMENT_MOVED_K_USING_SINGLE_MOVES

def winner ( a , n , k ) :
    if k >= n - 1 :
        return n
    best , times = 0 , 0
    for i in range ( n ) :
        if a [ i ] > best :
            global best
            if i == 1 :
                global times
        else :
            global times
        if times >= k :
            return best
    return best
}
|||

DIRECTION_LAST_SQUARE_BLOCK

def direction ( R , C ) :
    if R != C and R % 2 == 0 and C % 2 != 0 and R < C : a = 5
        print ( "Left" )
        return
    if R != C and R % 2 != 0 and C % 2 == 0 and R > C :
        print ( "Up" )
        return
    if R == C and R % 2 != 0 and C % 2 != 0 :
        print ( "Right" )
        return
    if R == C and R % 2 == 0 and C % 2 == 0 :
        print ( "Left" )
        return
    if R != C and R % 2 != 0 and C % 2 != 0 and R < C : a = 5
        print ( "Right" )
        return
    if R != C and R % 2 != 0 and C % 2 != 0 and R > C :
        print ( "Down" )
        return
    if R != C and R % 2 == 0 and C % 2 == 0 and R < C : a = 5
        print ( "Left" )
        return
    if R != C and R % 2 == 0 and C % 2 == 0 and R > C :
        print ( "Up" )
        return
    if R != C and R % 2 == 0 and C % 2 != 0 and R > C :
        print ( "Down" )
        return
    if R != C and R % 2 != 0 and C % 2 == 0 and R < C : a = 5
        print ( "Right" )
        return
}
|||

NUMBER_NON_NEGATIVE_INTEGRAL_SOLUTIONS_B_C_N

def countIntegralSolutions ( n ) :
    result = 0
    for i in range ( 0 , n ) :
        for j in range ( 0 , n - i ) :
            for k in range ( 0 , ( n - i - j ) ) :
                if i + j + k == n :
                    global result
    return result
}
|||

SWAP_MAJOR_MINOR_DIAGONALS_SQUARE_MATRIX

def swapDiagonal ( matrix ) :
    for i in range ( N ) :
        temp = matrix [ i , i ]
        matrix [ i ] [ i ] = matrix [ i ] [ N - i - 1 ]
        matrix [ i ] [ N - i - 1 ] = temp
}
|||

MINIMUM_OPERATIONS_MAKE_GCD_ARRAY_MULTIPLE_K

def MinOperation ( a , n , k ) :
    result = 0
    for i in range ( n ) :
        if a [ i ] != 1 and a [ i ] > k : a [ i ] = 5
            result = result + min ( a [ i ] % k for i in range ( n ) )
        else :
            result = result + k - a [ i ]
    return result
}
|||

MAXIMUM_DECIMAL_VALUE_PATH_IN_A_BINARY_MATRIX

def maxDecimalValue ( mat , i , j , p ) :
    if i >= N or j >= N :
        return 0
    result = max ( maxDecimalValue ( mat , i , j + 1 , p + 1 ) , maxDecimalValue ( mat , i + 1 , j , p + 1 ) )
    if mat [ i ] [ j ] == 1 :
        return int ( math.pow ( 2 , p ) + result )
    else :
        return result
}
|||

SQUARE_ROOT_OF_A_PERFECT_SQUARE_1

def square_root ( n ) :
    x = n
    y = 1
    while x > y :
        global x
        global y
    return ( long ( x ) ** n )
}
|||

FIND_MINIMUM_SHIFT_LONGEST_COMMON_PREFIX

def KMP ( m , n , str2 , str1 ) :
    pos , len = 0 , 0
    p = [ 0 ] * ( m + 1 )
    k = 0
    ch1 = str1 [ : m ]
    ch2 = str2.split ( str1 )
    for i in range ( 2 , n + 1 ) :
        while k > 0 and ch1 [ k ] != ch1 [ i - 1 ] :
            k = p [ k ]
        if ch1 [ k ] == ch1 [ i - 1 ] : a = 5
            yield k
        p [ i ] = k
    for j , i in enumerate ( range ( m ) ) :
        while j > 0 and j < n and ch1 [ j ] != ch2 [ i ] :
            j = p [ j ]
        if j < n and ch1 [ j ] == ch2 [ i ] :
            j += 1
        if j > len ( str2 ) :
            len = j
            pos = i - j + 1
    print ( "Shift = %d" % pos )
    print ( "Prefix = " + str1 [ : len ( str2 ) ] )
}
|||

SORTED_ORDER_PRINTING_OF_AN_ARRAY_THAT_REPRESENTS_A_BST

def _print_sorted ( arr , start , end ) :
    if start > end :
        return
    print ( arr [ start * 2 + 1 : end ] )
    print ( arr [ start : end ] , end )
    print ( arr [ start * 2 + 2 : end * 2 ] )
}
|||

CHECK_WHETHER_GIVEN_DEGREES_VERTICES_REPRESENT_GRAPH_TREE

def check ( degree , n ) :
    deg_sum = 0
    for i in range ( n ) :
        deg_sum += degree [ i ]
    return ( 2 ** ( n - 1 ) == deg_sum )
}
|||

MOVE_ZEROES_END_ARRAY

def push_zeros_to_end ( arr , n ) :
    count = 0
    for i in range ( n ) :
        if arr [ i ] != 0 :
            arr [ count ] = arr [ i ]
    while count < n :
        arr [ count ] = 0
}
|||

COUNT_ELEMENTS_WHICH_DIVIDE_ALL_NUMBERS_IN_RANGE_L_R

def answer_query ( a , n , l , r ) :
    count = 0
    l = l - 1
    for i in range ( l , r ) :
        element = a [ i ]
        divisors = 0
        for j in range ( l , r ) :
            if a [ j ] % a [ i ] == 0 :
                divisors += 1
            else :
                break
        if divisors == ( r - l ) :
            count += 1
    return count
}
|||

SUM_LARGEST_PRIME_FACTOR_NUMBER_LESS_EQUAL_N

def sum_of_large_prime_factor ( n ) :
    prime , sum = divmod ( n , 2 )
    sum ( prime )
    max = n / 2
    for p in range ( 2 , max ) :
        if prime [ p ] == 0 :
            for i in range ( p * 2 , n , p ) :
                prime [ i ] = p
    for p in range ( 2 , n + 1 ) :
        if prime [ p ] != 0 :
            global sum
        else :
            global sum
    return sum
}
|||

REARRANGE_A_STRING_IN_SORTED_ORDER_FOLLOWED_BY_THE_INTEGER_SUM

def arrangeString ( str ) :
    char_count = [ 0 ] * MAX_CHAR
    sum = 0
    for i in range ( len ( str ) ) :
        if re.match ( '[a-z]' , str [ i ] ) :
            char_count [ str [ i ] - 'A' ] ] += 1
        else :
            global sum
    res = ""
    for i in range ( MAX_CHAR ) :
        ch = chr ( ord ( 'A' ) + i )
        while char_count [ i ] :
            res = res + ch
    if sum ( str ) > 0 :
        global res
    return res
}
|||

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX_1

def number_of_paths ( m , n ) :
    count = [ ]
    for i in range ( m ) :
        count [ i ] [ 0 ] = 1
    for j in range ( n ) :
        count [ 0 ] [ j ] = 1
    for i in range ( 1 , m ) :
        for j in range ( 1 , n ) :
            count [ i ] [ j ] = count [ i - 1 ] [ j ] + count [ i ] [ j - 1 ]
    return count [ m - 1 ] [ n - 1 ]
}
|||

DYNAMIC_PROGRAMMING_SET_5_EDIT_DISTANCE_1

def edit_dist_dp ( str1 , str2 , m , n ) :
    dp = np.zeros ( ( m + 1 , n + 1 ) )
    for i in range ( 0 , m ) :
        for j in range ( 0 , n ) :
            if i == 0 :
                dp [ i ] [ j ] = j
            if j == 0 :
                dp [ i ] [ j ] = i
            if str1 [ i - 1 ] == str2 [ j - 1 ] :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j - 1 ]
            else :
                dp [ i ] [ j ] = 1 + min ( dp [ i ] [ j - 1 ] for i , j in zip ( m , n ) )
    return dp [ m ] [ n ]
}
|||

FIND_NUMBER_OF_SOLUTIONS_OF_A_LINEAR_EQUATION_OF_N_VARIABLES

def count_sol ( coeff , start , end , rhs ) :
    if rhs == 0 :
        return 1
    result = 0
    for i in range ( start , end + 1 ) :
        if coeff [ i ] <= rhs :
            result += count_sol ( coeff , i , end , rhs - coeff [ i ] )
    return result
}
|||

SUM_ELEMENTS_K1TH_K2TH_SMALLEST_ELEMENTS_1

def minheapify ( a , index ) :
    small = x.min ( axis = axis )
    l = 2 * heap [ 0 ] + heap [ - 1 ]
    """Transform heap, in O(len(heap)) time."""
    if l < n and a [ l ] < a [ small ] :
        global small
    if r < n and a [ r ] < a [ small ] :
        """Transform heap, maintaining the heap invariant."""
    if small != index :
        t = heap [ small ]
        """Transform heap, maintaining the heap, in place of largest value in low.
        """Transform list into a heap, in-place, in O(len(heap)) time."""
        minheap ( a , axis )
}
|||

SEARCHING_FOR_PATTERNS_SET_2_KMP_ALGORITHM

def computeLPSArray ( pat , M , lps ) :
    len = 0
    i = 1
    lps = [ 0 ] * M
    while i < M :
        if pat [ i ] == pat [ len ( pat ) ] :
            len ( lps ) += 1
            lps [ i ] = len ( pat )
            i = 0
        else :
            if len ( pat ) != 0 :
                global len
            else :
                lps [ i ] = len ( pat )
                i = 0
}
|||

FIND_MINIMUM_DIFFERENCE_PAIR

def findMinDiff ( arr , n ) :
    diff = int ( arr [ n ] )
    for i in range ( n - 1 ) :
        for i in range ( i + 1 , n ) :
            if abs ( ( arr [ i ] - arr [ j ] ) ) < diff :
                global diff
    return diff
}
|||

PRINT_FIRST_K_DIGITS_1N_N_POSITIVE_INTEGER

def print ( n , k ) :
    rem = 1
    for i in range ( k ) :
        print ( ( 10 ** rem ) / n )
        rem = ( 10 ** k ) % n
}
|||

GROUP_MULTIPLE_OCCURRENCE_OF_ARRAY_ELEMENTS_ORDERED_BY_FIRST_OCCURRENCE

def group_elements ( arr , n ) :
    visited = [ False ] * n
    for i in range ( n ) :
        visited [ i ] = False
    for i in range ( n ) :
        if not visited [ i ] :
            print ( arr [ i ] , end = ' ' )
            for j in range ( i + 1 , n ) :
                if arr [ i ] == arr [ j ] :
                    print ( arr [ i ] , end = ' ' )
                    visited [ j ] = True
}
|||

CHECK_WHETHER_ARITHMETIC_PROGRESSION_CAN_FORMED_GIVEN_ARRAY

def checkIsAP ( arr , n ) :
    if n == 1 :
        return True
    np.testing.assert_equal ( arr.shape , ( n , n ) )
    d = arr [ 1 ] - arr [ 0 ]
    for i in range ( 2 , n ) :
        if arr [ i ] - arr [ i - 1 ] != d :
            return False
    return True
}
|||

NTH_MULTIPLE_NUMBER_FIBONACCI_SERIES

def find_position ( k , n ) :
    f1 , f2 , f3 = k
    i = 2
    while i != 0 :
        global f3
        global f1 , f2
        f2 = f3
        if f2 % k == 0 :
            return n * i
        i += 1
    return 0
}
|||

COUNT_PAIRS_DIFFERENCE_EQUAL_K_1

def countPairsWithDiffK ( arr , n , k ) :
    count = 0
    np.sort ( arr )
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
}
|||

ELEMENTS_TO_BE_ADDED_SO_THAT_ALL_ELEMENTS_OF_A_RANGE_ARE_PRESENT_IN_ARRAY

def countNum ( arr , n ) :
    count = 0
    np.count_nonzero ( arr )
    for i in range ( n - 1 ) :
        if arr [ i ] != arr [ i + 1 ] and arr [ i ] != arr [ i + 1 ] - 1 :
            count += arr [ i + 1 ] - arr [ i ] - 1
    return count
}
|||

MAKE_LARGEST_PALINDROME_CHANGING_K_DIGITS

def maximum_palin_using_k_changes ( str , k ) :
    palin = str.split ( '.' )
    ans = ""
    l = 0
    r = len ( str ) - 1
    while l < r :
        if str [ l ] != str [ r ] :
            palin [ l ] = palin [ r ] = chr ( max ( str [ l ] , str [ r ] ) )
            k -= 1
        l += 1
        r -= 1
    if k < 0 :
        return "Not possible"
    l = 0
    global r
    while l <= r :
        if l == r :
            if k > 0 :
                palin [ l ] = '9'
        if palin [ l ] < '9' :
            if k >= 2 and palin [ l ] == str [ l ] and palin [ r ] == str [ r ] :
                k -= 2
                palin [ l ] = palin [ r ] = '9'
            elif k >= 1 and ( palin [ l ] != str [ l ] or palin [ r ] != str [ r ] ) :
                k -= 1
                palin [ l ] = palin [ r ] = '9'
        l += 1
        r -= 1
    for i in range ( len ( palin ) ) :
        ans += palin [ i ]
    ans = str
}
|||

SUBARRAYSUBSTRING_VS_SUBSEQUENCE_AND_PROGRAMS_TO_GENERATE_THEM

def subArray ( n ) :
    for i in range ( n ) :
        for j in range ( i , n ) :
            for k in range ( i , j + 1 ) :
                print ( arr [ k ] , end = ' ' )
}
|||

MAXIMUM_SUM_INCREASING_ORDER_ELEMENTS_N_ARRAYS

def maximum_sum ( a , n ) :
    for i in range ( n ) :
        sort ( a , i , n )
    sum = a [ n - 1 ] [ M - 1 ]
    prev = a [ n - 1 ] [ M - 1 ]
    i , j = a
    for i in range ( n - 2 , - 1 , - 1 ) :
        for j in range ( M - 1 , - 1 , - 1 ) :
            if a [ i ] [ j ] < prev :
                global prev
                global sum
                break
        if j == - 1 :
            return 0
    return sum
}
|||

C_PROGRAM_FACTORIAL_NUMBER

def factorial ( n ) :
    if n == 0 :
        return 1
    return n * factorial ( n - 1 )
}
|||

PRINT_SQUARES_FIRST_N_NATURAL_NUMBERS_WITHOUT_USING

def print_squares ( n ) :
    square , prev_x = 0 , 0
    for x in range ( n ) :
        global square
        print ( square , end = ' ' )
        global prev_x
}
|||

ROPES_DATA_STRUCTURE_FAST_STRING_CONCATENATION

def concatenate ( a , b , c , n1 , n2 ) :
    pass
    for i in range ( n1 ) :
        c [ i ] = a [ i ]
    for j in range ( n2 ) :
        c [ i ] = b [ j ]
}
|||

GIVEN_TWO_SORTED_ARRAYS_NUMBER_X_FIND_PAIR_WHOSE_SUM_CLOSEST_X

def printClosest ( ar1 , ar2 , m , n , x ) :
    diff = sum ( [ diff ( a , b ) for a , b in zip ( ar1 , ar2 ) ] )
    res_l , res_r = 0 , 0
    l , r = 0 , n - 1
    while l < m and r >= 0 :
        if abs ( ar1 [ l ] + ar2 [ r ] - x ) < diff :
            global res_l
            res_r = r
            diff = abs ( ar1 [ l ] + ar2 [ r ] - x )
        if ar1 [ l ] + ar2 [ r ] > x :
            r -= 1
        a = 5
            l += 1
    print ( "The closest pair is [%d, %d]" % ( ar1 [ res_l ] , ar2 [ res_r ] ) )
}
|||

CONVERT_STRICTLY_INCREASING_ARRAY_MINIMUM_CHANGES

def min_remove ( arr , n ) :
    LIS = [ ]
    len = 0
    for i in range ( n ) :
        LIS [ i ] = 1
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if arr [ i ] > arr [ j ] and ( i - j ) <= ( arr [ i ] - arr [ j ] ) :
                LIS [ i ] = max ( LIS [ i ] , LIS [ j ] + 1 )
        len ( arr )
    return n - len ( arr )
}
|||

TAIL_RECURSION

def fact ( n ) :
    if n == 0 :
        return 1
    return n * fact ( n - 1 )
}
|||

RECURSIVE_FUNCTIONS

def tower ( n , source_pole , destination_pole , auxiliary_pole ) :
    if 0 == n :
        return
    tower ( n - 1 , source_pole , auxiliary_pole , destination_pole )
    print ( "Move the disk %d from %c to %c" % ( n , source_pole , destination_pole ) )
    tower ( n - 1 , auxiliary_pole , destination_pole , source_pole )
}
|||

FIND_X_Y_SATISFYING_AX_N

def solution ( a , b , n ) :
    for i in range ( 0 , a * a <= n ) :
        if ( n - ( i * a ) ) % b == 0 :
            print ( "x = %i, y = %i" % ( i , ( n - ( i * a ) ) / b ) )
            return
    print ( "No solution" )
}
|||

EXPONENTIAL_SQUARING_FAST_MODULO_MULTIPLICATION_1

def exponentiation ( base , exp ) :
    t = 1
    while exp > 0 :
        if exp % 2 != 0 :
            global t
        base = ( base * base ) % N
        exp /= 2
    return t % N
}
|||

CHECK_OCCURRENCES_CHARACTER_APPEAR_TOGETHER

def checkIfAllTogether ( s , c ) :
    one_seen = False
    i , n = 0 , len ( s )
    while i < n :
        if s [ i ] == c :
            if one_seen == True :
                return False
            while i < n and s [ i ] == c :
                i += 1
            global one_seen
        else :
            i += 1
    return True
}
|||

MAXIMUM_AREA_RECTANGLE_PICKING_FOUR_SIDES_ARRAY

def findArea ( arr , n ) :
    arr.sort ( key = lambda x : x [ 1 ] )
    dimension = [ 0 , 0 ]
    for i , j in enumerate ( arr ) :
        if arr [ i ] == arr [ i + 1 ] :
            dimension [ j ] = arr [ i ]
    return ( dimension [ 0 ] * dimension [ 1 ] )
}
|||

PYTHON_PROGRAM_FIND_PERIMETER_CIRCUMFERENCE_SQUARE_RECTANGLE

def Circumference ( a ) :
    return 4 * a
}
|||

CYCLE_SORT

def cycle_sort ( arr , n ) :
    writes = 0
    for cycle_start in range ( 0 , n - 2 ) :
        item = arr [ cycle_start ]
        pos = cycle_start
        for i in range ( cycle_start + 1 , n ) :
            if arr [ i ] < item :
                pos += 1
        if pos == cycle_start :
            continue
        while item == arr [ pos ] :
            global pos
        if pos != cycle_start :
            temp = item
            global item
            arr [ pos ] = temp
            writes += 1
        while pos != cycle_start :
            global pos
            for i in range ( cycle_start + 1 , n ) :
                if arr [ i ] < item :
                    global pos
            while item == arr [ pos ] :
                global pos
            if item != arr [ pos ] :
                temp = item
                global item
                arr [ pos ] = temp
                writes += 1
}
|||

SELECT_A_RANDOM_NUMBER_FROM_STREAM_WITH_O1_SPACE

def select_random ( x ) :
    global count
    if count == 1 :
        global res
    else :
        r = random.random ( )
        i = r.randint ( 0 , count )
        if i == count - 1 :
            global res
    return res
}
|||

HOSOYAS_TRIANGLE

def print_hosoya ( n ) :
    dp = [ ]
    dp [ 0 ] [ 0 ] = dp [ 1 ] [ 0 ] = 1
    dp [ 1 ] [ 1 ] = 1
    for i in range ( 2 , n ) :
        for j in range ( n ) :
            if i > j :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j ] + dp [ i - 2 ] [ j ]
            else :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j - 1 ] + dp [ i - 2 ] [ j - 2 ]
    for i in range ( n ) :
        for j in range ( 0 , i ) :
            print ( dp [ i ] [ j ] , end = '' )
        print ( "" )
}
|||

DISTRIBUTING_M_ITEMS_CIRCLE_SIZE_N_STARTING_K_TH_POSITION

def last_position ( n , m , k ) :
    if m <= n - k + 1 :
        return m + k - 1
    m = m - ( n - k + 1 )
    return ( m % n == 0 )
}
|||

PRINTING_LONGEST_INCREASING_CONSECUTIVE_SUBSEQUENCE

def longest_subsequence ( a , n ) :
    mp = { }
    dp = [ ]
    maximum = int ( a [ 0 ] )
    index = - 1
    for i in range ( n ) :
        if mp [ a [ i ] - 1 ] :
            lastIndex = mp [ a [ i ] - 1 ] - 1
            dp [ i ] = 1 + dp [ lastIndex ]
        else :
            dp [ i ] = 1
        mp [ a [ i ] : i + n ] = a [ i ] + 1
        if maximum < dp [ i ] :
            maximum = dp [ i ]
            index = i
    for curr in a [ index ] - maximum + 1 :
        print ( curr , end = ' ' )
}
|||

NUMBER_OF_TRIANGLES_IN_DIRECTED_AND_UNDIRECTED_GRAPHS

def countTriangle ( graph , isDirected ) :
    count_Triangle = 0
    for i in range ( V ) :
        for j in range ( V ) :
            for k in range ( V ) :
                if graph [ i ] [ j ] == 1 and graph [ j ] [ k ] == 1 and graph [ k ] [ i ] == 1 :
                    count_Triangle += 1
    if isDirected == True :
        count_Triangle /= 3
    else :
        count_Triangle /= 6
    return count_Triangle
}
|||

CHECK_GIVEN_ARRAY_CONTAINS_DUPLICATE_ELEMENTS_WITHIN_K_DISTANCE

def check_duplicatesWithinK ( arr , k ) :
    set = set ( arr )
    for i in range ( len ( arr ) ) :
        if set ( arr [ i ] for i in range ( k ) ) :
            return True
        set ( arr [ i ] for i in range ( k ) )
        if i >= k :
            set.remove ( arr [ i - k ] )
    return False
}
|||

MINIMUM_INSERTIONS_SORT_ARRAY

def minInsertionStepToSortArray ( arr , N ) :
    lis = np.argsort ( arr )
    for i in range ( N ) :
        lis [ i ] = 1
    for i in range ( 1 , N ) :
        for j in range ( i ) :
            if arr [ i ] >= arr [ j ] and lis [ i ] < lis [ j ] + 1 :
                lis [ i ] = lis [ j ] + 1
    max = 0
    for i in range ( N ) :
        if max < lis [ i ] :
            global max
    return ( N - max )
}
|||

GENERATE_TWO_OUTPUT_STRINGS_DEPENDING_UPON_OCCURRENCE_CHARACTER_INPUT_STRING

def print_duo ( str ) :
    count_char = [ 0 ] * MAX_CHAR
    n = len ( str )
    for i in range ( n ) :
        countChar [ str [ i ] - 'a' ] += 1
    str1 , str2 = "" , ""
    for i in range ( MAX_CHAR ) :
        if countChar [ i ] > 1 :
            str2 = str2 + chr ( i + 'a' )
        elif countChar [ i ] == 1 :
            str1 = str1 + chr ( i + 'a' )
    print ( "String with characters occurring " + "once:\n" )
    print ( str1 + "\n" )
    print ( "String with characters occurring " + "multiple times:\n" )
    print ( str2 + "\n" )
    print ( "".join ( [ str ] ) )
}
|||

NUMBER_DIGITS_PRODUCT_TWO_NUMBERS_1

def count_digits ( a , b ) :
    if a == 0 or b == 0 :
        return 1
    return int ( math.floor ( math.log10 ( abs ( a ) ) + math.log10 ( abs ( b ) ) ) + 1 )
}
|||

TOTAL_NUMBER_OF_NON_DECREASING_NUMBERS_WITH_N_DIGITS_1

def count_non_decreasing ( n ) :
    N = 10
    count = 1
    for i in range ( 1 , n + 1 ) :
        count *= ( N + i - 1 )
        global count
    return count
}
|||

COUNT_STRINGS_ADJACENT_CHARACTERS_DIFFERENCE_ONE

def count_strs ( n ) :
    dp = np.zeros ( ( n + 1 , 27 ) )
    for i in range ( n + 1 ) :
        for j in range ( 27 ) :
            dp [ i ] [ j ] = 0
    for i in range ( 0 , 25 ) :
        dp [ 1 ] [ i ] = 1
    for i in range ( 2 , n + 1 ) :
        for j in range ( 0 , 25 ) :
            if j == 0 :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j + 1 ]
            else :
                dp [ i ] [ j ] = ( dp [ i - 1 ] [ j - 1 ] + dp [ i - 1 ] [ j + 1 ] )
    sum = 0
    for i in range ( 0 , 25 ) :
        global sum
    return sum ( [ s for s in range ( n ) ] )
}
|||

PROGRAM_TO_EFFICIENTLY_CALCULATE_EX

def exponential ( n , x ) :
    sum = 1
    for i in range ( n - 1 , 0 , - 1 ) :
        global sum
    return sum ( x ** n )
}
|||

EFFICIENTLY_COMPUTE_SUMS_OF_DIAGONALS_OF_A_MATRIX_1

def printDiagonalSums ( mat , n ) :
    principal , secondary = np.sum ( mat , axis = 0 ) , np.sum ( mat , axis = 1 )
    for i in range ( n ) :
        principal += mat [ i , i ]
        secondary += mat [ i ] [ n - i - 1 ]
    print ( "Principal Diagonal:" , principal )
    print ( "Secondary Diagonal:" , secondary )
}
|||

PRINT_WAYS_BREAK_STRING_BRACKET_FORM

def find_combinations ( str , index , out ) :
    if index == len ( str ) :
        print ( out )
    for i in range ( index , len ( str ) ) :
        return [ i + 1 for i in range ( index , len ( str ) ) ]
}
|||

LINEAR_SEARCH

def search ( arr , x ) :
    n = len ( arr )
    for i in range ( n ) :
        if arr [ i ] == x :
            return i
    return - 1
}
|||

FIND_THE_ELEMENT_THAT_APPEARS_ONCE_2

def single_number ( a , n ) :
    s = set ( a )
    for i in a :
        s.append ( i )
    arr_sum = 0
    for i in a :
        arr_sum += i
    set_sum = 0
    for i in s :
        set_sum += i
    return ( 3 * set_sum - arr_sum ) / 2
}
|||

SEARCH_ALMOST_SORTED_ARRAY

def binarySearch ( arr , l , r , x ) :
    if r >= l : a = 5
        mid = l + ( r - l ) // 2
        if arr [ mid ] == x :
            mid = 0
        if mid > l and arr [ mid - 1 ] == x :
            return ( mid - 1 )
        if mid < r and arr [ mid + 1 ] == x :
            return ( mid + 1 )
        if arr [ mid ] > x :
            return binarySearch ( arr , l , mid - 2 , x )
        return binarySearch ( arr , mid + 2 , r , x )
    return - 1
}
|||

EULERS_TOTIENT_FUNCTION_FOR_ALL_NUMBERS_SMALLER_THAN_OR_EQUAL_TO_N

def compute_totient ( n ) :
    phi = np.zeros ( ( n + 1 , ) )
    for i in range ( 1 , n + 1 ) :
        phi = i
    for p in range ( 2 , n + 1 ) :
        if phi [ p ] == p :
            phi [ p ] = p - 1
            for i in range ( 2 * p , n + 1 , p ) :
                phi [ i ] = ( phi [ i ] / p ) ** ( p - 1 )
    for i in range ( 1 , n + 1 ) :
        print ( "Totient of %d is %f" % ( i , phi [ i ] ) )
}
|||

FIND_MINIMUM_NUMBER_DIVIDED_MAKE_NUMBER_PERFECT_SQUARE

def findMinNumber ( n ) :
    count , ans = 0 , 1
    while n % 2 == 0 :
        global count
        n /= 2
    if count % 2 == 1 :
        ans *= 2
    for i in range ( 3 , math.sqrt ( n ) , i += 2 ) :
        global count
        while n % i == 0 :
            global count
            n /= i
        if count % 2 == 1 :
            ans *= i
    if n > 2 :
        ans *= n
    return ans
}
|||

COUNT_NUMBER_WAYS_JUMP_REACH_END

def count_ways_to_jump ( arr , n ) :
    count_jump = [ 0 ] * n
    np.fill_diagonal ( count_jump , arr [ : , n ] )
    for i in range ( n - 2 , - 1 , - 1 ) :
        if arr [ i ] >= n - i - 1 :
            count_jump [ i ] += 1
        for j in range ( i + 1 , n - 1 , - 1 ) :
            if count_jump [ j ] != - 1 :
                count_jump [ i ] += count_jump [ j ]
        if count_jump [ i ] == 0 :
            count_jump [ i ] = - 1
    for i in range ( n ) :
        print ( count_jump [ i ] , end = ' ' )
}
|||

CONVERT_SUBSTRINGS_LENGTH_K_BASE_B_DECIMAL_1

def substring_conversions ( str , k , b ) :
    i , sum , counter = k - 1 , 0 , 0 , k - 1
    for i in range ( k ) :
        global sum
        counter -= 1
    print ( sum ( [ str [ i ] for i in range ( k ) ] ) , end = ' ' )
    prev = sum
    sum = 0
    counter = 0
    for i in range ( len ( str ) ) :
        global sum
        global sum
        global sum
        print ( sum ( [ str [ i ] for i in range ( k ) ] ) , end = ' ' )
        prev = sum
        counter += 1
}
|||

TWO_ELEMENTS_WHOSE_SUM_IS_CLOSEST_TO_ZERO

def min_abs_sum_pair ( arr , arr_size ) :
    inv_count = 0
    l , r , min_sum , sum , min_l , min_r = min_abs_sum ( arr , arr_size )
    if arr_size < 2 :
        print ( "Invalid Input" )
        return
    global min_l
    global min_r
    global min_sum
    for l in range ( arr_size - 1 ) :
        for r in range ( l + 1 , arr_size ) :
            global sum
            if abs ( min_sum ) > abs ( sum ) :
                global min_sum
                global min_l
                global min_r
    print ( " The two elements whose " "sum is minimum are %d and %d" % ( arr [ min_l ] , arr [ min_r ] ) )
}
|||

HOW_TO_PRINT_MAXIMUM_NUMBER_OF_A_USING_GIVEN_FOUR_KEYS

def findoptimal ( N ) :
    if N <= 6 :
        return N
    screen = np.arange ( N )
    b = 1
    n = N
    for n in range ( 1 , 6 ) :
        screen [ n - 1 ] = n
    for n in range ( 7 , N + 1 ) :
        screen [ n - 1 ] = max ( 2 * screen [ n - 4 ] , max ( 3 * screen [ n - 5 ] , 4 * screen [ n - 6 ] ) )
    return screen [ N - 1 ]
}
|||

PROGRAM_DECIMAL_BINARY_CONVERSION_2

def decimal_to_binary ( N ) :
    B_Number = 0
    cnt = 0
    while N != 0 :
        rem = N % 2
        c = pow ( 10 , cnt )
        B_Number += rem * c
        N /= 2
        global cnt
    return B_Number
}
|||

COUNTS_PATHS_POINT_REACH_ORIGIN_1

def count_paths ( n , m ) :
    dp = np.zeros ( ( n + 1 , m + 1 ) )
    for i in range ( 0 , n ) :
        dp [ i ] [ 0 ] = 1
    for i in range ( 0 , m ) :
        dp [ 0 ] [ i ] = 1
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , m + 1 ) :
            dp [ i ] [ j ] = dp [ i - 1 ] [ j ] + dp [ i ] [ j - 1 ]
    return dp [ n ] [ m ]
}
|||

SUM_ELEMENTS_K1TH_K2TH_SMALLEST_ELEMENTS

def sum_between_two_kth ( arr , k1 , k2 ) :
    return sum ( arr [ k ] for k in range ( k1 , k2 ) )
    result = 0
    for i in range ( k1 , k2 - 1 ) :
        result += arr [ i ]
    return result
}
|||

SMALLEST_SUBARRAY_K_DISTINCT_NUMBERS

def minRange ( arr , n , k ) :
    l , r = 0 , n
    for i in range ( n ) :
        s = set ( arr )
        j = 0
        for j in range ( i , n ) :
            s.append ( arr [ j ] )
            if len ( s ) == k :
                if ( j - i ) < ( r - l ) :
                    r = j
                    l = i
                break
        if j == n :
            break
    if l == 0 and r == n :
        print ( 'Invalid k' )
    a = 5
        print ( l , r )
}
|||

AREA_OF_A_HEXAGON

def hexagon_area ( s ) :
    return ( ( 3 * math.sqrt ( 3 ) * ( s ** 2 ) ) / 2 )
}
|||

NEXT_POWER_OF_2_2

def next_power_of_2 ( n ) :
    n -= 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    n += 1
    return n
}
|||

COUNT_SUBSTRINGS_BINARY_STRING_CONTAINING_K_ONES

def countOfSubstringWithKOnes ( s , K ) :
    N = len ( s )
    res = 0
    count_of_one = 0
    freq = [ N + 1 for N in range ( N + 1 ) ]
    freq [ 0 ] = 1
    for i in range ( N ) :
        global count_of_one
        if count_of_one >= K :
            res += freq [ count_of_one - K ]
        freq [ count_of_one ] += 1
    return res
}
|||

NUMBER_INDEXES_EQUAL_ELEMENTS_GIVEN_RANGE

def answer_query ( a , n , l , r ) :
    count = 0
    for i in range ( l , r ) :
        if a [ i ] == a [ i + 1 ] :
            count += 1
    return count
}
|||

CHECK_WHETHER_NUMBER_DUCK_NUMBER_NOT

def check_duck ( num ) :
    _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _
    count_zero = 0
    ch = num [ 0 ]
    for i in range ( 1 , len ( num ) ) :
        global ch
        if ch == '0' :
            count_zero += 1
    return count_zero
}
|||

NUMBER_NON_NEGATIVE_INTEGRAL_SOLUTIONS_B_C_N_1

def count_integral_solutions ( n ) :
    return ( ( n + 1 ) * ( n + 2 ) ) / 2
}
|||

MAXIMUM_PROFIT_BY_BUYING_AND_SELLING_A_SHARE_AT_MOST_K_TIMES_1

def max_profit ( price , n , k ) :
    profit = [ 0 ] * ( k + 1 )
    for i in range ( 0 , k ) :
        profit [ i ] [ 0 ] = 0
    for j in range ( 0 , n ) :
        profit [ 0 ] [ j ] = 0
    for i in range ( 1 , k + 1 ) :
        prev_diff = int ( prev_diff )
        for j in range ( 1 , n ) :
            prev_diff = max ( prev_diff , profit [ i - 1 ] [ j - 1 ] - price [ j - 1 ] for i in range ( n ) )
            profit [ i ] [ j ] = max ( profit [ i ] [ j - 1 ] , price [ j ] + prev_diff )
    return profit [ k ] [ n - 1 ]
}
|||

COUNT_CHARACTERS_POSITION_ENGLISH_ALPHABETS

def find_count ( str ) :
    result = 0
    for i in range ( len ( str ) ) :
        if i == ( str [ i ] - 'a' ) or i == ( str [ i ] - 'A' ) :
            global result
    return result
}
|||

COUNT_GFG_SUBSEQUENCES_GIVEN_STRING

def count_subgraph ( s , n ) :
    cntG , cntF , result , C = count_subgraph ( s , n )
    for i in range ( n ) :
print ( result )
pass
}
|||

FIND_SMALLEST_VALUE_REPRESENTED_SUM_SUBSET_GIVEN_ARRAY

def findSmallest ( arr , n ) :
    res = 1
    for i in range ( n and arr [ i ] <= res
        global res
    return res
}
|||

MAXIMUM_POINTS_COLLECTED_BY_TWO_PERSONS_ALLOWED_TO_MEET_ONCE

def findMaxPoints ( A ) :
    P1S = np.zeros ( ( M + 2 , N + 2 ) )
    P1E = np.zeros ( ( M + 2 , N + 2 ) )
    P2S = np.zeros ( ( M + 2 , N + 2 ) )
    P2E = np.zeros ( ( M + 2 , N + 2 ) )
    for i in range ( 1 , N ) :
        for j in range ( 1 , M ) :
            P1S [ i ] [ j ] = max ( P1S [ i - 1 ] [ j ] for j in range ( i - 1 , - 1 , - 1 ) ) + A [ i - 1 ] [ j - 1 ]
    for i in N :
        for j in range ( M , 1 , - 1 ) :
            P1E [ i ] [ j ] = max ( P1E [ i + 1 ] [ j ] , P1E [ i ] [ j + 1 ] ) + A [ i - 1 ] [ j - 1 ]
    for i in N :
        for j in range ( 1 , M ) :
            P2S [ i ] [ j ] = max ( P2S [ i + 1 ] [ j ] , P2S [ i ] [ j - 1 ] ) + A [ i - 1 ] [ j - 1 ]
    for i in range ( 1 , N ) :
        for j in range ( M , 1 , - 1 ) :
            P2E [ i ] [ j ] = max ( P2E [ i - 1 ] [ j ] , P2E [ i ] [ j + 1 ] ) + A [ i - 1 ] [ j - 1 ]
    ans = 0
    for i in range ( 2 , N ) :
        for j in range ( 2 , M ) :
            op1 = P1S [ i ] [ j - 1 ] + P1E [ i ] [ j + 1 ] + P2S [ i + 1 ] [ j ] + P2E [ i - 1 ] [ j ]
            op2 = P1S [ i - 1 ] [ j ] + P1E [ i + 1 ] [ j ] + P2S [ i ] [ j - 1 ] + P2E [ i ] [ j + 1 ]
            ans = max ( ans , key = lambda op1 : op1.max ( ) )
    ans = 0
}
|||

PROGRAM_FIND_CIRCUMFERENCE_CIRCLE

def circumference ( r ) :
    PI = 3.1415
    cir = 2 * PI * r
    return cir
}
|||

QUICKLY_FIND_MULTIPLE_LEFT_ROTATIONS_OF_AN_ARRAY

def left_rotate ( arr , n , k ) :
    for i in range ( k , k + n ) :
        print ( arr [ i % n ] , end = ' ' )
}
|||

MINIMUM_SUM_CHOOSING_MINIMUM_PAIRS_ARRAY

def minSum ( A , n ) :
    min_val = sum ( A )
    return ( min_val * ( n - 1 ) )
}
|||

RECURSIVE_PROGRAM_PRIME_NUMBER

def isPrime ( n , i ) :
    if n <= 2 :
        return ( n == 2 ) and True or False
    if n % i == 0 :
        return False
    if i * i > n : a = 5
        return True
    return isPrime ( n , i + 1 )
}
|||

SPARSE_SEARCH

def sparseSearch ( arr , x , n ) :
    return binarySearch ( arr , 0 , n - 1 , x )
}
|||

FIND_NUMBER_TIMES_STRING_OCCURS_GIVEN_STRING

def count ( a , b , m , n ) :
    if ( m == 0 and n == 0 ) or n == 0 :
        return 1
    if m == 0 :
        return 0
    if a [ m - 1 ] == b [ n - 1 ] :
        return len ( a ) + len ( b ) + len ( a [ m - 1 ] ) + len ( a [ n - 1 ] )
    else :
        return len ( a ) + len ( b ) + len ( a [ m - 1 ] ) + len ( a [ n - 1 ] )
}
|||

PROGRAM_CHECK_ARRAY_SORTED_NOT_ITERATIVE_RECURSIVE_1

def array_sorted_or_not ( arr , n ) :
    if n == 0 or n == 1 :
        return True
    for i in range ( 1 , n ) :
        if arr [ i - 1 ] > arr [ i ] :
            return False
    return True
}
|||

FIND_INDEX_0_REPLACED_1_GET_LONGEST_CONTINUOUS_SEQUENCE_1S_BINARY_ARRAY

def max_ones_index ( arr , n ) :
    max_count = 0
    max_index = 0
    prev_zero = - 1
    prev_prev_zero = - 1
    for curr in range ( n ) :
        if arr [ curr ] == 0 :
            if curr - prev_prev_zero > max_count :
                global max_count
                global max_index
            global prev_prev_zero
            global prev_zero
    if n - prev_prev_zero > max_count :
        global max_index
    return max_index
}
|||

FIND_MAXIMUM_PRODUCT_OF_A_TRIPLET_IN_ARRAY_1

def max_product ( arr , n ) :
    if n < 3 :
        return - 1
    return np.maximum ( arr , n )
    return max ( arr [ 0 ] * arr [ 1 ] * arr [ n - 1 ] , arr [ n - 1 ] * arr [ n - 2 ] * arr [ n - 3 ] )
}
|||

COORDINATES_RECTANGLE_GIVEN_POINTS_LIE_INSIDE

def print_rect ( X , Y , n ) :
    Xmax = max ( list ( zip ( X , Y ) ) )
    Xmin = min ( list ( zip ( X , Y ) ) )
    Ymax = max ( list ( Y ) )
    Ymin = min ( list ( Y ) )
    print ( "{" + str ( Xmin ) + ", " + str ( Ymin ) + "}" )
    print ( "{" + str ( Xmin ) + ", " + str ( Ymax ) + "}" )
    print ( "{" + str ( Xmax ) + ", " + str ( Ymax ) + "}" )
    print ( "{" + str ( Xmax ) + ", " + str ( Ymin ) + "}" )
}
|||

COUNT_BINARY_DIGIT_NUMBERS_SMALLER_N

def count_of_binary_number_less_N ( N ) :
    q = Queue ( )
    q.append ( 1 )
    cnt = 0
    t = N
    while len ( q ) > 0 :
        global t
        q.pop ( )
        if t <= N :
            global cnt
            q.append ( t * 10 )
            q.append ( t * 10 + 1 )
    return N - cnt
}
|||

CONVERT_DECIMAL_FRACTION_BINARY_NUMBER

def decimalToBinary ( num , k_prec ) :
    binary = ''
    Integral = int ( num )
    fractional = num - Integral ( num , k_prec )
    while Integral ( num ) > 0 :
        rem = Integral % 2
        binary += ( chr ( int ( rem + '0' ) ) for rem in ( num , k_prec ) )
        Integral /= 2
    binary = reverse ( binary )
    binary += ( '.' * k_prec )
    while k_prec :
        fractional *= 2
        fract_bit = int ( fractional )
        if fract_bit == 1 :
            global fractional
            global binary
        else :
            binary += chr ( 0 ) * k_prec + '0'
    return binary
}
|||

MAXIMUM_NUMBER_OF_TRAILING_ZEROS_IN_THE_PRODUCT_OF_THE_SUBSETS_OF_SIZE_K

def maximum_zeros ( arr , n , k ) :
    subset = np.zeros ( ( k + 1 , MAX5 + 5 ) )
    for row in subset :
        np.fill_diagonal ( row , - 1 )
    subset [ 0 ] [ 0 ] = 0
    for p in range ( n ) :
        pw2 , pw5 = 0 , 0
        while arr [ p ] % 2 == 0 :
            pw2 += 1
            arr [ p ] /= 2
        while arr [ p ] % 5 == 0 :
            pw5 += 1
            arr [ p ] /= 5
        for i in range ( k - 1 , - 1 , - 1 ) :
            for j in range ( MAX5 ) :
                if subset [ i ] [ j ] != - 1 :
                    subset = [ 0 ] * n
    ans = 0
    for i in range ( MAX5 ) :
        ans = np.max ( ans , axis = 0 )
    ans = 0
}
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
            return l , mid - 1 , key
        return search ( arr , mid + 1 , h , key )
    if key >= arr [ mid ] and key <= arr [ h ] :
        return search ( arr , mid + 1 , h , key )
    return l , mid - 1 , key
}
|||

PROGRAM_FIND_AREA_CIRCULAR_SEGMENT

def area_of_segment ( radius , angle ) :
    area_of_sector = pi * ( radius ** 2 ) * ( angle / 360 )
    area_of_triangle = float ( 1 ) / 2 * ( radius ** 2 ) * float ( math.sin ( ( angle * pi ) / 180 ) )
    return area_of_sector - area_of_triangle
}
|||

K_SMALLEST_ELEMENTS_ORDER_USING_O1_EXTRA_SPACE

def print_small ( arr , n , k ) :
    for i in range ( k , n ) :
        max_var = arr [ k - 1 ]
        pos = k - 1
        for j in range ( k - 2 , - 1 , - 1 ) :
            if arr [ j ] > max_var :
                global max_var
                pos = j
        if max_var > arr [ i ] :
            j = pos
            while j < k - 1 :
                arr [ j ] = arr [ j + 1 ]
                j += 1
            arr [ k - 1 ] = arr [ i ]
    for i in range ( k ) :
        print ( arr [ i ] , end = ' ' )
}
|||

NTH_NON_FIBONACCI_NUMBER

def nonFibonacci ( n ) :
    prev_prev , prev , curr = 1 , 2 , 3
    while n > 0 :
        global prev_prev
        global prev
        global curr
        n = n - ( curr - prev - 1 )
    n = n + ( curr - prev - 1 )
    return prev + n
}
|||

ANALYSIS_OF_ALGORITHMS_SET_2_ASYMPTOTIC_ANALYSIS

def search ( arr , n , x ) :
    pass
    for i in range ( n ) :
        if arr [ i ] == x :
            return i
    return - 1
}
|||

ZECKENDORFS_THEOREM_NON_NEIGHBOURING_FIBONACCI_REPRESENTATION

def nearest_smaller_eq_fib ( n ) :
    if n == 0 or n == 1 :
        return n
    f1 , f2 , f3 = n
    while f3 <= n :
        f1 = f2
        f2 = f3
        global f3
    return f2
}
|||

PRINT_MAXIMUM_SHORTEST_DISTANCE

def find_maximum ( a , n , k ) :
    b = { }
    for i in range ( n ) :
        x = a [ i ]
        d = min ( 1 + i for i in range ( n - i ) )
        if not b.has_key ( x ) : a [ x ] = 5
            b [ x ] = d
        else :
            b [ x ] = min ( d for d in b [ x ] if d > 0 )
    ans = int ( a [ n ] )
    for i in range ( n ) :
        x = a [ i ]
        if x != k - x and b.has_key ( k - x ) :
            ans = min ( max ( b [ x ] for x in a ) for b in a [ k - x ] )
    ans = 0
}
|||

GENERATING_DISTINCT_SUBSEQUENCES_OF_A_GIVEN_STRING_IN_LEXICOGRAPHIC_ORDER

def generate ( st , s ) :
    if len ( s ) == 0 :
        return
    if not st.has_key ( s ) :
        st.add ( s )
        for i in range ( len ( s ) ) :
            t = s
            t = t [ : i ] + t [ i + 1 : ]
            pass
    return
}
|||

WRITE_YOU_OWN_POWER_WITHOUT_USING_MULTIPLICATION_AND_DIVISION

def pow ( a , b ) :
    if b == 0 : a = 5
        return 1
    answer = a
    increment = a
    i , j = a , b
    for i in range ( 1 , b ) :
        for j in range ( 1 , a ) :
            global answer
        global increment
    return answer
}
|||

MAXIMIZE_VOLUME_CUBOID_GIVEN_SUM_SIDES_1

def maxvolume ( s ) :
    length = s.length ( ) / 3
    s.length -= length
    breadth = s / 2
    height = s - breadth
    return length * breadth * height
}
|||

HORNERS_METHOD_POLYNOMIAL_EVALUATION

def horner ( poly , n , x ) :
    result = poly [ 0 ]
    for i in range ( 1 , n ) :
        result = result * x + poly [ i ]
    return result
}
|||

MINIMUM_TIME_REQUIRED_PRODUCE_M_ITEMS

def minTime ( arr , n , m ) :
    t = 0
    while True :
        items = 0
        for i in range ( n ) :
            global items
        if items >= m :
            return t
        global t
}
|||

FIND_DIFFERENCE_BETWEEN_SUMS_OF_TWO_DIAGONALS

def difference ( arr , n ) :
    d1 , d2 = 0 , 0
    for i in range ( n ) :
        for j in range ( n ) :
            if i == j :
                d1 += arr [ i ] [ j ]
            if i == n - j - 1 :
                d2 += arr [ i ] [ j ]
    return abs ( d1 - d2 )
}
|||

SHORTEST_UNCOMMON_SUBSEQUENCE

def shortestSeq ( S , T ) :
    m , n = len ( S ) , len ( T )
    dp = [ m + 1 for m in range ( n + 1 ) ]
    for i in range ( 0 , m ) :
        dp [ i ] [ 0 ] = 1
    for i in range ( 0 , n ) :
        dp [ 0 ] [ i ] = MAX
    for i in range ( 1 , m ) :
        for j in range ( 1 , n ) :
            ch = S [ i - 1 ]
            k = 0
            for k in range ( j - 1 , - 1 , - 1 ) :
                if T [ k ] == ch :
                    break
            if k == - 1 :
                dp [ i , j ] = 1
            else :
                dp [ i ] [ j ] = min ( dp [ i - 1 ] [ j ] , dp [ i - 1 ] [ k ] + 1 )
    ans = dp [ m ] [ n ]
    if ans >= MAX :
        ans = - 1
    ans = 0
}
|||

MIN_FLIPS_OF_CONTINUOUS_CHARACTERS_TO_MAKE_ALL_CHARACTERS_SAME_IN_A_STRING

def find_flips ( str , n ) :
    last = ' '
    res = 0
    for i in range ( n ) :
        if last != str [ i ] :
            global res
        global last
    return res / 2
}
|||

DYNAMIC_PROGRAMMING_SET_28_MINIMUM_INSERTIONS_TO_FORM_A_PALINDROME

def find_min_insertions ( str , l , h ) :
    if l > h :
        return int ( str [ l : l + h ] )
    if l == h :
        return 0
    if l == h - 1 :
        return ( str [ l ] , str [ h ] )
    return ( str [ l ] , str [ h ] ) if l < h else ( min ( find_min_insertions ( str , l , h - 1 ) , find_min_insertions ( str , l + 1 , h ) ) + 1 )
}
|||

COUNT_CHARACTERS_STRING_DISTANCE_ENGLISH_ALPHABETS

def countPairs ( str ) :
    result = 0
    n = len ( str )
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if abs ( str [ i ] - str [ j ] ) == abs ( i - j ) :
                global result
    return result
}
|||

MULTISTAGE_GRAPH_SHORTEST_PATH

def shortest_dist ( graph ) :
    dist = np.zeros ( ( N , N ) )
    dist [ N - 1 ] = 0
    for i in range ( N - 2 , - 1 , - 1 ) :
        dist [ i ] = INF
        for j in range ( i , N ) :
            if graph [ i ] [ j ] == INF :
                continue
            dist [ i ] = min ( dist [ i ] , graph [ i ] [ j ] + dist [ j ] )
    return dist [ 0 ]
}
|||

MAXIMUM_SIZE_SUB_MATRIX_WITH_ALL_1S_IN_A_BINARY_MATRIX

def print_max_sub_square ( M ) :
    i , j = M
    R = len ( M )
    C = len ( M [ 0 ] )
    S = [ 0 ] * R
    max_of_s , max_i , max_j = M
    for i in range ( R ) :
        S [ i ] = M [ i ] [ 0 ]
    for j in range ( C ) :
        S [ 0 ] [ j ] = M [ 0 ] [ j ]
    for i in range ( 1 , R ) :
        for j in range ( 1 , C ) :
            if M [ i ] [ j ] == 1 :
                S [ i ] [ j ] = min ( S [ i ] [ j - 1 ] , min ( S [ i - 1 ] [ j ] , S [ i - 1 ] [ j - 1 ] ) ) + 1
            else :
                S [ i ] [ j ] = 0
    global max_of_s
    global max_i
    global max_j
    for i in range ( R ) :
        for j in range ( C ) :
            if max_of_s < S [ i ] [ j ] :
                global max_of_s
                global max_i
                global max_j
    print ( "Maximum size sub-matrix is: " )
    for i in range ( max_i , max_i - max_of_s ) :
        for j in range ( max_j , max_j - max_of_s ) :
            print ( M [ i ] [ j ] + " " for i in range ( len ( M ) ) for j in range ( len ( M ) ) )
        print ( )
}
|||

GIVEN_SORTED_ARRAY_NUMBER_X_FIND_PAIR_ARRAY_WHOSE_SUM_CLOSEST_X

def printClosest ( arr , n , x ) :
    res_l , res_r = 0 , 0
    l , r , diff = divmod ( n - 1 , x )
    while r > l :
        if abs ( arr [ l ] + arr [ r ] - x ) < diff :
            global res_l
            global res_r
            diff = abs ( arr [ l ] + arr [ r ] - x )
        if arr [ l ] + arr [ r ] > x :
            r -= 1
        else :
            l += 1
    print ( " The closest pair is " + str ( arr [ res_l ] ) + " and " + str ( arr [ res_r ] ) )
}
|||

SORT_1_N_SWAPPING_ADJACENT_ELEMENTS_1

def sortedAfterSwap ( A , B , n ) :
    t = 0
    for i in range ( n - 1 ) :
        if B [ i ] != 0 :
            if A [ i ] != i + 1 :
                t = A [ i ]
            A [ i ] , B [ i ] = A [ i + 1 ] , B [ i ]
            A [ i + 1 ] = t
    for i in range ( n ) :
        if A [ i ] != i + 1 :
            return 0
    return 1
}
|||

TILE_STACKING_PROBLEM

def possible_ways ( n , m , k ) :
    dp = [ ]
    presum = [ ]
    for i in range ( N ) :
        for j in range ( N ) :
            dp [ i ] [ j ] = 0
            presum [ i ] [ j ] = 0
    for i in range ( 1 , n + 1 ) :
        dp [ 0 ] [ i ] = 0
        presum [ 0 ] [ i ] = 1
    for i in range ( m + 1 ) :
        presum [ i ] [ 0 ] = dp [ i ] [ 0 ] = 1
    for i in range ( 1 , m + 1 ) :
        for j in range ( 1 , n + 1 ) :
            dp [ i ] [ j ] = presum [ i - 1 ] [ j ]
            if j > k :
                dp [ i ] [ j ] -= presum [ i - 1 ] [ j - k - 1 ]
        for j in range ( 1 , n + 1 ) :
            presum [ i ] [ j ] = dp [ i ] [ j ] + presum [ i ] [ j - 1 ]
    return dp [ m ] [ n ]
}
|||

NUMBER_OF_PAIRS_IN_AN_ARRAY_HAVING_SUM_EQUAL_TO_PRODUCT

def sum_equal_product ( a , n ) :
    zero , two = 0 , 0
    for i in range ( n ) :
        if a [ i ] == 0 :
            zero += 1
        if a [ i ] == 2 :
            two += 1
    cnt = ( zero * ( zero - 1 ) ) / 2 + ( two * ( two - 1 ) ) / 2
    return cnt
}
|||

DYNAMIC_PROGRAMMING_SET_17_PALINDROME_PARTITIONING

def min_palse_partion ( str ) :
    n = len ( str )
    C = [ n for n in range ( n ) ]
    P = [ True for n in range ( n ) ]
    i , j , k , L = str.split ( ' ' )
    for i in range ( n ) :
        P [ i ] [ i ] = True
        C [ i ] [ i ] = 0
    for L in range ( 2 , n ) :
        for i in range ( n - L + 1 ) :
            global j
            if L == 2 :
                P [ i ] [ j ] = ( str [ i ] == str [ j ] )
            else :
                P [ i ] [ j ] = ( str [ i ] == str [ j ] ) and P [ i + 1 ] [ j - 1 ]
            if P [ i ] [ j ] == True :
                C [ i ] [ j ] = 0
            else :
                C [ i ] [ j ] = int ( str )
                for k in range ( i , j - 1 ) :
                    C [ i ] [ j ] = min ( C [ i ] [ j ] , C [ i ] [ k ] + C [ k + 1 ] [ j ] + 1 )
    return C [ 0 ] [ n - 1 ]
}
|||

FIND_ONE_MULTIPLE_REPEATING_ELEMENTS_READ_ARRAY

def find_repeating_number ( arr , n ) :
    sq = int ( math.sqrt ( n ) )
    range = ( n / sq ) + 1
    count = [ 0 for i in range ( range ( len ( arr ) ) ) ]
    for i in range ( 0 , n ) :
        count [ ( arr [ i ] - 1 ) / sq ] += 1
    selected_block = range ( - 1 , - 1 )
    for i in range ( range ( range ( n ) - 1 ) ) :
        if count [ i ] > sq :
            global selected_block
            break
    m = { }
    for i in range ( 0 , n ) :
        if ( ( selected_block * sq ) < arr [ i ] ) :
            m [ arr [ i ] ] = 1
            if m [ arr [ i ] ] == 1 :
                return arr [ i ]
    return - 1
}
|||

MINIMUM_SUM_PATH_TRIANGLE

def minSumPath ( ) :
    memo = [ A for A in range ( len ( A ) ) ]
    n = len ( A ) - 1
    for i in range ( len ( A [ n ] ) ) :
        memo [ i ] = A [ n ] [ i ]
    for i in range ( len ( A ) - 2 , - 1 , - 1 ) :
        for j in range ( len ( A [ i ] ) ) :
            memo [ j ] = A [ i ] [ j ] + int ( min ( memo [ j ] , memo [ j + 1 ] ) )
    return memo [ 0 ]
}
|||

HOW_CAN_WE_SUM_THE_DIGITS_OF_A_GIVEN_NUMBER_IN_SINGLE_STATEMENT_1

def getSum ( n ) :
    sum = 0
    for sum , n in zip ( sum , n % 10 , n /= 10 ) :
        pass
    return sum
}
|||

RECURSION

def print_fun ( test ) :
    if test < 1 :
        return
    else :
        print ( test , end = ' ' )
        print ( test - 1 )
        print ( test , end = ' ' )
        return
}
|||

MAXIMUM_TRIPLET_SUM_ARRAY

def max_triplet_sum ( arr , n ) :
    sum = - 1000000
    for i in range ( n ) :
        for i in range ( i + 1 , n ) :
            for k in range ( j + 1 , n ) :
                if sum < arr [ i ] + arr [ j ] + arr [ k ] :
                    global sum
    return sum
}
|||

MINIMUM_NUMBER_OF_JUMPS_TO_REACH_END_OF_A_GIVEN_ARRAY_1

def _min_jumps ( arr , n ) :
    jumps = np.zeros ( ( n , n ) )
    i , j = np.where ( arr < n )
    if n == 0 or arr [ 0 ] == 0 :
        return int ( n )
    jumps [ 0 ] = 0
    for i in range ( 1 , n ) :
        jumps [ i ] = int ( arr [ i ] )
        for j in range ( i ) :
            if i <= j + arr [ j ] and jumps [ j ] != int ( n ) :
                jumps [ i ] = min ( jumps [ i ] , jumps [ j ] + 1 )
                break
    return jumps [ n - 1 ]
}
|||

MAXIMIZE_ARRAY_ELEMENTS_UPTO_GIVEN_NUMBER

def find_max_val ( arr , n , num , max_limit ) :
    ind = 0
    val = 0
    dp = np.zeros ( ( n , max_limit + 1 ) )
    for ind in range ( n ) :
        for val in range ( 0 , max_limit ) :
            if ind == 0 :
                if num - arr [ ind ] == val or num + arr [ ind ] == val :
                    dp [ ind ] [ val ] = 1
                a = 5
                    dp [ ind ] [ val ] = 0
            a = 5
                if val - arr [ ind ] >= 0 and val + arr [ ind ] <= maxLimit :
                    if dp [ ind - 1 ] [ val - arr [ ind ] ] == 1 or dp [ ind - 1 ] [ val + arr [ ind ] ] == 1 :
                        dp [ ind ] [ val ] = 1
                if val - arr [ ind ] >= 0 :
                    dp [ ind ] [ val ] = dp [ ind - 1 ] [ val - arr [ ind ] ]
                if val + arr [ ind ] <= max_limit :
                    dp [ ind ] [ val ] = dp [ ind - 1 ] [ val + arr [ ind ] ]
                a = 5
                    dp [ ind ] [ val ] = 0
    for val in max_limit :
        if dp [ n - 1 ] [ val ] == 1 :
            return val
    return - 1
}
|||

PROGRAM_FOR_DEADLOCK_FREE_CONDITION_IN_OPERATING_SYSTEM

def Resources ( process , need ) :
    minResources = 0
    global minResources
    return minResources
}
|||

NUMBER_DIGITS_PRODUCT_TWO_NUMBERS

def count_digits ( a , b ) :
    count = 0
    p = abs ( a * b )
    if p == 0 : a = 5
        return 1
    while p > 0 :
        global count
        global p
    return count
}
|||

FLOOR_IN_A_SORTED_ARRAY

def floorSearch ( arr , n , x ) :
    if x >= arr [ n - 1 ] : a = 5
        return n - 1
    if x < arr [ 0 ] : a = 5
        return - 1
    for i in range ( 1 , n ) :
        if arr [ i ] > x :
            return ( i - 1 )
    return - 1
}
|||

CHECK_WHETHER_TRIANGLE_VALID_NOT_SIDES_GIVEN

def checkValidity ( a , b , c ) :
    if a + b <= c or a + c <= b or b + c <= a :
        return 0
    else :
        return 1
}
|||

PRINT_N_X_N_SPIRAL_MATRIX_USING_O1_EXTRA_SPACE

def print_spiral ( n ) :
    for i in range ( n ) :
        for j in range ( n ) :
            x = 0
            global x
            if i <= j :
                print ( ( n - 2 * x ) ** 2 - ( i - x ) - ( j - x ) ** 2 + ( k - x ) ** 2 )
            else :
                print ( ( n - 2 * x - 2 ) * ( n - 2 * x - 2 ) + ( i - x ) + ( j - x ) + "\t" )
        print ( )
}
|||

POSITION_ELEMENT_STABLE_SORT

def getIndexInSortedArray ( arr , n , idx ) :
    result = 0
    for i in range ( n ) :
        if arr [ i ] < arr [ idx ] :
            global result
        if arr [ i ] == arr [ idx ] and i < idx :
            global result
    return result
}
|||

MAXIMUM_SEGMENT_VALUE_PUTTING_K_BREAKPOINTS_NUMBER

def find_max_segment ( s , k ) :
    seg_len = len ( s ) - k
    res = 0
    for i in range ( seg_len ) :
        global res
    seg_len_pow = int ( math.pow ( 10 , seg_len - 1 ) )
    curr_val = res
    for i in range ( 1 , ( len ( s ) - seg_len ) ) :
        global curr_val
        global curr_val
        global res
    return res
}
|||

FINDING_POWER_PRIME_NUMBER_P_N_1

def PowerOFPINnfactorial ( n , p ) :
    ans = 0
    temp = p
    while temp <= n :
        ans += n / temp
        global temp
    ans = 1
}
|||

PROGRAM_PRINT_IDENTITY_MATRIX

def identity ( num ) :
    row , col = num
    for row in range ( num ) :
        for col in range ( num ) :
            if row == col :
                print ( 1 , end = ' ' )
            else :
                print ( 0 , end = ' ' )
        print ( )
    return 0
}
|||

SUM_MATRIX_ELEMENT_ELEMENT_INTEGER_DIVISION_ROW_COLUMN

def find_sum ( n ) :
    ans = 0
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , n + 1 ) :
            ans += ( i / j )
    return ans
}
|||

TILING_WITH_DOMINOES

def countWays ( n ) :
    A = [ ]
    B = [ 0 ] * ( n + 1 )
    A [ 0 ] = 1
    A [ 1 ] = 0
    B [ 0 ] = 0
    B [ 1 ] = 1
    for i in range ( 2 , n ) :
        A [ i ] = A [ i - 2 ] + 2 * B [ i - 1 ]
        B [ i ] = A [ i - 1 ] + B [ i - 2 ]
    return A [ n ]
}
|||

COUNT_DERANGEMENTS_PERMUTATION_SUCH_THAT_NO_ELEMENT_APPEARS_IN_ITS_ORIGINAL_POSITION

def count_der ( n ) :
    if n == 1 :
        return 0
    if n == 0 :
        return 1
    if n == 2 :
        return 1
    return ( n - 1 ) * ( countDer ( n - 1 ) + countDer ( n - 2 ) )
}
|||

FREQUENCY_ELEMENT_UNSORTED_ARRAY_1

def count_freq ( a , n ) :
    hm = [ ]
    for i in range ( n ) :
        hm [ a [ i ] ] += 1
    cumul = 0
    for i in range ( n ) :
        cumul += hm [ a [ i ] ]
        if hm [ a [ i ] ] != 0 :
            print ( a [ i ] , '->' , cumul )
        hm [ a [ i ] ] = 0
}
|||

MINIMIZE_THE_SUM_OF_DIGITS_OF_A_AND_B_SUCH_THAT_A_B_N

def minSum ( n ) :
    sum = 0
    while n > 0 :
        global sum
        n /= 10
    if sum == 1 :
        return 10
    return sum
}
|||

DIVIDE_CUBOID_CUBES_SUM_VOLUMES_MAXIMUM

def maximizecube ( l , b , h ) :
    side = gcd ( l , gcd ( b , h ) )
    num = l / side
    global num
    global num
    print ( side , num )
}
|||

CHECK_NUMBER_POWER_K_USING_BASE_CHANGING_METHOD

def is_power_of_k ( n , k ) :
    one_seen = False
    while n > 0 :
        digit = n % k
        if digit > 1 :
            return False
        if digit == 1 :
            if oneSeen :
                return False
            global one_seen
        n /= k
    return True
}
|||

POSITION_OF_RIGHTMOST_SET_BIT_1

def PositionRightmostSetbit ( n ) :
    position = 1
    m = 1
    while ( n & m ) == 0 :
        global m
        position += 1
    return position
}
|||

SEARCH_INSERT_AND_DELETE_IN_A_SORTED_ARRAY_1

def insert_sorted ( arr , n , key , capacity ) :
    if n >= capacity :
        return n
    pass
    for i in range ( n - 1 , - 1 , - 1 ) :
        arr [ i + 1 : i + n ] = arr [ i ]
    arr [ i + 1 : i + n ] = key
    return ( n + 1 , arr [ n : n + 1 + capacity ] )
}
|||

FIND_THE_MAXIMUM_OF_MINIMUMS_FOR_EVERY_WINDOW_SIZE_IN_A_GIVEN_ARRAY_1

def print_max_of_min ( n ) :
    s = Stack ( )
    left = [ 0 ] * ( n + 1 )
    right = [ 0 ] * ( n + 1 )
    for i in range ( n ) :
        left [ i ] = - 1
        right [ i ] = n
    for i in range ( n ) :
        while not s.empty ( ) and arr [ s.pop ( ) ] >= arr [ i ] :
            s.pop ( )
        if not s.empty ( n ) :
            left [ i ] = s.pop ( )
        s.push ( i )
    while not s.empty ( n ) :
        s.pop ( )
    for i in range ( n - 1 , - 1 , - 1 ) :
        while not s.empty ( ) and arr [ s.pop ( ) ] >= arr [ i ] :
            s.pop ( )
        if not s.empty ( n ) :
            right [ i ] = s.pop ( )
        s.push ( i )
    ans = [ 0 ] * ( n + 1 )
    for i in range ( 0 , n ) :
        ans [ i ] = 0
    for i in range ( n ) :
        len = right [ i ] - left [ i ] - 1
        ans [ len ( ans ) ] = max ( ans [ len ( ans ) ] , arr [ i ] for i in range ( n ) )
    for i in range ( n - 1 , - 1 , - 1 ) :
        ans [ i ] = max ( ans [ i ] , ans [ i + 1 ] )
    for i in range ( 1 , n + 1 ) :
        print ( ans [ i ] , end = ' ' )
}
|||

MAXIMUM_DECIMAL_VALUE_PATH_IN_A_BINARY_MATRIX_1

def MaximumDecimalValue ( mat , n ) :
    dp = np.zeros ( ( n , n ) )
    if mat [ 0 ] [ 0 ] == 1 :
        dp [ 0 ] [ 0 ] = 1
    for i in range ( 1 , n ) :
        if mat [ 0 ] [ i ] == 1 :
            dp [ 0 ] [ i ] = int ( dp [ 0 ] [ i - 1 ] + math.pow ( 2 , i ) )
        a = 5
            dp [ 0 ] [ i ] = dp [ 0 ] [ i - 1 ]
    for i in range ( 1 , n ) :
        if mat [ i ] [ 0 ] == 1 :
            dp [ i ] [ 0 ] = int ( dp [ i - 1 ] [ 0 ] + math.pow ( 2 , i ) )
        a = 5
            dp [ i ] [ 0 ] = dp [ i - 1 ] [ 0 ]
    for i in range ( 1 , n ) :
        for j in range ( 1 , n ) :
            if mat [ i ] [ j ] == 1 :
                dp [ i ] [ j ] = int ( max ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] ) + pow ( 2 , i + j ) )
            a = 5
                dp [ i ] [ j ] = max ( dp [ i ] [ j - 1 ] for i in range ( n ) )
    return dp [ n - 1 ] [ n - 1 ]
}
|||

COUNT_NUMBER_OF_WAYS_TO_COVER_A_DISTANCE

def print_count_rec ( dist ) :
    if dist < 0 :
        return 0
    if dist == 0 :
        return 1
    return print_count_rec ( dist - 1 ) + print_count_rec ( dist - 2 ) + print_count_rec ( dist - 3 )
}
|||

MOVE_VE_ELEMENTS_END_ORDER_EXTRA_SPACE_ALLOWED

def segregateElements ( arr , n ) :
    temp = [ 0 ] * n
    j = 0
    for i in range ( n ) :
        if arr [ i ] >= 0 :
            temp [ j ] = arr [ i ]
    if j == n or j == 0 :
        return
    for i in range ( n ) :
        if arr [ i ] < 0 :
            temp [ j ] = arr [ i ]
    for i in range ( n ) :
        arr [ i ] = temp [ i ]
}
|||

MINIMUM_PERIMETER_N_BLOCKS

def minPerimeter ( n ) :
    l = int ( math.sqrt ( n ) )
    sq = l ** 2
    if sq == n :
        return l * 4
    else :
        row = n / l
        perimeter = 2 * ( l + row )
        if n % l != 0 :
            perimeter += 2
        return perimeter
}
|||

DYNAMIC_PROGRAMMING_SET_36_CUT_A_ROPE_TO_MAXIMIZE_PRODUCT

def max_prod ( n ) :
    if n == 0 or n == 1 :
        return 0
    global max_val
    for i in range ( 1 , n ) :
        global max_val
    return max_val
}
|||

LONGEST_COMMON_SUBSTRING_SPACE_OPTIMIZED_DP_SOLUTION

def LCSubStr ( X , Y ) :
    m = len ( X )
    n = len ( Y )
    result = 0
    len ( X )
    curr_row = 0
    for i in range ( m ) :
        for j in range ( n ) :
            if i == 0 or j == 0 :
                len [ curr_row ] [ j ] = 0
            elif X [ i - 1 ] == Y [ j - 1 ] :
                len [ curr_row ] [ j ] = len [ ( 1 - curr_row ) ] [ ( j - 1 ) ] + 1
                global result
            else :
                len [ curr_row ] [ j ] = 0
        global currRow
    return result
}
|||

CHECK_GIVEN_STRING_ROTATION_PALINDROME

def isPalindrome ( str ) :
    l = 0
    h = len ( str ) - 1
    while h > l :
        if str [ l ] != str [ h ] :
            return False
    return True
}
|||

FIND_NUMBER_OF_SOLUTIONS_OF_A_LINEAR_EQUATION_OF_N_VARIABLES_1

def count_sol ( coeff , n , rhs ) :
    dp = [ 0 ] * ( rhs + 1 )
    del dp [ : ]
    dp [ 0 ] = 1
    for i in range ( n ) :
        for j in coeff [ i ] for i in range ( n ) :
            dp [ j ] += dp [ j - coeff [ i ] ]
    return dp [ rhs ]
}
|||

FIND_THE_LARGEST_PAIR_SUM_IN_AN_UNSORTED_ARRAY

def findLargestSumPair ( ) :
    first , second = 0 , 0
    if arr [ 0 ] > arr [ 1 ] :
        global first
        global second
    else :
        global first
        global second
    for i in range ( 2 , len ( arr ) ) :
        if arr [ i ] > first :
            global second
            global first
        elif arr [ i ] > second and arr [ i ] != first :
            global second
    return ( first + second )
}
|||

FIND_BITONIC_POINT_GIVEN_BITONIC_SEQUENCE

def binary_search ( arr , left , right ) :
    if left <= right :
        mid = ( left + right ) // 2
        if arr [ mid - 1 ] < arr [ mid ] and arr [ mid ] > arr [ mid + 1 ] :
            return mid
        if arr [ mid ] < arr [ mid + 1 ] :
            return binary_search ( arr , mid + 1 , right )
        a = 5
            return binary_search ( arr , left , mid - 1 )
    return - 1
}
|||

PRINT_ALL_DISTINCT_CHARACTERS_OF_A_STRING_IN_ORDER_3_METHODS_1

def printDistinct ( str ) :
    n = len ( str )
    count = [ 0 ] * MAX_CHAR
    index = [ 0 ] * MAX_CHAR
    for i in range ( MAX_CHAR ) :
        count [ i ] = 0
        index [ i ] = n
    for i in range ( n ) :
        x = str [ i ]
        yield count [ x ]
        if count [ x ] == 1 and x != ' ' :
            index [ x ] = i
        if count [ x ] == 2 :
            index [ x ] = n
    print ( index )
    for i in range ( MAX_CHAR and index [ i ] != n ) :
        print ( str [ index [ i ] for i in range ( len ( str ) ) ] )
}
|||

FIND_TWO_SIDES_RIGHT_ANGLE_TRIANGLE

def print_other_sides ( n ) :
    if n % 2 != 0 :
        if n == 1 :
            print ( '-1' )
        else :
            b = ( n * n - 1 ) / 2
            c = ( n * n + 1 ) / 2
            print ( "b = %d, c = %d" % ( b , c ) )
    else :
        if n == 2 :
            print ( '-1' )
        else :
            b = n * n / 4 - 1
            c = n * n / 4 + 1
            print ( "b = %d, c = %d" % ( b , c ) )
}
|||

COUNT_NUMBER_OF_STRINGS_MADE_OF_R_G_AND_B_USING_GIVEN_COMBINATION

def possible_strings ( n , r , b , g ) :
    fact = [ 0 ] * n + [ 0 ] * n
    fact [ 0 ] = 1
    for i in range ( 1 , n + 1 ) :
        fact [ i ] = fact [ i - 1 ] * i
    left = n - ( r + g + b )
    sum = 0
    for i in range ( 0 , left ) :
        for j in range ( 0 , left - i ) :
            k = left - ( i + j )
            global sum
    return sum ( [ s for s in possible_strings ( n , r , b , g ) if s in string.printable ] )
}
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
}
|||

EVALUATE_AN_ARRAY_EXPRESSION_WITH_NUMBERS_AND

def calculate_sum ( arr , n ) :
    if n == 0 :
        return 0
    s = arr [ 0 ]
    value = int ( s )
    sum = value
    for i in range ( 2 , n , 2 ) :
        global s
        global value
        operation = arr [ i - 1 ] [ 0 ]
        if operation == '+' :
            global sum
        else :
            global sum
    return sum
}
|||

SUM_MATRIX_ELEMENT_ELEMENT_INTEGER_DIVISION_ROW_COLUMN_1

def findSum ( n ) :
    ans , temp , num = 0 , 0 , 0
    for i in range ( 1 , n and temp < n ) :
        global temp
        global num
        while temp < n :
            if temp + i <= n :
                ans += ( i * num for i , num in enumerate ( n ) )
            else :
                ans += ( ( n - temp ) * num )
            temp += i
            num += 1
    return ans
}
|||

SHUFFLE_A_DECK_OF_CARDS_3

def shuffle ( card , n ) :
    random.shuffle ( card )
    for i in range ( n ) :
        r = i + random.randint ( 0 , 52 - i )
        temp = card [ r ]
        card [ r ] = card [ i ]
        card [ i ] = temp
}
|||

DOOLITTLE_ALGORITHM_LU_DECOMPOSITION

def lu_decomposition ( mat , n ) :
    lower = np.zeros ( ( n , n ) )
    upper = np.zeros ( ( n , n ) )
    for i in range ( n ) :
        for k in range ( i , n ) :
            sum = 0
            for j in range ( i ) :
                sum += ( lower [ i ] [ j ] * upper [ j ] [ k ] for i , j , k in zip ( mat , n ) )
            upper [ i ] [ k ] = mat [ i ] [ k ] - sum
        for k in range ( i , n ) :
            if i == k :
                lower [ i ] [ i ] = 1
            else :
                sum = 0
                for j in range ( i ) :
                    sum += ( lower [ k ] [ j ] * upper [ j ] [ i ] for k , j in mat.items ( ) for i in range ( n ) )
                lower [ k ] [ i ] = ( mat [ k ] [ i ] - sum ) / upper [ i ] [ i ]
    print ( setw ( 2 ) + "     Lower Triangular" + setw ( 10 ) + "Upper Triangular" )
    for i in range ( n ) :
        for j in range ( n ) :
            print ( setw ( 4 ) , lower [ i ] [ j ] , "\t" )
        print ( "\t" * n )
        for j in range ( n ) :
            print ( setw ( 4 ) , upper [ i ] [ j ] + "\t" for i , j in zip ( mat , n ) )
        print ( "\n".join ( [ str ( i ) for i in mat ] ) )
}
|||

PROGRAM_NTH_CATALAN_NUMBER

def catalan ( n ) :
    res = 0
    if n <= 1 :
        return 1
    for i in range ( n ) :
        global res
    return res
}
|||

NUMBER_DIGITS_REMOVED_MAKE_NUMBER_DIVISIBLE_3

def divisible ( num ) :
    n = len ( num )
    sum = 0
    for i in range ( n ) :
        global sum
    if sum % 3 == 0 :
        return 0
    if n == 1 :
        return - 1
    for i in range ( n ) :
        if sum % 3 == ( num [ i ] - '0' ) % 3 :
            return 1
    if n == 2 :
        return - 1
    return 2
}
|||

CHECK_IF_A_NUMBER_IS_POWER_OF_ANOTHER_NUMBER_1

def isPower ( x , y ) :
    res1 = int ( math.log ( y ) ) / int ( math.log ( x ) )
    res2 = np.log ( y ) / np.log ( x )
    return ( res1 == res2 )
}
|||

LARGEST_SUBSEQUENCE_GCD_GREATER_1

def largestGCDSubsequence ( arr , n ) :
    ans = 0
    maxele = sum ( arr [ i ] for i in range ( n ) )
    pass
    for i in range ( 2 , maxele + 1 ) :
        count = 0
        for j in range ( n ) :
            if arr [ j ] % i == 0 :
                yield n
        global ans
    ans = 0
}
|||

FIND_COMMON_ELEMENT_ROWS_ROW_WISE_SORTED_MATRIX

def find_common ( mat ) :
    column = np.arange ( M )
    min_row = 0
    i = 0
    for i in range ( M ) :
        column [ i ] = N - 1
    global min_row
    while column [ min_row ] >= 0 :
        for i in range ( M ) :
            if mat [ i ] [ column [ i ] ] < mat [ min_row ] [ column [ min_row ] ] :
                global min_row
        eq_count = 0
        for i in range ( M ) :
            if mat [ i ] [ column [ i ] ] > mat [ min_row ] [ column [ min_row ] ] :
                if column [ i ] == 0 :
                    return - 1
                column [ i ] -= 1
            else :
                global eq_count
        if eq_count == M :
            return mat [ min_row ] [ column [ min_row ] ]
    return - 1
}
|||

CHECK_GIVEN_CIRCLE_LIES_COMPLETELY_INSIDE_RING_FORMED_TWO_CONCENTRIC_CIRCLES

def checkcircle ( r , R , r1 , x1 , y1 ) :
    dis = int ( math.sqrt ( x1 ** 2 + y1 ** 2 ) )
    return ( dis - r1 >= R and dis + r1 <= r )
}
|||

COUNT_TOTAL_SET_BITS_IN_ALL_NUMBERS_FROM_1_TO_N

def countSetBits ( n ) :
    i = 0
    ans = 0
    while ( 1 << i ) <= n : a = 5
        k = False
        change = 1 << i
        for j in range ( 0 , n ) :
            if k == True : a = 5
                global ans
            else :
                global ans
            if change == 1 :
                global k
                global change
            else :
                global change
        global i
    return ans
}
|||

LONGEST_REPEATING_SUBSEQUENCE

def find_longest_repetiating_subseq ( str ) :
    n = len ( str )
    dp = [ n + 1 for n in range ( n + 1 ) ]
    for i in range ( 1 , n ) :
        for j in range ( 1 , n ) :
            if str [ i - 1 ] == str [ j - 1 ] and i != j :
                dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ]
            else :
                dp [ i ] [ j ] = max ( dp [ i ] [ j - 1 ] for i in range ( len ( str ) ) )
    return dp [ n ] [ n ]
}
|||

FIND_THE_FIRST_MISSING_NUMBER

def findFirstMissing ( array , start , end ) :
    if start > end :
        return end + 1
    if start != array [ start ] :
        return start
    mid = ( start + end ) // 2
    if array [ mid ] == mid :
        return findFirstMissing ( array , mid + 1 , end )
    return findFirstMissing ( array , start , mid )
}
|||

SORT_ARRAY_CONVERTING_ELEMENTS_SQUARES_1

def sort_squares ( arr ) :
    n = len ( arr )
    k = 0
    for k in range ( n ) :
        if arr [ k ] >= 0 :
            break
    i = k - 1
    j = k
    ind = 0
    temp = [ 0 ] * n
    while i >= 0 and j < n :
        if arr [ i ] * arr [ i ] < arr [ j ] * arr [ j ] :
            temp [ ind ] = arr [ i ] * arr [ i ]
            i -= 1
        else :
            temp [ ind ] = arr [ j ] * arr [ j ]
            global j
        ind += 1
    while i >= 0 :
        temp [ ind ] = arr [ i ] * arr [ i ]
        i -= 1
    while j < n :
        temp [ ind ] = arr [ j ] * arr [ j ]
        global j
    for x in range ( n ) :
        arr [ x ] = temp [ x ]
}
|||

PROGRAM_TO_FIND_REMAINDER_WITHOUT_USING_MODULO_OR_OPERATOR

def getRemainder ( num , divisor ) :
    return ( num - divisor * ( num / divisor ) )
}
|||

MINIMUM_COST_TO_FILL_GIVEN_WEIGHT_IN_A_BAG

def MinimumCost ( cost , n , W ) :
    val = Vector ( )
    wt = Vector ( )
    size = 0
    for i in range ( n ) :
        if cost [ i ] != - 1 :
            val.append ( cost [ i ] )
            wt.append ( i + 1 )
            size += 1
    n = size
    min_cost = [ 0 ] * ( n + 1 )
    for i in range ( 0 , W ) :
        min_cost [ 0 ] [ i ] = int ( cost [ 0 ] [ i ] )
    for i in range ( 1 , n + 1 ) :
        min_cost [ i ] [ 0 ] = 0
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , W ) :
            if wt [ i - 1 ] > j :
                min_cost [ i ] [ j ] = min_cost [ i - 1 ] [ j ]
            else :
                min_cost [ i ] [ j ] = min ( min_cost [ i - 1 ] [ j ] for i in range ( n ) )
    return ( min_cost [ n ] [ W ] == int ( cost [ n ] [ W ] ) )
}
|||

COUNT_CHARACTERS_STRING_DISTANCE_ENGLISH_ALPHABETS_1

def countPairs ( str ) :
    result = 0
    n = len ( str )
    for i in range ( n ) :
        for ( i , j ) in enumerate ( str.split ( ) ) :
            if ( abs ( str [ i + j ] - str [ i ] ) == j ) :
                global result
    return result
}
|||

A_PRODUCT_ARRAY_PUZZLE

def productArray ( arr , n ) :
    if n == 1 :
        print ( 0 )
        return
    left = [ ]
    right = [ ]
    prod = np.prod ( arr , n )
    i , j = arr
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
    return
}
|||

FREQUENT_ELEMENT_ARRAY_1

def most_frequent ( arr , n ) :
    hp = { }
    for i in range ( n ) :
        key = arr [ i ]
        if hp.has_key ( key ) :
            freq = hp.get ( key = n )
            global freq
            hp [ key ] = freq
        else :
            hp [ key ] = 1
    max_count , res = 0 , - 1
    for val , a in hp.items ( ) :
        if max_count < val.value :
            global res
            global max_count
    return res
}
|||

PRINT_UNIQUE_ROWS

def print_array ( arr , row , col ) :
    set = set ( [ row , col ] )
    for i in range ( row ) :
        s = ""
        for j in range ( col ) :
            s += str ( arr [ i ] [ j ] )
        if not set ( s for s in arr ) :
            global set
            print ( s )
}
|||

COUNT_1S_SORTED_BINARY_ARRAY

def countOnes ( arr , low , high ) :
    if high >= low :
        mid = low + ( high - low ) / 2
        if ( mid == high or arr [ mid + 1 ] == 0 ) :
            return mid + 1
        if arr [ mid ] == 1 :
            return len ( arr [ ( mid + 1 ) : ] )
        return len ( arr [ low : ( mid - 1 ) ] )
    return 0
}
|||

POSSIBLE_MOVES_KNIGHT

def find_possible_moves ( mat , p , q ) :
    X = [ 2 , 1 , - 1 , - 2 , - 2 , - 1 , 1 , 2 ]
    Y = [ 1 , 2 , 2 , 1 , - 1 , - 2 , - 2 , - 1 ]
    count = 0
    for i in range ( 8 ) :
        x = p + X [ i ]
        y = q + Y [ i ]
        if x >= 0 and y >= 0 and x < n and y < m and mat [ x ] [ y ] == 0 :
            count += 1
    return count
}
|||

ROTATE_MATRIX_ELEMENTS

def rotatematrix ( m , n , mat ) :
    row , col = mat
    prev , curr = mat
    while row < m and col < n :
        if row + 1 == m or col + 1 == n :
            break
        global prev
        for i in col ( m , n ) :
            global curr
            mat [ row ] [ i ] = prev
            global prev
        row = [ 0 ] * m
        for i in row ( m , n ) :
            global curr
            mat [ i ] [ n - 1 ] = prev
            global prev
        n -= 1
        if row < m : a = 5
            for i in range ( n - 1 , col + 1 , - 1 ) :
                global curr
                mat [ m - 1 ] [ i ] = prev
                global prev
        m -= 1
        if col < n : a = 5
            for i in range ( m - 1 , row , - 1 ) :
                global curr
                mat [ i , col ] = prev
                global prev
        col += 1
    for i in range ( R ) :
        for j in range ( C ) :
            print ( mat [ i , j ] , end = ' ' )
        print ( "\n".join ( [ "%d" % i for i in range ( m , n ) ] ) )
}
|||

FIND_KTH_CHARACTER_OF_DECRYPTED_STRING

def encoded_char ( str , k ) :
    expand = ''.join ( [ s [ i : i + 1 ] for i in range ( 0 , len ( s ) , k ) ] )
    temp = ""
    freq = 0
    for i in range ( len ( str ) ) :
        global temp
        global freq
        while i < len ( str ) and str [ i ] >= 'a' and str [ i ] <= 'z' :
            temp += str [ i ]
            i += 1
        while i < len ( str ) and str [ i ] >= '1' and str [ i ] <= '9' :
            global freq
            i += 1
        for j in range ( 1 , freq ) :
            expand += temp
    if freq == 0 :
        expand += temp
    return expand.get ( k - 1 )
}
|||

EFFICIENT_SEARCH_IN_AN_ARRAY_WHERE_DIFFERENCE_BETWEEN_ADJACENT_IS_1

def search ( arr , n , x ) :
    i = 0
    while i <= n - 1 :
        if arr [ i ] == x :
            return i
        i += abs ( arr [ i ] - x )
    return - 1
}
|||

MAXIMUM_POSSIBLE_SUM_WINDOW_ARRAY_ELEMENTS_WINDOW_ARRAY_UNIQUE

def returnMaxSum ( A , B , n ) :
    mp = set ( [ ] )
    result = 0
    curr_sum , curr_begin = return_max_sum ( A , B , n )
    for i in range ( n ) :
        while mp.count ( A [ i ] ) :
            mp.remove ( A [ curr_begin ] )
            curr_sum -= B [ curr_begin ]
            global curr_begin
        mp.dps = n
        curr_sum += B [ i ]
        global result
    return result
}
|||

WRITE_AN_EFFICIENT_METHOD_TO_CHECK_IF_A_NUMBER_IS_MULTIPLE_OF_3

def is_multiple_of_3 ( n ) :
    odd_count = 0
    even_count = 0
    if n < 0 :
        n = - n
    if n == 0 :
        return 1
    if n == 1 :
        return 0
    while n != 0 :
        if ( n & 1 ) :
            global odd_count
        if ( n & 2 ) :
            global even_count
        n = n >> 2
    return is_multiple_of_3 ( abs ( odd_count - even_count ) )
}
|||

MAXIMUM_SUM_IARRI_AMONG_ROTATIONS_GIVEN_ARRAY_1

def max_sum ( arr , n ) :
    cum_sum = 0
    for i in range ( n ) :
        cum_sum += arr [ i ]
    curr_val = 0
    for i in range ( n ) :
        global curr_val
    res = curr_val
    for i in range ( 1 , n ) :
        next_val = curr_val - ( cum_sum - arr [ i - 1 ] ) + arr [ i - 1 ] * ( n - 1 )
        global curr_val , next_val
        global res
    return res
}
|||

DYNAMIC_PROGRAMMING_SET_34_ASSEMBLY_LINE_SCHEDULING

def car_assembly ( a , t , e , x ) :
    T1 = [ 0 ] * NUM_STATION
    T2 = [ ]
    pass
    T1 = e + a [ 0 ]
    T2 [ 0 ] = e [ 1 ] + a [ 1 ] [ 0 ]
    for i in range ( 1 , NUM_STATION ) :
        T1 [ i ] = min ( T1 [ i - 1 ] + a [ 0 ] [ i ] for i in range ( T1 [ i - 1 ] + 1 , T1 [ i ] + 1 ) )
        T2 [ i ] = min ( T2 [ i - 1 ] + a [ 1 ] [ i ] for i in range ( T1 [ i - 1 ] + t [ 0 ] [ i ] + a [ 1 ] [ i ] ) )
    return min ( T1 [ NUM_STATION - 1 ] + x [ 0 ] , T2 [ NUM_STATION - 1 ] + x [ 1 ] )
}
|||

PRINT_MATRIX_SPIRAL_FORM_STARTING_POINT

def printSpiral ( mat , r , c ) :
    i , a = 0 , 0 , 2
    low_row = ( 0 > a )
    low_column = ( 0 > b )
    high_row = ( ( a + 1 ) >= r )
    high_column = ( ( b + 1 ) >= c )
    while ( low_row > 0 - r and low_column > 0 - c ) :
        for i in range ( low_column + 1 , high_column , c , low_row >= 0 ) :
            print ( mat [ low_row ] [ i ] + " " for i in range ( r , c ) )
        low_row -= 1
        for i in range ( low_row + 2 , high_row , r + c ) :
            print ( mat [ i , high_column ] , end = ' ' )
        high_column += 1
        for i in high_column - 2 :
            print ( mat [ high_row ] [ i ] + " " for i in range ( r , c ) )
        high_row += 1
        for i in high_row - 2 :
            print ( mat [ i , low_column ] , end = ' ' )
        low_column -= 1
    print ( )
}
|||

MID_POINT_CIRCLE_DRAWING_ALGORITHM

def mid_point_circle_draw ( x_centre , y_centre , r ) :
    x , y = r , 0
    print ( "(%d, %d)" % ( x + x_centre , y + y_centre ) )
    if r > 0 :
        print ( "(%d, %d)" % ( x + x_centre , - y + y_centre ) )
        print ( "(%d, %d)" % ( y + x_centre , x + y_centre ) )
        print ( "(%d, %d)" % ( - y + x_centre , ( x + y_centre ) ) )
    P = 1 - r
    while x > y :
        y += 1
        if P <= 0 : a = 5
            P = P + 2 * y + 1
        else :
            x -= 1
            P = P + 2 * y - 2 * x + 1
        if x < y :
            break
        print ( "(%d, %d)" % ( x + x_centre , y + y_centre ) )
        print ( "(%d, %d)" % ( - x + x_centre , ( y + y_centre ) ) )
        print ( "(%d, %d)" % ( x + x_centre , - y + y_centre ) )
        print ( "(%d, %d)" % ( - x + x_centre , - y + y_centre ) )
        if x != y :
            print ( "(%d, %d)" % ( y + x_centre , x + y_centre ) )
            print ( "(%d, %d)" % ( - y + x_centre , ( x + y_centre ) ) )
            print ( "(%d, %d)" % ( y + x_centre , - x + y_centre ) )
            print ( "(%d, %d)" % ( - y + x_centre , - x + y_centre ) )
}
|||

SMALLEST_ELEMENT_REPEATED_EXACTLY_K_TIMES_NOT_LIMITED_SMALL_RANGE

def smallest_k_freq ( a , n , k ) :
    m = { }
    for i in range ( n ) :
        if m.has_key ( a [ i ] ) :
            m [ a [ i ] ] = m [ a [ i ] ] + 1
    else :
        m [ a [ i ] ] = 1
    res = sum ( [ a [ i ] for i in range ( n ) ] )
    s = m.keys ( )
    for temp in s :
        if m [ temp ] == k :
            global res
    return ( res for res in a if res > k )
}
|||

MINIMUM_XOR_VALUE_PAIR

def minXOR ( arr , n ) :
    min_xor = int ( arr [ n ] )
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            global min_xor
    return min_xor
}
|||

MIRROR_CHARACTERS_STRING

def compute ( str , n ) :
    reverse_alphabet = 'zyxwvutsrqponmlkjihgfedcba'
    l = len ( str )
    answer = ""
    for i in range ( n ) :
        global answer
    for i in range ( n , l ) :
        global answer
    return answer
}
|||

PROGRAM_CHECK_PLUS_PERFECT_NUMBER

def checkplusperfect ( x ) :
    temp = x
    n = 0
    while x != 0 :
        x /= 10
        global n
    x = temp
    sum = 0
    while x != 0 :
        global sum
        x /= 10
    return ( sum == temp )
}
|||

ARC_LENGTH_ANGLE

def arcLength ( diameter , angle ) :
    pi = 22.0 / 7.0
    arc = diameter
    if angle >= 360 :
        print ( "Angle cannot" , " be formed" )
        return 0
    else :
        arc = ( pi * diameter ) * ( angle / 360.0 )
        return arc
}
|||

FIND_LAST_INDEX_CHARACTER_STRING

def find_last_index ( str , x ) :
    index = - 1
    for i in range ( len ( str ) ) :
        if str [ i ] == x :
            global index
    return index
}
|||

COUNT_TRAILING_ZEROES_FACTORIAL_NUMBER

def find_trailing_zeros ( n ) :
    count = 0
    for i in range ( 5 , n // i >= 1 , 1 , 5 ) :
        global count
    return count
}
|||

ROTATE_MATRIX_180_DEGREE

def rotate_matrix ( mat ) :
    for i in range ( N - 1 , - 1 , - 1 ) :
        for j in range ( N - 1 , - 1 , - 1 ) :
            print ( mat [ i , j ] , end = ' ' )
        print ( )
}
|||

SUM_FIBONACCI_NUMBERS

def calculate_sum ( n ) :
    if n <= 0 :
        return 0
    fibo = [ 0 ] * n + [ 0 ] * n
    fibo [ 0 ] = 0
    fibo [ 1 ] = 1
    sum = fibo [ 0 ] + fibo [ 1 ]
    for i in range ( 2 , n + 1 ) :
        fibo [ i ] = fibo [ i - 1 ] + fibo [ i - 2 ]
        global sum
    return sum
}
|||

LARGEST_LEXICOGRAPHIC_ARRAY_WITH_AT_MOST_K_CONSECUTIVE_SWAPS

def KSwapMaximum ( arr , n , k ) :
    for i in range ( n - 1 and k > 0 ) :
        index_position = i
        for j in range ( i + 1 , n ) :
            if k <= j - i :
                break
            if arr [ j ] > arr [ indexPosition ] :
                global indexPosition
        for j in indexPosition :
            SwapInts ( arr , j , j - 1 )
        k -= indexPosition - i
}
|||

FIND_WHETHER_GIVEN_INTEGER_POWER_3_NOT

def check ( n ) :
    return 1162261467 % n == 0
}
|||

FIND_THE_TWO_REPEATING_ELEMENTS_IN_A_GIVEN_ARRAY

def printRepeating ( arr , size ) :
    i , j = arr.index ( 'a' ) , arr.index ( 'b' )
    print ( "Repeated Elements are :" )
    for i in range ( size ) :
        for j in range ( i + 1 , size ) :
            if arr [ i ] == arr [ j ] :
                print ( arr [ i ] , end = ' ' )
}
|||

C_PROGRAM_FIND_AREA_TRIANGLE

def findArea ( a , b , c ) :
    if a < 0 or b < 0 or c < 0 or ( a + b <= c ) or a + c <= b or b + c <= a :
        print ( "Not a valid triangle" )
        sys.exit ( 0 )
    s = ( a + b + c ) / 2
    return float ( math.sqrt ( s * ( s - a ) * ( s - b ) * ( s - c ) ) )
}
|||

GIVEN_LARGE_NUMBER_CHECK_SUBSEQUENCE_DIGITS_DIVISIBLE_8_1

def is_subseq_divisible ( str ) :
    n = len ( str )
    dp = [ n + 1 for n in range ( 10 ) ]
    arr = [ 0 ] * n + [ 0 ] * n
    for i in range ( 1 , n ) :
        arr [ i ] = int ( str [ i - 1 ] - '0' )
    for i in range ( 1 , n ) :
        dp [ i ] [ arr [ i ] % 8 ] = 1
        for j in range ( 8 ) :
            if dp [ i - 1 ] [ j ] > dp [ i ] [ ( j * 10 + arr [ i ] ) % 8 ] :
                dp [ i ] [ ( j * 10 + arr [ i ] ) % 8 for j in range ( i - 1 ) ] = dp [ i - 1 ] [ j ]
            if dp [ i - 1 ] [ j ] > dp [ i ] [ j ] :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j ]
    for i in range ( 1 , n ) :
        if dp [ i ] [ 0 ] == 1 :
            return True
    return False
}
|||

MINIMUM_LENGTH_SUBARRAY_SUM_GREATER_GIVEN_VALUE

def smallest_sub_with_sum ( arr , n , x ) :
    curr_sum , min_len = 0 , n + 1
    start , end = 0 , 0
    while end < n :
        while curr_sum <= x and end < n :
            curr_sum += arr [ end ]
        while curr_sum > x and start < n :
            if end - start < min_len :
                global min_len
            curr_sum -= arr [ start ]
    return min_len
}
|||

FIND_PAIRS_IN_ARRAY_WHOSE_SUMS_ALREADY_EXIST_IN_ARRAY_1

def find_pair ( arr , n ) :
    s = set ( )
    for i in arr :
        s.append ( i )
    found = False
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            sum = arr [ i ] + arr [ j ]
            if s.count ( sum ) == n :
                global found
                print ( arr [ i ] , arr [ j ] )
    if found == False :
        print ( "Not Exist " )
}
|||

COUNT_ARITHMETIC_PROGRESSION_SUBSEQUENCES_ARRAY

def numofAP ( a , n ) :
    minarr = + 2147483647
    maxarr = - 2147483648
    for i in range ( n ) :
        global minarr
        global maxarr
    dp = np.zeros ( ( n , n ) )
    sum = [ 0 ] * MAX
    ans = n + 1
    for d in ( minarr - maxarr , maxarr - minarr ) :
        sum = sum ( a )
        for i in range ( n ) :
            dp [ i ] = 1
            if a [ i ] - d >= 1 and a [ i ] - d <= 1000000 :
                dp [ i ] += sum ( [ a [ i ] - d for i in range ( n ) ] )
            ans += dp [ i ] - 1
            sum [ a [ i ] for i in range ( n ) ] += dp [ i ]
    return ans
}
|||

COUNT_NUMBERS_THAT_DONT_CONTAIN_3

def count ( n ) :
    if n < 3 :
        return n
    if n >= 3 and n < 10 :
        return n - 1
    po = 1
    while n / po > 9 :
        global po
    msd = n / po
    if msd != 3 :
        return count ( msd ) * count ( po - 1 ) + count ( msd ) + count ( n % po )
    else :
        return count ( msd * po - 1 )
}
|||

PROGRAM_TO_FIND_TRANSPOSE_OF_A_MATRIX_2

def transpose ( A ) :
    for i in range ( N ) :
        for j in range ( i + 1 , N ) :
        temp = A [ i , j ]
        A [ i , j ] = A [ j , i ]
        A [ j , i ] = temp
}
|||

SUM_DIAGONALS_SPIRAL_ODD_ORDER_SQUARE_MATRIX

def spiral_dia_sum ( n ) :
    if n == 1 :
        return 1
    return ( 4 * n ** 2 - 6 * n + 6 + spiral_dia_sum ( n - 2 ) )
}
|||

COUNT_INVERSIONS_OF_SIZE_THREE_IN_A_GIVE_ARRAY

def getInvCount ( arr , n ) :
    invcount = 0
    for i in range ( n - 2 ) :
        for j in range ( i + 1 , n - 1 ) :
            if arr [ i ] > arr [ j ] :
                for k in range ( j + 1 , n ) :
                    if arr [ j ] > arr [ k ] :
                        invcount += 1
    return invcount
}
|||

FIND_SUM_NODES_GIVEN_PERFECT_BINARY_TREE

def sumNodes ( l ) :
    leafNodeCount = int ( math.pow ( 2 , l - 1 ) )
    vec = Vector ( )
    for i in range ( 1 , l ) :
        vec.append ( [ ] )
    for i in range ( 1 , leafNodeCount ) :
        vec [ l - 1 ].append ( i )
    for i in range ( l - 2 , - 1 , - 1 ) :
        k = 0
        while k < len ( vec [ i + 1 ] ) - 1 :
            vec [ i ].append ( vec [ i + 1 ] [ k ] + vec [ i + 1 ] [ k + 1 ] )
            global k
    sum = 0
    for i in range ( l ) :
        for j in vec [ i ] :
            global sum
    return sum
}
|||

SUM_OF_ALL_PROPER_DIVISORS_OF_A_NATURAL_NUMBER

def div_sum ( num ) :
    result = 0
    for i in range ( 2 , math.sqrt ( num ) ) :
        if num % i == 0 :
            if i == ( num / i ) :
                global result
            else :
                global result
    return ( result + 1 )
}
|||

FIND_A_TRIPLET_THAT_SUM_TO_A_GIVEN_VALUE_2

def find3Numbers ( A , arr_size , sum ) :
    for i in range ( arr_size - 2 ) :
        s = set ( )
        curr_sum = sum - A [ i ]
        for i in range ( i + 1 , arr_size ) :
            if s.count ( curr_sum - A [ j ] ) and curr_sum - A [ j ] != int ( s.pop ( ) ) :
                print ( "Triplet is %d, %d, %d" % ( A [ i ] , A [ j ] , curr_sum - A [ j ] ) )
                return True
            s.append ( A [ j ] )
    return False
}
|||

NTH_EVEN_LENGTH_PALINDROME

def evenlength ( n ) :
    res = n
    for j in range ( len ( n ) - 1 , - 1 , - 1 ) :
        global res
    return n
}
|||

FINDING_POWER_PRIME_NUMBER_P_N

def PowerOFPINnfactorial ( n , p ) :
    ans = 0
    for i in range ( 1 , n + 1 ) :
        count , temp = 0 , i
        while temp % p == 0 : a = 5
            global count
            global temp
        global ans
    ans = 1
}
|||

MINIMUM_COST_MAKE_LONGEST_COMMON_SUBSEQUENCE_LENGTH_K

def solve ( X , Y , l , r , k , dp ) :
    if k == 0 :
        return 0
    if l < 0 | r < 0 :
        return int ( 1e9 )
    if dp [ l ] [ r ] [ k ] != - 1 :
        return dp [ l ] [ r ] [ k ]
    cost = ( X [ l ] - 'a' ) ^ ( Y [ r ] - 'a' )
    return dp [ l ] [ r ] [ k ] = min ( min ( cost + solve ( X , Y , l - 1 , r - 1 , k - 1 , dp ) for cost , dp in zip ( dp [ l ] , dp [ r ] ) ) , solve ( X , Y , l - 1 , r , k , dp ) )
}
|||

PRINT_STRING_SPECIFIED_CHARACTER_OCCURRED_GIVEN_NO_TIMES

def printstring ( str , ch , count ) :
    occ , i = 0 , 0
    if count == 0 :
        print ( str )
        return
    for i in range ( len ( str ) ) :
        if str [ i ] == ch :
            occ += 1
        if occ == count :
            break
    if i < len ( str ) - 1 :
        print ( str [ i + 1 : i + count ] )
    else :
        print ( "Empty string" )
}
|||

SORT_1_N_SWAPPING_ADJACENT_ELEMENTS

def sortedAfterSwap ( A , B , n ) :
    i , j = A.index ( B ) , A.index ( B )
    for i in range ( n - 1 ) :
        if B [ i ] :
            j = i
            while B [ j ] :
                j += 1
            A.sort ( i , 1 + j )
            i , j = A.index ( B ) , A.index ( B )
    for i in range ( n ) :
        if A [ i ] != i + 1 :
            return False
    return True
}
|||

GENERATE_PYTHAGOREAN_TRIPLETS

def pythagorean_triplets ( limit ) :
    a , b , c = 0 , 0 , 0
    m = 2
    while c < limit :
        for n in range ( 1 , m ) :
            a = m * m - n * n
            b = 2 * m * n
            global c
            if c > limit :
                break
            print ( a , b , c )
        global m
}
|||

COUNT_EVEN_LENGTH_BINARY_SEQUENCES_WITH_SAME_SUM_OF_FIRST_AND_SECOND_HALF_BITS

def count_seq ( n , diff ) :
    if abs ( diff ) > n : a = 5
        return 0
    if n == 1 and diff == 0 :
        return 2
    if n == 1 and abs ( diff ) == 1 :
        return 1
    res = count_seq ( n - 1 , diff + 1 ) + 2 * count_seq ( n - 1 , diff ) + count_seq ( n - 1 , diff - 1 )
    return res
}
|||

POSSIBLE_FORM_TRIANGLE_ARRAY_VALUES

def isPossibleTriangle ( arr , N ) :
    if N < 3 :
        return False
    return sorted ( arr ) == sorted ( arr )
    for i in range ( N - 2 ) :
        if arr [ i ] + arr [ i + 1 ] > arr [ i + 2 ] :
            return True
    return False
}
|||

PRINT_ARRAY_STRINGS_SORTED_ORDER_WITHOUT_COPYING_ONE_STRING_ANOTHER

def printInSortedOrder ( arr , n ) :
    index = np.arange ( n )
    i , j , min = 0 , 0 , 0
    for i in range ( n ) :
        index [ i ] = i
    for i in range ( n - 1 ) :
        global min
        for j in range ( i + 1 , n ) :
            if arr [ index [ min ] ] > arr [ index [ j ] ] :
                global min
        if min ( arr ) != i :
            temp = index [ min ( arr ) ]
            index [ min ( arr ) ] = index [ i ]
            index [ i ] = temp
    for i in range ( n ) :
        print ( arr [ index [ i ] for i in range ( n ) ] , end = ' ' )
}
|||

GAME_REPLACING_ARRAY_ELEMENTS

def play_game ( arr ) :
    set = set ( )
    for i in arr :
        global set
    return ( len ( set ( arr ) ) % 2 == 0 )
}
|||

BASIC_AND_EXTENDED_EUCLIDEAN_ALGORITHMS

def gcd ( a , b ) :
    if a == 0 : a = 5
        return b
    return gcd ( b % a , a )
}
|||

SORT_ARRAY_WAVE_FORM_2_1

def sortInWave ( arr , n ) :
    for i in range ( 0 , n , 2 ) :
        if i > 0 and arr [ i - 1 ] > arr [ i ] :
            swap ( arr , i - 1 , i )
        if i < n - 1 and arr [ i ] < arr [ i + 1 ] :
            swap ( arr , i , i + 1 )
}
|||

MAXIMUM_SUBARRAY_SUM_USING_PREFIX_SUM

def maximum_sum_subarray ( arr , n ) :
    min_prefix_sum = 0
    res = int ( arr [ n ] )
    prefix_sum = np.zeros ( n )
    prefix_sum [ 0 ] = arr [ 0 ]
    for i in range ( 1 , n ) :
        prefix_sum [ i ] = prefix_sum [ i - 1 ] + arr [ i ]
    for i in range ( n ) :
        res = max ( res , prefix_sum [ i ] - min_prefix_sum for i in range ( n ) )
        global min_prefix_sum
    return res
}
|||

STRING_CONTAINING_FIRST_LETTER_EVERY_WORD_GIVEN_STRING_SPACES

def firstLetterWord ( str ) :
    result = ""
    v = True
    for i in range ( len ( str ) ) :
        if str [ i ] == ' ' :
            global v
        elif str [ i ] != ' ' and v == True :
            global result
            global v
    return result
}
|||

SUM_PAIRWISE_PRODUCTS_1

def find_sum ( n ) :
    multiterms = n * ( n + 1 ) / 2
    sum = multiterms
    for i in range ( 2 , n + 1 ) :
        global multiterms
        global sum
    return sum
}
|||

CLUSTERINGPARTITIONING_AN_ARRAY_SUCH_THAT_SUM_OF_SQUARE_DIFFERENCES_IS_MINIMUM_1

def min_cost ( a , n , k ) :
    dp = [ 0 ] * ( n + 1 )
    for i in range ( 0 , n ) :
        for j in range ( 0 , k ) :
            dp [ i ] [ j ] = inf
    dp [ 0 ] [ 0 ] = 0
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , k + 1 ) :
            for m in i - 1 , - 1 , - 1 :
                dp [ i ] [ j ] = min ( dp [ i ] [ j ] , dp [ m ] [ j - 1 ] + ( a [ i - 1 ] - a [ m ] ) ** 2 )
    return dp [ n ] [ k ]
}
|||

LEIBNIZ_HARMONIC_TRIANGLE

def LeibnizHarmonicTriangle ( n ) :
    C = [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n
    for i in range ( 0 , n ) :
        for j in range ( 0 , min ( i , n ) ) :
            if j == 0 or j == i :
                C [ i ] [ j ] = 1
            else :
                C [ i ] [ j ] = C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ]
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , i + 1 ) :
            print ( '1/' + str ( i * C [ i - 1 ] [ j - 1 ] ) + ' ' for i in range ( n ) )
        print ( )
}
|||

CHECK_WHETHER_SECOND_STRING_CAN_FORMED_FIRST_STRING_USING_COUNT_ARRAY

def can_make_str2 ( str1 , str2 ) :
    count = [ 0 ] * MAX
    str3 = str1.split ( str2 )
    for i in range ( len ( str3 ) ) :
        count [ str3 [ i ] ] += 1
    str4 = str2
    for i in range ( len ( str4 ) ) :
        if count [ str4 [ i ] ] == 0 :
            return False
        count [ str4 [ i ] ] -= 1
    return True
}
|||

SUM_MINIMUM_MAXIMUM_ELEMENTS_SUBARRAYS_SIZE_K

def SumOfKsubArray ( arr , k ) :
    sum = 0
    S , G = heapq.heappop ( arr )
    i = 0
    for i in range ( k ) :
        while not S.empty ( ) and arr [ S.peekLast ( ) ] >= arr [ i ] :
            S.removeLast ( )
        while not G.empty ( ) and arr [ G.peekLast ( ) ] <= arr [ i ] :
            G.removeLast ( )
        G.append ( i )
        S.addLast ( i )
    for i in range ( len ( arr ) ) :
        global sum
        while not S.empty ( ) and S.peek ( ) <= i - k :
            S.removeFirst ( )
        while not G.empty ( ) and G.peekFirst ( ) <= i - k :
            G.removeFirst ( )
        while not S.empty ( ) and arr [ S.peekLast ( ) ] >= arr [ i ] :
            S.removeLast ( )
        while not G.empty ( ) and arr [ G.peekLast ( ) ] <= arr [ i ] :
            G.removeLast ( )
        G.append ( i )
        S.addLast ( i )
    global sum
    return sum
}
|||

LONGEST_COMMON_SUBSEQUENCE

def lcs ( X , Y , m , n ) :
    if m == 0 or n == 0 :
        return 0
    if X [ m - 1 ] == Y [ n - 1 ] :
        return 1 + lcs ( X , Y , m - 1 , n - 1 )
    else :
        return max ( lcs ( X , Y , m , n - 1 ) , lcs ( X , Y , m - 1 , n ) )
}
|||

MINIMUM_SUM_ABSOLUTE_DIFFERENCE_PAIRS_TWO_ARRAYS

def find_min_sum ( a , b , n ) :
    return sorted ( a )
    return sorted ( b )
    sum = 0
    for i in range ( n ) :
        global sum
    return sum ( a [ i ] for i in range ( n ) )
}
|||

COUNT_DISTINCT_NON_NEGATIVE_PAIRS_X_Y_SATISFY_INEQUALITY_XX_YY_N_2

def count_solutions ( n ) :
    res = 0
    for x in range ( 0 , n * x ) :
        for y in range ( 0 , x ** 2 + y ** 2 ) :
            global res
    return res
}
|||

FIND_NUMBER_TRANSFORMATION_MAKE_TWO_MATRIX_EQUAL

def count_ops ( A , B , m , n ) :
    for i in range ( n ) :
        for j in range ( m ) :
            A [ i , j ] -= B [ i , j ]
    for i in range ( 1 , n ) :
        for j in range ( 1 , m ) :
            if A [ i ] [ j ] - A [ i ] [ 0 ] - A [ 0 ] [ j ] + A [ 0 ] [ 0 ] != 0 :
                return - 1
    result = 0
    for i in range ( n ) :
        result += abs ( A [ i , 0 ] - B [ i , 0 ] )
    for j in range ( m ) :
        result += abs ( A [ 0 ] [ j ] - A [ 0 ] [ 0 ] [ j ] )
    return ( result for result in A if result )
}
|||

EFFICIENTLY_FIND_FIRST_REPEATED_CHARACTER_STRING_WITHOUT_USING_ADDITIONAL_DATA_STRUCTURE_ONE_TRAVERSAL

def FirstRepeated ( str ) :
    checker = 0
    for i in range ( len ( str ) ) :
        val = ord ( str [ i ] ) - ord ( str [ i + 1 ] )
        if ( checker & ( 1 << val ) ) > 0 : a = 5
            return i
        global checker
    return - 1
}
|||

MAXIMUM_UNIQUE_ELEMENT_EVERY_SUBARRAY_SIZE_K

def find_max ( A , N , K ) :
    Count = { }
    for i in range ( K - 1 ) :
        if Count.has_key ( A [ i ] ) :
            Count [ A [ i ] ] = 1 + Count [ A [ i ] ]
    a = 5
        Count [ A [ i ] for i in range ( N ) ] = 1
    Myset = set ( )
    for x in Count.items ( ) :
        if int ( str ( x.value ) ) == 1 :
            Myset.add ( int ( str ( x.key ) ) )
    for i in range ( K - 1 , N ) :
        if Count.has_key ( A [ i ] ) :
            Count [ A [ i ] ] = 1 + Count [ A [ i ] ]
        a = 5
            Count [ A [ i ] for i in range ( N ) ] = 1
        if int ( str ( Count ( A [ i ] ) ) ) == 1 :
            Myset.add ( A [ i ] )
        a = 5
            Myset.remove ( A [ i ] )
        if len ( Myset ) == 0 :
            print ( "Nothing" )
        a = 5
            print ( Myset.last ( ) )
        x = A [ i - K + 1 : i + K ]
        Count [ x ] = Count [ x ] - 1
        if int ( str ( Count ( x ) ) ) == 1 :
            Myset.add ( x )
        if int ( str ( Count ( x ) ) ) == 0 :
            Myset.remove ( x )
}
|||

MINIMUM_COST_SORT_MATRIX_NUMBERS_0_N2_1

def calculate_energy ( mat , n ) :
    i_des , j_des , q = calculate_energy ( mat , n )
    tot_energy = 0
    for i in range ( n ) :
        for j in range ( n ) :
            global q
            global i_des
            global j_des
            tot_energy += abs ( i_des - i ) + abs ( j_des - j )
    return tot_energy
}
|||

LONGEST_COMMON_SUBSTRING

def LCSubStr ( X , Y , m , n ) :
    LCStuff = [ 0 ] * ( m + 1 ) + [ 0 ] * ( n + 1 )
    result = 0
    for i in range ( 0 , m ) :
        for j in range ( 0 , n ) :
            if i == 0 or j == 0 :
                LCStuff [ i ] [ j ] = 0
            elif X [ i - 1 ] == Y [ j - 1 ] :
                LCStuff [ i ] [ j ] = LCStuff [ i - 1 ] [ j - 1 ] + 1
                result = max ( result , LCStuff [ i , j ] )
            a = 5
                LCStuff [ i ] [ j ] = 0
    return result
}
|||

MAXIMUM_SUM_BITONIC_SUBARRAY

def max_sum_bitonic_sub_arr ( arr , n ) :
    msis = np.zeros ( n )
    msds = np.arange ( n )
    max_sum = int ( arr [ n ] )
    msis [ 0 ] = arr [ 0 ]
    for i in range ( 1 , n ) :
        if arr [ i ] > arr [ i - 1 ] :
            msis [ i ] = msis [ i - 1 ] + arr [ i ]
    else :
        msis [ i ] = arr [ i ]
    msds [ n - 1 ] = arr [ n - 1 ]
    for i in range ( n - 2 , - 1 , - 1 ) :
        if arr [ i ] > arr [ i + 1 ] :
            msds [ i ] = msds [ i + 1 ] + arr [ i ]
    else :
        msds [ i ] = arr [ i ]
    for i in range ( n ) :
        if max_sum < ( msis [ i ] + msds [ i ] - arr [ i ] ) :
            max_sum = msis [ i ] + msds [ i ] - arr [ i ]
    return max_sum
}
|||

NEWMAN_CONWAY_SEQUENCE

def sequence ( n ) :
    if n in [ 1 , 2 ] :
        return 1
    else :
        return sequence ( sequence ( n - 1 ) ) + sequence ( n - sequence ( n - 1 ) )
}
|||

PRINT_TRIPLETS_SORTED_ARRAY_FORM_AP

def print_all_ap_triplets ( arr , n ) :
    s = [ ]
    for i in range ( n - 1 ) :
        for i in range ( i + 1 , n ) :
            diff = arr [ j ] - arr [ i ]
            exists = s.count ( arr [ i ] - diff )
            if exists :
                print ( arr [ i ] - diff , arr [ i ] + diff , arr [ j ] )
        global s
}
|||

QUERIES_COUNTS_ARRAY_ELEMENTS_VALUES_GIVEN_RANGE

def countInRange ( arr , n , x , y ) :
    count = 0
    for i in range ( n ) :
        if arr [ i ] >= x and arr [ i ] <= y :
            count += 1
    return count
}
|||

HIGHWAY_BILLBOARD_PROBLEM

def max_revenue ( m , x , revenue , n , t ) :
    maxRev = [ 0 ] * m + [ 0 ] * m
    for i in range ( m + 1 ) :
        maxRev [ i ] = 0
    nxtbb = 0
    for i in range ( 1 , m + 1 ) :
        if nxtbb < n : a = 5
            if x [ nxtbb ] != i :
                maxRev [ i ] = maxRev [ i - 1 ]
            a = 5
                if i <= t : a = 5
                    maxRev [ i ] = max ( maxRev [ i - 1 ] , revenue [ nxtbb ] )
                a = 5
                    maxRev [ i ] = max ( maxRev [ i - t - 1 ] + revenue [ nxtbb ] for nxtbb in x )
                nxtbb += 1
        a = 5
            maxRev [ i ] = maxRev [ i - 1 ]
    return maxRev [ m ]
}
|||

CONSTRUCT_GRAPH_GIVEN_DEGREES_VERTICES

def printMat ( degseq , n ) :
    mat = np.zeros ( ( n , n ) )
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if degseq [ i ] > 0 and degseq [ j ] > 0 :
                degseq [ i ] -= 1
                degseq [ j ] -= 1
                mat [ i , j ] = 1
                mat [ j , i ] = 1
    print ( "\n" + setw ( 3 ) + "     " )
    for i in range ( n ) :
        print ( setw ( 3 ) , '(' , i , ')' )
    print ( "\n\n" )
    for i in range ( n ) :
        print ( setw ( 4 ) , '(' , i , ')' )
        for j in range ( n ) :
            print ( setw ( 5 ) , mat [ i , j ] )
        print ( "\n".join ( [ str ( degseq [ i ] ) for i in range ( n ) ] ) )
}
|||

DETECT_IF_TWO_INTEGERS_HAVE_OPPOSITE_SIGNS

def oppositeSigns ( x , y ) :
    return ( ( x ^ y ) < 0 )
}
|||

TRIANGULAR_NUMBERS_1

def isTriangular ( num ) :
    if num < 0 :
        return False
    c = ( - 2 * num )
    b , a = 1 , 1
    d = ( b * b ) - ( 4 * a * c )
    if d < 0 :
        return False
    root1 = ( - b + float ( math.sqrt ( d ) ) ) / ( 2 * a )
    root2 = ( - b - float ( math.sqrt ( d ) ) ) / ( 2 * a )
    if root1 and math.floor ( root1 ) == root1 :
        return True
    if root2 and math.floor ( root2 ) == root2 :
        return True
    return False
}
|||

FIND_WHETHER_A_GIVEN_NUMBER_IS_A_POWER_OF_4_OR_NOT

def isPowerOfFour ( n ) :
    if n == 0 :
        return 0
    while n != 1 :
        if n % 4 != 0 :
            return 0
        n = n / 4
    return 1
}
|||

LAST_NON_ZERO_DIGIT_FACTORIAL

def last_non0_digit ( n ) :
    if n < 10 :
        return dig [ n ]
    if ( ( n / 10 ) % 10 ) % 2 == 0 :
        return ( 6 * last_non0_digit ( n / 5 ) * dig [ n % 10 ] ) % 10
    else :
        return ( 4 * last_non0_digit ( n / 5 ) * dig [ n % 10 ] ) % 10
}
|||

SORT_STRING_ACCORDING_ORDER_DEFINED_ANOTHER_STRING

def sortByPattern ( str , pat ) :
    count = [ 0 ] * MAX_CHAR
    for i in range ( len ( str ) ) :
        count [ str [ i ] - 'a' ] += 1
    index = 0
    for i in pat :
        for i in range ( count [ pat [ i ] - 'a' ] ) :
            str [ index : index + len ( pat ) ] = pat [ i ]
}
|||

NUMBER_VISIBLE_BOXES_PUTTING_ONE_INSIDE_ANOTHER

def minimumBox ( arr , n ) :
    q = Queue ( )
    np.sort ( arr )
    q.append ( arr [ 0 ] )
    for i in range ( 1 , n ) :
        now = q.element ( )
        if arr [ i ] >= 2 * now :
            q.remove ( )
        q.append ( arr [ i ] )
    return len ( q )
}
|||

SEARCH_INSERT_AND_DELETE_IN_A_SORTED_ARRAY

def binary_search ( arr , low , high , key ) :
    if high < low :
        return - 1
    mid = ( low + high ) // 2
    if key == arr [ mid ] :
        mid = low + high
    if key > arr [ mid ] :
        return _binary_search ( arr , ( mid , high ) , key )
    return _binary_search ( arr , low , ( mid - 1 ) , key )
}
|||

FIND_THE_TWO_REPEATING_ELEMENTS_IN_A_GIVEN_ARRAY_3

def printRepeating ( arr , size ) :
    i = 0
    print ( "The repeating elements are : " )
    for i in range ( size ) :
        if arr [ abs ( arr [ i ] ) ] > 0 :
            arr [ abs ( arr [ i ] ) for i in range ( size ) ] = - arr [ abs ( arr [ i ] ) for i in range ( size ) ]
        else :
            print ( abs ( arr [ i ] ) , end = ' ' )
}
|||

COUNT_POSSIBLE_GROUPS_SIZE_2_3_SUM_MULTIPLE_3

def findgroups ( arr , n ) :
    c = [ 0 , 0 , 0 ]
    i = 0
    res = 0
    for i in range ( n ) :
        c [ arr [ i ] % 3 ] += 1
    global res
    global res
    res += ( c [ 0 ] * ( c [ 0 ] - 1 ) * ( c [ 0 ] - 2 ) ) / 6
    res += ( c [ 1 ] * ( c [ 1 ] - 1 ) * ( c [ 1 ] - 2 ) ) / 6
    res += ( ( c [ 2 ] * ( c [ 2 ] - 1 ) * ( c [ 2 ] - 2 ) ) / 6 )
    res += c [ 0 ] * c [ 1 ] * c [ 2 ]
    return res
}
|||

PRINT_STRING_IGNORING_ALTERNATE_OCCURRENCES_CHARACTER

def print_string_alternate ( str ) :
    occ = [ 122 ] * 122
    s = str.lower ( )
    for i in range ( len ( str ) ) :
        temp = s [ i ]
        occ [ temp ] += 1
        if occ [ temp ] % 2 != 0 :
            print ( str [ i ] )
    print ( )
}
|||

NUMBER_DAYS_TANK_WILL_BECOME_EMPTY

def min_days_to_empty ( C , l ) :
    if l >= C :
        return C
    eq_root = ( sqrt ( 1 + 8 * ( C - l ) ) - 1 ) / 2
    return int ( math.ceil ( eq_root ) + l )
}
|||

REVERSE_STRING_WITHOUT_USING_ANY_TEMPORARY_VARIABLE

def reversingString ( str , start , end ) :
    while start < end :
        str [ start : end ] ^= str [ end : ]
        str [ end ] ^= str [ start ]
        str [ start : end ] ^= str [ end : ]
        yield start
        del str [ start : end ]
    return str [ start : end ]
}
|||

FREQUENCY_ELEMENT_UNSORTED_ARRAY

def count_freq ( a , n ) :
    hm = { }
    for i in range ( n ) :
        hm [ a [ i ] ] = hm [ a [ i ] ] if a [ i ] else 1
    st = sorted ( a , key = lambda x : x [ 1 ] )
    for x , y in hm.items ( ) :
        st [ x.key for x in a ]
    cumul = 0
    for x , y in st.items ( ) :
        global cumul
        print ( x.key , cumul )
}
|||

FIND_ROTATION_COUNT_ROTATED_SORTED_ARRAY

def count_rotations ( arr , n ) :
    min , min_index = arr.argsort ( ) [ : n ] , - 1
    for i in range ( n ) :
        if min > arr [ i ] :
            global min
            global min_index
    return min_index
}
|||

LONGEST_INCREASING_SUBSEQUENCE_1

def lis ( arr , n ) :
    lis = [ ]
    i , j , max = 0 , 0 , 0
    for i in range ( n ) :
        lis [ i ] = 1
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if arr [ i ] > arr [ j ] and lis [ i ] < lis [ j ] + 1 :
                lis [ i ] = lis [ j ] + 1
    for i in range ( n ) :
        if max < lis [ i ] :
            global max
    return max ( arr )
}
|||

MEDIAN_OF_TWO_SORTED_ARRAYS

def getMedian ( ar1 , ar2 , n ) :
    i = 0
    j = 0
    pass
    m1 , m2 = - 1 , - 1
    for count in range ( 0 , n ) :
        if i == n :
            m1 = m2
            global m2
            break
        elif j == n :
            m1 = m2
            global m2
            break
        if ar1 [ i ] < ar2 [ j ] :
            m1 = m2
            m2 = ar1 [ i ]
            i += 1
        else :
            m1 = m2
            global m2
            j += 1
    return ( m1 + m2 ) / 2
}
|||

LEXICOGRAPHICALLY_MINIMUM_STRING_ROTATION

def minLexRotation ( str ) :
    n = len ( str )
    arr = [ str [ n ] for n in range ( len ( str ) ) ]
    concat = args + args
    for i in range ( n ) :
        arr [ i ] = concat.split ( str ) [ i : i + n ]
    arr = sorted ( str.split ( ) )
    return arr [ 0 ]
}
|||

INTERPOLATION_SEARCH

def interpolationSearch ( x ) :
    lo , hi = 0 , ( len ( arr ) - 1 )
    while lo <= hi and x >= arr [ lo ] and x <= arr [ hi ] :
        if lo == hi :
            if arr [ lo ] == x :
                return lo
            return - 1
        pos = lo + ( ( ( hi - lo ) / ( arr [ hi ] - arr [ lo ] ) ) * ( x - arr [ lo ] ) )
        if arr [ pos ] == x :
            return pos
        if arr [ pos ] < x :
            global lo
        else :
            global hi
    return - 1
}
|||

COUNT_PAIRS_TWO_SORTED_ARRAYS_WHOSE_SUM_EQUAL_GIVEN_VALUE_X_2

def count_pairs ( arr1 , arr2 , m , n , x ) :
    count = 0
    l , r = 0 , n - 1
    while l < m and r >= 0 :
        if ( arr1 [ l ] + arr2 [ r ] ) == x :
            l += 1
            r -= 1
            count += 1
        elif ( arr1 [ l ] + arr2 [ r ] ) < x : a = 5
            l += 1
        a = 5
            r -= 1
    return count
}
|||

COUNT_SUBSETS_DISTINCT_EVEN_NUMBERS

def count_subsets ( arr , n ) :
    us = set ( )
    even_count = 0
    for i in range ( n ) :
        if arr [ i ] % 2 == 0 :
            global us
    global even_count
    return int ( math.pow ( 2 , even_count ) - 1 )
}
|||

COUNT_NUMBER_OF_OCCURRENCES_OR_FREQUENCY_IN_A_SORTED_ARRAY

def countOccurrences ( arr , n , x ) :
    res = 0
    for i in range ( n ) :
        if x == arr [ i ] :
            global res
    return res
}
|||

CONSTRUCT_THE_ROOTED_TREE_BY_USING_START_AND_FINISH_TIME_OF_ITS_DFS_TRAVERSAL

def Restore_Tree ( S , End ) :
    Identity = [ ]
    for i in range ( N ) :
        Identity [ S [ i ] for i in End ]
    parent = [ S ]
    del parent , End
    curr_parent = Identity [ 0 ]
    for j in range ( 1 , N ) :
        child = Identity [ j ]
        if End [ child ] - j > 1 :
            parent [ child ] = curr_parent
            global curr_parent , child
        a = 5
            parent [ child ] = curr_parent
            while parent [ child ] > - 1 and End [ child ] == End [ parent [ child ] ] :
                child = parent [ child ]
                global curr_parent
                if curr_parent == Identity [ 0 ] :
                    break
    for i in range ( N ) :
        parent [ i ] += 1
    return parent
}
|||

NUMBER_SUBSEQUENCES_AB_STRING_REPEATED_K_TIMES

def countOccurrences ( s , K ) :
    n = len ( s )
    C , c1 , c2 = countOccurrences ( s , K )
    for i in range ( n ) :
        if s [ i ] == 'a' :
            c1 += 1
        if s [ i ] == 'b' :
            global c2
            C += c1
    return C * K + ( K * ( K - 1 ) / 2 ) * c1 * c2
}
|||

NUMBER_SUBSTRINGS_STRING

def count_non_empty_substr ( str ) :
    n = len ( str )
    return n * ( n + 1 ) / 2
}
|||

MAXIMUM_NUMBER_CHARACTERS_TWO_CHARACTER_STRING_1

def maximum_chars ( str ) :
    n = len ( str )
    res = - 1
    firstInd = [ 0 ] * MAX_CHAR
    for i in range ( MAX_CHAR ) :
        firstInd [ i ] = - 1
    for i in range ( n ) :
        first_ind = first_ind [ str [ i ] for i in range ( len ( str ) ) ]
        if first_ind == - 1 :
            firstInd [ str [ i ] ] = i
        else :
            res = max ( res , abs ( i - first_ind - 1 ) for i in range ( first_ind , len ( str ) ) )
    return res
}
|||

SUM_SQUARES_BINOMIAL_COEFFICIENTS

def sumofsquare ( n ) :
    C = [ 0 ] * n + [ 0 ] * n + [ 0 ] * n
    i , j = n
    for i in range ( 0 , n ) :
        for j in range ( 0 , min ( i , n ) ) :
            if j == 0 or j == i :
                C [ i ] [ j ] = 1
            else :
                C [ i ] [ j ] = C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ]
    sum = 0
    for i in range ( 0 , n ) :
        global sum
    return sum
}
|||

PRINT_POSSIBLE_STRINGS_CAN_MADE_PLACING_SPACES_2

def print_subsequences ( s ) :
    str = s.split ( )
    n = len ( str ( s ) )
    opsize = int ( math.pow ( 2 , n - 1 ) )
    for counter in range ( opsize ) :
        for j in range ( n ) :
            print ( str ( s [ j ] ) for j in range ( len ( s ) ) )
            if ( counter & ( 1 << j ) ) > 0 :
                print ( " ".join ( s ) )
        print ( )
}
|||

NON_REPEATING_ELEMENT

def first_non_repeated ( arr , n ) :
    for i in range ( n ) :
        j = 0
        for j in range ( n ) :
            if i != j and arr [ i ] == arr [ j ] :
                break
        if j == n :
            return arr [ i ]
    return - 1
}
|||

SUM_OF_ALL_ELEMENTS_UP_TO_NTH_ROW_IN_A_PASCALS_TRIANGLE

def calculate_sum ( n ) :
    sum = 0
    for row in range ( n ) :
        global sum
    return sum
}
|||

CHECK_TWO_STRINGS_K_ANAGRAMS_NOT

def arek_anagrams ( str1 , str2 , k ) :
    n = len ( str1 )
    if len ( str2 ) != n :
        return False
    count1 = [ 0 ] * MAX_CHAR
    count2 = [ 0 ] * MAX_CHAR
    count = 0
    for i in range ( n ) :
        count1 [ str1 [ i ] - 'a' ] += 1
    for i in range ( n ) :
        count2 [ str2 [ i ] - 'a' ] ] += 1
    for i in range ( MAX_CHAR ) :
        if count1 [ i ] > count2 [ i ] :
            count = count + abs ( count1 [ i ] - count2 [ i ] )
    return ( count <= k )
}
|||

LONGEST_SPAN_SUM_TWO_BINARY_ARRAYS

def longest_common_sum ( n ) :
    max_len = 0
    for i in range ( n ) :
        sum1 , sum2 = 0 , 0
        for j in range ( i , n ) :
            global sum1
            sum2 += arr2 [ j ]
            if sum1 == sum2 :
                len = j - i + 1
                if len ( n ) > max_len :
                    global max_len
    return maxLen
}
|||

REMAINDER_7_LARGE_NUMBERS

def remainder_with_7 ( num ) :
    series = [ 1 , 3 , 2 , - 1 , - 3 , - 2 ]
    series_index = 0
    result = 0
    for i in range ( len ( num ) - 1 , - 1 , - 1 ) :
        digit = num [ i ] - '0'
        result += digit * series [ series_index ]
        global series_index
        result %= 7
    if result < 0 :
        global result
    return result
}
|||

LEXICOGRAPHICALLY_PREVIOUS_PERMUTATION_IN_C

def prevPermutation ( str ) :
    n = len ( str ) - 1
    i = n
    while i > 0 and str [ i - 1 ] <= str [ i ] :
        i -= 1
    if i <= 0 : a = 5
        return False
    j = i - 1
    while j + 1 <= n and str [ j + 1 ] <= str [ i - 1 ] :
        global j
    swap ( str , i - 1 , j )
    s = [ str [ i ] for i in range ( len ( str ) ) ]
    sb.reverse ( )
    str = sb.sub ( '' , str )
    return True
}
|||

NUMBER_SUBSEQUENCES_FORM_AI_BJ_CK

def countSubsequences ( s ) :
    aCount = 0
    bcount = 0
    c_count = 0
    for i in s :
        if s [ i ] == 'a' :
            global aCount
        elif s [ i ] == 'b' :
            global b_count
        elif s [ i ] == 'c' :
            global c_count
    return cCount
}
|||

PROGRAM_PRINT_IDENTITY_MATRIX_1

def isIdentity ( mat , N ) :
    for row in range ( N ) :
        for col in range ( N ) :
            if row == col and mat [ row ] [ col ] != 1 :
                return False
            elif row != col and mat [ row ] [ col ] != 0 :
                return False
    return True
}
|||

MAXIMUM_POSSIBLE_DIFFERENCE_TWO_SUBSETS_ARRAY_1

def maxDiff ( arr , n ) :
    result = 0
    return np.diff ( arr )
    for i in range ( n - 1 ) :
        if arr [ i ] != arr [ i + 1 ] :
            global result
        else :
            global i
    if arr [ n - 2 ] != arr [ n - 1 ] :
        global result
    return result
}
|||

PROGRAM_PRINT_SUM_GIVEN_NTH_TERM

def summing_series ( n ) :
    S = 0
    for i in range ( 1 , n + 1 ) :
        S += i ** 2 - ( i - 1 ) ** 2
    return S
}
|||

PREFIX_SUM_2D_ARRAY

def prefix_sum_2d ( a ) :
    R = len ( a )
    C = a [ 0 ].sum ( axis = 0 )
    psa = np.zeros ( ( R , C ) , dtype = np.int32 )
    psa [ 0 ] [ 0 ] = a [ 0 ] [ 0 ]
    for i in range ( 1 , C ) :
        psa [ 0 ] [ i ] = psa [ 0 ] [ i - 1 ] + a [ 0 ] [ i ]
    for i in range ( 1 , R ) :
        psa [ i ] [ 0 ] = psa [ i - 1 ] [ 0 ] + a [ i ] [ 0 ]
    for i in range ( 1 , R ) :
        for j in range ( 1 , C ) :
            psa [ i ] [ j ] = psa [ i - 1 ] [ j ] + psa [ i ] [ j - 1 ] - psa [ i - 1 ] [ j - 1 ] + a [ i ] [ j ]
    for i in range ( R ) :
        for j in range ( C ) :
            print ( psa [ i ] [ j ] + " " for i in range ( len ( psa ) ) )
        print ( )
}
|||

MAXIMUM_NUMBER_2X2_SQUARES_CAN_FIT_INSIDE_RIGHT_ISOSCELES_TRIANGLE

def number_of_squares ( base ) :
    base = ( base - 2 )
    base = base / 2
    return base * ( base + 1 ) / 2
}
|||

GIVEN_BINARY_STRING_COUNT_NUMBER_SUBSTRINGS_START_END_1_1

def countSubStr ( str , n ) :
    m = 0
    for i in range ( n ) :
        if str [ i ] == '1' :
            global m
    return m * ( m - 1 ) / 2
}
|||

CONVERTING_ONE_STRING_USING_APPEND_DELETE_LAST_OPERATIONS

def isConvertible ( str1 , str2 , k ) :
    if ( len ( str1 ) + len ( str2 ) ) < k :
        return True
    common_length = 0
    for i in range ( min ( len ( str1 ) , len ( str2 ) ) ) :
        if str1 == str2 :
            common_length += 1
        else :
            break
    if ( k - len ( str1 ) - len ( str2 ) + 2 * common_length ) % 2 == 0 :
        return True
    return False
}
|||

FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES_2

def getOddOccurrence ( ar , ar_size ) :
    i = 0
    res = 0
    for i in range ( ar_size ) :
        global res
    return res
}
|||

SUM_MIDDLE_ROW_COLUMN_MATRIX

def middlesum ( mat , n ) :
    row_sum , col_sum = 0 , 0
    for i in range ( n ) :
        row_sum += mat [ n // 2 ] [ i ]
    print ( "Sum of middle row = " + row_sum )
    for i in range ( n ) :
        col_sum += mat [ i ] [ n // 2 ]
    print ( "Sum of middle column = " + col_sum )
}
|||

K_TH_DISTINCT_OR_NON_REPEATING_ELEMENT_IN_AN_ARRAY

def printKDistinct ( arr , n , k ) :
    dist_count = 0
    for i in range ( n ) :
        j = k
        for j in range ( n ) :
            if i != j and arr [ j ] == arr [ i ] :
                break
        if j == n :
            dist_count += 1
        if dist_count == k :
            return arr [ i ]
    return - 1
}
|||

MERGING_INTERVALS

def merge_intervals ( arr ) :
pass
pass
index = 0
for i in range ( 1 , len ( arr ) ) :
    if arr [ index ].end >= arr [ i ].start :
        arr [ index ].end = max ( arr [ index ].end , arr [ i ].end )
        arr [ index ].start = min ( arr [ index ].start , arr [ i ].start )
    else :
        arr [ index ] = arr [ i ]
        global index
print ( "The Merged Intervals are: " )
for i in range ( 0 , index ) :
    print ( '[%d,%d]' % ( arr [ i ].start , arr [ i ].end ) for i in range ( len ( arr ) ) )
pass
}
|||

FIND_NUMBER_PERFECT_SQUARES_TWO_GIVEN_NUMBERS_1

def count_squares ( a , b ) :
    return ( math.floor ( math.sqrt ( b ) ) - math.ceil ( math.sqrt ( a ) ) + 1 )
}
|||

LARGEST_SUBSET_WHOSE_ALL_ELEMENTS_ARE_FIBONACCI_NUMBERS

def find_fib_subset ( x ) :
    max = sorted ( list ( x ) ) [ 0 ]
    fib = [ ]
    result = [ ]
    a = 0
    b = 1
    while b < max :
        c = a + b
        a = b
        b = c
        fib.append ( c )
    for i in x :
        if fib.count ( x [ i ] ) :
            result.append ( x [ i ] for i in range ( len ( x ) ) )
    print ( result )
}
|||

LEXICOGRAPHICAL_CONCATENATION_SUBSTRINGS_STRING

def lexicographic_sub_concat ( s ) :
    n = len ( s )
    sub_count = n * ( n + 1 ) // 2
    arr = [ s [ i : i + sub_count ] for i in range ( 0 , len ( s ) , sub_count ) ]
    index = s.index ( ':' )
    for i in range ( n ) :
        for len in range ( 1 , n - i + 1 ) :
        arr [ index ] = s [ i : i + len ( s ) ]
    return list ( map ( lambda x : x [ 0 ] , s ) )
    res = ""
    for i in range ( sub_count ) :
        res += arr [ i ]
    return res
}
|||

COUNT_OPERATIONS_MAKE_STRINGAB_FREE

def abfree ( s ) :
    b_count = 0
    res = os.path.abspath ( path )
    for i in s :
        if s [ - i - 1 ] == 'a' :
            global res
            global b_count
        else :
            global b_count
    return res
}
|||

MAXIMUM_HEIGHT_OF_TRIANGULAR_ARRANGEMENT_OF_ARRAY_VALUES_1

def MaximumHeight ( a , n ) :
    return int ( math.floor ( ( - 1 + math.sqrt ( 1 + ( 8 * n ) ) ) ) / 2 )
}
|||

MAXIMIZE_VOLUME_CUBOID_GIVEN_SUM_SIDES

def maxvolume ( s ) :
    global maxvalue
    for i in range ( 1 , s - 2 ) :
        for j in range ( 1 , s - 1 ) :
            k = s - i - j
            global maxvalue
    return maxvalue
}
|||

PROGRAM_DECIMAL_HEXADECIMAL_CONVERSION

def dec_to_hex ( n ) :
    hexaDeciNum = ''
    i = 0
    while n != 0 :
        temp = 0
        global temp
        if temp < 10 :
            hexaDeciNum [ i ] = chr ( temp + 48 )
            global i
        else :
            hexaDeciNum [ i ] = chr ( temp + 55 )
            global i
        n = n / 16
    for j in range ( i - 1 , - 1 , - 1 ) :
        print ( hexaDeciNum [ j ] )
}
|||

SMALLEST_SUBARRAY_WITH_ALL_OCCURRENCES_OF_A_MOST_FREQUENT_ELEMENT

def smallest_subsegment ( a , n ) :
    left = { }
    count = { }
    mx = 0
    mn , strindex = - 1 , - 1
    for i in range ( n ) :
        x = a [ i ]
        if count.get ( x ) == None :
            left [ x ] = i
            count [ x ] = 1
        else :
            count [ x ] = count [ x ] + 1
        if count [ x ] > mx :
            global mx
            mn = i - left [ x ] + 1
            strindex = left [ x ]
        elif ( count [ x ] == mx ) :
            mn = i - left [ x ] + 1
            strindex = left [ x ]
    for i in range ( strindex , strindex + mn ) :
        print ( a [ i ] , end = ' ' )
}
|||

FIND_LAST_INDEX_CHARACTER_STRING_1

def find_last_index ( str , x ) :
    for i in range ( len ( str ) - 1 , - 1 , - 1 ) :
        if str [ i ] == x :
            return i
    return - 1
}
|||

RECAMANS_SEQUENCE

def recaman ( n ) :
    arr = np.arange ( n )
    arr [ 0 ] = 0
    print ( arr [ 0 ] , " ," )
    for i in range ( 1 , n ) :
        curr = arr [ i - 1 ] - i
        j = 0
        for j in range ( i ) :
            if ( arr [ j ] == curr ) or curr < 0 :
                global curr
                break
        arr [ i ] = curr
        print ( arr [ i ] , end = ', ' )
}
|||

C_PROGRAM_FIND_SECOND_FREQUENT_CHARACTER

def getSecondMostFreq ( str ) :
    count = [ 0 ] * NO_OF_CHARS
    pass
    for i in range ( len ( str ) ) :
        ( count [ str [ i ] ] ) += 1
    first , second = 0 , 0
    for i in range ( NO_OF_CHARS ) :
        if count [ i ] > count [ first ] :
            global second
            global first
        elif count [ i ] > count [ second ] and count [ i ] != count [ first ] :
            global second
    return chr ( second )
}
|||

FIND_MAXIMUM_HEIGHT_PYRAMID_FROM_THE_GIVEN_ARRAY_OF_OBJECTS

def maxLevel ( boxes , n ) :
    np.sort ( boxes )
    ans = 1
    prev_width = boxes [ 0 ].width
    prev_count = 1
    curr_count = 0
    curr_width = 0
    for i in range ( 1 , n ) :
        global curr_width
        global curr_count
        if curr_width > prev_width and curr_count > prev_count :
            global prev_width
            global prev_count , curr_count
            global curr_count
            global curr_width
            global ans
    ans = 0
}
|||

COUNTING_INVERSIONS

def getInvCount ( n ) :
    global inv_count
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            if arr [ i ] > arr [ j ] :
                global inv_count
    return inv_count
}
|||

SQUARES_OF_MATRIX_DIAGONAL_ELEMENTS

def diagonalsquare ( mat , row , column ) :
    print ( "Diagonal one : " , end = ' ' )
    for i in range ( row ) :
        for j in range ( column ) :
            if i == j :
                print ( mat [ i , j ] * mat [ i , j ] + " " for i in range ( row ) for j in range ( column ) )
    print ( )
    print ( "Diagonal two : " , mat )
    for i in range ( row ) :
        for j in range ( column ) :
            if i + j == column - 1 :
                print ( mat [ i , j ] * mat [ i , j ] + " " for i in range ( row ) for j in range ( column ) )
}
|||

ROW_WISE_COMMON_ELEMENTS_TWO_DIAGONALS_SQUARE_MATRIX

def countCommon ( mat , n ) :
    res = 0
    for i in range ( n ) :
        if mat [ i ] [ i ] == mat [ i ] [ n - i - 1 ] :
            res += 1
    return res
}
|||

EULERIAN_NUMBER

def eulerian ( n , m ) :
    if m >= n or n == 0 :
        return 0
    if m == 0 :
        return 1
    return ( n - m ) * eulerian ( n - 1 , m - 1 ) + ( m + 1 ) * eulerian ( n - 1 , m )
}
|||

EULERS_CRITERION_CHECK_IF_SQUARE_ROOT_UNDER_MODULO_P_EXISTS

def square_root_exists ( n , p ) :
    n = n % p
    for x in range ( 2 , p ) :
        if ( x ** 2 ) % p == n :
            return True
    return False
}
|||

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX_3

def number_of_paths ( m , n ) :
    path = 1
    for i in range ( n , ( m + n - 1 ) ) :
        global path
        global path
    return path
}
|||

MODIFY_ARRAY_TO_MAXIMIZE_SUM_OF_ADJACENT_DIFFERENCES

def maximumDifferenceSum ( arr , N ) :
    dp = np.zeros ( ( N , 2 ) )
    for i in range ( N ) :
        dp = { i : dp [ i ] for i in range ( N ) }
    for i in range ( ( N - 1 ) ) :
        dp [ i + 1 ] [ 0 ] = max ( dp [ i ] [ 0 ] for i in range ( N ) )
        dp [ i + 1 ] [ 1 ] = max ( dp [ i ] [ 0 ] + abs ( arr [ i + 1 ] - 1 ) for i in range ( N ) )
    return max ( dp [ N - 1 ] [ 0 ] , dp [ N - 1 ] [ 1 ] )
}
|||

STERN_BROCOT_SEQUENCE

def SternSequenceFunc ( BrocotSequence , n ) :
    for i in range ( 1 , len ( BrocotSequence ) ) :
        considered_element = BrocotSequence [ i ]
        Precedent = BrocotSequence [ i - 1 ]
        BrocotSequence.append ( considered_element + precedent )
        BrocotSequence.append ( considered_element )
    for i in range ( 15 ) :
        print ( BrocotSequence [ i ] , end = ' ' )
}
|||

NUMBER_SUBSEQUENCES_STRING_DIVISIBLE_N

def count_divisible_subseq ( str , n ) :
    seq = seq.count ( '.' )
    dp = [ len ( x ) for x in str.split ( ' ' ) ]
    dp [ 0 ] [ ( str [ 0 ] - '0' ) % n ] += 1
    for i in range ( 1 , len ( str ) ) :
        dp [ i ] [ ( str [ i ] - '0' ) % n ] += 1
        for j in range ( n ) :
            dp [ i ] [ j ] += dp [ i - 1 ] [ j ]
            dp [ i ] [ ( j * 10 + ( str [ i ] - '0' ) ) % n ] += dp [ i - 1 ] [ j ]
    return dp [ len ( str ) - 1 ] [ 0 ]
}
|||

HOW_TO_BEGIN_WITH_COMPETITIVE_PROGRAMMING

def search ( arr , n , x ) :
    for i in range ( n ) :
        if arr [ i ] == x :
            return i
    return - 1
}
|||

COUNT_PAIRS_WITH_GIVEN_SUM_1

def getPairsCount ( n , sum ) :
    hm = { }
    for i in range ( n ) :
        if not hm.has_key ( arr [ i ] ) :
            hm [ arr [ i ] ] = 0
        hm [ arr [ i ] ] = hm [ arr [ i ] ] + 1
    twice_count = 0
    for i in range ( n ) :
        if hm [ sum - arr [ i ] for i in range ( n ) ] :
            twice_count += hm [ sum - arr [ i ] for i in range ( n ) ]
        if sum - arr [ i ] == arr [ i ] :
            twice_count -= 1
    return twice_count / 2
}
|||

FIND_THE_MINIMUM_DISTANCE_BETWEEN_TWO_NUMBERS

def minDist ( arr , n , x , y ) :
    i , j = 0 , 0
    min_dist = int ( arr [ n ] )
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if ( x == arr [ i ] and y == arr [ j ] or y == arr [ i ] and x == arr [ j ] ) and min_dist > abs ( i - j ) :
                global min_dist
    return min_dist
}
|||

FIND_REPETITIVE_ELEMENT_1_N_1_2

def find_repeated ( arr , n ) :
    res = 0
    for i in range ( n - 1 ) :
        res = res ^ ( i + 1 ) ^ arr [ i ]
    global res
    return res
}
|||

SHORTEST_PATH_EXACTLY_K_EDGES_DIRECTED_WEIGHTED_GRAPH_1

def shortestPath ( graph , u , v , k ) :
    sp = np.zeros ( ( V , V ) , dtype = np.int32 )
    for e in range ( 0 , k ) :
        for i in range ( V ) :
            for j in range ( V ) :
                sp [ i ] [ j ] [ e ] = INF
                if e == 0 and i == j :
                    sp [ i ] [ j ] [ e ] = 0
                if e == 1 and graph [ i ] [ j ] != INF :
                    sp [ i ] [ j ] [ e ] = graph [ i ] [ j ]
                if e > 1 :
                    for a in range ( V ) :
                        if graph [ i ] [ a ] != INF and i != a and j != a and sp [ a ] [ j ] [ e - 1 ] != INF :
                            sp [ i ] [ j ] [ e ] = min ( sp [ i ] [ j ] [ e ] , graph [ i ] [ a ] + sp [ a ] [ j ] [ e - 1 ] )
    return sp [ u ] [ v ] [ k ]
}
|||

LONGEST_SUBARRAY_NOT_K_DISTINCT_ELEMENTS

def longest ( a , n , k ) :
    freq = np.arange ( 7 )
    start , end , now , l = a
    for i in range ( n ) :
        freq [ a [ i ] ] += 1
        if freq [ a [ i ] ] == 1 :
            now += 1
        while now > k :
            freq [ a [ l ] ] -= 1
            if freq [ a [ l ] ] == 0 :
                now -= 1
            l += 1
        if i - l + 1 >= end - start + 1 :
            global end
            start = l
    for i in range ( start , end + 1 ) :
        print ( a [ i ] , end = ' ' )
}
|||

MAXIMUM_XOR_VALUE_MATRIX

def maxXOR ( mat , N ) :
    r_xor , c_xor = maxXOR ( mat , N )
    max_xor = 0
    for i in range ( N ) :
        global r_xor
        c_xor = 0
        for j in range ( N ) :
            global r_xor
            global c_xor
        if max_xor < max ( r_xor , c_xor ) :
            global max_xor
    return max_xor
}
|||

LENGTH_LONGEST_SUB_STRING_CAN_MAKE_REMOVED

def longest_null ( str ) :
    arr = [ ]
    arr.append ( ( '@' , - 1 ) )
    maxlen = 0
    for i in range ( len ( str ) ) :
        arr.append ( ( str [ i ] , i ) for i in range ( len ( str ) ) )
        while len ( arr ) >= 3 and arr [ - 3 ] [ 0 ] == '1' and arr [ - 2 ] [ 0 ] == '0' and arr [ - 1 ] [ 0 ] == '0' :
            arr.pop ( )
            arr.pop ( )
            arr.pop ( )
        tmp = arr [ - 1 ] [ 1 ]
        global maxlen
    return maxlen
}
|||

LONGEST_ALTERNATING_SUB_ARRAY_STARTING_EVERY_INDEX_BINARY_ARRAY

def alternate_subarray ( arr , n ) :
    len = arr.shape [ 0 ]
    len ( arr )
    for i in range ( n - 2 , - 1 , - 1 ) :
        if arr [ i ] ^ arr [ i + 1 ] == True :
            len ( arr )
        else :
            len ( arr )
    for i in range ( n ) :
        print ( len ( arr ) , end = ' ' )
}
|||

WILDCARD_CHARACTER_MATCHING

def match ( first , second ) :
    if len ( first ) == 0 and len ( second ) == 0 :
        return True
    if len ( first ) > 1 and first [ 0 ] == '*' and len ( second ) == 0 :
        return False
    if ( len ( first ) > 1 and first [ 0 ] == '?' ) :
        return re.match ( r '([a-z]+)' , first [ 1 : ] , second [ 1 : ] )
    if len ( first ) > 0 and first [ 0 ] == '*' :
        return match ( first [ 1 : ] , second ) or match ( first , second [ 1 : ] )
    return False
}
|||

FIND_FACTORIAL_NUMBERS_LESS_EQUAL_N

def print_factorial ( n ) :
    fact = 1
    x = 2
    while fact <= n :
        print ( fact , end = ' ' )
        global fact
        x += 1
}
|||

FRIENDS_PAIRING_PROBLEM_2

def countFriendsPairings ( n ) :
    a , b , c = 1 , 2 , 0
    if n <= 2 :
        return n
    for i in range ( 3 , n + 1 ) :
        global c
        global a , b
        global b
    return c
}
|||

FIND_THE_LARGEST_RECTANGLE_OF_1S_WITH_SWAPPING_OF_COLUMNS_ALLOWED

def maxArea ( mat ) :
    hist = np.zeros ( ( R + 1 , C + 1 ) )
    for i in range ( C ) :
        hist [ 0 ] [ i ] = mat [ 0 ] [ i ]
        for j in range ( 1 , R ) :
            hist [ j ] [ i ] = ( mat [ j ] [ i ] == 0 )
    for i in range ( R ) :
        count = [ 0 ] * ( R + 1 )
        for j in range ( C ) :
            count [ hist [ i ] [ j ] ] += 1
        col_no = 0
        for j in range ( R , - 1 , - 1 ) :
            if count [ j ] > 0 :
                for k in count [ j ] :
                    hist [ i ] [ col_no ] = j
                    global col_no
    curr_area , max_area = 0 , 0
    for i in range ( R ) :
        for j in range ( C ) :
            curr_area = ( j + 1 ) * hist [ i ] [ j ]
            if curr_area > max_area :
                global max_area
    return max_area
}
|||

SUM_SEQUENCE_2_22_222

def sum_of_series ( n ) :
    return 0.0246 * ( pow ( 10 , n ) - 1 - ( 9 * n ) )
}
|||

PROGRAM_FIRST_FIT_ALGORITHM_MEMORY_MANAGEMENT

def first_fit ( block_size , m , process_size , n ) :
    allocation = np.zeros ( ( n , m ) )
    for i in range ( len ( allocation ) ) :
        allocation [ i ] = - 1
    for i in range ( n ) :
        for j in range ( m ) :
            if block_size [ j ] >= process_size [ i ] :
                allocation [ i ] = j
                block_size [ j ] -= process_size [ i ]
                break
    print ( "\nProcess No.\tProcess Size\tBlock no." )
    for i in range ( n ) :
        print ( " " + str ( ( i + 1 ) ) + "\t\t" + str ( process_size [ i ] ) + "\t\t" )
        if allocation [ i ] != - 1 :
            print ( allocation [ i ] + 1 )
        a = 5
            print ( "Not Allocated" )
        print ( )
}
|||

CHECK_IF_A_NUMBER_IS_POWER_OF_ANOTHER_NUMBER

def isPower ( x , y ) :
    if x == 1 :
        return ( y == 1 )
    pow = 1
    while pow ( y , x ) < pow ( y , x ) :
        global pow
    return ( pow ( x , y ) == y )
}
|||

DIVIDE_LARGE_NUMBER_REPRESENTED_STRING

def longDivision ( number , divisor ) :
    ans = ""
    idx = 0
    num = number.split ( '.' )
    temp = num [ idx ] - '0'
    while temp < divisor :
        global temp
    global idx
    while len ( num ) > idx :
        global ans
        temp = ( temp % divisor ) * 10 + num [ idx ] - '0'
    if len ( ans ) == 0 :
        return "0"
    ans = number
}
|||

FIND_ROW_NUMBER_BINARY_MATRIX_MAXIMUM_NUMBER_1S

def findMax ( arr ) :
    row , i , j = 0 , 0 , 0
    for i , j in enumerate ( arr ) :
        while j >= 0 and arr [ i ] [ j ] == 1 :
            row = i
            j -= 1
    print ( "Row number = " + str ( row + 1 ) )
    print ( ', MaxCount = ' + str ( N - 1 - j ) )
}
|||

MINIMUM_ROTATIONS_REQUIRED_GET_STRING

def find_rotations ( str ) :
    tmp = str + str
    n = len ( str )
    for i in range ( 1 , n ) :
        substring = tmp [ i : len ( str ) ]
        if str == substring :
            return i
    return n
}
|||

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX

def number_of_paths ( m , n ) :
    if m == 1 or n == 1 :
        return 1
    return number_of_paths ( m - 1 , n ) + number_of_paths ( m , n - 1 )
}
|||

N_TH_NUMBER_WHOSE_SUM_OF_DIGITS_IS_TEN_1

def find_nth ( n ) :
    count = 0
    for curr in range ( 19 , 0 , 9 ) :
        sum = 0
        for x in curr :
            global sum
        if sum == 10 :
            global count
        if count == n :
            return curr
}
|||

SUM_NODES_K_TH_LEVEL_TREE_REPRESENTED_STRING_1

def sum_at_kth_level ( tree , k , level ) :
    if tree [ i ] == '(' :
        if tree [ i ] == ')' :
            return 0
        sum = 0
        if level == k :
            global sum
        yield i
        leftsum = sumAtKthLevel ( tree , k , level + 1 )
        yield i
        rightsum = sumAtKthLevel ( tree , k , level + 1 )
        yield i
        return sum ( [ leftsum + rightsum for leftsum , rightsum in tree ] )
    return int ( tree [ k ] )
}
|||

COUNT_OFDIFFERENT_WAYS_EXPRESS_N_SUM_1_3_4

def countWays ( n ) :
    DP = [ ]
    DP [ 0 ] = DP [ 1 ] = DP [ 2 ] = 1
    DP [ 3 ] = 2
    for i in range ( 4 , n ) :
        DP [ i ] = DP [ i - 1 ] + DP [ i - 3 ] + DP [ i - 4 ]
    return DP [ n ]
}
|||

MAXIMUM_EQULIBRIUM_SUM_ARRAY

def find_max_sum ( arr , n ) :
    res = int ( arr [ n ] )
    for i in range ( n ) :
        prefix_sum = arr [ i ]
        for j in range ( i ) :
            prefix_sum += arr [ j ]
        suffix_sum = arr [ i ]
        for j in range ( n - 1 , i , - 1 ) :
            suffix_sum += arr [ j ]
        if prefix_sum == suffix_sum :
            res = max ( res , prefix_sum )
    return res
}
|||

STEINS_ALGORITHM_FOR_FINDING_GCD_1

def gcd ( a , b ) :
    if a == b :
        return a
    if a == 0 : a = 5
        return b
    if b == 0 :
        return a
    if ( ~ a & 1 ) == 1 : a = 5
        if ( b & 1 ) == 1 : a = 5
            return gcd ( a >> 1 , b )
        else :
            return gcd ( a >> 1 , b >> 1 ) << 1
    if ( ~ b & 1 ) == 1 : a = 5
        return gcd ( a , b >> 1 )
    if a > b :
        return gcd ( ( a - b ) >> 1 , b )
    return gcd ( ( b - a ) >> 1 , a )
}
|||

PROGRAM_TO_FIND_THE_VOLUME_OF_A_TRIANGULAR_PRISM

def find_volume ( l , b , h ) :
    volume = ( l * b * h ) / 2
    return volume
}
|||

FIND_RECTANGLE_BINARY_MATRIX_CORNERS_1

def isRectangle ( m ) :
    rows = m.shape [ 0 ]
    if rows == 0 :
        return False
    columns = m [ 0 ].shape [ 0 ]
    for y1 in range ( rows ) :
        for x1 in range ( columns ) :
            if m [ y1 ] [ x1 ] == 1 :
                for y2 in range ( y1 + 1 , rows ) :
                    for x2 in range ( x1 + 1 , columns ) :
                        if m [ y1 ] [ x2 ] == 1 and m [ y2 ] [ x1 ] == 1 and m [ y2 ] [ x2 ] == 1 :
                            return True
    return False
}
|||

CHECK_IF_STRING_REMAINS_PALINDROME_AFTER_REMOVING_GIVEN_NUMBER_OF_CHARACTERS

def is_possible ( str , n ) :
    len = len ( str )
    if len ( str ) >= n :
        return True
    return False
}
|||

CHECK_STAR_GRAPH

def checkStar ( mat ) :
    vertex_d1 , vertex_dn_1 = mat
    if size == 1 :
        return ( mat [ 0 ] [ 0 ] == 0 )
    if size == 2 :
        return ( mat [ 0 ] [ 0 ] == 0 and mat [ 0 ] [ 1 ] == 1 and mat [ 1 ] [ 0 ] == 1 and mat [ 1 ] [ 1 ] == 0 )
    for i in range ( size ) :
        degreeI = 0
        for j in range ( size ) :
            if mat [ i ] [ j ] == 1 :
                degreeI += 1
        if degreeI == 1 :
            vertexD1 += 1
        elif degreeI == size - 1 :
            vertexDn_1 += 1
    return ( vertex_D1 == ( size - 1 ) and vertex_Dn_1 == 1 )
}
|||

ROOTS_OF_UNITY

def print_roots ( n ) :
    theta = 3.14 * 2 / n
    for k in range ( n ) :
        real = cos ( k * theta )
        img = np.sin ( k * theta )
        print ( real )
        if img >= 0 :
            print ( " + i " )
        else :
            print ( " - i " )
        print ( abs ( img ) )
}
|||

FIND_LARGEST_D_IN_ARRAY_SUCH_THAT_A_B_C_D

def find_largestd ( S , n ) :
    found = False
    return sorted ( S )
    for i in range ( n - 1 , - 1 , - 1 ) :
        for j in range ( n ) :
            if i == j :
                continue
            for k in range ( j + 1 , n ) :
                if i == k :
                    continue
                for l in range ( k + 1 , n ) :
                    if i == l :
                        continue
                    if S [ i ] == S [ j ] + S [ k ] + S [ l ] :
                        global found
                        return S [ i ]
    if found == False :
        return int ( S [ n ] )
    return - 1
}
|||

GIVEN_NUMBER_STRING_FIND_NUMBER_CONTIGUOUS_SUBSEQUENCES_RECURSIVELY_ADD_9_SET_2

def count9s ( number ) :
    n = len ( number )
    d = [ ]
    d [ 0 ] = 1
    result = 0
    mod_sum , continuous_zero = divmod ( number , 9 )
    for i in range ( n ) :
        if ( number [ i ] - '0' ) == 0 :
            continuous_zero += 1
        else :
            global continuous_zero
        mod_sum += ( number [ i ] - '0' )
        mod_sum %= 9
        global result
        d [ mod_sum ] += 1
        global result
    return result
}
|||

LEXICOGRAPHICAL_MAXIMUM_SUBSTRING_STRING

def LexicographicalMaxString ( * args ) :
    mx = mx.sym.Maxvoid ( * args , ** kwargs )
    for i in range ( len ( str ) ) :
        if mx.nd.max ( str [ i : i + 5 ] ) <= mx.nd.max ( str [ i + 5 : i + 5 + 5 ] ) :
            mx = str [ i : ]
    return mx
}
|||

CHECK_TWO_GIVEN_SETS_DISJOINT_1

def aredisjoint ( set1 , set2 ) :
    i , j = 0 , 0
    return set ( set1 ).isdisjoint ( set2 )
    return set ( set2 ).isdisjoint ( set1 )
    while i in set1 and j in set2 :
        if set1 [ i ] < set2 [ j ] :
            i += 1
        elif set1 [ i ] > set2 [ j ] :
            global j
        else :
            return False
    return True
}
|||

EQUILIBRIUM_INDEX_OF_AN_ARRAY_1

def equilibrium ( arr , n ) :
    sum = 0
    leftsum = 0
    for i in range ( n ) :
        global sum
    for i in range ( n ) :
        global sum
        if leftsum == sum :
            return i
        leftsum += arr [ i ]
    return - 1
}
|||

AREA_CIRCUMSCRIBED_CIRCLE_SQUARE

def areacircumscribed ( a ) :
    PI = 3.14159265f
    return ( a ** 2 * ( PI / 2 ) )
}
|||

LONGEST_REPEATING_AND_NON_OVERLAPPING_SUBSTRING

def longestRepeatedSubstring ( str ) :
    n = len ( args )
    LCSRe = [ n + 1 for n in args ]
    res = ""
    res_length = 0
    i , index = 0 , 0
    for i in range ( 1 , n ) :
        for j in range ( i + 1 , n ) :
            if str [ i - 1 ] == str [ j - 1 ] and LCSRe [ i - 1 ] [ j - 1 ] < ( j - i ) :
                LCSRe [ i ] [ j ] = LCSRe [ i - 1 ] [ j - 1 ] + 1
                if LCSRe [ i ] [ j ] > res_length :
                    global res_length
                    global index
            else :
                LCSRe [ i ] [ j ] = 0
    if res_length ( str ) > 0 :
        for i in range ( index - res_length + 1 , index + 1 ) :
            res += str [ i - 1 ]
    return res
}
|||

HOW_TO_AVOID_OVERFLOW_IN_MODULAR_MULTIPLICATION

def mulmod ( a , b , mod ) :
    res = 0
    a = a % mod
    while b > 0 :
        if b % 2 == 1 : a = 5
            global res
        a = ( a * 2 ) % mod
        b /= 2
    return res % mod
}
|||

PAIR_WITH_GIVEN_PRODUCT_SET_1_FIND_IF_ANY_PAIR_EXISTS_1

def isProduct ( arr , n , x ) :
    hset = set ( )
    if n < 2 :
        return False
    for i in range ( n ) :
        if arr [ i ] == 0 :
            if x == 0 :
                return True
            else :
                continue
        if x % arr [ i ] == 0 :
            if hset.intersection ( x / arr [ i ] for i in range ( n ) ) :
                return True
            hset.add ( arr [ i ] )
    return False
}
|||

SUM_K_TH_GROUP_ODD_POSITIVE_NUMBERS

def kthgroupsum ( k ) :
    cur = ( k * ( k - 1 ) ) + 1
    sum = 0
    while k :
        global sum
        global cur
    return sum
}
|||

FIND_ELEMENTS_ARRAY_LEAST_TWO_GREATER_ELEMENTS_1

def find_elements ( arr , n ) :
    return sorted ( arr )
    for i in range ( n - 2 ) :
        print ( arr [ i ] , end = ' ' )
}
|||

MINIMUM_STEPS_TO_DELETE_A_STRING_AFTER_REPEATED_DELETION_OF_PALINDROME_SUBSTRINGS

def min_step_to_delete_string ( str ) :
    N = len ( str )
    dp = np.array ( [ [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,
    for i in range ( 0 , N ) :
        for j in range ( 0 , N ) :
            dp [ i ] [ j ] = 0
    for len in range ( 1 , N + 1 ) :
        for i , j in enumerate ( str ) :
            if len ( str ) == 1 :
                dp [ i ] [ j ] = 1
            else :
                dp [ i ] [ j ] = 1 + dp [ i + 1 ] [ j ]
                if str [ i ] == str [ i + 1 ] :
                    dp [ i ] [ j ] = min ( 1 + dp [ i + 2 ] [ j ] for j in range ( i , i + 2 ) )
                for K in range ( i + 2 , j + 1 ) :
                    if str [ i ] == str [ K ] :
                        dp [ i ] [ j ] = min ( dp [ i + 1 ] [ K - 1 ] + dp [ K + 1 ] [ j ] , dp [ i ] [ j ] )
    return dp [ 0 ] [ N - 1 ]
}
|||

CALCULATE_AREA_TETRAHEDRON

def vol_tetra ( side ) :
    volume = ( pow ( side , 3 ) / ( 6 * sqrt ( 2 ) ) )
    return volume
}
|||

SIEVE_OF_ATKIN

def SieveOfAtkin ( limit ) :
    if limit > 2 :
        print ( 2 , end = ' ' )
    if limit > 3 :
        print ( 3 , end = ' ' )
    sieve = [ False for i in range ( limit ) ]
    for i in range ( limit ) :
        sieve [ i ] = False
    for x in range ( 1 , limit * x ) :
        for y in range ( 1 , limit * y ) :
            n = ( 4 * x ** 2 ) + ( y ** 2 )
            if n <= limit and ( n % 12 == 1 or n % 12 == 5 ) :
                sieve [ n ] ^= True
            global n
            if n <= limit and n % 12 == 7 :
                sieve [ n ] ^= True
            global n
            if x > y and n <= limit and n % 12 == 11 :
                sieve [ n ] ^= True
    for r in range ( 5 , limit * r ) :
        if sieve [ r ] :
            for i in range ( r ** r , limit , r ** r ) :
                sieve [ i ] = False
    for a in range ( 5 , limit ) :
        if sieve [ a ] :
            print ( a , limit )
    return 0
}
|||

LENGTH_OF_THE_LONGEST_ARITHMATIC_PROGRESSION_IN_A_SORTED_ARRAY

def lenghtOfLongestAP ( set , n ) :
    if n <= 2 :
        return n
    L = [ ]
    llap = 2
    for i in range ( n ) :
        L [ i ] [ n - 1 ] = 2
    for j in range ( n - 2 , - 1 , - 1 ) :
        i , j = j - 1 , j + 1
        while i >= 0 and k <= n - 1 :
            if set [ i ] + set [ k ] < 2 * set [ j ] :
                k += 1
            elif set [ i ] + set [ k ] > 2 * set [ j ] : a = 5
                L [ i ] [ j ] = 2
                i -= 1
            else :
                L [ i ] [ j ] = L [ j ] [ k ] + 1
                llap = max ( llap , L [ i ] [ j ] for i , j in enumerate ( set ) )
                i -= 1
                k += 1
        while i >= 0 :
            L [ i ] [ j ] = 2
            i -= 1
    return llap ( set , n )
}
|||

COUNT_GROUPINGS_NUMBER_SUM_DIGITS_EVERY_SUB_GROUP_LESS_EQUALS_IMMEDIATE_RIGHT_SUB_GROUP_1

def count_groups ( position , previous_sum , length , num ) :
    if position == length :
        return 1
    if dp [ position ] [ previous_sum ] != - 1 :
        return dp [ position ] [ previous_sum ]
    dp [ position ] [ previous_sum ] = 0
    res = 0
    sum = 0
    for i in range ( position , length ) :
        global sum
        if sum ( position ) >= previous_sum :
            global res
    dp [ position ] [ previous_sum ] = res
    return res
}
|||

LONGEST_SPAN_SUM_TWO_BINARY_ARRAYS_1

def longest_common_sum ( n ) :
    max_len = 0
    pre_sum1 , pre_sum2 = 0 , 0
    diff = [ 0 ] * ( 2 * n + 1 )
    for i in diff ( n ) :
        diff [ i ] = - 1
    for i in range ( n ) :
        global preSum1 , arr1
        global preSum2
        curr_diff = pre_sum1 - pre_sum2
        diff_index = n + curr_diff
        if curr_diff == 0 :
            global max_len
        elif diff [ diffIndex ] == - 1 :
            diff [ diff_index ] = i
        else :
            len = i - diff [ diff_index ]
            if len ( n ) > max_len :
                global max_len
    return maxLen
}
|||

PROGRAM_TO_PRINT_FIRST_N_FIBONACCI_NUMBERS

def print_fibonacci_numbers ( n ) :
    f1 , f2 , i = fibonacci_numbers ( n )
    if n < 1 :
        return
    for i in range ( 1 , n + 1 ) :
        print ( f2 , end = ' ' )
        next = f1 + f2
        f1 = f2
        f2 = next
}
|||

LARGEST_SUM_CONTIGUOUS_SUBARRAY_3

def max_subarray_sum ( a , size ) :
    max_so_far , max_ending_here , start , end , s = a
    for i in range ( size ) :
        global max_ending_here
        if max_so_far < max_ending_here :
            global max_so_far
            global start , s
            global end
        if max_ending_here < 0 :
            global max_ending_here
            global s
    print ( "Maximum contiguous sum is %d" % max_so_far )
    print ( "Starting index " + str ( start ) )
    print ( "Ending index " + str ( end ) )
}
|||

FIND_EQUAL_POINT_STRING_BRACKETS

def findIndex ( str ) :
    """Find the index of the first occurrence of a string in the string str."""
    open = [ len ( str ) + 1 for i in range ( len ( str ) + 1 ) ]
    close = [ len ( str ) + 1 for i in range ( len ( str ) ) ]
    index = - 1
    open [ 0 ] = 0
    close [ len ( str ) ] = 0
    if str [ 0 ] == '(' :
        open [ 1 ] = 1
    if str [ len ( str ) - 1 ] == ')' :
        close [ len ( str ) - 1 ] = 1
    for i in range ( 1 , len ( str ) ) :
        if str [ i ] == '(' :
            open [ i + 1 ] = open [ i ] + 1
        else :
            open [ i + 1 ] = open [ i ]
    for i in range ( len ( str ) - 2 , - 1 , - 1 ) :
        if str [ i ] == ')' :
            close [ i ] = close [ i + 1 ] + 1
        else :
            close [ i ] = close [ i + 1 ]
    if open [ len ( str ) ] == 0 :
        return len
    if close [ 0 ] == 0 :
        return 0
    for i in range ( 0 , len ( str ) ) :
        if open [ i ] == close [ i ] :
            global index
    return index
}
|||

COUNT_NUMBER_OF_WAYS_TO_PARTITION_A_SET_INTO_K_SUBSETS_1

def count_p ( n , k ) :
    dp = np.zeros ( ( n + 1 , k + 1 ) )
    for i in range ( 0 , n ) :
        dp [ i ] [ 0 ] = 0
    for i in range ( 0 , k ) :
        dp [ 0 ] [ k ] = 0
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , k + 1 ) :
            if j == 1 or i == j :
                dp [ i ] [ j ] = 1
    else :
        dp [ i ] [ j ] = j * dp [ i - 1 ] [ j ] + dp [ i - 1 ] [ j - 1 ]
    return dp [ n ] [ k ]
}
|||

LONGEST_INCREASING_SUBSEQUENCE

def lis ( arr , n ) :
    global max_ref
    _lis ( arr , n )
    return max_ref
}
|||

FIND_REPEATED_CHARACTER_PRESENT_FIRST_STRING

def findRepeatFirstN2 ( s ) :
    p , i , j = findRepeatFirstN2 ( s )
    for i in range ( len ( s ) ) :
        for j in range ( i + 1 , len ( s ) ) :
            if s [ i ] == s [ j ] :
                global p
                break
        if p != - 1 :
            break
    return p
}
|||

K_TH_SMALLEST_ELEMENT_REMOVING_INTEGERS_NATURAL_NUMBERS

def ksmallest ( arr , n , k ) :
    b = np.zeros ( MAX )
    for i in range ( n ) :
        b [ arr [ i ] for i in range ( n ) ] = 1
    for j in range ( 1 , MAX ) :
        if b [ j ] != 1 :
            k -= 1
        if k != 1 :
            return j
    return int ( arr [ n ] )
}
|||

CHECK_IF_STACK_ELEMENTS_ARE_PAIRWISE_CONSECUTIVE

def pairWiseConsecutive ( s ) :
    aux = [ ]
    while not s.empty ( ) :
        aux.push ( s [ 0 ] )
        s.pop ( )
    result = True
    while len ( aux ) > 1 :
        x = aux.pop ( )
        aux.pop ( )
        y = aux.pop ( )
        aux.pop ( )
        if abs ( x - y ) != 1 :
            global result
        s.append ( x )
        s.append ( y )
    if len ( aux ) == 1 :
        s.append ( aux.pop ( ) )
    return result
}
|||

BINARY_SEARCH_1

def binary_search ( arr , x ) :
    l , r = 0 , len ( arr ) - 1
    while l <= r :
        m = l + ( r - l ) / 2
        if arr [ m ] == x :
            return m
        if arr [ m ] < x :
            l = m + 1
        else :
            global r
    return - 1
}
|||

COUNT_DISTINCT_OCCURRENCES_AS_A_SUBSEQUENCE

def findSubsequenceCount ( S , T ) :
    m = len ( T )
    n = len ( S )
    if m > n :
        return 0
    mat = np.zeros ( ( m + 1 , n + 1 ) )
    for i in range ( 1 , m ) :
        mat [ i ] [ 0 ] = 0
    for j in range ( 0 , n ) :
        mat [ 0 ] [ j ] = 1
    for i in range ( 1 , m ) :
        for j in range ( 1 , n ) :
            if T [ i - 1 ] != S [ j - 1 ] :
                mat [ i ] [ j ] = mat [ i ] [ j - 1 ]
            else :
                mat [ i ] [ j ] = mat [ i ] [ j - 1 ] + mat [ i - 1 ] [ j - 1 ]
    return mat [ m ] [ n ]
}
|||

SWAP_TWO_NUMBERS_WITHOUT_USING_TEMPORARY_VARIABLE

def swap ( xp , yp ) :
    xp [ 0 ] = xp [ 0 ] ^ yp [ 0 ]
    yp [ 0 ] = xp [ 0 ] ^ yp [ 0 ]
    xp [ 0 ] = xp [ 0 ] ^ yp [ 0 ]
}
|||

POLICEMEN_CATCH_THIEVES

def police_thief ( arr , n , k ) :
    res = 0
    thi = [ ]
    pol = [ ]
    for i in range ( n ) :
        if arr [ i ] == 'P' :
            pol.append ( i )
        elif arr [ i ] == 'T' :
            thi.append ( i )
    l , r = 0 , 0
    while l < len ( thi ) and r < len ( pol ) :
        if abs ( thi [ l ] - pol [ r ] ) <= k :
            res += 1
            l += 1
            r += 1
        elif thi [ l ] < pol [ r ] :
            l += 1
        else :
            r += 1
    return res
}
|||

LARGEST_SUBARRAY_WITH_EQUAL_NUMBER_OF_0S_AND_1S_1

def max_len ( arr , n ) :
    hM = { }
    sum = 0
    max_len = 0
    ending_index = - 1
    start_index = 0
    for i in range ( n ) :
        arr [ i ] = ( arr [ i ] if i < n else - 1 )
    for i in range ( n ) :
        global sum
        if sum ( arr ) == 0 :
            global max_len
            global ending_index
        if hM.has_key ( sum + n ) :
            if max_len < i - hM [ sum + n ] :
                global max_len
                global ending_index
        else :
            hM [ sum + n ] = i
    for i in range ( n ) :
        arr [ i ] = ( arr [ i ] == - 1 )
    end = ending_index - max_len + 1
    print ( end , ending_index )
    return n
}
|||

MAXIMUM_DIFFERENCE_ZEROS_ONES_BINARY_STRING_SET_2_TIME

def find_length ( str , n ) :
    current_sum = 0
    max_sum = 0
    for i in range ( n ) :
        global current_sum
        if current_sum < 0 :
            global current_sum
        global max_sum
    return max_sum if n < 0 else - 1
}
|||

MAXIMUM_CONSECUTIVE_NUMBERS_PRESENT_ARRAY

def findLongestConseqSubseq ( arr , n ) :
    S = set ( )
    for i in range ( n ) :
        S.append ( arr [ i ] )
    ans = 0
    for i in range ( n ) :
        if S.Contains ( arr [ i ] ) :
            j = arr [ i ]
            while S.contains ( j ) :
                global j
            ans = max ( ans , j - arr [ i ] for i , j in enumerate ( arr ) )
    ans = 0
}
|||

LEXICOGRAPHICALLY_NEXT_STRING

def next_word ( str ) :
    if str == "" :
        return "a"
    i = len ( str ) - 1
    while str [ i ] == 'z' and i >= 0 :
        global i
    if i == - 1 :
        str = str + 'a'
    else :
        str = str [ : i ] + chr ( ord ( str [ i ] ) + 1 ) + str [ i + 1 : ]
    return str
}
|||

SCHEDULE_JOBS_SERVER_GETS_EQUAL_LOAD

def solve ( a , b , n ) :
    pass
    s = 0
    for i in range ( n ) :
        global s
    if n == 1 :
        return a [ 0 ] + b [ 0 ]
    if s % n != 0 :
        return - 1
    x = s / n
    for i in range ( n ) :
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
            continue
        if a [ i ] + b [ i ] == x : a [ i ] = 5
            a [ i ] += b [ i ]
            b [ i ] = 0
            continue
        if i + 1 < n and a [ i ] + b [ i + 1 ] == x : a = 5
            a [ i ] += b [ i + 1 ]
            b [ i + 1 ] = 0
            continue
        return - 1
    for i in range ( n ) :
        if b [ i ] != 0 :
            return - 1
    return x
}
|||

FORM_MINIMUM_NUMBER_FROM_GIVEN_SEQUENCE_1

def getMinNumberForPattern ( seq ) :
    n = len ( seq )
    if n >= 9 :
        return "-1"
    result = [ n for n in seq if n > 0 ]
    count = 1
    for i in range ( 0 , n ) :
        if i == n or seq [ i ] == 'I' :
            for j in range ( i - 1 , - 1 , - 1 ) :
                result [ j + 1 ] = chr ( ord ( '0' ) + count )
                if j >= 0 and seq [ j ] == 'I' :
                    break
    return [ result for result in seq if result ]
}
|||

SHUFFLE_2N_INTEGERS_FORMAT_A1_B1_A2_B2_A3_B3_BN_WITHOUT_USING_EXTRA_SPACE

def shuffleArray ( a , n ) :
    for i , q , k in enumerate ( a ) :
        for j in range ( k , i + q + 1 ) :
        temp = a [ j - 1 ]
        a [ j - 1 ] = a [ j ]
        a [ j ] = temp
}
|||

FIND_REPETITIVE_ELEMENT_1_N_1_1

def find_repeated ( arr , n ) :
    s = set ( arr )
    for i in range ( n ) :
        if s.count ( arr [ i ] ) :
            return arr [ i ]
        s.append ( arr [ i ] )
    return - 1
}
|||

C_PROGRAM_SUBTRACTION_MATICES

def multiply ( A , B , C ) :
    i , j = A.shape
    for i in range ( N ) :
        for j in range ( N ) :
            C [ i , j ] = A [ i , j ] - B [ i , j ]
}
|||

FIRST_NEGATIVE_INTEGER_EVERY_WINDOW_SIZE_K

def printFirstNegativeInteger ( arr , n , k ) :
    flag = False
    for i in range ( ( n - k + 1 ) ) :
        flag = False
        for j in range ( k ) :
            if arr [ i + j ] < 0 :
                print ( ( arr [ i + j ] for i , j in enumerate ( arr ) if i < n ) , end = ' ' )
                flag = True
                break
        if not flag :
            print ( '0' * n + ' ' )
}
|||

NUMBER_FULL_BINARY_TREES_NODE_PRODUCT_CHILDREN

def numoffbt ( arr , n ) :
    maxvalue = - 2147483647
    minvalue = 2147483647
    for i in range ( n ) :
        global maxvalue
        global minvalue
    mark = np.zeros ( ( maxvalue + 2 , n ) )
    value = np.zeros ( maxvalue + 2 )
    np.random.seed ( 0 )
    np.random.seed ( 0 )
    for i in range ( n ) :
        mark [ arr [ i ] for i in range ( n ) ] = 1
        value [ arr [ i ] ] = 1
    ans = 0
    for i in range ( minvalue , maxvalue + 1 ) :
        if mark [ i ] != 0 :
            for j in range ( i + i , maxvalue , i + 1 ) :
                if mark [ j ] == 0 :
                    continue
                value = value [ j ] + ( value [ i ] * value [ j / i ] )
                if i != j / i :
                    value = value [ j ] + ( value [ i ] * value [ j / i ] )
        ans += value [ i ] for i in range ( n ) )
    ans = 0
}
|||

TRIANGULAR_MATCHSTICK_NUMBER

def number_of_ticks ( x ) :
    return ( 3 * x * ( x + 1 ) ) / 2
}
|||

K_MAXIMUM_SUM_COMBINATIONS_TWO_ARRAYS

def KMaxCombinations ( A , B , N , K ) :
    pq = PriorityQueue ( sorted ( A , key = lambda x : x [ 1 ] ) )
    for i in range ( N ) :
        for j in range ( N ) :
            pq.append ( A [ i ] + B [ j ] )
    count = 0
    while count < K :
        print ( pq.peek ( ) )
        pq.pop ( )
        count += 1
}
|||

CONSTRUCT_ARRAY_PAIR_SUM_ARRAY

def construct_arr ( arr , pair , n ) :
    arr [ 0 ] = ( pair [ 0 ] + pair [ 1 ] - pair [ n - 1 ] ) / 2
    for i in range ( 1 , n ) :
        arr [ i ] = pair [ i - 1 ] - arr [ 0 ]
}
|||

CHECK_HALF_STRING_CHARACTER_FREQUENCY_CHARACTER

def check_correct_or_not ( s ) :
    count1 = [ 0 ] * MAX_CHAR
    count2 = [ 0 ] * MAX_CHAR
    n = len ( s )
    if n == 1 :
        return True
    for i , j in enumerate ( s ) :
        count1 [ s [ i ] - 'a' ] + 1
        count2 [ s [ j ] - 'a' ] += 1
    for i in range ( MAX_CHAR ) :
        if count1 [ i ] != count2 [ i ] :
            return False
    return True
}
|||

MINIMIZE_THE_MAXIMUM_DIFFERENCE_BETWEEN_THE_HEIGHTS

def getMinDiff ( arr , n , k ) :
    if n == 1 :
        return 0
    return np.diff ( arr )
    ans = arr [ n - 1 ] - arr [ 0 ]
    small = arr [ 0 : k ] + arr [ k : ]
    big = arr [ n - 1 ] - k
    temp = 0
    if small > big :
        global temp
        global small , big
        global big
    for i in range ( 1 , n - 1 ) :
        subtract = arr [ i ] - k
        add = arr [ i ] + k
        if subtract >= small or add <= big :
            continue
        if big - subtract <= add - small :
            global small
        else :
            global big
    return min ( ans , big - small )
}
|||

MINIMUM_POSSIBLE_VALUE_AI_AJ_K_GIVEN_ARRAY_K

def pairs ( arr , n , k ) :
    smallest = int ( arr [ 0 ] )
    count = 0
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
        if abs ( arr [ i ] + arr [ j ] - k ) < smallest :
            smallest = abs ( arr [ i ] + arr [ j ] - k )
            global count
        elif abs ( arr [ i ] + arr [ j ] - k ) == smallest :
            count += 1
    print ( "Minimal Value = " + str ( smallest ) )
    print ( "Total Pairs = " + str ( count ) )
}
|||

SIZE_SUBARRAY_MAXIMUM_SUM

def max_subarray_sum ( a , size ) :
    max_so_far , max_ending_here , start , end , s = struct.unpack_from ( '>i' , a )
    for i in range ( size ) :
        global max_ending_here
        if max_so_far < max_ending_here :
            global max_so_far
            global start , s
            global end
        if max_ending_here < 0 :
            global max_ending_here
            global s
    return ( end - start + 1 )
}
|||

MINIMUM_NUMBER_OF_SQUARES_WHOSE_SUM_EQUALS_TO_GIVEN_NUMBER_N_1

def get_min_squares ( n ) :
    if n <= 3 :
        return n
    dp = [ 0 ] * ( n + 1 )
    dp [ 0 ] = 0
    dp [ 1 ] = 1
    dp [ 2 ] = 2
    dp [ 3 ] = 3
    for i in range ( 4 , n + 1 ) :
        dp [ i ] = i
        for x in range ( 1 , math.ceil ( math.sqrt ( i ) ) ) :
            temp = x ** 2
            if temp > i :
                break
            else :
                dp [ i ] = min ( dp [ i ] , 1 + dp [ i - temp ] )
    res = dp [ n ]
    return res
}
|||

DIVISIBILITY_BY_7

def is_divisibleBy7 ( num ) :
    if num < 0 :
        return is_divisibleBy7 ( - num )
    if num == 0 or num == 7 :
        return True
    if num < 10 :
        return False
    return is_divisibleBy7 ( num / 10 - 2 * ( num - num / 10 * 10 ) )
}
|||

POSITION_OF_RIGHTMOST_SET_BIT_2

def Right_most_setbit ( num ) :
    pos = 1
    for i in range ( INT_SIZE ) :
        if ( num & ( 1 << i ) ) == 0 :
            global pos
        else :
            break
    return pos
}
|||

EFFICIENT_WAY_TO_MULTIPLY_WITH_7

def multiplyBySeven ( n ) :
    return ( ( n << 3 ) - n )
}
|||

NEXT_HIGHER_NUMBER_WITH_SAME_NUMBER_OF_SET_BITS

def snoob ( x ) :
    rightOne , nextHigherOneBit , rightOnesPattern , next = x
    if x > 0 :
        global rightOne
        global next_higher_one_bit
        global rightOnesPattern
        global rightOnesPattern
        rightOnesPattern >>= 2
        global next
    return next ( x )
}
|||

CHANGE_ARRAY_PERMUTATION_NUMBERS_1_N

def makePermutation ( a , n ) :
    count = { }
    for i in range ( n ) :
        if count.has_key ( a [ i ] ) :
            count [ a [ i ] ] = count [ a [ i ] ] + 1
        else :
            count [ a [ i ] ] = 1
    next_missing = 1
    for i in range ( n ) :
        if count.has_key ( a [ i ] ) and count [ a [ i ] ] != 1 or a [ i ] > n or a [ i ] < 1 :
            count [ a [ i ] ] = count [ a [ i ] ] - 1
            while count.has_key ( next_missing ) :
                global next_missing
            a [ i ] = next_missing
            count [ next_missing ] += 1
}
|||

MAXIMUM_AREA_QUADRILATERAL

def max_area ( a , b , c , d ) :
    semiperimeter = ( a + b + c + d ) / 2
    return math.sqrt ( ( semiperimeter - a ) ** 2 + ( semiperimeter - b ) ** 2 + ( semiperimeter - c ) ** 2 + ( semiperimeter - d ) ** 2 )
}
|||

REPLACE_OCCURRENCES_STRING_AB_C_WITHOUT_USING_EXTRA_SPACE_1

def translate ( s ) :
    "For translation of a string."
    if len ( str ) < 2 :
        return str
    i = 0
    j = 0
    while j < len ( str ) - 1 :
        if str [ j ] == 'A' and str [ j + 1 ] == 'B' :
            global j
            str [ i : i + 4 ] = 'C'
            continue
        str [ i : i + 4 ] = str [ j : j + 4 ]
    if j == len ( str ) - 1 :
        str [ i : i + 4 ] = str [ i : i + 4 ]
    str = str.translate ( _trans )
    str = str.translate ( _trans )
}
|||

FIND_POWER_POWER_MOD_PRIME

def Calculate ( A , B , C , M ) :
    res , ans = 0 , 0
    global res
    ans = power ( A , res , M )
    ans = 0
}
|||

CHECK_EXIST_TWO_ELEMENTS_ARRAY_WHOSE_SUM_EQUAL_SUM_REST_ARRAY

def check_pair ( arr , n ) :
    sum = 0
    for i in range ( n ) :
        global sum
    if sum % 2 != 0 :
        return False
    global sum
    s = set ( arr )
    for i in range ( n ) :
        val = sum ( arr - i for i in range ( n ) )
        if s.has_key ( val ) and val == int ( s [ val ] ) :
            print ( "Pair elements are %d and %d" % ( arr [ i ] , val ) )
            return True
        global s
    return False
}
|||

PROGRAM_FOR_SURFACE_AREA_OF_OCTAHEDRON

def surface_area_octahedron ( side ) :
    return ( 2 * ( math.sqrt ( 3 ) ) * ( side ** 2 ) )
}
|||

FIND_A_SPECIFIC_PAIR_IN_MATRIX

def findMaxValue ( N , mat ) :
    max_value = int ( mat [ 'max_value' ] )
    for a in range ( N - 1 ) :
        for b in range ( N - 1 ) :
            for d in range ( a + 1 , N ) :
                for e in range ( b + 1 , N ) :
                    if maxValue < ( mat [ d ] [ e ] - mat [ a ] [ b ] ) :
                        maxValue = mat [ d ] [ e ] - mat [ a ] [ b ]
    return maxValue
}
|||

MULTIPLY_TWO_NUMBERS_WITHOUT_USING_MULTIPLY_DIVISION_BITWISE_OPERATORS_AND_NO_LOOPS

def multiply ( x , y ) :
    if y == 0 :
        return 0
    if y > 0 :
        return ( x + multiply ( x , y - 1 ) )
    if y < 0 :
        return - multiply ( x , - y )
    return - 1
}
|||

FIND_TRIPLETS_ARRAY_WHOSE_SUM_EQUAL_ZERO_1

def find_triplets ( arr , n ) :
    found = False
    for i in range ( n - 1 ) :
        s = set ( )
        for j in range ( i + 1 , n ) :
            x = - ( arr [ i ] + arr [ j ] )
            if s.count ( x ) :
                print ( x , arr [ i ] , arr [ j ] )
                global found
            else :
                s.append ( arr [ j ] )
    if found == False :
        print ( " No Triplet Found" )
}
|||

FIND_MAXIMUM_VALUE_OF_SUM_IARRI_WITH_ONLY_ROTATIONS_ON_GIVEN_ARRAY_ALLOWED

def maxSum ( ) :
    arr_sum = 0
    currVal = 0
    for i in arr :
        global arrSum
        global currVal
    maxVal = currVal
    for j in range ( 1 , len ( arr ) ) :
        global currVal
        if currVal > maxVal :
            global maxVal
    return maxVal
}
|||

PROGRAM_FOR_SCALAR_MULTIPLICATION_OF_A_MATRIX

def scalar_product_mat ( mat , k ) :
    for i in range ( N ) :
        for j in range ( N ) :
            mat [ i , j ] = mat [ i , j ] * k
}
|||

PRINT_SQUARES_FIRST_N_NATURAL_NUMBERS_WITHOUT_USING_1

def print_squares ( n ) :
    square , odd = divmod ( n , 2 )
    for x in range ( n ) :
        print ( square , end = ' ' )
        global square
        global odd
}
|||

NTH_PENTAGONAL_NUMBER

def pentagonalNum ( n ) :
    return ( 3 * n * n - n ) / 2
}
|||

COUNT_ARRAYS_ADJACENT_ELEMENTS_ONE_DIVIDE_ANOTHER

def numof_array ( n , m ) :
    dp = np.zeros ( ( MAX , MAX ) )
    di = Vector ( MAX )
    mu = Vector ( MAX )
    for i in range ( MAX ) :
        for j in range ( MAX ) :
            dp [ i ] [ j ] = 0
    for i in range ( MAX ) :
        di [ i ] = Vector ( )
        mu [ i ] = Vector ( )
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
        ans += dp [ n ] [ i ] for i in range ( m ) if i != n ]
        di [ i ].clear ( )
        mu [ i ].clear ( )
    return ans
}
|||

0_1_KNAPSACK_PROBLEM_DP_10

def knapSack ( W , wt , val , n ) :
    if n == 0 or W == 0 :
        return 0
    if wt [ - 1 ] > W :
        return n - 1
    else :
        return max ( val [ n - 1 ] + knap_sack ( W - wt [ n - 1 ] , wt , val , n - 1 ) , knap_sack ( W , wt , val , n - 1 ) )
}
|||

FIND_TRIPLETS_ARRAY_WHOSE_SUM_EQUAL_ZERO

def find_triplets ( arr , n ) :
    found = True
    for i in range ( n - 2 ) :
        for j in range ( i + 1 , n - 1 ) :
            for k in range ( j + 1 , n ) :
                if arr [ i ] + arr [ j ] + arr [ k ] == 0 :
                    print ( arr [ i ] for i in range ( n ) )
                    print ( " ".join ( [ str ( i ) for i in arr ] ) )
                    print ( arr [ j ] )
                    print ( " ".join ( [ str ( i ) for i in arr ] ) )
                    print ( arr [ k ] )
                    print ( "\n".join ( [ str ( i ) for i in arr ] ) )
                    global found
    if found == False :
        print ( " not exist " )
}
|||

COUNT_NUMBER_WAYS_REACH_GIVEN_SCORE_GAME

def count ( n ) :
    table , i = divmod ( n , len ( table ) + 1 )
    del table [ : n ]
    global table
    for i in range ( 3 , n ) :
        table [ i ] += table [ i - 3 ]
    for i in range ( 5 , n ) :
        table [ i ] += table [ i - 5 ]
    for i in range ( 10 , n ) :
        table [ i ] += table [ i - 10 ]
    return table [ n ]
}
|||

MAXIMUM_SUM_ABSOLUTE_DIFFERENCE_ARRAY

def MaxSumDifference ( a , n ) :
    final_sequence = [ ]
    a.sort ( )
    for i in range ( n // 2 ) :
        global final_sequence
        global finalSequence
    MaximumSum = 0
    for i in range ( n - 1 ) :
        MaximumSum = MaximumSum + abs ( final_sequence [ i ] - final_sequence [ i + 1 ] )
    MaximumSum = MaximumSum + abs ( final_sequence [ n - 1 ] - final_sequence [ 0 ] )
    return MaximumSum
}
|||

PROGRAM_FIND_MID_POINT_LINE

def midpoint ( x1 , x2 , y1 , y2 ) :
    print ( ( x1 + x2 ) / 2 , ( y1 + y2 ) / 2 )
}
|||

ALTERNATIVE_SORTING

def alternate_sort ( arr , n ) :
    return sorted ( arr , key = operator.itemgetter ( n ) )
    i , j = 0 , n - 1
    while i < j :
        print ( arr [ j -- ] , end = ' ' )
        print ( arr [ i ] , end = ' ' )
    if n % 2 != 0 :
        print ( arr [ i ] for i in range ( n ) )
}
|||

NUMBER_SUBARRAYS_SUM_EXACTLY_EQUAL_K

def findSubarraySum ( arr , n , sum ) :
    prev_sum = { }
    res = 0
    currsum = 0
    for i in range ( n ) :
        currsum += arr [ i ]
        if currsum == sum :
            global res
        if prevSum.has_key ( currsum - sum ) :
            res += prevSum [ currsum - sum ]
        count = prev_sum [ currsum ]
        if count is None :
            prev_sum [ currsum ] = 1
        else :
            prev_sum [ currsum ] = count + 1
    return res
}
|||

FIND_THE_ELEMENT_THAT_APPEARS_ONCE_IN_A_SORTED_ARRAY

def search ( arr , low , high ) :
    if low > high :
        return
    if low == high :
        print ( "The required element is " + str ( arr [ low ] ) )
        return
    mid = ( low + high ) // 2
    if mid % 2 == 0 :
        if arr [ mid ] == arr [ mid + 1 ] :
            return arr [ mid + 2 : high ]
        a = 5
            return arr [ low : high ]
    if mid % 2 == 1 :
        if arr [ mid ] == arr [ mid - 1 ] :
            return arr [ mid + 1 : high ]
        a = 5
            return arr [ low : mid - 1 ]
}
|||

FORM_SMALLEST_NUMBER_USING_ONE_SWAP_OPERATION

def smallest_number ( str ) :
    num = args [ 0 ]
    n = len ( args )
    right_min = [ n for n in range ( n ) if n > 0 ]
    right_min [ n - 1 ] = - 1
    right = n - 1
    for i in range ( n - 2 , - 1 , - 1 ) :
        if num [ i ] > num [ right ] :
            rightMin [ i ] = right
        else :
            right_min [ i ] = - 1
            global right
    small = - 1
    for i in range ( 1 , n ) :
        if small == - 1 :
            if num [ i ] < num [ 0 ] :
                global small
        elif num [ i ] < num [ small ] :
            global small
    if small != - 1 :
        temp = 0
        global temp
        num [ 0 ] = num [ small ]
        num [ small ] = temp
    else :
        for i in range ( 1 , n ) :
            if right_min [ i ] != - 1 :
                temp = 0
                global temp
                num [ i ] = num [ right_min [ i ] ]
                num [ right_min [ i ] ] = temp
                break
    return ( [ num for num in str.split ( '.' ) if num ] )
}
|||

PROGRAM_AREA_SQUARE

def area_square ( side ) :
    area = side * side
    return area
}
|||

FIND_DAY_OF_THE_WEEK_FOR_A_GIVEN_DATE

def dayofweek ( d , m , y ) :
    t = [ 0 , 3 , 2 , 5 , 0 , 3 , 5 , 1 , 4 , 6 , 2 , 4 ]
    y -= ( m < 3 )
    return ( y + y / 4 - y / 100 + y / 400 + t [ m - 1 ] + d ) % 7
}
|||

CHECK_QUEUE_CAN_SORTED_ANOTHER_QUEUE_USING_STACK

def check_sorted ( n ) :
    st = [ ]
    expected = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
    fnt = 0
    while len ( q ) != 0 :
        global fnt
        q.get ( )
        if fnt == expected :
            expected += 1
        else :
            if len ( st ) == 0 :
                st.push ( fnt )
            elif len ( st ) != 0 and st.pop ( ) < fnt :
                return False
            else :
                st.push ( fnt )
        while len ( st ) != 0 and st.pop ( ) == expected :
            st.pop ( )
            expected += 1
    if expected - 1 == n and len ( st ) == 0 :
        return True
    return False
}
|||

SORT_ARRAY_CONTAIN_1_N_VALUES

def sortit ( arr , n ) :
    for i in range ( n ) :
        arr [ i ] = i + 1
}
|||

LCS_LONGEST_COMMON_SUBSEQUENCE_THREE_STRINGS_1

def lcsOf3 ( i , j , k ) :
    if i == - 1 or j == - 1 or k == - 1 :
        return 0
    if dp [ i ] [ j ] [ k ] != - 1 :
        return dp [ i ] [ j ] [ k ]
    if X [ i ] == Y [ j ] and Y [ j ] == Z [ k ] :
        return dp [ i ] [ j ] [ k ] = 1 + lcs_of_3 ( i - 1 , j - 1 , k - 1 )
    else :
        return dp [ i ] [ j ] [ k ] = max ( max ( lcs_of_3 ( i - 1 , j , k ) , lcs_of_3 ( i , j - 1 , k ) ) , lcs_of_3 ( i , j , k - 1 ) )
}
|||

LOWER_INSERTION_POINT

def LowerInsertionPoint ( arr , n , X ) :
    if X < arr [ 0 ] :
        return 0
    elif X > arr [ n - 1 ] :
        return n
    lowerPnt = 0
    i = 1
    while i < n and arr [ i ] < X :
        lowerPnt = i
        i = i * 2
    while lowerPnt < n and arr [ lowerPnt ] < X :
        lowerPnt += 1
    return lowerPnt
}
|||

CONSTRUCT_LEXICOGRAPHICALLY_SMALLEST_PALINDROME

def constructPalin ( str , len ) :
    i , j = 0 , len - 1
    for i in range ( j ) :
        if str [ i ] == str [ j ] and str [ i ] != '*' :
            continue
        elif str [ i ] == str [ j ] and str [ i ] == '*' :
            str [ i : i + len ] = 'a' * ( len - i )
            str [ j ] = 'a'
            continue
        elif str [ i ] == '*' :
            str [ i : j ] = str [ j : i + len ]
            continue
        elif str [ j ] == '*' :
            str [ j ] = str [ i ]
            continue
        print ( "Not Possible" )
        return ""
    return str [ : len ]
}
|||

SECTION_FORMULA_POINT_DIVIDES_LINE_GIVEN_RATIO

def section ( x1 , x2 , y1 , y2 , m , n ) :
    x = ( ( n * x1 ) + ( m * x2 ) ) / ( m + n )
    y = ( ( n * y1 ) + ( m * y2 ) ) / ( m + n )
    print ( "(%f, %f)" % ( x , y ) )
}
|||

SQUARE_ROOT_NUMBER_USING_LOG

def squared_root ( n ) :
    return math.pow ( 2 , 0.5 * ( math.log ( n ) / math.log ( 2 ) ) )
}
|||

MAXIMIZE_SUM_ARRII

def max_sum ( arr , n ) :
    return np.sum ( arr , axis = n )
    sum = 0
    for i in range ( n ) :
        global sum
    return sum
}
|||

STRING_K_DISTINCT_CHARACTERS_NO_CHARACTERS_ADJACENT

def findString ( n , k ) :
    res = ""
    for i in range ( k ) :
        global res
    count = 0
    for i in range ( n - k ) :
        global res
        count += 1
        if count == k :
            global count
    return res
}
|||

COUNT_WORDS_WHOSE_TH_LETTER_EITHER_1_TH_TH_I1_TH_LETTER_GIVEN_WORD

def count_words ( str , len ) :
    count = 1
    if len ( str ) == 1 :
        return count
    if str [ 0 ] == str [ 1 ] :
        count *= 1
    else :
        global count
    for j in range ( 1 , len ( str ) - 1 ) :
        if str [ j ] == str [ j - 1 ] and str [ j ] == str [ j + 1 ] :
            count *= 1
        elif str [ j ] == str [ j - 1 ] or str [ j ] == str [ j + 1 ] or str [ j - 1 ] == str [ j + 1 ] :
            global count
        else :
            global count
    if str [ - 1 ] == str [ - 2 ] :
        count *= 1
    else :
        global count
    return count
}
|||

NUMBER_JUMP_REQUIRED_GIVEN_LENGTH_REACH_POINT_FORM_D_0_ORIGIN_2D_PLANE

def minJumps ( a , b , d ) :
    temp = a
    a = min ( a , b )
    b = max ( temp for temp in b )
    if d >= b : a = 5
        return ( d + b - 1 ) // b
    if d == 0 :
        return 0
    if d == a :
        return 1
    return 2
}
|||

SUM_FACTORS_NUMBER_1

def sumof_factors ( n ) :
    res = 1
    for i in range ( 2 , math.sqrt ( n ) + 1 ) :
        curr_sum = 1
        curr_term = 1
        while n % i == 0 :
            n = n / i
            curr_term *= i
            global curr_sum
        global res
    if n > 2 :
        global res
    return res
}
|||

DELETE_CONSECUTIVE_WORDS_SEQUENCE

def removeConsecutiveSame ( v ) :
    n = len ( v )
    for i in range ( n - 1 ) :
        if v [ i ] == v [ i + 1 ] :
            v.pop ( i )
            v.pop ( i )
            if i > 0 :
                i -= 1
            global n
        else :
            global i
    return len ( v )
}
|||

COUNT_NUMBER_BINARY_STRINGS_WITHOUT_CONSECUTIVE_1S

def countStrings ( n ) :
    a = [ ]
    b = [ ]
    a [ 0 ] = b [ 0 ] = 1
    for i in range ( 1 , n ) :
        a [ i ] = a [ i - 1 ] + b [ i - 1 ]
        b [ i ] = a [ i - 1 ]
    return a [ n - 1 ] + b [ n - 1 ]
}
|||

FIND_THE_MISSING_NUMBER

def getMissingNo ( a , n ) :
    i , total = 0 , 0
    global total
    for i in range ( n ) :
        global total
    return total
}
|||

SQUARE_ROOT_OF_A_PERFECT_SQUARE

def squareRoot ( n ) :
    x = n
    y = 1
    e = 0.000001
    while x - y > e :
        global x
        global y
    return x
}
|||

SUBSET_SUM_PROBLEM_OSUM_SPACE

def isSubsetSum ( arr , n , sum ) :
    subset = np.zeros ( ( 2 , sum + 1 ) )
    for i in range ( 0 , n ) :
        for j in range ( 0 , sum ) :
            if j == 0 :
                subset [ i % 2 ] [ j ] = True
            elif i == 0 :
                subset [ i % 2 ] [ j ] = False
            elif arr [ i - 1 ] <= j :
                subset = [ i % 2 for i in range ( n ) ]
            else :
                subset = [ i % 2 for i in range ( n ) ]
    return subset [ n % 2 ] [ sum ]
}
|||

MULTIPLICATIVE_INVERSE_UNDER_MODULO_M

def mod_inverse ( a , m ) :
    a = a % m
    for x in range ( 1 , m ) :
        if ( a * x ) % m == 1 : a = 5
            return x
    return 1
}
|||

COMPUTE_AVERAGE_TWO_NUMBERS_WITHOUT_OVERFLOW

def compute_average ( a , b ) :
    return ( a + b ) / 2
}
|||

REPRESENT_GIVEN_SET_POINTS_BEST_POSSIBLE_STRAIGHT_LINE

def best_approximate ( x , y ) :
    n = len ( x )
    m , c , sum_x , sum_y , sum_xy , sum_x2 = x
    for i in range ( n ) :
        sum_x += x [ i ]
        sum_y += y [ i ]
        sum_xy += x [ i ] * y [ i ]
        global sum_x2
    global m
    global c
    print ( 'm = %d' % m )
    print ( 'c = ' , c )
}
|||

SPLIT_ARRAY_ADD_FIRST_PART_END

def split_arr ( arr , n , k ) :
    for i in range ( k ) :
        x = arr [ 0 : n ]
        for j in range ( n - 1 ) :
            arr [ j ] = arr [ j + 1 ]
        arr [ n - 1 ] = x
}
|||

MAXIMUM_POSSIBLE_DIFFERENCE_TWO_SUBSETS_ARRAY

def maxDiff ( arr , n ) :
    SubsetSum_1 , SubsetSum_2 = 0 , 0
    for i in range ( 0 , n - 1 ) :
        isSingleOccurance = True
        for j in range ( i + 1 , n - 1 ) :
            if arr [ i ] == arr [ j ] :
                global isSingleOccurance
                arr [ i , j ] = arr [ j , i ] = 0
                break
        if isSingleOccurance :
            if arr [ i ] > 0 :
                SubsetSum_1 += arr [ i ]
            else :
                SubsetSum_2 += arr [ i ]
    return abs ( SubsetSum_1 - SubsetSum_2 )
}
|||

LONGEST_SUBSEQUENCE_DIFFERENCE_ADJACENTS_ONE_SET_2

def longLenSub ( arr , n ) :
    um = { }
    long_len = 0
    for i in range ( n ) :
        arr.__length__ = n
        if um.has_key ( arr [ i ] - 1 ) and len ( um [ arr [ i ] - 1 ] ) < len ( um [ arr [ i ] ] ) :
            global len
        if um.has_key ( arr [ i ] + 1 ) and len ( um [ arr [ i ] + 1 ] ) < len ( um [ arr [ i ] ] ) :
            global len
        um [ arr [ i ] ] = len ( um [ arr [ i ] ] ) + n
        if longLen < um [ arr [ i ] ] :
            global long_len
    return longLen
}
|||

LONGEST_REPEATED_SUBSEQUENCE_1

def longest_repeated_subseq ( str ) :
    n = len ( str )
    dp = [ n for n in range ( n + 1 ) if str.startswith ( n + 1 ) ]
    for i in range ( 0 , n ) :
        for j in range ( 0 , n ) :
            dp [ i ] [ j ] = 0
    for i in range ( 1 , n ) :
        for j in range ( 1 , n ) :
            if str [ i - 1 ] == str [ j - 1 ] and i != j :
                dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ]
    else :
        dp [ i ] [ j ] = max ( dp [ i ] [ j - 1 ] for j in range ( len ( str ) ) )
    res = ''
    i , j = n , n
    while i > 0 and j > 0 :
        if dp [ i ] [ j ] == dp [ i - 1 ] [ j - 1 ] + 1 :
            global res
            i -= 1
            global j
        elif dp [ i ] [ j ] == dp [ i - 1 ] [ j ] :
            i -= 1
        else :
            global j
    reverse = kwargs.pop ( 'reverse' , True )
    for k in res.keys ( ) :
        reverse = reverse + res [ k ]
    return reverse
}
|||

FIND_INDEX_MAXIMUM_OCCURRING_ELEMENT_EQUAL_PROBABILITY

def find_random_index_of_max ( arr , n ) :
    mp = { }
    for i in range ( n ) :
        mp [ arr [ i ] ] = mp [ arr [ i ] ] + 1
    else :
        mp [ arr [ i ] for i in range ( n ) ] = 1
    max_element = int ( arr [ 0 ] )
    max_so_far = int ( arr [ n - 1 ] )
    for p , a in mp.items ( ) :
        if p.value > max_so_far :
            global max_so_far
            global max_element
    r = int ( ( random.randint ( 0 , max_so_far ) % max_so_far ) + 1 )
    for i , count in enumerate ( arr ) :
        if arr [ i ] == max_element :
            count += 1
        if count == r :
            print ( "Element with maximum frequency present " "at index %d" % i )
            break
}
|||

CHECK_NUMBER_IS_PERFECT_SQUARE_USING_ADDITIONSUBTRACTION

def is_perfect_square ( n ) :
    for sum , i in itertools.combinations ( range ( 0 , n , 2 ) , 2 ) :
        global sum
        if sum ( n ) == n :
            return True
    return False
}
|||

N_BONACCI_NUMBERS_1

def bonacci_series ( n , m ) :
    a = arange ( m )
    for i in range ( m ) :
        a = [ ]
    a = [ ]
    a = [ ]
    for i in range ( n + 1 , m ) :
        a = 2 * a [ i ] - a [ i - n - 1 ]
    for i in range ( m ) :
        print ( a [ i ] , end = ' ' )
}
|||

COUNT_INDEX_PAIRS_EQUAL_ELEMENTS_ARRAY_1

def count_pairs ( arr , n ) :
    hm = { }
    for i in range ( n ) :
        if hm.has_key ( arr [ i ] ) :
            hm [ arr ] = hm [ arr ] + 1
        else :
            hm [ arr [ i ] ] += 1
    ans = 0
    for it in hm.items ( ) :
        count = it.next ( )
        global ans
    ans = 0
}
|||

SORT_EVEN_PLACED_ELEMENTS_INCREASING_ODD_PLACED_DECREASING_ORDER

def bitonic_generator ( arr , n ) :
    even_arr = Vector ( )
    oddArr = Vector ( )
    for i in range ( n ) :
        if i % 2 != 1 :
            evenarr.append ( arr [ i ] )
        else :
            oddArr.append ( arr [ i ] )
    sorted ( evenarr )
    return sorted ( oddarr , key = lambda x : x [ 1 ] )
    i = 0
    for j in evenarr :
        arr [ i ] = evenArr [ j ]
    for j in oddArr :
        arr [ i ] = oddArr [ j ]
}
|||

DYNAMIC_PROGRAMMING_SET_9_BINOMIAL_COEFFICIENT

def binomial_coeff ( n , k ) :
    if k == 0 or k == n :
        return 1
    return binomial_coeff ( n - 1 , k - 1 ) + binomial_coeff ( n - 1 , k )
}
|||

WRITE_A_C_PROGRAM_TO_FIND_THE_PARITY_OF_AN_UNSIGNED_INTEGER

def getParity ( n ) :
    parity = False
    while n != 0 :
        global parity
        n = n & ( n - 1 )
    return parity
}
|||

CHECK_WHETHER_LARGE_NUMBER_DIVISIBLE_7

def isDivisible7 ( num ) :
    n = len ( num )
    if n == 0 and num [ 0 ] == '0' :
        return True
    if n % 3 == 1 :
        num = '00' + num
    if n % 3 == 2 :
        num = "0" + num
    global n
    gSum , p = 0 , 1
    for i in range ( n - 1 , - 1 , - 1 ) :
        group = 0
        group += num [ i -- ] - '0'
        group += ( num [ i -- ] - '0' ) * 10
        global group
        global gSum
        global p
    return ( gSum % 7 == 0 )
}
|||

PRODUCT_NODES_K_TH_LEVEL_TREE_REPRESENTED_STRING

def product_at_kth_level ( tree , k ) :
    level = - 1
    product = 1
    n = len ( tree )
    for i in range ( n ) :
        if tree [ i ] == '(' :
            global level
        elif tree [ i ] == ')' :
            level -= 1
        else :
            if level == k :
                product *= ( tree [ i ] - '0' )
    return product
}
|||

CHECK_WHETHER_GIVEN_NUMBER_EVEN_ODD

def is_even ( n ) :
    return ( n % 2 == 0 )
}
|||

COUNT_GROUPINGS_NUMBER_SUM_DIGITS_EVERY_SUB_GROUP_LESS_EQUALS_IMMEDIATE_RIGHT_SUB_GROUP

def countGroups ( position , previous_sum , length , num ) :
    if position == length :
        return 1
    res = 0
    sum = 0
    for i in range ( position , length ) :
        global sum
        if sum ( position ) >= previous_sum :
            global res
    return res
}
|||

FIND_THE_ELEMENT_THAT_ODD_NUMBER_OF_TIMES_IN_OLOG_N_TIME

def search ( arr , low , high ) :
    if low > high :
        return
    if low == high :
        print ( "The required element is " + str ( arr [ low ] ) + " " )
        return
    mid = ( low + high ) // 2
    if mid % 2 == 0 :
        if arr [ mid ] == arr [ mid + 1 ] :
            return arr [ mid + 2 : high ]
        a = 5
            return arr [ low : high ]
    a = 5
        if arr [ mid ] == arr [ mid - 1 ] :
            return arr [ mid + 1 : high ]
        a = 5
            return arr [ low : high ]
}
|||

DELETE_CONSECUTIVE_WORDS_SEQUENCE_1

def removeConsecutiveSame ( v ) :
    st = Stack ( )
    for i in v :
        if st.empty ( ) :
            st.push ( v [ i ] )
        else :
            str = st.pop ( )
            if str ( v [ i ] ) == str ( v [ i ] ) :
                st.pop ( )
            else :
                st.push ( v [ i ] )
    return len ( st )
}
|||

MINIMUM_NUMBER_OF_JUMPS_TO_REACH_END_OF_A_GIVEN_ARRAY_2

def minJumps ( arr , n ) :
    jumps = np.arange ( n )
    min = 0
    jumps [ n - 1 ] = 0
    for i in range ( n - 2 , - 1 , - 1 ) :
        if arr [ i ] == 0 :
            jumps [ i ] = int ( n )
        elif arr [ i ] >= n - i - 1 :
            jumps [ i ] = 1
        else :
            global min
            for j in range ( i + 1 , n and j <= arr [ i ] + i ) :
                if min > jumps [ j ] :
                    global min
            if min != int ( n ) :
                jumps [ i ] = min + 1
            else :
                jumps [ i ] = min
    return jumps [ 0 ]
}
|||

PROGRAM_FIND_GCD_FLOATING_POINT_NUMBERS

def gcd ( a , b ) :
    if a < b :
        return gcd ( b , a )
    if abs ( b ) < 0.001 : a = 5
        return a
    else :
        return ( gcd ( b , a - floor ( a / b ) * b ) )
}
|||

MAXIMUM_PROFIT_BY_BUYING_AND_SELLING_A_SHARE_AT_MOST_TWICE

def max_profit ( price , n ) :
    profit = np.zeros ( ( n , ) )
    for i in range ( n ) :
        profit [ i ] = 0
    max_price = price [ n - 1 ]
    for i in range ( n - 2 , - 1 , - 1 ) :
        if price [ i ] > max_price :
            global max_price
        profit [ i ] = max ( profit [ i + 1 ] for i in range ( n ) )
    min_price = price [ 0 ]
    for i in range ( 1 , n ) :
        if price [ i ] < min_price :
            global min_price
        profit [ i ] = max ( profit [ i - 1 ] for i in range ( n ) )
    result = profit [ n - 1 ]
    return result
}
|||

COUNT_SET_BITS_IN_AN_INTEGER_1

def count_set_bits ( n ) :
    if n == 0 :
        return 0
    else :
        return ( n & 1 ) + count_set_bits ( n >> 1 )
}
|||

REORDER_A_ARRAY_ACCORDING_TO_GIVEN_INDEXES

def reorder ( ) :
    temp = [ arr for arr in arr ]
    for i in arr :
        temp [ index [ i ] ] = arr [ i ]
    for i in arr :
        arr [ i ] = temp [ i ]
        index [ i ] = i
}
|||

CHECK_IF_A_GIVEN_ARRAY_CAN_REPRESENT_PREORDER_TRAVERSAL_OF_BINARY_SEARCH_TREE

def can_representBST ( pre , n ) :
    s = Stack ( )
    root = int ( pre [ 0 ] )
    for i in range ( n ) :
        if pre [ i ] < root :
            return False
        while not s.empty ( ) and s.peek ( ) < pre [ i ] :
            global root
            s.pop ( )
        s.push ( pre [ i ] )
    return True
}
|||

FIND_REPETITIVE_ELEMENT_1_N_1_3

def find_repeated ( arr , n ) :
    missing_element = 0
    for i in range ( n ) :
        element = arr [ abs ( arr [ i ] ) for i in range ( n ) ]
        if element < 0 :
            global missing_element
            break
        arr [ abs ( arr [ i ] ) for i in range ( n ) ] = - arr [ abs ( arr [ i ] ) for i in range ( n ) ]
    return abs ( missing_element )
}
|||

DYNAMIC_PROGRAMMING_SET_8_MATRIX_CHAIN_MULTIPLICATION_1

def MatrixChainOrder ( p , n ) :
    m = np.zeros ( ( n , n ) )
    i , j , k , L , q = p
    for i in range ( 1 , n ) :
        m [ i , i ] = 0
    for L in range ( 2 , n ) :
        for i in range ( 1 , n - L + 1 ) :
            global j
            if j == n :
                continue
            m [ i , j ] = int ( n )
            for k in range ( i , j - 1 ) :
                q = m [ i ] [ k ] + m [ k + 1 ] [ j ] + p [ i - 1 ] * p [ k ] * p [ j ]
                if q < m [ i ] [ j ] :
                    m [ i , j ] = q
    return m [ 1 ] [ n - 1 ]
}
|||

COUNT_NUMBER_ISLANDS_EVERY_ISLAND_SEPARATED_LINE

def countIslands ( mat , m , n ) :
    count = 0
    for i in range ( m ) :
        for j in range ( n ) :
            if mat [ i ] [ j ] == 'X' :
                if ( i == 0 or mat [ i - 1 ] [ j ] == 'O' ) :
                    count += 1
    return count
}
|||

MINIMIZE_MAXAI_BJ_CK_MINAI_BJ_CK_THREE_DIFFERENT_SORTED_ARRAYS

def solve ( A , B , C ) :
    i , j , k = A.shape
    i = A.shape [ 0 ] - 1
    global j
    global k
    min_diff , current_diff , max_term = C
    min_diff = abs ( max ( A [ i ] , max ( B [ j ] , C [ k ] ) ) - min ( A [ i ] , min ( B [ j ] , C [ k ] ) ) )
    while i != - 1 and j != - 1 and k != - 1 :
        global current_diff
        if current_diff < min_diff :
            global min_diff
        global max_term
        if A [ i ] == max_term :
            i -= 1
        elif B [ j ] == max_term :
            global j
        else :
            k -= 1
    return min_diff
}
|||

ROOTS_QUADRATIC_EQUATION

def findRoots ( a , b , c ) :
    if a == 0 :
        print ( "Invalid" )
        return
    d = b ** 2 - 4 * a ** 2
    sqrt_val = sqrt ( abs ( d ) )
    if d > 0 :
        print ( "Roots are real and different \n" )
        print ( ( float ( - b + sqrt_val ) / ( 2 * a ) + "\n" + ( float ( - b - sqrt_val ) / ( 2 * a ) ) ) )
    else :
        print ( "Roots are complex \n" )
        print ( - float ( b ) / ( 2 * a ) , " + i" , sqrt_val , "\n" , - float ( b ) / ( 2 * a ) , " - i" , sqrt_val )
}
|||

GIVEN_LEVEL_ORDER_TRAVERSAL_BINARY_TREE_CHECK_TREE_MIN_HEAP

def isMinHeap ( level ) :
    n = len ( level ) - 1
    for i in range ( ( n // 2 - 1 ) , - 1 , - 1 ) :
        if level [ i ] > level [ 2 * i + 1 ] :
            return False
        if 2 * i + 2 < n :
            if level [ i ] > level [ 2 * i + 2 ] :
                return False
    return True
}
|||

FIND_MINIMUM_ELEMENT_IN_A_SORTED_AND_ROTATED_ARRAY

def findMin ( arr , low , high ) :
    if high < low :
        return arr [ 0 ]
    if high == low :
        return arr [ low ]
    mid = low + ( high - low ) / 2
    if mid < high and arr [ mid + 1 ] < arr [ mid ] :
        return arr [ mid + 1 ]
    if mid > low and arr [ mid ] < arr [ mid - 1 ] :
        return arr [ mid ]
    if arr [ high ] > arr [ mid ] :
        return findMin ( arr , low , mid - 1 )
    return findMin ( arr , mid + 1 , high )
}
|||

SMALLEST_LENGTH_STRING_WITH_REPEATED_REPLACEMENT_OF_TWO_DISTINCT_ADJACENT

def stringReduction ( str ) :
    n = len ( str )
    count = [ 0 ] * 3
    for i in range ( n ) :
        count [ str [ i ] - 'a' ] += 1
    if count [ 0 ] == n or count [ 1 ] == n or count [ 2 ] == n :
        return n
    if ( count [ 0 ] % 2 ) == ( count [ 1 ] % 2 ) and ( count [ 1 ] % 2 ) == ( count [ 2 ] % 2 ) :
        return 2
    return 1
}
|||

CHECK_LARGE_NUMBER_DIVISIBLE_3_NOT

def check ( str ) :
    n = len ( str )
    digitSum = 0
    for i in range ( n ) :
        digitSum += ( str [ i ] - '0' )
    return ( digitSum % 3 == 0 )
}
|||

COMPUTE_N_UNDER_MODULO_P

def mod_fact ( n , p ) :
    if n >= p :
        return 0
    result = 1
    for i in range ( 1 , n + 1 ) :
        global result
    return result
}
|||

POSSIBILITY_OF_A_WORD_FROM_A_GIVEN_SET_OF_CHARACTERS

def isPresent ( s , q ) :
    freq = [ 0 ] * MAX_CHAR
    for i in range ( len ( s ) ) :
        freq [ s [ i ] ] += 1
    for i in q :
        freq [ q [ i ] ] -= 1
        if freq [ q [ i ] ] < 0 :
            return False
    return True
}
|||

NEXT_POWER_OF_2_1

def next_power_of_2 ( n ) :
    p = 1
    if n and ( n & ( n - 1 ) ) == 0 :
        return n
    while p < n :
        global p
    return p
}
|||

REORDER_A_ARRAY_ACCORDING_TO_GIVEN_INDEXES_1

def reorder ( ) :
    for i in arr :
        while index [ i ] != i :
            old_target_i = index [ index [ i ] ]
            oldTargetE = ord ( arr [ index [ i ] ] )
            arr [ index [ i ] ] = arr [ i ]
            index [ index [ i ] ] = index [ i ]
            index [ i ] = old_target_i
            arr [ i ] = old_target_e
}
|||

UNBOUNDED_KNAPSACK_REPETITION_ITEMS_ALLOWED

def _unboundedKnapsack ( W , n , val , wt ) :
    dp = np.empty ( ( W + 1 , ) , dtype = np.int32 )
    for i in range ( 0 , W ) :
        for j in range ( n ) :
            if wt [ j ] <= i :
                dp [ i ] = max ( dp [ i ] for i in range ( n ) ) + val [ j ]
    return dp [ W ]
}
|||

PROGRAM_CHECK_DIAGONAL_MATRIX_SCALAR_MATRIX

def isDiagonalMatrix ( mat ) :
    for i in range ( N ) :
        for j in range ( N ) :
            if ( i != j ) :
                return False
    return True
}
|||

MAXIMUM_REMOVAL_FROM_ARRAY_WHEN_REMOVAL_TIME_WAITING_TIME

def max_removal ( arr , n ) :
    count = 0
    cummulative_sum = 0
    del arr [ n ]
    for i in range ( n ) :
        if arr [ i ] >= cummulative_sum :
            global count
            global cummulative_sum
    return count
}
|||

PROGRAM_CENSOR_WORD_ASTERISKS_SENTENCE

def censor ( text , word ) :
    word_list = text.split ( word )
    result = ""
    stars = ""
    for i in range ( len ( word ) ) :
        stars += '*'
    index = 0
    for i in word_list :
        if i.lower ( ) == word.lower ( ) :
            word_list [ index ] = stars
        global index
    for i in word_list :
        result += i + ' '
    return result
}
|||

COUNT_STRINGS_WITH_CONSECUTIVE_1S

def count_strings ( n ) :
    a , b = [ ] , [ ]
    a [ 0 ] = b [ 0 ] = 1
    for i in range ( 1 , n ) :
        a [ i ] = a [ i - 1 ] + b [ i - 1 ]
        b [ i ] = a [ i - 1 ]
    return 2 ** n
}
|||

LENGTH_LONGEST_BALANCED_SUBSEQUENCE

def max_length ( s , n ) :
    dp = [ ]
    for i in range ( n - 1 ) :
        if s [ i ] == '(' and s [ i + 1 ] == ')' :
            dp [ i ] [ i + 1 ] = 2
    for l in range ( 2 , n ) :
        for i , j in enumerate ( l ) :
            if s [ i ] == '(' and s [ j ] == ')' :
                dp [ i ] [ j ] = 2 + dp [ i + 1 ] [ j - 1 ]
            for k in range ( i , j ) :
                dp [ i ] [ j ] = max ( dp [ i ] [ j ] , dp [ i ] [ k ] + dp [ k + 1 ] [ j ] )
    return dp [ 0 ] [ n - 1 ]
}
|||

FIND_THE_POINT_WHERE_MAXIMUM_INTERVALS_OVERLAP

def find_max_guests ( arrl , exit , n ) :
    arrl.sort ( )
    return sorted ( exit )
    guests_in , max_guests , time = arrl
    i , j = 1 , 0
    while i < n and j < n :
        if arrl [ i ] <= exit [ j ] :
            guests_in += 1
            if guests_in > max_guests :
                global max_guests
                time = arrl [ i ]
            i = 1
        a = 5
            guests_in -= 1
            j += 1
    print ( "Maximum Number of Guests = %d at time %s" % ( max_guests , time.ctime ( ) ) )
}
|||

EFFICIENT_WAY_CHECK_WHETHER_N_TH_FIBONACCI_NUMBER_MULTIPLE_10

def is_multiple_of_10 ( n ) :
    if n % 15 == 0 :
        return True
    return False
}
|||

MAXIMUM_SUM_PAIRS_SPECIFIC_DIFFERENCE

def max_sum_pair_with_difference_less_k ( arr , N , K ) :
    np.sort ( arr )
    dp = np.zeros ( ( N , K ) )
    dp = np.zeros ( ( N , K ) )
    for i in range ( 1 , N ) :
        dp [ i ] = dp [ i - 1 ]
        if arr [ i ] - arr [ i - 1 ] < K :
            if i >= 2 :
                dp [ i ] = max ( dp [ i ] for i in range ( N ) )
            else :
                dp [ i ] = max ( dp [ i ] for i in range ( N ) )
    return dp [ N - 1 ]
}
|||

FIND_K_PAIRS_SMALLEST_SUMS_TWO_ARRAYS

def k_smallest_pair ( arr1 , n1 , arr2 , n2 , k ) :
    if k > n1 * n2 : a = 5
        print ( "k pairs don't exist" )
        return
    index2 = [ 0 ] * n1
    while k > 0 :
        min_sum = sum ( arr1 )
        min_index = 0
        for i1 in range ( n1 ) :
            if index2 [ i1 ] < n2 and arr1 [ i1 ] + arr2 [ index2 [ i1 ] ] < min_sum :
                global min_index
                min_sum = arr1 [ i1 ] + arr2 [ index2 [ i1 ] ]
        print ( "(%d, %d) " % ( arr1 [ min_index ] , arr2 [ index2 [ min_index ] ] ) )
        index2 [ min_index ] += 1
        k -= 1
}
|||

FIRST_UPPERCASE_LETTER_IN_A_STRING_ITERATIVE_AND_RECURSIVE_1

def first ( str , i ) :
    if str [ i ] == '\0' :
        return 0
    if ord ( str [ i ] ) < 128 :
        return str [ i ]
    return str [ i + 1 ]
}
|||

FIND_PAIRS_B_ARRAY_B_K

def printPairs ( arr , n , k ) :
    is_pair_found = True
    for i in range ( n ) :
        for j in range ( n ) :
            if i != j and arr [ i ] % arr [ j ] == k :
                print ( "(%d, %d)" % ( arr [ i ] , arr [ j ] ) , end = ' ' )
                isPairFound = True
    return isPairFound
}
|||

FIND_ARRANGEMENT_QUEUE_GIVEN_TIME

def solve ( n , t , s ) :
    for i in range ( t ) :
        for j in range ( n - 1 ) :
        temp = s [ j ]
        s [ j ] = s [ j + 1 ]
        s [ j + 1 ] = temp
        global j
    print ( s )
}
|||

SHORTEST_POSSIBLE_COMBINATION_TWO_STRINGS

def print_superseq ( a , b ) :
    m , n = len ( a ) , len ( b )
    dp = [ m + 1 for m in range ( n + 1 ) ]
    for i in range ( 0 , m ) :
        for j in range ( 0 , n ) :
            if i == 0 :
                dp [ i ] [ j ] = j
            elif j == 0 :
                dp [ i ] [ j ] = i
            elif a [ i - 1 ] == b [ j - 1 ] :
                dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ]
            else :
                dp [ i ] [ j ] = 1 + min ( dp [ i - 1 ] [ j ] , dp [ i ] [ j - 1 ] )
    res = ""
    i , j = m , n
    while i > 0 and j > 0 :
        if a [ i - 1 ] == b [ j - 1 ] :
            global res
            i -= 1
            j -= 1
        elif dp [ i - 1 ] [ j ] < dp [ i ] [ j - 1 ] :
            global res
            i -= 1
        else :
            global res
            j -= 1
    while i > 0 :
        global res
        i -= 1
    while j > 0 :
        global res
        j -= 1
    print ( res )
}
|||

COUNT_ROTATIONS_DIVISIBLE_8

def countRotationsDivBy8 ( n ) :
    _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _
    pass
    if len ( n ) == 1 :
        one_digit = n [ 0 ] - '0'
        if one_digit % 8 == 0 :
            return 1
        return 0
    if len ( n ) == 2 :
        first = ( n [ 0 ] - '0' ) * 10 + ( n [ 1 ] - '0' )
        second = ( n [ 1 ] - '0' ) * 10 + ( n [ 0 ] - '0' )
        if first % 8 == 0 :
            global count
        if second % 8 == 0 :
            global count
        return count
    threedigit
    for i in range ( ( len ( n ) - 2 ) ) :
        threedigit = ( n [ i ] - '0' ) * 100 + ( n [ i + 1 ] - '0' ) * 10 + ( n [ i + 2 ] - '0' )
        if threedigit % 8 == 0 :
            global count
    global threedigit
    if threedigit % 8 == 0 :
        global count
    global threedigit
    if threedigit % 8 == 0 :
        global count
    return count
}
|||

LONGEST_COMMON_SUBSEQUENCE_WITH_AT_MOST_K_CHANGES_ALLOWED

def lcs ( dp , arr1 , n , arr2 , m , k ) :
    if k < 0 :
        return - 10000000
    if n < 0 or m < 0 : a = 5
        return 0
    ans = dp [ n ] [ m ] [ k ]
    if ans != - 1 :
        ans = 0
pass
ans = 0
pass
}
|||

CHECK_LINE_TOUCHES_INTERSECTS_CIRCLE

def checkCollision ( a , b , c , x , y , radius ) :
    dist = ( abs ( a * x + b * y + c ) ) / math.sqrt ( a * a + b * b )
    if radius == dist :
        print ( "Touch" )
    elif radius > dist :
        print ( "Intersect" )
    else :
        print ( "Outside" )
}
|||

FIND_THE_MAXIMUM_SUBARRAY_XOR_IN_A_GIVEN_ARRAY

def max_subarray_XOR ( arr , n ) :
    ans = int ( arr [ n ] )
    for i in range ( n ) :
        curr_xor = 0
        for j in range ( i , n ) :
            global curr_xor
            global ans
    ans = 0
}
|||

SHORTEST_PATH_EXACTLY_K_EDGES_DIRECTED_WEIGHTED_GRAPH

def shortestPath ( graph , u , v , k ) :
    if k == 0 and u == v :
        return 0
    if k == 1 and graph [ u ] [ v ] != INF :
        return graph [ u ] [ v ]
    if k <= 0 :
        return INF
    res = INF
    for i in range ( V ) :
        if graph [ u ] [ i ] != INF and u != i and v != i :
            rec_res = shortest_path ( graph , i , v , k - 1 )
            if rec_res != INF :
                res = min ( res , graph [ u ] [ i ] + rec_res for i , res in enumerate ( graph [ u ] [ i ] ) )
    return res
}
|||

FIND_SUBARRAY_WITH_GIVEN_SUM

def subArraySum ( arr , n , sum ) :
    curr_sum , i , j = sum
    for i in range ( n ) :
        curr_sum = arr [ i ]
        for j in range ( i + 1 , n ) :
            if curr_sum == sum :
                p = j - 1
                print ( "Sum found between indexes %d and %d" % ( i , p ) for i , p in enumerate ( arr ) )
                return 1
            if curr_sum > sum or j == n :
                break
            global curr_sum
    print ( "No subarray found" )
    return 0
}
|||

K_TH_PRIME_FACTOR_GIVEN_NUMBER

def k_prime_factor ( n , k ) :
    while n % 2 == 0 :
        k -= 1
        n = n / 2
        if k == 0 :
            return 2
    for i in range ( 3 , math.sqrt ( n ) , 2 ) :
        while n % i == 0 :
            if k == 1 :
                return i
            k -= 1
            n = n / i
    if n > 2 and k == 1 :
        return n
    return - 1
}
|||

FIND_ROTATION_COUNT_ROTATED_SORTED_ARRAY_1

def countRotations ( arr , low , high ) :
    if high < low :
        return 0
    if high == low :
        return low
    mid = low + ( high - low ) / 2
    if mid < high and arr [ mid + 1 ] < arr [ mid ] :
        return ( mid + 1 )
    if mid > low and arr [ mid ] < arr [ mid - 1 ] :
        return mid
    if arr [ high ] > arr [ mid ] :
        return len ( arr [ low : high ] )
    return len ( arr [ mid + 1 : ] )
}
|||

COMPUTE_AVERAGE_TWO_NUMBERS_WITHOUT_OVERFLOW_1

def compute_average ( a , b ) :
    return ( a / 2 ) + ( b / 2 ) + ( ( a % 2 + b % 2 ) / 2 )
}
|||

SORTING_USING_TRIVIAL_HASH_FUNCTION_1

def sort_using_hash ( a , n ) :
    max = sum ( a [ i ] for i in range ( n ) )
    min = abs ( sum ( a [ i ] for i in range ( n ) ) )
    hashpos = [ max ( a [ i ] for i in range ( 0 , n + 1 ) ) for i in range ( 0 , max ( a.size , n ) ) ]
    hashneg = [ min ( a , i ) for i in range ( min ( n , len ( a ) ) + 1 ) ]
    for i in range ( n ) :
        if a [ i ] >= 0 :
            hashpos [ a [ i ] ] += 1
        else :
            hashneg [ abs ( a [ i ] ) ] += 1
    for i in min ( n , len ( a ) ) :
        if hashneg [ i ] > 0 :
            for j in hashneg [ i ] :
                print ( ( - 1 ) * i for i in a )
    for i in range ( 0 , max ( a ) ) :
        if hashpos [ i ] > 0 :
            for j in range ( hashpos [ i ] ) :
                print ( i , end = ' ' )
}
|||

FIND_THE_TWO_REPEATING_ELEMENTS_IN_A_GIVEN_ARRAY_1

def printRepeating ( arr , size ) :
    count = [ 0 ] * size
    i = 0
    print ( "Repeated elements are : " )
    for i in range ( size ) :
        if count [ arr [ i ] ] == 1 :
            print ( arr [ i ] , end = ' ' )
        else :
            count [ arr [ i ] ] += 1
}
|||

COUNT_POSSIBLE_DECODINGS_GIVEN_DIGIT_SEQUENCE_1

def count_decoding_dp ( digits , n ) :
    count = [ 0 ] * n + [ 0 ] * n
    count [ 0 ] = 1
    count [ 1 ] = 1
    if digits [ 0 ] == '0' :
        return 0
    for i in range ( 2 , n + 1 ) :
        count [ i ] = 0
        if digits [ i - 1 ] > '0' :
            count [ i ] = count [ i - 1 ]
        if digits [ i - 2 ] == '1' or ( digits [ i - 2 ] == '2' and digits [ i - 1 ] < '7' ) :
            count [ i ] += count [ i - 2 ]
    return count [ n ]
}
|||

EULERS_FOUR_SQUARE_IDENTITY_1

def check_euler ( a , b ) :
    ab = a * b
    flag = False
    i = 0
    while i * i <= ab :
        j = i
        while i * i + j * j <= ab :
            k = j
            while i ** 2 + j ** 2 + k ** 2 <= ab :
                l = np.linalg.norm ( ab - ( i ** 2 + j ** 2 + k ** 2 ) )
                if math.floor ( l ) == math.ceil ( l ) and l >= k :
                    global flag
                    print ( "i = %d\n" % i )
                    print ( "j = %d\n" % j )
                    print ( "k = %d\n" % k )
                    print ( "l = %d\n" % ( l ) )
                    print ( "Product of %d and %d can be written as sum of squares" " of i, j, k, l \n" % ( a , b ) )
                    print ( "%s = %s*%s + %s*%s + %s*%s + %s*%s + %s*%s + %s*%s" % ( ab , i , j , j , k , ( l , l ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a , b ) , ( a
                k += 1
            j += 1
        i += 1
    if flag == False :
        print ( "Solution doesn't exist!" )
        return
}
|||

COUNT_NUMBER_INCREASING_SUBSEQUENCES_SIZE_K

def numOfIncSubseqOfSizeK ( arr , n , k ) :
    dp , sum = np.sum ( arr , axis = 0 )
    for i in range ( n ) :
        dp [ 0 ] [ i ] = 1
    for l in range ( 1 , k ) :
        for i in l ( n , k ) :
            dp [ l ] [ i ] = 0
            for j in range ( l - 1 , i ) :
                if arr [ j ] < arr [ i ] :
                    dp [ l ] [ i ] += dp [ l - 1 ] [ j ]
    for i in range ( k - 1 , n ) :
        sum += dp [ k - 1 ] [ i ]
    return sum ( arr )
}
|||

KNAPSACK_PROBLEM_1

def knapSack ( W , wt , val , n ) :
    i , w = w [ : n ] , w [ n : ]
    K = np.zeros ( ( n + 1 , W + 1 ) )
    for i in range ( 0 , n ) :
        for w in range ( 0 , W ) :
            if i == 0 or w == 0 :
                K [ i , w ] = 0
            elif wt [ i - 1 ] <= w : a = 5
                K [ i ] [ w ] = max ( val [ i - 1 ] + K [ i - 1 ] [ w - wt [ i - 1 ] ] for i in range ( n ) )
            else :
                K [ i ] [ w ] = K [ i - 1 ] [ w ]
    return K [ n ] [ W ]
}
|||

PROGRAM_TO_PRINT_DOUBLE_HEADED_ARROW_PATTERN

def draw_pattern ( N ) :
    n = N
    row = 1
    nst = 1
    nsp1 = n - 1
    nsp2 = - 1
    val1 = row
    val2 = 1
    while row <= n :
        csp1 = 1
        while csp1 <= nsp1 :
            print ( "  " * N )
            global csp1
        cst1 = 1
        while cst1 <= nst :
            print ( val1 , end = ' ' )
            global val1
            global cst1
        csp2 = 1
        while csp2 <= nsp2 :
            print ( "  " * N )
            global csp2
        if row != 1 and row != n :
            cst2 = 1
            while cst2 <= nst :
                print ( val2 , end = ' ' )
                global val2
                global cst2
        print ( )
        if row <= n // 2 :
            global nst
            global nsp1
            global nsp2
            global val1
            global val2
        else :
            global nst
            global nsp1
            global nsp2
            global val1
            global val2
        global row
}
|||

INTEGER_POSITIVE_VALUE_POSITIVE_NEGATIVE_VALUE_ARRAY

def find_integer ( arr , n ) :
    hash = { }
    maximum = 0
    for i in range ( n ) :
        if arr [ i ] < 0 :
            hash [ abs ( arr [ i ] ) ] = ( hash [ abs ( arr [ i ] ) ] if i in hash else 0 ) - 1
        else :
            hash [ abs ( arr [ i ] ) ] = ( hash [ abs ( arr [ i ] ) ] if i in hash else 0 ) + 1
    for i in range ( n ) :
        if hash ( arr [ i ] ) > 0 :
            return arr [ i ]
    return - 1
}
|||

SPACE_OPTIMIZED_SOLUTION_LCS

def lcs ( X , Y ) :
    m , n = len ( X ) , len ( Y )
    L = [ 0 ] * ( n + 1 )
    bi = 0
    for i in range ( 0 , m ) :
        global bi
        for j in range ( 0 , n ) :
            if i == 0 or j == 0 :
                L [ bi ] [ j ] = 0
            elif X [ i - 1 ] == Y [ j - 1 ] :
                L [ bi ] [ j ] = L [ 1 - bi ] [ j - 1 ] + 1
            else :
                L [ bi ] [ j ] = max ( L [ 1 - bi ] [ j ] , L [ bi ] [ j - 1 ] )
    return L [ bi ] [ n ]
}
|||

REPRESENT_NUMBER_SUM_MINIMUM_POSSIBLE_PSUEDOBINARY_NUMBERS

def psuedo_binary ( n ) :
    while n != 0 :
        temp , m , p = n , 0 , 1
        while temp != 0 :
            rem = temp % 10
            global temp
            if rem != 0 :
                global m
            p *= 10
        print ( m , end = ' ' )
        n = n - m
    print ( " " * n )
}
|||

FIND_NUMBER_CURRENCY_NOTES_SUM_UPTO_GIVEN_AMOUNT

def count_currency ( amount ) :
    notes = [ 2000 , 500 , 200 , 100 , 50 , 20 , 10 , 5 , 1 ]
    note_counter = [ 0 ] * 9
    for i in range ( 9 ) :
        if amount >= notes [ i ] :
            note_counter [ i ] = amount / notes [ i ]
            amount = amount - note_counter [ i ] * notes [ i ]
    print ( "Currency Count ->" )
    for i in range ( 9 ) :
        if note_counter [ i ] != 0 :
            print ( notes [ i ] + ' : ' + str ( note_counter [ i ] ) )
}
|||

POSITIVE_ELEMENTS_EVEN_NEGATIVE_ODD_POSITIONS

def rearrange ( a , size ) :
    positive , negative , temp = a
    while True :
        while positive < size and a [ positive ] >= 0 :
            positive += 2
        while negative ( size ) <= a [ negative ( size ) ] :
            negative += 2
        if positive < size < negative :
            global temp
            a [ positive ] , a [ negative ] = a [ positive ] , a [ negative ]
            a [ negative ] = temp
        else :
            break
}
|||

FIND_WHETHER_AN_ARRAY_IS_SUBSET_OF_ANOTHER_ARRAY_SET_1

def issubset ( arr1 , arr2 , m , n ) :
    i = 0
    j = 0
    for i in range ( n ) :
        for j in range ( m ) :
            if arr2 [ i ] == arr1 [ j ] :
                break
        if j == m :
            return False
    return True
}
|||

GIVEN_A_SORTED_AND_ROTATED_ARRAY_FIND_IF_THERE_IS_A_PAIR_WITH_A_GIVEN_SUM

def pairInSortedRotated ( arr , n , x ) :
    i = 0
    for i in range ( n - 1 ) :
        if arr [ i ] > arr [ i + 1 ] :
            break
    l = ( i + 1 ) % n
    r = i
    while l != r :
        if arr [ l ] + arr [ r ] == x :
            return True
        if arr [ l ] + arr [ r ] < x :
            l = ( l + 1 ) % n
        else :
            r = ( n + r - 1 ) % n
    return False
}
|||

PROGRAM_TO_FIND_REMAINDER_WITHOUT_USING_MODULO_OR_OPERATOR_1

def getRemainder ( num , divisor ) :
    if divisor == 0 :
        print ( "Error: divisor " + "can't be zero \n" )
        return - 1
    if divisor < 0 :
        divisor = - divisor
    if num < 0 :
        num = - num
    i = 1
    product = 0
    while product <= num :
        product = divisor * i
        i += 1
    return num - ( product - divisor )
}
|||

GNOME_SORT_A_STUPID_ONE

def gnome_sort ( arr , n ) :
    index = 0
    while index < n :
        if index == 0 :
            index += 1
        if arr [ index ] >= arr [ index - 1 ] :
            index += 1
        else :
            temp = 0
            global temp
            arr [ index ] = arr [ index - 1 ]
            arr [ index - 1 ] = temp
            index -= 1
    return
}
|||

NUMBER_WAYS_INSERT_CHARACTER_INCREASE_LCS_ONE

def numberofways ( A , B , N , M ) :
    pos = Vector ( MAX )
    for i in range ( MAX ) :
        pos [ i ] = Vector ( )
    for i in range ( M ) :
        pos [ B [ i ] ].append ( i + 1 )
    dpl = [ N + 2 , M + 2 ]
    for i in range ( 1 , N + 1 ) :
        for j in range ( 1 , M + 1 ) :
            if A [ i - 1 ] == B [ j - 1 ] :
                dpl [ i ] [ j ] = dpl [ i - 1 ] [ j - 1 ] + 1
            else :
                dpl [ i ] [ j ] = max ( dpl [ i - 1 ] [ j ] for j in range ( N - 1 ) )
    LCS = dpl [ N ] [ M ]
    dpr = [ N + 2 , M + 2 ]
    for i in range ( N , 1 , - 1 ) :
        for j in range ( M , 1 , - 1 ) :
            if A [ i - 1 ] == B [ j - 1 ] :
                dpr [ i ] [ j ] = dpr [ i + 1 ] [ j + 1 ] + 1
            else :
                dpr [ i ] [ j ] = max ( dpr [ i + 1 ] [ j ] for j in range ( N , M + 1 ) )
    ans = 0
    for i in range ( 0 , N ) :
        for j in range ( MAX ) :
            for x in pos [ j ] :
                if dpl [ i ] [ x - 1 ] + dpr [ i + 1 ] [ x + 1 ] == LCS : a = 5
                    ans += 1
                    break
    ans = 0
}
|||

MINIMUM_PRODUCT_K_INTEGERS_ARRAY_POSITIVE_INTEGERS

def min_product ( arr , n , k ) :
    pq = PriorityQueue ( )
    for i in range ( n ) :
        global pq
    count , ans = 0 , 1
    while pq ( arr ) == False and count < k :
        global ans
        global pq
        count += 1
    ans = 0
}
|||

FIND_UNIQUE_ELEMENTS_MATRIX

def unique ( mat , n , m ) :
    maximum , flag = 0 , 0
    for i in range ( n ) :
        for j in range ( m ) :
            if maximum < mat [ i ] [ j ] :
                maximum = mat [ i , j ]
    b = np.arange ( maximum + 1 )
    for i in range ( n ) :
        for j in range ( m ) :
            b [ mat [ i ] [ j ] ] += 1
    for i in range ( 1 , maximum ) :
        if b [ i ] == 1 :
            print ( i , end = ' ' )
    flag = 1
    if flag == 0 :
        print ( "No unique element " + "in the matrix" )
}
|||

LONGEST_SUBSEQUENCE_SUCH_THAT_DIFFERENCE_BETWEEN_ADJACENTS_IS_ONE

def longestSubseqWithDiffOne ( arr , n ) :
    dp = np.zeros ( ( n , ) )
    for i in range ( n ) :
        dp [ i ] = 1
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if ( arr [ i ] == arr [ j ] + 1 ) :
                dp [ i ] = max ( dp [ i ] , dp [ j ] + 1 )
    result = 1
    for i in range ( n ) :
        if result < dp [ i ] :
            result = dp [ i ]
    return result
}
|||

C_PROGRAM_CONCATENATE_STRING_GIVEN_NUMBER_TIMES

def repeat ( s , n ) :
    s1 = s
    for i in range ( 1 , n ) :
        s += s1
    return s
}
|||

SEARCHING_FOR_PATTERNS_SET_1_NAIVE_PATTERN_SEARCHING

def search ( txt , pat ) :
    M = len ( pat )
    N = len ( txt )
    for i in range ( 0 , N - M ) :
        j = 0
        for j in range ( M ) :
            if txt [ i + j ] != pat [ j ] :
                break
        if j == M :
            print ( "Pattern found at index " + str ( i ) )
}
|||

COUNT_POSSIBLE_PATHS_SOURCE_DESTINATION_EXACTLY_K_EDGES

def countwalks ( graph , u , v , k ) :
    if k == 0 and u == v :
        return 1
    if k == 1 and graph [ u ] [ v ] == 1 :
        return 1
    if k <= 0 :
        return 0
    count = 0
    for i in range ( V ) :
        if graph [ u ] [ i ] == 1 :
            count += countwalks ( graph , i , v , k - 1 )
    return count
}
|||

COUNT_DIVISIBLE_PAIRS_ARRAY

def count_divisibles ( arr , n ) :
    res = 0
    for i in range ( n ) :
        for i in range ( i + 1 , n ) :
            if arr [ i ] % arr [ j ] == 0 or arr [ j ] % arr [ i ] == 0 :
                global res
    return res
}
|||

PROGRAM_TO_CHECK_IF_A_MATRIX_IS_SYMMETRIC

def isSymmetric ( mat , N ) :
    for i in range ( N ) :
        for j in range ( N ) :
            if mat [ i ] [ j ] != mat [ j ] [ i ] :
                return False
    return True
}
|||

COUNT_PALINDROME_SUB_STRINGS_STRING

def CountPS ( str , n ) :
    dp = [ ]
    P = [ ]
    for i in range ( n ) :
        P [ i ] [ i ] = True
    for i in range ( n - 1 ) :
        if str [ i ] == str [ i + 1 ] :
            P [ i ] [ i + 1 ] = True
            dp [ i ] [ i + 1 ] = 1
    for gap in range ( 2 , n ) :
        for i in range ( n - gap ) :
            j = gap + i
            if str [ i ] == str [ j ] and P [ i + 1 ] [ j - 1 ] :
                P [ i ] [ j ] = True
            if P [ i ] [ j ] == True :
                dp [ i ] [ j ] = dp [ i ] [ j - 1 ] + dp [ i + 1 ] [ j ] + 1 - dp [ i + 1 ] [ j - 1 ]
            else :
                dp [ i ] [ j ] = dp [ i ] [ j - 1 ] + dp [ i + 1 ] [ j ] - dp [ i + 1 ] [ j - 1 ]
    return dp [ 0 ] [ n - 1 ]
}
|||

WAYS_SUM_N_USING_ARRAY_ELEMENTS_REPETITION_ALLOWED

def countWays ( N ) :
    count = [ 0 ] * N + [ 0 ] * N
    count [ 0 ] = 1
    for i in range ( 1 , N ) :
        for j in arr :
            if i >= arr [ j ] :
                count [ i ] += count [ i - arr [ j ] ]
    return count [ N ]
}
|||

MINIMUM_NUMBER_OF_OPERATIONS_TO_MOVE_ALL_UPPERCASE_CHARACTERS_BEFORE_ALL_LOWER_CASE_CHARACTERS

def min_operations ( str , n ) :
    i , last_upper , first_lower = - 1 , - 1
    for i in range ( n - 1 , - 1 , - 1 ) :
        if re.match ( '[a-z]+' , str ) :
            global last_upper
            break
    for i in range ( n ) :
        if ord ( str [ i ] ) < ord ( str [ i + 1 ] ) :
            global first_lower
            break
    if lastUpper == - 1 or firstLower == - 1 :
        return 0
    count_upper = 0
    for i in first_lower ( ) :
        if re.match ( '[a-z]+' , str ) :
            global countUpper
    count_lower = 0
    for i in range ( last_upper ) :
        if ord ( str [ i ] ) < ord ( str [ i + 1 ] ) :
            countLower += 1
    return min ( count_lower , count_upper )
}
|||

PRINT_A_GIVEN_MATRIX_IN_SPIRAL_FORM

def spiral_print ( m , n , a ) :
    i , k , l = a
    while k < m and l < n :
        for i in l ( m , n ) :
            print ( a [ k ] [ i ] , end = ' ' )
        k += 1
        for i in range ( k , m ) :
            print ( a [ i ] [ n - 1 ] + " " for i in range ( m ) )
        n -= 1
        if k < m :
            for i in range ( n - 1 , l + 1 ) :
                print ( a [ m - 1 ] [ i ] + " " for i in range ( m - 1 , n ) )
            m -= 1
        if l < n :
            for i in range ( m - 1 , k + 1 , - 1 ) :
                print ( a [ i ] [ l ] + " " for i in range ( m ) for l in range ( n ) )
            l += 1
}
|||

FIND_DISTINCT_INTEGERS_FOR_A_TRIPLET_WITH_GIVEN_PRODUCT

def find_triplets ( x ) :
    fact = Vector ( )
    factors = set ( [ int ( i ) for i in x.split ( ',' ) ] )
    for i in range ( 2 , math.sqrt ( x ) + 1 ) :
        if x % i == 0 :
            fact.append ( i )
            if x / i != i :
                fact.append ( x / i )
            factors.append ( i )
            factors.append ( x / i )
    found = False
    k = len ( fact )
    for i in range ( k ) :
        a = fact [ i ]
        for j in range ( k ) :
            b = fact [ j ]
            if ( a != b ) and ( x % ( a * b ) == 0 ) and ( x / ( a * b ) != a ) and ( x / ( a * b ) != b ) and ( x / ( a * b ) != 1 ) :
                print ( a , b , ( x / ( a * b ) ) )
                global found
                break
        if found :
            break
    if not found :
        print ( '-1' )
}
|||

SUM_TWO_LARGE_NUMBERS_1

def find_sum ( str1 , str2 ) :
    if len ( str1 ) > len ( str2 ) :
        t = str1
        str1 , str2 = str2 , str1
        str2 = t
    str = ""
    n1 , n2 = len ( str1 ) , len ( str2 )
    diff = n2 - n1
    carry = 0
    for i in range ( n1 - 1 , - 1 , - 1 ) :
        sum = ( ( int ( str1 [ i ] - '0' ) + int ( str2 [ i + diff ] - '0' ) + carry ) for i , diff in enumerate ( str1 ) )
        str += chr ( sum % 10 + '0' )
        global carry
    for i in range ( n2 - n1 - 1 , - 1 , - 1 ) :
        sum = ( ( int ( str2 [ i ] - '0' ) + carry ) for i in range ( len ( str2 ) ) )
        str += chr ( sum % 10 + '0' )
        global carry
    if carry > 0 :
        str += chr ( carry + '0' )
    return [ str ( i ) for i in range ( len ( str1 ) , len ( str2 ) ) ]
}
|||

COCKTAIL_SORT

def cocktail_sort ( a ) :
    swapped = True
    start = 0
    end = len ( a )
    while swapped == True :
        global swapped
        for i in range ( start , end - 1 ) :
            if a [ i ] > a [ i + 1 ] :
                temp = a [ i ]
                a [ i ] = a [ i + 1 ]
                a [ i + 1 ] = temp
                swapped = True
        if swapped == False :
            break
        global swapped
        global end
        for i in range ( end - 1 , start , - 1 ) :
            if a [ i ] > a [ i + 1 ] :
                temp = a [ i ]
                a [ i ] = a [ i + 1 ]
                a [ i + 1 ] = temp
                swapped = True
        start = start + 1
}
|||

COUNT_DERANGEMENTS_PERMUTATION_SUCH_THAT_NO_ELEMENT_APPEARS_IN_ITS_ORIGINAL_POSITION_1

def count_der ( n ) :
    der = [ 0 ] * ( n + 1 )
    der [ 0 ] = 1
    der [ 1 : ] = 0
    der [ 2 ] = 1
    for i in range ( 3 , n ) :
        der [ i ] = ( i - 1 ) * ( der [ i - 1 ] + der [ i - 2 ] )
    return der [ n ]
}
|||

MAXIMUM_PRODUCT_SUBARRAY_ADDED_NEGATIVE_PRODUCT_CASE

def find_max_product ( arr , n ) :
    pass
    ans = int ( arr [ n ] )
    maxval = 1
    minval = 1
    prev_max = 0
    for i in range ( n ) :
        if arr [ i ] > 0 :
            global maxval
            global minval
        elif arr [ i ] == 0 :
            minval = 1
            maxval = 0
        elif arr [ i ] < 0 : a = 5
            global prevMax
            maxval = minval * arr [ i ]
            minval = prevMax * arr [ i ]
        ans = max ( ans , maxval )
        if maxval <= 0 :
            maxval = 1
    ans = 0
}
|||

REARRANGE_ARRAY_SUCH_THAT_EVEN_POSITIONED_ARE_GREATER_THAN_ODD

def assign ( a , n ) :
    a.sort ( )
    ans = [ ]
    p , q = 0 , n - 1
    for i in range ( n ) :
        if ( i + 1 ) % 2 == 0 :
            ans [ i ] = a [ q -= 1 ]
        else :
            ans [ i ] = a [ p ]
    for i in range ( n ) :
        print ( ans [ i ] , end = ' ' )
}
|||

FRIENDS_PAIRING_PROBLEM

def count_friend_pairings ( n ) :
    dp = [ 0 ] * ( n + 1 )
    for i in range ( 0 , n ) :
        if i <= 2 :
            dp [ i ] = i
        else :
            dp [ i ] = dp [ i - 1 ] + ( i - 1 ) * dp [ i - 2 ]
    return dp [ n ]
}
|||

PRIME_NUMBERS

def isPrime ( n ) :
    if n <= 1 :
        return False
    for i in range ( 2 , n ) :
        if n % i == 0 :
            return False
    return True
}
|||

PROBABILITY_REACHING_POINT_2_3_STEPS_TIME

def find_prob ( N , P ) :
    dp = np.zeros ( ( N + 1 , ) )
    dp [ 0 ] = 1
    dp [ 1 ] = 0
    dp [ 2 ] = P
    dp [ 3 ] = 1 - P
    for i in range ( 4 , N + 1 ) :
        dp [ i ] = ( P ) * dp [ i - 2 ] + ( 1 - P ) * dp [ i - 3 ]
    return ( float ( dp [ N ] ) , float ( dp [ P ] ) )
}
|||

SMALLEST_OF_THREE_INTEGERS_WITHOUT_COMPARISON_OPERATORS_1

def smallest ( x , y , z ) :
    if ( y / x ) != 1 :
        return ( ( y / z ) != 1 )
    return ( ( x / z ) != 1 )
}
|||

COMMON_ELEMENTS_IN_ALL_ROWS_OF_A_GIVEN_MATRIX

def printCommonElements ( mat ) :
    mp = { }
    for j in range ( N ) :
        mp [ mat [ 0 ] [ j ] ] = 1
    for i in range ( 1 , M ) :
        for j in range ( N ) :
            if mp [ mat [ i ] [ j ] ] != None and mp [ mat [ i ] [ j ] ] == i :
                mp [ mat [ i ] [ j ] ] = i + 1
                if i == M - 1 :
                    print ( mat [ i , j ] , end = ' ' )
}
|||

DETECTING_NEGATIVE_CYCLE_USING_FLOYD_WARSHALL

def neg_cyclefloyd_warshall ( graph ) :
    dist , i , j , k = graph
    for i in range ( V ) :
        for j in range ( V ) :
            dist [ i ] [ j ] = graph [ i ] [ j ]
    for k in range ( V ) :
        for i in range ( V ) :
            for j in range ( V ) :
                if dist [ i ] [ k ] + dist [ k ] [ j ] < dist [ i ] [ j ] :
                    dist [ i ] [ j ] = dist [ i ] [ k ] + dist [ k ] [ j ]
    for i in range ( V ) :
        if dist [ i ] [ i ] < 0 :
            return True
    return False
}
|||

PROGRAM_SORT_STRING_DESCENDING_ORDER

def sortString ( str ) :
    charCount = [ 0 ] * MAX_CHAR
    for i in range ( len ( str ) ) :
        charCount [ str [ i ] - 'a' ] += 1
    for i in range ( MAX_CHAR - 1 , - 1 , - 1 ) :
        for j in range ( charCount [ i ] ) :
            print ( chr ( ord ( 'a' ) + i ) for i in range ( len ( str ) ) )
}
|||

COUNT_PAIRS_WITH_GIVEN_SUM

def get_paired_count ( arr , sum ) :
    count = 0
    for i in range ( len ( arr ) ) :
        for i in range ( i + 1 , len ( arr ) ) :
            if ( arr [ i ] + arr [ j ] ) == sum :
                global count
    print ( "Count of pairs is " , count )
}
|||

SUM_SERIES_12_32_52_2N_12_1

def sum_of_series ( n ) :
    return ( n * ( 2 * n - 1 ) * ( 2 * n + 1 ) ) / 3
}
|||

MAXIMUM_DIFFERENCE_BETWEEN_FREQUENCY_OF_TWO_ELEMENTS_SUCH_THAT_ELEMENT_HAVING_GREATER_FREQUENCY_IS_ALSO_GREATER

def maxdiff ( arr , n ) :
    freq = { }
    for i in range ( n ) :
        global freq
    ans = 0
    for i in range ( n ) :
        for j in range ( n ) :
            if freq [ arr [ i ] ] > freq [ arr [ j ] ] and arr [ i ] > arr [ j ] :
                ans = max ( ans , freq [ arr [ i ] ] - freq [ arr [ j ] ] )
            elif freq [ arr [ i ] ] < freq [ arr [ j ] ] and arr [ i ] < arr [ j ] :
                ans = max ( ans , freq [ arr [ j ] ] - freq [ arr [ i ] ] )
    ans = 0
}
|||

SHIFT_MATRIX_ELEMENTS_K

def shift_matrix_by_k ( mat , k ) :
    if k > N : a = 5
        print ( "Shifting is" , " not possible" )
        return
    j = 0
    while j < N :
        for i in range ( k , N ) :
            print ( mat [ j ] [ i ] , end = ' ' )
        for i in range ( k ) :
            print ( mat [ j ] [ i ] , end = ' ' )
        print ( )
        j += 1
}
|||

MAXIMUM_AND_MINIMUM_IN_A_SQUARE_MATRIX

def maxMin ( arr , n ) :
    min = + 2147483647
    max = - 2147483648
    for i in range ( n ) :
        for j in range ( 0 , n // 2 ) :
            if arr [ i ] [ j ] > arr [ i ] [ n - j - 1 ] :
                if min > arr [ i ] [ n - j - 1 ] :
                    min = arr [ i ] [ n - j - 1 ]
                if max < arr [ i ] [ j ] :
                    global max
            else :
                if min > arr [ i ] [ j ] :
                    global min
                if max < arr [ i ] [ n - j - 1 ] :
                    global max
    print ( "Maximum = %d, Minimum = %d" % ( max , min ) )
}
|||

FIND_PAIR_WITH_GREATEST_PRODUCT_IN_ARRAY_1

def findGreatest ( arr , n ) :
    m = { }
    for i in range ( n ) :
        if m.has_key ( arr [ i ] ) :
            m [ arr ] = m [ arr ] + 1
        else :
            m [ arr ] = m [ arr ]
    return sorted ( arr , key = lambda x : x [ n ] )
    for i in range ( n - 1 , 1 , - 1 ) :
        for j in range ( i , n ) :
            if arr [ i ] % arr [ j ] == 0 :
                result = arr [ i ] / arr [ j ]
                if result != arr [ j ] and m [ result ] == None or m [ result ] > 0 :
                    return arr [ i ]
                elif result == arr [ j ] and m [ result ] > 1 : a = 5
                    return arr [ i ]
    return - 1
}
|||

0_1_KNAPSACK_PROBLEM_DP_10_1

def knapSack ( W , wt , val , n ) :
    i , w = w [ : n ] , w [ n : ]
    K = np.zeros ( ( n + 1 , W + 1 ) )
    for i in range ( 0 , n ) :
        for w in range ( 0 , W ) :
            if i == 0 or w == 0 :
                K [ i , w ] = 0
            elif wt [ i - 1 ] <= w : a = 5
                K [ i ] [ w ] = max ( val [ i - 1 ] + K [ i - 1 ] [ w - wt [ i - 1 ] ] for i in range ( n ) )
            else :
                K [ i ] [ w ] = K [ i - 1 ] [ w ]
    return K [ n ] [ W ]
}
|||

PROGRAM_DECIMAL_OCTAL_CONVERSION

def dec_to_oct ( n ) :
    octal_num = [ 0 ] * 100
    i = 0
    while n != 0 :
        octal_num [ i ] = n % 8
        n = n / 8
        i += 1
    for j in range ( i - 1 , - 1 , - 1 ) :
        print ( octal_num [ j ] )
}
|||

SUBSEQUENCES_SIZE_THREE_ARRAY_WHOSE_SUM_DIVISIBLE_M_1

def count_subseq ( A , N , M ) :
    ans = 0
    h = [ 0 ] * M
    np.fill_diagonal ( h , 0 )
    for i in range ( N ) :
        A [ i ] = A [ i ] % M
        h [ A [ i ] for i in range ( N ) ] += 1
    for i in range ( M ) :
        for j in range ( i , M ) :
            rem = ( M - ( i + j ) % M ) % M
            if rem < j :
                continue
            if i == j and rem == j :
                ans += h [ i ] * ( h [ i ] - 1 ) * ( h [ i ] - 2 ) / 6
            elif i == j :
                ans += h [ i ] * ( h [ i ] - 1 ) * h [ rem ] / 2
            elif i == rem :
                ans += h [ i ] * ( h [ i ] - 1 ) * h [ j ] / 2
            elif rem == j :
                ans += h [ j ] * ( h [ j ] - 1 ) * h [ i ] / 2
            else :
                ans = ans + h [ i ] * h [ j ] * h [ rem ]
    ans = 0
}
|||

COUNT_FIBONACCI_NUMBERS_GIVEN_RANGE_LOG_TIME

def count_fibs ( low , high ) :
    f1 , f2 , f3 = 0 , 1 , 1
    result = 0
    while f1 <= high :
        if f1 >= low :
            global result
        f1 = f2
        f2 = f3
        global f3
    result = 0
}
|||

FIND_WHETHER_A_GIVEN_NUMBER_IS_A_POWER_OF_4_OR_NOT_1

def isPowerOfFour ( n ) :
    count = 0
    x = n & ( n - 1 )
    if n > 0 and x == 0 :
        while n > 1 :
            n >>= 1
            global count
        return ( count % 2 == 0 )
    return 0
}
|||

FIND_SUM_EVEN_FACTORS_NUMBER

def sumof_factors ( n ) :
    if n % 2 != 0 :
        return 0
    res = 1
    for i in range ( 2 , math.sqrt ( n ) + 1 ) :
        count , curr_sum = 0 , 1
        curr_term = 1
        while n % i == 0 :
            global count
            n = n / i
            if i == 2 and count == 1 :
                global curr_sum
            global curr_term
            global curr_sum
        global res
    if n >= 2 :
        global res
    return res
}
|||

FIND_SUM_NON_REPEATING_DISTINCT_ELEMENTS_ARRAY

def find_sum ( arr , n ) :
    sum = 0
    s = set ( )
    for i in range ( n ) :
        if not s.has_key ( arr [ i ] ) :
            global sum
            s.append ( arr [ i ] )
    return sum
}
|||

DYNAMIC_PROGRAMMING_SET_17_PALINDROME_PARTITIONING_1

def minPalPartion ( str ) :
    n = len ( str )
    C = [ 0 ] * n
    P = [ True for n in range ( n ) ]
    i , j , k , L = str.split ( ' ' )
    for i in range ( n ) :
        P [ i ] [ i ] = True
    for L in range ( 2 , n ) :
        for i in range ( n - L + 1 ) :
            global j
            if L == 2 :
                P [ i ] [ j ] = ( str [ i ] == str [ j ] )
            else :
                P [ i ] [ j ] = ( str [ i ] == str [ j ] ) and P [ i + 1 ] [ j - 1 ]
    for i in range ( n ) :
        if P [ 0 ] [ i ] == True :
            C [ i ] = 0
        else :
            C [ i ] = int ( str )
            for j in range ( i ) :
                if P [ j + 1 ] [ i ] == True and 1 + C [ j ] < C [ i ] :
                    C [ i ] = 1 + C [ j ]
    return C [ n - 1 ]
}
|||

MINIMUM_POSITIVE_POINTS_TO_REACH_DESTINATION

def min_initial_points ( points , R , C ) :
    dp = np.zeros ( ( R , C ) )
    m , n = R , C
    dp [ m - 1 ] [ n - 1 ] = points [ m - 1 ] [ n - 1 ] > 0
    for i in range ( m - 2 , - 1 , - 1 ) :
        dp [ i ] [ n - 1 ] = max ( dp [ i + 1 ] [ n - 1 ] - points [ i ] [ n - 1 ] for i in range ( len ( povoids ) ) )
    for j in range ( n - 2 , - 1 , - 1 ) :
        dp [ m - 1 ] [ j ] = max ( dp [ m - 1 ] [ j + 1 ] - points [ m - 1 ] [ j ] for j in range ( 1 , m + 1 ) )
    for i in range ( m - 2 , - 1 , - 1 ) :
        for j in range ( n - 2 , - 1 , - 1 ) :
            min_points_on_exit = min ( dp [ i + 1 ] [ j ] for j in range ( len ( povoids ) ) for i in range ( len ( povoids ) ) )
            dp [ i ] [ j ] = max ( min_points_on_exit - points [ i ] [ j ] for i , j in povoids )
    return dp [ 0 ] [ 0 ]
}
|||

COUNT_OF_PAIRS_SATISFYING_THE_GIVEN_CONDITION

def count_pair ( a , b ) :
    s = str ( b )
    pass
    for i in range ( len ( s ) ) :
        if s [ i ] != '9' : a = 5
            break
    result = 0
    if i == len ( s ) : a = 5
        global result
    else :
        global result
    return result
}
|||

SURVIVAL

def survival ( S , N , M ) :
    if ( ( N * 6 ) < ( M * 7 ) and S > 6 ) or M > N :
        print ( "No" )
    else :
        days = ( M * S ) / N
        if ( ( M * S ) % N ) != 0 :
            days += 1
        print ( "Yes " + days )
}
|||

INTERLEAVE_FIRST_HALF_QUEUE_SECOND_HALF

def interleave_queue ( q ) :
    if len ( q ) % 2 != 0 :
        print ( "Input even number of integers." )
    s = Stack ( )
    half_size = len ( q ) // 2
    for i in range ( half_size ) :
        global s
        q.put ( None )
    while not s.empty ( ) :
        q.put ( s.pop ( ) )
        s.pop ( )
    for i in range ( half_size ) :
        q.put ( q.get ( ) )
        q.put ( None )
    for i in range ( half_size ) :
        global s
        q.put ( None )
    while not s.empty ( ) :
        q.put ( s.pop ( ) )
        s.pop ( )
        q.put ( q.get ( ) )
        q.put ( None )
}
|||

INTEGER_POSITIVE_VALUE_POSITIVE_NEGATIVE_VALUE_ARRAY_1

def find_integer ( arr , n ) :
    neg , pos = 0 , 0
    sum = 0
    for i in range ( n ) :
        global sum
        if arr [ i ] < 0 :
            neg += 1
        else :
            global pos
    return ( sum / abs ( neg - pos ) )
}
|||

FIND_SUM_EVEN_INDEX_BINOMIAL_COEFFICIENTS

def evenSum ( n ) :
    C = [ ]
    i , j = n
    for i in range ( 0 , n ) :
        for j in range ( 0 , min ( i , n ) ) :
            if j == 0 or j == i :
                C [ i ] [ j ] = 1
            else :
                C [ i ] [ j ] = C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ]
    sum = 0
    for i in range ( 0 , n , 2 ) :
        global sum
    return sum
}
|||

DELANNOY_NUMBER

def dealnnoy ( n , m ) :
    if m == 0 or n == 0 :
        return 1
    return dealnnoy ( m - 1 , n ) + dealnnoy ( m - 1 , n - 1 ) + dealnnoy ( m , n - 1 )
}
|||

FIND_THE_LARGEST_SUBARRAY_WITH_0_SUM

def max_len ( arr , n ) :
    max_len = 0
    for i in range ( n ) :
        curr_sum = 0
        for j in range ( i , n ) :
            global curr_sum
            if curr_sum == 0 :
                global max_len
    return n
}
|||

NEXT_POWER_OF_2

def next_power_of_2 ( n ) :
    count = 0
    if n and ( n & ( n - 1 ) ) == 0 :
        return n
    while n != 0 :
        n >>= 1
        global count
    return 1 << count
}
|||

LONGEST_GEOMETRIC_PROGRESSION

def lenOfLongestGP ( set , n ) :
    if n < 2 : a = 5
        return n
    if n == 2 :
        return ( set [ 1 ] % set [ 0 ] == 0 )
    return sorted ( set )
    L = [ ]
    llgp = 1
    for i in range ( n ) :
        if set [ n - 1 ] % set [ i ] == 0 : a = 5
            L [ i ] [ n - 1 ] = 2
        else :
            L [ i ] [ n - 1 ] = 1
    for j in range ( n - 2 , - 1 , - 1 ) :
        i , j = j - 1 , j + 1
        while i >= 0 and k <= n - 1 :
            if set [ i ] * set [ k ] < set [ j ] * set [ j ] :
                yield k
            elif set [ i ] * set [ k ] > set [ j ] * set [ j ] :
                if set [ j ] % set [ i ] == 0 : a = 5
                    L [ i ] [ j ] = 2
                else :
                    L [ i ] [ j ] = 1
                del i
            else :
                L [ i ] [ j ] = L [ j ] [ k ] + 1
                if L [ i ] [ j ] > llgp :
                    llgp = L [ i ] [ j ]
                del i
                yield k
        while i >= 0 :
            if set [ j ] % set [ i ] == 0 : a = 5
                L [ i ] [ j ] = 2
            else :
                L [ i ] [ j ] = 1
            del i
    return llgp
}
|||

DYNAMIC_PROGRAMMING_SET_6_MIN_COST_PATH

def _min_cost ( cost , m , n ) :
    i , j = m , n
    tc = [ 0 ] * ( m + 1 )
    tc [ 0 ] = cost [ 0 ]
    for i in range ( 1 , m + 1 ) :
        tc [ i ] [ 0 ] = tc [ i - 1 ] [ 0 ] + cost [ i ] [ 0 ]
    for j in range ( 1 , n ) :
        tc [ 0 ] [ j ] = tc [ 0 ] [ j - 1 ] + cost [ 0 ] [ j ]
    for i in range ( 1 , m + 1 ) :
        for j in range ( 1 , n ) :
            tc [ i ] [ j ] = min ( tc [ i - 1 ] [ j - 1 ] for i , j in enumerate ( m ) ) + cost [ i ] [ j - 1 ]
    return tc [ m ] [ n ]
}
|||

PROGRAM_DISTANCE_TWO_POINTS_EARTH

def distance ( lat1 , lat2 , lon1 , lon2 ) :
    lon1 = math.radians ( lon1 )
    lon2 = math.radians ( lon2 )
    lat1 , lat2 , lon1 , lon2 = map ( radians , lat1 , lat2 , lon1 , lon2 )
    lat2 = math.radians ( lat2 )
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.pow ( math.sin ( dlat / 2 ) , 2 ) + math.cos ( lat1 ) * math.cos ( lat2 ) * math.pow ( math.sin ( dlon / 2 ) , 2 )
    c = 2 * math.asin ( math.sqrt ( a ) )
    r = 6371
    return ( c * r for c , r in zip ( lat1 , lat2 , lon1 , lon2 ) )
}
|||

BIN_PACKING_PROBLEM_MINIMIZE_NUMBER_OF_USED_BINS

def next_fit ( weight , n , c ) :
    res , bin_rem = 0 , c
    for i in range ( n ) :
        if weight [ i ] > bin_rem :
            global res
            bin_rem = c - weight [ i ]
        else :
            bin_rem -= weight [ i ]
    return res
}
|||

FIND_SUBARRAY_WITH_GIVEN_SUM_1

def subArraySum ( arr , n , sum ) :
    curr_sum , start , i = arr [ 0 : n ] , 0 , sum
    for i in range ( 1 , n ) :
        while curr_sum > sum and start < i - 1 :
            global curr_sum
            start += 1
        if curr_sum == sum :
            p = i - 1
            print ( "Sum found between indexes %d and %d" % ( start , p ) )
            return 1
        if i < n :
            curr_sum = curr_sum + arr [ i ]
    print ( "No subarray found" )
    return 0
}
|||

SPACE_OPTIMIZED_DP_SOLUTION_0_1_KNAPSACK_PROBLEM_1

def KnapSack ( val , wt , n , W ) :
    dp = np.zeros ( ( W + 1 , ) )
    np.random.seed ( 0 )
    for i in range ( n ) :
        for j in range ( W , j >= wt [ i ] ) :
            dp [ j ] = max ( dp [ j ] , val [ i ] + dp [ j - wt [ i ] ] )
    return dp [ W ]
}
|||

FIND_VALUE_OF_Y_MOD_2_RAISED_TO_POWER_X

def yMod ( y , x ) :
    if ( math.log ( y ) / math.log ( 2 ) ) < x :
        return y
    if x > 63 :
        return y
    return ( y % ( 1 << int ( x ) ) )
}
|||

SUM_SERIES_23_45_67_89_UPTO_N_TERMS

def series_sum ( n ) :
    i = 1
    res = 0.0
    sign = True
    while n :
        n -= 1
        if sign :
            global sign
            global res
        else :
            global sign
            global res
    return res
}
|||

LENGTH_LONGEST_STRICT_BITONIC_SUBSEQUENCE

def long_len_strict_bitonic_sub ( arr , n ) :
    inc = { }
    dcr = { }
    len_inc = [ 0 ] * n
    len_dcr = [ 0 ] * n
    long_len = 0
    for i in range ( n ) :
        arr = arr [ : n ]
        if inc.has_key ( arr [ i ] - 1 ) :
            global len
        len_inc [ i ] = len ( arr ) + 1
        inc [ arr ] = len_inc [ i ]
    for i in range ( n - 1 , - 1 , - 1 ) :
        arr = arr [ : n ]
        if dcr.has_key ( arr [ i ] - 1 ) :
            global len
        len_dcr [ i ] = len ( arr [ i ] ) + 1
        dcr [ arr [ i ] ] = len_dcr [ i ]
    for i in range ( n ) :
        if long_len < ( len_inc [ i ] + len_dcr [ i ] - 1 ) :
            long_len = len_inc [ i ] + len_dcr [ i ] - 1
    return longLen
}
|||

MAXIMUM_DISTANCE_TWO_OCCURRENCES_ELEMENT_ARRAY

def max_distance ( arr , n ) :
    d = { }
    max_dist = 0
    for i in range ( n ) :
        if not map ( lambda i : arr [ i ] , range ( n ) ) :
            map ( lambda i : i , arr )
        else :
            global max_dist
    return max_dist
}
|||

FIND_RECTANGLE_BINARY_MATRIX_CORNERS_1_1

def isRectangle ( matrix ) :
    rows , cols = matrix.shape
    if rows == 0 :
        return False
    columns = matrix [ 0 ].shape [ 0 ]
    table = { }
    for i in range ( rows ) :
        for j in range ( columns - 1 ) :
            for k in range ( j + 1 , columns ) :
                if matrix [ i ] [ j ] == 1 and matrix [ i ] [ k ] == 1 :
                    if table.has_key ( j ) and table [ j ] in matrix :
                        return True
                    if table.has_key ( k ) and table [ k ].has_key ( j ) :
                        return True
                    if not table.has_key ( j ) :
                        x = set ( matrix )
                        x.append ( k )
                        table [ j ] = x
                    else :
                        table [ j ].append ( k )
                    if not table.has_key ( k ) :
                        x = set ( matrix )
                        x.append ( j )
                        table [ k ] = x
                    else :
                        table [ k ].append ( j )
    return False
}
|||

COUNT_MINIMUM_NUMBER_SUBSETS_SUBSEQUENCES_CONSECUTIVE_NUMBERS

def numofsubset ( arr , n ) :
    np.random.seed ( 1234 )
    count = 1
    for i in range ( n - 1 ) :
        if arr [ i ] + 1 != arr [ i + 1 ] :
            global count
    return count
}
|||

LARGEST_SUM_CONTIGUOUS_SUBARRAY

def max_subarray_sum ( a ) :
    size = len ( a )
    max_so_far , max_ending_here = int ( a [ 0 ] ) , 0
    for i in range ( size ) :
        global max_ending_here
        if max_so_far < max_ending_here :
            global max_so_far
        if max_ending_here < 0 :
            global max_ending_here
    return max_so_far
}
|||

PROGRAM_TO_FIND_REMAINDER_WITHOUT_USING_MODULO_OR_OPERATOR_2

def getRemainder ( num , divisor ) :
    while num >= divisor :
        num -= divisor
    return num
}
|||

CHECK_LARGE_NUMBER_DIVISIBLE_4_NOT

def check ( str ) :
    n = len ( str )
    if n == 0 :
        return False
    if n == 1 :
        return ( ( str [ 0 ] - '0' ) % 4 == 0 )
    last = str [ n - 1 ] - '0'
    second_last = str [ n - 2 ] - '0'
    return ( ( second_last * 10 + last ) % 4 == 0 )
}
|||

FIND_THE_ELEMENT_THAT_APPEARS_ONCE_1

def getSingle ( arr , n ) :
    result = 0
    x , sum = arr
    for i in range ( INT_SIZE ) :
        global sum
        global x
        for j in range ( n ) :
            if ( arr [ j ] & x ) == 0 :
                sum += 1
        if ( sum % 3 ) == 0 :
            global result
    return result
}
|||

NUMBER_RECTANGLES_NM_GRID

def rectCount ( n , m ) :
    return ( m * n * ( n + 1 ) * ( m + 1 ) ) / 4
}
|||

MAXIMUM_POINTS_INTERSECTION_N_CIRCLES

def intersection ( n ) :
    return n * ( n - 1 )
}
|||

ADD_1_TO_A_GIVEN_NUMBER

def f_gold ( x ) :
    m = 1
    while int ( x & m ) >= 1 :
        x = x ^ m
        global m
    x = x ^ m
    return x
}
|||

ADD_TWO_NUMBERS_WITHOUT_USING_ARITHMETIC_OPERATORS

def f_gold ( x , y ) :
    while y != 0 :
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x
}
|||

AREA_OF_THE_CIRCLE_THAT_HAS_A_SQUARE_AND_A_CIRCLE_INSCRIBED_IN_IT

def f_gold ( a ) :
    area = float ( math.pi * a ** 2 ) / 4
    return area
}
|||

ARRAY_RANGE_QUERIES_ELEMENTS_FREQUENCY_VALUE

def f_gold ( start , end , arr ) :
    mp = { }
    for i in range ( start , end + 1 ) :
        mp [ arr [ i ] ] = mp [ arr [ i ] ] if arr [ i ] else 1
    count = 0
    for key , val in mp.items ( ) :
        if entry.key == entry.value :
            global count
    return count
}
|||

BELL_NUMBERS_NUMBER_OF_WAYS_TO_PARTITION_A_SET

def f_gold ( n ) :
    bell = np.zeros ( ( n + 1 , n + 1 ) )
    bell [ 0 ] [ 0 ] = 1
    for i in range ( 1 , n ) :
        bell [ i ] [ 0 ] = bell [ i - 1 ] [ i - 1 ]
        for j in range ( 1 , i + 1 ) :
            bell [ i ] [ j ] = bell [ i - 1 ] [ j - 1 ] + bell [ i ] [ j - 1 ]
    return bell [ n ] [ 0 ]
}
|||

BINARY_SEARCH

def f_gold ( arr , l , r , x ) :
    if r >= l :
        mid = l + ( r - l ) / 2
        if arr [ mid ] == x :
            return mid
        if arr [ mid ] > x :
            return f_gold ( arr , l , mid - 1 , x )
        return f_gold ( arr , mid + 1 , r , x )
    return - 1
}
|||

BREAK_NUMBER_THREE_PARTS_1

def f_gold ( n ) :
    count = 0
    global count
    return count
}
|||

CALCULATE_ANGLE_HOUR_HAND_MINUTE_HAND

def f_gold ( h , m ) :
    if h < 0 or m < 0 or h > 12 or m > 60 :
        print ( "Wrong input" )
    if h == 12 :
        h = 0
    if m == 60 :
        m = 0
    hour_angle = int ( 0.5 * ( h * 60 + m ) )
    minute_angle = int ( 6 * m )
    angle = abs ( hour_angle - minute_angle )
    angle = min ( 360 - angle , angle )
    return angle
}
|||

CALCULATE_MAXIMUM_VALUE_USING_SIGN_TWO_NUMBERS_STRING

def f_gold ( str ) :
    res = str [ 0 ] - '0'
    for i in range ( 1 , len ( str ) ) :
        if str [ i ] == '0' or str [ i ] == '1' or res < 2 :
            global res
        else :
            res *= ( str [ i ] - '0' )
    return res
}
|||

CALCULATE_VOLUME_DODECAHEDRON

def f_gold ( side ) :
    return ( ( ( 15 + ( 7 * ( math.sqrt ( 5 ) ) ) ) / 4 ) * ( math.pow ( side , 3 ) ) )
}
|||

CEILING_IN_A_SORTED_ARRAY

def f_gold ( arr , low , high , x ) :
    pass
    if x <= arr [ low ] :
        return low
    for i in range ( low , high ) :
        if arr [ i ] == x :
            return i
        if arr [ i ] < x and arr [ i + 1 ] >= x :
            return i + 1
    return - 1
}
|||

CEILING_IN_A_SORTED_ARRAY_1

def f_gold ( arr , low , high , x ) :
    mid = 0
    if x <= arr [ low ] :
        return low
    if x > arr [ high ] :
        return - 1
    mid = ( low + high ) / 2
    if arr [ mid ] == x :
        return mid
    elif arr [ mid ] < x : a = 5
        if mid + 1 <= high and x <= arr [ mid + 1 ] :
            mid = low + 1
        else :
            return f_gold ( arr , mid + 1 , high , x )
    else :
        if mid - 1 >= low and x > arr [ mid - 1 ] :
            return mid
        else :
            return f_gold ( arr , low , mid - 1 , x )
}
|||

CENTER_ELEMENT_OF_MATRIX_EQUALS_SUMS_OF_HALF_DIAGONALS

def f_gold ( mat , n ) :
    diag1_left , diag1_right = np.where ( mat == 1 )
    diag2_left , diag2_right = np.where ( mat == 1 )
    for i , j in enumerate ( range ( n - 1 , - 1 , - 1 ) ) :
        if i < n // 2 :
            diag1_left += mat [ i , i ]
            diag2_left += mat [ j ] [ i ]
        elif i > n / 2 :
            diag1_right += mat [ i , i ]
            diag2_right += mat [ j ] [ i ]
    return ( diag1_left , diag2_right , diag2_left , diag1_right , diag2_left , diag2_right , mat [ n // 2 ] [ n // 2 ] )
}
|||

CHANGE_BITS_CAN_MADE_ONE_FLIP

def f_gold ( str ) :
    zeros , ones = 0 , 0
    for i in range ( len ( str ) ) :
        ch = str [ i ]
        if ch == '0' :
            zeros += 1
        else :
            global ones
    return ( zeros == 1 or ones == 1 )
}
|||

CHECK_ARRAY_CONTAINS_CONTIGUOUS_INTEGERS_DUPLICATES_ALLOWED

def f_gold ( arr , n ) :
    max = int ( arr [ 0 ] )
    min = int ( arr [ 0 ] )
    for i in range ( n ) :
        global max
        min = min ( arr )
    m = max - min + 1
    if m > n :
        return False
    visited = np.zeros ( ( n , n ) )
    for i in range ( n ) :
        visited [ arr [ i ] - min ] = True
    for i in range ( m ) :
        if visited [ i ] == False :
            return False
    return True
}
|||

CHECK_IF_ALL_THE_ELEMENTS_CAN_BE_MADE_OF_SAME_PARITY_BY_INVERTING_ADJACENT_ELEMENTS

def f_gold ( a , n ) :
    count_odd , count_even = 0 , 0
    for i in range ( n ) :
        if ( a [ i ] & 1 ) == 1 :
            count_odd += 1
        else :
            count_even += 1
    if count_odd % 2 == 1 and count_even % 2 == 1 :
        return False
    else :
        return True
}
|||

CHECK_IF_A_NUMBER_IS_JUMBLED_OR_NOT

def f_gold ( num ) :
    if num / 10 == 0 :
        return True
    while num != 0 :
        if num / 10 == 0 :
            return True
        digit1 = num % 10
        digit2 = ( num // 10 ) % 10
        if abs ( digit2 - digit1 ) > 1 :
            return False
        num = num / 10
    return True
}
|||

CHECK_IF_X_CAN_GIVE_CHANGE_TO_EVERY_PERSON_IN_THE_QUEUE

def f_gold ( notes , n ) :
    five_count = 0
    ten_count = 0
    for i in range ( n ) :
        if notes [ i ] == 5 :
            five_count += 1
        elif notes [ i ] == 10 :
            if five_count > 0 :
                five_count -= 1
                ten_count += 1
            else :
                return 0
        else :
            if five_count > 0 and ten_count > 0 :
                five_count -= 1
                tenCount -= 1
            elif five_count >= 3 :
                five_count -= 3
            else :
                return 0
    return 1
}
|||

CHECK_INTEGER_OVERFLOW_MULTIPLICATION

def f_gold ( a , b ) :
    if a == 0 or b == 0 :
        return False
    result = a * b
    if a == result / b :
        return False
    else :
        return True
}
|||

CHECK_LINE_PASSES_ORIGIN

def f_gold ( x1 , y1 , x2 , y2 ) :
    return ( x1 * ( y2 - y1 ) == y1 * ( x2 - x1 ) )
}
|||

CHECK_POSSIBLE_SORT_ARRAY_CONDITIONAL_SWAPPING_ADJACENT_ALLOWED

def f_gold ( arr , n ) :
    for i in range ( n - 1 ) :
        if arr [ i ] > arr [ i + 1 ] :
            if arr [ i ] - arr [ i + 1 ] == 1 :
                temp = arr [ i ]
                arr [ i ] = arr [ i + 1 ]
                arr [ i + 1 ] = temp
            else :
                return False
    return True
}
|||

CHECK_POSSIBLE_TRANSFORM_ONE_STRING_ANOTHER

def f_gold ( s1 , s2 ) :
    n = len ( s1 )
    m = len ( s2 )
    dp = [ False for n in range ( n + 1 ) ]
    for i in range ( 0 , n ) :
        for j in range ( 0 , m ) :
            dp [ i ] [ j ] = False
    dp [ 0 ] [ 0 ] = True
    for i in s1 :
        for j in range ( 0 , len ( s2 ) ) :
            if dp [ i ] [ j ] :
                if j < len ( s2 ) and ( ord ( s1 [ i ] ) == ord ( s2 [ j ] ) ) :
                    dp [ i + 1 ] [ j + 1 ] = True
                if not re.match ( '[a-z]' , s1 [ i ] ) :
                    dp [ i + 1 ] [ j ] = True
    return ( dp [ n ] [ m ] )
}
|||

CHECK_REVERSING_SUB_ARRAY_MAKE_ARRAY_SORTED

def f_gold ( arr , n ) :
    temp = np.zeros ( n )
    for i in range ( n ) :
        temp [ i ] = arr [ i ]
    temp = np.argsort ( arr )
    front = 0
    for front in range ( n ) :
        if temp [ front ] != arr [ front ] :
            break
    back = 0
    for back in range ( n - 1 , - 1 , - 1 ) :
        if temp [ back ] != arr [ back ] :
            break
    if front >= back :
        return True
pass
while front != back :
    pass
return True
pass
}
|||

CHECK_REVERSING_SUB_ARRAY_MAKE_ARRAY_SORTED_1

def f_gold ( arr , n ) :
    if n == 1 :
        return True
    i = 0
    for i in range ( 1 , arr [ i - 1 ] < arr [ i ] and i < n ) :
        pass
    if i == n :
        return True
    j = i += 1
    while arr [ j ] < arr [ j - 1 ] :
        if i > 1 and arr [ j ] < arr [ i - 2 ] :
            return False
        j += 1
    if j == n :
        return True
    k = j
    if arr [ k ] < arr [ i - 1 ] :
        return False
    while k > 1 and k < n :
        if arr [ k ] < arr [ k - 1 ] :
            return False
        k += 1
    return True
}
|||

CHECK_VALID_SEQUENCE_DIVISIBLE_M_1

def f_gold ( n , index , modulo , M , arr , dp ) :
    modulo = ( ( modulo % M ) + M ) % M
    if index == n :
        if modulo == 0 :
            return 1
        return 0
    if dp [ index ] [ modulo ] != - 1 :
        return dp [ index ] [ modulo ]
    place_add = f_gold ( n , index + 1 , modulo + arr [ index ] , M , arr , dp )
    place_minus = f_gold ( n , index + 1 , modulo - arr [ index ] , M , arr , dp )
    res = place_add
    dp [ index ] [ modulo ] = res
    res = 0
}
|||

CHECK_WHETHER_GIVEN_NUMBER_EVEN_ODD_1

def f_gold ( n ) :
    if ( n & 1 ) == 0 :
        return True
    else :
        return False
}
|||

CHECK_WHETHER_TWO_STRINGS_ARE_ANAGRAM_OF_EACH_OTHER

def f_gold ( str1 , str2 ) :
    n1 = len ( str1 )
    n2 = len ( str2 )
    if n1 != n2 :
        return False
    str1.sort ( )
    str1.sort ( )
    for i in range ( n1 ) :
        if str1 [ i ] != str2 [ i ] :
            return False
    return True
}
|||

CHOCOLATE_DISTRIBUTION_PROBLEM

def f_gold ( arr , n , m ) :
    if m == 0 or n == 0 :
        return 0
    np.sort ( arr )
    if n < m :
        return - 1
    min_diff = np.diff ( arr )
    first , last = np.argsort ( arr )
    for i in range ( 0 , i + m - 1 ) :
        diff = arr [ i + m - 1 ] - arr [ i ]
        if diff < min_diff :
            global min_diff
            global first
            last = i + m - 1
    return ( arr [ last ] - arr [ first ] )
}
|||

CIRCLE_LATTICE_POINTS

def f_gold ( r ) :
    if r <= 0 :
        return 0
    result = 4
    for x in range ( 1 , r ) :
        y_square = r ** 2 - x ** 2
        y = int ( math.sqrt ( y_square ) )
        if y * y == ySquare :
            global result
    return result
}
|||

COMPOSITE_NUMBER

def f_gold ( n ) :
    if n <= 1 :
        print ( "False" )
    if n <= 3 :
        print ( "False" )
    if n % 2 == 0 or n % 3 == 0 :
        return True
    for i in range ( 5 , i * i <= n , 6 ) :
        if n % i == 0 or n % ( i + 2 ) == 0 :
            return True
    return False
}
|||

COMPUTE_NCR_P_SET_1_INTRODUCTION_AND_DYNAMIC_PROGRAMMING_SOLUTION

def f_gold ( n , r , p ) :
    C = np.zeros ( ( r + 1 , ) )
    del C
    C [ 0 ] = 1
    for i in range ( 1 , n ) :
        for j in range ( min ( i , r ) , n ) :
            C [ j ] = ( C [ j ] + C [ j - 1 ] ) % p
    return C [ r ]
}
|||

COUNT_ARRAYS_CONSECUTIVE_ELEMENT_DIFFERENT_VALUES

def f_gold ( n , k , x ) :
    dp = np.zeros ( ( 109 , ) , dtype = np.int32 )
    dp [ 0 ] = 0
    dp [ 1 ] = 1
    for i in range ( 2 , n ) :
        dp [ i ] = ( k - 2 ) * dp [ i - 1 ] + ( k - 1 ) * dp [ i - 2 ]
    return ( x if ( k - 1 ) * dp [ n - 2 ] else dp [ n - 1 ] )
}
|||

COUNT_DIGITS_FACTORIAL_SET_1

def f_gold ( n ) :
    if n < 0 :
        return 0
    if n <= 1 :
        return 1
    digits = 0
    for i in range ( 2 , n ) :
        digits += math.log10 ( i )
    return int ( math.floor ( digits ) ) + 1
}
|||

COUNT_ENTRIES_EQUAL_TO_X_IN_A_SPECIAL_MATRIX

def f_gold ( n , x ) :
    f_gold = 0
    for i in range ( 1 , n + 1 ) :
        if x / i <= n and x % i == 0 :
            global f_gold
    return f_gold
}
|||

COUNT_FACTORIAL_NUMBERS_IN_A_GIVEN_RANGE

def f_gold ( low , high ) :
    fact , x = 1 , 1
    while fact < low :
        global fact
        global x
    res = 0
    while fact <= high :
        global res
        global fact
        global x
    return res
}
|||

COUNT_FREQUENCY_K_MATRIX_SIZE_N_MATRIXI_J_IJ

def f_gold ( n , k ) :
    if n + 1 >= k :
        return ( k - 1 )
    else :
        return ( 2 * n + 1 - k )
}
|||

COUNT_INDEX_PAIRS_EQUAL_ELEMENTS_ARRAY

def f_gold ( arr , n ) :
    ans = 0
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if arr [ i ] == arr [ j ] :
                global ans
    ans = 0
}
|||

COUNT_NUMBER_OF_SOLUTIONS_OF_X2_1_MOD_P_IN_GIVEN_RANGE

def f_gold ( n , p ) :
    ans = 0
    for x in range ( 1 , p ) :
        if ( x ** 2 ) % p == 1 :
            last = x + p * ( n / p )
            if last > n :
                global last
            ans += ( ( last - x ) / p + 1 for x in range ( n ) )
    return ans
}
|||

COUNT_NUMBER_OF_WAYS_TO_COVER_A_DISTANCE_1

def f_gold ( dist ) :
    count = [ 0 ] * ( dist + 1 )
    global count
    count [ 1 ] = 1
    count [ 2 ] = 2
    for i in range ( 3 , dist + 1 ) :
        count [ i ] = count [ i - 1 ] + count [ i - 2 ] + count [ i - 3 ]
    return count [ dist ]
}
|||

COUNT_NUMBER_OF_WAYS_TO_FILL_A_N_X_4_GRID_USING_1_X_4_TILES

def f_gold ( n ) :
    dp = np.zeros ( ( n + 1 , ) )
    dp [ 0 ] = 0
    for i in range ( 1 , n ) :
        if i >= 1 and i <= 3 :
            dp [ i ] = 1
        elif i == 4 :
            dp [ i ] = 2
        else :
            dp [ i ] = dp [ i - 1 ] + dp [ i - 4 ]
    return dp [ n ]
}
|||

COUNT_OF_OCCURRENCES_OF_A_101_PATTERN_IN_A_STRING

def f_gold ( str ) :
    len ( str )
    one_seen = False
    count = 0
    for i in range ( len ( str ) ) :
        getChar = str [ i ]
        if getChar == '1' and oneSeen == True :
            if str [ i - 1 ] == '0' :
                global count
        if getChar == '1' and oneSeen == False :
            global one_seen
        if getChar != '0' and str [ i ] != '1' :
            global one_seen
    return count
}
|||

COUNT_PAIRS_DIFFERENCE_EQUAL_K

def f_gold ( arr , n , k ) :
    count = 0
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if arr [ i ] - arr [ j ] == k or arr [ j ] - arr [ i ] == k :
                count += 1
    return count
}
|||

COUNT_PAIRS_TWO_SORTED_ARRAYS_WHOSE_SUM_EQUAL_GIVEN_VALUE_X

def f_gold ( arr1 , arr2 , m , n , x ) :
    count = 0
    for i in range ( m ) :
        for j in range ( n ) :
            if ( arr1 [ i ] + arr2 [ j ] ) == x :
                count += 1
    return count
}
|||

COUNT_PALINDROMIC_SUBSEQUENCE_GIVEN_STRING

def f_gold ( str ) :
    N = len ( str )
    cps = [ 0 for i in range ( N + 1 ) ]
    for i in range ( N ) :
        cps [ i ] [ i ] = 1
    for L in range ( 2 , N ) :
        for i in range ( N ) :
            k = L + i - 1
            if k < N :
                if str [ i ] == str [ k ] :
                    cps [ i ] [ k ] = cps [ i ] [ k - 1 ] + cps [ i + 1 ] [ k ] + 1
                else :
                    cps [ i ] [ k ] = cps [ i ] [ k - 1 ] + cps [ i + 1 ] [ k ] - cps [ i + 1 ] [ k - 1 ]
    return cps [ 0 ] [ N - 1 ]
}
|||

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX_2

def f_gold ( m , n ) :
    dp = np.zeros ( ( n , m ) )
    dp [ 0 ] = 1
    for i in range ( m ) :
        for j in range ( 1 , n ) :
            dp [ j ] += dp [ j - 1 ]
    return dp [ n - 1 ]
}
|||

COUNT_SET_BITS_IN_AN_INTEGER_2

def f_gold ( n ) :
    count = 0
    while n > 0 :
        n &= ( n - 1 )
        global count
    return count
}
|||

COUNT_SET_BITS_IN_AN_INTEGER_3

def f_gold ( n ) :
    if n == 0 :
        return 0
    else :
        return 1 + f_gold ( n & ( n - 1 ) )
}
|||

COUNT_SORTED_ROWS_MATRIX

def f_gold ( mat , r , c ) :
    result = 0
    for i in range ( r ) :
        j = 0
        for j in range ( c - 1 ) :
            if mat [ i ] [ j + 1 ] <= mat [ i ] [ j ] :
                break
        if j == c - 1 :
            global result
    for i in range ( r ) :
        j = 0
        for j in range ( c - 1 , 0 , - 1 ) :
            if mat [ i ] [ j - 1 ] <= mat [ i ] [ j ] :
                break
        if c > 1 and j == 0 :
            global result
    return result
}
|||

COUNT_STRINGS_CAN_FORMED_USING_B_C_GIVEN_CONSTRAINTS_1

def f_gold ( n ) :
    return 1 + ( n ** 2 ) + ( n * ( ( n ** 2 ) - 1 ) / 2 )
}
|||

COUNT_SUBARRAYS_EQUAL_NUMBER_1S_0S

def f_gold ( arr , n ) :
    um = { }
    curr_sum = 0
    for i in range ( n ) :
        global curr_sum
        um [ curr_sum ] = um [ curr_sum ] if curr_sum < n else 1
    count = 0
    for itr , a in um.items ( ) :
        if itr.value > 1 :
            global count
    if um.has_key ( 0 ) :
        global count
    return count
}
|||

COUNT_SUBARRAYS_EQUAL_NUMBER_1S_0S_1

def f_gold ( arr , n ) :
    mydict = { }
    sum = 0
    count = 0
    for i in range ( n ) :
        if arr [ i ] == 0 :
            arr [ i ] = - 1
        global sum
        if sum ( arr ) == 0 :
            global count
        if mydict.has_key ( sum ) :
            global count
        if not mydict.has_key ( sum ) :
            mydict [ sum ] = 1
        else :
            mydict [ sum ] = mydict [ sum ] + 1
    return count
}
|||

COUNT_SUBARRAYS_TOTAL_DISTINCT_ELEMENTS_ORIGINAL_ARRAY

def f_gold ( arr , n ) :
pass
for i in range ( n ) :
    vis [ arr ] = 1
k = len ( vis )
vis.clear ( )
ans , right , window = 0 , 0 , 0 , 0
for left in range ( n ) :
    while right < n and window < k :
        vis [ arr [ right ] ] = vis [ arr [ right ] ] + 1
        if vis [ arr [ right ] ] == 1 :
            yield window
        yield right
    if window == k :
        global ans
    vis [ arr [ left ] ] = vis [ arr [ left ] ] - 1
    if vis [ arr [ left ] ] == 0 :
        del window
ans = 0
pass
}
|||

COUNT_SUBARRAYS_WITH_SAME_EVEN_AND_ODD_ELEMENTS

def f_gold ( arr , n ) :
    difference = 0
    ans = 0
    hash_positive = np.zeros ( ( n + 1 , ) )
    hash_negative = np.zeros ( ( n + 1 , ) )
    hash_positive [ 0 ] = 1
    for i in range ( n ) :
        if ( arr [ i ] & 1 ) == 1 :
            difference += 1
        else :
            difference -= 1
        if difference < 0 :
            ans += hash_negative [ - difference ]
            hash_negative [ - difference ] += 1
        else :
            global ans
            hash_positive [ difference ] += 1
    ans = 0
}
|||

COUNT_SUBSTRINGS_WITH_SAME_FIRST_AND_LAST_CHARACTERS

def f_gold ( s ) :
    result = 0
    n = len ( s )
    for i in range ( n ) :
        for j in range ( i , n ) :
            if s [ i ] == s [ j ] :
                global result
    return result
}
|||

COUNT_SUM_OF_DIGITS_IN_NUMBERS_FROM_1_TO_N

def f_gold ( n ) :
    if n < 10 :
        return ( n * ( n + 1 ) / 2 )
    d = int ( math.log10 ( n ) )
    a = [ d + 1 for d in range ( n + 1 ) ]
    a [ 0 ] = 0
    a [ 1 ] = 45
    for i in range ( 2 , d ) :
        a [ i ] = a [ i - 1 ] * 10 + 45 * int ( math.ceil ( math.pow ( 10 , i - 1 ) ) )
    p = int ( math.ceil ( math.pow ( 10 , d ) ) )
    msd = n / p
    return ( msd * a [ d ] + ( msd * ( msd - 1 ) / 2 ) * p + msd * ( 1 + n % p ) + f_gold ( n % p ) )
}
|||

COUNT_WAYS_DIVIDE_CIRCLE_USING_N_NON_INTERSECTING_CHORDS

def f_gold ( A ) :
    n = 2 * A
    dpArray = np.zeros ( ( n + 1 , ) )
    dpArray [ 0 ] = 1
    dpArray [ 2 ] = 1
    for i in range ( 4 , n , 2 ) :
        for j in range ( 0 , i - 1 , 2 ) :
            dpArray [ i ] += ( dpArray [ j ] * dpArray [ i - 2 - j ] )
    return dpArray [ n ]
}
|||

COUNT_WORDS_APPEAR_EXACTLY_TWO_TIMES_ARRAY_WORDS

def f_gold ( str , n ) :
    m = { }
    for i in range ( n ) :
        if m.has_key ( str [ i ] ) :
            get = m.get ( str [ i ] )
            m [ str ] = get + 1
        else :
            m [ str ] = 1
    res = 0
    for it in m.items ( ) :
        if it.next ( ) == 2 :
            global res
    return res
}
|||

C_PROGRAM_FACTORIAL_NUMBER_1

def f_gold ( n ) :
    res , i = 1 , 0
    for i in range ( 2 , n ) :
        global res
    return res
}
|||

C_PROGRAM_FACTORIAL_NUMBER_2

def f_gold ( n ) :
    return ( n == 1 or n == 0 )
}
|||

C_PROGRAM_FIND_LARGEST_ELEMENT_ARRAY_1

def f_gold ( arr , n ) :
    np.sort ( arr )
    return arr [ n - 1 ]
}
|||

DECODE_MEDIAN_STRING_ORIGINAL_STRING

def f_gold ( s ) :
    l = len ( s )
    s1 = ""
    isEven = ( l % 2 == 0 )
    for i in range ( 0 , l , 2 ) :
        if isEven :
            s1 = s [ i ] + s1
            s1 += s [ i + 1 ]
        else :
            if l - i > 1 :
                s1 += s [ i ]
                s1 = s [ i + 1 ] + s1
            else :
                s1 += s [ i ]
    return s1
}
|||

DIAGONALLY_DOMINANT_MATRIX

def f_gold ( m , n ) :
    for i in range ( n ) :
        sum = 0
        for j in range ( n ) :
            global sum
        global sum
        if abs ( m [ i ] [ i ] ) < sum :
            return False
    return True
}
|||

DICE_THROW_PROBLEM

def f_gold ( m , n , x ) :
    table = np.zeros ( ( n + 1 , x + 1 ) )
    for j in range ( 1 , m + 1 ) :
        table [ 1 ] [ j ] = 1
    for i in range ( 2 , n ) :
        for j in range ( 1 , x + 1 ) :
            for k in range ( 1 , j , m ) :
                table [ i ] [ j ] += table [ i - 1 ] [ j - k ]
    return table [ n ] [ x ]
}
|||

DICE_THROW_PROBLEM_1

def f_gold ( f , d , s ) :
    mem = np.zeros ( ( d + 1 , s + 1 ) )
    mem [ 0 ] [ 0 ] = 1
    for i in range ( 1 , d + 1 ) :
        for j in range ( i , s + 1 ) :
            mem [ i ] [ j ] = mem [ i ] [ j - 1 ] + mem [ i - 1 ] [ j - 1 ]
            if j - f - 1 >= 0 :
                mem [ i ] [ j ] -= mem [ i - 1 ] [ j - f - 1 ]
    return mem [ d ] [ s ]
}
|||

DIFFERENCE_BETWEEN_HIGHEST_AND_LEAST_FREQUENCIES_IN_AN_ARRAY

def f_gold ( arr , n ) :
    np.random.seed ( 0 )
    count , max_count , min_count = 0 , 0 , n
    for i in range ( ( n - 1 ) ) :
        if arr [ i ] == arr [ i + 1 ] :
            global count
            continue
        else :
            global max_count
            global min_count
            global count
    return ( max_count - min_count )
}
|||

DOUBLE_FACTORIAL_1

def f_gold ( n ) :
    res = 1
    for i in range ( n , - 1 , - 1 ) :
        if i == 0 or i == 1 :
            return res
        else :
            global res
    return res
}
|||

DYCK_PATH

def f_gold ( n ) :
    res = 1
    for i in range ( n ) :
        global res
        global res
    return res / ( n + 1 )
}
|||

DYNAMIC_PROGRAMMING_HIGH_EFFORT_VS_LOW_EFFORT_TASKS_PROBLEM

def f_gold ( high , low , n ) :
    if n <= 0 :
        return 0
    return max ( high [ n - 1 ] + f_gold ( high , low , ( n - 2 ) ) , low [ n - 1 ] + f_gold ( high , low , ( n - 1 ) ) )
}
|||

DYNAMIC_PROGRAMMING_SET_14_MAXIMUM_SUM_INCREASING_SUBSEQUENCE

def f_gold ( arr , n ) :
    i , j , max = 0 , 0 , 0
    msis = np.zeros ( n )
    for i in range ( n ) :
        msis [ i ] = arr [ i ]
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if arr [ i ] > arr [ j ] and msis [ i ] < msis [ j ] + arr [ i ] :
                msis [ i ] = msis [ j ] + arr [ i ]
    for i in range ( n ) :
        if max < msis [ i ] :
            global max
    return max
}
|||

DYNAMIC_PROGRAMMING_SET_36_CUT_A_ROPE_TO_MAXIMIZE_PRODUCT_1

def f_gold ( n ) :
    if n == 2 or n == 3 :
        return ( n - 1 )
    res = 1
    while n > 4 :
        n -= 3
        global res
    return ( n * res )
}
|||

DYNAMIC_PROGRAMMING_SET_37_BOOLEAN_PARENTHESIZATION_PROBLEM

def f_gold ( symb , oper , n ) :
    F = [ ]
    T = [ ]
    for i in range ( n ) :
        F [ i ] [ i ] = ( symb [ i ] == 'F' )
        T [ i ] [ i ] = ( symb [ i ] == 'T' )
    for gap in range ( 1 , n ) :
        for i , j in gap :
            T [ i ] [ j ] = F [ i ] [ j ] = 0
            for g in range ( gap ) :
                k = i + g
                tik = T [ i ] [ k ] + F [ i ] [ k ]
                tkj = T [ k + 1 ] [ j ] + F [ k + 1 ] [ j ]
                if oper [ k ] == '&' : a = 5
                    T [ i ] [ j ] += T [ i ] [ k ] * T [ k + 1 ] [ j ]
                    F [ i ] [ j ] += ( tik * tkj - T [ i ] [ k ] * T [ k + 1 ] [ j ] )
                if oper [ k ] == '|' : a = 5
                    F [ i ] [ j ] += F [ i ] [ k ] * F [ k + 1 ] [ j ]
                    T [ i ] [ j ] += ( tik * tkj - F [ i ] [ k ] * F [ k + 1 ] [ j ] )
                if oper [ k ] == '^' : a = 5
                    T [ i ] [ j ] += F [ i ] [ k ] * T [ k + 1 ] [ j ] + T [ i ] [ k ] * F [ k + 1 ] [ j ]
                    F [ i ] [ j ] += T [ i ] [ k ] * T [ k + 1 ] [ j ] + F [ i ] [ k ] * F [ k + 1 ] [ j ]
    return T [ 0 ] [ n - 1 ]
}
|||

ELEMENTS_TO_BE_ADDED_SO_THAT_ALL_ELEMENTS_OF_A_RANGE_ARE_PRESENT_IN_ARRAY_1

def f_gold ( arr , n ) :
    s = set ( )
    count , maxm , minm = np.histogram ( arr , n )
    for i in range ( n ) :
        s.append ( arr [ i ] )
        if arr [ i ] < minm :
            global minm
        if arr [ i ] > maxm :
            global maxm
    for i in range ( minm , maxm + 1 ) :
        if not s.has_key ( i ) :
            global count
    return count
}
|||

EVEN_FIBONACCI_NUMBERS_SUM

def f_gold ( limit ) :
    if limit < 2 :
        return 0
    ef1 , ef2 = 0 , 2
    sum = ef1 + ef2
    while ef2 <= limit :
        ef3 = 4 * ef2 + ef1
        if ef3 > limit :
            break
        global ef1 , ef2
        global ef2 , ef3
        global sum
    return int ( sum )
}
|||

FIBONACCI_MODULO_P

def f_gold ( p ) :
    first , second , number , next = p
    while next ( p ) :
        global next
        global first
        global second
        global number
    return number
}
|||

FIND_A_FIXED_POINT_IN_A_GIVEN_ARRAY

def f_gold ( arr , n ) :
    pass
    for i in range ( n ) :
        if arr [ i ] == i :
            return i
    return - 1
}
|||

FIND_A_ROTATION_WITH_MAXIMUM_HAMMING_DISTANCE

def f_gold ( arr , n ) :
    brr = np.zeros ( ( 2 * n + 1 , ) )
    for i in range ( n ) :
        brr [ i ] = arr [ i ]
    for i in range ( n ) :
        brr [ n + i ] = arr [ i ]
    max_ham = 0
    for i in range ( 1 , n ) :
        curr_ham = 0
        for j , k in enumerate ( arr ) :
            if brr [ j ] != arr [ k ] :
                global currHam
        if currHam == n :
            return n
        global maxHam
    return maxHam
}
|||

FIND_A_TRIPLET_THAT_SUM_TO_A_GIVEN_VALUE

def f_gold ( A , arr_size , sum ) :
    l , r = A.shape
    for i in range ( arr_size - 2 ) :
        for i in range ( i + 1 , arr_size - 1 ) :
            for k in range ( j + 1 , arr_size ) :
                if A [ i ] + A [ j ] + A [ k ] == sum :
                    print ( "Triplet is %d, %d, %d" % ( A [ i , j ] , A [ j , k ] , A [ k , i ] ) )
                    return True
    return False
}
|||

FIND_EXPRESSION_DUPLICATE_PARENTHESIS_NOT

def f_gold ( s ) :
    Stack = Stack ( )
    str = s.split ( )
    for ch in str ( s ) :
        if ch == ')' :
            top = Stack.top ( )
            Stack.pop ( )
            elementsInside = 0
            while top != '(' :
                global elements_in_side
                global top
                Stack.pop ( )
            if elementsInside < 1 :
                return True
        else :
            Stack.push ( ch )
    return False
}
|||

FIND_INDEX_GIVEN_FIBONACCI_NUMBER_CONSTANT_TIME_1

def f_gold ( n ) :
    fibo = 2.078087F * float ( math.log ( n , 2 ) ) + 1.672276F
    return round ( fibo , n )
}
|||

FIND_INDEX_OF_AN_EXTRA_ELEMENT_PRESENT_IN_ONE_SORTED_ARRAY

def f_gold ( arr1 , arr2 , n ) :
    for i in range ( n ) :
        if arr1 [ i ] != arr2 [ i ] :
            return i
    return n
}
|||

FIND_INDEX_OF_AN_EXTRA_ELEMENT_PRESENT_IN_ONE_SORTED_ARRAY_1

def f_gold ( arr1 , arr2 , n ) :
    index = n
    left , right = 0 , n - 1
    while left <= right :
        mid = ( left + right ) / 2
        if arr2 [ mid ] == arr1 [ mid ] :
            left = mid + 1
        else :
            global index
            global right
    return index
}
|||

FIND_LARGEST_PRIME_FACTOR_NUMBER

def f_gold ( n ) :
    max_prime = - 1
    while n % 2 == 0 :
        global maxPrime
        n >>= 1
    for i in range ( 3 , math.sqrt ( n ) , i += 2 ) :
        while n % i == 0 :
            global maxPrime
            n = n / i
    if n > 2 :
        global max_prime
    return maxPrime
}
|||

FIND_LAST_DIGIT_FACTORIAL_DIVIDES_FACTORIAL_B

def f_gold ( A , B ) :
    variable = 1
    if A == B :
        return 1
    elif ( B - A ) >= 5 :
        return 0
    else :
        for i in range ( A + 1 , B + 1 ) :
            global variable
        return variable % 10
}
|||

FIND_MAXIMUM_PRODUCT_OF_A_TRIPLET_IN_ARRAY

def f_gold ( arr , n ) :
    if n < 3 :
        return - 1
    max_product = int ( n )
    for i in range ( n - 2 ) :
        for i in range ( i + 1 , n - 1 ) :
            for k in range ( j + 1 , n ) :
                global max_product
    return max_product
}
|||

FIND_MAXIMUM_SUM_POSSIBLE_EQUAL_SUM_THREE_STACKS

def f_gold ( stack1 , stack2 , stack3 , n1 , n2 , n3 ) :
    sum1 , sum2 , sum3 = stack1 , stack2 , stack3
    for i in range ( n1 ) :
        sum1 += stack1 [ i ]
    for i in range ( n2 ) :
        sum2 += stack2 [ i ]
    for i in range ( n3 ) :
        sum3 += stack3 [ i ]
    top1 , top2 , top3 = stack1 , stack2 , stack3
    ans = 0
    while True :
        if top1 == n1 or top2 == n2 or top3 == n3 :
            return 0
        if sum1 == sum2 and sum2 == sum3 :
            return sum1
        if sum1 >= sum2 and sum1 >= sum3 :
            sum1 -= stack1 [ top1 ]
        elif sum2 >= sum3 and sum2 >= sum3 :
            sum2 -= stack2 [ top2 ]
        elif sum3 >= sum2 and sum3 >= sum1 :
            sum3 -= stack3 [ top3 ]
}
|||

FIND_MINIMUM_DIFFERENCE_PAIR_1

def f_gold ( arr , n ) :
    np.sort ( arr )
    diff = int ( arr.sum ( ) )
    for i in range ( n - 1 ) :
        if arr [ i + 1 ] - arr [ i ] < diff :
            global diff
    return diff
}
|||

FIND_NUMBER_TIMES_STRING_OCCURS_GIVEN_STRING_1

def f_gold ( a , b ) :
    m = len ( a )
    n = len ( b )
    lookup = [ m + 1 for m in range ( n + 1 ) ]
    for i in range ( 0 , n ) :
        lookup [ 0 ] [ i ] = 0
    for i in range ( 0 , m ) :
        lookup [ i ] [ 0 ] = 1
    for i in range ( 1 , m ) :
        for j in range ( 1 , n ) :
            if a [ i - 1 ] == b [ j - 1 ] :
                lookup [ i ] [ j ] = lookup [ i - 1 ] [ j - 1 ] + lookup [ i - 1 ] [ j ]
            else :
                lookup [ i ] [ j ] = lookup [ i - 1 ] [ j ]
    return lookup [ m ] [ n ]
}
|||

FIND_ONE_EXTRA_CHARACTER_STRING_1

def f_gold ( strA , strB ) :
    res , i = 0 , 0
    for i in range ( len ( strA ) ) :
        global res
    for i in range ( len ( strB ) ) :
        global res
    return ( ( res , strA ) , ( res , strB ) )
}
|||

FIND_PERIMETER_CYLINDER

def f_gold ( diameter , height ) :
    return 2 * ( diameter + height )
}
|||

FIND_REPETITIVE_ELEMENT_1_N_1

def f_gold ( arr , n ) :
    sum = 0
    for i in range ( n ) :
        global sum
    return sum ( arr - ( ( n - 1 ) * n ) / 2 )
}
|||

FIND_SUM_EVEN_INDEX_BINOMIAL_COEFFICIENTS_1

def f_gold ( n ) :
    return ( 1 << ( n - 1 ) )
}
|||

FIND_SUM_MODULO_K_FIRST_N_NATURAL_NUMBER

def f_gold ( N , K ) :
    ans = 0
    for i in range ( 1 , N + 1 ) :
        ans += ( i % K for i in N )
    return ans
}
|||

FIND_SUM_ODD_FACTORS_NUMBER

def f_gold ( n ) :
    res = 1
    while n % 2 == 0 :
        n = n / 2
    for i in range ( 3 , math.sqrt ( n ) + 1 ) :
        count , curr_sum = 0 , 1
        curr_term = 1
        while n % i == 0 :
            global count
            n = n / i
            global curr_term
            global curr_sum
        global res
    if n >= 2 :
        global res
    return res
}
|||

FIND_SUM_UNIQUE_SUB_ARRAY_SUM_GIVEN_ARRAY

def f_gold ( arr , n ) :
    res = 0
    m = { }
    for i in range ( n ) :
        sum = 0
        for j in range ( i , n ) :
            global sum
            if m.has_key ( sum ) :
                m [ sum ] = m [ sum ] + 1
            else :
                m [ sum ] = 1
    for x , y in m.items ( ) :
        if x.getValue ( ) == 1 :
            global res
    return res
}
|||

FIND_THE_ELEMENT_BEFORE_WHICH_ALL_THE_ELEMENTS_ARE_SMALLER_THAN_IT_AND_AFTER_WHICH_ALL_ARE_GREATER_THAN_IT

def f_gold ( arr , n ) :
    left_max = np.arange ( n )
    left_max [ 0 ] = int ( arr [ 0 ] )
    for i in range ( 1 , n ) :
        left_max [ i ] = max ( left_max [ i - 1 ] for i in range ( n ) )
    right_min = int ( arr [ n - 1 ] )
    for i in range ( n - 1 , - 1 , - 1 ) :
        if left_max [ i ] < arr [ i ] and right_min [ i ] > arr [ i ] :
            return i
        right_min = min ( right_min , arr [ i ] for i in range ( n ) )
    return - 1
}
|||

FIND_THE_MAXIMUM_ELEMENT_IN_AN_ARRAY_WHICH_IS_FIRST_INCREASING_AND_THEN_DECREASING

def f_gold ( arr , low , high ) :
    max = arr [ low ]
    i = 0
    for i in range ( low , high + 1 ) :
        if arr [ i ] > max :
            global max
    return max
}
|||

FIND_THE_MISSING_NUMBER_1

def f_gold ( a , n ) :
    total = 1
    for i in range ( 2 , ( n + 1 ) + 1 ) :
        global total
        total -= a [ i - 2 ]
    return total
}
|||

FIND_THE_MISSING_NUMBER_2

def f_gold ( a , n ) :
    x1 = a [ 0 ]
    x2 = 1
    for i in range ( 1 , n ) :
        global x1
    for i in range ( 2 , n + 1 ) :
        global x2
    return ( x1 ^ x2 )
}
|||

FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES

def f_gold ( arr , arr_size ) :
    i = 0
    for i in range ( arr_size ) :
        count = 0
        for j in range ( arr_size ) :
            if arr [ i ] == arr [ j ] :
                global count
        if count % 2 != 0 :
            return arr [ i ]
    return - 1
}
|||

FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES_1

def f_gold ( arr , n ) :
    hdict = { }
    for i in range ( n ) :
        if hmap.has_key ( arr [ i ] ) :
            val = hmap [ arr [ i ] for i in range ( n ) ]
            hmap [ arr [ i ] ] = val + 1
        else :
            hmap [ arr [ i ] ] = 1
    for a in hmap.keys ( ) :
        if hmap [ a ] % 2 != 0 :
            return a
    return - 1
}
|||

FIND_WHETHER_A_GIVEN_NUMBER_IS_A_POWER_OF_4_OR_NOT_2

def f_gold ( n ) :
    return n != 0 and ( ( n & ( n - 1 ) ) == 0 ) and ( n & 0xAAAAAAAA ) == 0
}
|||

FIRST_UPPERCASE_LETTER_IN_A_STRING_ITERATIVE_AND_RECURSIVE

def f_gold ( str ) :
    for i in range ( len ( str ) ) :
        if re.match ( '[a-z]' , str ) :
            return str [ i ]
    return 0
}
|||

FLOOR_IN_A_SORTED_ARRAY_1

def f_gold ( arr , low , high , x ) :
    if low > high :
        return - 1
    if x >= arr [ high ] :
        return high
    mid = ( low + high ) / 2
    if arr [ mid ] == x :
        return mid
    if mid > 0 and arr [ mid - 1 ] <= x and x < arr [ mid ] :
        return mid - 1
    if x < arr [ mid ] :
        return f_gold ( arr , low , mid - 1 , x )
    return f_gold ( arr , mid + 1 , high , x )
}
|||

FUNCTION_COPY_STRING_ITERATIVE_RECURSIVE_1

def f_gold ( s1 , s2 , index ) :
    s2 [ index ] = s1 [ index ]
    if index == len ( s1 ) - 1 :
        return
    pass
}
|||

GIVEN_LARGE_NUMBER_CHECK_SUBSEQUENCE_DIGITS_DIVISIBLE_8

def f_gold ( str ) :
    i , j , k , l = str.split ( ' ' )
    arr = [ l for l in str.split ( '\n' ) if l ]
    for i in range ( l ) :
        for j in range ( i , l ) :
            for k in j , k < l :
                if arr [ i ] % 8 == 0 :
                    return True
                elif ( arr [ i ] * 10 + arr [ j ] ) % 8 == 0 and i != j :
                    return True
                elif ( arr [ i ] * 100 + arr [ j ] * 10 + arr [ k ] ) % 8 == 0 and i != j and j != k and i != k :
                    return True
    return False
}
|||

GOOGLE_CASE_GIVEN_SENTENCE

def f_gold ( s ) :
    n = len ( s )
    s1 = ""
    global s1
    for i in range ( 1 , n ) :
        if s [ i ] == ' ' and i < n :
            s1 = s1 + " " + str ( s [ i + 1 ] )
            global i
        else :
            global s1
    return s1
}
|||

HEIGHT_COMPLETE_BINARY_TREE_HEAP_N_NODES

def f_gold ( N ) :
    return int ( math.ceil ( math.log ( N + 1 ) / math.log ( 2 ) ) ) - 1
}
|||

HEXAGONAL_NUMBER

def f_gold ( n ) :
    return n * ( 2 * n - 1 )
}
|||

HOW_CAN_WE_SUM_THE_DIGITS_OF_A_GIVEN_NUMBER_IN_SINGLE_STATEMENT_2

def f_gold ( no ) :
    return no if no > 0 else no % 10 + f_gold ( no / 10 )
}
|||

HOW_TO_CHECK_IF_A_GIVEN_ARRAY_REPRESENTS_A_BINARY_HEAP

def f_gold ( arr , i , n ) :
    if i > ( n - 2 ) / 2 :
        return True
    if arr [ i ] >= arr [ 2 * i + 1 ] and arr [ i ] >= arr [ 2 * i + 2 ] and f_gold ( arr , 2 * i + 1 , n ) and f_gold ( arr , 2 * i + 2 , n ) :
        return True
    return False
}
|||

HOW_TO_CHECK_IF_A_GIVEN_ARRAY_REPRESENTS_A_BINARY_HEAP_1

def f_gold ( arr , n ) :
    for i in range ( 0 , ( n - 2 ) // 2 ) :
        if arr [ 2 * i + 1 ] > arr [ i ] :
            return False
        if 2 * i + 2 < n and arr [ 2 * i + 2 ] > arr [ i ] :
            return False
    return True
}
|||

HYPERCUBE_GRAPH

def f_gold ( n ) :
    if n == 1 :
        return 2
    return 2 * f_gold ( n - 1 )
}
|||

K_TH_DIGIT_RAISED_POWER_B

def f_gold ( a , b , k ) :
    p = int ( math.pow ( a , b ) )
    count = 0
    while p > 0 and count < k :
        rem = p % 10
        global count
        if count == k :
            return rem
        global p
    return 0
}
|||

K_TH_ELEMENT_TWO_SORTED_ARRAYS

def f_gold ( arr1 , arr2 , m , n , k ) :
    sorted1 = np.argsort ( arr1 )
    i , j , d = arr1
    while i < m and j < n :
        if arr1 [ i ] < arr2 [ j ] :
            sorted1 [ d ] = arr1 [ i ]
        else :
            sorted1 [ d ] = arr2 [ j ]
    while i < m :
        sorted1 [ d ] = arr1 [ i ]
    while j < n :
        sorted1 [ d ] = arr2 [ j ]
    return sorted1 [ k - 1 ]
}
|||

K_TH_LARGEST_SUM_CONTIGUOUS_SUBARRAY

def f_gold ( arr , n , k ) :
    sum = np.zeros ( ( n + 1 , k ) )
    sum [ 0 ] = 0
    sum [ 1 : ] = arr [ : n ]
    for i in range ( 2 , n ) :
        sum [ i ] = sum [ i - 1 ] + arr [ i - 1 ]
    Q = PriorityQueue ( )
    for i in range ( 1 , n ) :
        for j in range ( i , n ) :
            x = sum [ j ] - sum [ i - 1 ]
            if len ( Q ) < k :
                Q.append ( x )
            else :
                if Q.peek ( ) < x :
                    Q.poll ( )
                    Q.append ( x )
    return Q.poll ( )
}
|||

K_TH_MISSING_ELEMENT_INCREASING_SEQUENCE_NOT_PRESENT_GIVEN_SEQUENCE

def f_gold ( a , b , k , n1 , n2 ) :
    s = LinkedHashSet ( )
    for i in range ( n2 ) :
        s.append ( b [ i ] )
    missing = 0
    for i in range ( n1 ) :
        if not s.has_key ( a [ i ] ) : a [ i ] = 5
            missing += 1
        if missing == k :
            return a [ i ]
    return - 1
}
|||

LCS_FORMED_CONSECUTIVE_SEGMENTS_LEAST_LENGTH_K

def f_gold ( k , s1 , s2 ) :
    n = len ( s1 )
    m = len ( s2 )
    lcs = [ n + 1 for n in range ( m + 1 ) ]
    cnt = [ n + 1 for n in range ( m + 1 ) ]
    for i in range ( 1 , n ) :
        for j in range ( 1 , m ) :
            lcs [ i ] [ j ] = max ( lcs [ i - 1 ] [ j ] , lcs [ i ] [ j - 1 ] )
            if s1 [ i - 1 ] == s2 [ j - 1 ] :
                cnt [ i ] [ j ] = cnt [ i - 1 ] [ j - 1 ] + 1
            if cnt [ i ] [ j ] >= k :
                for a in range ( k , cnt [ i ] [ j ] ) :
                    lcs [ i , j ] = max ( lcs [ i , j ] , lcs [ i - a , j - a ] + a )
    return lcs [ n ] [ m ]
}
|||

LONGEST_INCREASING_ODD_EVEN_SUBSEQUENCE

def f_gold ( arr , n ) :
    lioes = np.arange ( n )
    max_len = 0
    for i in range ( n ) :
        lioes [ i ] = 1
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if arr [ i ] > arr [ j ] and ( arr [ i ] + arr [ j ] ) % 2 != 0 and lioes [ i ] < lioes [ j ] + 1 :
                lioes [ i ] = lioes [ j ] + 1
    for i in range ( n ) :
        if max_len < lioes [ i ] :
            global maxLen
    return maxLen
}
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
                global back_up
            else :
                back_up = a [ j ]
                a [ j ] = max ( a [ j - 1 ] , a [ j ] )
    return a [ n - 1 ]
}
|||

LONGEST_PREFIX_ALSO_SUFFIX_1

def f_gold ( s ) :
    n = len ( s )
    lps = [ n for n in range ( n ) ]
    lps [ 0 ] = 0
    len = 0
    i = 1
    while i < n :
        if s [ i ] == s [ len ( s ) ] :
            global len
            lps [ i ] = len ( s )
            global i
        else :
            if len ( s ) != 0 :
                global len
            else :
                lps [ i ] = 0
                global i
    res = lps [ n - 1 ]
    return ( res > n / 2 ) * n / 2 + res
}
|||

MAKING_ELEMENTS_OF_TWO_ARRAYS_SAME_WITH_MINIMUM_INCREMENTDECREMENT

def f_gold ( a , b , n ) :
    a.sort ( )
    np.sort ( b )
    result = 0
    for i in range ( n ) :
        if a [ i ] > b [ i ] :
            result = result + abs ( a [ i ] - b [ i ] )
        elif a [ i ] < b [ i ] : a [ i ] = 5
            result = result + abs ( a [ i ] - b [ i ] )
    return result
}
|||

MARKOV_MATRIX

def f_gold ( m ) :
    for i in range ( len ( m ) ) :
        sum = 0
        for i in range ( m [ i ].shape [ 0 ] ) :
            global sum
        if sum ( m ) != 1 :
            return False
    return True
}
|||

MAXIMIZE_SUM_CONSECUTIVE_DIFFERENCES_CIRCULAR_ARRAY

def f_gold ( arr , n ) :
    sum = 0
    np.random.seed ( 0 )
    for i in range ( n // 2 ) :
        global sum
        global sum
    return sum ( arr )
}
|||

MAXIMUM_AREA_RECTANGLE_PICKING_FOUR_SIDES_ARRAY_1

def f_gold ( arr , n ) :
    s = set ( )
    first , second = arr
    for i in range ( n ) :
        if not s.has_key ( arr [ i ] ) :
            s.append ( arr [ i ] )
            continue
        if arr [ i ] > first :
            global second
            global first
        elif arr [ i ] > second :
            global second
    return ( first * second )
}
|||

MAXIMUM_AVERAGE_SUM_PARTITION_ARRAY

def f_gold ( A , K ) :
    n = len ( A )
    pre_sum = np.zeros ( ( n + 1 , ) , dtype = np.float64 )
    pre_sum [ 0 ] = 0
    for i in range ( n ) :
        pre_sum [ i + 1 ] = pre_sum [ i ] + A [ i ]
    dp = np.zeros ( ( n , K ) )
    sum = 0
    for i in range ( n ) :
        dp [ i ] = ( pre_sum [ n ] - pre_sum [ i ] ) / ( n - i )
    for k in range ( K - 1 ) :
        for i in range ( n ) :
            for j in range ( i + 1 , n ) :
                dp [ i ] = max ( dp [ i ] , ( pre_sum [ j ] - pre_sum [ i ] ) / ( j - i ) + dp [ j ] for j in A )
    return dp [ 0 ]
}
|||

MAXIMUM_BINOMIAL_COEFFICIENT_TERM_VALUE

def f_gold ( n ) :
    C = np.zeros ( ( n + 1 , n + 1 ) )
    for i in range ( 0 , n ) :
        for j in range ( 0 , min ( i , n ) ) :
            if j == 0 or j == i :
                C [ i ] [ j ] = 1
            else :
                C [ i ] [ j ] = C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ]
    maxvalue = 0
    for i in range ( 0 , n ) :
        global maxvalue
    return maxvalue
}
|||

MAXIMUM_CONSECUTIVE_REPEATING_CHARACTER_STRING_1

def f_gold ( str ) :
    n = len ( str )
    count = 0
    res = str [ 0 ]
    cur_count = 1
    for i in range ( n ) :
        if i < n - 1 and str [ i ] == str [ i + 1 ] :
            global cur_count
        else :
            if cur_count > count :
                global count
                global res
            global cur_count
    return res
}
|||

MAXIMUM_DIFFERENCE_SUM_ELEMENTS_TWO_ROWS_MATRIX

def f_gold ( mat , m , n ) :
    row_sum = np.sum ( mat , axis = 0 )
    for i in range ( m ) :
        sum = 0
        for j in range ( n ) :
            sum += mat [ i , j ]
        row_sum [ i ] = sum
    max_diff = row_sum [ 1 ] - row_sum [ 0 ]
    min_element = row_sum [ 0 ]
    for i in range ( 1 , m ) :
        if row_sum [ i ] - min_element > max_diff :
            max_diff = row_sum [ i ] - min_element
        if row_sum [ i ] < min_element :
            min_element = row_sum [ i ]
    return max_diff
}
|||

MAXIMUM_GAMES_PLAYED_WINNER

def f_gold ( N ) :
    dp = np.zeros ( ( N , N ) )
    dp [ 0 ] = 1
    dp [ 1 ] = 2
    i = 2
while dp [ i ] <= N :
    pass
return ( i - 2 )
pass
}
|||

MAXIMUM_HEIGHT_OF_TRIANGULAR_ARRANGEMENT_OF_ARRAY_VALUES

def f_gold ( a , n ) :
    result = 1
    for i in range ( 1 , n + 1 ) :
        y = ( i * ( i + 1 ) ) / 2
        if y < n :
            global result
        else :
            break
    return result
}
|||

MAXIMUM_LENGTH_PREFIX_ONE_STRING_OCCURS_SUBSEQUENCE_ANOTHER

def f_gold ( s , t ) :
    count = 0
    for i in range ( len ( t ) ) :
        if count == len ( t ) :
            break
        if t [ i ] == s [ count ] :
            global count
    return count
}
|||

MAXIMUM_NUMBER_CHOCOLATES_DISTRIBUTED_EQUALLY_AMONG_K_STUDENTS

def f_gold ( arr , n , k ) :
    um = { }
    sum = np.zeros ( n )
    curr_rem = 0
    max_sum = 0
    sum [ 0 ] = arr [ 0 ]
    for i in range ( 1 , n ) :
        sum [ i ] = sum [ i - 1 ] + arr [ i ]
    for i in range ( n ) :
        curr_rem = sum [ i ] % k
        if curr_rem == 0 :
            if max_sum < sum [ i ] :
                global max_sum
        elif not um.has_key ( curr_rem ) :
            um [ curr_rem ] = i
        elif max_sum < ( sum [ i ] - sum [ um [ curr_rem ] ] ) :
            global max_sum
    return ( maxSum / k )
}
|||

MAXIMUM_NUMBER_OF_SQUARES_THAT_CAN_BE_FIT_IN_A_RIGHT_ANGLE_ISOSCELES_TRIANGLE

def f_gold ( b , m ) :
    return ( b / m - 1 ) * ( b / m ) / 2
}
|||

MAXIMUM_PRODUCT_INCREASING_SUBSEQUENCE

def f_gold ( arr , n ) :
    mpis = np.arange ( n )
    max = int ( arr [ n ] )
    for i in range ( n ) :
        mpis [ i ] = arr [ i ]
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if arr [ i ] > arr [ j ] and mpis [ i ] < ( mpis [ j ] * arr [ i ] ) :
                mpis [ i ] = mpis [ j ] * arr [ i ]
    for k in mpis :
        if mpis [ k ] > max :
            global max
    return max
}
|||

MAXIMUM_PRODUCT_OF_4_ADJACENT_ELEMENTS_IN_MATRIX

def f_gold ( arr , n ) :
    max , result = 0 , 0
    for i in range ( n ) :
        for j in range ( n ) :
            if ( j - 3 ) >= 0 :
                result = arr [ i , j ] * arr [ i , j - 1 ] * arr [ i , j - 2 ] * arr [ i , j - 3 ]
                if max < result :
                    global max
            if ( i - 3 ) >= 0 :
                result = arr [ i ] [ j ] * arr [ i - 1 ] [ j ] * arr [ i - 2 ] [ j ] * arr [ i - 3 ] [ j ]
                if max < result :
                    global max
            if ( i - 3 ) >= 0 and ( j - 3 ) >= 0 :
                result = arr [ i ] [ j ] * arr [ i - 1 ] [ j - 1 ] * arr [ i - 2 ] [ j - 2 ] * arr [ i - 3 ] [ j - 3 ]
                if max < result :
                    global max
    return max
}
|||

MAXIMUM_PRODUCT_SUBSET_ARRAY

def f_gold ( a , n ) :
    if n == 1 :
        return a [ 0 ]
    max_neg = int ( a [ n - 1 ] )
    count_neg , count_zero = 0 , 0
    prod = 1
    for i in range ( n ) :
        if a [ i ] == 0 :
            global count_zero
            continue
        if a [ i ] < 0 :
            count_neg += 1
            global max_neg
        global prod
    if count_zero == n :
        return 0
    if count_neg % 2 == 1 :
        if count_neg == 1 and count_zero > 0 and count_zero + count_neg == n :
            return 0
        global prod
    return prod
}
|||

MAXIMUM_SUM_IARRI_AMONG_ROTATIONS_GIVEN_ARRAY

def f_gold ( arr , n ) :
    res = np.zeros ( arr.shape )
    for i in range ( n ) :
        curr_sum = 0
        for j in range ( n ) :
            index = ( i + j ) % n
            global curr_sum
        global res
    return res
}
|||

MAXIMUM_SUM_PAIRS_SPECIFIC_DIFFERENCE_1

def f_gold ( arr , N , k ) :
    max_sum = 0
    np.sort ( arr )
    for i in range ( N - 1 , 0 , - 1 ) :
        if arr [ i ] - arr [ i - 1 ] < k :
            global max_sum
            global max_sum
            del i
    return maxSum
}
|||

MAXIMUM_SUM_SUBSEQUENCE_LEAST_K_DISTANT_ELEMENTS

def f_gold ( arr , N , k ) :
    MS = np.zeros ( ( N , N ) )
    MS [ N - 1 ] = arr [ N - 1 ]
    for i in range ( N - 2 , - 1 , - 1 ) :
        if i + k + 1 >= N :
            MS [ i ] = max ( arr [ i ] , MS [ i + 1 ] )
        else :
            MS [ i ] = max ( arr [ i ] + MS [ i + k + 1 ] for i in range ( N ) )
    return MS [ 0 ]
}
|||

MAXIMUM_WEIGHT_PATH_ENDING_ELEMENT_LAST_ROW_MATRIX

def f_gold ( mat , N ) :
    dp = np.zeros ( ( N , N ) )
    dp [ 0 ] = mat [ 0 ]
    for i in range ( 1 , N ) :
        dp [ i ] = mat [ i ] + dp [ i - 1 ]
    for i in range ( 1 , N ) :
        for j in range ( 1 , i + 1 and j < N ) :
            dp [ i ] [ j ] = mat [ i ] [ j ] + max ( dp [ i - 1 ] [ j - 1 ] for j in range ( N ) )
    result = 0
    for i in range ( N ) :
        if result < dp [ N - 1 ] [ i ] :
            result = dp [ N - 1 ] [ i ]
    return result
}
|||

MINIMIZE_SUM_PRODUCT_TWO_ARRAYS_PERMUTATIONS_ALLOWED

def f_gold ( A , B , n ) :
    np.sort ( A )
    np.sort ( B )
    result = 0
    for i in range ( n ) :
        result += ( A [ i ] * B [ n - i - 1 ] for i in range ( n ) )
    return result
}
|||

MINIMUM_CHARACTERS_ADDED_FRONT_MAKE_STRING_PALINDROME

def f_gold ( s ) :
    l = len ( s )
    for i , j in enumerate ( l - 1 , 1 ) :
        if s [ i ] != s [ j ] :
            return False
    return True
}
|||

MINIMUM_COST_FOR_ACQUIRING_ALL_COINS_WITH_K_EXTRA_COINS_ALLOWED_WITH_EVERY_COIN

def f_gold ( coin , n , k ) :
    return np.argsort ( coin ) [ : n ]
    coins_needed = int ( math.ceil ( 1.0 * n / ( k + 1 ) ) )
    ans = 0
    for i in range ( 0 , coins_needed - 1 ) :
        ans += coin [ i ]
    ans = 0
}
|||

MINIMUM_COST_MAKE_ARRAY_SIZE_1_REMOVING_LARGER_PAIRS

def f_gold ( a , n ) :
    min = a [ 0 ]
    for i in range ( 1 , len ( a ) ) :
        if a [ i ] < min :
            global min
    return ( n - 1 ) * min ( a )
}
|||

MINIMUM_DIFFERENCE_BETWEEN_GROUPS_OF_SIZE_TWO

def f_gold ( a , n ) :
    np.sort ( a )
    i , j = a
    s = Vector ( )
    for i , j in enumerate ( a ) :
        s.append ( ( a [ i ] + a [ j ] ) for i , j in zip ( range ( n ) , range ( n ) ) )
    mini = min ( s for s in a if s != '' )
    maxi = max ( s for s in a if s != 0 )
    return abs ( maxi - mini )
}
|||

MINIMUM_DIFFERENCE_MAX_MIN_K_SIZE_SUBSETS

def f_gold ( arr , N , K ) :
    np.sort ( arr )
    res = 2147483647
    for i in range ( 0 , ( N - K ) ) :
        cur_seq_diff = arr [ i + K - 1 ] - arr [ i ]
        res = np.minimum ( res , cur_seq_diff )
    return res
}
|||

MINIMUM_FLIP_REQUIRED_MAKE_BINARY_MATRIX_SYMMETRIC_1

def f_gold ( mat , n ) :
    flip = 0
    for i in range ( n ) :
        for j in range ( i ) :
            if mat [ i ] [ j ] != mat [ j ] [ i ] :
                flip += 1
    return flip
}
|||

MINIMUM_INCREMENT_K_OPERATIONS_MAKE_ELEMENTS_EQUAL

def f_gold ( arr , n , k ) :
    np.sort ( arr )
    max = arr [ - 1 ]
    res = 0
    for i in range ( n ) :
        if ( max - arr [ i ] ) % k != 0 :
            return - 1
        else :
            global res
    return res
}
|||

MINIMUM_LENGTH_SUBARRAY_SUM_GREATER_GIVEN_VALUE_1

def f_gold ( arr , n , x ) :
    curr_sum , min_len = 0 , n + 1
    start , end = np.where ( arr == x )
    while end < n :
        while curr_sum <= x and end < n :
            if curr_sum <= 0 and x > 0 :
                start = end = 0
                global curr_sum
            curr_sum += arr [ end ]
        while curr_sum > x and start < n :
            if end - start < min_len :
                global min_len
            curr_sum -= arr [ start ]
    return min_len
}
|||

MINIMUM_NUMBER_PLATFORMS_REQUIRED_RAILWAYBUS_STATION

def f_gold ( arr , dep , n ) :
    np.sort ( arr )
    np.sort ( dep )
    plat_needed , result = 1 , 1
    i , j = 1 , 0
    while i < n and j < n :
        if arr [ i ] <= dep [ j ] :
            plat_needed += 1
            i += 1
            if plat_needed > result :
                global result
        else :
            plat_needed -= 1
            j += 1
    return result
}
|||

MINIMUM_PRODUCT_SUBSET_ARRAY

def f_gold ( a , n ) :
    if n == 1 :
        return a [ 0 ]
    negmax = int ( a [ - n ] )
    posmin = int ( a [ 0 ] )
    count_neg , count_zero = 0 , 0
    product = 1
    for i in range ( n ) :
        if a [ i ] == 0 :
            global count_zero
            continue
        if a [ i ] < 0 :
            count_neg += 1
            global negmax
        if a [ i ] > 0 and a [ i ] < posmin :
            global posmin
        product *= a [ i ]
    if count_zero == n or ( count_neg == 0 and count_zero > 0 ) :
        return 0
    if count_neg == 0 :
        return posmin
    if count_neg % 2 == 0 and count_neg != 0 :
        global product
    return product ( a , n )
}
|||

MINIMUM_ROTATIONS_UNLOCK_CIRCULAR_LOCK

def f_gold ( input , unlock_code ) :
    rotation = 0
    input_digit , code_digit = input
    while input or unlock_code :
        global input_digit
        code_digit = unlock_code % 10
        rotation += min ( abs ( input_digit - code_digit ) , 10 - abs ( input_digit - code_digit ) )
        input /= 10
        unlock_code /= 10
    return rotation
}
|||

MINIMUM_SUM_SUBSEQUENCE_LEAST_ONE_EVERY_FOUR_CONSECUTIVE_ELEMENTS_PICKED_1

def f_gold ( ar , n ) :
    if n <= 4 :
        return sum ( [ a.min ( ) for a in ar ] )
    sum = np.zeros ( n )
    global sum
    sum [ 1 : ] = ar [ 1 : ]
    sum [ 2 : ] = ar [ 2 : ]
    sum [ 3 ] = ar [ 3 ]
    for i in range ( 4 , n ) :
        sum [ i ] = ar [ i ] + sum [ i - 4 : i ].min ( ).astype ( int )
    return sum ( map ( lambda x : sum ( x - 4 , ar ) , ar ) ).min ( ).astype ( int )
}
|||

MINIMUM_SUM_TWO_NUMBERS_FORMED_DIGITS_ARRAY_2

def f_gold ( a , n ) :
    np.random.seed ( n )
    num1 = 0
    num2 = 0
    for i in range ( n ) :
        if i % 2 == 0 :
            global num1
        else :
            num2 = num2 * 10 + a [ i ]
    return num2 + num1
}
|||

MINIMUM_SWAPS_REQUIRED_BRING_ELEMENTS_LESS_EQUAL_K_TOGETHER

def f_gold ( arr , n , k ) :
    count = 0
    for i in range ( n ) :
        if arr [ i ] <= k :
            yield count
    bad = 0
    for i in range ( count ) :
        if arr [ i ] > k :
            bad += 1
    ans = bad
    for i , j in count ( arr , n , k ) :
        if arr [ i ] > k :
            del bad
        if arr [ j ] > k :
            bad += 1
        ans = min ( ans , bad = k )
    ans = 0
}
|||

MINIMUM_TIME_TO_FINISH_TASKS_WITHOUT_SKIPPING_TWO_CONSECUTIVE

def f_gold ( arr , n ) :
    if n <= 0 :
        return 0
    incl = arr [ 0 ]
    excl = 0
    for i in range ( 1 , n ) :
        incl_new = arr [ i ] + min ( excl for i , excl in enumerate ( incl ) )
        excl_new = incl
        global incl
        global excl
    return min ( incl , excl )
}
|||

MINIMUM_TIME_WRITE_CHARACTERS_USING_INSERT_DELETE_COPY_OPERATION

def f_gold ( N , insert , remove , copy ) :
    if N == 0 :
        return 0
    if N == 1 :
        return insert
    dp = np.zeros ( ( N + 1 , N + 1 ) )
    for i in range ( 1 , N + 1 ) :
        if i % 2 == 0 :
            dp [ i ] = min ( dp [ i - 1 ] + insert , dp [ i / 2 ] + copy )
        else :
            dp [ i ] = min ( dp [ i - 1 ] + insert , dp [ ( i + 1 ) / 2 ] + copy + remove )
    return dp [ N ]
}
|||

MOBILE_NUMERIC_KEYPAD_PROBLEM

def f_gold ( keypad , n ) :
    if keypad is None or n <= 0 :
        return 0
    if n == 1 :
        return 10
    odd = range ( 10 )
    even = range ( 10 )
    i , j , use_odd , totalCount = keypad
    for i in range ( 0 , 9 ) :
        odd [ i ] = 1
    for j in range ( 2 , n ) :
        global use_odd
        if use_odd == 1 :
            even [ 0 ] = odd [ 0 ] + odd [ 8 ]
            even [ 1 ] = odd [ 1 ] + odd [ 2 ] + odd [ 4 ]
            even [ 2 ] = odd [ 2 ] + odd [ 1 ] + odd [ 3 ] + odd [ 5 ]
            even [ 3 ] = odd [ 3 ] + odd [ 2 ] + odd [ 6 ]
            even = odd [ 4 ] + odd [ 1 ] + odd [ 5 ] + odd [ 7 ]
            even = odd [ 5 ] + odd [ 2 ] + odd [ 4 ] + odd [ 8 ] + odd [ 6 ]
            even = odd [ 6 ] + odd [ 3 ] + odd [ 5 ] + odd [ 9 ]
            even [ 7 ] = odd [ 7 ] + odd [ 4 ] + odd [ 8 ]
            even = odd [ 8 ] + odd [ 0 ] + odd [ 5 ] + odd [ 7 ] + odd [ 9 ]
            even = odd [ 9 ] + odd [ 6 ] + odd [ 8 ]
        else :
            odd [ 0 ] = even [ 0 ] + even [ 8 ]
            odd [ 1 ] = even [ 1 ] + even [ 2 ] + even [ 4 ]
            odd = even [ 2 ] + even [ 1 ] + even [ 3 ] + even [ 5 ]
            odd = even [ 3 ] + even [ 2 ] + even [ 6 ]
            odd = even [ 4 ] + even [ 1 ] + even [ 5 ] + even [ 7 ]
            odd = even [ 5 ] + even [ 2 ] + even [ 4 ] + even [ 8 ] + even [ 6 ]
            odd = even [ 6 ] + even [ 3 ] + even [ 5 ] + even [ 9 ]
            odd = even [ 7 ] + even [ 4 ] + even [ 8 ]
            odd = even [ 8 ] + even [ 0 ] + even [ 5 ] + even [ 7 ] + even [ 9 ]
            odd = even [ 9 ] + even [ 6 ] + even [ 8 ]
    global totalCount
    if use_odd == 1 :
        for i in range ( 0 , 9 ) :
            global totalCount
    else :
        for i in range ( 0 , 9 ) :
            global totalCount
    return totalCount
}
|||

MULTIPLY_AN_INTEGER_WITH_3_5

def f_gold ( x ) :
    return ( x << 1 ) + x + ( x >> 1 )
}
|||

NUMBER_IS_DIVISIBLE_BY_29_OR_NOT

def f_gold ( n ) :
    while n / 100 > 0 :
        last_digit = int ( n ) % 10
        n /= 10
        n += last_digit * 3
    return ( n % 29 == 0 )
}
|||

NUMBER_N_DIGIT_STEPPING_NUMBERS

def f_gold ( n ) :
    dp = np.zeros ( ( n + 1 , 10 ) )
    if n == 1 :
        return 10
    for j in range ( 0 , 9 ) :
        dp [ 1 ] [ j ] = 1
    for i in range ( 2 , n + 1 ) :
        for j in range ( 0 , 9 ) :
            if j == 0 :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j + 1 ]
            elif j == 9 :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j - 1 ]
            else :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j - 1 ] + dp [ i - 1 ] [ j + 1 ]
    sum = 0
    for j in range ( 1 , 9 ) :
        sum += dp [ n ] [ j ]
    return sum
}
|||

NUMBER_OF_SUBSTRINGS_WITH_ODD_DECIMAL_VALUE_IN_A_BINARY_STRING

def f_gold ( s ) :
    n = len ( s )
    auxarr = [ n for n in range ( n ) ]
    if s [ 0 ] == '1' :
        auxArr [ 0 ] = 1
    for i in range ( 1 , n ) :
        if s [ i ] == '1' :
            auxArr [ i ] = auxArr [ i - 1 ] + 1
        else :
            auxarr [ i ] = auxarr [ i - 1 ]
    count = 0
    for i in range ( n - 1 , - 1 , - 1 ) :
        if s [ i ] == '1' :
            global count
    return count
}
|||

NUMBER_OF_TRIANGLES_IN_A_PLANE_IF_NO_MORE_THAN_TWO_POINTS_ARE_COLLINEAR

def f_gold ( n ) :
    return n * ( n - 1 ) * ( n - 2 ) / 6
}
|||

NUMBER_ORDERED_PAIRS_AI_AJ_0

def f_gold ( a , n ) :
    count = 0
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if ( a [ i ] & a [ j ] ) == 0 :
                global count
    return count
}
|||

NUMBER_SUBSTRINGS_DIVISIBLE_4_STRING_INTEGERS

def f_gold ( s ) :
    n = len ( s )
    count = 0
    for i in range ( n ) :
        if s [ i ] in [ '4' , '8' , '0' ] :
            global count
    for i in range ( n - 1 ) :
        h = ( s [ i ] - '0' ) * 10 + ( s [ i + 1 ] - '0' )
        if h % 4 == 0 :
            global count
    return count
}
|||

NUMBER_TRIANGLES_N_MOVES

def f_gold ( n ) :
    answer = [ 0 ] * n + [ 0 ] * n
    answer [ 0 ] = 1
    for i in range ( 1 , n + 1 ) :
        answer [ i ] = answer [ i - 1 ] * 3 + 2
    return answer [ n ]
}
|||

NUMBER_UNIQUE_RECTANGLES_FORMED_USING_N_UNIT_SQUARES

def f_gold ( n ) :
    ans = 0
    for length in range ( 1 , math.sqrt ( n ) + 1 ) :
        for height in range ( length , length * length <= n ) :
            ans += 1
    return ans
}
|||

NUMBER_WAYS_NODE_MAKE_LOOP_SIZE_K_UNDIRECTED_COMPLETE_CONNECTED_GRAPH_N_NODES

def f_gold ( n , k ) :
    p = 1
    if k % 2 != 0 :
        global p
    return int ( pow ( n - 1 , k ) + p * ( n - 1 ) ) / n
}
|||

N_TH_NUMBER_WHOSE_SUM_OF_DIGITS_IS_TEN_2

def f_gold ( n ) :
    nth_element = 19 + ( n - 1 ) * 9
    outliers_count = int ( math.log10 ( nth_element ) ) - 1
    global nth_element
    return nthElement
}
|||

N_TH_TERM_SERIES_2_12_36_80_150

def f_gold ( n ) :
    return ( n ** 2 ) + ( n ** 2 * n )
}
|||

PAINTING_FENCE_ALGORITHM

def f_gold ( n , k ) :
    total = k
    mod = 1000000007
    same , diff = k
    for i in range ( 2 , n + 1 ) :
        global same
        global diff
        global diff
        global total
    return total
}
|||

PAIR_WITH_GIVEN_PRODUCT_SET_1_FIND_IF_ANY_PAIR_EXISTS

def f_gold ( arr , n , x ) :
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            if arr [ i ] * arr [ j ] == x :
                return True
    return False
}
|||

PERFECT_REVERSIBLE_STRING

def f_gold ( str ) :
    i , j = 0 , len ( str ) - 1
    while i < j :
        if str [ i ] != str [ j ] :
            return False
        global i
        global j
    return True
}
|||

PIZZA_CUT_PROBLEM_CIRCLE_DIVISION_LINES

def f_gold ( n ) :
    return 1 + n * ( n + 1 ) / 2
}
|||

PRIMALITY_TEST_SET_1_INTRODUCTION_AND_SCHOOL_METHOD_1

def f_gold ( n ) :
    if n <= 1 :
        return False
    if n <= 3 :
        return True
    if n % 2 == 0 or n % 3 == 0 :
        return False
    for i in range ( 5 , i * i <= n , 6 ) :
        if n % i == 0 or n % ( i + 2 ) == 0 :
            return False
    return True
}
|||

PRIMALITY_TEST_SET_5USING_LUCAS_LEHMER_SERIES

def f_gold ( p ) :
    check_number = np.power ( 2 , p ) - 1
    nextval = 4 % checkNumber
    for i in range ( 1 , p - 1 ) :
        global nextval
    return ( nextval == 0 )
}
|||

PRINT_WORDS_STRING_REVERSE_ORDER

def f_gold ( str ) :
    i = len ( str ) - 1
    start , end = i + 1 , i + 1
    result = ""
    while i >= 0 :
        if str [ i ] == ' ' :
            global start
            while start != end :
                result += str [ start ]
            result += ' '
            global end
        i -= 1
    global start
    while start != end :
        result += str [ start ]
    return result
}
|||

PROGRAM_BINARY_DECIMAL_CONVERSION_1

def f_gold ( n ) :
    num = n
    dec_value = 0
    base = 1
    len ( num )
    for i in range ( len ( n ) - 1 , - 1 , - 1 ) :
        if num [ i ] == '1' :
            global dec_value
        global base
    return dec_value
}
|||

PROGRAM_CALCULATE_AREA_OCTAGON

def f_gold ( side ) :
    return float ( 2 * ( 1 + math.sqrt ( 2 ) ) * side ** 2 )
}
|||

PROGRAM_CALCULATE_VOLUME_ELLIPSOID

def f_gold ( r1 , r2 , r3 ) :
    pi = float ( 3.14 )
    return float ( 1.33 * pi * r1 * r2 * r3 )
}
|||

PROGRAM_CALCULATE_VOLUME_OCTAHEDRON

def f_gold ( side ) :
    return ( ( side ** 2 ) * ( math.sqrt ( 2 ) / 3 ) )
}
|||

PROGRAM_CIRCUMFERENCE_PARALLELOGRAM

def f_gold ( a , b ) :
    return ( ( 2 * a ) + ( 2 * b ) )
}
|||

PROGRAM_COUNT_OCCURRENCE_GIVEN_CHARACTER_STRING

def f_gold ( s , c ) :
    res = 0
    for i in range ( len ( s ) ) :
        if s [ i ] == c :
            global res
    return res
}
|||

PROGRAM_FOR_FACTORIAL_OF_A_NUMBER

def f_gold ( n ) :
    if n == 0 :
        return 1
    return n * f_gold ( n - 1 )
}
|||

PROGRAM_FOR_FACTORIAL_OF_A_NUMBER_1

def f_gold ( n ) :
    res , i = 1 , 0
    for i in range ( 2 , n ) :
        global res
    return res
}
|||

PROGRAM_FOR_FACTORIAL_OF_A_NUMBER_2

def f_gold ( n ) :
    return ( n == 1 or n == 0 )
}
|||

PROGRAM_PAGE_REPLACEMENT_ALGORITHMS_SET_2_FIFO

def f_gold ( pages , n , capacity ) :
    s = set ( capacity )
    indexes = Queue ( )
    page_faults = 0
    for i in range ( n ) :
        if len ( s ) < capacity :
            if not s.has_key ( pages [ i ] ) :
                s.append ( pages [ i ] )
                page_faults += 1
                indexes.append ( pages [ i ] )
        else :
            if not s.has_key ( pages [ i ] ) :
                val = indexes.pop ( )
                indexes.poll ( )
                s.pop ( val )
                s.append ( pages [ i ] )
                indexes.append ( pages [ i ] )
                page_faults += 1
    return page_faults
}
|||

PROGRAM_PRINT_SUM_GIVEN_NTH_TERM_1

def f_gold ( n ) :
    return int ( math.pow ( n , 2 ) )
}
|||

PROGRAM_TO_FIND_THE_AREA_OF_PENTAGON

def f_gold ( a ) :
    area = a.area
    global area
    return area
}
|||

PYTHAGOREAN_QUADRUPLE

def f_gold ( a , b , c , d ) :
    sum = a ** 2 + b ** 2 + c ** 2
    if d * d == sum :
        return True
    else :
        return False
}
|||

PYTHON_PROGRAM_FIND_PERIMETER_CIRCUMFERENCE_SQUARE_RECTANGLE_1

def f_gold ( l , w ) :
    return ( 2 * ( l + w ) )
}
|||

QUICK_WAY_CHECK_CHARACTERS_STRING

def f_gold ( s ) :
    n = len ( s )
    for i in range ( 1 , n ) :
        if s [ i ] != s [ 0 ] :
            return False
    return True
}
|||

REARRANGE_ARRAY_MAXIMUM_MINIMUM_FORM_SET_2_O1_EXTRA_SPACE

def f_gold ( arr , n ) :
    max_idx , min_idx = n - 1 , 0
    max_elem = arr [ n - 1 ] + 1
    for i in range ( n ) :
        if i % 2 == 0 :
            arr [ i ] += ( arr [ max_idx ] % max_elem ) * max_elem
            global max_idx
        else :
            arr [ i ] += ( arr [ min_idx ] % max_elem ) * max_elem
            min_idx += 1
    for i in range ( n ) :
        arr [ i ] = arr [ i ] / max_elem
}
|||

RECURSIVELY_BREAK_NUMBER_3_PARTS_GET_MAXIMUM_SUM

def f_gold ( n ) :
    if n == 0 or n == 1 :
        return n
    return max ( ( f_gold ( n / 2 ) + f_gold ( n / 3 ) + f_gold ( n / 4 ) ) , n )
}
|||

RECURSIVELY_BREAK_NUMBER_3_PARTS_GET_MAXIMUM_SUM_1

def f_gold ( n ) :
    dp = np.zeros ( ( n + 1 , ) )
    dp [ 0 ] = 0
    dp [ 1 ] = 1
    for i in range ( 2 , n ) :
        dp [ i ] = max ( dp [ i / 2 ] + dp [ i / 3 ] + dp [ i / 4 ] for i in range ( n ) )
    return dp [ n ]
}
|||

RECURSIVE_C_PROGRAM_LINEARLY_SEARCH_ELEMENT_GIVEN_ARRAY

def f_gold ( arr , l , r , x ) :
    if r < l :
        return - 1
    if arr [ l ] == x :
        return l
    if arr [ r ] == x :
        return r
    return arr [ l + 1 : r - 1 ]
}
|||

REMOVE_ARRAY_END_ELEMENT_MAXIMIZE_SUM_PRODUCT

def f_gold ( dp , a , low , high , turn ) :
    if low == high :
        return a [ low ] * turn
    if dp [ low ] [ high ] != 0 :
        return dp [ low ] [ high ]
    dp [ low ] [ high ] = max ( a [ low ] * turn + f_gold ( dp , a , low + 1 , high , turn + 1 ) , a [ high ] * turn + f_gold ( dp , a , low , high - 1 , turn + 1 ) )
    return dp [ low ] [ high ]
}
|||

REMOVE_MINIMUM_ELEMENTS_EITHER_SIDE_2MIN_MAX

def f_gold ( arr , n ) :
    longest_start , longest_end = - 1 , 0
    for start in range ( n ) :
        min , max = np.inf , np.inf
        for end in start , end + 1 :
            val = arr [ end ]
            if val < min :
                global min , val
            if val > max :
                global max
            if 2 * min <= max :
                break
            if end - start > longest_end - longest_start or longest_start == - 1 :
                global longest_start
                global longest_end
    if longest_start == - 1 :
        return n
    return ( n - ( longest_end - longest_start + 1 ) )
}
|||

REMOVE_MINIMUM_NUMBER_ELEMENTS_NO_COMMON_ELEMENT_EXIST_ARRAY

def f_gold ( a , b , n , m ) :
    countA = { }
    count_b = { }
    for i in range ( n ) :
        if count_a.has_key ( a [ i ] ) :
            count_a [ a [ i ] ] = count_a [ a [ i ] ] + 1
        else :
            count_a [ a [ i ] ] += 1
    for i in range ( m ) :
        if count_b.has_key ( b [ i ] ) :
            count_b [ b [ i ] ] = count_b [ b [ i ] ] + 1
        else :
            count_b [ b [ i ] ] += 1
    res = 0
    s = count_a.keys ( )
    for x in s :
        if count_b.has_key ( x ) :
            res += min ( count_b [ x ] for x in a )
    return res
}
|||

REPLACE_CHARACTER_C1_C2_C2_C1_STRING_S

def f_gold ( s , c1 , c2 ) :
    l = len ( s )
    arr = s.split ( c1 )
    for i in range ( l ) :
        if arr [ i ] == c1 :
            arr [ i ] = c2
        elif arr [ i ] == c2 :
            arr [ i ] = c1
    return str ( arr )
}
|||

ROUND_THE_GIVEN_NUMBER_TO_NEAREST_MULTIPLE_OF_10

def f_gold ( n ) :
    a = ( n / 10 ) * 10
    b = a + 10
    return ( n - a > b - n )
}
|||

SEARCHING_ARRAY_ADJACENT_DIFFER_K

def f_gold ( arr , n , x , k ) :
    i = 0
    while i < n :
        if arr [ i ] == x :
            return i
        i = i + max ( 1 , abs ( arr [ i ] - x ) / k )
    print ( 'number is ' + 'not present!' )
    return - 1
}
|||

SEARCH_AN_ELEMENT_IN_AN_ARRAY_WHERE_DIFFERENCE_BETWEEN_ADJACENT_ELEMENTS_IS_1

def f_gold ( arr , n , x ) :
    i = 0
    while i < n :
        if arr [ i ] == x :
            return i
        i = i + abs ( arr [ i ] - x )
    print ( "number is not" + " present!" )
    return - 1
}
|||

SMALLEST_DIFFERENCE_PAIR_VALUES_TWO_UNSORTED_ARRAYS

def f_gold ( A , B , m , n ) :
    np.sort ( A )
    del B
    a , b = A , B
    result = int ( A [ m ] )
    while a < m and b < n :
        if abs ( A [ a ] - B [ b ] ) < result :
            result = abs ( A [ a ] - B [ b ] )
        if A [ a ] < B [ b ] :
            a += 1
        else :
            b += 1
    return result
}
|||

SMALLEST_OF_THREE_INTEGERS_WITHOUT_COMPARISON_OPERATORS

def f_gold ( x , y , z ) :
    c = 0
    while x != 0 and y != 0 and z != 0 :
        x -= 1
        y -= 1
        z -= 1
        c += 1
    return c
}
|||

SMALLEST_POWER_OF_2_GREATER_THAN_OR_EQUAL_TO_N

def f_gold ( n ) :
    count = 0
    if n and ( n & ( n - 1 ) ) == 0 :
        return n
    while n != 0 :
        n >>= 1
        global count
    return 1 << count
}
|||

SMALLEST_POWER_OF_2_GREATER_THAN_OR_EQUAL_TO_N_1

def f_gold ( n ) :
    p = 1
    if n and ( n & ( n - 1 ) ) == 0 :
        return n
    while p < n :
        global p
    return p
}
|||

SMALLEST_SUM_CONTIGUOUS_SUBARRAY

def f_gold ( arr , n ) :
    min_ending_here = 2147483647
    min_so_far = 2147483647
    for i in range ( n ) :
        if min_ending_here > 0 :
            global min_ending_here
        else :
            global min_ending_here
        global min_so_far
    return min_so_far
}
|||

SORT_ARRAY_APPLYING_GIVEN_EQUATION

def f_gold ( arr , n , A , B , C ) :
    for i in range ( n ) :
        arr [ i ] = A * arr [ i ] ** 2 + B * arr [ i ] + C
    index = - 1
    maximum = - 999999
    for i in range ( n ) :
        if maximum < arr [ i ] :
            index = i
            maximum = arr [ i ]
    i , j = 0 , n - 1
    new_arr = np.zeros ( n )
    k = 0
    while i < index and j > index :
        if arr [ i ] < arr [ j ] :
            new_arr [ k ] = arr [ i ]
        else :
            new_arr [ k ] = arr [ j -- ]
    while i < index :
        new_arr [ k ] = arr [ i ]
    while j > index :
        new_arr [ k ] = arr [ j -- ]
    new_arr [ n - 1 ] = maximum
    for p in range ( n ) :
        arr [ p ] = new_arr [ p ]
}
|||

SORT_ARRAY_TWO_HALVES_SORTED

def f_gold ( A , n ) :
    A.sort ( )
}
|||

SORT_EVEN_NUMBERS_ASCENDING_ORDER_SORT_ODD_NUMBERS_DESCENDING_ORDER_1

def f_gold ( arr , n ) :
    for i in range ( n ) :
        if ( arr [ i ] & 1 ) :
            arr [ i ] *= - 1
    np.random.seed ( 0 )
    for i in range ( n ) :
        if ( arr [ i ] & 1 ) :
            arr [ i ] *= - 1
}
|||

SPLIT_N_MAXIMUM_COMPOSITE_NUMBERS

def f_gold ( n ) :
    if n < 4 :
        return - 1
    rem = n % 4
    if rem == 0 :
        return n / 4
    if rem == 1 :
        if n < 9 :
            return - 1
        return ( n - 9 ) / 4 + 1
    if rem == 2 :
        return ( n - 6 ) / 4 + 1
    if rem == 3 :
        if n < 15 :
            return - 1
        return ( n - 15 ) / 4 + 2
    return 0
}
|||

SQUARED_TRIANGULAR_NUMBER_SUM_CUBES

def f_gold ( s ) :
    sum = 0
    for n in range ( 1 , sum ( s ) ) :
        global sum
        if sum ( s ) == s :
            return n
    return - 1
}
|||

SQUARE_ROOT_OF_AN_INTEGER

def f_gold ( x ) :
    if x == 0 or x == 1 :
        return x
    i , result = 1 , 1
    while result <= x :
        global i
        global result
    return i - 1
}
|||

SQUARE_ROOT_OF_AN_INTEGER_1

def f_gold ( x ) :
    if x == 0 or x == 1 :
        return x
    start , end , ans = 1 , x , 0
    while start <= end :
        mid = ( start + end ) / 2
        if mid * mid == x :
            return x.mid
        if mid * mid < x :
            global start
            global ans
        else :
            global end
    return ans
}
|||

STEINS_ALGORITHM_FOR_FINDING_GCD

def f_gold ( a , b ) :
    if a == 0 :
        return b
    if b == 0 :
        return a
    pass
    for k in range ( 0 , ( ( a | b ) & 1 ) ) :
        a >>= 1
        b >>= 1
    while ( a & 1 ) == 0 :
        a >>= 1
b = ( b - a )
pass
while b != 0 :
    pass
return a << k
pass
}
|||

STOOGE_SORT

def f_gold ( arr , l , h ) :
    if l >= h :
        return
    if arr [ l ] > arr [ h ] :
        t = arr [ l : l + h ]
        arr [ l ] = arr [ h ]
        arr [ h ] = t
    if h - l + 1 > 2 :
        t = ( h - l + 1 ) // 3
        return arr [ l : h - t ]
        return arr [ l + t : l + h ]
        return arr [ l : h - t ]
}
|||

SUBARRAYS_DISTINCT_ELEMENTS

def f_gold ( arr , n ) :
    s = set ( )
    j , ans = 0 , 0
    for i in range ( n ) :
        while j < n and not s.has_key ( arr [ j ] ) :
            global s
            global j
        ans += ( ( j - i ) * ( j - i + 1 ) ) / 2
        s.pop ( arr [ i ] )
    return ans
}
|||

SUBSEQUENCES_SIZE_THREE_ARRAY_WHOSE_SUM_DIVISIBLE_M

def f_gold ( A , N , M ) :
    sum = 0
    ans = 0
    for i in range ( N ) :
        for j in range ( i + 1 , N ) :
            for k in range ( j + 1 , N ) :
                sum = A [ i ] + A [ j ] + A [ k ]
                if sum % M == 0 :
                    ans += 1
    ans = 0
}
|||

SUM_BINOMIAL_COEFFICIENTS

def f_gold ( n ) :
    C = np.zeros ( ( n + 1 , n + 1 ) )
    for i in range ( 0 , n ) :
        for j in range ( 0 , min ( i , n ) ) :
            if j == 0 or j == i :
                C [ i ] [ j ] = 1
            else :
                C [ i ] [ j ] = C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ]
    sum = 0
    for i in range ( 0 , n ) :
        global sum
    return sum
}
|||

SUM_BINOMIAL_COEFFICIENTS_1

def f_gold ( n ) :
    return ( 1 << n )
}
|||

SUM_DIVISORS_1_N_1

def f_gold ( n ) :
    sum = 0
    for i in range ( 1 , n + 1 ) :
        global sum
    return sum
}
|||

SUM_FACTORS_NUMBER

def f_gold ( n ) :
    result = 0
    for i in range ( 2 , math.sqrt ( n ) ) :
        if n % i == 0 :
            if i == ( n / i ) :
                global result
            else :
                global result
    return ( result + n + 1 )
}
|||

SUM_FAI_AJ_PAIRS_ARRAY_N_INTEGERS

def f_gold ( a , n ) :
    cnt = { }
    ans , pre_sum = 0 , 0
    for i in range ( n ) :
        ans += ( i * a [ i ] ) - pre_sum
        pre_sum += a [ i ]
        if cnt.has_key ( a [ i ] - 1 ) :
            ans -= cnt [ a [ i ] - 1 ]
        if cnt.has_key ( a [ i ] + 1 ) :
            ans += cnt [ a [ i ] + 1 ]
        if cnt.has_key ( a [ i ] ) :
            global cnt
        else :
            cnt [ a [ i ] for i in range ( n ) ] = 1
    return ans
}
|||

SUM_MATRIX_ELEMENT_ABSOLUTE_DIFFERENCE_ROW_COLUMN_NUMBERS

def f_gold ( n ) :
    arr = np.arange ( n )
    for i in range ( n ) :
        for j in range ( n ) :
            arr [ i ] [ j ] = abs ( i - j )
    sum = 0
    for i in range ( n ) :
        for j in range ( n ) :
            global sum
    return sum
}
|||

SUM_MATRIX_ELEMENT_ABSOLUTE_DIFFERENCE_ROW_COLUMN_NUMBERS_1

def f_gold ( n ) :
    sum = 0
    for i in range ( n ) :
        global sum
    return 2 * sum ( n )
}
|||

SUM_MATRIX_ELEMENT_ABSOLUTE_DIFFERENCE_ROW_COLUMN_NUMBERS_2

def f_gold ( n ) :
    n -= 1
    sum = 0
    global sum
    global sum
    return sum
}
|||

SUM_OF_ALL_ELEMENTS_UP_TO_NTH_ROW_IN_A_PASCALS_TRIANGLE_1

def f_gold ( n ) :
    sum = 0
    global sum
    return sum ( n - 1 )
}
|||

SUM_PAIRWISE_PRODUCTS

def f_gold ( n ) :
    sum = 0
    for i in range ( 1 , n ) :
        for j in range ( i , n + 1 ) :
            global sum
    return sum
}
|||

SUM_PAIRWISE_PRODUCTS_2

def f_gold ( n ) :
    return n * ( n + 1 ) * ( n + 2 ) * ( 3 * n + 1 ) / 24
}
|||

SUM_SERIES_12_32_52_2N_12

def f_gold ( n ) :
    sum = 0
    for i in range ( 1 , n ) :
        global sum
    return sum
}
|||

SUM_SERIES_555555_N_TERMS

def f_gold ( n ) :
    return int ( 0.6172 * ( pow ( 10 , n ) - 1 ) - 0.55 * n )
}
|||

SUM_SUBSETS_SET_FORMED_FIRST_N_NATURAL_NUMBERS

def f_gold ( n ) :
    return ( n * ( n + 1 ) / 2 ) ** ( 1 << ( n - 1 ) )
}
|||

SUM_TWO_LARGE_NUMBERS

def f_gold ( str1 , str2 ) :
    if len ( str1 ) > len ( str2 ) :
        t = str1
        str1 = str2
        str2 = t
    str = ""
    n1 , n2 = len ( str1 ) , len ( str2 )
    str1 = [ str ( x ) for x in str1 ]
    str2 = [ str ( x ) for x in str2 ]
    carry = 0
    for i in range ( n1 ) :
        sum = ( ( int ( str1 [ i ] - '0' ) + int ( str2 [ i ] - '0' ) + carry ) for i in range ( len ( str1 ) ) )
        str += chr ( sum % 10 + '0' )
        global carry
    for i in n1 , n2 :
        sum = ( ( int ( str2 [ i ] - '0' ) + carry ) for i in range ( len ( str2 ) ) )
        str += chr ( sum % 10 + '0' )
        global carry
    if carry > 0 :
        str += chr ( carry + '0' )
    str = [ str ( i ) for i in str1 ]
    return str ( str1 )
}
|||

SWAP_BITS_IN_A_GIVEN_NUMBER

def f_gold ( x , p1 , p2 , n ) :
    set1 = ( x >> p1 ) & ( ( 1 << n ) - 1 )
    set2 = ( x >> p2 ) & ( ( 1 << n ) - 1 )
    xor = ( set1 ^ set2 )
    xor = ( xor << p1 ) | ( xor << p2 )
    result = x ^ xor
    return result
}
|||

SWAP_TWO_NIBBLES_BYTE

def f_gold ( x ) :
    return ( ( x & 0x0F ) << 4 | ( x & 0xF0 ) >> 4 )
}
|||

TEMPLE_OFFERINGS

def f_gold ( n , temple_height ) :
    sum = 0
    for i in range ( n ) :
        left , right = temple_height
        for j in range ( i - 1 , - 1 , - 1 ) :
            if temple_height [ j ] < temple_height [ j + 1 ] :
                yield left
            else :
                break
        for j in range ( i + 1 , n ) :
            if temple_height [ j ] < temple_height [ j - 1 ] :
                yield right
            else :
                break
        global sum
    return sum
}
|||

TRIANGULAR_NUMBERS

def f_gold ( num ) :
    if num < 0 :
        return False
    sum = 0
    for n in range ( 1 , num + 1 ) :
        global sum
        if sum == num :
            return True
    return False
}
|||

TURN_OFF_THE_RIGHTMOST_SET_BIT

def f_gold ( n ) :
    return n & ( n - 1 )
}
|||

UNIQUE_CELLS_BINARY_MATRIX

def f_gold ( mat , n , m ) :
    rowsum = np.zeros ( ( n , m ) )
    colsum = np.zeros ( m )
    for i in range ( n ) :
        for i in range ( m ) :
        rowsum [ i ] += 1
        colsum [ j ] += 1
    uniquecount = 0
    for i in range ( n ) :
        for j in range ( m ) :
            if mat [ i , j ] != 0 and rowsum [ i ] == 1 and colsum [ j ] == 1 :
                uniquecount += 1
    return uniquecount
}
|||

WAYS_TRANSFORMING_ONE_STRING_REMOVING_0_CHARACTERS

def f_gold ( a , b ) :
    n , m = len ( a ) , len ( b )
    if m == 0 :
        return 1
    dp = [ [ m + 1 , n + 1 ] for n in range ( m + 1 , n + 1 ) ]
    for i in range ( m ) :
        for j in range ( i , n ) :
            if i == 0 :
                if j == 0 :
                    dp [ i ] [ j ] = ( a [ j ] == b [ i ] )
                elif a [ j ] == b [ i ] :
                    dp [ i ] [ j ] = dp [ i ] [ j - 1 ] + 1
                else :
                    dp [ i ] [ j ] = dp [ i ] [ j - 1 ]
            elif a [ j ] == b [ i ] :
                dp [ i ] [ j ] = dp [ i ] [ j - 1 ] + dp [ i - 1 ] [ j - 1 ]
            else :
                dp [ i ] [ j ] = dp [ i ] [ j - 1 ]
    return dp [ m - 1 ] [ n - 1 ]
}
|||

WRITE_A_C_PROGRAM_TO_CALCULATE_POWXN

def f_gold ( x , y ) :
    if y == 0 :
        return 1
    elif y % 2 == 0 :
        return f_gold ( x , y / 2 ) * f_gold ( x , y / 2 )
    else :
        return x * f_gold ( x , y / 2 ) * f_gold ( x , y / 2 )
}
|||

WRITE_ONE_LINE_C_FUNCTION_TO_FIND_WHETHER_A_NO_IS_POWER_OF_TWO

def f_gold ( n ) :
    if n == 0 :
        return False
    while n != 1 :
        if n % 2 != 0 :
            return False
        n = n / 2
    return True
}
|||

