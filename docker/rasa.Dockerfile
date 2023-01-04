FROM rasa/rasa:3.4.0-full

USER root
COPY ./src /app

USER 1001
