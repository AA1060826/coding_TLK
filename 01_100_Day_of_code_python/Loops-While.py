while exit != "Yes":
    animal = input("Name an animal: ")
    if animal == "dog":
        print("woof")
    if animal == "cat":
        print("meow")
    if animal == "bird":
        print("tweet")
    else:
        print("Unavailable")
    exit = input("Do you want to exit? ")

