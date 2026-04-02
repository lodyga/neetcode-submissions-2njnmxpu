class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        """
        Time complexity: O(n2)
            O(coin_length * amount)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {}  # {amount:  ways to make it up}
        coins.sort()

        def dfs(amount, lowest_coin):
            if amount == 0:
                return 1
            elif amount < 0:
                return 0
            elif (lowest_coin, amount) in memo:
                return memo[(lowest_coin, amount)]

            memo[(lowest_coin, amount)] = 0
            for coin in coins:
                if coin >= lowest_coin:
                    memo[(lowest_coin, amount)] += dfs(amount - coin, coin)
            return memo[(lowest_coin, amount)]

        return dfs(amount, coins[0])