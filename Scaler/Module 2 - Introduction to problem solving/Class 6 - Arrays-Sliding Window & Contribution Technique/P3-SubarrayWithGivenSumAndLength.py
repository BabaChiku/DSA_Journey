# Problem Description
'''
Given an array A of length N. Also given are integers B and C.
Return 1 if there exists a subarray with length B having sum C and 0 otherwise
'''

# Problem Constraints
'''
1 <= N <= 10^5
1 <= A[i] <= 10^4
1 <= B <= N
1 <= C <= 10^9
'''

# Input Format
'''
First argument A is an array of integers.
The remaining arguments B and C are integers
'''

# Output Format
'''
Return 1 if such a subarray exist and 0 otherwise.
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        n = len(A) # length of the array
        # Edge case: if B is greater than the length of the array, return 0
        if B > n: 
            return 0
        
        # Calculate the sum of the first window of size B
        window_sum = sum(A[:B])
        
        # Check if the sum of the first window is equal to C
        if window_sum == C:
            return 1
        
        # Slide the window from start to end of the array
        for i in range(B, n):
            # Update the window sum by removing the first element of the previous window and adding the new element
            window_sum += A[i] - A[i - B]
            
            # Check if the current window sum is equal to C
            if window_sum == C:
                return 1
        
        return 0
    

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
This solution uses the sliding window technique to efficiently find a subarray of length B with sum C. 
It first calculates the sum of the initial window of size B and then iteratively updates the sum by sliding the window one element at a time. 
If at any point the sum of the current window equals C, the function returns 1. If no such subarray is found by the end of the array, it returns 0.
'''