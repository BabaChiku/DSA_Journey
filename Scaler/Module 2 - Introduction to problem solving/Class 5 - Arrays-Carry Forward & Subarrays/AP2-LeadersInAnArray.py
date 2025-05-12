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

# Time Complexity
'''
The time complexity of this solution is O(N), where N is the length of the array A.
This is because we are iterating through the array A once to find the leaders, and the reverse operation is O(N) as well.
'''

# Space Complexity
'''
The space complexity of this solution is O(N), where N is the number of leaders found.
'''

# Solution
'''
This solution uses a single loop to find the leaders in the array A by keeping track of the maximum value seen so far from the right side of the array.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test case 1
        A = [1, 1, 3]
        print("Test case 1: Finding leaders in A=[1, 1, 3]")
        print("Leaders:", s.solve(A))
        # Test case 2
        A = [2, 1, 2]
        print("Test case 2: Finding leaders in A=[2, 1, 2]")
        print("Leaders:", s.solve(A))
    else:
        try:
            A = list(map(int, sys.argv[1].strip("[]").split(",")))
            print("Finding leaders in A =", A)
            print("Leaders:", s.solve(A))
        except Exception as e:
            print("Invalid input. Please provide a list of integers separated by commas.")
            print("Error:", e)
            print("Usage: python AP2-LeadersInAnArray.py [1,2,3]")
            print("Where [1,2,3] is the input array.")