FROM python:latest

RUN pip3 install python-telegram-bot
RUN pip3 install python-binance
RUN pip3 install pandas-datareader
RUN pip3 install dateparser

COPY my_bot.py .
COPY ../keys.py .

CMD ["python", "my_bot.py"]
