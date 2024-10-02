from random import randint
player_one_name=input("hey player one what is your name ") 
print(player_one_name)
#player_one_class=input("chose your class")
    
player_two_name=input("what is your name player two ")
if player_two_name=="":
    player_two_name="cpu"
p1_life=10
p2_life=10
game=True
rounds=0
while game:
    rounds+=1 
    if rounds==1:
        print(str(rounds)+" round")
    else:
        print(str(rounds)+" rounds")
    p1_roll=randint(1,6)
    p2_roll=randint(1,6)
    #if player_one_class=="1":   
    print(p1_roll)
    print(p2_roll)
    if p1_roll>p2_roll:
        p2_life-=p1_roll-p2_roll
        print(player_one_name+" wins and dyyls "+str(p1_roll-p2_roll))
    elif p2_roll>p1_roll:
        p1_life-=p2_roll-p1_roll
        print(player_two_name+" wins and deels "+str(p2_roll-p1_roll))
    else:
        print("it is a draw")
    input("press enter to continue")
    if p1_life<=0:
        game=False
        print(player_one_name+" loses in "+str(rounds)+" rounds")
    elif p2_life<=0:
        game=False
        print(player_two_name+" loses in "+str(rounds)+" rounds")
