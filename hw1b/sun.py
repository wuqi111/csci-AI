# -*- coding: UTF-8 -*-
import numpy as np
from time import time

startTime = time()
inputFile = open("input12.txt")
outputFile = file("output.txt", "w")
lines = inputFile.readlines()
n = len(lines)


dimensions = int(lines[0])
policeOfficer = int(lines[1])
scooters = int(lines[2])


matrix = [0] * dimensions
for i in range(dimensions):
    matrix[i] = [0] * dimensions


col = [False] * dimensions
diag1 = [False] * (2*dimensions - 1)
diag2 = [False] * (2*dimensions - 1)


def isValid(x, y):
    return not col[x] and not diag1[x + y] and not diag2[x - y + dimensions - 1]

MaxCount = [0]
localMax = [0]

def dfs(idx, matrix, occupiedSpot, sumCount, policeOfficer, matrixRowIdx):

    if occupiedSpot == 0:
        MaxCount[0] = max(sumCount, MaxCount[0])
        print "Score",  MaxCount[0]
        return

    if idx == dimensions:
        return

    if sumCount + (id)

    for x in matrixRowIdx[idx]:
         if not isValid(x, idx):
                continue
         elif MaxCount[0] - matrix[idx][x] - sumCount > occupiedSpot * localMax[0]:
                continue
         elif dimensions - idx == occupiedSpot:
                col[x] = diag1[x + idx] = diag2[x - idx + dimensions - 1] = True
                dfs(idx + 1, matrix, occupiedSpot - 1, sumCount + matrix[idx][x], policeOfficer, matrixRowIdx)
                col[x] = diag1[x + idx] = diag2[x - idx + dimensions - 1] = False
         else:
                col[x] = diag1[x + idx] = diag2[x - idx + dimensions - 1] = True
                dfs(idx + 1, matrix, occupiedSpot - 1, sumCount + matrix[idx][x], policeOfficer, matrixRowIdx)
                col[x] = diag1[x + idx] = diag2[x - idx + dimensions - 1] = False
                dfs(idx + 1, matrix, occupiedSpot, sumCount, policeOfficer, matrixRowIdx)

    return


def generateRowIdxDesMatrix(matrix):
    matrixIdx = [0] * dimensions
    for i in range(dimensions):
        matrix[i] = np.array(matrix[i])
        matrixIdx[i] = list(np.argsort(-matrix[i]))
    return matrixIdx

def generateColIdxDesMatrix(matrix):
    matrix= np.array(matrix)
    matrixIdx2 = list(np.argsort(-matrix, axis=0))
    return matrixIdx2


for j in range(3, n):
    eachLine = lines[j].strip('\n')
    position = eachLine.split(",")
    posX = int(position[0])
    posY = int(position[1])
    matrix[posX][posY] += 1
    localMax[0] = max(localMax[0], matrix[posX][posY])

if dimensions <= 15:

        matrixRowIdx = generateRowIdxDesMatrix(matrix)
        posMax = np.where(matrix == np.max(matrix))


        dfs(0, matrix, policeOfficer, 0, policeOfficer, matrixRowIdx)

        ans = str(MaxCount[0])
        print "MaxCount", MaxCount[0]
        #outputFile.write(ans)

        stopTime = time()

        print "Time", stopTime - startTime



else:
    print "over dimension limitation"

inputFile.close()
outputFile.close()