staff = ["James", "Samuel", "David", "Senyo", "Ben", "Gayel", "Grace", "Mimi", "Priscilla"]

while True:
    print("Hello! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()
    

    if name in staff:
        print("Hello {}, you're welcome".format(name))
        remove = input("Would you like to be removed from the system?(y/n): ").lower()

        if remove == "y":
            staff.remove(name)
            print("Successfully removed")
        elif remove == "n":
            print("No worries, I didn't want you to leave anyway!")

    else:
        print("Hello {}!, I don't think we've met yet.".format(name))
        add_me = input("Would you like to be added to the system?(y/n): ").strip().lower()

        if add_me == "y":
            staff.append(name)
            print("Successfully added to staff. Thank you")
        elif add_me == "n":
            print ("You can always join us.")

            
