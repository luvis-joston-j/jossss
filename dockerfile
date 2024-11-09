FROM ubuntu
RUN apt install python3 -y
RUN apt install python3-flask -y
COPY jos /tmp
EXPOSE 80
CMD ["pyrhon3","/tmp/jos"]
