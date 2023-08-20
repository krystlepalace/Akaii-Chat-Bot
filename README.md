# Akaii Telegram bot
 A simple yet moderator-bot for Telegram chats with speech recognition, can translate voice messages to text.


<a href="https://hub.docker.com/r/fubukedev/akaii-bot"><img src="https://img.shields.io/badge/Docker%20Hub-akaii--bot-blue"></a>  [<img src="https://img.shields.io/badge/Telegram-%40akaii__chat__bot-blue">](https://t.me/akaii_chat_bot) 

# Contents
 1. <a href="#install">Install</a>
  * <a href="#prequisites">Prequisites</a> 
  * <a href="#basic-startup">Basic startup</a>
  * <a href="#systemd">Systemd</a>
  * <a href="#docker--docker-compose">Docker + Docker Compose</a>
 2. <a href="#TODO">Todo</a>


## Install 

### Prequisites:
1. Python 3.11 or higher
2. Linux (if you want to run bot with systemd and have ffmpeg in your PATH)
3. Systemd (to run bot as service);
4. Docker (to build your own image with better vosk model or to run bot with docker compose).
5. Any vosk model you want (and you can get it here https://alphacephei.com/vosk/models)

### Basic startup
1. git clone https://github.com/krystlepalace/Akaii-Telegram-bot
2. cd Akaii-Tekegram-bot && python -m venv .venv
3. source .venv/bin/activate (or .venv/Scripts/activate on windows)
4. pip install -r requirements.txt
5. replace '.env.example' with just '.env' and fill all variables
6. put your vosk model folder in utils/neuro/vosk/ and rename model folder as 'model'
7. python main.py

### Systemd 
1. Make sure to complete steps 1-6 from basic startup
2. Replace 'akaii-bot.service.example' with just 'akaii-bot.service' and fill the WorkingDirectory and ExecStart variables
3. Copy 'akaii-bot.service' to '/etc/systemd/system/'
4. sudo systemctl enable akaii-bot.service and sudo systemctl start akaii-bot.service
5. Now service should work, you can check it by systemctl status akaii-bot.service

### Docker + Docker Compose
1. Replace 'docker-compose.example.yml' with just 'docker-compose.yml'
2. Edit '.env':
    * model path in docker container is '/app/utils/neuro/vosk/model'
    * media path is 'app/media/'
    * redis is just 'redis'
    * 'bot_token' is your bot's token
3. Run 'docker compose up -d'
4. Check container with docker compose ps

 * Also you may want to use stronger vosk models to get better speech recognition, so you will need to build new docker image.
 * To do this just download any vosk model you want and replace old model with it.
 * Before 'docker build' edit .env and fill variables like this:
```
MODEL_FULL_PATH='/app/utils/neuro/vosk/model'
MEDIA_FULL_PATH='/app/media/'
```
 * Then simply run docker build -t akaii-bot:1.0 .
 * And that's it, after build you can run bot in the container with command docker run akaii-bot


## TODO
1. Make /settings menu in full inline mode. Settings menu contains 3 keyboards: first lists all chat settings with clickable buttons, other two for toggling each settings.
2. Add middlewares
3. Make better filters
4. Any structure improvements from using patterns to re-arranging folders and files.
5. NSFW recognition with NudeNet
6. Make 3 docker image versions for each release with different models or make model folder customizable with docker compose
