for i in range(int(input())):
    x=[]
    for j in range(4):
        x.append(input())
    x=sorted(x)
    bar,barg=x[0].split()
    eib, eibg = x[1].split()
    mal, malg = x[2].split()
    rea, reag = x[3].split()
    if int(barg)>int(eibg) and int(reag)<int(malg):
        print('Barcelona')
    else:
        print('RealMadrid')

