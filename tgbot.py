import telebot


TOKEN = '6915685271:AAF9UF5__Z2Z2HgFDjQ2Tb73TYoRp2XAlTU'

OWNER_ID = '6368020335'

bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, """Привет! Ответь на вопросы, пожалуйста
1. Какая у тебя проблема?
2. Имя и свой кабинет? 

Hello! Answer the questions please
1. What is your problem?
2. Name and account? """)

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    bot.forward_message(OWNER_ID, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Спасибо за ваше сообщение! Мы скоро свяжемся с вами.")

if __name__ == "__main__":
    bot.polling(none_stop=True)
