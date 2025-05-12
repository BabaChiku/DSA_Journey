# Problem Description
'''
Given an integer array A containing N distinct integers, you have to find all the leaders in array A. An element is a leader if it is strictly greater than all the elements to its right side.
NOTE: The rightmost element is always a leader.
'''

# Problem Constraints
'''
1 <= N <= 10^5
1 <= A[i] <= 10^8
'''

# Input Format
'''
There is a single input argument which a integer array A
'''

# Output Format
'''
Return an integer array denoting all the leader elements of the array.
'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        # Initialize the length of the array A
        n = len(A)
        # Initialize the list of leaders
        leaders = []
        # Initialize the maximum value to zero
        max_val = 0
        
        # Loop through the array A from right to left
        for i in range(n - 1, -1, -1):
            # If the current element is greater than the maximum value, it is a leader
            if A[i] > max_val:
                leaders.append(A[i])
                max_val = A[i]
        
        # Reverse the list of leaders to maintain the original order
        leaders.reverse()
        
        # Return the list of leaders
        return leaders