import telebot
import random
import encuentros_scifi
import encuentros_fantasia
from telegram.ext import (Updater, CommandHandler)
from auth import token



def main():
    updater= Updater(token=token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ayuda", ayuda))
    dp.add_handler(CommandHandler("scifi", scifi))
    dp.add_handler(CommandHandler("fantasia", fantasia))
    updater.start_polling()
    updater.idle

def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Hola. Bien, Ya me he iniciado."
    )

def ayuda(bot, update):
    text = "Simplemente escribe /scifi o /fantasia para generar un encuentro de ese tipo."
    update.message.reply_text(text)

def scifi(bot, update):
    text = "Has seleccionado CIENCIA FICCIÓN"
    update.message.reply_text(text)
    text = random.choice(encuentros_scifi.lista)
    update.message.reply_text(text)


def fantasia(bot, update):
    text = "Has seleccionado FANTASÍA"
    update.message.reply_text(text)
    text = random.choice(encuentros_fantasia.lista)
    update.message.reply_text(text)


if __name__ == '__main__':
    main()
