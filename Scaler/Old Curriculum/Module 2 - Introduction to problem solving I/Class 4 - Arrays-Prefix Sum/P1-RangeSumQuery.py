# Problem Description
'''
You are given an integer array A of length N.
You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
For each query, you have to find the sum of all elements from L to R indices in A (0 - indexed).
More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.
'''

# Problem Constraints
'''
1 <= N, M <= 10^5
1 <= A[i] <= 10^9
0 <= L <= R < N
'''

# Input Format
'''
The first argument is the integer array A.
The second argument is the 2D integer array B.
'''

# Output Format
'''
Return an integer array of length M where i-th element is the answer for i-th query in B.
'''

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):
        # Find the length of the array A
        n = len(A)
        # Find the length of the array B
        m = len(B)
        # Initialize the the result array with zeros
        result = [0] * m
        # Initialize the prefix sum array with zeros
        prefix_sum = [0] * (n + 1)
        # Calculate the prefix sum of the array A
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]
        # Loop through the array B to calculate the sum for each query
        for i in range(m):
            # Get the left and right indices from the query
            L = B[i][0]
            R = B[i][1]
            # Calculate the sum from L to R using the prefix sum array
            result[i] = prefix_sum[R + 1] - prefix_sum[L]
        # Return the result array
        return result
    
    def optimized_rangeSum(self, A, B):
        # Find the length of the array A
        n = len(A)
        # Find the length of the array B
        m = len(B)
        # Initialize the result array with zeros
        result = [0] * m
        # Calculate the prefix sum of the array A using a single loop
        for i in range(1, n):
            A[i] = A[i - 1] + A[i]
        # Loop through the array B to calculate the sum for each query using a single loop
        for i in range(m):
            # Get the left and right indices from the query
            L = B[i][0]
            R = B[i][1]
            # Calculate the sum from L to R using the prefix sum array in a single line
            if L == 0:
                result[i] = A[R]
            else:
                result[i] = A[R] - A[L-1]
        # Return the result array
        return result


# Time Complexity
'''
The time complexity of the rangeSum function is O(N + M), where N is the length of the array A and M is the number of queries in B.
The time complexity of the optimized_rangeSum function is O(N + M) as well.
'''

# Space Complexity
'''
The space complexity of the rangeSum function is O(N) for the prefix sum array.
The space complexity of the optimized_rangeSum function is O(1) as it modifies the input array A in place.
'''

# Solution
'''
This solution uses the prefix sum technique to efficiently calculate the sum of elements in a given range.
The prefix sum array is constructed in O(N) time, and each query can be answered in O(1) time using the prefix sum array.
The optimized solution modifies the input array A in place to save space, but it may not be suitable if the original array needs to be preserved.
Also, the optimized solution is needs to handle the case when L = 0 separately to avoid index out of range error.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test case 1
        A = [1, 2, 3, 4, 5]
        B = [[0, 2], [1, 3], [2, 4]]
        print("Test case 1: Finding sum of elements in A=[1, 2, 3, 4, 5] for queries B=[[0, 2], [1, 3], [2, 4]]")
        print("Output:", s.rangeSum(A, B))  # Expected output: [6, 9, 12]
        print("Optimized Output:", s.optimized_rangeSum(A, B))
        # Expected output: [6, 9, 12]
        # Test case 2
        A = [2, 2, 2]
        B = [[0, 0], [1, 2]]
        print("Test case 2: Finding sum of elements in A=[2, 2, 2] for queries B=[[0, 0], [1, 2]]")
        print("Output:", s.rangeSum(A, B))  # Expected output: [2, 6]
        print("Optimized Output:", s.optimized_rangeSum(A, B))
    else:
        try:
            # Read input from command line arguments
            A = list(map(int, sys.argv[1].strip('[]').split(',')))
            # If there are only three arguments
            if len(sys.argv) == 3:
                B = [list(map(int, x.strip('[]').split(','))) for x in sys.argv[2].strip('[]').split('],[')]
            # If there are more than three arguments
            else:
                B = [list(map(int, x.strip('[]').split(','))) for x in sys.argv[2:]]
            print("Input A:", A)
            print("Input B:", B)
            print("Output:", s.rangeSum(A, B))
            print("Optimized Output:", s.optimized_rangeSum(A, B))
        except Exception as e:
            print("Invalid input, please provide a valid input format.")
            print("Error:", e)
            print("Usage: python P1-RangeSumQuery.py [1,2,3,4,5] [[0,2],[1,3],[2,4]]")
            print("Where [1,2,3,4,5] is the array A and [[0,2],[1,3],[2,4]] are the queries in B.")

