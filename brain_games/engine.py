import prompt
import re


NUMBER_OF_ROUNDS = 3


def play(game):
    """Launches a game, checks user`s answer and prints result.

    Arguments:
        game {module} -- the game module
    """

    print(f'Welcome to the Brain Games!\n{game.RULE_TEXT}\n')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!\n')

    for _ in range(NUMBER_OF_ROUNDS):

        result, question = game.generate_round()
        print('Question:', question)
        user_answer = prompt.string('Your answer: ').lower()

        while re.fullmatch(game.ANSWER_PATTERN, user_answer) is None:
            print('Answer is not correct!')
            user_answer = prompt.string('Your answer: ').lower()

        if str(result) != user_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{result}'."
            )
            print(f"Let's try again, {user_name}!")
            break

        print('Correct!')

    else:
        print(f'Congratulations, {user_name}!')
