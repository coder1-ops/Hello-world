def magic(n):
    magicSquare=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicSquare.append(l)
        
    i=n//2
    j=n-1
    count=1
    num=n*n
    
    while(count<=num):
        if(i==-1 and j==n):
            i=0
            j=n-2
        
        else:
            if(i==-1):
                i=n-1
            if(j==n):
                j=0
                
        if(magicSquare[i][j]!=0):
            i+=1
            j-=2
            continue
        
        else:
            magicSquare[i][j]=count
            count+=1
            
        i=i-1
        j=j+1
        
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j], end=" ")
        print()
        
    print("the sum across each row/col/diagonal is", n*(n**2 + 1)/2)
    
  