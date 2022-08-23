from random import randint
from brain_games.games.logic import start_game


def generate_question():
	result = 0
	symbols = ['+', '-', '*']
	num1 = randint(0,100)
	num2 = randint(0,100)
	rand_sym_number = randint(0,2)
	symbol = symbols[rand_sym_number] 
	if symbol == '+':
		result = num1 + num2
	elif symbol == '-':
		result = num1 - num2
	elif symbol == '*':
		result = num1 * num2
	
	question = f'{num1} {symbol} {num2}'
	return [question, str(result)]


def brain_calc():
    description = 'What is the result of the expression?'
    start_game(description, generate_question)
