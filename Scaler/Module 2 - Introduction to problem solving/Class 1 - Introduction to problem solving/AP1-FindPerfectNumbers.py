# Problem Description
'''
You are given an integer A. You have to tell whether it is a perfect number or not.

Perfect number is a positive integer which is equal to the sum of its proper positive divisors.

A proper divisor of a natural number is the divisor that is strictly less than the number.

'''

# Problem Constraints
'''
1 <= A <= 106
'''

# Input Format
'''
First and only argument contains a single positive integer A.
'''

# Output Format
'''
Return 1 if A is a perfect number and 0 otherwise.
'''

class Solution:
    # @param A : integer
    # @return an integer
    def isPerfect(self, A):
        # Check if A is less than 2
        if A < 2:
            return 0
        # Initialize the sum of factors to 1
        sum_of_factors = 1
        # Loop from 2 to the square root of A (inclusive)
        for i in range(2, int(A**0.5)+1):
            # Check if i is a factor of A
            if A % i == 0:
                # Add i to the sum of factors
                sum_of_factors += i
                # Check if the corresponding factor is different from i
                if i != A // i:
                    # Add the corresponding factor to the sum of factors
                    sum_of_factors += A // i
        # Check if the sum of factors is equal to A
        if sum_of_factors == A:
            return 1
        return 0
    
    def isPerfectOptimized(self, A):
        # Check if A is less than 2
        if A < 2:
            return 0
        # Check if A is a perfect square
        if (int(A**0.5))**2 == A:
            return 0
        # Check if A is odd
        if A%2!=0:
            return 0
        # Initialize the sum of factors to 1
        sum_of_factors = 1
        # Loop from 2 to the square root of A (inclusive)
        for i in range(2, int(A**0.5)+1):
            # Check if i is a factor of A
            if A % i == 0:
                # Add i to the sum of factors
                sum_of_factors += i
                # Add the corresponding factor to the sum of factors
                sum_of_factors += A // i
            # Check if the sum of factors is greater than A
            if sum_of_factors > A:
                return 0
        # Check if the sum of factors is equal to A
        if sum_of_factors == A:
            return 1
        return 0


# Time Complexity
'''
The time complexity of this solution is O(sqrt(A)) because we loop from 2 to the square root of A.
'''

# Space Complexity
'''
The space complexity of this solution is O(1) because we use a constant amount of extra space.
'''

# Optimized Approach
'''
We can optimize the solution by checking if A is odd, a perfect square.
Then we can loop from 2 to the square root of A.
While adding the factors to the sum of factors and checking if the sum of factors is greater than A to prevent unnecessary iterations.

** There has been no proven perfect odd number found yet, so we can check if A is odd and return 0.
** A perfect square is never a perfect even number, so we can check if A is a perfect square and return 0.
'''

import sys

if __name__ == "__main__":
    s = Solution()

    if len(sys.argv) != 2:
        # Test cases to validate the solution
        test_cases = [6, 28, 496, 8128, 10030557]
        for A in test_cases:
            print(f"Test case: A = {A}")
            print("isPerfect:", bool(s.isPerfect(A)))
            print("isPerfectOptimized:", bool(s.isPerfectOptimized(A)))
            print()
    else:
        try:
            # Take the input from the command
            A = int(sys.argv[1])
            print (f"Test case: A = {A}")
            print("isPerfect:", bool(s.isPerfect(A)))
            print("isPerfectOptimized:", bool(s.isPerfectOptimized(A)))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except Exception as e:
            print("An error occurred. Please refer to the message below for more details.")
            print(str(e))