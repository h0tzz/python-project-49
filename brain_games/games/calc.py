import operator
import random


RULE_TEXT = 'What is the result of the expression?'
ANSWER_PATTERN = '[-+]?\\d+'
OPERATORS = ((operator.add, '+'),
             (operator.sub, '-'),
             (operator.mul, '*'))


def generate_round():
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    operator_type, operator_text = random.choice(OPERATORS)
    result = operator_type(number1, number2)
    question = '{} {} {}'.format(number1, operator_text, number2)
    return result, question
