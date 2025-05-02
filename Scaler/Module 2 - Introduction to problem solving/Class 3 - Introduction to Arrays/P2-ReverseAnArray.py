# Problem Description
'''
Given an array A of N integers and also given two integers B and C. Reverse the elements of the array A within the given inclusive range [B, C].
'''

# Problem Constraints
'''
1 <= N <= 10^5
1 <= A[i] <= 10^9
0 <= B <= C <= N - 1
'''

# Input Format
'''
The first argument A is an array of integer.
The second and third arguments are integers B and C.
'''

# Output Format
'''
Return the array A after reversing in the given range.
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        # Initialize the left and right pointers
        left = B
        right = C
        
        # Loop until the left pointer is less than the right pointer
        while left < right:
            # Swap the elements at the left and right pointers
            A[left], A[right] = A[right], A[left]
            # Without using a temporary variable, we can swap the elements in the array A
            # A[left] = A[left] + A[right]
            # A[right] = A[left] - A[right]
            # A[left] = A[left] - A[right]
            # This is a common technique to swap two numbers without using a temporary variable
            # However, it is not recommended as it can lead to overflow issues in some languages
            # In Python, we can simply use the tuple unpacking method to swap the elements

            # Move the pointers towards each other
            left += 1
            right -= 1
        
        # Return the modified array A
        return A
    
# Time Complexity
'''
The time complexity of the solution is O(N) where N is the length of the array A.
This is because we are iterating through the array A once to reverse the elements in the given range.
'''

# Space Complexity
'''
The space complexity of the solution is O(1) because we are using a constant amount of extra space.
This is because we are only using a few variables to store the left and right pointers.
'''

# Solution
'''
The solution is efficient and works well for the given constraints.
The time complexity is O(N) and the space complexity is O(1).
'''

import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Example input: [1, 2, 3, 4, 5], B = 2, C = 3
        A = [1, 2, 3, 4, 5]
        B = 2
        C = 3
        print("Test case 1: Reversing A=[1, 2, 3, 4, 5] from B=2 to C=3")
        print("Output:", s.solve(A, B, C))
        # Expected output: [1, 2, 4, 3, 5]
        # Example input: [1, 2, 3, 4, 5], B = 0, C = 4
        A = [1, 2, 3, 4, 5]
        B = 0
        C = 4
        print("Test case 2: Reversing A=[1, 2, 3, 4, 5] from B=0 to C=4")
        print("Output:", s.solve(A, B, C))
        # Expected output: [5, 4, 3, 2, 1]
    else:
        try:
            # Example input: [1, 2, 3, 4, 5], B = 2, C = 3
            A = [int(x) for x in sys.argv[1].strip('[]').split(',')]
            B = int(sys.argv[2])
            C = int(sys.argv[3])
            print("Test case: Reversing A={} from B={} to C={}".format(A, B, C))
            print("Output:", s.solve(A, B, C))
        except:
            print("Invalid input. Please provide the array A and the indices B and C.")
            print("Example: python P2-ReverseAnArray.py '[1, 2, 3, 4, 5]' 2 3")
        