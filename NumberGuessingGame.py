import random
lowest_num, highest_num = 1, 10
print(f"Guess the number between {lowest_num} to {highest_num}")

num = random.randint(lowest_num, highest_num)
print(num)


while True:
    # Get the user guess
    try:
        user_guess: int = int(input('Guess: '))
    except ValueError:
        print('Please enter a valid number.')
        continue

    if user_guess > num:
        print("You need to guess lower number")
    elif user_guess < num:
        print("you need to guess higher number")
    elif user_guess == num:
        print("CORRECT !!!!!!!!!")
        break

