# Clippy

Clippy is a Telegram bot that can send you your logfiles from a slurm script. 

## getting started
Text `@vbc_clip_bot` from your Telegram account so that the bot can send you files. Run `pip install python-telegram-bot` to install
the needed python package (you can install it in your `carla` conda env, there should be no conflicts). Before running a script, 
change the path for your `vbc_clip_bot_token.txt` to where you store the token (text me to get this token). Next you will need 
to find out your chatid. To do this run `get_chat_id.py` and text the bot `/start`. It should send you a integer. You will need
to replace `my_id` in `bot.py` with this integer.

## running `bot.py`
Add `bot.py` to the end of your slurm script. You will need to source and activate a conda environment with the telegram python
package in that script. `bot.py` accepts two keywords, `-f` or `--file` to specify the logfile to send you and `-m` or `--message` 
if you also want to send a message. For the time being you will need to call this file in a loop in your `.slrm` script if you
are running multiple jobs from one scipt (if there is demand i can add a feature so you dont need to loop).

## example
There is an example script, aptly named `example.slrm` for you to test if everything is working.
