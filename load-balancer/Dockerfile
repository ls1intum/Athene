FROM python:3.7.7
LABEL author="Jan Philip Bernius <janphilip.bernius@tum.de>"

COPY ./load-balancer/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -qr /tmp/requirements.txt

WORKDIR /usr/src/app
COPY ./load-balancer/src/ src/

# Run the image as a non-root user
RUN groupadd -r textbal && useradd --no-log-init -r -g textbal textbal
RUN mkdir -p /usr/src/app/logs/ && chown -R textbal:textbal /usr/src/app/
VOLUME ["/usr/src/app/logs"]
USER textbal

EXPOSE 8000
CMD uvicorn --host 0.0.0.0 --port 8000 --reload src.main:app
