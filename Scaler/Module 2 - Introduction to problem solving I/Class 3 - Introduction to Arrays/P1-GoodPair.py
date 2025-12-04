# Problem Description
'''
Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B). Check if any good pair exist or not.
'''

# Problem Constraints
'''
1 <= A.size() <= 10^4
1 <= A[i] <= 10^9
1 <= B <= 10^9
'''

# Input Format
'''
First argument is an integer array A.
Second argument is an integer B.
'''

# Output Format
'''
Return 1 if good pair exist otherwise return 0.
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # length of the array A
        n = len(A)
        # Loop through the array A
        for i in range(n-1):
            for j in range(i+1, n):
                # Check if A[i] + A[j] is equal to B
                if A[i] + A[j] == B:
                    return 1
        return 0
    
    def optimized_solution(self, A, B):
        # Initialize the dictionary to store the count of each element
        count = {}
        # Loop through the array A
        for i in range(len(A)):
            # Check if B - A[i] is in the dictionary
            if B - A[i] in count:
                return 1
            # Increment the count of A[i]
            count[A[i]] = count.get(A[i], 0) + 1
        return 0


# Time Complexity
'''
The time complexity of the brute force solution is O(N^2) where N is the length of the array A.
The time complexity of the optimized solution is O(N) where N is the length of the array A.
'''

# Space Complexity
'''
The space complexity of the brute force solution is O(1) because we use a constant amount of extra space.
The space complexity of the optimized solution is O(N) where N is the length of the array A.
'''

# Solution
'''
Brute force solution:
The brute force solution is to loop through the array A and for each pair of elements (i, j), check if A[i] + A[j] is equal to B. If we find such a pair, we return 1, otherwise we return 0.
Its slightly optimized by skipping the elements which are already checked. True brute force would be to check all the elements in the array.

Optimized solution:
The optimized solution is to use a dictionary to store the count of each element in the array A. We loop through the array A and for each element A[i], we check if B - A[i] is in the dictionary. If it is, we return 1. Otherwise, we increment the count of A[i] in the dictionary. If we don't find any good pair, we return 0.
'''

import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        A = [1, 2, 3, 4, 5]
        B = 6
        print("Test case 1: Good pair exist for B=6 in A=[1, 2, 3, 4, 5]")
        print(bool(s.solve(A, B)))
        print(bool(s.optimized_solution(A, B)))  # 1
        A = [1, 2, 3, 4, 5]
        B = 10
        print("Test case 2: Good pair does not exist for B=10 in A=[1, 2, 3, 4, 5]")
        print(bool(s.solve(A, B)))
        print(bool(s.optimized_solution(A, B)))  # 0
    else:
        try:
            A = list(map(int, sys.argv[1].split(',')))
            B = int(sys.argv[2])
            print(s.solve(A, B))
            print(s.optimized_solution(A, B))
        except:
            print("Invalid input. Please enter a list of integers separated by commas and an integer B.")