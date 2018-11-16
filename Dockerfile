FROM python:3.6
ADD . /code
WORKDIR /code
RUN apt-get update -y
RUN pip install -r requirements.txt

RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf

CMD ["mysqld"]

CMD python main.py