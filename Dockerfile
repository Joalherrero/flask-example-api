FROM python:2.7

WORKDIR /app

EXPOSE 8080

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ADD models/* /app/models/
ADD resources/* /app/resources/


ADD app.py /app/app.py


CMD ["python", "app.py"]
