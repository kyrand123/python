# Knights to was "ni" video reference
# https://www.youtube.com/watch?v=zIV4poUZAQo

# python ChatBox.py

from random import randint   #import the random feature into Python

file = open("stop-words.txt") 
stopwords = file.readlines()



file2 = open("male-names.txt") #Open the selected file from the computer
malenames = file2.readlines() #read in all the data from the file

file3 = open("female-names.txt")
femalenames = file3.readlines()


while True:                                                     #Forever looping
    name = input("Hello, what is your name? ")                  #Ask for the user to type there name and store it in name
    print("That's a nice name " + name)                         #print a message and end with the data stored in the variable name
    age = input(name + " and how old are you? ")
    print("So you are " + age + " years old ")
    day = input(name + " Has your day been good or bad? ")
    if day == "good":                                               #if the requiered variable input is good then do this
        print("I am glad that you have had a nice day ")
        print("As you are in such a cheery mood we are going to play a game")
    if day == "bad":                                                        #if the variable is bad then do this
        print("I am sorry that you have had a bad day ")
        answer = input("To cheer up your day did you wanna play a game? ")
        if answer == "yes":
            print("I am glad you want to play a game, think of a random number between 1 and 10 ")
            print("Write yes if i guess correctly or no if I have not guessed it ")
            number = randint(1,10)                                              #create a random number for the game
            game = input("Okay is your number  " + str(number) + " ")           #stores the integer number as a string.
            if game == "no":
                print("Looks like I will never guess it then, oh well moving on ")
            if game == "yes":
                print("Yay it only took me my first attempt ")
        print("Hope that this has cheered you up ")
        print("Before I go we are going to play another game ")
    game2 = input("Would you like to play another game? ")
    if game2 == "yes":
        print("Okay, I know it sounds silly but I can predict the name of your future partner ")
        partner = input("Okay, would you like a husband or a wife? ")
        if partner == "husband":
            print("What we are going to do is you can give me a number and I will select the name from my memory of your perfect husband")
            chosenNum = input("Okay, give me a number between 0 and 3899, there is a lot of names ")
            print("Okay, your future husband will be called " + malenames[int(chosenNum)])          #get the selected number from the data file and show it, (meaning show data 4 if 4 is requested)
            print("What a great name!")
        if partner == "wife":
            print("What we are going to do is you can give me a number and I will select the name from my memory of your perfect wife")
            chosenNum1 = input("Okay, give me a number between 0 and 4953, there is a lot of names ")
            print("Okay, your future wife will be called " + femalenames[int(chosenNum1)])
            print("What a great name!")
    if game2 == "no":
        print("Take it you are not in the gaming mood then.")
    print(" ")                                                              #creates a blank space.
    print("I will now start all over again for your own amusment")
    print(" ")


        
        #for word in stopwords:
        #next = word.strip()
        #filtered = input.replace(next, " !!!!! ")
    
    
    
