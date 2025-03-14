#lab0.1

num = int(input())
listAns = []
printCount = 0
'''
listAns = ['0']
printCount = 1
'''
for i in range(num):
    a, b, c, d = input().split()
    print(a, b, c, d)
    a, b, c, d = int(a), int(b), int(c), int(d)
    #print(a, b, c, d)
    e1 = a//1000
    e2 = (a//10)%10
    e3 = b//1000
    e4 = (b//10)%10
    e5 = c//1000
    e6 = (c//10)%10
    e7 = d//1000
    e8 = (d//10)%10
    #f ok
    f1 = e1*2
    f2 = e2*2
    f3 = e3*2
    f4 = e4*2
    f5 = e5*2
    f6 = e6*2
    f7 = e7*2
    f8 = e8*2
    #g ok
    g1 = f1//10 + f1%10
    g2 = f2//10 + f2%10
    g3 = f3//10 + f3%10
    g4 = f4//10 + f4%10
    g5 = f5//10 + f5%10
    g6 = f6//10 + f6%10
    g7 = f7//10 + f7%10
    g8 = f8//10 + f8%10
    #o ok
    o1 = (a//100)%10
    o2 = a%10
    o3 = (b//100)%10
    o4 = b%10
    o5 = (c//100)%10
    o6 = c%10
    o7 = (d//100)%10
    o8 = d%10
    print(g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8)
    print(o1 + o2 + o3 + o4 + o5 + o6 + o7 + o8)
    sum = g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8 + o1 + o2 + o3 + o4 + o5 + o6 + o7 + o8
    judge = sum%10
    if judge == 0:
        listAns.append('Valid')
    else:
        listAns.append('Invalid')
while(printCount <= num):
    print(listAns[printCount])
    printCount += 1