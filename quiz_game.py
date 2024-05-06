print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")
print(playing)

if playing != "yes":
    quit()
    print("Okay! Let's play :)")

answer = input("What does CPU stands for? ")
if answer == "central processing unit":
    print('Correct!')
else:
    print("Incorrect!")


    answer = input("What does GPU stands for? ")
if answer == "graphics processing unit":
    print('Correct!')
else:
    print("Incorrect!")


    answer = input("What does RAM stands for? ")
if answer == "ramdom access memory":
    print('Correct!')
else:
    print("Incorrect!")


    answer = input("What does SQL stands for? ")
if answer == "structured query language":
    print('Correct!')
else:
    print("Incorrect!")