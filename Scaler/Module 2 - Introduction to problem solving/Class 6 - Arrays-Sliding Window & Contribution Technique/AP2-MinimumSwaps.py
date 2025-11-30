# Problem Description
'''
Given an array of integers A and an integer B, find and return the minimum number of swaps required to bring all the numbers less than or equal to B together.
Note: It is possible to swap any two elements, not necessarily consecutive.
'''

# Problem Constraints
'''
1 <= length of the array <= 100000
-10^9 <= A[i], B <= 10^9
'''

# Input Format
'''
The first argument given is the integer array A.
The second argument given is the integer B.
'''

# Output Format
'''
Return the minimum number of swaps.
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        
        # Count how many elements are less than or equal to B
        count = sum(1 for x in A if x <= B)
        
        # If there are no such elements, no swaps are needed
        if count == 0:
            return 0
        
        # Find the number of elements greater than B in the first 'count' elements
        bad_count = sum(1 for x in A[:count] if x > B)
        
        min_swaps = bad_count
        
        # Use a sliding window to find the minimum number of bad elements in any window of size 'count'
        for i in range(count, n):
            if A[i - count] > B:
                bad_count -= 1
            if A[i] > B:
                bad_count += 1
            
            min_swaps = min(min_swaps, bad_count)
        
        return min_swaps
    

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
This solution uses a sliding window technique to find the minimum number of swaps required to bring all elements less than or equal to B together.
It first counts the number of such elements, then uses a sliding window of that size to find the window with the fewest elements greater than B, which corresponds to the minimum swaps needed.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test case 1
        A = [1, 12, 10, 3, 14, 10, 5]
        B = 8
        print("Minimum swaps required for A =", A, "and B =", B, "is:", s.solve(A, B))
        # Test case 2
        A = [5, 17, 100, 11]
        B = 20
        print("Minimum swaps required for A =", A, "and B =", B, "is:", s.solve(A, B))
    else:
        try:
            A = list(map(int, sys.argv[1].strip().split(',')))
            B = int(sys.argv[2])
            print("Minimum swaps required for A =", A, "and B =", B, "is:", s.solve(A, B))
        except Exception as e:
            print("Invalid input. Please provide the array A and integer B as input.")
            print("Error:", e)
            print("Usage: python AP2-MinimumSwaps.py 1,2,3,4,5 4")
            print("Where 1,2,3,4,5 is the input array A and 4 is B.")