import random
def choose():
    words=['mountains','computer','mathematics','keyboard','scientific','rainbow','flavour']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumb=''.join(random.sample(word,len(word)))
    return jumb

def thank(p1n,p2n,p1s,p2s):
    print(p1n,', your score is',p1s)
    print(p2n,', your score is',p2s)
    print('thank you for playing this game')
    print('have a nice day')


def play():
    p1name=input('player1 please enter your name ::: ')
    p2name=input('player2 please enter your name ::: ')
    p1s=0
    p2s=0
    turn=0
    while(1):
        word=choose()
        question=jumble(word)
        print('Question :: ',question)
        if turn%2==0:
            print(p1name,'its your turn now')
            ans=input('Enter your guess :::  ')
            if ans==word:
                print('congrats you guessed it right')
                p1s+=1
                print(p1name,'your updated score is',p1s)
            else:
                print('sorry your guess was wrong the ans is',word)
            c=input('want to continue(y/n)')
            if c=='n':
                thank(p1name,p2name,p1s,p2s)
                break
        else:
            print(p2name,'its your turn now')
            ans=input('Enter your guess :::  ')
            if ans==word:
                print('congrats you guessed it right')
                p2s+=1
                print(p2name,'your updated score is',p2s)
            else:
                print('sorry your guess was wrong the ans is',word)
            c=input('want to continue(y/n)')
            if c=='n':
                thank(p1name,p2name,p1s,p2s)
                break
        turn+=1
        
