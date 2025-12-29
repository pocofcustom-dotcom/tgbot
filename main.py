@bot.message_handler(content_types=['text', 'photo', 'video', 'document'])
def forward_to_channel(message):
    print("Получено сообщение от:", message.chat.id, message.chat.type)
    if message.chat.type == "private":
        bot.copy_message(
            chat_id=CHANNEL_ID,
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )
