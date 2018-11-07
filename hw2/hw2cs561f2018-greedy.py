import time
t = time.clock()


def mergersort(list1, n):
	for i in range(n - 1):
		glo = i
		for j in range(i + 1, n):
			if sum(list(map(lambda x : int(x), list1[j][13:20]))) > sum(list(map(lambda x : int(x), list1[glo][13:20]))):
				glo = j
		temp = list1[i]
		list1[i] = list1[glo]
		list1[glo] = temp
	return list1
		


def dfs(restL,restS,DayofS,DayofL,pickS,pickL,countS,countL):
	global best_list
	global efficiency_rate 

	if efficiency_rate < 1.0 - float(sum(DayofS)) / (p * 7):
		efficiency_rate = 1.0 - float(sum(DayofS)) / (p * 7)
		best_list = pickS[:]
		print best_list
	elif efficiency_rate == 1.0 - float(sum(DayofS)) / (p * 7):
		check = pickS[:]
		if int(check[0][0:5]) < int(best_list[0][0:5]):
			best_list = check
			print best_list

	if countS == countL and restS and restL or not restL and restS:
		for i in range(len(restS)):
			restLL = restL[:]
			restSS = restS[:]
			DayofSS = DayofS[:]
			DayofLL = DayofL[:]
			pickSS = pickS[:]
			pickLL = pickL[:]
			countSS = countS
			countLL = countL

			current = restSS[i]
			maptoint = list(map(lambda x :int(x), current[13:20]))
			Maynewday = [DayofSS[m] - maptoint[m] for m in range(7)]
			pickornot = min(Maynewday)
			if pickornot >= 0:
				if current in restLL:
					restLL.remove(current)
				restSS.remove(current)
				pickSS.append(current)
				dfs(restLL, restSS, Maynewday, DayofLL, pickSS, pickLL, countSS+1, countLL)
			else:
				Maynewday = [DayofSS[m] + maptoint[m] for m in range(7)]
	elif countL != countS and restL and restS:
		restLLL = restL[:]
		restSSS = restS[:]
		DayofSSS = DayofS[:]
		DayofLLL = DayofL[:]
		pickSSS = pickS[:]
		pickLLL = pickL[:]
		countSSS = countS
		countLLL = countL
		check = 1 
		for i in range(len(restL)):
			restLL = restL[:]
			restSS = restS[:]
			DayofSS = DayofS[:]
			DayofLL = DayofL[:]
			pickSS = pickS[:]
			pickLL = pickL[:]
			countSS = countS
			countLL = countL
			current = restLL[i]

			Maynewday = list(map(lambda x : int(x),current[13:20]))
			Maynewday = [DayofLL[m] - Maynewday[m] for m in range(7)]
			pickornot = min(Maynewday)
			if pickornot >= 0 and check == 1:
				if current in restSS:
					restSS.remove(current)
				restLL.remove(current)
				pickLL.append(current)
				restLLL = restLL
				restSSS = restSS
				DayofSSS = DayofSS
				DayofLLL = Maynewday
				pickSSS = pickSS
				pickLLL = pickLL
				countSSS = countSS
				countLLS = countLL
				check = 0
			else:
				Maynewday = [DayofLL[m] + Maynewday[m] for m in range(7)]
		dfs(restLLL, restSSS, DayofSSS, DayofLLL, pickSSS, pickLLL, countSSS, countLLL+1)

inputfile = open('input22.txt')
outputfile = file('output.txt','w')
line = inputfile.readlines()

b = int(line[0])
p = int(line[1])
L = int(line[2])
S = int(line[3+L])
A = int(line[4+L+S])
Lid = []
Sid = []
Alist = []
restL = []
restS = []
DayofL = [b] * 7
DayofS = [p] * 7
pickS = []
pickL = []
Bothrest = []


for i in range(3, 3+L):
	Lid.append(line[i].strip('\n\r'))

for i in range(4+L, 4+L+S):
	Sid.append(line[i].strip('\n\r'))

for i in range(5+L+S, 5+L+S+A):
	Alist.append(line[i].strip('\n\r'))

for i in range(len(Alist)):
	temp = Alist[i].strip('\n\r')
	Applicantid = temp[0:5]
	Gender = temp[5]
	Age = int(temp[6:9])
	Pets = temp[9]
	Midical = temp[10]
	Car = temp[11]
	Diriverlicence = temp[12]
	DayOfNeed = temp[13:20]
	if Applicantid in Lid:
		occaupyday = list(map(lambda x :int(x),DayOfNeed))
		DayofL = [DayofL[i] - occaupyday[i] for i in range(7)]
	if Applicantid in Sid:
		occaupyday = list(map(lambda x :int(x),DayOfNeed))
		DayofS = [DayofS[i] - occaupyday[i] for i in range(7)]
	if Applicantid not in Lid and Applicantid not in Sid and Gender == 'F' and Age > 17 and Pets == 'N':
		restL.append(temp)
	if Applicantid not in Lid and Applicantid not in Sid and Midical == 'N' and Car == 'Y' and Diriverlicence == 'Y':
		restS.append(temp)

for i in range(len(Alist)):
	temp = Alist[i].strip('\n\r')
	if temp in restL and temp in restS:
		Bothrest.append(temp)

for i in range(len(Bothrest)):
	temp = Bothrest[i].strip('\n\r')
	if temp in restS:
		restS.remove(temp)

for i in range(len(Bothrest)):
	temp = Bothrest[i].strip('\n\r')
	if temp in restL:
		restL.remove(temp)

Bothrest = mergersort(Bothrest, len(Bothrest))
restS = mergersort(restS, len(restS))
restL = mergersort(restL, len(restL))


restS = Bothrest + restS
restL = Bothrest + restL
print restS
print restL

effcient = 0
best_list = []
good_list = []
efficiency_rate = 0
countL = 0
countS = 0
dfs(restL,restS,DayofS,DayofL,pickS,pickL,countS,countL)

print best_list

print time.clock() - t

outputfile.close()
inputfile.close()