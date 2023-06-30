FROM ubuntu:latest
RUN apt update
RUN apt install python3-pip -y
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /home/app
COPY . /home/app
CMD ["python3","manage.py","runserver","0.0.0.0:8001"]
