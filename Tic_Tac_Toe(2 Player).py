
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

#Check if the Tic tac Toe is Full,and there is no space left
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
  print('Do You Want to be Player 1 or Player 2')
  playerno=input()   #Choosing to be which Player
  Board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
  if playerno==2 :   #If Computer has to start First
   print('The computer will go first')
   while 1:
    #Do the Desired Move as per the algorithm
    CompMove(Board,compsym,mysym)
    
    #If Computer wins as per the current status
    if isWinner(compsym,Board):
     print("The Board Status after the move is:")
     print('\n')
     printboard(Board)
     print('\n')   
     print('The Computer Has Won ')
     break
    #If it is not a Winning State for the computer ,then print the Board Status
     print('\n')
     print("The Board Status after the move is:")
    print('\n')
    printboard(Board)
    print('\n')
    
    #If no more moves are possible and the Board Is Full
    if Full(Board):
       print('The Match Is Draw')
       break  
        
    #Print the Remaining  Board Positions that are available
    PrintRemain(Board)
    
    #Let the Player input the valid Move
    playermove(Board,mysym)
    print('\n')
    print("The Board Status after the move is:")
    print('\n')
    printboard(Board)
    
    
  else:
    #When Its the turn of the player to start 
    print("Start Your move:")
    
    while 1:
    #The player ,plays his Valid Move
     playermove(Board,mysym)
     print('\n')
     print("The Board Status after the move is:")
     print('\n')
     printboard(Board)
        
    #If no more moves are possible and the Board Is Full
     if Full(Board):
       print('The Match Is Draw')
       break 
    #If the Move of the player is the Winning Move
     if isWinner(mysym,Board):
        print("The Board Status after the move is:")
        print('\n')
        printboard(Board)
        print('\n')   
        print('Congrats!! You Won!!  ')
        break
      
     CompMove(Board,compsym,mysym)
    #IF The move of The computer is the Winning move
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
     PrintRemain(Board)
    
  print('Want TO play Again ?? Y or N')
  playagain=raw_input().upper()

  if playagain=='N':
    break;
    
main()