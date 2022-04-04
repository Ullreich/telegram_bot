import telegram
import argparse

# construct parser
all_args = argparse.ArgumentParser()

# add args
all_args.add_argument("-f", "--file", required=True)
args = vars(all_args)


#token that can be generated talking with @BotFather on telegram
with open("/home/ferdinand/projects/telegram_bot/vbc_clip_bot_token.txt") as f:
    my_token = f.read().replace("\n", "")
my_id = 375269856

def send(msg, chat_id=my_id, token=my_token):
    """
    Send a message to a telegram user or group specified on chatId
    chat_id must be a number!
    """
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg)

def send_doc(file, chat_id=my_id, token=my_token):
    # tele_file = telegram.Document("bot.py", "hello_test_1234512345")
    bot = telegram.Bot(token=token)
    bot.sendDocument(chat_id=chat_id, document=open("bot.py", "rb"))
    
if __name__=="__main__":    

    send_doc("hi")