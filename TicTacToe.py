
#Input The Symbol

def inputSymbol():
 print('So select your Symbol -> X or O')
 symbol=raw_input().upper()
 while not(symbol=='X' or symbol=='O'):
  print('So select your Symbol -> X or O')
  symbol=raw_input().upper()
 if symbol=='X':
     return 'X'
 else:
   return 'O'
    
#Printing THE  Board
def printboard(Board):
 i=7;
 a=""
 while 1:
  for j in range(2):
   a=a+' '+Board[i]+' '+'|'
   i=i+1
  a=a+' '+Board[i]
  print(a)
  a=''
  i=i-5
  if(i<0):
   break
  print('---+---+---')
 

    
#State Of Board Is Winning
    
def isWinner(sym,Board):
    return ((Board[7]==sym and Board[8]==sym and Board[9]==sym)or
           (Board[4]==sym and Board[5]==sym and Board[6]==sym)or
           (Board[1]==sym and Board[2]==sym and Board[3]==sym)or
           (Board[7]==sym and Board[5]==sym and Board[3]==sym)or
           (Board[9]==sym and Board[5]==sym and Board[1]==sym)or
           (Board[7]==sym and Board[4]==sym and Board[1]==sym)or
           (Board[5]==sym and Board[8]==sym and Board[2]==sym)or
           (Board[3]==sym and Board[6]==sym and Board[9]==sym))

#Input the move from Player

def playermove(Board,mysym):
    
    while 1:
        print('Enter Your Valid Move')
        move=input()
        if move>=1 and move<=9 and Board[move]==' ':
         Board[move]=mysym
         break

#The Next Move of Computer will Win or Not
def CompMoveWin(Board,compsym):
    
    for i in range(1,10):
     if Board[i]==' ':
        Board[i]=compsym
        if isWinner(compsym,Board):
          return i
        Board[i]=' '
    return 0

#The Next Move of Player Will win or Not
def PlayerMoveWin(Board,compsym,mysym):
    
    for i in range(1,10):
     if Board[i]==' ':
      Board[i]=mysym
      if isWinner(mysym,Board):
        Board[i]=compsym
        return i
      Board[i]=' '
    return 0

#Any Corner Place Is Empty Or Not
def CheckCorner(Board,compsym):
    if Board[7]==' ':
        Board[7]=compsym
        return 7
    if Board[9]==' ':
        Board[9]=compsym
        return 9
    if Board[1]==' ':
        Board[1]=compsym
        return 1
    if Board[3]==' ':
        Board[3]=compsym
        return 3
    return 0

#Center Location is Empty OR not
def CheckCenter(Board,compsym):
    if Board[5]==' ':
        Board[5]=compsym
        return 5
    return 0

#Check if any of the other 4 locations are empty or not
def CheckOthers(Board,compsym):
   
    if Board[8]==' ':
        Board[8]=compsym
        return 8
    if Board[4]==' ':
        Board[4]=compsym
        return 4
    if Board[6]==' ':
        Board[6]=compsym
        return 6
    if Board[2]==' ':
        Board[2]=compsym
        return 2
    return 0
        
#Deciding The Move of the Computer
def CompMove(Board,compsym,mysym):
    if CompMoveWin(Board,compsym)!=0:
     return 1
    if PlayerMoveWin(Board,compsym,mysym)!=0:
     return 1
    if CheckCorner(Board,compsym)!=0:
     return 1
    if CheckCenter(Board,compsym)!=0:
     return 1
    if CheckOthers(Board,compsym)!=0:
     return 1
    return 0

def PrintRemain(Board):
 remain=''
 for i in range(1,10):
     if Board[i]==' ':
      remain=remain+' '+str(i)
 print('You can choose a Move from'+remain)

def Full(Board):
    for i in range(1,10):
        if Board[i]==' ':
            return 0
    return 1     
#Tic Tac Toe
def main():

 print('Enter Your Name')
 name=raw_input()
 print("Hello "+name+".Let's Play Tic-Tac-Toe")
 while 1:
  compsym=''
  mysym=''
  mysym=inputSymbol()
  if mysym=='X':
   compsym='O'
  else:
   compsym='X'
  print('The computer will go first')
  Board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

  while 1:
   val=CompMove(Board,compsym,mysym)
   if val==0:
    print('The Match Is Draw')
    break
   if isWinner(compsym,Board):
    print("The Board Status after the move is:")
    print('\n')
    printboard(Board)
    print('\n')   
    print('The Computer Has Won ')
    break
   print('\n')
   print("The Board Status after the move is:")
   print('\n')
   printboard(Board)
   print('\n')
   if Full(Board):
      print('The Match Is Draw')
      break  
   PrintRemain(Board)
   playermove(Board,mysym)
   print('\n')
   print("The Board Status after the move is:")
   print('\n')
   printboard(Board)
  print('Want TO play Again ?? Y or N')
  playagain=raw_input().upper()
  if playagain=='N':
    break;
    
main()