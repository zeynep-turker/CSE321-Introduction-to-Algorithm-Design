#PART1#
def minimumCost(N,S,board,n,M,i,which,cityChangingCost):

	if(i == n):
		return sumBoard(board) + cityChangingCost
	else :
		if(N[i] < S[i]):
			board.append(N[i])
			if(which == 1):
				cityChangingCost = cityChangingCost + M
			which = 0
		else: 
			board.append(S[i])
			if(which == 0):
				cityChangingCost = cityChangingCost + M
			which = 1
		return minimumCost(N,S,board,n,M,i+1,which,cityChangingCost)	


def sumBoard(board):
	sum = 0
	for i in range(0,len(board)):
		sum = sum + board[i]
		
	return sum
#PART1 DRIVER#
def PART1():
	print "Example 1"
	N = [1,3,20,30]
	S = [50,20,2,4]
	board = []
	n = 4
	M = 10
	which = -1
	print "NY :",N
	print "SF :",S
	print "Total Cost:",minimumCost(N,S,board,n,M,0,which,0)
	print ""
	print "Example 2"
	N = [1,20,20,4]
	S = [50,2,2,30]
	board = []
	n = 4
	M = 10
	which = -1
	print "NY :",N
	print "SF :",S
	print "Total Cost:",minimumCost(N,S,board,n,M,0,which,0)
#PART2#
def sort(arr):
	for i in range(0,len(arr)-1):
		for j in range(i+1,len(arr)):
			if(arr[i][1] > arr[j][1]):
				temp1 = arr[i][0]
				temp2 = arr[i][1]
				arr[i][0] = arr[j][0]
				arr[i][1] = arr[j][1]
				arr[j][0] = temp1
				arr[j][1] = temp2
			
			
			
def sessions(arr,listt):
	sort(arr)
	k = 0
	listt.append(arr[k])
	for i in range(1,len(arr)):	
		if(arr[i][0] >= arr[k][1]):
			listt.append(arr[i])
			k = i

#PART2 DRIVER#
def PART2():
	print "Example 1"	
	arr = [[3,5],[3,4],[4,7],[8,9]]
	print "Sessions:",arr
	listt = []
	sessions(arr,listt)
	print "Optimal list of sessions:",listt
	print ""
	print "Example 2"
	arr = [[3,5],[1,2],[1,5],[5,8],[6,9]]
	print "Sessions:",arr
	listt = []
	sessions(arr,listt)
	print "Optimal list of sessions:",listt



#PART5#
				
			
def operations(arr):
	operation = []
	while len(arr) > 1:
		a = min(arr)
		arr.remove(a)
		b = min(arr)
		arr.remove(b)
		arr.append(a+b)
		operation.append(a+b)
			
					
	print "minimum operation number is :",sum(operation)
	return "Sum :",arr[0]


#PART5 DRIVER#

def PART5():
	print "Example 1"
	arr = [5,5,4]
	print "Array :",arr
	print operations(arr)
	print ""
	print "Example 2"
	arr = [5,8]
	print "Array :",arr
	print operations(arr)


def Driver():
	print "PART1"
	print ""
	PART1()
	print ""
	print "PART2"
	print ""
	PART2()
	print ""
	print "PART5"
	print ""
	PART5()

Driver()
