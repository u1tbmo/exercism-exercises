def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    if target < 0:
        raise ValueError("target can't be negative")

    # Memoization
    dp = [float("inf")] * (target + 1)
    dp[0] = 0
    coin_used = [-1] * (target + 1)

    # For each number from 1 to target, find the minimum number of coins needed to make that number
    for i in range(1, target + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    # If dp[target] is still inf, then there is no solution
    if dp[target] == float("inf"):
        raise ValueError("can't make target with given coins")

    # Backtrack to find the coins used
    result = []
    while target > 0:
        result.append(coin_used[target])
        target -= coin_used[target]

    return sorted(result)
