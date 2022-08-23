import prompt
from random import randint
from brain_games.games_logic.helpers import start_game


MAX_ANSWERS_COUNT = 3

def rule_fn(n):
    return n % 2 == 0

def generate_question():
    return randint(0,100)

def brain_even():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    start_game(description, generate_question, rule_fn)
