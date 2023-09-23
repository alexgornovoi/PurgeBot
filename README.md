# Incogbot

Incogbot is a discord bot made using [discord.py](https://discordpy.readthedocs.io/en/stable/) library. In order to avoid rate limits it is recommended that you create your own version of this bot.

## Creating The Application
1. Visit [Discord Developer Portal](https://discord.com/developers/applications) and create a new application.
2. Go to the "Bot" tab, reset your token and save the new token for later. Scroll down and enable "Message Content Intent".
3. Next go to the OAuth2 tab, click on URL Generator.
4. Select "bot" from scope and select the following permission.
    1. Manage Messages
    2. Read Message History
    3. Send Messages
5. Copy the generated link, paste it into your browser, and invite the bot to the correct server.

## Running The Bot Locally

1. Clone the project

```bash
  git clone https://github.com/alexgornovoi/incogbot
```

2. Go to the project directory

```bash
  cd incogbot
```

3. Install discord.py library and python-dotenv

```bash
  pip install -U discord.py
```
```bash
  pip install python-dotenv
```

4. Create a .env in the root of the directory. In this .env you will want the following lines.
```bash
token =  123456789
guildId = 123456789
```
Where token is the bot token you saved from before and guilId is the [Server ID](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-#:~:text=Obtaining%20Server%20IDs%20%2D%20Mobile%20App,ID%20to%20get%20the%20ID) where you added the bot.  
:warning: **Do not share your .env or any information inside it**: Be very careful here!

5. Next start the bot. To check that it is working you can do "/incogbot" to check if there bot has started.
```bash
  python3 incogbot.py
```
## Usage

:warning: While running the bot you will get warning messages when too many requests are made. This is expected and discord.py built features handle timing out the bot when it reaches discord api limit.
### /clear_all
This command will clear all messages in the channel it was sent in.
### /clear {days}
This command will clear all messages from before the inputted amount of days **for only the user that sent the command**.
### /clear_bot
This command will clear all of incogbot sent messages. (This is useful for cleaning channels where the bot may be used alot.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
