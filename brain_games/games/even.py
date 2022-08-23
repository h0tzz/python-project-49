import random


RULE_TEXT = 'Answer "yes" if number even otherwise answer "no".'
ANSWER_PATTERN = 'yes|no'


def generate_round():
    number = random.randint(1, 100)
    result = 'yes' if number % 2 == 0 else 'no'
    question = str(number)
    return result, question
