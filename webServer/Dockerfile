FROM python:3.10

WORKDIR /webServer
COPY requirements.txt /webServer/requirements.txt

RUN pip install -r /webServer/requirements.txt

COPY . /webServer/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]