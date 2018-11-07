inputfile = open('/Users/wuqi/Documents/py561/hw1b/input1.txt')
outfile = file('/Users/wuqi/Documents/py561/hw1b/output.txt','w')
listfirst = inputfile.readlines()
# value=[[0]*4 for i in range(3)]

 n = listfirst[0]  #n * n city area
 p = listfirst[1]  #p the number of police offers
 s = listfirst[2]  #s the number of scooters
 array = [[0]*n for i range(n)]

for i in range(3,len(listfirst)):
	val = listfirst[i]
	val = val.strip('\n')
	val = val.split(',')
	row = val[0]
	col = val[1]
	array[col,row] += 1


print array
outfile.write(array)


inputfile.close()
outfile.close()