# Problem Description
'''
You are given an integer array C of size A. Now you need to find a subarray (contiguous elements) so that the sum of contiguous elements is maximum.
But the sum must not exceed B.
'''

# Problem Constraints
'''
1 <= A <= 10^3
1 <= B <= 10^9
1 <= C[i] <= 10^6
'''

# Input Format
'''
The first argument is the integer A.
The second argument is the integer B.
The third argument is the integer array C.
'''

# Output Format
'''
Return a single integer which denotes the maximum sum.
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def maxSubarray(self, A, B, C):
        # Initialize the max_sum to 0
        max_sum = 0

        # Iterate through the array C
        for i in range(A):
            # Initialize the current_sum to 0
            current_sum = 0
            
            # Iterate through the subarray starting from index i
            for j in range(i, A):
                # Add the current element to the current_sum
                current_sum += C[j]
                
                # If the current_sum exceeds B, break the loop
                if current_sum > B:
                    break
                
                # Update max_sum if current_sum is greater
                max_sum = max(max_sum, current_sum)
        
        # Return the maximum sum found
        return max_sum


# Time Complexity
'''
The time complexity of this solution is O(N^2), where N is the size of the array C.
This is because we are using a nested loop to iterate through all possible subarrays of C.
'''

# Space Complexity
'''
The space complexity of this solution is O(1) as we are using a constant amount of extra space for variables.
'''

# Solution
'''
This solution iterates through all possible subarrays of the array C and calculates their sums.
It maintains a variable `max_sum` to keep track of the maximum sum found so far. 
For each starting index `i`, it initializes `current_sum` to 0 and iterates through the subarray starting from `i` to the end of the array. 
It adds each element to `current_sum` and checks if it exceeds B. If it does, it breaks the inner loop. 
Otherwise, it updates `max_sum` if `current_sum` is greater than the current `max_sum`.
If the sum exceeds B, it breaks the inner loop and continues with the next starting index.
'''



import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test case 1
        A = 5
        B = 12
        C = [2, 1, 3, 4, 5]
        print(f"Test case 1: Finding max subarray sum for A={A}, B={B}, C={C}")
        print("Maximum subarray sum:", s.maxSubarray(A, B, C))
        # Test case 2
        A = 3
        B = 1
        C = [2, 2, 2]
        print(f"Test case 2: Finding max subarray sum for A={A}, B={B}, C={C}")
        print("Maximum subarray sum:", s.maxSubarray(A, B, C))
    else:
        try:
            A = int(sys.argv[1])
            B = int(sys.argv[2])
            C = list(map(int, sys.argv[3].strip("[]").split(",")))
            print(f"Finding max subarray sum for A={A}, B={B}, C={C}")
            print("Maximum subarray sum:", s.maxSubarray(A, B, C))
        except Exception as e:
            print("Invalid input. Please provide a valid input.")
            print("Error:", e)
            print("Usage: python P1-MaximumSubarrayEasy.py 5 12 [2,1,3,4,5]")
            print("Where [2,1,3,4,5] is the input array C and 5 is the size of the array A, and 12 is the maximum sum B.")