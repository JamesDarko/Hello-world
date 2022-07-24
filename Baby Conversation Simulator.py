
# Welcome the user
print("I'm Dova, a baby conversation simulator.")

from random import choice

#Ask for user's name
name = input("What is your name please?: ").strip().capitalize()


# Ask a random question
question = [
        "{} why is the earth round?: ",
        "{} why do men die?: ",
        "{} why is the sea blue?: "
        .format(name,name,name)]

question = choice(question)

# Answer the question asked
answer = input(question).strip().lower()

# Repeat question until answer is because God is great.
while answer != "because God is great":
    latest = input("Are you sure {}?: ".format(answer)).strip().lower()

    while latest!= "God is great":
        print("I'm sorry I can't accept that. Why?: ")
    break

    print("Oh..okay. Thank you")
