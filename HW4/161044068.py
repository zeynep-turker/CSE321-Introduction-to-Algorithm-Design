#PART1-b)
def convert2DtoSpecial(Arr,m,n):
	num=0
	for i in range(m-1):
		for j in range(n-1):
			if(Arr[i][j]+Arr[i+1][j+1] > Arr[i][j+1]+Arr[i+1][j]):
				if(num == 1):
					Arr[k][l+1] = Arr[k][l+1] - dif
					print "There are changeble element more than 1 in Arr"
					return
				k = i 
				l = j
				temp = Arr[i][j]+Arr[i+1][j+1]
				dif = temp - (Arr[i][j+1]+Arr[i+1][j])
				print "changes ",Arr[i][j+1],"(Arr[",i,",",j+1,"])","be ",Arr[i][j+1] + dif
				Arr[i][j+1] = Arr[i][j+1] + dif
				num = num +1
	if(num == 0):
		print "There are not changeble element in Arr"
		return
				

def printArr(Arr,m):
	for i in range(m):
		print Arr[i]

#PART1b DRIVER	
def DriverPart1b():
	print "Example 1:"	
	Arr = [[37,23,22,32],[21,6,7,10],[53,34,30,31],[32,13,9,6],[43,21,15,8]]
	m = 5
	n =4
	print "2D Array"
	printArr(Arr,m)
	print "Convert Special Array"
	convert2DtoSpecial(Arr,m,n)
	print "New Array"
	printArr(Arr,m)
	print "Example 2:"
	Arr = [[12,17,13,28,23],[17,22,16,29,23],[24,28,22,34,24],[11,13,6,17,7],[45,44,32,37,23],[36,33,19,21,8],[75,66,51,53,38]]
	m = 7
	n =5
	print "2D Array"
	printArr(Arr,m)
	print "Convert Special Array"
	convert2DtoSpecial(Arr,m,n)
	print "New Array"
	printArr(Arr,m)

#PART1-c)
def min(a, l, r,leftmost,minimum):
	if (r-l==1):
		if(minimum[0] > a[l]):
			minimum[0] = a[l]
			leftmost[0] = l
		return a[l]
	m=(l+r)/2
	min(a,l,m,leftmost,minimum)
	min(a,m,r,leftmost,minimum)
	return leftmost[0]
	
def leftmostMinEl(a,l,r):
	if (r-l==1):
		leftmost = [0]
		minimum = [(a[l])[0]]
		print "Leftmost minimum element for row :",l+1,"->>",(a[l])[min((a[l]),0,len((a[l])),leftmost,minimum)],",index :",leftmost[0]
		return a[l]
	m=(l+r)/2
	leftmostMinEl(a,l,m)
	leftmostMinEl(a,m,r)

#PART1c DRIVER
def DriverPart1c():
	print "Example 1:"
	Arr = [[37,23,22,32],[21,6,7,10],[53,34,30,31],[32,13,9,6],[43,21,15,8]]
	printArr(Arr,len(Arr))
	leftmostMinEl(Arr,0,len(Arr))
	print "Example 2:"
	Arr = [[12,17,13,28,23],[17,22,16,29,23],[24,28,22,34,24],[11,13,6,17,7],[45,44,32,37,23],[36,33,19,21,8],[75,66,51,53,38]]
	printArr(Arr,len(Arr))
	leftmostMinEl(Arr,0,len(Arr))
#PART2
def kthElement(A, B, m, n, k, i, j):

	if (i == m): 	#if it is reached end of A
		return B[j + k - 1]

	if (j == n):	#if it is reached end of B
		return A[i + k - 1]

	# k should never reach 0 or exceed sizes of arrays
	if (k == 0 or k > (m - i) + (n - j)):
		return -1
	if (k == 1): #Compare first elements of A and B
		if (A[i] < B[j]):
		    return A[i]
		else:
		    return B[j]
	x = k / 2 #k is divided by 2
	#if size of A is less than k / 2
	if (x - 1 >= m - i):
		# Last element of A is not kth
        # We can directly return the (k-m)th element in B
		if (A[m - 1] < B[j + x - 1]):
			return B[j + (k - (m - i) - 1)]
		else:
			return kthElement(A, B, m, n, k - x,i, j + x)
 	# Size of B is less than k / 2
	if (x-1 >= n-j):
		if (B[n - 1] < A[i + x - 1]):
			return A[i + (k - (n - j) - 1)]
		else:
			return kthElement(A, B, m, n, k - x,i + x, j)
	else:
		if (A[x + i - 1] < B[x + j - 1]):
			return kthElement(A, B, m, n, k - x,i + x, j)
		else:
			return kthElement(A, B, m, n, k - x,i, j + x)

#PART2 DRIVER
def DriverPart2():
	print "Example 1:"
	A = [2, 3, 6, 7, 9]
	B = [1, 4, 8, 10]
	k = 6;
	print "A :",A
	print "B :",B
	print k,"kth elements is :",kthElement(A, B, len(A), len(B),k,0,0)
	print "Example 2:"
	C = [15,17,19,21,27]
	D = [18,20,27,26,30]
	k = 5;
	print "A :",C
	print "B :",D
	x = kthElement(C, D, len(C), len(D),k,0,0)
	print k,"kth elements is :",x

