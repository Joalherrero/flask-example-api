FROM python:alpine3.11

COPY . /app
WORKDIR /app

RUN pip install -U Flask

EXPOSE 8080

ENTRYPOINT ["python"]
CMD ["app.py"]
