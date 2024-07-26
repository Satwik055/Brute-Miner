FROM python:3.9

WORKDIR /app

COPY main.py .

COPY modules/ /app/modules/

COPY models/ /app/models/

COPY requirements.txt .

RUN pip install -r requirements.txt 

CMD ["python", "./main.py"]