# Use Alpine as base
FROM alpine:3.17
#FROM alpine:3.10

# Maintainer
LABEL maintainer="andreas@lacework.net"

RUN apk add --no-cache py3-pip

COPY ./app /app

WORKDIR /app

RUN pip3 install -r ./requirements.txt

EXPOSE 5000

CMD ["python3", "/app/app.py"]
