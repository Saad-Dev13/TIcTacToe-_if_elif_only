import random
#Global List
list1=[]
#main function
def main():
    #MAIN MENU INTERFACE
    print("     Main Menu     ")
    print("Welcome to the Game")
    print("1.) Multiplayer")
    print("2.) Single Player")
    print("3.) Exit")
    main_choice=input("Press 1 to play Multiplayer, press 2 to play Single Player, or any key to Exit: ")
    if main_choice=="1":
        multiplayer()
    elif main_choice=="2":
        single()
    else:
        exit()
#Multiplayer function
def multiplayer():
    print("Multiplayer Mode")
    #assigning variables
    n1,n2,n3,n4,n5,n6,n7,n8,n9=1,2,3,4,5,6,7,8,9
   
    #Player Name
    player1=input("Player1 Enter Your name: ").upper()
    player2=input("Player2 Enter Your name: ").upper()
    temp_name=player1
    #symbol choice
    sign_check=0
    while sign_check==0:
        print(player1,end='')
        symbol1=input(" Choose Your Symbol (X or O): ").upper()
        symbol2="O"
        if symbol1=="X":
            symbol1="X"
            symbol2="O"
            sign_check=1
        elif symbol1=="O":
            symbol1="O"
            symbol2="X"
            sign_check=1
        else:
            print("Invalid input.Choose your symbol again")
    print(player1,"Your symbol is",symbol1)
    print(player2,"Your symbol is",symbol2)
    limit_var=symbol1
    #toss
    toss_check=0
    while toss_check==0:
        print(player1,end='')
        choice=input(" make your call (Heads or Tails): ").lower()
        heads,tails="heads","tails"
        if choice==heads:
            choice=0
            toss_check=1
        elif choice==tails:
            choice=1
            toss_check=1
        else:
            print("Invalid Input, enter Heads or Tails only")
    import random
    toss=random.randint(0,1)
    if(choice!=toss):
        player1,player2=player2,player1
        symbol1=symbol2
        symbol2=limit_var
    print(player1,"have won the toss")
    
    #user turns
    counter=1
     #table
    print("    |    |    ")
    print("",n1," |",n2," | ",n3,"  ")
    print("----|----|----")
    print("    |    |    ")
    print("",n4," |",n5," | ",n6,"  ")
    print("----|----|----")
    print("    |    |    ")
    print("",n7," |",n8," | ",n9,"  ")
    print("    |    |    ")
    print("")
    while counter<=9:
        #Game Draw Condition will be checked First of all
        if counter==9:
            print("Game Draw")
            again_checker=input("Press 1 to play again or any other key to main menu")
            if again_checker=="1":
                multiplayer()
            else:    
                main()
        
    #input from user 1 
        check_a=True
        while check_a:
            print(player1,end='')
            try1=int(input(" Enter the number where you want to place your mark:"))
            #Checking if choice already taken
            if try1 in list1: continue
        #user 1 marking his/her choice on table and appending choice in list
            if(try1==n1):
                n1=symbol1
                list1.append(n1)
            elif(try1==n2):
                n2=symbol1
                list1.append(n2)
            elif(try1==n3):
                n3=symbol1
                list1.append(n3)  
            elif(try1==n4):
                n4=symbol1
                list1.append(n4)
            elif(try1==n5):
                n5=symbol1
                list1.append(n5)
            elif(try1==n6):
                n6=symbol1
                list1.append(n6)
            elif(try1==n7):
                n7=symbol1
                list1.append(n7)
            elif(try1==n8):
                n8=symbol1
                list1.append(n8)
            elif(try1==n9):
                n9=symbol1
                list1.append(n9)
            else:
                print("Invalid Input,Input Again")
                continue
                    
            print("    |    |    ")
            print("",n1," |",n2," | ",n3,"  ")
            print("----|----|----")
            print("    |    |    ")
            print("",n4," |",n5," | ",n6,"  ")
            print("----|----|----")
            print("    |    |    ")
            print("",n7," |",n8," | ",n9,"  ")
            print("    |    |    ")
            print("")
            #Checking winning condition
            if(n1==n2==n3=="X")or(n4==n5==n6=="X")or(n1==n4==n7=="X")or(n7==n8==n9=="X")or(n3==n6==n9=="X")or(n2==n5==n8=="X")or(n1==n5==n9=="X")or(n3==n5==n7=="X")or(n1==n2==n3=="O")or(n4==n5==n6=="O")or(n1==n4==n7=="O")or(n7==n8==n9=="O")or(n3==n6==n9=="O")or(n2==n5==n8=="O")or(n1==n5==n9=="O")or(n3==n5==n7=="O"):
                print(player1,"has won the game")
                #If wins
                again_checker=input("Press 1 if you want to exit or any key to go to main menu")
                if again_checker=="1":
                    multiplayer()
                else:    
                    main()
            counter+=1   
            #Inner while loop will end when checker is false
            check_a=False 
    #input from user 2
        check_b=True
        while check_b:
            print(player2,end='')
            try2=int(input(" Enter the number where you want to place your mark:"))
            #checking if choice already taken
            if try2 in list1: continue
            #user 2 marking choice on table and appending choice in list
            if(try2==n1):
                n1=symbol2
                list1.append(n1)
            elif(try2==n2):
                n2=symbol2
                list1.append(n2)
            elif(try2==n3):
                n3=symbol2
                list1.append(n3)
            elif(try2==n4):
                n4=symbol2
                list1.append(n4)
            elif(try2==n5):
                n5=symbol2
                list1.append(n5)
            elif(try2==n6):
                n6=symbol2
                list1.append(n6)
            elif(try2==n7):
                n7=symbol2
                list1.append(n7)
            elif(try2==n8):
                n8=symbol2
                list1.append(n8)
            elif(try2==n9):
                n9=symbol2
                list1.append(n9)
            else:
                print("Invalid Input,Input again")   
                continue 
            print("    |    |    ")
            print("",n1," |",n2," | ",n3,"  ")
            print("----|----|----")
            print("    |    |    ")
            print("",n4," |",n5," | ",n6,"  ")
            print("----|----|----")
            print("    |    |    ")
            print("",n7," |",n8," | ",n9,"  ")
            print("    |    |    ")
            print("")
            #checking winning condition
            if(n1==n2==n3=="O")or(n4==n5==n6=="O")or(n1==n4==n7=="O")or(n7==n8==n9=="O")or(n3==n6==n9=="O")or(n2==n5==n8=="O")or(n1==n5==n9=="O")or(n3==n5==n7=="O")or(n1==n2==n3=="X")or(n4==n5==n6=="X")or(n1==n4==n7=="X")or(n7==n8==n9=="X")or(n3==n6==n9=="X")or(n2==n5==n8=="X")or(n1==n5==n9=="X")or(n3==n5==n7=="X"):
                print(player2,"has won the game")
                again_checker=input("Press 1 if you want to play again or any key to go to main menu")
                if again_checker=="1":
                    multiplayer()
                else:
                    main()
            counter+=1
            check_b=False
    
        
        
