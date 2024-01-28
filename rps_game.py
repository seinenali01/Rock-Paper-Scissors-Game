import random
def get_user_choice():
    while True:
        user_choice = input("Enter your choice(rock,paper,scissors) or 'q' to quit: ")
        if user_choice in ('rock','paper','scissors','q'):
            return user_choice
        else:
            print("Invalid choice.Please enter rock,paper,scisssors,or'q' to quit.")
def get_computer_choice():
    return random.choice(['rock','paper','scissors'])
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie!"
    elif(
        (user_choice == 'rock' and computer_choice == 'scissors')or
        (user_choice == 'paper' and computer_choice == 'rock')or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You Win!"
    else:
        return "Computer Wins!"
def play_game():
    user_points = 0
    computer_points = 0
    while True:
        user_choice = get_user_choice()
        if user_choice == 'q':
            break
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You Win!":
            user_points += 1
        elif result == "Computer Wins!":
            computer_points += 1
        print(f"Your Points:{user_points}\nComputer Points:{computer_points}")
        print()
    print("GAME OVER!")
    print(f"Your Total Points: {user_points}\nComputer Total Points: {computer_points}") 

    if user_points > computer_points:
         print("CONGRATULATIONS!You are the overall winner!")
    elif user_points < computer_points:
        print("SORRY!The computer is the overall win!")
    else:
        print("It's a Tie!No overall winner.")  

play_game()                        
                   