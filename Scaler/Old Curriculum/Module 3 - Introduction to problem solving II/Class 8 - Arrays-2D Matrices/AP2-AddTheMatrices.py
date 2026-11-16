# Problem Description
'''
You are given two matrices A & B of same size, you have to return another matrix which is the sum of A and B.
Note: Matrices are of same size means the number of rows and number of columns of both matrices are equal.
'''

# Problem Constraints
'''
1 <= A.size(), B.size() <= 1000
1 <= A[i].size(), B[i].size() <= 1000
1 <= A[i][j], B[i][j] <= 1000
'''

# Input Format
'''
The first argument is the 2D integer array A The second argument is the 2D integer array B
'''

# Output Format
'''
You have to return a vector of vector of integers after doing required operations.
'''


class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        num_rows = len(A)
        num_cols = len(A[0]) if num_rows > 0 else 0

        resArr = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

        # Perform matrix addition
        for i in range(num_rows):
            for j in range(num_cols):
                resArr[i][j] = A[i][j] + B[i][j]

        return resArr
    
    def solve_inplace(self, A, B):
        num_rows = len(A)
        num_cols = len(A[0]) if num_rows > 0 else 0

        # Perform matrix addition in place
        for i in range(num_rows):
            for j in range(num_cols):
                A[i][j] += B[i][j]

        return A
    

# Time Complexity
'''
The time complexity of this solution is O(N*M), where N is the number of rows and M is the number of columns in the matrices A and B.
This is because we are iterating through each element of the matrices once to perform the addition.
'''

# Space Complexity
'''
The space complexity of this solution is O(1) for the in-place version as we are modifying the matrix A in place and not using any additional space that grows with input size.
For the version that creates a new result matrix, the space complexity is O(N*M) due to the additional matrix used to store the result.
'''

# Solution
'''
This solution iterates through each element of the given matrices A and B and adds the corresponding elements together.
It uses a nested loop where the outer loop iterates over rows and the inner loop iterates over columns.
The addition is done either in place, modifying the original matrix A, or by creating a new result matrix, which is then returned as the final result.
'''



import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test case 1
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        print("Input Matrix A:", A)
        print("Input Matrix B:", B)
        print("Resultant Matrix (New Matrix):", s.solve(A, B))
        print("Resultant Matrix (In-place):", s.solve_inplace(A, B))
        # Test case 2
        A = [[1, 2, 3], [4, 1, 2], [7, 8, 9]]
        B = [[9, 9, 7], [1, 2, 4], [4, 6, 3]]
        print("Input Matrix A:", A)
        print("Input Matrix B:", B)
        print("Resultant Matrix (New Matrix):", s.solve(A, B))
        print("Resultant Matrix (In-place):", s.solve_inplace(A, B))
    else:
        try:
            # Custom input
            A = eval(sys.argv[1])
            B = eval(sys.argv[2])
            print("Input Matrix A:", A)
            print("Input Matrix B:", B)
            print("Resultant Matrix (New Matrix):", s.solve(A, B))
            print("Resultant Matrix (In-place):", s.solve_inplace(A, B))
        except Exception as e:
            print("Error in input format. Please provide valid 2D matrices.")
            print("Exception:", e)
            print("Usage: python AP2-AddTheMatrices.py '[[1,2],[3,4]]' '[[5,6],[7,8]]'")
            print("Where both arguments are 2D integer matrices.")
    