def single():
    print("Single Player Mode")     
    n1,n2,n3,n4,n5,n6,n7,n8,n9=1,2,3,4,5,6,7,8,9
    print("Welcome to tictactoe!")
    player=input("Enter your name :")
    computer="computer"
    while True:
        symbol2=input("Choose a symbol X or O :").upper()
        if(symbol2=="X"):
            symbol2="X"
            csymbol="O"
            break
        elif symbol2 == "O":
            symbol2="O"
            csymbol="X"
            break

    while True:
        toss=int(input("Enter 1 for heads and 2 for tails :"))
        if toss == 1 or toss == 2:
            #little loop to make sure user only chose 1 or 2
            break
    from random import randint
    x=randint(1,2)
    #Condition if user wins the toss
    if(toss==x):
        print("You won, make your first move")
        count=1
        #next loop will terminate after 9 turns
        while count<=9:
            print("    |    |    ")
            print("",n1," |",n2," | ",n3,"  ")
            print("----|----|----")
            print("    |    |    ")
            print("",n4," |",n5," | ",n6,"  ")
            print("----|----|----")
            print("    |    |    ")
            print("",n7," |",n8," | ",n9,"  ")
            print("    |    |    ")
            print("")
            
            while True:
                n=int(input("Choose a number from 1 to 9 :"))
                #marking and also checking that place is already not taken
                if(n==1):
                    if n1 != csymbol and n1 != symbol2:
                        n1=symbol2
                        break
                elif(n==2):
                    if n2 != csymbol and n2 != symbol2:
                        n2=symbol2
                        break
                elif(n==3):
                    if n3 != csymbol and n3 != symbol2:
                        n3=symbol2
                        break
                elif(n==4):
                    if n4 != csymbol and n4 != symbol2:
                        n4=symbol2
                        break
                elif(n==5):
                    if n5 != csymbol and n5 != symbol2:
                        n5=symbol2
                        break
                elif(n==6):
                    if n6 != csymbol and n6 != symbol2:
                        n6=symbol2
                        break
                elif(n==7):
                    if n7 != csymbol and n7 != symbol2:
                        n7=symbol2
                        break
                elif(n==8):
                    if n8 != csymbol and n8 != symbol2:
                        n8=symbol2
                        break
                else:
                    if n9 != csymbol and n9 != symbol2:
                        n9=symbol2
                        break
            print("    |    |    ")
            print("",n1," |",n2," | ",n3,"  ")
            print("----|----|----")
            print("    |    |    ")
            print("",n4," |",n5," | ",n6,"  ")
            print("----|----|----")
            print("    |    |    ")
            print("",n7," |",n8," | ",n9,"  ")
            print("    |    |    ")
            print("")
            #if user has not chosen 5th place on table on first try, computer will take 5th place
            if count==1:
                print("Computer turn")
                if (n==1 or n==2 or n==3 or n==4 or n==6 or n==7 or n==8 or n==9):
                    n5=csymbol
                    #if user has taken 5th place then all places will be free, computer will take corner place 1
                elif (n==5):
                    n1=csymbol
            #Computer turn if its second turn
            if count==2:
                print("Computer turn")
                #Plus technique, marking upper side of plus if horzontals or verticals are taken and middle is computer symbol already
                if (n6==n4==symbol2 and n5==csymbol and n2!=csymbol):
                    n2=csymbol
                elif (n2==n8==symbol2 and n5==csymbol and n4!=csymbol):
                    n4=csymbol
                #One Turn technique, marking middle of turn
                elif (n8==n1==symbol2 or n2==n7==symbol2):
                    n4=csymbol
                elif (n8==n3==symbol2 or n2==n9==symbol2):
                    n6==csymbol
                elif (n6==n7==symbol2 or n4==n9==symbol2):
                    n8=csymbol
                elif (n6==n1==symbol2 or n4==n3==symbol2):
                    n2=csymbol
                #Breaking Two Combos, 3rd place empty
                elif (n3==n7==symbol2):
                    n4=csymbol
                elif (n1==n9==symbol2):
                    n6=csymbol
                #V turn technique, two combos , 3rd is already taken by computer
                elif (n1==n5==symbol2 and n9==csymbol):
                    n3=csymbol
                elif (n9==n5==symbol2 and n1==csymbol):
                    n3=csymbol
                elif (n3==n5==symbol2 and n7==csymbol):
                    n1=csymbol
                #again breaking two combo    
                elif (n7==n5==symbol2 and n3!=csymbol):
                    n3=csymbol
                elif (n2==n4==symbol2):
                    n1=csymbol
                elif (n4==n8==symbol2):
                    n7=csymbol
                elif (n8==n6==symbol2):
                    n9=csymbol
                elif (n2==n6==symbol2):
                    n3=csymbol
                elif (n1==symbol2 and n3==symbol2):
                    n2=csymbol
                elif (n4==symbol2 and n6==symbol2):
                    n5=csymbol
                elif (n7==symbol2 and n9==symbol2):
                    n8=csymbol
                elif (n1==symbol2 and n7==symbol2):
                    n4=csymbol
                elif (n2==symbol2 and n8==symbol2):
                    n5=csymbol
                elif (n3==symbol2 and n9==symbol2):
                    n6=csymbol
                elif (n1==symbol2 and n9==symbol2):
                    n5=csymbol
                elif (n3==symbol2 and n7==symbol2):
                    n5=csymbol
                elif (n5==symbol2 and n3==symbol2):
                    n7=csymbol
                elif (n1==symbol2 and n2==symbol2):
                    n3=csymbol
                elif (n4==symbol2 and n5==symbol2):
                    n6=csymbol
                elif (n7==symbol2 and n8==symbol2):
                    n9=csymbol
                elif (n3==symbol2 and n2==symbol2):
                    n1=csymbol
                elif (n6==symbol2 and n5==symbol2):
                    n4=csymbol
                elif (n8==symbol2 and n9==symbol2):
                    n7=csymbol
                elif (n1==symbol2 and n4==symbol2):
                    n7=csymbol
                elif (n2==symbol2 and n5==symbol2):
                    n8=csymbol
                elif (n3==symbol2 and n6==symbol2):
                    n9=csymbol
                elif (n7==symbol2 and n4==symbol2):
                    n1=csymbol
                elif (n8==symbol2 and n5==symbol2):
                    n2=csymbol
                elif (n9==symbol2 and n6==symbol2):
                    n3=csymbol
                elif (n1==symbol2 and n5==symbol2):
                    n9=csymbol
                elif (n9==symbol2 and n5==symbol2):
                    n1=csymbol
                elif (n3==symbol2 and n5==symbol2):
                    n7=csymbol
                elif (n7==symbol2 and n5==symbol2):
                    n3=csymbol 
                #two are taken by computer completing 3rd box    
                elif (n1==csymbol and n3==csymbol):
                    n2=csymbol
                elif (n4==csymbol and n6==csymbol):
                    n5=csymbol
                elif (n7==csymbol and n9==csymbol):
                    n8=csymbol
                elif (n8==csymbol and n7==csymbol):
                    n4=csymbol
                elif (n2==csymbol and n8==csymbol):
                    n5=csymbol
                elif (n3==csymbol and n9==csymbol):
                    n6=csymbol
                elif (n1==csymbol and n9==csymbol):
                    n5=csymbol
                elif (n3==csymbol and n7==csymbol):
                    n5=csymbol
                elif (n5==csymbol and n3==csymbol):
                    n7=csymbol
                elif (n1==csymbol and n2==csymbol):
                    n3=csymbol
                elif (n4==csymbol and n5==csymbol):
                    n6=csymbol
                elif (n7==csymbol and n8==csymbol):
                    n9=csymbol
                elif (n3==csymbol and n2==csymbol):
                    n1=csymbol
                elif (n6==csymbol and n5==csymbol):
                    n4=csymbol
                elif (n8==csymbol and n9==csymbol):
                    n7=csymbol
                elif (n1==csymbol and n4==csymbol):
                    n7=csymbol
                elif (n2==csymbol and n5==csymbol):
                    n8=csymbol
                elif (n3==csymbol and n6==csymbol):
                    n9=csymbol
                elif (n7==csymbol and n4==csymbol):
                    n1=csymbol
                elif (n8==csymbol and n5==csymbol):
                    n2=csymbol
                elif (n9==csymbol and n6==csymbol):
                    n3=csymbol
                elif (n1==csymbol and n5==csymbol):
                    n9=csymbol
                elif (n9==csymbol and n5==csymbol):
                    n1=csymbol
                elif (n3==csymbol and n5==csymbol):
                    n7=csymbol
                elif (n7==csymbol and n5==csymbol):
                    n3=csymbol
            if count==3:
                print("Computer turn")
                if (n1==n3==csymbol and n2!=symbol2):
                    n2=csymbol
                elif (n1==n3==symbol2 and n2!=csymbol):
                    n2=csymbol
                elif (n4==n6==csymbol and n5!=symbol2):
                    n5=csymbol
                elif (n7==n9==csymbol and n8!=symbol2):
                    n8=csymbol
                elif (n8==n7==csymbol and n4!=symbol2):
                    n4=csymbol
                elif (n2==n8==csymbol and n5!=symbol2):
                    n5=csymbol
                elif (n3==n9==csymbol and n6!=symbol2):
                    n6=csymbol
                elif (n1==n9==csymbol and n5!=symbol2):
                    n5=csymbol
                elif (n3==n7==csymbol and n5!=symbol2):
                    n5=csymbol
                elif (n5==n3==csymbol and n7!=symbol2):
                    n7=csymbol
                elif (n1==n2==csymbol and n3!=symbol2):
                    n3=csymbol
                elif (n4==n5==csymbol and n6!=symbol2):
                    n6=csymbol
                elif (n7==n8==csymbol and n9!=symbol2):
                    n9=csymbol
                elif (n3==n2==csymbol and n1!=symbol2):
                    n1=csymbol
                elif (n6==n5==csymbol and n4!=symbol2):
                    n4=csymbol
                elif (n8==n9==csymbol and n7!=symbol2):
                    n7=csymbol
                elif (n1==n4==csymbol and n7!=symbol2):
                    n7=csymbol
                elif (n2==n5==csymbol and n8!=symbol2):
                    n8=csymbol
                elif (n3==n6==csymbol and n9!=symbol2):
                    n9=csymbol
                elif (n7==n4==csymbol and n1!=symbol2):
                    n1=csymbol
                elif (n8==n5==csymbol and n2!=symbol2):
                    n2=csymbol
                elif (n9==n6==csymbol and n3!=symbol2):
                    n3=csymbol
                elif (n1==n5==csymbol and n9!=symbol2):
                    n9=csymbol
                elif (n9==n5==csymbol and n1!=symbol2):
                    n1=csymbol
                elif (n3==n5==csymbol and n7!=symbol2):
                    n7=csymbol
                elif (n7==n5==csymbol and n3!=symbol2):
                    n3=csymbol
                elif (n3==n6==symbol2 and n9!=csymbol):
                    n9=csymbol
                elif (n4==n6==symbol2 and n5!=csymbol):
                    n5=csymbol
                elif (n7==n9==symbol2 and n8!=csymbol):
                    n8=csymbol
                elif (n1==n7==symbol2 and n4!=csymbol):
                    n4=csymbol
                elif (n2==n8==symbol2 and n5!=csymbol):
                    n5=csymbol
                elif (n3==n9==symbol2 and n6!=csymbol):
                    n6=csymbol
                elif (n1==n9==symbol2 and n5!=csymbol):
                    n5=csymbol
                elif (n3==n7==symbol2 and n5!=csymbol):
                    n5=csymbol
                elif (n5==n3==symbol2 and n7!=csymbol):
                    n7=csymbol
                elif (n1==n2==symbol2 and n3!=csymbol):
                    n3=csymbol
                elif (n4==n5==symbol2 and n6!=csymbol):
                    n6=csymbol
                elif (n7==n8==symbol2 and n9!=csymbol):
                    n9=csymbol
                elif (n3==n2==symbol2 and n1!=csymbol):
                    n1=csymbol
                elif (n6==n5==symbol2 and n4!=csymbol):
                    n4=csymbol
                elif (n8==n9==symbol2 and n7!=csymbol):
                    n7=csymbol
                elif (n1==n4==symbol2 and n7!=csymbol):
                    n7=csymbol
                elif (n2==n5==symbol2 and n8!=csymbol):
                    n8=csymbol
                elif (n7==n4==symbol2 and n1!=csymbol):
                    n1=csymbol
                elif (n8==n5==symbol2 and n2!=csymbol):
                    n2=csymbol
                elif (n9==n6==symbol2 and n3!=csymbol):
                    n3=csymbol
                elif (n1==n5==symbol2 and n9!=csymbol):
                    n9=csymbol
                elif (n9==n5==symbol2 and n1!=csymbol):
                    n1=csymbol
                elif (n3==n5==symbol2 and n7!=csymbol):
                    n7=csymbol
                elif (n7==n5==symbol2 and n3!=csymbol):
                    n3=csymbol
                elif (n2==n4==symbol2 and n1!=csymbol):
                    n1=csymbol
                elif (n4==n8==symbol2 and n7!=csymbol):
                    n7=csymbol
                elif (n8==n6==symbol2 and n9!=csymbol):
                    n9=csymbol
                elif (n2==n6==symbol2 and n3!=csymbol):
                    n3=csymbol
                elif (n2==n4==n9==symbol2 and n3!=csymbol):
                    n3=csymbol
                elif (n8==n6==n1==symbol2 and n7!=csymbol):
                    n7=csymbol
                elif (n2==n6==n7==symbol2 and n1!=csymbol):
                    n1=csymbol
                elif (n4==n8==n3==symbol2 and n9!=csymbol):
                    n9=csymbol
                elif (n1==n3==n8==symbol2 and n9!=csymbol):
                    n9=csymbol
                elif (n1==n7==n6==symbol2 and n3!=csymbol):
                    n3=csymbol
                elif (n7==n9==n2==symbol2 and n1!=csymbol):
                    n1=csymbol
                elif (n9==n3==n4==symbol2 and n7!=csymbol):
                    n7=csymbol
            if(n1==n2==n3 or n4==n5==n6 or n7==n8==n9 or n7==n8==n9 or n1==n5==n9 or n3==n5==n7 or n1==n4==n7 or n2==n5==n8 or n3==n6==n9):
                print("    |    |    ")
                print("",n1," |",n2," | ",n3,"  ")
                print("----|----|----")
                print("    |    |    ")
                print("",n4," |",n5," | ",n6,"  ")
                print("----|----|----")
                print("    |    |    ")
                print("",n7," |",n8," | ",n9,"  ")
                print("    |    |    ")
                print("")
                print(player,"lost")
                again_checker=input("press 1 to play again or any key to go to main menu:")
                if again_checker==1:
                    single()
                else:
                    main()
            if count==4:
                print("Computer turn")
                if (n1==n3==csymbol and n2!=symbol2):
                    n2=csymbol
                elif (n4==n6==csymbol and n5!=symbol2):
                    n5=csymbol
                elif (n7==n9==csymbol and n8!=symbol2):
                    n8=csymbol
                elif (n8==n7==csymbol and n4!=symbol2):
                    n4=csymbol
                elif (n2==n8==csymbol and n5!=symbol2):
                    n5=csymbol
                elif (n3==n9==csymbol and n6!=symbol2):
                    n6=csymbol
                elif (n1==n9==csymbol and n5!=symbol2):
                    n5=csymbol
                elif (n3==n7==csymbol and n5!=symbol2):
                    n5=csymbol
                elif (n5==n3==csymbol and n7!=symbol2):
                    n7=csymbol
                elif (n1==n2==csymbol and n3!=symbol2):
                    n3=csymbol
                elif (n4==n5==csymbol and n6!=symbol2):
                    n6=csymbol
                elif (n7==n8==csymbol and n9!=symbol2):
                    n9=csymbol
                elif (n3==n2==csymbol and n1!=symbol2):
                    n1=csymbol
                elif (n6==n5==csymbol and n4!=symbol2):
                    n4=csymbol
                elif (n8==n9==csymbol and n7!=symbol2):
                    n7=csymbol
                elif (n1==n4==csymbol and n7!=symbol2):
                    n7=csymbol
                elif (n2==n5==csymbol and n8!=symbol2):
                    n8=csymbol
                elif (n3==n6==csymbol and n9!=symbol2):
                    n9=csymbol
                elif (n7==n4==csymbol and n1!=symbol2):
                    n1=csymbol
                elif (n8==n5==csymbol and n2!=symbol2):
                    n2=csymbol
                elif (n9==n6==csymbol and n3!=symbol2):
                    n3=csymbol
                elif (n1==n5==csymbol and n9!=symbol2):
                    n9=csymbol
                elif (n9==n5==csymbol and n1!=symbol2):
                    n1=csymbol
                elif (n3==n5==csymbol and n7!=symbol2):
                    n7=csymbol
                elif (n7==n5==csymbol and n3!=symbol2):
                    n3=csymbol
                elif (n3==n6==symbol2 and n9!=csymbol):
                    n9=csymbol
                elif (n1==n3==symbol2 and n2!=csymbol):
                    n2=csymbol
                elif (n4==n6==symbol2 and n5!=csymbol):
                    n5=csymbol
                elif (n7==n9==symbol2 and n8!=csymbol):
                    n8=csymbol
                elif (n1==n7==symbol2 and n4!=csymbol):
                    n4=csymbol
                elif (n2==n8==symbol2 and n5!=csymbol):
                    n5=csymbol
                elif (n3==n9==symbol2 and n6!=csymbol):
                    n6=csymbol
                elif (n1==n9==symbol2 and n5!=csymbol):
                    n5=csymbol
                elif (n3==n7==symbol2 and n5!=csymbol):
                    n5=csymbol
                elif (n5==n3==symbol2 and n7!=csymbol):
                    n7=csymbol
                elif (n1==n2==symbol2 and n3!=csymbol):
                    n3=csymbol
                elif (n4==n5==symbol2 and n6!=csymbol):
                    n6=csymbol
                elif (n7==n8==symbol2 and n9!=csymbol):
                    n9=csymbol
                elif (n3==n2==symbol2 and n1!=csymbol):
                    n1=csymbol
                elif (n6==n5==symbol2 and n4!=csymbol):
                    n4=csymbol
                elif (n8==n9==symbol2 and n7!=csymbol):
                    n7=csymbol
                elif (n1==n4==symbol2 and n7!=csymbol):
                    n7=csymbol
                elif (n2==n5==symbol2 and n8!=csymbol):
                    n8=csymbol
                elif (n7==n4==symbol2 and n1!=csymbol):
                    n1=csymbol
                elif (n8==n5==symbol2 and n2!=csymbol):
                    n2=csymbol
                elif (n9==n6==symbol2 and n3!=csymbol):
                    n3=csymbol
                elif (n1==n5==symbol2 and n9!=csymbol):
                    n9=csymbol
                elif (n9==n5==symbol2 and n1!=csymbol):
                    n1=csymbol
                elif (n3==n5==symbol2 and n7!=csymbol):
                    n7=csymbol
                elif (n7==n5==symbol2 and n3!=csymbol):
                    n3=csymbol
                elif (n1==n3==n5==n8==symbol2 and n4!=csymbol):
                    n4=csymbol
                elif (n1==n7==n5==n6==symbol2 and n2!=csymbol):
                    n2=csymbol
                elif (n2==n5==n7==n9==symbol2 and n6!=csymbol):
                    n6=csymbol
                elif (n3==n9==n5==n4==symbol2 and n8!=csymbol):
                    n8=csymbol
            if(n1==n2==n3 or n4==n5==n6 or n7==n8==n9 or n7==n8==n9 or n1==n5==n9 or n3==n5==n7 or n1==n4==n7 or n2==n5==n8 or n3==n6==n9):
                print("    |    |    ")
                print("",n1," |",n2," | ",n3,"  ")
                print("----|----|----")
                print("    |    |    ")
                print("",n4," |",n5," | ",n6,"  ")
                print("----|----|----")
                print("    |    |    ")
                print("",n7," |",n8," | ",n9,"  ")
                print("    |    |    ")
                print("")
                print(player,"You lost")
                again_checker=input("Press 1 to play again or any key to go to main menu:")
                if again_checker==1:
                    single()
                else:
                    main()
            if count==5:
                print("Game Draw")
                again_checker=input("Press 1 to play again or any key to go to main menu:: ")
                if again_checker=="1":
                    single()
                else:
                    main()
            count+=1
        
    #Condition if computer wins the toss    
    else:
        print("You lost the toss now computer will make the first move")
        count=1
        while count<=9:
            if count>=2:
                while True:
                    n=int(input("Choose a number from 1 to 9 :"))
                    if(n==1):
                        if n1 != csymbol and n1 != symbol2:
                            n1=symbol2
                            break
                    elif(n==2):
                        if n2 != csymbol and n2 != symbol2:
                            n2=symbol2
                            break
                    elif(n==3):
                        if n3 != csymbol and n3 != symbol2:
                            n3=symbol2
                            break
                    elif(n==4):
                        if n4 != csymbol and n4 != symbol2:
                            n4=symbol2
                            break
                    elif(n==5):
                        if n5 != csymbol and n5 != symbol2:
                            n5=symbol2
                            break
                    elif(n==6):
                        if n6 != csymbol and n6 != symbol2:
                            n6=symbol2
                            break
                    elif(n==7):
                        if n7 != csymbol and n7 != symbol2:
                            n7=symbol2
                            break
                    elif(n==8):
                        if n8 != csymbol and n8 != symbol2:
                            n8=symbol2
                            break
                    else:
                        if n9 != csymbol and n9 != symbol2:
                            n9=symbol2
                            break
                print("    |    |    ")
                print("",n1," |",n2," | ",n3,"  ")
                print("----|----|----")
                print("    |    |    ")
                print("",n4," |",n5," | ",n6,"  ")
                print("----|----|----")
                print("    |    |    ")
                print("",n7," |",n8," | ",n9,"  ")
                print("    |    |    ")
                print("")
            #always chosing 5th place on first try
            if count==1:
                n5=csymbol
                print("    |    |    ")
                print("",n1," |",n2," | ",n3,"  ")
                print("----|----|----")
                print("    |    |    ")
                print("",n4," |",n5," | ",n6,"  ")
                print("----|----|----")
                print("    |    |    ")
                print("",n7," |",n8," | ",n9,"  ")
                print("    |    |    ")
                print("")
                print("Your turn")
            if count==2:
                print("Computer turn")
                if (n1==symbol2 and n4!=csymbol):
                    n4=csymbol
                elif (n2==symbol2 and n1!=csymbol):
                    n1=csymbol
                elif (n3==symbol2 and n2!=csymbol):
                    n2=csymbol
                elif (n4==symbol2 and n1!=csymbol):
                    n1=csymbol
                elif (n6==symbol2 and n9!=csymbol):
                    n9=csymbol
                elif (n7==symbol2 and n8!=csymbol):
                    n8=csymbol
                elif (n8==symbol2 and n7!=csymbol):
                    n7=csymbol
                elif (n9==symbol2 and n6!=csymbol):
                    n6=csymbol
                print("    |    |    ")
                print("",n1," |",n2," | ",n3,"  ")
                print("----|----|----")
                print("    |    |    ")
                print("",n4," |",n5," | ",n6,"  ")
                print("----|----|----")
                print("    |    |    ")
                print("",n7," |",n8," | ",n9,"  ")
                print("    |    |    ")
                print("")
            if count==3:
                print("Computer turn")
                if (n1==n3==csymbol and n2!=symbol2):
                    n2=csymbol
                elif (n4==n6==csymbol and n5!=symbol2):
                    n5=csymbol
                elif (n7==n9==csymbol and n8!=symbol2):
                    n8=csymbol
                elif (n8==n7==csymbol and n4!=symbol2):
                    n4=csymbol
                elif (n2==n8==csymbol and n5!=symbol2):
                    n5=csymbol
                elif (n3==n9==csymbol and n6!=symbol2):
                    n6=csymbol
                elif (n1==n9==csymbol and n5!=symbol2):
                    n5=csymbol
                elif (n3==n7==csymbol and n5!=symbol2):
                    n5=csymbol
                elif (n5==n3==csymbol and n7!=symbol2):
                    n7=csymbol
                elif (n1==n2==csymbol and n3!=symbol2):
                    n3=csymbol
                elif (n4==n5==csymbol and n6!=symbol2):
                    n6=csymbol
                elif (n7==n8==csymbol and n9!=symbol2):
                    n9=csymbol
                elif (n3==n2==csymbol and n1!=symbol2):
                    n1=csymbol
                elif (n6==n5==csymbol and n4!=symbol2):
                    n4=csymbol
                elif (n8==n9==csymbol and n7!=symbol2):
                    n7=csymbol
                elif (n1==n4==csymbol and n7!=symbol2):
                    n7=csymbol
                elif (n2==n5==csymbol and n8!=symbol2):
                    n8=csymbol
                elif (n3==n6==csymbol and n9!=symbol2):
                    n9=csymbol
                elif (n7==n4==csymbol and n1!=symbol2):
                    n1=csymbol
                elif (n8==n5==csymbol and n2!=symbol2):
                    n2=csymbol
                elif (n9==n6==csymbol and n3!=symbol2):
                    n3=csymbol
                elif (n1==n5==csymbol and n9!=symbol2):
                    n9=csymbol
                elif (n9==n5==csymbol and n1!=symbol2):
                    n1=csymbol
                elif (n3==n5==csymbol and n7!=symbol2):
                    n7=csymbol
                elif (n7==n5==csymbol and n3!=symbol2):
                    n3=csymbol
                elif (n1==n5==csymbol and n9==symbol2 and n6!=csymbol):
                    n6=csymbol
                elif (n4==n5==csymbol and n6==symbol2 and n3!=csymbol):
                    n3=csymbol
                elif (n7==n5==csymbol and n3==symbol2 and n3!=csymbol):
                    n6=csymbol
                elif (n8==n5==csymbol and n2==symbol2 and n1!=csymbol):
                    n1=csymbol
                elif (n9==n5==csymbol and n1==symbol2 and n4!=csymbol):
                    n4=csymbol
                elif (n6==n5==csymbol and n4==symbol2 and n7!=csymbol):
                    n7=csymbol
                elif (n3==n5==csymbol and n7==symbol2 and n8!=csymbol):
                    n8=csymbol
                elif (n2==n5==csymbol and n8==symbol2 and n9!=csymbol):
                    n9=csymbol
                print("    |    |    ")
                print("",n1," |",n2," | ",n3,"  ")
                print("----|----|----")
                print("    |    |    ")
                print("",n4," |",n5," | ",n6,"  ")
                print("----|----|----")
                print("    |    |    ")
                print("",n7," |",n8," | ",n9,"  ")
                print("    |    |    ")
                print("")
            if count==4:
                print("Computer turn")
                if (n3==n6==symbol2 and n9!=csymbol):
                    n9=csymbol
                elif (n1==n3==symbol2 and n2!=csymbol):
                    n2=csymbol
                elif (n4==n6==symbol2 and n5!=csymbol):
                    n5=csymbol
                elif (n7==n9==symbol2 and n8!=csymbol):
                    n8=csymbol
                elif (n1==n7==symbol2 and n4!=csymbol):
                    n4=csymbol
                elif (n2==n8==symbol2 and n5!=csymbol):
                    n5=csymbol
                elif (n3==n9==symbol2 and n6!=csymbol):
                    n6=csymbol
                elif (n1==n9==symbol2 and n5!=csymbol):
                    n5=csymbol
                elif (n3==n7==symbol2 and n5!=csymbol):
                    n5=csymbol
                elif (n5==n3==symbol2 and n7!=csymbol):
                    n7=csymbol
                elif (n1==n2==symbol2 and n3!=csymbol):
                    n3=csymbol
                elif (n4==n5==symbol2 and n6!=csymbol):
                    n6=csymbol
                elif (n7==n8==symbol2 and n9!=csymbol):
                    n9=csymbol
                elif (n3==n2==symbol2 and n1!=csymbol):
                    n1=csymbol
                elif (n6==n5==symbol2 and n4!=csymbol):
                    n4=csymbol
                elif (n8==n9==symbol2 and n7!=csymbol):
                    n7=csymbol
                elif (n1==n4==symbol2 and n7!=csymbol):
                    n7=csymbol
                elif (n2==n5==symbol2 and n8!=csymbol):
                    n8=csymbol
                elif (n7==n4==symbol2 and n1!=csymbol):
                    n1=csymbol
                elif (n8==n5==symbol2 and n2!=csymbol):
                    n2=csymbol
                elif (n9==n6==symbol2 and n3!=csymbol):
                    n3=csymbol
                elif (n1==n5==symbol2 and n9!=csymbol):
                    n9=csymbol
                elif (n9==n5==symbol2 and n1!=csymbol):
                    n1=csymbol
                elif (n3==n5==symbol2 and n7!=csymbol):
                    n7=csymbol
                elif (n7==n5==symbol2 and n3!=csymbol):
                    n3=csymbol
                elif (n1==n3==csymbol and n2!=symbol2):
                    n2=csymbol
                elif (n4==n6==csymbol and n5!=symbol2):
                    n5=csymbol
                elif (n7==n9==csymbol and n8!=symbol2):
                    n8=csymbol
                elif (n8==n7==csymbol and n4!=symbol2):
                    n4=csymbol
                elif (n2==n8==csymbol and n5!=symbol2):
                    n5=csymbol
                elif (n3==n9==csymbol and n6!=symbol2):
                    n6=csymbol
                elif (n1==n9==csymbol and n5!=symbol2):
                    n5=csymbol
                elif (n3==n7==csymbol and n5!=symbol2):
                    n5=csymbol
                elif (n5==n3==csymbol and n7!=symbol2):
                    n7=csymbol
                elif (n1==n2==csymbol and n3!=symbol2):
                    n3=csymbol
                elif (n4==n5==csymbol and n6!=symbol2):
                    n6=csymbol
                elif (n7==n8==csymbol and n9!=symbol2):
                    n9=csymbol
                elif (n3==n2==csymbol and n1!=symbol2):
                    n1=csymbol
                elif (n6==n5==csymbol and n4!=symbol2):
                    n4=csymbol
                elif (n8==n9==csymbol and n7!=symbol2):
                    n7=csymbol
                elif (n1==n4==csymbol and n7!=symbol2):
                    n7=csymbol
                elif (n2==n5==csymbol and n8!=symbol2):
                    n8=csymbol
                elif (n3==n6==csymbol and n9!=symbol2):
                    n9=csymbol
                elif (n7==n4==csymbol and n1!=symbol2):
                    n1=csymbol
                elif (n8==n5==csymbol and n2!=symbol2):
                    n2=csymbol
                elif (n9==n6==csymbol and n3!=symbol2):
                    n3=csymbol
                elif (n1==n5==csymbol and n9!=symbol2):
                    n9=csymbol
                elif (n9==n5==csymbol and n1!=symbol2):
                    n1=csymbol
                elif (n3==n5==csymbol and n7!=symbol2):
                    n7=csymbol
                elif (n7==n5==csymbol and n3!=symbol2):
                    n3=csymbol
                elif (n9==n5==n2==csymbol and n7!=symbol2):
                    n7=csymbol
                elif (n3==n5==n4==csymbol and n9!=symbol2):
                    n9=csymbol
                elif (n1==n5==n8==csymbol and n3!=symbol2):
                    n3=csymbol
                elif (n7==n5==n6==csymbol and n1!=symbol2):
                    n1=csymbol
                elif (n7==n5==n2==csymbol and n9!=symbol2):
                    n9=csymbol
                elif (n9==n5==n4==csymbol and n3!=symbol2):
                    n3=csymbol
                elif (n3==n5==n8==csymbol and n1!=symbol2):
                    n1=csymbol
                elif (n1==n5==n6==csymbol and n7!=symbol2):
                    n7=csymbol
                print("    |    |    ")
                print("",n1," |",n2," | ",n3,"  ")
                print("----|----|----")
                print("    |    |    ")
                print("",n4," |",n5," | ",n6,"  ")
                print("----|----|----")
                print("    |    |    ")
                print("",n7," |",n8," | ",n9,"  ")
                print("    |    |    ")
                print("")
            if count==5:
                print("Computer turn")
                if (n1!=symbol2 and n1!=csymbol):
                    n1=csymbol
                elif (n2!=symbol2 and n2!=csymbol):
                    n2=csymbol
                elif (n3!=symbol2 and n3!=csymbol):
                    n3=csymbol
                elif (n4!=symbol2 and n4!=csymbol):
                    n4=csymbol
                elif (n5!=symbol2 and n5!=csymbol):
                    n5=csymbol
                elif (n6!=symbol2 and n6!=csymbol):
                    n6=csymbol
                elif (n7!=symbol2 and n7!=csymbol):
                    n7=csymbol
                elif (n8!=symbol2 and n8!=csymbol):
                    n8=csymbol
                elif (n9!=symbol2 and n9!=csymbol):
                    n9=csymbol
                print("    |    |    ")
                print("",n1," |",n2," | ",n3,"  ")
                print("----|----|----")
                print("    |    |    ")
                print("",n4," |",n5," | ",n6,"  ")
                print("----|----|----")
                print("    |    |    ")
                print("",n7," |",n8," | ",n9,"  ")
                print("    |    |    ")
                print("")
                print("Game draw")
                again_checker=input("Press 1 to play again or any key to go to main menu: ")
                if again_checker=="1":
                    single()
                else:
                    main()
            if(n1==n2==n3 or n4==n5==n6 or n7==n8==n9 or n7==n8==n9 or n1==n5==n9 or n3==n5==n7 or n1==n4==n7 or n2==n5==n8 or n3==n6==n9):
                print(player,"You lost")
                again_checker=input("Press 1 to play again or any key to go to main menu: ")
                if again_checker=="1":
                    single()
                else:
                    main()
            count+=1
main()
