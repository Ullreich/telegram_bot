import telegram
import argparse
from os.path import exists

# construct parser
parser = argparse.ArgumentParser()

# add args
parser.add_argument("-f", "--file", required=False)
parser.add_argument("-m", "--message", required=False)
args = parser.parse_args()


#token that can be generated talking with @BotFather on telegram
if exists("./vbc_clip_bot_token.txt"):
    with open("./vbc_clip_bot_token.txt") as f:
        my_token = f.read().replace("\n", "")
else:
    with open("/users/ferdinand.ullreich/scripts/telegram_bot/vbc_clip_bot_token.txt") as f:
        my_token = f.read().replace("\n", "")
my_id = 375269856

def send_msg(msg, chat_id=my_id, token=my_token):
    """
    Send a message to a telegram user or group specified on chatId
    chat_id must be a number!
    """
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg)

def send_doc(file=args.file, chat_id=my_id, token=my_token):
    bot = telegram.Bot(token=token)
    bot.sendDocument(chat_id=chat_id, document=open(file, "rb"))

if __name__=="__main__":    
    if args.message:
        send_msg()
        
    if args.file:
        send_doc()