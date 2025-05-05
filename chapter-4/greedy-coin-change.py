def greedy_coin_change(coins, amount):
    """
    Greedily selects coins to make up the given amount.
    
    Args:
        coins (list): List of coin denominations.
        amount (int): The total amount to make change for.
    
    Returns:
        list: List of coins used to make up the amount.
    """
    # Sort coins in descending order
    coins.sort(reverse=True)
    
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    
    return result

# Example usage
coins = [1, 5, 10, 25]
amount = 63
result = greedy_coin_change(coins, amount)
print(f"Coins used to make {amount}: {result}")  # Output: Coins used to make 63: [25, 25, 10, 1, 1, 1]

# Test cases
assert greedy_coin_change([1, 5, 10, 25], 63) == [25, 25, 10, 1, 1, 1]
assert greedy_coin_change([1, 5, 10, 25], 99) == [25, 25, 25, 10, 10, 1, 1, 1, 1]
assert greedy_coin_change([1, 5, 10, 25], 0) == []
assert greedy_coin_change([1, 5, 10, 25], 1) == [1]
assert greedy_coin_change([1, 5, 10, 25], 5) == [5]
assert greedy_coin_change([1, 5, 10, 25], 10) == [10]
assert greedy_coin_change([1, 5, 10, 25], 25) == [25]
assert greedy_coin_change([1, 5, 10, 25], 50) == [25, 25]