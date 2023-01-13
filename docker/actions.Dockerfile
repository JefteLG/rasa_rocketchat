FROM rasa/rasa-sdk:3.4.0

USER root
COPY ./src/actions /app/actions
RUN pip install -r /app/actions/requirements.txt

USER 1001

# CMD ["python -m rasa_sdk -p 5055 --actions actions --debug"]