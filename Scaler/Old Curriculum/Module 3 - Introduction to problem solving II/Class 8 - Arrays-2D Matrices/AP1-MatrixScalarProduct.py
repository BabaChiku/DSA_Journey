# Problem Description
'''
You are given a matrix A and and an integer B, you have to perform scalar multiplication of matrix A with an integer B.
'''

# Problem Constraints
'''
1 <= A.size() <= 1000
1 <= A[i].size() <= 1000
1 <= A[i][j] <= 1000
1 <= B <= 1000
'''

# Input Format
'''
First argument is 2D array of integers A representing matrix.
Second argument is an integer B.
'''

# Output Format
'''
You have to return a 2D array of integers after doing required operations.
'''


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        num_rows = len(A)
        num_cols = len(A[0]) if num_rows > 0 else 0

        # Perform scalar multiplication
        for i in range(num_rows):
            for j in range(num_cols):
                A[i][j] *= B

        return A


# Time Complexity
'''
The time complexity of this solution is O(N*M), where N is the number of rows and M is the number of columns in the matrix A.
This is because we are iterating through each element of the matrix once to perform the scalar multiplication.
'''

# Space Complexity
'''
The space complexity of this solution is O(1) as we are modifying the matrix A in place and not using any additional space that grows with input size.
'''

# Solution
'''
This solution iterates through each element of the given matrix A and multiplies it by the scalar B.
It uses a nested loop where the outer loop iterates over rows and the inner loop iterates over columns.
The multiplication is done in place, modifying the original matrix A, which is then returned as the final result.
'''



import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test case 1
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        B = 2
        print(f"Given matrix A = {A} and scalar B = {B}\nThe matrix after scalar multiplication is: {s.solve(A, B)}")  # Expected output: [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
        # Test case 2
        A = [[1]]
        B = 5
        print(f"Given matrix A = {A} and scalar B = {B}\nThe matrix after scalar multiplication is: {s.solve(A, B)}")  # Expected output: [[5]]
    else:
        try:
            A = eval(sys.argv[1])
            B = int(sys.argv[2])
            print(f"Given matrix A = {A} and scalar B = {B}\nThe matrix after scalar multiplication is: {s.solve(A, B)}")
        except Exception as e:
            print("Error in input format. Please provide a valid 2D integer matrix and an integer scalar.")
            print(f"Error details: {e}")
            print("Usage: python AP1-MatrixScalarProduct.py '[[1,2,3],[4,5,6],[7,8,9]]' 2")
            print("Where the first argument is the matrix and the second argument is the scalar.")