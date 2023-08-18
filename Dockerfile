FROM python:3.11-bullseye
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt /app/
COPY . /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
