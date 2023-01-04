FROM rasa/rasa-sdk:3.4.0

USER root
COPY ./src/actions /app/actions

USER 1001

# CMD ["python -m rasa_sdk -p 5055 --actions actions --debug"]