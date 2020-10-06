import random
print("Number guessing game")
number = random.randint(0, 99)
chances = 0
print("Guess a number (less than 99):")
while True:
	guess = int(input())
	if guess == number:
		print('CONGRATULATIONS! YOU HAVE GUESSED THE NUMBER '+str(number)+' IN '+str(chances)+' ATTEMPTS!')
		print("You Win!!!!!!")
		break 
	elif guess < number:
		print("Your guess was too low: Guess a number higher than", guess)
	else:
		print("Your guess was too high: Guess a number lower than", guess)
	chances += 1