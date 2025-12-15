FROM alpine

WORKDIR /app

RUN apk add --no-cache python3 py3-pip

COPY app.py /app/app.py

CMD ["python3", "app.py"]
