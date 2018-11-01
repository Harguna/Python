n=int(input())
for i in range(n):
    r=input()
    if ("SC" in r) or ("EC" in r) or ("SE" in r):
        print('no')
    else:
        print('yes')