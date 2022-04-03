import telegram


#token that can be generated talking with @BotFather on telegram
my_token = '5238357535:AAFShZRCdaIMttsBMPKw9DpmOdRTDaGL1zU'

def send(msg, chat_id, token=my_token):
    """
    Send a message to a telegram user or group specified on chatId
    chat_id must be a number!
    """
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg)
    
send("hi", 375269856)