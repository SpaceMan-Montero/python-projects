import random

# Function that represents the Magic 8-Ball game: Provide it a name
# and question, then it will provide you an answer


def magic8ball(name="", question=""):
    # Initialized 'answer' variable to avoid potential reference errors
    answer = ""
    # Generate a random number between 1 and 9
    random_number = random.randint(1, 9)
    # print(random_number)

    # The various answers available by the Magic 8 Ball
    # in a if-elif-else control flow
    if random_number == 1:
        answer = "Yes - definitely"
    elif random_number == 2:
        answer = "It is decidedly so"
    elif random_number == 3:
        answer = "Without a doubt"
    elif random_number == 4:
        answer = "Reply hazy, try again"
    elif random_number == 5:
        answer = "Ask again later"
    elif random_number == 6:
        answer = "Better not tell you now"
    elif random_number == 7:
        answer = "My sources say no"
    elif random_number == 8:
        answer = "Outlook not so good"
    elif random_number == 9:
        answer = "Very doubtful"
    else:
        answer = "Error: Unexpected random number"

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
