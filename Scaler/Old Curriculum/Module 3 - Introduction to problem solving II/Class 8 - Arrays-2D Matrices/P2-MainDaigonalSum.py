# Problem Description
'''
You are given a N X N integer matrix. You have to find the sum of all the main diagonal elements of A.
Main diagonal of a matrix A is a collection of elements A[i, j] such that i = j.
'''

# Problem Constraints
'''
1 <= N <= 10^3
-1000 <= A[i][j] <= 1000
'''

# Input Format
'''
2D integer matrix A. [python]
There are 1 lines in the input. First 2 integers R, C are the number of rows and columns. Then R * C integers follow corresponding to the rowwise numbers in the 2D array A.
'''

# Output Format
'''
Return an integer denoting the sum of main diagonal elements.
'''

class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        main_diagonal_sum = 0

        for i in range(n):
            main_diagonal_sum += A[i][i]

        return main_diagonal_sum
    
    def solve_pythonic(self, A):
        return sum(A[i][i] for i in range(len(A)))
    
    def solve_single_line_input(self, A):
        N = int(A[0])
        M = int(A[1])

        max_ele_idx = (N*M)+1
        ele = 2
        dSum = 0
        # print(f"N: {N}, M: {M}, max_ele_idx: {max_ele_idx}")
        # print(f"A: {A}")
        # print("Calculating main diagonal sum...")

        while ele<=max_ele_idx:
            # print(f"Adding A[{ele}] = {A[ele]} to diagonal sum")
            dSum += int(A[ele])
            ele += M+1
        
        return dSum
    

# Time Complexity
'''
The time complexity of this solution is O(N), where N is the number of rows (or columns) in the matrix A.
This is because we are iterating through the main diagonal elements of the matrix exactly once.
'''

# Space Complexity
'''
The space complexity of this solution is O(1) as we are using only a constant amount of extra space to store the sum.
'''

# Solution
'''
This solution iterates through the main diagonal of the matrix and sums up the elements.
It uses a single loop that runs from 0 to N-1, where N is the number of rows (or columns) in the matrix.
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
        print(f"Input:\n{A}")
        print(f"Main diagonal sum: {s.solve(A)}\n")
        # Test case 2
        A = [3, 3, 1, -2, -3, -4, 5, -6, -7, -8, 9]
        print(f"Input (single line):\n{A}")
        print(f"Main diagonal sum: {s.solve_single_line_input(A)}\n")
    else:
        try:
            # Read input from command line arguments
            A = eval(sys.argv[1])
            print(f"Input:\n{A}")
            print(f"Main diagonal sum: {s.solve(A)}")
        except Exception as e:
            print("Error in input format. Please provide a valid 2D integer matrix.")
            print(f"Error parsing input: {e}")
            print("Usage: python P2-MainDaigonalSum.py '[[1, -2, -3], [-4, 5, -6], [-7, -8, 9]]'")
            print("Where '[[1, -2, -3], [-4, 5, -6], [-7, -8, 9]]' is the input 2D integer matrix A.")