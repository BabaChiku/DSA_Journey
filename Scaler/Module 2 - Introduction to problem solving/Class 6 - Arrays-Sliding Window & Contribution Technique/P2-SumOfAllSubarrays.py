# Problem Description
'''
You are given an integer array A of length N.
You have to find the sum of all subarray sums of A.
More formally, a subarray is defined as a contiguous part of an array which we can obtain by deleting zero or more elements from either end of the array.
A subarray sum denotes the sum of all the elements of that subarray.

Note : Be careful of integer overflow issues while calculations. Use appropriate datatypes.
'''

# Problem Constraints
'''
1 <= N <= 10^5
1 <= Ai <= 10^4
'''

# Input Format
'''
The first argument is the integer array A.
'''

# Output Format
'''
Return a single integer denoting the sum of all subarray sums of the given array.
'''

class Solution:
    # @param A : list of integers
     # @return an long
    def subarraySum(self, A):
        n = len(A)
        total_sum = 0
        
        # Iterate through each element in the array
        for i in range(n):
            # Calculate the contribution of A[i] to the total sum
            contribution = A[i] * (i + 1) * (n - i)
            total_sum += contribution
            
        return total_sum


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
This solution calculates the sum of all subarray sums by iterating through each element in the array and calculating its contribution to the total sum based on its position.
The contribution of each element A[i] is determined by how many subarrays it can be part of, which is given by (i + 1) * (n - i), where n is the length of the array.
This approach ensures that we efficiently compute the result in linear time without needing to explicitly generate all subarrays.
'''



import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test case 1
        A = [1, 2, 3]
        print("Finding sum of all subarray sums for A =", A)
        print("Sum of all subarray sums:", s.subarraySum(A))
        # Test case 2
        A = [2, 1, 3]
        print("Finding sum of all subarray sums for A =", A)
        print("Sum of all subarray sums:", s.subarraySum(A))
    else:
        try:
            A = list(map(int, sys.argv[1].strip("[]").split(",")))
            print(f"Finding sum of all subarray sums for A = {A}")
            print("Sum of all subarray sums:", s.subarraySum(A))
        except Exception as e:
            print("Invalid input. Please provide list of integers as input.")
            print("Error:", e)
            print("Usage: python P2-SumOfAllSubarrays.py [2,1,3,4,5]")
            print("Where [2,1,3,4,5] is the input array A.")