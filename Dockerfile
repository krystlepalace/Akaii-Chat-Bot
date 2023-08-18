FROM python:3.11-bullseye
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt /app/
COPY Akaii-Telegram-bot /app/bot
WORKDIR /app
RUN pip install --no-cache-dir --upgrade pip \
&& pip install --no-cache-dir -r requirements.txt
CMD ["python", "bot/main.py"]
