import random

# Function that represents the Magic 8-Ball game: Provide it a name
# and question, then it will provide you an answer


def magic8ball(name="", question=""):
    # Initialized 'answer' variable to avoid potential reference errors
    answer = ""
    # Generate a random number between 0 and 8
    random_number = random.randint(0, 8)
    # print(random_number)

    # The various answers available by the Magic 8 Ball
    # in  a list that stores the possible answers
    # and can be accessed through the random number
    # generated as an index (more scalable solution compared to i)
    answers = ["Yes - definitely", "It is decidedly so", "Without a doubt",
               "Reply hazy, try again", "Ask again later",
               "Better not tell you now", "My sources say no",
               "Outlook not so good", "Very doubtful"]

    # Checks to see if the random number generated i valid
    if random_number < 0 or random_number > 8:
        print("Error: Unexpected random number")
    else:
        answer = answers[random_number]

    # Conditions for different scenerios
    if question == "":
        print("No question was provided")
    else:
        if name == "":
            print("Question: " + question)
            print("Magic 8-Ball's answer: " + answer)
        else:
            print("{} asks: {}".format(name, question))
            print("Magic 8-Ball's answer: " + answer)


# magic8ball("Barry", "Does Batman eat ice-cream?")
# magic8ball(question="Can I get pudding?")
# magic8ball(name="Damien")
# magic8ball("Damien")

name = input("What is your name? ")
question = input("What do you wish to ask? ")

magic8ball(name, question)
