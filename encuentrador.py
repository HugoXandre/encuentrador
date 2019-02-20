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
        text="Hola. Ya me he iniciado."
    )

def ayuda(bot, update):
    text = "Simplemente escribe /scifi o /fantasia para generar un encuentro de ese tipo."
    update.message.reply_text(text)

def scifi(bot, update):
    text = "Has seleccionado CIENCIA FICCIÓN"
    random.seed()
    update.message.reply_text(text)
    text = encuentros_scifi.encuentro_random
    update.message.reply_text(text)

def fantasia(bot, update):
        text = "Has seleccionado FANTASÍA"
        update.message.reply_text(text)
        numero = encuentros_fantasia.cuantos_encuentros
        numero = int(numero)
        #text = "De un total de", numero , "posibles encuentros, se ha seleccionado:"
        #update.message.reply_text(text)
        text = ""
        text = encuentros_fantasia.encuentro_random
        update.message.reply_text(text)






if __name__ == '__main__':
    main()
