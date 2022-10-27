dp = [0 for i in range(61)]
dp[0]=dp[1]=1
for i in range(2, 61):

	dp[i] = 0

	for j in range(i):
		dp[i] += dp[j] * dp[i - j - 1]
	
for _ in range(int(input())):
	n = int(input())
	n //= 2
	print(dp[n])