FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip

RUN useradd -ms /bin/bash appuser

USER appuser

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR /app

COPY app/ .

EXPOSE 3000

CMD ["python3", "app.py"]
