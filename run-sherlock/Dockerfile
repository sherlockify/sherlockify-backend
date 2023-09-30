FROM python:3

WORKDIR /app

COPY sherlock/requirements.txt ./sherlock_requirements.txt
RUN pip install -r sherlock_requirements.txt
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]