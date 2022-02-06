print("Welcome to my Star Wars quiz")

playing = input("Let's play a game!, Would you like to play? ").lower()

if playing != "yes":
    quit()

print("Let us see if you are strong with the Dark Side!!")

score = 0

answer = input("Who gave the go ahead for Order 66? ")
if answer == "Emperor Palpatine" :
    print("You are strong with the Dark side!")
    score += 1
else:
    print("Seems like the light has called for you!")

answer = input(" Who is considered the strongest Sith Lord? ")
if answer == "Darth Vader" :
        print("You are strong with the Dark Side!")
        score += 1
else:
    print("Seems like the light has taken you!")

answer = input("Who was the most powerful sith in the Old Republic? ")
if answer == "Darth Revan" :
    print("You are strong with the Dark Side!")
    score += 1
else: 
    print(" Are you sure you are a Sith?")

answer = input("Who was the one that turned Anakin to the dark side ")
if answer == "Palpatine" :
    print("You are strong with the Dark Side!")
    score += 1
else: 
    print(" Are you sure you are a Sith?")

    answer = input("Who was Palpatines master? ").lower()
if answer == "Plagueis the Wise" :
    print("You are strong with the Dark Side!")
    score += 1
else: 
    print(" Are you sure you are a Sith?")

    answer = input("What is Emperor Palpatines sith name? ").lower()
if answer == "Darth Sidious" :
    print("You are strong with the Dark Side!")
    score += 1
else: 
    print(" Are you sure you are a Sith?")

    answer = input("Who was Darth revans right hand man?  ").lower()
if answer == "Darth Malak" :
    print("You are strong with the Dark Side!")
    score += 1
else: 
    print(" Are you sure you are a Sith?")

    answer = input("Who was Luke Skywalkers father?  ")
if answer == "Anakin Skywalker" :
    print("You are strong with the Dark Side!")
    score += 1
else: 
    print(" Are you sure you are a Sith?")

    answer = input("Who is Darth Vaders apprentice that eventually turned to the light?  ")
if answer == "Starkiller" :
    print("You are strong with the Dark Side!")
    score += 1
else: 
    print(" Are you sure you are a Sith?")

    answer = input("Who was the first sith lord?  ")
if answer == "Ajunta Pall" :
    print("You are strong with the Dark Side!")
    score += 1
else: 
    print(" Are you sure you are a Sith?")

print("Your connection to the Dark side" + str (score) + "You are strong with the Dark Side!")

