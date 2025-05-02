# Problem Description
'''
Given an array, arr[] of size N, the task is to find the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.
'''

# Problem Constraints
'''
1 <= N <= 10^5
-10^5 <= A[i] <= 10^5
Sum of all elements of A <= 10^9
'''

# Input Format
'''
First argument contains an array A of integers of size N
'''

# Output Format
'''
Return the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Initialize the length of the array A
        n = len(A)
        # Check if the length of A is less than or equal to 1
        if n <= 1:
            # If true, return 0 as there are no special indices
            return 0
        # Initialize the even prefix sum array with zeros
        prefix_sum_even = [0] * n
        # Initialize the odd prefix sum array with zeros
        prefix_sum_odd = [0] * n
        # Initialize the count of special indices to zero
        count = 0
        # Initialize the first element of the even prefix sum array
        prefix_sum_even[0] = A[0]
        # Initialize the first element of the odd prefix sum array
        prefix_sum_odd[0] = 0
        # Calculate the prefix sums for even and odd indices
        for i in range(1, n):
            if i % 2 == 0:
                prefix_sum_even[i] = prefix_sum_even[i - 1] + A[i]
                prefix_sum_odd[i] = prefix_sum_odd[i - 1]
            else:
                prefix_sum_odd[i] = prefix_sum_odd[i - 1] + A[i]
                prefix_sum_even[i] = prefix_sum_even[i - 1]
        
        # Check if the last element of the even prefix sum array is equal to the last element of the odd prefix sum array. [Edge case]
        if prefix_sum_even[n - 1] == prefix_sum_odd[n - 1]:
            # If true, increment the count by 1. This indicates that the first index is a special index.
            count += 1
        
        # Loop through the array A to find special indices
        for i in range(1, n):
            # Calculate the sum of even and odd indexed elements after removing A[i]
            if i % 2 == 0:
                even_sum = prefix_sum_even[i - 1] + (prefix_sum_odd[n - 1] - prefix_sum_odd[i])
                odd_sum = prefix_sum_odd[i - 1] + (prefix_sum_even[n - 1] - prefix_sum_even[i])
            else:
                even_sum = prefix_sum_even[i - 1] + (prefix_sum_odd[n - 1] - prefix_sum_odd[i])
                odd_sum = prefix_sum_odd[i - 1] + (prefix_sum_even[n - 1] - prefix_sum_even[i])

            # Check if the sums are equal after removing A[i]
            if even_sum == odd_sum:
                count += 1
        
        # Return the count of special indices
        return count
    
    def edge_case_free(self, A):
        # Initialize the length of the array A
        n = len(A)
        # Initialize the even prefix sum array with zeros
        prefix_sum_even = [0] * (n + 1)
        # Initialize the odd prefix sum array with zeros
        prefix_sum_odd = [0] * (n + 1)
        # Initialize the count of special indices to zero
        count = 0
        # Calculate the prefix sums for even and odd indices
        for i in range(n):
            if i % 2 == 0: # If the index is even
                prefix_sum_even[i + 1] = prefix_sum_even[i] + A[i]
                prefix_sum_odd[i + 1] = prefix_sum_odd[i]
            else: # If the index is odd
                prefix_sum_odd[i + 1] = prefix_sum_odd[i] + A[i]
                prefix_sum_even[i + 1] = prefix_sum_even[i]
        
        # Loop through the array A to find special indices
        for i in range(n):
            # Calculate the sum of even and odd indexed elements after removing A[i]
            if i % 2 == 0:
                even_sum = prefix_sum_even[i] + (prefix_sum_odd[n] - prefix_sum_odd[i + 1])
                odd_sum = prefix_sum_odd[i] + (prefix_sum_even[n] - prefix_sum_even[i + 1])
            else:
                even_sum = prefix_sum_even[i] + (prefix_sum_odd[n] - prefix_sum_odd[i + 1])
                odd_sum = prefix_sum_odd[i] + (prefix_sum_even[n] - prefix_sum_even[i + 1])

            # Check if the sums are equal after removing A[i]
            if even_sum == odd_sum:
                count += 1
        
        # Return the count of special indices
        return count

# Time Complexity
'''
The time complexity of the solve function is O(N), where N is the length of the array A. This is because we are iterating through the array A twice: once to calculate the prefix sums and once to find the special indices.
'''

# Space Complexity
'''
The space complexity of the solve function is O(N) for the prefix sum arrays.
This is because we are using two additional arrays of size N to store the prefix sums.
'''

# Solution
'''
This solution uses the prefix sum technique to efficiently calculate the count of special indices in the array A.
The odd and even indexed prefix sums are calculated in a single pass, and the special indices are found in another pass.
The prefix_sum_even array stores the sum of elements at even indices, and the prefix_sum_odd array stores the sum of elements at odd indices.
To calculate the prefix sums, we check if the index is even or odd. If the index is even, we add the current element to the even prefix sum and keep the odd prefix sum unchanged, by initializing it with the previous value. If the index is odd, we add the current element to the odd prefix sum and keep the even prefix sum unchanged, by initializing it with the previous value.
To find the special indices, we loop through the array A and calculate the sum of even and odd indexed elements after removing A[i]. We check if the sums are equal after removing A[i]. If they are equal, we increment the count of special indices.
To calculate the sum of even and odd indexed elements after removing A[i], we use the prefix sums to get the sum of elements before and after index i.
After removing an at index i, the even indexed elements become odd indexed and vice versa. So, we need to adjust the prefix sums accordingly.
For even sum, we add the prefix sum of even indexed elements before index i and the prefix sum of odd indexed elements after index i. For odd sum, we add the prefix sum of odd indexed elements before index i and the prefix sum of even indexed elements after index i.
Finally, we return the count of special indices.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Example input: [2, 1, 6, 4], Expected output: 1
        A = [2, 1, 6, 4]
        print("Test case 1: Finding special indices in A=[2, 1, 6, 4]")
        print("Special Indices Count:", s.solve(A))
        print("Special Indices Count (Edge Case Free):", s.edge_case_free(A))
        # Example input: [1, 1, 1], Expected output: 3
        A = [1, 1, 1]
        print("Test case 2: Finding special indices in A=[1, 1, 1]")
        print("Special Indices Count:", s.solve(A))
        print("Special Indices Count (Edge Case Free):", s.edge_case_free(A))
    else:
        try:
            A = list(map(int, sys.argv[1].strip('[]').split(',')))
            print("Input array:", A)
            print("Special Indices Count:", s.solve(A))
            print("Special Indices Count (Edge Case Free):", s.edge_case_free(A))
        except Exception as e:
            print("Invalid input, please provide a valid array.")
            print("Error:", e)
            print("Usage: python P2-SpecialIndex.py [array]")
            print("Example: python P2-SpecialIndex.py [2,1,6,4]")
            print("Where array is a comma-separated list of integers enclosed in square brackets.")