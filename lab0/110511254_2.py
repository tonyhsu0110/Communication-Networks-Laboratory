#lab0_2

listD = []
#def cal(*listN):
def cal(listN):
    listD.clear()
    times = listN[0]
    listN.pop(0)
    listN.append(0)
    if(times == 1):
        return 0
    else:
        for j in range(times):
            a = 0
            b = 0
            for k in range(j+1):
                a += listN[k]
            for m in range(j+1, times+1):
                b += listN[m]
            a = a//(j+1)
            if times == (j+1):
                b = 0
            else:
                b = b//(times - (j+1))
            if(a>b):
                listD.append(a-b)
            else:
                listD.append(b-a)
            #print(listD[:])
        min = listD[0]
        minIn = 0
        for p in range(1, times):
            if listD[p] < min:
                min = listD[p]
                minIn = p
            #print('p and minIn are both ', p, ' , listD[', p, '] is ', listD[p], ', and min is ', min)
        return minIn

listAns = [] #store index
listDiff = [] #store diff
listNum = []

a = int(input()) #how many testcase
for i in range(a):
    listNum = list(map(int, input().split()))
    #print(listNum[:])
    result = cal(listNum)
    listAns.append(result)
for i in range(a):
    print(listAns[i])