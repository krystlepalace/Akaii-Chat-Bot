# Akaii Telegram bot
 A simple yet moderator-bot for Telegram chats with speech recognition for translation voice messages to text.


<a href="https://hub.docker.com/r/fubukedev/akaii-bot"><img src="https://img.shields.io/badge/Docker%20Hub-akaii--bot-blue"></a>  [<img src="https://img.shields.io/badge/Telegram-%40AkaiiChatBot-blue">](https://t.me/akaii_chat_bot) 


## Install 

### Prequisites:
1. Python 3.11 or higher
2. Linux (if you want to run bot with systemd and have ffmpeg in your PATH)
3. Systemd (to run bot as service);
4. Docker (to build your own image with better vosk model or to run bot with docker compose).

### Basic startup
1. git clone https://github.com/krystlepalace/Akaii-Telegram-bot
2. cd Akaii-Tekegram-bot && python -m venv .venv
3. source .venv/bin/activate (or .venv/Scripts/activate on windows)
4. replace '.env.example' with just '.env' and fill all variables
5. python main.py

### Systemd 
1. Make sure to complete steps 1-4 from basic startup
2. Replace 'akaii-bot.service.example' with just 'akaii-bot.service' and will the WorkingDirectory and ExecStart variables
3. Copy 'akaii-bot.service' to '/etc/systemd/system/'
4. sudo systemctl enable akaii-bot.service and sudo systemctl start akaii-bot.service
5. Now service should work, you can check it by systemctl status akaii-bot.service

### Docker + Docker Compose
1. Replace 'docker-compose.example.yml' with just 'docker-compose.yml'
2. Run docker compose up -d
3. Check container with docker compose ps

