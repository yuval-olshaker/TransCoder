MAXIMUM_NUMBER_CHARACTERS_TWO_CHARACTER_STRING

def maximum_chars ( str ) :
    n = len ( str )
    res = - 1
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            if str [ i ] == str [ j ] :
                res = max ( res , abs ( j - i - 1 ) )
    return res
|||

FIND_MIRROR_IMAGE_POINT_2_D_PLANE

def mirror_image ( a , b , c , x1 , y1 ) :
    temp = - 2 * ( a * x1 + b * y1 + c ) / ( a ** 2 + b ** 2 )
    x = temp * a + x1
    y = temp * b + y1
    return ( x , y )
|||

EFFICIENTLY_COMPUTE_SUMS_OF_DIAGONALS_OF_A_MATRIX

def printDiagonalSums ( mat , n ) :
    principal , secondary = 0 , 0
    for i in range ( n ) :
        for j in range ( n ) :
            if i == j :
                principal += mat [ i ] [ j ]
            if ( i + j ) == ( n - 1 ) :
                secondary += mat [ i ] [ j ]
    print ( "Principal Diagonal:" , principal )
    print ( "Secondary Diagonal:" , secondary )
|||

COUNTS_PATHS_POINT_REACH_ORIGIN

def countPaths ( n , m ) :
    if n == 0 or m == 0 :
        return 1
    return ( countPaths ( n - 1 , m ) + countPaths ( n , m - 1 ) )
|||

FIND_A_TRIPLET_THAT_SUM_TO_A_GIVEN_VALUE_1

def find3Numbers ( A , arr_size , sum ) :
    l , r = quickSort ( A , 0 , arr_size - 1 )
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
|||

CHECK_GIVEN_MATRIX_IS_MAGIC_SQUARE_OR_NOT

def isMagicSquare ( mat ) :
    sum , sum2 = 0 , 0
    for i in range ( N ) :
        sum = sum + mat [ i ] [ i ]
    for i in range ( N ) :
        sum2 = sum2 + mat [ i ] [ N - 1 - i ]
    if sum != sum2 :
        return False
    for i in range ( N ) :
        rowSum = 0
        for j in range ( N ) :
            rowSum += mat [ i ] [ j ]
        if rowSum != sum :
            return False
    for i in range ( N ) :
        colSum = 0
        for j in range ( N ) :
            colSum += mat [ j ] [ i ]
        if sum != colSum :
            return False
    return True
|||

SEQUENCES_GIVEN_LENGTH_EVERY_ELEMENT_EQUAL_TWICE_PREVIOUS_1

def getTotalNumberOfSequences ( m , n ) :
    T = [ 0 ] * ( m + 1 )
    for i in range ( m + 1 ) :
        for j in range ( n + 1 ) :
            if i == 0 or j == 0 :
                T [ i ] [ j ] = 0
            elif i < j :
                T [ i ] [ j ] = 0
            elif j == 1 :
                T [ i ] [ j ] = i
            else :
                T [ i ] [ j ] = T [ i - 1 ] [ j ] + T [ i / 2 ] [ j - 1 ]
    return T [ m ] [ n ]
|||

FIND_DIFFERENCE_BETWEEN_SUMS_OF_TWO_DIAGONALS_1

def difference ( arr , n ) :
    d1 , d2 = 0 , 0
    for i in range ( n ) :
        d1 += arr [ i ] [ i ]
        d2 += arr [ i ] [ n - i - 1 ]
    return abs ( d1 - d2 )
|||

MINIMUM_NUMBER_SUBSETS_DISTINCT_ELEMENTS

def subset ( ar , n ) :
    res = 0
    ar.sort ( )
    for i in range ( n ) :
        count = 1
        for _ in range ( n - 1 ) :
            if ar [ i ] == ar [ i + 1 ] :
                count += 1
            else :
                break
        res = max ( res , count )
    return res
|||

DECIMAL_BINARY_CONVERSION_WITHOUT_USING_ARITHMETIC_OPERATORS

def decToBin ( n ) :
    if n == 0 :
        return '0'
    bin = ''
    while n :
        bin = ( ( n & 1 ) == 0 and '0' or '1' ) + bin
        n >>= 1
    return bin
|||

FIND_NTH_TERM_DRAGON_CURVE_SEQUENCE

def Dragon_Curve_Sequence ( n ) :
    s = '1'
    for i in range ( 2 , n + 1 ) :
        temp = '1'
        prev , zero , one = '1' , '0' , '1'
        for c in s :
            temp += c
            if prev == '0' :
                temp += one
                prev = one
            else :
                temp += zero
                prev = zero
        s = temp
    return s
|||

STACK_SET_3_REVERSE_STRING_USING_STACK

def reverse ( str ) :
    n , i = len ( str ) , 0
    for i in range ( n // 2 ) :
        swap ( str [ i : i + 1 ] )
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
    arr = sorted ( arr , key = lambda x : ( x [ 0 ] , x [ 1 ] ) )
    arr = sorted ( arr , key = lambda x : ( x [ 0 ] , x [ 1 ] ) )
    low , high = ( n + 1 ) // 2 , n - 1
    while low < high :
        temp = arr [ low ]
        arr [ low ] , arr [ high ] = arr [ high ] , temp
        low += 1
        high -= 1
    return arr
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
    for i in range ( 1 , y + 1 ) :
        if n % i == 0 :
            if n / i > b :
                count += 1
            if i > b :
                count += 1
    if y * y == n and y > b :
        count -= 1
    print ( count )
|||

CHECK_CHARACTERS_GIVEN_STRING_CAN_REARRANGED_FORM_PALINDROME

def can_form_palindrome ( str ) :
    count = [ 0 ] * NO_OF_CHARS
    for c in str :
        count [ ord ( c ) ] += 1
    odd = 0
    for c in range ( NO_OF_CHARS ) :
        if ( count [ c ] & 1 ) == 1 :
            odd += 1
        if odd > 1 :
            return False
    return True
|||

MAXIMUM_TRIPLET_SUM_ARRAY_1

def max_triplet_sum ( arr , n ) :
    arr.sort ( )
    return arr [ n - 1 ] + arr [ n - 2 ] + arr [ n - 3 ]
|||

FIND_MEDIAN_ROW_WISE_SORTED_MATRIX

def binary_median ( m , r , c ) :
    max = int ( min ( m ) )
    min = int ( max )
    for i in range ( r ) :
        if m [ i ] [ 0 ] < min :
            min = m [ i ] [ 0 ]
        if m [ i ] [ c - 1 ] > max :
            max = m [ i ] [ c - 1 ]
    desired = ( r * c + 1 ) // 2
    while min < max :
        mid = min + ( max - min ) // 2
        place = 0
        get = 0
        for i in range ( r ) :
            get = bisect.bisect_left ( m , mid )
            if get < 0 :
                get = abs ( get ) - 1
            else :
                while get < len ( m [ i ] ) and m [ i ] [ get ] == mid :
                    get += 1
            place = place + get
        if place < desired :
            min = mid + 1
        else :
            max = mid
    return min
|||

HEIGHT_N_ARY_TREE_PARENT_ARRAY_GIVEN

def findHeight ( parent , n ) :
    res = 0
    for i in range ( n ) :
        p , current = i , 1
        while parent [ p ] != - 1 :
            current += 1
            p = parent [ p ]
        res = max ( res , current )
    return res
|||

CHECK_LARGE_NUMBER_DIVISIBLE_20

def divisibleBy20 ( num ) :
    last_two_digits = int ( num [ - 2 : ] )
    return ( ( last_two_digits % 5 == 0 ) and ( last_two_digits % 4 == 0 ) )
|||

MAXIMUM_VALUE_CHOICE_EITHER_DIVIDING_CONSIDERING

def maxDP ( n ) :
    res = [ 0 ] * ( n + 1 )
    for i in range ( 2 , n + 1 ) :
        res [ i ] = max ( i , ( res [ i / 2 ] + res [ i / 3 ] + res [ i / 4 ] + res [ i / 5 ] ) )
    return res [ n ]
|||

QUERIES_ON_ARRAY_WITH_DISAPPEARING_AND_REAPPEARING_ELEMENTS

def PerformQueries ( a , vec ) :
    ans = [ ]
    n = int ( len ( a ) - 1 )
    q = int ( len ( vec ) )
    for i in range ( q ) :
        t = vec [ i ] [ 0 ]
        m = vec [ i ] [ 1 ]
        if m > n :
            ans.append ( - 1 )
            continue
        turn = int ( t / n )
        rem = int ( t % n )
        if rem == 0 and turn % 2 == 1 :
            ans.append ( - 1 )
            continue
        if rem == 0 and turn % 2 == 0 :
            ans.append ( a [ m ] )
            continue
        if turn % 2 == 0 :
            cursize = n - rem
        else :
            cursize = rem
        if cursize < m :
            ans.append ( - 1 )
            continue
        ans.append ( a [ m + rem ] )
    else :
        cursize = rem
    if cursize < m :
        ans.append ( - 1 )
        continue
    ans.append ( a [ m ] )
for i in ans :
    print ( i , end = ' ' )
|||

FIND_THE_MINIMUM_DISTANCE_BETWEEN_TWO_NUMBERS_1

def minDist ( arr , n , x , y ) :
    i = 0
    min_dist = sys.maxint
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
|||

UNION_AND_INTERSECTION_OF_TWO_SORTED_ARRAYS_2

def printUnion ( arr1 , arr2 , m , n ) :
    i , j = 0 , 0
    while i < m and j < n :
        if arr1 [ i ] < arr2 [ j ] :
            print ( arr1 [ i ] , end = ' ' )
        elif arr2 [ j ] < arr1 [ i ] :
            print ( arr2 [ j ] , end = ' ' )
        else :
            print ( arr2 [ j ] , end = ' ' )
            i += 1
    while i < m :
        print ( arr1 [ i ] , end = ' ' )
    while j < n :
        print ( arr2 [ j ] , end = ' ' )
|||

WORD_WRAP_PROBLEM_SPACE_OPTIMIZED_SOLUTION

def solve_word_wrap ( arr , n , k ) :
    i , j = 0 , 0
    currlen = 0
    cost = 0
    dp = [ 0 ] * n
    ans = [ 0 ] * n
    dp [ n - 1 ] = 0
    ans [ n - 1 ] = n - 1
    for i in range ( n - 2 , - 1 , - 1 ) :
        currlen = - 1
        dp [ i ] = sys.maxint
        for j in range ( i , n ) :
            currlen += ( arr [ j ] + 1 )
            if currlen > k :
                break
            if j == n - 1 :
                cost = 0
            else :
                cost = ( k - currlen ) * ( k - currlen ) + dp [ j + 1 ]
            if cost < dp [ i ] :
                dp [ i ] = cost
                ans [ i ] = j
    i = 0
    while i < n :
        print ( ( i + 1 ) , ( ans [ i ] + 1 ) , end = ' ' )
        i = ans [ i ] + 1
|||

COUNT_DISTINCT_SUBSEQUENCES

def count_sub ( str ) :
    last = [ - 1 ] * MAX_CHAR
    last [ - 1 ] = - 1
    n = len ( str )
    dp = [ 1 ] * n + [ 0 ] * n
    for i in range ( 1 , n + 1 ) :
        dp [ i ] = 2 * dp [ i - 1 ]
        if last [ int ( str [ i - 1 ] ) ] != - 1 :
            dp [ i ] = dp [ i ] - dp [ last [ int ( str [ i - 1 ] ) ] ]
        last [ int ( str [ i - 1 ] ) ] = ( i - 1 )
    return dp [ n ]
|||

LONGEST_EVEN_LENGTH_SUBSTRING_SUM_FIRST_SECOND_HALF_3

def find_length ( str , n ) :
    ans = 0
    for i in range ( 0 , n - 2 ) :
        l , r = i + 1 , i + 1
        lsum , rsum = 0 , 0
        while r < n and l >= 0 :
            lsum += str [ l ] - '0'
            rsum += str [ r ] - '0'
            if lsum == rsum :
                ans = max ( ans , r - l + 1 )
            l -= 1
            r += 1
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
            if j > 0 and j < M - 1 :
                mat [ i ] [ j ] += max ( mat [ i - 1 ] [ j ] , max ( mat [ i - 1 ] [ j - 1 ] , mat [ i - 1 ] [ j + 1 ] ) )
            elif j > 0 :
                mat [ i ] [ j ] += max ( mat [ i - 1 ] [ j ] , mat [ i - 1 ] [ j - 1 ] )
            elif j < M - 1 :
                mat [ i ] [ j ] += max ( mat [ i - 1 ] [ j ] , mat [ i - 1 ] [ j + 1 ] )
            res = max ( mat [ i ] [ j ] , res )
    return res
|||

MAXIMUM_CONSECUTIVE_REPEATING_CHARACTER_STRING

def max_repeated ( str ) :
    len ( str )
    count = 0
    res = str [ 0 ]
    for i in range ( len ( str ) ) :
        cur_count = 1
        for j in range ( i + 1 , len ( str ) ) :
            if str [ i ] != str [ j ] :
                break
            cur_count += 1
        if cur_count > count :
            count = cur_count
            res = str [ i ]
    return res
|||

MAXIMUM_LENGTH_SUBSEQUENCE_DIFFERENCE_ADJACENT_ELEMENTS_EITHER_0_1

def maxLenSub ( arr , n ) :
    mls , max = [ 1 ] , 0
    for i in range ( n ) :
        mls [ i ] = 1
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if abs ( arr [ i ] - arr [ j ] ) <= 1 and mls [ i ] < mls [ j ] + 1 :
                mls [ i ] , mls [ j ] = mls [ j ] + 1
    for i in range ( n ) :
        if max < mls [ i ] :
            max = mls [ i ]
    return max
|||

BREAKING_NUMBER_FIRST_PART_INTEGRAL_DIVISION_SECOND_POWER_10

def calculate ( N ) :
    len ( N )
    l = ( len ( N ) ) // 2
    count = 0
    for i in range ( 1 , l + 1 ) :
        s = N [ : i ]
        l1 = len ( s )
        t = N [ i : l1 + i ]
        if s [ 0 ] == '0' or t [ 0 ] == '0' :
            continue
        if s == t :
            count += 1
    return count
|||

PROGRAM_BINARY_DECIMAL_CONVERSION

def binary_to_decimal ( n ) :
    num = n
    dec_value = 0
    base = 1
    temp = num
    while temp > 0 :
        last_digit = temp % 10
        temp = temp / 10
        dec_value += last_digit * base
        base = base * 2
    return dec_value
|||

HOW_CAN_WE_SUM_THE_DIGITS_OF_A_GIVEN_NUMBER_IN_SINGLE_STATEMENT

def getSum ( n ) :
    sum = 0
    while n != 0 :
        sum = sum + n % 10
        n = n / 10
    return sum
|||

FIND_N_TH_ELEMENT_FROM_STERNS_DIATOMIC_SERIES

def findSDSFunc ( n ) :
    DP = [ 0 ] * ( n + 1 )
    for i in range ( 2 , n + 1 ) :
        if i % 2 == 0 :
            DP [ i ] = DP [ i / 2 ]
        else :
            DP [ i ] = DP [ ( i - 1 ) / 2 ] + DP [ ( i + 1 ) / 2 ]
    return DP [ n ]
|||

NUMBER_SINK_NODES_GRAPH

def count_sink ( n , m , edge_from , edge_to ) :
    mark = [ 1 for i in range ( n + 1 ) if edge_from [ i ] == edge_to [ i ] ]
    count = 0
    for i in range ( 1 , n + 1 ) :
        if mark [ i ] == 0 :
            count += 1
    return count
|||

BREAK_NUMBER_THREE_PARTS

def count_of_ways ( n ) :
    count = 0
    for i in range ( 0 , n ) :
        for j in range ( 0 , n ) :
            for k in range ( 0 , n ) :
                if i + j + k == n :
                    count += 1
    return count
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
|||

MAXIMUM_NUMBER_SEGMENTS_LENGTHS_B_C

def maximum_segments ( n , a , b , c ) :
    dp = [ - 1 ] * n + [ 0 ] * n
    dp [ 0 ] = 0
    for i in range ( n ) :
        if dp [ i ] != - 1 :
            if i + a <= n :
                dp [ i + a ] = max ( dp [ i ] + 1 , dp [ i + a ] )
            if i + b <= n :
                dp [ i + b ] = max ( dp [ i ] + 1 , dp [ i + b ] )
            if i + c <= n :
                dp [ i + c ] = max ( dp [ i ] + 1 , dp [ i + c ] )
    return dp [ n ]
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
    placeAdd = isPossible ( n , index + 1 , sum + arr [ index ] , M , arr , dp )
    placeMinus = isPossible ( n , index + 1 , sum - arr [ index ] , M , arr , dp )
    res = ( placeAdd or placeMinus )
    dp [ index ] [ sum ] = ( res )
    return res
|||

FIND_PAIR_WITH_GREATEST_PRODUCT_IN_ARRAY

def findGreatest ( arr , n ) :
    result = - 1
    for i in range ( n ) :
        for j in range ( n - 1 ) :
            for k in range ( j + 1 , n ) :
                if arr [ j ] * arr [ k ] == arr [ i ] :
                    result = max ( result , arr [ i ] )
    return result
|||

MAXIMUM_SUBARRAY_SUM_ARRAY_CREATED_REPEATED_CONCATENATION

def max_subarray_sum_repeated ( a , n , k ) :
    max_so_far = 0
    INT_MIN , max_ending_here = 0 , 0
    for i in range ( n * k ) :
        max_ending_here = max_ending_here + a [ i % n ]
        if max_so_far < max_ending_here :
            max_so_far = max_ending_here
        if max_ending_here < 0 :
            max_ending_here = 0
    return max_so_far , max_ending_here
|||

LEONARDO_NUMBER_1

def leonardo ( n ) :
    dp = [ 0 ] * ( n + 1 )
    dp [ 0 ] = dp [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        dp [ i ] = dp [ i - 1 ] + dp [ i - 2 ] + 1
    return dp [ n ]
|||

SUM_OF_ALL_SUBSTRINGS_OF_A_STRING_REPRESENTING_A_NUMBER

def sum_of_substrings ( num ) :
    n = len ( num )
    sumofdigit = [ ]
    sumofdigit.append ( num [ 0 ] - '0' )
    res = sumofdigit [ 0 ]
    for i in range ( 1 , n ) :
        numi = num [ i ] - '0'
        sumofdigit.append ( ( i + 1 ) * numi + 10 * sumofdigit [ i - 1 ] )
        res += sumofdigit [ i ]
    return res
|||

PRUFER_CODE_TREE_CREATION

def print_tree_edges ( prufer , m ) :
    vertices = m + 2
    vertex_set = [ ]
    for i in range ( vertices ) :
        vertex_set.append ( 0 )
    for i in range ( vertices - 2 ) :
        vertex_set [ prufer [ i ] - 1 ] += 1
    print ( "\nThe edge set E(G) is :\n" )
    j = 0
    for i in range ( vertices - 2 ) :
        for j in range ( vertices ) :
            if vertex_set [ j ] == 0 :
                vertex_set [ j ] = - 1
                print ( "(%d, %d) " % ( j + 1 , prufer [ i ] ) )
                vertex_set [ prufer [ i ] - 1 ] -= 1
                break
    j = 0
    for i in range ( vertices ) :
        if vertex_set [ i ] == 0 and j == 0 :
            print ( "(%d, " % ( i + 1 ) )
            j += 1
        elif vertex_set [ i ] == 0 and j == 1 :
            print ( ( i + 1 ) + ")\n" )
|||

PROGRAM_FIND_SMALLEST_DIFFERENCE_ANGLES_TWO_PARTS_GIVEN_CIRCLE

def find_minimum_angle ( arr , n ) :
    l , sum , ans = 0 , 0 , 360
    for i in range ( n ) :
        sum += arr [ i ]
        while sum >= 180 :
            ans = min ( ans , 2 * abs ( 180 - sum ) )
            sum -= arr [ l ]
            l += 1
        ans = min ( ans , 2 * abs ( 180 - sum ) )
    return ans
|||

FIND_MAXIMUM_AVERAGE_SUBARRAY_OF_K_LENGTH

def find_max_average ( arr , n , k ) :
    if k > n :
        return - 1
    csum = [ arr [ 0 ] ]
    for i in range ( 1 , n ) :
        csum [ i ] = csum [ i - 1 ] + arr [ i ]
    max_sum , max_end = csum [ k - 1 ] , k - 1
    for i in range ( k , n ) :
        curr_sum = csum [ i ] - csum [ i - k ]
        if curr_sum > max_sum :
            max_sum = curr_sum
            max_end = i
    return max_end - k + 1
|||

SQUARE_PYRAMIDAL_NUMBER_SUM_SQUARES

def find_S ( s ) :
    sum = 0
    for n in range ( 1 , s ) :
        sum += n ** 2
        if sum == s :
            return n
    return - 1
|||

PROGRAM_TO_CALCULATE_AREA_OF_AN_CIRCLE_INSCRIBED_IN_A_SQUARE

def area_of_inscribed_circle ( a ) :
    return ( PI / 4 ) * a ** 2
|||

MINIMUM_NUMBER_CHARACTERS_REMOVED_MAKE_BINARY_STRING_ALTERNATE

def count_to_make_0lternate ( s ) :
    result = 0
    for i in ( len ( s ) - 1 ) :
        if s [ i ] == s [ i + 1 ] :
            result += 1
    return result
|||

FIND_ELEMENTS_PRESENT_FIRST_ARRAY_NOT_SECOND

def find_missing ( a , b , n , m ) :
    for i in range ( n ) :
        j = 0
        for j in range ( m ) :
            if a [ i ] == b [ j ] :
                break
            if j == m :
                print ( a [ i ] , end = ' ' )
|||

REARRANGE_ARRAY_MAXIMUM_MINIMUM_FORM

def rearrange ( arr , n ) :
    temp = [ ]
    small , large = 0 , n - 1
    flag = True
    for i in range ( n ) :
        if flag :
            temp.append ( arr [ large ] )
        else :
            temp.append ( arr [ small ] )
        flag = not flag
    arr = temp [ : ]
    return arr
|||

DYNAMIC_PROGRAMMING_SET_15_LONGEST_BITONIC_SUBSEQUENCE

def lbs ( arr , n ) :
    i , j = 0 , 0
    lis = [ 1 ] * n
    for i in range ( n ) :
        lis [ i ] = 1
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if arr [ i ] > arr [ j ] and lis [ i ] < lis [ j ] + 1 :
                lis [ i ] = lis [ j ] + 1
    lds = [ 1 ] * n
    for i in range ( n ) :
        lds [ i ] = 1
    for i in range ( n - 2 , - 1 , - 1 ) :
        for j in range ( n - 1 , - 1 , - 1 ) :
            if arr [ i ] > arr [ j ] and lds [ i ] < lds [ j ] + 1 :
                lds [ i ] = lds [ j ] + 1
    max = lis [ 0 ] + lds [ 0 ] - 1
    for i in range ( 1 , n ) :
        if lis [ i ] + lds [ i ] - 1 > max :
            max = lis [ i ] + lds [ i ] - 1
    return max
|||

COUNT_PAIRS_WHOSE_PRODUCTS_EXIST_IN_ARRAY

def count_pairs ( arr , n ) :
    result = 0
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            product = arr [ i ] * arr [ j ]
            for k in range ( n ) :
                if arr [ k ] == product :
                    result += 1
                    break
    return result
|||

COUNT_SINGLE_NODE_ISOLATED_SUB_GRAPHS_DISCONNECTED_GRAPH

def compute ( graph , N ) :
    count = 0
    for i in range ( 1 , 7 ) :
        if graph [ i ] == 0 :
            count += 1
    return count
|||

HARDY_RAMANUJAN_THEOREM

def exact_prime_factor_count ( n ) :
    count = 0
    if n % 2 == 0 :
        count += 1
        while n % 2 == 0 :
            n = n // 2
    for i in range ( 3 , math.sqrt ( n ) , 2 ) :
        if n % i == 0 :
            count += 1
            while n % i == 0 :
                n = n // i
    if n > 2 :
        count += 1
    return count
|||

SHORTEST_COMMON_SUPERSEQUENCE_1

def superSeq ( X , Y , m , n ) :
    dp = [ [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m +
|||

POWER_SET

def print_power_set ( set , set_size ) :
    pow_set_size = int ( math.pow ( 2 , set_size ) )
    counter , j = 0 , 0
    for counter in range ( pow_set_size ) :
        for j in range ( set_size ) :
            if ( counter & ( 1 << j ) ) :
                print ( set [ j ] )
        print ( )
|||

CHECK_ARRAY_MAJORITY_ELEMENT

def isMajority ( a , n ) :
    mp = { }
    for i in range ( n ) :
        if mp.has_key ( a [ i ] ) :
            mp [ a [ i ] ] = mp [ a [ i ] ] + 1
        else :
            mp [ a [ i ] ] = 1
    for x , y in mp.items ( ) :
        if x >= n / 2 :
            return True
    return False
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
            print ( arr [ i ] [ l ] , end = ' ' )
            cnt += 1
        l += 1
        if cnt == total :
            break
        for i in range ( l , n ) :
            print ( arr [ m - 1 ] [ i ] , end = ' ' )
            cnt += 1
        m -= 1
        if cnt == total :
            break
        if k < m :
            for i in range ( m - 1 , k - 1 ) :
                print ( arr [ i ] [ n - 1 ] , end = ' ' )
                cnt += 1
            n -= 1
        if cnt == total :
            break
        if l < n :
            for i in range ( n - 1 , l - 1 ) :
                print ( arr [ k ] [ i ] , end = ' ' )
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

def printMinIndexChar ( str , patt ) :
    minIndex = sys.maxint
    m = len ( str )
    n = len ( patt )
    for i in range ( n ) :
        for j in range ( m ) :
            if patt [ i ] == str [ j ] and j < minIndex :
                minIndex = j
                break
    if minIndex != sys.maxint :
        print ( "Minimum Index Character = " + str [ minIndex ] )
    else :
        print ( "No character present" )
|||

PROGRAM_TO_FIND_TRANSPOSE_OF_A_MATRIX_1

def transpose ( A , B ) :
    i , j = 0 , 0
    for i in range ( N ) :
        for j in range ( M ) :
            B [ i , j ] = A [ j , i ]
|||

COUNT_NATURAL_NUMBERS_WHOSE_PERMUTATION_GREATER_NUMBER

def count_number ( n ) :
    result = 0
    for i in range ( 1 , 9 ) :
        s = Stack ( )
        if i <= n :
            s.push ( i )
            result += 1
        while not s.empty ( ) :
            tp = s.top ( )
            s.pop ( )
            for j in range ( tp % 10 , 9 ) :
                x = tp * 10 + j
                if x <= n :
                    s.push ( x )
                    result += 1
    return result
|||

FIND_FIRST_NATURAL_NUMBER_WHOSE_FACTORIAL_DIVISIBLE_X

def first_factorial_divisible_number ( x ) :
    i = 1
    fact = 1
    for i in range ( 1 , x ) :
        fact = fact * i
        if fact % x == 0 :
            break
    return i
|||

PRINT_EQUAL_SUM_SETS_ARRAY_PARTITION_PROBLEM_SET_2

def printEqualSumSets ( arr , n ) :
    i , currSum , sum = 0 , 0 , 0
    for i in range ( len ( arr ) ) :
        sum += arr [ i ]
    if ( sum & 1 ) == 1 :
        print ( "-1" )
        return
    k = sum >> 1
    dp = [ False for i in range ( n + 1 , k + 1 ) ]
    for i in range ( 1 , k + 1 ) :
        dp [ 0 ] [ i ] = False
    for i in range ( 0 , n + 1 ) :
        dp [ i ] [ 0 ] = True
    for i in range ( 1 , n + 1 ) :
        for currSum in range ( 1 , k + 1 ) :
            dp [ i ] [ currSum ] = dp [ i - 1 ] [ currSum ]
            if arr [ i - 1 ] <= currSum :
                dp [ i ] [ currSum ] = dp [ i ] [ currSum ] | dp [ i - 1 ] [ currSum - arr [ i - 1 ] ]
    set1 = [ ]
    set2 = [ ]
    if not dp [ n ] [ k ] :
        print ( "-1\n" )
        return
    i = n
    currSum = k
    while i > 0 and currSum >= 0 :
        if dp [ i - 1 ] [ currSum ] :
            i -= 1
            set2.append ( arr [ i ] )
        elif dp [ i - 1 ] [ currSum - arr [ i - 1 ] ] :
            i -= 1
            currSum -= arr [ i ]
            set1.append ( arr [ i ] )
    print ( "Set 1 elements: " )
    for i in range ( len ( set1 ) ) :
        print ( set1 [ i ] , end = ' ' )
    print ( "\nSet 2 elements: " )
    for i in range ( len ( set2 ) ) :
        print ( set2 [ i ] , end = ' ' )
|||

COUNTING_PAIRS_PERSON_CAN_FORM_PAIR_ONE_1

def number_of_ways ( x ) :
    dp = [ 0 ] * ( x + 1 )
    dp [ 0 ] = dp [ 1 ] = 1
    for i in range ( 2 , x + 1 ) :
        dp [ i ] = dp [ i - 1 ] + ( i - 1 ) * dp [ i - 2 ]
    return dp [ x ]
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
|||

COUNT_SET_BITS_IN_AN_INTEGER

def count_set_bits ( n ) :
    count = 0
    while n :
        count += n & 1
        n >>= 1
    return count
|||

MODULUS_TWO_FLOAT_DOUBLE_NUMBERS

def findMod ( a , b ) :
    if a < 0 :
        a = - a
    if b < 0 :
        b = - b
    mod = a
    while mod >= b :
        mod = mod - b
    if a < 0 :
        return - mod
    return mod
|||

FIND_A_SPECIFIC_PAIR_IN_MATRIX_1

def findMaxValue ( N , mat ) :
    maxValue = int ( "-1" )
    maxArr = [ [ ] for i in range ( N ) ]
    maxv = mat [ N - 1 ] [ N - 1 ]
    for j in range ( N - 2 , - 1 , - 1 ) :
        if mat [ N - 1 ] [ j ] > maxv :
            maxv = mat [ N - 1 ] [ j ]
        maxArr [ N - 1 ] [ j ] = maxv
    maxv = mat [ N - 1 ] [ N - 1 ]
    for i in range ( N - 2 , - 1 , - 1 ) :
        if mat [ i ] [ N - 1 ] > maxv :
            maxv = mat [ i ] [ N - 1 ]
        maxArr [ i ] [ N - 1 ] = maxv
    for i in range ( N - 2 , - 1 , - 1 ) :
        for j in range ( N - 2 , - 1 , - 1 ) :
            if maxArr [ i + 1 ] [ j + 1 ] - mat [ i ] [ j ] > maxValue :
                maxValue = maxArr [ i + 1 ] [ j + 1 ] - mat [ i ] [ j ]
            maxArr [ i ] [ j ] = max ( mat [ i ] [ j ] , max ( maxArr [ i ] [ j + 1 ] , maxArr [ i + 1 ] [ j ] ) )
    return maxValue
|||

MINIMUM_SUM_TWO_NUMBERS_FORMED_DIGITS_ARRAY

def solve ( arr , n ) :
    arr.sort ( )
    a , b = 0 , 0
    for i in range ( n ) :
        if i % 2 != 0 :
            a = a * 10 + arr [ i ]
        else :
            b = b * 10 + arr [ i ]
    return a + b
|||

COUNT_DISTINCT_NON_NEGATIVE_PAIRS_X_Y_SATISFY_INEQUALITY_XX_YY_N_2_1

def count_solutions ( n ) :
    x , y_count , res = 0 , 0 , 0
    for y_count in range ( 0 , y_count * y_count , n ) :
        pass
    while y_count != 0 :
        res += y_count
        x += 1
        while y_count != 0 and ( x * x + ( y_count - 1 ) * ( y_count - 1 ) >= n ) :
            y_count -= 1
    return res
|||

FIND_INDEX_GIVEN_FIBONACCI_NUMBER_CONSTANT_TIME

def find_index ( n ) :
    if n <= 1 :
        return n
    a , b , c = 0 , 1 , 1
    res = 1
    while c < n :
        c , a , b , c = a + b , a , b
        res += 1
        a , b , c = b , c , a , b
    return res
|||

PROGRAM_OCTAL_DECIMAL_CONVERSION

def octal_to_decimal ( n ) :
    num = n
    dec_value = 0
    base = 1
    temp = num
    while temp > 0 :
        last_digit = temp % 10
        temp = temp / 10
        dec_value += last_digit * base
        base = base * 8
    return dec_value
|||

FIND_PERMUTED_ROWS_GIVEN_ROW_MATRIX

def permutated_rows ( mat , m , n , r ) :
    s = set ( )
    for j in range ( n ) :
        s.add ( mat [ r ] [ j ] )
    for i in range ( m ) :
        if i == r :
            continue
        j = None
        for j in range ( n ) :
            if not s.intersection ( mat [ i ] [ j ] ) :
                break
        if j != n :
            continue
        print ( i , end = ' ' )
|||

PRINT_A_CLOSEST_STRING_THAT_DOES_NOT_CONTAIN_ADJACENT_DUPLICATES

def no_adjacent_dup ( s1 ) :
    n = len ( s1 )
    s = s1 [ : ]
    for i in range ( 1 , n ) :
        if s [ i ] == s [ i - 1 ] :
            s [ i ] = 'a'
            while s [ i ] == s [ i - 1 ] or ( i + 1 < n and s [ i ] == s [ i + 1 ] ) :
                s [ i ] += 1
            i += 1
    return ( [ s [ i ] for i in range ( 1 , n ) ] )
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
    if n < cl :
        return False
    return ( str [ : cl ] == corner and str [ n - cl : ] == corner )
|||

LONGEST_SUBARRAY_COUNT_1S_ONE_COUNT_0S

def lenOfLongSubarr ( arr , n ) :
    um = { }
    sum , maxLen = 0 , 0
    for i in range ( n ) :
        sum += arr [ i ] if i > 0 else - 1
        if sum == 1 :
            maxLen = i + 1
        elif not um.has_key ( sum ) :
            um [ sum ] = i
        if um.has_key ( sum - 1 ) :
            if maxLen < ( i - um [ sum - 1 ] ) :
                maxLen = i - um [ sum - 1 ]
    return maxLen
|||

DIVIDE_CONQUER_SET_6_SEARCH_ROW_WISE_COLUMN_WISE_SORTED_2D_ARRAY

def search ( mat , from_row , to_row , from_col , to_col , key ) :
    i = from_row + ( to_row - from_row ) / 2
    j = from_col + ( to_col - from_col ) / 2
    if mat [ i ] [ j ] == key :
        print ( "Found %d at %d %d" % ( key , i , j ) )
    else :
        if i != to_row or j != from_col :
            search ( mat , from_row , i , j , to_col , key )
        if from_row == to_row and from_col + 1 == to_col :
            if mat [ from_row ] [ to_col ] == key :
                print ( "Found %d at %d %d" % ( key , from_row , to_col ) )
            if mat [ i ] [ j ] < key :
                if i + 1 <= to_row :
                    search ( mat , i + 1 , to_row , from_col , to_col , key )
            else :
                if j - 1 >= from_col :
                    search ( mat , from_row , to_row , from_col , j - 1 , key )
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
|||

URLIFY_GIVEN_STRING_REPLACE_SPACES

def replace_spaces ( str ) :
    space_count , i = 0 , 0
    for i in range ( len ( str ) ) :
        if str [ i ] == ' ' :
            space_count += 1
    while str [ i - 1 ] == ' ' :
        space_count -= 1
        i -= 1
    new_length = i + space_count * 2
    if new_length > MAX :
        return str
    index = new_length - 1
    new_str = str [ : index ]
    str = str [ index : ]
    for j in range ( i - 1 , - 1 , - 1 ) :
        if new_str [ j ] == ' ' :
            str [ index ] = '0'
            str [ index - 1 ] = '2'
            str [ index - 2 ] = '%'
            index = index - 3
        else :
            str [ index ] = new_str [ j ]
            index -= 1
    return str
|||

MAXIMUM_PATH_SUM_STARTING_CELL_0_TH_ROW_ENDING_CELL_N_1_TH_ROW

def MaximumPath ( Mat ) :
    result = 0
    dp = [ [ 0 ] * N for N in range ( N + 2 ) ]
    for rows in dp :
        np.random.shuffle ( rows )
    for i in range ( N ) :
        dp [ 0 ] [ i + 1 ] = Mat [ 0 ] [ i ]
    for i in range ( 1 , N ) :
        for j in range ( 1 , N + 1 ) :
            dp [ i ] [ j ] = max ( dp [ i - 1 ] [ j - 1 ] , max ( dp [ i - 1 ] [ j ] , dp [ i - 1 ] [ j + 1 ] ) ) + Mat [ i ] [ j - 1 ]
    for i in range ( 0 , N + 1 ) :
        result = max ( result , dp [ N - 1 ] [ i ] )
    return result
|||

COMPUTE_THE_INTEGER_ABSOLUTE_VALUE_ABS_WITHOUT_BRANCHING

def get_abs ( n ) :
    mask = n >> ( SIZE_INT * CHAR_BIT - 1 )
    return ( ( n + mask ) ^ mask )
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
        return dp [ i ] [ j ] = countPS ( i + 1 , j ) + countPS ( i , j - 1 ) + 1
    else :
        return dp [ i ] [ j ] = countPS ( i + 1 , j ) + countPS ( i , j - 1 ) - countPS ( i + 1 , j - 1 )
|||

LARGEST_SUM_CONTIGUOUS_SUBARRAY_2

def max_subarray_sum ( a , size ) :
    max_so_far = a [ 0 ]
    curr_max = a [ 0 ]
    for i in range ( 1 , size ) :
        curr_max = max ( a [ i ] , curr_max + a [ i ] )
        max_so_far = max ( max_so_far , curr_max )
    return max_so_far
|||

COUNT_MINIMUM_STEPS_GET_GIVEN_DESIRED_ARRAY

def count_min_operations ( n ) :
    result = 0
    while True :
        zero_count = 0
        i = 0
        for i in range ( n ) :
            if arr [ i ] % 2 == 1 :
                break
            elif arr [ i ] == 0 :
                zero_count += 1
        if zero_count == n :
            return result
        if i == n :
            for j in range ( n ) :
                arr [ j ] = arr [ j ] / 2
            result += 1
        for j in range ( i , n ) :
            if arr [ j ] % 2 == 1 :
                arr [ j ] -= 1
                result += 1
|||

PRINT_FIBONACCI_SEQUENCE_USING_2_VARIABLES_1

def fib ( n ) :
    a , b = 0 , 1
    if n >= 0 :
        print ( a , end = ' ' )
    if n >= 1 :
        print ( b , end = ' ' )
    for i in range ( 2 , n + 1 ) :
        print ( a + b , end = ' ' )
        b , a = a + b , b - a
|||

PROGRAM_CHECK_INPUT_INTEGER_STRING

def isNumber ( s ) :
    for c in s :
        if ord ( c ) == 0 : return False
    return True
|||

MINIMUM_HEIGHT_TRIANGLE_GIVEN_BASE_AREA

def minHeight ( base , area ) :
    d = ( 2 * area ) / base
    return math.ceil ( d )
|||

FIND_POSITION_GIVEN_NUMBER_AMONG_NUMBERS_MADE_4_7

def findpos ( n ) :
    k , pos , i = 0 , 0 , 0
    while k != len ( n ) :
        try :
            pos = pos * 2 + 1
        except TypeError :
            pass
        try :
            pos = pos * 2 + 2
        except TypeError :
            pass
        i += 1
        k += 1
    return pos
|||

MINIMUM_OPERATIONS_REQUIRED_SET_ELEMENTS_BINARY_MATRIX

def minOperation ( arr ) :
    ans = 0
    for i in range ( N - 1 , - 1 , - 1 ) :
        for j in range ( M - 1 , - 1 , - 1 ) :
            if arr [ i ] [ j ] == False :
                ans += 1
                for k in range ( 0 , i + 1 ) :
                    for h in range ( 0 , j + 1 ) :
                        if arr [ k ] [ h ] == True :
                            arr [ k ] [ h ] = False
                        else :
                            arr [ k ] [ h ] = True
    return ans
|||

LONGEST_EVEN_LENGTH_SUBSTRING_SUM_FIRST_SECOND_HALF_2

def find_length ( str , n ) :
    sum = [ 0 ] * ( n + 1 )
    for i in range ( 1 , n + 1 ) :
        sum [ i ] = ( sum [ i - 1 ] + str [ i - 1 ] - '0' )
    ans = 0
    for len in range ( 2 , n + 1 , 2 ) :
        for i in range ( 0 , n - len ) :
            j = i + len - 1
            if sum [ i + len / 2 ] - sum [ i ] == sum [ i + len ] - sum [ i + len / 2 ] :
                ans = max ( ans , len )
    return ans
|||

MULTIPLY_LARGE_NUMBERS_REPRESENTED_AS_STRINGS

def multiply ( num1 , num2 ) :
    len1 = len ( num1 )
    len2 = len ( num2 )
    if len1 == 0 or len2 == 0 :
        return '0'
    result = [ 0 ] * ( len1 + len2 )
    i_n1 = 0
    i_n2 = 0
    for i in range ( len1 - 1 , - 1 , - 1 ) :
        carry = 0
        n1 = num1 [ i ] - '0'
        i_n2 = 0
        for j in range ( len2 - 1 , - 1 , - 1 ) :
            n2 = num2 [ j ] - '0'
            sum = n1 * n2 + result [ i_n1 + i_n2 ] + carry
            carry = sum / 10
            result [ i_n1 + i_n2 ] = sum % 10
            i_n2 += 1
        if carry > 0 :
            result [ i_n1 + i_n2 ] += carry
        i_n1 += 1
    i = len ( result ) - 1
    while i >= 0 and result [ i ] == 0 :
        i -= 1
    if i == - 1 :
        return '0'
    s = ''
    while i >= 0 :
        s += ( result [ i ] )
    return s
|||

PARTITION_NUMBER_TWO_DIVISBLE_PARTS

def find_division ( str , a , b ) :
    len = len ( str )
    lr = [ ( ord ( str [ 0 ] ) - ord ( '0' ) ) % a for i in range ( 1 , len ) ]
    for i in range ( 1 , len ) :
        lr [ i ] = ( ( lr [ i - 1 ] * 10 ) % a + ( ord ( str [ i ] ) - ord ( '0' ) ) ) % a
    rl = [ ( ord ( str [ len - 1 ] ) - ord ( '0' ) ) % b ) % b for i in range ( len + 1 , len ) ]
    power10 = 10
    for i in range ( len - 2 , - 1 , - 1 ) :
        rl [ i ] = ( rl [ i + 1 ] + ( ord ( str [ i ] ) - ord ( '0' ) ) * power10 ) % b
        power10 = ( power10 * 10 ) % b
    for i in range ( len - 1 ) :
        if lr [ i ] != 0 :
            continue
        if rl [ i + 1 ] == 0 :
            print ( "YES" )
            for k in range ( 0 , i + 1 ) :
                print ( str [ k ] )
            print ( ", " )
            for k in range ( i + 1 , len ) :
                print ( str [ k ] )
            return
    print ( "NO" )
|||

PROGRAM_BEST_FIT_ALGORITHM_MEMORY_MANAGEMENT

def bestFit ( blockSize , m , processSize , n ) :
    allocation = [ ]
    for i in range ( n ) :
        allocation.append ( - 1 )
    for i in range ( n ) :
        bestIdx = - 1
        for j in range ( m ) :
            if blockSize [ j ] >= processSize [ i ] :
                if bestIdx == - 1 :
                    bestIdx = j
                elif blockSize [ bestIdx ] > blockSize [ j ] :
                    bestIdx = j
        if bestIdx != - 1 :
            allocation.append ( bestIdx )
            blockSize [ bestIdx ] -= processSize [ i ]
    print ( "\nProcess No.\tProcess Size\tBlock no." )
    for i in range ( n ) :
        print ( "   " + str ( i + 1 ) + "\t\t" + str ( processSize [ i ] ) + "\t\t" )
        if allocation [ i ] != - 1 :
            print ( allocation [ i ] + 1 )
        else :
            print ( "Not Allocated" )
        print ( )
|||

FINDING_THE_MAXIMUM_SQUARE_SUB_MATRIX_WITH_ALL_EQUAL_ELEMENTS

def largestKSubmatrix ( a ) :
    dp = [ [ 0 ] * Row ]
    result = 0
    for i in range ( Row ) :
        for j in range ( Col ) :
            if i == 0 or j == 0 :
                dp [ i ] [ j ] = 1
            else :
                if a [ i ] [ j ] == a [ i - 1 ] [ j ] and a [ i ] [ j ] == a [ i ] [ j - 1 ] and a [ i ] [ j ] == a [ i - 1 ] [ j - 1 ] :
                    dp [ i ] [ j ] = ( dp [ i - 1 ] [ j ] > dp [ i ] [ j - 1 ] and dp [ i - 1 ] [ j ] > dp [ i - 1 ] [ j - 1 ] + 1 )
                    dp [ i - 1 ] [ j ] = ( dp [ i ] [ j - 1 ] > dp [ i - 1 ] [ j ] and dp [ i ] [ j - 1 ] > dp [ i - 1 ] [ j - 1 ] + 1 )
                else :
                    dp [ i ] [ j ] = 1
            result = result > dp [ i ] [ j ]
    return result
|||

FRIENDS_PAIRING_PROBLEM_1

def countFriendsPairings ( n ) :
    if dp [ n ] != - 1 :
        return dp [ n ]
    if n > 2 :
        return dp [ n ] = countFriendsPairings ( n - 1 ) + ( n - 1 ) * countFriendsPairings ( n - 2 )
    else :
        return dp [ n ] = n
|||

FIRST_ELEMENT_OCCURRING_K_TIMES_ARRAY

def first_element ( arr , n , k ) :
    count_dict = { }
    for i in range ( n ) :
        a = 0
        if count_dict.get ( arr [ i ] , 0 ) :
            a = count_dict [ arr [ i ] ]
        count_dict [ arr [ i ] ] = a + 1
    for i in range ( n ) :
        if count_dict [ arr [ i ] ] == k :
            return arr [ i ]
    return - 1
|||

SUM_SERIES_0_6_0_06_0_006_0_0006_N_TERMS

def sum_of_series ( n ) :
    return ( 0.666 ) ** ( 1 - 1 / pow ( 10 , n ) )
|||

COUNT_WORDS_IN_A_GIVEN_STRING

def countWords ( str ) :
    state = OUT
    wc = 0
    i = 0
    while i < len ( str ) :
        if str [ i ] in ( ' ' , '\n' , '\t' ) :
            state = OUT
        elif state == OUT :
            state = IN
            yield wc
        i += 1
|||

PARTITION_INTO_TWO_SUBARRAYS_OF_LENGTHS_K_AND_N_K_SUCH_THAT_THE_DIFFERENCE_OF_SUMS_IS_MAXIMUM

def maxDifference ( arr , N , k ) :
    M , S , S1 , max_difference = 0 , 0 , 0 , 0
    for i in range ( N ) :
        S += arr [ i ]
    temp = 0
    for i in range ( N ) :
        for j in range ( i + 1 , N ) :
            if arr [ i ] < arr [ j ] :
                temp = arr [ i ]
                arr [ i ] , arr [ j ] = arr [ j ] , temp
    M = max ( k , N - k )
    for i in range ( M ) :
        S1 += arr [ i ]
    max_difference = S1 - ( S - S1 )
    return max_difference
|||

HOW_WILL_YOU_PRINT_NUMBERS_FROM_1_TO_200_WITHOUT_USING_LOOP

def print_nos ( n ) :
    if n > 0 :
        print_nos ( n - 1 )
        print ( n , end = ' ' )
    return
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
    ones , twos = 0 , 0
    common_bit_mask = 0
    for i in range ( n ) :
        twos = twos | ( ones & arr [ i ] )
        ones = ones ^ arr [ i ]
        common_bit_mask = ~ ( ones & twos )
        ones &= common_bit_mask
        twos &= common_bit_mask
    return ones , twos
|||

CASSINIS_IDENTITY

def cassini ( n ) :
    return ( n & 1 ) or - 1
|||

DISTRIBUTING_ALL_BALLS_WITHOUT_REPETITION

def distributingBalls ( k , n , str ) :
    a = [ ]
    for i in range ( n ) :
        a.append ( str [ i ] - 'a' )
    for i in range ( MAX_CHAR ) :
        if a [ i ] > k :
            return False
    return True
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
|||

MAXIMIZE_ARRJ_ARRI_ARRL_ARRK_SUCH_THAT_I_J_K_L

def find_max_value ( arr , n ) :
    if n < 4 :
        print ( "The array should have" " atleast 4 elements" )
    table1 = np.zeros ( ( n + 1 , ) )
    table2 = np.zeros ( ( n , ) )
    table3 = np.zeros ( ( n - 1 , ) )
    table4 = np.zeros ( ( n - 2 , ) )
    np.fill_diagonal ( table1 , np.inf )
    np.fill_diagonal ( table2 , np.inf )
    np.fill_diagonal ( table3 , np.inf )
    np.fill_diagonal ( table4 , np.inf )
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
|||

SORT_AN_ARRAY_OF_0S_1S_AND_2S

def sort012 ( a , arr_size ) :
    lo = 0
    hi = arr_size - 1
    mid , temp = 0 , 0
    while mid <= hi :
        try :
            temp = a [ mid ]
            a [ lo ] , a [ mid ] = a [ mid ] , a [ mid ]
            a [ mid ] = temp
            lo += 1
            mid += 1
            break
        except IndexError :
            mid += 1
            break
|||

NTH_EVEN_FIBONACCI_NUMBER

def evenFib ( n ) :
    if n < 1 :
        return n
    if n == 1 :
        return 2
    return ( ( 4 * evenFib ( n - 1 ) ) + evenFib ( n - 2 ) )
|||

NEXT_GREATER_ELEMENT

def printNGE ( arr , n ) :
    next , i , j = - 1 , - 1 , - 1
    for i in range ( n ) :
        next = - 1
        for j in range ( i + 1 , n ) :
            if arr [ i ] < arr [ j ] :
                next = arr [ j ]
                break
        print ( arr [ i ] , " -- " , next )
|||

CHECK_WHETHER_GIVEN_CIRCLE_RESIDE_BOUNDARY_MAINTAINED_OUTER_CIRCLE_INNER_CIRCLE

def fit_or_not_fit ( R , r , x , y , rad ) :
    val = math.sqrt ( math.pow ( x , 2 ) + math.pow ( y , 2 ) )
    if val + rad <= R and val - rad >= R - r :
        print ( "Fits" )
    else :
        print ( "Doesn't Fit" )
|||

BASIC_AND_EXTENDED_EUCLIDEAN_ALGORITHMS_1

def gcdExtended ( a , b , x , y ) :
    if a == 0 :
        x = 0
        y = 1
        return b
    x1 , y1 = 1 , 1
    gcd = gcdExtended ( b % a , a , x1 , y1 )
    x , y = y1 - ( b // a ) * x1 , x1
    return gcd
|||

FIND_SMALLEST_RANGE_CONTAINING_ELEMENTS_FROM_K_LISTS

def findSmallestRange ( arr , n , k ) :
    i , minval , maxval , minrange , minel = 0 , 0 , 0 , 0 , 0
    flag , minind = 0 , 0 , 0
    for i in range ( 0 , k ) :
        ptr = [ 0 ] * k
    minrange = float ( 'inf' )
    while True :
        minind = - 1
        minval = float ( 'inf' )
        maxval = float ( 'inf' )
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
|||

FIND_THE_MINIMUM_COST_TO_REACH_A_DESTINATION_WHERE_EVERY_STATION_IS_CONNECTED_IN_ONE_DIRECTION

def minCost ( cost ) :
    dist = [ INF ]
    for i in range ( N ) :
        dist.append ( INF )
    dist [ 0 ] = 0
    for i in range ( N ) :
        for j in range ( i + 1 , N ) :
            if dist [ j ] > dist [ i ] + cost [ i ] [ j ] :
                dist [ j ] = dist [ i ] + cost [ i ] [ j ]
    return dist [ N - 1 ]
|||

MIDDLE_OF_THREE_USING_MINIMUM_COMPARISONS_1

def middle_of_three ( a , b , c ) :
    if a > b :
        if b > c :
            return b
        elif a > c :
            return c
        else :
            return a
    else :
        if a > c :
            return a
        elif b > c :
            return c
        else :
            return b
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
|||

COMPUTE_MODULUS_DIVISION_BY_A_POWER_OF_2_NUMBER

def getModulo ( n , d ) :
    return ( n & ( d - 1 ) )
|||

COUNT_BINARY_STRINGS_K_TIMES_APPEARING_ADJACENT_TWO_SET_BITS

def count_strings ( n , k ) :
    dp = [ [ 1 , 1 ] , [ 1 , 1 ] ]
    dp [ 1 ] [ 0 ] [ 0 ] = 1
    dp [ 1 ] [ 0 ] [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        for j in range ( i , k + 1 ) :
            dp [ i ] [ j ] [ 0 ] = dp [ i - 1 ] [ j ] [ 0 ] + dp [ i - 1 ] [ j ] [ 1 ]
            dp [ i ] [ j ] [ 1 ] = dp [ i - 1 ] [ j ] [ 0 ]
            if j - 1 >= 0 :
                dp [ i ] [ j ] [ 1 ] += dp [ i - 1 ] [ j - 1 ] [ 1 ]
    return dp [ n ] [ k ] [ 0 ] + dp [ n ] [ k ] [ 1 ]
|||

FINDING_K_MODULUS_ARRAY_ELEMENT

def print_equal_mod_numbers ( arr , n ) :
    arr.sort ( )
    d = arr [ n - 1 ] - arr [ 0 ]
    v = [ ]
    for i in range ( 1 , d * i <= d ) :
        if d % i == 0 :
            v.append ( i )
            if i != d / i :
                v.append ( d / i )
    for i in range ( len ( v ) ) :
        temp = arr [ 0 ] % v [ i ]
        j = 0
        for j in range ( 1 , n ) :
            if arr [ j ] % v [ i ] != temp :
                break
        if j == n :
            print ( v [ i ] , end = ' ' )
|||

CIRCULAR_MATRIX_CONSTRUCT_A_MATRIX_WITH_NUMBERS_1_TO_MN_IN_SPIRAL_WAY

def spiral_fill ( m , n , a ) :
    val = 1
    k , l = 0 , 0
    while k < m and l < n :
        for i in range ( l , n ) :
            a [ k ] [ i ] = val ++
        k += 1
        for i in range ( k , m ) :
            a [ i ] [ n - 1 ] = val ++
        n -= 1
        if k < m :
            for i in range ( n - 1 , l , - 1 ) :
                a [ m - 1 ] [ i ] = val ++
            m -= 1
        if l < n :
            for i in range ( m - 1 , k , - 1 ) :
                a [ i ] [ l ] = val ++
            l += 1
|||

FIND_THE_TWO_REPEATING_ELEMENTS_IN_A_GIVEN_ARRAY_2

def printRepeating ( arr , size ) :
    xor = arr [ 0 ]
    set_bit_no = 0
    i = 0
    n = size - 2
    x , y = 0 , 0
    for i in range ( 1 , size ) :
        xor ^= arr [ i ]
    for i in range ( 1 , n + 1 ) :
        xor ^= i
    set_bit_no = ( xor & ~ ( xor - 1 ) )
    for i in range ( size ) :
        a = arr [ i ] & set_bit_no
        if a != 0 :
            x = x ^ arr [ i ]
        else :
            y = y ^ arr [ i ]
    for i in range ( 1 , n + 1 ) :
        a = i & set_bit_no
        if a != 0 :
            x = x ^ i
        else :
            y = y ^ i
    print ( "The two reppeated elements are :" )
    print ( x , y )
|||

COUNT_POSSIBLE_WAYS_TO_CONSTRUCT_BUILDINGS

def countWays ( N ) :
    if N == 1 :
        return 4
    countB , countS , prevCountB , prevCountS = 1 , 1 , 1 , 1
    for i in range ( 2 , N + 1 ) :
        prevCountB , prevCountS , prevCountB = countB , prevCountS , prevCountB + prevCountS , prevCountB
        countB , prevCountS , prevCountB = countS , prevCountS , prevCountB + prevCountS , prevCountB + prevCountS
    result = countS + countB
    return ( result * result )
|||

ONE_LINE_FUNCTION_FOR_FACTORIAL_OF_A_NUMBER

def factorial ( n ) :
    return ( n if n == 1 or n == 0 else 1 ) * factorial ( n - 1 )
|||

CHECK_GIVEN_MATRIX_SPARSE_NOT

def isSparse ( array , m , n ) :
    counter = 0
    for i in range ( m ) :
        for j in range ( n ) :
            if array [ i ] [ j ] == 0 :
                counter += 1
    return ( counter > ( ( m * n ) / 2 ) )
|||

DYNAMIC_PROGRAMMING_SET_10_0_1_KNAPSACK_PROBLEM

def knapSack ( W , wt , val , n ) :
    if n == 0 or W == 0 :
        return 0
    if wt [ - 1 ] > W :
        return knapSack ( W , wt , val , n - 1 )
    else :
        return max ( val [ - 1 ] + knapSack ( W - wt [ - 1 ] , wt , val , n - 1 ) , knapSack ( W , wt , val , n - 1 ) )
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
            min_sum = curr_sum
            res_index = ( i - k + 1 )
    print ( "Subarray between [%d, %d] has minimum average" % ( res_index , ( res_index + k - 1 ) ) )
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
|||

A_PRODUCT_ARRAY_PUZZLE_1

def productArray ( arr , n ) :
    if n == 1 :
        print ( '0' )
        return
    i , temp = 1 , 1
    prod = [ ]
    for j in range ( n ) :
        prod.append ( 1 )
    for i in range ( n ) :
        prod.append ( temp )
        temp *= arr [ i ]
    temp = 1
    for i in range ( n - 1 , - 1 , - 1 ) :
        prod.append ( temp )
        temp *= arr [ i ]
    for i in range ( n ) :
        print ( prod [ i ] , end = ' ' )
    return
|||

FIND_PAIRS_GIVEN_SUM_ELEMENTS_PAIR_DIFFERENT_ROWS

def pairSum ( mat , n , sum ) :
    for i in range ( n ) :
        mat.sort ( )
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            left , right = 0 , n - 1
            while left < n and right >= 0 :
                if ( mat [ i ] [ left ] + mat [ j ] [ right ] ) == sum :
                    print ( "(" + str ( mat [ i ] [ left ] ) + ", " + str ( mat [ j ] [ right ] ) + "), " )
                    left += 1
                    right -= 1
                else :
                    if ( mat [ i ] [ left ] + mat [ j ] [ right ] ) < sum :
                        left += 1
                    else :
                        right -= 1
|||

CHECK_STRING_CAN_OBTAINED_ROTATING_ANOTHER_STRING_2_PLACES

def is_rotated ( str1 , str2 ) :
    if len ( str1 ) != len ( str2 ) :
        return False
    clock_rot = ""
    anticlock_rot = ""
    _ , _ , _ , _ , _ , _ , _ , _ , _ , _ , _ = str2
    anticlock_rot = anticlock_rot + str2 [ - 2 : ] + str2 [ : - 2 ]
    clock_rot = clock_rot + str2 [ 2 : ] + str2 [ : 2 ]
    return ( str1 == clock_rot or str1 == anticlock_rot )
|||

N_TH_NUMBER_WHOSE_SUM_OF_DIGITS_IS_TEN

def find_nth ( n ) :
    count = 0
    for curr in range ( 1 , 10 ) :
        sum = 0
        for x in range ( curr , 0 , 10 ) :
            sum = sum + x % 10
        if sum == 10 :
            count += 1
        if count == n :
            return curr
|||

PROGRAM_FIND_SLOPE_LINE

def slope ( x1 , y1 , x2 , y2 ) :
    return ( y2 - y1 ) / ( x2 - x1 )
|||

GCD_ELEMENTS_GIVEN_RANGE

def range_gcd ( n , m ) :
    return ( n , m )
|||

LONGEST_ALTERNATING_SUB_ARRAY_STARTING_EVERY_INDEX_BINARY_ARRAY_1

def alternate_subarray ( arr , n ) :
    count = 1
    prev = arr [ 0 ]
    for i in range ( 1 , n ) :
        if ( arr [ i ] ^ prev ) == False :
            while count > 0 :
                print ( count )
        count += 1
        prev = arr [ i ]
    while count != 0 :
        print ( count )
|||

FIND_UNIT_DIGIT_X_RAISED_POWER_Y

def unit_digit_x_raised_y ( x , y ) :
    res = 1
    for i in range ( y ) :
        res = ( res * x ) % 10
    return res
|||

MULTIPLY_LARGE_INTEGERS_UNDER_LARGE_MODULO

def modulo_multiplication ( a , b , mod ) :
    res = 0
    a %= mod
    while b :
        if ( b & 1 ) :
            res = ( res + a ) % mod
        a = ( 2 * a ) % mod
        b >>= 1
    return res
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
            res.append ( 9 )
            s -= 9
        else :
            res.append ( s )
            s = 0
    res.append ( s + 1 )
    print ( "Smallest number is " )
    for i in range ( m ) :
        print ( res [ i ] )
|||

C_PROGRAM_FIND_LARGEST_ELEMENT_ARRAY

def largest ( ) :
    i = 0
    max = arr [ 0 ]
    for i in range ( 1 , len ( arr ) ) :
        if arr [ i ] > max :
            max = arr [ i ]
    return max
|||

COUNT_NUMBERS_CAN_CONSTRUCTED_USING_TWO_NUMBERS

def count_nums ( n , x , y ) :
    arr = [ ]
    if x <= n :
        arr.append ( True )
    if y <= n :
        arr.append ( True )
    result = 0
    for i in range ( min ( x , y ) , n + 1 ) :
        if arr [ i ] :
            if i + x <= n :
                arr.append ( True )
            if i + y <= n :
                arr.append ( True )
            result += 1
    return result
|||

BUBBLE_SORT_1

def bubble_sort ( arr , n ) :
    i , j , temp = 0 , 0 , 0
    swapped = 0
    for i in range ( n - 1 ) :
        swapped = 0
        for j in range ( n - i - 1 ) :
            if arr [ j ] > arr [ j + 1 ] :
                temp = arr [ j ]
                arr [ j ] , arr [ j + 1 ] = arr [ j + 1 ] , arr [ j + 1 ]
                arr [ j + 1 ] , arr [ j + 1 ] = temp , arr [ j + 1 ]
                swapped = 1
        if swapped == 0 :
            break
|||

MAXIMUM_SUM_2_X_N_GRID_NO_TWO_ELEMENTS_ADJACENT

def max_sum ( grid , n ) :
    incl = max ( grid [ 0 ] [ 0 ] , grid [ 1 ] [ 0 ] )
    excl , excl_new = 0 , 0
    for i in range ( 1 , n ) :
        excl_new = max ( excl , incl )
        incl = excl + max ( grid [ 0 ] [ i ] , grid [ 1 ] [ i ] )
        excl = excl_new
    return max ( excl , incl )
|||

GCD_FACTORIALS_TWO_NUMBERS

def gcdOfFactorial ( m , n ) :
    min = m if m < n else n
    return factorial ( min )
|||

AREA_OF_A_SECTOR

def SectorArea ( radius , angle ) :
    if angle >= 360 :
        print ( "Angle not possible" )
    else :
        sector = ( ( 22 * radius ** 2 ) / 7 ) * ( angle / 360 )
        print ( sector )
|||

COUNT_EVEN_LENGTH_BINARY_SEQUENCES_WITH_SAME_SUM_OF_FIRST_AND_SECOND_HALF_BITS_1

def count_seq ( n ) :
    nCr , res = 1 , 1
    for r in range ( 1 , n + 1 ) :
        nCr = ( nCr * ( n + 1 - r ) ) // r
        res += nCr ** 2
    return res
|||

LONGEST_EVEN_LENGTH_SUBSTRING_SUM_FIRST_SECOND_HALF_1

def find_length ( str ) :
    n = len ( str )
    maxlen = 0
    sum = [ 0 ] * n
    for i in range ( n ) :
        sum [ i ] = str [ i ] - '0'
    for len in range ( 2 , n + 1 ) :
        for i in range ( n - len + 1 ) :
            j = i + len - 1
            k = len // 2
            sum [ i ] = sum [ i ] + sum [ j - k + 1 ]
            if len % 2 == 0 and sum [ i ] == sum [ ( j - k + 1 ) ] and len > maxlen :
                maxlen = len
    return maxlen
|||

SWAP_ALL_ODD_AND_EVEN_BITS

def swap_bits ( x ) :
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
        swap ( arr , i , i + 1 )
|||

FIND_HARMONIC_MEAN_USING_ARITHMETIC_MEAN_GEOMETRIC_MEAN

def compute ( a , b ) :
    AM , GM , HM = ( a + b ) / 2 , math.sqrt ( a * b ) , ( GM * GM ) / AM
    return HM
|||

COUNT_BALANCED_BINARY_TREES_HEIGHT_H

def count_bt ( h ) :
    dp = [ 1 ] * ( h + 1 )
    for i in range ( 2 , h + 1 ) :
        dp [ i ] = ( dp [ i - 1 ] * ( ( 2 * dp [ i - 2 ] ) % MOD + dp [ i - 1 ] ) % MOD ) % MOD
    return dp [ h ]
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
            res += 1
    return ( res , 0 )
|||

SHUFFLE_A_GIVEN_ARRAY

def randomize ( arr , n ) :
    r = random.Random ( )
    for i in range ( n - 1 , 0 , - 1 ) :
        j = r.randint ( i + 1 , i + 1 )
        temp = arr [ i ]
        arr [ i ] = arr [ j ]
        arr [ j ] = temp
    print ( list ( arr ) )
|||

UGLY_NUMBERS

def getNthUglyNo ( n ) :
    ugly = [ ]
    i2 , i3 , i5 = 0 , 0 , 0
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    next_ugly_no = 1
    ugly.append ( 1 )
    for i in range ( 1 , n ) :
        next_ugly_no = min ( next_multiple_of_2 , min ( next_multiple_of_3 , next_multiple_of_5 ) )
        ugly.append ( next_ugly_no )
        if next_ugly_no == next_multiple_of_2 :
            i2 = i2 + 1
            next_multiple_of_2 = ugly [ i2 ] * 2
        if next_ugly_no == next_multiple_of_3 :
            i3 = i3 + 1
            next_multiple_of_3 = ugly [ i3 ] * 3
        if next_ugly_no == next_multiple_of_5 :
            i5 = i5 + 1
            next_multiple_of_5 = ugly [ i5 ] * 5
    return next_ugly_no
|||

MINIMUM_COST_CUT_BOARD_SQUARES

def minimum_cost_of_breaking ( X , Y , m , n ) :
    res = 0
    X.sort ( key = lambda x : x [ 1 ] )
    Y.sort ( key = lambda x : x [ 1 ] )
    hzntl , vert = 1 , 1
    i , j = 0 , 0
    while i < m and j < n :
        if X [ i ] > Y [ j ] :
            res += X [ i ] * vert
            hzntl += 1
            i += 1
        else :
            res += Y [ j ] * hzntl
            vert += 1
            j += 1
    total = 0
    while i < m :
        total += X [ i ]
    res += total * vert
    total = 0
    while j < n :
        total += Y [ j ]
    res += total * hzntl
    return res
|||

DYNAMIC_PROGRAMMING_SET_10_0_1_KNAPSACK_PROBLEM_1

def knapSack ( W , wt , val , n ) :
    i , w = 0 , 0
    K = [ 0 ] * ( n + 1 ) * ( W + 1 )
    for i in range ( 0 , n + 1 ) :
        for w in range ( 0 , W + 1 ) :
            if i == 0 or w == 0 :
                K [ i ] [ w ] = 0
            elif wt [ i - 1 ] <= w :
                K [ i ] [ w ] = max ( val [ i - 1 ] + K [ i - 1 ] [ w - wt [ i - 1 ] ] , K [ i - 1 ] [ w ] )
            else :
                K [ i ] [ w ] = K [ i - 1 ] [ w ]
    return K [ n ] [ W ]
|||

STACK_PERMUTATIONS_CHECK_IF_AN_ARRAY_IS_STACK_PERMUTATION_OF_OTHER

def check_stack_permutation ( ip , op , n ) :
    input = Queue ( )
    for i in range ( n ) :
        input.put ( ip [ i ] )
    output = Queue ( )
    for i in range ( n ) :
        output.put ( op [ i ] )
    temp_stack = Stack ( )
    while not input.empty ( ) :
        ele = input.get ( )
        if ele == output.get ( ) :
            output.put ( ele )
            while not temp_stack.empty ( ) :
                if temp_stack.get ( ) == output.get ( ) :
                    temp_stack.pop ( )
                    output.put ( ele )
                else :
                    break
        else :
            temp_stack.push ( ele )
    return ( input.empty ( ) and temp_stack.empty ( ) )
|||

PROBABILITY_THREE_RANDOMLY_CHOSEN_NUMBERS_AP

def procal ( n ) :
    return ( 3.0 * n ) / ( 4.0 * ( n ** 2 ) - 1 )
|||

REMOVE_BRACKETS_ALGEBRAIC_STRING_CONTAINING_OPERATORS

def simplify ( str ) :
    len ( str )
    res = [ ]
    index , i = 0 , 0
    s = Stack ( )
    s.push ( 0 )
    while i < len ( str ) :
        if str [ i ] == '+' :
            if s.pop ( ) == 1 :
                res.append ( '-' )
            if s.pop ( ) == 0 :
                res.append ( '+' )
        elif str [ i ] == '-' :
            if s.pop ( ) == 1 :
                res.append ( '+' )
            elif s.pop ( ) == 0 :
                res.append ( '-' )
        elif str [ i ] == '(' and i > 0 :
            if str [ i - 1 ] == '-' :
                x = ( s.pop ( ) == 1 )
                s.push ( x )
            elif str [ i - 1 ] == '+' :
                s.push ( s.pop ( ) )
        elif str [ i ] == ')' :
            s.pop ( )
        else :
            res.append ( str [ i ] )
        i += 1
    return ''.join ( res )
|||

FIND_NUMBER_PERFECT_SQUARES_TWO_GIVEN_NUMBERS

def count_squares ( a , b ) :
    cnt = 0
    for i in range ( a , b + 1 ) :
        for j in range ( 1 , j ** 2 ) :
            if j ** 2 == i :
                cnt += 1
    return cnt
|||

K_NUMBERS_DIFFERENCE_MAXIMUM_MINIMUM_K_NUMBER_MINIMIZED

def min_diff ( arr , n , k ) :
    result = int ( 0 )
    arr.sort ( )
    for i in range ( 0 , n - k ) :
        result = min ( result , arr [ i + k - 1 ] - arr [ i ] )
    return result
|||

CHECK_LARGE_NUMBER_DIVISIBLE_13_NOT

def checkDivisibility ( num ) :
    length = len ( num )
    if length == 1 and num [ 0 ] == '0' :
        return True
    if length % 3 == 1 :
        num += '00'
        length += 2
    elif length % 3 == 2 :
        num += '0'
        length += 1
    sum , p = 0 , 1
    for i in range ( length - 1 , - 1 , - 1 ) :
        group = 0
        group += num [ i ] - '0'
        group += ( num [ i ] - '0' ) * 10
        group += ( num [ i ] - '0' ) * 100
        sum = sum + group * p
        p *= ( - 1 )
    sum = abs ( sum )
    return ( sum % 13 == 0 )
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
                print ( sum , end = ' ' )
            print ( )
|||

FIND_THE_POINT_WHERE_MAXIMUM_INTERVALS_OVERLAP_1

def max_overlap ( start , end , n ) :
    maxa = sum ( [ x for x in start if x != end ] )
    maxb = sum ( [ x for x in end if x != start ] )
    maxc = max ( [ maxa , maxb ] )
    x = [ 0 ] * ( maxc + 2 )
    cur , idx = 0 , 0
    for i in range ( n ) :
        yield x [ start [ i ] ]
        del x [ end [ i ] + 1 ]
    maxy = int ( 0 )
    for i in range ( 0 , maxc ) :
        cur += x [ i ]
        if maxy < cur :
            maxy = cur
            idx = i
    print ( "Maximum value is:" , maxy , " at position: " , idx , "" )
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
|||

C_PROGRAM_ADDITION_TWO_MATRICES

def add ( A , B , C ) :
    i , j = 0 , 0
    for i in range ( N ) :
        for j in range ( N ) :
            C [ i , j ] = A [ i , j ] + B [ i , j ]
|||

FIND_MAXIMUM_AVERAGE_SUBARRAY_OF_K_LENGTH_1

def find_max_average ( arr , n , k ) :
    if k > n :
        return - 1
    sum = arr [ 0 ]
    for i in range ( k ) :
        sum += arr [ i ]
    max_sum , max_end = sum , k - 1
    for i in range ( k , n ) :
        sum = sum + arr [ i ] - arr [ i - k ]
        if sum > max_sum :
            max_sum = sum
            max_end = i
    return max_end - k + 1
|||

FIND_CENTER_CIRCLE_USING_ENDPOINTS_DIAMETER

def center ( x1 , x2 , y1 , y2 ) :
    print ( float ( x1 + x2 ) / 2 , float ( y1 + y2 ) / 2 )
|||

TOTAL_NUMBER_OF_NON_DECREASING_NUMBERS_WITH_N_DIGITS

def count_non_decreasing ( n ) :
    dp = { }
    for i in range ( 10 ) :
        dp [ i ] [ 1 ] = 1
    for digit in range ( 0 , 9 ) :
        for len in range ( 2 , n + 1 ) :
            for x in range ( 0 , digit ) :
                dp [ digit ] [ len ] += dp [ x ] [ len - 1 ]
    count = 0
    for i in range ( 10 ) :
        count += dp [ i ] [ n ]
    return count
|||

PRINT_REVERSE_STRING_REMOVING_VOWELS

def replace_original ( s , n ) :
    r = [ s [ n - 1 - i ] for i in range ( n ) ]
    if s [ i ] not in [ 'a' , 'e' , 'i' , 'o' , 'u' ] :
        print ( r [ i ] )
|||

FIND_ELEMENTS_PRESENT_FIRST_ARRAY_NOT_SECOND_1

def find_missing ( a , b , n , m ) :
    s = set ( )
    for i in range ( m ) :
        s.add ( b [ i ] )
    for i in range ( n ) :
        if not s.intersection ( a [ i ] ) :
            print ( a [ i ] , end = ' ' )
|||

COUNT_STRINGS_CAN_FORMED_USING_B_C_GIVEN_CONSTRAINTS

def count_str ( n , b_count , c_count ) :
    if b_count < 0 or c_count < 0 :
        return 0
    if n == 0 :
        return 1
    if b_count == 0 and c_count == 0 :
        return 1
    res = count_str ( n - 1 , b_count , c_count )
    res += count_str ( n - 1 , b_count - 1 , c_count )
    res += count_str ( n - 1 , b_count , c_count - 1 )
    return res
|||

GOLD_MINE_PROBLEM

def getMaxGold ( gold , m , n ) :
    goldTable = [ [ 0 ] * m , [ 0 ] * n ]
    for rows in goldTable :
        del rows [ 0 ]
    for col in range ( n - 1 , - 1 , - 1 ) :
        for row in range ( m ) :
            right = ( col == n - 1 )
            right_up = ( row == 0 or col == n - 1 )
            right_down = ( row == m - 1 or col == n - 1 )
            goldTable [ row ] [ col ] = gold [ row ] [ col ] + max ( right , max ( right_up , right_down ) ) ;
    res = goldTable [ 0 ] [ 0 ]
    for i in range ( 1 , m ) :
        res = max ( res , goldTable [ i ] [ 0 ] )
    return res
|||

COUNT_WAYS_BUILD_STREET_GIVEN_CONSTRAINTS

def countWays ( n ) :
    dp = [ [ 0 ] * n + [ 1 ] * n + [ 2 ] * n + [ 3 ] * n + [ 4 ] * n + [ 5 ] * n + [ 6 ] * n + [ 7 ] * n + [ 8 ] * n + [ 9 ] * n + [ 10 ] * n + [ 11 ] * n + [ 12 ] * n + [ 13 ] * n + [ 14 ] * n + [ 15 ] * n + [ 16 ] * n + [ 17 ] * n + [ 18 ] * n + [ 19 ] * n + [ 20 ] * n + [ 21 ] * n + [ 22 ] * n + [ 23 ] * n + [ 24 ] * n + [ 25 ] * n + [ 26 ] * n + [ 27 ] * n + [ 28 ] * n + [ 29 ] * n + [ 30 ] * n + [ 31 ] * n + [ 32 ] * n + [ 33 ] * n + [ 34 ] * n + [ 35 ] * n + [ 36 ] * n + [ 37 ] * n + [ 38 ] * n + [ 39 ] * n + [ 40 ] * n + [ 41 ] * n + [ 42 ] * n + [ 39 ] * n + [ 42 ] * n + [ 39 ] * n + [ 40 ] * n + [ 41 ] * n + [ 42 ] * n + [ 39 ] * n + [ 41 ] * n + [ 42 ] * n + [ 39 ] * n + [ 41 ] * n + [ 42 ] * n + [ 39 ] * n + [ 39 ] * n + [ 41 ] * n + [ 42 ] * n + [ 39 ] * n + [ 39 ] * n + [ 39 ] * n + [ 39 ] * n + [ 39 ] * n + [ 39 ] * n + [ 39 ] * n + [ 39 ] * n + [ 39 ] * n + [ 39 ] * n + [ 39 ] * n + [
|||

RETURN_A_PAIR_WITH_MAXIMUM_PRODUCT_IN_ARRAY_OF_INTEGERS_1

def max_product ( arr , n ) :
    if n < 2 :
        print ( "No pairs exists" )
        return
    if n == 2 :
        print ( arr [ 0 ] , arr [ 1 ] )
        return
    posa , posb = int ( arr [ 0 ] ) , int ( arr [ 1 ] )
    nega , negb = int ( arr [ 0 ] ) , int ( arr [ 1 ] )
    for i in range ( n ) :
        if arr [ i ] > posa :
            posb = posa
            posa = arr [ i ]
        elif arr [ i ] > posb :
            posb = arr [ i ]
        if arr [ i ] < 0 and abs ( arr [ i ] ) > abs ( nega ) :
            negb = nega
            nega = arr [ i ]
        elif arr [ i ] < 0 and abs ( arr [ i ] ) > abs ( negb ) :
            negb = arr [ i ]
    if nega * negb > posa * posb :
        print ( """
                Max product pair is {
                    %d, %d}
                    """ % ( nega , negb ) )
    else :
        print ( """
                 Max product pair is {
                     %d, %d}""" % ( posa , posb ) )
|||

POSITION_OF_RIGHTMOST_SET_BIT

def get_first_set_bit_pos ( n ) :
    return int ( ( math.log10 ( n & - n ) ) / math.log10 ( 2 ) ) + 1
|||

LONGEST_SUBSEQUENCE_WHERE_EVERY_CHARACTER_APPEARS_AT_LEAST_K_TIMES

def longest_subseq_with_k ( str , k ) :
    n = len ( str )
    freq = [ 0 for i in range ( n ) ]
    for i in range ( n ) :
        if freq [ str [ i ] - 'a' ] >= k :
            print ( str [ i ] )
|||

POSSIBLE_TO_MAKE_A_DIVISIBLE_BY_3_NUMBER_USING_ALL_DIGITS_IN_AN_ARRAY

def is_possible_to_make_divisible ( arr , n ) :
    remainder = 0
    for i in range ( n ) :
        remainder = ( remainder + arr [ i ] ) % 3
    return ( remainder == 0 )
|||

AREA_SQUARE_CIRCUMSCRIBED_CIRCLE

def find_Area ( r ) :
    return ( 2 * r ** 2 )
|||

FIND_MAXIMUM_DOT_PRODUCT_TWO_ARRAYS_INSERTION_0S

def MaxDotProduct ( A , B , m , n ) :
    dp = [ 0 ] * ( n + 1 )
    for row in dp :
        np.random.shuffle ( row )
    for i in range ( 1 , n + 1 ) :
        for j in range ( i , m + 1 ) :
            dp [ i ] [ j ] = max ( ( dp [ i - 1 ] [ j - 1 ] + ( A [ j - 1 ] * B [ i - 1 ] ) ) , dp [ i ] [ j - 1 ] )
    return dp [ n ] [ m ]
|||

FIND_DISTINCT_SUBSET_SUBSEQUENCE_SUMS_ARRAY

def print_dist_sum ( arr , n ) :
    sum = 0
    for i in range ( n ) :
        sum += arr [ i ]
    dp = [ [ False ] * ( n + 1 ) + [ sum + 1 ] * ( n + 1 ) for i in range ( n + 1 ) ]
    for i in range ( 0 , n + 1 ) :
        dp [ i ] [ 0 ] = True
    for i in range ( 1 , n + 1 ) :
        dp [ i ] [ arr [ i - 1 ] ] = True
        for j in range ( 1 , sum + 1 ) :
            if dp [ i - 1 ] [ j ] == True :
                dp [ i ] [ j ] = True
                dp [ i ] [ j + arr [ i - 1 ] ] = True
    for j in range ( 0 , sum + 1 ) :
        if dp [ n ] [ j ] == True :
            print ( j , end = ' ' )
|||

SPLIT_NUMERIC_ALPHABETIC_AND_SPECIAL_SYMBOLS_FROM_A_STRING

def splitString ( str ) :
    alpha , num , special = [ ] , [ ] , [ ]
    for c in str :
        if ord ( c ) < 128 :
            num.append ( c )
        elif ord ( c ) > 127 :
            alpha.append ( c )
        else :
            special.append ( c )
    print ( alpha )
    print ( num )
    print ( special )
|||

MAXIMUM_SUM_ALTERNATING_SUBSEQUENCE_SUM

def max_alternate_sum ( arr , n ) :
    if n == 1 :
        return arr [ 0 ]
    dec = [ ]
    inc = [ ]
    dec = inc + [ arr [ 0 ] ]
    flag = 0
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if arr [ j ] > arr [ i ] :
                dec [ i ] = max ( dec [ i ] , inc [ j ] + arr [ i ] )
                flag = 1
            elif arr [ j ] < arr [ i ] and flag == 1 :
                inc [ i ] = max ( inc [ i ] , dec [ j ] + arr [ i ] )
    result = int ( '-' )
    for i in range ( n ) :
        if result < inc [ i ] :
            result = inc [ i ]
        if result < dec [ i ] :
            result = dec [ i ]
    return result
|||

FIND_PAIR_MAXIMUM_GCD_ARRAY

def find_max_gcd ( arr , n ) :
    high = 0
    for i in range ( n ) :
        high = max ( high , arr [ i ] )
    divisors = [ 0 ] * ( high + 1 )
    for i in range ( n ) :
        for j in range ( 1 , math.sqrt ( arr [ i ] ) ) :
            if arr [ i ] % j == 0 :
                divisors [ j ] += 1
                if j != arr [ i ] / j :
                    divisors [ arr [ i ] / j ] += 1
    for i in range ( high , 1 , - 1 ) :
        if divisors [ i ] > 1 :
            return i
    return 1
|||

FIND_MINIMUM_NUMBER_OF_COINS_THAT_MAKE_A_CHANGE_1

def minCoins ( coins , m , V ) :
    table = [ int ( i ) for i in range ( V + 1 ) ]
    for i in range ( 1 , V + 1 ) :
        table.append ( int ( coins [ i ] ) )
    for i in range ( 1 , V + 1 ) :
        for j in range ( m ) :
            if coins [ j ] <= i :
                sub_res = table [ i - coins [ j ] ]
                if sub_res != int ( i ) and sub_res + 1 < table [ i ] :
                    table [ i ] = sub_res + 1
    return table [ V ]
|||

SUM_NODES_K_TH_LEVEL_TREE_REPRESENTED_STRING

def sum_at_kth_level ( tree , k ) :
    level = - 1
    sum = 0
    n = len ( tree )
    for i in range ( n ) :
        if tree [ i ] == '(' :
            level += 1
        elif tree [ i ] == ')' :
            level -= 1
        else :
            if level == k :
                sum += ( tree [ i ] - '0' )
    return sum
|||

DYNAMIC_PROGRAMMING_SET_4_LONGEST_COMMON_SUBSEQUENCE

def lcs ( X , Y , m , n ) :
    if m == 0 or n == 0 :
        return 0
    if X [ m - 1 ] == Y [ n - 1 ] :
        return 1 + lcs ( X , Y , m - 1 , n - 1 )
    else :
        return max ( lcs ( X , Y , m , n - 1 ) , lcs ( X , Y , m - 1 , n ) )
|||

CHECK_GIVEN_SENTENCE_GIVEN_SET_SIMPLE_GRAMMER_RULES

def check_sentence ( str ) :
    len ( str )
    if str [ 0 ] < 'A' or str [ 0 ] > 'Z' :
        return False
    if str [ len ( str ) - 1 ] != '.' :
        return False
    prev_state , curr_state = 0 , 0
    index = 1
    while index <= len ( str ) :
        if str [ index ] >= 'A' and str [ index ] <= 'Z' :
            curr_state = 0
        elif str [ index ] == ' ' :
            curr_state = 1
        elif str [ index ] >= 'a' and str [ index ] <= 'z' :
            curr_state = 2
        elif str [ index ] == '.' :
            curr_state = 3
        if prev_state == curr_state and curr_state != 2 :
            return False
        if prev_state == 2 and curr_state == 0 :
            return False
        if curr_state == 3 and prev_state != 1 :
            return ( index + 1 , str [ index ] )
        index += 1
        prev_state , curr_state = curr_state , curr_state
    return False
|||

CHECK_DIVISIBILITY_LARGE_NUMBER_999

def isDivisible999 ( num ) :
    n = len ( num )
    if n == 0 and num [ 0 ] == '0' :
        return True
    if n % 3 == 1 :
        num = '00' + num
    if n % 3 == 2 :
        num = '0' + num
    gSum = 0
    for i in range ( n ) :
        group = 0
        group += ( num [ i ] - '0' ) * 100
        group += ( num [ i ] - '0' ) * 10
        group += num [ i ] - '0'
        gSum += group
    if gSum > 1000 :
        num = str ( gSum )
        n = len ( num )
        gSum = isDivisible999 ( num ) and 1 or 0
    return ( gSum == 999 )
|||

CHECK_LARGE_NUMBER_DIVISIBLE_9_NOT

def check ( str ) :
    n = len ( str )
    digitSum = 0
    for i in range ( n ) :
        digitSum += ( str [ i ] - '0' )
    return ( digitSum % 9 == 0 )
|||

NUMBER_OF_BINARY_TREES_FOR_GIVEN_PREORDER_SEQUENCE_LENGTH

def countTrees ( n ) :
    BT = [ 0 ] * ( n + 1 )
    for i in range ( 0 , n + 1 ) :
        BT [ i ] = 0
    BT [ 0 ] = BT [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        for j in range ( 0 , i + 1 ) :
            BT [ i ] += BT [ j ] * BT [ i - j - 1 ]
    return BT [ n ]
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
|||

FIND_SUM_MODULO_K_FIRST_N_NATURAL_NUMBER_1

def find_sum ( N , K ) :
    ans = 0
    y = N / K
    x = N % K
    ans = ( K * ( K - 1 ) / 2 ) * y + ( x * ( x + 1 ) ) / 2
    return ans
|||

WAYS_REMOVE_ONE_ELEMENT_BINARY_STRING_XOR_BECOMES_ZERO

def xorZero ( s ) :
    one_count , zero_count = 0 , 0
    str = s.split ( ' ' )
    n = len ( str )
    for i in range ( n ) :
        if str [ i ] == '1' :
            one_count += 1
        else :
            zero_count += 1
    if one_count % 2 == 0 :
        return zero_count
    return one_count
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
|||

MINIMUM_SUM_SUBSEQUENCE_LEAST_ONE_EVERY_FOUR_CONSECUTIVE_ELEMENTS_PICKED

def min_sum ( arr , n ) :
    dp = [ ]
    if n == 1 :
        return arr [ 0 ]
    if n == 2 :
        return min ( arr [ 0 ] , arr [ 1 ] )
    if n == 3 :
        return min ( arr [ 0 ] , min ( arr [ 1 ] , arr [ 2 ] ) )
    if n == 4 :
        return min ( min ( arr [ 0 ] , arr [ 1 ] ) , min ( arr [ 2 ] , arr [ 3 ] ) )
    dp.append ( arr [ 0 ] )
    dp.append ( arr [ 1 ] )
    dp.append ( arr [ 2 ] )
    dp.append ( arr [ 3 ] )
    for i in range ( 4 , n ) :
        dp.append ( arr [ i ] + min ( min ( dp [ i - 1 ] , dp [ i - 2 ] ) , min ( dp [ i - 3 ] , dp [ i - 4 ] ) ) )
    return min ( min ( dp [ - 1 ] , dp [ - 2 ] ) , min ( dp [ - 4 ] , dp [ - 3 ] ) )
|||

MAXIMUM_PATH_SUM_TRIANGLE

def max_path_sum ( tri , m , n ) :
    for i in range ( m - 1 , - 1 , - 1 ) :
        for j in range ( 0 , i + 1 ) :
            if tri [ i + 1 ] [ j ] > tri [ i + 1 ] [ j + 1 ] :
                tri [ i ] [ j ] += tri [ i + 1 ] [ j ]
            else :
                tri [ i ] [ j ] += tri [ i + 1 ] [ j + 1 ]
    return tri [ 0 ] [ 0 ]
|||

FIND_THREE_ELEMENT_FROM_DIFFERENT_THREE_ARRAYS_SUCH_THAT_THAT_A_B_C_K

def findTriplet ( a1 , a2 , a3 , n1 , n2 , n3 , sum ) :
    for i in range ( n1 ) :
        for j in range ( n2 ) :
            for k in range ( n3 ) :
                if a1 [ i ] + a2 [ j ] + a3 [ k ] == sum :
                    return True
    return False
|||

TAIL_RECURSION_FIBONACCI

def fib ( n , a , b ) :
    if n == 0 :
        return a
    if n == 1 :
        return b
    return fib ( n - 1 , b , a + b )
|||

PROGRAM_TO_CHECK_IF_A_GIVEN_NUMBER_IS_LUCKY_ALL_DIGITS_ARE_DIFFERENT

def isLucky ( n ) :
    arr = [ ]
    for i in range ( 10 ) :
        arr.append ( False )
    while n > 0 :
        digit = n % 10
        if arr [ digit ] :
            return False
        arr.append ( True )
        n = n / 10
    return True
|||

GIVEN_N_X_N_SQUARE_MATRIX_FIND_SUM_SUB_SQUARES_SIZE_K_X_K_1

def printSumTricky ( mat , k ) :
    if k > n :
        return
    stripSum = [ [ 0 ] * n for n in range ( n ) ]
    for j in range ( n ) :
        sum = 0
        for i in range ( k ) :
            sum += mat [ i ] [ j ]
        stripSum [ 0 ] [ j ] = sum
        for i in range ( 1 , n - k + 1 ) :
            sum += ( mat [ i + k - 1 ] [ j ] - mat [ i - 1 ] [ j ] )
            stripSum [ i ] [ j ] = sum
    for i in range ( n - k + 1 ) :
        sum = 0
        for j in range ( k ) :
            sum += stripSum [ i ] [ j ]
        print ( sum , end = ' ' )
        for j in range ( 1 , n - k + 1 ) :
            sum += ( stripSum [ i ] [ j + k - 1 ] - stripSum [ i ] [ j - 1 ] )
            print ( sum , end = ' ' )
        print ( )
|||

SCHEDULE_ELEVATOR_TO_REDUCE_THE_TOTAL_TIME_TAKEN

def minTime ( n , k , a ) :
    temp = 0
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if a [ i ] < a [ j ] :
                temp = a [ i ]
                a [ i ] , a [ j ] = a [ j ] , a [ i ]
                a [ j ] = temp
    minTime = 0
    for i in range ( 0 , n , k ) :
        minTime += ( 2 * a [ i ] )
    return minTime
|||

ODD_EVEN_SORT_BRICK_SORT

def oddEvenSort ( arr , n ) :
    isSorted = False
    while not isSorted :
        isSorted = True
        temp = 0
        for i in range ( 1 , n - 2 + 1 , 2 ) :
            if arr [ i ] > arr [ i + 1 ] :
                temp = arr [ i ]
                arr [ i ] , arr [ i + 1 ] = arr [ i + 1 ] , arr [ i + 1 ]
                isSorted = False
        for i in range ( 0 , n - 2 + 1 , 2 ) :
            if arr [ i ] > arr [ i + 1 ] :
                temp = arr [ i ]
                arr [ i ] , arr [ i + 1 ] = arr [ i + 1 ] , arr [ i + 1 ]
                isSorted = False
    return
|||

RETURN_MAXIMUM_OCCURRING_CHARACTER_IN_THE_INPUT_STRING

def getMaxOccuringChar ( str ) :
    count = [ 0 ] * ASCII_SIZE
    len = len ( str )
    for c in str :
        count [ c ] += 1
    max = - 1
    result = ' '
    for c in str :
        if max < count [ c ] :
            max = count [ c ]
            result = c
    return result
|||

COUNT_NUMBER_PAIRS_N_B_N_GCD_B_B

def CountPairs ( n ) :
    k = n
    imin = 1
    ans = 0
    while imin <= n :
        imax = n // k
        ans += k * ( imax - imin + 1 )
        imin = imax + 1
        k = n // imin
    return ans
|||

K_TH_DISTINCT_OR_NON_REPEATING_ELEMENT_IN_AN_ARRAY_1

def printKDistinct ( arr , n , k ) :
    h = { }
    for i in range ( n ) :
        if h.has_key ( arr [ i ] ) :
            h [ arr [ i ] ] = h [ arr [ i ] ] + 1
        else :
            h [ arr [ i ] ] = 1
    if len ( h ) < k :
        return - 1
    dist_count = 0
    for i in range ( n ) :
        if h [ arr [ i ] ] == 1 :
            dist_count += 1
        if dist_count == k :
            return arr [ i ]
    return - 1
|||

GENERATE_BINARY_PERMUTATIONS_1S_0S_EVERY_POINT_PERMUTATIONS

def generate ( ones , zeroes , str , len ) :
    if len == len ( str ) :
        print ( str , end = ' ' )
        return
    generate ( ones + 1 , zeroes , str + '1' , len )
    if ones > zeroes :
        generate ( ones , zeroes + 1 , str + '0' , len )
|||

SEARCH_INSERT_AND_DELETE_IN_AN_UNSORTED_ARRAY

def findElement ( arr , n , key ) :
    for i in range ( n ) :
        if arr [ i ] == key :
            return i
    return - 1
|||

LCS_LONGEST_COMMON_SUBSEQUENCE_THREE_STRINGS

def lcsOf3 ( X , Y , Z , m , n , o ) :
    L = [ [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * n + [ 0 ] * o + [ 0 ] * m + [ 0 ] * m +
|||

MAXIMUM_SUM_SUBARRAY_REMOVING_ONE_ELEMENT

def max_sum_subarray_removing_one_ele ( arr , n ) :
    fw = [ ]
    bw = [ ]
    cur_max , max_so_far = arr [ 0 ] , arr [ 0 ]
    fw.append ( arr [ 0 ] )
    for i in range ( 1 , n ) :
        cur_max = max ( arr [ i ] , cur_max + arr [ i ] )
        max_so_far = max ( max_so_far , cur_max )
        fw.append ( cur_max )
    cur_max = max_so_far = bw [ - 1 ] = arr [ n - 1 ]
    for i in range ( n - 2 , - 1 , - 1 ) :
        cur_max = max ( arr [ i ] , cur_max + arr [ i ] )
        max_so_far = max ( max_so_far , cur_max )
        bw.append ( cur_max )
    fans = max_so_far
    for i in range ( 1 , n - 1 , - 1 ) :
        fans = max ( fans , fw [ i - 1 ] + bw [ i + 1 ] )
    return fans
|||

COUNT_NUMBER_WAYS_TILE_FLOOR_SIZE_N_X_M_USING_1_X_M_SIZE_TILES

def countWays ( n , m ) :
    count = [ 0 ] * ( n + 1 )
    i = 0
    for i in range ( 1 , n + 1 ) :
        if i > m :
            count [ i ] = count [ i - 1 ] + count [ i - m ]
        elif i < m :
            count [ i ] = 1
        else :
            count [ i ] = 2
    return count [ n ]
|||

MIDDLE_OF_THREE_USING_MINIMUM_COMPARISONS

def middle_of_three ( a , b , c ) :
    if ( a < b and b < c ) or ( c < b and b < a ) :
        return b
    elif ( b < a and a < c ) or ( c < a and a < b ) :
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
            if arr1 [ i ] == arr2 [ j ] :
                if current + 1 > table [ j ] :
                    table [ j ] = current + 1
                if arr1 [ i ] > arr2 [ j ] :
                    if table [ j ] > current :
                        current = table [ j ]
    result = 0
    for i in range ( m ) :
        if table [ i ] > result :
            result = table [ i ]
    return result
|||

MAXIMUM_SUBSEQUENCE_SUM_SUCH_THAT_NO_THREE_ARE_CONSECUTIVE

def max_sum_wo3_consec ( arr , n ) :
    sum = [ ]
    if n >= 1 :
        sum.append ( arr [ 0 ] )
    if n >= 2 :
        sum.append ( arr [ 0 ] + arr [ 1 ] )
    if n > 2 :
        sum.append ( max ( sum [ 1 : ] , max ( arr [ 1 : ] + arr [ 2 : ] , arr [ 0 ] + arr [ 2 ] ) ) )
    for i in range ( 3 , n ) :
        sum.append ( max ( max ( sum [ i - 1 ] , sum [ i - 2 ] + arr [ i ] ) , arr [ i ] + arr [ i - 1 ] + sum [ i - 3 ] ) )
    return sum [ - 1 ]
|||

EULERIAN_NUMBER_1

def eulerian ( n , m ) :
    dp = [ [ 0 ] * n + [ 0 ] * m + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] *
|||

DOUBLE_FACTORIAL

def doublefactorial ( n ) :
    if n == 0 or n == 1 :
        return 1
    return n * doublefactorial ( n - 2 )
|||

REARRANGE_POSITIVE_AND_NEGATIVE_NUMBERS_PUBLISH

def rearrange ( arr , n ) :
    i , temp = - 1 , 0
    for j in range ( n ) :
        if arr [ j ] < 0 :
            i += 1
            temp = arr [ i ]
            arr [ i ] , arr [ j ] = arr [ j ] , temp
    pos , neg = i + 1 , 0
    while pos < n and neg < pos and arr [ neg ] < 0 :
        temp = arr [ neg ]
        arr [ neg ] , arr [ pos ] = arr [ pos ] , temp
        pos += 1
        neg += 2
|||

MAXIMIZE_ARRAY_SUN_AFTER_K_NEGATION_OPERATIONS

def maximum_sum ( arr , n , k ) :
    for i in range ( 1 , k + 1 ) :
        min = + 2147483647
        index = - 1
        for j in range ( n ) :
            if arr [ j ] < min :
                min = arr [ j ]
                index = j
        if min == 0 :
            break
        arr [ index ] = - arr [ index ]
    sum = 0
    for i in range ( n ) :
        sum += arr [ i ]
    return sum
|||

MAXIMUM_SUM_INCREASING_SUBSEQUENCE_FROM_A_PREFIX_AND_A_GIVEN_ELEMENT_AFTER_PREFIX_IS_MUST

def pre_compute ( a , n , index , k ) :
    dp = [ [ ] for i in range ( n ) ]
    for i in range ( n ) :
        if a [ i ] > a [ 0 ] :
            dp [ 0 ].append ( a [ i ] + a [ 0 ] )
        else :
            dp [ 0 ].append ( a [ i ] )
    for i in range ( 1 , n ) :
        for j in range ( n ) :
            if a [ j ] > a [ i ] and j > i :
                if dp [ i - 1 ] [ i ] + a [ j ] > dp [ i - 1 ] [ j ] :
                    dp [ i ].append ( dp [ i - 1 ] [ i ] + a [ j ] )
                else :
                    dp [ i ].append ( dp [ i - 1 ] [ j ] )
            else :
                dp [ i ].append ( dp [ i - 1 ] [ j ] )
    return dp [ index ] [ k ]
|||

FUNCTION_COPY_STRING_ITERATIVE_RECURSIVE

def my_copy ( s1 , s2 ) :
    i = 0
    for c in s1 :
        s2 [ i ] = c
|||

GIVEN_TWO_STRINGS_FIND_FIRST_STRING_SUBSEQUENCE_SECOND_1

def isSubSequence ( str1 , str2 , m , n ) :
    j = 0
    for i in range ( n and j < m ) :
        if str1 [ j ] == str2 [ i ] :
            j += 1
    return ( j == m )
|||

FIND_UNIT_DIGIT_X_RAISED_POWER_Y_1

def unitnumber ( x , y = None ) :
    x = x % 10
    if y is not None :
        y = y % 4 + 4
    return ( ( ( int ( math.pow ( x , y ) ) ) % 10 ) , ( ( int ( math.pow ( x , y ) ) ) % 10 ) , ( ( int ( math.pow ( x , y ) ) ) % 10 ) , ( ( int ( math.pow ( x , y ) ) ) % 10 ) , ( ( int ( math.pow ( x , y ) ) ) % 10 ) , ( ( int ( math.pow ( x , y ) ) ) % 10 ) , ( ( int ( math.pow ( x , y ) ) ) % 10 ) , ( ( int ( math.pow ( x , y )
|||

PROGRAM_NEXT_FIT_ALGORITHM_MEMORY_MANAGEMENT

def NextFit ( blockSize , m , processSize , n ) :
    allocation , j = [ - 1 ] , 0
    print ( "\nProcess No.\tProcess Size\tBlock no.\n" )
    for i in range ( n ) :
        while j < m :
            if blockSize [ j ] >= processSize [ i ] :
                allocation [ i ] = j
                blockSize [ j ] -= processSize [ i ]
                break
            j = ( j + 1 ) % m
    print ( "\nProcess Size.\tProcess Size.\n" )
    for i in range ( n ) :
        print ( i + 1 , "\t\t" , processSize [ i ] , "\t\t" )
        if allocation [ i ] != - 1 :
            print ( allocation [ i ] + 1 )
        else :
            print ( "Not Allocated" )
        print ( "" )
|||

NOBLE_INTEGERS_IN_AN_ARRAY_COUNT_OF_GREATER_ELEMENTS_IS_EQUAL_TO_VALUE

def noble_integer ( arr ) :
    size = len ( arr )
    for i in range ( size ) :
        count = 0
        for j in range ( size ) :
            if arr [ i ] < arr [ j ] :
                count += 1
        if count == arr [ i ] :
            return arr [ i ]
    return - 1
|||

MINIMUM_FLIP_REQUIRED_MAKE_BINARY_MATRIX_SYMMETRIC

def minimumflip ( mat , n ) :
    transpose = [ ]
    for i in range ( n ) :
        for j in range ( n ) :
            transpose.append ( mat [ j ] [ i ] )
    flip = 0
    for i in range ( n ) :
        for j in range ( n ) :
            if transpose [ i ] [ j ] != mat [ i ] [ j ] :
                flip += 1
    return flip / 2
|||

SEGREGATE_EVEN_ODD_NUMBERS_SET_3

def array_even_and_odd ( arr , n ) :
    i , j = - 1 , 0
    while j != n :
        if arr [ j ] % 2 == 0 :
            i += 1
            temp = arr [ i ]
            arr [ i ] , arr [ j ] = arr [ j ] , temp
        j += 1
    for k in range ( n ) :
        print ( arr [ k ] , end = ' ' )
|||

DFS_N_ARY_TREE_ACYCLIC_GRAPH_REPRESENTED_ADJACENCY_LIST

def dfs ( list , node , arrival ) :
    print ( node )
    for i in range ( len ( list [ node ] ) ) :
        if list [ node ] [ i ] != arrival :
            dfs ( list , list [ node ] [ i ] , node )
|||

HOW_TO_TURN_OFF_A_PARTICULAR_BIT_IN_A_NUMBER

def turnOffK ( n , k ) :
    if k <= 0 :
        return n
    return ( n & ~ ( 1 << ( k - 1 ) ) )
|||

NUMBER_SUBSTRINGS_DIVISIBLE_8_NOT_3

def count ( s , len ) :
    MAX = 1000
    cur , dig = 0 , 0
    sum = [ 0 ] * MAX
    dp = [ [ 0 ] * MAX , [ 0 ] * 3 ]
    dp [ 0 ] [ 0 ] = 1
    for i in range ( 1 , len ) :
        dig = ord ( s [ i - 1 ] ) - 48
        cur += dig
        cur %= 3
        sum [ i ] = cur
        dp [ i ] [ 0 ] = dp [ i - 1 ] [ 0 ]
        dp [ i ] [ 1 ] = dp [ i - 1 ] [ 1 ]
        dp [ i ] [ 2 ] = dp [ i - 1 ] [ 2 ]
        dp [ i ] [ sum [ i ] ] += 1
    ans , dprev , value , dprev2 = 0 , 0 , 0 , 0
    for i in range ( 1 , len ) :
        dig = ord ( s [ i - 1 ] ) - 48
        if dig == 8 :
            ans += 1
        if i - 2 >= 0 :
            dprev = ord ( s [ i - 2 ] ) - 48
            value = dprev * 10 + dig
            if ( value % 8 == 0 ) :
                ans += 1
        if i - 3 >= 0 :
            dprev2 = ord ( s [ i - 3 ] ) - 48
            dprev = ord ( s [ i - 2 ] ) - 48
            value = dprev2 * 100 + dprev * 10 + dig
            if value % 8 != 0 :
                continue
            ans += ( i - 2 )
            ans -= ( dp [ i - 3 ] [ sum [ i ] ] )
    return ans
|||

ADD_1_TO_A_GIVEN_NUMBER_1

def add_one ( x ) :
    return ( - ( ~ x ) )
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
|||

FIND_FIRST_REPEATING_ELEMENT_ARRAY_INTEGERS

def print_first_repeating ( arr ) :
    min = - 1
    set = set ( )
    for i in range ( len ( arr ) - 1 , - 1 , - 1 ) :
        if set.intersection ( arr [ i ] ) :
            min = i
        else :
            set.add ( arr [ i ] )
    if min != - 1 :
        print ( "The first repeating element is " + str ( arr [ min ] ) )
    else :
        print ( "There are no repeating elements" )
|||

COST_BALANCE_PARANTHESES

def costToBalance ( s ) :
    if len ( s ) == 0 :
        print ( 0 )
    ans = 0
    o , c = 0 , 0
    for c in s :
        if c == '(' :
            o += 1
        if c == ')' :
            c += 1
    if o != c :
        return - 1
    a = [ ]
    if s [ 0 ] == '(' :
        a.append ( 1 )
    else :
        a.append ( - 1 )
    if a [ 0 ] < 0 :
        ans += abs ( a [ 0 ] )
    for i in range ( 1 , len ( s ) ) :
        if s [ i ] == '(' :
            a.append ( a [ i - 1 ] + 1 )
        else :
            a.append ( a [ i - 1 ] - 1 )
        if a [ i ] < 0 :
            ans += abs ( a [ i ] )
    return ans
|||

COIN_GAME_WINNER_EVERY_PLAYER_THREE_CHOICES

def find_winner ( x , y , n ) :
    dp = [ False ] * ( n + 1 )
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
|||

SEQUENCES_GIVEN_LENGTH_EVERY_ELEMENT_EQUAL_TWICE_PREVIOUS

def getTotalNumberOfSequences ( m , n ) :
    if m < n :
        return 0
    if n == 0 :
        return 1
    return getTotalNumberOfSequences ( m - 1 , n ) + getTotalNumberOfSequences ( m / 2 , n - 1 )
|||

FIND_DUPLICATES_GIVEN_ARRAY_ELEMENTS_NOT_LIMITED_RANGE

def _print_duplicates ( arr , n ) :
    d = { }
    count = 0
    dup = False
    for i in range ( n ) :
        if d.has_key ( arr [ i ] ) :
            count = d [ arr [ i ] ]
            d [ arr [ i ] ] = count + 1
        else :
            d [ arr [ i ] ] = 1
    for key , value in d.items ( ) :
        if value > 1 :
            print ( key , end = ' ' )
            dup = True
    if not dup :
        print ( '-1' )
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
            temp = temp / 10
        if cur == sum :
            count += 1
            i += 9
        else :
            i += 1
    print ( count )
|||

MINIMUM_COST_CONNECT_WEIGHTED_NODES_REPRESENTED_ARRAY

def minimum_cost ( a , n ) :
    mn = sys.maxint
    sum = 0
    for i in range ( n ) :
        mn = min ( a [ i ] , mn )
        sum += a [ i ]
    return mn * ( sum - mn )
|||

FIND_ALL_DIVISORS_OF_A_NATURAL_NUMBER_SET_2

def print_divisors ( n ) :
    v = [ ]
    for i in range ( 1 , math.sqrt ( n ) + 1 ) :
        if n % i == 0 :
            if n / i == i :
                print ( i , end = ' ' )
            else :
                print ( i , end = ' ' )
                v.append ( n / i )
    for i in range ( len ( v ) - 1 , - 1 , - 1 ) :
        print ( v [ i ] , end = ' ' )
|||

SQUARES_OF_MATRIX_DIAGONAL_ELEMENTS_1

def diagonalsquare ( mat , row , column ) :
    print ( " Diagonal one : " , end = ' ' )
    for i in range ( row ) :
        print ( mat [ i ] [ i ] * mat [ i ] [ i ] + " " , end = ' ' )
    print ( )
    print ( " Diagonal two : " , end = ' ' )
    for i in range ( row ) :
        print ( mat [ i ] [ row - i - 1 ] * mat [ i ] [ row - i - 1 ] + " " , end = ' ' )
|||

C_PROGRAM_FIND_AREA_TRIANGLE_1

def polygon_area ( X , Y , n ) :
    area = 0.0
    j = n - 1
    for i in range ( n ) :
        area += ( X [ j ] + X [ i ] ) * ( Y [ j ] - Y [ i ] )
        j = i
    return abs ( area / 2.0 )
|||

RANGE_QUERIES_FOR_FREQUENCIES_OF_ARRAY_ELEMENTS

def find_frequency ( arr , n , left , right , element ) :
    count = 0
    for i in range ( left - 1 , right ) :
        if arr [ i ] == element :
            count += 1
    return count
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
            if x <= b and x > r :
                r = x
            if n // x <= b and n // x > r :
                r = n // x
        for i in range ( 1 , k ) :
            print ( r * i + ' ' )
        res = n - ( r * ( k * ( k - 1 ) // 2 ) )
        print ( res )
|||

FIND_THREE_ELEMENT_FROM_DIFFERENT_THREE_ARRAYS_SUCH_THAT_THAT_A_B_C_K_1

def findTriplet ( a1 , a2 , a3 , n1 , n2 , n3 , sum ) :
    s = set ( )
    for i in range ( n1 ) :
        s.add ( a1 [ i ] )
    al = [ s [ i ] for i in range ( n2 ) ]
    for i in range ( n3 ) :
        for j in range ( n1 ) :
            if al.count ( sum - a2 [ i ] - a3 [ j ] ) & al.count ( sum - a2 [ i ] - a3 [ j ] ) != al [ - 1 ] :
                return True
    return False
|||

FIND_THE_MAXIMUM_ELEMENT_IN_AN_ARRAY_WHICH_IS_FIRST_INCREASING_AND_THEN_DECREASING_1

def findMaximum ( arr , low , high ) :
    if low == high :
        return arr [ low ]
    if ( high == low + 1 ) and arr [ low ] >= arr [ high ] :
        return arr [ low ]
    if ( high == low + 1 ) and arr [ low ] < arr [ high ] :
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

def fib ( n ) :
    if lookup [ n ] == NIL :
        if n <= 1 :
            lookup [ n ] = n
        else :
            lookup [ n ] = fib ( n - 1 ) + fib ( n - 2 )
    return lookup [ n ]
|||

MODULAR_EXPONENTIATION_POWER_IN_MODULAR_ARITHMETIC

def power ( x , y , p ) :
    res = 1
    x = x % p
    while y :
        if ( y & 1 ) == 1 :
            res = ( res * x ) % p
        y = y >> 1
        x = ( x * x ) % p
    return res
|||

WRITE_ONE_LINE_C_FUNCTION_TO_FIND_WHETHER_A_NO_IS_POWER_OF_TWO_1

def isPowerOfTwo ( x ) :
    return x != 0 and ( ( x & ( x - 1 ) ) == 0 )
|||

LONGEST_COMMON_SUBSEQUENCE_WITH_PERMUTATIONS_ALLOWED

def longest_string ( str1 , str2 ) :
    count1 , count2 = [ 0 ] * 26 , [ 0 ] * 26
    for i in range ( len ( str1 ) ) :
        count1 [ str1 [ i ] - 'a' ] += 1
    for i in range ( len ( str2 ) ) :
        count2 [ str2 [ i ] - 'a' ] += 1
    result = ""
    for i in range ( 26 ) :
        for j in range ( 1 , min ( count1 [ i ] , count2 [ i ] ) + 1 ) :
            result += chr ( 'a' + str ( i ) )
    print ( result )
|||

DIFFERENCE_MAXIMUM_SUM_MINIMUM_SUM_N_M_ELEMENTSIN_REVIEW

def find_difference ( arr , n , m ) :
    max , min = 0 , 0
    arr.sort ( )
    for i , j in enumerate ( arr ) :
        min += arr [ i ]
        max += arr [ j ]
    return ( max - min )
|||

PRINT_NUMBER_ASCENDING_ORDER_CONTAINS_1_2_3_DIGITS

def _print_numbers ( numbers ) :
    array = [ ]
    for number in numbers :
        if _find_contains_one_two_three ( number ) :
            array.append ( number )
    array.sort ( )
    strbuf = ''
    items = array.items ( )
    for item in items :
        value = int ( item [ 1 ] )
        if len ( strbuf ) > 0 :
            strbuf += ', '
        strbuf += str ( value )
    return ( strbuf ) or '-1'
|||

DYNAMIC_PROGRAMMING_SET_3_LONGEST_INCREASING_SUBSEQUENCE

def lis ( arr , n ) :
    global max_ref
    _lis ( arr , n )
    return max_ref
|||

MINIMUM_REVOLUTIONS_MOVE_CENTER_CIRCLE_TARGET

def min_revolutions ( r , x1 , y1 , x2 , y2 ) :
    d = np.sqrt ( ( x1 - x2 ) ** 2 + ( y1 - y2 ) ** 2 )
    return np.ceil ( d / ( 2 * r ) )
|||

CHECK_TWO_GIVEN_SETS_DISJOINT

def are_disjoint ( set1 , set2 ) :
    for i in range ( len ( set1 ) ) :
        for j in range ( len ( set2 ) ) :
            if set1 [ i ] == set2 [ j ] :
                return False
    return True
|||

FIND_MINIMUM_SUM_FACTORS_NUMBER

def find_min_sum ( num ) :
    sum = 0
    for i in range ( 2 , num * i <= num + 1 ) :
        while num % i == 0 :
            sum += i
            num /= i
    sum += num
    return sum
|||

FREQUENT_ELEMENT_ARRAY

def most_frequent ( arr , n ) :
    arr.sort ( )
    max_count , res = 1 , arr [ 0 ]
    curr_count = 1
    for i in range ( 1 , n ) :
        if arr [ i ] == arr [ i - 1 ] :
            curr_count += 1
        else :
            if curr_count > max_count :
                max_count = curr_count
                res = arr [ i - 1 ]
            curr_count = 1
    if curr_count > max_count :
        max_count = curr_count
        res = arr [ n - 1 ]
    return res
|||

MINIMUM_XOR_VALUE_PAIR_1

def minXOR ( arr , n ) :
    arr = np.array ( arr )
    minXor = np.inf
    val = 0
    for i in range ( n - 1 ) :
        val = arr [ i ] ^ arr [ i + 1 ]
        minXor = min ( minXor , val )
    return minXor
|||

MINIMUM_SUM_PRODUCT_TWO_ARRAYS

def minproduct ( a , b , n , k ) :
    diff , res = 0 , 0
    temp = 0
    for i in range ( n ) :
        pro = a [ i ] * b [ i ]
        res = res + pro
        if pro < 0 and b [ i ] < 0 :
            temp = ( a [ i ] + 2 * k ) * b [ i ]
        elif pro < 0 and a [ i ] < 0 :
            temp = ( a [ i ] - 2 * k ) * b [ i ]
        elif pro > 0 and a [ i ] < 0 :
            temp = ( a [ i ] + 2 * k ) * b [ i ]
        elif pro > 0 and a [ i ] > 0 :
            temp = ( a [ i ] - 2 * k ) * b [ i ]
        d = abs ( pro - temp )
        if d > diff :
            diff = d
    return res - diff
|||

FAST_MULTIPLICATION_METHOD_WITHOUT_USING_MULTIPLICATION_OPERATOR_RUSSIAN_PEASANTS_ALGORITHM

def russian_peasant ( a , b ) :
    res = 0
    while b :
        if ( b & 1 ) :
            res = res + a
        a = a << 1
        b = b >> 1
    return res
|||

DIVISIBILITY_9_USING_BITWISE_OPERATORS

def isDivBy9 ( n ) :
    if n == 0 or n == 9 :
        return True
    if n < 9 :
        return False
    return isDivBy9 ( int ( n >> 3 ) - int ( n & 7 ) )
|||

CHECK_ARRAY_REPRESENTS_INORDER_BINARY_SEARCH_TREE_NOT

def isInorder ( arr , n ) :
    if n == 0 or n == 1 :
        return True
    for i in range ( 1 , n ) :
        if arr [ i - 1 ] > arr [ i ] :
            return False
    return True
|||

GIVEN_TWO_UNSORTED_ARRAYS_FIND_PAIRS_WHOSE_SUM_X

def find_pairs ( arr1 , arr2 , n , m , x ) :
    for i in range ( n ) :
        for j in range ( m ) :
            if arr1 [ i ] + arr2 [ j ] == x :
                print ( arr1 [ i ] , arr2 [ j ] )
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
            num = num [ : i ] + '0' + num [ i + 1 : ]
    if i < 0 :
        num = '1' + num
    return num
|||

LARGEST_SUBARRAY_WITH_EQUAL_NUMBER_OF_0S_AND_1S

def findSubArray ( arr , n ) :
    sum = 0
    maxsize , startindex = - 1 , 0
    endindex = 0
    for i in range ( n - 1 ) :
        sum = ( arr [ i ] == 0 )
        for j in range ( i + 1 , n ) :
            if arr [ j ] == 0 :
                sum += - 1
            else :
                sum += 1
            if sum == 0 and maxsize < j - i + 1 :
                maxsize = j - i + 1
                startindex = i
    endindex = startindex + maxsize - 1
    if maxsize == - 1 :
        print ( "No such subarray" )
    else :
        print ( startindex , endindex )
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
            if Hash.intersection ( product ) :
                result += 1
    return result
|||

DYNAMIC_PROGRAMMING_SET_12_LONGEST_PALINDROMIC_SUBSEQUENCE

def lps ( seq ) :
    n = len ( seq )
    i , j , cl = 0 , 0 , 0
    L = [ [ 1 ] * n for i in range ( n ) ]
    for i in range ( n ) :
        L [ i ] [ i ] = 1
    for cl in range ( 2 , n + 1 ) :
        for i in range ( n - cl + 1 ) :
            j = i + cl - 1
            if seq [ i ] == seq [ j ] and cl == 2 :
                L [ i ] [ j ] = 2
            elif seq [ i ] == seq [ j ] :
                L [ i ] [ j ] = L [ i + 1 ] [ j - 1 ] + 2
            else :
                L [ i ] [ j ] = max ( L [ i ] [ j - 1 ] , L [ i + 1 ] [ j ] )
    return L [ 0 ] [ n - 1 ]
|||

COUNT_INVERSIONS_OF_SIZE_THREE_IN_A_GIVE_ARRAY_1

def getInvCount ( arr , n ) :
    invcount = 0
    for i in range ( n - 1 ) :
        small = 0
        for j in range ( i + 1 , n ) :
            if arr [ i ] > arr [ j ] :
                small += 1
        great = 0
        for j in range ( i - 1 , - 1 , - 1 ) :
            if arr [ i ] < arr [ j ] :
                great += 1
        invcount += great * small
    return invcount
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
            if pos_from_right % 4 == 1 :
                sum = sum + 2
            elif pos_from_right % 4 == 2 :
                sum = sum + 4
            elif pos_from_right % 4 == 3 :
                sum = sum + 8
            elif pos_from_right % 4 == 0 :
                sum = sum + 6
    if sum % 10 == 0 :
        return True
    return False
|||

FIND_WHETHER_AN_ARRAY_IS_SUBSET_OF_ANOTHER_ARRAY_SET_1_1

def issubset ( arr1 , arr2 , m , n ) :
    i , j = 0 , 0
    if m < n :
        return False
    arr1.sort ( )
    arr2.sort ( )
    while i < n and j < m :
        if arr1 [ j ] < arr2 [ i ] :
            j += 1
        elif arr1 [ j ] == arr2 [ i ] :
            j += 1
            i += 1
        elif arr1 [ j ] > arr2 [ i ] :
            return False
    if i < n :
        return False
    else :
        return True
|||

DYNAMIC_PROGRAMMING_SUBSET_SUM_PROBLEM_1

def is_subset_sum ( set , n , sum ) :
    subset = [ True for i in range ( sum + 1 ) ]
    for i in range ( 0 , n + 1 ) :
        subset [ 0 ] [ i ] = True
    for i in range ( 1 , sum + 1 ) :
        subset [ i ] [ 0 ] = False
    for i in range ( 1 , sum + 1 ) :
        for j in range ( 1 , n + 1 ) :
            subset [ i ] [ j ] = subset [ i ] [ j - 1 ]
            if i >= set [ j - 1 ] :
                subset [ i ] [ j ] = subset [ i ] [ j ] or subset [ i - set [ j - 1 ] ] [ j - 1 ]
    return subset [ sum ] [ n ]
|||

SUM_K_TH_GROUP_ODD_POSITIVE_NUMBERS_1

def kthgroupsum ( k ) :
    return k * k * k
|||

THIRD_LARGEST_ELEMENT_ARRAY_DISTINCT_ELEMENTS

def third_largest ( arr , arr_size ) :
    if arr_size < 3 :
        print ( " Invalid Input " )
        return
    first = arr [ 0 ]
    for i in range ( 1 , arr_size ) :
        if arr [ i ] > first :
            first = arr [ i ]
    second = int ( first )
    for i in range ( arr_size ) :
        if arr [ i ] > second and arr [ i ] < first :
            second = arr [ i ]
    third = int ( second )
    for i in range ( arr_size ) :
        if arr [ i ] > third and arr [ i ] < second :
            third = arr [ i ]
    print ( "The third Largest " "element is " , third )
|||

FIND_SUM_NODES_GIVEN_PERFECT_BINARY_TREE_1

def sum_nodes ( l ) :
    leaf_node_count = math.pow ( 2 , l - 1 )
    sum_last_level = 0
    sum_last_level = ( leaf_node_count * ( leaf_node_count + 1 ) ) / 2
    sum = sum_last_level * l
    return sum
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
        return a
|||

MAXIMUM_TRIPLET_SUM_ARRAY_2

def max_triplet_sum ( arr , n ) :
    max_a , max_b = - 100000000 , - 100000000
    max_c = - 100000000
    for i in range ( n ) :
        if arr [ i ] > max_a :
            max_c = max_b
            max_b = max_a
            max_a = arr [ i ]
        elif arr [ i ] > max_b :
            max_c = max_b
            max_b = arr [ i ]
        elif arr [ i ] > max_c :
            max_c = arr [ i ]
    return ( max_a , max_b , max_c )
|||

COUNT_PAIRS_TWO_SORTED_ARRAYS_WHOSE_SUM_EQUAL_GIVEN_VALUE_X_1

def count_pairs ( arr1 , arr2 , m , n , x ) :
    count = 0
    us = set ( )
    for i in range ( m ) :
        us.add ( arr1 [ i ] )
    for j in range ( n ) :
        if us.intersection ( arr2 [ j ] ) :
            count += 1
    return count
|||

MINIMUM_STEPS_REACH_END_ARRAY_CONSTRAINTS

def getMinStepToReachEnd ( arr , N ) :
    visit = [ False ] * N
    distance = [ 0 ] * N
    digit = [ [ ] for i in range ( 10 ) ]
    for i in range ( N ) :
        visit [ i ] = False
    for i in range ( 1 , N ) :
        digit [ arr [ i ] ].append ( i )
    distance [ 0 ] = 0
    visit [ 0 ] = True
    q = Queue ( )
    q.put ( 0 )
    while not q.empty ( ) :
        idx = q.get ( )
        q.put ( 0 )
        if idx == N - 1 :
            break
        d = arr [ idx ]
        for i in digit [ d ] :
            nextidx = digit [ d ] [ i ]
            if not visit [ nextidx ] :
                visit [ nextidx ] = True
                q.put ( nextidx )
                distance [ nextidx ] = distance [ idx ] + 1
        digit [ d ].clear ( )
        if idx - 1 >= 0 and not visit [ idx - 1 ] :
            visit [ idx - 1 ] = True
            q.put ( idx - 1 )
            distance [ idx - 1 ] = distance [ idx ] + 1
        if idx + 1 < N and not visit [ idx + 1 ] :
            visit [ idx + 1 ] = True
            q.put ( idx + 1 )
            distance [ idx + 1 ] = distance [ idx ] + 1
    return distance [ N - 1 ]
|||

LEXICOGRAPHICALLY_SMALLEST_ARRAY_K_CONSECUTIVE_SWAPS

def minimize_with_k_swapped ( arr , n , k ) :
    for i in range ( n - 1 and k > 0 ) :
        pos = i
        for j in range ( i + 1 , n ) :
            if j - i > k :
                break
            if arr [ j ] < arr [ pos ] :
                pos = j
        temp = None
        for j in range ( pos , i > 0 ) :
            temp = arr [ j ]
            arr [ j ] , arr [ j - 1 ] = arr [ j - 1 ] , temp
        k -= pos - i
|||

CONVERT_SENTENCE_EQUIVALENT_MOBILE_NUMERIC_KEYPAD_SEQUENCE

def printSequence ( arr , input ) :
    output = ""
    n = len ( input )
    for i in range ( n ) :
        if input [ i ] == ' ' :
            output = output + "0"
        else :
            position = input [ i ] - 'A'
            output = output + arr [ position ]
    return output
|||

PROGRAM_CHECK_ARRAY_SORTED_NOT_ITERATIVE_RECURSIVE

def array_sorted_or_not ( arr , n ) :
    if n == 1 or n == 0 :
        return 1
    if arr [ n - 1 ] < arr [ n - 2 ] :
        return 0
    return array_sorted_or_not ( arr , n - 1 )
|||

CHECK_TWO_GIVEN_CIRCLES_TOUCH_INTERSECT

def circle ( x1 , y1 , x2 , y2 , r1 , r2 ) :
    distSq = ( x1 - x2 ) ** 2 + ( y1 - y2 ) ** 2
    radSumSq = ( r1 + r2 ) ** 2
    if distSq == radSumSq :
        return 1
    elif distSq > radSumSq :
        return - 1
    else :
        return 0
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
|||

PADOVAN_SEQUENCE

def pad ( n ) :
    pPrevPrev , pPrev , pCurr , pNext = 1 , 1 , 1 , 1
    for i in range ( 3 , n ) :
        pNext = pPrevPrev + pPrev
        pPrevPrev = pPrev
        pPrev = pCurr
        pCurr = pNext
    return pNext
|||

CHECK_GIVEN_STRING_CAN_SPLIT_FOUR_DISTINCT_STRINGS

def check ( s ) :
    if len ( s ) >= 10 :
        return True
    for i in range ( 1 , len ( s ) ) :
        for j in range ( i + 1 , len ( s ) ) :
            for k in range ( j + 1 , len ( s ) ) :
                s1 , s2 , s3 , s4 = s [ : i ] , s [ i : j ] , s [ j : k ] , s [ k : ]
                try :
                    s1 = s [ i ]
                    s2 = s [ i ]
                    s3 = s [ j ]
                    s4 = s [ k ]
                except StringIndexError :
                    pass
                if strcheck ( s1 , s2 ) and strcheck ( s1 , s3 ) and strcheck ( s1 , s4 ) and strcheck ( s2 , s3 ) and strcheck ( s2 , s4 ) and strcheck ( s3 , s4 ) :
                    return True
    return False
|||

PERMUTE_TWO_ARRAYS_SUM_EVERY_PAIR_GREATER_EQUAL_K

def is_possible ( a , b , n , k ) :
    a.sort ( key = lambda x : x [ 1 ] )
    b.sort ( key = lambda x : x [ 0 ] )
    for i in range ( n ) :
        if a [ i ] + b [ i ] < k :
            return False
    return True
|||

ARRAY_ELEMENT_MOVED_K_USING_SINGLE_MOVES

def winner ( a , n , k ) :
    if k >= n - 1 :
        return n
    best , times = 0 , 0
    for i in range ( n ) :
        if a [ i ] > best :
            best = a [ i ]
            if i == 1 :
                times = 1
        else :
            times += 1
        if times >= k :
            return best
    return best
|||

DIRECTION_LAST_SQUARE_BLOCK

def direction ( R , C ) :
    if R != C and R % 2 == 0 and C % 2 != 0 and R < C :
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
    if R != C and R % 2 != 0 and C % 2 != 0 and R < C :
        print ( "Right" )
        return
    if R != C and R % 2 != 0 and C % 2 != 0 and R > C :
        print ( "Down" )
        return
    if R != C and R % 2 == 0 and C % 2 == 0 and R < C :
        print ( "Left" )
        return
    if R != C and R % 2 == 0 and C % 2 == 0 and R > C :
        print ( "Up" )
        return
    if R != C and R % 2 == 0 and C % 2 != 0 and R > C :
        print ( "Down" )
        return
|||

NUMBER_NON_NEGATIVE_INTEGRAL_SOLUTIONS_B_C_N

def countIntegralSolutions ( n ) :
    result = 0
    for i in range ( 0 , n ) :
        for j in range ( 0 , n - i ) :
            for k in range ( 0 , ( n - i - j ) ) :
                if i + j + k == n :
                    result += 1
    return result
|||

SWAP_MAJOR_MINOR_DIAGONALS_SQUARE_MATRIX

def swapDiagonal ( matrix ) :
    for i in range ( N ) :
        temp = matrix [ i ] [ i ]
        matrix [ i ] [ i ] = matrix [ i ] [ N - i - 1 ]
        matrix [ i ] [ N - i - 1 ] = temp
|||

MINIMUM_OPERATIONS_MAKE_GCD_ARRAY_MULTIPLE_K

def MinOperation ( a , n , k ) :
    result = 0
    for i in range ( n ) :
        if a [ i ] != 1 and a [ i ] > k :
            result = result + min ( a [ i ] % k , k - a [ i ] % k )
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
        return int ( math.pow ( 2 , p ) + result )
    else :
        return result
|||

SQUARE_ROOT_OF_A_PERFECT_SQUARE_1

def square_root ( n ) :
    x = n
    y = 1
    while x > y :
        x = ( x + y ) / 2
        y = n // x
    return long ( x )
|||

FIND_MINIMUM_SHIFT_LONGEST_COMMON_PREFIX

def KMP ( m , n , str2 , str1 ) :
    pos , len = 0 , 0
    p = [ 0 ] * ( m + 1 )
    k = 0
    ch1 = str1 [ : m ]
    ch2 = str2 [ : m ]
    for i in range ( 2 , n + 1 ) :
        while k and ch1 [ k ] != ch1 [ i - 1 ] :
            k = p [ k ]
        if ch1 [ k ] == ch1 [ i - 1 ] :
            k += 1
        p [ i ] = k
    for j , i in enumerate ( m ) :
        while j and j < n and ch1 [ j ] != ch2 [ i ] :
            j = p [ j ]
        if j < n and ch1 [ j ] == ch2 [ i ] :
            j += 1
        if j > len :
            len = j
            pos = i - j + 1
    print ( "Shift = " + str ( pos ) )
    print ( "Prefix = " + str1 [ : len ] )
|||

SORTED_ORDER_PRINTING_OF_AN_ARRAY_THAT_REPRESENTS_A_BST

def _print_sorted ( arr , start , end ) :
    if start > end :
        return
    _print_sorted ( arr , start * 2 + 1 , end )
    print ( arr [ start ] , end )
    _print_sorted ( arr , start * 2 + 2 , end )
|||

CHECK_WHETHER_GIVEN_DEGREES_VERTICES_REPRESENT_GRAPH_TREE

def check ( degree , n ) :
    deg_sum = 0
    for i in range ( n ) :
        deg_sum += degree [ i ]
    return ( 2 ** ( n - 1 ) == deg_sum )
|||

MOVE_ZEROES_END_ARRAY

def push_zeros_to_end ( arr , n ) :
    count = 0
    for i in range ( n ) :
        if arr [ i ] != 0 :
            arr [ count ] = arr [ i ]
    while count < n :
        arr [ count ] = 0
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
|||

SUM_LARGEST_PRIME_FACTOR_NUMBER_LESS_EQUAL_N

def sum_of_large_prime_factor ( n ) :
    prime , sum = [ 0 ] * ( n + 1 ) , 0
    prime.sort ( )
    max = n // 2
    for p in range ( 2 , max + 1 ) :
        if prime [ p ] == 0 :
            for i in range ( p * 2 , n + 1 , p ) :
                prime [ i ] = p
    for p in range ( 2 , n + 1 ) :
        if prime [ p ] != 0 :
            sum += prime [ p ]
        else :
            sum += p
    return sum
|||

REARRANGE_A_STRING_IN_SORTED_ORDER_FOLLOWED_BY_THE_INTEGER_SUM

def arrangeString ( str ) :
    char_count = [ 0 ]
    sum = 0
    for c in str :
        if ord ( c ) < 128 :
            char_count [ c - ord ( 'A' ) ] += 1
        else :
            sum = sum + ( ord ( c ) - ord ( '0' ) )
    res = ""
    for i in range ( MAX_CHAR ) :
        ch = chr ( ord ( 'A' ) + i )
        while char_count [ i ] != 0 :
            res = res + ch
    if sum :
        res = res + sum
    return res
|||

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX_1

def number_of_paths ( m , n ) :
    count = [ [ 0 ] * m for i in range ( m ) ]
    for i in range ( m ) :
        count [ i ] [ 0 ] = 1
    for j in range ( n ) :
        count [ 0 ] [ j ] = 1
    for i in range ( 1 , m ) :
        for j in range ( 1 , n ) :
            count [ i ] [ j ] = count [ i - 1 ] [ j ] + count [ i ] [ j - 1 ]
    return count [ m - 1 ] [ n - 1 ]
|||

DYNAMIC_PROGRAMMING_SET_5_EDIT_DISTANCE_1

def edit_dist_dp ( str1 , str2 , m , n ) :
    dp = [ [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m
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
|||

SUM_ELEMENTS_K1TH_K2TH_SMALLEST_ELEMENTS_1

def minheapify ( a , index ) :
    small = index
    l = 2 * index + 1
    r = 2 * index + 2
    if l < n and a [ l ] < a [ small ] :
        small = l
    if r < n and a [ r ] < a [ small ] :
        small = r
    if small != index :
        t = a [ small ]
        a [ small ] , a [ index ] = a [ index ] , a [ small ]
        a [ index ] = t
        minheapify ( a , small )
|||

SEARCHING_FOR_PATTERNS_SET_2_KMP_ALGORITHM

def computeLPSArray ( pat , M , lps ) :
    len = 0
    i = 1
    lps [ 0 ] = 0
    while i < M :
        if pat [ i ] == pat [ len ] :
            len += 1
            lps [ i ] = len
            i += 1
        else :
            if len != 0 :
                len = lps [ len - 1 ]
            else :
                lps [ i ] = len
                i += 1
|||

FIND_MINIMUM_DIFFERENCE_PAIR

def findMinDiff ( arr , n ) :
    diff = sys.maxsize
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            if abs ( ( arr [ i ] - arr [ j ] ) ) < diff :
                diff = abs ( ( arr [ i ] - arr [ j ] ) )
    return diff
|||

PRINT_FIRST_K_DIGITS_1N_N_POSITIVE_INTEGER

def print ( n , k ) :
    rem = 1
    for i in range ( k ) :
        print ( ( 10 ** rem ) / n )
        rem = ( 10 ** rem ) % n
|||

GROUP_MULTIPLE_OCCURRENCE_OF_ARRAY_ELEMENTS_ORDERED_BY_FIRST_OCCURRENCE

def group_elements ( arr , n ) :
    visited = [ False for i in range ( n ) ]
    for i in range ( n ) :
        if not visited [ i ] :
            print ( arr [ i ] , end = ' ' )
            for j in range ( i + 1 , n ) :
                if arr [ i ] == arr [ j ] :
                    print ( arr [ i ] , end = ' ' )
                    visited [ j ] = True
|||

CHECK_WHETHER_ARITHMETIC_PROGRESSION_CAN_FORMED_GIVEN_ARRAY

def checkIsAP ( arr , n ) :
    if n == 1 : return True
    arr.sort ( )
    d = arr [ 1 ] - arr [ 0 ]
    for i in range ( 2 , n ) :
        if arr [ i ] - arr [ i - 1 ] != d : return False
    return True
|||

NTH_MULTIPLE_NUMBER_FIBONACCI_SERIES

def find_position ( k , n ) :
    f1 , f2 , f3 = 0 , 1 , 0
    i = 2
    while i != 0 :
        f3 = f1 + f2
        f1 , f2 , f3 = f2 , f3
        if f2 % k == 0 :
            return n * i
        i += 1
    return 0
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
    for i in range ( n - 1 ) :
        if arr [ i ] != arr [ i + 1 ] and arr [ i ] != arr [ i + 1 ] - 1 :
            count += arr [ i + 1 ] - arr [ i ] - 1
    return count
|||

MAKE_LARGEST_PALINDROME_CHANGING_K_DIGITS

def maximum_palin_using_k_changes ( str , k ) :
    palin = str.split ( )
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
    r = len ( str ) - 1
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
    for i in palin :
        ans += i
    return ans
|||

SUBARRAYSUBSTRING_VS_SUBSEQUENCE_AND_PROGRAMS_TO_GENERATE_THEM

def subArray ( n ) :
    for i in range ( n ) :
        for j in range ( i , n ) :
            for k in range ( i , j ) :
                print ( arr [ k ] , end = ' ' )
|||

MAXIMUM_SUM_INCREASING_ORDER_ELEMENTS_N_ARRAYS

def maximum_sum ( a , n ) :
    for i in range ( n ) :
        sort ( a , i , n )
    sum = a [ n - 1 ] [ M - 1 ]
    prev = a [ n - 1 ] [ M - 1 ]
    i , j = n - 2 , n - 1
    for i in range ( n - 2 , - 1 , - 1 ) :
        for j in range ( M - 1 , - 1 , - 1 ) :
            if a [ i ] [ j ] < prev :
                prev = a [ i ] [ j ]
                sum += prev
                break
        if j == - 1 :
            return 0
    return sum
|||

C_PROGRAM_FACTORIAL_NUMBER

def factorial ( n ) :
    if n == 0 :
        return 1
    return n * factorial ( n - 1 )
|||

PRINT_SQUARES_FIRST_N_NATURAL_NUMBERS_WITHOUT_USING

def print_squares ( n ) :
    square , prev_x = 0 , 0
    for x in range ( n ) :
        square = ( square + x + prev_x )
        print ( square , end = ' ' )
        prev_x = x
|||

ROPES_DATA_STRUCTURE_FAST_STRING_CONCATENATION

def concatenate ( a , b , c , n1 , n2 ) :
    i = 0
    for i in range ( n1 ) :
        c [ i ] = a [ i ]
    for j in range ( n2 ) :
        c [ i ] += b [ j ]
|||

GIVEN_TWO_SORTED_ARRAYS_NUMBER_X_FIND_PAIR_WHOSE_SUM_CLOSEST_X

def printClosest ( ar1 , ar2 , m , n , x ) :
    diff = sys.maxint
    res_l , res_r = 0 , 0
    l , r = 0 , n - 1
    while l < m and r >= 0 :
        if abs ( ar1 [ l ] + ar2 [ r ] - x ) < diff :
            res_l = l
            res_r = r
            diff = abs ( ar1 [ l ] + ar2 [ r ] - x )
        if ar1 [ l ] + ar2 [ r ] > x :
            r -= 1
        else :
            l += 1
    print ( "The closest pair is [" + str ( ar1 [ res_l ] ) + ", " + str ( ar2 [ res_r ] ) + "]" )
|||

CONVERT_STRICTLY_INCREASING_ARRAY_MINIMUM_CHANGES

def min_remove ( arr , n ) :
    LIS = [ ]
    len = 0
    for i in range ( n ) :
        LIS.append ( 1 )
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if arr [ i ] > arr [ j ] and ( i - j ) <= ( arr [ i ] - arr [ j ] ) :
                LIS [ i ] = max ( LIS [ i ] , LIS [ j ] + 1 )
        len = max ( len , LIS [ i ] )
    return n - len
|||

TAIL_RECURSION

def fact ( n ) :
    if n == 0 :
        return 1
    return n * fact ( n - 1 )
|||

RECURSIVE_FUNCTIONS

def tower ( n , source_pole , destination_pole , auxiliary_pole ) :
    if 0 == n :
        return
    tower ( n - 1 , source_pole , auxiliary_pole , destination_pole )
    print ( "Move the disk %d from %c to %c" % ( n , source_pole , destination_pole ) )
    tower ( n - 1 , auxiliary_pole , destination_pole , source_pole )
|||

FIND_X_Y_SATISFYING_AX_N

def solution ( a , b , n ) :
    for i in range ( 0 , a * a <= n ) :
        if ( n - ( i * a ) ) % b == 0 :
            print ( "x = %d, y = %d" % ( i , ( n - ( i * a ) ) / b ) )
            return
    print ( "No solution" )
|||

EXPONENTIAL_SQUARING_FAST_MODULO_MULTIPLICATION_1

def exponentiation ( base , exp ) :
    t = 1
    while exp > 0 :
        if exp % 2 != 0 :
            t = ( t * base ) % N
        base = ( base * base ) % N
        exp /= 2
    return t % N
|||

CHECK_OCCURRENCES_CHARACTER_APPEAR_TOGETHER

def checkIfAllTogether ( s , c ) :
    oneSeen = False
    i , n = 0 , len ( s )
    while i < n :
        if s [ i ] == c :
            if oneSeen == True :
                return False
            while i < n and s [ i ] == c :
                i += 1
            oneSeen = True
        else :
            i += 1
    return True
|||

MAXIMUM_AREA_RECTANGLE_PICKING_FOUR_SIDES_ARRAY

def findArea ( arr , n ) :
    arr.sort ( key = lambda x : x [ 1 ] )
    dimension = [ 0 , 0 ]
    for i , j in enumerate ( arr ) :
        if arr [ i ] == arr [ i + 1 ] :
            dimension [ j ] = arr [ i ++ ]
    return ( dimension [ 0 ] * dimension [ 1 ] )
|||

PYTHON_PROGRAM_FIND_PERIMETER_CIRCUMFERENCE_SQUARE_RECTANGLE

def Circumference ( a ) :
    return 4 * a
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
            pos += 1
        if pos != cycle_start :
            temp = item
            item = arr [ pos ]
            arr [ pos ] = temp
            writes += 1
        while pos != cycle_start :
            pos = cycle_start
            for i in range ( cycle_start + 1 , n ) :
                if arr [ i ] < item :
                    pos += 1
            while item == arr [ pos ] :
                pos += 1
            if item != arr [ pos ] :
                temp = item
                item = arr [ pos ]
                arr [ pos ] = temp
                writes += 1
|||

SELECT_A_RANDOM_NUMBER_FROM_STREAM_WITH_O1_SPACE

def select_random ( x ) :
    global count
    if count == 1 :
        res = x
    else :
        r = random.Random ( )
        i = r.randint ( 0 , count )
        if i == count - 1 :
            res = x
    return res
|||

HOSOYAS_TRIANGLE

def print_hosoya ( n ) :
    dp = [ [ 0 ] * N for i in range ( N ) ]
    dp [ 0 ] [ 0 ] = dp [ 1 ] [ 0 ] = 1
    dp [ 1 ] [ 1 ] = 1
    for i in range ( 2 , n ) :
        for j in range ( n ) :
            if i > j :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j ] + dp [ i - 2 ] [ j ]
            else :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j - 1 ] + dp [ i - 2 ] [ j - 2 ]
    for i in range ( n ) :
        for j in range ( 0 , i + 1 ) :
            print ( dp [ i ] [ j ] , end = '' )
        print ( '' )
|||

DISTRIBUTING_M_ITEMS_CIRCLE_SIZE_N_STARTING_K_TH_POSITION

def last_position ( n , m , k ) :
    if m <= n - k + 1 :
        return m + k - 1
    m = m - ( n - k + 1 )
    return ( m % n == 0 )
|||

PRINTING_LONGEST_INCREASING_CONSECUTIVE_SUBSEQUENCE

def longest_subsequence ( a , n ) :
    mp = { }
    dp = [ ]
    maximum = int ( - 1 )
    index = - 1
    for i in range ( n ) :
        if mp [ a [ i ] - 1 ] :
            lastIndex = mp [ a [ i ] - 1 ] - 1
            dp.append ( 1 + dp [ lastIndex ] )
        else :
            dp.append ( 1 )
        mp [ a [ i ] ] = i + 1
        if maximum < dp [ i ] :
            maximum = dp [ i ]
            index = i
    for curr in a [ index ] - maximum + 1 :
        print ( curr , end = ' ' )
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
|||

CHECK_GIVEN_ARRAY_CONTAINS_DUPLICATE_ELEMENTS_WITHIN_K_DISTANCE

def check_duplicatesWithinK ( arr , k ) :
    set = set ( )
    for i in range ( len ( arr ) ) :
        if set.issubset ( arr [ i ] ) :
            return True
        set.add ( arr [ i ] )
        if i >= k :
            set.remove ( arr [ i - k ] )
    return False
|||

MINIMUM_INSERTIONS_SORT_ARRAY

def minInsertionStepToSortArray ( arr , N ) :
    lis = [ 1 ] * N
    for i in range ( N ) :
        lis [ i ] = 1
    for i in range ( 1 , N ) :
        for j in range ( i ) :
            if arr [ i ] >= arr [ j ] and lis [ i ] < lis [ j ] + 1 :
                lis [ i ] = lis [ j ] + 1
    max = 0
    for i in range ( N ) :
        if max < lis [ i ] :
            max = lis [ i ]
    return ( N - max )
|||

GENERATE_TWO_OUTPUT_STRINGS_DEPENDING_UPON_OCCURRENCE_CHARACTER_INPUT_STRING

def print_duo ( str ) :
    count_char = [ 0 ] * MAX_CHAR
    n = len ( str )
    for i in range ( n ) :
        count_char [ str [ i ] - 'a' ] += 1
    str1 , str2 = "" , ""
    for i in range ( MAX_CHAR ) :
        if count_char [ i ] > 1 :
            str2 = str2 + chr ( i + 'a' )
        elif count_char [ i ] == 1 :
            str1 = str1 + chr ( i + 'a' )
    print ( "String with characters occurring ""once:\n" )
    print ( str1 , end = '' )
    print ( "String with characters occurring ""multiple times:\n" )
    print ( str2 , end = '' )
    print ( "" )
|||

NUMBER_DIGITS_PRODUCT_TWO_NUMBERS_1

def count_digits ( a , b ) :
    if a == 0 or b == 0 :
        return 1
    return int ( math.floor ( math.log10 ( abs ( a ) ) + math.log10 ( abs ( b ) ) ) ) + 1
|||

TOTAL_NUMBER_OF_NON_DECREASING_NUMBERS_WITH_N_DIGITS_1

def count_non_decreasing ( n ) :
    N = 10
    count = 1
    for i in range ( 1 , n + 1 ) :
        count *= ( N + i - 1 )
        count /= i
    return count
|||

COUNT_STRINGS_ADJACENT_CHARACTERS_DIFFERENCE_ONE

def count_strs ( n ) :
    dp = [ [ 0 ] * 27 for i in range ( n + 1 ) ]
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
        sum = ( sum + dp [ n ] [ i ] )
    return sum
|||

PROGRAM_TO_EFFICIENTLY_CALCULATE_EX

def exponential ( n , x ) :
    sum = 1
    for i in range ( n - 1 , 0 , - 1 ) :
        sum = 1 + x * sum / i
    return sum
|||

EFFICIENTLY_COMPUTE_SUMS_OF_DIAGONALS_OF_A_MATRIX_1

def printDiagonalSums ( mat , n ) :
    principal , secondary = 0 , 0
    for i in range ( n ) :
        principal += mat [ i ] [ i ]
        secondary += mat [ i ] [ n - i - 1 ]
    print ( "Principal Diagonal:" , principal )
    print ( "Secondary Diagonal:" , secondary )
|||

PRINT_WAYS_BREAK_STRING_BRACKET_FORM

def find_combinations ( str , index , out ) :
    if index == len ( str ) :
        print ( out )
    for i in range ( index , len ( str ) ) :
        find_combinations ( str , i + 1 , out + '(' + str [ index : i + 1 ] + ')' )
|||

LINEAR_SEARCH

def search ( arr , x ) :
    n = len ( arr )
    for i in range ( n ) :
        if arr [ i ] == x :
            return i
    return - 1
|||

FIND_THE_ELEMENT_THAT_APPEARS_ONCE_2

def single_number ( a , n ) :
    s = set ( )
    for i in a :
        s.add ( i )
    arr_sum = 0
    for i in a :
        arr_sum += i
    set_sum = 0
    for i in s :
        set_sum += i
    return ( 3 * set_sum - arr_sum ) / 2
|||

SEARCH_ALMOST_SORTED_ARRAY

def binarySearch ( arr , l , r , x ) :
    if r >= l :
        mid = l + ( r - l ) // 2
        if arr [ mid ] == x :
            return mid
        if mid > l and arr [ mid - 1 ] == x :
            return ( mid - 1 )
        if mid < r and arr [ mid + 1 ] == x :
            return ( mid + 1 )
        if arr [ mid ] > x :
            return binarySearch ( arr , l , mid - 2 , x )
        return binarySearch ( arr , mid + 2 , r , x )
    return - 1
|||

EULERS_TOTIENT_FUNCTION_FOR_ALL_NUMBERS_SMALLER_THAN_OR_EQUAL_TO_N

def compute_totient ( n ) :
    phi = [ i for i in range ( 1 , n + 1 ) if i != 0 ]
    for p in range ( 2 , n + 1 ) :
        if phi [ p ] == p :
            phi [ p ] = p - 1
            for i in range ( 2 * p , n + 1 , p ) :
                phi [ i ] = ( phi [ i ] / p ) ** ( p - 1 )
    for i in range ( 1 , n + 1 ) :
        print ( "Totient of %d is %d" % ( i , phi [ i ] ) )
|||

FIND_MINIMUM_NUMBER_DIVIDED_MAKE_NUMBER_PERFECT_SQUARE

def findMinNumber ( n ) :
    count , ans = 0 , 1
    while n % 2 == 0 :
        count += 1
        n /= 2
    if count % 2 == 1 :
        ans *= 2
    for i in range ( 3 , math.sqrt ( n ) , 2 ) :
        count = 0
        while n % i == 0 :
            count += 1
            n /= i
        if count % 2 == 1 :
            ans *= i
    if n > 2 :
        ans *= n
    return ans
|||

COUNT_NUMBER_WAYS_JUMP_REACH_END

def count_ways_to_jump ( arr , n ) :
    count_jump = [ 0 ] * n
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
|||

CONVERT_SUBSTRINGS_LENGTH_K_BASE_B_DECIMAL_1

def substring_conversions ( str , k , b ) :
    i , sum , counter = 0 , 0 , k - 1
    for i in range ( k ) :
        sum = int ( sum + ( ( str [ i ] - '0' ) * pow ( b , counter ) ) )
        counter -= 1
    print ( sum , end = ' ' )
    prev = sum
    sum = 0
    counter = 0
    for i in range ( len ( str ) ) :
        sum = int ( prev - ( ( str [ i - k ] - '0' ) * pow ( b , k - 1 ) ) )
        sum = sum * b
        sum = sum + ( str [ i ] - '0' )
        print ( sum , end = ' ' )
        prev = sum
        counter += 1
|||

TWO_ELEMENTS_WHOSE_SUM_IS_CLOSEST_TO_ZERO

def min_abs_sum_pair ( arr , arr_size ) :
    inv_count = 0
    l , r , min_sum , sum , min_l , min_r = 0 , 0 , 0 , 0
    if arr_size < 2 :
        print ( "Invalid Input" )
        return
    min_l = 0
    min_r = 1
    min_sum = arr [ 0 ] + arr [ 1 ]
    for l in range ( arr_size - 1 ) :
        for r in range ( l + 1 , arr_size ) :
            sum = arr [ l ] + arr [ r ]
            if abs ( min_sum ) > abs ( sum ) :
                min_sum = sum
                min_l = l
                min_r = r
    print ( " The two elements whose " "sum is minimum are " , arr [ min_l ] , arr [ min_r ] )
|||

HOW_TO_PRINT_MAXIMUM_NUMBER_OF_A_USING_GIVEN_FOUR_KEYS

def findoptimal ( N ) :
    if N <= 6 :
        return N
    screen = [ ]
    b = 0
    n = 0
    for n in range ( 1 , 6 ) :
        screen.append ( n )
    for n in range ( 7 , N ) :
        screen.append ( max ( 2 * screen [ n - 4 ] , max ( 3 * screen [ n - 5 ] , 4 * screen [ n - 6 ] ) ) )
    return screen [ N - 1 ]
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
        cnt += 1
    return B_Number
|||

COUNTS_PATHS_POINT_REACH_ORIGIN_1

def count_paths ( n , m ) :
    dp = [ [ 1 ] * n + [ m + 1 ] * n for i in range ( 0 , n + 1 ) ]
    for i in range ( 0 , m + 1 ) :
        dp [ i ] [ 0 ] = 1
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , m + 1 ) :
            dp [ i ] [ j ] = dp [ i - 1 ] [ j ] + dp [ i ] [ j - 1 ]
    return dp [ n ] [ m ]
|||

SUM_ELEMENTS_K1TH_K2TH_SMALLEST_ELEMENTS

def sum_between_two_kth ( arr , k1 , k2 ) :
    arr.sort ( )
    result = 0
    for i in range ( k1 , k2 - 1 ) :
        result += arr [ i ]
    return result
|||

SMALLEST_SUBARRAY_K_DISTINCT_NUMBERS

def minRange ( arr , n , k ) :
    l , r = 0 , n
    for i in range ( n ) :
        s = set ( )
        j = 0
        for j in range ( i , n ) :
            s.add ( arr [ j ] )
            if len ( s ) == k :
                if ( j - i ) < ( r - l ) :
                    r = j
                    l = i
                break
        if j == n :
            break
    if l == 0 and r == n :
        print ( "Invalid k" )
    else :
        print ( l , r )
|||

AREA_OF_A_HEXAGON

def hexagon_area ( s ) :
    return ( ( 3 * math.sqrt ( 3 ) * ( s ** 2 ) ) / 2 )
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
|||

COUNT_SUBSTRINGS_BINARY_STRING_CONTAINING_K_ONES

def countOfSubstringWithKOnes ( s , K ) :
    N = len ( s )
    res = 0
    countOfOne = 0
    freq = [ 1 ] * ( N + 1 )
    for i in range ( N ) :
        countOfOne += ( s [ i ] - '0' )
        if countOfOne >= K :
            res += freq [ countOfOne - K ]
        freq [ countOfOne ] += 1
    return res
|||

NUMBER_INDEXES_EQUAL_ELEMENTS_GIVEN_RANGE

def answer_query ( a , n , l , r ) :
    count = 0
    for i in range ( l , r ) :
        if a [ i ] == a [ i + 1 ] :
            count += 1
    return count
|||

CHECK_WHETHER_NUMBER_DUCK_NUMBER_NOT

def check_duck ( num ) :
    len ( num )
    count_zero = 0
    ch = None
    for i in range ( 1 , len ( num ) ) :
        ch = num [ i ]
        if ch == '0' :
            count_zero += 1
    return count_zero
|||

NUMBER_NON_NEGATIVE_INTEGRAL_SOLUTIONS_B_C_N_1

def count_integral_solutions ( n ) :
    return ( ( n + 1 ) * ( n + 2 ) ) / 2
|||

MAXIMUM_PROFIT_BY_BUYING_AND_SELLING_A_SHARE_AT_MOST_K_TIMES_1

def max_profit ( price , n , k ) :
    profit = [ [ 0 ] * ( k + 1 ) for i in range ( k + 1 ) ]
    for i in range ( 0 , k + 1 ) :
        profit [ i ] [ 0 ] = 0
    for j in range ( 0 , n + 1 ) :
        profit [ 0 ] [ j ] = 0
    for i in range ( 1 , k + 1 ) :
        prev_diff = int ( 0 )
        for j in range ( 1 , n + 1 ) :
            prev_diff = max ( prev_diff , profit [ i - 1 ] [ j - 1 ] - price [ j - 1 ] )
            profit [ i ] [ j ] = max ( profit [ i ] [ j - 1 ] , price [ j ] + prev_diff )
    return profit [ k ] [ n - 1 ]
|||

COUNT_CHARACTERS_POSITION_ENGLISH_ALPHABETS

def find_count ( str ) :
    result = 0
    for c in str :
        if c in ( ord ( 'a' ) , ord ( 'z' ) ) :
            result += 1
    return result
|||

COUNT_GFG_SUBSEQUENCES_GIVEN_STRING

def count_subgraph ( s , n ) :
    cntG , cntF , result , C = 0 , 0 , 0 , 0
    for i in range ( n ) :
        try :
            cntG += 1
            result += C
        except :
            continue
    print ( result )
|||

FIND_SMALLEST_VALUE_REPRESENTED_SUM_SUBSET_GIVEN_ARRAY

def findSmallest ( arr , n ) :
    res = 1
    for i in range ( n and arr [ i ] <= res :
        res = res + arr [ i ]
    return res
|||

MAXIMUM_POINTS_COLLECTED_BY_TWO_PERSONS_ALLOWED_TO_MEET_ONCE

def findMaxPoints ( A ) :
    P1S = [ [ ] for i in range ( M + 2 ) ]
    P1E = [ [ ] for i in range ( M + 2 ) ]
    P2S = [ [ ] for i in range ( M + 2 ) ]
    P2E = [ [ ] for i in range ( M + 2 ) ]
    for i in range ( 1 , N + 1 ) :
        for j in range ( 1 , M + 1 ) :
            P1S [ i ] [ j ] = max ( P1S [ i - 1 ] [ j ] , P1S [ i ] [ j - 1 ] ) + A [ i - 1 ] [ j - 1 ]
    for i in range ( N , - 1 , - 1 ) :
        for j in range ( M , - 1 , - 1 ) :
            P1E [ i ] [ j ] = max ( P1E [ i + 1 ] [ j ] , P1E [ i ] [ j + 1 ] ) + A [ i - 1 ] [ j - 1 ]
    for i in range ( N , - 1 , - 1 ) :
        for j in range ( M , - 1 , - 1 ) :
            P2S [ i ] [ j ] = max ( P2S [ i + 1 ] [ j ] , P2S [ i ] [ j - 1 ] ) + A [ i - 1 ] [ j - 1 ]
    for i in range ( 1 , N + 1 ) :
        for j in range ( M , - 1 , - 1 ) :
            P2E [ i ] [ j ] = max ( P2E [ i - 1 ] [ j ] , P2E [ i ] [ j + 1 ] ) + A [ i - 1 ] [ j - 1 ]
    ans = 0
    for i in range ( 2 , N + 1 ) :
        for j in range ( 2 , M + 1 ) :
            op1 = P1S [ i ] [ j - 1 ] + P1E [ i ] [ j + 1 ] + P2S [ i + 1 ] [ j ] + P2E [ i - 1 ] [ j ]
            op2 = P1S [ i - 1 ] [ j ] + P1E [ i + 1 ] [ j + 1 ] + P2S [ i - 1 ] [ j ]
            ans += op1
|||

PROGRAM_FIND_CIRCUMFERENCE_CIRCLE

def circumference ( r ) :
    PI = 3.1415
    cir = 2 * PI * r
    return cir
|||

QUICKLY_FIND_MULTIPLE_LEFT_ROTATIONS_OF_AN_ARRAY

def left_rotate ( arr , n , k ) :
    for i in range ( k , k + n ) :
        print ( arr [ i % n ] , end = ' ' )
|||

MINIMUM_SUM_CHOOSING_MINIMUM_PAIRS_ARRAY

def minSum ( A , n ) :
    min_val = sum ( A )
    return ( min_val * ( n - 1 ) )
|||

RECURSIVE_PROGRAM_PRIME_NUMBER

def isPrime ( n , i ) :
    if n <= 2 :
        return ( n == 2 )
    if n % i == 0 :
        return False
    if i * i > n :
        return True
    return isPrime ( n , i + 1 )
|||

SPARSE_SEARCH

def sparseSearch ( arr , x , n ) :
    return binarySearch ( arr , 0 , n - 1 , x )
|||

FIND_NUMBER_TIMES_STRING_OCCURS_GIVEN_STRING

def count ( a , b , m , n ) :
    if ( m == 0 and n == 0 ) or n == 0 :
        return 1
    if m == 0 :
        return 0
    if a [ m - 1 ] == b [ n - 1 ] :
        return count ( a , b , m - 1 , n - 1 ) + count ( a , b , m - 1 , n )
    else :
        return count ( a , b , m - 1 , n )
|||

PROGRAM_CHECK_ARRAY_SORTED_NOT_ITERATIVE_RECURSIVE_1

def array_sorted_or_not ( arr , n ) :
    if n == 0 or n == 1 :
        return True
    for i in range ( 1 , n ) :
        if arr [ i - 1 ] > arr [ i ] :
            return False
    return True
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
                max_count = curr - prev_prev_zero
                max_index = prev_zero
            prev_prev_zero = prev_zero
            prev_zero = curr
    if n - prev_prev_zero > max_count :
        max_index = prev_zero
    return max_index
|||

FIND_MAXIMUM_PRODUCT_OF_A_TRIPLET_IN_ARRAY_1

def max_product ( arr , n ) :
    if n < 3 :
        return - 1
    arr.sort ( )
    return max ( arr [ 0 ] * arr [ 1 ] * arr [ n - 1 ] , arr [ n - 1 ] * arr [ n - 2 ] * arr [ n - 3 ] )
|||

COORDINATES_RECTANGLE_GIVEN_POINTS_LIE_INSIDE

def print_rect ( X , Y , n ) :
    Xmax = sorted ( list ( X ) ) [ : n ]
    Xmin = sorted ( list ( X ) ) [ : n ]
    Ymax = sorted ( list ( Y ) ) [ : n ]
    Ymin = sorted ( list ( Y ) ) [ : n ]
    print ( "{" + str ( Xmin ) + ", " + str ( Ymin ) + "}" )
    print ( "{" + str ( Xmin ) + ", " + str ( Ymax ) + "}" )
    print ( "{" + str ( Xmax ) + ", " + str ( Ymax ) + "}" )
    print ( "{" + str ( Xmax ) + ", " + str ( Ymin ) + "}" )
|||

COUNT_BINARY_DIGIT_NUMBERS_SMALLER_N

def count_of_binary_number_less_N ( N ) :
    q = Queue ( )
    q.put ( 1 )
    cnt = 0
    t = None
    while q.size ( ) > 0 :
        t = q.get ( )
        q.put ( )
        if t <= N :
            cnt += 1
            q.put ( t * 10 )
            q.put ( t * 10 + 1 )
    return cnt
|||

CONVERT_DECIMAL_FRACTION_BINARY_NUMBER

def decimalToBinary ( num , k_prec ) :
    binary = ""
    Integral = int ( num )
    fractional = num - Integral
    while Integral > 0 :
        rem = Integral % 2
        binary += chr ( int ( rem + '0' ) )
        Integral /= 2
    binary = reverse ( binary )
    binary += chr ( '.' )
    while k_prec :
        fractional *= 2
        fract_bit = int ( fractional )
        if fract_bit == 1 :
            fractional -= fract_bit
            binary += chr ( 1 + '0' )
        else :
            binary += chr ( 0 + '0' )
    return binary
|||

MAXIMUM_NUMBER_OF_TRAILING_ZEROS_IN_THE_PRODUCT_OF_THE_SUBSETS_OF_SIZE_K

def maximum_zeros ( arr , n , k ) :
    subset = [ [ - 1 ] * MAX5 + [ 0 ] * MAX5 for row in subset ]
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
                    subset [ i + 1 ] [ j + pw5 ] = max ( subset [ i + 1 ] [ j + pw5 ] , subset [ i ] [ j ] + pw2 )
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
        return search ( arr , mid + 1 , h , key )
    return search ( arr , l , mid - 1 , key )
|||

PROGRAM_FIND_AREA_CIRCULAR_SEGMENT

def area_of_segment ( radius , angle ) :
    area_of_sector = pi * ( radius ** 2 ) * ( angle / 360 )
    area_of_triangle = float ( 1 ) / 2 * ( radius ** 2 ) * float ( math.sin ( ( angle * pi ) / 180 ) )
    return area_of_sector - area_of_triangle
|||

K_SMALLEST_ELEMENTS_ORDER_USING_O1_EXTRA_SPACE

def print_small ( arr , n , k ) :
    for i in range ( k , n ) :
        max_var = arr [ k - 1 ]
        pos = k - 1
        for j in range ( k - 2 , - 1 , - 1 ) :
            if arr [ j ] > max_var :
                max_var = arr [ j ]
                pos = j
        if max_var > arr [ i ] :
            j = pos
            while j < k - 1 :
                arr [ j ] , arr [ j + 1 ] = arr [ j + 1 ] , arr [ j ]
                j += 1
            arr [ k - 1 ] , arr [ i ] = arr [ i ] , arr [ i ]
    for i in range ( k ) :
        print ( arr [ i ] , end = ' ' )
|||

NTH_NON_FIBONACCI_NUMBER

def nonFibonacci ( n ) :
    prev_prev , prev , curr = 1 , 2 , 3
    while n > 0 :
        prev_prev , prev , curr = prev , curr , prev_prev + prev
        n = n - ( curr - prev - 1 )
    n = n + ( curr - prev - 1 )
    return prev + n
|||

ANALYSIS_OF_ALGORITHMS_SET_2_ASYMPTOTIC_ANALYSIS

def search ( arr , n , x ) :
    i = 0
    for i in range ( n ) :
        if arr [ i ] == x :
            return i
    return - 1
|||

ZECKENDORFS_THEOREM_NON_NEIGHBOURING_FIBONACCI_REPRESENTATION

def nearest_smaller_eq_fib ( n ) :
    if n == 0 or n == 1 :
        return n
    f1 , f2 , f3 = 0 , 1 , 1
    while f3 <= n :
        f1 , f2 , f3 = f2 , f3 , f1 + f2
    return f2
|||

PRINT_MAXIMUM_SHORTEST_DISTANCE

def find_maximum ( a , n , k ) :
    b = { }
    for i in range ( n ) :
        x = a [ i ]
        d = min ( 1 + i , n - i )
        if not b.has_key ( x ) :
            b [ x ] = d
        else :
            b [ x ] = min ( d , b [ x ] )
    ans = int ( 0 )
    for i in range ( n ) :
        x = a [ i ]
        if x != k - x and b.has_key ( k - x ) :
            ans = min ( max ( b [ x ] , b [ k - x ] ) , ans )
    return ans
|||

GENERATING_DISTINCT_SUBSEQUENCES_OF_A_GIVEN_STRING_IN_LEXICOGRAPHIC_ORDER

def generate ( st , s ) :
    if len ( s ) == 0 :
        return
    if not st.has_key ( s ) :
        st [ s ] = [ ]
        for t in s :
            t = t.split ( ' ' )
            t = t [ 0 ] + t [ 1 : ]
            generate ( st , t )
    return
|||

WRITE_YOU_OWN_POWER_WITHOUT_USING_MULTIPLICATION_AND_DIVISION

def pow ( a , b ) :
    if b == 0 :
        return 1
    answer = a
    increment = a
    i , j = 0 , 0
    for i in range ( 1 , b ) :
        for j in range ( 1 , a ) :
            answer += increment
        increment = answer
    return answer
|||

MAXIMIZE_VOLUME_CUBOID_GIVEN_SUM_SIDES_1

def maxvolume ( s ) :
    length = s / 3
    s -= length
    breadth = s / 2
    height = s - breadth
    return length * breadth * height
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
    while True :
        items = 0
        for i in range ( n ) :
            items += ( t / arr [ i ] )
        if items >= m :
            return t
        t += 1
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
|||

SHORTEST_UNCOMMON_SUBSEQUENCE

def shortestSeq ( S , T ) :
    m , n = len ( S ) , len ( T )
    dp = [ [ 1 ] * m + [ n + 1 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m
|||

MIN_FLIPS_OF_CONTINUOUS_CHARACTERS_TO_MAKE_ALL_CHARACTERS_SAME_IN_A_STRING

def find_flips ( str , n ) :
    last = ' '
    res = 0
    for i in range ( n ) :
        if last != str [ i ] :
            res += 1
        last = str [ i ]
    return res / 2
|||

DYNAMIC_PROGRAMMING_SET_28_MINIMUM_INSERTIONS_TO_FORM_A_PALINDROME

def find_min_insertions ( str , l , h ) :
    if l > h :
        return int ( l )
    if l == h :
        return 0
    if l == h - 1 :
        return ( str [ l ] , str [ h ] )
    return ( str [ l ] , find_min_insertions ( str , l + 1 , h - 1 ) )
|||

COUNT_CHARACTERS_STRING_DISTANCE_ENGLISH_ALPHABETS

def countPairs ( str ) :
    result = 0
    n = len ( str )
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if abs ( str [ i ] - str [ j ] ) == abs ( i - j ) :
                result += 1
    return result
|||

MULTISTAGE_GRAPH_SHORTEST_PATH

def shortest_dist ( graph ) :
    dist = [ INF ]
    dist [ - 1 ] = 0
    for i in range ( N - 2 , - 1 , - 1 ) :
        dist [ i ] = INF
        for j in range ( i , N ) :
            if graph [ i ] [ j ] == INF :
                continue
            dist [ i ] = min ( dist [ i ] , graph [ i ] [ j ] + dist [ j ] )
    return dist [ 0 ]
|||

MAXIMUM_SIZE_SUB_MATRIX_WITH_ALL_1S_IN_A_BINARY_MATRIX

def print_max_sub_square ( M ) :
    i , j = 0 , 0
    R = len ( M )
    C = len ( M [ 0 ] )
    S = [ [ 0 ] * R , [ 0 ] * C ]
    max_of_s , max_i , max_j = 0 , 0 , 0
    for i in range ( R ) :
        S [ i ] [ 0 ] = M [ i ] [ 0 ]
    for j in range ( C ) :
        S [ 0 ] [ j ] = M [ 0 ] [ j ]
    for i in range ( 1 , R ) :
        for j in range ( 1 , C ) :
            if M [ i ] [ j ] == 1 :
                S [ i ] [ j ] = min ( S [ i ] [ j - 1 ] , min ( S [ i - 1 ] [ j ] , S [ i - 1 ] [ j - 1 ] ) ) + 1
            else :
                S [ i ] [ j ] = 0
    max_of_s = S [ 0 ] [ 0 ]
    max_i , max_j = 0 , 0
    for i in range ( R ) :
        for j in range ( C ) :
            if max_of_s < S [ i ] [ j ] :
                max_of_s = S [ i ] [ j ]
                max_i = i
                max_j = j
    print ( "Maximum size sub-matrix is: " )
    for i in range ( max_i , max_i - max_of_s , 2 ) :
        for j in range ( max_j , max_j - max_of_s , 2 ) :
            print ( M [ i ] [ j ] , end = ' ' )
        print ( )
|||

GIVEN_SORTED_ARRAY_NUMBER_X_FIND_PAIR_ARRAY_WHOSE_SUM_CLOSEST_X

def printClosest ( arr , n , x ) :
    res_l , res_r = 0 , 0
    l , r = 0 , n - 1 , int ( x )
    while r > l :
        if abs ( arr [ l ] + arr [ r ] - x ) < diff :
            res_l = l
            res_r = r
            diff = abs ( arr [ l ] + arr [ r ] - x )
        if arr [ l ] + arr [ r ] > x :
            r -= 1
        else :
            l += 1
    print ( " The closest pair is " + str ( arr [ res_l ] ) + " and " + str ( arr [ res_r ] ) )
|||

SORT_1_N_SWAPPING_ADJACENT_ELEMENTS_1

def sortedAfterSwap ( A , B , n ) :
    t = 0
    for i in range ( n - 1 ) :
        if B [ i ] != 0 :
            if A [ i ] != i + 1 :
                t = A [ i ]
            A [ i ] , A [ i + 1 ] = A [ i + 1 ] , A [ i + 1 ]
            A [ i + 1 ] = t
    for i in range ( n ) :
        if A [ i ] != i + 1 :
            return 0
    return 1
|||

TILE_STACKING_PROBLEM

def possible_ways ( n , m , k ) :
    dp = [ [ 0 ] * N for i in range ( N ) ]
    presum = [ [ 0 ] * N for i in range ( N ) ]
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
|||

NUMBER_OF_PAIRS_IN_AN_ARRAY_HAVING_SUM_EQUAL_TO_PRODUCT

def sum_equal_product ( a , n ) :
    zero , two = 0 , 0
    for i in range ( n ) :
        if a [ i ] == 0 : zero += 1
        if a [ i ] == 2 : two += 1
    cnt = ( zero * ( zero - 1 ) ) / 2 + ( two * ( two - 1 ) ) / 2
    return cnt
|||

DYNAMIC_PROGRAMMING_SET_17_PALINDROME_PARTITIONING

def min_palse_partion ( str ) :
    n = len ( str )
    C = [ [ ] for i in range ( n ) ]
    P = [ [ ] for i in range ( n ) ]
    i , j , k , L = 0 , 0 , 0 , 0
    for i in range ( n ) :
        P [ i ] [ i ] = True
        C [ i ] [ i ] = 0
    for L in range ( 2 , n + 1 ) :
        for i in range ( n - L + 1 ) :
            j = i + L - 1
            if L == 2 :
                P [ i ] [ j ] = ( str [ i ] == str [ j ] )
            else :
                P [ i ] [ j ] = ( str [ i ] == str [ j ] ) and P [ i + 1 ] [ j - 1 ]
            if P [ i ] [ j ] == True :
                C [ i ] [ j ] = 0
            else :
                C [ i ] [ j ] = int ( str [ i ] )
                for k in range ( i , j - 1 ) :
                    C [ i ] [ j ] = min ( C [ i ] [ j ] , C [ i ] [ k ] + C [ k + 1 ] [ j ] + 1 )
    return C [ 0 ] [ n - 1 ]
|||

FIND_ONE_MULTIPLE_REPEATING_ELEMENTS_READ_ARRAY

def find_repeating_number ( arr , n ) :
    sq = int ( math.sqrt ( n ) )
    range = ( n // sq ) + 1
    count = [ 0 ] * range
    for i in range :
        count [ ( arr [ i ] - 1 ) // sq ] += 1
    selected_block = range - 1
    for i in range - 1 :
        if count [ i ] > sq :
            selected_block = i
            break
    m = { }
    for i in range ( 0 , n ) :
        if ( ( selected_block * sq ) < arr [ i ] ) :
            m [ arr [ i ] ] = 1
            if m [ arr [ i ] ] == 1 :
                return arr [ i ]
    return - 1
|||

MINIMUM_SUM_PATH_TRIANGLE

def minSumPath ( ) :
    memo = [ ]
    n = len ( A ) - 1
    for i in range ( len ( A [ n ] ) ) :
        memo.append ( A [ n ] [ i ] )
    for i in range ( len ( A ) - 2 , - 1 , - 1 ) :
        for j in range ( len ( A [ i ] ) ) :
            memo.append ( A [ i ] [ j ] + int ( min ( memo [ j ] , memo [ j + 1 ] ) ) )
    return memo [ 0 ]
|||

HOW_CAN_WE_SUM_THE_DIGITS_OF_A_GIVEN_NUMBER_IN_SINGLE_STATEMENT_1

def getSum ( n ) :
    sum = 0
    for n in range ( 0 , n ) :
        sum += n % 10 , n /= 10
    return sum
|||

RECURSION

def print_fun ( test ) :
    if test < 1 :
        return
    else :
        print ( test , end = ' ' )
        print_fun ( test - 1 )
        print ( test , end = ' ' )
        return
|||

MAXIMUM_TRIPLET_SUM_ARRAY

def max_triplet_sum ( arr , n ) :
    sum = - 1000000
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            for k in range ( j + 1 , n ) :
                if sum < arr [ i ] + arr [ j ] + arr [ k ] :
                    sum = arr [ i ] + arr [ j ] + arr [ k ]
    return sum
|||

MINIMUM_NUMBER_OF_JUMPS_TO_REACH_END_OF_A_GIVEN_ARRAY_1

def _min_jumps ( arr , n ) :
    jumps = [ ]
    i , j = 0 , 0
    if n == 0 or arr [ 0 ] == 0 :
        return int ( 'inf' )
    jumps.append ( 0 )
    for i in range ( 1 , n ) :
        jumps.append ( int ( 'inf' ) )
        for j in range ( i ) :
            if i <= j + arr [ j ] and jumps [ j ] != int ( 'inf' ) :
                jumps [ i ] = min ( jumps [ i ] , jumps [ j ] + 1 )
                break
    return jumps [ n - 1 ]
|||

MAXIMIZE_ARRAY_ELEMENTS_UPTO_GIVEN_NUMBER

def find_max_val ( arr , n , num , max_limit ) :
    ind = 0
    val = 0
    dp = [ [ 0 ] * ( n + 1 ) ] * ( max_limit + 1 )
    for ind in range ( n ) :
        for val in range ( 0 , max_limit + 1 ) :
            if ind == 0 :
                if num - arr [ ind ] == val or num + arr [ ind ] == val :
                    dp [ ind ] [ val ] = 1
                else :
                    dp [ ind ] [ val ] = 0
            else :
                if val - arr [ ind ] >= 0 and val + arr [ ind ] <= max_limit :
                    if dp [ ind - 1 ] [ val - arr [ ind ] ] == 1 or dp [ ind - 1 ] [ val + arr [ ind ] ] == 1 :
                        dp [ ind ] [ val ] = 1
                elif val - arr [ ind ] >= 0 :
                    dp [ ind ] [ val ] = dp [ ind - 1 ] [ val - arr [ ind ] ]
                elif val + arr [ ind ] <= max_limit :
                    dp [ ind ] [ val ] = dp [ ind - 1 ] [ val + arr [ ind ] ]
                else :
                    dp [ ind ] [ val ] = 0
    for val in range ( max_limit , - 1 , - 1 ) :
        if dp [ n - 1 ] [ val ] == 1 :
            return val
    return - 1
|||

PROGRAM_FOR_DEADLOCK_FREE_CONDITION_IN_OPERATING_SYSTEM

def Resources ( process , need ) :
    min_resources = 0
    min_resources = process * ( need - 1 ) + 1
    return min_resources
|||

NUMBER_DIGITS_PRODUCT_TWO_NUMBERS

def count_digits ( a , b ) :
    count = 0
    p = abs ( a * b )
    if p == 0 :
        return 1
    while p > 0 :
        count += 1
        p = p / 10
    return count
|||

FLOOR_IN_A_SORTED_ARRAY

def floorSearch ( arr , n , x ) :
    if x >= arr [ n - 1 ] :
        return n - 1
    if x < arr [ 0 ] :
        return - 1
    for i in range ( 1 , n ) :
        if arr [ i ] > x :
            return ( i - 1 )
    return - 1
|||

CHECK_WHETHER_TRIANGLE_VALID_NOT_SIDES_GIVEN

def checkValidity ( a , b , c ) :
    if a + b <= c or a + c <= b or b + c <= a :
        return 0
    else :
        return 1
|||

PRINT_N_X_N_SPIRAL_MATRIX_USING_O1_EXTRA_SPACE

def print_spiral ( n ) :
    for i in range ( n ) :
        for j in range ( n ) :
            x = min ( min ( i , j ) , min ( n - 1 - i , n - 1 - j ) )
            if i <= j :
                print ( ( n - 2 * x ) * ( n - 2 * x ) - ( i - x ) - ( j - x ) + "\t" )
            else :
                print ( ( n - 2 * x - 2 ) * ( n - 2 * x - 2 ) + ( i - x ) + ( j - x ) + "\t" )
        print ( )
|||

POSITION_ELEMENT_STABLE_SORT

def getIndexInSortedArray ( arr , n , idx ) :
    result = 0
    for i in range ( n ) :
        if arr [ i ] < arr [ idx ] :
            result += 1
        if arr [ i ] == arr [ idx ] and i < idx :
            result += 1
    return result
|||

MAXIMUM_SEGMENT_VALUE_PUTTING_K_BREAKPOINTS_NUMBER

def find_max_segment ( s , k ) :
    seg_len = len ( s ) - k
    res = 0
    for i in range ( seg_len ) :
        res = res * 10 + ( s [ i ] - '0' )
    seg_len_pow = int ( math.pow ( 10 , seg_len - 1 ) )
    curr_val = res
    for i in range ( 1 , ( len ( s ) - seg_len ) ) :
        curr_val = curr_val - ( s [ i - 1 ] - '0' ) * seg_len_pow
        curr_val = curr_val * 10 + ( s [ i + seg_len - 1 ] - '0' )
        res = max ( res , curr_val )
    return res
|||

FINDING_POWER_PRIME_NUMBER_P_N_1

def PowerOFPINnfactorial ( n , p ) :
    ans = 0
    temp = p
    while temp <= n :
        ans += n // temp
        temp = temp * p
    return ans
|||

PROGRAM_PRINT_IDENTITY_MATRIX

def identity ( num ) :
    row , col = 0 , 0
    for row in range ( num ) :
        for col in range ( num ) :
            if row == col :
                print ( 1 , end = '' )
            else :
                print ( 0 , end = '' )
        print ( )
    return 0
|||

SUM_MATRIX_ELEMENT_ELEMENT_INTEGER_DIVISION_ROW_COLUMN

def find_sum ( n ) :
    ans = 0
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , n + 1 ) :
            ans += ( i / j )
    return ans
|||

TILING_WITH_DOMINOES

def countWays ( n ) :
    A = [ 1 ] * ( n + 1 )
    B = [ 0 ] * ( n + 1 )
    for i in range ( 2 , n + 1 ) :
        A [ i ] = A [ i - 2 ] + 2 * B [ i - 1 ]
        B [ i ] = A [ i - 1 ] + B [ i - 2 ]
    return A [ n ]
|||

COUNT_DERANGEMENTS_PERMUTATION_SUCH_THAT_NO_ELEMENT_APPEARS_IN_ITS_ORIGINAL_POSITION

def count_der ( n ) :
    if n == 1 :
        return 0
    if n == 0 :
        return 1
    if n == 2 :
        return 1
    return ( n - 1 ) * ( count_der ( n - 1 ) + count_der ( n - 2 ) )
|||

FREQUENCY_ELEMENT_UNSORTED_ARRAY_1

def count_freq ( a , n ) :
    hm = { }
    for i in range ( n ) :
        hm [ a [ i ] ] += 1
    cumul = 0
    for i in range ( n ) :
        cumul += hm [ a [ i ] ]
        if hm [ a [ i ] ] != 0 :
            print ( a [ i ] , "->" , cumul )
        hm [ a [ i ] ] = 0
|||

MINIMIZE_THE_SUM_OF_DIGITS_OF_A_AND_B_SUCH_THAT_A_B_N

def minSum ( n ) :
    sum = 0
    while n > 0 :
        sum += ( n % 10 )
        n /= 10
    if sum == 1 :
        return 10
    return sum
|||

DIVIDE_CUBOID_CUBES_SUM_VOLUMES_MAXIMUM

def maximizecube ( l , b , h ) :
    side = gcd ( l , gcd ( b , h ) )
    num = l / side
    num = ( num * b / side )
    num = ( num * h / side )
    print ( side , num )
|||

CHECK_NUMBER_POWER_K_USING_BASE_CHANGING_METHOD

def is_power_of_k ( n , k ) :
    one_seen = False
    while n :
        digit = n % k
        if digit > 1 :
            return False
        if digit == 1 :
            if one_seen :
                return False
            one_seen = True
        n /= k
    return True
|||

POSITION_OF_RIGHTMOST_SET_BIT_1

def PositionRightmostSetbit ( n ) :
    position = 1
    m = 1
    while ( n & m ) == 0 :
        m = m << 1
        position += 1
    return position
|||

SEARCH_INSERT_AND_DELETE_IN_A_SORTED_ARRAY_1

def insert_sorted ( arr , n , key , capacity ) :
    if n >= capacity :
        return n
    i = 0
    for ( i , item ) in enumerate ( arr ) :
        arr [ i + 1 ] = item
    arr [ i + 1 ] = key
    return ( n + 1 , arr )
|||

FIND_THE_MAXIMUM_OF_MINIMUMS_FOR_EVERY_WINDOW_SIZE_IN_A_GIVEN_ARRAY_1

def print_max_of_min ( n ) :
    s = Stack ( )
    left = [ - 1 ] * n + [ n ]
    right = [ n ] * n + [ n ]
    for i in range ( n ) :
        left [ i ] = - 1
        right [ i ] = n
    for i in range ( n ) :
        while not s.empty ( ) and arr [ s.pop ( ) ] >= arr [ i ] :
            s.pop ( )
        if not s.empty ( ) :
            left [ i ] = s.pop ( )
        s.push ( i )
    while not s.empty ( ) :
        s.pop ( )
    for i in range ( n - 1 , - 1 , - 1 ) :
        while not s.empty ( ) and arr [ s.pop ( ) ] >= arr [ i ] :
            s.pop ( )
        if not s.empty ( ) :
            right [ i ] = s.pop ( )
        s.push ( i )
    ans = [ ]
    for i in range ( 0 , n + 1 ) :
        ans.append ( 0 )
    for i in range ( 0 , n + 1 ) :
        len = right [ i ] - left [ i ] - 1
        ans [ len ] = max ( ans [ len ] , arr [ i ] )
    for i in range ( n - 1 , - 1 , - 1 ) :
        ans [ i ] = max ( ans [ i ] , ans [ i + 1 ] )
    for i in range ( 1 , n + 1 ) :
        print ( ans [ i ] , end = ' ' )
|||

MAXIMUM_DECIMAL_VALUE_PATH_IN_A_BINARY_MATRIX_1

def MaximumDecimalValue ( mat , n ) :
    dp = [ 0 ] * n
    if mat [ 0 ] [ 0 ] == 1 :
        dp [ 0 ] [ 0 ] = 1
    for i in range ( 1 , n ) :
        if mat [ 0 ] [ i ] == 1 :
            dp [ 0 ] [ i ] = int ( dp [ 0 ] [ i - 1 ] + pow ( 2 , i ) )
        else :
            dp [ 0 ] [ i ] = dp [ 0 ] [ i - 1 ]
    for i in range ( 1 , n ) :
        if mat [ i ] [ 0 ] == 1 :
            dp [ i ] [ 0 ] = int ( dp [ i - 1 ] [ 0 ] + pow ( 2 , i ) )
        else :
            dp [ i ] [ 0 ] = dp [ i - 1 ] [ 0 ]
    for i in range ( 1 , n ) :
        for j in range ( 1 , n ) :
            if mat [ i ] [ j ] == 1 :
                dp [ i ] [ j ] = int ( max ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] ) + pow ( 2 , i + j ) )
            else :
                dp [ i ] [ j ] = max ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] )
    return dp [ n - 1 ] [ n - 1 ]
|||

COUNT_NUMBER_OF_WAYS_TO_COVER_A_DISTANCE

def print_count_rec ( dist ) :
    if dist < 0 :
        return 0
    if dist == 0 :
        return 1
    return print_count_rec ( dist - 1 ) + print_count_rec ( dist - 2 ) + print_count_rec ( dist - 3 )
|||

MOVE_VE_ELEMENTS_END_ORDER_EXTRA_SPACE_ALLOWED

def segregateElements ( arr , n ) :
    temp = [ ]
    j = 0
    for i in range ( n ) :
        if arr [ i ] >= 0 :
            temp.append ( arr [ i ] )
    if j == n or j == 0 :
        return
    for i in range ( n ) :
        if arr [ i ] < 0 :
            temp.append ( arr [ i ] )
    for i in range ( n ) :
        arr [ i ] = temp [ i ]
|||

MINIMUM_PERIMETER_N_BLOCKS

def minPerimeter ( n ) :
    l = int ( math.sqrt ( n ) )
    sq = l * l
    if sq == n :
        return l * 4
    else :
        row = n // l
        perimeter = 2 * ( l + row )
        if n % l != 0 :
            perimeter += 2
        return perimeter
|||

DYNAMIC_PROGRAMMING_SET_36_CUT_A_ROPE_TO_MAXIMIZE_PRODUCT

def max_prod ( n ) :
    if n == 0 or n == 1 :
        return 0
    max_val = 0
    for i in range ( 1 , n ) :
        max_val = max ( max_val , max ( i * ( n - i ) , max_prod ( n - i ) ** 2 ) )
    return max_val
|||

LONGEST_COMMON_SUBSTRING_SPACE_OPTIMIZED_DP_SOLUTION

def LCSubStr ( X , Y ) :
    m = len ( X )
    n = len ( Y )
    result = 0
    len = [ 0 ] * ( n - 1 )
    curr_row = 0
    for i in range ( m ) :
        for j in range ( n ) :
            if i == 0 or j == 0 :
                len [ curr_row ] [ j ] = 0
            elif X [ i - 1 ] == Y [ j - 1 ] :
                len [ curr_row ] [ j ] = len [ ( 1 - curr_row ) ] [ ( j - 1 ) ] + 1
                result = max ( result , len [ curr_row ] [ j ] )
            else :
                len [ curr_row ] [ j ] = 0
        curr_row = 1 - curr_row
    return result
|||

CHECK_GIVEN_STRING_ROTATION_PALINDROME

def isPalindrome ( str ) :
    l = 0
    h = len ( str ) - 1
    while h > l :
        if str [ l ] != str [ h -- ] :
            return False
    return True
|||

FIND_NUMBER_OF_SOLUTIONS_OF_A_LINEAR_EQUATION_OF_N_VARIABLES_1

def count_sol ( coeff , n , rhs ) :
    dp = [ 0 ] * ( rhs + 1 )
    dp [ 0 ] = 1
    for i in range ( n ) :
        for j in range ( coeff [ i ] , rhs + 1 ) :
            dp [ j ] += dp [ j - coeff [ i ] ]
    return dp [ rhs ]
|||

FIND_THE_LARGEST_PAIR_SUM_IN_AN_UNSORTED_ARRAY

def findLargestSumPair ( ) :
    first , second = arr [ 0 ] , arr [ 1 ]
    if arr [ 0 ] > arr [ 1 ] :
        first , second = arr [ 0 ] , arr [ 1 ]
    else :
        first , second = arr [ 1 ] , arr [ 0 ]
    for i in range ( 2 , len ( arr ) ) :
        if arr [ i ] > first :
            second , first = first , arr [ i ]
        elif arr [ i ] > second and arr [ i ] != first :
            second , first = first , second
    return ( first , second )
|||

FIND_BITONIC_POINT_GIVEN_BITONIC_SEQUENCE

def binary_search ( arr , left , right ) :
    if left <= right :
        mid = ( left + right ) // 2
        if arr [ mid - 1 ] < arr [ mid ] and arr [ mid ] > arr [ mid + 1 ] :
            return mid
        if arr [ mid ] < arr [ mid + 1 ] :
            return binary_search ( arr , mid + 1 , right )
        else :
            return binary_search ( arr , left , mid - 1 )
    return - 1
|||

PRINT_ALL_DISTINCT_CHARACTERS_OF_A_STRING_IN_ORDER_3_METHODS_1

def printDistinct ( str ) :
    n = len ( str )
    count = [ 0 ] * MAX_CHAR
    index = [ ]
    for i in range ( MAX_CHAR ) :
        count [ i ] = 0
        index.append ( n )
    for i in range ( n ) :
        x = str [ i ]
        yield count [ x ]
        if count [ x ] == 1 and x != ' ' :
            index.append ( i )
        if count [ x ] == 2 :
            index.append ( n )
    index.sort ( )
    for i in range ( MAX_CHAR and index [ i ] != n ) :
        print ( str [ index [ i ] ] )
|||

FIND_TWO_SIDES_RIGHT_ANGLE_TRIANGLE

def print_other_sides ( n ) :
    if n % 2 != 0 :
        if n == 1 :
            print ( "-1" )
        else :
            b = ( n * n - 1 ) / 2
            c = ( n * n + 1 ) / 2
            print ( "b = %d, c = %d" % ( b , c ) )
    else :
        if n == 2 :
            print ( "-1" )
        else :
            b = n * n / 4 - 1
            c = n * n / 4 + 1
            print ( "b = %d, c = %d" % ( b , c ) )
|||

COUNT_NUMBER_OF_STRINGS_MADE_OF_R_G_AND_B_USING_GIVEN_COMBINATION

def possible_strings ( n , r , b , g ) :
    fact = [ 1 ] * n + [ 1 ] * n
    for i in range ( 1 , n + 1 ) :
        fact [ i ] = fact [ i - 1 ] * i
    left = n - ( r + g + b )
    sum = 0
    for i in range ( 0 , left + 1 ) :
        for j in range ( 0 , left - i + 1 ) :
            k = left - ( i + j )
            sum = sum + fact [ n ] / ( fact [ i + r ] * fact [ j + b ] * fact [ k + g ] )
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
    return arr
|||

EVALUATE_AN_ARRAY_EXPRESSION_WITH_NUMBERS_AND

def calculate_sum ( arr , n ) :
    if n == 0 :
        return 0
    s = arr [ 0 ]
    value = int ( s )
    sum = value
    for i in range ( 2 , n + 1 , 2 ) :
        s = arr [ i ]
        value = int ( s )
        operation = arr [ i - 1 ] [ 0 ]
        if operation == '+' :
            sum += value
        else :
            sum -= value
    return sum
|||

SUM_MATRIX_ELEMENT_ELEMENT_INTEGER_DIVISION_ROW_COLUMN_1

def findSum ( n ) :
    ans , temp , num = 0 , 0 , 0
    for i in range ( 1 , n + 1 , 2 ) :
        temp = i - 1
        num = 1
        while temp < n :
            if temp + i <= n :
                ans += ( i * num )
            else :
                ans += ( ( n - temp ) * num )
            temp += i
            num += 1
    return ans
|||

SHUFFLE_A_DECK_OF_CARDS_3

def shuffle ( card , n ) :
    rand = random.Random ( )
    for i in range ( n ) :
        r = i + rand.randint ( 0 , 52 - i )
        temp = card [ r ]
        card [ r ] = card [ i ]
        card [ i ] = temp
|||

DOOLITTLE_ALGORITHM_LU_DECOMPOSITION

def lu_decomposition ( mat , n ) :
    lower = [ 0 ] * n
    upper = [ 0 ] * n
    for i in range ( n ) :
        for k in range ( i , n ) :
            sum = 0
            for j in range ( i ) :
                sum += ( lower [ i ] [ j ] * upper [ j ] [ k ] )
            upper [ i ] [ k ] = mat [ i ] [ k ] - sum
        for k in range ( i , n ) :
            if i == k :
                lower [ i ] [ i ] = 1
            else :
                sum = 0
                for j in range ( i ) :
                    sum += ( lower [ k ] [ j ] * upper [ j ] [ i ] )
                lower [ k ] [ i ] = ( mat [ k ] [ i ] - sum ) / upper [ i ] [ i ]
    print ( setw ( 2 ) , "     Lower Triangular" , setw ( 10 ) , "Upper Triangular" )
    for i in range ( n ) :
        for j in range ( n ) :
            print ( setw ( 4 ) , lower [ i ] [ j ] , "\t" )
        print ( "\t" )
        for j in range ( n ) :
            print ( setw ( 4 ) , upper [ i ] [ j ] , "\t" )
        print ( "\n" )
|||

PROGRAM_NTH_CATALAN_NUMBER

def catalan ( n ) :
    res = 0
    if n <= 1 :
        return 1
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
|||

CHECK_IF_A_NUMBER_IS_POWER_OF_ANOTHER_NUMBER_1

def isPower ( x , y ) :
    res1 = int ( math.log ( y , 2 ) ) / int ( math.log ( x , 2 ) )
    res2 = math.log ( y , 2 ) / math.log ( x , 2 )
    return ( res1 == res2 )
|||

LARGEST_SUBSEQUENCE_GCD_GREATER_1

def largestGCDSubsequence ( arr , n ) :
    ans = 0
    maxele = sum ( arr )
    for i in range ( 2 , maxele + 1 ) :
        count = 0
        for j in range ( n ) :
            if arr [ j ] % i == 0 :
                count += 1
        ans = max ( ans , count )
    return ans
|||

FIND_COMMON_ELEMENT_ROWS_ROW_WISE_SORTED_MATRIX

def find_common ( mat ) :
    column = [ ]
    min_row = 0
    i = 0
    for i in range ( M ) :
        column.append ( N - 1 )
    min_row = 0
    while column [ min_row ] >= 0 :
        for i in range ( M ) :
            if mat [ i ] [ column [ i ] ] < mat [ min_row ] [ column [ min_row ] ] :
                min_row = i
        eq_count = 0
        for i in range ( M ) :
            if mat [ i ] [ column [ i ] ] > mat [ min_row ] [ column [ min_row ] ] :
                if column [ i ] == 0 :
                    return - 1
                column [ i ] -= 1
            else :
                eq_count += 1
        if eq_count == M :
            return mat [ min_row ] [ column [ min_row ] ]
    return - 1
|||

CHECK_GIVEN_CIRCLE_LIES_COMPLETELY_INSIDE_RING_FORMED_TWO_CONCENTRIC_CIRCLES

def checkcircle ( r , R , r1 , x1 , y1 ) :
    dis = int ( math.sqrt ( x1 ** 2 + y1 ** 2 ) )
    return ( dis - r1 >= R and dis + r1 <= r )
|||

COUNT_TOTAL_SET_BITS_IN_ALL_NUMBERS_FROM_1_TO_N

def countSetBits ( n ) :
    i = 0
    ans = 0
    while ( 1 << i ) <= n :
        k = False
        change = 1 << i
        for j in range ( 0 , n ) :
            if k == True :
                ans += 1
            else :
                ans += 0
            if change == 1 :
                k = not k
                change = 1 << i
            else :
                change -= 1
        i += 1
    return ans
|||

LONGEST_REPEATING_SUBSEQUENCE

def find_longest_repetiating_subseq ( str ) :
    n = len ( str )
    dp = [ [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n
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
    temp = [ ]
    while i >= 0 and j < n :
        if arr [ i ] * arr [ i ] < arr [ j ] * arr [ j ] :
            temp.append ( arr [ i ] * arr [ i ] )
            i -= 1
        else :
            temp.append ( arr [ j ] * arr [ j ] )
            j += 1
        ind += 1
    while i >= 0 :
        temp.append ( arr [ i ] * arr [ i ] )
        i -= 1
    while j < n :
        temp.append ( arr [ j ] * arr [ j ] )
        j += 1
    for x in range ( n ) :
        arr [ x ] = temp [ x ]
|||

PROGRAM_TO_FIND_REMAINDER_WITHOUT_USING_MODULO_OR_OPERATOR

def getRemainder ( num , divisor ) :
    return ( num - divisor * ( num / divisor ) )
|||

MINIMUM_COST_TO_FILL_GIVEN_WEIGHT_IN_A_BAG

def MinimumCost ( cost , n , W ) :
    val = [ ]
    wt = [ ]
    size = 0
    for i in range ( n ) :
        if cost [ i ] != - 1 :
            val.append ( cost [ i ] )
            wt.append ( i + 1 )
            size += 1
    n = size
    min_cost = [ [ ] , [ ] , [ ] ]
    for i in range ( 0 , W + 1 ) :
        min_cost [ 0 ].append ( int ( i ) )
    for i in range ( 1 , n + 1 ) :
        min_cost [ i ].append ( 0 )
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , W + 1 ) :
            if wt [ i - 1 ] > j :
                min_cost [ i ] [ j ] = min_cost [ i - 1 ] [ j ]
            else :
                min_cost [ i ] [ j ] = min ( min_cost [ i - 1 ] [ j ] , min_cost [ i ] [ j - wt [ i - 1 ] ] + val [ i - 1 ] )
    return ( min_cost [ n ] [ W ] , min_cost [ n ] [ W ] )
|||

COUNT_CHARACTERS_STRING_DISTANCE_ENGLISH_ALPHABETS_1

def countPairs ( str ) :
    result = 0
    n = len ( str )
    for i in range ( n ) :
        for j in range ( 1 , n and j <= MAX_CHAR ) :
            if ( abs ( str [ i + j ] - str [ i ] ) == j ) :
                result += 1
    return result
|||

A_PRODUCT_ARRAY_PUZZLE

def productArray ( arr , n ) :
    if n == 1 :
        print ( 0 )
        return
    left = [ ]
    right = [ ]
    prod = [ ]
    i , j = 0 , 0
    left.append ( 1 )
    right.append ( 1 )
    for i in range ( 1 , n ) :
        left.append ( arr [ i - 1 ] * left [ i - 1 ] )
    for j in range ( n - 2 , - 1 , - 1 ) :
        right.append ( arr [ j + 1 ] * right [ j + 1 ] )
    for i in range ( n ) :
        prod.append ( left [ i ] * right [ i ] )
    for i in range ( n ) :
        print ( prod [ i ] , end = ' ' )
    return
|||

FREQUENT_ELEMENT_ARRAY_1

def most_frequent ( arr , n ) :
    hp = { }
    for i in range ( n ) :
        key = arr [ i ]
        if hp.has_key ( key ) :
            freq = hp [ key ]
            freq += 1
            hp [ key ] = freq
        else :
            hp [ key ] = 1
    max_count , res = 0 , - 1
    for val , count in hp.items ( ) :
        if max_count < count :
            res = val
            max_count = count
    return res
|||

PRINT_UNIQUE_ROWS

def print_array ( arr , row , col ) :
    set = set ( )
    for i in range ( row ) :
        s = ""
        for j in range ( col ) :
            s += str ( arr [ i ] [ j ] )
        if not set.issubset ( s ) :
            set.add ( s )
            print ( s )
|||

COUNT_1S_SORTED_BINARY_ARRAY

def countOnes ( arr , low , high ) :
    if high >= low :
        mid = low + ( high - low ) // 2
        if ( mid == high or arr [ mid + 1 ] == 0 ) :
            return mid + 1
        if arr [ mid ] == 1 :
            return countOnes ( arr , ( mid + 1 ) , high )
        return countOnes ( arr , low , ( mid - 1 ) )
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
|||

ROTATE_MATRIX_ELEMENTS

def rotatematrix ( m , n , mat ) :
    row , col = 0 , 0
    prev , curr = None , None
    while row < m and col < n :
        if row + 1 == m or col + 1 == n :
            break
        prev = mat [ row + 1 ] [ col ]
        for i in range ( col , n ) :
            curr = mat [ row ] [ i ]
            mat [ row ] [ i ] = prev
            prev = curr
        row += 1
        for i in range ( row , m ) :
            curr = mat [ i ] [ n - 1 ]
            mat [ i ] [ n - 1 ] = prev
            prev = curr
        n -= 1
        if row < m :
            for i in range ( n - 1 , col + 1 ) :
                curr = mat [ m - 1 ] [ i ]
                mat [ m - 1 ] [ i ] = prev
                prev = curr
        m -= 1
        if col < n :
            for i in range ( m - 1 , row + 1 ) :
                curr = mat [ i ] [ col ]
                mat [ i ] [ col ] = prev
                prev = curr
        col += 1
    for i in range ( R ) :
        for j in range ( C ) :
            print ( mat [ i ] [ j ] , end = '' )
        print ( '' )
|||

FIND_KTH_CHARACTER_OF_DECRYPTED_STRING

def encoded_char ( str , k ) :
    expand = ""
    temp = ""
    freq = 0
    for i in range ( len ( str ) ) :
        temp = ""
        freq = 0
        while i < len ( str ) and str [ i ] >= 'a' and str [ i ] <= 'z' :
            temp += str [ i ]
            i += 1
        while i < len ( str ) and str [ i ] >= '1' and str [ i ] <= '9' :
            freq = freq * 10 + str [ i ] - '0'
            i += 1
        for j in range ( 1 , freq + 1 ) :
            expand += temp
    if freq == 0 :
        expand += temp
    return expand [ k - 1 ]
|||

EFFICIENT_SEARCH_IN_AN_ARRAY_WHERE_DIFFERENCE_BETWEEN_ADJACENT_IS_1

def search ( arr , n , x ) :
    i = 0
    while i <= n - 1 :
        if arr [ i ] == x :
            return i
        i += abs ( arr [ i ] - x )
    return - 1
|||

MAXIMUM_POSSIBLE_SUM_WINDOW_ARRAY_ELEMENTS_WINDOW_ARRAY_UNIQUE

def returnMaxSum ( A , B , n ) :
    mp = set ( )
    result = 0
    curr_sum , curr_begin = 0 , 0
    for i in range ( n ) :
        while mp.issubset ( A [ i ] ) :
            mp.remove ( A [ curr_begin ] )
            curr_sum -= B [ curr_begin ]
            curr_begin += 1
        mp.add ( A [ i ] )
        curr_sum += B [ i ]
        result = max ( result , curr_sum )
    return result
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
            odd_count += 1
        if ( n & 2 ) :
            even_count += 1
        n = n >> 2
    return is_multiple_of_3 ( abs ( odd_count - even_count ) )
|||

MAXIMUM_SUM_IARRI_AMONG_ROTATIONS_GIVEN_ARRAY_1

def max_sum ( arr , n ) :
    cum_sum = 0
    for i in range ( n ) :
        cum_sum += arr [ i ]
    curr_val = 0
    for i in range ( n ) :
        curr_val += i * arr [ i ]
    res = curr_val
    for i in range ( 1 , n ) :
        next_val = curr_val - ( cum_sum - arr [ i - 1 ] ) + arr [ i - 1 ] * ( n - 1 )
        curr_val = next_val
        res = max ( res , next_val )
    return res
|||

DYNAMIC_PROGRAMMING_SET_34_ASSEMBLY_LINE_SCHEDULING

def car_assembly ( a , t , e , x ) :
    T1 = [ ]
    T2 = [ ]
    i = 0
    T1.append ( e [ 0 ] + a [ 0 ] [ 0 ] )
    T2.append ( e [ 1 ] + a [ 1 ] [ 0 ] )
    for i in range ( NUM_STATION ) :
        T1.append ( min ( T1 [ i - 1 ] + a [ 0 ] [ i ] , T2 [ i - 1 ] + t [ 1 ] [ i ] + a [ 0 ] [ i ] ) )
        T2.append ( min ( T2 [ i - 1 ] + a [ 1 ] [ i ] , T1 [ i - 1 ] + t [ 0 ] [ i ] + a [ 1 ] [ i ] ) )
    return min ( T1 [ NUM_STATION - 1 ] + x [ 0 ] , T2 [ NUM_STATION - 1 ] + x [ 1 ] )
|||

PRINT_MATRIX_SPIRAL_FORM_STARTING_POINT

def printSpiral ( mat , r , c ) :
    i , a = 0 , 2
    low_row = ( 0 > a ) & ( a < r )
    low_column = ( 0 > b ) & ( b - 1 )
    high_row = ( ( a + 1 ) >= r ) & ( r - 1 )
    high_column = ( ( b + 1 ) >= c ) & ( c - 1 )
    while ( low_row > 0 - r and low_column > 0 - c ) :
        for i in range ( low_column + 1 , high_column , c , low_row >= 0 ) :
            print ( mat [ low_row ] [ i ] , end = ' ' )
        low_row -= 1
        for i in range ( low_row + 2 , high_row , r , high_column < c ) :
            print ( mat [ i ] [ high_column ] , end = ' ' )
        high_column += 1
        for i in range ( high_column - 2 , low_column , 0 , r ) :
            print ( mat [ high_row ] [ i ] , end = ' ' )
        high_row += 1
        for i in range ( high_row - 2 , low_row , 0 , 0 , low_column >= 0 ) :
            print ( mat [ i ] [ low_column ] , end = ' ' )
        low_column -= 1
    print ( )
|||

MID_POINT_CIRCLE_DRAWING_ALGORITHM

def mid_point_circle_draw ( x_centre , y_centre , r ) :
    x , y = r
    print ( "(%d, %d)" % ( x , y ) )
    if r > 0 :
        print ( "(%d, %d)" % ( x + x_centre , - y + y_centre ) )
        print ( "(%d, %d)" % ( y + x_centre , x + y_centre ) )
        print ( "(%d, %d)" % ( - y + x_centre , x + y_centre ) )
    P = 1 - r
    while x > y :
        y += 1
        if P <= 0 :
            P = P + 2 * y + 1
        else :
            x -= 1
            P = P + 2 * y - 2 * x + 1
        if x < y :
            break
        print ( "(%d, %d)" % ( x + x_centre , y + y_centre ) )
        print ( "(%d, %d)" % ( - x + x_centre , y + y_centre ) )
        print ( "(%d, %d)" % ( x + x_centre , y + y_centre ) )
        print ( "(%d, %d)" % ( - x + x_centre , y + y_centre ) )
        print ( "(%d, %d)" % ( - y + x_centre , y + y_centre ) )
        print ( "(%d, %d)" % ( - x + x_centre , y + y_centre ) )
        if x != y :
            print ( "(%d, %d)" % ( y + x_centre , x + y_centre ) )
            print ( "(%d, %d)" % ( - y + x_centre , y + y_centre ) )
|||

SMALLEST_ELEMENT_REPEATED_EXACTLY_K_TIMES_NOT_LIMITED_SMALL_RANGE

def smallest_k_freq ( a , n , k ) :
    m = { }
    for i in range ( n ) :
        if m.has_key ( a [ i ] ) :
            m [ a [ i ] ] = m [ a [ i ] ] + 1
        else :
            m [ a [ i ] ] = 1
    res = sys.maxsize
    s = m.keys ( )
    for temp in s :
        if m [ temp ] == k :
            res = min ( res , temp )
    return ( res , - 1 )
|||

MINIMUM_XOR_VALUE_PAIR

def minXOR ( arr , n ) :
    min_xor = sys.maxint
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            min_xor = min ( min_xor , arr [ i ] ^ arr [ j ] )
    return min_xor
|||

MIRROR_CHARACTERS_STRING

def compute ( str , n ) :
    reverse_alphabet = 'zyxwvutsrqponmlkjihgfedcba'
    l = len ( str )
    answer = ""
    for i in range ( n ) :
        answer = answer + str [ i ]
    for i in range ( n , l ) :
        answer = answer + reverse_alphabet [ str [ i ] - 'a' ]
    return answer
|||

PROGRAM_CHECK_PLUS_PERFECT_NUMBER

def checkplusperfect ( x ) :
    temp = x
    n = 0
    while x != 0 :
        x /= 10
        n += 1
    x = temp
    sum = 0
    while x != 0 :
        sum += pow ( x % 10 , n )
        x /= 10
    return ( sum == temp )
|||

ARC_LENGTH_ANGLE

def arcLength ( diameter , angle ) :
    pi = 22.0 / 7.0
    arc = None
    if angle >= 360 :
        print ( "Angle cannot" + " be formed" )
        return None
    else :
        arc = ( pi * diameter ) * ( angle / 360.0 )
        return arc
|||

FIND_LAST_INDEX_CHARACTER_STRING

def find_last_index ( str , x ) :
    index = - 1
    for i in range ( len ( str ) ) :
        if str [ i ] == x :
            index = i
    return index
|||

COUNT_TRAILING_ZEROES_FACTORIAL_NUMBER

def find_trailing_zeros ( n ) :
    count = 0
    for i in range ( 5 , n // i >= 1 , 1 , 5 ) :
        count += n // i
    return count
|||

ROTATE_MATRIX_180_DEGREE

def rotate_matrix ( mat ) :
    for i in range ( N - 1 , - 1 , - 1 ) :
        for j in range ( N - 1 , - 1 , - 1 ) :
            print ( mat [ i ] [ j ] , end = ' ' )
        print ( )
|||

SUM_FIBONACCI_NUMBERS

def calculate_sum ( n ) :
    if n <= 0 :
        return 0
    fibo = [ 0 ] * ( n + 1 )
    sum = fibo [ 0 ] + fibo [ 1 ]
    for i in range ( 2 , n + 1 ) :
        fibo [ i ] = fibo [ i - 1 ] + fibo [ i - 2 ]
        sum += fibo [ i ]
    return sum
|||

LARGEST_LEXICOGRAPHIC_ARRAY_WITH_AT_MOST_K_CONSECUTIVE_SWAPS

def KSwapMaximum ( arr , n , k ) :
    for i in range ( n - 1 and k > 0 ) :
        index_position = i
        for j in range ( i + 1 , n ) :
            if k <= j - i :
                break
            if arr [ j ] > arr [ index_position ] :
                index_position = j
        for j in range ( index_position , i > 0 ) :
            SwapInts ( arr , j , j - 1 )
        k -= index_position - i
|||

FIND_WHETHER_GIVEN_INTEGER_POWER_3_NOT

def check ( n ) :
    return 1162261467 % n == 0
|||

FIND_THE_TWO_REPEATING_ELEMENTS_IN_A_GIVEN_ARRAY

def printRepeating ( arr , size ) :
    i , j = 0 , 0
    print ( "Repeated Elements are :" )
    for i in range ( size ) :
        for j in range ( i + 1 , size ) :
            if arr [ i ] == arr [ j ] :
                print ( arr [ i ] , end = ' ' )
|||

C_PROGRAM_FIND_AREA_TRIANGLE

def findArea ( a , b , c ) :
    if a < 0 or b < 0 or c < 0 or ( a + b <= c ) or a + c <= b or b + c <= a :
        print ( "Not a valid triangle" )
        exit ( 0 )
    s = ( a + b + c ) / 2
    return float ( math.sqrt ( s * ( s - a ) * ( s - b ) * ( s - c ) ) )
|||

GIVEN_LARGE_NUMBER_CHECK_SUBSEQUENCE_DIGITS_DIVISIBLE_8_1

def is_subseq_divisible ( str ) :
    n = len ( str )
    dp = [ [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0
|||

DELETE_ARRAY_ELEMENTS_WHICH_ARE_SMALLER_THAN_NEXT_OR_BECOME_SMALLER

def delete_elements ( arr , n , k ) :
    s = Stack ( )
    s.push ( arr [ 0 ] )
    count = 0
    for i in range ( 1 , n ) :
        while not s.empty ( ) and s.peek ( ) < arr [ i ] and count < k :
            s.pop ( )
            count += 1
        s.push ( arr [ i ] )
    m = len ( s )
    v = [ ]
    while not s.empty ( ) :
        v.append ( s.peek ( ) )
        s.pop ( )
    for x in v :
        print ( x , end = '' ) ;
    print ( '' )
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
                min_len = end - start
            curr_sum -= arr [ start ]
    return min_len
|||

FIND_PAIRS_IN_ARRAY_WHOSE_SUMS_ALREADY_EXIST_IN_ARRAY_1

def find_pair ( arr , n ) :
    s = set ( )
    for i in arr :
        s.add ( i )
    found = False
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            sum = arr [ i ] + arr [ j ]
            if s.intersection ( sum ) :
                found = True
                print ( arr [ i ] , arr [ j ] )
    if found == False :
        print ( "Not Exist " )
|||

COUNT_ARITHMETIC_PROGRESSION_SUBSEQUENCES_ARRAY

def numofAP ( a , n ) :
    minarr = + 2147483647
    maxarr = - 2147483648
    for i in range ( n ) :
        minarr = min ( minarr , a [ i ] )
        maxarr = max ( maxarr , a [ i ] )
    dp = [ ]
    sum = [ ]
    ans = n + 1
    for d in range ( ( minarr - maxarr ) , ( maxarr - minarr ) + 1 ) :
        sum.append ( 0 )
        for i in range ( n ) :
            dp.append ( 1 )
            if a [ i ] - d >= 1 and a [ i ] - d <= 1000000 :
                dp [ i ] += sum [ a [ i ] - d ]
            ans += dp [ i ] - 1
            sum [ a [ i ] ] += dp [ i ]
    return ans
|||

COUNT_NUMBERS_THAT_DONT_CONTAIN_3

def count ( n ) :
    if n < 3 :
        return n
    if n >= 3 and n < 10 :
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
            temp = A [ i ] [ j ]
            A [ i ] [ j ] = A [ j ] [ i ]
            A [ j ] [ i ] = temp
|||

SUM_DIAGONALS_SPIRAL_ODD_ORDER_SQUARE_MATRIX

def spiral_dia_sum ( n ) :
    if n == 1 :
        return 1
    return ( 4 * n ** 2 - 6 * n + 6 + spiral_dia_sum ( n - 2 ) )
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
|||

FIND_SUM_NODES_GIVEN_PERFECT_BINARY_TREE

def sumNodes ( l ) :
    leafNodeCount = int ( math.pow ( 2 , l - 1 ) )
    vec = [ ]
    for i in range ( 1 , l + 1 ) :
        vec.append ( [ ] )
    for i in range ( 1 , leafNodeCount ) :
        vec [ - 1 ].append ( i )
    for i in range ( l - 2 , - 1 , - 1 ) :
        k = 0
        while k < len ( vec [ i + 1 ] ) - 1 :
            vec [ i ].append ( vec [ i + 1 ] [ k ] + vec [ i + 1 ] [ k + 1 ] )
            k += 2
    sum = 0
    for i in range ( l ) :
        for j in range ( len ( vec [ i ] ) ) :
            sum += vec [ i ] [ j ]
    return sum
|||

SUM_OF_ALL_PROPER_DIVISORS_OF_A_NATURAL_NUMBER

def div_sum ( num ) :
    result = 0
    for i in range ( 2 , math.sqrt ( num ) ) :
        if num % i == 0 :
            if i == ( num / i ) :
                result += i
            else :
                result += ( i + num / i )
    return ( result + 1 )
|||

FIND_A_TRIPLET_THAT_SUM_TO_A_GIVEN_VALUE_2

def find3Numbers ( A , arr_size , sum ) :
    for i in range ( arr_size - 2 ) :
        s = set ( )
        curr_sum = sum - A [ i ]
        for j in range ( i + 1 , arr_size ) :
            if s.issubset ( curr_sum - A [ j ] ) and curr_sum - A [ j ] not in ( s.pop ( ) , curr_sum - A [ j ] ) :
                print ( "Triplet is %d, %d, %d" % ( A [ i ] , A [ j ] , curr_sum - A [ j ] ) )
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
    for i in range ( 1 , n + 1 ) :
        count , temp = 0 , i
        while temp % p == 0 :
            count += 1
            temp = temp // p
        ans += count
    return ans
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
    return dp [ l ] [ r ] [ k ] = min ( min ( cost + solve ( X , Y , l - 1 , r - 1 , k - 1 , dp ) , solve ( X , Y , l - 1 , r , k , dp ) ) , min ( cost + solve ( X , Y , l , r - 1 , k , dp ) , solve ( X , Y , l , r - 1 , k , dp ) ) )
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
        print ( str [ i + 1 ] )
    else :
        print ( "Empty string" )
|||

SORT_1_N_SWAPPING_ADJACENT_ELEMENTS

def sortedAfterSwap ( A , B , n ) :
    i , j = 0 , 0
    for i in range ( n - 1 ) :
        if B [ i ] :
            j = i
            while B [ j ] : j += 1
            A.sort ( i , j + 1 )
            i = j
    for i in range ( n ) :
        if A [ i ] != i + 1 :
            return False
    return True
|||

GENERATE_PYTHAGOREAN_TRIPLETS

def pythagorean_triplets ( limit ) :
    a , b , c = 0 , 0 , 0
    m = 2
    while c < limit :
        for n in range ( 1 , m ) :
            a , b , c = m * m - n * n , 2 * m * n , m * m + n * n
            if c > limit :
                break
            print ( a , b , c )
        m += 1
|||

COUNT_EVEN_LENGTH_BINARY_SEQUENCES_WITH_SAME_SUM_OF_FIRST_AND_SECOND_HALF_BITS

def count_seq ( n , diff ) :
    if abs ( diff ) > n :
        return 0
    if n == 1 and diff == 0 :
        return 2
    if n == 1 and abs ( diff ) == 1 :
        return 1
    res = count_seq ( n - 1 , diff + 1 ) + 2 * count_seq ( n - 1 , diff ) + count_seq ( n - 1 , diff - 1 )
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
    return False
|||

PRINT_ARRAY_STRINGS_SORTED_ORDER_WITHOUT_COPYING_ONE_STRING_ANOTHER

def printInSortedOrder ( arr , n ) :
    index = [ ]
    i , j , min = 0 , 0 , 0
    for i in range ( n ) :
        index.append ( i )
    for i in range ( n - 1 ) :
        min = i
        for j in range ( i + 1 , n ) :
            if arr [ index [ min ] ] > arr [ index [ j ] ] :
                min = j
        if min != i :
            temp = index [ min ]
            index [ min ] , index [ i ] = index [ i ] , index [ i ]
            index [ i ] = temp
    for i in range ( n ) :
        print ( arr [ index [ i ] ] , end = ' ' )
|||

GAME_REPLACING_ARRAY_ELEMENTS

def play_game ( arr ) :
    set = set ( )
    for i in arr :
        set.add ( i )
    return ( len ( set ) % 2 == 0 )
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
        if i > 0 and arr [ i - 1 ] > arr [ i ] :
            swap ( arr , i - 1 , i )
        if i < n - 1 and arr [ i ] < arr [ i + 1 ] :
            swap ( arr , i , i + 1 )
|||

MAXIMUM_SUBARRAY_SUM_USING_PREFIX_SUM

def maximum_sum_subarray ( arr , n ) :
    min_prefix_sum = 0
    res = int ( '-1' )
    prefix_sum = [ arr [ 0 ] ]
    for i in range ( 1 , n ) :
        prefix_sum [ i ] = prefix_sum [ i - 1 ] + arr [ i ]
    for i in range ( n ) :
        res = max ( res , prefix_sum [ i ] - min_prefix_sum )
        min_prefix_sum = min ( min_prefix_sum , prefix_sum [ i ] )
    return res
|||

STRING_CONTAINING_FIRST_LETTER_EVERY_WORD_GIVEN_STRING_SPACES

def firstLetterWord ( str ) :
    result = ""
    v = True
    for c in str :
        if c == " " :
            v = True
        elif c != " " and v == True :
            result += ( c )
            v = False
    return result
|||

SUM_PAIRWISE_PRODUCTS_1

def find_sum ( n ) :
    multiterms = n * ( n + 1 ) / 2
    sum = multiterms
    for i in range ( 2 , n + 1 ) :
        multiterms = multiterms - ( i - 1 )
        sum = sum + multiterms ** i
    return sum
|||

CLUSTERINGPARTITIONING_AN_ARRAY_SUCH_THAT_SUM_OF_SQUARE_DIFFERENCES_IS_MINIMUM_1

def min_cost ( a , n , k ) :
    dp = [ [ inf ] * n + [ k + 1 ] * k + [ 0 ] * n + [ 0 ] * k + [ 0 ] * n + [ 0 ] * k + [ 0 ] * n + [ 0 ] * k + [ 0 ] * n + [ 0 ] * k + [ 0 ] * n + [ 0 ] * k + [ 0 ] * n + [ 0 ] * k + [ 0 ] * n + [ 0 ] * k + [ 0 ] * n + [ 0 ] * k + [ 0 ] * n + [ 0 ] * k + [ 0 ] * n + [ 0 ] * k + [ 0 ] * k + [ 0 ] * n + [ 0 ] * k + [ 0 ] * k + [ 0 ] * n + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * n + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k + [ 0 ] * k ]
|||

LEIBNIZ_HARMONIC_TRIANGLE

def LeibnizHarmonicTriangle ( n ) :
    C = [ [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n ]
    
|||

CHECK_WHETHER_SECOND_STRING_CAN_FORMED_FIRST_STRING_USING_COUNT_ARRAY

def can_make_str2 ( str1 , str2 ) :
    count = [ 0 ] * MAX
    str3 = str1.split ( ' ' )
    for i in range ( len ( str3 ) ) :
        count [ str3 [ i ] ] += 1
    str4 = str2.split ( ' ' )
    for i in range ( len ( str4 ) ) :
        if count [ str4 [ i ] ] == 0 :
            return False
        count [ str4 [ i ] ] -= 1
    return True
|||

SUM_MINIMUM_MAXIMUM_ELEMENTS_SUBARRAYS_SIZE_K

def SumOfKsubArray ( arr , k ) :
    sum = 0
    S , G = deque ( ) , deque ( )
    i = 0
    for i in range ( k ) :
        while not S.empty ( ) and arr [ S.popleft ( ) ] >= arr [ i ] :
            S.popleft ( )
        while not G.empty ( ) and arr [ G.popleft ( ) ] <= arr [ i ] :
            G.popleft ( )
        G.append ( i )
        S.append ( i )
    for i in range ( len ( arr ) ) :
        sum += arr [ S.popleft ( ) ] + arr [ G.popleft ( ) ]
        while not S.empty ( ) and S.popleft ( ) <= i - k :
            S.popleft ( )
        while not G.empty ( ) and G.popleft ( ) <= i - k :
            G.popleft ( )
        while not S.empty ( ) and arr [ S.popleft ( ) ] >= arr [ i ] :
            S.popleft ( )
        while not G.empty ( ) and arr [ G.popleft ( ) ] <= arr [ i ] :
            G.popleft ( )
        G.append ( i )
        S.append ( i )
    sum += arr [ S.popleft ( ) ] + arr [ G.popleft ( ) ]
    return sum
|||

LONGEST_COMMON_SUBSEQUENCE

def lcs ( X , Y , m , n ) :
    if m == 0 or n == 0 :
        return 0
    if X [ m - 1 ] == Y [ n - 1 ] :
        return 1 + lcs ( X , Y , m - 1 , n - 1 )
    else :
        return max ( lcs ( X , Y , m , n - 1 ) , lcs ( X , Y , m - 1 , n ) )
|||

MINIMUM_SUM_ABSOLUTE_DIFFERENCE_PAIRS_TWO_ARRAYS

def find_min_sum ( a , b , n ) :
    a.sort ( )
    b.sort ( )
    sum = 0
    for i in range ( n ) :
        sum = sum + abs ( a [ i ] - b [ i ] )
    return sum
|||

COUNT_DISTINCT_NON_NEGATIVE_PAIRS_X_Y_SATISFY_INEQUALITY_XX_YY_N_2

def count_solutions ( n ) :
    res = 0
    for x in range ( 0 , n * n ) :
        for y in range ( 0 , x * x + y * y ) :
            res += 1
    return res
|||

FIND_NUMBER_TRANSFORMATION_MAKE_TWO_MATRIX_EQUAL

def count_ops ( A , B , m , n ) :
    for i in range ( n ) :
        for j in range ( m ) :
            A [ i ] [ j ] -= B [ i ] [ j ]
    for i in range ( 1 , n ) :
        for j in range ( 1 , m ) :
            if A [ i ] [ j ] - A [ i ] [ 0 ] - A [ 0 ] [ j ] + A [ 0 ] [ 0 ] != 0 :
                return - 1
    result = 0
    for i in range ( n ) :
        result += abs ( A [ i ] [ 0 ] )
    for j in range ( m ) :
        result += abs ( A [ 0 ] [ j ] - A [ 0 ] [ 0 ] )
    return ( result )
|||

EFFICIENTLY_FIND_FIRST_REPEATED_CHARACTER_STRING_WITHOUT_USING_ADDITIONAL_DATA_STRUCTURE_ONE_TRAVERSAL

def FirstRepeated ( str ) :
    checker = 0
    for i in range ( len ( str ) ) :
        val = ord ( str [ i ] ) - ord ( 'a' )
        if ( checker & ( 1 << val ) ) > 0 :
            return i
        checker |= ( 1 << val )
    return - 1
|||

MAXIMUM_UNIQUE_ELEMENT_EVERY_SUBARRAY_SIZE_K

def find_max ( A , N , K ) :
    Count = { }
    for i in range ( K - 1 ) :
        if Count.has_key ( A [ i ] ) :
            Count [ A [ i ] ] = 1 + Count [ A [ i ] ]
        else :
            Count [ A [ i ] ] = 1
    Myset = TreeSet ( )
    for x in Count.items ( ) :
        if int ( str ( x ) ) == 1 :
            Myset.add ( int ( str ( x ) ) )
    for i in range ( K - 1 , N ) :
        if Count.has_key ( A [ i ] ) :
            Count [ A [ i ] ] = 1 + Count [ A [ i ] ]
        else :
            Count [ A [ i ] ] = 1
        if int ( str ( Count [ A [ i ] ] ) ) == 1 :
            Myset.add ( A [ i ] )
        else :
            Myset.remove ( A [ i ] )
        if len ( Myset ) == 0 :
            print ( "Nothing" )
        else :
            print ( Myset.last ( ) )
        x = A [ i - K + 1 ]
        Count [ x ] = Count [ x ] - 1
        if int ( str ( Count [ x ] ) ) == 1 :
            Myset.add ( x )
        if int ( str ( Count [ x ] ) ) == 0 :
            Myset.remove ( x )
|||

MINIMUM_COST_SORT_MATRIX_NUMBERS_0_N2_1

def calculate_energy ( mat , n ) :
    i_des , j_des , q = mat
    tot_energy = 0
    for i in range ( n ) :
        for j in range ( n ) :
            q = mat [ i ] [ j ] / n
            i_des = q
            j_des = mat [ i ] [ j ] - ( n * q )
            tot_energy += abs ( i_des - i ) + abs ( j_des - j )
    return tot_energy
|||

LONGEST_COMMON_SUBSTRING

def LCSubStr ( X , Y , m , n ) :
    LCStuff = [ [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] *
|||

MAXIMUM_SUM_BITONIC_SUBARRAY

def max_sum_bitonic_sub_arr ( arr , n ) :
    msis = [ ]
    msds = [ ]
    max_sum = int ( "-1" )
    msis.append ( arr [ 0 ] )
    for i in range ( 1 , n ) :
        if arr [ i ] > arr [ i - 1 ] :
            msis.append ( msis [ i - 1 ] + arr [ i ] )
        else :
            msis.append ( arr [ i ] )
    msds.append ( arr [ n - 1 ] )
    for i in range ( n - 2 , - 1 , - 1 ) :
        if arr [ i ] > arr [ i + 1 ] :
            msds.append ( msds [ i + 1 ] + arr [ i ] )
        else :
            msds.append ( arr [ i ] )
    for i in range ( n ) :
        if max_sum < ( msis [ i ] + msds [ i ] - arr [ i ] ) :
            max_sum = msis [ i ] + msds [ i ] - arr [ i ]
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

def print_all_ap_triplets ( arr , n ) :
    s = [ ]
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            diff = arr [ j ] - arr [ i ]
            exists = s.count ( arr [ i ] - diff )
            if exists :
                print ( arr [ i ] - diff , arr [ i ] , arr [ j ] )
        s.append ( arr [ i ] )
|||

QUERIES_COUNTS_ARRAY_ELEMENTS_VALUES_GIVEN_RANGE

def countInRange ( arr , n , x , y ) :
    count = 0
    for i in range ( n ) :
        if arr [ i ] >= x and arr [ i ] <= y :
            count += 1
    return count
|||

HIGHWAY_BILLBOARD_PROBLEM

def max_revenue ( m , x , revenue , n , t ) :
    max_rev = [ 0 ] * m + [ 0 ] * m
    nxtbb = 0
    for i in range ( m + 1 ) :
        if nxtbb < n :
            if x [ nxtbb ] != i :
                max_rev [ i ] = max_rev [ i - 1 ]
            else :
                if i <= t :
                    max_rev [ i ] = max ( max_rev [ i - 1 ] , revenue [ nxtbb ] )
                else :
                    max_rev [ i ] = max ( max_rev [ i - t - 1 ] + revenue [ nxtbb ] , max_rev [ i - 1 ] )
                nxtbb += 1
        else :
            max_rev [ i ] = max_rev [ i - 1 ]
    return max_rev [ m ]
|||

CONSTRUCT_GRAPH_GIVEN_DEGREES_VERTICES

def printMat ( degseq , n ) :
    mat = [ [ 0 ] * n for i in range ( n ) ]
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if degseq [ i ] > 0 and degseq [ j ] > 0 :
                degseq [ i ] -= 1
                degseq [ j ] -= 1
                mat [ i ] [ j ] = 1
                mat [ j ] [ i ] = 1
    print ( "\n" + setw ( 3 ) + "     " )
    for i in range ( n ) :
        print ( setw ( 3 ) + "(" + str ( i ) + ")" )
    print ( "\n\n" )
    for i in range ( n ) :
        print ( setw ( 4 ) + "(" + str ( i ) + ")" )
        for j in range ( n ) :
            print ( setw ( 5 ) + mat [ i ] [ j ] )
        print ( "\n" )
|||

DETECT_IF_TWO_INTEGERS_HAVE_OPPOSITE_SIGNS

def oppositeSigns ( x , y ) :
    return ( ( x ^ y ) < 0 )
|||

TRIANGULAR_NUMBERS_1

def isTriangular ( num ) :
    if num < 0 :
        return False
    c = ( - 2 * num )
    b , a = 1 , 1
    d = ( b ** 2 ) - ( 4 * a ** 2 )
    if d < 0 :
        return False
    root1 = ( - b + float ( math.sqrt ( d ) ) ) / ( 2 * a )
    root2 = ( - b - float ( math.sqrt ( d ) ) ) / ( 2 * a )
    if root1 and math.floor ( root1 ) == root1 :
        return True
    if root2 and math.floor ( root2 ) == root2 :
        return True
    return False
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
|||

LAST_NON_ZERO_DIGIT_FACTORIAL

def last_non0_digit ( n ) :
    if n < 10 :
        return dig [ n ]
    if ( ( n / 10 ) % 10 ) % 2 == 0 :
        return ( 6 * last_non0_digit ( n / 5 ) * dig [ n % 10 ] ) % 10
    else :
        return ( 4 * last_non0_digit ( n / 5 ) * dig [ n % 10 ] ) % 10
|||

SORT_STRING_ACCORDING_ORDER_DEFINED_ANOTHER_STRING

def sortByPattern ( str , pat ) :
    count = [ 0 for i in range ( len ( str ) ) ]
    index = 0
    for i in range ( len ( pat ) ) :
        for j in range ( count [ pat [ i ] - 'a' ] ) :
            str [ index ] = pat [ i ]
    return str , count
|||

NUMBER_VISIBLE_BOXES_PUTTING_ONE_INSIDE_ANOTHER

def minimumBox ( arr , n ) :
    q = Queue ( )
    q.put ( arr [ 0 ] )
    q.put ( arr [ 1 ] )
    for i in range ( 1 , n ) :
        now = q.get ( )
        if arr [ i ] >= 2 * now :
            q.put ( )
        q.put ( arr [ i ] )
    return q.get ( )
|||

SEARCH_INSERT_AND_DELETE_IN_A_SORTED_ARRAY

def binary_search ( arr , low , high , key ) :
    if high < low :
        return - 1
    mid = ( low + high ) // 2
    if key == arr [ mid ] :
        return mid
    if key > arr [ mid ] :
        return binary_search ( arr [ ( mid + 1 ) : ] , high , key )
    return binary_search ( arr [ low : ( mid - 1 ) ] , key )
|||

FIND_THE_TWO_REPEATING_ELEMENTS_IN_A_GIVEN_ARRAY_3

def printRepeating ( arr , size ) :
    i = 0
    print ( "The repeating elements are : " )
    for i in range ( size ) :
        if arr [ abs ( arr [ i ] ) ] > 0 :
            arr [ abs ( arr [ i ] ) ] = - arr [ abs ( arr [ i ] ) ]
        else :
            print ( abs ( arr [ i ] ) , end = ' ' )
|||

COUNT_POSSIBLE_GROUPS_SIZE_2_3_SUM_MULTIPLE_3

def findgroups ( arr , n ) :
    c = [ 0 , 0 , 0 ]
    i = 0
    res = 0
    for i in range ( n ) :
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

def print_string_alternate ( str ) :
    occ = [ 0 ] * 122
    s = str.lower ( )
    for i in range ( len ( str ) ) :
        temp = s [ i ]
        occ [ temp ] += 1
        if occ [ temp ] % 2 != 0 :
            print ( str [ i ] )
    print ( )
|||

NUMBER_DAYS_TANK_WILL_BECOME_EMPTY

def min_days_to_empty ( C , l ) :
    if l >= C :
        return C
    eq_root = ( math.sqrt ( 1 + 8 * ( C - l ) ) - 1 ) / 2
    return int ( math.ceil ( eq_root ) + l )
|||

REVERSE_STRING_WITHOUT_USING_ANY_TEMPORARY_VARIABLE

def reversingString ( str , start , end ) :
    while start < end :
        str [ start ] ^= str [ end ]
        str [ end ] ^= str [ start ]
        str [ start ] ^= str [ end ]
        start += 1
        end -= 1
    return str
|||

FREQUENCY_ELEMENT_UNSORTED_ARRAY

def count_freq ( a , n ) :
    hm = { }
    for i in range ( n ) :
        hm [ a [ i ] ] = hm [ a [ i ] ] if i in hm else 1
    st = sorted ( hm.items ( ) , key = lambda x : x [ 1 ] )
    cumul = 0
    for x in st :
        cumul += x [ 1 ]
        print ( x [ 0 ] , cumul )
|||

FIND_ROTATION_COUNT_ROTATED_SORTED_ARRAY

def count_rotations ( arr , n ) :
    min , min_index = arr [ 0 ] , - 1
    for i in range ( n ) :
        if min > arr [ i ] :
            min , min_index = arr [ i ] , i
    return min_index
|||

LONGEST_INCREASING_SUBSEQUENCE_1

def lis ( arr , n ) :
    lis = [ 1 ] * n
    i , j , max = 0 , 0
    for i in range ( n ) :
        lis [ i ] = 1
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if arr [ i ] > arr [ j ] and lis [ i ] < lis [ j ] + 1 :
                lis [ i ] = lis [ j ] + 1
    for i in range ( n ) :
        if max < lis [ i ] :
            max = lis [ i ]
    return max
|||

MEDIAN_OF_TWO_SORTED_ARRAYS

def getMedian ( ar1 , ar2 , n ) :
    i = 0
    j = 0
    count = 0
    m1 , m2 = - 1 , - 1
    for count in range ( 0 , n ) :
        if i == n :
            m1 , m2 = m2 , ar2 [ 0 ]
            break
        elif j == n :
            m1 , m2 = m2 , ar1 [ 0 ]
            break
        if ar1 [ i ] < ar2 [ j ] :
            m1 , m2 = m2 , ar1 [ i ]
            i += 1
        else :
            m1 , m2 = m2 , ar2 [ j ]
            j += 1
    return ( m1 + m2 ) / 2
|||

LEXICOGRAPHICALLY_MINIMUM_STRING_ROTATION

def minLexRotation ( str ) :
    n = len ( str )
    arr = [ ]
    concat = str + str
    for i in range ( n ) :
        arr.append ( concat [ i : i + n ] )
    arr.sort ( )
    return ''.join ( arr )
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
            lo = pos + 1
        else :
            hi = pos - 1
    return - 1
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
        elif ( arr1 [ l ] + arr2 [ r ] ) < x :
            l += 1
        else :
            r -= 1
    return count
|||

COUNT_SUBSETS_DISTINCT_EVEN_NUMBERS

def count_subsets ( arr , n ) :
    us = set ( )
    even_count = 0
    for i in range ( n ) :
        if arr [ i ] % 2 == 0 :
            us.add ( arr [ i ] )
    even_count = len ( us )
    return int ( pow ( 2 , even_count ) - 1 )
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

def Restore_Tree ( S , End ) :
    Identity = [ ]
    for i in range ( N ) :
        Identity.append ( i )
    parent = [ ]
    del Identity [ 0 ]
    curr_parent = Identity [ 0 ]
    for j in range ( 1 , N ) :
        child = Identity [ j ]
        if End [ child ] - j > 1 :
            parent.append ( curr_parent )
            curr_parent = child
        else :
            parent.append ( curr_parent )
            while parent [ child ] > - 1 and End [ child ] == End [ parent [ child ] ] :
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
    C , c1 , c2 = 0 , 0 , 0
    for c in s :
        if c == 'a' :
            c1 += 1
        if c == 'b' :
            c2 += 1
            C += c1
    return C * K + ( K * ( K - 1 ) / 2 ) * c1 * c2
|||

NUMBER_SUBSTRINGS_STRING

def count_non_empty_substr ( str ) :
    n = len ( str )
    return n * ( n + 1 ) // 2
|||

MAXIMUM_NUMBER_CHARACTERS_TWO_CHARACTER_STRING_1

def maximum_chars ( str ) :
    n = len ( str )
    res = - 1
    first_ind = [ - 1 ] * MAX_CHAR
    for i in range ( MAX_CHAR ) :
        first_ind [ i ] = - 1
    for i in range ( n ) :
        first_ind [ str [ i ] ] = i
    res = max ( res , abs ( i - first_ind [ - 1 ] ) )
    return res
|||

SUM_SQUARES_BINOMIAL_COEFFICIENTS

def sumofsquare ( n ) :
    C = [ [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n +
|||

PRINT_POSSIBLE_STRINGS_CAN_MADE_PLACING_SPACES_2

def print_subsequences ( s ) :
    s = s.split ( )
    n = len ( s )
    opsize = int ( math.pow ( 2 , n - 1 ) )
    for counter in range ( opsize ) :
        for j in range ( n ) :
            print ( s [ j ] )
            if ( counter & ( 1 << j ) ) > 0 :
                print ( " " )
        print ( )
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
|||

SUM_OF_ALL_ELEMENTS_UP_TO_NTH_ROW_IN_A_PASCALS_TRIANGLE

def calculate_sum ( n ) :
    sum = 0
    for row in range ( n ) :
        sum = sum + ( 1 << row )
    return sum
|||

CHECK_TWO_STRINGS_K_ANAGRAMS_NOT

def arek_anagrams ( str1 , str2 , k ) :
    n = len ( str1 )
    if len ( str2 ) != n :
        return False
    count1 = [ ]
    count2 = [ ]
    count = 0
    for i in range ( n ) :
        count1.append ( str1 [ i ] - 'a' )
    for i in range ( n ) :
        count2.append ( str2 [ i ] - 'a' )
    for i in range ( MAX_CHAR ) :
        if count1 [ i ] > count2 [ i ] :
            count = count + abs ( count1 [ i ] - count2 [ i ] )
    return ( count <= k )
|||

LONGEST_SPAN_SUM_TWO_BINARY_ARRAYS

def longest_common_sum ( n ) :
    max_len = 0
    for i in range ( n ) :
        sum1 , sum2 = 0 , 0
        for j in range ( i , n ) :
            sum1 += arr1 [ j ]
            sum2 += arr2 [ j ]
            if sum1 == sum2 :
                len = j - i + 1
            else :
                len = j - i
            if len > max_len :
                max_len = len
    return max_len
|||

REMAINDER_7_LARGE_NUMBERS

def remainder_with_7 ( num ) :
    series = [ 1 , 3 , 2 , - 1 , - 3 , - 2 ]
    series_index = 0
    result = 0
    for i in range ( len ( num ) - 1 , - 1 , - 1 ) :
        digit = num [ i ] - '0'
        result += digit * series [ series_index ]
        series_index = ( series_index + 1 ) % 6
        result %= 7
    if result < 0 :
        result = ( result + 7 ) % 7
    return result
|||

LEXICOGRAPHICALLY_PREVIOUS_PERMUTATION_IN_C

def prevPermutation ( str ) :
    n = len ( str ) - 1
    i = n
    while i > 0 and str [ i - 1 ] <= str [ i ] : i -= 1
    if i <= 0 :
        return False
    j = i - 1
    while j + 1 <= n and str [ j + 1 ] <= str [ i - 1 ] : j += 1
    swap ( str [ i - 1 ] , str [ j ] )
    s = [ str [ i - 1 ] ]
    s.reverse ( )
    str = ''.join ( s )
    return True
|||

NUMBER_SUBSEQUENCES_FORM_AI_BJ_CK

def countSubsequences ( s ) :
    aCount = 0
    bCount = 0
    cCount = 0
    for c in s :
        if c == 'a' :
            aCount = ( 1 + 2 * aCount )
        elif c == 'b' :
            bCount = ( aCount + 2 * bCount )
        elif c == 'c' :
            cCount = ( bCount + 2 * cCount )
    return cCount
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
|||

MAXIMUM_POSSIBLE_DIFFERENCE_TWO_SUBSETS_ARRAY_1

def maxDiff ( arr , n ) :
    result = 0
    arr.sort ( )
    for i in range ( n - 1 ) :
        if arr [ i ] != arr [ i + 1 ] :
            result += abs ( arr [ i ] )
        else :
            i += 1
    if arr [ n - 2 ] != arr [ n - 1 ] :
        result += abs ( arr [ n - 1 ] )
    return result
|||

PROGRAM_PRINT_SUM_GIVEN_NTH_TERM

def summing_series ( n ) :
    S = 0
    for i in range ( 1 , n + 1 ) :
        S += i ** 2 - ( i - 1 ) ** 2
    return S
|||

PREFIX_SUM_2D_ARRAY

def prefix_sum_2d ( a ) :
    R , C = a.shape
    psa = np.zeros ( ( R , C ) )
    psa [ 0 ] [ 0 ] = a [ 0 ] [ 0 ]
    for i in range ( 1 , C ) :
        psa [ 0 ] [ i ] = psa [ 0 ] [ i - 1 ] + a [ 0 ] [ i ]
    for i in range ( 1 , R ) :
        psa [ i ] [ 0 ] = psa [ i - 1 ] [ 0 ] + a [ i ] [ 0 ]
    for i in range ( 1 , R ) :
        for j in range ( 1 , C ) :
            psa [ i ] [ j ] = psa [ i - 1 ] [ j ] + psa [ i ] [ j - 1 ] - psa [ i - 1 ] [ j - 1 ] + a [ i ] [ j ]
    for i in range ( 0 , R ) :
        for j in range ( 0 , C ) :
            print ( psa [ i ] [ j ] , end = ' ' )
        print ( )
|||

MAXIMUM_NUMBER_2X2_SQUARES_CAN_FIT_INSIDE_RIGHT_ISOSCELES_TRIANGLE

def number_of_squares ( base ) :
    base = ( base - 2 )
    base = base / 2
    return base * ( base + 1 ) / 2
|||

GIVEN_BINARY_STRING_COUNT_NUMBER_SUBSTRINGS_START_END_1_1

def countSubStr ( str , n ) :
    m = 0
    for i in range ( n ) :
        if str [ i ] == '1' :
            m += 1
    return m * ( m - 1 ) / 2
|||

CONVERTING_ONE_STRING_USING_APPEND_DELETE_LAST_OPERATIONS

def isConvertible ( str1 , str2 , k ) :
    if ( len ( str1 ) + len ( str2 ) ) < k :
        return True
    commonLength = 0
    for i in range ( min ( len ( str1 ) , len ( str2 ) ) ) :
        if str1 == str2 :
            commonLength += 1
        else :
            break
    if ( k - len ( str1 ) - len ( str2 ) + 2 * commonLength ) % 2 == 0 :
        return True
    return False
|||

FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES_2

def getOddOccurrence ( ar , ar_size ) :
    i = 0
    res = 0
    for i in range ( ar_size ) :
        res = res ^ ar [ i ]
    return res
|||

SUM_MIDDLE_ROW_COLUMN_MATRIX

def middlesum ( mat , n ) :
    row_sum , col_sum = 0 , 0
    for i in range ( n ) :
        row_sum += mat [ n // 2 ] [ i ]
    print ( "Sum of middle row = " + str ( row_sum ) )
    for i in range ( n ) :
        col_sum += mat [ i ] [ n // 2 ]
    print ( "Sum of middle column = " + str ( col_sum ) )
|||

K_TH_DISTINCT_OR_NON_REPEATING_ELEMENT_IN_AN_ARRAY

def printKDistinct ( arr , n , k ) :
    dist_count = 0
    for i in range ( n ) :
        j = 0
        for j in range ( n ) :
            if i != j and arr [ j ] == arr [ i ] :
                break
        if j == n :
            dist_count += 1
        if dist_count == k :
            return arr [ i ]
    return - 1
|||

MERGING_INTERVALS

def merge_intervals ( arr ) :
    arr.sort ( key = lambda i1 : i2 [ 0 ] - i1 [ 1 ] )
    index = 0
    for i in range ( 1 , len ( arr ) ) :
        if arr [ index ] [ 'end' ] >= arr [ i ] [ 'start' ] :
            arr [ index ] [ 'end' ] = max ( arr [ index ] [ 'end' ] , arr [ i ] [ 'end' ] )
            arr [ index ] [ 'start' ] = min ( arr [ index ] [ 'start' ] , arr [ i ] [ 'start' ] )
        else :
            arr [ index ] = arr [ i ]
            index += 1
    print ( 'The Merged Intervals are: ' )
    for i in range ( 0 , index + 1 ) :
        print ( '[%d,%d]' % ( arr [ i ] [ 'start' ] , arr [ i ] [ 'end' ] ) )
|||

FIND_NUMBER_PERFECT_SQUARES_TWO_GIVEN_NUMBERS_1

def count_squares ( a , b ) :
    return ( math.floor ( math.sqrt ( b ) ) - math.ceil ( math.sqrt ( a ) ) + 1 )
|||

LARGEST_SUBSET_WHOSE_ALL_ELEMENTS_ARE_FIBONACCI_NUMBERS

def find_fib_subset ( x ) :
    max = max ( list ( x ) )
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
        if fib.count ( i ) :
            result.append ( i )
    print ( result )
|||

LEXICOGRAPHICAL_CONCATENATION_SUBSTRINGS_STRING

def lexicographic_sub_concat ( s ) :
    n = len ( s )
    sub_count = n * ( n + 1 ) // 2
    arr = [ ]
    index = 0
    for i in range ( n ) :
        for len in range ( 1 , n - i + 1 ) :
            arr.append ( s [ i : i + len ] )
    arr.sort ( )
    res = ""
    for i in range ( sub_count ) :
        res += arr [ i ]
    return res
|||

COUNT_OPERATIONS_MAKE_STRINGAB_FREE

def abfree ( s ) :
    b_count = 0
    res = 0
    for c in s :
        if c == 'a' :
            res = ( res + b_count )
            b_count = ( b_count * 2 )
        else :
            b_count += 1
    return res
|||

MAXIMUM_HEIGHT_OF_TRIANGULAR_ARRANGEMENT_OF_ARRAY_VALUES_1

def MaximumHeight ( a , n ) :
    return int ( math.floor ( ( - 1 + math.sqrt ( 1 + ( 8 * n ) ) ) ) / 2 )
|||

MAXIMIZE_VOLUME_CUBOID_GIVEN_SUM_SIDES

def maxvolume ( s ) :
    maxvalue = 0
    for i in range ( 1 , s - 2 ) :
        for j in range ( 1 , s - 1 ) :
            k = s - i - j
            maxvalue = max ( maxvalue , i * j * k )
    return maxvalue
|||

PROGRAM_DECIMAL_HEXADECIMAL_CONVERSION

def dec_to_hex ( n ) :
    hexaDeciNum = [ ]
    i = 0
    while n != 0 :
        temp = 0
        temp = n % 16
        if temp < 10 :
            hexaDeciNum.append ( chr ( temp + 48 ) )
            i += 1
        else :
            hexaDeciNum.append ( chr ( temp + 55 ) )
            i += 1
        n = n / 16
    for j in range ( i - 1 , - 1 , - 1 ) :
        print ( hexaDeciNum [ j ] )
|||

SMALLEST_SUBARRAY_WITH_ALL_OCCURRENCES_OF_A_MOST_FREQUENT_ELEMENT

def smallest_subsegment ( a , n ) :
    left = { }
    count = { }
    mx = 0
    mn , strindex = - 1 , - 1
    for i in range ( n ) :
        x = a [ i ]
        if count [ x ] == None :
            left [ x ] = i
            count [ x ] = 1
        else :
            count [ x ] = count [ x ] + 1
        if count [ x ] > mx :
            mx = count [ x ]
            mn = i - left [ x ] + 1
            strindex = left [ x ]
        elif ( count [ x ] == mx ) :
            mn = i - left [ x ] + 1
            strindex = left [ x ]
    for i in range ( strindex , strindex + mn ) :
        print ( a [ i ] , end = ' ' )
|||

FIND_LAST_INDEX_CHARACTER_STRING_1

def find_last_index ( str , x ) :
    for i in range ( len ( str ) - 1 , - 1 , - 1 ) :
        if str [ i ] == x :
            return i
    return - 1
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
                curr = arr [ i - 1 ] + i
                break
        arr [ i ] = curr
        print ( arr [ i ] , ", " )
|||

C_PROGRAM_FIND_SECOND_FREQUENT_CHARACTER

def getSecondMostFreq ( str ) :
    count = [ 0 ] * NO_OF_CHARS
    i = 0
    for c in str :
        ( count [ c ] , count [ c ] ) += 1
    first , second = 0 , 0
    for c in NO_OF_CHARS :
        if count [ c ] > count [ first ] :
            second , first = first , c
        elif count [ c ] > count [ second ] and count [ c ] != count [ first ] :
            second , first = c , first
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
        if curr_width > prev_width and curr_count > prev_count :
            prev_width = curr_width
            prev_count = curr_count
            curr_count = 0
            curr_width = 0
            ans += 1
    return ans
|||

COUNTING_INVERSIONS

def getInvCount ( n ) :
    inv_count = 0
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            if arr [ i ] > arr [ j ] :
                inv_count += 1
    return inv_count
|||

SQUARES_OF_MATRIX_DIAGONAL_ELEMENTS

def diagonalsquare ( mat , row , column ) :
    print ( "Diagonal one : " )
    for i in range ( row ) :
        for j in range ( column ) :
            if i == j :
                print ( mat [ i ] [ j ] * mat [ i ] [ j ] + " " )
    print ( )
    print ( "Diagonal two : " )
    for i in range ( row ) :
        for j in range ( column ) :
            if i + j == column - 1 :
                print ( mat [ i ] [ j ] * mat [ i ] [ j ] + " " )
|||

ROW_WISE_COMMON_ELEMENTS_TWO_DIAGONALS_SQUARE_MATRIX

def countCommon ( mat , n ) :
    res = 0
    for i in range ( n ) :
        if mat [ i ] [ i ] == mat [ i ] [ n - i - 1 ] :
            res += 1
    return res
|||

EULERIAN_NUMBER

def eulerian ( n , m ) :
    if m >= n or n == 0 :
        return 0
    if m == 0 :
        return 1
    return ( n - m ) * eulerian ( n - 1 , m - 1 ) + ( m + 1 ) * eulerian ( n - 1 , m )
|||

EULERS_CRITERION_CHECK_IF_SQUARE_ROOT_UNDER_MODULO_P_EXISTS

def square_root_exists ( n , p ) :
    n = n % p
    for x in range ( 2 , p ) :
        if ( x ** 2 ) % p == n :
            return True
    return False
|||

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX_3

def number_of_paths ( m , n ) :
    path = 1
    for i in range ( n , ( m + n - 1 ) ) :
        path *= i
        path /= ( i - n + 1 )
    return path
|||

MODIFY_ARRAY_TO_MAXIMIZE_SUM_OF_ADJACENT_DIFFERENCES

def maximumDifferenceSum ( arr , N ) :
    dp = [ 0 ] * ( N )
    for i in range ( N ) :
        dp [ i ] = dp [ i ] + 1
    for i in range ( ( N - 1 ) ) :
        dp [ i + 1 ] = max ( dp [ i ] , dp [ i ] + abs ( 1 - arr [ i ] ) )
        dp [ i + 1 ] = max ( dp [ i ] + abs ( arr [ i + 1 ] - 1 ) , dp [ i ] + abs ( arr [ i + 1 ] - arr [ i ] ) )
    return max ( dp [ N - 1 ] , dp [ N - 1 ] + 1 )
|||

STERN_BROCOT_SEQUENCE

def SternSequenceFunc ( BrocotSequence , n ) :
    for i in range ( 1 , n ) :
        considered_element = BrocotSequence [ i ]
        precedent = BrocotSequence [ i - 1 ]
        BrocotSequence.append ( considered_element + precedent )
        BrocotSequence.append ( considered_element )
    for i in range ( 15 ) :
        print ( BrocotSequence [ i ] , end = ' ' )
|||

NUMBER_SUBSEQUENCES_STRING_DIVISIBLE_N

def count_divisible_subseq ( str , n ) :
    len ( str )
    dp = [ 0 ] * len ( str )
    dp [ 0 ] [ ( str [ 0 ] - '0' ) % n ] += 1
    for i in range ( 1 , len ( str ) ) :
        dp [ i ] [ ( str [ i ] - '0' ) % n ] += 1
        for j in range ( n ) :
            dp [ i ] [ j ] += dp [ i - 1 ] [ j ]
            dp [ i ] [ ( j * 10 + ( str [ i ] - '0' ) ) % n ] += dp [ i - 1 ] [ j ]
    return dp [ len ( str ) - 1 ] [ 0 ]
|||

HOW_TO_BEGIN_WITH_COMPETITIVE_PROGRAMMING

def search ( arr , n , x ) :
    for i in range ( n ) :
        if arr [ i ] == x :
            return i
    return - 1
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
        if hm.has_key ( sum - arr [ i ] ) :
            twice_count += hm [ sum - arr [ i ] ]
        if sum - arr [ i ] == arr [ i ] :
            twice_count -= 1
    return twice_count / 2
|||

FIND_THE_MINIMUM_DISTANCE_BETWEEN_TWO_NUMBERS

def minDist ( arr , n , x , y ) :
    i , j = 0 , 0
    min_dist = sys.maxint
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if ( x == arr [ i ] and y == arr [ j ] or y == arr [ i ] and x == arr [ j ] ) and min_dist > abs ( i - j ) :
                min_dist = abs ( i - j )
    return min_dist
|||

FIND_REPETITIVE_ELEMENT_1_N_1_2

def find_repeated ( arr , n ) :
    res = 0
    for i in range ( n - 1 ) :
        res = res ^ ( i + 1 ) ^ arr [ i ]
    res = res ^ arr [ n - 1 ]
    return res
|||

SHORTEST_PATH_EXACTLY_K_EDGES_DIRECTED_WEIGHTED_GRAPH_1

def shortestPath ( graph , u , v , k ) :
    sp = [ [ INF ] * V [ V ] [ k + 1 ] for e in range ( 0 , k + 1 ) ]
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
|||

LONGEST_SUBARRAY_NOT_K_DISTINCT_ELEMENTS

def longest ( a , n , k ) :
    freq = [ 0 ] * 7
    start , end , now , l = 0 , 0 , 0 , 0
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
            end = i
            start = l
    for i in range ( start , end + 1 ) :
        print ( a [ i ] , end )
|||

MAXIMUM_XOR_VALUE_MATRIX

def maxXOR ( mat , N ) :
    r_xor , c_xor = 0 , 0
    max_xor = 0
    for i in range ( N ) :
        r_xor = 0
        c_xor = 0
        for j in range ( N ) :
            r_xor = r_xor ^ mat [ i ] [ j ]
            c_xor = c_xor ^ mat [ j ] [ i ]
        if max_xor < max ( r_xor , c_xor ) :
            max_xor = max ( r_xor , c_xor )
    return max_xor
|||

LENGTH_LONGEST_SUB_STRING_CAN_MAKE_REMOVED

def longest_null ( str ) :
    arr = [ ( '@' , - 1 ) ]
    maxlen = 0
    for i in range ( len ( str ) ) :
        arr.append ( ( str [ i ] , i ) )
        while len ( arr ) >= 3 and arr [ - 3 ] [ 0 ] == '1' and arr [ - 2 ] [ 0 ] == '0' and arr [ - 1 ] [ 0 ] == '0' :
            arr.pop ( - 3 )
            arr.pop ( - 2 )
            arr.pop ( - 1 )
        tmp = arr [ - 1 ] [ 1 ]
        maxlen = max ( maxlen , i - tmp )
    return maxlen
|||

LONGEST_ALTERNATING_SUB_ARRAY_STARTING_EVERY_INDEX_BINARY_ARRAY

def alternate_subarray ( arr , n ) :
    len = [ 1 ] * n
    for i in range ( n - 2 , - 1 , - 1 ) :
        if arr [ i ] ^ arr [ i + 1 ] == True :
            len [ i ] = len [ i + 1 ] + 1
        else :
            len [ i ] = 1
    for i in range ( n ) :
        print ( len [ i ] , end = ' ' )
|||

WILDCARD_CHARACTER_MATCHING

def match ( first , second ) :
    if len ( first ) == 0 and len ( second ) == 0 :
        return True
    if len ( first ) > 1 and first [ 0 ] == '*' and len ( second ) == 0 :
        return False
    if ( len ( first ) > 1 and first [ 0 ] == '?' ) or ( len ( first ) != 0 and second != '?' and first [ 0 ] == second [ 0 ] ) :
        return match ( first [ 1 : ] , second [ 1 : ] )
    if len ( first ) > 0 and first [ 0 ] == '*' :
        return match ( first [ 1 : ] , second ) or match ( first , second [ 1 : ] )
    return False
|||

FIND_FACTORIAL_NUMBERS_LESS_EQUAL_N

def print_factorial ( n ) :
    fact = 1
    x = 2
    while fact <= n :
        print ( fact , end = ' ' )
        fact = fact * x
        x += 1
|||

FRIENDS_PAIRING_PROBLEM_2

def countFriendsPairings ( n ) :
    a , b , c = 1 , 2 , 0
    if n <= 2 :
        return n
    for i in range ( 3 , n + 1 ) :
        c = b + ( i - 1 ) * a
        a , b , c = b , c , c
    return c
|||

FIND_THE_LARGEST_RECTANGLE_OF_1S_WITH_SWAPPING_OF_COLUMNS_ALLOWED

def maxArea ( mat ) :
    hist = [ 0 ] * ( R + 1 )
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
                    col_no += 1
    curr_area , max_area = 0 , 0
    for i in range ( R ) :
        for j in range ( C ) :
            curr_area = ( j + 1 ) * hist [ i ] [ j ]
            if curr_area > max_area :
                max_area = curr_area
    return max_area
|||

SUM_SEQUENCE_2_22_222

def sum_of_series ( n ) :
    return 0.0246 * ( pow ( 10 , n ) - 1 - ( 9 * n ) )
|||

PROGRAM_FIRST_FIT_ALGORITHM_MEMORY_MANAGEMENT

def first_fit ( block_size , m , process_size , n ) :
    allocation = [ - 1 ] * n
    for i in range ( n ) :
        allocation [ i ] = - 1
    for i in range ( n ) :
        for j in range ( m ) :
            if block_size [ j ] >= process_size [ i ] :
                allocation [ i ] = j
                block_size [ j ] -= process_size [ i ]
                break
    print ( "\nProcess No.\tProcess Size\tBlock no." )
    for i in range ( n ) :
        print ( " " * ( i + 1 ) + "\t\t" + str ( process_size [ i ] ) + "\t\t" )
        if allocation [ i ] != - 1 :
            print ( allocation [ i ] + 1 )
        else :
            print ( "Not Allocated" )
        print ( )
|||

CHECK_IF_A_NUMBER_IS_POWER_OF_ANOTHER_NUMBER

def isPower ( x , y ) :
    if x == 1 :
        return ( y == 1 )
    pow = 1
    while pow < y :
        pow = pow * x
    return ( pow == y )
|||

DIVIDE_LARGE_NUMBER_REPRESENTED_STRING

def longDivision ( number , divisor ) :
    ans = ""
    idx = 0
    num = number.split ( )
    temp = num [ idx ] - '0'
    while temp < divisor :
        temp = temp * 10 + ( num [ ++ idx ] - '0' )
    idx += 1
    while len ( num ) > idx :
        ans += ( temp / divisor )
        temp = ( temp % divisor ) * 10 + num [ idx ++ ] - '0'
    if len ( ans ) == 0 :
        return "0"
    return ans
|||

FIND_ROW_NUMBER_BINARY_MATRIX_MAXIMUM_NUMBER_1S

def findMax ( arr ) :
    row , i , j = 0 , N - 1 , N - 1
    for i , j in enumerate ( arr ) :
        while j >= 0 and arr [ i ] [ j ] == 1 :
            row = i
            j -= 1
    print ( "Row number = " + str ( row + 1 ) )
    print ( ", MaxCount = " + str ( N - 1 - j ) )
|||

MINIMUM_ROTATIONS_REQUIRED_GET_STRING

def find_rotations ( str ) :
    tmp = str + str
    n = len ( str )
    for i in range ( 1 , n + 1 ) :
        substring = tmp [ i : i + len ( str ) ]
        if str == substring :
            return i
    return n
|||

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX

def number_of_paths ( m , n ) :
    if m == 1 or n == 1 :
        return 1
    return number_of_paths ( m - 1 , n ) + number_of_paths ( m , n - 1 )
|||

N_TH_NUMBER_WHOSE_SUM_OF_DIGITS_IS_TEN_1

def find_nth ( n ) :
    count = 0
    for curr in range ( 19 , 0 , 9 ) :
        sum = 0
        for x in range ( curr , 0 , 10 ) :
            sum = sum + x % 10
        if sum == 10 :
            count += 1
        if count == n :
            return curr
|||

SUM_NODES_K_TH_LEVEL_TREE_REPRESENTED_STRING_1

def sum_at_kth_level ( tree , k , level ) :
    if tree [ i ] == '(' :
        if tree [ i ] == ')' :
            return 0
        sum = 0
        if level == k :
            sum = tree [ i ] - '0'
        i += 1
        leftsum = sum_at_kth_level ( tree , k , level + 1 )
        i += 1
        rightsum = sum_at_kth_level ( tree , k , level + 1 )
        i += 1
        return sum + leftsum + rightsum
    return int ( tree [ i ] )
|||

COUNT_OFDIFFERENT_WAYS_EXPRESS_N_SUM_1_3_4

def countWays ( n ) :
    DP = [ 0 ] * ( n + 1 )
    for i in range ( 4 , n + 1 ) :
        DP [ i ] = DP [ i - 1 ] + DP [ i - 3 ] + DP [ i - 4 ]
    return DP [ n ]
|||

MAXIMUM_EQULIBRIUM_SUM_ARRAY

def find_max_sum ( arr , n ) :
    res = int ( '' )
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
|||

STEINS_ALGORITHM_FOR_FINDING_GCD_1

def gcd ( a , b ) :
    if a == b : return a
    if a == 0 : return b
    if b == 0 : return a
    if ( ~ a & 1 ) == 1 :
        if ( b & 1 ) == 1 : return gcd ( a >> 1 , b )
        else : return gcd ( a >> 1 , b >> 1 ) << 1
    if ( ~ b & 1 ) == 1 : return gcd ( a , b >> 1 )
    if a > b : return gcd ( ( a - b ) >> 1 , b )
    return gcd ( ( b - a ) >> 1 , a )
|||

PROGRAM_TO_FIND_THE_VOLUME_OF_A_TRIANGULAR_PRISM

def find_volume ( l , b , h ) :
    volume = ( l * b * h ) / 2
    return volume
|||

FIND_RECTANGLE_BINARY_MATRIX_CORNERS_1

def isRectangle ( m ) :
    rows = m.shape [ 0 ]
    if rows == 0 : return False
    columns = m.shape [ 1 ]
    for y1 in range ( rows ) :
        for x1 in range ( columns ) :
            if m [ y1 , x1 ] == 1 :
                for y2 in range ( y1 + 1 , rows ) :
                    for x2 in range ( x1 + 1 , columns ) :
                        if m [ y1 , x2 ] == 1 and m [ y2 , x1 ] == 1 and m [ y2 , x2 ] == 1 :
                            return True
    return False
|||

CHECK_IF_STRING_REMAINS_PALINDROME_AFTER_REMOVING_GIVEN_NUMBER_OF_CHARACTERS

def is_possible ( str , n ) :
    len = len ( str )
    if len >= n :
        return True
    return False
|||

CHECK_STAR_GRAPH

def checkStar ( mat ) :
    vertexD1 , vertexDn_1 = 0 , 0
    if size == 1 :
        return ( mat [ 0 ] [ 0 ] , mat [ 0 ] [ 1 ] , mat [ 1 ] [ 0 ] , mat [ 1 ] [ 1 ] , mat [ 0 ] [ 2 ] , mat [ 1 ] [ 2 ] , mat [ 0 ] [ 3 ] , mat [ 1 ] [ 3 ] , mat [ 0 ] [ 4 ] , mat [ 1 ] [ 4 ] , mat [ 1 ] [ 4 ] , mat [ 0 ] [ 5 ] , mat [ 1 ] [ 5 ] , mat [ 0 ] [ 6 ] , mat [ 1 ] [ 6 ] , mat [ 0 ] [ 7 ] , mat [ 1 ] [ 7 ] , mat [ 0 ] [ 8 ] , mat [ 1 ] [ 8 ] , mat [ 0 ] [ 9 ] , mat [ 1 ] [ 9 ] , mat [ 0 ] [ 10 ] , mat [ 1 ] [ 10 ] , mat [ 0 ] [ 11 ] , mat [ 1 ] [ 11 ] , mat [ 0 ] [ 12 ] , mat [ 1 ] [ 12 ] , mat [ 0 ] [ 13 ] , mat [ 1 ] [ 13 ] , mat [ 0 ] [ 14 ] , mat [ 1 ] [ 14 ] , mat [ 0 ] [ 15 ] , mat [ 1 ] [ 15 ] , mat [ 0 ] [ 16 ] , mat [ 1 ] [ 16 ] , mat [ 0 ] [ 17 ] , mat [ 1 ] [ 17 ] , mat [ 0 ] [ 18 ] , mat [ 1 ] [ 18 ] , mat [ 0 ] [ 19 ] , mat [ 1 ] [ 19 ] , mat [ 0 ] [ 20 ] , mat [ 1 ] [ 20 ] , mat [ 0 ] [ 21 ] , mat [ 1 ] [ 21 ] , mat [ 0 ] [ 22 ] , mat [ 1 ] [ 22 ] , mat [ 0 ] [ 23 ] , mat [ 1 ] [ 23 ] , mat [ 0 ] [ 24 ] , mat [ 1 ] [ 24 ] , mat [ 0 ] [ 25 ] , mat [ 1 ] [ 25 ] , mat [ 0 ] [ 26 ] , mat [ 1 ] [ 26 ] , mat [ 0 ] [ 27 ] , mat [ 1 ] [ 27 ] , mat [ 0 ] [ 28 ] , mat [ 1 ] [ 28 ] , mat [ 0 ] [ 29 ] ,
|||

ROOTS_OF_UNITY

def print_roots ( n ) :
    theta = 3.14 * 2 / n
    for k in range ( n ) :
        real = cos ( k * theta )
        img = sin ( k * theta )
        print ( real )
        if img >= 0 :
            print ( " + i " )
        else :
            print ( " - i " )
        print ( abs ( img ) )
|||

FIND_LARGEST_D_IN_ARRAY_SUCH_THAT_A_B_C_D

def find_largestd ( S , n ) :
    found = False
    S.sort ( )
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
                        found = True
                        return S [ i ]
    if found == False :
        return int ( S [ 0 ] )
|||

GIVEN_NUMBER_STRING_FIND_NUMBER_CONTIGUOUS_SUBSEQUENCES_RECURSIVELY_ADD_9_SET_2

def count9s ( number ) :
    n = len ( number )
    d = [ 1 ] * 9
    result = 0
    mod_sum , continuous_zero = 0 , 0
    for i in range ( n ) :
        if ( number [ i ] - '0' ) == 0 :
            continuous_zero += 1
        else :
            continuous_zero = 0
        mod_sum += ( number [ i ] - '0' )
        mod_sum %= 9
        result += d [ mod_sum ]
        d [ mod_sum ] += 1
        result -= continuous_zero
    return result
|||

LEXICOGRAPHICAL_MAXIMUM_SUBSTRING_STRING

def LexicographicalMaxString ( * args ) :
    mx = ""
    for arg in args :
        if mx <= arg : mx = arg
    return mx
|||

CHECK_TWO_GIVEN_SETS_DISJOINT_1

def aredisjoint ( set1 , set2 ) :
    i , j = 0 , 0
    set1.sort ( )
    set2.sort ( )
    while i < len ( set1 ) and j < len ( set2 ) :
        if set1 [ i ] < set2 [ j ] :
            i += 1
        elif set1 [ i ] > set2 [ j ] :
            j += 1
        else :
            return False
    return True
|||

EQUILIBRIUM_INDEX_OF_AN_ARRAY_1

def equilibrium ( arr , n ) :
    sum = 0
    leftsum = 0
    for i in range ( n ) :
        sum += arr [ i ]
    for i in range ( n ) :
        sum -= arr [ i ]
        if leftsum == sum :
            return i
        leftsum += arr [ i ]
    return - 1
|||

AREA_CIRCUMSCRIBED_CIRCLE_SQUARE

def areacircumscribed ( a ) :
    PI = 3.14159265f
    return ( a * a * ( PI / 2 ) )
|||

LONGEST_REPEATING_AND_NON_OVERLAPPING_SUBSTRING

def longestRepeatedSubstring ( str ) :
    n = len ( str )
    LCSRe = [ [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n ]
|||

HOW_TO_AVOID_OVERFLOW_IN_MODULAR_MULTIPLICATION

def mulmod ( a , b , mod ) :
    res = 0
    a = a % mod
    while b :
        if b % 2 == 1 :
            res = ( res + a ) % mod
        a = ( a * 2 ) % mod
        b //= 2
    return res % mod
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
            if hset.intersection ( x / arr [ i ] ) :
                return True
            hset.add ( arr [ i ] )
    return False
|||

SUM_K_TH_GROUP_ODD_POSITIVE_NUMBERS

def kthgroupsum ( k ) :
    cur = ( k * ( k - 1 ) ) + 1
    sum = 0
    while k :
        sum += cur
        cur += 2
    return sum
|||

FIND_ELEMENTS_ARRAY_LEAST_TWO_GREATER_ELEMENTS_1

def find_elements ( arr , n ) :
    arr.sort ( )
    for i in range ( n - 2 ) :
        print ( arr [ i ] , end = ' ' )
|||

MINIMUM_STEPS_TO_DELETE_A_STRING_AFTER_REPEATED_DELETION_OF_PALINDROME_SUBSTRINGS

def min_step_to_delete_string ( str ) :
    N = len ( str )
    dp = [ [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0 ] * N + [ 0
|||

CALCULATE_AREA_TETRAHEDRON

def vol_tetra ( side ) :
    volume = ( pow ( side , 3 ) / ( 6 * sqrt ( 2 ) ) )
    return volume
|||

SIEVE_OF_ATKIN

def SieveOfAtkin ( limit ) :
    if limit > 2 :
        print ( 2 , end = ' ' )
    if limit > 3 :
        print ( 3 , end = ' ' )
    sieve = [ False for i in range ( limit ) ]
    for x in range ( 1 , limit * 2 ) :
        for y in range ( 1 , limit * 2 ) :
            n = ( 4 * x * x ) + ( y * y )
            if n <= limit and ( n % 12 == 1 or n % 12 == 5 ) :
                sieve [ n ] ^= True
            n = ( 3 * x * x ) + ( y * y )
            if n <= limit and n % 12 == 7 :
                sieve [ n ] ^= True
            n = ( 3 * x * x ) - ( y * y )
            if x > y and n <= limit and n % 12 == 11 :
                sieve [ n ] ^= True
    for r in range ( 5 , limit * 2 ) :
        if sieve [ r ] :
            for i in range ( r * r , limit , r * r ) :
                sieve [ i ] = False
    for a in range ( 5 , limit ) :
        if sieve [ a ] :
            print ( a , end = ' ' )
    return 0
|||

LENGTH_OF_THE_LONGEST_ARITHMATIC_PROGRESSION_IN_A_SORTED_ARRAY

def lenghtOfLongestAP ( set , n ) :
    if n <= 2 :
        return n
    L = [ [ ] for i in range ( n ) ]
    llap = 2
    for i in range ( n ) :
        L [ i ] [ n - 1 ] = 2
    for j in range ( n - 2 , - 1 , - 1 ) :
        i , k = j - 1 , j + 1
        while i >= 0 and k <= n - 1 :
            if set [ i ] + set [ k ] < 2 * set [ j ] :
                k += 1
            elif set [ i ] + set [ k ] > 2 * set [ j ] :
                L [ i ] [ j ] = 2
                i -= 1
            else :
                L [ i ] [ j ] = L [ j ] [ k ] + 1
                llap = max ( llap , L [ i ] [ j ] )
                i -= 1
                k += 1
        while i >= 0 :
            L [ i ] [ j ] = 2
            i -= 1
    return llap
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
        sum += ( num [ i ] - '0' )
        if sum >= previous_sum :
            res += count_groups ( i + 1 , sum , length , num )
    dp [ position ] [ previous_sum ] = res
    return res
|||

LONGEST_SPAN_SUM_TWO_BINARY_ARRAYS_1

def longest_common_sum ( n ) :
    max_len = 0
    pre_sum1 , pre_sum2 = 0 , 0
    diff = [ - 1 ] * ( 2 * n + 1 )
    for i in range ( len ( diff ) ) :
        pre_sum1 += arr1 [ i ]
        pre_sum2 += arr2 [ i ]
        curr_diff = pre_sum1 - pre_sum2
        diff_index = n + curr_diff
        if curr_diff == 0 :
            max_len = i + 1
        elif diff [ diff_index ] == - 1 :
            diff [ diff_index ] = i
        else :
            len = i - diff [ diff_index ]
            if len > max_len :
                max_len = len
    return max_len
|||

PROGRAM_TO_PRINT_FIRST_N_FIBONACCI_NUMBERS

def print_fibonacci_numbers ( n ) :
    f1 , f2 , i = 0 , 1 , i
    if n < 1 :
        return
    for i in range ( 1 , n + 1 ) :
        print ( f2 , end = ' ' )
        next = f1 + f2
        f1 , f2 = f2 , next
|||

LARGEST_SUM_CONTIGUOUS_SUBARRAY_3

def max_subarray_sum ( a , size ) :
    max_so_far , max_ending_here , start , end , s = int ( a [ : size ] ) , 0 , 0 , 0 , 0
    for i in range ( size ) :
        max_ending_here += a [ i ]
        if max_so_far < max_ending_here :
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0 :
            max_ending_here = 0
            s = i + 1
    print ( "Maximum contiguous sum is %d" % max_so_far )
    print ( "Starting index %d" % start )
    print ( "Ending index %d" % end )
|||

FIND_EQUAL_POINT_STRING_BRACKETS

def findIndex ( str ) :
    len ( str )
    open = [ ]
    close = [ ]
    index = - 1
    open.append ( 0 )
    close.append ( 0 )
    if str [ 0 ] == '(' :
        open.append ( 1 )
    if str [ len - 1 ] == ')' :
        close.append ( 1 )
    for i in range ( 1 , len ( str ) ) :
        if str [ i ] == '(' :
            open.append ( open [ i ] + 1 )
        else :
            open.append ( open [ i ] )
    for i in range ( len - 2 , - 1 , - 1 ) :
        if str [ i ] == ')' :
            close.append ( close [ i + 1 ] + 1 )
        else :
            close.append ( close [ i + 1 ] )
    if open [ len ] == 0 :
        return len
    if close [ 0 ] == 0 :
        return 0
    for i in range ( 0 , len ( open ) ) :
        if open [ i ] == close [ i ] :
            index = i
    return index
|||

COUNT_NUMBER_OF_WAYS_TO_PARTITION_A_SET_INTO_K_SUBSETS_1

def count_p ( n , k ) :
    dp = [ [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n + [ k + 1 ] * k + [ 0 ] * n +
|||

LONGEST_INCREASING_SUBSEQUENCE

def lis ( arr , n ) :
    global max_ref
    _lis ( arr , n )
    return max_ref
|||

FIND_REPEATED_CHARACTER_PRESENT_FIRST_STRING

def findRepeatFirstN2 ( s ) :
    p , i , j = - 1 , 0 , 0
    for i in range ( len ( s ) ) :
        for j in range ( i + 1 , len ( s ) ) :
            if s [ i ] == s [ j ] :
                p = i
                break
        if p != - 1 :
            break
    return p
|||

K_TH_SMALLEST_ELEMENT_REMOVING_INTEGERS_NATURAL_NUMBERS

def ksmallest ( arr , n , k ) :
    b = [ 1 for i in range ( n ) ]
    for i in range ( MAX ) :
        b [ arr [ i ] ] = 1
    for j in range ( 1 , MAX ) :
        if b [ j ] != 1 :
            k -= 1
        if k != 1 :
            return j
    return int ( '-1' )
|||

CHECK_IF_STACK_ELEMENTS_ARE_PAIRWISE_CONSECUTIVE

def pairWiseConsecutive ( s ) :
    aux = [ ]
    while not s.empty ( ) :
        aux.append ( s.pop ( ) )
        s.pop ( )
    result = True
    while aux.size ( ) > 1 :
        x = aux.pop ( )
        aux.pop ( )
        y = aux.pop ( )
        aux.pop ( )
        if abs ( x - y ) != 1 :
            result = False
        s.append ( x )
        s.append ( y )
    if len ( aux ) == 1 :
        s.append ( aux.pop ( ) )
    return result
|||

BINARY_SEARCH_1

def binary_search ( arr , x ) :
    l , r = 0 , len ( arr ) - 1
    while l <= r :
        m = l + ( r - l ) // 2
        if arr [ m ] == x :
            return m
        if arr [ m ] < x :
            l = m + 1
        else :
            r = m - 1
    return - 1
|||

COUNT_DISTINCT_OCCURRENCES_AS_A_SUBSEQUENCE

def findSubsequenceCount ( S , T ) :
    m = len ( T )
    n = len ( S )
    if m > n :
        return 0
    mat = [ [ 0 ] * m + [ n + 1 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m
|||

SWAP_TWO_NUMBERS_WITHOUT_USING_TEMPORARY_VARIABLE

def swap ( xp , yp ) :
    xp [ 0 ] = xp [ 0 ] ^ yp [ 0 ]
    yp [ 0 ] = xp [ 0 ] ^ yp [ 0 ]
    xp [ 0 ] = xp [ 0 ] ^ yp [ 0 ]
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
|||

LARGEST_SUBARRAY_WITH_EQUAL_NUMBER_OF_0S_AND_1S_1

def max_len ( arr , n ) :
    hM = { }
    sum = 0
    max_len = 0
    ending_index = - 1
    start_index = 0
    for i in range ( n ) :
        arr [ i ] = ( arr [ i ] == 0 )
    for i in range ( n ) :
        sum += arr [ i ]
        if sum == 0 :
            max_len = i + 1
            ending_index = i
        if hM.has_key ( sum + n ) :
            if max_len < i - hM [ sum + n ] :
                max_len = i - hM [ sum + n ]
                ending_index = i
        else :
            hM [ sum + n ] = i
    for i in range ( n ) :
        arr [ i ] = ( arr [ i ] == - 1 )
    end = ending_index - max_len + 1
    print ( end , ending_index )
    return max_len
|||

MAXIMUM_DIFFERENCE_ZEROS_ONES_BINARY_STRING_SET_2_TIME

def find_length ( str , n ) :
    current_sum = 0
    max_sum = 0
    for i in range ( n ) :
        current_sum += ( str [ i ] == '0' )
        if current_sum < 0 :
            current_sum = 0
        max_sum = max ( current_sum , max_sum )
    return max_sum if max_sum > 0 else - 1
|||

MAXIMUM_CONSECUTIVE_NUMBERS_PRESENT_ARRAY

def findLongestConseqSubseq ( arr , n ) :
    S = set ( )
    for i in range ( n ) :
        S.add ( arr [ i ] )
    ans = 0
    for i in range ( n ) :
        if S.intersection ( arr [ i ] ) :
            j = arr [ i ]
            while S.intersection ( j ) :
                j += 1
            ans = max ( ans , j - arr [ i ] )
    return ans
|||

LEXICOGRAPHICALLY_NEXT_STRING

def next_word ( str ) :
    if str == "" :
        return "a"
    i = len ( str ) - 1
    while str [ i ] == "z" and i >= 0 :
        i -= 1
    if i == - 1 :
        str = str + 'a'
    else :
        str = str [ : i ] + chr ( ord ( str [ i ] ) + 1 ) + str [ i + 1 : ]
    return str
|||

SCHEDULE_JOBS_SERVER_GETS_EQUAL_LOAD

def solve ( a , b , n ) :
    i = 0
    s = 0
    for i in range ( n ) :
        s += ( a [ i ] + b [ i ] )
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
        if a [ i ] + b [ i ] == x :
            a [ i ] += b [ i ]
            b [ i ] = 0
            continue
        if i + 1 < n and a [ i ] + b [ i + 1 ] == x :
            a [ i ] += b [ i + 1 ]
            b [ i + 1 ] = 0
            continue
        return - 1
    for i in range ( n ) :
        if b [ i ] != 0 :
            return - 1
    return x
|||

FORM_MINIMUM_NUMBER_FROM_GIVEN_SEQUENCE_1

def getMinNumberForPattern ( seq ) :
    n = len ( seq )
    if n >= 9 :
        return "-1"
    result = [ ]
    count = 1
    for i in range ( 0 , n ) :
        if i == n or seq [ i ] == 'I' :
            for j in range ( i - 1 , - 1 , - 1 ) :
                result.append ( chr ( int ( '0' + count , 16 ) ) )
                if j >= 0 and seq [ j ] == 'I' :
                    break
    return ''.join ( result )
|||

SHUFFLE_2N_INTEGERS_FORMAT_A1_B1_A2_B2_A3_B3_BN_WITHOUT_USING_EXTRA_SPACE

def shuffleArray ( a , n ) :
    for i , q , k in enumerate ( a ) :
        for j in range ( k , i + q , - 1 ) :
            temp = a [ j - 1 ]
            a [ j - 1 ] = a [ j ]
            a [ j ] = temp
|||

FIND_REPETITIVE_ELEMENT_1_N_1_1

def find_repeated ( arr , n ) :
    s = set ( )
    for i in range ( n ) :
        if s.issubset ( arr [ i ] ) :
            return arr [ i ]
        s.add ( arr [ i ] )
    return - 1
|||

C_PROGRAM_SUBTRACTION_MATICES

def multiply ( A , B , C ) :
    i , j = 0 , 0
    for i in range ( N ) :
        for j in range ( N ) :
            C [ i ] [ j ] = A [ i ] [ j ] - B [ i ] [ j ]
|||

FIRST_NEGATIVE_INTEGER_EVERY_WINDOW_SIZE_K

def printFirstNegativeInteger ( arr , n , k ) :
    flag = False
    for i in range ( ( n - k + 1 ) ) :
        flag = False
        for j in range ( k ) :
            if arr [ i + j ] < 0 :
                print ( ( arr [ i + j ] , arr [ i + j ] ) )
                flag = True
                break
        if not flag :
            print ( "0" , end = ' ' )
|||

NUMBER_FULL_BINARY_TREES_NODE_PRODUCT_CHILDREN

def numoffbt ( arr , n ) :
    maxvalue = - 2147483647
    minvalue = 2147483647
    for i in range ( n ) :
        maxvalue = max ( maxvalue , arr [ i ] )
        minvalue = min ( minvalue , arr [ i ] )
    mark = [ 0 ] * ( maxvalue + 2 )
    value = [ 0 ] * ( maxvalue + 2 )
    del mark [ 0 ]
    del value [ 0 ]
    for i in range ( n ) :
        mark [ arr [ i ] ] = 1
        value [ arr [ i ] ] = 1
    ans = 0
    for i in range ( minvalue , maxvalue + 1 ) :
        if mark [ i ] != 0 :
            for j in range ( i + i , maxvalue + 1 , i ) :
                if mark [ j ] == 0 :
                    continue
                value [ j ] = value [ j ] + ( value [ i ] * value [ j / i ] )
                if i != j / i :
                    value [ j ] = value [ j ] + ( value [ i ] * value [ j / i ] )
        ans += value [ i ]
    return ans
|||

TRIANGULAR_MATCHSTICK_NUMBER

def number_of_ticks ( x ) :
    return ( 3 * x * ( x + 1 ) ) / 2
|||

K_MAXIMUM_SUM_COMBINATIONS_TWO_ARRAYS

def KMaxCombinations ( A , B , N , K ) :
    pq = PriorityQueue ( sorted ( A ) )
    for i in range ( N ) :
        for j in range ( N ) :
            pq.add ( A [ i ] + B [ j ] )
    count = 0
    while count < K :
        print ( pq.get ( ) )
        pq.pop ( )
        count += 1
|||

CONSTRUCT_ARRAY_PAIR_SUM_ARRAY

def construct_arr ( arr , pair , n ) :
    arr [ 0 ] = ( pair [ 0 ] + pair [ 1 ] - pair [ n - 1 ] ) / 2
    for i in range ( 1 , n ) :
        arr [ i ] = pair [ i - 1 ] - arr [ 0 ]
|||

CHECK_HALF_STRING_CHARACTER_FREQUENCY_CHARACTER

def check_correct_or_not ( s ) :
    count1 = [ ]
    count2 = [ ]
    n = len ( s )
    if n == 1 :
        return True
    for i , c in enumerate ( s ) :
        count1.append ( ord ( c ) - ord ( 'a' ) )
        count2.append ( ord ( c ) - ord ( 'a' ) )
    for i in range ( MAX_CHAR ) :
        if count1 [ i ] != count2 [ i ] :
            return False
    return True
|||

MINIMIZE_THE_MAXIMUM_DIFFERENCE_BETWEEN_THE_HEIGHTS

def getMinDiff ( arr , n , k ) :
    if n == 1 :
        return 0
    arr.sort ( )
    ans = arr [ n - 1 ] - arr [ 0 ]
    small = arr [ 0 ] + k
    big = arr [ n - 1 ] - k
    temp = 0
    if small > big :
        temp = small
        small = big
        big = temp
    for i in range ( 1 , n - 1 ) :
        subtract = arr [ i ] - k
        add = arr [ i ] + k
        if subtract >= small or add <= big :
            continue
        if big - subtract <= add - small :
            small = subtract
        else :
            big = add
    return min ( ans , big - small )
|||

MINIMUM_POSSIBLE_VALUE_AI_AJ_K_GIVEN_ARRAY_K

def pairs ( arr , n , k ) :
    smallest = int ( '-inf' )
    count = 0
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if abs ( arr [ i ] + arr [ j ] - k ) < smallest :
                smallest = abs ( arr [ i ] + arr [ j ] - k )
                count = 1
            elif abs ( arr [ i ] + arr [ j ] - k ) == smallest :
                count += 1
    print ( 'Minimal Value = %d' % smallest )
    print ( 'Total Pairs = %d' % count )
|||

SIZE_SUBARRAY_MAXIMUM_SUM

def max_subarray_sum ( a , size ) :
    max_so_far , max_ending_here , start , end , s = int ( a [ : size ] ) , 0 , 0 , 0 , 0
    for i in range ( size ) :
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

def get_min_squares ( n ) :
    if n <= 3 :
        return n
    dp = [ 0 ] * ( n + 1 )
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
|||

POSITION_OF_RIGHTMOST_SET_BIT_2

def Right_most_setbit ( num ) :
    pos = 1
    for i in range ( INT_SIZE ) :
        if ( num & ( 1 << i ) ) == 0 :
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
    right_one , next_higher_one_bit , right_ones_pattern , next = x
    if next_higher_one_bit :
        right_one = x & - x
        next_higher_one_bit = x + right_one
        right_ones_pattern = x ^ next_higher_one_bit
        right_ones_pattern = ( right_ones_pattern ) // right_one
        right_ones_pattern >>= 2
        next = next_higher_one_bit | right_ones_pattern
    return next
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
                next_missing += 1
            a [ i ] = next_missing
            count [ next_missing ] = 1
|||

MAXIMUM_AREA_QUADRILATERAL

def max_area ( a , b , c , d ) :
    semiperimeter = ( a + b + c + d ) / 2
    return math.sqrt ( ( semiperimeter - a ) ** 2 + ( semiperimeter - b ) ** 2 + ( semiperimeter - c ) ** 2 + ( semiperimeter - d ) ** 2 )
|||

REPLACE_OCCURRENCES_STRING_AB_C_WITHOUT_USING_EXTRA_SPACE_1

def translate ( s ) :
    """translate(s) -> string

 Return a copy of the string s with all occurrences of substring
 s[i:j], where i <= len(s) and j >= len(s).

 """
    return s [ : 0 ].translate ( string.maketrans ( s , '' ) )
    # Capitalize a string, e.g."aBc dEf" -> "Abc def".
    # This means that "Abc def" -> "Abc Def".
    # If there is no '%' prefix, then split on a newline.
    # Otherwise, we look for "%n" in s.replace("\n", "\n").
|||

FIND_POWER_POWER_MOD_PRIME

def Calculate ( A , B , C , M ) :
    res , ans = power ( B , C , M - 1 )
    ans = power ( A , res , M )
    return ans
|||

CHECK_EXIST_TWO_ELEMENTS_ARRAY_WHOSE_SUM_EQUAL_SUM_REST_ARRAY

def check_pair ( arr , n ) :
    sum = 0
    for i in range ( n ) :
        sum += arr [ i ]
    if sum % 2 != 0 :
        return False
    sum = sum / 2
    s = set ( )
    for i in range ( n ) :
        val = sum - arr [ i ]
        if s.issuperset ( val ) and val in ( s.union ( val ) ) :
            print ( "Pair elements are %d and %d" % ( arr [ i ] , val ) )
            return True
        s.add ( arr [ i ] )
    return False
|||

PROGRAM_FOR_SURFACE_AREA_OF_OCTAHEDRON

def surface_area_octahedron ( side ) :
    return ( 2 * ( np.sqrt ( 3 ) ) * ( side ** 2 ) )
|||

FIND_A_SPECIFIC_PAIR_IN_MATRIX

def findMaxValue ( N , mat ) :
    maxValue = int ( "" )
    for a in range ( N - 1 ) :
        for b in range ( N - 1 ) :
            for d in range ( a + 1 , N ) :
                for e in range ( b + 1 , N ) :
                    if maxValue < ( mat [ d ] [ e ] - mat [ a ] [ b ] ) :
                        maxValue = mat [ d ] [ e ] - mat [ a ] [ b ]
    return maxValue
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
|||

FIND_TRIPLETS_ARRAY_WHOSE_SUM_EQUAL_ZERO_1

def find_triplets ( arr , n ) :
    found = False
    for i in range ( n - 1 ) :
        s = set ( )
        for j in range ( i + 1 , n ) :
            x = - ( arr [ i ] + arr [ j ] )
            if s.intersection ( x ) :
                print ( x , arr [ i ] , arr [ j ] )
                found = True
            else :
                s.add ( arr [ j ] )
    if found == False :
        print ( " No Triplet Found" )
|||

FIND_MAXIMUM_VALUE_OF_SUM_IARRI_WITH_ONLY_ROTATIONS_ON_GIVEN_ARRAY_ALLOWED

def maxSum ( ) :
    arrSum = 0
    currVal = 0
    for i in range ( len ( arr ) ) :
        arrSum = arrSum + arr [ i ]
        currVal = currVal + ( i * arr [ i ] )
    maxVal = currVal
    for j in range ( 1 , len ( arr ) ) :
        currVal = currVal + arrSum - len ( arr ) * arr [ len ( arr ) - j ]
        if currVal > maxVal :
            maxVal = currVal
    return maxVal
|||

PROGRAM_FOR_SCALAR_MULTIPLICATION_OF_A_MATRIX

def scalar_product_mat ( mat , k ) :
    for i in range ( N ) :
        for j in range ( N ) :
            mat [ i , j ] = mat [ i , j ] * k
|||

PRINT_SQUARES_FIRST_N_NATURAL_NUMBERS_WITHOUT_USING_1

def print_squares ( n ) :
    square , odd = 0 , 1
    for x in range ( n ) :
        print ( square , end = ' ' )
        square , odd = square + odd , odd + 2
|||

NTH_PENTAGONAL_NUMBER

def pentagonalNum ( n ) :
    return ( 3 * n ** 2 - n ) / 2
|||

COUNT_ARRAYS_ADJACENT_ELEMENTS_ONE_DIVIDE_ANOTHER

def numof_array ( n , m ) :
    dp = [ ]
    di = [ ]
    mu = [ ]
    for i in range ( MAX ) :
        for j in range ( MAX ) :
            dp [ i ] [ j ] = 0
    for i in range ( MAX ) :
        di.append ( [ ] )
        mu.append ( [ ] )
    for i in range ( 1 , m ) :
        for j in range ( 2 * i , m , i += 1 ) :
            di [ j ].append ( i )
            mu [ i ].append ( j )
        di [ i ].append ( i )
    for i in range ( 1 , m ) :
        dp [ 1 ] [ i ] = 1
    for i in range ( 2 , n ) :
        for j in range ( 1 , m ) :
            dp [ i ] [ j ] = 0
            for x in di [ j ] :
                dp [ i ] [ j ] += dp [ i - 1 ] [ x ]
            for x in mu [ j ] :
                dp [ i ] [ j ] += dp [ i - 1 ] [ x ]
    ans = 0
    for i in range ( 1 , m ) :
        ans += dp [ n ] [ i ]
        di.reverse ( )
        mu.reverse ( )
    return ans
|||

0_1_KNAPSACK_PROBLEM_DP_10

def knapSack ( W , wt , val , n ) :
    if n == 0 or W == 0 :
        return 0
    if wt [ - 1 ] > W :
        return knapSack ( W , wt , val , n - 1 )
    else :
        return max ( val [ - 1 ] + knapSack ( W - wt [ - 1 ] , wt , val , n - 1 ) , knapSack ( W , wt , val , n - 1 ) )
|||

FIND_TRIPLETS_ARRAY_WHOSE_SUM_EQUAL_ZERO

def find_triplets ( arr , n ) :
    found = True
    for i in range ( n - 2 ) :
        for j in range ( i + 1 , n - 1 ) :
            for k in range ( j + 1 , n ) :
                if arr [ i ] + arr [ j ] + arr [ k ] == 0 :
                    print ( arr [ i ] , end = ' ' )
                    print ( arr [ j ] , end = ' ' )
                    print ( arr [ k ] , end = ' ' )
                    print ( arr [ i ] , end = ' ' )
                    print ( arr [ j ] , end = ' ' )
                    print ( arr [ k ] , end = ' ' )
                    print ( arr [ i ] , end = ' ' )
                    found = True
    if found == False :
        print ( ' not exist ' )
|||

COUNT_NUMBER_WAYS_REACH_GIVEN_SCORE_GAME

def count ( n ) :
    table , i = [ 0 ] * ( n + 1 ) , 0
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
    final_sequence = [ ]
    final_sequence.sort ( )
    for i in range ( n // 2 ) :
        final_sequence.append ( a [ i ] )
        final_sequence.append ( a [ n - i - 1 ] )
    MaximumSum = 0
    for i in range ( n - 1 ) :
        MaximumSum = MaximumSum + abs ( final_sequence [ i ] - final_sequence [ i + 1 ] )
    MaximumSum = MaximumSum + abs ( final_sequence [ n - 1 ] - final_sequence [ 0 ] )
    return MaximumSum
|||

PROGRAM_FIND_MID_POINT_LINE

def midpoint ( x1 , x2 , y1 , y2 ) :
    print ( ( x1 + x2 ) / 2 , ( y1 + y2 ) / 2 )
|||

ALTERNATIVE_SORTING

def alternate_sort ( arr , n ) :
    arr.sort ( )
    i , j = 0 , n - 1
    while i < j :
        print ( arr [ j ] , end = ' ' )
        print ( arr [ i ] , end = ' ' )
    if n % 2 != 0 :
        print ( arr [ i ] )
|||

NUMBER_SUBARRAYS_SUM_EXACTLY_EQUAL_K

def findSubarraySum ( arr , n , sum ) :
    prevSum = { }
    res = 0
    currsum = 0
    for i in range ( n ) :
        currsum += arr [ i ]
        if currsum == sum :
            res += 1
        if prevSum.has_key ( currsum - sum ) :
            res += prevSum [ currsum - sum ]
        count = prevSum.get ( currsum )
        if count == None :
            prevSum [ currsum ] = 1
        else :
            prevSum [ currsum ] = count + 1
    return res
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
            search ( arr , mid + 2 , high )
        else :
            search ( arr , low , mid )
    elif mid % 2 == 1 :
        if arr [ mid ] == arr [ mid - 1 ] :
            search ( arr , mid + 1 , high )
        else :
            search ( arr , low , mid - 1 )
|||

FORM_SMALLEST_NUMBER_USING_ONE_SWAP_OPERATION

def smallest_number ( str ) :
    num = str.split ( '.' )
    n = len ( str )
    right_min = [ - 1 ] * n
    right = n - 1
    for i in range ( n - 2 , - 1 , - 1 ) :
        if num [ i ] > num [ right ] :
            right_min [ i ] = right
        else :
            right_min [ i ] = - 1
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
            temp = num [ 0 ]
            num [ 0 ] = num [ small ]
            num [ small ] = temp
        else :
            for i in range ( 1 , n ) :
                if right_min [ i ] != - 1 :
                    temp = num [ i ]
                    num [ i ] = num [ right_min [ i ] ]
                    num [ right_min [ i ] ] = temp
                    break
    return ( [ num [ i ] for i in range ( 1 , n ) ] )
|||

PROGRAM_AREA_SQUARE

def area_square ( side ) :
    area = side * side
    return area
|||

FIND_DAY_OF_THE_WEEK_FOR_A_GIVEN_DATE

def dayofweek ( d , m , y ) :
    t = [ 0 , 3 , 2 , 5 , 0 , 3 , 5 , 1 , 4 , 6 , 2 , 4 ]
    y -= ( m < 3 )
    return ( y + y / 4 - y / 100 + y / 400 + t [ m - 1 ] + d ) % 7
|||

CHECK_QUEUE_CAN_SORTED_ANOTHER_QUEUE_USING_STACK

def check_sorted ( n ) :
    st = [ ]
    expected = 1
    fnt = None
    while q.size != 0 :
        fnt = q.pop ( )
        q.extend ( [ fnt ] )
        if fnt == expected :
            expected += 1
        else :
            if len ( st ) == 0 :
                st.append ( fnt )
            elif len ( st ) != 0 and st [ - 1 ] < fnt :
                return False
            else :
                st.append ( fnt )
        while len ( st ) != 0 and st [ - 1 ] == expected :
            st.pop ( )
            expected += 1
    if expected - 1 == n and len ( st ) == 0 :
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
    if i == - 1 or j == - 1 or k == - 1 :
        return 0
    if dp [ i ] [ j ] [ k ] != - 1 :
        return dp [ i ] [ j ] [ k ]
    if X [ i ] == Y [ j ] and Y [ j ] == Z [ k ] :
        return dp [ i ] [ j ] [ k ] = 1 + lcsOf3 ( i - 1 , j - 1 , k - 1 )
    else :
        return dp [ i ] [ j ] [ k ] = max ( max ( lcsOf3 ( i - 1 , j , k ) , lcsOf3 ( i , j - 1 , k ) ) , lcsOf3 ( i , j , k - 1 ) )
|||

LOWER_INSERTION_POINT

def LowerInsertionPoint ( arr , n , X ) :
    if X < arr [ 0 ] :
        return 0
    elif X > arr [ n - 1 ] :
        return n
    lower_pnt = 0
    i = 1
    while i < n and arr [ i ] < X :
        lower_pnt = i
        i = i * 2
    while lower_pnt < n and arr [ lower_pnt ] < X :
        lower_pnt += 1
    return lower_pnt
|||

CONSTRUCT_LEXICOGRAPHICALLY_SMALLEST_PALINDROME

def constructPalin ( str , len ) :
    i , j = 0 , len - 1
    for i in range ( j ) :
        if str [ i ] == str [ j ] and str [ i ] != '*' :
            continue
        elif str [ i ] == str [ j ] and str [ i ] == '*' :
            str [ i ] = 'a'
            str [ j ] = 'a'
            continue
        elif str [ i ] == '*' :
            str [ i ] = str [ j ]
            continue
        elif str [ j ] == '*' :
            str [ j ] = str [ i ]
            continue
        print ( "Not Possible" )
        return ""
    return str
|||

SECTION_FORMULA_POINT_DIVIDES_LINE_GIVEN_RATIO

def section ( x1 , x2 , y1 , y2 , m , n ) :
    x = ( ( n * x1 ) + ( m * x2 ) ) / ( m + n )
    y = ( ( n * y1 ) + ( m * y2 ) ) / ( m + n )
    print ( "(%f, %f)" % ( x , y ) )
|||

SQUARE_ROOT_NUMBER_USING_LOG

def squared_root ( n ) :
    return math.pow ( 2 , 0.5 * ( math.log ( n ) / math.log ( 2 ) ) )
|||

MAXIMIZE_SUM_ARRII

def max_sum ( arr , n ) :
    arr.sort ( )
    sum = 0
    for i in range ( n ) :
        sum += ( arr [ i ] * i )
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
        if count == k :
            count = 0
    return res
|||

COUNT_WORDS_WHOSE_TH_LETTER_EITHER_1_TH_TH_I1_TH_LETTER_GIVEN_WORD

def count_words ( str , len ) :
    count = 1
    if len == 1 :
        return count
    if str [ 0 ] == str [ 1 ] :
        count *= 1
    else :
        count *= 2
    for j in range ( 1 , len - 1 ) :
        if str [ j ] == str [ j - 1 ] and str [ j ] == str [ j + 1 ] :
            count *= 1
        elif str [ j ] == str [ j - 1 ] or str [ j ] == str [ j + 1 ] or str [ j - 1 ] == str [ j + 1 ] :
            count *= 2
        else :
            count *= 3
    if str [ len - 1 ] == str [ len - 2 ] :
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
    if d >= b :
        return ( d + b - 1 ) // b
    if d == 0 :
        return 0
    if d == a :
        return 1
    return 2
|||

SUM_FACTORS_NUMBER_1

def sumof_factors ( n ) :
    res = 1
    for i in range ( 2 , math.sqrt ( n ) ) :
        curr_sum = 1
        curr_term = 1
        while n % i == 0 :
            n = n // i
            curr_term *= i
            curr_sum += curr_term
        res *= curr_sum
    if n > 2 :
        res *= ( 1 + n )
    return res
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
            n = n - 2
        else :
            i += 1
    return len ( v )
|||

COUNT_NUMBER_BINARY_STRINGS_WITHOUT_CONSECUTIVE_1S

def countStrings ( n ) :
    a = [ ]
    b = [ ]
    a.append ( b.append = 1 )
    for i in range ( 1 , n ) :
        a.append ( a [ i - 1 ] + b [ i - 1 ] )
        b.append ( a [ i - 1 ] )
    return a.append ( b )
|||

FIND_THE_MISSING_NUMBER

def getMissingNo ( a , n ) :
    i , total = ( n + 1 ) * ( n + 2 ) / 2
    for i in range ( n ) :
        total -= a [ i ]
    return total
|||

SQUARE_ROOT_OF_A_PERFECT_SQUARE

def squareRoot ( n ) :
    x = n
    y = 1
    e = 0.000001
    while x - y > e :
        x = ( x + y ) / 2
        y = n / x
    return x
|||

SUBSET_SUM_PROBLEM_OSUM_SPACE

def isSubsetSum ( arr , n , sum ) :
    subset = [ [ ] for i in range ( 0 , n + 1 ) ]
    for i in range ( 0 , sum + 1 ) :
        for j in range ( 0 , sum + 1 ) :
            if j == 0 :
                subset [ i % 2 ] [ j ] = True
            elif i == 0 :
                subset [ i % 2 ] [ j ] = False
            elif arr [ i - 1 ] <= j :
                subset [ i % 2 ] [ j ] = subset [ ( i + 1 ) % 2 ] [ j - arr [ i - 1 ] ] or subset [ ( i + 1 ) % 2 ] [ j ]
            else :
                subset [ i % 2 ] [ j ] = subset [ ( i + 1 ) % 2 ] [ j ]
    return subset [ n % 2 ] [ sum ]
|||

MULTIPLICATIVE_INVERSE_UNDER_MODULO_M

def mod_inverse ( a , m ) :
    a = a % m
    for x in range ( 1 , m ) :
        if ( a * x ) % m == 1 :
            return x
    return 1
|||

COMPUTE_AVERAGE_TWO_NUMBERS_WITHOUT_OVERFLOW

def compute_average ( a , b ) :
    return ( a + b ) / 2
|||

REPRESENT_GIVEN_SET_POINTS_BEST_POSSIBLE_STRAIGHT_LINE

def best_approximate ( x , y ) :
    n = len ( x )
    m , c , sum_x , sum_y , sum_xy , sum_x2 = 0 , 0 , 0 , 0 , 0
    for i in range ( n ) :
        sum_x += x [ i ]
        sum_y += y [ i ]
        sum_xy += x [ i ] * y [ i ]
        sum_x2 += pow ( x [ i ] , 2 )
    m = ( n * sum_xy - sum_x * sum_y ) / ( n * sum_x2 - pow ( sum_x , 2 ) )
    c = ( sum_y - m * sum_x ) / n
    print ( 'm = %f' % m )
    print ( 'c = %f' % c )
|||

SPLIT_ARRAY_ADD_FIRST_PART_END

def split_arr ( arr , n , k ) :
    for i in range ( k ) :
        x = arr [ 0 ]
        for j in range ( n - 1 ) :
            arr [ j ] , arr [ j + 1 ] = arr [ j + 1 ] , arr [ j ]
        arr [ n - 1 ] , arr [ n - 1 ] = x , arr [ n - 1 ]
|||

MAXIMUM_POSSIBLE_DIFFERENCE_TWO_SUBSETS_ARRAY

def maxDiff ( arr , n ) :
    SubsetSum_1 , SubsetSum_2 = 0 , 0
    for i in range ( 0 , n - 1 ) :
        is_single_occurrence = True
        for j in range ( i + 1 , n - 1 ) :
            if arr [ i ] == arr [ j ] :
                is_single_occurrence = False
                arr [ i ] , arr [ j ] = arr [ i ] , arr [ j ]
                break
        if is_single_occurrence :
            if arr [ i ] > 0 :
                SubsetSum_1 += arr [ i ]
            else :
                SubsetSum_2 += arr [ i ]
    return abs ( SubsetSum_1 - SubsetSum_2 )
|||

LONGEST_SUBSEQUENCE_DIFFERENCE_ADJACENTS_ONE_SET_2

def longLenSub ( arr , n ) :
    um = { }
    longLen = 0
    for i in range ( n ) :
        len = 0
        if um.has_key ( arr [ i ] - 1 ) and len < um [ arr [ i ] - 1 ] :
            len = um [ arr [ i ] - 1 ]
        if um.has_key ( arr [ i ] + 1 ) and len < um [ arr [ i ] + 1 ] :
            len = um [ arr [ i ] + 1 ]
        um [ arr [ i ] ] = len + 1
        if longLen < um [ arr [ i ] ] :
            longLen = um [ arr [ i ] ]
    return longLen
|||

LONGEST_REPEATED_SUBSEQUENCE_1

def longest_repeated_subseq ( str ) :
    n = len ( str )
    dp = [ [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0
|||

FIND_INDEX_MAXIMUM_OCCURRING_ELEMENT_EQUAL_PROBABILITY

def find_random_index_of_max ( arr , n ) :
    mp = { }
    for i in range ( n ) :
        if mp.has_key ( arr [ i ] ) :
            mp [ arr [ i ] ] = mp [ arr [ i ] ] + 1
        else :
            mp [ arr [ i ] ] = 1
    max_element = int ( '-1' )
    max_so_far = int ( '-1' )
    for p , q in mp.items ( ) :
        if q > max_so_far :
            max_so_far = q
            max_element = p
    r = int ( ( random.random ( ) * max_so_far ) + 1 )
    for i , count in enumerate ( arr ) :
        if arr [ i ] == max_element :
            count += 1
        if count == r :
            print ( 'Element with maximum frequency present ' 'at index %d' % i )
            break
|||

CHECK_NUMBER_IS_PERFECT_SQUARE_USING_ADDITIONSUBTRACTION

def is_perfect_square ( n ) :
    for sum , i in itertools.combinations ( range ( 1 , n + 1 ) , 2 ) :
        sum += i
        if sum == n :
            return True
    return False
|||

N_BONACCI_NUMBERS_1

def bonacci_series ( n , m ) :
    a = [ 0 ] * m
    a [ n - 1 ] = 1
    a [ n ] = 1
    for i in range ( n + 1 , m ) :
        a [ i ] = 2 * a [ i - 1 ] - a [ i - n - 1 ]
    for i in range ( m ) :
        print ( a [ i ] , end = ' ' )
|||

COUNT_INDEX_PAIRS_EQUAL_ELEMENTS_ARRAY_1

def count_pairs ( arr , n ) :
    hm = { }
    for i in range ( n ) :
        if hm.has_key ( arr [ i ] ) :
            hm [ arr [ i ] ] = hm [ arr [ i ] ] + 1
        else :
            hm [ arr [ i ] ] = 1
    ans = 0
    for key , count in hm.items ( ) :
        ans += ( count * ( count - 1 ) ) / 2
    return ans
|||

SORT_EVEN_PLACED_ELEMENTS_INCREASING_ODD_PLACED_DECREASING_ORDER

def bitonic_generator ( arr , n ) :
    evenArr = [ ]
    oddArr = [ ]
    for i in range ( n ) :
        if i % 2 != 1 :
            evenArr.append ( arr [ i ] )
        else :
            oddArr.append ( arr [ i ] )
    evenArr.sort ( )
    oddArr.sort ( )
    i = 0
    for j in evenArr :
        arr [ i ] = evenArr [ j ]
    for j in oddArr :
        arr [ i ] = oddArr [ j ]
    return arr
|||

DYNAMIC_PROGRAMMING_SET_9_BINOMIAL_COEFFICIENT

def binomial_coeff ( n , k ) :
    if k == 0 or k == n :
        return 1
    return binomial_coeff ( n - 1 , k - 1 ) + binomial_coeff ( n - 1 , k )
|||

WRITE_A_C_PROGRAM_TO_FIND_THE_PARITY_OF_AN_UNSIGNED_INTEGER

def getParity ( n ) :
    parity = False
    while n != 0 :
        parity = not parity
        n = n & ( n - 1 )
    return parity
|||

CHECK_WHETHER_LARGE_NUMBER_DIVISIBLE_7

def isDivisible7 ( num ) :
    n = len ( num )
    if n == 0 and num [ 0 ] == '0' :
        return True
    if n % 3 == 1 :
        num = '00' + num
    if n % 3 == 2 :
        num = '0' + num
    n = len ( num )
    gSum , p = 0 , 1
    for i in range ( n - 1 , - 1 , - 1 ) :
        group = 0
        group += num [ i ] - '0'
        group += ( num [ i ] - '0' ) * 10
        group += ( num [ i ] - '0' ) * 100
        gSum = gSum + group * p
        p = p * - 1
    return ( gSum % 7 == 0 )
|||

PRODUCT_NODES_K_TH_LEVEL_TREE_REPRESENTED_STRING

def product_at_kth_level ( tree , k ) :
    level = - 1
    product = 1
    n = len ( tree )
    for i in range ( n ) :
        if tree [ i ] == '(' :
            level += 1
        elif tree [ i ] == ')' :
            level -= 1
        else :
            if level == k :
                product *= ( tree [ i ] - '0' )
    return product
|||

CHECK_WHETHER_GIVEN_NUMBER_EVEN_ODD

def is_even ( n ) :
    return ( n % 2 == 0 )
|||

COUNT_GROUPINGS_NUMBER_SUM_DIGITS_EVERY_SUB_GROUP_LESS_EQUALS_IMMEDIATE_RIGHT_SUB_GROUP

def countGroups ( position , previous_sum , length , num ) :
    if position == length :
        return 1
    res = 0
    sum = 0
    for i in range ( position , length ) :
        sum += ( num [ i ] - '0' )
        if sum >= previous_sum :
            res += countGroups ( i + 1 , sum , length , num )
    return res
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
            search ( arr , mid + 2 , high )
        else :
            search ( arr , low , mid )
    else :
        if arr [ mid ] == arr [ mid - 1 ] :
            search ( arr , mid + 1 , high )
        else :
            search ( arr , low , mid - 1 )
|||

DELETE_CONSECUTIVE_WORDS_SEQUENCE_1

def removeConsecutiveSame ( v ) :
    st = [ ]
    for i in range ( len ( v ) ) :
        if st == [ ] :
            st.append ( v [ i ] )
        else :
            str = st.pop ( )
            if str == v [ i ] :
                st.pop ( )
            else :
                st.append ( v [ i ] )
    return len ( st )
|||

MINIMUM_NUMBER_OF_JUMPS_TO_REACH_END_OF_A_GIVEN_ARRAY_2

def minJumps ( arr , n ) :
    jumps = [ ]
    min = None
    jumps.append ( 0 )
    for i in range ( n - 2 , - 1 , - 1 ) :
        if arr [ i ] == 0 :
            jumps.append ( int ( arr [ i ] ) )
        elif arr [ i ] >= n - i - 1 :
            jumps.append ( 1 )
        else :
            min = int ( arr [ i ] )
            for j in range ( i + 1 , n and j <= arr [ i ] + i ) :
                if min > jumps [ j ] :
                    min = jumps [ j ]
            if min != int ( arr [ i ] ) :
                jumps.append ( min + 1 )
            else :
                jumps.append ( min )
    return jumps [ 0 ]
|||

PROGRAM_FIND_GCD_FLOATING_POINT_NUMBERS

def gcd ( a , b ) :
    if a < b :
        return gcd ( b , a )
    if abs ( b ) < 0.001 :
        return a
    else :
        return ( gcd ( b , a - floor ( a / b ) * b ) )
|||

MAXIMUM_PROFIT_BY_BUYING_AND_SELLING_A_SHARE_AT_MOST_TWICE

def max_profit ( price , n ) :
    profit = [ 0 ] * n
    max_price = price [ n - 1 ]
    for i in range ( n - 1 ) :
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

def count_set_bits ( n ) :
    if n == 0 :
        return 0
    else :
        return ( n & 1 ) + count_set_bits ( n >> 1 )
|||

REORDER_A_ARRAY_ACCORDING_TO_GIVEN_INDEXES

def reorder ( ) :
    temp = [ ]
    for i in range ( len ( arr ) ) :
        temp.append ( index [ i ] )
    for i in range ( len ( arr ) ) :
        arr [ i ] = temp [ i ]
        index [ i ] = i
|||

CHECK_IF_A_GIVEN_ARRAY_CAN_REPRESENT_PREORDER_TRAVERSAL_OF_BINARY_SEARCH_TREE

def can_representBST ( pre , n ) :
    s = Stack ( )
    root = int ( '-1' )
    for i in range ( n ) :
        if pre [ i ] < root :
            return False
        while not s.empty ( ) and s.peek ( ) < pre [ i ] :
            root = s.pop ( )
            s.pop ( )
        s.push ( pre [ i ] )
    return True
|||

FIND_REPETITIVE_ELEMENT_1_N_1_3

def find_repeated ( arr , n ) :
    missing_element = 0
    for i in range ( n ) :
        element = arr [ abs ( arr [ i ] ) ]
        if element < 0 :
            missing_element = arr [ i ]
            break
        arr [ abs ( arr [ i ] ) ] = - arr [ abs ( arr [ i ] ) ]
    return abs ( missing_element )
|||

DYNAMIC_PROGRAMMING_SET_8_MATRIX_CHAIN_MULTIPLICATION_1

def MatrixChainOrder ( p , n ) :
    m = [ [ ] for i in range ( n ) ]
    i , j , k , L , q = 0 , 0 , 0 , 0
    for i in range ( 1 , n ) :
        m [ i ] [ i ] = 0
    for L in range ( 2 , n ) :
        for i in range ( 1 , n - L + 1 ) :
            j = i + L - 1
            if j == n :
                continue
            m [ i ] [ j ] = int ( m [ i ] [ j ] )
            for k in range ( i , j - 1 ) :
                q = m [ i ] [ k ] + m [ k + 1 ] [ j ] + p [ i - 1 ] * p [ k ] * p [ j ]
                if q < m [ i ] [ j ] :
                    m [ i ] [ j ] = q
    return m [ 1 ] [ n - 1 ]
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
|||

MINIMIZE_MAXAI_BJ_CK_MINAI_BJ_CK_THREE_DIFFERENT_SORTED_ARRAYS

def solve ( A , B , C ) :
    i , j , k = A.shape
    min_diff , current_diff , max_term = abs ( max ( A [ i ] , max ( B [ j ] , C [ k ] ) ) - min ( A [ i ] , min ( B [ j ] , C [ k ] ) ) )
    while i != - 1 and j != - 1 and k != - 1 :
        current_diff , current_term = abs ( max ( A [ i ] , max ( B [ j ] , C [ k ] ) ) - min ( A [ i ] , min ( B [ j ] , C [ k ] ) ) )
        if current_diff < min_diff :
            min_diff = current_diff
        max_term , current_term = abs ( max ( A [ i ] , max ( B [ j ] , C [ k ] ) ) - min ( A [ i ] , min ( B [ j ] , C [ k ] ) ) )
        if A [ i ] == max_term :
            i -= 1
        elif B [ j ] == max_term :
            j -= 1
        else :
            k -= 1
    return min_diff , current_diff , max_term
|||

ROOTS_QUADRATIC_EQUATION

def findRoots ( a , b , c ) :
    if a == 0 :
        print ( "Invalid" )
        return
    d = b ** 2 - 4 * a * c
    sqrt_val = sqrt ( abs ( d ) )
    if d > 0 :
        print ( "Roots are real and different \n" )
        print ( float ( - b + sqrt_val ) / ( 2 * a ) + "\n" + float ( - b - sqrt_val ) / ( 2 * a ) )
    else :
        print ( "Roots are complex \n" )
        print ( - float ( b / ( 2 * a ) ) + " + i" + sqrt_val + "\n" + - float ( b / ( 2 * a ) ) + " - i" + sqrt_val )
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
|||

FIND_MINIMUM_ELEMENT_IN_A_SORTED_AND_ROTATED_ARRAY

def findMin ( arr , low , high ) :
    if high < low :
        return arr [ 0 ]
    if high == low :
        return arr [ low ]
    mid = low + ( high - low ) // 2
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
        count [ str [ i ] - 'a' ] += 1
    if count [ 0 ] == n or count [ 1 ] == n or count [ 2 ] == n :
        return n
    if ( count [ 0 ] % 2 ) == ( count [ 1 ] % 2 ) and ( count [ 1 ] % 2 ) == ( count [ 2 ] % 2 ) :
        return 2
    return 1
|||

CHECK_LARGE_NUMBER_DIVISIBLE_3_NOT

def check ( str ) :
    n = len ( str )
    digitSum = 0
    for i in range ( n ) :
        digitSum += ( str [ i ] - '0' )
    return ( digitSum % 3 == 0 )
|||

COMPUTE_N_UNDER_MODULO_P

def mod_fact ( n , p ) :
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
    for c in s :
        freq [ c ] += 1
    for c in q :
        freq [ c ] -= 1
        if freq [ c ] < 0 :
            return False
    return True
|||

NEXT_POWER_OF_2_1

def next_power_of_2 ( n ) :
    p = 1
    if n and ( n & ( n - 1 ) ) == 0 :
        return n
    while p < n :
        p <<= 1
    return p
|||

REORDER_A_ARRAY_ACCORDING_TO_GIVEN_INDEXES_1

def reorder ( ) :
    for i in range ( len ( arr ) ) :
        while index [ i ] != i :
            old_target_i = index [ index [ i ] ]
            old_target_e = ord ( arr [ index [ i ] ] )
            arr [ index [ i ] ] = arr [ i ]
            index [ index [ i ] ] = index [ i ]
            index [ i ] = old_target_i
            arr [ i ] = old_target_e
|||

UNBOUNDED_KNAPSACK_REPETITION_ITEMS_ALLOWED

def _unboundedKnapsack ( W , n , val , wt ) :
    dp = [ 0 ] * ( W + 1 )
    for i in range ( 0 , W + 1 ) :
        for j in range ( 0 , n ) :
            if wt [ j ] <= i :
                dp [ i ] = max ( dp [ i ] , dp [ i - wt [ j ] ] + val [ j ] )
    return dp [ W ]
|||

PROGRAM_CHECK_DIAGONAL_MATRIX_SCALAR_MATRIX

def isDiagonalMatrix ( mat ) :
    for i in range ( N ) :
        for j in range ( N ) :
            if ( i != j ) :
                return False
    return True
|||

MAXIMUM_REMOVAL_FROM_ARRAY_WHEN_REMOVAL_TIME_WAITING_TIME

def max_removal ( arr , n ) :
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
    result = ""
    stars = ""
    for i in word :
        stars += '*'
    index = 0
    for i in word_list :
        if i == word :
            word_list [ index ] = stars
        index += 1
    for i in word_list :
        result += i + ' '
    return result
|||

COUNT_STRINGS_WITH_CONSECUTIVE_1S

def count_strings ( n ) :
    a , b = [ 0 ] , [ 1 ]
    for i in range ( 1 , n ) :
        a [ i ] = a [ i - 1 ] + b [ i - 1 ]
        b [ i ] = a [ i - 1 ]
    from 2 ** n
    return ( 1 << n ) - a [ n - 1 ] - b [ n - 1 ]
|||

LENGTH_LONGEST_BALANCED_SUBSEQUENCE

def max_length ( s , n ) :
    dp = [ [ ] for i in range ( n ) ]
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
|||

FIND_THE_POINT_WHERE_MAXIMUM_INTERVALS_OVERLAP

def find_max_guests ( arrl , exit , n ) :
    arrl.sort ( )
    exit.sort ( )
    guests_in , max_guests , time = arrl [ 0 ] , arrl [ 1 ] , arrl [ 2 ]
    i , j = 1 , 0
    while i < n and j < n :
        if arrl [ i ] <= exit [ j ] :
            guests_in += 1
            if guests_in > max_guests :
                max_guests = guests_in
                time = arrl [ i ]
            i += 1
        else :
            guests_in -= 1
            j += 1
    print ( "Maximum Number of Guests = " + str ( max_guests ) + " at time " + str ( time ) )
|||

EFFICIENT_WAY_CHECK_WHETHER_N_TH_FIBONACCI_NUMBER_MULTIPLE_10

def is_multiple_of_10 ( n ) :
    if n % 15 == 0 :
        return True
    return False
|||

MAXIMUM_SUM_PAIRS_SPECIFIC_DIFFERENCE

def max_sum_pair_with_difference_less_k ( arr , N , K ) :
    arr.sort ( )
    dp = [ 0 ] * N
    for i in range ( 1 , N ) :
        dp [ i ] = dp [ i - 1 ]
        if arr [ i ] - arr [ i - 1 ] < K :
            if i >= 2 :
                dp [ i ] = max ( dp [ i ] , dp [ i - 2 ] + arr [ i ] + arr [ i - 1 ] )
            else :
                dp [ i ] = max ( dp [ i ] , arr [ i ] + arr [ i - 1 ] )
    return dp [ N - 1 ]
|||

FIND_K_PAIRS_SMALLEST_SUMS_TWO_ARRAYS

def k_smallest_pair ( arr1 , n1 , arr2 , n2 , k ) :
    if k > n1 * n2 :
        print ( "k pairs don't exist" )
        return
    index2 = range ( n1 )
    while k > 0 :
        min_sum = sys.maxint
        min_index = 0
        for i1 in range ( n1 ) :
            if index2 [ i1 ] < n2 and arr1 [ i1 ] + arr2 [ index2 [ i1 ] ] < min_sum :
                min_index = i1
                min_sum = arr1 [ i1 ] + arr2 [ index2 [ i1 ] ]
        print ( "(" + str ( arr1 [ min_index ] ) + ", " + str ( arr2 [ index2 [ min_index ] ] ) + ") " )
        index2 [ min_index ] += 1
        k -= 1
|||

FIRST_UPPERCASE_LETTER_IN_A_STRING_ITERATIVE_AND_RECURSIVE_1

def first ( str , i ) :
    if str [ i ] == '\0' :
        return 0
    if ord ( str [ i ] ) < 128 :
        return str [ i ]
    return first ( str , i + 1 )
|||

FIND_PAIRS_B_ARRAY_B_K

def printPairs ( arr , n , k ) :
    isPairFound = True
    for i in range ( n ) :
        for j in range ( n ) :
            if i != j and arr [ i ] % arr [ j ] == k :
                print ( "(" + str ( arr [ i ] ) + ", " + str ( arr [ j ] ) + ")" + " " )
                isPairFound = True
    return isPairFound
|||

FIND_ARRANGEMENT_QUEUE_GIVEN_TIME

def solve ( n , t , s ) :
    for i in range ( t ) :
        for j in range ( n - 1 ) :
            if s [ j ] == 'B' and s [ j + 1 ] == 'G' :
                temp = s [ j ]
                s [ j ] = s [ j + 1 ]
                s [ j + 1 ] = temp
                j += 1
        print ( s )
|||

SHORTEST_POSSIBLE_COMBINATION_TWO_STRINGS

def print_superseq ( a , b ) :
    m , n = len ( a ) , len ( b )
    dp = [ [ 0 ] * m + [ 0 ] * n + [ 0 ] * n for i in range ( 0 , m ) ]
    for i in range ( 0 , n ) :
        for j in range ( 0 , m ) :
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
            res = a [ i - 1 ] + res
            i -= 1
            j -= 1
        elif dp [ i - 1 ] [ j ] < dp [ i ] [ j - 1 ] :
            res = a [ i - 1 ] + res
            i -= 1
        else :
            res = b [ j - 1 ] + res
            j -= 1
    while i > 0 :
        res = a [ i - 1 ] + res
        i -= 1
    while j > 0 :
        res = b [ j - 1 ] + res
        j -= 1
    print ( res )
|||

COUNT_ROTATIONS_DIVISIBLE_8

def countRotationsDivBy8 ( n ) :
    n = n.split ( )
    count = 0
    if len ( n ) == 1 :
        oneDigit = n [ 0 ] - '0'
        if oneDigit % 8 == 0 :
            return 1
        return 0
    if len ( n ) == 2 :
        first = ( n [ 0 ] - '0' ) * 10 + ( n [ 1 ] - '0' )
        second = ( n [ 1 ] - '0' ) * 10 + ( n [ 0 ] - '0' )
        if first % 8 == 0 :
            count += 1
        if second % 8 == 0 :
            count += 1
        return count
    threeDigit = 0
    for i in range ( ( len ( n ) - 2 ) ) :
        threeDigit = ( n [ i ] - '0' ) * 100 + ( n [ i + 1 ] - '0' ) * 10 + ( n [ i + 2 ] - '0' )
        if threeDigit % 8 == 0 :
            count += 1
    threeDigit = ( n [ len ( n ) - 1 ] - '0' ) * 100 + ( n [ 0 ] - '0' ) * 10 + ( n [ 1 ] - '0' )
    if threeDigit % 8 == 0 :
        count += 1
    threeDigit = ( n [ len ( n ) - 2 ] - '0' ) * 100 + ( n [ len ( n ) - 1 ] - '0' ) * 10 + ( n [ 0 ] - '0' )
    if threeDigit % 8 == 0 :
        count += 1
    return count
|||

LONGEST_COMMON_SUBSEQUENCE_WITH_AT_MOST_K_CHANGES_ALLOWED

def lcs ( dp , arr1 , n , arr2 , m , k ) :
    if k < 0 :
        return - 10000000
    if n < 0 or m < 0 :
        return 0
    ans = dp [ n ] [ m ] [ k ]
    if ans != - 1 :
        return ans
    try :
        ans = max ( lcs ( dp , arr1 , n - 1 , arr2 , m , k ) , lcs ( dp , arr1 , n , arr2 , m - 1 , k ) )
        if arr1 [ n - 1 ] == arr2 [ m - 1 ] :
            ans = max ( ans , 1 + lcs ( dp , arr1 , n - 1 , arr2 , m - 1 , k ) )
        ans = max ( ans , 1 + lcs ( dp , arr1 , n - 1 , arr2 , m - 1 , k - 1 ) )
    except :
        pass
    return ans
|||

CHECK_LINE_TOUCHES_INTERSECTS_CIRCLE

def checkCollision ( a , b , c , x , y , radius ) :
    dist = ( abs ( a * x + b * y + c ) ) / math.sqrt ( a ** 2 + b ** 2 )
    if radius == dist :
        print ( "Touch" )
    elif radius > dist :
        print ( "Intersect" )
    else :
        print ( "Outside" )
|||

FIND_THE_MAXIMUM_SUBARRAY_XOR_IN_A_GIVEN_ARRAY

def max_subarray_XOR ( arr , n ) :
    ans = int ( 0 )
    for i in range ( n ) :
        curr_xor = 0
        for j in range ( i , n ) :
            curr_xor = curr_xor ^ arr [ j ]
            ans = max ( ans , curr_xor )
    return ans
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
            rec_res = shortestPath ( graph , i , v , k - 1 )
            if rec_res != INF :
                res = min ( res , graph [ u ] [ i ] + rec_res )
    return res
|||

FIND_SUBARRAY_WITH_GIVEN_SUM

def subArraySum ( arr , n , sum ) :
    curr_sum , i , j = 0 , 0 , 0
    for i in range ( n ) :
        curr_sum = arr [ i ]
        for j in range ( i + 1 , n + 1 ) :
            if curr_sum == sum :
                p = j - 1
                print ( "Sum found between indexes " + str ( i ) + " and " + str ( p ) )
                return 1
            if curr_sum > sum or j == n :
                break
            curr_sum = curr_sum + arr [ j ]
    print ( "No subarray found" )
    return 0
|||

K_TH_PRIME_FACTOR_GIVEN_NUMBER

def k_prime_factor ( n , k ) :
    while n % 2 == 0 :
        k -= 1
        n = n // 2
        if k == 0 :
            return 2
    for i in range ( 3 , math.sqrt ( n ) , 2 ) :
        while n % i == 0 :
            if k == 1 :
                return i
            k -= 1
            n = n // i
    if n > 2 and k == 1 :
        return n
    return - 1
|||

FIND_ROTATION_COUNT_ROTATED_SORTED_ARRAY_1

def countRotations ( arr , low , high ) :
    if high < low :
        return 0
    if high == low :
        return low
    mid = low + ( high - low ) // 2
    if mid < high and arr [ mid + 1 ] < arr [ mid ] :
        return ( mid + 1 )
    if mid > low and arr [ mid ] < arr [ mid - 1 ] :
        return mid
    if arr [ high ] > arr [ mid ] :
        return countRotations ( arr , low , mid - 1 )
    return countRotations ( arr , mid + 1 , high )
|||

COMPUTE_AVERAGE_TWO_NUMBERS_WITHOUT_OVERFLOW_1

def compute_average ( a , b ) :
    return ( a / 2 ) + ( b / 2 ) + ( ( a % 2 + b % 2 ) / 2 )
|||

SORTING_USING_TRIVIAL_HASH_FUNCTION_1

def sort_using_hash ( a , n ) :
    max = sum ( a )
    min = abs ( sum ( a ) )
    hashpos = [ ]
    hashneg = [ ]
    for i in range ( n ) :
        if a [ i ] >= 0 :
            hashpos.append ( a [ i ] )
        else :
            hashneg.append ( abs ( a [ i ] ) )
    for i in range ( min , 0 , - 1 ) :
        if hashneg [ i ] > 0 :
            for j in range ( hashneg [ i ] ) :
                print ( ( - 1 ) * i , end = ' ' )
    for i in range ( 0 , max ) :
        if hashpos [ i ] > 0 :
            for j in range ( hashpos [ i ] ) :
                print ( i , end = ' ' )
|||

FIND_THE_TWO_REPEATING_ELEMENTS_IN_A_GIVEN_ARRAY_1

def printRepeating ( arr , size ) :
    count = [ 0 ] * size
    i = 0
    print ( "Repeated elements are : " )
    for i in range ( size ) :
        if count [ arr [ i ] ] == 1 :
            print ( arr [ i ] + " " )
        else :
            count [ arr [ i ] ] += 1
|||

MINIMUM_STEPS_MINIMIZE_N_PER_GIVEN_CONDITION

def getMinSteps ( n ) :
    table = [ n + 1 ] * ( n + 1 )
    for i in range ( 0 , n + 1 ) :
        table [ i ] = n - i
    for i in range ( n , - 1 , - 1 ) :
        if not ( i % 2 > 0 ) :
            table [ i / 2 ] = min ( table [ i ] + 1 , table [ i / 2 ] )
        if not ( i % 3 > 0 ) :
            table [ i / 3 ] = min ( table [ i ] + 1 , table [ i / 3 ] )
    return table [ 1 ]
|||

COUNT_POSSIBLE_DECODINGS_GIVEN_DIGIT_SEQUENCE_1

def count_decoding_dp ( digits , n ) :
    count = [ 1 ] * ( n + 1 )
    if digits [ 0 ] == '0' :
        return 0
    for i in range ( 2 , n + 1 ) :
        count [ i ] = 0
        if digits [ i - 1 ] > '0' :
            count [ i ] = count [ i - 1 ]
        if digits [ i - 2 ] == '1' or ( digits [ i - 2 ] == '2' and digits [ i - 1 ] < '7' ) :
            count [ i ] += count [ i - 2 ]
    return count [ n ]
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
            while i * i + j * j + k * k <= ab :
                l = math.sqrt ( ab - ( i * i + j * j + k * k ) )
                if math.floor ( l ) == math.ceil ( l ) and l >= k :
                    flag = True
                    print ( "i = %d\n" % i )
                    print ( "j = %d\n" % j )
                    print ( "k = %d\n" % k )
                    print ( "l = %d\n" % int ( l ) )
                    print ( "Product of %d and %d can be written as sum of squares" " of i, j, k, l \n" % ( a , b ) )
                    print ( "%d = %d*%d + %d*%d + %d*%d + %d*%d + %d*%d\n" % ( ab , i , i , j , j , k , k , int ( l ) , int ( l ) ) )
                k += 1
            j += 1
        i += 1
    if flag == False :
        print ( "Solution doesn't exist!" )
        return
|||

COUNT_NUMBER_INCREASING_SUBSEQUENCES_SIZE_K

def numOfIncSubseqOfSizeK ( arr , n , k ) :
    dp , sum = [ 0 ] , 0
    for i in range ( n ) :
        dp [ 0 ] [ i ] = 1
    for l in range ( 1 , k ) :
        for i in range ( l , n ) :
            dp [ l ] [ i ] = 0
            for j in range ( l - 1 , i ) :
                if arr [ j ] < arr [ i ] :
                    dp [ l ] [ i ] += dp [ l - 1 ] [ j ]
    for i in range ( k - 1 , n ) :
        sum += dp [ k - 1 ] [ i ]
    return sum
|||

KNAPSACK_PROBLEM_1

def knapSack ( W , wt , val , n ) :
    i , w = 0 , 0
    K = [ 0 ] * ( n + 1 ) * ( W + 1 )
    for i in range ( 0 , n + 1 ) :
        for w in range ( 0 , W + 1 ) :
            if i == 0 or w == 0 :
                K [ i ] [ w ] = 0
            elif wt [ i - 1 ] <= w :
                K [ i ] [ w ] = max ( val [ i - 1 ] + K [ i - 1 ] [ w - wt [ i - 1 ] ] , K [ i - 1 ] [ w ] )
            else :
                K [ i ] [ w ] = K [ i - 1 ] [ w ]
    return K [ n ] [ W ]
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
            print ( "  " , end = ' ' )
            csp1 = csp1 + 1
        cst1 = 1
        while cst1 <= nst :
            print ( val1 , end = ' ' )
            val1 = val1 - 1
            cst1 = cst1 + 1
        csp2 = 1
        while csp2 <= nsp2 :
            print ( "  " , end = ' ' )
            csp2 = csp2 + 1
        if row != 1 and row != n :
            cst2 = 1
            while cst2 <= nst :
                print ( val2 , end = ' ' )
                val2 = val2 + 1
                cst2 = cst2 + 1
        print ( )
        if row <= n / 2 :
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

def find_integer ( arr , n ) :
    hash = { }
    maximum = 0
    for i in range ( n ) :
        if arr [ i ] < 0 :
            hash [ abs ( arr [ i ] ) ] = ( hash [ abs ( arr [ i ] ) ] if i in hash else 0 ) - 1
        else :
            hash [ abs ( arr [ i ] ) ] = ( hash [ abs ( arr [ i ] ) ] if i in hash else 0 ) + 1
    for i in range ( n ) :
        if hash [ i ] > 0 :
            return arr [ i ]
    return - 1
|||

SPACE_OPTIMIZED_SOLUTION_LCS

def lcs ( X , Y ) :
    m , n = len ( X ) , len ( Y )
    L = [ [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0
|||

REPRESENT_NUMBER_SUM_MINIMUM_POSSIBLE_PSUEDOBINARY_NUMBERS

def psuedo_binary ( n ) :
    while n != 0 :
        temp , m , p = n , 0 , 1
        while temp != 0 :
            rem = temp % 10
            temp , m , p = temp , m , p
            if rem != 0 :
                m += p
            p *= 10
        print ( m , end = ' ' )
        n = n - m
    print ( ' ' )
|||

FIND_NUMBER_CURRENCY_NOTES_SUM_UPTO_GIVEN_AMOUNT

def count_currency ( amount ) :
    notes = [ 2000 , 500 , 200 , 100 , 50 , 20 , 10 , 5 , 1 ]
    note_counter = [ ]
    for i in range ( 9 ) :
        if amount >= notes [ i ] :
            note_counter.append ( amount / notes [ i ] )
            amount = amount - note_counter [ i ] * notes [ i ]
    print ( "Currency Count ->" )
    for i in range ( 9 ) :
        if note_counter [ i ] != 0 :
            print ( notes [ i ] , " : " , note_counter [ i ] )
|||

POSITIVE_ELEMENTS_EVEN_NEGATIVE_ODD_POSITIONS

def rearrange ( a , size ) :
    positive , negative = 0 , 1 , 0
    temp = 0
    while True :
        while positive < size and a [ positive ] >= 0 :
            positive += 2
        while negative < size and a [ negative ] <= 0 :
            negative += 2
        if positive < size and negative < size :
            temp = a [ positive ]
            a [ positive ] , a [ negative ] = a [ negative ] , temp
        else :
            break
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
            temp = arr [ index ]
            arr [ index ] = arr [ index - 1 ]
            arr [ index - 1 ] = temp
            index -= 1
    return
|||

NUMBER_WAYS_INSERT_CHARACTER_INCREASE_LCS_ONE

def numberofways ( A , B , N , M ) :
    pos = [ ]
    for i in range ( MAX ) :
        pos.append ( [ ] )
    for i in range ( M ) :
        pos [ B [ i ] ].append ( i + 1 )
    dpl = [ [ ] for i in range ( N + 2 ) ]
    dpr = [ [ ] for i in range ( N + 2 ) ]
    for i in range ( 1 , N + 1 ) :
        for j in range ( 1 , M + 1 ) :
            if A [ i - 1 ] == B [ j - 1 ] :
                dpl [ i ] [ j ] = dpl [ i - 1 ] [ j - 1 ] + 1
            else :
                dpl [ i ] [ j ] = max ( dpl [ i - 1 ] [ j ] , dpl [ i ] [ j - 1 ] )
    LCS = dpl [ N ] [ M ]
    dpr = [ [ ] for i in range ( N + 2 ) ]
    for i in range ( N , 1 , - 1 ) :
        for j in range ( M , - 1 , - 1 ) :
            if A [ i - 1 ] == B [ j - 1 ] :
                dpr [ i ] [ j ] = dpr [ i + 1 ] [ j + 1 ] + 1
            else :
                dpr [ i ] [ j ] = max ( dpr [ i + 1 ] [ j ] , dpr [ i ] [ j + 1 ] )
    ans = 0
    for i in range ( 0 , N + 1 ) :
        for j in range ( 0 , MAX ) :
            for x in pos [ j ] :
                if dpl [ i ] [ x - 1 ] + dpr [ i + 1 ] [ x + 1 ] == LCS :
                    ans += 1
                    break
    return ans
|||

MINIMUM_PRODUCT_K_INTEGERS_ARRAY_POSITIVE_INTEGERS

def min_product ( arr , n , k ) :
    pq = PriorityQueue ( )
    for i in range ( n ) :
        pq.add ( arr [ i ] )
    count , ans = 0 , 1
    while pq.empty ( ) == False and count < k :
        ans = ans * pq.element ( )
        pq.pop ( )
        count += 1
    return ans
|||

FIND_UNIQUE_ELEMENTS_MATRIX

def unique ( mat , n , m ) :
    maximum , flag = 0 , 0
    for i in range ( n ) :
        for j in range ( m ) :
            if maximum < mat [ i ] [ j ] :
                maximum = mat [ i ] [ j ]
        b = [ 0 ] * ( maximum + 1 )
        for i in range ( n ) :
            for j in range ( m ) :
                b [ mat [ i ] [ j ] ] += 1
        for i in range ( 1 , maximum + 1 ) :
            if b [ i ] == 1 :
                print ( i , end = ' ' )
        flag = 1
        if flag == 0 :
            print ( 'No unique element ' + 'in the matrix' )
    
|||

LONGEST_SUBSEQUENCE_SUCH_THAT_DIFFERENCE_BETWEEN_ADJACENTS_IS_ONE

def longestSubseqWithDiffOne ( arr , n ) :
    dp = [ 1 ] * n
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
|||

C_PROGRAM_CONCATENATE_STRING_GIVEN_NUMBER_TIMES

def repeat ( s , n ) :
    s1 = s
    for i in range ( 1 , n ) :
        s += s1
    return s
|||

SEARCHING_FOR_PATTERNS_SET_1_NAIVE_PATTERN_SEARCHING

def search ( txt , pat ) :
    M = len ( pat )
    N = len ( txt )
    for i in range ( 0 , N - M + 1 ) :
        j = 0
        for j in range ( M ) :
            if txt [ i + j ] != pat [ j ] :
                break
        if j == M :
            print ( "Pattern found at index " + str ( i ) )
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
|||

COUNT_DIVISIBLE_PAIRS_ARRAY

def count_divisibles ( arr , n ) :
    res = 0
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if arr [ i ] % arr [ j ] == 0 or arr [ j ] % arr [ i ] == 0 :
                res += 1
    return res
|||

PROGRAM_TO_CHECK_IF_A_MATRIX_IS_SYMMETRIC

def isSymmetric ( mat , N ) :
    for i in range ( N ) :
        for j in range ( N ) :
            if mat [ i ] [ j ] != mat [ j ] [ i ] :
                return False
    return True
|||

COUNT_PALINDROME_SUB_STRINGS_STRING

def CountPS ( str , n ) :
    dp = [ [ ] for i in range ( n ) ]
    P = [ [ ] for i in range ( n ) ]
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
|||

WAYS_SUM_N_USING_ARRAY_ELEMENTS_REPETITION_ALLOWED

def countWays ( N ) :
    count = [ 0 ] * ( N + 1 )
    count [ 0 ] = 1
    for i in range ( 1 , N + 1 ) :
        for j in range ( len ( arr ) ) :
            if i >= arr [ j ] :
                count [ i ] += count [ i - arr [ j ] ]
    return count [ N ]
|||

MINIMUM_NUMBER_OF_OPERATIONS_TO_MOVE_ALL_UPPERCASE_CHARACTERS_BEFORE_ALL_LOWER_CASE_CHARACTERS

def min_operations ( str , n ) :
    i , last_upper = - 1 , - 1
    first_lower = - 1
    for i in range ( n - 1 , - 1 , - 1 ) :
        if re.search ( r '[\W_]' , str [ i ] ) :
            last_upper = i
            break
    for i in range ( n ) :
        if re.search ( r '[\W_]' , str [ i ] ) :
            first_lower = i
            break
    if last_upper == - 1 or first_lower == - 1 :
        return 0
    count_upper = 0
    for i in range ( first_lower , n ) :
        if re.search ( r '[\W_]' , str [ i ] ) :
            count_upper += 1
    count_lower = 0
    for i in range ( last_upper ) :
        if re.search ( r '[\W_]' , str [ i ] ) :
            count_lower += 1
    return min ( count_lower , count_upper )
|||

PRINT_A_GIVEN_MATRIX_IN_SPIRAL_FORM

def spiral_print ( m , n , a ) :
    i , k , l = 0 , 0 , 0
    while k < m and l < n :
        for i in range ( l , n ) :
            print ( a [ k ] [ i ] , end = ' ' )
        k += 1
        for i in range ( k , m ) :
            print ( a [ i ] [ n - 1 ] , end = ' ' )
        n -= 1
        if k < m :
            for i in range ( n - 1 , i >= l ) :
                print ( a [ m - 1 ] [ i ] , end = ' ' )
            m -= 1
        if l < n :
            for i in range ( m - 1 , i >= k ) :
                print ( a [ i ] [ l ] , end = ' ' )
            l += 1
|||

FIND_DISTINCT_INTEGERS_FOR_A_TRIPLET_WITH_GIVEN_PRODUCT

def find_triplets ( x ) :
    fact = [ ]
    factors = set ( )
    for i in range ( 2 , math.sqrt ( x ) + 1 ) :
        if x % i == 0 :
            fact.append ( i )
            if x / i != i :
                fact.append ( x / i )
            factors.add ( i )
            factors.add ( x / i )
    found = False
    k = len ( fact )
    for i in range ( k ) :
        a = fact [ i ]
        for j in range ( k ) :
            b = fact [ j ]
            if ( a != b ) and ( x % ( a * b ) == 0 ) and ( x / ( a * b ) != a ) and ( x / ( a * b ) != b ) and ( x / ( a * b ) != 1 ) :
                print ( a , b , ( x / ( a * b ) ) )
                found = True
                break
        if found :
            break
    if not found :
        print ( '-1' )
|||

SUM_TWO_LARGE_NUMBERS_1

def find_sum ( str1 , str2 ) :
    if len ( str1 ) > len ( str2 ) :
        t = str1
        str1 = str2
        str2 = t
    str = ""
    n1 , n2 = len ( str1 ) , len ( str2 )
    diff = n2 - n1
    carry = 0
    for i in range ( n1 - 1 , - 1 , - 1 ) :
        sum = ( int ( str1 [ i ] - '0' ) + int ( str2 [ i + diff ] - '0' ) + carry )
        str += chr ( sum % 10 + '0' )
        carry = sum / 10
    for i in range ( n2 - n1 - 1 , - 1 , - 1 ) :
        sum = ( int ( str2 [ i ] - '0' ) + carry )
        str += chr ( sum % 10 + '0' )
        carry = sum / 10
    if carry :
        str += chr ( carry + '0' )
    return [ str ].reverse ( ) [ : : - 1 ]
|||

COCKTAIL_SORT

def cocktail_sort ( a ) :
    swapped = True
    start = 0
    end = len ( a )
    while swapped == True :
        swapped = False
        for i in range ( start , end - 1 ) :
            if a [ i ] > a [ i + 1 ] :
                temp = a [ i ]
                a [ i ] , a [ i + 1 ] = a [ i + 1 ] , a [ i + 1 ]
                a [ i + 1 ] = temp
                swapped = True
        if swapped == False :
            break
        swapped = False
        end = end - 1
        for i in range ( end - 1 , - start , - 1 ) :
            if a [ i ] > a [ i + 1 ] :
                temp = a [ i ]
                a [ i ] , a [ i + 1 ] = a [ i + 1 ] , a [ i + 1 ]
                a [ i + 1 ] = temp
                swapped = True
        start = start + 1
    return a
|||

COUNT_DERANGEMENTS_PERMUTATION_SUCH_THAT_NO_ELEMENT_APPEARS_IN_ITS_ORIGINAL_POSITION_1

def count_der ( n ) :
    der = [ 1 ] * ( n + 1 )
    der [ 0 ] = 1
    der [ 1 ] = 0
    der [ 2 ] = 1
    for i in range ( 3 , n + 1 ) :
        der [ i ] = ( i - 1 ) * ( der [ i - 1 ] + der [ i - 2 ] )
    return der [ n ]
|||

MAXIMUM_PRODUCT_SUBARRAY_ADDED_NEGATIVE_PRODUCT_CASE

def find_max_product ( arr , n ) :
    i = 0
    ans = int ( 0 )
    maxval = 1
    minval = 1
    prev_max = 0
    for i in range ( n ) :
        if arr [ i ] > 0 :
            maxval = maxval * arr [ i ]
            minval = min ( 1 , minval * arr [ i ] )
        elif arr [ i ] == 0 :
            minval = 1
            maxval = 0
        elif arr [ i ] < 0 :
            prev_max = maxval
            maxval = minval * arr [ i ]
            minval = prev_max * arr [ i ]
        ans = max ( ans , maxval )
        if maxval <= 0 :
            maxval = 1
    return ans
|||

REARRANGE_ARRAY_SUCH_THAT_EVEN_POSITIONED_ARE_GREATER_THAN_ODD

def assign ( a , n ) :
    a.sort ( )
    ans = [ ]
    p , q = 0 , n - 1
    for i in range ( n ) :
        if ( i + 1 ) % 2 == 0 :
            ans.append ( a [ q -- ] )
        else :
            ans.append ( a [ p ++ ] )
    for i in range ( n ) :
        print ( ans [ i ] , end = ' ' )
|||

FRIENDS_PAIRING_PROBLEM

def count_friend_pairings ( n ) :
    dp = [ ]
    for i in range ( 0 , n + 1 ) :
        if i <= 2 :
            dp.append ( i )
        else :
            dp.append ( dp [ i - 1 ] + ( i - 1 ) * dp [ i - 2 ] )
    return dp [ n ]
|||

PRIME_NUMBERS

def isPrime ( n ) :
    if n <= 1 :
        return False
    for i in range ( 2 , n ) :
        if n % i == 0 :
            return False
    return True
|||

PROBABILITY_REACHING_POINT_2_3_STEPS_TIME

def find_prob ( N , P ) :
    dp = np.zeros ( ( N + 1 , N + 1 ) )
    dp [ 0 ] = 1
    dp [ 1 ] = 0
    dp [ 2 ] = P
    dp [ 3 ] = 1 - P
    for i in range ( 4 , N + 1 ) :
        dp [ i ] = ( P ) * dp [ i - 2 ] + ( 1 - P ) * dp [ i - 3 ]
    return ( float ( dp [ N ] ) , float ( dp [ N + 1 ] ) )
|||

SMALLEST_OF_THREE_INTEGERS_WITHOUT_COMPARISON_OPERATORS_1

def smallest ( x , y , z ) :
    if ( y / x ) != 1 :
        return ( ( y / z ) != 1 )
    return ( ( x / z ) != 1 )
|||

COMMON_ELEMENTS_IN_ALL_ROWS_OF_A_GIVEN_MATRIX

def printCommonElements ( mat ) :
    mp = { }
    for j in range ( N ) :
        mp [ mat [ 0 ] [ j ] ] = 1
    for i in range ( 1 , M ) :
        for j in range ( N ) :
            if mp [ mat [ i ] [ j ] ] != 0 and mp [ mat [ i ] [ j ] ] == i :
                mp [ mat [ i ] [ j ] ] = i + 1
                if i == M - 1 :
                    print ( mat [ i ] [ j ] , end = ' ' )
|||

DETECTING_NEGATIVE_CYCLE_USING_FLOYD_WARSHALL

def neg_cyclefloyd_warshall ( graph ) :
    dist , i , j , k = [ ] , [ ] , [ ] , [ ]
    for i in range ( V ) :
        for j in range ( V ) :
            dist.append ( graph [ i , j ] )
    for k in range ( V ) :
        for i in range ( V ) :
            for j in range ( V ) :
                if dist [ i ] [ k ] + dist [ k ] [ j ] < dist [ i ] [ j ] :
                    dist [ i ] [ j ] = dist [ i ] [ k ] + dist [ k ] [ j ]
    for i in range ( V ) :
        if dist [ i ] [ i ] < 0 :
            return True
    return False
|||

PROGRAM_SORT_STRING_DESCENDING_ORDER

def sortString ( str ) :
    charCount = [ 0 ] * MAX_CHAR
    for i in range ( len ( str ) ) :
        charCount [ str [ i ] - 'a' ] += 1
    for i in range ( MAX_CHAR - 1 , - 1 , - 1 ) :
        for j in range ( charCount [ i ] ) :
            print ( chr ( 'a' + str [ j ] ) )
|||

COUNT_PAIRS_WITH_GIVEN_SUM

def get_paired_count ( arr , sum ) :
    count = 0
    for i in range ( len ( arr ) ) :
        for j in range ( i + 1 , len ( arr ) ) :
            if ( arr [ i ] + arr [ j ] ) == sum :
                count += 1
    print ( "Count of pairs is " + str ( count ) )
|||

SUM_SERIES_12_32_52_2N_12_1

def sum_of_series ( n ) :
    return ( n * ( 2 * n - 1 ) ** ( 2 * n + 1 ) ) / 3
|||

MAXIMUM_DIFFERENCE_BETWEEN_FREQUENCY_OF_TWO_ELEMENTS_SUCH_THAT_ELEMENT_HAVING_GREATER_FREQUENCY_IS_ALSO_GREATER

def maxdiff ( arr , n ) :
    freq = { }
    for i in range ( n ) :
        freq [ arr [ i ] ] = freq [ arr [ i ] ] if i in freq else 1
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

def shift_matrix_by_k ( mat , k ) :
    if k > N :
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
                    max = arr [ i ] [ j ]
            else :
                if min > arr [ i ] [ j ] :
                    min = arr [ i ] [ j ]
                if max < arr [ i ] [ n - j - 1 ] :
                    max = arr [ i ] [ n - j - 1 ]
    print ( "Maximum = " + str ( max ) + ", Minimum = " + str ( min ) )
|||

FIND_PAIR_WITH_GREATEST_PRODUCT_IN_ARRAY_1

def findGreatest ( arr , n ) :
    m = { }
    for i in range ( n ) :
        if m.has_key ( arr [ i ] ) :
            m [ arr [ i ] ] = m [ arr [ i ] ] + 1
        else :
            m [ arr [ i ] ] = m [ arr [ i ] ]
    arr.sort ( )
    for i in range ( n - 1 , 1 , - 1 ) :
        for j in range ( i , j + 1 , - 1 ) :
            if arr [ i ] % arr [ j ] == 0 :
                result = arr [ i ] / arr [ j ]
                if result != arr [ j ] and m [ result ] == 0 or m [ result ] > 0 :
                    return arr [ i ]
                elif result == arr [ j ] and m [ result ] > 1 :
                    return arr [ i ]
    return - 1
|||

0_1_KNAPSACK_PROBLEM_DP_10_1

def knapSack ( W , wt , val , n ) :
    i , w = 0 , 0
    K = [ 0 ] * ( n + 1 ) * ( W + 1 )
    for i in range ( 0 , n + 1 ) :
        for w in range ( 0 , W + 1 ) :
            if i == 0 or w == 0 :
                K [ i ] [ w ] = 0
            elif wt [ i - 1 ] <= w :
                K [ i ] [ w ] = max ( val [ i - 1 ] + K [ i - 1 ] [ w - wt [ i - 1 ] ] , K [ i - 1 ] [ w ] )
            else :
                K [ i ] [ w ] = K [ i - 1 ] [ w ]
    return K [ n ] [ W ]
|||

PROGRAM_DECIMAL_OCTAL_CONVERSION

def dec_to_oct ( n ) :
    octal_num = [ ]
    i = 0
    while n != 0 :
        octal_num.append ( n % 8 )
        n = n // 8
        i += 1
    for j in range ( i - 1 , - 1 , - 1 ) :
        print ( octal_num [ j ] )
|||

SUBSEQUENCES_SIZE_THREE_ARRAY_WHOSE_SUM_DIVISIBLE_M_1

def count_subseq ( A , N , M ) :
    ans = 0
    h = [ 0 ] * M
    h [ A [ i ] % M ] += 1
    for i in range ( N ) :
        A [ i ] = A [ i ] % M
        h [ A [ i ] ] += 1
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
    return ans
|||

COUNT_FIBONACCI_NUMBERS_GIVEN_RANGE_LOG_TIME

def count_fibs ( low , high ) :
    f1 , f2 , f3 = 0 , 1 , 1
    result = 0
    while f1 <= high :
        if f1 >= low :
            result += 1
        f1 , f2 , f3 = f2 , f3 , f1 + f2
    return result
|||

FIND_WHETHER_A_GIVEN_NUMBER_IS_A_POWER_OF_4_OR_NOT_1

def isPowerOfFour ( n ) :
    count = 0
    x = n & ( n - 1 )
    if n and x == 0 :
        while n > 1 :
            n >>= 1
            count += 1
        return ( count % 2 == 0 )
|||

FIND_SUM_EVEN_FACTORS_NUMBER

def sumof_factors ( n ) :
    if n % 2 != 0 :
        return 0
    res = 1
    for i in range ( 2 , math.sqrt ( n ) ) :
        count , curr_sum = 0 , 1
        curr_term = 1
        while n % i == 0 :
            count += 1
            n = n // i
            if i == 2 and count == 1 :
                curr_sum = 0
            curr_term *= i
            curr_sum += curr_term
        res *= curr_sum
    if n >= 2 :
        res *= ( 1 + n )
    return res
|||

FIND_SUM_NON_REPEATING_DISTINCT_ELEMENTS_ARRAY

def find_sum ( arr , n ) :
    sum = 0
    s = set ( )
    for i in range ( n ) :
        if not s.issubset ( arr [ i ] ) :
            sum += arr [ i ]
            s.add ( arr [ i ] )
    return sum
|||

DYNAMIC_PROGRAMMING_SET_17_PALINDROME_PARTITIONING_1

def minPalPartion ( str ) :
    n = len ( str )
    C = [ [ ] for i in range ( n ) ]
    P = [ [ ] for i in range ( n ) ]
    i , j , k , L = 0 , 0 , 0 , 0
    for i in range ( n ) :
        P [ i ] [ i ] = True
    for L in range ( 2 , n + 1 ) :
        for i in range ( n - L + 1 ) :
            j = i + L - 1
            if L == 2 :
                P [ i ] [ j ] = ( str [ i ] == str [ j ] )
            else :
                P [ i ] [ j ] = ( str [ i ] == str [ j ] ) and P [ i + 1 ] [ j - 1 ]
    for i in range ( n ) :
        if P [ 0 ] [ i ] == True :
            C [ i ] = 0
        else :
            C [ i ] = int ( P [ i ] [ j ] )
            for j in range ( i ) :
                if P [ j + 1 ] [ i ] == True and 1 + C [ j ] < C [ i ] :
                    C [ i ] = 1 + C [ j ]
    return C [ n - 1 ]
|||

MINIMUM_POSITIVE_POINTS_TO_REACH_DESTINATION

def min_initial_points ( points , R , C ) :
    dp = [ 0 ] * R
    m , n = R , C
    dp [ m - 1 ] [ n - 1 ] = points [ m - 1 ] [ n - 1 ] > 0
    for i in range ( m - 2 , - 1 , - 1 ) :
        dp [ i ] [ n - 1 ] = max ( dp [ i + 1 ] [ n - 1 ] - points [ i ] [ n - 1 ] , 1 )
    for j in range ( n - 2 , - 1 , - 1 ) :
        dp [ m - 1 ] [ j ] = max ( dp [ m - 1 ] [ j + 1 ] - points [ m - 1 ] [ j ] , 1 )
    for i in range ( m - 2 , - 1 , - 1 ) :
        for j in range ( n - 2 , - 1 , - 1 ) :
            min_points_on_exit = min ( dp [ i + 1 ] [ j ] , dp [ i ] [ j + 1 ] )
            dp [ i ] [ j ] = max ( min_points_on_exit - points [ i ] [ j ] , 1 )
    return dp [ 0 ] [ 0 ]
|||

COUNT_OF_PAIRS_SATISFYING_THE_GIVEN_CONDITION

def count_pair ( a , b ) :
    s = str ( b )
    i = 0
    for c in s :
        if c != '9' :
            break
    result = 0
    if i == len ( s ) :
        result = a * len ( s )
    else :
        result = a * ( len ( s ) - 1 )
    return result
|||

SURVIVAL

def survival ( S , N , M ) :
    if ( ( N * 6 ) < ( M * 7 ) and S > 6 ) or M > N :
        print ( "No" )
    else :
        days = ( M * S ) / N
        if ( ( M * S ) % N ) != 0 :
            days += 1
        print ( "Yes " + str ( days ) )
|||

INTERLEAVE_FIRST_HALF_QUEUE_SECOND_HALF

def interleave_queue ( q ) :
    if len ( q ) % 2 != 0 :
        print ( "Input even number of integers." )
    s = Stack ( )
    half_size = len ( q ) // 2
    for i in range ( half_size ) :
        s.push ( q.pop ( ) )
        q.pop ( )
    while not s.empty ( ) :
        q.push ( s.pop ( ) )
        s.pop ( )
    for i in range ( half_size ) :
        q.push ( q.pop ( ) )
        q.pop ( )
    for i in range ( half_size ) :
        s.push ( q.pop ( ) )
        q.pop ( )
    while not s.empty ( ) :
        q.push ( s.pop ( ) )
        s.pop ( )
        q.push ( q.pop ( ) )
        q.pop ( )
|||

INTEGER_POSITIVE_VALUE_POSITIVE_NEGATIVE_VALUE_ARRAY_1

def find_integer ( arr , n ) :
    neg , pos = 0 , 0
    sum = 0
    for i in range ( n ) :
        sum += arr [ i ]
        if arr [ i ] < 0 :
            neg += 1
        else :
            pos += 1
    return ( sum / abs ( neg - pos ) )
|||

FIND_SUM_EVEN_INDEX_BINOMIAL_COEFFICIENTS

def evenSum ( n ) :
    C = [ [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n
|||

DELANNOY_NUMBER

def dealnnoy ( n , m ) :
    if m == 0 or n == 0 :
        return 1
    return dealnnoy ( m - 1 , n ) + dealnnoy ( m - 1 , n - 1 ) + dealnnoy ( m , n - 1 )
|||

FIND_THE_LARGEST_SUBARRAY_WITH_0_SUM

def max_len ( arr , n ) :
    max_len = 0
    for i in range ( n ) :
        curr_sum = 0
        for j in range ( i , n ) :
            curr_sum += arr [ j ]
            if curr_sum == 0 :
                max_len = max ( max_len , j - i + 1 )
    return max_len
|||

NEXT_POWER_OF_2

def next_power_of_2 ( n ) :
    count = 0
    if n and ( n & ( n - 1 ) ) == 0 :
        return n
    while n != 0 :
        n >>= 1
        count += 1
    return 1 << count
|||

LONGEST_GEOMETRIC_PROGRESSION

def lenOfLongestGP ( set , n ) :
    if n < 2 :
        return n
    if n == 2 :
        return ( set [ 1 ] % set [ 0 ] == 0 )
    set.sort ( )
    L = [ [ 0 ] * n for i in range ( n ) ]
    llgp = 1
    for i in range ( n ) :
        if set [ n - 1 ] % set [ i ] == 0 :
            L [ i ] [ n - 1 ] = 2
        else :
            L [ i ] [ n - 1 ] = 1
    for j in range ( n - 2 , - 1 , - 1 ) :
        i = j - 1 , j + 1
        while i >= 0 and k <= n - 1 :
            if set [ i ] * set [ k ] < set [ j ] * set [ j ] :
                k += 1
            elif set [ i ] * set [ k ] > set [ j ] * set [ j ] :
                if set [ j ] % set [ i ] == 0 :
                    L [ i ] [ j ] = 2
                else :
                    L [ i ] [ j ] = 1
                del L [ i ] [ j ]
            else :
                L [ i ] [ j ] = L [ j ] [ k ] + 1
                if L [ i ] [ j ] > llgp :
                    llgp = L [ i ] [ j ]
                del L [ i ] [ j ]
                del L [ i ] [ k ]
        while i >= 0 :
            if set [ j ] % set [ i ] == 0 :
                L [ i ] [ j ] = 2
            else :
                L [ i ] [ j ] = 1
            del L [ i ] [ j ]
    return llgp
|||

DYNAMIC_PROGRAMMING_SET_6_MIN_COST_PATH

def _min_cost ( cost , m , n ) :
    i , j = 0 , 0
    tc = [ [ 0 ] * m + [ n + 1 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m ]
    return tc
|||

PROGRAM_DISTANCE_TWO_POINTS_EARTH

def distance ( lat1 , lat2 , lon1 , lon2 ) :
    lon1 = math.radians ( lon1 )
    lon2 = math.radians ( lon2 )
    lat1 = math.radians ( lat1 )
    lat2 = math.radians ( lat2 )
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.pow ( math.sin ( dlat / 2 ) , 2 ) + math.cos ( lat1 ) * math.cos ( lat2 ) * math.pow ( math.sin ( dlon / 2 ) , 2 )
    c = 2 * math.asin ( math.sqrt ( a ) )
    r = 6371
    return ( c * r )
|||

BIN_PACKING_PROBLEM_MINIMIZE_NUMBER_OF_USED_BINS

def next_fit ( weight , n , c ) :
    res , bin_rem = 0 , c
    for i in range ( n ) :
        if weight [ i ] > bin_rem :
            res += 1
            bin_rem = c - weight [ i ]
        else :
            bin_rem -= weight [ i ]
    return res , bin_rem
|||

FIND_SUBARRAY_WITH_GIVEN_SUM_1

def subArraySum ( arr , n , sum ) :
    curr_sum , start = arr [ 0 ] , 0 , 0
    for i in range ( 1 , n + 1 ) :
        while curr_sum > sum and start < i - 1 :
            curr_sum = curr_sum - arr [ start ]
            start += 1
        if curr_sum == sum :
            p = i - 1
            print ( "Sum found between indexes " + str ( start ) + " and " + str ( p ) )
            return 1
        if i < n :
            curr_sum = curr_sum + arr [ i ]
    print ( "No subarray found" )
    return 0
|||

SPACE_OPTIMIZED_DP_SOLUTION_0_1_KNAPSACK_PROBLEM_1

def KnapSack ( val , wt , n , W ) :
    dp = np.zeros ( ( W + 1 , ) )
    dp [ 0 ] = 0
    for i in range ( n ) :
        for j in range ( W , j >= wt [ i ] ) :
            dp [ j ] = max ( dp [ j ] , val [ i ] + dp [ j - wt [ i ] ] )
    return dp [ W ]
|||

FIND_VALUE_OF_Y_MOD_2_RAISED_TO_POWER_X

def yMod ( y , x ) :
    if ( math.log ( y ) / math.log ( 2 ) ) < x : return y
    if x > 63 : return y
    return ( y % ( 1 << int ( x ) ) )
|||

SUM_SERIES_23_45_67_89_UPTO_N_TERMS

def series_sum ( n ) :
    i = 1
    res = 0.0
    sign = True
    while n > 0 :
        n -= 1
        if sign :
            sign = not sign
            res = res + float ( yield i ) / yield i
        else :
            sign = not sign
            res = res - float ( yield i ) / yield i
    return res
|||

LENGTH_LONGEST_STRICT_BITONIC_SUBSEQUENCE

def long_len_strict_bitonic_sub ( arr , n ) :
    inc = { }
    dcr = { }
    len_inc = [ ]
    len_dcr = [ ]
    long_len = 0
    for i in range ( n ) :
        len = 0
        if inc.has_key ( arr [ i ] - 1 ) :
            len = inc [ arr [ i ] - 1 ]
        len_inc.append ( len + 1 )
        inc [ arr [ i ] ] = len_inc [ i ]
    for i in range ( n - 1 , - 1 , - 1 ) :
        len = 0
        if dcr.has_key ( arr [ i ] - 1 ) :
            len = dcr [ arr [ i ] - 1 ]
        len_dcr.append ( len + 1 )
        dcr [ arr [ i ] ] = len_dcr [ i ]
    for i in range ( n ) :
        if long_len < ( len_inc + len_dcr [ i ] - 1 ) :
            long_len = len_inc [ i ] + len_dcr [ i ] - 1
    return long_len
|||

MAXIMUM_DISTANCE_TWO_OCCURRENCES_ELEMENT_ARRAY

def max_distance ( arr , n ) :
    d = { }
    max_dist = 0
    for i in range ( n ) :
        if not d.has_key ( arr [ i ] ) :
            d [ arr [ i ] ] = i
        else :
            max_dist = max ( max_dist , i - d [ arr [ i ] ] )
    return max_dist
|||

FIND_RECTANGLE_BINARY_MATRIX_CORNERS_1_1

def isRectangle ( matrix ) :
    rows = len ( matrix )
    if rows == 0 :
        return False
    columns = len ( matrix [ 0 ] )
    table = { }
    for i in range ( rows ) :
        for j in range ( columns - 1 ) :
            for k in range ( j + 1 , columns ) :
                if matrix [ i ] [ j ] == 1 and matrix [ i ] [ k ] == 1 :
                    if table.has_key ( j ) and table [ j ].has_key ( k ) :
                        return True
                    if table.has_key ( k ) and table [ k ].has_key ( j ) :
                        return True
                    if not table.has_key ( j ) :
                        x = set ( [ k ] )
                        table [ j ].add ( x )
                    else :
                        table [ j ].add ( k )
                    if not table.has_key ( k ) :
                        x = set ( [ j ] )
                        table [ k ].add ( x )
                    else :
                        table [ k ].add ( j )
    return False
|||

COUNT_MINIMUM_NUMBER_SUBSETS_SUBSEQUENCES_CONSECUTIVE_NUMBERS

def numofsubset ( arr , n ) :
    arr.sort ( )
    count = 1
    for i in range ( n - 1 ) :
        if arr [ i ] + 1 != arr [ i + 1 ] :
            count += 1
    return count
|||

LARGEST_SUM_CONTIGUOUS_SUBARRAY

def max_subarray_sum ( a ) :
    size = len ( a )
    max_so_far , max_ending_here = int ( a [ 0 ] ) , 0
    for i in range ( size ) :
        max_ending_here = max_ending_here + a [ i ]
        if max_so_far < max_ending_here :
            max_so_far , max_ending_here = max_ending_here , max_ending_here
        if max_ending_here < 0 :
            max_ending_here , max_ending_here = 0 , 0
    return max_so_far , max_ending_here
|||

PROGRAM_TO_FIND_REMAINDER_WITHOUT_USING_MODULO_OR_OPERATOR_2

def getRemainder ( num , divisor ) :
    while num >= divisor :
        num -= divisor
    return num
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
|||

FIND_THE_ELEMENT_THAT_APPEARS_ONCE_1

def getSingle ( arr , n ) :
    result = 0
    x , sum = 0 , 0
    for i in range ( INT_SIZE ) :
        sum = 0
        x = ( 1 << i )
        for j in range ( n ) :
            if ( arr [ j ] & x ) == 0 :
                sum += 1
        if ( sum % 3 ) == 0 :
            result |= x
    return result
|||

NUMBER_RECTANGLES_NM_GRID

def rectCount ( n , m ) :
    return ( m * n * ( n + 1 ) * ( m + 1 ) ) / 4
|||

MAXIMUM_POINTS_INTERSECTION_N_CIRCLES

def intersection ( n ) :
    return n * ( n - 1 )
|||

ADD_1_TO_A_GIVEN_NUMBER

def f_gold ( x ) :
    m = 1
    while int ( x & m ) >= 1 :
        x = x ^ m
        m <<= 1
    x = x ^ m
    return x
|||

ADD_TWO_NUMBERS_WITHOUT_USING_ARITHMETIC_OPERATORS

def f_gold ( x , y ) :
    while y != 0 :
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x
|||

AREA_OF_THE_CIRCLE_THAT_HAS_A_SQUARE_AND_A_CIRCLE_INSCRIBED_IN_IT

def f_gold ( a ) :
    area = float ( math.pi * a ** 2 ) / 4
    return area
|||

ARRAY_RANGE_QUERIES_ELEMENTS_FREQUENCY_VALUE

def f_gold ( start , end , arr ) :
    mp = { }
    for i in range ( start , end + 1 ) :
        mp [ arr [ i ] ] = mp [ arr [ i ] ] if i in mp else 1
    count = 0
    for key , value in mp.items ( ) :
        if key == arr [ i ] :
            count += 1
    return count
|||

BELL_NUMBERS_NUMBER_OF_WAYS_TO_PARTITION_A_SET

def f_gold ( n ) :
    bell = [ 1 for i in range ( n + 1 ) ]
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
        if arr [ mid ] > x :
            return f_gold ( arr , l , mid - 1 , x )
        return f_gold ( arr , mid + 1 , r , x )
|||

BREAK_NUMBER_THREE_PARTS_1

def f_gold ( n ) :
    count = 0
    count = ( n + 1 ) * ( n + 2 ) / 2
    return count
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
|||

CALCULATE_MAXIMUM_VALUE_USING_SIGN_TWO_NUMBERS_STRING

def f_gold ( str ) :
    res = str [ 0 ] - '0'
    for c in str [ 1 : ] :
        if c == '0' or c == '1' or res < 2 :
            res += ( c - '0' )
        else :
            res *= ( c - '0' )
    return res
|||

CALCULATE_VOLUME_DODECAHEDRON

def f_gold ( side ) :
    return ( ( ( 15 + ( 7 * ( math.sqrt ( 5 ) ) ) ) / 4 ) ** ( math.pow ( side , 3 ) ) )
|||

CEILING_IN_A_SORTED_ARRAY

def f_gold ( arr , low , high , x ) :
    i = 0
    if x <= arr [ low ] :
        return low
    for i in range ( low , high ) :
        if arr [ i ] == x :
            return i
        if arr [ i ] < x and arr [ i + 1 ] >= x :
            return i + 1
    return - 1
|||

CEILING_IN_A_SORTED_ARRAY_1

def f_gold ( arr , low , high , x ) :
    mid = 0
    if x <= arr [ low ] :
        return low
    if x > arr [ high ] :
        return - 1
    mid = ( low + high ) // 2
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
    diag1_left , diag1_right = 0 , 0
    diag2_left , diag2_right = 0 , 0
    for i , j in enumerate ( n - 1 ) :
        if i < n / 2 :
            diag1_left += mat [ i ] [ i ]
            diag2_left += mat [ j ] [ i ]
        elif i > n / 2 :
            diag1_right += mat [ i ] [ i ]
            diag2_right += mat [ j ] [ i ]
    return ( diag1_left , diag2_right , diag2_left , diag1_right , diag2_left , diag2_right , mat [ n / 2 ] [ n / 2 ] )
|||

CHANGE_BITS_CAN_MADE_ONE_FLIP

def f_gold ( str ) :
    zeros , ones = 0 , 0
    for ch in str :
        if ch == '0' :
            zeros += 1
        else :
            ones += 1
    return ( zeros == 1 or ones == 1 )
|||

CHECK_ARRAY_CONTAINS_CONTIGUOUS_INTEGERS_DUPLICATES_ALLOWED

def f_gold ( arr , n ) :
    max = int ( arr [ 0 ] )
    min = int ( arr [ 1 ] )
    for i in range ( n ) :
        max = max ( max , arr [ i ] )
        min = min ( min , arr [ i ] )
    m = max - min + 1
    if m > n :
        return False
    visited = [ ]
    for i in range ( n ) :
        visited.append ( arr [ i ] - min )
    for i in range ( m ) :
        if visited [ i ] == False :
            return False
    return True
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
|||

CHECK_IF_A_NUMBER_IS_JUMBLED_OR_NOT

def f_gold ( num ) :
    if num / 10 == 0 :
        return True
    while num != 0 :
        if num / 10 == 0 :
            return True
        digit1 = num % 10
        digit2 = ( num / 10 ) % 10
        if abs ( digit2 - digit1 ) > 1 :
            return False
        num = num / 10
    return True
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
                ten_count -= 1
            elif five_count >= 3 :
                five_count -= 3
            else :
                return 0
    return 1
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
|||

CHECK_LINE_PASSES_ORIGIN

def f_gold ( x1 , y1 , x2 , y2 ) :
    return ( x1 * ( y2 - y1 ) == y1 * ( x2 - x1 ) )
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
|||

CHECK_POSSIBLE_TRANSFORM_ONE_STRING_ANOTHER

def f_gold ( s1 , s2 ) :
    n = len ( s1 )
    m = len ( s2 )
    dp = [ False for i in range ( n + 1 ) ]
    for i in range ( 0 , n + 1 ) :
        for j in range ( 0 , m + 1 ) :
            dp [ i ] [ j ] = False
    dp [ 0 ] [ 0 ] = True
    for i in range ( 0 , len ( s1 ) ) :
        for j in range ( 0 , len ( s2 ) ) :
            if dp [ i ] [ j ] :
                if j < len ( s2 ) and ( ord ( s1 [ i ] ) == ord ( s2 [ j ] ) ) :
                    dp [ i + 1 ] [ j + 1 ] = True
                if not ord ( s1 [ i ] ) :
                    dp [ i + 1 ] [ j ] = True
    return ( dp [ n ] [ m ] )
|||

CHECK_REVERSING_SUB_ARRAY_MAKE_ARRAY_SORTED

def f_gold ( arr , n ) :
    temp = [ arr [ i ] for i in range ( n ) ]
    temp.sort ( )
    front = 0
    for front in temp :
        if temp [ front ] != arr [ front ] :
            break
    back = 0
    for back in temp :
        if temp [ back ] != arr [ back ] :
            break
    if front >= back :
        return True
    do :
        front += 1
        if arr [ front - 1 ] < arr [ front ] :
            return False
    while front != back :
        return True
    return False
|||

CHECK_REVERSING_SUB_ARRAY_MAKE_ARRAY_SORTED_1

def f_gold ( arr , n ) :
    if n == 1 :
        return True
    i = 0
    for i in range ( 1 , arr [ i - 1 ] < arr [ i ] , i ) :
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
    return res
|||

CHECK_WHETHER_GIVEN_NUMBER_EVEN_ODD_1

def f_gold ( n ) :
    if ( n & 1 ) == 0 :
        return True
    else :
        return False
|||

CHECK_WHETHER_TWO_STRINGS_ARE_ANAGRAM_OF_EACH_OTHER

def f_gold ( str1 , str2 ) :
    n1 = len ( str1 )
    n2 = len ( str2 )
    if n1 != n2 :
        return False
    str1 = sorted ( str1 )
    str2 = sorted ( str2 )
    for i in range ( n1 ) :
        if str1 [ i ] != str2 [ i ] :
            return False
    return True
|||

CHOCOLATE_DISTRIBUTION_PROBLEM

def f_gold ( arr , n , m ) :
    if m == 0 or n == 0 :
        return 0
    arr.sort ( )
    if n < m :
        return - 1
    min_diff = sys.maxint
    first , last = 0 , 0
    for i in range ( 0 , i + m - 1 , n ) :
        diff = arr [ i + m - 1 ] - arr [ i ]
        if diff < min_diff :
            min_diff = diff
            first = i
            last = i + m - 1
    return ( arr [ last ] - arr [ first ] )
|||

CIRCLE_LATTICE_POINTS

def f_gold ( r ) :
    if r <= 0 :
        return 0
    result = 4
    for x in range ( 1 , r ) :
        y_square = r ** 2 - x ** 2
        y = int ( math.sqrt ( y_square ) )
        if y * y == y_square :
            result += 4
    return result
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
|||

COMPUTE_NCR_P_SET_1_INTRODUCTION_AND_DYNAMIC_PROGRAMMING_SOLUTION

def f_gold ( n , r , p ) :
    C = np.zeros ( ( r + 1 , ) )
    C [ 0 ] = 1
    for i in range ( 1 , n + 1 ) :
        for j in range ( min ( i , r ) , 0 , - 1 ) :
            C [ j ] = ( C [ j ] + C [ j - 1 ] ) % p
    return C [ r ]
|||

COUNT_ARRAYS_CONSECUTIVE_ELEMENT_DIFFERENT_VALUES

def f_gold ( n , k , x ) :
    dp = [ 0 ] * 109
    dp [ 0 ] = 1
    for i in range ( 2 , n ) :
        dp [ i ] = ( k - 2 ) * dp [ i - 1 ] + ( k - 1 ) * dp [ i - 2 ]
    return ( x == 1 and ( k - 1 ) * dp [ n - 2 ] or dp [ n - 1 ] )
|||

COUNT_DIGITS_FACTORIAL_SET_1

def f_gold ( n ) :
    if n < 0 :
        return 0
    if n <= 1 :
        return 1
    digits = 0
    for i in range ( 2 , n + 1 ) :
        digits += math.log10 ( i )
    return int ( math.floor ( digits ) ) + 1
|||

COUNT_ENTRIES_EQUAL_TO_X_IN_A_SPECIAL_MATRIX

def f_gold ( n , x ) :
    f_gold = 0
    for i in range ( 1 , n + 1 ) :
        if x / i <= n and x % i == 0 :
            f_gold += 1
    return f_gold
|||

COUNT_FACTORIAL_NUMBERS_IN_A_GIVEN_RANGE

def f_gold ( low , high ) :
    fact , x = 1 , 1
    while fact < low :
        fact , x = fact * x , x + 1
    res = 0
    while fact <= high :
        res += 1
        fact , x = fact * x , x + 1
    return res
|||

COUNT_FREQUENCY_K_MATRIX_SIZE_N_MATRIXI_J_IJ

def f_gold ( n , k ) :
    if n + 1 >= k :
        return ( k - 1 )
    else :
        return ( 2 * n + 1 - k )
|||

COUNT_INDEX_PAIRS_EQUAL_ELEMENTS_ARRAY

def f_gold ( arr , n ) :
    ans = 0
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if arr [ i ] == arr [ j ] :
                ans += 1
    return ans
|||

COUNT_NUMBER_OF_SOLUTIONS_OF_X2_1_MOD_P_IN_GIVEN_RANGE

def f_gold ( n , p ) :
    ans = 0
    for x in range ( 1 , p ) :
        if ( x ** 2 ) % p == 1 :
            last = x + p * ( n // p )
        else :
            last -= p
        ans += ( ( last - x ) // p + 1 )
    return ans
|||

COUNT_NUMBER_OF_WAYS_TO_COVER_A_DISTANCE_1

def f_gold ( dist ) :
    count = [ 1 , 1 , 2 ]
    for i in range ( 3 , dist + 1 ) :
        count.append ( count [ i - 1 ] + count [ i - 2 ] + count [ i - 3 ] )
    return count [ dist ]
|||

COUNT_NUMBER_OF_WAYS_TO_FILL_A_N_X_4_GRID_USING_1_X_4_TILES

def f_gold ( n ) :
    dp = [ 0 ] * ( n + 1 )
    dp [ 0 ] = 0
    for i in range ( 1 , n + 1 ) :
        if i >= 1 and i <= 3 :
            dp [ i ] = 1
        elif i == 4 :
            dp [ i ] = 2
        else :
            dp [ i ] = dp [ i - 1 ] + dp [ i - 4 ]
    return dp [ n ]
|||

COUNT_OF_OCCURRENCES_OF_A_101_PATTERN_IN_A_STRING

def f_gold ( str ) :
    len ( str )
    one_seen = False
    count = 0
    for char in str :
        if char == '1' and one_seen == True :
            if char [ - 1 ] == '0' :
                count += 1
        if char == '1' and one_seen == False :
            one_seen = True
        if char != '0' and char != '1' :
            one_seen = False
    return count
|||

COUNT_PAIRS_DIFFERENCE_EQUAL_K

def f_gold ( arr , n , k ) :
    count = 0
    for i in range ( n ) :
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
            if ( arr1 [ i ] + arr2 [ j ] ) == x :
                count += 1
    return count
|||

COUNT_PALINDROMIC_SUBSEQUENCE_GIVEN_STRING

def f_gold ( str ) :
    N = len ( str )
    cps = [ 1 for i in range ( N + 1 ) ]
    for L in range ( 2 , N + 1 ) :
        for i in range ( N ) :
            k = L + i - 1
            if k < N :
                if str [ i ] == str [ k ] :
                    cps [ i ] [ k ] = cps [ i ] [ k - 1 ] + cps [ i + 1 ] [ k ] + 1
                else :
                    cps [ i ] [ k ] = cps [ i ] [ k - 1 ] + cps [ i + 1 ] [ k ] - cps [ i + 1 ] [ k - 1 ]
    return cps [ 0 ] [ N - 1 ]
|||

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX_2

def f_gold ( m , n ) :
    dp = np.zeros ( ( n , m ) )
    dp [ 0 ] = 1
    for i in range ( m ) :
        for j in range ( 1 , n ) :
            dp [ j ] += dp [ j - 1 ]
    return dp [ n - 1 ]
|||

COUNT_SET_BITS_IN_AN_INTEGER_2

def f_gold ( n ) :
    count = 0
    while n > 0 :
        n &= ( n - 1 )
        count += 1
    return count
|||

COUNT_SET_BITS_IN_AN_INTEGER_3

def f_gold ( n ) :
    if n == 0 :
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
        if j == c - 1 :
            result += 1
    for i in range ( r ) :
        j = 0
        for j in range ( c - 1 , 0 , - 1 ) :
            if mat [ i ] [ j - 1 ] <= mat [ i ] [ j ] :
                break
        if c > 1 and j == 0 :
            result += 1
    return result
|||

COUNT_STRINGS_CAN_FORMED_USING_B_C_GIVEN_CONSTRAINTS_1

def f_gold ( n ) :
    return 1 + ( n ** 2 ) + ( n * ( ( n ** 2 ) - 1 ) / 2 )
|||

COUNT_SUBARRAYS_EQUAL_NUMBER_1S_0S

def f_gold ( arr , n ) :
    um = { }
    curr_sum = 0
    for i in range ( n ) :
        curr_sum += ( arr [ i ] == 0 )
        um [ curr_sum ] = um [ curr_sum ] if curr_sum != 0 else 1
    count = 0
    for itr , val in um.items ( ) :
        if val > 1 :
            count += ( ( val * ( val - 1 ) ) / 2 )
    if um.has_key ( 0 ) :
        count += um [ 0 ]
    return count
|||

COUNT_SUBARRAYS_EQUAL_NUMBER_1S_0S_1

def f_gold ( arr , n ) :
    mydict = { }
    sum = 0
    count = 0
    for i in range ( n ) :
        if arr [ i ] == 0 :
            arr [ i ] = - 1
        sum += arr [ i ]
        if sum == 0 :
            count += 1
        if mydict.has_key ( sum ) :
            count += mydict [ sum ]
        if not mydict.has_key ( sum ) :
            mydict [ sum ] = 1
        else :
            mydict [ sum ] = mydict [ sum ] + 1
    return count
|||

COUNT_SUBARRAYS_TOTAL_DISTINCT_ELEMENTS_ORIGINAL_ARRAY

def f_gold ( arr , n ) :
    vis = { }
    for key in arr :
        vis [ arr [ key ] ] = 1
    k = len ( vis )
    vis.clear ( )
    ans , right , window = 0 , 0 , 0
    for left in range ( n ) :
        while right < n and window < k :
            vis [ arr [ right ] ] = vis [ arr [ right ] ] + 1
            if vis [ arr [ right ] ] == 1 :
                window += 1
            right += 1
        if window == k :
            ans += ( n - right + 1 )
        vis [ arr [ left ] ] = vis [ arr [ left ] ] - 1
        if vis [ arr [ left ] ] == 0 :
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
        if ( arr [ i ] & 1 ) == 1 :
            difference += 1
        else :
            difference -= 1
        if difference < 0 :
            ans += hash_negative [ - difference ]
            hash_negative [ - difference ] += 1
        else :
            ans += hash_positive [ difference ]
            hash_positive [ difference ] += 1
    return ans
|||

COUNT_SUBSTRINGS_WITH_SAME_FIRST_AND_LAST_CHARACTERS

def f_gold ( s ) :
    result = 0
    n = len ( s )
    for i in range ( n ) :
        for j in range ( i , n ) :
            if s [ i ] == s [ j ] :
                result += 1
    return result
|||

COUNT_SUM_OF_DIGITS_IN_NUMBERS_FROM_1_TO_N

def f_gold ( n ) :
    if n < 10 :
        return ( n * ( n + 1 ) / 2 )
    d = int ( math.log10 ( n ) )
    a = [ 0 ] * ( d + 1 )
    a [ 0 ] = 45
    for i in range ( 2 , d + 1 ) :
        a [ i ] = a [ i - 1 ] * 10 + 45 * int ( math.ceil ( math.pow ( 10 , i - 1 ) ) )
    p = int ( math.ceil ( math.pow ( 10 , d ) ) )
    msd = n / p
    return ( msd * a [ d ] + ( msd * ( msd - 1 ) / 2 ) * p + msd * ( 1 + n % p ) + f_gold ( n % p ) )
|||

COUNT_WAYS_DIVIDE_CIRCLE_USING_N_NON_INTERSECTING_CHORDS

def f_gold ( A ) :
    n = 2 * A
    dpArray = [ 1 ] * n + [ 1 ] * n
    for i in range ( 4 , n + 1 , 2 ) :
        for j in range ( 0 , i - 1 , 2 ) :
            dpArray [ i ] += ( dpArray [ j ] * dpArray [ i - 2 - j ] )
    return dpArray [ n ]
|||

COUNT_WORDS_APPEAR_EXACTLY_TWO_TIMES_ARRAY_WORDS

def f_gold ( str , n ) :
    m = { }
    for i in range ( n ) :
        if m.has_key ( str [ i ] ) :
            get = m [ str [ i ] ]
            m [ str [ i ] ] = get + 1
        else :
            m [ str [ i ] ] = 1
    res = 0
    for key , value in m.items ( ) :
        if value == 2 :
            res += 1
    return res
|||

C_PROGRAM_FACTORIAL_NUMBER_1

def f_gold ( n ) :
    res , i = 1 , 0
    for i in range ( 2 , n + 1 ) :
        res *= i
    return res
|||

C_PROGRAM_FACTORIAL_NUMBER_2

def f_gold ( n ) :
    return ( n == 1 or n == 0 )
|||

C_PROGRAM_FIND_LARGEST_ELEMENT_ARRAY_1

def f_gold ( arr , n ) :
    arr.sort ( )
    return arr [ n - 1 ]
|||

DECODE_MEDIAN_STRING_ORIGINAL_STRING

def f_gold ( s ) :
    l = len ( s )
    s1 = ""
    is_even = ( l % 2 == 0 )
    for i in range ( 0 , l , 2 ) :
        if is_even :
            s1 = s [ i ] + s1
            s1 += s [ i + 1 ]
        else :
            if l - i > 1 :
                s1 += s [ i ]
                s1 = s [ i + 1 ] + s1
            else :
                s1 += s [ i ]
    return s1
|||

DIAGONALLY_DOMINANT_MATRIX

def f_gold ( m , n ) :
    for i in range ( n ) :
        sum = 0
        for j in range ( n ) :
            sum += abs ( m [ i ] [ j ] )
        sum -= abs ( m [ i ] [ i ] )
        if abs ( m [ i ] [ i ] ) < sum :
            return False
    return True
|||

DICE_THROW_PROBLEM

def f_gold ( m , n , x ) :
    table = [ [ 0 ] * ( n + 1 ) + [ x + 1 ] * ( n + 1 ) for x in range ( 1 , m + 1 ) ]
    for j in range ( 1 , x + 1 ) :
        table [ 1 ] [ j ] = 1
    for i in range ( 2 , n + 1 ) :
        for j in range ( 1 , x + 1 ) :
            for k in range ( 1 , j + 1 ) and k <= m :
                table [ i ] [ j ] += table [ i - 1 ] [ j - k ]
    return table [ n ] [ x ]
|||

DICE_THROW_PROBLEM_1

def f_gold ( f , d , s ) :
    mem = [ 1 ] * ( d + 1 )
    mem [ 0 ] [ 0 ] = 1
    for i in range ( 1 , d + 1 ) :
        for j in range ( i , s + 1 ) :
            mem [ i ] [ j ] = mem [ i ] [ j - 1 ] + mem [ i - 1 ] [ j - 1 ]
            if j - f - 1 >= 0 :
                mem [ i ] [ j ] -= mem [ i - 1 ] [ j - f - 1 ]
    return mem [ d ] [ s ]
|||

DIFFERENCE_BETWEEN_HIGHEST_AND_LEAST_FREQUENCIES_IN_AN_ARRAY

def f_gold ( arr , n ) :
    arr.sort ( )
    count , max_count , min_count = 0 , 0 , n
    for i in range ( ( n - 1 ) ) :
        if arr [ i ] == arr [ i + 1 ] :
            count += 1
            continue
        else :
            max_count = max ( max_count , count )
            min_count = min ( min_count , count )
            count = 0
    return ( max_count - min_count )
|||

DOUBLE_FACTORIAL_1

def f_gold ( n ) :
    res = 1
    for i in range ( n , - 1 , - 1 ) :
        if i == 0 or i == 1 :
            return res
        else :
            res *= i
    return res
|||

DYCK_PATH

def f_gold ( n ) :
    res = 1
    for i in range ( n ) :
        res *= ( 2 ** n - i )
        res /= ( i + 1 )
    return res / ( n + 1 )
|||

DYNAMIC_PROGRAMMING_HIGH_EFFORT_VS_LOW_EFFORT_TASKS_PROBLEM

def f_gold ( high , low , n ) :
    if n <= 0 :
        return 0
    return max ( high [ n - 1 ] + f_gold ( high , low , ( n - 2 ) ) , low [ n - 1 ] + f_gold ( high , low , ( n - 1 ) ) )
|||

DYNAMIC_PROGRAMMING_SET_14_MAXIMUM_SUM_INCREASING_SUBSEQUENCE

def f_gold ( arr , n ) :
    i , j , max = 0 , 0 , 0
    msis = [ ]
    for i in range ( n ) :
        msis.append ( arr [ i ] )
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if arr [ i ] > arr [ j ] and msis [ i ] < msis [ j ] + arr [ i ] :
                msis [ i ] , msis [ j ] = msis [ j ] , msis [ i ]
    for i in range ( n ) :
        if max < msis [ i ] :
            max = msis [ i ]
    return max
|||

DYNAMIC_PROGRAMMING_SET_36_CUT_A_ROPE_TO_MAXIMIZE_PRODUCT_1

def f_gold ( n ) :
    if n == 2 or n == 3 :
        return ( n - 1 )
    res = 1
    while n > 4 :
        n -= 3
        res *= 3
    return ( n * res )
|||

DYNAMIC_PROGRAMMING_SET_37_BOOLEAN_PARENTHESIZATION_PROBLEM

def f_gold ( symb , oper , n ) :
    F = [ ]
    T = [ ]
    for i in range ( n ) :
        F.append ( ( symb [ i ] , symb [ i + 1 ] ) )
        T.append ( ( symb [ i ] , symb [ i + 1 ] ) )
    for gap in range ( 1 , n ) :
        for i , j in zip ( gap , n ) :
            T [ i ] = F [ i ] = 0
            for g in range ( gap ) :
                k = i + g
                tik = T [ i ] + F [ i ] [ k ]
                tkj = T [ k + 1 ] + F [ k + 1 ] [ j ]
                if oper [ k ] == '&' :
                    T [ i ] += T [ i ] * T [ k + 1 ] [ j ]
                    F [ i ] += ( tik * tkj - T [ i ] * T [ k + 1 ] [ j ] )
                if oper [ k ] == '|' :
                    F [ i ] += F [ i ] * F [ k + 1 ] [ j ]
                    T [ i ] += ( tik * tkj - F [ i ] * F [ k + 1 ] [ j ] )
                if oper [ k ] == '^' :
                    T [ i ] += F [ i ] * T [ k + 1 ] [ j ] + T [ i ] * F [ k + 1 ] [ j ]
                    F [ i ] += T [ i ] * T [ k + 1 ] [ j ] + F [ i ] * F [ k + 1 ] [ j ]
    return T [ 0 ] [ n - 1 ]
|||

ELEMENTS_TO_BE_ADDED_SO_THAT_ALL_ELEMENTS_OF_A_RANGE_ARE_PRESENT_IN_ARRAY_1

def f_gold ( arr , n ) :
    s = set ( )
    count , maxm , minm = 0 , int ( min ( arr ) ) , int ( max ( arr ) )
    for i in range ( n ) :
        s.add ( arr [ i ] )
        if arr [ i ] < minm :
            minm = arr [ i ]
        if arr [ i ] > maxm :
            maxm = arr [ i ]
    for i in range ( minm , maxm + 1 ) :
        if not s.add ( i ) :
            count += 1
    return count
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
        ef1 , ef2 = ef2 , ef3
        sum += ef2
    return int ( sum )
|||

FIBONACCI_MODULO_P

def f_gold ( p ) :
    first , second , number , next = 1 , 1 , 2 , 1
    while next > 0 :
        next = ( first + second ) % p
        first , second , number += 1
    return number
|||

FIND_A_FIXED_POINT_IN_A_GIVEN_ARRAY

def f_gold ( arr , n ) :
    i = 0
    for i in range ( n ) :
        if arr [ i ] == i :
            return i
    return - 1
|||

FIND_A_ROTATION_WITH_MAXIMUM_HAMMING_DISTANCE

def f_gold ( arr , n ) :
    brr = [ arr [ i ] for i in range ( 2 * n + 1 ) ]
    for i in range ( n ) :
        brr [ n + i ] = arr [ i ]
    max_ham = 0
    for i in range ( 1 , n ) :
        curr_ham = 0
        for j , k in enumerate ( ( i , n ) ) :
            if brr [ j ] != arr [ k ] :
                curr_ham += 1
        if curr_ham == n :
            return n
        max_ham = max ( max_ham , curr_ham )
    return max_ham
|||

FIND_A_TRIPLET_THAT_SUM_TO_A_GIVEN_VALUE

def f_gold ( A , arr_size , sum ) :
    l , r = A.shape
    for i in range ( arr_size - 2 ) :
        for j in range ( i + 1 , arr_size - 1 ) :
            for k in range ( j + 1 , arr_size ) :
                if A [ i , j , k ] + A [ j , k ] == sum :
                    print ( "Triplet is %d, %d, %d" % ( A [ i , j , k ] , A [ j , k ] ) )
                    return True
    return False
|||

FIND_EXPRESSION_DUPLICATE_PARENTHESIS_NOT

def f_gold ( s ) :
    Stack = Stack ( )
    str = s.split ( )
    for ch in str :
        if ch == ')' :
            top = Stack.top ( )
            Stack.pop ( )
            elementsInside = 0
            while top != '(' :
                elementsInside += 1
                top = Stack.top ( )
                Stack.pop ( )
            if elementsInside < 1 :
                return True
        else :
            Stack.push ( ch )
    return False
|||

FIND_INDEX_GIVEN_FIBONACCI_NUMBER_CONSTANT_TIME_1

def f_gold ( n ) :
    fibo = 2.078087F * float ( math.log ( n , 2 ) ) + 1.672276F
    return round ( fibo , 2 )
|||

FIND_INDEX_OF_AN_EXTRA_ELEMENT_PRESENT_IN_ONE_SORTED_ARRAY

def f_gold ( arr1 , arr2 , n ) :
    for i in range ( n ) :
        if arr1 [ i ] != arr2 [ i ] :
            return i
    return n
|||

FIND_INDEX_OF_AN_EXTRA_ELEMENT_PRESENT_IN_ONE_SORTED_ARRAY_1

def f_gold ( arr1 , arr2 , n ) :
    index = n
    left , right = 0 , n - 1
    while left <= right :
        mid = ( left + right ) // 2
        if arr2 [ mid ] == arr1 [ mid ] :
            left = mid + 1
        else :
            index = mid
            right = mid - 1
    return index
|||

FIND_LARGEST_PRIME_FACTOR_NUMBER

def f_gold ( n ) :
    max_prime = - 1
    while n % 2 == 0 :
        max_prime = 2
        n >>= 1
    for i in range ( 3 , math.sqrt ( n ) , 2 ) :
        while n % i == 0 :
            max_prime = i
            n = n / i
    if n > 2 :
        max_prime = n
    return max_prime
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
            variable = int ( variable * ( i % 10 ) ) % 10
        return variable % 10
|||

FIND_MAXIMUM_PRODUCT_OF_A_TRIPLET_IN_ARRAY

def f_gold ( arr , n ) :
    if n < 3 :
        return - 1
    max_product = int ( '-1' )
    for i in range ( n - 2 ) :
        for j in range ( i + 1 , n - 1 ) :
            for k in range ( j + 1 , n ) :
                max_product = max ( max_product , arr [ i ] * arr [ j ] * arr [ k ] )
    return max_product
|||

FIND_MAXIMUM_SUM_POSSIBLE_EQUAL_SUM_THREE_STACKS

def f_gold ( stack1 , stack2 , stack3 , n1 , n2 , n3 ) :
    sum1 , sum2 , sum3 = 0 , 0 , 0 , 0
    for i in range ( n1 ) :
        sum1 += stack1 [ i ]
    for i in range ( n2 ) :
        sum2 += stack2 [ i ]
    for i in range ( n3 ) :
        sum3 += stack3 [ i ]
    top1 , top2 , top3 = 0 , 0 , 0 , 0
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
|||

FIND_MINIMUM_DIFFERENCE_PAIR_1

def f_gold ( arr , n ) :
    arr.sort ( )
    diff = sys.maxsize
    for i in range ( n - 1 ) :
        if arr [ i + 1 ] - arr [ i ] < diff :
            diff = arr [ i + 1 ] - arr [ i ]
    return diff
|||

FIND_NUMBER_TIMES_STRING_OCCURS_GIVEN_STRING_1

def f_gold ( a , b ) :
    m = len ( a )
    n = len ( b )
    lookup = [ 0 ] * ( m + 1 ) * ( n + 1 )
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
|||

FIND_ONE_EXTRA_CHARACTER_STRING_1

def f_gold ( strA , strB ) :
    res , i = 0 , 0
    for i in range ( len ( strA ) ) :
        res ^= strA [ i ]
    for i in range ( len ( strB ) ) :
        res ^= strB [ i ]
    return ( chr ( res ) , i )
|||

FIND_PERIMETER_CYLINDER

def f_gold ( diameter , height ) :
    return 2 * ( diameter + height )
|||

FIND_REPETITIVE_ELEMENT_1_N_1

def f_gold ( arr , n ) :
    sum = 0
    for i in range ( n ) :
        sum += arr [ i ]
    return sum - ( ( ( n - 1 ) * n ) / 2 )
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
    for i in range ( 3 , math.sqrt ( n ) ) :
        count , curr_sum = 0 , 1
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
    m = { }
    for i in range ( n ) :
        sum = 0
        for j in range ( i , n ) :
            sum += arr [ j ]
            if m.has_key ( sum ) :
                m [ sum ] = m [ sum ] + 1
            else :
                m [ sum ] = 1
    for x , y in m.items ( ) :
        if y == 1 :
            res += x
    return res
|||

FIND_THE_ELEMENT_BEFORE_WHICH_ALL_THE_ELEMENTS_ARE_SMALLER_THAN_IT_AND_AFTER_WHICH_ALL_ARE_GREATER_THAN_IT

def f_gold ( arr , n ) :
    left_max = [ int ( x ) for x in arr ]
    right_min = int ( arr [ - 1 ] )
    for i in range ( 1 , n ) :
        left_max [ i ] = max ( left_max [ i - 1 ] , arr [ i - 1 ] )
    right_min = int ( arr [ - 1 ] )
    for i in range ( n - 1 , - 1 , - 1 ) :
        if left_max [ i ] < arr [ i ] and right_min [ i ] > arr [ i ] :
            return i
        right_min = min ( right_min , arr [ i ] )
    return - 1
|||

FIND_THE_MAXIMUM_ELEMENT_IN_AN_ARRAY_WHICH_IS_FIRST_INCREASING_AND_THEN_DECREASING

def f_gold ( arr , low , high ) :
    max = arr [ low ]
    i = 0
    for i in range ( low , high + 1 ) :
        if arr [ i ] > max :
            max = arr [ i ]
    return max
|||

FIND_THE_MISSING_NUMBER_1

def f_gold ( a , n ) :
    total = 1
    for i in range ( 2 , ( n + 1 ) + 1 ) :
        total += i
        total -= a [ i - 2 ]
    return total
|||

FIND_THE_MISSING_NUMBER_2

def f_gold ( a , n ) :
    x1 = a [ 0 ]
    x2 = 1
    for i in range ( 1 , n + 1 ) :
        x1 = x1 ^ a [ i ]
    for i in range ( 2 , n + 1 ) :
        x2 = x2 ^ i
    return ( x1 ^ x2 )
|||

FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES

def f_gold ( arr , arr_size ) :
    i = 0
    for i in range ( arr_size ) :
        count = 0
        for j in range ( arr_size ) :
            if arr [ i ] == arr [ j ] :
                count += 1
        if count % 2 != 0 :
            return arr [ i ]
    return - 1
|||

FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES_1

def f_gold ( arr , n ) :
    hdict = { }
    for i in range ( n ) :
        if hdict.has_key ( arr [ i ] ) :
            val = hdict [ arr [ i ] ]
            hdict [ arr [ i ] ] = val + 1
        else :
            hdict [ arr [ i ] ] = 1
    for a in hdict.keys ( ) :
        if hdict [ a ] % 2 != 0 :
            return a
|||

FIND_WHETHER_A_GIVEN_NUMBER_IS_A_POWER_OF_4_OR_NOT_2

def f_gold ( n ) :
    return n != 0 and ( ( n & ( n - 1 ) ) == 0 ) and ( n & 0xAAAAAAAA ) == 0
|||

FIRST_UPPERCASE_LETTER_IN_A_STRING_ITERATIVE_AND_RECURSIVE

def f_gold ( str ) :
    for c in str :
        if ord ( c ) < 128 :
            return c
    return 0
|||

FLOOR_IN_A_SORTED_ARRAY_1

def f_gold ( arr , low , high , x ) :
    if low > high :
        return - 1
    if x >= arr [ high ] :
        return high
    mid = ( low + high ) // 2
    if arr [ mid ] == x :
        return mid
    if mid > 0 and arr [ mid - 1 ] <= x and x < arr [ mid ] :
        return mid - 1
    if x < arr [ mid ] :
        return f_gold ( arr , low , mid - 1 , x )
    return f_gold ( arr , mid + 1 , high , x )
|||

FUNCTION_COPY_STRING_ITERATIVE_RECURSIVE_1

def f_gold ( s1 , s2 , index ) :
    s2 = s2 [ index ]
    if index == len ( s1 ) - 1 :
        return s1
    return s1 [ index ]
|||

GIVEN_LARGE_NUMBER_CHECK_SUBSEQUENCE_DIGITS_DIVISIBLE_8

def f_gold ( str ) :
    i , j , k , l = len ( str ) , len ( str ) , len ( str ) , len ( str )
    arr = [ 0 for i in range ( l ) ]
    for i in range ( l ) :
        for j in range ( i , l ) :
            for k in range ( j , l ) :
                if arr [ i ] % 8 == 0 :
                    return True
                elif ( arr [ i ] * 10 + arr [ j ] ) % 8 == 0 and i != j :
                    return True
                elif ( arr [ i ] * 100 + arr [ j ] * 10 + arr [ k ] ) % 8 == 0 and i != j and j != k and i != k :
                    return True
    return False
|||

GOOGLE_CASE_GIVEN_SENTENCE

def f_gold ( s ) :
    n = len ( s )
    s1 = ""
    s1 = s1 + chr ( ord ( s [ 0 ] ) )
    for i in range ( 1 , n ) :
        if s [ i ] == ' ' and i < n :
            s1 = s1 + " " + chr ( ord ( s [ i + 1 ] ) )
            i += 1
        else :
            s1 = s1 + chr ( ord ( s [ i ] ) )
    return s1
|||

HEIGHT_COMPLETE_BINARY_TREE_HEAP_N_NODES

def f_gold ( N ) :
    return int ( math.ceil ( math.log ( N + 1 ) / math.log ( 2 ) ) ) - 1
|||

HEXAGONAL_NUMBER

def f_gold ( n ) :
    return n * ( 2 * n - 1 )
|||

HOW_CAN_WE_SUM_THE_DIGITS_OF_A_GIVEN_NUMBER_IN_SINGLE_STATEMENT_2

def f_gold ( no ) :
    return no if no > 0 else no % 10 + f_gold ( no / 10 )
|||

HOW_TO_CHECK_IF_A_GIVEN_ARRAY_REPRESENTS_A_BINARY_HEAP

def f_gold ( arr , i , n ) :
    if i > ( n - 2 ) / 2 :
        return True
    if arr [ i ] >= arr [ 2 * i + 1 ] and arr [ i ] >= arr [ 2 * i + 2 ] and f_gold ( arr , 2 * i + 1 , n ) and f_gold ( arr , 2 * i + 2 , n ) :
        return True
    return False
|||

HOW_TO_CHECK_IF_A_GIVEN_ARRAY_REPRESENTS_A_BINARY_HEAP_1

def f_gold ( arr , n ) :
    for i in range ( 0 , ( n - 2 ) // 2 ) :
        if arr [ 2 * i + 1 ] > arr [ i ] :
            return False
        if 2 * i + 2 < n and arr [ 2 * i + 2 ] > arr [ i ] :
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
    p = int ( math.pow ( a , b ) )
    count = 0
    while p > 0 and count < k :
        rem = p % 10
        count += 1
        if count == k :
            return rem
        p = p / 10
|||

K_TH_ELEMENT_TWO_SORTED_ARRAYS

def f_gold ( arr1 , arr2 , m , n , k ) :
    sorted1 = [ ]
    i , j , d = 0 , 0 , 0
    while i < m and j < n :
        if arr1 [ i ] < arr2 [ j ] :
            sorted1.append ( arr1 [ i ++ ] )
        else :
            sorted1.append ( arr2 [ j ++ ] )
    while i < m :
        sorted1.append ( arr1 [ i ++ ] )
    while j < n :
        sorted1.append ( arr2 [ j ++ ] )
    return sorted1 [ k - 1 ]
|||

K_TH_LARGEST_SUM_CONTIGUOUS_SUBARRAY

def f_gold ( arr , n , k ) :
    sum = [ 0 ] * ( n + 1 )
    for i in range ( 2 , n + 1 ) :
        sum [ i ] = sum [ i - 1 ] + arr [ i - 1 ]
    Q = PriorityQueue ( )
    for i in range ( 1 , n + 1 ) :
        for j in range ( i , n + 1 ) :
            x = sum [ j ] - sum [ i - 1 ]
            if len ( Q ) < k :
                Q.add ( x )
            else :
                if Q.peek ( ) < x :
                    Q.poll ( )
                    Q.add ( x )
    return Q.get ( )
|||

K_TH_MISSING_ELEMENT_INCREASING_SEQUENCE_NOT_PRESENT_GIVEN_SEQUENCE

def f_gold ( a , b , k , n1 , n2 ) :
    s = set ( )
    for i in range ( n2 ) :
        s.add ( b [ i ] )
    missing = 0
    for i in range ( n1 ) :
        if not s.intersection ( a [ i ] ) :
            missing += 1
        if missing == k :
            return a [ i ]
    return - 1
|||

LCS_FORMED_CONSECUTIVE_SEGMENTS_LEAST_LENGTH_K

def f_gold ( k , s1 , s2 ) :
    n = len ( s1 )
    m = len ( s2 )
    lcs = [ [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m
|||

LONGEST_INCREASING_ODD_EVEN_SUBSEQUENCE

def f_gold ( arr , n ) :
    lioes = [ 1 ] * n
    max_len = 0
    for i in range ( n ) :
        lioes [ i ] = 1
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if arr [ i ] > arr [ j ] and ( arr [ i ] + arr [ j ] ) % 2 != 0 and lioes [ i ] < lioes [ j ] + 1 :
                lioes [ i ] = lioes [ j ] + 1
    for i in range ( n ) :
        if max_len < lioes [ i ] :
            max_len = lioes [ i ]
    return max_len
|||

LONGEST_PALINDROME_SUBSEQUENCE_SPACE

def f_gold ( s ) :
    n = len ( s )
    a = [ ]
    for i in range ( n - 1 , - 1 , - 1 ) :
        back_up = 0
        for j in range ( i , n ) :
            if j == i :
                a.append ( 1 )
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
    len = 0
    i = 1
    while i < n :
        if s [ i ] == s [ len ( s ) ] :
            len += 1
            lps [ i ] = len
            i += 1
        else :
            if len != 0 :
                len = lps [ len - 1 ]
            else :
                lps [ i ] = 0
                i += 1
    res = lps [ n - 1 ]
    return ( res > n / 2 )
|||

MAKING_ELEMENTS_OF_TWO_ARRAYS_SAME_WITH_MINIMUM_INCREMENTDECREMENT

def f_gold ( a , b , n ) :
    a.sort ( )
    b.sort ( )
    result = 0
    for i in range ( n ) :
        if a [ i ] > b [ i ] :
            result = result + abs ( a [ i ] - b [ i ] )
        elif a [ i ] < b [ i ] :
            result = result + abs ( a [ i ] - b [ i ] )
    return result
|||

MARKOV_MATRIX

def f_gold ( m ) :
    for i in range ( len ( m ) ) :
        sum = 0
        for j in range ( len ( m [ i ] ) ) :
            sum = sum + m [ i ] [ j ]
        if sum != 1 :
            return False
    return True
|||

MAXIMIZE_SUM_CONSECUTIVE_DIFFERENCES_CIRCULAR_ARRAY

def f_gold ( arr , n ) :
    sum = 0
    arr.sort ( )
    for i in range ( n // 2 ) :
        sum -= ( 2 * arr [ i ] )
        sum += ( 2 * arr [ n - i - 1 ] )
    return sum
|||

MAXIMUM_AREA_RECTANGLE_PICKING_FOUR_SIDES_ARRAY_1

def f_gold ( arr , n ) :
    s = set ( )
    first , second = 0 , 0
    for i in range ( n ) :
        if not s.issubset ( arr [ i ] ) :
            s.add ( arr [ i ] )
            continue
        if arr [ i ] > first :
            second = first
            first , second = arr [ i ] , arr [ i ]
        elif arr [ i ] > second :
            second , first = arr [ i ] , arr [ i ]
    return ( first , second )
|||

MAXIMUM_AVERAGE_SUM_PARTITION_ARRAY

def f_gold ( A , K ) :
    n = len ( A )
    pre_sum = np.zeros ( ( n + 1 , ) )
    pre_sum [ 0 ] = 0
    for i in range ( n ) :
        pre_sum [ i + 1 ] = pre_sum [ i ] + A [ i ]
    dp = np.zeros ( ( n , ) )
    sum = 0
    for i in range ( n ) :
        dp [ i ] = ( pre_sum [ n ] - pre_sum [ i ] ) / ( n - i )
    for k in range ( K - 1 ) :
        for i in range ( n ) :
            for j in range ( i + 1 , n ) :
                dp [ i ] = max ( dp [ i ] , ( pre_sum [ j ] - pre_sum [ i ] ) / ( j - i ) + dp [ j ] )
    return dp
|||

MAXIMUM_BINOMIAL_COEFFICIENT_TERM_VALUE

def f_gold ( n ) :
    C = [ [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n
|||

MAXIMUM_CONSECUTIVE_REPEATING_CHARACTER_STRING_1

def f_gold ( str ) :
    n = len ( str )
    count = 0
    res = str [ 0 ]
    cur_count = 1
    for i in range ( n ) :
        if i < n - 1 and str [ i ] == str [ i + 1 ] :
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
    row_sum = [ ]
    for i in range ( m ) :
        sum = 0
        for j in range ( n ) :
            sum += mat [ i , j ]
        row_sum.append ( sum )
    max_diff = row_sum [ 1 ] - row_sum [ 0 ]
    min_element = row_sum [ 0 ]
    for i in range ( 1 , m ) :
        if row_sum [ i ] - min_element > max_diff :
            max_diff = row_sum [ i ] - min_element
        if row_sum [ i ] < min_element :
            min_element = row_sum [ i ]
    return max_diff
|||

MAXIMUM_GAMES_PLAYED_WINNER

def f_gold ( N ) :
    dp = [ 1 , 2 ]
    i = 2
    do = dp [ i - 1 ] + dp [ i - 2 ]
    while dp [ i ] <= N :
        dp [ i ] = dp [ i - 1 ] + dp [ i - 2 ]
    return ( i - 2 )
|||

MAXIMUM_HEIGHT_OF_TRIANGULAR_ARRANGEMENT_OF_ARRAY_VALUES

def f_gold ( a , n ) :
    result = 1
    for i in range ( 1 , n + 1 ) :
        y = ( i * ( i + 1 ) ) / 2
        if y < n :
            result = i
        else :
            break
    return result
|||

MAXIMUM_LENGTH_PREFIX_ONE_STRING_OCCURS_SUBSEQUENCE_ANOTHER

def f_gold ( s , t ) :
    count = 0
    for c in t :
        if count == len ( t ) :
            break
        if c == s [ count ] :
            count += 1
    return count
|||

MAXIMUM_NUMBER_CHOCOLATES_DISTRIBUTED_EQUALLY_AMONG_K_STUDENTS

def f_gold ( arr , n , k ) :
    um = { }
    sum = [ ]
    curr_rem = 0
    max_sum = 0
    sum.append ( arr [ 0 ] )
    for i in range ( 1 , n ) :
        sum [ i ] = sum [ i - 1 ] + arr [ i ]
    for i in range ( n ) :
        curr_rem = sum [ i ] % k
        if curr_rem == 0 :
            if max_sum < sum [ i ] :
                max_sum = sum [ i ]
        elif not um.has_key ( curr_rem ) :
            um [ curr_rem ] = i
        elif max_sum < ( sum [ i ] - sum [ um [ curr_rem ] ] ) :
            max_sum = sum [ i ] - sum [ um [ curr_rem ] ]
    return ( max_sum / k )
|||

MAXIMUM_NUMBER_OF_SQUARES_THAT_CAN_BE_FIT_IN_A_RIGHT_ANGLE_ISOSCELES_TRIANGLE

def f_gold ( b , m ) :
    return ( b / m - 1 ) ** 2 / 2
|||

MAXIMUM_PRODUCT_INCREASING_SUBSEQUENCE

def f_gold ( arr , n ) :
    mpis = [ ]
    max = int ( arr [ i ] )
    for i in range ( n ) :
        mpis.append ( arr [ i ] )
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if arr [ i ] > arr [ j ] and mpis [ i ] < ( mpis [ j ] * arr [ i ] ) :
                mpis [ i ] = mpis [ j ] * arr [ i ]
    for k in mpis :
        if mpis [ k ] > max :
            max = mpis [ k ]
    return max
|||

MAXIMUM_PRODUCT_OF_4_ADJACENT_ELEMENTS_IN_MATRIX

def f_gold ( arr , n ) :
    max , result = 0 , 0
    for i in range ( n ) :
        for j in range ( n ) :
            if ( j - 3 ) >= 0 :
                result = arr [ i ] [ j ] * arr [ i ] [ j - 1 ] * arr [ i ] [ j - 2 ] * arr [ i ] [ j - 3 ]
                if max < result :
                    max = result
            if ( i - 3 ) >= 0 :
                result = arr [ i ] [ j ] * arr [ i - 1 ] [ j ] * arr [ i - 2 ] [ j ] * arr [ i - 3 ] [ j ]
                if max < result :
                    max = result
            if ( i - 3 ) >= 0 and ( j - 3 ) >= 0 :
                result = arr [ i ] [ j ] * arr [ i - 1 ] [ j - 1 ] * arr [ i - 2 ] [ j - 2 ] * arr [ i - 3 ] [ j - 3 ]
                if max < result :
                    max = result
    return max
|||

MAXIMUM_PRODUCT_SUBSET_ARRAY

def f_gold ( a , n ) :
    if n == 1 :
        return a [ 0 ]
    max_neg = int ( a [ 0 ] )
    count_neg , count_zero = 0 , 0
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
    if count_neg % 2 == 1 :
        if count_neg == 1 and count_zero > 0 and count_zero + count_neg == n :
            return 0
        prod = prod / max_neg
    return prod
|||

MAXIMUM_SUM_IARRI_AMONG_ROTATIONS_GIVEN_ARRAY

def f_gold ( arr , n ) :
    res = int ( 0 )
    for i in range ( n ) :
        curr_sum = 0
        for j in range ( n ) :
            index = ( i + j ) % n
            curr_sum += j * arr [ index ]
        res = max ( res , curr_sum )
    return res
|||

MAXIMUM_SUM_PAIRS_SPECIFIC_DIFFERENCE_1

def f_gold ( arr , N , k ) :
    max_sum = 0
    arr.sort ( )
    for i in range ( N - 1 , 0 , - 1 ) :
        if arr [ i ] - arr [ i - 1 ] < k :
            max_sum += arr [ i ]
            max_sum += arr [ i - 1 ]
            del arr [ i ]
    return max_sum
|||

MAXIMUM_SUM_SUBSEQUENCE_LEAST_K_DISTANT_ELEMENTS

def f_gold ( arr , N , k ) :
    MS = [ arr [ i ] for i in range ( N ) ]
    for i in range ( N - 2 , - 1 , - 1 ) :
        if i + k + 1 >= N :
            MS [ i ] = max ( arr [ i ] , MS [ i + 1 ] )
        else :
            MS [ i ] = max ( arr [ i ] + MS [ i + k + 1 ] , MS [ i + 1 ] )
    return MS [ 0 ]
|||

MAXIMUM_WEIGHT_PATH_ENDING_ELEMENT_LAST_ROW_MATRIX

def f_gold ( mat , N ) :
    dp = [ 0 ] * N
    for i in range ( 1 , N ) :
        dp [ i ] = mat [ i ] + dp [ i - 1 ]
    for i in range ( 1 , N ) :
        for j in range ( 1 , i + 1 and j < N ) :
            dp [ i ] = mat [ i ] + max ( dp [ i - 1 ] [ j - 1 ] , dp [ i - 1 ] [ j ] )
    result = 0
    for i in range ( N ) :
        if result < dp [ N - 1 ] [ i ] :
            result = dp [ N - 1 ] [ i ]
    return result
|||

MINIMIZE_SUM_PRODUCT_TWO_ARRAYS_PERMUTATIONS_ALLOWED

def f_gold ( A , B , n ) :
    A.sort ( )
    B.sort ( )
    result = 0
    for i in range ( n ) :
        result += ( A [ i ] * B [ n - i - 1 ] )
    return result
|||

MINIMUM_CHARACTERS_ADDED_FRONT_MAKE_STRING_PALINDROME

def f_gold ( s ) :
    l = len ( s )
    for i , j in enumerate ( l - 1 ) :
        if s [ i ] != s [ j ] :
            return False
    return True
|||

MINIMUM_COST_FOR_ACQUIRING_ALL_COINS_WITH_K_EXTRA_COINS_ALLOWED_WITH_EVERY_COIN

def f_gold ( coin , n , k ) :
    coin.sort ( )
    coins_needed = int ( math.ceil ( 1.0 * n / ( k + 1 ) ) )
    ans = 0
    for i in range ( 0 , coins_needed - 1 ) :
        ans += coin [ i ]
    return ans
|||

MINIMUM_COST_MAKE_ARRAY_SIZE_1_REMOVING_LARGER_PAIRS

def f_gold ( a , n ) :
    min = a [ 0 ]
    for i in range ( 1 , len ( a ) ) :
        if a [ i ] < min :
            min = a [ i ]
    return ( n - 1 ) * min
|||

MINIMUM_DIFFERENCE_BETWEEN_GROUPS_OF_SIZE_TWO

def f_gold ( a , n ) :
    a.sort ( )
    i , j = 0 , n
    s = [ ]
    for i , j in enumerate ( a ) :
        s.append ( ( i , j ) )
    mini = min ( s )
    maxi = max ( s )
    return abs ( maxi - mini )
|||

MINIMUM_DIFFERENCE_MAX_MIN_K_SIZE_SUBSETS

def f_gold ( arr , N , K ) :
    arr.sort ( )
    res = 2147483647
    for i in range ( 0 , ( N - K ) ) :
        cur_seq_diff = arr [ i + K - 1 ] - arr [ i ]
        res = min ( res , cur_seq_diff )
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
    arr.sort ( )
    max = arr [ - 1 ]
    res = 0
    for i in range ( n ) :
        if ( max - arr [ i ] ) % k != 0 :
            return - 1
        else :
            res += ( max - arr [ i ] ) / k
    return res
|||

MINIMUM_LENGTH_SUBARRAY_SUM_GREATER_GIVEN_VALUE_1

def f_gold ( arr , n , x ) :
    curr_sum , min_len = 0 , n + 1
    start , end = 0 , 0
    while end < n :
        while curr_sum <= x and end < n :
            if curr_sum <= 0 and x > 0 :
                start = end
                curr_sum = 0
            curr_sum += arr [ end ]
        while curr_sum > x and start < n :
            if end - start < min_len :
                min_len = end - start
            curr_sum -= arr [ start ]
    return min_len
|||

MINIMUM_NUMBER_PLATFORMS_REQUIRED_RAILWAYBUS_STATION

def f_gold ( arr , dep , n ) :
    arr.sort ( )
    dep.sort ( )
    plat_needed , result = 1 , 1
    i , j = 1 , 0
    while i < n and j < n :
        if arr [ i ] <= dep [ j ] :
            plat_needed += 1
            i += 1
            if plat_needed > result :
                result = plat_needed
        else :
            plat_needed -= 1
            j += 1
    return result
|||

MINIMUM_PRODUCT_SUBSET_ARRAY

def f_gold ( a , n ) :
    if n == 1 :
        return a [ 0 ]
    negmax = int ( a [ 0 ] )
    posmin = int ( a [ 0 ] )
    count_neg , count_zero = 0 , 0
    product = 1
    for i in range ( n ) :
        if a [ i ] == 0 :
            count_zero += 1
            continue
        if a [ i ] < 0 :
            count_neg += 1
            negmax = max ( negmax , a [ i ] )
        if a [ i ] > 0 and a [ i ] < posmin :
            posmin = a [ i ]
        product *= a [ i ]
    if count_zero == n or ( count_neg == 0 and count_zero > 0 ) :
        return 0
    if count_neg == 0 :
        return posmin
    if count_neg % 2 == 0 and count_neg != 0 :
        product = product / negmax
    return product
|||

MINIMUM_ROTATIONS_UNLOCK_CIRCULAR_LOCK

def f_gold ( input , unlock_code ) :
    rotation = 0
    input_digit , code_digit = input
    while input or unlock_code :
        input_digit = input % 10
        code_digit = unlock_code % 10
        rotation += min ( abs ( input_digit - code_digit ) , 10 - abs ( input_digit - code_digit ) )
        input /= 10
        unlock_code /= 10
    return rotation
|||

MINIMUM_SUM_SUBSEQUENCE_LEAST_ONE_EVERY_FOUR_CONSECUTIVE_ELEMENTS_PICKED_1

def f_gold ( ar , n ) :
    if n <= 4 :
        return sum ( ar ).min ( ).astype ( int )
    sum = [ ar [ i ] for i in range ( n ) ]
    for i in range ( 4 , n ) :
        sum [ i ] = ar [ i ] + sum [ i - 4 : i ]
    return sum [ n - 4 : n ]
|||

MINIMUM_SUM_TWO_NUMBERS_FORMED_DIGITS_ARRAY_2

def f_gold ( a , n ) :
    a.sort ( )
    num1 = 0
    num2 = 0
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
    for i in range ( n ) :
        if arr [ i ] <= k :
            count += 1
    bad = 0
    for i in range ( count ) :
        if arr [ i ] > k :
            bad += 1
    ans = bad
    for i , j in enumerate ( count , start = 1 ) :
        if arr [ i ] > k :
            bad -= 1
        if arr [ j ] > k :
            bad += 1
        ans = min ( ans , bad )
    return ans
|||

MINIMUM_TIME_TO_FINISH_TASKS_WITHOUT_SKIPPING_TWO_CONSECUTIVE

def f_gold ( arr , n ) :
    if n <= 0 :
        return 0
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

def f_gold ( N , insert , remove , copy ) :
    if N == 0 :
        return 0
    if N == 1 :
        return insert
    dp = [ 0 ] * ( N + 1 )
    for i in range ( 1 , N + 1 ) :
        if i % 2 == 0 :
            dp [ i ] = min ( dp [ i - 1 ] + insert , dp [ i / 2 ] + copy )
        else :
            dp [ i ] = min ( dp [ i - 1 ] + insert , dp [ ( i + 1 ) / 2 ] + copy + remove )
    return dp [ N ]
|||

MOBILE_NUMERIC_KEYPAD_PROBLEM

def f_gold ( keypad , n ) :
    if keypad is None or n <= 0 :
        return 0
    if n == 1 :
        return 10
    odd = [ ]
    even = [ ]
    i = 0 , 0 , 0 , useOdd , totalCount = 0
    for i in range ( 0 , 9 ) :
        odd.append ( 1 )
    for j in range ( 2 , n ) :
        useOdd = 1 - useOdd
        if useOdd == 1 :
            even.append ( odd [ 0 ] + odd [ 8 ] )
            even.append ( odd [ 1 ] + odd [ 2 ] + odd [ 4 ] )
            even.append ( odd [ 2 ] + odd [ 1 ] + odd [ 3 ] + odd [ 5 ] )
            even.append ( odd [ 3 ] + odd [ 2 ] + odd [ 6 ] )
            even.append ( odd [ 4 ] + odd [ 1 ] + odd [ 5 ] + odd [ 7 ] )
            even.append ( odd [ 5 ] + odd [ 2 ] + odd [ 4 ] + odd [ 8 ] + odd [ 6 ] )
            even.append ( odd [ 6 ] + odd [ 3 ] + odd [ 5 ] + odd [ 9 ] )
            even.append ( odd [ 7 ] + odd [ 4 ] + odd [ 8 ] )
            even.append ( odd [ 8 ] + odd [ 0 ] + odd [ 5 ] + odd [ 7 ] + odd [ 9 ] )
            even.append ( odd [ 9 ] + odd [ 6 ] + odd [ 8 ] )
        else :
            odd.append ( even [ 0 ] + even [ 8 ] )
            odd.append ( even [ 1 ] + even [ 2 ] + even [ 4 ] )
            odd.append ( even [ 2 ] + even [ 1 ] + even [ 3 ] + even [ 5 ] )
            odd.append ( even [ 3 ] + even [ 2 ] + even [ 6 ] )
            odd.append ( even [ 4 ] + even [ 1 ] + even [ 5 ] + even [ 7 ] )
            odd.append ( even [ 5 ] + odd [ 2 ] + odd [ 4 ] + odd [ 8 ] )
            odd.append ( even [ 6 ] + odd [ 3 ] + odd [ 5 ] + odd [ 9 ] )
    return sum ( odd )
    
|||

MULTIPLY_AN_INTEGER_WITH_3_5

def f_gold ( x ) :
    return ( x << 1 ) + x + ( x >> 1 )
|||

NUMBER_IS_DIVISIBLE_BY_29_OR_NOT

def f_gold ( n ) :
    while n / 100 > 0 :
        last_digit = int ( n % 10 )
        n /= 10
        n += last_digit * 3
    return ( n % 29 == 0 )
|||

NUMBER_N_DIGIT_STEPPING_NUMBERS

def f_gold ( n ) :
    dp = [ 0 ] * ( n + 1 )
    if n == 1 : return 10
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
|||

NUMBER_OF_SUBSTRINGS_WITH_ODD_DECIMAL_VALUE_IN_A_BINARY_STRING

def f_gold ( s ) :
    n = len ( s )
    auxArr = [ ]
    if s [ 0 ] == '1' :
        auxArr.append ( 1 )
    for i in range ( 1 , n ) :
        if s [ i ] == '1' :
            auxArr.append ( auxArr [ i - 1 ] + 1 )
        else :
            auxArr.append ( auxArr [ i - 1 ] )
    count = 0
    for i in range ( n - 1 , - 1 , - 1 ) :
        if s [ i ] == '1' :
            count += auxArr [ i ]
    return count
|||

NUMBER_OF_TRIANGLES_IN_A_PLANE_IF_NO_MORE_THAN_TWO_POINTS_ARE_COLLINEAR

def f_gold ( n ) :
    return n * ( n - 1 ) ** ( n - 2 ) / 6
|||

NUMBER_ORDERED_PAIRS_AI_AJ_0

def f_gold ( a , n ) :
    count = 0
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if ( a [ i ] & a [ j ] ) == 0 :
                count += 2
    return count
|||

NUMBER_SUBSTRINGS_DIVISIBLE_4_STRING_INTEGERS

def f_gold ( s ) :
    n = len ( s )
    count = 0
    for i in range ( n ) :
        if s [ i ] in [ '4' , '8' , '0' ] :
            count += 1
    for i in range ( n - 1 ) :
        h = ( s [ i ] - '0' ) * 10 + ( s [ i + 1 ] - '0' )
        if h % 4 == 0 :
            count = count + i + 1
    return count
|||

NUMBER_TRIANGLES_N_MOVES

def f_gold ( n ) :
    answer = [ 1 ] * ( n + 1 )
    for i in range ( 1 , n + 1 ) :
        answer [ i ] = answer [ i - 1 ] * 3 + 2
    return answer [ n ]
|||

NUMBER_UNIQUE_RECTANGLES_FORMED_USING_N_UNIT_SQUARES

def f_gold ( n ) :
    ans = 0
    for length in range ( 1 , math.sqrt ( n ) + 1 ) :
        for height in range ( length , length * length <= n ) :
            ans += 1
    return ans
|||

NUMBER_WAYS_NODE_MAKE_LOOP_SIZE_K_UNDIRECTED_COMPLETE_CONNECTED_GRAPH_N_NODES

def f_gold ( n , k ) :
    p = 1
    if k % 2 != 0 :
        p = - 1
    return int ( pow ( n - 1 , k ) + p * ( n - 1 ) ) / n
|||

N_TH_NUMBER_WHOSE_SUM_OF_DIGITS_IS_TEN_2

def f_gold ( n ) :
    nth_element = 19 + ( n - 1 ) * 9
    outliers_count = int ( math.log10 ( nth_element ) - 1 )
    nth_element += 9 * outliers_count
    return nth_element
|||

N_TH_TERM_SERIES_2_12_36_80_150

def f_gold ( n ) :
    return ( n ** 2 ) + ( n ** 2 * n )
|||

PAINTING_FENCE_ALGORITHM

def f_gold ( n , k ) :
    total = k
    mod = 1000000007
    same , diff = 0 , k
    for i in range ( 2 , n + 1 ) :
        same , diff = diff , int ( total * ( k - 1 ) )
        diff = diff % mod
        total = ( same + diff ) % mod
    return total
|||

PAIR_WITH_GIVEN_PRODUCT_SET_1_FIND_IF_ANY_PAIR_EXISTS

def f_gold ( arr , n , x ) :
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            if arr [ i ] * arr [ j ] == x :
                return True
    return False
|||

PERFECT_REVERSIBLE_STRING

def f_gold ( str ) :
    i , j = 0 , len ( str ) - 1
    while i < j :
        if str [ i ] != str [ j ] :
            return False
        i += 1
        j -= 1
    return True
|||

PIZZA_CUT_PROBLEM_CIRCLE_DIVISION_LINES

def f_gold ( n ) :
    return 1 + n * ( n + 1 ) / 2
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
|||

PRIMALITY_TEST_SET_5USING_LUCAS_LEHMER_SERIES

def f_gold ( p ) :
    check_number = math.pow ( 2 , p ) - 1
    nextval = 4 % check_number
    for i in range ( 1 , p - 1 ) :
        nextval = ( nextval * nextval - 2 ) % check_number
    return ( nextval == 0 )
|||

PRINT_WORDS_STRING_REVERSE_ORDER

def f_gold ( str ) :
    i = len ( str ) - 1
    start , end = i + 1 , i + 1
    result = ""
    while i >= 0 :
        if str [ i ] == ' ' :
            start = i + 1
            while start != end :
                result += str [ start ]
            result += ' '
            end = i
        i -= 1
    start = 0
    while start != end :
        result += str [ start ]
    return result
|||

PROGRAM_BINARY_DECIMAL_CONVERSION_1

def f_gold ( n ) :
    num = n
    dec_value = 0
    base = 1
    len ( num )
    for i in range ( len ( num ) - 1 , - 1 , - 1 ) :
        if num [ i ] == '1' :
            dec_value += base
        base = base * 2
    return dec_value
|||

PROGRAM_CALCULATE_AREA_OCTAGON

def f_gold ( side ) :
    return float ( 2 * ( 1 + np.sqrt ( 2 ) ) * side ** 2 )
|||

PROGRAM_CALCULATE_VOLUME_ELLIPSOID

def f_gold ( r1 , r2 , r3 ) :
    pi = float ( 3.14 )
    return float ( 1.33 * pi * r1 * r2 * r3 )
|||

PROGRAM_CALCULATE_VOLUME_OCTAHEDRON

def f_gold ( side ) :
    return ( ( side ** 2 ) * ( math.sqrt ( 2 ) / 3 ) )
|||

PROGRAM_CIRCUMFERENCE_PARALLELOGRAM

def f_gold ( a , b ) :
    return ( ( 2 * a ) + ( 2 * b ) )
|||

PROGRAM_COUNT_OCCURRENCE_GIVEN_CHARACTER_STRING

def f_gold ( s , c ) :
    res = 0
    for i in range ( len ( s ) ) :
        if s [ i ] == c :
            res += 1
    return res
|||

PROGRAM_FOR_FACTORIAL_OF_A_NUMBER

def f_gold ( n ) :
    if n == 0 :
        return 1
    return n * f_gold ( n - 1 )
|||

PROGRAM_FOR_FACTORIAL_OF_A_NUMBER_1

def f_gold ( n ) :
    res , i = 1 , 0
    for i in range ( 2 , n + 1 ) :
        res *= i
    return res
|||

PROGRAM_FOR_FACTORIAL_OF_A_NUMBER_2

def f_gold ( n ) :
    return ( n == 1 or n == 0 )
|||

PROGRAM_PAGE_REPLACEMENT_ALGORITHMS_SET_2_FIFO

def f_gold ( pages , n , capacity ) :
    s = set ( capacity )
    indexes = queue.Queue ( )
    page_faults = 0
    for i in range ( n ) :
        if len ( s ) < capacity :
            if not s.issubset ( pages ) :
                s.add ( pages [ i ] )
                page_faults += 1
                indexes.add ( pages [ i ] )
        else :
            if not s.issubset ( pages ) :
                val = indexes.pop ( )
                indexes.clear ( )
                s.remove ( val )
                s.add ( pages [ i ] )
                indexes.add ( pages [ i ] )
                page_faults += 1
    return page_faults
|||

PROGRAM_PRINT_SUM_GIVEN_NTH_TERM_1

def f_gold ( n ) :
    return int ( math.pow ( n , 2 ) )
|||

PROGRAM_TO_FIND_THE_AREA_OF_PENTAGON

def f_gold ( a ) :
    area = float ( 'inf' )
    area = ( math.sqrt ( 5 * ( 5 + 2 * ( math.sqrt ( 5 ) ) ) ) * a ** 2 ) / 4
    return area
|||

PYTHAGOREAN_QUADRUPLE

def f_gold ( a , b , c , d ) :
    sum = a ** 2 + b ** 2 + c ** 2
    if d ** 2 == sum :
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
    max_idx , min_idx = n - 1 , 0
    max_elem = arr [ n - 1 ] + 1
    for i in range ( n ) :
        if i % 2 == 0 :
            arr [ i ] += ( arr [ max_idx ] % max_elem ) * max_elem
            max_idx -= 1
        else :
            arr [ i ] += ( arr [ min_idx ] % max_elem ) * max_elem
            min_idx += 1
    for i in range ( n ) :
        arr [ i ] = arr [ i ] / max_elem
|||

RECURSIVELY_BREAK_NUMBER_3_PARTS_GET_MAXIMUM_SUM

def f_gold ( n ) :
    if n == 0 or n == 1 :
        return n
    return max ( ( f_gold ( n / 2 ) + f_gold ( n / 3 ) + f_gold ( n / 4 ) ) , n )
|||

RECURSIVELY_BREAK_NUMBER_3_PARTS_GET_MAXIMUM_SUM_1

def f_gold ( n ) :
    dp = [ 0 ] * ( n + 1 )
    dp [ 0 ] = 1
    for i in range ( 2 , n + 1 ) :
        dp [ i ] = max ( dp [ i / 2 ] + dp [ i / 3 ] + dp [ i / 4 ] , i )
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
    if low == high :
        return a [ low ] * turn
    if dp [ low ] [ high ] != 0 :
        return dp [ low ] [ high ]
    dp [ low ] [ high ] = max ( a [ low ] * turn + f_gold ( dp , a , low + 1 , high , turn + 1 ) , a [ high ] * turn + f_gold ( dp , a , low , high - 1 , turn + 1 ) )
    return dp [ low ] [ high ]
|||

REMOVE_MINIMUM_ELEMENTS_EITHER_SIDE_2MIN_MAX

def f_gold ( arr , n ) :
    longest_start , longest_end = - 1 , 0
    for start in range ( n ) :
        min , max = int ( arr [ start ] ) , int ( arr [ start + 1 ] )
        for end in range ( start , n ) :
            val = arr [ end ]
            if val < min : min , val = val , val
            if val > max : max , val = val , val
            if 2 * min <= max : break
            if end - start > longest_end - longest_start or longest_start == - 1 :
                longest_start = start
                longest_end = end
    if longest_start == - 1 :
        return n
    return ( n - ( longest_end - longest_start + 1 ) )
|||

REMOVE_MINIMUM_NUMBER_ELEMENTS_NO_COMMON_ELEMENT_EXIST_ARRAY

def f_gold ( a , b , n , m ) :
    count_a = { }
    count_b = { }
    for i in range ( n ) :
        if count_a.has_key ( a [ i ] ) :
            count_a [ a [ i ] ] = count_a [ a [ i ] ] + 1
        else :
            count_a [ a [ i ] ] = 1
    for i in range ( m ) :
        if count_b.has_key ( b [ i ] ) :
            count_b [ b [ i ] ] = count_b [ b [ i ] ] + 1
        else :
            count_b [ b [ i ] ] = 1
    res = 0
    s = count_a.keys ( )
    for x in s :
        if count_b.has_key ( x ) :
            res += min ( count_b [ x ] , count_a [ x ] )
    return res
|||

REPLACE_CHARACTER_C1_C2_C2_C1_STRING_S

def f_gold ( s , c1 , c2 ) :
    l = len ( s )
    arr = s [ : l ]
    for i in range ( l ) :
        if arr [ i ] == c1 :
            arr [ i ] = c2
        elif arr [ i ] == c2 :
            arr [ i ] = c1
    return str ( arr )
|||

ROUND_THE_GIVEN_NUMBER_TO_NEAREST_MULTIPLE_OF_10

def f_gold ( n ) :
    a = ( n // 10 ) * 10
    b = a + 10
    return ( n - a > b - n )
|||

SEARCHING_ARRAY_ADJACENT_DIFFER_K

def f_gold ( arr , n , x , k ) :
    i = 0
    while i < n :
        if arr [ i ] == x :
            return i
        i = i + max ( 1 , abs ( arr [ i ] - x ) / k )
    print ( "number is " + "not present!" )
    return - 1
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
|||

SMALLEST_DIFFERENCE_PAIR_VALUES_TWO_UNSORTED_ARRAYS

def f_gold ( A , B , m , n ) :
    A.sort ( )
    B.sort ( )
    a , b = 0 , 0
    result = sys.maxsize
    while a < m and b < n :
        if abs ( A [ a ] - B [ b ] ) < result :
            result = abs ( A [ a ] - B [ b ] )
        if A [ a ] < B [ b ] :
            a += 1
        else :
            b += 1
    return result
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
|||

SMALLEST_POWER_OF_2_GREATER_THAN_OR_EQUAL_TO_N

def f_gold ( n ) :
    count = 0
    if n and ( n & ( n - 1 ) ) == 0 :
        return n
    while n != 0 :
        n >>= 1
        count += 1
    return 1 << count
|||

SMALLEST_POWER_OF_2_GREATER_THAN_OR_EQUAL_TO_N_1

def f_gold ( n ) :
    p = 1
    if n and ( n & ( n - 1 ) ) == 0 :
        return n
    while p < n :
        p <<= 1
    return p
|||

SMALLEST_SUM_CONTIGUOUS_SUBARRAY

def f_gold ( arr , n ) :
    min_ending_here = 2147483647
    min_so_far = 2147483647
    for i in range ( n ) :
        if min_ending_here > 0 :
            min_ending_here = arr [ i ]
        else :
            min_ending_here += arr [ i ]
        min_so_far = min ( min_so_far , min_ending_here )
    return min_so_far
|||

SORT_ARRAY_APPLYING_GIVEN_EQUATION

def f_gold ( arr , n , A , B , C ) :
    for i in range ( n ) :
        arr [ i ] = A * arr [ i ] * arr [ i ] + B * arr [ i ] + C
    index = - 1
    maximum = - 999999
    for i in range ( n ) :
        if maximum < arr [ i ] :
            index = i
            maximum = arr [ i ]
    i , j = 0 , n - 1
    new_arr = [ ]
    k = 0
    while i < index and j > index :
        if arr [ i ] < arr [ j ] :
            new_arr.append ( arr [ i ++ ] )
        else :
            new_arr.append ( arr [ j -- ] )
    while i < index :
        new_arr.append ( arr [ i ++ ] )
    while j > index :
        new_arr.append ( arr [ j -- ] )
    new_arr.append ( maximum )
    for p in range ( n ) :
        arr [ p ] = new_arr [ p ]
    return arr
|||

SORT_ARRAY_TWO_HALVES_SORTED

def f_gold ( A , n ) :
    A.sort ( )
|||

SORT_EVEN_NUMBERS_ASCENDING_ORDER_SORT_ODD_NUMBERS_DESCENDING_ORDER_1

def f_gold ( arr , n ) :
    for i in range ( n ) :
        if ( arr [ i ] & 1 ) :
            arr [ i ] *= - 1
    arr.sort ( )
    for i in range ( n ) :
        if ( arr [ i ] & 1 ) :
            arr [ i ] *= - 1
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
|||

SQUARED_TRIANGULAR_NUMBER_SUM_CUBES

def f_gold ( s ) :
    sum = 0
    for n in range ( 1 , s ) :
        sum += n ** 2 * n ** 2
        if sum == s :
            return n
|||

SQUARE_ROOT_OF_AN_INTEGER

def f_gold ( x ) :
    if x == 0 or x == 1 :
        return x
    i , result = 1 , 1
    while result <= x :
        i += 1
        result = i * i
    return i - 1
|||

SQUARE_ROOT_OF_AN_INTEGER_1

def f_gold ( x ) :
    if x == 0 or x == 1 :
        return x
    start , end , ans = 1 , x , 0
    while start <= end :
        mid = ( start + end ) / 2
        if mid * mid == x :
            return mid
        if mid * mid < x :
            start = mid + 1
            ans = mid
        else :
            end = mid - 1
    return ans
|||

STEINS_ALGORITHM_FOR_FINDING_GCD

def f_gold ( a , b ) :
    if a == 0 :
        return b
    if b == 0 :
        return a
    k = 0
    for ( ( a | b ) & 1 ) == 0 :
        a >>= 1
        b >>= 1
    while ( a & 1 ) == 0 :
        a >>= 1
    do :
        while ( b & 1 ) == 0 :
            b >>= 1
        if a > b :
            temp = a
            a , b = b , temp
        b = ( b - a )
    while b != 0 :
        return a << k
|||

STOOGE_SORT

def f_gold ( arr , l , h ) :
    if l >= h :
        return
    if arr [ l ] > arr [ h ] :
        t = arr [ l ]
        arr [ l ] , arr [ h ] = arr [ h ] , arr [ l ]
    if h - l + 1 > 2 :
        t = ( h - l + 1 ) // 3
        f_gold ( arr , l , h - t )
        f_gold ( arr , l + t , h )
        f_gold ( arr , l , h - t )
|||

SUBARRAYS_DISTINCT_ELEMENTS

def f_gold ( arr , n ) :
    s = set ( )
    j , ans = 0 , 0
    for i in range ( n ) :
        while j < n and not s.issubset ( arr [ j ] ) :
            s.add ( arr [ i ] )
            j += 1
        ans += ( ( j - i ) * ( j - i + 1 ) ) / 2
        s.remove ( arr [ i ] )
    return ans
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
    return ans
|||

SUM_BINOMIAL_COEFFICIENTS

def f_gold ( n ) :
    C = [ [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0
|||

SUM_BINOMIAL_COEFFICIENTS_1

def f_gold ( n ) :
    return ( 1 << n )
|||

SUM_DIVISORS_1_N_1

def f_gold ( n ) :
    sum = 0
    for i in range ( 1 , n + 1 ) :
        sum += ( n / i ) ** i
    return sum
|||

SUM_FACTORS_NUMBER

def f_gold ( n ) :
    result = 0
    for i in range ( 2 , math.sqrt ( n ) ) :
        if n % i == 0 :
            if i == ( n / i ) :
                result += i
            else :
                result += ( i + n / i )
    return ( result + n + 1 )
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
            cnt [ a [ i ] ] = cnt [ a [ i ] ] + 1
        else :
            cnt [ a [ i ] ] = 1
    return ans
|||

SUM_MATRIX_ELEMENT_ABSOLUTE_DIFFERENCE_ROW_COLUMN_NUMBERS

def f_gold ( n ) :
    arr = [ [ abs ( i - j ) for j in range ( n ) ] for i in range ( n ) ]
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
    return sum
|||

SUM_OF_ALL_ELEMENTS_UP_TO_NTH_ROW_IN_A_PASCALS_TRIANGLE_1

def f_gold ( n ) :
    sum = 0
    sum = 1 << n
    return ( sum - 1 )
|||

SUM_PAIRWISE_PRODUCTS

def f_gold ( n ) :
    sum = 0
    for i in range ( 1 , n + 1 ) :
        for j in range ( i , n + 1 ) :
            sum = sum + i * j
    return sum
|||

SUM_PAIRWISE_PRODUCTS_2

def f_gold ( n ) :
    return n * ( n + 1 ) * ( n + 2 ) * ( 3 * n + 1 ) / 24
|||

SUM_SERIES_12_32_52_2N_12

def f_gold ( n ) :
    sum = 0
    for i in range ( 1 , n + 1 ) :
        sum = sum + ( 2 ** i - 1 ) * ( 2 ** i - 1 )
    return sum
|||

SUM_SERIES_555555_N_TERMS

def f_gold ( n ) :
    return int ( 0.6172 * ( pow ( 10 , n ) - 1 ) - 0.55 * n )
|||

SUM_SUBSETS_SET_FORMED_FIRST_N_NATURAL_NUMBERS

def f_gold ( n ) :
    return ( n * ( n + 1 ) / 2 ) ** ( 1 << ( n - 1 ) )
|||

SUM_TWO_LARGE_NUMBERS

def f_gold ( str1 , str2 ) :
    if len ( str1 ) > len ( str2 ) :
        t = str1
        str1 , str2 = str2 , t
    str = ""
    n1 , n2 = len ( str1 ) , len ( str2 )
    str1 = [ str [ i ] - '0' for i in range ( n1 ) ]
    str2 = [ str [ i ] - '0' for i in range ( n2 ) ]
    carry = 0
    for i in range ( n1 ) :
        sum = ( int ( str1 [ i ] - '0' ) + int ( str2 [ i ] - '0' ) + carry )
        str += chr ( sum % 10 + '0' )
        carry = sum / 10
    for i in range ( n1 , n2 ) :
        sum = ( int ( str2 [ i ] - '0' ) + carry )
        str += chr ( sum % 10 + '0' )
        carry = sum / 10
    if carry > 0 :
        str += chr ( carry + '0' )
    str = "".join ( str )
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

def f_gold ( n , temple_height ) :
    sum = 0
    for i in range ( n ) :
        left , right = 0 , 0
        for j in range ( i - 1 , - 1 , - 1 ) :
            if temple_height [ j ] < temple_height [ j + 1 ] :
                left += 1
            else :
                break
        for j in range ( i + 1 , n ) :
            if temple_height [ j ] < temple_height [ j - 1 ] :
                right += 1
            else :
                break
        sum += max ( right , left ) + 1
    return sum
|||

TRIANGULAR_NUMBERS

def f_gold ( num ) :
    if num < 0 :
        return False
    sum = 0
    for n in range ( 1 , num + 1 ) :
        sum = sum + n
        if sum == num :
            return True
    return False
|||

TURN_OFF_THE_RIGHTMOST_SET_BIT

def f_gold ( n ) :
    return n & ( n - 1 )
|||

UNIQUE_CELLS_BINARY_MATRIX

def f_gold ( mat , n , m ) :
    rowsum = [ ]
    colsum = [ ]
    for i in range ( n ) :
        for j in range ( m ) :
            if mat [ i ] [ j ] != 0 :
                rowsum.append ( i )
                colsum.append ( j )
    uniquecount = 0
    for i in range ( n ) :
        for j in range ( m ) :
            if mat [ i ] [ j ] != 0 and rowsum [ i ] == 1 and colsum [ j ] == 1 :
                uniquecount += 1
    return uniquecount
|||

WAYS_TRANSFORMING_ONE_STRING_REMOVING_0_CHARACTERS

def f_gold ( a , b ) :
    n , m = len ( a ) , len ( b )
    if m == 0 :
        return 1
    dp = [ 0 ] * ( m + 1 ) * ( n + 1 )
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
|||

WRITE_A_C_PROGRAM_TO_CALCULATE_POWXN

def f_gold ( x , y ) :
    if y == 0 :
        return 1
    elif y % 2 == 0 :
        return f_gold ( x , y / 2 ) * f_gold ( x , y / 2 )
    else :
        return x * f_gold ( x , y / 2 ) * f_gold ( x , y / 2 )
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
|||

