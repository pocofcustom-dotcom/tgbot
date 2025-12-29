import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text', 'photo', 'video', 'document'])
def forward_to_channel(message):
    user_info = f"{message.from_user.first_name} {message.from_user.last_name or ''} (@{message.from_user.username or 'no_username'})"
    print(f"Сообщение от: {user_info}, chat_id: {message.chat.id}, type: {message.chat.type}")

    if message.chat.type == "private":
        try:
            bot.copy_message(
                chat_id=CHANNEL_ID,
                from_chat_id=message.chat.id,
                message_id=message.message_id
            )
            print("Сообщение успешно отправлено в канал ✅")
        except Exception as e:
            print("Ошибка при отправке в канал:", e)

bot.infinity_polling()
