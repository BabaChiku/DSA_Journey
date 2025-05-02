# Problem Description
'''
Given an array A of N integers. 
Count the number of elements that have at least 1 elements greater than itself.
'''

# Problem Constraints
'''
1 <= N <= 10^5
1 <= A[i] <= 10^9
'''

# Input Format
'''
First and only argument is an array of integers A.
'''

# Output Format
'''
Return the count of elements.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Find the length of the array A
        n = len(A)
        # If the length of the array A is less than or equal to 1, return 0
        if n <= 1:
            return 0
        # Initialize the count variable to 0
        count = 0
        # Initialize the max_value variable to -1
        max_value = -1
        max_element = 0
        # Loop through the array A to find the maximum value using two pointers
        i = 0
        j = n - 1
        while i < j:
            # Check if A[i] is greater than A[j]
            if A[i] > A[j]:
                # If A[i] is greater, check if it is greater than max_value
                if A[i] > max_value:
                    # If A[i] is greater than max_value, increment the count variable by max_element(number of maximum elements found so far, as all of now have at least one greater than itself) + 1(A[j] has A[i] greater than itself)
                    count += max_element + 1
                    # Set max_element to 1 as we have found a new maximum element
                    max_element = 1
                    # Update the max_value to A[i]
                    max_value = A[i]
                elif A[i] < max_value:
                    # If A[i] is not greater than max_value, increment the count variable by 2, as both A[i] and A[j] have at least one greater than itself
                    count += 2
                else:
                    # If A[i] is equal to max_value, increment the count variable by 1, as A[j] has at least one greater than itself
                    count += 1
                    # Increment the max_element variable by 1, as we have found another maximum element
                    max_element += 1
            elif A[j] > A[i]:
                # If A[j] is greater, check if it is greater than max_value
                if A[j] > max_value:
                    # If A[j] is greater than max_value, increment the count variable by max_element + 1
                    count += max_element + 1
                    # Set max_element to 1 as we have found a new maximum element
                    max_element = 1
                    # Update the max_value to A[j]
                    max_value = A[j]
                elif A[j] < max_value:
                    # If A[j] is not greater than max_value, increment the count variable by 2
                    count += 2
                else:
                    # If A[j] is equal to max_value, increment the count variable by 1
                    count += 1
                    # Increment the max_element variable by 1, as we have found another maximum element
                    max_element += 1
            else:
                # If A[i] is equal to A[j], check if A[i] is greater than max_value
                if A[i] > max_value:
                    # If A[i] is greater than max_value, increment the count variable by max_element only, as both A[i] and A[j] are equal and are greater than max_value
                    count += max_element
                    # Set max_element to 2 as we have found two new maximum elements
                    max_element = 2
                    # Update the max_value to A[i]
                    max_value = A[i]
                elif A[i] < max_value:
                    # If A[i] is not greater than max_value, increment the count variable by 2, as both A[i] and A[j] have at least one greater than itself
                    count += 2
                else:
                    # If A[i] is equal to max_value
                    # Increment the max_element variable by 2, as we have found two maximum elements
                    max_element += 2
            
            # Move the pointers towards each other
            i += 1
            j -= 1
        
        # If i is equal to j, check if A[i] is greater than max_value
        if i == j:
            # If A[i] is greater than max_value, increment the count variable 
            if A[i] > max_value:
                # Increment the count variable by max_element only, as A[i] is the same element as A[j] 
                count += max_element
                # Set max_element to 1 as we have found a new maximum element
                max_element = 1
                # Update the max_value to A[i]
                max_value = A[i]
            elif A[i] < max_value:
                # If A[i] is not greater than max_value, increment the count variable by 1, as A[i] has at least one greater than itself
                count += 1
        
        # Return the count variable
        return count
    
    
    def simple_solve(self, A):
        # Find the length of the array A
        N=len(A)
        # If the length of the array A is less than or equal to 1, return 0
        if N<=1:
            return 0
        # Initialize the maxEle, count, i, j variables
        i=0
        j=N-1
        maxEle=A[i]
        count=0
        # Loop through the array A to find the maximum value using two pointers
        while i<=j:
            # Check if A[i] is greater than A[j]
            if A[i]>A[j]:
                # If A[i] is greater, check if it is greater than maxEle
                if A[i]>maxEle:
                    maxEle=A[i]
            else:
                # If A[j] is greater or equal, check if it is greater than maxEle
                if A[j]>maxEle:
                    maxEle=A[j]
            # Move the pointers towards each other
            i+=1
            j-=1
        
        # Reset the pointers to the beginning and end of the array A
        i=0
        j=N-1
        while i<j:
            # Check if element is not equal to maxEle
            if A[i]!=maxEle:
                count+=1
            if A[j]!=maxEle:
                count+=1
            # Move the pointers towards each other
            i+=1
            j-=1
        # If i is equal to j, check if A[i] is not equal to maxEle
        if i==j:
            if A[i]!=maxEle:
                count+=1
        # Return the count variable
        return count


# Time Complexity
'''
The time complexity of the solution is O(N) where N is the length of the array A.
This is because we are iterating through the array A once to find the maximum value and count the elements that have at least 1 element greater than itself.
'''

# Space Complexity
'''
The space complexity of the solution is O(1) because we are using a constant amount of extra space.
This is because we are only using a few variables to store the maximum value, count, and other variables.
'''

# Solution
'''
The solution is to use two pointers to find the maximum value in the array A and count the elements that have at least 1 element greater than itself.
The two pointers are initialized to the beginning and end of the array A. We compare the elements at the two pointers and update the maximum value and count accordingly. Finally, we return the count variable.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Example input: [1, 2, 3, 4, 5]
        A = [1, 2, 3, 4, 5]
        print("Test case 1: Counting elements in A=[1, 2, 3, 4, 5]")
        print("Output:", s.solve(A))
        # Expected output: 4 (1, 2, 3, and 4 have at least one element greater than themselves)
        # Example input: [5, 5, 5]
        A = [5, 5, 5]
        print("Test case 2: Counting elements in A=[5, 5, 5]")
        print("Output:", s.solve(A))
        # Expected output: 0 (no element has at least one element greater than itself)
    else:
        try:
            A = list(map(int, sys.argv[1].strip('[]').split(',')))
            print("Test case 3: Counting elements in A={}".format(A))
            print("Output:", s.solve(A))
        except Exception as e:
            print("Invalid input, please provide a valid array of integers.")
            print("Error:", e)
            print("Usage: python AP3-CountOfElements.py [1,2,3,4,5]")
            print("Where [1,2,3,4,5] is the input array")