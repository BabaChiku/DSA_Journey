# Problem Description
'''
You are given a N X N integer matrix. You have to find the sum of all the minor diagonal elements of A.
Minor diagonal of a M X M matrix A is a collection of elements A[i, j] such that i + j = M + 1 (where i, j are 1-based).
'''

# Problem Constraints
'''
1 <= N <= 10^3
-1000 <= A[i][j] <= 1000
'''

# Input Format
'''
First and only argument is a 2D integer matrix A.
'''

# Output Format
'''
Return an integer denoting the sum of minor diagonal elements.
'''


class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        minor_diagonal_sum = 0

        for i in range(n):
            minor_diagonal_sum += A[i][n - 1 - i]

        return minor_diagonal_sum


# Time Complexity
'''
The time complexity of this solution is O(N), where N is the number of rows (or columns) in the square matrix A.
This is because we are iterating through each row of the matrix once to access the corresponding minor diagonal element.
'''

# Space Complexity
'''
The space complexity of this solution is O(1) as we are using only a constant amount of extra space to store the sum of the minor diagonal elements.
'''

# Solution
'''
This solution iterates through each row of the given square matrix A and accesses the corresponding minor diagonal element using the formula A[i][n - 1 - i], where n is the size of the matrix.
It maintains a running sum of these elements in the variable minor_diagonal_sum, which is returned at the end.
'''



import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test case 1
        A = [
            [1, -2, -3],
            [-4, 5, -6],
            [-7, -8, 9]
        ]
        print("Input Matrix A:", A)
        result = s.solve(A)
        print("Minor Diagonal Sum:", result)
        # Test case 2
        A = [
            [3, 2],
            [2, 3]
        ]
        print("Input Matrix A:", A)
        result = s.solve(A)
        print("Minor Diagonal Sum:", result)
    else:
        try:
            A = eval(sys.argv[1])
            print("Input Matrix A:", A)
            result = s.solve(A)
            print("Minor Diagonal Sum:", result)
        except Exception as e:
            print("Error in input format. Please provide valid 2D matrices.")
            print("Error:", e)
            print("Usage: python AP3-MinorDiagonalSum.py '[[1,2,3],[4,5,6],[7,8,9]]'")
            print("Make sure to provide a valid 2D integer matrix as input.")