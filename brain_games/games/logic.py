import prompt
from brain_games.cli import welcome_user


MAX_ANSWERS_COUNT = 3


def start_game_description(description):
	print(description)


def ask_question(question):
	print(f'Question: {question}')


def get_user_answer():
	answer = prompt.string(f'Your answer: ')
	return answer


def play_game(user_name, generate_question, correct_answers_coount=0):
	if correct_answers_coount == MAX_ANSWERS_COUNT:
		print(f'Congratulations, {user_name}!')
		return

	[question, correct_answer] = generate_question()

	ask_question(question)

	user_answer = get_user_answer()
	is_ans_correct = correct_answer = user_answer

	if not is_ans_correct:
		print(f'''"{user_answer}" is wrong answer ;(. Correct answer was "{correct_answer}". 
Let's try again, {user_name}!''')
	else:
		print('Correct!')
		play_game(user_name, generate_question, correct_answers_coount + 1)


def start_game(description, generate_question):
	user_name = welcome_user()
	start_game_description(description)
	play_game(user_name, generate_question, 0)

