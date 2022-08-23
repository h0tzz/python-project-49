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


def get_correct_answer(new_question, rule_fn):
	return "yes" if rule_fn(new_question) else "no"


def play_game(user_name, generate_question, rule_fn, correct_answers_coount=0):
	if correct_answers_coount == MAX_ANSWERS_COUNT:
		print(f'Congratulations, {user_name}!')
		return
	new_question = generate_question()
	ask_question(new_question)
	user_answer = get_user_answer()
	correct_answer = get_correct_answer(new_question, rule_fn)
	is_ans_correct = correct_answer == user_answer
	if not is_ans_correct:
		print(f'''"{user_answer}" is wrong answer ;(. Correct answer was "{correct_answer}". Let's try again, {user_name}!''')
	else:
		print('Correct!')
		play_game(user_name, generate_question, rule_fn, correct_answers_coount + 1)


def start_game(description, generate_question, rule_fn):
	user_name = welcome_user()
	start_game_description(description)
	play_game(user_name, generate_question, rule_fn, 0)

