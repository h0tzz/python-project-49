import random
import math


RULE_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'
ANSWER_PATTERN = 'yes|no'


def is_prime(number):
    if number == 2:
        return True
    divider = int(math.sqrt(number))
    divider_now = 2
    while divider_now <= divider:
        if number % divider_now == 0:
            return False
        divider_now += 1
    return True


def generate_round():
    number = random.randint(2, 300)
    result = 'yes' if is_prime(number) else 'no'
    question = str(number)
    return result, question
