# WatchCoin
## Purpose
This project aim at monitoring which coins will be listed in a short period on big markets such as Binance - as first monitored one - allowing us
to buy them before their mainstream release and hopefully consequential growth.

The data scraping part will be initially based only on twitter posts, can't exclude more sources in future.
The notification part is delegated to a telegram bot working as information dispatcher.


## File Content

* twitter.py:\
Core of the twitter information-gathering bot.

* telegram.py:\
This is obviously the telegram bot core code.

* .env:\
Environment variable, keepin them safe and local:)



##### NOTE
* https://realpython.com/twitter-bot-python-tweepy/
* https://docs.tweepy.org/en/stable/api.html
* https://docs.aiogram.dev/en/latest/examples/index.html
