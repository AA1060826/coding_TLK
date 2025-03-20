counter = 0
while True:
    print("Never going to ___ you up")
    Answer = input(": ")
    if Answer != "give":
        print("Wrong, try again")
        counter += 1
    else:
        break
print("You got it wrong this many times:", counter)

