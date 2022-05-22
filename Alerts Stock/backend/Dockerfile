FROM python:3.9-slim-buster

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ["__init__.py", "api_yahoo.py", "data.json","df_yahoo.csv", "patterns.py", "test_system.py", "test.py", "db.py", "/app/"]
COPY ./main.py /app/main.py

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]


# docker build -t testbackend . 