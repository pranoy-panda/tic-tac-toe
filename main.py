#tic tac toe game
s=[]
count=0
def cross_marker(i):
   s[i]='X'

def zero_marker(i):
   s[i]='0'

def blank_marker():
    return ' '   
def mid_line():
    print '-----'

for i in range(9):
    s.append(blank_marker())
def board():
        print s[0]+'|'+s[1]+'|'+s[2]
        mid_line()
        print s[3]+'|'+s[4]+'|'+s[5]
        mid_line()
        print s[6]+'|'+s[7]+'|'+s[8]

def blank_board():
    s=[]
    for i in range(9):
        s.append(str(i))
    print s[0]+'|'+s[1]+'|'+s[2]
    mid_line()
    print s[3]+'|'+s[4]+'|'+s[5]
    mid_line()
    print s[6]+'|'+s[7]+'|'+s[8]


def declare_winner():
    if s[0]==s[1]==s[2]=='X' or s[3]==s[4]==s[5]=='X'  or  s[6]==s[7]==s[8]=='X' :
        print 'player1 wins'
        count=1
        
    elif s[0]==s[3]==s[6]=='X' or s[1]==s[4]==s[7]=='X'  or  s[2]==s[5]==s[8]=='X' :
        print 'player1 wins'
        count=1
    elif s[0]==s[4]==s[8]=='X' or s[2]==s[4]==s[6]=='X'   :
        print 'player1 wins'
        count=1
    
    elif s[0]==s[1]==s[2]=='0' or s[3]==s[4]==s[5]=='0'  or  s[6]==s[7]==s[8]=='0' :
        print 'player2 wins'
        count=1
    elif s[0]==s[3]==s[6]=='0' or s[1]==s[4]==s[7]=='0'  or  s[2]==s[5]==s[8]=='0' :
        print 'player2 wins'
        count=1
        
    elif s[0]==s[4]==s[8]=='0' or s[2]==s[4]==s[6]=='0'   :
        print 'player2 wins'
        count=1

        
blank_board()    
for i in range(9):
    s.append(blank_marker)

choice=raw_input('do you wish to play tic tac toe game,Y/N\n')
if choice=="Y":
	print 'let the game begin'

while choice=='Y':
    
    for i in range(9):
        print 'player 1'
        pl1=input()
        cross_marker(pl1)
        board()
        print 'player 2'
        pl2=input()
        zero_marker(pl2)
        board()
        declare_winner()

    if count==0:
        print 'draw'
       
    
    choice=raw_input('do you wish to play anathor match')
    count=0
