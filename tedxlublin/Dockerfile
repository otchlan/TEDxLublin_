# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /www

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
COPY ./requirements.txt /www/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /www/requirements.txt

# copy project
COPY . .

COPY ./entrypoint.sh /www/entrypoint.sh
RUN chmod +x /www/entrypoint.sh

RUN echo "Excute the entrypoint.sh script"
RUN echo "debug 123"
ENTRYPOINT ["bash", "/www/entrypoint.sh"]

EXPOSE 8000