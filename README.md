# **Rock-Paper-Scissors-Game**

## **Overview**
A `Rock, Paper, Scissors` Game where the computer's move is random, and points are awarded for each win. The user can choose to quit playing, and the total points are displayed at the end.

## **How to Run**

1. Save the provided Python script in a file with a `.py` extension, for example, `rps_game.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the Python script is saved using the `cd` command (Change Directory).
4. Run the script using the following command:
   ```bash
   python rps_game.py

 ## **Code Explanation**

1. **Import necessary library:**
   ```bash
   import random
   ```
    - This line imports the **`random`** module, which is used later to generate random choices for the computer player.

2. **Functions:**
   - **'get_user_choice:'**
     ```bash
     def get_user_choice():
         #...(function code)
     ```
     - This function prompts the user to input their choice, and it continues prompting until a valid choice is entered ('rock', 'paper', 'scissors', or 'q' to quit).
       
   - **'get_computer_choice:'**
      ```bash
     def get_computer_choice():
          #...(function code)
      ```
      - This function generates a random choice for the computer player from the list ['rock', 'paper', 'scissors'] using **`random.choice`**.
        
   - **'determine_winner:'**
      ```bash
      def determine_winner(user_choice, computer_choice):
          #...(function code)
      ```
      - This function compares the user's choice and the computer's choice to determine the winner based on the rock, paper, scissors rules.
        
   - **'play_game:'**
      ```bash
        def play_game():
          #...(function code)
      ```
      - This function initiates the game loop. It repeatedly gets the user's choice, generates the computer's choice, determines the winner, and updates the scores until the user decides to quit by entering 'q'. Finally, it displays the overall game results.

## **How the Game Works**
  - The user is prompted to enter their choice (rock, paper, scissors) or 'q to quit.
  - The computer generates a random choice.
  - The winner is determined based on the rules of rock, paper, scissors.
  - Points are updated, and the game continues until the user decides to quit.
  - The overall winner is declared at the end.

## **Output**
![rps_game](https://github.com/seinenali01/Rock-Paper-Scissors-Game/assets/157710508/3ae534e6-35cb-4416-9cf4-4e75227648c8)

            
