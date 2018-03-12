import math
import sys 
import numpy as np

#returns True if n if perfect square
def perfect_square(n):  
	if n-int(n):
		return False
	else:
		return True	



#return number of alive neighbours around position [p,q]
def neighbor_counter(p,q):
	alive=0
	#counting in previous row
	if p-1>=0:
		for i in range(-1,2):
			if q+i>=0 and q+i<n:
				if grid[p-1][q+i] == 1:
					alive+=1			
	#counting in own row
	for i in [-1,1]:
		if q+i>=0 and q+i<n:
			if grid[p][q+i] == 1:
				alive+=1
	#counting in next row
	if p+1<n:
		for i in range(-1,2):
			if q+i>=0 and q+i<n:
				if grid[p+1][q+i]==1:
					alive+=1
	return alive






a=[]
file_path=raw_input("Enter file path: ")
file=open(file_path)
for line in file:
	for ch in line:
		if ch=='0' or ch=='1':
			a.append(ch)

#converting string array to int array
a=[int(x) for x in a]

n = math.sqrt(len(a))

#check n is a perfect square or not
if not perfect_square(n):
	print "\nCan't make a matrix from input\n"
	sys.exit()

#converting to a matrix
n=int(n)
grid=np.zeros((n,n),int)
for i in range(0,n):
	for j in range(0,n):
		grid[i][j]=a[i*n+j]

current=np.zeros(n,int)	

for i in range(0,n):
	for j in range(0,n):
		living=neighbor_counter(i,j)
		if grid[i][j] == 1:
			if living<2:
				current[j]=0
			elif living >3:
				current[j]=0;
			else:
				current[j]=1
		else:
			if living == 3:
				current[j]=1
			else:
				current[j]=0									
	print current
