import telebot
import workouts
from config import TG_BOT_TOKEN


bot = telebot.TeleBot(TG_BOT_TOKEN)


def create_markup(*args):
	buttoms = []
	for buttom_name in args:
		buttoms.append(telebot.types.InlineKeyboardButton(buttom_name, callback_data=buttom_name.lower()))
	return buttoms


@bot.message_handler(commands=['start'])
def start_command(message):
	photo = open('FitGym.jpg', 'rb')
	bot.send_photo(message.chat.id, photo, caption=f'Hello, *{message.from_user.first_name}*!\n'
												   f'Welcome to \n'
												   f'The Workout Program Generator-bot \n'
												   f'I can create a workout program for gym.', parse_mode='Markdown')
	markup = telebot.types.InlineKeyboardMarkup()
	markup.row(*create_markup('Glutes', 'ABS', 'Full Body', 'Arms'))
	markup.row(*create_markup('Legs', 'Delts', 'Chest', 'Back'))
	bot.send_message(message.chat.id, '*Tap a body part you want to target*', parse_mode="Markdown", reply_markup=markup)


body_part = None


@bot.callback_query_handler(lambda call: True)
def handle(call):
	global body_part
	body_part = call.data.capitalize()
	bot.send_message(chat_id=call.message.chat.id, text=f'You\'ve choose ---> *{body_part} !*', parse_mode="Markdown")
	bot.send_message(chat_id=call.message.chat.id, text='*Text the number of exercises you want to get*', parse_mode="Markdown")
	bot.answer_callback_query(call.id)
	bot.register_next_step_handler(call.message, sent_workout)


def sent_workout(message):
	number = message.text
	workout = workouts.generate_workout(body_part, number)
	for exercise in workout:
		bot.send_message(message.chat.id, text=exercise, parse_mode="Markdown")


bot.polling(none_stop=True, interval=0)
