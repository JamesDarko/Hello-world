print("Welcome to Magdar's Cinema")

movies ={
    "WAR ROOM":[12,2],
    "BLACK PANTHER":[18,5],
    "GOD'S NOT DEAD":[18,8],
    "FAITH":[16,3]
    }

while True:
    # Ask name for connection
    name = input("Your name would be nice:")
    
    # Accept response from user
    choice = input("Hello {},what movie would you like to watch today?: ".format(name)).strip().upper()

    if choice in movies:

    # Ask for age
        age = int(input("How old are you?: "))

    # Check age
        if age >= movies[choice][0]:

    # Check number of remaining seat for movie
            if movies[choice][1]>0:
                print("{} loading... Grab a seat and enjoy.".format(choice))

    # Update remaining number of seats for movie
                tickets_remaining = movies[choice][1]-1
                print("Remaining tickets",tickets_remaining)

    # Tell user tickets for movie is sold out
                if movies[choice][1] <=0:
                    print("Sorry, We've ran out of tickets for {}.".format(choice))
        else:
            print("I'm sorry, but you are too young to watch {}.".format(choice))
    else:
        print("{} currently unvailable...Please try another movie. Thank you".format(choice))
              
