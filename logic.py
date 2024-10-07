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
    
    return sophia_gain, mateo_gain
