import random
def q16_guessing_game():
    target = random.randint(1, 100) # [cite: 191]
    attempts = 7
    while attempts > 0:
        guess = int(input(f"Guess (Attempts left: {attempts}): "))
        if guess == target:
            print("Correct! You won."); return
        # Hints for High/Low [cite: 190]
        print("Too High" if guess > target else "Too Low")
        attempts -= 1
    print(f"Failed! The number was {target}.")