FROM python:3.5-buster

ADD . .

# RUN export FLASK_APP=app.py
# ENV FLASK_APP app.py
RUN pip install -r requirements.txt

CMD FLASK_APP=app.py flask run --port 7777 --host=0.0.0.0
