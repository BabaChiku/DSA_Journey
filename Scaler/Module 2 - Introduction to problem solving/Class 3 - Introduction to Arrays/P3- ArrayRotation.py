# Problem Description
'''
Given an integer array A of size N and an integer B, you have to return the same array after rotating it B times towards the right.
'''

# Problem Constraints
'''
1 <= N <= 10^5
1 <= A[i] <=10^9
1 <= B <= 10^9
'''

# Input Format
'''
The first argument given is the integer array A.
The second argument given is the integer B.
'''

# Output Format
'''
Return the array A after rotating it B times to the right.
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        # Get the length of the array A
        n = len(A)
        # Calculate the effective number of rotations needed
        B = B % n

        # If B is 0, return the original array A
        if B == 0:
            return A
        
        # Reverse the entire array A
        i = 0
        j = n - 1
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

        # Reverse the first B elements of the array A
        i = 0
        j = B - 1
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

        # Reverse the remaining n - B elements of the array A
        i = B
        j = n - 1
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

        # Return the modified array A
        return A
    

# Time Complexity
'''
The time complexity of the solution is O(N) where N is the length of the array A.
This is because we are reversing the array A three times, each taking O(N) time.
'''

# Space Complexity
'''
The space complexity of the solution is O(1) because we are not using any extra space to store the result.
This is because we are modifying the array A in place.
'''

# Solution
'''
The solution uses the reverse method to rotate the array A B times to the right.
The idea is to reverse the entire array A, then reverse the first B elements, and finally reverse the remaining n - B elements. This will give us the desired result of rotating the array A B times to the right.
'''

import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Example input: [1, 2, 3, 4, 5], B = 2
        A = [1, 2, 3, 4, 5]
        B = 2
        result = s.solve(A, B)
        print("Test case 1: Rotating A=[1, 2, 3, 4, 5] B=2 times")
        print("Output:", result)
        # Expected output: [4, 5, 1, 2, 3]
        # Example input: [1, 2, 3, 4, 5], B = 7
        A = [1, 2, 3, 4, 5]
        B = 7
        result = s.solve(A, B)
        print("Test case 2: Rotating A=[1, 2, 3, 4, 5] B=7 times")
        print("Output:", result)
        # Expected output: [4, 5, 1, 2, 3]
    else:
        try:
            A = list(map(int, sys.argv[1].strip('[]').split(',')))
            B = int(sys.argv[2])
            result = s.solve(A, B)
            print("Test case: Rotating A={} B={} times".format(A, B))
            print("Output:", result)
        except Exception as e:
            print("Invalid input. Please provide the array A and the integer B.")
            print("Error:", e)
            print("Usage: python script.py [1, 2, 3, 4, 5] 2")
            print("Where [1, 2, 3, 4, 5] is the array and 2 is the number of rotations.")
