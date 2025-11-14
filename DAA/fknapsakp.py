def greedy_fractional_knapsack(w, p, W):
    n = len(w)
    x = [0] * n  # fractions of items to take
    weight = 0

    for i in range(n):
        if weight + w[i] <= W:
            x[i] = 1
            weight += w[i]
        else:
            x[i] = (W - weight) / w[i]
            weight = W
            break

    return x

# Example usage:
weights = [10, 20, 30]
profits = [60, 100, 120]
capacity = 50

# Make sure items are sorted by value/weight ratio before calling the function if needed
ratios = [(profits[i] / weights[i], weights[i], profits[i]) for i in range(len(weights))]
ratios.sort(key=lambda x: x[0], reverse=True)
sorted_weights = [item[1] for item in ratios]
sorted_profits = [item[2] for item in ratios]
print("Weights of item :" ,weights)
print("Profit from each item :",profits)
print("Capacity of Bag :",capacity)
fractions = greedy_fractional_knapsack(sorted_weights, sorted_profits, capacity)
print("Fractions of items to take:", fractions)
total_profit = 0
for i in range(len(profits)):
    total_profit += fractions[i] * profits[i]

print("Total profit:", total_profit)
