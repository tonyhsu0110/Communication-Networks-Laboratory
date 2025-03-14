#lab0_3

progg = []

def blank(totalM, second, kinds):
    #listB = [[0] * (kinds) for _ in range(totalM+1)]
    listB = [[0] * (totalM+1) for _ in range(kinds)]
    #print(listB)
    second.sort()
    second.reverse()
    #print(second)
    for k in range(totalM+1):
        progg.append(k)
    '''
    for k in range(0, kinds):
        listB[k][0] = second[k-1]
    for k in range(0, (totalM+1)):
        listB[0][k] = k-1
    '''
    for m in range(0, kinds):
        '''
        listB[m][0] = 0
        for n in range(1, (totalM+1)):
            if (progg[n] - second[m])<0:
                listB[m][n] = -1
        '''
        for n in range(0, (totalM+1)):
            if (progg[n] - second[m])<0:
                if n==0:
                    listB[m][n] = 0
                else:
                    listB[m][n] = -1
            else:
                
                if m==0:
                    if (progg[n]%second[0])==0:
                        listB[m][n] = progg[n]/second[0]
                    else:
                        listB[m][n] = -1
                else:
                    if listB[m][n-second[m]] == -1:
                        for t in range(m):
                            if listB[t][n]!=-1:
                                listB[m][n] = listB[t][n]
                                break
                            else:
                                listB[m][n] = -1
                        #listB[m][n] = -1
                    else:
                        listB[m][n] = listB[m][n-second[m]] +1
                        min = listB[m][n]
                        for p in range(m):
                            if(n==0):
                                min = 0
                            else:
                                if listB[p][n]!=-1:
                                    if (listB[p][n]<min):
                                        min = listB[p][n]
                                #if (listB[p][n]!=-1) and (listB[p][n]<min):
                                #    min = listB[p][n]
                        listB[m][n] = min
                    #listB[m][n] = min
                
    #print(listB)
    if totalM == 0:
        return 0
    else:
        return int(listB[kinds-1][totalM])

firstLine = []
secondLine = []
ans = []

a = int(input()) #how many testcase
#print(a)
for i in range(a):
    firstLine.clear()
    secondLine.clear()
    firstLine = list(map(int, input().split()))
    #print(len(firstLine))
    secondLine = list(map(int, input().split()))
    #print(len(secondLine))
    #kinds = firstLine[0]  #紙幣數量
    #totalMoney = firstLine[1]
    anstemp = blank(firstLine[1], secondLine, firstLine[0])
    ans.append(anstemp)
for r in range(a):
    print(ans[r])