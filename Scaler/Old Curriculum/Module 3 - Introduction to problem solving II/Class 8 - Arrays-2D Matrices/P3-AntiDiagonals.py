# Problem Description
'''
Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.
'''

# Problem Constraints
'''
1<= N <= 1000
1<= A[i][j] <= 1e9
'''

# Input Format
'''
Only argument is a 2D array A of size N * N.
'''

# Output Format
'''
Return a 2D integer array of size (2 * N-1) * N, representing the anti-diagonals of input array A.
The vacant spaces in the grid should be assigned to 0.
'''


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        N = len(A)      # number of rows
        M = len(A[0])   # number of columns
        x = min(N,M)    # number of elements in each anti-diagonal

        # Initialize the anti-diagonal matrix with zeros
        aDigMat = [[0]*x for _ in range(M+N-1)]
        row = 0

        # Fill the anti-diagonal matrix from the given matrix A starting from first row
        for k in range(M):
            i=0
            j=k
            while(i<N and j>=0):
                aDigMat[row][i]=A[i][j]
                i+=1
                j-=1
            row+=1
        
        # Fill the anti-diagonal matrix from the given matrix A starting from last column
        for k in range(1,N):
            i=k
            j=M-1
            idx=0
            while(i<N and j>=0):
                aDigMat[row][idx]=A[i][j]
                i+=1
                j-=1
                idx+=1
            row+=1
        
        return aDigMat


# Time Complexity
'''
The time complexity of this solution is O(N * N), where N is the number of rows (or columns) in the matrix A.
This is because we are iterating through each element of the matrix exactly once to fill the anti-diagonal matrix.
'''

# Space Complexity
'''
The space complexity of this solution is O(N * N) as we are using extra space to store the anti-diagonal matrix.
'''

# Solution
'''
This solution constructs the anti-diagonal matrix by iterating through the given matrix A.
It first fills the anti-diagonals starting from the first row and then fills the remaining anti-diagonals starting from the last column.
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
        print(f"For the matrix A = {A}\n The anti-diagonals are: {s.diagonal(A)}")  # Expected output: [[1, 0, 0], [2, 4, 0], [3, 5, 7], [6, 8, 0], [9, 0, 0]]

        # Test case 2
        A = [
            [1, 2],
            [3, 4]
        ]
        print(f"For the matrix A = {A}\n The anti-diagonals are: {s.diagonal(A)}")  # Expected output: [[1, 0], [2, 3], [4, 0]]
    else:
        try:
            A = eval(sys.argv[1])
            print(f"For the matrix A = {A}\n The anti-diagonals are: {s.diagonal(A)}")
        except Exception as e:
            print("Error in input format. Please provide a valid 2D integer matrix.")
            print(f"Error: {e}")
            print("Usage: python P3-AntiDiagonals.py '[[1,2,3],[4,5,6],[7,8,9]]'")
            print("Where the input is a 2D integer matrix.")