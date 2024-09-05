FROM python:3.10.10-alpine

WORKDIR /workdir
COPY . /workdir

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888
EXPOSE 9999

CMD ["python3", "run.py"]