import random
user_score =0
computer_score = 0
a = ["rock","paper","scissor",]
b = random.choice(a)
while True:
    enter = str(input('''enter your choice "rock","paper","scissor"''')).lower()
    b = random.choice(a)
    print("computer CHoice",b)
    if enter  not in (a):
        print("Enter valid Option")
        continue
    elif ((b == "rock" and enter == "paper")or
          (b == "paper" and enter == "scissor")or
          (b == "scissor" and enter == "rock" )
         ):
        print("you win")
        user_score+=1
    elif enter==b:
        print("tie")
    else:
        print("you loss")
        computer_score+=1
        print(f"user_score={user_score} and computer_score={computer_score}")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break