#lab0.1

def deal2(ev1):
    ev2 = ev1*2
    re = ev2//10 + ev2%10
    return re

def deal1(cardNum):
    sumOdd = int(cardNum[1]) + int(cardNum[3])
    even1 = (int(cardNum[0]))
    even2 = (int(cardNum[2]))
    sumEv1 = deal2(even1)
    sumEv2 = deal2(even2)
    sumEven = sumEv1 + sumEv2
    total = sumOdd + sumEven
    return total
    
num = int(input())
listAns = []
printCount = 0
for i in range(num):
    a, b, c, d = input().split()
    num1 = deal1(a)
    num2 = deal1(b)
    num3 = deal1(c)
    num4 = deal1(d)
    sum = num1 + num2 + num3 + num4
    judge = sum%10
    if judge == 0:
        listAns.append('Valid')
    else:
        listAns.append('Invalid')
while(printCount < num):
    print(listAns[printCount])
    printCount += 1