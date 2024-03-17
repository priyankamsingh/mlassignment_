# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-slim

EXPOSE 5002

WORKDIR /app
COPY . /app

# Install pip requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

#running flask api in docker container

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
#CMD ["python", "app.py"]