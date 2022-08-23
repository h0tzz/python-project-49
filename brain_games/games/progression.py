from random import randrange


RULE_TEXT = 'What number is missing in the progression?'
ANSWER_PATTERN = '\\d+'


def generate_round():
    step = randrange(2, 15, 1)
    element = randrange(1, 20, 1)
    progression_length = randrange(6, 12)
    progression = []
    for _ in range(progression_length):
        progression.append(element)
        element += step
    element_to_search = randrange(len(progression))
    result = progression[element_to_search]
    progression[element_to_search] = '..'
    question = ' '.join(map(str, progression))
    return result, question
