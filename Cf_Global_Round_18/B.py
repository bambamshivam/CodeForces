import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	l,r=M();ans=1000000
	def f(l,t):
		a=l//t
		if a%2==0:b=(l)%t + (a//2)*t
		else:b=(a//2 +1)*t
		return b
	for i in range(18):
		t=1<<i;ans=min(ans,f(r+1,t)-f(l,t))
	print(ans)