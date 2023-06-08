n=int(input("Enter the num : "))
if n%2==0:
    fr=n//2
    inf=fr+1
    inno=1
    sp=0
    for i in range(fr):
        sp+=1
        for j in range(sp):
            print(" ",end=" ")
        print(n,end='')
        n-=1
        inf-=1
        for k in range(inf):
            print("  ",end="  ")
        print(inno)
        inno+=1
    for p in range(fr):
        sp-=1
        for q in range(sp+1):
            print(" ",end=" ")
        print(n,end=" ")
        n-=1
        inf+=1
        for k in range(inf-1):
            print(" ",end="   ")
        print(inno)
        inno+=1
else:
    print("please enter an even number ")
    
    

    
    
