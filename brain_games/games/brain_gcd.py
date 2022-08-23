from random import randint
import math
from brain_games.games.logic import start_game


def generate_question():
	num1 = randint(0,100)
	num2 = randint(0,100)
	question = f'{num1} {num2}'
	result = math.gcd(num1, num2)
	return [question, str(result)]


def brain_gcd():
	description = "Find the greatest common divisor of given numbers."
	start_game(description, generate_question)