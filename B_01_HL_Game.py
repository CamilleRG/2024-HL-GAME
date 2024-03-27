# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes  / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instruction():
    print('''

   **** Instructions ****

   TO begin, decide on a score goal; (eg: The first one to get a 
   score of 50 wins).

   For each round of the game, you win points by rolling dice.
   The winner of the round is the one who gets 13 (or slightly less).

   If you win the round, then your score will increase by the 
   number of points that you earned. If your first roll of two 
   dice is a double (eg: both dice show a three). then your score 
   will be DOUBLE the number of points.

   If you lose the round, then you don't get any points.

   If you and the computer tie (eg: you both get a score of 11, 
   then you will have 11 points added to your score.

   Your goal is to try to get to the target score before the
   computer.

   Good luck.

    ''')


# Checks for an integer more than 0 (allows <enter>
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# Mian Routine Starts here

# Initialise game variables
mode = "regular"
rounds_played = 0

print("🔼🔼🔼 Welcome to the Higher Lower Game 🔻🔻🔻")
print()

want_instruction = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instruction == "yes":
    instruction()



# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds Heading
    if mode == "infinite":
        rounds_heading = f"\n♾♾♾ Round {rounds_played + 1} (Infinite Mode) ♾♾♾"

    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    # get user choice
    user_choice = input("Choose: ")

    # If user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

#  Game loop ends here

# Game History / Statistics area