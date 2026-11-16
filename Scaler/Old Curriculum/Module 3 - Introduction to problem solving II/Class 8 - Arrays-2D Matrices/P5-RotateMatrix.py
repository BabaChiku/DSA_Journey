# Problem Description
'''
You are given a n x n 2D matrix A representing an image.
Rotate the image by 90 degrees (clockwise).
You need to do this in place.
Note: If you end up using an additional array, you will only receive partial score.
'''

# Problem Constraints
'''
1 <= n <= 1000
'''

# Input Format
'''
First argument is a 2D matrix A of integers
'''

# Output Format
'''
Return the 2D rotated matrix.
'''


class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        n = len(A)
        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        # Reverse each row
        for i in range(n):
            A[i].reverse()
        return A
    
    def solve_expanded(self, A):
        N = len(A)      # number of rows
        # Check if the matrix is empty
        if N==0:
            return A
        M = len(A[0])   # number of columns

        # Transpose the matrix
        for i in range(N):
            for j in range(i+1, M):
                temp = A[i][j]
                A[i][j] = A[j][i]
                A[j][i] = temp
        
        # Reverse each row
        for i in range(N):
            l = 0
            r = M-1
            while(l<r):
                temp = A[i][l]
                A[i][l] = A[i][r]
                A[i][r] = temp
                l+=1
                r-=1
        
        return A


# Time Complexity
'''
The time complexity of this solution is O(N^2), where N is the number of rows (or columns) in the matrix A.
This is because we are iterating through each element of the matrix twice: once for transposing and once for reversing each row.
'''

# Space Complexity
'''
The space complexity of this solution is O(1) as we are performing the rotation in place without using any extra space.
'''

# Solution
'''
This solution first transposes the matrix by swapping elements across the main diagonal.
After transposing, it reverses each row to achieve the 90-degree clockwise rotation.
The transposition is done using a nested loop where the outer loop iterates over rows and the inner loop iterates over columns starting from the current row index.
Reversing each row is done using a two-pointer approach, swapping elements from the start and end of the row until they meet in the middle.

180-degree rotation can be achieved by reversing each row and then reversing each column.
270-degree rotation can be achieved by transposing the matrix and then reversing each column or by reversing each row followed by transposing the matrix.
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
        print(f"For the matrix A = {A}\n The rotated matrix is: {s.solve(A)}")  # Expected output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        # Test case 2
        A = [
            [1, 2],
            [3, 4]
        ]
        print(f"For the matrix A = {A}\n The rotated matrix is: {s.solve(A)}")  # Expected output: [[3, 1], [4, 2]]
    else:
        try:
            # Read input from command line arguments
            A = eval(sys.argv[1])
            print(f"For the matrix A = {A}\n The rotated matrix is: {s.solve(A)}")
        except Exception as e:
            print("Error in input format. Please provide a valid 2D integer matrix.")
            print(f"Error: {e}")
            print("Usage example: python P5-RotateMatrix.py '[[1,2,3],[4,5,6],[7,8,9]]'")
            print("Where the input matrix is provided as a string argument.")