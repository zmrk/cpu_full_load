FROM       python:3

WORKDIR    /root

RUN        ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

COPY       *.py ./

CMD        ["sh", "-c", "python -u main.py"]
