# Problem Description
'''
Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:
1. Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.
2. Length of the subarray is be odd, and the sum of all the elements of the subarray must be greater than B.
Your task is to find the count of good subarrays in A.
'''

# Problem Constraints
'''
1 <= len(A) <= 5 x 10^3
1 <= A[i] <= 10^3
1 <= B <= 10^7
'''

# Input Format
'''
The first argument given is the integer array A.
The second argument given is an integer B.
'''

# Output Format
'''
Return the count of good subarrays in A.
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        good_subarray_count = 0
        
        # Iterate through all possible subarrays
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += A[j]
                length = j - i + 1
                
                # Check the conditions for a good subarray
                if (length % 2 == 0 and current_sum < B) or (length % 2 == 1 and current_sum > B):
                    good_subarray_count += 1
                    
        return good_subarray_count
    

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
This solution uses a nested loop to iterate through all possible subarrays and calculates their sums. 
It then checks the conditions for a good subarray based on the length and sum, and counts the number of good subarrays.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test case 1
        A = [1, 2, 3, 4, 5]
        B = 4
        print("Count of good subarrays for A =", A, "and B =", B)
        print("Good subarray count:", s.solve(A, B))
        # Test case 2
        A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
        B = 65
        print("Count of good subarrays for A =", A, "and B =", B)
        print("Good subarray count:", s.solve(A, B))
    else:
        try:
            A = list(map(int, sys.argv[1].split(',')))
            B = int(sys.argv[2])
            print("Count of good subarrays for A =", A, "and B =", B)
            print("Good subarray count:", s.solve(A, B))
        except Exception as e:
            print("Invalid input. Please provide the array A and integer B as input.")
            print("Error:", e)
            print("Usage: python AP1-GoodSubarraysEasy.py 1,2,3,4,5 4")
            print("Where 1,2,3,4,5 is the input array A and 4 is B.")