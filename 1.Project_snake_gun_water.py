import random
computer = random.choice([-1,0,1])
dictionary ={"s":1,"w":-1,"g":0}
yourstring = input("Enter your choice s for snake w for water g for gun : ")
you = dictionary[yourstring]
if computer == -1 and you== -1:
    print(f"TIE as computer choose {computer} and you choose {you}")
elif computer == -1 and you== 0:
    print(f"Computer win as computer choose {computer} and you choose {you}")
elif computer == -1 and you== 1:
    print(f"you win as computer choose {computer} and you choose {you}")
elif computer == 0 and you== -1:
    print(f"you win as computer choose {computer} and you choose {you}")
elif computer == 0 and you== 0:
    print(f"TIE as computer choose {computer} and you choose {you}")
elif computer == 0 and you== 1:
    print(f"Computer win as computer choose {computer} and you choose {you}")
elif computer == 1 and you== -1:
    print(f"Computer win as computer choose {computer} and you choose {you}")
elif computer == 1 and you== 0:
    print(f"you win as computer choose {computer} and you choose {you}")
elif computer == 1 and you== 1:
    print(f"TIE as computer choose {computer} and you choose {you}")
else:
    print("ERROR")