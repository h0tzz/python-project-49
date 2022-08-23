from random import randint
from brain_games.games.logic import start_game


def is_even(n):
    return n % 2 == 0

def generate_question():
    num = randint(0,100)
    answer = "yes" if is_even(num) else "no"
    return [num, answer]


def brain_even():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    start_game(description, generate_question)
