def maxProfit(prices):
    maximum = 0
    minimum = prices[0]
    for i in range(len(prices)):
        if prices[i] < minimum:
            minimum = prices[i]
        else:
            maximum = max(maximum,prices[i] - minimum)
    return maximum

prices = [int(i) for i in input().split()]
print(maxProfit(prices))