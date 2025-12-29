import telebot

TOKEN = "8138229793:AAHcWYOug4sB621euJ6QymW-ygYMWQNaISg"
CHANNEL_ID = -1003607502652

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text', 'photo', 'video', 'document'])
def forward_to_channel(message):
    if message.chat.type == "private":
        bot.copy_message(
            chat_id=CHANNEL_ID,
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )

bot.polling(none_stop=True)