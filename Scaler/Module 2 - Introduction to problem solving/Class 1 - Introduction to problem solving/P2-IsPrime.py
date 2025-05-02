# Problem Description
'''
Given a number A. Return 1 if A is prime and return 0 if not. 

Note : 
The value of A can cross the range of Integer.
'''

# Problem Constraints
'''
1 <= A <= 10^9
'''

# Input Format
'''
The first argument is a single integer A.
'''

# Output Format
'''
Return 1 if A is prime else return 0.
'''

class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        # Check if A is less than 2
        if A < 2:
            return 0
        # Loop from 2 to the square root of A (inclusive)
        for i in range(2, int(A**0.5)+1):
            # Check if i is a factor of A
            if A % i == 0:
                return 0
        return 1
    
    def isPrimeOptimized(self, A):
        # Check if A is less than 2
        if A < 2:
            return 0
        # Check if A is 2
        if A == 2:
            return 1
        # Check if A is even
        if A % 2 == 0:
            return 0
        # Loop from 3 to the square root of A (inclusive) in steps of 2
        for i in range(3, int(A**0.5)+1, 2):
            # Check if i is a factor of A
            if A % i == 0:
                return 0
        return 1
    

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
We can optimize the solution by checking if A is less than 2, if A is 2, and if A is even.
Then we can loop from 3 to the square root of A in steps of 2.
'''

import sys

def main():
    # Test cases to validate the solution
    test_cases = [1, 2, 10030557]
    sol = Solution()
    for A in test_cases:
        print(f"Test case: A = {A}")
        print("isPrime:", sol.isPrime(A))
        print("isPrimeOptimized:", sol.isPrimeOptimized(A))
        print()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    else:
        try:
            # Take the input from the command line
            A = int(sys.argv[1])

            # Create an object of the class
            sol = Solution()
            
            print(f"Is {A} a prime number?")
            # Call the function and print the result
            print("isPrime:", bool(sol.isPrime(A)))
            print("isPrimeOptimized:", bool(sol.isPrimeOptimized(A)))
        except ValueError:
            print("Usage: python3 P2-IsPrime.py A")
            print("A: An integer")
            print("Invalid input. Please enter an integer.")
        except Exception as e:
            print("An error occurred. Please refer to the message below for more details.")
            print(str(e))