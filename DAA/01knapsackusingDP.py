def knapsack_dp(weights, profits, capacity):
    n = len(weights)
    # Create a 2D DP table with dimensions (n+1) x (capacity+1)
    dp = [[0 for x in range(capacity + 1)] for y in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # The last cell of the DP table contains the maximum profit
    return dp[n][capacity]


# Example usage
profits = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_profit = knapsack_dp(weights, profits, capacity)
print("Maximum profit (0/1 Knapsack using DP):", max_profit)
