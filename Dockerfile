FROM ubuntu

RUN apt update
RUN apt install python python3-pip -y

RUN pip3 install --upgrade pip
RUN pip3 install python-telegram-bot
RUN pip3 install python-binance
RUN pip3 install pandas-datareader
RUN pip3 install dateparser

COPY my_bot.py /opt/.
COPY keys.py /opt/.

CMD "python3 /opt/my_bot.py"
