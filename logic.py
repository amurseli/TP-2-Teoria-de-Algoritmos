def coins_game(coins):
    n = len(coins)
    dp = [[0] * n for _ in range(n)]
    
    #Caso base: una sola moneda
    for i in range(n):
        dp[i][i] = coins[i]
    
    #Caso base: dos monedas
    for i in range(n - 1):
        dp[i][i+1] = max(coins[i], coins[i+1])
    
    for d in range(2, n):
        for i in range(n - d):
            j = i + d
            if coins[i+1] > coins[j]:
                dp[i][j] = coins[i] + dp[i+2][j]
            else:
                dp[i][j] = coins[i] + dp[i+1][j-1]
            
            if coins[j-1] > coins[i]:
                dp[i][j] = max(dp[i][j], coins[j] + dp[i][j-2])
            else:
                dp[i][j] = max(dp[i][j], coins[j] + dp[i+1][j-1])
    
    sophia_gain = dp[0][n-1]
    mateo_gain = sum(coins) - sophia_gain

    return sophia_gain, mateo_gain, dp


def reconstruct_solution(coins, dp):
    n = len(coins)
    i, j = 0, n - 1
    is_sophia_turn = True

    while i <= j:
        if is_sophia_turn:
            first = coins[i] + min(dp[i+2][j] if i+2 <= j else 0, dp[i+1][j-1] if i+1 <= j-1 else 0)
            if first >= dp[i][j]:
                print(f"Sophia debe agarrar la primera ({coins[i]}); ", end="")
                i += 1
            else:
                print(f"Sophia debe agarrar la ultima ({coins[j]}); ", end="")
                j -= 1
        else:
            if coins[i] > coins[j]:
                print(f"Mateo agarra la primera ({coins[i]}); ", end="")
                i += 1
            else:
                print(f"Mateo agarra la ultima ({coins[j]}); ", end="")
                j -= 1
        is_sophia_turn = not is_sophia_turn