#PART3
def maxSubArraySum(a, l, r,result,temp,maxSum,start):
	if (r-l==1):
		temp[0] = temp[0] + a[l]
		if(temp[0] > maxSum[0]):
			maxSum[0] = temp[0]
			result[0] = start[0]
			result[1] = l
			result[2] = maxSum[0]
 
		if(temp[0]<0):
			temp[0] = 0
			start[0] = l + 1
 
		return a[l]
	
	m=(l+r)/2
	maxSubArraySum(a,l,m,result,temp,maxSum,start)
	maxSubArraySum(a,m,r,result,temp,maxSum,start)


def printSubArr(arr,i,j):

	for x in range(i,j+1):
		print arr[x],
		
#PART3 DRIVER
def DriverPart3():
	print "Example 1:"           
	array = [5,-6,6,7,-6,7,-4,3]
	result = [0,0,0]
	temp = [0]
	maxSum = [-1000]
	start = [0]
	maxSubArraySum(array,0,len(array),result,temp,maxSum,start)
	print "Array :",array
	printSubArr(array,result[0],result[1])
	print "Sum :",result[2]
	print "Example 2:"
	array = [1,-2,3,7,5,1,-4,4]
	result = [0,0,0]
	temp = [0]
	maxSum = [-1000]
	start = [0]
	maxSubArraySum(array,0,len(array),result,temp,maxSum,start)
	print "Array :",array
	printSubArr(array,result[0],result[1])
	print "Sum :",result[2]

#PART4
def bipartite(Graph,Color,l,h,queue):
	if(len(queue) == 0):
		return True
	if(len(queue) != 0):
		u = queue.pop(0)
		if(Graph[u][u] == 1):
			return False
	
		for x in range(3):
			if (Graph[u][x] and Color[x] == -1):
				Color[x] = 1 - Color[u]
				queue.append(x) 
			if(Graph[u][x] and (Color[x] == Color[u])):
				return False

	mid = (l + h) / 2
	return bipartite(Graph,Color, l, mid,queue)
	return bipartite(Graph,Color, mid+1, h,queue)
#PART4 DRIVER
def DriverPart4():
	print "Example 1:"
	Graph = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]] 
	Color = [-1,-1,-1,-1]
	queue = []
	queue.append(0)
	Color[0] = 1
	print "Graph : ",Graph
	x = bipartite(Graph,Color,0,len(Graph)-1,queue)
	if(x == True):
		print "Graph is bipartite."
	else :
		print "Graph is not bipartite."
	print "Example 2:"
	Graph = [[0,1,0,0,0,1], [1,0,1,0,0,0], [0,1,0,1,0,0], [0,0,1,0,1,0],[0,0,0,1,0,1],[1,0,0,0,1,0]] 
	Color = [-1,-1,-1,-1,-1]
	queue = []
	queue.append(0)
	Color[0] = 1
	print "Graph : ",Graph
	x = bipartite(Graph,Color,0,len(Graph)-1,queue)
	if(x == True):
		print "Graph is bipartite."
	else :
		print "Graph is not bipartite."


#PART5
def createDifferArr(a,b,l,r,z):

	if (r-l==1):
		if(l<9):
			z[l] = b[l+1]-a[l]
			return b[l+1]-a[l]
		else:
			return
		

	m=(l+r)/2
	u=createDifferArr(a,b,l,m,z)
	v=createDifferArr(a,b,m,r,z)

def findMax(arr):
	if (len(arr) == 1):
		return 0
	elif (len(arr) == 2):
		if arr[0] > arr[1]:
   			return 0
    		else:
        		return 1
	else:
		mid = len(arr) / 2
		arr1 = arr[0:mid]
		arr2 = arr[mid:len(arr)]
		maxA = findMax(arr1)
		maxB = findMax(arr2) + mid
		if (arr[maxA] > arr[maxB]):
			return maxA
		else:
			return maxB


def findBestDay(c,p):
	a = [0,0,0,0,0,0,0,0,0]
	createDifferArr(c,p,0,10,a)
	tmp = findMax(a)
	result = tmp + 1
	return result

#PART5 DRIVER
def DriverPart5():
	print "Example 1:"
	c = [5, 11, 2, 21, 5, 7, 8, 12, 13, 0]
	p = [0, 7, 9, 5, 21, 7, 13, 10, 14, 20]
	result = findBestDay(c,p)
	print "C : ",c
	print "P : ",p
	print "Best Day : ",result
	print "Example 2:"
	c = [2, 10, 8, 22, 3, 6, 8, 1, 9, 0]
	p = [0, 4, 20, 5, 21, 5, 7, 8, 6, 5]
	result = findBestDay(c,p)
	print "C : ",c
	print "P : ",p
	print "Best Day : ",result


print "PART1b"
DriverPart1b()
print " "
print "PART1c"
DriverPart1c()
print " "
print "PART2"
DriverPart2()
print " "
print "PART3"
DriverPart3()
print " "
print "PART4"
DriverPart4()
print " "
print "PART5"
DriverPart5()

