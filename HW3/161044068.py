#PART1

def boxes(A,first,end):
	if len(A)/2 % 2 == 1:
		if first == len(A)/2:
			return
	if len(A)/2 % 2 == 0:
		if first == ((len(A)/2)+1):
			return
	
	temp = A[first]
	A[first] = A[end]
	A[end] = temp
	boxes(A,first+2,end-2)


#*****
#PART2
def findFakeCoin(A,B,n):
	if n == 1 :
		print "Fake Coin  : ",A.index(B[0])+1,". coin"
		return A[0]
	half = n/2
	A1 = copyArray(B,0,half)
	A2 = copyArray(B,half,n)
	w = compare(findSum(A1),findSum(A2))
	if w == 1 :
		findFakeCoin(A,A2,len(A2))
	if w == -1 :
		findFakeCoin(A,A1,len(A1))	
	
		
		
		

def compare(weight1,weight2):
	if weight1 > weight2 : return 1
	if weight1 < weight2 : return -1
	if weight1 == weight2 : return 0 
 

def copyArray(A,first,end):
	newArr = []
	for x in range(first, end):
		newArr.append(A[x])

	return newArr

#******
#PART3
def insertionSort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        position = i-1
       	while position >= 0 and current < arr[position]:
            arr[position + 1] = arr[position]
            position -= 1
        arr[position + 1] = current
  

def quickSort(arr,low,high):

  if low < high:
      pivot = partition(arr,low,high)
      quickSort(arr,low,pivot-1)
      quickSort(arr,pivot+1,high)

def partition(arr,low,high):

  x = arr[low]
  left = low+1
  right = high
  test = False

  while not test:
      while left <= right and arr[left] <= x:
          left = left + 1

      while arr[right] >= x and right >= left:
          right = right -1

      if right < left:
          test = True
      else:
          temp = arr[left]
          arr[left] = arr[right]
          arr[right] = temp

  temp = arr[low]
  arr[low] = arr[right]
  arr[right] = temp

  return right
#*****
#PART4
def findMedian(A):
	insertionSort(A)
	n = len(A)
	if n % 2 != 0:
		median = A[n/2]
	else:
		median = (A[(n-1)/2] + A[n/2])/2.0

	return median
#*****
#PART5
def createSubArrays(arr, index, subarr,B): 
    if index == len(arr):   
        if len(subarr) != 0:
            B.append(subarr) 
    else: 
        createSubArrays(arr, index + 1, subarr,B) 
        createSubArrays(arr, index + 1,subarr+[arr[index]],B) 
      
    return


def findSum(arr):
	 if len(arr)== 1: 
		return arr[0] 
	 else: 
		return arr[0]+findSum(arr[1:])

def splitAsBound(p,C,s,i):
	if i == len(p): return
 	if (findSum(p[i])) >= s:
			C.append(p[i])
	splitAsBound(p,C,s,i+1)


def mulp(arr):
	if len(arr) == 1: return arr[0]
	return arr[0]*mulp(arr[1:])

def arrMulp(arr,newArr,i):
	if i == len(arr): return
	newArr.append(mulp(arr[i]))
	arrMulp(arr,newArr,i+1)

def findOptimalSubArray(A):
	B = []
	C = []
	newArr = []
	x = (max(A) + min(A))/4*len(A)
	print "Array",A
	createSubArrays(A,0,[],B)
	splitAsBound(B,C,x,0)
	arrMulp(C,newArr,0)
	print "The optimal sub-array is",C[newArr.index(min(newArr))]
	return

#*****
def Part1Driver():
	A = [0,0,0,0,0,0,1,1,1,1,1,1]
	print "Before: ",A
	boxes(A,1,len(A)-2)
	print "After: ",A
	A = [0,0,0,0,0,0,0,1,1,1,1,1,1,1]
	print "Before: ",A
	boxes(A,1,len(A)-2)
	print "After: ",A

def Part2Driver():
	A = [1,-1,1,1,1,1]
	B = copyArray(A,0,len(A))
	print "My coins : ",A
	findFakeCoin(A,B,len(B))
	A = [1,1,1,1,1,-1,1]
	B = copyArray(A,0,len(A))
	print "My coins : ",A
	findFakeCoin(A,B,len(B))
def Part3Driver():
	A = [12,45,1,5,3]
	print "Before Insertion Sort,A:",A
	insertionSort(A)
	print "After Insertion Sort,A:",A
	B = [6,1,4,3,2]
	print "Before Quick Sort,A:",B
	quickSort(B,0,len(B)-1)
	print "After Quick Sort,A:",B

def Part4Driver():
	A = [6,1,4,3,2,0]
	median = findMedian(A)
	print A,"=> median : ",median
	B = [6,1,4,3,2]
	median = findMedian(B)
	print B,"=> median : ",median
	
	return

def Part5Driver():
	A = [2, 4, 7, 5, 22, 11]
	findOptimalSubArray(A)
	A = [-1,0,2,3,7]
	findOptimalSubArray(A)
	return

def Driver():
	print "#PART1#"
	Part1Driver()
	print "#PART2#"
	Part2Driver()
	print "#PART3#"
	Part3Driver()
	print "#PART4#"
	Part4Driver()
	print "#PART5#"
	Part5Driver()
	return


Driver()






