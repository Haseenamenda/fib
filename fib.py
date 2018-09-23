def printFibonacciseries(N):
	f1=0
	f2=1
	if(N<1):
		return
	for x in range(0,N):
		print(f2,end=" ")
		next=f1+f2
		f1=f2
		f2=next
printFibonacciseries(5)
