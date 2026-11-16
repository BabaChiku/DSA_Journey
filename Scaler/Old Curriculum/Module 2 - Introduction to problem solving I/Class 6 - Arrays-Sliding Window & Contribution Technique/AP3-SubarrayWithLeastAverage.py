# Problem Description
'''
Given an array A of size N, find the subarray of size B with the least average.
'''

# Problem Constraints
'''
1 <= B <= N <= 10^5
-10^5 <= A[i] <= 10^5
'''

# Input Format
'''
First argument contains an array A of integers of size N.
Second argument contains integer B.
'''

# Output Format
'''
Return the index of the first element of the subarray of size B that has least average.
Array indexing starts from 0.
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        
        # Calculate the sum of the first 'B' elements
        current_sum = sum(A[:B])
        min_sum = current_sum
        min_index = 0
        
        # Use a sliding window to find the subarray with the least sum
        for i in range(B, n):
            current_sum += A[i] - A[i - B]
            if current_sum < min_sum:
                min_sum = current_sum
                min_index = i - B + 1
        
        return min_index
    

# Time Complexity
'''
The time complexity of this solution is O(N), where N is the size of the array A.
'''

# Space Complexity
'''
The space complexity of this solution is O(1) since we are using a constant amount of extra space.
'''

# Solution
'''
This solution uses a sliding window technique to efficiently find the subarray of size B with the least average.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test case 1
        A = [3, 7, 90, 20, 10, 50, 40]
        B = 3
        print(f"Minimum average subarray in array {A} of size {B} starts at index: {s.solve(A, B)}")  # Expected output: 3
        # Test case 2
        A = [3, 7, 5, 20, -10, 0, 12]
        B = 2
        print(f"Minimum average subarray in array {A} of size {B} starts at index: {s.solve(A, B)}")  # Expected output: 4
    else:
        try:
            # Read input from command line arguments
            A = list(map(int, sys.argv[1].strip().split(',')))
            B = int(sys.argv[2])
            print(f"Minimum average subarray in array {A} of size {B} starts at index: {s.solve(A, B)}")
        except Exception as e:
            print("Invalid input. Please provide the array A and integer B as input.")
            print("Error:", e)
            print("Example usage: python AP3-SubarrayWithLeastAverage.py 3,7,90,20,10,50,40 3")
            print("Where 3,7,90,20,10,50,40 is the input array A and 3 is B.")