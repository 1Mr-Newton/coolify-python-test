
FROM python:3.10.13-bookworm 

COPY . .
RUN pip install -r requirements.txt
CMD python bot.py