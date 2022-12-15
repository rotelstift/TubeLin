FROM python:latest

RUN apt-get update
RUN apt-get install -y libffi-dev libnacl-dev python3-dev
RUN python3 -m pip install -U discord.py

WORKDIR /projects
