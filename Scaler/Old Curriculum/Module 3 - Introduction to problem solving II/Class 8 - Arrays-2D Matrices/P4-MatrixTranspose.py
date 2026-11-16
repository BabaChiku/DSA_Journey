# Problem Description
'''
Given a 2D integer array A, return the transpose of A.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
'''

# Problem Constraints
'''
1 <= A.size() <= 1000
1 <= A[i].size() <= 1000
1 <= A[i][j] <= 1000
'''

# Input Format
'''
First argument is a 2D matrix of integers.
'''

# Output Format
'''
You have to return the Transpose of this 2D matrix.
'''


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        # Get the number of rows and columns in the original matrix
        if not A or not A[0]:
            return []

        num_rows = len(A)
        num_cols = len(A[0])
        transposed_matrix = [[0] * num_rows for _ in range(num_cols)]   # Initialize the transposed matrix with zeros

        # Fill the transposed matrix
        for i in range(num_rows):
            for j in range(num_cols):
                transposed_matrix[j][i] = A[i][j]
        return transposed_matrix


# Time Complexity
'''
    The time complexity of this solution is O(N * M), where N is the number of rows and M is the number of columns in the matrix A.
    This is because we are iterating through each element of the matrix exactly once.
'''

# Space Complexity
'''
The space complexity of this solution is O(N * M) as we are using extra space to store the transposed matrix.
'''

# Solution
'''
This solution constructs the transposed matrix by iterating through the given matrix A.
It switches the row and column indices to fill the transposed matrix.
For each element A[i][j] in the original matrix, it places it in position transposed_matrix[j][i] in the transposed matrix.
Swapping rows with columns in the same array is not feasible when the matrix is not square, hence a new matrix is created to store the result.
'''



import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test case 1
        A = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        print(f"For the matrix A = {A}\n The transpose is: {s.solve(A)}")  # Expected output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        # Test case 2
        A = [
            [1, 2]
            [1, 2]
            [1, 2]
        ]
        print(f"For the matrix A = {A}\n The transpose is: {s.solve(A)}")  # Expected output: [[1, 1, 1], [2, 2, 2]]
    else:
        try:
            # Read input from command line arguments
            A = eval(sys.argv[1])
            print(f"For the matrix A = {A}\n The transpose is: {s.solve(A)}")
        except Exception as e:
            print("Error in input format. Please provide a valid 2D integer matrix.")
            print(f"Error: {e}")
            print("Usage example: python P4-MatrixTranspose.py '[[1,2,3],[4,5,6],[7,8,9]]'")
            print("Where the input is a 2D integer matrix.")