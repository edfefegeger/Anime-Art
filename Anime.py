import configparser
from openai import OpenAI
import telebot

client = OpenAI()
config = configparser.ConfigParser()
config.read('congig.conf')
Telegram_bot_token = '8050648683:AAGEiCSQfE9f5CjhpryhIxcvTCbWIL-0jRk'

bot = telebot.TeleBot(Telegram_bot_token)

create_texts = {}

@bot.message_handler(commands=['create'])
def make(message):
    try:
        print("Dalle")

        command_text = message.text.replace('/create', '').strip()
        create_texts[message.chat.id] = command_text
        print(message.text)

        bot.send_message(message.chat.id, f"Thank you! You have such a awesome request! Now I’m gonna make a magic happen! ✨Your request: {message.text}")

        response = client.images.generate(
            model="dall-e-3",
            prompt=command_text + " cute anime girl chat room pictures ",
            size="1024x1024",
            quality="standard",
            n=1,
        )

        # Получаем URL сгенерированного изображения
        image_url = response.data[0].url
        print(image_url)

        try:
            # Отправляем изображение в ответ на исходное сообщение
            bot.send_photo(message.chat.id, image_url, reply_to_message_id=message.message_id)
            print("Изображение отправлено в чат")

        except Exception as e:
            print(f"Ошибка при отправке изображения {image_url}: {e}")
    except Exception as e:
        print(f"Ошибка {e}")

# Запускаем бота
bot.polling(none_stop=True, timeout=123)
