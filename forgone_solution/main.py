t = int(input())
for i in range(1,t+1):
    a = []
    b = 0
    n = input()
    flag = False
    for digit in n:
        #print("Current: ",digit)
        if digit == '4':
            a.append('3')
            flag = True
        elif digit == '6':
            a.append('5')
            flag = True
        else:
            a.append(digit)
    if flag:
        a = int("".join(a))
        b = int(n) - a
    else:
        b = 1
        a = int(n) - b
    print("Case #"+str(i)+":",a,b)
