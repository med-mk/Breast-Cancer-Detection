FROM python:3.6

COPY requirements.txt .

RUN pip install --upgrade -r requirements.txt

RUN apt-get update

RUN apt-get install ffmpeg libsm6 libxext6 libgl1 python3-opencv  -y

COPY server server/

EXPOSE 5000

CMD ["python", "server/main.py"]