# Problem Description
'''
Say you have an array, A, for which the i-th element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Return the maximum possible profit.
'''

# Problem Constraints
'''
0 <= A.size() <= 700000
1 <= A[i] <= 10^7
'''

# Input Format
'''
The first and the only argument is an array of integers, A.
'''

# Output Format
'''
Return an integer, representing the maximum possible profit.
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        # Initialize the length of the array A
        n = len(A)
        # If the array is empty, return 0
        if n == 0:
            return 0

        # Initialize the minimum price to the first element of the array A
        min_price = A[0]
        # Initialize the maximum profit to 0
        max_profit = 0

        # Loop through the array A to find the maximum profit
        for i in range(1, n):
            # Update the minimum price if the current price is less than the minimum price
            min_price = min(min_price, A[i])
            # Update the maximum profit if the current profit is greater than the maximum profit
            max_profit = max(max_profit, A[i] - min_price)

        # Return the maximum profit
        return max_profit


# Time Complexity
'''
The time complexity of this solution is O(N), where N is the length of the array A.
This is because we are iterating through the array A once to find the minimum price and maximum profit.
'''

# Space Complexity
'''
The space complexity of this solution is O(1), as we are using only a constant amount of space to store the minimum price and maximum profit.
'''

# Solution
'''
This solution uses a single pass through the array to find the minimum price and maximum profit.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test case 1
        A = [1, 2]
        print("Test case 1: Finding maximum profit in A=[1, 2]")
        print("Maximum profit:", s.maxProfit(A))
        # Test case 2
        A = [1, 4, 5, 2, 4]
        print("Test case 2: Finding maximum profit in A=[1, 4, 5, 2, 4]")
        print("Maximum profit:", s.maxProfit(A))
    else:
        try:
            # Read the input array from command line arguments
            A = list(map(int, sys.argv[1].strip("[]").split(",")))
            print("Input array:", A)
            print("Maximum profit:", s.solve(A))
        except Exception as e:
            print("Invalid input. Please provide a list of integers separated by commas.")
            print("Error:", e)
            print("Usage: python AP4-BestTimeToBuyAndSellStocks.py [1,2,3]")
            print("Where [1,2,3] is the input array.")