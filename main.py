import telebot
import os


TOKEN = os.getenv("BOT_TOKEN")

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

bot.infinity_polling()
