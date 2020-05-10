FROM python:3
RUN apt-get update

# DNS & dig command
RUN apt-get install bind9 --yes
RUN apt-get install dnsutils --yes
RUN pip install dnspython

# Comparator app
COPY comp.py /home
COPY dns_cfg/*db.dsk /etc/bind/
COPY dns_cfg/named.conf.local /etc/bind

#service bind9 restart && 
CMD python /home/comp.py && /bin/bash