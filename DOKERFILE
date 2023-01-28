FROM python:3.10.2
COPY requirements.txt /miso-back-sports/requirements.txt
WORKDIR /miso-back-sports
RUN pip install -r requirements.txt
COPY . /miso-back-sports/
ENTRYPOINT [“python”]
CMD [“run.py"]