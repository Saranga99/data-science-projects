FROM python:3.9-slim-buster

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./app.py /app/app.py

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]


# docker build -t testfrontend . 