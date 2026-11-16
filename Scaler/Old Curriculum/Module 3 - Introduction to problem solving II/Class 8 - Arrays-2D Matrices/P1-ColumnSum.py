# Problem Description
'''
You are given a 2D integer matrix A, return a 1D integer array containing column-wise sums of original matrix.
'''

# Problem Constraints
'''
1 <= A.size() <= 10^3
1 <= A[i].size() <= 10^3
1 <= A[i][j] <= 10^3
'''

# Input Format
'''
First argument is a 2D array of integers.(2D matrix).
'''

# Output Format
'''
Return a single integer which denotes the maximum sum.
'''


class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        if not A or not A[0]:
            return []

        num_rows = len(A)
        num_cols = len(A[0])
        column_sums = [0] * num_cols

        for j in range(num_cols):
            for i in range(num_rows):
                column_sums[j] += A[i][j]

        return column_sums


# Time Complexity
'''
The time complexity of this solution is O(N * M), where N is the number of rows and M is the number of columns in the matrix A.
This is because we are iterating through each element of the matrix exactly once.
'''

# Space Complexity
'''
The space complexity of this solution is O(M) as we are using an extra array of size M to store the column sums.
'''

# Solution
'''
This solution iterates through each column of the matrix and sums up the elements in that column.
It uses a nested loop where the outer loop iterates over columns and the inner loop iterates over rows.
The sum for each column is stored in the `column_sums` array, which is returned as the final result.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test case 1
        A = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 2, 3, 4]
        ]
        print(f"Input:\n{A}")
        print(f"Column-wise sums: {s.solve(A)}\n")
    else:
        try:
            # Read input from command line arguments
            A = eval(sys.argv[1])
            print(f"Input:\n{A}")
            print(f"Column-wise sums: {s.solve(A)}\n")
        except Exception as e:
            print(f"Invalid input format. Please provide a valid 2D integer matrix.\n")
            print(f"Error parsing input: {e}\n")
            print("Usage: python P1-ColumnSum.py '[[1,2,3,4],[5,6,7,8],[9,2,3,4]]'")
            print("Where the matrix is provided as a string argument.")
