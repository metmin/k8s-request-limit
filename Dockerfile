FROM python:3.9.6-alpine3.14

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY src/. .

CMD ["sleep", "12000"]