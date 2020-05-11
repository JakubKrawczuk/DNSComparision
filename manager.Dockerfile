FROM python:3
RUN apt-get update

COPY manager_app/* /home/

WORKDIR /home
CMD python manager.py && /bin/bash