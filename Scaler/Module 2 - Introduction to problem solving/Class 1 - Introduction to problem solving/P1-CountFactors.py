#Problem Description
'''
Given an integer A, you need to find the count of it's factors.

Factor of a number is the number which divides it perfectly leaving no remainder.

Example : 1, 2, 3, 6 are factors of 6
'''

# Problem Constraints
'''
1 <= A <= 109
'''

# Input Format
'''
First and only argument is an integer A.
'''

# Output Format
'''
Return the count of factors of A.
'''

class Solution:
    # @param A : integer
    # @return an integer
    def solveWithFor(self, A):
        count = 0
        # Loop from 1 to the square root of A (inclusive)
        for i in range(1, int(A**0.5)+1):
            # Check if i is a factor of A
            if A % i == 0:
                count += 1
                # Check if the corresponding factor is different from i
                if i != A // i:
                    count += 1
        return count
    
    def solveWithWhile(self, A):
        count = 2  # Start with 2 to account for 1 and A itself
        i = 2
        # Loop while i squared is less than or equal to A
        while (i * i) <= A:
            # Check if i squared is equal to A
            if (i * i) == A:
                count += 1
            # Check if i is a factor of A
            elif A % i == 0:
                count += 2
            i += 1
        return count



# Time Complexity
'''
The time complexity of this solution is O(sqrt(A)) because we loop from 1 to the square root of A.
'''

# Space Complexity
'''
The space complexity of this solution is O(1) because we use a constant amount of extra space.
'''

# Optimized solution
'''
We can optimize the solution by looping from 1 to the square root of A and checking if i is a factor of A.
If i is a factor of A, we increment the count by 2.
If i squared is equal to A, we increment the count by 1.
This way, we avoid checking if the corresponding factor is different from i.
'''

import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test cases
        print("Test case 1: Factor of 6")
        print(s.solve_with_for(6))  # 4
        print(s.solve_with_while(6))  # 4
        print("Test case 2: Factor of 10")
        print(s.solve_with_for(10))  # 4
        print(s.solve_with_while(10))  # 4
    else:
        try:
            A = int(sys.argv[1])
            print(f"Factors of {A}:")
            print(s.solve_with_for(A))
            print(s.solve_with_while(A))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            sys.exit(1)
        except Exception as e:
            print("An error occurred. Refer to the message below for more details.")
            print(str(e))
            sys.exit(1)