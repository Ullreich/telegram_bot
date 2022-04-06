from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import Updater
from os.path import exists

if exists("./vbc_clip_bot_token.txt"):
    with open("./vbc_clip_bot_token.txt") as f:
        my_token = f.read().replace("\n", "")
else:
    with open("/users/ferdinand.ullreich/scripts/telegram_bot/vbc_clip_bot_token.txt") as f:
        my_token = f.read().replace("\n", "")
        
updater = Updater(token=my_token, use_context=True)

def id(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(update.message.chat_id))
    
dispatcher = updater.dispatcher
start_handler = CommandHandler('id', id)
dispatcher.add_handler(start_handler)

updater.start_polling()