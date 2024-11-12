FROM ubuntu
RUN apt update
RUN apt install python3 -y
RUN apt install python3-flask -y
COPY app.py /tmp
EXPOSE 80
CMD ["python3","/tmp/app.py"]
