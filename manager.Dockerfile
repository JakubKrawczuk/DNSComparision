FROM python:3
RUN apt-get update

COPY manager.py /home

CMD python /home/manager.py && /bin/bash