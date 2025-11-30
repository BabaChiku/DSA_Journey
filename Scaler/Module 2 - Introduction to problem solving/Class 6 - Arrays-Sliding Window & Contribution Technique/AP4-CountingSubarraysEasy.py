# Problem Description
'''
Given an array A of N non-negative numbers and a non-negative number B,
you need to find the number of subarrays in A with a sum less than B.
We may assume that there is no overflow.
'''

# Problem Constraints
'''
1 <= N <= 5 x 10^3
1 <= A[i] <= 1000
1 <= B <= 10^7
'''

# Input Format
'''
First argument is an integer array A.
Second argument is an integer B.
'''

# Output Format
'''
Return an integer denoting the number of subarrays in A having sum less than B.
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        count = 0
        
        # Iterate through all possible subarrays
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += A[j]
                
                # If the sum of the current subarray is less than B, increment the count
                if current_sum < B:
                    count += 1
                else:
                    # No need to check further as the sum will only increase
                    break
                    
        return count
    

# Time Complexity
'''
The time complexity of this solution is O(N^2), where N is the size of the array A.
'''

# Space Complexity
'''
The space complexity of this solution is O(1) since we are using a constant amount of extra space.
'''

# Solution
'''
This solution uses a nested loop to iterate through all possible subarrays and count those with a sum less than B.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test case 1
        A = [2, 5, 6]
        B = 10
        print(f"In the given array A: {A} and sum B: {B}, the number of subarrays with sum less than B is: {s.solve(A, B)}")
        # Test case 2
        A = [1, 11, 2, 3, 15]
        B = 10
        print(f"In the given array A: {A} and sum B: {B}, the number of subarrays with sum less than B is: {s.solve(A, B)}")
    else:
        try:
            A = list(map(int, sys.argv[1].split(',')))
            B = int(sys.argv[2])
            print(f"In the given array A: {A} and sum B: {B}, the number of subarrays with sum less than B is: {s.solve(A, B)}")
        except Exception as e:
            print("Invalid input. Please provide the array A and integer B as input.")
            print("Error:", e)
            print("Example usage: python AP4-CountingSubarraysEasy.py 2,5,6 10")
            print("Where the first argument '2,5,6' is the array A and the second argument '10' is the integer B.")