import prompt
from brain_games.cli import welcome_user
from random import randint

MAX_ANSWERS_COUNT = 3


def is_even(n):
    return n % 2 == 0


def start_game_description():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def ask_user(number):
    print(f'Question: {number}')


def get_user_answer():
    answer = prompt.string("Your answer: ")
    return answer


def get_correct_answer(question_number):
    return "yes" if is_even(question_number) else "no"


def play_game(user_name, correct_ans_count=0):
    if correct_ans_count == MAX_ANSWERS_COUNT:
        print(f'Congratulations, {user_name}!')
        return

    question_number = randint(0, 100)
    ask_user(question_number)
    user_answer = get_user_answer()
    correct_answer = get_correct_answer(question_number)
    is_ans_correct = correct_answer == user_answer

    if not is_ans_correct:
        print(f'''"{user_answer}" is wrong answer ;(. Correct answer was "{correct_answer}".
Let's try again, {user_name}!''')
    else:
        print('Correct!')
        play_game(user_name, correct_ans_count + 1)


def brain_even():
    user_name = welcome_user()
    start_game_description()
    play_game(user_name)
