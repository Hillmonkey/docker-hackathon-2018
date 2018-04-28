FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN apt-get -y update  && apt-get -y install python3-pip
RUN [ "pip", "install", "twilio==6.12.1" ]
WORKDIR /usr/src/app
COPY ./app .

CMD [ "python3", "./main.py" ]
