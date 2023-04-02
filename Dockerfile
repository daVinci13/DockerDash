FROM python:3.11.2-alpine

RUN apk update && apk add --no-cache gcc musl-dev linux-headers
RUN pip install --no-cache-dir flask docker solidicons

WORKDIR /app

COPY . /app

EXPOSE 5000

CMD ["python", "app.py"]

