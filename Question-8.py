dp = [0 for i in range(101)]
dp[1] = 0
dp[2] = 1
dp[3] = 2
dp[4] = 4
dp[0] = 0
dp[5] = 6
dp[6] = 9
for i in range(7, 101):
	
	mx = -1
	
	for j in range(1, i + 1):
	
		if mx > dp[j] * (i - j):
			mx = mx
	
		else:
			mx = dp[j] * (i - j)
	
		dp[i] = mx
	
for _ in range(int(input())):
	
	n = int(input())
	print(dp[n])