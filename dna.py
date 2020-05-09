import random

def evolve(x):
    index=random.randint(0,len(x)-1)
    p=random.randint(1,100)
    
    if (p==1):
        if (x[index]=='0'):
            x[index]=1
        else:
            x[index]=0
    


with open('C:/Users/Nishat/Desktop/dna.txt') as dna:
    x=dna.read()
    x=list(x)
for i in range(0,200):
    evolve(x)
print(x)