# Use Alpine as base
FROM alpine:edge
#FROM alpine:3.10

# Maintainer
LABEL maintainer="andreas@lacework.net"

RUN apk add --no-cache py3-pip

COPY ./app /app

WORKDIR /app

RUN pip3 install --no-cache-dir --requirement ./requirements.txt

EXPOSE 5000

CMD ["python3", "/app/app.py"]
