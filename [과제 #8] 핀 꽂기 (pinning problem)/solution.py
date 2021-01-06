

# A= [tuple(map(int, input().split())) for _ in range(n)]


n =10
A = [(19, 19) ,(1 ,11) ,(19, 20) ,(16, 17) ,(2 ,11) ,(2 ,2) ,(18, 18) ,(3 ,16) ,(1 ,11) ,(8 ,8)]


# n = 11
# A = [(1,4),(3,5),(0,6),(5,7),(3,8),(5,9),(6,10),(8,11),(8,12),(2,14),(12,14)]



# n = 5
# A = [ (7, 7), (3, 4), (0 ,10), (2, 5), (3 ,5)]



A = sorted(A, key=lambda x: x[1])
S = [s for s,_ in A]
F = [f for _,f in A]


pins = [0]

k = 0
for p in range(1, n-1):
	# if p==0 and S[k] <= S[p]:
	# 	pins.append(S[p])
	# 	k = p
	if F[k] <= S[p]:
		pins.append(S[p])
		k = p
print((pins))

