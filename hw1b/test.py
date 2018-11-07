# -*- coding:utf-8 -*- 


def dfs(nums,number,value,maxrest):
	# print '\n\n\n\n\n'
	# print number
	global best_value

	eachcol = value
	eachnumber = number
	# global number
	rower = [0]*n  #record every row situation
	restvalue = maxrest[nums]

	for i in range(nums):
		if collonm[i] == -1:
			continue
		rower[collonm[i]] = 1  #第n列第m行
		d = nums - i 
		if collonm[i] - d >= 0:
			rower[collonm[i] - d] = 1
		if collonm[i] + d <= n - 1:
			rower[collonm[i] + d] = 1


	for j in range(n):
		tuplev = local_sort[nums][j]
		index = tuplev[0]
		value11 = tuplev[1]
		if rower[index] == 1 and j < n - 1 :# or array[j][nums] == 0 and j < n - 1:
			continue
		elif rower[index] == 0 : #and array[j][nums] != 0:
			if number < p:
				collonm[nums] = index
				number = eachnumber + 1
				value = eachcol + value11
			elif eachcol + value11 > value:
				value = eachcol + value11
		
		if nums < n - 1 and best_value < value + restvalue:
			if number < p:
				dfs(nums + 1, number, value, maxrest) 
			elif number == p:
				if best_value < value:
					best_value = value
					# print best_value
				collonm[nums] = -1
				dfs(nums + 1, eachnumber, eachcol, maxrest)
		elif number == p:
			if best_value < value:
				best_value = value
			# print best_value

		if j == n - 1 and nums < n - 1 and n != p and number < p and best_value < value + restvalue:
			collonm[nums] = -1
			dfs(nums + 1, eachnumber, eachcol,maxrest)
 
inputfile = open('/Users/wuqi/Documents/py561/hw1b/input15.txt')
outfile = file('/Users/wuqi/Documents/py561/hw1b/output15.txt','w')
listfirst = inputfile.readlines()
# value=[[0]*4 for i in range(3)]
n = int(listfirst[0])  #n * n city area
p = int(listfirst[1])  #p the number of police offers
s = int(listfirst[2])  #s the number of scooters
array = [[0]*n for i in range(n)]  #store the scooters number of each node
collonm = [-1]*n #list(range(n))    # record every col's storage
value = 0 #compute the point activity
best_value = 0
number = 0

for i in range(3,len(listfirst)):
	val = listfirst[i]
	val = val.strip('\n')
	val = val.split(',')
	row = int(val[0])
	col = int(val[1])
	array[col][row] += 1

Maxvalue_eachcol = [0]*n

for i in range(n):
	Maxexcp = 0
	for j in range(n):
		if Maxexcp < array[j][i]:
			Maxexcp = array[j][i]
	Maxvalue_eachcol[i] = Maxexcp

temp = 0
maxrest = [0]*n
for i in range(n-1,-1,-1):
	maxrest[i] = temp
	temp += Maxvalue_eachcol[i]
	
# print maxrest
# print Maxvalue_eachcol
# print array


local_sort = [[0]*n for i in range(n)]
for i in range(n):
	for j in range(n):
		local_sort[i][j] = array[j][i]
	local_sort[i] = sorted(enumerate(local_sort[i]), key=lambda x:x[1],reverse = True)
# print local_sort

# sumvalue = sum(Maxvalue_eachcol)

# print array
# print Maxvalue_eachcol
# print sumvalue

dfs(0,number,value,maxrest)
print best_value
outfile.write(str(best_value))

inputfile.close()
outfile.close()


