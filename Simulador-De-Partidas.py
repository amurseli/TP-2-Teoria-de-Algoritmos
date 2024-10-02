
def coinGame(coins):
    s_coins = []
    total = 0
    Mtotal = 0
    while len(coins) > 0:
        selectedCoin = input(f"Que moneda quiere: {coins}")
        coins.remove(int(selectedCoin))
        s_coins.append(int(selectedCoin))
        total = total + int(selectedCoin)

        if(len(coins) > 0):
            pop = ""
            if coins[0] > coins[-1]:
                pop = coins.pop(0)
            else:
                pop = coins.pop(-1)
            Mtotal = Mtotal + pop
    print(f"with coins:{s_coins} you scored {total} vs {Mtotal}")


coinGame([96,594,437,950,674])