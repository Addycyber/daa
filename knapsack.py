def fractional_knapsack(value, weight, capacity):
    ratio = [(v/w, v, w) for v, w in zip(value, weight)]
    ratio.sort(reverse=True)

    total_value = 0
    for r, v, w in ratio:
        if capacity >= w:
            total_value += v
            capacity -= w
        else:
            total_value += r * capacity
            break
    return total_value

# Example
value = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50

print("Maximum value in Knapsack:", fractional_knapsack(value, weight, capacity))
