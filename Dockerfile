FROM ubuntu

RUN apt update
RUN apt install nginx postgresql postgresql-contrib python-pip net-tools
RUN pip install requests maya clint
RUN service nginx start
RUN service postgresql start