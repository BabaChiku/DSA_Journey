# Problem Description
'''
You will be given an integer n. You need to return the count of prime numbers less than or equal to n.
'''

# Problem Constraints
'''
0 <= n <= 10^3
'''

# Input Format
'''
Single input parameter n in function.
'''

# Output Format
'''
Return the count of prime numbers less than or equal to n.
'''


class Solution:

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
    
    # @param A : integer
    # @return an integer
    def countPrime(self, A):
        # Check if A is less than 2
        if A < 2:
            return 0
        # Initialize the count of primes to 0
        count = 0
        # Loop from 2 to A (inclusive)
        for i in range(2, A+1):
            # Check if i is prime
            if self.isPrime(i):
                count += 1
        return count
    
    
    def countPrimeOptimized(self, A):
        # Check if A is less than 2
        if A < 2:
            return 0
        # Initialize the count of primes to 0
        count = 0
        # Initialize the list of prime numbers to all True
        is_prime = [True] * (A+1)
        # Set 0 and 1 to False
        # is_prime[0] = is_prime[1] = False
        length = 2 if len(is_prime)>2 else len(is_prime)
        for i in range(length):
            is_prime[i]=False
        # Loop from 2 to the square root of A (inclusive)
        for i in range(2, int(A**0.5)+1):
            # Check if i is prime
            if is_prime[i]:
                # Loop from i squared to A in steps of i
                for j in range(i*i, A+1, i):
                    # Set j to False
                    is_prime[j] = False
        # Loop from 2 to A (inclusive)
        for i in range(2, A+1):
            # Check if i is prime
            if is_prime[i]:
                count += 1
        return count
    

# Time Complexity
'''
Normal Approach: The time complexity of this solution is O(n*sqrt(n)) because we loop from 2 to the square root of A and then from 2 to A.
Optimized Approach: The time complexity of this solution is O(n*log(log(n))) because we loop from 2 to the square root of A and then from 2 to A.
'''

# Space Complexity
'''
Normal Approach: The space complexity of this solution is O(1) because we use a constant amount of extra space.
Optimized Approach: The space complexity of this solution is O(n) because we use a list of size n+1.
'''

# Optimized Approach
'''
We can optimize the above approach by using the Sieve of Eratosthenes algorithm.
We will initialize a list of size n+1 with all elements set to True.
We will then loop from 2 to the square root of n and mark all multiples of i as False.
Finally, we will count the number of True elements in the list.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test cases to validate the solution
        test_cases = [0, 1, 2, 10, 100, 1000]
        for A in test_cases:
            print(f"Test case: A = {A}")
            print("countPrime:", s.countPrime(A))
            print("countPrimeOptimized:", s.countPrimeOptimized(A))
            print()
    else:
        try:
            A = int(sys.argv[1])
            print(f"Count of prime numbers less than or equal to {A}:")
            print("countPrime:", s.countPrime(A))
            print("countPrimeOptimized:", s.countPrimeOptimized(A))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except Exception as e:
            print("An error occurred. Please refer to the message below for more details.")
            print(e)
