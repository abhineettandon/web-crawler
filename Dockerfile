FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN crawl4ai-setup

CMD [ "python", "app.py" ]