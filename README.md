# Input-Name-Greeting-Python-Script
A simple Python script that prompts the user to input their name and greets them accordingly.

The code infinitely loops until the user inputs something.


**User Input Prompt:**
The input() function is used to prompt the user to enter their name.

The message "Enter Your Name: " is displayed.


**Validation Loop:**
A while loop is initiated to ensure that the user provides a valid name. The loop continues as long as the length of the name variable is equal to 0, indicating that no name has been entered.

Within the loop, the user is prompted again with the message "No name entered, please enter your name: " until a non-empty name is provided.


**Greeting Message:**
Once a valid name is provided (i.e., the length of name is not zero), the loop exits, and a greeting message is printed using f-string formatting.
The message includes the user's name.


**Usage:**
-Run the script in a Python environment.

-Enter your name when prompted.

-If you fail to enter a name or provide an empty input, the script will prompt you to enter your name again until a valid name is provided.

-Once a valid name is provided, the script will greet you with a welcome message.

