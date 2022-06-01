import random

options = ["R", "P", "S"]
option_name = {"R": "Rock", "P": "Paper", "S": "Scissors"}
rules = ["PR", "RS", "SP"]
in_game = True
def print_choices_and_winner(user_choice, cpu_choice):
    if (f"{user_choice}{cpu_choice}" in rules):
        print("Winner!")
    print(f"Player ({option_name[user_choice]}) : CPU ({option_name[cpu_choice]})")



while in_game:
    user_choice = input(f"Enter your choice ({options}): ")
    if (user_choice not in options):
        print("invalid choice")
        continue
    cpu_choice = random.choice(options);
    if cpu_choice is not user_choice:
        in_game = False
        print_choices_and_winner(user_choice, cpu_choice)
    else:
        print('tie!')

