from random import randint
from brain_games.games.logic import start_game


def generate_question():
	result = 0
	symbols = ['+', '-', '*']
	num1 = randint(0,100)
	num2 = randint(0,100)
	rand_sym_number = randint(0,2)

	if rand_sym_number == '+':
		result = num1 + num2
	elif rand_sym_number == '-':
		result = num1 - num2
	else:
		result = num1 * num2
	
	question = f'{num1} {symbols[rand_sym_number]} {num2}'
	return [question, result]


def brain_calc():
    description = 'What is the result of the expression?'
    start_game(description, generate_question)
