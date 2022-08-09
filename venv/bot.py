import telebot
import workouts
from config import TG_BOT_TOKEN

# creating Bot instance
gymbot = telebot.TeleBot(TG_BOT_TOKEN)

# handling start command
@gymbot.message_handler(commands=['start'])
def answer_start_command(message):
	gymbot.send_message(message.chat.id, f'Hello, *{message.from_user.first_name}*!\n'
												   f'Welcome to \n'
												   f'The Workout Program Generator-bot \n'
												   f'I can create a workout program for gym.\n'
									               f'', parse_mode='Markdown')
	markup = telebot.types.InlineKeyboardMarkup()
	markup_buttons = []
	for button_name in ['Glutes', 'ABS', 'Full Body', 'Arms', 'Legs', 'Delts', 'Chest', 'Back']:
		markup_buttons.append(telebot.types.InlineKeyboardButton(button_name, callback_data=button_name.lower()))
	markup.row(*markup_buttons[:len(markup_buttons)//2])
	markup.row(*markup_buttons[len(markup_buttons)//2:])
	gymbot.send_message(message.chat.id, '*Choose a body part you want to target*', parse_mode="Markdown", reply_markup=markup)

# handling help command
@gymbot.message_handler(commands=['help'])
def answer_help_command(message):
	gymbot.send_message(message.chat.id, 'Hello! \n'
									  'This bot generates exercise program for the gym! \n'
									  'Text /start to start and follow the steps!')


# variable for a part of the body
body_part = None


# handling markup answer (saving value to global variable body_part)
@gymbot.callback_query_handler(lambda call: True)
def handle_boby_part_markup(call):
	global body_part
	body_part = call.data.capitalize()
	gymbot.answer_callback_query(call.id)
	ask_number_of_exercises(call.message)


# asking user about the number of exercises
def ask_number_of_exercises(message):
	gymbot.send_message(chat_id=message.chat.id, text=f'Greate! You chose ---> *{body_part} !*', parse_mode="Markdown")
	gymbot.send_message(chat_id=message.chat.id, text='*Text the number of exercises you want to get*', parse_mode="Markdown")
	gymbot.register_next_step_handler(message, sent_workout_to_user)


# sending workout to the user
def sent_workout_to_user(message):
	try:
		number = message.text
		workout = workouts.generate_workout(body_part, number)
		for exercise in workout:
			gymbot.send_message(message.chat.id, text=exercise, parse_mode="Markdown")
	except:
		gymbot.send_message(message.chat.id, 'Bot expects only digits. Use digits, please	', parse_mode="Markdown")
		gymbot.register_next_step_handler(message, sent_workout_to_user)
	else:
		ask_user_to_continue(message)


# ask the user to generate one more program
def ask_user_to_continue(message):
	gymbot.send_message(message.chat.id,"Would you like generate one more program?\n"
										"Text *Yes/No*", parse_mode="Markdown")


# handling any users messages
@gymbot.message_handler(content_types=["text"])
def handle_user_messages(message):
	if message.text.capitalize() == 'Yes':
		answer_start_command(message)
	elif message.text.capitalize() == 'No':
		gymbot.send_message(message.chat.id, 'Bot stopped.\n'
											'text */start* command to restart', parse_mode="Markdown")
	else:
		gymbot.send_message(message.chat.id, 'Unexpected command. Please, use:\n'
										  '*/start* to start the bot again\n'
										  '*/help* to get help information', parse_mode="Markdown")


gymbot.polling(none_stop=True, interval=0)
