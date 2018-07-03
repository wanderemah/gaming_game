import random


def guessing_game(lives=5):
    max_lives = lives
    print(
        f"\nODDS\nThe best guessing game available today.\nGuess the three digit magic number\nYou have {max_lives} chance(s). ")
    number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(number_list)
    magic_number = number_list[:3]
    # print(magic_number)
    while True:
        correct = 0
        present = []
        guesses = input(f"\nGuess the three digit number that has no repeated digit from 0 to 9:  ")

        if len(guesses) != 3:
            print("Only three digit numbers allowed")
            continue
        try:
            int(guesses)/2
            guess = list(guesses)
            lives -= 1
            print(f"{lives} chances left")

            if lives == 0:
                print(f"Sorry. Your chances are done\n{guesses} is the correct number")
                again = input("Wanna play again!!   ")
                if again == "yes":
                    guessing_game()
                else:
                    print("Thanks for playing")
                    break

            for index in range(3):
                if int(guess[index]) in magic_number:
                    print(f"{guess[index]} is present")
                    present.append(int(guess[index]))

            if len(present) == 0:
                print("Wrong. Try again")
                continue
            else:
                for num in present:
                    index_in_guess = guess.index(str(num))
                    index_in_magic_num = magic_number.index(num)
                    if index_in_guess == index_in_magic_num:
                        print(f"{num} is in the right position")
                        correct += 1
                    else:
                        print(f"{num} is in the wrong position")

            if correct == 3:
                print(f"{guesses} is the correct number")
                again = input("Wanna play again!!   ")
                if lives == (max_lives - 1):
                    max_lives += 1
                    print("You got it right in one shot. You've earned a bonus chance")
                if again == "yes":
                    guessing_game(max_lives)
                else:
                    print("Thanks for playing")
                    break
            else:
                continue

        except ValueError:
            print("Only three digit numbers allowed")
            continue


guessing_game()
