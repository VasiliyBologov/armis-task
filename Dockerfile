FROM python:3.10.16-slim as armis

# OS dependencies
RUN apt-get update && apt install --no-install-recommends --no-install-suggests -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    gcc \
    supervisor

WORKDIR /app

COPY ./ ./

RUN pip3 install -r requirements.txt

COPY supervisord.conf /etc/supervisord.conf

EXPOSE 9300

CMD ["supervisord"]