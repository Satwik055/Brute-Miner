FROM python:3.9

WORKDIR /bruteit-miner

COPY app/ /bruteit-miner/app/

COPY database/ /bruteit-miner/database/

COPY model/ /bruteit-miner/model/

COPY script/ /bruteit-miner/script/

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./app/main.py"]