FROM python:3.10.9-slim-buster
WORKDIR /workspace
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python3","application.py"]