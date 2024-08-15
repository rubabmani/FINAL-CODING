import random

a=["rock", "scisoor", "paper"]
while True:
    Ccount=0
    Ucount=0
    uc=int(input("""
                 Game start....
                 press 1 for play Game
                 press 2 for exit
                 
                 """))
    if uc==1:
        for b in range (1,6):
        
            yourinput=int(input("""
                            1 for rock
                            2 for scisoor
                            3 for paper
                            
                            """))
            if yourinput==1:
                yourinput="rock"
            elif yourinput==2:
                yourinput="scissor"
            elif yourinput==3:
                yourinput="paper" 
            Cchoice=random.choice(a)
            if Cchoice==yourinput:
                print("computer choice is", Cchoice)
                print("your choice is", yourinput)
                print("round is draw")
                Ccount=Ccount+1
                Ucount=Ucount+1
            elif (yourinput=="rock" and Cchoice=="scisoor") or (yourinput=="paper" and Cchoice=="rock") or (yourinput=="scissor" and Cchoice=="paper"):
                print("computer choice is", Cchoice)
                print("your choice is", yourinput)
                print("you win this round")
                Ucount=Ucount+1
            else:
                print("computer choice is", Cchoice)
                print("your choice is", yourinput)
                print("computer win this round")
                Ccount=Ccount+1
            if Ccount==Ucount:
                print("computer points are", Ccount)
                print("your points are", Ucount)
                print("Game draw")
            elif Ccount>Ucount:
                print("computer points are", Ccount)
                print("your points are", Ucount)
                print("computer win the game")
            else:
                Ccount<Ucount
                print("computer points are", Ccount)
                print("your points are", Ucount)
                print("you win the game")
        else:
            break