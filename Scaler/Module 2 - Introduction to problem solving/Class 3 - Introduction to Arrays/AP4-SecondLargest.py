# Problem Description
'''
You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.
'''

# Problem Constraints
'''
1 <= |A| <= 10^5
0 <= A[i] <= 10^9
'''

# Input Format
'''
The first argument is an integer array A.
'''

# Output Format
'''
Return the second largest element. If no such element exist then return -1.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Find the length of the array A
        n = len(A)
        # If the length of the array A is less than or equal to 1, return -1
        if n <= 1:
            return -1
        # Initialize the first and second largest variables to -1
        first_largest = -1
        second_largest = -1
        # Loop through the array A to find the first and second largest elements using two pointers
        i = 0
        j = n - 1
        while i < j:
            # Check if A[i] is greater than A[j]
            if A[i] > A[j]:
                # If A[i] is greater, check if it is greater than first_largest
                if A[i] > first_largest:
                    # If A[i] is greater than first_largest, set second_largest to first_largest and first_largest to A[i]
                    second_largest = first_largest
                    first_largest = A[i]
                elif A[i] > second_largest and A[i] != first_largest:
                    # If A[i] is not greater than first_largest but greater than second_largest, set second_largest to A[i]
                    second_largest = A[i]
            elif A[j] > A[i]:
                # If A[j] is greater, check if it is greater than first_largest
                if A[j] > first_largest:
                    # If A[j] is greater than first_largest, set second_largest to first_largest and first_largest to A[j]
                    second_largest = first_largest
                    first_largest = A[j]
                elif A[j] > second_largest and A[j] != first_largest:
                    # If A[j] is not greater than first_largest but greater than second_largest, set second_largest to A[j]
                    second_largest = A[j]
            # Move the pointers towards each other
            i += 1
            j -= 1
        
        # If i is equal to j
        if i == j:
            # Check if A[i] is greater than first_largest
            if A[i] > first_largest:
                # If A[i] is greater than first_largest, set second_largest to first_largest and first_largest to A[i]
                second_largest = first_largest
                first_largest = A[i]
            elif A[i] > second_largest and A[i] != first_largest:
                # If A[i] is not greater than first_largest but greater than second_largest, set second_largest to A[i]
                second_largest = A[i]
        
        # Return second_largest
        return second_largest


# Time Complexity
'''
The time complexity of the solution is O(N) where N is the length of the array A.
This is because we are iterating through the array A once to find the first and second largest elements.
'''

# Space Complexity
'''
The space complexity of the solution is O(1) because we are using a constant amount of extra space.
This is because we are only using a few variables to store the first and second largest elements.
'''

# Solution
'''
The solution is to use two pointers to find the first and second largest elements in the array A.
We can do this by iterating through the array A and comparing the elements at the two pointers. 
If we find an element that is greater than the first largest, we set the second largest to the first largest and the first largest to the current element.
If we find an element that is greater than the second largest but not greater than the first largest, we set the second largest to the current element. 
Finally, we return the second largest element.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Example input: [1, 2, 3, 4, 5]
        A = [1, 2, 3, 4, 5]
        print("Test case 1: Finding second largest element in A=[1, 2, 3, 4, 5]")
        print("Output:", s.solve(A))
        # Expected output: 4
        # Example input: [1]
        A = [1]
        print("Test case 2: Finding second largest element in A=[1]")
        print("Output:", s.solve(A))
        # Expected output: -1
    else:
        try:
            A = list(map(int, sys.argv[1].strip('[]').split(',')))
            print("Test case 3: Finding second largest element in A={}".format(A))
            print("Output:", s.solve(A))
        except Exception as e:
            print("Invalid input, please provide a valid integer array.")
            print("Error:", e)
            print("Usage: python AP4-SecondLargest.py [1,2,3,4,5]")
            print("Where [1, 2, 3, 4, 5] is the input array.")