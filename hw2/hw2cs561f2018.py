import time
t = time.clock()

def dfs(restL,restS,DayofS,DayofL,pickS,pickL,countS,countL):
	Spoint = (0,0,[])
	Lpoint = (0,0,[])
	if countS == Max:
		current = (p*7 - sum(DayofS), b*7 - sum(DayofL),pickS)
		return current

	size1 = 0
	for i in restS:
		size1+=sum(i[1])
	size1 =size1 + (p*7 - sum(DayofS))

	size2 = 0
	for i in restL:
		size2+=sum(i[1])
	size2 =size2 + (b*7 - sum(DayofL))

	if countS == countL:
		if restS:
			for i in range(len(restS)):
				restLL = restL[:]
				restSS = restS[:]
				DayofSS = DayofS[:]
				pickSS = pickS[:]

				current = restSS[i]
				# maptoint =  current[1]
				Maynewday = [DayofSS[m] - current[1][m] for m in range(7)]
				pickornot = min(Maynewday)
				if pickornot >= 0:
					if current in restLL:
						restLL.remove(current)
					restSS.remove(current)
					pickSS.append(current)
				else:
					Maynewday = DayofSS
				
				if size1 > Spoint[0]:
					point = dfs(restLL, restSS, Maynewday, DayofL, pickSS,pickL, countS+1, countL)
					if Spoint[0] < point[0]:
						Spoint = point

		else:
			point = dfs(restL,restS,DayofS,DayofL,pickS,pickL,countS+1,countL)
			Spoint = point
		
		return Spoint
			

	elif countL != countS:
		if restL:
			for i in range(len(restL)):
				restLL = restL[:]
				restSS = restS[:]
				DayofLL = DayofL[:]
				pickLL = pickL[:]
				
				current = restLL[i]

				# maptoint = list(map(lambda x : int(x),current[13:20]))
				Maynewday = [DayofLL[m] - current[1][m] for m in range(7)]
				pickornot = min(Maynewday)
				if pickornot >= 0:
					if current in restSS:
						restSS.remove(current)
					restLL.remove(current)
					pickLL.append(current)
				else:
					Maynewday = DayofLL
					# print Maynewday
				
				if size2 > Lpoint[1]:
					point = dfs(restLL, restSS, DayofS, Maynewday, pickS,pickLL, countS, countL+1)
					if Lpoint[1] < point[1]:
						Lpoint = point
		else:
			point = dfs(restL,restS,DayofS,DayofL,pickS,pickL,countS,countL+1)
			Lpoint = point
		
		return Lpoint
			

inputfile = open('bad8.txt')
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
	occaupyday = list(map(lambda x :int(x),DayOfNeed))
	if Applicantid in Lid:
		DayofL = [DayofL[i] - occaupyday[i] for i in range(7)]
	if Applicantid in Sid:
		DayofS = [DayofS[i] - occaupyday[i] for i in range(7)]
	if Applicantid not in Lid and Applicantid not in Sid and Gender == 'F' and Age > 17 and Pets == 'N':
		tuple1 = (Applicantid, occaupyday)
		restL.append(tuple1)
	if Applicantid not in Lid and Applicantid not in Sid and Midical == 'N' and Car == 'Y' and Diriverlicence == 'Y':
		tuple1 = (Applicantid,occaupyday)
		restS.append(tuple1)


Max = max(len(restL),len(restS))

countL = 0
countS = 0
# print restS
# print restL

point = dfs(restL,restS,DayofS,DayofL,pickS,pickL,countS,countL)
print point[2][0][0]


print time.clock() - t

outputfile.write(str(point[2][0][0]))

outputfile.close()
inputfile.close()