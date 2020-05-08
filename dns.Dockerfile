FROM python:3
RUN apt-get update

# DNS & dig command
RUN apt-get install bind9 --yes
RUN apt-get install dnsutils --yes
RUN pip install dnspython

# Comparator app
COPY comp.py /home

CMD service bind9 restart && python /home/comp.py && /bin/bash