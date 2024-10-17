def maxProfit(prices):
    maximum = 0
    minimum = prices[0]

    for i in range(len(prices)):
        if prices[i] < minimum:
            minimum = prices[i]
        else:
            maximum += prices[i] - minimum
            minimum = prices[i]
    return maximum

# [7,1,5,3,6,4]
prices = [int(i) for i in input("Enter space seperated elements: ").split()]
print(maxProfit(prices))