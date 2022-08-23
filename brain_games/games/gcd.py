import random


RULE_TEXT = 'Find the greatest common divisor of given numbers.'
ANSWER_PATTERN = '[-+]?\\d+'


def gcd(num1, num2):
    a = num1
    b = num2
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def generate_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    result = gcd(number1, number2)
    question = '{} {}'.format(number1, number2)
    return result, question
